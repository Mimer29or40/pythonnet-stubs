from __future__ import annotations

import functools
import itertools
import json
import re
from collections.abc import Callable
from collections.abc import Mapping
from collections.abc import Sequence
from concurrent.futures import Executor
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from dataclasses import field
from pathlib import Path
from typing import Any
from typing import AnyStr
from typing import Final
from typing import TypeVar
from typing import cast

import black
import isort
from black import Mode
from black import TargetVersion
from black import WriteBack
from isort import Config

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

T = TypeVar("T")

logger = get_logger(__name__)

# TODO - Need to handle method that override methods in parent classes better
# Example Object.Equals(Object) -> AFObject.Equals(AFObject)


def verify_attribute(obj1, obj2, type: str, attribute: str, should_raise: bool = True) -> None:
    attr1 = getattr(obj1, attribute)
    attr2 = getattr(obj2, attribute)
    if attr1 != attr2:
        message: str = f"{type} have different {attribute} values: {attr1} != {attr2}"
        if should_raise:
            raise AttributeError(message)
        logger.warning(message)


def merge_mapping(
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


def merge_namespace(
    namespace1: CNamespace, namespace2: CNamespace, should_raise: bool = True
) -> CNamespace:
    logger.debug("Merging Namespaces: %s", namespace1)

    verify_attribute(namespace1, namespace2, "Namespaces", "name", should_raise)

    type_map: Mapping[str, CTypeDefinition] = merge_mapping(
        mapping1=namespace1.types,
        mapping2=namespace2.types,
        merge_func=merge_type_def,
        should_raise=should_raise,
    )

    return CNamespace(name=namespace1.name, types=type_map)


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


def merge_parameter(
    parameter1: CParameter, parameter2: CParameter, should_raise: bool = True
) -> CParameter:
    verify_attribute(parameter1, parameter2, "Parameters", "type", should_raise)
    verify_attribute(parameter1, parameter2, "Parameters", "default", should_raise)
    verify_attribute(parameter1, parameter2, "Parameters", "out", should_raise)

    return CParameter(
        name=parameter1.name,
        type=parameter1.type,
        default=parameter1.default,
        out=parameter1.out,
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


@dataclass
class Imports:
    types: Final[set[str]] = field(default_factory=set)
    type_vars: Final[set[str]] = field(default_factory=set)
    include_event_type: bool = False

    def add_type(self, type: CType, inner: bool = True) -> None:
        if type.generic:
            self.add_type_var(type)
            return

        self.types.add(type.import_name)
        if inner:
            for inner_type in type.inner:
                self.add_type(inner_type)

    def add_type_var(self, type: CType) -> None:
        self.add_type(CType(name="TypeVar", namespace="typing"))
        self.type_vars.add(type.name)

    def build(self, namespace: str = None) -> Sequence[str]:
        if self.include_event_type:
            self.add_type(CType(name="Generic", namespace="typing"))
            self.add_type_var(CType(name="T"))

        lines: list[str] = []

        for type in sorted(self.types):
            split: Sequence[str] = type.split(".")
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


class Doc:
    data: Mapping[str, Any]

    def __init__(self, data: Mapping[str, Any]):
        self.data = data

    @classmethod
    def split_node_str(cls, node_str: str) -> tuple[str, str | None]:
        result: list[str] = []
        i: int = 0
        n: int = len(node_str)
        bracket_count: int = 0
        while i < n:
            c: str = node_str[i]
            i = i + 1
            if c in (".", ":") and bracket_count == 0:
                return "".join(result), "".join(node_str[i:])
            if c in ("[", "("):
                bracket_count += 1
            elif c in ("]", ")"):
                bracket_count -= 1
            result.append(c)
        return "".join(result), None

    @classmethod
    def translate(cls, pattern: str) -> str:
        star: object = object()

        parts: list[str | object] = []
        i: int = 0
        n: int = len(pattern)
        while i < n:
            c: str = pattern[i]
            i = i + 1
            if c == "*":
                parts.append(star)
            elif c == "$":
                j = i
                while j < n and pattern[j] not in (",", "]", ")"):
                    j = j + 1
                parts.append(r"\$" if j >= n else star)
                i = j
            else:
                parts.append(re.escape(c))
        assert i == n

        result: list[str] = []
        i: int = 0
        n: int = len(parts)
        while i < n and parts[i] is not star:
            result.append(parts[i])
            i += 1

        next_group_num = itertools.count().__next__
        while i < n:
            assert parts[i] is star
            i += 1
            if i == n:
                result.append(".*")
                break
            assert parts[i] is not star
            fixed: list[str | object] = []
            while i < n and parts[i] is not star:
                fixed.append(parts[i])
                i += 1
            fixed_str: str = "".join(fixed)
            if i == n:
                result.append(".*")
                result.append(fixed_str)
            else:
                group_num: int = next_group_num()
                result.append(f"(?=(?P<g{group_num}>.*?{fixed_str}))(?P=g{group_num})")
        assert i == n

        result_str: str = "".join(result)
        return rf"(?s:{result_str})\Z"

    @classmethod
    @functools.lru_cache(maxsize=256, typed=True)
    def _compile_pattern(cls, pattern: AnyStr) -> re.Pattern:
        result: AnyStr
        if isinstance(pattern, bytes):
            pat_str: str = str(pattern, "ISO-8859-1")
            res_str: str = cls.translate(pat_str)
            result = bytes(res_str, "ISO-8859-1")
        else:
            result = cls.translate(pattern)
        return re.compile(result)

    def get(self, node_str: str) -> Doc | None:
        node: str
        search: str = node_str
        data: Mapping[str, Any] = self.data
        while True:
            if search in data:
                return Doc(data[search])
            node, search = self.split_node_str(search)
            for key in data:
                pattern: re.Pattern = self._compile_pattern(key)
                if pattern.match(node) is not None:
                    data = data[key]
                    if search is None:
                        return Doc(data)
                    break
            else:
                return None

    def doc_string(self, indent: int = 0, line_length: int = 100) -> Sequence[str]:
        indent_str: str = "    " * indent

        doc: str | None = self.data.get("doc", None)
        doc_formatted: Mapping[str, Sequence[str]] = self.data.get("doc_formatted", {})
        parameters: Mapping[str, str] = self.data.get("parameters", {})
        return_str: str | None = self.data.get("return", None)
        exceptions: Mapping[str, str] = self.data.get("exceptions", {})

        if len(parameters) == 0 and return_str is None and len(exceptions) == 0:
            if doc is None:
                return (f'{indent_str}""""""',)
            if "\n" not in doc and 4 * indent + len(doc) + 3 <= line_length:
                return (f'{indent_str}"""{doc}"""',)

        doc = '"""' + doc.replace("\n", "\n\n")
        doc_lines: list[str] = list(self.split(doc, indent, line_length))

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

        lines: list[str] = []
        for doc_paragraph in text.splitlines():
            words: list[str] = doc_paragraph.split(" ")
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


type_conversion: Final[Mapping[str, str]] = {}


def build_namespace(
    namespace: CNamespace,
    doc: Doc,
    line_length: int = 100,
) -> Sequence[str]:
    imports = Imports()
    imports.add_type(CType(name="annotations", namespace="__future__"))

    built_types: list[Sequence[str]] = []
    for type_def in namespace.types.values():
        logger.debug("Building type: %s", type_def)
        built_type: Sequence[str] = build_type_def(
            type_def=type_def,
            imports=imports,
            doc=doc,
            indent=0,
            line_length=line_length,
        )
        built_types.append(built_type)

    lines: list[str] = list(imports.build(namespace.name))
    for built_type in built_types:
        lines.extend(built_type)
    return lines


def build_type_def(
    type_def: CTypeDefinition,
    imports: Imports,
    doc: Doc,
    indent: int = 0,
    line_length: int = 100,
) -> Sequence[str]:
    type_name: str = type_def.__class__.__name__
    if type_name == "CClass":
        return build_class(cast("CClass", type_def), imports, doc, indent, line_length)
    if type_name == "CStruct":
        return build_struct(cast("CStruct", type_def), imports, doc, indent, line_length)
    if type_name == "CInterface":
        return build_interface(cast("CInterface", type_def), imports, doc, indent, line_length)
    if type_name == "CEnum":
        return build_enum(cast("CEnum", type_def), imports, doc, indent, line_length)
    if type_name == "CDelegate":
        return build_delegate(cast("CDelegate", type_def), imports, doc, indent, line_length)


def build_class(
    type_def: CClass,
    imports: Imports,
    doc: Doc,
    indent: int = 0,
    line_length: int = 100,
) -> Sequence[str]:
    parents: list[str] = []
    if type_def.abstract:
        imports.add_type(CType(name="ABC", namespace="abc"))
        parents.append("ABC")

    if len(type_def.generic_args) > 0:
        imports.add_type(CType(name="Generic", namespace="typing"))
        args: list[str] = []
        for arg in type_def.generic_args:
            args.append(build_type(arg, imports))
        parents.append(f"Generic[{', '.join(args)}]")

    if type_def.super_class is not None:
        parents.append(build_type(type_def.super_class, imports))
    for interface in type_def.interfaces:
        parents.append(build_type(interface, imports))

    lines: list[str] = []
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

    for nested_type_def in type_def.nested_types.values():
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
    parents: list[str] = []
    if len(type_def.generic_args) > 0:
        imports.add_type(CType(name="Generic", namespace="typing"))
        args: list[str] = []
        for arg in type_def.generic_args:
            args.append(build_type(arg, imports))
        parents.append(f"Generic[{', '.join(args)}]")

    for interface in type_def.interfaces:
        parents.append(build_type(interface, imports))

    lines: list[str] = []
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

    for nested_type_def in type_def.nested_types.values():
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
    imports.add_type(CType(name="Enum", namespace="System"))
    lines: list[str] = [f"{'    ' * indent}class {type_def.name}(Enum):"]

    indent_str: str = "    " * (indent + 1)
    doc_str: Sequence[str]
    doc_node: Doc = doc.get(str(type_def))
    if doc_node is not None:
        doc_str = doc_node.doc_string(indent=indent + 1, line_length=line_length)
    else:
        doc_str = [f'{indent_str}""""""']
    lines.extend(doc_str)

    for field in type_def.fields:
        lines.append(f"{indent_str}{make_python_name(field)}: {type_def.name} = ...")

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

    parameters: list[str] = []
    for parameter in type_def.parameters:
        parameters.append(build_type(parameter.type, imports, convert=True))

    return_str: str = build_type(type_def.return_type, imports, convert=True)

    imports.add_type(CType(name="Callable", namespace="typing"))
    lines: list[str] = [
        f"{indent_str}{type_def.name}: Callable[[{', '.join(parameters)}], {return_str}] = ...",
    ]

    doc_str: Sequence[str]
    doc_node: Doc = doc.get(str(type_def))
    if doc_node is not None:
        doc_str = doc_node.doc_string(indent=indent, line_length=line_length)
    else:
        doc_str = [f'{indent_str}""""""']
    lines.extend(doc_str)

    return tuple(lines)


def build_type(
    type: CType,
    imports: Imports,
    convert: bool = False,
) -> str:
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
            type_str = type_map[type.name]
        except KeyError:
            imports.add_type(type, inner=False)
            type_str = type.name
            if len(type.inner) > 0:
                children: list[str] = []
                for inner_type in type.inner:
                    children.append(build_type(inner_type, imports, convert=convert))
                type_str = f"{type_str}[{', '.join(children)}]"
    else:
        imports.add_type(type)
        type_str = type.simple_name

    if type.nullable:
        imports.add_type(CType(name="Optional", namespace="typing"))
        type_str = f"Optional[{type_str}]"
    return type_str


def build_parameter(
    parameter: CParameter,
    imports: Imports,
) -> str:
    param_str: str = f", {parameter.name}: {build_type(parameter.type, imports, convert=True)}"
    if parameter.default:
        param_str = param_str + " = ..."
    return param_str


def build_field(
    field: CField,
    imports: Imports,
    doc: Doc,
    indent: int = 0,
    line_length: int = 100,
) -> Sequence[str]:
    imports.add_type(CType(name="Final", namespace="typing"))

    type_str: str = build_type(field.return_type, imports, convert=True)
    if field.static:
        imports.add_type(CType(name="ClassVar", namespace="typing"))
        type_str = f"ClassVar[{type_str}]"

    doc_str: Sequence[str]
    doc_node: Doc = doc.get(str(field))
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
    lines: list[str] = []

    if overload:
        imports.add_type(CType(name="overload", namespace="typing"))
        lines.append(f"{'    ' * indent}@overload")

    parameters: Sequence[str] = tuple(
        map(lambda p: build_parameter(p, imports), constructor.parameters)
    )
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

    if property.static:
        imports.add_type(CType(name="ClassVar", namespace="typing"))
        type_str: str = f"ClassVar[{build_type(property.type, imports, convert=True)}]"
        if not property.setter:
            imports.add_type(CType(name="Final", namespace="typing"))
            type_str = f"Final[{type_str}]"

        doc_str: Sequence[str]
        doc_node: Doc = doc.get(str(property))
        if doc_node is not None:
            doc_str = doc_node.doc_string(indent=indent, line_length=line_length)
        else:
            doc_str = [f'{indent_str}""""""']

        return f"{indent_str}{property.name}: {type_str} = ...", *doc_str

    lines: list[str] = [f"{indent_str}@property"]

    property_type: str = build_type(property.type, imports, convert=True)
    lines.append(f"{indent_str}def {property.name}(self) -> {property_type}:")

    doc_str: Sequence[str]
    doc_node: Doc = doc.get(str(property))
    if doc_node is not None:
        doc_str = doc_node.doc_string(indent=indent + 1, line_length=line_length)
    else:
        doc_str = [f'{"    " * (indent + 1)}""""""']
    lines.extend(doc_str)

    if property.setter:
        lines.append(f"{indent_str}@{property.name}.setter")
        lines.append(f"{indent_str}def {property.name}(self, value: {property_type}) -> None: ...")

    return tuple(lines)


def build_method(
    method: CMethod,
    imports: Imports,
    doc: Doc,
    overload: bool,
    indent: int = 0,
    line_length: int = 100,
) -> Sequence[str]:
    lines: list[str] = []

    self_cls: str = "self"
    if method.static:
        self_cls = "cls"
        lines.append(f"{'    ' * indent}@classmethod")

    if overload:
        imports.add_type(CType(name="overload", namespace="typing"))
        lines.append(f"{'    ' * indent}@overload")

    parameters: Sequence[str] = tuple(map(lambda p: build_parameter(p, imports), method.parameters))

    return_str: str
    if len(method.return_types) > 1:
        imports.add_type(CType(name="Tuple", namespace="typing"))
        return_types: list[str] = []
        for return_type in method.return_types:
            return_types.append(build_type(return_type, imports, convert=True))
        return_str = f"Tuple[{', '.join(return_types)}]"
    else:
        return_str = build_type(method.return_types[0], imports, convert=True)

    lines.append(
        f"{'    ' * indent}def {method.name}({self_cls}{''.join(parameters)}) -> {return_str}:"
    )

    doc_str: Sequence[str]
    doc_node: Doc = doc.get(str(method))
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

    lines: list[str] = [
        f"{indent_str}{event.name}: EventType[{build_type(event.type, imports, convert=True)}] = ..."
    ]

    doc_str: Sequence[str]
    doc_node: Doc = doc.get(str(event))
    if doc_node is not None:
        doc_str = doc_node.doc_string(indent=indent, line_length=line_length)
    else:
        doc_str = [f'{indent_str}""""""']
    lines.extend(doc_str)

    return tuple(lines)


def build_stub(namespace: CNamespace, doc: Doc, output_dir: Path, line_length: int) -> None:
    logger.debug("Building namespace: %s", namespace.name)

    namespace_dir: Path = output_dir
    namespace_file: Path = Path()
    for name in namespace.name.split("."):
        dir_name: str = f"{name}-stubs" if namespace_dir is output_dir else name
        namespace_dir = namespace_dir / dir_name
        namespace_dir.mkdir(parents=True, exist_ok=True)

        namespace_file = namespace_dir / "__init__.pyi"
        namespace_file.touch(exist_ok=True)

    lines: Sequence[str] = build_namespace(
        namespace=namespace,
        doc=doc,
        line_length=line_length,
    )

    logger.info("Writing file: %r", str(namespace_file))
    namespace_file.write_text("\n".join(lines))


def build_stubs(
    skeleton_files: Sequence[Path],
    doc_files: Sequence[Path],
    output_dir: Path,
    line_length: int,
    multi_threaded: bool,
    format_files: bool,
) -> int | str:
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

    doc: Doc = Doc({})
    for doc_file in doc_files:
        logger.info("Loading Doc File: %r", str(doc_file))
        with doc_file.open("r") as file:
            loaded_doc_dict_tree: dict[str, Any] = json.load(file)

        new_doc: Doc = Doc(loaded_doc_dict_tree)
        doc = merge_doc(doc, new_doc)

    if multi_threaded:
        executor: Executor = ThreadPoolExecutor(max_workers=16, thread_name_prefix="Worker")
        for namespace in namespaces.values():
            executor.submit(build_stub, namespace, doc, output_dir, line_length)
        executor.shutdown(wait=True)
    else:
        for namespace in namespaces.values():
            build_stub(namespace, doc, output_dir, line_length)

    if format_files:

        def format_file(file: Path) -> None:
            logger.debug("Formatting file: %s", file)
            try:
                isort.file(file, config=isort_config)
            except Exception as e:
                logger.warning('Unable to run isort on file "%s":', file, exc_info=e)

            try:
                black.format_file_in_place(
                    file, fast=False, mode=black_mode, write_back=WriteBack.YES
                )
            except Exception as e:
                logger.warning('Unable to run black on file "%s":', file, exc_info=e)

        logger.info("Formatting stub files")
        isort_config = Config(
            profile="black",
            line_length=line_length,
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
            line_length=line_length,
            is_pyi=True,
        )

        if multi_threaded:
            executor: Executor = ThreadPoolExecutor(max_workers=16, thread_name_prefix="Worker")
            for file in output_dir.rglob("*.pyi"):
                executor.submit(format_file, file)
            executor.shutdown(wait=True)
        else:
            for file in output_dir.rglob("*.pyi"):
                format_file(file)

    return 0
