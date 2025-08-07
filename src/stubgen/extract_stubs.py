"""Extract stubs from C# libraries to create skeleton files."""

from __future__ import annotations

import json
import sys
from argparse import ZERO_OR_MORE
from collections import defaultdict
from concurrent.futures import Executor
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from dataclasses import replace
from pathlib import Path
from typing import TYPE_CHECKING
from typing import override

import clr
from System import Delegate
from System import MulticastDelegate
from System import Nullable
from System import TypeLoadException
from System.Reflection import BindingFlags
from System.Reflection import TypeInfo

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
from stubgen.util import _is_valid_python_name
from stubgen.util import make_python_name

if TYPE_CHECKING:  # pragma: no cover
    from argparse import ArgumentParser

    # noinspection PyProtectedMember
    from argparse import _SubParsersAction
    from collections.abc import Callable
    from collections.abc import Iterable
    from collections.abc import Mapping
    from collections.abc import Sequence
    from logging import Logger

    from System.Reflection import Assembly
    from System.Reflection import ConstructorInfo
    from System.Reflection import EventInfo
    from System.Reflection import FieldInfo
    from System.Reflection import MethodInfo
    from System.Reflection import ParameterInfo
    from System.Reflection import PropertyInfo

    from stubgen.command import CommandResult
    from stubgen.model import CWrapper

    type ExtractFunc[M, T] = Callable[[M], T]
    type MemberFunc[T] = Callable[[TypeInfo, BindingFlags], Iterable[T]]

logger: Logger = get_logger(__name__)


def extract_type(info: TypeInfo | None, use_generic: bool = False) -> CType | None:
    """Extract a TypeInfo object into a CType."""
    if info is None:
        return None

    if use_generic and info.IsConstructedGenericType:
        # Converts IEquatable[Class] -> IEquatable[$T]
        info = info.GetGenericTypeDefinition()

    reference: bool = info.IsByRef
    nullable: bool = False

    name: str = make_python_name(info.Name)
    underlying_type: TypeInfo = Nullable.GetUnderlyingType(info)
    if underlying_type is not None:
        info = underlying_type
        name = make_python_name(info.Name)
        nullable = True

    generic: bool = info.IsGenericParameter
    if info.IsNested and not generic:
        parent: TypeInfo = info.DeclaringType
        while parent is not None:
            name = f"{make_python_name(parent.Name)}.{name}"
            parent = parent.DeclaringType

    extracted: CType = CType(
        name=name,
        namespace=None if generic else info.Namespace,
        inner=list(map(extract_type, info.GetGenericArguments())),
        reference=reference,
        generic=generic,
        nullable=nullable,
    )

    if info.IsArray and extracted.name != "Array":
        return CType(name="Array", namespace="System", inner=[extracted])
    return extracted


def extract_parameter(info: ParameterInfo) -> CParameter:
    """Extract a ParameterInfo object into a CParameter."""
    default: bool
    try:
        # This is here because record methods don't have "HasDefaultValue"
        default = info.HasDefaultValue
    except TypeLoadException:
        default = info.IsOptional

    return CParameter(
        name="param" if info.Name is None else make_python_name(info.Name),
        type=extract_type(info.ParameterType),
        default=default,
        out=info.IsOut,
    )


def extract_field(info: FieldInfo) -> CField:
    """Extract a FieldInfo object into a CField."""
    return CField(
        name=make_python_name(info.Name),
        declaring_type=extract_type(info.DeclaringType, use_generic=True),
        return_type=extract_type(info.FieldType),
        static=info.IsStatic,
    )


def extract_constructor(info: ConstructorInfo) -> CConstructor:
    """Extract a ConstructorInfo object into a CConstructor."""
    return CConstructor(
        declaring_type=extract_type(info.DeclaringType, use_generic=True),
        parameters=list(map(extract_parameter, info.GetParameters())),
    )


def extract_property(info: PropertyInfo) -> CProperty:
    """Extract a PropertyInfo object into a CProperty."""
    get_method: MethodInfo = info.GetGetMethod()
    set_method: MethodInfo = info.GetSetMethod()

    declaring_type: TypeInfo = info.DeclaringType
    if get_method is not None:
        declaring_type = get_method.GetBaseDefinition().DeclaringType

    return CProperty(
        name=make_python_name(info.Name),
        declaring_type=extract_type(declaring_type, use_generic=True),
        type=extract_type(info.PropertyType),
        setter=set_method is not None,
        static=get_method is not None and get_method.IsStatic,
    )


def extract_method(info: MethodInfo) -> CMethod:
    """Extract a MethodInfo object into a CMethod."""
    return_types: list[CType] = [extract_type(info.ReturnType)]

    parameters: list[CParameter] = []
    for parameter_info in info.GetParameters():
        parameter: CParameter = extract_parameter(parameter_info)
        parameters.append(parameter)
        if parameter.out:
            return_types.append(parameter.type)

    return CMethod(
        name=make_python_name(info.Name),
        declaring_type=extract_type(info.GetBaseDefinition().DeclaringType, use_generic=True),
        parameters=parameters,
        return_types=return_types,
        static=info.IsStatic,
    )


def extract_event(info: EventInfo) -> CEvent:
    """Extract a EventInfo object into a CEvent."""
    return CEvent(
        name=make_python_name(info.Name),
        declaring_type=extract_type(info.DeclaringType),
        type=extract_type(info.EventHandlerType),
    )


def _extract_members[T: CWrapper](
    type_info: TypeInfo, member_func: MemberFunc, skip_parents: bool = False
) -> dict[str, T]:
    binding_flags: BindingFlags = BindingFlags.Public | BindingFlags.Instance | BindingFlags.Static
    found: dict[str, T] = {obj.unique_name: obj for obj in member_func(type_info, binding_flags)}

    def get_parents(type_info: TypeInfo) -> list[TypeInfo]:
        parents: list[TypeInfo] = []
        if type_info.BaseType is not None:
            parents.append(type_info.BaseType)
            parents.extend(get_parents(type_info.BaseType))
        interface: TypeInfo
        for interface in type_info.GetInterfaces():
            parents.append(interface)
            parents.extend(get_parents(interface))
        return parents

    if skip_parents:
        return found

    binding_flags: BindingFlags = BindingFlags.Public | BindingFlags.Instance
    parent: TypeInfo
    for parent in get_parents(type_info):
        member: T
        for member in member_func(parent, binding_flags):
            key: str = member.unique_name
            try:
                found[key] = replace(found[key], declaring_type=member.declaring_type)
            except KeyError:
                found[key] = member

    return dict(sorted(found.items()))


def _get_fields(type_info: TypeInfo, binding_flags: BindingFlags) -> Iterable[CField]:
    return map(extract_field, type_info.GetFields(binding_flags))


def _get_constructors(type_info: TypeInfo, binding_flags: BindingFlags) -> Iterable[CConstructor]:
    return map(extract_constructor, type_info.GetConstructors(binding_flags))


def _get_properties(type_info: TypeInfo, binding_flags: BindingFlags) -> Iterable[CProperty]:
    return map(extract_property, type_info.GetProperties(binding_flags))


DUNDER_METHODS: Mapping[str, tuple[str, bool]] = {
    "op_Addition": ("__add__", True),
    "op_BitwiseAnd": ("__and__", True),
    "op_BitwiseOr": ("__or__", True),
    # op_Decrement
    "op_Division": ("__truediv__", True),
    "op_Equality": ("__eq__", True),
    "op_ExclusiveOr": ("__xor__", True),
    "op_GreaterThan": ("__gt__", True),
    "op_GreaterThanOrEqual": ("__ge__", True),
    # op_Implicit
    # op_Increment
    "op_Inequality": ("__ne__", True),
    "op_LeftShift": ("__lshift__", True),
    "op_LessThan": ("__lt__", True),
    "op_LessThanOrEqual": ("__le__", True),
    "op_Modulus": ("__mod__", True),
    "op_Multiply": ("__mul__", True),
    "op_OnesComplement": ("__invert__", True),
    "op_RightShift": ("__rshift__", True),
    "op_Subtraction": ("__sub__", True),
    "op_UnaryNegation": ("__neg__", True),
    "op_UnaryPlus": ("__pos__", True),
    # op_UnsignedRightShift
    "get_Item": ("__getitem__", False),
    "set_Item": ("__setitem__", False),
    "Remove": ("__delitem__", False),
    "get_Count": ("__len__", False),
    "Contains": ("__contains__", False),
    "ContainsKey": ("__contains__", False),
}


def _get_methods(type_info: TypeInfo) -> dict[str, CMethod]:
    def _get(type_info: TypeInfo, binding_flags: BindingFlags) -> Iterable[CMethod]:
        return map(extract_method, type_info.GetMethods(binding_flags))

    methods: dict[str, CMethod] = _extract_members(type_info, _get)

    dunder_methods: list[CMethod] = []
    method: CMethod
    for method in methods.values():
        if method.name in DUNDER_METHODS:
            dunder_name: str
            remove_param: bool
            dunder_name, remove_param = DUNDER_METHODS[method.name]
            dunder_methods.append(
                replace(
                    method,
                    name=dunder_name,
                    parameters=(
                        [replace(p, name="other") for p in method.parameters[1:]]
                        if remove_param
                        else method.parameters
                    ),
                    static=False,
                )
            )
        elif method.name == "GetEnumerator":
            dunder_methods.append(
                replace(
                    method,
                    name="__iter__",
                    return_types=[
                        replace(
                            method.return_types[0],
                            name="Iterator",
                            namespace="collections.abc",
                        )
                    ],
                )
            )
    methods.update({m.unique_name: m for m in dunder_methods})

    return {
        k: m
        for k, m in methods.items()
        if not m.name.startswith(("get_", "set_", "add_", "remove_"))
    }


def _get_events(type_info: TypeInfo, binding_flags: BindingFlags) -> Iterable[CEvent]:
    return map(extract_event, type_info.GetEvents(binding_flags))


def _get_nested(type_info: TypeInfo, binding_flags: BindingFlags) -> Iterable[CTypeDefinition]:
    return map(extract_type_def, type_info.GetNestedTypes(binding_flags))


def extract_type_def(info: TypeInfo) -> CTypeDefinition | None:
    """Extract a TypeInfo into a wrapper."""
    if info.IsValueType:
        if info.IsEnum:
            return extract_enum(info)
        return extract_class(info)
    if info.IsInterface:
        return extract_class(info)
    # noinspection PyTypeChecker
    if info not in (Delegate, MulticastDelegate) and info.IsSubclassOf(Delegate):
        return extract_delegate(info)
    if info.IsClass:
        return extract_class(info)
    # This should never be reached unless C# adds a new fundamental type
    return None  # pragma: no cover


def extract_class(info: TypeInfo) -> CClass:
    """Extract a TypeInfo object into a CClass."""
    logger.info("Extracting class '%s.%s'", info.Namespace, info.Name)

    return CClass(
        name=make_python_name(info.Name),
        namespace=info.Namespace,
        parent=extract_type(info.DeclaringType),
        abstract=info.IsAbstract,
        generic_args=list(map(extract_type, info.GetGenericArguments())),
        super_class=extract_type(info.BaseType),
        interfaces=sorted(map(extract_type, info.GetInterfaces())),
        fields=_extract_members(info, _get_fields),
        constructors=_extract_members(info, _get_constructors, skip_parents=True),
        properties=_extract_members(info, _get_properties),
        methods=_get_methods(info),
        events=_extract_members(info, _get_events),
        nested_types=_extract_members(info, _get_nested),
    )


def extract_enum(info: TypeInfo) -> CEnum:
    """Extract a TypeInfo object into a CEnum."""
    logger.info("Extracting enum '%s.%s'", info.Namespace, info.Name)

    return CEnum(
        name=make_python_name(info.Name),
        namespace=info.Namespace,
        parent=extract_type(info.DeclaringType),
        fields=list(map(make_python_name, info.GetEnumNames())),
    )


def extract_delegate(info: TypeInfo) -> CDelegate:
    """Extract a TypeInfo object into a CDelegate."""
    logger.info("Extracting delegate '%s.%s'", info.Namespace, info.Name)

    invoke: MethodInfo = info.GetMethod("Invoke")

    return CDelegate(
        name=make_python_name(info.Name),
        namespace=info.Namespace,
        parent=extract_type(info.DeclaringType),
        parameters=list(map(extract_parameter, invoke.GetParameters())),
        return_type=extract_type(invoke.ReturnType),
    )


def extract_assemblies(
    assemblies: Sequence[str],
    output_dir: Path,
    threads: int,
) -> None:
    """Extract type information from the provided assemblies."""

    def extract_assembly(assembly_name: str, output_dir: Path = output_dir) -> None:
        logger.info("Extracting assembly: %r", assembly_name)

        # noinspection PyUnresolvedReferences
        cs_assembly: Assembly = clr.AddReference(assembly_name)

        def valid_type(type_info: TypeInfo) -> bool:
            if type_info.Namespace is None or type_info.IsNested:
                return False
            if "." in type_info.Namespace:
                return all(map(_is_valid_python_name, type_info.Namespace.split(".")))
            return _is_valid_python_name(type_info.Namespace)

        type_definitions: dict[str, list[CTypeDefinition]] = defaultdict(list)
        info: TypeInfo
        for info in (t for t in cs_assembly.GetTypes() if valid_type(t)):
            type_definition: CTypeDefinition = extract_type_def(info)
            if type_definition is None:
                logger.warning("Unable to parse type: %s", info.FullName)
                continue
            type_definitions[type_definition.namespace].append(type_definition)

        assembly: CAssembly = CAssembly(
            name=cs_assembly.GetName().Name,
            version=cs_assembly.GetName().Version.ToString(),
            namespaces={
                namespace.name: namespace
                for namespace in sorted(
                    CNamespace(name=name, types={t.unique_name: t for t in sorted(types)})
                    for name, types in type_definitions.items()
                )
            },
        )
        skeleton_file: Path = output_dir / f"{assembly.name}_{assembly.version}_skeleton.json"
        logger.debug("Generating skeleton file: '%s'", skeleton_file)
        skeleton_file.write_text(json.dumps(assembly.to_json(), indent=2))

        doc_file: Path = output_dir / f"{assembly.name}_{assembly.version}_doc.json"
        logger.debug("Generating doc file: '%s'", doc_file)
        doc_file.write_text(json.dumps(assembly.doc_tree().to_json(), indent=2))

    if threads > 1:
        executor: Executor
        with ThreadPoolExecutor(max_workers=threads, thread_name_prefix="Worker") as executor:
            executor.map(extract_assembly, assemblies)
    else:
        assembly_name: str
        for assembly_name in assemblies:
            extract_assembly(assembly_name, output_dir)


@dataclass(frozen=True, kw_only=True)
class ExtractArguments(CommandArguments):
    """Arguments to run the 'extract' command."""

    command: str = "extract"

    skip_failed: bool = False
    paths: Sequence[Path] = ()

    use_all: bool = False
    use_built_in: bool = False
    use_core: bool = False

    assemblies: Sequence[str]

    @classmethod
    @override
    def populate_parser(cls, sub_parser: _SubParsersAction[ArgumentParser]) -> None:
        extract_command = sub_parser.add_parser(
            "extract",
            help="extract types from assemblies to json",
        )
        extract_command.add_argument(
            "-s",
            "--skip-failed",
            action="store_true",
            help="skips failed assemblies",
            dest="skip_failed",
        )
        extract_command.add_argument(
            "-p",
            "--path",
            action="append",
            default=[],
            type=Path,
            help="additional directories to add to the path",
            dest="paths",
        )

        assembly_group = extract_command.add_mutually_exclusive_group()
        assembly_group.add_argument(
            "-a",
            "--all",
            action="store_true",
            help="process all assemblies",
            dest="use_all",
        )
        assembly_group.add_argument(
            "-b",
            "--built_in",
            action="store_true",
            help="process built-in assemblies",
            dest="use_built_in",
        )
        assembly_group.add_argument(
            "-c",
            "--core",
            action="store_true",
            help="process core assemblies",
            dest="use_core",
        )

        extract_command.add_argument(
            "assemblies",
            nargs=ZERO_OR_MORE,
            help="names of dll assemblies to process",
        )


def command_extract(args: ExtractArguments) -> CommandResult:
    """Run the 'extract' command."""
    logger.debug("Arguments: %s", args)

    path: Path
    for path in args.paths:
        path_str: str = str(path.resolve())
        sys.path.append(path_str)

    assembly_names: list[str] = []
    if args.use_all:
        from stubgen.defaults import ASSEMBLIES
        from stubgen.defaults import BUILT_INS
        from stubgen.defaults import CORE

        assembly_names.extend(ASSEMBLIES)
        assembly_names.extend(BUILT_INS)
        assembly_names.extend(CORE)
    elif args.use_built_in:
        from stubgen.defaults import BUILT_INS

        assembly_names.extend(BUILT_INS)
    elif args.use_core:
        from stubgen.defaults import CORE

        assembly_names.extend(CORE)
    assembly_names.extend(args.assemblies)
    assembly_names = sorted(set(assembly_names))

    extract_assemblies(
        assembly_names,
        args.output_dir,
        args.threads,
    )

    return 0
