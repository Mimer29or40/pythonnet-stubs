from __future__ import annotations

import re
from abc import ABC
from abc import abstractmethod
from collections.abc import Mapping
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any
from typing import Self
from typing import TypeVar
from typing import Union

from stubgen.log import get_logger

T = TypeVar("T")

JsonType = Union[None, int, float, str, Sequence, Mapping]

logger = get_logger(__name__)


@dataclass(frozen=True)
class CNamespace:
    name: str
    types: Mapping[str, CTypeDefinition]

    def __str__(self) -> str:
        return self.name

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
            "types": {k: v.to_json() for k, v in self.types.items()},
        }

    @classmethod
    def from_json(cls, json: JsonType) -> CNamespace:
        return cls(
            name=json["name"],
            types={k: CTypeDefinition.from_json(v) for k, v in json["types"].items()},
        )


@dataclass(frozen=True)
class CTypeDefinition(ABC):
    name: str
    namespace: str | None
    nested: CType | None

    def __str__(self) -> str:
        name: str = self.simple_name
        if self.nested is not None:
            name = f"{self.nested.full_name}.{name}"
        elif self.namespace is not None:
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

    @property
    def simple_name(self) -> str:
        name: str = self.name
        if hasattr(self, "generic_args"):
            if len(self.generic_args) > 0:
                generic: str = ", ".join(map(str, self.generic_args))
                name = f"{name}[{generic}]"
        return name

    @abstractmethod
    def to_json(self) -> JsonType:
        pass

    @abstractmethod
    def to_doc_json(self) -> tuple[str, JsonType]:
        pass

    @classmethod
    def from_json(cls, json: JsonType) -> Self:
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


@dataclass(frozen=True)
class CClass(CTypeDefinition):
    abstract: bool
    generic_args: Sequence[CType]
    super_class: CType | None
    interfaces: Sequence[CType]
    fields: Mapping[str, CField]
    constructors: Mapping[str, CConstructor]
    properties: Mapping[str, CProperty]
    methods: Mapping[str, CMethod]
    events: Mapping[str, CEvent]
    nested_types: Mapping[str, CTypeDefinition]

    def to_json(self) -> JsonType:
        return {
            "type": "class",
            "name": self.name,
            "namespace": self.namespace,
            "nested": None if self.nested is None else self.nested.to_json(),
            "abstract": self.abstract,
            "generic_args": tuple(a.to_json() for a in self.generic_args),
            "super_class": None if self.super_class is None else self.super_class.to_json(),
            "interfaces": tuple(sorted(i.to_json() for i in self.interfaces)),
            "fields": {k: v.to_json() for k, v in self.fields.items()},
            "constructors": {k: v.to_json() for k, v in self.constructors.items()},
            "properties": {k: v.to_json() for k, v in self.properties.items()},
            "methods": {k: v.to_json() for k, v in self.methods.items()},
            "events": {k: v.to_json() for k, v in self.events.items()},
            "nested_types": {k: v.to_json() for k, v in self.nested_types.items()},
        }

    def to_doc_json(self) -> tuple[str, JsonType]:
        doc_json: dict[str, Any] = {"doc": "", "doc_formatted": {}}

        members: Sequence[CMember] = (
            *self.fields.values(),
            *self.constructors.values(),
            *self.properties.values(),
            *self.methods.values(),
            *self.events.values(),
        )
        for member in members:
            if member.declaring_type.name == self.name:
                name, json = member.to_doc_json()
                doc_json[name] = json

        child: CTypeDefinition
        for child in self.nested_types.values():
            name, json = child.to_doc_json()
            doc_json[name] = json

        return self.simple_name, doc_json

    @classmethod
    def from_json(cls, json: JsonType) -> Self:
        return cls(
            name=json["name"],
            namespace=json["namespace"],
            nested=CType.from_json(json["nested"]),
            abstract=json["abstract"],
            generic_args=tuple(map(CType.from_json, json["generic_args"])),
            super_class=CType.from_json(json["super_class"]),
            interfaces=tuple(map(CType.from_json, json["interfaces"])),
            fields={k: CField.from_json(v) for k, v in json["fields"].items()},
            constructors={k: CConstructor.from_json(v) for k, v in json["constructors"].items()},
            properties={k: CProperty.from_json(v) for k, v in json["properties"].items()},
            methods={k: CMethod.from_json(v) for k, v in json["methods"].items()},
            events={k: CEvent.from_json(v) for k, v in json["events"].items()},
            nested_types={k: CTypeDefinition.from_json(v) for k, v in json["nested_types"].items()},
        )


@dataclass(frozen=True)
class CStruct(CClass):
    def to_json(self) -> JsonType:
        json: dict[str, Any] = dict(**super().to_json())
        json["type"] = "struct"
        return json


@dataclass(frozen=True)
class CInterface(CTypeDefinition):
    generic_args: Sequence[CType]
    interfaces: Sequence[CType]
    fields: Mapping[str, CField]
    properties: Mapping[str, CProperty]
    methods: Mapping[str, CMethod]
    events: Mapping[str, CEvent]
    nested_types: Mapping[str, CTypeDefinition]

    def to_json(self) -> JsonType:
        return {
            "type": "interface",
            "name": self.name,
            "namespace": self.namespace,
            "nested": None if self.nested is None else self.nested.to_json(),
            "generic_args": tuple(a.to_json() for a in self.generic_args),
            "interfaces": tuple(sorted(i.to_json() for i in self.interfaces)),
            "fields": {k: v.to_json() for k, v in self.fields.items()},
            "properties": {k: v.to_json() for k, v in self.properties.items()},
            "methods": {k: v.to_json() for k, v in self.methods.items()},
            "events": {k: v.to_json() for k, v in self.events.items()},
            "nested_types": {k: v.to_json() for k, v in self.nested_types.items()},
        }

    def to_doc_json(self) -> tuple[str, JsonType]:
        doc_json: dict[str, Any] = {"doc": "", "doc_formatted": {}}

        members: Sequence[CMember] = (
            *self.fields.values(),
            *self.properties.values(),
            *self.methods.values(),
            *self.events.values(),
        )
        for member in members:
            if member.declaring_type.name == self.name:
                name, json = member.to_doc_json()
                doc_json[name] = json

        child: CTypeDefinition
        for child in self.nested_types.values():
            name, json = child.to_doc_json()
            doc_json[name] = json

        return self.simple_name, doc_json

    @classmethod
    def from_json(cls, json: JsonType) -> Self:
        return cls(
            name=json["name"],
            namespace=json["namespace"],
            nested=CType.from_json(json["nested"]),
            generic_args=tuple(sorted(map(CType.from_json, json["generic_args"]))),
            interfaces=tuple(map(CType.from_json, json["interfaces"])),
            fields={k: CField.from_json(v) for k, v in json["fields"].items()},
            properties={k: CProperty.from_json(v) for k, v in json["properties"].items()},
            methods={k: CMethod.from_json(v) for k, v in json["methods"].items()},
            events={k: CEvent.from_json(v) for k, v in json["events"].items()},
            nested_types={k: CTypeDefinition.from_json(v) for k, v in json["nested_types"].items()},
        )


@dataclass(frozen=True)
class CEnum(CTypeDefinition):
    fields: Sequence[str]

    def to_json(self) -> JsonType:
        return {
            "type": "enum",
            "name": self.name,
            "namespace": self.namespace,
            "nested": None if self.nested is None else self.nested.to_json(),
            "fields": self.fields,
        }

    def to_doc_json(self) -> tuple[str, JsonType]:
        return self.simple_name, {
            "doc": "",
            "doc_formatted": {},
            **{f: {"doc": ""} for f in self.fields},
        }

    @classmethod
    def from_json(cls, json: JsonType) -> Self:
        return cls(
            name=json["name"],
            namespace=json["namespace"],
            nested=CType.from_json(json["nested"]),
            fields=tuple(json["fields"]),
        )


@dataclass(frozen=True)
class CDelegate(CTypeDefinition):
    parameters: Sequence[CParameter]
    return_type: CType

    @property
    def simple_name(self) -> str:
        param_types: str = ", ".join(str(p.type) for p in self.parameters)
        return f"{self.name}({param_types})"

    def to_json(self) -> JsonType:
        return {
            "type": "delegate",
            "name": self.name,
            "namespace": self.namespace,
            "nested": None if self.nested is None else self.nested.to_json(),
            "parameters": tuple(p.to_json() for p in self.parameters),
            "return_type": self.return_type.to_json(),
        }

    def to_doc_json(self) -> tuple[str, JsonType]:
        doc_json: dict[str, Any] = {"doc": "", "doc_formatted": {}}
        if len(self.parameters) > 0:
            doc_json["parameters"] = {p.name: "" for p in self.parameters}
        if self.return_type is not None and self.return_type != CType("Void", "System"):
            doc_json["return"] = ""
        return self.simple_name, doc_json

    @classmethod
    def from_json(cls, json: JsonType) -> Self:
        return cls(
            name=json["name"],
            namespace=json["namespace"],
            nested=CType.from_json(json["nested"]),
            parameters=tuple(map(CParameter.from_json, json["parameters"])),
            return_type=CType.from_json(json["return_type"]),
        )


@dataclass(frozen=True)
class CType:
    name: str
    namespace: str | None = None
    inner: Sequence[CType] = tuple()
    reference: bool = False
    generic: bool = False
    nullable: bool = False

    def __str__(self) -> str:
        return self.full_name

    def __lt__(self, other: CType) -> bool:
        return CType.compare(self, other) < 0

    def __le__(self, other: CType) -> bool:
        return CType.compare(self, other) <= 0

    def __gt__(self, other: CType) -> bool:
        return CType.compare(self, other) > 0

    def __ge__(self, other: CType) -> bool:
        return CType.compare(self, other) >= 0

    @property
    def import_name(self) -> str:
        name: str = self.name
        if self.namespace is not None:
            name = f"{self.namespace}.{name}"
        return name

    @property
    def simple_name(self) -> str:
        name: str = self.name
        if len(self.inner) > 0:
            name = f"{name}[{', '.join(t.simple_name for t in self.inner)}]"
        return name

    @property
    def full_name(self) -> str:
        name: str = self.name
        if self.reference:
            name = "*" + name
        if self.generic:
            name = "$" + name
        if self.nullable:
            name = name + "?"
        if self.namespace is not None:
            name = f"{self.namespace}:{name}"
        if len(self.inner) > 0:
            name = f"{name}[{', '.join(map(str, self.inner))}]"
        return name

    def to_json(self) -> JsonType:
        return str(self)

    @classmethod
    def from_json(cls, json: JsonType) -> CType | None:
        if json is None:
            return None
        match: re.Match = re.match(
            r"(?:(\w+(?:\.\w+)*):)?(\$?\*?\w+(?:\.\w+)*\??)(?:\[(.*)])?", json
        )
        name: str = match.group(2)
        inner: Sequence[CType] = tuple()
        if (inner_str := match.group(3)) is not None:
            inner = tuple(map(CType.from_json, inner_str.split(", ")))
        return cls(
            name=re.sub(r"[?$*]", "", name),
            namespace=match.group(1),
            inner=inner,
            reference="*" in name,
            generic="$" in name,
            nullable="?" in name,
        )

    @staticmethod
    def compare(type0: CType, type1: CType) -> int:
        if type0.namespace != type1.namespace:
            if type0.namespace is None:
                return -1
            if type1.namespace is None:
                return 1
            return -1 if type0.namespace < type1.namespace else 1
        if type0.name != type1.name:
            return -1 if type0.name < type1.name else 1
        if (inner := CType.compare_seq(type0.inner, type1.inner)) != 0:
            return inner
        if type0.reference != type1.reference:
            return 1 if type0.reference else -1
        if type0.generic != type1.generic:
            return 1 if type0.generic else -1
        if type0.nullable != type1.nullable:
            return 1 if type0.nullable else -1
        return 0

    @staticmethod
    def compare_seq(types0: Sequence[CType], types1: Sequence[CType]) -> int:
        len0: int = len(types0)
        len1: int = len(types1)
        if len0 < len1:
            return -1
        if len0 > len1:
            return 1

        type0: CType
        type1: CType
        for type0, type1 in zip(types0, types1, strict=False):
            if (compare := CType.compare(type0, type1)) != 0:
                return compare
        return 0


@dataclass(frozen=True)
class CParameter:
    name: str
    type: CType
    default: bool = False
    out: bool = False

    def to_json(self) -> JsonType:
        return {
            "name": self.name,
            "type": self.type.to_json(),
            "default": self.default,
            "out": self.out,
        }

    @classmethod
    def from_json(cls, json: JsonType) -> CParameter:
        return cls(
            name=json["name"],
            type=CType.from_json(json["type"]),
            default=json["default"],
            out=json["out"],
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
        for param0, param1 in zip(params0, params1, strict=False):
            str0: str = str(param0.type)
            str1: str = str(param1.type)
            if str0 < str1:
                return -1
            if str0 > str1:
                return 1
        return 0


@dataclass(frozen=True)
class CMember(ABC):
    name: str
    declaring_type: CType

    def __str__(self) -> str:
        return f"{self.declaring_type}.{self.name}"

    @abstractmethod
    def to_json(self) -> JsonType:
        pass

    @abstractmethod
    def to_doc_json(self) -> tuple[str, JsonType]:
        pass


@dataclass(frozen=True)
class CField(CMember):
    return_type: CType
    static: bool = False

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
            "return_type": self.return_type.to_json(),
            "static": self.static,
        }

    def to_doc_json(self) -> tuple[str, JsonType]:
        doc_json: dict[str, Any] = {"doc": "", "doc_formatted": {}}
        if self.return_type is not None and self.return_type != CType("Void", "System"):
            doc_json["return"] = ""
        return self.name, doc_json

    @classmethod
    def from_json(cls, json: JsonType) -> CField:
        return cls(
            name=json["name"],
            declaring_type=CType.from_json(json["declaring_type"]),
            return_type=CType.from_json(json["return_type"]),
            static=json["static"],
        )


@dataclass(frozen=True)
class CConstructor(CMember):
    parameters: Sequence[CParameter]

    def __init__(self, declaring_type: CType, parameters: Sequence[CParameter]) -> None:
        super().__init__("__init__", declaring_type)
        object.__setattr__(self, "parameters", parameters)

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
            "parameters": tuple(p.to_json() for p in self.parameters),
        }

    def to_doc_json(self) -> tuple[str, JsonType]:
        doc_json: dict[str, Any] = {"doc": "", "doc_formatted": {}}
        if len(self.parameters) > 0:
            doc_json["parameters"] = {p.name: "" for p in self.parameters}
        param_types: str = ", ".join(str(p.type) for p in self.parameters)
        return f"__init__({param_types})", doc_json

    @classmethod
    def from_json(cls, json: JsonType) -> CConstructor:
        return cls(
            declaring_type=CType.from_json(json["declaring_type"]),
            parameters=tuple(map(CParameter.from_json, json["parameters"])),
        )


@dataclass(frozen=True)
class CProperty(CMember):
    type: CType
    setter: bool = False
    static: bool = False

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

    def to_doc_json(self) -> tuple[str, JsonType]:
        doc_json: dict[str, Any] = {"doc": "", "doc_formatted": {}}
        if self.type is not None and self.type != CType("Void", "System"):
            doc_json["return"] = ""
        return self.name, doc_json

    @classmethod
    def from_json(cls, json: JsonType) -> CProperty:
        return cls(
            name=json["name"],
            declaring_type=CType.from_json(json["declaring_type"]),
            type=CType.from_json(json["type"]),
            setter=json["setter"],
            static=json["static"],
        )


@dataclass(frozen=True)
class CMethod(CMember):
    parameters: Sequence[CParameter]
    return_types: Sequence[CType]
    static: bool = False

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
            "parameters": tuple(p.to_json() for p in self.parameters),
            "return_types": tuple(r.to_json() for r in self.return_types),
            "static": self.static,
        }

    def to_doc_json(self) -> tuple[str, JsonType]:
        doc_json: dict[str, Any] = {"doc": "", "doc_formatted": {}, "exceptions": {}}
        if len(self.parameters) > 0:
            doc_json["parameters"] = {p.name: "" for p in self.parameters}
        if len(self.return_types) > 0 and self.return_types[0] != CType("Void", "System"):
            doc_json["return"] = ""
        param_types: str = ", ".join(str(p.type) for p in self.parameters)
        return f"{self.name}({param_types})", doc_json

    @classmethod
    def from_json(cls, json: JsonType) -> CMethod:
        return cls(
            name=json["name"],
            declaring_type=CType.from_json(json["declaring_type"]),
            parameters=tuple(map(CParameter.from_json, json["parameters"])),
            return_types=tuple(map(CType.from_json, json["return_types"])),
            static=json["static"],
        )


@dataclass(frozen=True)
class CEvent(CMember):
    type: CType

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
        }

    def to_doc_json(self) -> tuple[str, JsonType]:
        return self.name, {"doc": "", "doc_formatted": {}}

    @classmethod
    def from_json(cls, json: JsonType) -> CEvent:
        return cls(
            name=json["name"],
            declaring_type=CType.from_json(json["declaring_type"]),
            type=CType.from_json(json["type"]),
        )
