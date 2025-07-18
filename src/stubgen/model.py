"""Classes that represent C# object."""

from __future__ import annotations

import re
from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
from dataclasses import field
from typing import TYPE_CHECKING
from typing import Any
from typing import ClassVar
from typing import Self
from typing import override

from stubgen.log import get_logger

if TYPE_CHECKING:  # pragma: no cover
    from collections.abc import Mapping
    from collections.abc import Sequence
    from logging import Logger
    from typing import Literal

    type CompareResults = Literal[-1, 0, 1]
    type JsonType = None | int | float | str | Sequence | Mapping

logger: Logger = get_logger(__name__)


def _compare_boolean(x: bool | None, y: bool | None) -> CompareResults:  # pragma: no cover
    match x, y:
        case (None, None):
            return 0
        case (None, bool()):
            return -1
        case (bool(), None):
            return 1
        case (bool(), bool()):
            return 0 if x == y else (-1 if y else 1)
    # This should never be reached, as long as the parameter types are correct
    return 0


def _compare_string(x: str | None, y: str | None) -> CompareResults:  # pragma: no cover
    match x, y:
        case (None, None):
            return 0
        case (None, str()):
            return -1
        case (str(), None):
            return 1
        case (str(), str()):
            return 0 if x == y else (-1 if x < y else 1)
    # This should never be reached, as long as the parameter types are correct
    return 0


def _json_doc() -> dict[str, Any]:
    return {"doc": "", "doc_formatted": {}}


@dataclass(frozen=True)
class DocTree:
    """A tree data structure for representing doc-strings for C# objects."""

    name: str
    doc: str = ""
    doc_formatted: Mapping[str, Sequence[str]] = field(default_factory=dict)
    parameters: Mapping[str, str] = field(default_factory=dict)
    return_doc: str | None = None
    exceptions: Mapping[str, str] = field(default_factory=dict)
    nodes: Sequence[DocTree] = ()

    # def __getitem__(self, key, /):
    #     pass
    #
    # def __len__(self):
    #     pass
    #
    # def __iter__(self):
    #     pass

    # def get(self, key, default=None):
    #     'D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.'
    #     try:
    #         return self[key]
    #     except KeyError:
    #         return default
    #
    # def __contains__(self, key):
    #     try:
    #         self[key]
    #     except KeyError:
    #         return False
    #     else:
    #         return True
    #
    # def keys(self):
    #     "D.keys() -> a set-like object providing a view on D's keys"
    #     return KeysView(self)
    #
    # def items(self):
    #     "D.items() -> a set-like object providing a view on D's items"
    #     return ItemsView(self)
    #
    # def values(self):
    #     "D.values() -> an object providing a view on D's values"
    #     return ValuesView(self)
    #
    # def __eq__(self, other):
    #     if not isinstance(other, Mapping):
    #         return NotImplemented
    #     return dict(self.items()) == dict(other.items())


@dataclass(frozen=True, kw_only=True)
class CWrapper(ABC):
    """Base class for C# wrappers."""

    name: str

    @override
    def __str__(self) -> str:
        return self.name

    def __lt__(self, other: CWrapper) -> bool:
        """Compare two C# wrappers."""
        return self.compare(self, other) < 0

    def __le__(self, other: CWrapper) -> bool:
        """Compare two C# wrappers."""
        return self.compare(self, other) <= 0

    def __gt__(self, other: CWrapper) -> bool:
        """Compare two C# wrappers."""
        return self.compare(self, other) > 0

    def __ge__(self, other: CWrapper) -> bool:
        """Compare two C# wrappers."""
        return self.compare(self, other) >= 0

    @property
    def doc_name(self) -> str:
        """Get the simple name of the wrapped object."""
        return self.name

    @abstractmethod
    def to_json(self) -> JsonType:
        """Convert this object into a JSON compatible object."""

    @abstractmethod
    def to_doc_json(self) -> tuple[str, JsonType]:
        """Convert this object into the doc format."""

    @classmethod
    @abstractmethod
    def from_json(cls, json: JsonType) -> CNamespace:
        """Convert a JSON compatible object into a C# wrapper object."""

    @classmethod
    def compare(cls, x: Self, y: Self) -> CompareResults:
        """Compare two C# wrappers."""
        return _compare_string(x.name, y.name)

    @classmethod
    def compare_seq(cls, x: Sequence[Self], y: Sequence[Self]) -> CompareResults:
        """Compare two sequences of C# wrappers."""
        x_len: int = len(x)
        y_len: int = len(y)
        if x_len < y_len:
            return -1
        if x_len > y_len:
            return 1

        _x: Self
        _y: Self
        c: CompareResults
        for _x, _y in zip(x, y, strict=False):
            if (c := cls.compare(_x, _y)) != 0:
                return c
        return 0


@dataclass(frozen=True, kw_only=True)
class CType(CWrapper):
    """C# Type wrapper."""

    VOID: ClassVar[CType]

    namespace: str | None = None
    inner: Sequence[CType] = ()
    reference: bool = False
    generic: bool = False
    nullable: bool = False

    @override
    def __str__(self) -> str:
        return self.full_name

    @property
    def import_name(self) -> str:
        """Get the name to use when importing this CType."""
        name: str = self.name
        if self.namespace is not None:
            name = f"{self.namespace}.{name}"
        return name

    @property
    @override
    def doc_name(self) -> str:
        name: str = self.name
        if len(self.inner) > 0:
            name = f"{name}[{', '.join(t.doc_name for t in self.inner)}]"
        return name

    @property
    def full_name(self) -> str:
        """Get the full name representation of this CType."""
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

    @override
    def to_json(self) -> JsonType:
        return self.full_name

    @override
    def to_doc_json(self) -> tuple[str, JsonType]:
        raise NotImplementedError

    @classmethod
    @override
    def from_json(cls, json: JsonType) -> CType | None:
        if json is None:
            return None
        match: re.Match = re.match(
            r"(?:(\w+(?:\.\w+)*):)?(\$?\*?\w+(?:\.\w+)*\??)(?:\[(.*)])?",
            json,
        )
        name: str = match.group(2)
        inner: Sequence[CType] = ()
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

    @classmethod
    @override
    def compare(cls, x: Self, y: Self) -> CompareResults:
        c: CompareResults
        if (c := _compare_string(x.namespace, y.namespace)) != 0:
            return c
        if (c := _compare_string(x.name, y.name)) != 0:
            return c
        if (c := cls.compare_seq(x.inner, y.inner)) != 0:
            return c
        if (c := _compare_boolean(x.reference, y.reference)) != 0:
            return c
        if (c := _compare_boolean(x.generic, y.generic)) != 0:
            return c
        if (c := _compare_boolean(x.nullable, y.nullable)) != 0:
            return c
        return 0


CType.VOID = CType(name="Void", namespace="System")


@dataclass(frozen=True, kw_only=True)
class CParameter(CWrapper):
    """C# Parameter wrapper."""

    type: CType
    default: bool = False
    out: bool = False

    @override
    def to_json(self) -> JsonType:
        return {
            "name": self.name,
            "type": self.type.to_json(),
            "default": self.default,
            "out": self.out,
        }

    @override
    def to_doc_json(self) -> tuple[str, JsonType]:
        raise NotImplementedError

    @classmethod
    @override
    def from_json(cls, json: JsonType) -> CParameter:
        return cls(
            name=json["name"],
            type=CType.from_json(json["type"]),
            default=json["default"],
            out=json["out"],
        )

    @classmethod
    @override
    def compare(cls, x: Self, y: Self) -> CompareResults:
        """Compare two C# wrappers."""
        return CType.compare(x.type, y.type)


@dataclass(frozen=True, kw_only=True)
class CMember(CWrapper, ABC):
    """C# Member wrapper."""

    declaring_type: CType

    @override
    def __str__(self) -> str:
        return f"{self.declaring_type}.{self.name}"


@dataclass(frozen=True, kw_only=True)
class CField(CMember):
    """C# Field wrapper."""

    return_type: CType
    static: bool = False

    @override
    def to_json(self) -> JsonType:
        return {
            "name": self.name,
            "declaring_type": self.declaring_type.to_json(),
            "return_type": self.return_type.to_json(),
            "static": self.static,
        }

    @override
    def to_doc_json(self) -> tuple[str, JsonType]:
        doc_json: dict[str, Any] = _json_doc()
        if self.return_type is not None and self.return_type != CType.VOID:
            doc_json["return"] = ""
        return self.doc_name, doc_json

    @classmethod
    @override
    def from_json(cls, json: JsonType) -> CField:
        return cls(
            name=json["name"],
            declaring_type=CType.from_json(json["declaring_type"]),
            return_type=CType.from_json(json["return_type"]),
            static=json["static"],
        )


@dataclass(frozen=True, kw_only=True)
class CConstructor(CMember):
    """C# Constructor wrapper."""

    name: str = "__init__"
    parameters: Sequence[CParameter] = ()

    @override
    def __str__(self) -> str:
        param_types: str = ", ".join(p.type.full_name for p in self.parameters)
        return f"{self.declaring_type}.{self.name}({param_types})"

    @property
    def doc_name(self) -> str:
        """Get the name that appears when generating the doc json."""
        param_types: str = ", ".join(p.type.full_name for p in self.parameters)
        return f"{self.name}({param_types})"

    @override
    def to_json(self) -> JsonType:
        return {
            "declaring_type": self.declaring_type.to_json(),
            "parameters": tuple(p.to_json() for p in self.parameters),
        }

    @override
    def to_doc_json(self) -> tuple[str, JsonType]:
        doc_json: dict[str, Any] = _json_doc()
        if len(self.parameters) > 0:
            doc_json["parameters"] = {p.name: "" for p in self.parameters}
        return self.doc_name, doc_json

    @classmethod
    @override
    def from_json(cls, json: JsonType) -> CConstructor:
        return cls(
            declaring_type=CType.from_json(json["declaring_type"]),
            parameters=tuple(map(CParameter.from_json, json["parameters"])),
        )

    @classmethod
    @override
    def compare(cls, x: Self, y: Self) -> CompareResults:
        return CParameter.compare_seq(x.parameters, y.parameters)


@dataclass(frozen=True, kw_only=True)
class CProperty(CMember):
    """C# Property wrapper."""

    type: CType
    setter: bool = False
    static: bool = False

    @override
    def to_json(self) -> JsonType:
        return {
            "name": self.name,
            "declaring_type": self.declaring_type.to_json(),
            "type": self.type.to_json(),
            "setter": self.setter,
            "static": self.static,
        }

    @override
    def to_doc_json(self) -> tuple[str, JsonType]:
        doc_json: dict[str, Any] = _json_doc()
        if self.type is not None and self.type != CType.VOID:
            doc_json["return"] = ""
        return self.doc_name, doc_json

    @classmethod
    @override
    def from_json(cls, json: JsonType) -> CProperty:
        return cls(
            name=json["name"],
            declaring_type=CType.from_json(json["declaring_type"]),
            type=CType.from_json(json["type"]),
            setter=json["setter"],
            static=json["static"],
        )


@dataclass(frozen=True, kw_only=True)
class CMethod(CMember):
    """C# Method wrapper."""

    parameters: Sequence[CParameter] = ()
    return_types: Sequence[CType] = ()
    static: bool = False

    @override
    def __str__(self) -> str:
        param_types: str = ", ".join(p.type.full_name for p in self.parameters)
        return f"{self.declaring_type}.{self.name}({param_types})"

    @property
    def doc_name(self) -> str:
        """Get the name that appears when generating the doc json."""
        param_types: str = ", ".join(p.type.full_name for p in self.parameters)
        return f"{self.name}({param_types})"

    @override
    def to_json(self) -> JsonType:
        return {
            "name": self.name,
            "declaring_type": self.declaring_type.to_json(),
            "parameters": tuple(p.to_json() for p in self.parameters),
            "return_types": tuple(r.to_json() for r in self.return_types),
            "static": self.static,
        }

    @override
    def to_doc_json(self) -> tuple[str, JsonType]:
        doc_json: dict[str, Any] = {**_json_doc(), "exceptions": {}}
        if len(self.parameters) > 0:
            doc_json["parameters"] = {p.name: "" for p in self.parameters}
        if len(self.return_types) > 0 and self.return_types[0] != CType.VOID:
            doc_json["return"] = ""
        return self.doc_name, doc_json

    @classmethod
    @override
    def from_json(cls, json: JsonType) -> CMethod:
        return cls(
            name=json["name"],
            declaring_type=CType.from_json(json["declaring_type"]),
            parameters=tuple(map(CParameter.from_json, json["parameters"])),
            return_types=tuple(map(CType.from_json, json["return_types"])),
            static=json["static"],
        )

    @classmethod
    @override
    def compare(cls, x: Self, y: Self) -> CompareResults:
        c: CompareResults
        if (c := _compare_string(x.name, y.name)) != 0:
            return c
        if (c := CParameter.compare_seq(x.parameters, y.parameters)) != 0:
            return c
        return 0


@dataclass(frozen=True, kw_only=True)
class CEvent(CMember):
    """C# Event wrapper."""

    type: CType

    @override
    def to_json(self) -> JsonType:
        return {
            "name": self.name,
            "declaring_type": self.declaring_type.to_json(),
            "type": self.type.to_json(),
        }

    @override
    def to_doc_json(self) -> tuple[str, JsonType]:
        return self.doc_name, _json_doc()

    @classmethod
    @override
    def from_json(cls, json: JsonType) -> CEvent:
        return cls(
            name=json["name"],
            declaring_type=CType.from_json(json["declaring_type"]),
            type=CType.from_json(json["type"]),
        )


@dataclass(frozen=True, kw_only=True)
class CNamespace(CWrapper):
    """C# Namespace wrapper."""

    types: Mapping[str, CTypeDefinition] = field(default_factory=dict)

    @override
    def to_json(self) -> JsonType:
        return {
            "name": self.name,
            "types": {k: v.to_json() for k, v in self.types.items()},
        }

    @override
    def to_doc_json(self) -> tuple[str, JsonType]:
        raise NotImplementedError

    @classmethod
    @override
    def from_json(cls, json: JsonType) -> CNamespace:
        return cls(
            name=json["name"],
            types={k: CTypeDefinition.from_json(v) for k, v in json["types"].items()},
        )


@dataclass(frozen=True, kw_only=True)
class CTypeDefinition(CWrapper, ABC):
    """Base class for C# type definition wrappers."""

    namespace: str | None = None
    nested: CType | None = None

    @override
    def __str__(self) -> str:
        name: str = self.doc_name
        if self.nested is not None:
            name = f"{self.nested.full_name}.{name}"
        elif self.namespace is not None:
            name = f"{self.namespace}.{name}"
        return name

    @property
    @override
    def doc_name(self) -> str:
        name: str = super().doc_name
        generic_args: Sequence[CType] = getattr(self, "generic_args", [])
        if len(generic_args) > 0:
            generic: str = ", ".join(map(str, generic_args))
            name = f"{name}[{generic}]"
        return name

    @classmethod
    @override
    def from_json(cls, json: JsonType) -> Self:
        match json["type"]:
            case "class":
                return CClass.from_json(json)
            case "struct":
                return CStruct.from_json(json)
            case "interface":
                return CInterface.from_json(json)
            case "enum":
                return CEnum.from_json(json)
            case "delegate":
                return CDelegate.from_json(json)
        return None  # pragma: no cover


@dataclass(frozen=True, kw_only=True)
class CClass(CTypeDefinition):
    """C# Class wrapper."""

    abstract: bool = False
    generic_args: Sequence[CType] = ()
    super_class: CType | None = None
    interfaces: Sequence[CType] = ()
    fields: Mapping[str, CField] = field(default_factory=dict)
    constructors: Mapping[str, CConstructor] = field(default_factory=dict)
    properties: Mapping[str, CProperty] = field(default_factory=dict)
    methods: Mapping[str, CMethod] = field(default_factory=dict)
    events: Mapping[str, CEvent] = field(default_factory=dict)
    nested_types: Mapping[str, CTypeDefinition] = field(default_factory=dict)

    @override
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

    @override
    def to_doc_json(self) -> tuple[str, JsonType]:
        doc_json: dict[str, Any] = _json_doc()

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

        return self.doc_name, doc_json

    @classmethod
    @override
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


@dataclass(frozen=True, kw_only=True)
class CStruct(CClass):
    """C# Struct wrapper."""

    @override
    def to_json(self) -> JsonType:
        json: dict[str, Any] = dict(**super().to_json())
        json["type"] = "struct"
        return json


@dataclass(frozen=True, kw_only=True)
class CInterface(CTypeDefinition):
    """C# Interface wrapper."""

    generic_args: Sequence[CType] = ()
    interfaces: Sequence[CType] = ()
    fields: Mapping[str, CField] = field(default_factory=dict)
    properties: Mapping[str, CProperty] = field(default_factory=dict)
    methods: Mapping[str, CMethod] = field(default_factory=dict)
    events: Mapping[str, CEvent] = field(default_factory=dict)
    nested_types: Mapping[str, CTypeDefinition] = field(default_factory=dict)

    @override
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

    @override
    def to_doc_json(self) -> tuple[str, JsonType]:
        doc_json: dict[str, Any] = _json_doc()

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

        return self.doc_name, doc_json

    @classmethod
    @override
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


@dataclass(frozen=True, kw_only=True)
class CEnum(CTypeDefinition):
    """C# Enum wrapper."""

    fields: Sequence[str] = ()

    @override
    def to_json(self) -> JsonType:
        return {
            "type": "enum",
            "name": self.name,
            "namespace": self.namespace,
            "nested": None if self.nested is None else self.nested.to_json(),
            "fields": self.fields,
        }

    @override
    def to_doc_json(self) -> tuple[str, JsonType]:
        return self.doc_name, {
            "doc": "",
            "doc_formatted": {},
            **{f: {"doc": ""} for f in self.fields},
        }

    @classmethod
    @override
    def from_json(cls, json: JsonType) -> Self:
        return cls(
            name=json["name"],
            namespace=json["namespace"],
            nested=CType.from_json(json["nested"]),
            fields=tuple(json["fields"]),
        )


@dataclass(frozen=True, kw_only=True)
class CDelegate(CTypeDefinition):
    """C# Delegate wrapper."""

    parameters: Sequence[CParameter] = ()
    return_type: CType = CType.VOID

    @property
    @override
    def doc_name(self) -> str:
        param_types: str = ", ".join(p.type.full_name for p in self.parameters)
        return f"{self.name}({param_types})"

    @override
    def to_json(self) -> JsonType:
        return {
            "type": "delegate",
            "name": self.name,
            "namespace": self.namespace,
            "nested": None if self.nested is None else self.nested.to_json(),
            "parameters": tuple(p.to_json() for p in self.parameters),
            "return_type": self.return_type.to_json(),
        }

    @override
    def to_doc_json(self) -> tuple[str, JsonType]:
        doc_json: dict[str, Any] = _json_doc()
        if len(self.parameters) > 0:
            doc_json["parameters"] = {p.name: "" for p in self.parameters}
        if self.return_type is not None and self.return_type != CType.VOID:
            doc_json["return"] = ""
        return self.doc_name, doc_json

    @classmethod
    @override
    def from_json(cls, json: JsonType) -> Self:
        return cls(
            name=json["name"],
            namespace=json["namespace"],
            nested=CType.from_json(json["nested"]),
            parameters=tuple(map(CParameter.from_json, json["parameters"])),
            return_type=CType.from_json(json["return_type"]),
        )
