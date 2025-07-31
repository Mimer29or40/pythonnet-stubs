"""Classes that represent C# object."""

from __future__ import annotations

import re
from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
from dataclasses import field
from functools import partial
from textwrap import TextWrapper
from typing import TYPE_CHECKING
from typing import Any
from typing import ClassVar
from typing import Self
from typing import override

from stubgen.log import get_logger
from stubgen.util import compare_boolean
from stubgen.util import compare_string
from stubgen.util import compare_version
from stubgen.util import merge_mapping
from stubgen.util import merge_sequence
from stubgen.util import merge_string

if TYPE_CHECKING:  # pragma: no cover
    from collections.abc import Mapping
    from collections.abc import Sequence
    from logging import Logger

    from stubgen.util import CompareResults

    type JsonType = None | int | float | str | Sequence | Mapping

logger: Logger = get_logger(__name__)


@dataclass(frozen=True)
class DocTree:
    """A tree data structure for representing doc-strings for C# objects."""

    children: Sequence[DocNode] = field(default_factory=list)

    def __getitem__(self, node: str, /) -> DocNode | None:
        """Get a descendant node of this tree.

        :param node: The fully qualified name of the node to get.
        :return: The DocNode node, if it exists.
        """
        return DocTree._get_node(self.children, self._split_node_string(node))

    def to_json(self) -> JsonType:
        """Convert this DocTree into a JSON compatible object."""
        return {c.name: c.to_json() for c in self.children}

    @classmethod
    def from_json(cls, obj: JsonType) -> Self:
        """Convert a JSON object into a DocTree."""
        return DocTree(
            children=[DocNode.from_json(k, v) for k, v in obj.items()],
        )

    @classmethod
    def merge(cls, obj1: DocTree, obj2: DocTree) -> DocTree:
        """Merge two DocTrees into a single DocTree."""
        children: Mapping[str, DocNode] = merge_mapping(
            {c.name: c for c in obj1.children},
            {c.name: c for c in obj2.children},
            DocNode.merge,
        )

        return DocTree(children=sorted(children.values(), key=lambda c: c.name))

    @staticmethod
    def _get_node(children: Sequence[DocNode], nodes: Sequence[str]) -> DocNode | None:
        nodes_len: int = len(nodes)
        if nodes_len == 0:
            return None
        node: str = nodes[0]
        child: DocNode
        for child in children:
            if child.name == node:
                return child if nodes_len == 1 else DocTree._get_node(child.children, nodes[1:])
        return DocNode(nodes[-1])

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


@dataclass(frozen=True)
class DocNode:
    """A node for a tree data structure for representing doc-strings for C# objects."""

    name: str
    doc: str = ""
    doc_formatted: Mapping[str, Sequence[str]] = field(default_factory=dict)
    parameter_docs: Mapping[str, str] | None = None
    return_doc: str | None = None
    exception_docs: Mapping[str, str] | None = None
    children: Sequence[DocNode] = field(default_factory=list)

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
        """Convert this DocNode into a JSON compatible object."""
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
        child: DocNode
        for child in self.children:
            obj[child.name] = child.to_json()
        return obj

    @classmethod
    def from_json(cls, name: str, obj: JsonType) -> Self:
        """Convert a JSON object into a DocTree."""
        obj = dict(obj)
        return DocNode(
            name=name,
            doc=obj.pop("doc", ""),
            doc_formatted=obj.pop("doc_formatted", {}),
            parameter_docs=obj.pop("parameters", None),
            return_doc=obj.pop("return", None),
            exception_docs=obj.pop("exceptions", None),
            children=[DocNode.from_json(k, v) for k, v in obj.items()],
        )

    @classmethod
    def merge(cls, obj1: DocNode, obj2: DocNode) -> DocNode:
        """Merge two DocNodes into a single DocNode."""
        logger.debug("Merging DocNode %r and %r", obj1.name, obj2.name)

        doc: str = merge_string(obj1.doc, obj2.doc)

        doc_formatted: Mapping[str, Sequence[str]] = merge_mapping(
            obj1.doc_formatted,
            obj2.doc_formatted,
            partial(merge_sequence, merge_func=merge_string),
        )

        parameter_docs: Mapping[str, str] | None = merge_mapping(
            obj1.parameter_docs,
            obj2.parameter_docs,
            merge_string,
        )

        return_doc: str | None = merge_string(obj1.return_doc, obj2.return_doc)

        exception_docs: Mapping[str, str] | None = merge_mapping(
            obj1.exception_docs,
            obj2.exception_docs,
            merge_string,
        )
        if exception_docs is not None:
            exception_docs = dict(sorted(exception_docs.items()))

        children: Mapping[str, DocNode] = merge_mapping(
            {c.name: c for c in obj1.children},
            {c.name: c for c in obj2.children},
            DocNode.merge,
        )

        return DocNode(
            name=obj1.name,
            doc=doc,
            doc_formatted=doc_formatted,
            parameter_docs=parameter_docs,
            return_doc=return_doc,
            exception_docs=exception_docs,
            children=sorted(children.values(), key=lambda c: c.name),
        )


class DocNodeMixin(ABC):
    """A mixin for objects that can provide DocNoes."""

    @abstractmethod
    def doc_node(self) -> DocNode:
        """Convert this object into a DocNode."""


class MergeMixin(ABC):
    """A mixin for objects that can be merged."""

    @classmethod
    @abstractmethod
    def merge(cls, obj1: Self, obj2: Self) -> Self:
        """Merge two objects into a one."""


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

    @classmethod
    @abstractmethod
    def from_json(cls, json: JsonType) -> Self:
        """Convert a JSON compatible object into a C# wrapper object."""

    @classmethod
    def compare(cls, x: Self, y: Self) -> CompareResults:
        """Compare two C# wrappers."""
        return compare_string(x.name, y.name)

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
    inner: Sequence[CType] = field(default_factory=list)
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

    @classmethod
    @override
    def from_json(cls, json: JsonType) -> Self | None:
        if json is None:
            return None
        match: re.Match = re.match(
            r"(?:(\w+(?:\.\w+)*):)?(\$?\*?\w+(?:\.\w+)*\??)(?:\[(.*)])?",
            json,
        )
        name: str = match.group(2)
        inner: Sequence[CType] = []
        if (inner_str := match.group(3)) is not None:
            inner = list(map(CType.from_json, inner_str.split(", ")))
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
        if (c := compare_string(x.namespace, y.namespace)) != 0:
            return c
        if (c := compare_string(x.name, y.name)) != 0:
            return c
        if (c := cls.compare_seq(x.inner, y.inner)) != 0:
            return c
        if (c := compare_boolean(x.reference, y.reference)) != 0:
            return c
        if (c := compare_boolean(x.generic, y.generic)) != 0:
            return c
        if (c := compare_boolean(x.nullable, y.nullable)) != 0:
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

    @classmethod
    @override
    def from_json(cls, json: JsonType) -> Self:
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
class CMember(CWrapper, DocNodeMixin, ABC):
    """C# Member wrapper."""

    declaring_type: CType


@dataclass(frozen=True, kw_only=True)
class CField(CMember):
    """C# Field wrapper."""

    return_type: CType
    # TODO(Ryan): Check for readonly to influence Final or not
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
    def doc_node(self) -> DocNode:
        return_doc: str | None = None
        if self.return_type is not None and self.return_type != CType.VOID:
            return_doc = ""
        return DocNode(name=self.unique_name, return_doc=return_doc)

    @classmethod
    @override
    def from_json(cls, json: JsonType) -> Self:
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
    parameters: Sequence[CParameter] = field(default_factory=list)

    @property
    def unique_name(self) -> str:
        """Get the name that appears when generating the doc json."""
        param_types: str = ", ".join(p.type.full_name for p in self.parameters)
        return f"{self.name}({param_types})"

    @override
    def to_json(self) -> JsonType:
        return {
            "declaring_type": self.declaring_type.to_json(),
            "parameters": [p.to_json() for p in self.parameters],
        }

    @override
    def doc_node(self) -> DocNode:
        parameter_docs: Mapping[str, str] | None = None
        if len(self.parameters) > 0:
            parameter_docs = {p.name: "" for p in self.parameters}
        return DocNode(name=self.unique_name, parameter_docs=parameter_docs)

    @classmethod
    @override
    def from_json(cls, json: JsonType) -> Self:
        return cls(
            declaring_type=CType.from_json(json["declaring_type"]),
            parameters=list(map(CParameter.from_json, json["parameters"])),
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
    def doc_node(self) -> DocNode:
        return_doc: str | None = None
        if self.type is not None and self.type != CType.VOID:
            return_doc = ""
        return DocNode(name=self.unique_name, return_doc=return_doc)

    @classmethod
    @override
    def from_json(cls, json: JsonType) -> Self:
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

    parameters: Sequence[CParameter] = field(default_factory=list)
    return_types: Sequence[CType] = field(default_factory=list)
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
            "parameters": [p.to_json() for p in self.parameters],
            "return_types": [r.to_json() for r in self.return_types],
            "static": self.static,
        }

    @override
    def doc_node(self) -> DocNode:
        parameter_docs: Mapping[str, str] | None = None
        if len(self.parameters) > 0:
            parameter_docs = {p.name: "" for p in self.parameters}
        return_doc: str | None = None
        if len(self.return_types) > 0 and self.return_types[0] != CType.VOID:
            return_doc = ""
        return DocNode(
            name=self.unique_name,
            parameter_docs=parameter_docs,
            return_doc=return_doc,
            exception_docs={},
        )

    @classmethod
    @override
    def from_json(cls, json: JsonType) -> Self:
        return cls(
            name=json["name"],
            declaring_type=CType.from_json(json["declaring_type"]),
            parameters=list(map(CParameter.from_json, json["parameters"])),
            return_types=list(map(CType.from_json, json["return_types"])),
            static=json["static"],
        )

    @classmethod
    @override
    def compare(cls, x: Self, y: Self) -> CompareResults:
        c: CompareResults
        if (c := compare_string(x.name, y.name)) != 0:
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
    def doc_node(self) -> DocNode:
        return DocNode(name=self.unique_name)

    @classmethod
    @override
    def from_json(cls, json: JsonType) -> Self:
        return cls(
            name=json["name"],
            declaring_type=CType.from_json(json["declaring_type"]),
            type=CType.from_json(json["type"]),
        )


@dataclass(frozen=True, kw_only=True)
class CTypeDefinition(CWrapper, DocNodeMixin, MergeMixin, ABC):
    """Base class for C# type definition wrappers."""

    namespace: str | None = None
    parent: CType | None = None

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
            case "interface":
                return CInterface.from_json(json)
            case "enum":
                return CEnum.from_json(json)
            case "delegate":
                return CDelegate.from_json(json)
        raise NotImplementedError  # pragma: no cover

    @classmethod
    @override
    def merge(cls, obj1: Self, obj2: Self) -> Self:
        match obj1, obj2:
            case CClass(), CClass():
                return CClass.merge(obj1, obj2)
            case CInterface(), CInterface():
                return CInterface.merge(obj1, obj2)
            case CEnum(), CEnum():
                return CEnum.merge(obj1, obj2)
            case CDelegate(), CDelegate():
                return CDelegate.merge(obj1, obj2)
        raise TypeError(
            f"Type definitions are not the same: {type(obj1)} != {type(obj2)}"
        )  # pragma: no cover


@dataclass(frozen=True, kw_only=True)
class CClass(CTypeDefinition):
    """C# Class wrapper."""

    abstract: bool = False
    generic_args: Sequence[CType] = field(default_factory=list)
    super_class: CType | None = None
    interfaces: Sequence[CType] = field(default_factory=list)
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
            "parent": None if self.parent is None else self.parent.to_json(),
            "abstract": self.abstract,
            "generic_args": [a.to_json() for a in self.generic_args],
            "super_class": None if self.super_class is None else self.super_class.to_json(),
            "interfaces": sorted(i.to_json() for i in self.interfaces),
            "fields": {k: v.to_json() for k, v in self.fields.items()},
            "constructors": {k: v.to_json() for k, v in self.constructors.items()},
            "properties": {k: v.to_json() for k, v in self.properties.items()},
            "methods": {k: v.to_json() for k, v in self.methods.items()},
            "events": {k: v.to_json() for k, v in self.events.items()},
            "nested_types": {k: v.to_json() for k, v in self.nested_types.items()},
        }

    @override
    def doc_node(self) -> DocNode:
        members: Sequence[CMember] = (
            *self.fields.values(),
            *self.constructors.values(),
            *self.properties.values(),
            *self.methods.values(),
            *self.events.values(),
        )
        return DocNode(
            self.unique_name,
            children=[
                *(m.doc_node() for m in members if m.declaring_type.name == self.name),
                *(c.doc_node() for c in self.nested_types.values()),
            ],
        )

    @classmethod
    @override
    def from_json(cls, json: JsonType) -> Self:
        return cls(
            name=json["name"],
            namespace=json["namespace"],
            parent=CType.from_json(json["parent"]),
            abstract=json["abstract"],
            generic_args=list(map(CType.from_json, json["generic_args"])),
            super_class=CType.from_json(json["super_class"]),
            interfaces=list(map(CType.from_json, json["interfaces"])),
            fields={k: CField.from_json(v) for k, v in json["fields"].items()},
            constructors={k: CConstructor.from_json(v) for k, v in json["constructors"].items()},
            properties={k: CProperty.from_json(v) for k, v in json["properties"].items()},
            methods={k: CMethod.from_json(v) for k, v in json["methods"].items()},
            events={k: CEvent.from_json(v) for k, v in json["events"].items()},
            nested_types={k: CTypeDefinition.from_json(v) for k, v in json["nested_types"].items()},
        )

    @classmethod
    @override
    def merge(cls, obj1: Self, obj2: Self) -> Self:
        logger.debug("Merging CClasses %r and %r", obj1.name, obj2.name)

        def first[T: CWrapper](o1: T, _: T) -> T:  # pragma: no cover
            return o1

        interfaces: Sequence[CType] = merge_sequence(obj1.interfaces, obj2.interfaces, first)
        fields: Mapping[str, CField] = merge_mapping(
            obj1.fields,
            obj2.fields,
            first,
        )
        constructors: Mapping[str, CConstructor] = merge_mapping(
            obj1.constructors,
            obj2.constructors,
            first,
        )
        properties: Mapping[str, CProperty] = merge_mapping(
            obj1.properties,
            obj2.properties,
            first,
        )
        methods: Mapping[str, CMethod] = merge_mapping(
            obj1.methods,
            obj2.methods,
            first,
        )
        events: Mapping[str, CEvent] = merge_mapping(
            obj1.events,
            obj2.events,
            first,
        )
        nested_types: Mapping[str, CTypeDefinition] = merge_mapping(
            obj1.nested_types,
            obj2.nested_types,
            CTypeDefinition.merge,
        )

        return CClass(
            name=obj1.name,
            namespace=obj1.namespace,
            parent=obj1.parent,
            abstract=obj1.abstract,
            generic_args=obj1.generic_args,
            super_class=obj1.super_class,
            interfaces=sorted(interfaces),
            fields=dict(sorted(fields.items())),
            constructors=dict(sorted(constructors.items())),
            properties=dict(sorted(properties.items())),
            methods=dict(sorted(methods.items())),
            events=dict(sorted(events.items())),
            nested_types=dict(sorted(nested_types.items())),
        )


@dataclass(frozen=True, kw_only=True)
class CInterface(CTypeDefinition):
    """C# Interface wrapper."""

    generic_args: Sequence[CType] = field(default_factory=list)
    interfaces: Sequence[CType] = field(default_factory=list)
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
            "parent": None if self.parent is None else self.parent.to_json(),
            "generic_args": [a.to_json() for a in self.generic_args],
            "interfaces": sorted(i.to_json() for i in self.interfaces),
            "fields": {k: v.to_json() for k, v in self.fields.items()},
            "properties": {k: v.to_json() for k, v in self.properties.items()},
            "methods": {k: v.to_json() for k, v in self.methods.items()},
            "events": {k: v.to_json() for k, v in self.events.items()},
            "nested_types": {k: v.to_json() for k, v in self.nested_types.items()},
        }

    @override
    def doc_node(self) -> DocNode:
        members: Sequence[CMember] = (
            *self.fields.values(),
            *self.properties.values(),
            *self.methods.values(),
            *self.events.values(),
        )
        return DocNode(
            self.unique_name,
            children=[
                *(m.doc_node() for m in members if m.declaring_type.name == self.name),
                *(c.doc_node() for c in self.nested_types.values()),
            ],
        )

    @classmethod
    @override
    def from_json(cls, json: JsonType) -> Self:
        return cls(
            name=json["name"],
            namespace=json["namespace"],
            parent=CType.from_json(json["parent"]),
            generic_args=sorted(map(CType.from_json, json["generic_args"])),
            interfaces=list(map(CType.from_json, json["interfaces"])),
            fields={k: CField.from_json(v) for k, v in json["fields"].items()},
            properties={k: CProperty.from_json(v) for k, v in json["properties"].items()},
            methods={k: CMethod.from_json(v) for k, v in json["methods"].items()},
            events={k: CEvent.from_json(v) for k, v in json["events"].items()},
            nested_types={k: CTypeDefinition.from_json(v) for k, v in json["nested_types"].items()},
        )

    @classmethod
    @override
    def merge(cls, obj1: Self, obj2: Self) -> Self:
        logger.debug("Merging CInterfaces %r and %r", obj1.name, obj2.name)

        def first[T: CWrapper](o1: T, _: T) -> T:  # pragma: no cover
            return o1

        interfaces: Sequence[CType] = merge_sequence(obj1.interfaces, obj2.interfaces, first)
        fields: Mapping[str, CField] = merge_mapping(
            obj1.fields,
            obj2.fields,
            first,
        )
        properties: Mapping[str, CProperty] = merge_mapping(
            obj1.properties,
            obj2.properties,
            first,
        )
        methods: Mapping[str, CMethod] = merge_mapping(
            obj1.methods,
            obj2.methods,
            first,
        )
        events: Mapping[str, CEvent] = merge_mapping(
            obj1.events,
            obj2.events,
            first,
        )
        nested_types: Mapping[str, CTypeDefinition] = merge_mapping(
            obj1.nested_types,
            obj2.nested_types,
            CTypeDefinition.merge,
        )

        return CInterface(
            name=obj1.name,
            namespace=obj1.namespace,
            parent=obj1.parent,
            generic_args=obj1.generic_args,
            interfaces=sorted(interfaces),
            fields=dict(sorted(fields.items())),
            properties=dict(sorted(properties.items())),
            methods=dict(sorted(methods.items())),
            events=dict(sorted(events.items())),
            nested_types=dict(sorted(nested_types.items())),
        )


@dataclass(frozen=True, kw_only=True)
class CEnum(CTypeDefinition):
    """C# Enum wrapper."""

    fields: Sequence[str] = field(default_factory=list)

    @override
    def to_json(self) -> JsonType:
        return {
            "type": "enum",
            "name": self.name,
            "namespace": self.namespace,
            "parent": None if self.parent is None else self.parent.to_json(),
            "fields": self.fields,
        }

    @override
    def doc_node(self) -> DocNode:
        return DocNode(
            self.unique_name,
            children=[DocNode(f) for f in self.fields],
        )

    @classmethod
    @override
    def from_json(cls, json: JsonType) -> Self:
        return cls(
            name=json["name"],
            namespace=json["namespace"],
            parent=CType.from_json(json["parent"]),
            fields=list(json["fields"]),
        )

    @classmethod
    @override
    def merge(cls, obj1: Self, obj2: Self) -> Self:
        logger.debug("Merging CEnums %r and %r", obj1.name, obj2.name)

        return CEnum(
            name=obj1.name,
            namespace=obj1.namespace,
            parent=obj1.parent,
            fields=obj1.fields,
        )


@dataclass(frozen=True, kw_only=True)
class CDelegate(CTypeDefinition):
    """C# Delegate wrapper."""

    parameters: Sequence[CParameter] = field(default_factory=list)
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
            "parent": None if self.parent is None else self.parent.to_json(),
            "parameters": [p.to_json() for p in self.parameters],
            "return_type": self.return_type.to_json(),
        }

    @override
    def doc_node(self) -> DocNode:
        parameter_docs: Mapping[str, str] | None = None
        if len(self.parameters) > 0:
            parameter_docs = {p.name: "" for p in self.parameters}
        return_doc: str | None = None
        if self.return_type is not None and self.return_type != CType.VOID:
            return_doc = ""
        return DocNode(self.unique_name, parameter_docs=parameter_docs, return_doc=return_doc)

    @classmethod
    @override
    def from_json(cls, json: JsonType) -> Self:
        return cls(
            name=json["name"],
            namespace=json["namespace"],
            parent=CType.from_json(json["parent"]),
            parameters=list(map(CParameter.from_json, json["parameters"])),
            return_type=CType.from_json(json["return_type"]),
        )

    @classmethod
    @override
    def merge(cls, obj1: Self, obj2: Self) -> Self:
        logger.debug("Merging CDelegates %r and %r", obj1.name, obj2.name)

        return CDelegate(
            name=obj1.name,
            namespace=obj1.namespace,
            parent=obj1.parent,
            parameters=obj1.parameters,
            return_type=obj1.return_type,
        )


@dataclass(frozen=True, kw_only=True)
class CNamespace(CWrapper, DocNodeMixin, MergeMixin):
    """C# Namespace wrapper."""

    types: Mapping[str, CTypeDefinition] = field(default_factory=dict)

    @override
    def to_json(self) -> JsonType:
        return {
            "name": self.name,
            "types": {k: v.to_json() for k, v in self.types.items()},
        }

    @override
    def doc_node(self) -> DocNode:
        return DocNode(
            self.unique_name.split(".")[-1],
            children=[t.doc_node() for t in self.types.values()],
        )

    @classmethod
    @override
    def from_json(cls, json: JsonType) -> Self:
        return cls(
            name=json["name"],
            types={k: CTypeDefinition.from_json(v) for k, v in json["types"].items()},
        )

    @classmethod
    @override
    def merge(cls, obj1: Self, obj2: Self) -> Self:
        logger.debug("Merging CNamespaces %r and %r", obj1.name, obj2.name)

        return CNamespace(
            name=obj1.name,
            types=dict(
                sorted(
                    merge_mapping(
                        obj1.types,
                        obj2.types,
                        CTypeDefinition.merge,
                    ).items(),
                )
            ),
        )


@dataclass(frozen=True)
class CAssembly(CWrapper):
    """C# Assembly wrapper."""

    version: str
    namespaces: Mapping[str, CNamespace] = field(default_factory=dict)

    @override
    def to_json(self) -> JsonType:
        return {
            "name": self.name,
            "version": self.version,
            "namespaces": {k: v.to_json() for k, v in self.namespaces.items()},
        }

    def doc_tree(self) -> DocTree:
        """Create a DocTree for this CAssembly."""
        # This will have to handle deep namespaces A.B.C
        # TODO(Ryan): Do this

    @classmethod
    @override
    def from_json(cls, json: JsonType) -> Self:
        return cls(
            name=json["name"],
            version=json["version"],
            namespaces={k: CNamespace.from_json(v) for k, v in json["namespaces"].items()},
        )

    @classmethod
    @override
    def compare(cls, x: Self, y: Self) -> CompareResults:
        c: CompareResults
        if (c := compare_string(x.name, y.name)) != 0:
            return c
        if (c := compare_version(x.version, y.version)) != 0:
            return c
        return 0
