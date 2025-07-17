from __future__ import annotations

import itertools
import json
import sys
from argparse import ZERO_OR_MORE
from collections import defaultdict
from collections.abc import Sequence
from concurrent.futures import Executor
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING
from typing import override

import clr
from System import Delegate
from System import MulticastDelegate
from System import Nullable
from System.Reflection import Assembly
from System.Reflection import AssemblyName
from System.Reflection import BindingFlags
from System.Reflection import ConstructorInfo
from System.Reflection import EventInfo
from System.Reflection import FieldInfo
from System.Reflection import MethodInfo
from System.Reflection import ParameterInfo
from System.Reflection import PropertyInfo
from System.Reflection import TypeInfo

from stubgen.command import CommandArguments
from stubgen.defaults import ASSEMBLIES
from stubgen.defaults import BUILT_INS
from stubgen.defaults import CORE
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
from stubgen.model import CParameter
from stubgen.model import CProperty
from stubgen.model import CStruct
from stubgen.model import CType
from stubgen.model import CTypeDefinition
from stubgen.util import is_name_valid
from stubgen.util import make_python_name

if TYPE_CHECKING:  # pragma: no cover
    from argparse import ArgumentParser

    # noinspection PyProtectedMember
    from argparse import _SubParsersAction
    from collections.abc import Callable
    from collections.abc import Collection
    from collections.abc import Mapping
    from collections.abc import Sequence
    from logging import Logger
    from typing import TypeVar

    from stubgen.command import CommandResult

    T = TypeVar("T")

logger: Logger = get_logger(__name__)


def extract_type_def(info: TypeInfo) -> CTypeDefinition | None:
    def is_delegate() -> bool:
        if info in (Delegate, MulticastDelegate):
            return False
        # noinspection PyTypeChecker
        return info.IsSubclassOf(Delegate) or info.IsSubclassOf(MulticastDelegate)

    if not is_name_valid(info.Namespace):
        return None

    if info.IsValueType:
        if info.IsEnum:
            return extract_enum(info)
        return extract_struct(info)
    if info.IsInterface:
        return extract_interface(info)
    if is_delegate():
        return extract_delegate(info)
    if info.IsClass:
        return extract_class(info)


def extract_class(info: TypeInfo) -> CClass | None:
    logger.info(f'Extracting class "{info.Namespace}.{info.Name}"')
    return CClass(
        name=make_python_name(info.Name),
        namespace=info.Namespace,
        nested=extract_type(info.DeclaringType),
        abstract=info.IsAbstract,
        generic_args=tuple(map(extract_type, info.GetGenericArguments())),
        super_class=extract_type(info.BaseType),
        interfaces=tuple(sorted(map(extract_type, info.GetInterfaces()))),
        fields=extract_fields(info),
        constructors=extract_constructors(info),
        properties=extract_properties(info),
        methods=extract_methods(info),
        events=extract_events(info),
        nested_types=extract_nested_types(info),
    )


def extract_struct(info: TypeInfo) -> CStruct | None:
    logger.info(f'Extracting struct "{info.Namespace}.{info.Name}"')
    return CStruct(
        name=make_python_name(info.Name),
        namespace=info.Namespace,
        nested=extract_type(info.DeclaringType),
        abstract=info.IsAbstract,
        generic_args=tuple(map(extract_type, info.GetGenericArguments())),
        super_class=extract_type(info.BaseType),
        interfaces=tuple(sorted(map(extract_type, info.GetInterfaces()))),
        fields=extract_fields(info),
        constructors=extract_constructors(info),
        properties=extract_properties(info),
        methods=extract_methods(info),
        events=extract_events(info),
        nested_types=extract_nested_types(info),
    )


def extract_interface(info: TypeInfo) -> CInterface | None:
    logger.info(f'Extracting interface "{info.Namespace}.{info.Name}"')
    return CInterface(
        name=make_python_name(info.Name),
        namespace=info.Namespace,
        nested=extract_type(info.DeclaringType),
        generic_args=tuple(map(extract_type, info.GetGenericArguments())),
        interfaces=tuple(sorted(map(extract_type, info.GetInterfaces()))),
        fields=extract_fields(info),
        properties=extract_properties(info),
        methods=extract_methods(info),
        events=extract_events(info),
        nested_types=extract_nested_types(info),
    )


def extract_enum(info: TypeInfo) -> CEnum | None:
    logger.info(f'Extracting enum "{info.Namespace}.{info.Name}"')
    return CEnum(
        name=make_python_name(info.Name),
        namespace=info.Namespace,
        nested=extract_type(info.DeclaringType),
        fields=tuple(info.GetEnumNames()),
    )


def extract_delegate(info: TypeInfo) -> CDelegate | None:
    logger.info(f'Extracting delegate "{info.Namespace}.{info.Name}"')

    invoke: MethodInfo = info.GetMethod("Invoke")

    return CDelegate(
        name=make_python_name(info.Name),
        namespace=info.Namespace,
        nested=extract_type(info.DeclaringType),
        parameters=tuple(map(extract_parameter, invoke.GetParameters())),
        return_type=extract_type(invoke.ReturnType),
    )


def extract_type(info: TypeInfo, use_generic: bool = False) -> CType | None:
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
    elif name == "Nullable":
        args = info.GetGenericArguments()
        if len(args) > 0:
            info = args[0]
            name = make_python_name(info.Name)
            nullable = True

    generic: bool = info.IsGenericParameter
    if info.IsNested and not generic:
        parent: TypeInfo = info.DeclaringType
        while parent is not None:
            name = f"{make_python_name(parent.Name)}.{name}"
            parent = parent.DeclaringType

    extracted = CType(
        name=name,
        namespace=None if generic else info.Namespace,
        inner=tuple(map(extract_type, info.GetGenericArguments())),
        reference=reference,
        generic=generic,
        nullable=nullable,
    )

    if info.IsArray and extracted.name != "Array":
        return CType(name="Array", namespace="System", inner=(extracted,))
    return extracted


def extract_parameter(info: ParameterInfo) -> CParameter:
    return CParameter(
        name="param" if info.Name is None else make_python_name(info.Name),
        type=extract_type(info.ParameterType),
        default=info.HasDefaultValue,
        out=info.IsOut,
    )


def extract_field(info: FieldInfo) -> CField:
    return CField(
        name=make_python_name(info.Name),
        declaring_type=extract_type(info.DeclaringType),
        return_type=extract_type(info.FieldType),
        static=info.IsStatic,
    )


def extract_constructor(info: ConstructorInfo) -> CConstructor:
    return CConstructor(
        declaring_type=extract_type(info.DeclaringType),
        parameters=tuple(map(extract_parameter, info.GetParameters())),
    )


def extract_property(info: PropertyInfo) -> CProperty:
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
        parameters=tuple(parameters),
        return_types=tuple(return_types),
        static=info.IsStatic,
    )


def extract_event(info: EventInfo) -> CEvent:
    return CEvent(
        name=make_python_name(info.Name),
        declaring_type=extract_type(info.DeclaringType),
        type=extract_type(info.EventHandlerType),
    )


def extract_base_members(
    type_info: TypeInfo,
    found: dict[str, T],
    extract: Callable[[TypeInfo, BindingFlags], Collection[T]],
) -> None:
    bases: list[T] = []
    base_binding_flags: BindingFlags = BindingFlags.Public | BindingFlags.Instance
    if type_info.BaseType is not None:
        bases.extend(extract(type_info.BaseType, base_binding_flags))
    interface: TypeInfo
    for interface in type_info.GetInterfaces():
        bases.extend(extract(interface, base_binding_flags))

    base: T
    for base in bases:
        key: str = base.to_doc_json()[0]
        new: T
        if key in found:
            new = dataclasses.replace(found[key], declaring_type=base.declaring_type)
        else:
            new = base
        found[key] = new


def extract_fields(type_info: TypeInfo) -> Mapping[str, CField]:
    def extract_raw(type_info: TypeInfo, binding_flags: BindingFlags = None) -> Collection[CField]:
        found: dict[str, CField] = {}

        info: FieldInfo
        if binding_flags is None:
            binding_flags = BindingFlags.Public | BindingFlags.Instance | BindingFlags.Static
        for info in type_info.GetFields(binding_flags):
            obj: CField = extract_field(info)
            key: str = obj.to_doc_json()[0]
            found[key] = obj

        extract_base_members(type_info, found, extract_raw)

        return found.values()

    raw_members: Collection[CField] = extract_raw(type_info)

    sorted_members: Sequence[CField] = sorted(raw_members)

    return {str(member): member for member in sorted_members}


def extract_constructors(type_info: TypeInfo) -> Mapping[str, CConstructor]:
    def extract_raw(
        type_info: TypeInfo, binding_flags: BindingFlags = None
    ) -> Collection[CConstructor]:
        found: dict[str, CConstructor] = {}

        info: ConstructorInfo
        if binding_flags is None:
            binding_flags = BindingFlags.Public | BindingFlags.Instance | BindingFlags.Static
        for info in type_info.GetConstructors(binding_flags):
            obj: CConstructor = extract_constructor(info)
            key: str = obj.to_doc_json()[0]
            found[key] = obj

        return found.values()

    raw_members: Collection[CConstructor] = extract_raw(type_info)

    sorted_members: Sequence[CConstructor] = sorted(raw_members)

    return {str(member): member for member in sorted_members}


def extract_properties(type_info: TypeInfo) -> Mapping[str, CProperty]:
    def extract_raw(
        type_info: TypeInfo, binding_flags: BindingFlags = None
    ) -> Collection[CProperty]:
        found: dict[str, CProperty] = {}

        info: PropertyInfo
        if binding_flags is None:
            binding_flags = BindingFlags.Public | BindingFlags.Instance | BindingFlags.Static
        for info in type_info.GetProperties(binding_flags):
            obj: CProperty = extract_property(info)
            key: str = obj.to_doc_json()[0]
            found[key] = obj

        extract_base_members(type_info, found, extract_raw)

        return found.values()

    raw_members: Collection[CProperty] = extract_raw(type_info)

    sorted_members: Sequence[CProperty] = sorted(raw_members)

    # TODO - Item property will need a special type to handle get/set of different types
    excluded: Collection[str] = ("Item",)

    def filter_func(member: CProperty) -> bool:
        return member.name not in excluded

    return {str(member): member for member in sorted_members if filter_func(member)}


def extract_methods(type_info: TypeInfo) -> Mapping[str, CMethod]:
    def extract_raw(type_info: TypeInfo, binding_flags: BindingFlags = None) -> Collection[CMethod]:
        found: dict[str, CMethod] = {}

        info: MethodInfo
        if binding_flags is None:
            binding_flags = BindingFlags.Public | BindingFlags.Instance | BindingFlags.Static
        for info in type_info.GetMethods(binding_flags):
            obj: CMethod = extract_method(info)
            key: str = obj.to_doc_json()[0]
            found[key] = obj

        extract_base_members(type_info, found, extract_raw)

        return found.values()

    raw_members: list[CMethod] = list(extract_raw(type_info))

    supported_methods: Mapping[str, tuple[str, bool]] = {
        "op_Addition": ("__add__", True),
        "op_BitwiseAnd": ("__and__", True),
        "op_BitwiseOr": ("__or__", True),
        # "op_Decrement": "",
        "op_Division": ("__truediv__", True),
        "op_Equality": ("__eq__", True),
        "op_ExclusiveOr": ("__xor__", True),
        "op_GreaterThan": ("__gt__", True),
        "op_GreaterThanOrEqual": ("__ge__", True),
        # "op_Implicit": ""
        # "op_Increment": "",
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
        # "op_UnsignedRightShift": "",
        "get_Item": ("__getitem__", False),
        "set_Item": ("__setitem__", False),
        "Remove": ("__delitem__", False),
        "get_Count": ("__len__", False),
        "Contains": ("__contains__", False),
        "ContainsKey": ("__contains__", False),
    }

    method: CMethod
    for method in tuple(raw_members):
        if method.name in supported_methods:
            new_name, remove_param = supported_methods[method.name]
            parameters: Sequence[CParameter] = method.parameters
            if remove_param:
                parameters = tuple(
                    map(
                        lambda p: dataclasses.replace(p, name="other"),
                        method.parameters[1:],
                    )
                )

            method: CMethod = dataclasses.replace(
                method,
                name=new_name,
                parameters=parameters,
                static=False,
            )
            raw_members.append(method)
        if method.name == "GetEnumerator":
            return_types: Sequence[CType] = (
                dataclasses.replace(
                    method.return_types[0],
                    name="Iterator",
                    namespace="typing",
                ),
            )
            method: CMethod = dataclasses.replace(
                method,
                name="__iter__",
                return_types=return_types,
            )
            raw_members.append(method)

    sorted_members: Sequence[CMethod] = sorted(raw_members)

    def filter_func(member: CMethod) -> bool:
        return not (
            member.name.startswith("get_")
            or member.name.startswith("set_")
            or member.name.startswith("add_")
            or member.name.startswith("remove_")
        )

    return {str(member): member for member in sorted_members if filter_func(member)}


def extract_events(type_info: TypeInfo) -> Mapping[str, CEvent]:
    def extract_raw(type_info: TypeInfo, binding_flags: BindingFlags = None) -> Collection[CEvent]:
        found: dict[str, CEvent] = {}

        info: EventInfo
        if binding_flags is None:
            binding_flags = BindingFlags.Public | BindingFlags.Instance | BindingFlags.Static
        for info in type_info.GetEvents(binding_flags):
            obj: CEvent = extract_event(info)
            key: str = obj.to_doc_json()[0]
            found[key] = obj

        extract_base_members(type_info, found, extract_raw)

        return found.values()

    raw_members: Collection[CEvent] = extract_raw(type_info)

    sorted_members: Sequence[CEvent] = sorted(raw_members)

    return {str(member): member for member in sorted_members}


def extract_nested_types(type_info: TypeInfo) -> Mapping[str, CTypeDefinition]:
    def extract_raw(
        type_info: TypeInfo, binding_flags: BindingFlags = None
    ) -> Collection[CTypeDefinition]:
        found: dict[str, CTypeDefinition] = {}

        info: TypeInfo
        if binding_flags is None:
            binding_flags = BindingFlags.Public
        for info in type_info.GetNestedTypes(binding_flags):
            obj: CTypeDefinition = extract_type_def(info)
            key: str = obj.to_doc_json()[0]
            found[key] = obj

        return found.values()

    raw_members: Collection[CTypeDefinition] = extract_raw(type_info)

    sorted_members: Sequence[CTypeDefinition] = sorted(raw_members)

    return {str(member): member for member in sorted_members}


def extract_assembly(assembly_name: str, output_dir: Path, overwrite: bool) -> int | str:
    logger.info("Extracting assembly: %r", assembly_name)

    assembly: Assembly = clr.AddReference(assembly_name)
    name: AssemblyName = assembly.GetName()

    assembly_name: str = name.Name
    assembly_version: str = name.Version.ToString()

    extract_file: Path = output_dir / f"{assembly_name}_{assembly_version}_skeleton.json"
    if extract_file.exists() and not overwrite:
        logger.critical("Extract file already exists: %r", str(extract_file))
        return 1

    doc_file: Path = output_dir / f"{assembly_name}_{assembly_version}_doc.json"
    if doc_file.exists() and not overwrite:
        logger.critical("Doc file already exists: %r", str(doc_file))
        return 1

    logger.debug("Parsing types")
    type_definitions: dict[str, list[CTypeDefinition]] = defaultdict(list)
    info: TypeInfo
    for info in assembly.GetTypes():
        if info.Namespace is None or info.IsNested:
            continue
        type_definition: CTypeDefinition = extract_type_def(info)
        if type_definition is None:
            logger.warning("Unable to parse type: %s", info.FullName)
            continue
        type_definitions[type_definition.namespace].append(type_definition)

    namespaces: Sequence[CNamespace] = tuple(
        CNamespace(name=namespace, types={str(t): t for t in sorted(type_list)})
        for namespace, type_list in type_definitions.items()
    )

    logger.debug("Saving types to file: %r", str(extract_file))
    with extract_file.open("w") as file:
        json.dump(
            {
                "name": assembly_name,
                "version": assembly_version,
                "namespaces": {
                    str(namespace): namespace.to_json() for namespace in sorted(namespaces)
                },
            },
            file,
            indent=2,
        )

    logger.debug("Generating doc file: %r", str(doc_file))
    main_doc_namespace = {}
    for namespace in namespaces:
        curr = main_doc_namespace
        for n in namespace.name.split("."):
            if n not in curr:
                curr[n] = {"doc": ""}
            curr = curr[n]
        for type in namespace.types.values():
            name, doc_json = type.to_doc_json()
            curr[name] = doc_json

    with doc_file.open("w") as file:
        json.dump(
            main_doc_namespace,
            file,
            indent=2,
        )

    return 0


def extract_assemblies(
    assembly_names: Sequence[str],
    output_dir: Path,
    overwrite: bool,
    skip_failed: bool,
    multi_threaded: bool,
) -> int | str:
    if multi_threaded:
        executor: Executor = ThreadPoolExecutor(max_workers=16, thread_name_prefix="Worker")
        for exit_code in executor.map(
            extract_assembly,
            assembly_names,
            itertools.repeat(output_dir),
            itertools.repeat(overwrite),
        ):
            if exit_code != 0 and not skip_failed:
                executor.shutdown(cancel_futures=True)
                return exit_code
        executor.shutdown(wait=True)
    else:
        assembly_name: str
        for assembly_name in assembly_names:
            try:
                exit_code: int | str = extract_assembly(assembly_name, output_dir, overwrite)
                if exit_code != 0 and not skip_failed:
                    return exit_code
            except Exception as e:
                if skip_failed:
                    logger.warning("Could not extract assembly: %s", assembly_name, exc_info=e)
                else:
                    raise e from None

    return 0


@dataclass(frozen=True, kw_only=True)
class ExtractArguments(CommandArguments):
    """Arguments to run the 'extract' command."""

    command: str = "extract"

    skip_failed: bool = False
    paths: Sequence[Path] = ()
    overwrite: bool = False

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
        extract_command.add_argument(
            "-w",
            "--overwrite",
            action="store_true",
            help="overwrite existing files",
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
        assembly_names.extend(ASSEMBLIES)
        assembly_names.extend(BUILT_INS)
        assembly_names.extend(CORE)
    elif args.use_built_in:
        assembly_names.extend(BUILT_INS)
    elif args.use_core:
        assembly_names.extend(CORE)
    assembly_names.extend(args.assemblies)
    assembly_names = sorted(set(assembly_names))

    exit_code: CommandResult
    if args.multi_threaded:
        executor: Executor = ThreadPoolExecutor(max_workers=16, thread_name_prefix="Worker")
        for exit_code in executor.map(
            extract_assembly,
            assembly_names,
            itertools.repeat(args.output_dir),
            itertools.repeat(args.overwrite),
        ):
            if exit_code != 0 and not args.skip_failed:
                executor.shutdown(cancel_futures=True)
                return exit_code
        executor.shutdown(wait=True)
    else:
        assembly_name: str
        for assembly_name in assembly_names:
            try:
                exit_code = extract_assembly(assembly_name, args.output_dir, args.overwrite)
                if exit_code != 0 and not args.skip_failed:
                    return exit_code
            except Exception as e:
                if args.skip_failed:
                    logger.warning("Could not extract assembly: %s", assembly_name, exc_info=e)
                else:
                    raise e from None

    return 0
