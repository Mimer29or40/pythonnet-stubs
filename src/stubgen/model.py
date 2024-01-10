from __future__ import annotations

import dataclasses
import re
from abc import ABC
from collections import defaultdict
from dataclasses import dataclass
from types import NoneType
from typing import Any
from typing import Dict
from typing import List
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Set
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import Union

from System import Delegate
from System import MulticastDelegate
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
from stubgen.util import make_python_name

logger = get_logger(__name__)

T = TypeVar("T")

JsonType = Union[NoneType, int, float, str, Sequence, Mapping]


@dataclass
class CAssembly:
    name: str
    version: str
    culture: str
    public_key_token: str
    namespaces: Mapping[str, CNamespace]

    def to_json(self) -> JsonType:
        return {
            "name": self.name,
            "version": self.version,
            "culture": self.culture,
            "public_key_token": self.public_key_token,
            "namespaces": {k: v.to_json() for k, v in self.namespaces.items()},
        }

    @classmethod
    def from_json(cls, json: JsonType) -> CAssembly:
        return cls(
            name=json["name"],
            version=json["version"],
            culture=json["culture"],
            public_key_token=json["public_key_token"],
            namespaces={k: CNamespace.from_json(v) for k, v in json["namespaces"].items()},
        )

    @classmethod
    def extract(cls, assembly: Assembly) -> CAssembly:
        raw_namespaces: Dict[str, List[CTypeDefinition]] = defaultdict(list)
        info: TypeInfo
        for info in assembly.GetTypes():
            if info.Namespace is None or info.IsNested:
                continue
            wrapper: CTypeDefinition = CTypeDefinition.from_info(info)
            if wrapper is None:
                print("Unable to parse type:", info.FullName)
                continue
            raw_namespaces[wrapper.namespace].append(wrapper)

        namespaces: Dict[str, CNamespace] = {}
        for namespace, type_list in raw_namespaces.items():
            namespaces[namespace] = CNamespace(
                name=namespace,
                types={str(t): t for t in sorted(type_list)},
            )

        asm_name: AssemblyName = assembly.GetName()
        return cls(
            name=asm_name.Name,
            version=asm_name.Version.ToString(),
            culture=asm_name.CultureName,
            public_key_token="".join(map(lambda b: f"{b:0x}", asm_name.GetPublicKeyToken())),
            namespaces=namespaces,
        )


@dataclass
class CNamespace:
    name: str
    types: Mapping[str, CTypeDefinition]

    def to_json(self) -> JsonType:
        return {
            "name": self.name,
            "types": {k: v.to_json() for k, v in self.types.items()},
        }

    @classmethod
    def from_json(cls, json: JsonType) -> CNamespace:
        return cls(
            name=json["name"],
            types={k: CTypeDefinition.from_json(v) for k, v in json["types"].items()},
        )


@dataclass
class CTypeDefinition(ABC):
    name: str
    namespace: Optional[str]

    def __str__(self) -> str:
        name: str = self.name
        if self.namespace is not None:
            name = f"{self.namespace}.{name}"
        return name

    def __lt__(self, other: CField) -> bool:
        return self.name < other.name

    def __le__(self, other: CField) -> bool:
        return self.name <= other.name

    def __gt__(self, other: CField) -> bool:
        return self.name > other.name

    def __ge__(self, other: CField) -> bool:
        return self.name >= other.name

    def to_json(self) -> JsonType:
        pass

    @classmethod
    def from_json(cls: Type[T], json: JsonType) -> T:
        type: str = json["type"]
        if type == "class":
            return CClass.from_json(json)
        if type == "struct":
            return CStruct.from_json(json)
        if type == "interface":
            return CInterface.from_json(json)
        if type == "enum":
            return CEnum.from_json(json)
        if type == "delegate":
            return CDelegate.from_json(json)

    @classmethod
    def from_info(cls: Type[T], info: TypeInfo) -> T:
        if info.IsValueType:
            if info.IsEnum:
                return CEnum.from_info(info)
            return CStruct.from_info(info)
        if info.IsInterface:
            return CInterface.from_info(info)
        if (info.IsSubclassOf(Delegate) or info.IsSubclassOf(MulticastDelegate)) and info not in (
            Delegate,
            MulticastDelegate,
        ):
            return CDelegate.from_info(info)
        if info.IsClass:
            return CClass.from_info(info)

    @classmethod
    def get_nested_types(cls, type: TypeInfo) -> Sequence[CTypeDefinition]:
        return tuple(sorted(map(CTypeDefinition.from_info, type.GetNestedTypes())))


@dataclass
class CClass(CTypeDefinition):
    abstract: bool
    generic_args: Sequence[CType]
    super_class: CType
    interfaces: Sequence[CType]
    fields: Mapping[str, CField]
    constructors: Mapping[str, CConstructor]
    properties: Mapping[str, CProperty]
    methods: Mapping[str, CMethod]
    dunder_methods: Mapping[str, CMethod]
    events: Mapping[str, CEvent]
    nested: Mapping[str, CTypeDefinition]

    def __str__(self) -> str:
        name: str = self.name
        if self.namespace is not None:
            name = f"{self.namespace}.{name}"
        # TODO - Handle generic
        return name

    def to_json(self) -> JsonType:
        return {
            "type": "class",
            "name": self.name,
            "namespace": self.namespace,
            "abstract": self.abstract,
            "generic_args": tuple(sorted(map(CType.to_json, self.generic_args))),
            "super_class": None if self.super_class is None else self.super_class.to_json(),
            "interfaces": tuple(sorted(map(CType.to_json, self.interfaces))),
            "fields": {k: v.to_json() for k, v in self.fields.items()},
            "constructors": {k: v.to_json() for k, v in self.constructors.items()},
            "properties": {k: v.to_json() for k, v in self.properties.items()},
            "methods": {k: v.to_json() for k, v in self.methods.items()},
            "dunder_methods": {k: v.to_json() for k, v in self.dunder_methods.items()},
            "events": {k: v.to_json() for k, v in self.events.items()},
            "nested": {k: v.to_json() for k, v in self.nested.items()},
        }

    @classmethod
    def from_json(cls: Type[T], json: JsonType) -> T:
        return cls(
            name=json["name"],
            namespace=json["namespace"],
            abstract=json["abstract"],
            generic_args=tuple(map(CType.from_json, json["generic_args"])),
            super_class=CType.from_json(json["super_class"]),
            interfaces=tuple(map(CType.from_json, json["interfaces"])),
            fields={k: CField.from_json(v) for k, v in json["fields"].items()},
            constructors={k: CConstructor.from_json(v) for k, v in json["constructors"].items()},
            properties={k: CProperty.from_json(v) for k, v in json["properties"].items()},
            methods={k: CMethod.from_json(v) for k, v in json["methods"].items()},
            dunder_methods={k: CMethod.from_json(v) for k, v in json["dunder_methods"].items()},
            events={k: CEvent.from_json(v) for k, v in json["events"].items()},
            nested={k: CTypeDefinition.from_json(v) for k, v in json["nested"].items()},
        )

    @classmethod
    def from_info(cls: Type[T], info: TypeInfo) -> T:
        logger.info(f'Processing {cls.__name__} "{info.Namespace}.{info.Name}"')
        return cls(
            name=make_python_name(info.Name),
            namespace=info.Namespace,
            abstract=info.IsAbstract,
            generic_args=tuple(map(CType.from_info, info.GetGenericArguments())),
            super_class=CType.from_info(info.BaseType),
            interfaces=tuple(sorted(map(CType.from_info, info.GetInterfaces()))),
            fields={str(f): f for f in CField.get(info) if f is not None},
            constructors={str(c): c for c in CConstructor.get(info) if c is not None},
            properties={str(p): p for p in CProperty.get(info) if p is not None},
            methods={str(m): m for m in CMethod.get(info) if m is not None},
            dunder_methods={str(m): m for m in CMethod.get_dunder(info) if m is not None},
            events={str(e): e for e in CEvent.get(info) if e is not None},
            nested={str(n): n for n in CTypeDefinition.get_nested_types(info) if n is not None},
        )


@dataclass
class CStruct(CClass):
    def to_json(self) -> JsonType:
        json: Dict[str, Any] = dict(**super().to_json())
        json["type"] = "struct"
        return json


@dataclass
class CInterface(CTypeDefinition):
    generic_args: Sequence[CType]
    super_class: CType
    properties: Mapping[str, CProperty]
    methods: Mapping[str, CMethod]
    dunder_methods: Mapping[str, CMethod]
    events: Mapping[str, CEvent]

    def __str__(self) -> str:
        name: str = self.name
        if self.namespace is not None:
            name = f"{self.namespace}.{name}"
        # TODO - Handle generic
        return name

    def to_json(self) -> JsonType:
        return {
            "type": "interface",
            "name": self.name,
            "namespace": self.namespace,
            "generic_args": tuple(map(CType.to_json, self.generic_args)),
            "super_class": None if self.super_class is None else self.super_class.to_json(),
            "properties": {k: v.to_json() for k, v in self.properties.items()},
            "methods": {k: v.to_json() for k, v in self.methods.items()},
            "dunder_methods": {k: v.to_json() for k, v in self.dunder_methods.items()},
            "events": {k: v.to_json() for k, v in self.events.items()},
        }

    @classmethod
    def from_json(cls: Type[T], json: JsonType) -> T:
        return cls(
            name=json["name"],
            namespace=json["namespace"],
            generic_args=tuple(sorted(map(CType.from_json, json["generic_args"]))),
            super_class=CType.from_json(json["super_class"]),
            properties={k: CProperty.from_json(v) for k, v in json["properties"].items()},
            methods={k: CMethod.from_json(v) for k, v in json["methods"].items()},
            dunder_methods={k: CMethod.from_json(v) for k, v in json["dunder_methods"].items()},
            events={k: CEvent.from_json(v) for k, v in json["events"].items()},
        )

    @classmethod
    def from_info(cls: Type[T], info: TypeInfo) -> T:
        logger.info(f'Processing {cls.__name__} "{info.Namespace}.{info.Name}"')
        return cls(
            name=make_python_name(info.Name),
            namespace=info.Namespace,
            generic_args=tuple(map(CType.from_info, info.GetGenericArguments())),
            super_class=CType.from_info(info.BaseType),
            properties={str(p): p for p in CProperty.get(info) if p is not None},
            methods={str(m): m for m in CMethod.get(info) if m is not None},
            dunder_methods={str(m): m for m in CMethod.get_dunder(info) if m is not None},
            events={str(e): e for e in CEvent.get(info) if e is not None},
        )


@dataclass
class CEnum(CTypeDefinition):
    fields: Sequence[str]

    def to_json(self) -> JsonType:
        return {
            "type": "enum",
            "name": self.name,
            "namespace": self.namespace,
            "fields": self.fields,
        }

    @classmethod
    def from_json(cls: Type[T], json: JsonType) -> T:
        return cls(
            name=json["name"],
            namespace=json["namespace"],
            fields=tuple(json["fields"]),
        )

    @classmethod
    def from_info(cls: Type[T], info: TypeInfo) -> T:
        logger.info(f'Processing {cls.__name__} "{info.Namespace}.{info.Name}"')
        return cls(
            name=make_python_name(info.Name),
            namespace=info.Namespace,
            fields=tuple(info.GetEnumNames()),
        )


@dataclass
class CDelegate(CTypeDefinition):
    parameters: Sequence[CParameter]
    return_type: CType

    def to_json(self) -> JsonType:
        return {
            "type": "delegate",
            "name": self.name,
            "namespace": self.namespace,
            "parameters": tuple(map(CParameter.to_json, self.parameters)),
            "return_type": self.return_type.to_json(),
        }

    @classmethod
    def from_json(cls: Type[T], json: JsonType) -> T:
        return cls(
            name=json["name"],
            namespace=json["namespace"],
            parameters=tuple(map(CParameter.from_json, json["parameters"])),
            return_type=CType.from_json(json["return_type"]),
        )

    @classmethod
    def from_info(cls: Type[T], info: TypeInfo) -> T:
        logger.info(f'Processing {cls.__name__} "{info.Namespace}.{info.Name}"')

        invoke: MethodInfo = info.GetMethod("Invoke")

        return cls(
            name=make_python_name(info.Name),
            namespace=info.Namespace,
            parameters=tuple(map(CParameter.from_info, invoke.GetParameters())),
            return_type=CType.from_info(invoke.ReturnType),
        )


@dataclass(frozen=True)
class CType:
    name: str
    namespace: Optional[str]
    inner: Sequence[CType]
    is_generic: bool

    def __str__(self) -> str:
        name: str = ("$" if self.is_generic else "") + self.name
        if self.namespace is not None:
            name = f"{self.namespace}.{name}"
        if len(self.inner) > 0:
            name = f"{name}[{', '.join(map(str, self.inner))}]"
        return name

    def __lt__(self, other: CType) -> bool:
        if self.name == other.name:
            return CType.compare(self.inner, other.inner) < 0
        return self.name < other.name

    def __le__(self, other: CType) -> bool:
        if self.name == other.name:
            return CType.compare(self.inner, other.inner) <= 0
        return self.name <= other.name

    def __gt__(self, other: CType) -> bool:
        if self.name == other.name:
            return CType.compare(self.inner, other.inner) > 0
        return self.name > other.name

    def __ge__(self, other: CType) -> bool:
        if self.name == other.name:
            return CType.compare(self.inner, other.inner) >= 0
        return self.name >= other.name

    def to_json(self) -> JsonType:
        return str(self)

    @classmethod
    def from_json(cls, json: JsonType) -> Optional[CType]:
        if json is None:
            return None
        match: re.Match = re.match(r"(\w+(?:\.\w+)*)\.(\$?\w+)(?:\[(.*)])?", json)
        name: str = match.group(2)
        inner: Sequence[CType] = tuple()
        if (inner_str := match.group(3)) is not None:
            inner = tuple(map(CType.from_json, inner_str.split(", ")))
        return cls(
            name=name.replace("$", ""),
            namespace=match.group(1),
            inner=inner,
            is_generic="$" in name,
        )

    @classmethod
    def from_info(cls, info: TypeInfo) -> Optional[CType]:
        if info is None:
            return None
        return cls(
            name=make_python_name(info.Name),
            namespace=info.Namespace,
            inner=tuple(map(CType.from_info, info.GetGenericArguments())),
            is_generic=info.IsGenericParameter,
        )

    @classmethod
    def get_base_types(cls, type: TypeInfo) -> Sequence[CType]:
        found: List[CType] = []
        if type.BaseType is not None:
            found.extend(cls.get_base_types(type.BaseType))
        for interface in type.GetInterfaces():
            found.extend(cls.get_base_types(interface))
        found.append(CType.from_info(type))
        return tuple(dict.fromkeys(found).keys())

    @staticmethod
    def compare(types0: Sequence[CType], types1: Sequence[CType]) -> int:
        len0: int = len(types0)
        len1: int = len(types1)
        if len0 < len1:
            return -1
        if len0 > len1:
            return 1

        type0: CType
        type1: CType
        for type0, type1 in zip(types0, types1):
            if type0 < type1:
                return -1
            if type0 > type1:
                return 1
        return 0


@dataclass(frozen=True)
class CParameter:
    name: str
    type: CType
    has_default: bool
    is_out: bool

    def to_json(self) -> JsonType:
        return {
            "name": self.name,
            "type": self.type.to_json(),
            "has_default": self.has_default,
            "is_out": self.is_out,
        }

    @classmethod
    def from_json(cls, json: JsonType) -> CParameter:
        return cls(
            name=json["name"],
            type=CType.from_json(json["type"]),
            has_default=json["has_default"],
            is_out=json["is_out"],
        )

    @classmethod
    def from_info(cls, info: ParameterInfo) -> CParameter:
        return cls(
            name=make_python_name(info.Name),
            type=CType.from_info(info.ParameterType),
            has_default=info.HasDefaultValue,
            is_out=info.IsOut,
        )

    @staticmethod
    def compare(params0: Sequence[CParameter], params1: Sequence[CParameter]) -> int:
        len0: int = len(params0)
        len1: int = len(params1)
        if len0 < len1:
            return -1
        if len0 > len1:
            return 1

        param0: CParameter
        param1: CParameter
        for param0, param1 in zip(params0, params1):
            str0: str = str(param0.type)
            str1: str = str(param1.type)
            if str0 < str1:
                return -1
            if str0 > str1:
                return 1
        return 0


@dataclass(frozen=True)
class CField:
    name: str
    declaring_type: CType
    returns: CType
    static: bool

    def __str__(self) -> str:
        return f"{self.declaring_type}.{self.name}"

    def __lt__(self, other: CField) -> bool:
        return self.name < other.name

    def __le__(self, other: CField) -> bool:
        return self.name <= other.name

    def __gt__(self, other: CField) -> bool:
        return self.name > other.name

    def __ge__(self, other: CField) -> bool:
        return self.name >= other.name

    def to_json(self) -> JsonType:
        return {
            "name": self.name,
            "declaring_type": self.declaring_type.to_json(),
            "returns": self.returns.to_json(),
            "static": self.static,
        }

    @classmethod
    def from_json(cls, json: JsonType) -> CField:
        return cls(
            name=json["name"],
            declaring_type=CType.from_json(json["declaring_type"]),
            returns=CType.from_json(json["returns"]),
            static=json["static"],
        )

    @classmethod
    def from_info(cls, info: FieldInfo) -> CField:
        return cls(
            name=make_python_name(info.Name),
            declaring_type=CType.from_info(info.DeclaringType),
            returns=CType.from_info(info.FieldType),
            static=info.IsStatic,
        )

    @classmethod
    def get(cls, type: TypeInfo, exclude_static: bool = False) -> Sequence[CField]:
        def check(obj: CField) -> str:
            return obj.name

        found: Set[CField] = set()
        if type.BaseType is not None:
            found.update(cls.get(type.BaseType, exclude_static=True))
        for interface in type.GetInterfaces():
            found.update(cls.get(interface, exclude_static=True))

        check_list: Sequence[str] = tuple(map(check, found))
        info: MethodInfo
        for info in type.GetFields():
            if info.IsStatic and exclude_static:
                continue
            parsed = cls.from_info(info)
            if check(parsed) in check_list:
                continue
            found.add(parsed)
        return tuple(sorted(found))


@dataclass(frozen=True)
class CConstructor:
    declaring_type: CType
    parameters: Sequence[CParameter]

    def __str__(self) -> str:
        param_types: str = ", ".join(str(p.type) for p in self.parameters)
        return f"{self.declaring_type}.__init__({param_types})"

    def __lt__(self, other: CConstructor) -> bool:
        return CParameter.compare(self.parameters, other.parameters) < 0

    def __le__(self, other: CConstructor) -> bool:
        return CParameter.compare(self.parameters, other.parameters) <= 0

    def __gt__(self, other: CConstructor) -> bool:
        return CParameter.compare(self.parameters, other.parameters) > 0

    def __ge__(self, other: CConstructor) -> bool:
        return CParameter.compare(self.parameters, other.parameters) >= 0

    def to_json(self) -> JsonType:
        return {
            "declaring_type": self.declaring_type.to_json(),
            "parameters": tuple(map(CParameter.to_json, self.parameters)),
        }

    @classmethod
    def from_json(cls, json: JsonType) -> CConstructor:
        return cls(
            declaring_type=CType.from_json(json["declaring_type"]),
            parameters=tuple(map(CParameter.from_json, json["parameters"])),
        )

    @classmethod
    def from_info(cls, info: ConstructorInfo) -> CConstructor:
        return cls(
            declaring_type=CType.from_info(info.DeclaringType),
            parameters=tuple(map(CParameter.from_info, info.GetParameters())),
        )

    @classmethod
    def get(cls, type: TypeInfo) -> Sequence[CConstructor]:
        return tuple(sorted(map(CConstructor.from_info, type.GetConstructors())))


@dataclass(frozen=True)
class CProperty:
    name: str
    declaring_type: CType
    type: CType
    setter: bool
    static: bool

    def __str__(self) -> str:
        return f"{self.declaring_type}.{self.name}"

    def __lt__(self, other: CProperty) -> bool:
        return self.name < other.name

    def __le__(self, other: CProperty) -> bool:
        return self.name <= other.name

    def __gt__(self, other: CProperty) -> bool:
        return self.name > other.name

    def __ge__(self, other: CProperty) -> bool:
        return self.name >= other.name

    def to_json(self) -> JsonType:
        return {
            "name": self.name,
            "declaring_type": self.declaring_type.to_json(),
            "type": self.type.to_json(),
            "setter": self.setter,
            "static": self.static,
        }

    @classmethod
    def from_json(cls, json: JsonType) -> CProperty:
        return cls(
            name=json["name"],
            declaring_type=CType.from_json(json["declaring_type"]),
            type=CType.from_json(json["type"]),
            setter=json["setter"],
            static=json["static"],
        )

    @classmethod
    def from_info(cls, info: PropertyInfo) -> CProperty:
        get_method: MethodInfo = info.GetGetMethod()
        set_method: MethodInfo = info.GetSetMethod()

        return cls(
            name=make_python_name(info.Name),
            declaring_type=CType.from_info(info.DeclaringType),
            type=CType.from_info(info.PropertyType),
            setter=set_method is not None,
            static=get_method is not None and get_method.IsStatic,
        )

    @classmethod
    def get(cls, type: TypeInfo) -> Sequence[CProperty]:
        def check(obj: CProperty) -> str:
            return obj.name

        found: Set[CProperty] = set()
        if type.BaseType is not None:
            found.update(cls.get(type.BaseType))
        for interface in type.GetInterfaces():
            found.update(cls.get(interface))

        check_list: Sequence[str] = tuple(map(check, found))
        info: PropertyInfo
        for info in type.GetProperties():
            parsed = cls.from_info(info)
            if check(parsed) in check_list:
                continue
            found.add(parsed)
        return tuple(sorted(found))


@dataclass(frozen=True)
class CMethod:
    name: str
    declaring_type: CType
    parameters: Sequence[CParameter]
    returns: Sequence[CType]
    static: bool
    overload: bool

    def __str__(self) -> str:
        param_types: str = ", ".join(str(p.type) for p in self.parameters)
        return f"{self.declaring_type}.{self.name}({param_types})"

    def __lt__(self, other: CMethod) -> bool:
        if self.name == other.name:
            return CParameter.compare(self.parameters, other.parameters) < 0
        return self.name < other.name

    def __le__(self, other: CMethod) -> bool:
        if self.name == other.name:
            return CParameter.compare(self.parameters, other.parameters) <= 0
        return self.name <= other.name

    def __gt__(self, other: CMethod) -> bool:
        if self.name == other.name:
            return CParameter.compare(self.parameters, other.parameters) > 0
        return self.name > other.name

    def __ge__(self, other: CMethod) -> bool:
        if self.name == other.name:
            return CParameter.compare(self.parameters, other.parameters) >= 0
        return self.name >= other.name

    def to_json(self) -> JsonType:
        return {
            "name": self.name,
            "declaring_type": self.declaring_type.to_json(),
            "parameters": tuple(map(CParameter.to_json, self.parameters)),
            "returns": tuple(map(CType.to_json, self.returns)),
            "static": self.static,
            "overload": self.overload,
        }

    @classmethod
    def from_json(cls, json: JsonType) -> CMethod:
        return cls(
            name=json["name"],
            declaring_type=CType.from_json(json["declaring_type"]),
            parameters=tuple(map(CParameter.from_json, json["parameters"])),
            returns=tuple(map(CType.from_json, json["returns"])),
            static=json["static"],
            overload=json["overload"],
        )

    @classmethod
    def from_info(cls, info: MethodInfo) -> CMethod:
        return_types: List[CType] = [CType.from_info(info.ReturnType)]

        parameters: List[CParameter] = []
        for parameter_info in info.GetParameters():
            parameter: CParameter = CParameter.from_info(parameter_info)
            parameters.append(parameter)
            if parameter.is_out:
                return_types.append(parameter.type)

        return cls(
            name=make_python_name(info.Name),
            declaring_type=CType.from_info(info.DeclaringType),
            parameters=tuple(parameters),
            returns=tuple(return_types),
            static=info.IsStatic,
            overload=False,  # TODO
        )

    @classmethod
    def _get_raw(cls, type: TypeInfo, exclude_static: bool = False) -> Sequence[MethodInfo]:
        def check(obj: MethodInfo) -> Tuple[str, Sequence[str]]:
            return obj.Name, tuple(map(lambda p: p.ParameterType.FullName, obj.GetParameters()))

        found: List[MethodInfo] = []
        if type.BaseType is not None:
            found.extend(cls._get_raw(type.BaseType, exclude_static=True))
        for interface in type.GetInterfaces():
            found.extend(cls._get_raw(interface, exclude_static=True))

        check_list: Sequence[Tuple[str, Sequence[str]]] = tuple(map(check, found))
        info: MethodInfo
        for info in type.GetMethods():
            if info.IsStatic and exclude_static:
                continue
            if check(info) in check_list:
                continue
            found.append(info)
        return tuple(found)

    @classmethod
    def get(cls, type: TypeInfo) -> Sequence[CMethod]:
        def func(method: CMethod) -> bool:
            return not (method.name.startswith("get_") or method.name.startswith("set_"))

        return tuple(sorted(filter(func, map(cls.from_info, cls._get_raw(type)))))

    @classmethod
    def get_dunder(cls, type: TypeInfo) -> Sequence[CMethod]:
        dunder_methods: Set[CMethod] = set()

        supported_methods: Mapping[str, Tuple[str, bool]] = {
            # Arithmetic
            "op_Addition": ("__add__", True),
            "op_Subtraction": ("__sub__", True),
            "op_Multiply": ("__mul__", True),
            "op_Division": ("__truediv__", True),
            "op_Modulus": ("__mod__", True),
            "op_UnaryNegation": ("__neg__", True),
            "op_UnaryPlus": ("__pos__", True),
            # "op_Increment": "",
            # "op_Decrement": "",
            # Bitwise
            "op_BitwiseAnd": ("__and__", True),
            "op_BitwiseOr": ("__or__", True),
            "op_ExclusiveOr": ("__xor__", True),
            "op_LeftShift": ("__lshift__", True),
            "op_RightShift": ("__rshift__", True),
            "op_OnesComplement": ("__invert__", True),
            # "op_UnsignedRightShift": "",
            # Comparison
            "op_Equality": ("__eq__", True),
            "op_Inequality": ("__ne__", True),
            "op_LessThanOrEqual": ("__le__", True),
            "op_GreaterThanOrEqual": ("__ge__", True),
            "op_LessThan": ("__lt__", True),
            "op_GreaterThan": ("__gt__", True),
            # Other
            # "op_Implicit": ""
            # Collections
            "get_Item": ("__getitem__", False),  # TODO - Check parameters
            "set_Item": ("__setitem__", False),  # TODO - Check parameters
        }
        # Remove -> __delitem__

        def func(method: CMethod) -> bool:
            return method.name in supported_methods

        method: CMethod
        for method in filter(func, map(cls.from_info, cls._get_raw(type))):
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
            dunder_methods.add(method)

        interface: TypeInfo
        for interface in CType.get_base_types(type):
            if interface.name == "IEnumerable":
                return_type: CType
                if len(interface.inner) > 0:
                    return_type = interface.inner[0]
                else:
                    return_type = CType("object", None, (), False)
                method = CMethod(
                    name="__iter__",
                    declaring_type=CType.from_info(type),
                    parameters=tuple(),
                    returns=(CType("Iterator", "typing", (return_type,), False),),
                    static=False,
                    overload=False,
                )
                dunder_methods.add(method)
            elif interface.name == "ICollection":
                method = CMethod(
                    name="__len__",
                    declaring_type=CType.from_info(type),
                    parameters=tuple(),
                    returns=(CType("int", None, tuple(), False),),
                    static=False,
                    overload=False,
                )
                dunder_methods.add(method)

                return_type: CType
                if len(interface.inner) > 0:
                    return_type = interface.inner[0]
                else:
                    return_type = CType("object", None, (), False)
                method = CMethod(
                    name="__contains__",
                    declaring_type=CType.from_info(type),
                    parameters=(CParameter("value", return_type, False, False),),
                    returns=(CType("bool", None, tuple(), False),),
                    static=False,
                    overload=False,
                )
                dunder_methods.add(method)
        return tuple(sorted(dunder_methods))


@dataclass(frozen=True)
class CEvent:
    name: str
    declaring_type: CType
    type: CType

    def __str__(self) -> str:
        return f"{self.declaring_type}.{self.name} -> ({self.type})"

    def __lt__(self, other: CProperty) -> bool:
        return self.name < other.name

    def __le__(self, other: CProperty) -> bool:
        return self.name <= other.name

    def __gt__(self, other: CProperty) -> bool:
        return self.name > other.name

    def __ge__(self, other: CProperty) -> bool:
        return self.name >= other.name

    def to_json(self) -> JsonType:
        return {
            "name": self.name,
            "declaring_type": self.declaring_type.to_json(),
            "type": self.type.to_json(),
        }

    @classmethod
    def from_json(cls, json: JsonType) -> CEvent:
        return cls(
            name=json["name"],
            declaring_type=CType.from_json(json["declaring_type"]),
            type=CType.from_json(json["type"]),
        )

    @classmethod
    def from_info(cls, info: EventInfo) -> CEvent:
        return cls(
            name=make_python_name(info.Name),
            declaring_type=CType.from_info(info.DeclaringType),
            type=CType.from_info(info.EventHandlerType),
        )

    @classmethod
    def get(cls, type: TypeInfo) -> Sequence[CEvent]:
        def check(obj: CEvent) -> str:
            return obj.name

        found: Set[CEvent] = set()
        if type.BaseType is not None:
            found.update(cls.get(type.BaseType))
        for interface in type.GetInterfaces():
            found.update(cls.get(interface))

        check_list: Sequence[str] = tuple(map(check, found))
        info: EventInfo
        for info in type.GetEvents():
            parsed = cls.from_info(info)
            if check(parsed) in check_list:
                continue
            found.add(parsed)
        return tuple(sorted(found))
