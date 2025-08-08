"""Build stubs from skeleton files."""

from __future__ import annotations

import contextlib
import json
import subprocess
from concurrent.futures import Executor
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from dataclasses import field
from pathlib import Path
from typing import TYPE_CHECKING
from typing import ClassVar
from typing import override

from stubgen.command import CommandArguments
from stubgen.log import get_logger
from stubgen.model import CAssembly
from stubgen.model import CClass
from stubgen.model import CConstructor
from stubgen.model import CDelegate
from stubgen.model import CEnum
from stubgen.model import CEvent
from stubgen.model import CField
from stubgen.model import CMethod
from stubgen.model import CNamespace
from stubgen.model import CParameter
from stubgen.model import CProperty
from stubgen.model import CType
from stubgen.model import CTypeDefinition
from stubgen.model import DocNode
from stubgen.model import DocTree
from stubgen.util import merge_mapping

if TYPE_CHECKING:  # pragma: no cover
    from argparse import ArgumentParser

    # noinspection PyProtectedMember
    from argparse import _SubParsersAction
    from collections.abc import Mapping
    from collections.abc import Sequence
    from logging import Logger

    from stubgen.command import CommandResult

logger: Logger = get_logger(__name__)


@dataclass(frozen=True)
class Builder:
    """Class that builds the stub files for C# libraries."""

    ABC: ClassVar[str] = "abc.ABC"
    CALLABLE: ClassVar[str] = "collections.abc.Callable"
    CLASS_VAR: ClassVar[str] = "typing.ClassVar"
    ENUM: ClassVar[str] = "System.Enum"
    EVENT_TYPE: ClassVar[str] = "--[EVENT_TYPE]--"
    FINAL: ClassVar[str] = "typing.Final"
    OVERLOAD: ClassVar[str] = "typing.overload"
    SELF: ClassVar[str] = "typing.Self"

    line_length: int
    doc_tree: DocTree = field(default_factory=DocTree)
    import_set: set[str] = field(default_factory=set)

    def import_type(self, obj: CType) -> None:
        """Add a type to the import list."""
        if obj == CType.VOID or obj.generic or "." in obj.name:
            # VOID does NOT need to be imported.
            # No longer need to declare TypeVar.
            # Nested types have a "." in the name and do not need to be imported.
            return
        self.import_set.add(obj.import_name)
        inner: CType
        for inner in obj.inner:
            self.import_type(inner)

    def build_type(self, obj: CType, convert: bool = False) -> str:
        """Build a string representation for a CType."""
        logger.debug("Building type: %s", obj.unique_name)

        if obj == CType.VOID:
            return "None"

        type_str: str
        if convert and not obj.reference:
            # Don't convert if object is a reference because basic python objects are only by value
            type_map: Mapping[str, str] = {
                "Boolean": "bool",
                "SByte": "int",
                "Byte": "int",
                "Int16": "int",
                "UInt16": "int",
                "Int32": "int",
                "UInt32": "int",
                "Int64": "int",
                "UInt64": "int",
                "Single": "float",
                "Double": "float",
                "String": "str",
                "Object": "object",
                "Void": "None",
            }
            # char    System.Char
            # decimal System.Decimal
            # nint    System.IntPtr
            # nuint   System.UIntPtr

            try:
                type_str = type_map[obj.name]
            except KeyError:
                self.import_type(obj)
                type_str = obj.name
        else:
            self.import_type(obj)
            type_str = obj.name

        if len(obj.inner) > 0:
            children: list[str] = [self.build_type(t, convert=convert) for t in obj.inner]
            type_str = f"{type_str}[{', '.join(children)}]"

        if obj.nullable:
            type_str = f"{type_str} | None"
        return type_str

    def build_parameter(self, obj: CParameter) -> str:
        """Build a string representation for a CParameter."""
        logger.debug("Building parameter: %s", obj.unique_name)

        param_str: str = f"{obj.name}: {self.build_type(obj.type, convert=True)}"
        if obj.default:
            param_str = param_str + " = ..."
        return param_str

    def build_generic_params(self, *types: CType, declaring_type: CType | None = None) -> str:
        """Build a generic param declaration."""

        def extract_generic(type: CType) -> list[CType]:  # noqa: A002
            types: list[CType] = []
            if type.generic:
                types.append(type)
            types.extend(t for inner in type.inner for t in extract_generic(inner))
            return types

        generic_types: list[CType] = list(
            dict.fromkeys(extracted for t in types for extracted in extract_generic(t))
        )
        if declaring_type is not None:
            for t in extract_generic(declaring_type):
                with contextlib.suppress(ValueError):
                    generic_types.remove(t)
        generic_params: str = ""
        if len(generic_types) > 0:
            generic_params = f"[{', '.join(self.build_type(gt) for gt in generic_types)}]"
        return generic_params

    def build_field(self, obj: CField, indent: int = 0) -> Sequence[str]:
        """Build a list of strings to represent a CField."""
        logger.debug("Building field: %s", obj.unique_name)

        type_str: str = self.build_type(obj.return_type, convert=True)
        if obj.static:
            # This code is disabled as Final and ClassVar do not play nicely together
            # Final implies ClassVar
            self.import_set.add(self.CLASS_VAR)
            type_str = f"ClassVar[{type_str}]"
        else:
            self.import_set.add(self.FINAL)
            type_str = f"Final[{type_str}]"

        lines: list[str] = [f"{'    ' * indent}{obj.name}: {type_str}"]

        doc_node: DocNode = self.doc_tree[obj.unique_name]
        lines.extend(doc_node.doc_string(line_length=self.line_length, indent=indent))

        return lines

    def build_fields(self, obj: CClass, indent: int = 0) -> Sequence[str]:
        """Build the fields for a CClass."""
        lines: list[str] = []
        for _obj in obj.fields.values():
            lines.extend(self.build_field(_obj, indent=indent))
        return lines

    def build_constructor(
        self, obj: CConstructor, overload: bool, indent: int = 0
    ) -> Sequence[str]:
        """Build a list of strings to represent a CConstructor."""
        logger.debug("Building constructor: %s", obj.unique_name)

        lines: list[str] = []

        if overload:
            self.import_set.add(self.OVERLOAD)
            lines.append(f"{'    ' * indent}@overload")

        generic_params: str = self.build_generic_params(
            *(param.type for param in obj.parameters),
            declaring_type=obj.declaring_type,
        )

        parameters: Sequence[str] = [
            "self",
            *(self.build_parameter(p) for p in obj.parameters),
        ]
        lines.append(
            f"{'    ' * indent}def __init__{generic_params}({', '.join(parameters)}) -> None:"
        )

        doc_node: DocNode = self.doc_tree[obj.unique_name]
        lines.extend(doc_node.doc_string(line_length=self.line_length, indent=indent + 1))

        return lines

    def build_constructors(self, obj: CClass, indent: int = 0) -> Sequence[str]:
        """Build the constructors for a CClass."""
        lines: list[str] = []
        overload_c: bool = len(obj.constructors) > 1
        for _obj in obj.constructors.values():
            lines.extend(self.build_constructor(_obj, overload=overload_c, indent=indent))
        return lines

    def build_property(self, obj: CProperty, indent: int = 0) -> Sequence[str]:
        """Build a list of strings to represent a CProperty."""
        logger.debug("Building property: %s", obj.unique_name)

        indent_str: str = "    " * indent

        lines: list[str] = []
        self_cls: str = "self"
        if obj.static:
            self_cls = "cls"
            lines.append(f"{indent_str}@classmethod")

        lines.append(f"{indent_str}@property")

        property_type: str = self.build_type(obj.type, convert=True)
        lines.append(f"{indent_str}def {obj.name}({self_cls}) -> {property_type}:")

        doc_node: DocNode = self.doc_tree[obj.unique_name]
        lines.extend(doc_node.doc_string(line_length=self.line_length, indent=indent + 1))

        if obj.setter:
            if obj.static:
                lines.append(f"{indent_str}@classmethod")
            lines.extend(
                (
                    f"{indent_str}@{obj.name}.setter",
                    f"{indent_str}def {obj.name}({self_cls}, value: {property_type}) -> None: ...",
                )
            )

        return lines

    def build_properties(self, obj: CClass, indent: int = 0) -> Sequence[str]:
        """Build the properties for a CClass."""
        lines: list[str] = []
        for _obj in obj.properties.values():
            lines.extend(self.build_property(_obj, indent=indent))
        return lines

    def build_method(self, obj: CMethod, overload: bool, indent: int = 0) -> Sequence[str]:
        """Build a list of strings to represent a CMethod."""
        logger.debug("Building method: %s", obj.unique_name)

        lines: list[str] = []

        self_cls: str = "self"
        if obj.static:
            self_cls = "cls"
            lines.append(f"{'    ' * indent}@classmethod")

        if overload:
            self.import_set.add(self.OVERLOAD)
            lines.append(f"{'    ' * indent}@overload")

        generic_params: str = self.build_generic_params(
            *(param.type for param in obj.parameters),
            *obj.return_types,
            declaring_type=obj.declaring_type,
        )

        param_strs: Sequence[str] = [
            self_cls,
            *(self.build_parameter(p) for p in obj.parameters),
        ]

        return_str: str
        if len(obj.return_types) > 1:
            return_strs: list[str] = [self.build_type(t, convert=True) for t in obj.return_types]
            return_str = f"tuple[{', '.join(return_strs)}]"
        else:
            return_str = self.build_type(obj.return_types[0], convert=True)

        lines.append(
            f"{'    ' * indent}def {obj.name}{generic_params}"
            f"({', '.join(param_strs)}) -> {return_str}:"
        )

        doc_node: DocNode = self.doc_tree[obj.unique_name]
        lines.extend(doc_node.doc_string(line_length=self.line_length, indent=indent + 1))

        return lines

    def build_methods(self, obj: CClass, indent: int = 0) -> Sequence[str]:
        """Build the methods for a CClass."""
        lines: list[str] = []
        method_names: Sequence[str] = [m.name for m in obj.methods.values()]
        for _obj in obj.methods.values():
            overload_m: bool = len([m for m in method_names if m == _obj.name]) > 1
            lines.extend(self.build_method(_obj, overload=overload_m, indent=indent))
        return lines

    def build_event(self, obj: CEvent, indent: int = 0) -> Sequence[str]:
        """Build a list of strings to represent a CEvent."""
        logger.debug("Building event: %s", obj.unique_name)

        indent_str: str = "    " * indent

        self.import_set.add(self.EVENT_TYPE)
        self.import_set.add(self.SELF)

        lines: list[str] = [
            f"{indent_str}{obj.name}: EventType[{self.build_type(obj.type, convert=True)}] = ..."
        ]

        doc_node: DocNode = self.doc_tree[obj.unique_name]
        lines.extend(doc_node.doc_string(line_length=self.line_length, indent=indent))

        return lines

    def build_events(self, obj: CClass, indent: int = 0) -> Sequence[str]:
        """Build the events for a CClass."""
        lines: list[str] = []
        for _obj in obj.events.values():
            lines.extend(self.build_event(_obj, indent=indent))
        return lines

    def build_nested_types(self, obj: CClass, indent: int = 0) -> Sequence[str]:
        """Build the nested types for a CClass."""
        lines: list[str] = []
        for _obj in obj.nested_types.values():
            lines.extend(self.build_type_def(_obj, indent=indent))
        return lines

    def build_type_def(self, obj: CTypeDefinition, indent: int = 0) -> Sequence[str]:
        """Build a list of strings to represent a CTypeDefinition python stub."""
        match obj:
            case CClass():
                return self.build_class(obj, indent=indent)
            case CEnum():
                return self.build_enum(obj, indent=indent)
            case CDelegate():
                return self.build_delegate(obj, indent=indent)
        raise NotImplementedError  # pragma: no cover

    def build_class(self, obj: CClass, indent: int = 0) -> Sequence[str]:
        """Build a list of strings to represent a CClass python stub."""
        logger.debug("Building class: %s", obj.unique_name)

        parents: list[str] = []
        if obj.abstract:
            self.import_set.add(self.ABC)
            parents.append("ABC")
        if obj.super_class is not None:
            parents.append(self.build_type(obj.super_class))
        parents.extend(self.build_type(_obj) for _obj in obj.interfaces)

        generic_arg_str: str = ""
        if len(obj.generic_args) > 0:
            generic_arg_str = f"[{', '.join(self.build_type(_obj) for _obj in obj.generic_args)}]"

        parent_str: str = f"({', '.join(parents)})" if len(parents) > 0 else ""

        lines: list[str] = [f"{'    ' * indent}class {obj.name}{generic_arg_str}{parent_str}:"]

        doc_node: DocNode = self.doc_tree[obj.unique_name]
        lines.extend(doc_node.doc_string(line_length=self.line_length, indent=indent + 1))

        lines.extend(self.build_fields(obj, indent=indent + 1))
        lines.extend(self.build_constructors(obj, indent=indent + 1))
        lines.extend(self.build_properties(obj, indent=indent + 1))
        lines.extend(self.build_methods(obj, indent=indent + 1))
        lines.extend(self.build_events(obj, indent=indent + 1))
        lines.extend(self.build_nested_types(obj, indent=indent + 1))

        return lines

    def build_enum(self, obj: CEnum, indent: int = 0) -> Sequence[str]:
        """Build a list of strings to represent a CEnum python stub."""
        logger.debug("Building enum: %s", obj.unique_name)

        self.import_set.add(self.ENUM)

        lines: list[str] = [f"{'    ' * indent}class {obj.name}(Enum):"]

        doc_node: DocNode = self.doc_tree[obj.unique_name]
        lines.extend(doc_node.doc_string(line_length=self.line_length, indent=indent + 1))

        for field_obj in obj.fields:
            lines.append(f"{'    ' * (indent + 1)}{field_obj}: {obj.name} = ...")

            doc_node: DocNode = self.doc_tree[f"{obj.namespace}.{obj.name}.{field_obj}"]
            lines.extend(doc_node.doc_string(line_length=self.line_length, indent=indent + 1))

        return lines

    def build_delegate(self, obj: CDelegate, indent: int = 0) -> Sequence[str]:
        """Build a list of strings to represent a CDelegate python stub."""
        logger.debug("Building delegate: %s", obj.unique_name)

        self.import_set.add(self.CALLABLE)

        generic_params: str = self.build_generic_params(
            *(param.type for param in obj.parameters),
            obj.return_type,
        )

        parameters: Sequence[str] = [self.build_type(p.type, convert=True) for p in obj.parameters]

        return_str: str = self.build_type(obj.return_type, convert=True)

        lines: list[str] = [
            f"{'    ' * indent}type {obj.name}{generic_params} = "
            f"Callable[[{', '.join(parameters)}], {return_str}]",
        ]

        doc_node: DocNode = self.doc_tree[obj.unique_name]
        lines.extend(doc_node.doc_string(line_length=self.line_length, indent=indent))

        return lines

    def build_import_set(self, namespace: str) -> Sequence[str]:
        """Build a list of strings to represent the imports for this namespace."""
        lines: list[str] = []

        import_event_type: bool = False

        import_name: str
        for import_name in sorted(self.import_set):
            if import_name == self.EVENT_TYPE:
                import_event_type = True
                continue

            split: Sequence[str] = import_name.split(".")
            namespace_name: str = ".".join(split[:-1])
            if namespace == namespace_name:
                continue
            lines.append(f"from {namespace_name} import {split[-1]}")

        if import_event_type:
            lines.append("class EventType[T]:")
            lines.append("    def __iadd__(self, other: T) -> Self: ...")
            lines.append("    def __isub__(self, other: T) -> Self: ...")

        return lines

    def build(self, obj: CNamespace) -> Sequence[str]:
        """Build a list of strings to represent a python stub."""
        self.import_set.clear()

        built_type_lines: list[str] = []
        for _, type_def in sorted(obj.types.items()):
            built_type_lines.extend(self.build_type_def(type_def, indent=0))

        lines: list[str] = [
            f'"""Automatically generated stubs for C# namespace: {obj.name}."""',
            "",
        ]
        lines.extend(self.build_import_set(obj.name))
        lines.extend(built_type_lines)
        return lines


def build_stubs(
    builder: Builder,
    namespaces: Sequence[CNamespace],
    output_dir: Path,
    threads: int,
) -> None:
    """Build stub files for the provided namespaces."""
    logger.info("Building stub files.")

    def build_stub(
        namespace: CNamespace,
        builder: Builder = builder,
        output_dir: Path = output_dir,
    ) -> None:
        logger.info("Building namespace: %s", namespace.name)

        namespace_dir: Path = output_dir
        namespace_file: Path = Path()
        for name in namespace.name.split("."):
            dir_name: str = f"{name}-stubs" if namespace_dir is output_dir else name
            namespace_dir = namespace_dir / dir_name
            namespace_dir.mkdir(parents=True, exist_ok=True)

            namespace_file = namespace_dir / "__init__.pyi"
            namespace_file.touch(exist_ok=True)

        lines: Sequence[str] = builder.build(namespace)

        logger.info("Writing file: %r", str(namespace_file))
        namespace_file.write_text("\n".join(lines))

    if threads > 1:
        executor: Executor
        with ThreadPoolExecutor(max_workers=threads, thread_name_prefix="Worker") as executor:
            executor.map(build_stub, namespaces)
    else:
        for namespace in namespaces:
            build_stub(namespace)


def format_stubs(args: BuildArguments) -> None:
    """Format stub files for the provided namespaces."""
    logger.info("Formatting stub files.")

    from ruff.__main__ import find_ruff_bin

    process = subprocess.run(
        [
            find_ruff_bin(),
            "check",
            "--verbose",
            "--fix",
            "--target-version",
            "py313",
            "--line-length",
            str(args.line_length),
        ],
        capture_output=True,
        cwd=args.output_dir,
        text=True,
    )
    if process.stdout:
        logger.info(process.stdout)
    if process.stderr:
        logger.error(process.stderr)

    process = subprocess.run(
        [
            find_ruff_bin(),
            "format",
            "--verbose",
            "--target-version",
            "py313",
            "--line-length",
            str(args.line_length),
        ],
        capture_output=True,
        cwd=args.output_dir,
        text=True,
    )
    if process.stdout:
        logger.info(process.stdout)
    if process.stderr:
        logger.error(process.stderr)


@dataclass(frozen=True, kw_only=True)
class BuildArguments(CommandArguments):
    """Arguments to run the 'build' command."""

    command: str = "build"

    line_length: int = 100
    format_files: bool = False

    skeletons: str
    docs: str

    @classmethod
    @override
    def populate_parser(cls, sub_parser: _SubParsersAction[ArgumentParser]) -> None:
        build_command = sub_parser.add_parser("build", help="build stub file tree")

        build_command.add_argument(
            "-l",
            "--line-length",
            type=int,
            default=100,
            help="max length for a line in characters",
            dest="line_length",
        )
        build_command.add_argument(
            "-f",
            "--format-files",
            action="store_true",
            help="format generated stub files",
            dest="format_files",
        )

        build_command.add_argument(
            "skeletons",
            help="glob to the skeleton files",
        )
        build_command.add_argument(
            "docs",
            help="glob to the doc_tree files",
        )


def command_build(args: BuildArguments) -> CommandResult:
    """Run the 'build' command."""
    logger.debug("Arguments: %s", args)

    doc_tree: DocTree = DocTree()
    for doc_tree_file in Path().glob(args.docs):
        logger.info("Loading DocTree File: '%s'", doc_tree_file)
        new_doc_tree: DocTree = DocTree.from_json(json.loads(doc_tree_file.read_text()))
        doc_tree = DocTree.merge(doc_tree, new_doc_tree)

    builder: Builder = Builder(line_length=args.line_length, doc_tree=doc_tree)

    namespaces: Mapping[str, CNamespace] = {}
    for skeleton_file in Path().glob(args.skeletons):
        logger.info("Loading skeletons file: '%s'", skeleton_file)
        skeleton: CAssembly = CAssembly.from_json(json.loads(skeleton_file.read_text()))
        namespaces = merge_mapping(namespaces, skeleton.namespaces, CNamespace.merge)

    build_stubs(
        builder,
        list(namespaces.values()),
        args.output_dir,
        args.threads,
    )

    if args.format_files:
        format_stubs(args)

    return 0
