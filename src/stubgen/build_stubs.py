"""Build stubs from skeleton files."""

from __future__ import annotations

import json
from concurrent.futures import Executor
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING
from typing import Any
from typing import cast
from typing import override

import black
import isort
from black import Mode
from black import TargetVersion
from black import WriteBack
from isort import Config

from stubgen.command import CommandArguments
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
from stubgen.model import DocNode
from stubgen.model import ImportList
from stubgen.util import make_python_name

if TYPE_CHECKING:  # pragma: no cover
    from argparse import ArgumentParser

    # noinspection PyProtectedMember
    from argparse import _SubParsersAction
    from collections.abc import Callable
    from collections.abc import Mapping
    from collections.abc import Sequence
    from logging import Logger

    from stubgen.command import CommandResult

logger: Logger = get_logger(__name__)

# TODO(Ryan): Need to handle method that override methods in parent classes better
# Example Object.Equals(Object) -> AFObject.Equals(AFObject)


def verify_attribute(
    obj1: object, obj2: object, type_name: str, attribute: str, should_raise: bool = True
) -> None:
    attr1 = getattr(obj1, attribute)
    attr2 = getattr(obj2, attribute)
    if attr1 != attr2:
        message: str = f"{type_name} have different {attribute} values: {attr1} != {attr2}"
        if should_raise:
            raise AttributeError(message)
        logger.warning(message)


def merge_mapping[T](
    mapping1: Mapping[str, T],
    mapping2: Mapping[str, T],
    merge_func: Callable[[T, T, bool], T],
    should_raise: bool = True,
) -> Mapping[str, T]:
    key_list: set[str] = set(mapping1.keys())
    key_list.update(mapping2.keys())

    obj: T
    merged: dict[str, T] = {}
    for key in sorted(key_list):
        if key in mapping1:
            obj = mapping1[key]
            if key in mapping2:
                obj = merge_func(obj, mapping2[key], should_raise)
            merged[key] = obj
        elif key in mapping2:
            obj = mapping2[key]
            merged[key] = obj

    return merged


def merge_parameter(obj1: CParameter, obj2: CParameter, should_raise: bool = True) -> CParameter:
    verify_attribute(obj1, obj2, "Parameters", "type", should_raise)
    verify_attribute(obj1, obj2, "Parameters", "default", should_raise)
    verify_attribute(obj1, obj2, "Parameters", "out", should_raise)

    return CParameter(
        name=obj1.name,
        type=obj1.type,
        default=obj1.default,
        out=obj1.out,
    )


def merge_parameters(
    parameters1: Sequence[CParameter],
    parameters2: Sequence[CParameter],
    should_raise: bool = True,
) -> Sequence[CParameter]:
    len1: int = len(parameters1)
    len2: int = len(parameters2)
    if len1 != len2:
        message: str = f"Parameters have different length: {len1} != {len2}"
        if should_raise:
            raise AttributeError(message)
        logger.warning(message)
    return tuple(
        merge_parameter(p1, p2, should_raise)
        for p1, p2 in zip(parameters1, parameters2, strict=False)
    )


def merge_field(field1: CField, field2: CField, should_raise: bool = True) -> CField:
    verify_attribute(field1, field2, "Fields", "name", should_raise)
    verify_attribute(field1, field2, "Fields", "declaring_type", should_raise)
    verify_attribute(field1, field2, "Fields", "return_type", should_raise)
    verify_attribute(field1, field2, "Fields", "static", should_raise)

    return CField(
        name=field1.name,
        declaring_type=field1.declaring_type,
        return_type=field1.return_type,
        static=field1.static,
    )


def merge_constructor(
    constructor1: CConstructor, constructor2: CConstructor, should_raise: bool = True
) -> CConstructor:
    verify_attribute(constructor1, constructor2, "Constructors", "declaring_type", should_raise)

    parameters: Sequence[CParameter] = merge_parameters(
        constructor1.parameters, constructor2.parameters, should_raise
    )

    return CConstructor(
        declaring_type=constructor1.declaring_type,
        parameters=parameters,
    )


def merge_property(
    property1: CProperty, property2: CProperty, should_raise: bool = True
) -> CProperty:
    verify_attribute(property1, property2, "Properties", "name", should_raise)
    verify_attribute(property1, property2, "Properties", "declaring_type", should_raise)
    verify_attribute(property1, property2, "Properties", "type", should_raise)
    verify_attribute(property1, property2, "Properties", "static", should_raise)

    return CProperty(
        name=property1.name,
        declaring_type=property1.declaring_type,
        type=property1.type,
        setter=property1.setter or property2.setter,
        static=property1.static,
    )


def merge_method(method1: CMethod, method2: CMethod, should_raise: bool = True) -> CMethod:
    verify_attribute(method1, method2, "Methods", "name", should_raise)
    verify_attribute(method1, method2, "Methods", "declaring_type", should_raise)
    verify_attribute(method1, method2, "Methods", "return_types", should_raise)
    verify_attribute(method1, method2, "Methods", "static", should_raise)

    parameters: Sequence[CParameter] = merge_parameters(
        method1.parameters, method2.parameters, should_raise
    )

    return CMethod(
        name=method1.name,
        declaring_type=method1.declaring_type,
        parameters=parameters,
        return_types=method1.return_types,
        static=method1.static,
    )


def merge_event(event1: CEvent, event2: CEvent, should_raise: bool = True) -> CEvent:
    verify_attribute(event1, event2, "Properties", "name", should_raise)
    verify_attribute(event1, event2, "Properties", "declaring_type", should_raise)
    verify_attribute(event1, event2, "Properties", "type", should_raise)

    return CEvent(
        name=event1.name,
        declaring_type=event1.declaring_type,
        type=event1.type,
    )


def merge_type_def(
    type_def1: CTypeDefinition, type_def2: CTypeDefinition, should_raise: bool = True
) -> CTypeDefinition:
    logger.debug("Merging Type Definitions: %s", type_def1)
    class1: str = type_def1.__class__.__name__
    class2: str = type_def2.__class__.__name__

    if class1 != class2:
        raise TypeError(f"Type definitions are not the same: {class1} != {class2}")

    verify_attribute(type_def1, type_def2, "Type Definitions", "name", True)
    verify_attribute(type_def1, type_def2, "Type Definitions", "namespace", True)
    verify_attribute(type_def1, type_def2, "Type Definitions", "nested", True)

    if class1 == "CClass":
        return merge_class(cast("CClass", type_def1), cast("CClass", type_def2), should_raise)
    if class1 == "CStruct":
        return merge_struct(cast("CStruct", type_def1), cast("CStruct", type_def2), should_raise)
    if class1 == "CInterface":
        return merge_interface(
            cast("CInterface", type_def1), cast("CInterface", type_def2), should_raise
        )
    if class1 == "CEnum":
        return merge_enum(cast("CEnum", type_def1), cast("CEnum", type_def2), should_raise)
    if class1 == "CDelegate":
        return merge_delegate(
            cast("CDelegate", type_def1), cast("CDelegate", type_def2), should_raise
        )


def merge_class(class1: CClass, class2: CClass, should_raise: bool = True) -> CClass:
    verify_attribute(class1, class2, "Classes", "abstract", should_raise)
    verify_attribute(class1, class2, "Classes", "generic_args", should_raise)
    verify_attribute(class1, class2, "Classes", "super_class", should_raise)

    interfaces: Sequence[CType] = tuple(sorted({*class1.interfaces, *class2.interfaces}))
    fields: Mapping[str, CField] = merge_mapping(
        mapping1=class1.fields,
        mapping2=class2.fields,
        merge_func=merge_field,
        should_raise=should_raise,
    )
    constructors: Mapping[str, CConstructor] = merge_mapping(
        mapping1=class1.constructors,
        mapping2=class2.constructors,
        merge_func=merge_constructor,
        should_raise=should_raise,
    )
    properties: Mapping[str, CProperty] = merge_mapping(
        mapping1=class1.properties,
        mapping2=class2.properties,
        merge_func=merge_property,
        should_raise=should_raise,
    )
    methods: Mapping[str, CMethod] = merge_mapping(
        mapping1=class1.methods,
        mapping2=class2.methods,
        merge_func=merge_method,
        should_raise=should_raise,
    )
    events: Mapping[str, CEvent] = merge_mapping(
        mapping1=class1.events,
        mapping2=class2.events,
        merge_func=merge_event,
        should_raise=should_raise,
    )
    nested_types: Mapping[str, CTypeDefinition] = merge_mapping(
        mapping1=class1.nested_types,
        mapping2=class2.nested_types,
        merge_func=merge_type_def,
        should_raise=should_raise,
    )

    return CClass(
        name=class1.name,
        namespace=class1.namespace,
        nested=class1.nested,
        abstract=class1.abstract,
        generic_args=class1.generic_args,
        super_class=class1.super_class,
        interfaces=interfaces,
        fields=fields,
        constructors=constructors,
        properties=properties,
        methods=methods,
        events=events,
        nested_types=nested_types,
    )


def merge_struct(struct1: CStruct, struct2: CStruct, should_raise: bool = True) -> CStruct:
    verify_attribute(struct1, struct2, "Structs", "abstract", should_raise)
    verify_attribute(struct1, struct2, "Structs", "generic_args", should_raise)
    verify_attribute(struct1, struct2, "Structs", "super_class", should_raise)

    interfaces: Sequence[CType] = tuple(sorted({*struct1.interfaces, *struct2.interfaces}))
    fields: Mapping[str, CField] = merge_mapping(
        mapping1=struct1.fields,
        mapping2=struct2.fields,
        merge_func=merge_field,
        should_raise=should_raise,
    )
    constructors: Mapping[str, CConstructor] = merge_mapping(
        mapping1=struct1.constructors,
        mapping2=struct2.constructors,
        merge_func=merge_constructor,
        should_raise=should_raise,
    )
    properties: Mapping[str, CProperty] = merge_mapping(
        mapping1=struct1.properties,
        mapping2=struct2.properties,
        merge_func=merge_property,
        should_raise=should_raise,
    )
    methods: Mapping[str, CMethod] = merge_mapping(
        mapping1=struct1.methods,
        mapping2=struct2.methods,
        merge_func=merge_method,
        should_raise=should_raise,
    )
    events: Mapping[str, CEvent] = merge_mapping(
        mapping1=struct1.events,
        mapping2=struct2.events,
        merge_func=merge_event,
        should_raise=should_raise,
    )
    nested_types: Mapping[str, CTypeDefinition] = merge_mapping(
        mapping1=struct1.nested_types,
        mapping2=struct2.nested_types,
        merge_func=merge_type_def,
        should_raise=should_raise,
    )

    return CStruct(
        name=struct1.name,
        namespace=struct1.namespace,
        nested=struct1.nested,
        abstract=struct1.abstract,
        generic_args=struct1.generic_args,
        super_class=struct1.super_class,
        interfaces=interfaces,
        fields=fields,
        constructors=constructors,
        properties=properties,
        methods=methods,
        events=events,
        nested_types=nested_types,
    )


def merge_interface(
    interface1: CInterface, interface2: CInterface, should_raise: bool = True
) -> CInterface:
    verify_attribute(interface1, interface2, "Interfaces", "generic_args", should_raise)

    interfaces: Sequence[CType] = tuple(sorted({*interface1.interfaces, *interface2.interfaces}))
    fields: Mapping[str, CField] = merge_mapping(
        mapping1=interface1.fields,
        mapping2=interface2.fields,
        merge_func=merge_field,
        should_raise=should_raise,
    )
    properties: Mapping[str, CProperty] = merge_mapping(
        mapping1=interface1.properties,
        mapping2=interface2.properties,
        merge_func=merge_property,
        should_raise=should_raise,
    )
    methods: Mapping[str, CMethod] = merge_mapping(
        mapping1=interface1.methods,
        mapping2=interface2.methods,
        merge_func=merge_method,
        should_raise=should_raise,
    )
    events: Mapping[str, CEvent] = merge_mapping(
        mapping1=interface1.events,
        mapping2=interface2.events,
        merge_func=merge_event,
        should_raise=should_raise,
    )
    nested_types: Mapping[str, CTypeDefinition] = merge_mapping(
        mapping1=interface1.nested_types,
        mapping2=interface2.nested_types,
        merge_func=merge_type_def,
        should_raise=should_raise,
    )

    return CInterface(
        name=interface1.name,
        namespace=interface1.namespace,
        nested=interface1.nested,
        generic_args=interface1.generic_args,
        interfaces=interfaces,
        fields=fields,
        properties=properties,
        methods=methods,
        events=events,
        nested_types=nested_types,
    )


def merge_enum(enum1: CEnum, enum2: CEnum, should_raise: bool = True) -> CEnum:
    verify_attribute(enum1, enum2, "Enums", "fields", should_raise)

    return CEnum(
        name=enum1.name,
        namespace=enum1.namespace,
        nested=enum1.nested,
        fields=enum1.fields,
    )


def merge_delegate(
    delegate1: CDelegate, delegate2: CDelegate, should_raise: bool = True
) -> CDelegate:
    verify_attribute(delegate1, delegate2, "Delegates", "parameters", should_raise)
    verify_attribute(delegate1, delegate2, "Delegates", "return_type", should_raise)

    return CDelegate(
        name=delegate1.name,
        namespace=delegate1.namespace,
        nested=delegate1.nested,
        parameters=delegate1.parameters,
        return_type=delegate1.return_type,
    )


def merge_namespace(obj1: CNamespace, obj2: CNamespace, should_raise: bool = True) -> CNamespace:
    logger.debug("Merging Namespaces: %s", obj1)

    verify_attribute(obj1, obj2, "Namespaces", "name", should_raise)

    type_map: Mapping[str, CTypeDefinition] = merge_mapping(
        mapping1=obj1.types,
        mapping2=obj2.types,
        merge_func=merge_type_def,
        should_raise=should_raise,
    )

    return CNamespace(name=obj1.name, types=type_map)


def merge_doc(self, other: DocNode) -> DocNode:
    return DocNode(merge_doc_node(self.data, other.data))


def merge_doc_node(d1: Mapping[str, Any], d2: Mapping[str, Any]) -> Mapping[str, Any]:
    new_dict: dict[str, Any] = dict(**d1)

    for k2, v2 in d2.items():
        if k2 not in new_dict:
            new_dict[k2] = v2
            continue

        v1: Any = new_dict[k2]
        if k2 in ("doc", "return"):
            new_dict[k2] = (v1 + "\n" + v2) if v1 != "" and v2 != "" else (v1 + v2)
        elif k2 == "doc_formatted":
            new: dict[str, Sequence[str]] = dict(**v1)
            for k, v in v2.items():
                if k in new:
                    new[k] += v
                else:
                    new[k] = v
            new_dict[k2] = new
        elif k2 in ("parameters", "exceptions"):
            new: dict[str, str] = dict(**v1)
            for k, v in v2.items():
                if k in new:
                    new[k] = (new[k] + "\n" + v) if new[k] != "" and v != "" else (new[k] + v)
                else:
                    new[k] = v
            new_dict[k2] = new
        else:
            new_dict[k2] = merge_doc_node(v1, v2)
    return new_dict


def build_type(
    *,
    obj: CType,
    import_list: ImportList,
    convert: bool = False,
) -> str:
    """Build a string representation for a CType."""
    logger.debug("Building type: %s", obj.unique_name)

    if obj == CType.VOID:
        return "None"

    type_str: str
    if convert:
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
            import_list.add_type(obj)
            type_str = obj.name
    else:
        import_list.add_type(obj)
        type_str = obj.name

    if len(obj.inner) > 0:
        children: list[str] = [
            build_type(obj=t, import_list=import_list, convert=convert) for t in obj.inner
        ]
        type_str = f"{type_str}[{', '.join(children)}]"

    if obj.nullable:
        type_str = f"{type_str} | None"
    return type_str


def build_parameter(
    *,
    obj: CParameter,
    import_list: ImportList,
) -> str:
    """Build a string representation for a CParameter."""
    logger.debug("Building parameter: %s", obj.unique_name)

    param_str: str = f"{obj.name}: {build_type(obj=obj.type, import_list=import_list)}"
    if obj.default:
        param_str = param_str + " = ..."
    return param_str


def build_field(
    *,
    obj: CField,
    import_list: ImportList,
    doc_tree: DocNode,
    line_length: int,
    indent: int = 0,
) -> Sequence[str]:
    """Build a list of strings to represent a CField."""
    logger.debug("Building field: %s", obj.unique_name)

    import_list.add_final()

    type_str: str = build_type(obj=obj.return_type, import_list=import_list)
    if obj.static:
        import_list.add_class_var()
        type_str = f"ClassVar[{type_str}]"

    lines: list[str] = [f"{'    ' * indent}{obj.name}: Final[{type_str}] = ..."]

    doc_node: DocNode = doc_tree[obj.unique_name]
    lines.extend(doc_node.doc_string(indent=indent, line_length=line_length))

    return lines


def build_constructor(
    *,
    obj: CConstructor,
    import_list: ImportList,
    doc_tree: DocNode,
    overload: bool,
    line_length: int,
    indent: int = 0,
) -> Sequence[str]:
    """Build a list of strings to represent a CConstructor."""
    logger.debug("Building constructor: %s", obj.unique_name)

    lines: list[str] = []

    if overload:
        import_list.add_overload()
        lines.append(f"{'    ' * indent}@overload")

    parameters: Sequence[str] = [
        "self",
        *(build_parameter(obj=p, import_list=import_list) for p in obj.parameters),
    ]
    lines.append(f"{'    ' * indent}def __init__({', '.join(parameters)}) -> None:")

    doc_node: DocNode = doc_tree[obj.unique_name]
    lines.extend(doc_node.doc_string(indent=indent + 1, line_length=line_length))

    return lines


def build_property(
    *,
    obj: CProperty,
    import_list: ImportList,
    doc_tree: DocNode,
    line_length: int,
    indent: int = 0,
) -> Sequence[str]:
    """Build a list of strings to represent a CProperty."""
    logger.debug("Building property: %s", obj.unique_name)

    indent_str: str = "    " * indent

    if obj.static:
        import_list.add_type(CType(name="ClassVar", namespace="typing"))
        type_str: str = f"ClassVar[{build_type(obj=obj.type, import_list=import_list)}]"
        if not obj.setter:
            import_list.add_type(CType(name="Final", namespace="typing"))
            type_str = f"Final[{type_str}]"

        lines: list[str] = [f"{indent_str}{obj.name}: {type_str} = ..."]

        doc_node: DocNode = doc_tree[obj.unique_name]
        lines.extend(doc_node.doc_string(indent=indent, line_length=line_length))

        return lines

    lines: list[str] = [f"{indent_str}@property"]

    property_type: str = build_type(obj=obj.type, import_list=import_list)
    lines.append(f"{indent_str}def {obj.name}(self) -> {property_type}:")

    doc_node: DocNode = doc_tree[obj.unique_name]
    lines.extend(doc_node.doc_string(indent=indent + 1, line_length=line_length))

    if obj.setter:
        lines.append(f"{indent_str}@{obj.name}.setter")
        lines.append(f"{indent_str}def {obj.name}(self, value: {property_type}) -> None: ...")

    return lines


def build_method(
    *,
    obj: CMethod,
    import_list: ImportList,
    doc_tree: DocNode,
    overload: bool,
    line_length: int = 100,
    indent: int = 0,
) -> Sequence[str]:
    """Build a list of strings to represent a CMethod."""
    logger.debug("Building method: %s", obj.unique_name)

    lines: list[str] = []

    self_cls: str = "self"
    if obj.static:
        self_cls = "cls"
        lines.append(f"{'    ' * indent}@classmethod")

    if overload:
        import_list.add_overload()
        lines.append(f"{'    ' * indent}@overload")

    parameters: Sequence[str] = [
        self_cls,
        *(build_parameter(obj=p, import_list=import_list) for p in obj.parameters),
    ]

    return_str: str
    if len(obj.return_types) > 1:
        return_types: list[str] = [
            build_type(obj=t, import_list=import_list) for t in obj.return_types
        ]
        return_str = f"tuple[{', '.join(return_types)}]"
    else:
        return_str = build_type(obj=obj.return_types[0], import_list=import_list)

    lines.append(f"{'    ' * indent}def {obj.name}({', '.join(parameters)}) -> {return_str}:")

    doc_node: DocNode = doc_tree[obj.unique_name]
    lines.extend(doc_node.doc_string(indent=indent + 1, line_length=line_length))

    return lines


def build_event(
    *,
    obj: CEvent,
    import_list: ImportList,
    doc_tree: DocNode,
    line_length: int,
    indent: int = 0,
) -> Sequence[str]:
    """Build a list of strings to represent a CEvent."""
    logger.debug("Building event: %s", obj.unique_name)

    indent_str: str = "    " * indent

    import_list.add_event_type()

    lines: list[str] = [
        f"{indent_str}{obj.name}: "
        f"EventType[{build_type(obj=obj.type, import_list=import_list)}] = ..."
    ]

    doc_node: DocNode = doc_tree[obj.unique_name]
    lines.extend(doc_node.doc_string(indent=indent, line_length=line_length))

    return lines


def build_type_def(
    *,
    obj: CTypeDefinition,
    doc_tree: DocNode,
    import_list: ImportList,
    line_length: int,
    indent: int = 0,
) -> Sequence[str]:
    """Build a list of strings to represent a CTypeDefinition python stub."""
    match obj:
        case CClass():
            return build_class(
                obj=obj,
                doc_tree=doc_tree,
                import_list=import_list,
                line_length=line_length,
                indent=indent,
            )
        case CStruct():
            return build_struct(
                obj=obj,
                doc_tree=doc_tree,
                import_list=import_list,
                line_length=line_length,
                indent=indent,
            )
        case CInterface():
            return build_interface(
                obj=obj,
                doc_tree=doc_tree,
                import_list=import_list,
                line_length=line_length,
                indent=indent,
            )
        case CEnum():
            return build_enum(
                obj=obj,
                doc_tree=doc_tree,
                import_list=import_list,
                line_length=line_length,
                indent=indent,
            )
        case CDelegate():
            return build_delegate(
                obj=obj,
                doc_tree=doc_tree,
                import_list=import_list,
                line_length=line_length,
                indent=indent,
            )
    raise NotImplementedError  # pragma: no cover


def build_class(
    *,
    obj: CClass,
    doc_tree: DocNode,
    import_list: ImportList,
    line_length: int,
    indent: int = 0,
) -> Sequence[str]:
    """Build a list of strings to represent a CClass python stub."""
    logger.debug("Building class: %s", obj.unique_name)

    parents: list[str] = []
    if obj.abstract:
        import_list.add_abc()
        parents.append("ABC")

    generic_arg_str: str = ""
    if len(obj.generic_args) > 0:
        args: list[str] = [build_type(obj=arg, import_list=import_list) for arg in obj.generic_args]
        generic_arg_str = f"[{', '.join(args)}]"

    if obj.super_class is not None:
        parents.append(build_type(obj=obj.super_class, import_list=import_list))

    parents.extend(
        build_type(obj=interface_obj, import_list=import_list) for interface_obj in obj.interfaces
    )

    parents_str: str = f"({', '.join(parents)})" if len(parents) > 0 else ""
    lines: list[str] = [f"{'    ' * indent}class {obj.name}{generic_arg_str}{parents_str}:"]

    doc_node: DocNode = doc_tree[obj.unique_name] or DocNode("Blank")
    lines.extend(doc_node.doc_string(line_length, indent=indent + 1))

    for field_obj in obj.fields.values():
        lines.extend(
            build_field(
                obj=field_obj,
                import_list=import_list,
                doc_tree=doc_tree,
                line_length=line_length,
                indent=indent + 1,
            ),
        )

    constructor_overload: bool = len(obj.constructors) > 1
    for constructor_obj in obj.constructors.values():
        lines.extend(
            build_constructor(
                obj=constructor_obj,
                import_list=import_list,
                doc_tree=doc_tree,
                overload=constructor_overload,
                indent=indent + 1,
                line_length=line_length,
            )
        )

    for property_obj in obj.properties.values():
        lines.extend(
            build_property(
                obj=property_obj,
                import_list=import_list,
                doc_tree=doc_tree,
                line_length=line_length,
                indent=indent + 1,
            )
        )

    method_names: Sequence[str] = [m.name for m in obj.methods.values()]
    for method_obj in obj.methods.values():
        method_overload: bool = len([m for m in method_names if m == method_obj.name]) > 1
        lines.extend(
            build_method(
                obj=method_obj,
                import_list=import_list,
                doc_tree=doc_tree,
                overload=method_overload,
                line_length=line_length,
                indent=indent + 1,
            )
        )

    for event_obj in obj.events.values():
        lines.extend(
            build_event(
                obj=event_obj,
                import_list=import_list,
                doc_tree=doc_tree,
                line_length=line_length,
                indent=indent + 1,
            )
        )

    for nested_obj in obj.nested_types.values():
        lines.extend(
            build_type_def(
                obj=nested_obj,
                import_list=import_list,
                doc_tree=doc_tree,
                line_length=line_length,
                indent=indent + 1,
            )
        )

    return lines


def build_struct(
    *,
    obj: CStruct,
    doc_tree: DocNode,
    import_list: ImportList,
    line_length: int,
    indent: int = 0,
) -> Sequence[str]:
    """Build a list of strings to represent a CStruct python stub."""
    logger.debug("Building struct: %s", obj.unique_name)

    return build_class(
        obj=obj,
        doc_tree=doc_tree,
        import_list=import_list,
        line_length=line_length,
        indent=indent,
    )


def build_interface(
    *,
    obj: CInterface,
    doc_tree: DocNode,
    import_list: ImportList,
    line_length: int,
    indent: int = 0,
) -> Sequence[str]:
    """Build a list of strings to represent a CInterface python stub."""
    logger.debug("Building interface: %s", obj.unique_name)

    generic_arg_str: str = ""
    if len(obj.generic_args) > 0:
        args: list[str] = [build_type(obj=arg, import_list=import_list) for arg in obj.generic_args]
        generic_arg_str = f"[{', '.join(args)}]"

    parents: list[str] = [
        build_type(obj=interface_obj, import_list=import_list) for interface_obj in obj.interfaces
    ]

    parents_str: str = f"({', '.join(parents)})" if len(parents) > 0 else ""
    lines: list[str] = [f"{'    ' * indent}class {obj.name}{generic_arg_str}{parents_str}:"]

    doc_node: DocNode = doc_tree[obj.unique_name] or DocNode("Blank")
    lines.extend(doc_node.doc_string(line_length, indent=indent + 1))

    for field_obj in obj.fields.values():
        lines.extend(
            build_field(
                obj=field_obj,
                import_list=import_list,
                doc_tree=doc_tree,
                line_length=line_length,
                indent=indent + 1,
            ),
        )

    for property_obj in obj.properties.values():
        lines.extend(
            build_property(
                obj=property_obj,
                import_list=import_list,
                doc_tree=doc_tree,
                line_length=line_length,
                indent=indent + 1,
            )
        )

    method_names: Sequence[str] = [m.name for m in obj.methods.values()]
    for method_obj in obj.methods.values():
        method_overload: bool = len([m for m in method_names if m == method_obj.name]) > 1
        lines.extend(
            build_method(
                obj=method_obj,
                import_list=import_list,
                doc_tree=doc_tree,
                overload=method_overload,
                line_length=line_length,
                indent=indent + 1,
            )
        )

    for event_obj in obj.events.values():
        lines.extend(
            build_event(
                obj=event_obj,
                import_list=import_list,
                doc_tree=doc_tree,
                line_length=line_length,
                indent=indent + 1,
            )
        )

    for nested_obj in obj.nested_types.values():
        lines.extend(
            build_type_def(
                obj=nested_obj,
                import_list=import_list,
                doc_tree=doc_tree,
                line_length=line_length,
                indent=indent + 1,
            )
        )

    return lines


def build_enum(
    *,
    obj: CEnum,
    doc_tree: DocNode,
    import_list: ImportList,
    line_length: int,
    indent: int = 0,
) -> Sequence[str]:
    """Build a list of strings to represent a CEnum python stub."""
    logger.debug("Building enum: %s", obj.unique_name)

    import_list.add_enum()

    lines: list[str] = [f"{'    ' * indent}class {obj.name}(Enum):"]

    doc_node: DocNode = doc_tree[obj.unique_name] or DocNode("Blank")
    lines.extend(doc_node.doc_string(line_length, indent=indent + 1))

    for field_obj in obj.fields:
        lines.append(f"{'    ' * (indent + 1)}{make_python_name(field_obj)}: {obj.name} = ...")

        doc_node: DocNode = doc_tree[f"{obj.namespace}.{obj.name}.{field_obj}"] or DocNode("Blank")
        lines.extend(doc_node.doc_string(line_length, indent=indent + 1))

    return lines


def build_delegate(
    *,
    obj: CDelegate,
    doc_tree: DocNode,
    import_list: ImportList,
    line_length: int,
    indent: int = 0,
) -> Sequence[str]:
    """Build a list of strings to represent a CDelegate python stub."""
    logger.debug("Building delegate: %s", obj.unique_name)

    import_list.add_callable()

    parameters: Sequence[str] = [
        build_type(obj=p.type, import_list=import_list, convert=True) for p in obj.parameters
    ]

    return_str: str = build_type(obj=obj.return_type, import_list=import_list)

    lines: list[str] = [
        f"{'    ' * indent}{obj.name}: Callable[[{', '.join(parameters)}], {return_str}] = ...",
    ]

    doc_node: DocNode = doc_tree[obj.unique_name] or DocNode("Blank")
    lines.extend(doc_node.doc_string(line_length, indent=indent))

    return lines


def build_namespace(
    *,
    obj: CNamespace,
    doc_tree: DocNode,
    line_length: int,
) -> Sequence[str]:
    """Build a list of strings to represent a python stub."""
    logger.debug("Building namespace: %s", obj.name)

    import_list = ImportList()

    built_type_lines: list[str] = []
    for _, type_def in sorted(obj.types.items()):
        built_type_lines.extend(
            build_type_def(
                obj=type_def,
                doc_tree=doc_tree,
                import_list=import_list,
                line_length=line_length,
                indent=0,
            )
        )

    lines: list[str] = [
        f'"""Automatically generated stubs for C# namespace: {obj.name}."""',
        "",
    ]
    lines.extend(import_list.build(obj.name))
    lines.extend(built_type_lines)
    return lines


def build_stub(
    namespace: CNamespace,
    doc_tree: DocNode,
    output_dir: Path,
    line_length: int,
) -> None:
    namespace_dir: Path = output_dir
    namespace_file: Path = Path()
    for name in namespace.name.split("."):
        dir_name: str = f"{name}-stubs" if namespace_dir is output_dir else name
        namespace_dir = namespace_dir / dir_name
        namespace_dir.mkdir(parents=True, exist_ok=True)

        namespace_file = namespace_dir / "__init__.pyi"
        namespace_file.touch(exist_ok=True)

    lines: Sequence[str] = build_namespace(
        obj=namespace,
        doc_tree=doc_tree,
        line_length=line_length,
    )

    logger.info("Writing file: %r", str(namespace_file))
    namespace_file.write_text("\n".join(lines))


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

    doc_glob: str = args.docs
    doc_files: list[Path] = []
    for file_path in Path().glob(doc_glob):
        doc_files.append(file_path)
        logger.debug("Using doc_tree file: '%s'", file_path)

    doc_tree: DocNode = DocNode({})
    for doc_file in doc_files:
        logger.info("Loading DocNode File: '%s'", doc_file)
        with doc_file.open("r") as file:
            loaded_doc_dict_tree: dict[str, Any] = json.load(file)

        new_doc: DocNode = DocNode(loaded_doc_dict_tree)
        doc_tree = merge_doc(doc_tree, new_doc)

    skeleton_glob: str = args.skeletons
    skeleton_files: list[Path] = []
    for file_path in Path().glob(skeleton_glob):
        skeleton_files.append(file_path)
        logger.debug("Using skeleton file: '%s'", file_path)

    namespaces: dict[str, CNamespace] = {}
    for skeleton_file in skeleton_files:
        logger.info("Loading skeletons file: '%s'", skeleton_file)
        with skeleton_file.open("r") as file:
            skeleton_dict: dict[str, Any] = json.load(file)

        for namespace_json in skeleton_dict["namespaces"].values():
            namespace: CNamespace = CNamespace.from_json(namespace_json)
            if namespace.name in namespaces:
                namespace = merge_namespace(namespaces[namespace.name], namespace, False)
            namespaces[namespace.name] = namespace

    if args.multi_threaded:
        executor: Executor = ThreadPoolExecutor(max_workers=16, thread_name_prefix="Worker")
        for namespace in namespaces.values():
            executor.submit(build_stub, namespace, doc_tree, args.output_dir, args.line_length)
        executor.shutdown(wait=True)
    else:
        for namespace in namespaces.values():
            build_stub(namespace, doc_tree, args.output_dir, args.line_length)

    if args.format_files:

        def format_file(file: Path) -> None:
            logger.debug("Formatting file: %s", file)
            try:
                isort.file(file, config=isort_config)
            except Exception as e:
                logger.warning("Unable to run isort on file '%s':", file, exc_info=e)

            try:
                black.format_file_in_place(
                    file, fast=False, mode=black_mode, write_back=WriteBack.YES
                )
            except Exception as e:
                logger.warning("Unable to run black on file '%s':", file, exc_info=e)

        logger.info("Formatting stub files")
        isort_config = Config(
            profile="black",
            line_length=args.line_length,
            force_single_line=True,
        )
        black_mode: Mode = Mode(
            target_versions={
                TargetVersion.PY38,
                TargetVersion.PY39,
                TargetVersion.PY310,
                TargetVersion.PY311,
                TargetVersion.PY312,
            },
            line_length=args.line_length,
            is_pyi=True,
        )

        if args.multi_threaded:
            executor: Executor = ThreadPoolExecutor(max_workers=16, thread_name_prefix="Worker")
            for file in args.output_dir.rglob("*.pyi"):
                executor.submit(format_file, file)
            executor.shutdown(wait=True)
        else:
            for file in args.output_dir.rglob("*.pyi"):
                format_file(file)

    return 0
