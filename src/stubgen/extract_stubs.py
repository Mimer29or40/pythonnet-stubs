from __future__ import annotations

import dataclasses
import json
from collections import defaultdict
from pathlib import Path
from typing import Dict
from typing import List
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Set
from typing import Tuple
from typing import Union

import clr
from System import Delegate
from System import MulticastDelegate
from System import Nullable
from System.Reflection import Assembly
from System.Reflection import AssemblyName
from System.Reflection import ConstructorInfo
from System.Reflection import EventInfo
from System.Reflection import FieldInfo
from System.Reflection import MethodInfo
from System.Reflection import ParameterInfo
from System.Reflection import PropertyInfo
from System.Reflection import TypeInfo

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
from stubgen.util import make_python_name

logger = get_logger(__name__)


def extract_type_def(info: TypeInfo) -> CTypeDefinition:
    def is_delegate() -> bool:
        if info in (Delegate, MulticastDelegate):
            return False
        return info.IsSubclassOf(Delegate) or info.IsSubclassOf(MulticastDelegate)

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


def extract_class(info: TypeInfo) -> CClass:
    logger.info(f'Processing class "{info.Namespace}.{info.Name}"')
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


def extract_struct(info: TypeInfo) -> CStruct:
    logger.info(f'Processing struct "{info.Namespace}.{info.Name}"')
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


def extract_interface(info: TypeInfo) -> CInterface:
    logger.info(f'Processing interface "{info.Namespace}.{info.Name}"')
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


def extract_enum(info: TypeInfo) -> CEnum:
    logger.info(f'Processing enum "{info.Namespace}.{info.Name}"')
    return CEnum(
        name=make_python_name(info.Name),
        namespace=info.Namespace,
        nested=extract_type(info.DeclaringType),
        fields=tuple(info.GetEnumNames()),
    )


def extract_delegate(info: TypeInfo) -> CDelegate:
    logger.info(f'Processing delegate "{info.Namespace}.{info.Name}"')

    invoke: MethodInfo = info.GetMethod("Invoke")

    return CDelegate(
        name=make_python_name(info.Name),
        namespace=info.Namespace,
        nested=extract_type(info.DeclaringType),
        parameters=tuple(map(extract_parameter, invoke.GetParameters())),
        return_type=extract_type(invoke.ReturnType),
    )


def extract_type(info: TypeInfo, use_generic: bool = False) -> Optional[CType]:
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
    # TODO - Item property should actually be a method
    get_method: MethodInfo = info.GetGetMethod()
    set_method: MethodInfo = info.GetSetMethod()

    return CProperty(
        name=make_python_name(info.Name),
        declaring_type=extract_type(info.DeclaringType, use_generic=True),
        type=extract_type(info.PropertyType),
        setter=set_method is not None,
        static=get_method is not None and get_method.IsStatic,
    )


def extract_method(info: MethodInfo) -> CMethod:
    return_types: List[CType] = [extract_type(info.ReturnType)]

    parameters: List[CParameter] = []
    for parameter_info in info.GetParameters():
        parameter: CParameter = extract_parameter(parameter_info)
        parameters.append(parameter)
        if parameter.out:
            return_types.append(parameter.type)

    return CMethod(
        name=make_python_name(info.Name),
        declaring_type=extract_type(info.DeclaringType, use_generic=True),
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


def _extract_fields(info: TypeInfo, exclude_static: bool = False) -> Sequence[FieldInfo]:
    def check(obj: FieldInfo) -> str:
        return obj.Name

    found: Set[FieldInfo] = set()
    if info.BaseType is not None:
        found.update(_extract_fields(info.BaseType, exclude_static=True))
    for interface in info.GetInterfaces():
        found.update(_extract_fields(interface, exclude_static=True))

    check_list: Sequence[str] = tuple(map(check, found))
    info: MethodInfo
    for info in info.GetFields():
        if info.IsStatic and exclude_static:
            continue
        if check(info) not in check_list:
            found.add(info)
    return tuple(found)


def extract_fields(info: TypeInfo) -> Mapping[str, CField]:
    return {str(f): f for f in sorted(map(extract_field, _extract_fields(info)))}


def extract_constructors(info: TypeInfo) -> Mapping[str, CConstructor]:
    return {str(c): c for c in sorted(map(extract_constructor, info.GetConstructors()))}


def _extract_properties(type: TypeInfo) -> Sequence[PropertyInfo]:
    def check(obj: PropertyInfo) -> str:
        return obj.Name

    found: Set[PropertyInfo] = set()
    if type.BaseType is not None:
        found.update(_extract_properties(type.BaseType))
    for interface in type.GetInterfaces():
        found.update(_extract_properties(interface))

    check_list: Sequence[str] = tuple(map(check, found))
    info: PropertyInfo
    for info in type.GetProperties():
        if check(info) not in check_list:
            found.add(info)
    return tuple(found)


def extract_properties(info: TypeInfo) -> Mapping[str, CProperty]:
    return {str(p): p for p in sorted(map(extract_property, _extract_properties(info)))}


def _extract_methods(type: TypeInfo, exclude_static: bool = False) -> Sequence[MethodInfo]:
    def check(obj: MethodInfo) -> Tuple[str, Sequence[str]]:
        return obj.Name, tuple(map(lambda p: p.ParameterType.FullName, obj.GetParameters()))

    found: List[MethodInfo] = []
    if type.BaseType is not None:
        found.extend(_extract_methods(type.BaseType, exclude_static=True))
    for interface in type.GetInterfaces():
        found.extend(_extract_methods(interface, exclude_static=True))

    check_list: Sequence[Tuple[str, Sequence[str]]] = tuple(map(check, found))
    info: MethodInfo
    for info in type.GetMethods():
        if info.IsStatic and exclude_static:
            continue
        if check(info) not in check_list:
            found.append(info)
    return tuple(found)


def extract_methods(info: TypeInfo) -> Mapping[str, CMethod]:
    methods: List[CMethod] = list(map(extract_method, _extract_methods(info)))

    supported_methods: Mapping[str, Tuple[str, bool]] = {
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
    }
    # Remove -> __delitem__

    method: CMethod
    for method in tuple(filter(lambda m: m.name in supported_methods, methods)):
        new_name, remove_param = supported_methods[method.name]
        parameters: Sequence[CParameter] = method.parameters
        if remove_param:
            parameters = tuple(
                map(lambda p: dataclasses.replace(p, name="other"), method.parameters[1:])
            )

        method: CMethod = dataclasses.replace(
            method,
            name=new_name,
            parameters=parameters,
            static=False,
        )
        methods.append(method)

    def get_base_types(_info: TypeInfo) -> Sequence[TypeInfo]:
        found: List[CType] = []
        if _info.BaseType is not None:
            found.extend(get_base_types(_info.BaseType))
        for interface in _info.GetInterfaces():
            found.extend(get_base_types(interface))
        found.append(_info)
        return tuple(dict.fromkeys(found).keys())

    interface: TypeInfo
    for interface in get_base_types(info):
        declaring_type: CType = extract_type(interface, use_generic=True)
        inner_types: Sequence[CType] = tuple(map(extract_type, interface.GetGenericArguments()))
        if interface.Name in ("IEnumerable", "IEnumerable`1"):
            return_types: Sequence[CType]
            if len(inner_types) > 0:
                return_types = inner_types
            else:
                return_types = (CType(name="Object", namespace="System"),)
            method = CMethod(
                name="__iter__",
                declaring_type=declaring_type,
                parameters=tuple(),
                return_types=(CType(name="Iterator", namespace="typing", inner=return_types),),
            )
            methods.append(method)
        elif interface.Name in ("ICollection", "ICollection`1"):
            method = CMethod(
                name="__len__",
                declaring_type=declaring_type,
                parameters=tuple(),
                return_types=(CType(name="Int32", namespace="System"),),
            )
            methods.append(method)

            return_type: CType
            if len(inner_types) > 0:
                return_type = inner_types[0]
            else:
                return_type = CType(name="Object", namespace="System")
            method = CMethod(
                name="__contains__",
                declaring_type=declaring_type,
                parameters=(CParameter(name="value", type=return_type),),
                return_types=(CType(name="Boolean", namespace="System"),),
            )
            methods.append(method)

    def func(method: CMethod) -> bool:
        return not (
            method.name.startswith("get_")
            or method.name.startswith("set_")
            or method.name.startswith("add_")
            or method.name.startswith("remove_")
        )

    return {str(m): m for m in sorted(filter(func, methods))}


def _extract_events(info: TypeInfo) -> Sequence[EventInfo]:
    def check(obj: EventInfo) -> str:
        return obj.Name

    found: Set[EventInfo] = set()
    if info.BaseType is not None:
        found.update(_extract_events(info.BaseType))
    for interface in info.GetInterfaces():
        found.update(_extract_events(interface))

    check_list: Sequence[str] = tuple(map(check, found))
    info: EventInfo
    for info in info.GetEvents():
        if check(info) not in check_list:
            found.add(info)
    return tuple(found)


def extract_events(info: TypeInfo) -> Mapping[str, CEvent]:
    return {str(e): e for e in sorted(map(extract_event, _extract_events(info)))}


def extract_nested_types(info: TypeInfo) -> Mapping[str, CTypeDefinition]:
    return {str(n): n for n in sorted(map(extract_type_def, info.GetNestedTypes()))}


def extract_assembly(assembly_name: str, output_dir: Path, overwrite: bool) -> Union[int, str]:
    logger.debug(f"Extracting assembly: %r", assembly_name)

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

    logger.info("Parsing types")
    type_definitions: Dict[str, List[CTypeDefinition]] = defaultdict(list)
    info: TypeInfo
    for info in assembly.GetTypes():
        if info.Namespace is None or info.IsNested:
            continue
        type_definition: CTypeDefinition = extract_type_def(info)
        if type_definition is None:
            logger.warning("Unable to parse type:", info.FullName)
            continue
        type_definitions[type_definition.namespace].append(type_definition)

    namespaces: Sequence[CNamespace] = tuple(
        CNamespace(name=namespace, types={str(t): t for t in sorted(type_list)})
        for namespace, type_list in type_definitions.items()
    )

    logger.info("Saving types to file")
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

    logger.info("Generating doc file")
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
