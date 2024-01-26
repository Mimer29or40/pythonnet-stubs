from __future__ import annotations

import json
from dataclasses import dataclass
from dataclasses import field
from pathlib import Path
from typing import Any
from typing import Dict
from typing import Final
from typing import List
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Set
from typing import Union
from typing import cast

import black
from black import Mode
from black import TargetVersion

from stubgen.log import get_logger
from stubgen.model import CClass
from stubgen.model import CConstructor
from stubgen.model import CDelegate
from stubgen.model import CEnum
from stubgen.model import CEvent
from stubgen.model import CField
from stubgen.model import CInterface
from stubgen.model import CMethod
from stubgen.model import CNamespace
from stubgen.model import CProperty
from stubgen.model import CStruct
from stubgen.model import CType
from stubgen.model import CTypeDefinition
from stubgen.util import rm_tree

logger = get_logger(__name__)


@dataclass
class Imports:
    py: Final[Set[str]] = field(default_factory=set)
    c: Final[Set[str]] = field(default_factory=set)
    type_vars: Final[Set[str]] = field(default_factory=set)
    include_event_type: bool = False

    def add_py_type(self, type: str) -> None:
        self.py.add(type)

    def add_c_type(self, type: CType) -> None:
        if type.generic:
            self.py.add("typing.TypeVar")
            self.type_vars.add(type.name)
        else:
            self.c.add(type.import_name)
        for inner_type in type.inner:
            self.add_c_type(inner_type)

    def build(self, namespace: str = None) -> Sequence[str]:
        if self.include_event_type:
            self.py.add("typing.Generic")
            self.type_vars.add("T")

        lines: List[str] = []

        for py_type in sorted(self.py):
            split: Sequence[str] = py_type.split(".")
            namespace_name: str = ".".join(split[:-1])
            name: str = split[-1]
            lines.append(f"from {namespace_name} import {name}")

        for c_type in sorted(self.c):
            split: Sequence[str] = c_type.split(".")
            namespace_name: str = ".".join(split[:-1])
            name: str = split[-1]
            if namespace is not None and namespace == namespace_name:
                continue
            lines.append(f"from {namespace_name} import {name}")

        lines.extend(f'{t} = TypeVar("{t}")' for t in sorted(self.type_vars))

        if self.include_event_type:
            lines.append("class EventType(Generic[T]):")
            lines.append("    def __iadd__(self, other: T): ...")
            lines.append("    def __isub__(self, other: T): ...")

        return tuple(lines)


def merge_namespace(namespace1: CNamespace, namespace2: CNamespace) -> CNamespace:
    if namespace1.name != namespace2.name:
        raise NameError(f"Namespace name mismatch: {namespace1.name} != {namespace2.name}")

    type_list: Set[str] = set(namespace1.types.keys())
    type_list.update(namespace2.types.keys())

    type_map: Dict[str, CTypeDefinition] = {}
    for type_str in sorted(type_list):
        if type_str in namespace1.types:
            type_def: CTypeDefinition = namespace1.types[type_str]
            if type_str in namespace2.types:
                logger.warning("Duplicate type in namespace %r: %r", namespace1.name, str(type_def))
            type_map[type_str] = type_def
        elif type_str in namespace2.types:
            type_def: CTypeDefinition = namespace2.types[type_str]
            type_map[type_str] = type_def

    return CNamespace(name=namespace1.name, types=type_map)


class Doc:
    data: Mapping[str, Any]

    def __init__(self, data: Mapping[str, Any]):
        self.data = data

    def get(self, node_str: str) -> Optional[Doc]:
        search: str
        doc_dict: Mapping[str, Any] = self.data
        while True:
            if node_str in doc_dict:
                return Doc(doc_dict[node_str])
            if "." in node_str:
                search, node_str = node_str.split(".", 1)
            else:
                search = node_str
            if search not in doc_dict:
                return None
            doc_dict = doc_dict[search]

    def doc_string(self, indent: int = 0, line_length: int = 100) -> Sequence[str]:
        indent_str: str = "    " * indent

        doc: Optional[str] = self.data.get("doc", None)
        doc_formatted: Mapping[str, Sequence[str]] = self.data.get("doc_formatted", {})
        parameters: Mapping[str, str] = self.data.get("parameters", {})
        return_str: Optional[str] = self.data.get("return", None)
        exceptions: Mapping[str, str] = self.data.get("exceptions", {})

        if len(parameters) == 0 and return_str is None and len(exceptions) == 0:
            if doc is None:
                return (f'{indent_str}""""""',)
            if "\n" not in doc and 4 * indent + len(doc) + 3 <= line_length:
                return (f'{indent_str}"""{doc}"""',)

        doc = '"""' + doc.replace("\n", "\n\n")
        doc_lines: List[str] = list(self.split(doc, indent, line_length))

        if len(parameters) > 0 or return_str is not None or len(exceptions) > 0:
            doc_lines.append(indent_str)

            for param, param_doc in parameters.items():
                param_str: str = f":param {param}: {param_doc}"
                doc_lines.extend(self.split(param_str, indent, line_length, "  "))

            if return_str is not None:
                doc_lines.extend(self.split(f":return: {return_str}", indent, line_length, "  "))

            for exception, exception_doc in exceptions.items():
                param_str: str = f":except {exception}: {exception_doc}"
                doc_lines.extend(self.split(param_str, indent, line_length, "  "))

        line_index: int = 0
        while line_index < len(doc_lines):
            line: str = doc_lines[line_index]
            for replace_str, replace_seq in doc_formatted.items():
                replace_str = f"%{replace_str}%"
                if replace_str in line:
                    doc_lines[line_index] = line.replace(replace_str, replace_seq[0])
                    for new_line in reversed(replace_seq[1:]):
                        doc_lines.insert(line_index + 1, indent_str + new_line)
            line_index += 1

        doc_lines.append(indent_str + '"""')
        return tuple(doc_lines)

    @staticmethod
    def split(
        text: str, indent: int = 0, line_length: int = 100, prefix: str = ""
    ) -> Sequence[str]:
        indent_str: str = "    " * indent

        lines: List[str] = []
        for doc_paragraph in text.splitlines():
            words: List[str] = doc_paragraph.split(" ")
            doc_line: str = indent_str + words[0]
            for word in words[1:]:
                if len(doc_line) + len(word) + 1 > line_length:
                    lines.append(doc_line)
                    doc_line = indent_str + prefix + word
                else:
                    doc_line += " " + word
            lines.append(doc_line)
        return lines


def merge_doc(self, other: Doc) -> Doc:
    return Doc(merge_doc_node(self.data, other.data))


def merge_doc_node(d1: Mapping[str, Any], d2: Mapping[str, Any]) -> Mapping[str, Any]:
    new_dict: Dict[str, Any] = dict(**d1)

    for k2, v2 in d2.items():
        if k2 not in new_dict:
            new_dict[k2] = v2
            continue

        v1: Any = new_dict[k2]
        if k2 in ("doc", "return"):
            new_dict[k2] = (v1 + "\n" + v2) if v1 != "" and v2 != "" else (v1 + v2)
        elif k2 == "doc_formatted":
            new: Dict[str, Sequence[str]] = dict(**v1)
            for k, v in v2.items():
                if k in new:
                    new[k] += v
                else:
                    new[k] = v
            new_dict[k2] = new
        elif k2 in ("parameters", "exceptions"):
            new: Dict[str, str] = dict(**v1)
            for k, v in v2.items():
                if k in new:
                    new[k] = (new[k] + "\n" + v) if new[k] != "" and v != "" else (new[k] + v)
                else:
                    new[k] = v
            new_dict[k2] = new
        else:
            new_dict[k2] = merge_doc_node(v1, v2)
    return new_dict


type_conversion: Final[Mapping[str, str]] = {}


def convert_type(type: CType) -> str:
    if len(type.inner) > 0:
        return type.simple_name

    return ""


# TODO - Nested types break doc tree
# TODO - Replace c types with python types, i.e. Int32 -> int, String -> str, Void -> None, etc
def build_type_def(
    type_def: CTypeDefinition,
    imports: Imports,
    doc: Doc,
    indent: int = 0,
    line_length: int = 100,
) -> Sequence[str]:
    type_name: str = type_def.__class__.__name__
    if type_name == "CClass":
        return build_class(cast(CClass, type_def), imports, doc, indent, line_length)
    if type_name == "CStruct":
        return build_struct(cast(CStruct, type_def), imports, doc, indent, line_length)
    if type_name == "CInterface":
        return build_interface(cast(CInterface, type_def), imports, doc, indent, line_length)
    if type_name == "CEnum":
        return build_enum(cast(CEnum, type_def), imports, doc, indent, line_length)
    if type_name == "CDelegate":
        return build_delegate(cast(CDelegate, type_def), imports, doc, indent, line_length)


def build_class(
    type_def: CClass,
    imports: Imports,
    doc: Doc,
    indent: int = 0,
    line_length: int = 100,
) -> Sequence[str]:
    parents: List[str] = []
    if type_def.abstract:
        imports.add_py_type("abc.ABC")
        parents.append("ABC")

    if len(type_def.generic_args) > 0:
        imports.add_py_type("typing.Generic")
        args: List[str] = []
        for arg in type_def.generic_args:
            imports.add_c_type(arg)
            args.append(arg.name)
        parents.append(f"Generic[{', '.join(args)}]")

    if type_def.super_class is not None:
        imports.add_c_type(type_def.super_class)
        parents.append(type_def.super_class.simple_name)
    for interface in type_def.interfaces:
        imports.add_c_type(interface)
        parents.append(interface.simple_name)

    lines: List[str] = []
    if len(parents) > 0:
        par_str: str = ", ".join(parents)
        lines.append(f"{'    ' * indent}class {type_def.name}({par_str}):")
    else:
        lines.append(f"{'    ' * indent}class {type_def.name}:")

    doc_lines: Sequence[str]
    doc_node: Doc = doc.get(str(type_def))
    if doc_node is not None:
        doc_lines = doc_node.doc_string(indent=indent + 1, line_length=line_length)
    else:
        doc_lines = [f'{"    " * (indent + 1)}""""""']
    lines.extend(doc_lines)

    for field in type_def.fields.values():
        field_lines: Sequence[str] = build_field(
            field=field,
            imports=imports,
            doc=doc,
            indent=indent + 1,
            line_length=line_length,
        )
        lines.extend(field_lines)

    constructor_overload: bool = len(type_def.constructors) > 1
    for constructor in type_def.constructors.values():
        constructor_lines: Sequence[str] = build_constructor(
            constructor=constructor,
            imports=imports,
            doc=doc,
            overload=constructor_overload,
            indent=indent + 1,
            line_length=line_length,
        )
        lines.extend(constructor_lines)

    for property in type_def.properties.values():
        property_lines: Sequence[str] = build_property(
            property=property,
            imports=imports,
            doc=doc,
            indent=indent + 1,
            line_length=line_length,
        )
        lines.extend(property_lines)

    method_names: Sequence[str] = tuple(map(lambda m: m.name, type_def.methods.values()))
    for method in type_def.methods.values():
        method_overload: bool = len(tuple(filter(lambda m: m == method.name, method_names))) > 1
        method_lines: Sequence[str] = build_method(
            method=method,
            imports=imports,
            doc=doc,
            overload=method_overload,
            indent=indent + 1,
            line_length=line_length,
        )
        lines.extend(method_lines)

    for event in type_def.events.values():
        event_lines: Sequence[str] = build_event(
            event=event,
            imports=imports,
            doc=doc,
            indent=indent + 1,
            line_length=line_length,
        )
        lines.extend(event_lines)

    for nested_type_def in type_def.nested.values():
        nested_type_def_lines: Sequence[str] = build_type_def(
            type_def=nested_type_def,
            imports=imports,
            doc=doc,
            indent=indent + 1,
            line_length=line_length,
        )
        lines.extend(nested_type_def_lines)

    return tuple(lines)


def build_struct(
    type_def: CStruct,
    imports: Imports,
    doc: Doc,
    indent: int = 0,
    line_length: int = 100,
) -> Sequence[str]:
    return build_class(
        type_def=type_def,
        imports=imports,
        doc=doc,
        indent=indent,
        line_length=line_length,
    )


def build_interface(
    type_def: CInterface,
    imports: Imports,
    doc: Doc,
    indent: int = 0,
    line_length: int = 100,
) -> Sequence[str]:
    parents: List[str] = []
    if len(type_def.generic_args) > 0:
        imports.add_py_type("typing.Generic")
        args: List[str] = []
        for arg in type_def.generic_args:
            imports.add_c_type(arg)
            args.append(arg.name)
        parents.append(f"Generic[{', '.join(args)}]")

    for interface in type_def.interfaces:
        imports.add_c_type(interface)
        parents.append(interface.simple_name)

    lines: List[str] = []
    if len(parents) > 0:
        par_str: str = ", ".join(parents)
        lines.append(f"{'    ' * indent}class {type_def.name}({par_str}):")
    else:
        lines.append(f"{'    ' * indent}class {type_def.name}:")

    doc_lines: Sequence[str]
    doc_node: Doc = doc.get(str(type_def))
    if doc_node is not None:
        doc_lines = doc_node.doc_string(indent=indent + 1, line_length=line_length)
    else:
        doc_lines = [f'{"    " * (indent + 1)}""""""']
    lines.extend(doc_lines)

    for field in type_def.fields.values():
        field_lines: Sequence[str] = build_field(
            field=field,
            imports=imports,
            doc=doc,
            indent=indent + 1,
            line_length=line_length,
        )
        lines.extend(field_lines)

    for property in type_def.properties.values():
        property_lines: Sequence[str] = build_property(
            property=property,
            imports=imports,
            doc=doc,
            indent=indent + 1,
            line_length=line_length,
        )
        lines.extend(property_lines)

    method_names: Sequence[str] = tuple(map(lambda m: m.name, type_def.methods.values()))
    for method in type_def.methods.values():
        method_overload: bool = len(tuple(filter(lambda m: m == method.name, method_names))) > 1
        method_lines: Sequence[str] = build_method(
            method=method,
            imports=imports,
            doc=doc,
            overload=method_overload,
            indent=indent + 1,
            line_length=line_length,
        )
        lines.extend(method_lines)

    for event in type_def.events.values():
        event_lines: Sequence[str] = build_event(
            event=event,
            imports=imports,
            doc=doc,
            indent=indent + 1,
            line_length=line_length,
        )
        lines.extend(event_lines)

    for nested_type_def in type_def.nested.values():
        nested_type_def_lines: Sequence[str] = build_type_def(
            type_def=nested_type_def,
            imports=imports,
            doc=doc,
            indent=indent + 1,
            line_length=line_length,
        )
        lines.extend(nested_type_def_lines)

    return tuple(lines)


def build_enum(
    type_def: CEnum,
    imports: Imports,
    doc: Doc,
    indent: int = 0,
    line_length: int = 100,
) -> Sequence[str]:
    imports.add_c_type(CType(name="Enum", namespace="System"))
    lines: List[str] = [f"{'    ' * indent}class {type_def.name}(Enum):"]

    doc_str: Sequence[str]
    indent_str: str = "    " * (indent + 1)
    doc_node: Doc = doc.get(f"{type_def.namespace}.{type_def.name}")
    if doc_node is not None:
        doc_str = doc_node.doc_string(indent=indent + 1, line_length=line_length)
    else:
        doc_str = [f'{indent_str}""""""']
    lines.extend(doc_str)

    for field in type_def.fields:
        lines.append(f"{indent_str}{field}: {type_def.name} = ...")

        doc_node: Doc = doc.get(f"{type_def.namespace}.{type_def.name}.{field}")
        if doc_node is not None:
            doc_str = doc_node.doc_string(indent=indent + 1, line_length=line_length)
        else:
            doc_str = [f'{indent_str}""""""']
        lines.extend(doc_str)

    return tuple(lines)


def build_delegate(
    type_def: CDelegate,
    imports: Imports,
    doc: Doc,
    indent: int = 0,
    line_length: int = 100,
) -> Sequence[str]:
    indent_str: str = "    " * indent

    parameters: List[str] = []
    for parameter in type_def.parameters:
        imports.add_c_type(parameter.type)
        parameters.append(parameter.type.simple_name)

    imports.add_c_type(type_def.return_type)
    return_str: str = type_def.return_type.simple_name

    imports.add_py_type("typing.Callable")
    lines: List[str] = [
        f"{indent_str}{type_def.name}: Callable[[{', '.join(parameters)}], {return_str}] = ...",
    ]

    doc_str: Sequence[str]
    doc_node: Doc = doc.get(f"{type_def.namespace}.{type_def.name}")
    if doc_node is not None:
        doc_str = doc_node.doc_string(indent=indent, line_length=line_length)
    else:
        doc_str = [f'{indent_str}""""""']
    lines.extend(doc_str)

    return tuple(lines)


def build_field(
    field: CField,
    imports: Imports,
    doc: Doc,
    indent: int = 0,
    line_length: int = 100,
) -> Sequence[str]:
    imports.add_py_type("typing.Final")
    imports.add_c_type(field.return_type)

    type_str: str = field.return_type.name
    if field.static:
        imports.add_py_type("typing.ClassVar")
        type_str = f"ClassVar[{type_str}]"

    doc_str: Sequence[str]
    doc_node: Doc = doc.get(f"{field.declaring_type.import_name}.{field.name}")
    if doc_node is not None:
        doc_str = doc_node.doc_string(indent=indent, line_length=line_length)
    else:
        doc_str = [f'{"    " * indent}""""""']

    return f"{'    ' * indent}{field.name}: Final[{type_str}] = ...", *doc_str


def build_constructor(
    constructor: CConstructor,
    imports: Imports,
    doc: Doc,
    overload: bool,
    indent: int = 0,
    line_length: int = 100,
) -> Sequence[str]:
    lines: List[str] = []

    if overload:
        imports.add_py_type("typing.overload")
        lines.append(f"{'    ' * indent}@overload")

    parameters: List[str] = []
    for parameter in constructor.parameters:
        imports.add_c_type(parameter.type)
        parameters.append(f", {parameter.name}: {parameter.type.simple_name}")

    lines.append(f"{'    ' * indent}def __init__(self{''.join(parameters)}):")

    doc_str: Sequence[str]
    doc_node: Doc = doc.get(str(constructor))
    if doc_node is not None:
        doc_str = doc_node.doc_string(indent=indent + 1, line_length=line_length)
    else:
        doc_str = [f'{"    " * (indent + 1)}""""""']
    lines.extend(doc_str)

    return tuple(lines)


def build_property(
    property: CProperty,
    imports: Imports,
    doc: Doc,
    indent: int = 0,
    line_length: int = 100,
) -> Sequence[str]:
    indent_str: str = "    " * indent

    lines: List[str] = []

    self_cls: str = "self"
    if property.static:
        self_cls = "cls"
        lines.append(f"{indent_str}@classmethod")

    lines.append(f"{indent_str}@property")
    imports.add_c_type(property.type)
    lines.append(f"{indent_str}def {property.name}({self_cls}) -> {property.type.simple_name}:")

    doc_str: Sequence[str]
    doc_node: Doc = doc.get(f"{property.declaring_type.import_name}.{property.name}")
    if doc_node is not None:
        doc_str = doc_node.doc_string(indent=indent + 1, line_length=line_length)
    else:
        doc_str = [f'{"    " * (indent + 1)}""""""']
    lines.extend(doc_str)

    if property.setter:
        if property.static:
            lines.append(f"{indent_str}@classmethod")
        lines.append(f"{indent_str}@{property.name}.setter")
        lines.append(
            f"{indent_str}def {property.name}({self_cls}, "
            f"value: {property.type.simple_name}) -> None: ..."
        )

    return tuple(lines)


def build_method(
    method: CMethod,
    imports: Imports,
    doc: Doc,
    overload: bool,
    indent: int = 0,
    line_length: int = 100,
) -> Sequence[str]:
    lines: List[str] = []

    self_cls: str = "self"
    if method.static:
        self_cls = "cls"
        lines.append(f"{'    ' * indent}@classmethod")

    if overload:
        imports.add_py_type("typing.overload")
        lines.append(f"{'    ' * indent}@overload")

    parameters: List[str] = []
    for parameter in method.parameters:
        imports.add_c_type(parameter.type)
        parameters.append(f", {parameter.name}: {parameter.type.simple_name}")

    return_str: str
    if len(method.return_types) > 1:
        imports.add_py_type("typing.Tuple")
        return_types: List[str] = []
        for return_type in method.return_types:
            imports.add_c_type(return_type)
            return_types.append(return_type.simple_name)
        return_str = f"Tuple[{', '.join(return_types)}]"
    else:
        imports.add_c_type(method.return_types[0])
        return_str = method.return_types[0].simple_name
    lines.append(
        f"{'    ' * indent}def {method.name}({self_cls}{''.join(parameters)}) -> {return_str}:"
    )

    doc_str: Sequence[str]
    param_types: str = ", ".join(str(p.type) for p in method.parameters)
    doc_node: Doc = doc.get(f"{method.declaring_type.import_name}.{method.name}({param_types})")
    if doc_node is not None:
        doc_str = doc_node.doc_string(indent=indent + 1, line_length=line_length)
    else:
        doc_str = [f'{"    " * (indent + 1)}""""""']
    lines.extend(doc_str)

    return tuple(lines)


def build_event(
    event: CEvent,
    imports: Imports,
    doc: Doc,
    indent: int = 0,
    line_length: int = 100,
) -> Sequence[str]:
    indent_str: str = "    " * indent

    imports.include_event_type = True
    imports.add_c_type(event.type)

    lines: List[str] = [f"{indent_str}{event.name}: EventType[{event.type.simple_name}] = ..."]

    doc_str: Sequence[str]
    doc_node: Doc = doc.get(f"{event.declaring_type.import_name}.{event.name}")
    if doc_node is not None:
        doc_str = doc_node.doc_string(indent=indent, line_length=line_length)
    else:
        doc_str = [f'{indent_str}""""""']
    lines.extend(doc_str)

    return tuple(lines)


def build_stubs(
    skeleton_files: Sequence[Path], doc_files: Sequence[Path], output_dir: Path, line_length: int
) -> Union[int, str]:
    namespaces: Dict[str, CNamespace] = {}
    for skeleton_file in skeleton_files:
        with skeleton_file.open("r") as file:
            skeleton_dict: Dict[str, Any] = json.load(file)

        assembly_name: str = skeleton_dict["name"]
        assembly_version: str = skeleton_dict["version"]
        logger.info("Loading skeletons for assembly: '%s v%s'", assembly_name, assembly_version)

        for namespace_json in skeleton_dict["namespaces"].values():
            namespace: CNamespace = CNamespace.from_json(namespace_json)
            if namespace.name in namespaces:
                namespace = merge_namespace(namespaces[namespace.name], namespace)
            namespaces[namespace.name] = namespace

    doc: Doc = Doc({})
    for doc_file in doc_files:
        logger.info("Loading Doc File: %r", str(doc_file))
        with doc_file.open("r") as file:
            loaded_doc_dict_tree: Dict[str, Any] = json.load(file)

        new_doc: Doc = Doc(loaded_doc_dict_tree)
        doc = merge_doc(doc, new_doc)

    for namespace in namespaces.values():
        namespace_dir: Path = output_dir
        namespace_file: Path = Path()
        for name in namespace.name.split("."):
            dir_name: str = f"{name}-stubs" if namespace_dir is output_dir else name
            namespace_dir = namespace_dir / dir_name
            # if namespace_dir.exists():
            #     rm_tree(namespace_dir)
            namespace_dir.mkdir(parents=True, exist_ok=True)

            namespace_file = namespace_dir / "__init__.pyi"
            namespace_file.touch(exist_ok=True)

        imports = Imports()
        imports.add_py_type("__future__.annotations")

        built_types: List[Sequence[str]] = []
        for type_def in namespace.types.values():
            logger.info("Building type: %s", type_def)
            built_type: Sequence[str] = build_type_def(
                type_def=type_def,
                imports=imports,
                doc=doc,
                indent=0,
                line_length=line_length,
            )
            built_types.append(built_type)

        lines: List[str] = list(imports.build(namespace.name))
        for built_type in built_types:
            lines.extend(built_type)

        logger.info("Formatting code")
        code: str = "\n".join(lines)
        black_mode: Mode = Mode(
            target_versions={
                TargetVersion.PY38,
                TargetVersion.PY39,
                TargetVersion.PY310,
                TargetVersion.PY311,
                TargetVersion.PY312,
            },
            line_length=line_length,
            # string_normalization: bool = True
            is_pyi=True,
            # is_ipynb: bool = False
            # skip_source_first_line: bool = False
            # magic_trailing_comma: bool = True
            # experimental_string_processing: bool = False
            # python_cell_magics: Set[str] = field(default_factory=set)
            # preview: bool = False
        )
        formatted_code: str = black.format_file_contents(code, fast=False, mode=black_mode)

        logger.info("Writing file: %r", str(namespace_file))
        namespace_file.write_text(formatted_code)

    return 0
