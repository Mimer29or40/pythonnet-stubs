"""Classes that represent C# object."""

from __future__ import annotations

import re
from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
from dataclasses import field
from textwrap import TextWrapper
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


@dataclass(frozen=True)
class DocTree:
    """A tree data structure for representing doc-strings for C# objects."""

    name: str
    doc: str = ""
    doc_formatted: Mapping[str, Sequence[str]] = field(default_factory=dict)
    parameter_docs: Mapping[str, str] | None = None
    return_doc: str | None = None
    exception_docs: Mapping[str, str] | None = None
    children: Sequence[DocTree] = ()

    def __getitem__(self, node: str, /) -> DocTree | None:
        """Get a descendant node of this tree.

        :param node: The fully qualified name of the node to get.
        :return: The DocTree node, if it exists.
        """
        return self._get(self._split_node_string(node))

    def _get(self, nodes: Sequence[str]) -> DocTree | None:
        nodes_len: int = len(nodes)
        if nodes_len == 0:
            return None
        node: str = nodes[0]
        child: DocTree
        for child in self.children:
            if child.name == node:
                return child if nodes_len == 1 else child._get(nodes[1:])  # noqa: SLF001
        return None

    @staticmethod
    def _split_node_string(string: str) -> Sequence[str]:
        result: list[str] = []
        i: int
        s: str
        brackets: int = 0
        start: int = 0
        for i, s in enumerate(string):
            match s:
                case "." | ":" if brackets == 0:
                    result.append(string[start:i])
                    start = i + 1
                case "[" | "(":
                    brackets += 1
                case "]" | ")":
                    brackets -= 1
        if start != len(string):
            result.append(string[start:])
        return result

    def doc_string(self, line_length: int, indent: int = 0) -> Sequence[str]:  # noqa: C901
        """Generate a doc-string sequence for this tree."""
        indent_str: str = "    " * indent

        params: list[str] = []
        if self.parameter_docs is not None:
            params = [f":param {k}: {v}" for k, v in self.parameter_docs.items()]
        exceptions: list[str] = []
        if self.exception_docs is not None:
            exceptions = [f":except {k}: {v}" for k, v in self.exception_docs.items()]

        simple_doc: bool = len(params) == 0 and self.return_doc is None and len(exceptions) == 0

        if simple_doc and "\n" not in self.doc:
            line: str = f'{indent_str}"""{self.doc}"""'
            if len(line) > line_length:
                line += "   # noqa: E501"
            return [line]

        result: list[str] = []
        doc_wrapper: TextWrapper = TextWrapper(
            width=line_length,
            initial_indent=indent_str,
            subsequent_indent=indent_str,
        )
        paragraph: str
        for paragraph in f'"""{self.doc.replace("\n", "\n\n")}'.splitlines():
            if paragraph == "":
                result.append("")
            else:
                result.extend(doc_wrapper.wrap(paragraph))

        if not simple_doc:
            result.append("")

            extra_wrapper: TextWrapper = TextWrapper(
                width=line_length,
                initial_indent=indent_str,
                subsequent_indent=f"{indent_str}  ",
            )

            param: str
            for param in params:
                result.extend(extra_wrapper.wrap(param))

            if self.return_doc is not None:
                result.extend(extra_wrapper.wrap(f":return: {self.return_doc}"))

            exception: str
            for exception in exceptions:
                result.extend(extra_wrapper.wrap(exception))

        if len(self.doc_formatted) > 0:
            line_index: int = 0
            while line_index < len(result):
                line: str = result[line_index]
                for replace_str, replace_seq in self.doc_formatted.items():
                    replace_str = f"%{replace_str}%"
                    if replace_str in line:
                        result[line_index] = line.replace(replace_str, replace_seq[0])
                        for new_line in reversed(replace_seq[1:]):
                            result.insert(line_index + 1, indent_str + new_line)
                line_index += 1

        result.append(f'{indent_str}"""')
        return result

    def to_json(self) -> JsonType:
        """Convert this DocTree into a JSON compatible object."""
        obj: dict[str, Any] = {
            "doc": self.doc,
            "doc_formatted": self.doc_formatted,
        }
        if self.parameter_docs is not None:
            obj["parameters"] = self.parameter_docs
        if self.return_doc is not None:
            obj["return"] = self.return_doc
        if self.exception_docs is not None:
            obj["exceptions"] = self.exception_docs
        child: DocTree
        for child in self.children:
            obj[child.name] = child.to_json()
        return obj

    @classmethod
    def from_json(cls, name: str, obj: JsonType) -> Self:
        """Convert a JSON object into a DocTree."""
        obj = dict(obj)

        doc: str = obj.pop("doc", "")
        doc_formatted: Mapping[str, Sequence[str]] = obj.pop("doc_formatted", {})
        parameter_docs: Mapping[str, str] | None = obj.pop("parameters", None)
        return_doc: str | None = obj.pop("return", None)
        exception_docs: Mapping[str, str] | None = obj.pop("exceptions", None)
        children: Sequence[DocTree] = tuple(DocTree.from_json(k, v) for k, v in obj.items())

        return DocTree(
            name,
            doc=doc,
            doc_formatted=doc_formatted,
            parameter_docs=parameter_docs,
            return_doc=return_doc,
            exception_docs=exception_docs,
            children=children,
        )


@dataclass(frozen=True)
class ImportList:
    """A data structure that holds imports for a stub file."""

    EVENT_TYPE: ClassVar[str] = "--[EVENT_TYPE]--"

    types: set[str] = field(default_factory=set)

    def add_type(self, obj: CType) -> None:
        """Add a type to the import list."""
        if obj.generic:
            # No longer need to declare TypeVar.
            return
        self.types.add(obj.import_name)
        inner: CType
        for inner in obj.inner:
            self.add_type(inner)

    def add_event_type(self) -> None:
        """Add EventType to the import list."""
        self.types.add(self.EVENT_TYPE)

    def build(self, namespace: str) -> Sequence[str]:
        """Build a sequence of import strings."""
        lines: list[str] = []
        # TODO(Ryan): Move this to build_stubs

        import_event_type: bool = False

        import_name: str
        for import_name in sorted(self.types):
            if import_name == self.EVENT_TYPE:
                import_event_type = True

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


@dataclass(frozen=True, kw_only=True)
class CWrapper(ABC):
    """Base class for C# wrappers."""

    name: str

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
    def unique_name(self) -> str:
        """Get the simple name of the wrapped object."""
        return self.name

    @abstractmethod
    def to_json(self) -> JsonType:
        """Convert this object into a JSON compatible object."""

    @abstractmethod
    def to_doc_tree(self) -> DocTree:
        """Convert this object into a DocTree."""

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

    @property
    def import_name(self) -> str:
        """Get the name to use when importing this CType."""
        name: str = self.name
        if self.namespace is not None:
            name = f"{self.namespace}.{name}"
        return name

    @property
    @override
    def unique_name(self) -> str:
        name: str = self.name
        if len(self.inner) > 0:
            name = f"{name}[{', '.join(t.unique_name for t in self.inner)}]"
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
            name = f"{name}[{', '.join(t.full_name for t in self.inner)}]"
        return name

    @override
    def to_json(self) -> JsonType:
        return self.full_name

    @override
    def to_doc_tree(self) -> DocTree:
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
    def to_doc_tree(self) -> DocTree:
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
    def to_doc_tree(self) -> DocTree:
        return_doc: str | None = None
        if self.return_type is not None and self.return_type != CType.VOID:
            return_doc = ""
        return DocTree(name=self.unique_name, return_doc=return_doc)

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

    @property
    def unique_name(self) -> str:
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
    def to_doc_tree(self) -> DocTree:
        parameter_docs: Mapping[str, str] | None = None
        if len(self.parameters) > 0:
            parameter_docs = {p.name: "" for p in self.parameters}
        return DocTree(name=self.unique_name, parameter_docs=parameter_docs)

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
    def to_doc_tree(self) -> DocTree:
        return_doc: str | None = None
        if self.type is not None and self.type != CType.VOID:
            return_doc = ""
        return DocTree(name=self.unique_name, return_doc=return_doc)

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

    @property
    def unique_name(self) -> str:
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
    def to_doc_tree(self) -> DocTree:
        parameter_docs: Mapping[str, str] | None = None
        if len(self.parameters) > 0:
            parameter_docs = {p.name: "" for p in self.parameters}
        return_doc: str | None = None
        if len(self.return_types) > 0 and self.return_types[0] != CType.VOID:
            return_doc = ""
        return DocTree(
            name=self.unique_name,
            parameter_docs=parameter_docs,
            return_doc=return_doc,
            exception_docs={},
        )

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
    def to_doc_tree(self) -> DocTree:
        return DocTree(name=self.unique_name)

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
    def to_doc_tree(self) -> DocTree:
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

    @property
    @override
    def unique_name(self) -> str:
        name: str = super().unique_name
        generic_args: Sequence[CType] = getattr(self, "generic_args", [])
        if len(generic_args) > 0:
            generic: str = ", ".join(t.full_name for t in generic_args)
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
    def to_doc_tree(self) -> DocTree:
        members: Sequence[CMember] = (
            *self.fields.values(),
            *self.constructors.values(),
            *self.properties.values(),
            *self.methods.values(),
            *self.events.values(),
        )
        return DocTree(
            self.unique_name,
            children=(
                *(m.to_doc_tree() for m in members if m.declaring_type.name == self.name),
                *(c.to_doc_tree() for c in self.nested_types.values()),
            ),
        )

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
    def to_doc_tree(self) -> DocTree:
        members: Sequence[CMember] = (
            *self.fields.values(),
            *self.properties.values(),
            *self.methods.values(),
            *self.events.values(),
        )
        return DocTree(
            self.unique_name,
            children=(
                *(m.to_doc_tree() for m in members if m.declaring_type.name == self.name),
                *(c.to_doc_tree() for c in self.nested_types.values()),
            ),
        )

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
    def to_doc_tree(self) -> DocTree:
        return DocTree(
            self.unique_name,
            children=tuple(DocTree(f) for f in self.fields),
        )

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
    def unique_name(self) -> str:
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
    def to_doc_tree(self) -> DocTree:
        parameter_docs: Mapping[str, str] | None = None
        if len(self.parameters) > 0:
            parameter_docs = {p.name: "" for p in self.parameters}
        return_doc: str | None = None
        if self.return_type is not None and self.return_type != CType.VOID:
            return_doc = ""
        return DocTree(self.unique_name, parameter_docs=parameter_docs, return_doc=return_doc)

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
