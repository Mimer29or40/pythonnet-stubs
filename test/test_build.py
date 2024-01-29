import unittest
from pathlib import Path
from typing import Any
from typing import Mapping
from typing import Sequence
from typing import Set

from test_base import TestBase

from stubgen.build_stubs import Doc
from stubgen.build_stubs import Imports
from stubgen.build_stubs import build_class
from stubgen.build_stubs import build_constructor
from stubgen.build_stubs import build_delegate
from stubgen.build_stubs import build_enum
from stubgen.build_stubs import build_event
from stubgen.build_stubs import build_field
from stubgen.build_stubs import build_interface
from stubgen.build_stubs import build_method
from stubgen.build_stubs import build_property
from stubgen.build_stubs import build_struct
from stubgen.build_stubs import build_stubs
from stubgen.build_stubs import merge_doc
from stubgen.build_stubs import merge_namespace
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


class TestMergeNamespace(TestBase):
    def test_name_mismatch(self) -> None:
        namespace1: CNamespace = CNamespace(name="NamespaceA", types={})
        namespace2: CNamespace = CNamespace(name="NamespaceB", types={})

        self.assertRaises(NameError, lambda: merge_namespace(namespace1, namespace2))

    def test_merge_empty(self) -> None:
        namespace1: CNamespace = CNamespace(
            name="Namespace",
            types={},
        )
        namespace2: CNamespace = CNamespace(
            name="Namespace",
            types={},
        )

        merged: CNamespace = merge_namespace(namespace1, namespace2)
        manual: CNamespace = CNamespace(
            name="Namespace",
            types={},
        )

        self.assertEqual(manual, merged)

    def test_merge_simple(self) -> None:
        namespace1: CNamespace = CNamespace(
            name="Namespace",
            types={
                "Namespace:ClassA": CClass(
                    name="ClassA",
                    namespace="Namespace",
                    nested=None,
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
            },
        )
        namespace2: CNamespace = CNamespace(
            name="Namespace",
            types={
                "Namespace:ClassB": CClass(
                    name="ClassB",
                    namespace="Namespace",
                    nested=None,
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
            },
        )

        merged: CNamespace = merge_namespace(namespace1, namespace2)
        manual: CNamespace = CNamespace(
            name="Namespace",
            types={
                "Namespace:ClassA": CClass(
                    name="ClassA",
                    namespace="Namespace",
                    nested=None,
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "Namespace:ClassB": CClass(
                    name="ClassB",
                    namespace="Namespace",
                    nested=None,
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
            },
        )

        self.assertEqual(manual, merged)

    def test_merge_simple_rev(self) -> None:
        namespace1: CNamespace = CNamespace(
            name="Namespace",
            types={
                "Namespace:ClassB": CClass(
                    name="ClassB",
                    namespace="Namespace",
                    nested=None,
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
            },
        )
        namespace2: CNamespace = CNamespace(
            name="Namespace",
            types={
                "Namespace:ClassA": CClass(
                    name="ClassA",
                    namespace="Namespace",
                    nested=None,
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
            },
        )

        merged: CNamespace = merge_namespace(namespace1, namespace2)
        manual: CNamespace = CNamespace(
            name="Namespace",
            types={
                "Namespace:ClassA": CClass(
                    name="ClassA",
                    namespace="Namespace",
                    nested=None,
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "Namespace:ClassB": CClass(
                    name="ClassB",
                    namespace="Namespace",
                    nested=None,
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
            },
        )

        self.assertEqual(manual, merged)

    def test_merge_overlap(self) -> None:
        namespace1: CNamespace = CNamespace(
            name="Namespace",
            types={
                "Namespace:ClassA": CClass(
                    name="ClassA",
                    namespace="Namespace",
                    nested=None,
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
            },
        )
        namespace2: CNamespace = CNamespace(
            name="Namespace",
            types={
                "Namespace:ClassA": CClass(
                    name="ClassA",
                    namespace="Namespace",
                    nested=None,
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
            },
        )

        merged: CNamespace = merge_namespace(namespace1, namespace2)
        manual: CNamespace = CNamespace(
            name="Namespace",
            types={
                "Namespace:ClassA": CClass(
                    name="ClassA",
                    namespace="Namespace",
                    nested=None,
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
            },
        )

        self.assertEqual(manual, merged)


class TestImports(TestBase):
    def test_add_py_type(self) -> None:
        imports = Imports()
        imports.add_py_type("namespaceA.TypeA")
        imports.add_py_type("namespaceA.TypeA")
        imports.add_py_type("namespaceA.TypeB")
        imports.add_py_type("namespaceB.TypeA")
        imports.add_py_type("namespaceB.TypeA")
        imports.add_py_type("namespaceB.TypeB")

        manual: Set[str] = {
            "namespaceA.TypeA",
            "namespaceA.TypeB",
            "namespaceB.TypeA",
            "namespaceB.TypeB",
        }

        self.assertEqual(manual, imports.py)

    def test_add_c_type(self) -> None:
        imports = Imports()
        imports.add_c_type(CType(name="TypeA", namespace="NamespaceA"))
        imports.add_c_type(CType(name="TypeA", namespace="NamespaceA"))
        imports.add_c_type(CType(name="TypeB", namespace="NamespaceA"))
        imports.add_c_type(CType(name="TypeA", namespace="NamespaceB"))
        imports.add_c_type(CType(name="TypeA", namespace="NamespaceB"))
        imports.add_c_type(CType(name="TypeB", namespace="NamespaceB"))

        manual: Set[str] = {
            "NamespaceA.TypeA",
            "NamespaceA.TypeB",
            "NamespaceB.TypeA",
            "NamespaceB.TypeB",
        }

        self.assertEqual(manual, imports.c)

    def test_add_c_type_inner(self) -> None:
        imports = Imports()
        imports.add_c_type(
            CType(
                name="Type",
                namespace="Namespace",
                inner=(CType(name="InnerA", namespace="Namespace"),),
            )
        )
        imports.add_c_type(
            CType(
                name="Type",
                namespace="Namespace",
                inner=(CType(name="InnerB", namespace="Namespace"),),
            )
        )

        manual: Set[str] = {"Namespace.Type", "Namespace.InnerA", "Namespace.InnerB"}

        self.assertEqual(manual, imports.c)

    def test_add_c_type_type_var(self) -> None:
        imports = Imports()
        imports.add_c_type(CType(name="T", namespace="Namespace", generic=True))
        imports.add_c_type(CType(name="U", namespace="Namespace", generic=True))
        imports.add_c_type(CType(name="V", namespace="Namespace", generic=True))

        manual: Set[str] = {"T", "U", "V"}

        self.assertEqual(set(), imports.c)
        self.assertEqual(manual, imports.type_vars)

    def test_build_empty(self) -> None:
        imports = Imports()

        lines: Sequence[str] = imports.build("Namespace")
        manual: Sequence[str] = ()

        self.assertEqual(manual, lines)

    def test_build_py(self) -> None:
        imports = Imports()
        imports.add_py_type("namespace.TypeA")
        imports.add_py_type("namespace.TypeB")
        imports.add_py_type("namespace.TypeC")
        imports.add_py_type("namespace.TypeD")

        lines: Sequence[str] = imports.build()
        manual: Sequence[str] = (
            "from namespace import TypeA",
            "from namespace import TypeB",
            "from namespace import TypeC",
            "from namespace import TypeD",
        )

        self.assertEqual(manual, lines)

    def test_build_c(self) -> None:
        imports = Imports()
        imports.add_c_type(CType(name="TypeA", namespace="Namespace"))
        imports.add_c_type(CType(name="TypeB", namespace="Namespace"))
        imports.add_c_type(CType(name="TypeC", namespace="Namespace"))
        imports.add_c_type(CType(name="TypeD", namespace="Namespace"))

        lines: Sequence[str] = imports.build()
        manual: Sequence[str] = (
            "from Namespace import TypeA",
            "from Namespace import TypeB",
            "from Namespace import TypeC",
            "from Namespace import TypeD",
        )

        self.assertEqual(manual, lines)

    def test_build_c_namespace(self) -> None:
        imports = Imports()
        imports.add_c_type(CType(name="TypeA", namespace="Namespace"))
        imports.add_c_type(CType(name="TypeB", namespace="Namespace.Namespace"))
        imports.add_c_type(CType(name="TypeC", namespace="Namespace.Namespace"))
        imports.add_c_type(CType(name="TypeD", namespace="Namespace.Namespace.Namespace"))

        lines: Sequence[str] = imports.build("Namespace.Namespace")
        manual: Sequence[str] = (
            "from Namespace.Namespace.Namespace import TypeD",
            "from Namespace import TypeA",
        )

        self.assertEqual(manual, lines)

    def test_build_type_vars(self) -> None:
        imports = Imports()
        imports.add_c_type(CType(name="T", namespace="Namespace", generic=True))
        imports.add_c_type(CType(name="U", namespace="Namespace", generic=True))
        imports.add_c_type(CType(name="V", namespace="Namespace", generic=True))

        lines: Sequence[str] = imports.build()
        manual: Sequence[str] = (
            "from typing import TypeVar",
            f'T = TypeVar("T")',
            f'U = TypeVar("U")',
            f'V = TypeVar("V")',
        )

        self.assertEqual(manual, lines)

    def test_build_include_event_type(self) -> None:
        imports = Imports()
        imports.include_event_type = True

        lines: Sequence[str] = imports.build()
        manual: Sequence[str] = (
            "from typing import Generic",
            f'T = TypeVar("T")',
            "class EventType(Generic[T]):",
            "    def __iadd__(self, other: T): ...",
            "    def __isub__(self, other: T): ...",
        )

        self.assertEqual(manual, lines)


class TestDoc(TestBase):
    def test_split_node_str(self) -> None:
        node_str: str = "Node.Node.Node.Node"

        result: str
        remainder: str
        result, remainder = Doc.split_node_str(node_str)

        self.assertEqual("Node", result)
        self.assertEqual("Node.Node.Node", remainder)

    def test_split_node_str_no_remainder(self) -> None:
        node_str: str = "Node"

        result: str
        remainder: str
        result, remainder = Doc.split_node_str(node_str)

        self.assertEqual("Node", result)
        self.assertEqual(None, remainder)

    def test_split_node_str_brackets(self) -> None:
        node_str: str = "Node[Namespace.Type].Node.Node.Node"

        result: str
        remainder: str
        result, remainder = Doc.split_node_str(node_str)

        self.assertEqual("Node[Namespace.Type]", result)
        self.assertEqual("Node.Node.Node", remainder)

    def test_split_node_str_brackets_no_remainder(self) -> None:
        node_str: str = "Node[Namespace.Type]"

        result: str
        remainder: str
        result, remainder = Doc.split_node_str(node_str)

        self.assertEqual("Node[Namespace.Type]", result)
        self.assertEqual(None, remainder)

    def test_split_node_str_brackets_multi(self) -> None:
        node_str: str = "Node[Namespace.Type, Namespace.Type].Node.Node.Node"

        result: str
        remainder: str
        result, remainder = Doc.split_node_str(node_str)

        self.assertEqual("Node[Namespace.Type, Namespace.Type]", result)
        self.assertEqual("Node.Node.Node", remainder)

    def test_split_node_str_brackets_multi_no_remainder(self) -> None:
        node_str: str = "Node[Namespace.Type, Namespace.Type]"

        result: str
        remainder: str
        result, remainder = Doc.split_node_str(node_str)

        self.assertEqual("Node[Namespace.Type, Namespace.Type]", result)
        self.assertEqual(None, remainder)

    def test_split_node_str_brackets_nested(self) -> None:
        node_str: str = "Node[Namespace.Type[$T]].Node.Node.Node"

        result: str
        remainder: str
        result, remainder = Doc.split_node_str(node_str)

        self.assertEqual("Node[Namespace.Type[$T]]", result)
        self.assertEqual("Node.Node.Node", remainder)

    def test_split_node_str_parenthesis(self) -> None:
        node_str: str = "Node(Namespace.Type).Node.Node.Node"

        result: str
        remainder: str
        result, remainder = Doc.split_node_str(node_str)

        self.assertEqual("Node(Namespace.Type)", result)
        self.assertEqual("Node.Node.Node", remainder)

    def test_split_node_str_parenthesis_no_remainder(self) -> None:
        node_str: str = "Node(Namespace.Type)"

        result: str
        remainder: str
        result, remainder = Doc.split_node_str(node_str)

        self.assertEqual("Node(Namespace.Type)", result)
        self.assertEqual(None, remainder)

    def test_split_node_str_parenthesis_multi(self) -> None:
        node_str: str = "Node(Namespace.Type, Namespace.Type).Node.Node.Node"

        result: str
        remainder: str
        result, remainder = Doc.split_node_str(node_str)

        self.assertEqual("Node(Namespace.Type, Namespace.Type)", result)
        self.assertEqual("Node.Node.Node", remainder)

    def test_split_node_str_parenthesis_multi_no_remainder(self) -> None:
        node_str: str = "Node(Namespace.Type, Namespace.Type)"

        result: str
        remainder: str
        result, remainder = Doc.split_node_str(node_str)

        self.assertEqual("Node(Namespace.Type, Namespace.Type)", result)
        self.assertEqual(None, remainder)

    def test_split_node_str_parenthesis_nested(self) -> None:
        node_str: str = "Node(Namespace.Type($T)).Node.Node.Node"

        result: str
        remainder: str
        result, remainder = Doc.split_node_str(node_str)

        self.assertEqual("Node(Namespace.Type($T))", result)
        self.assertEqual("Node.Node.Node", remainder)

    def test_split_node_str_colon(self) -> None:
        node_str: str = "Node:Node:Node:Node"

        result: str
        remainder: str
        result, remainder = Doc.split_node_str(node_str)

        self.assertEqual("Node", result)
        self.assertEqual("Node:Node:Node", remainder)

    def test_split_node_str_colon_no_remainder(self) -> None:
        node_str: str = "Node"

        result: str
        remainder: str
        result, remainder = Doc.split_node_str(node_str)

        self.assertEqual("Node", result)
        self.assertEqual(None, remainder)

    def test_split_node_str_colon_brackets(self) -> None:
        node_str: str = "Node[Namespace:Type]:Node:Node:Node"

        result: str
        remainder: str
        result, remainder = Doc.split_node_str(node_str)

        self.assertEqual("Node[Namespace:Type]", result)
        self.assertEqual("Node:Node:Node", remainder)

    def test_split_node_str_colon_brackets_no_remainder(self) -> None:
        node_str: str = "Node[Namespace:Type]"

        result: str
        remainder: str
        result, remainder = Doc.split_node_str(node_str)

        self.assertEqual("Node[Namespace:Type]", result)
        self.assertEqual(None, remainder)

    def test_split_node_str_colon_brackets_multi(self) -> None:
        node_str: str = "Node[Namespace:Type, Namespace:Type]:Node:Node:Node"

        result: str
        remainder: str
        result, remainder = Doc.split_node_str(node_str)

        self.assertEqual("Node[Namespace:Type, Namespace:Type]", result)
        self.assertEqual("Node:Node:Node", remainder)

    def test_split_node_str_colon_brackets_multi_no_remainder(self) -> None:
        node_str: str = "Node[Namespace:Type, Namespace:Type]"

        result: str
        remainder: str
        result, remainder = Doc.split_node_str(node_str)

        self.assertEqual("Node[Namespace:Type, Namespace:Type]", result)
        self.assertEqual(None, remainder)

    def test_split_node_str_colon_brackets_nested(self) -> None:
        node_str: str = "Node[Namespace:Type[$T]]:Node:Node:Node"

        result: str
        remainder: str
        result, remainder = Doc.split_node_str(node_str)

        self.assertEqual("Node[Namespace:Type[$T]]", result)
        self.assertEqual("Node:Node:Node", remainder)

    def test_split_node_str_colon_parenthesis(self) -> None:
        node_str: str = "Node(Namespace:Type):Node:Node:Node"

        result: str
        remainder: str
        result, remainder = Doc.split_node_str(node_str)

        self.assertEqual("Node(Namespace:Type)", result)
        self.assertEqual("Node:Node:Node", remainder)

    def test_split_node_str_colon_parenthesis_no_remainder(self) -> None:
        node_str: str = "Node(Namespace:Type)"

        result: str
        remainder: str
        result, remainder = Doc.split_node_str(node_str)

        self.assertEqual("Node(Namespace:Type)", result)
        self.assertEqual(None, remainder)

    def test_split_node_str_colon_parenthesis_multi(self) -> None:
        node_str: str = "Node(Namespace:Type, Namespace:Type):Node:Node:Node"

        result: str
        remainder: str
        result, remainder = Doc.split_node_str(node_str)

        self.assertEqual("Node(Namespace:Type, Namespace:Type)", result)
        self.assertEqual("Node:Node:Node", remainder)

    def test_split_node_str_colon_parenthesis_multi_no_remainder(self) -> None:
        node_str: str = "Node(Namespace:Type, Namespace:Type)"

        result: str
        remainder: str
        result, remainder = Doc.split_node_str(node_str)

        self.assertEqual("Node(Namespace:Type, Namespace:Type)", result)
        self.assertEqual(None, remainder)

    def test_split_node_str_colon_parenthesis_nested(self) -> None:
        node_str: str = "Node(Namespace:Type($T)):Node:Node:Node"

        result: str
        remainder: str
        result, remainder = Doc.split_node_str(node_str)

        self.assertEqual("Node(Namespace:Type($T))", result)
        self.assertEqual("Node:Node:Node", remainder)

    def test_translate(self) -> None:
        pattern: str = "Pattern"

        result: str = Doc.translate(pattern)

        self.assertEqual(r"(?s:Pattern)\Z", result)

    def test_translate_brackets(self) -> None:
        pattern: str = "Pattern[Namespace:Type]"

        result: str = Doc.translate(pattern)

        self.assertEqual(r"(?s:Pattern\[Namespace:Type\])\Z", result)

    def test_translate_wildcard_star(self) -> None:
        pattern: str = "Pattern[*]"

        result: str = Doc.translate(pattern)

        self.assertEqual(r"(?s:Pattern\[.*\])\Z", result)

    def test_translate_wildcard_generic_bracket(self) -> None:
        pattern: str = "Pattern[$T]"

        result: str = Doc.translate(pattern)

        self.assertEqual(r"(?s:Pattern\[.*\])\Z", result)

    def test_translate_wildcard_generic_bracket_long(self) -> None:
        pattern: str = "Pattern[$TKey]"

        result: str = Doc.translate(pattern)

        self.assertEqual(r"(?s:Pattern\[.*\])\Z", result)

    def test_translate_wildcard_generic_bracket_multi(self) -> None:
        pattern: str = "Pattern[$TKey, $TValue]"

        result: str = Doc.translate(pattern)

        self.assertEqual(r"(?s:Pattern\[(?=(?P<g0>.*?,\ ))(?P=g0).*\])\Z", result)

    def test_translate_wildcard_generic_parenthesis(self) -> None:
        pattern: str = "Pattern($T)"

        result: str = Doc.translate(pattern)

        self.assertEqual(r"(?s:Pattern\(.*\))\Z", result)

    def test_translate_wildcard_generic_parenthesis_long(self) -> None:
        pattern: str = "Pattern($TKey)"

        result: str = Doc.translate(pattern)

        self.assertEqual(r"(?s:Pattern\(.*\))\Z", result)

    def test_translate_wildcard_generic_parenthesis_multi(self) -> None:
        pattern: str = "Pattern($TKey, $TValue)"

        result: str = Doc.translate(pattern)

        self.assertEqual(r"(?s:Pattern\((?=(?P<g0>.*?,\ ))(?P=g0).*\))\Z", result)

    def test_get_shallow_node(self) -> None:
        doc_tree: Mapping[str, Any] = {"Node": {"doc": ""}}
        doc_dict: Doc = Doc(doc_tree)
        node: Doc = doc_dict.get("Node")

        self.assertIsNotNone(node)
        self.assertIsInstance(node, Doc)
        self.assertEqual({"doc": ""}, node.data)

    def test_get_shallow_node_missing(self) -> None:
        doc_tree: Mapping[str, Any] = {"Node": {"doc": ""}}
        doc_dict: Doc = Doc(doc_tree)
        node: Doc = doc_dict.get("Not Present")

        self.assertIsNone(node)

    def test_get_shallow_node_wildcard(self) -> None:
        doc_tree: Mapping[str, Any] = {"Node[*]": {"doc": ""}}
        doc_dict: Doc = Doc(doc_tree)
        node: Doc = doc_dict.get("Node[Namespace:TypeA]")

        self.assertIsNotNone(node)
        self.assertIsInstance(node, Doc)
        self.assertEqual({"doc": ""}, node.data)

    def test_get_shallow_node_wildcard_generic_bracket(self) -> None:
        doc_tree: Mapping[str, Any] = {"Node[$T]": {"doc": ""}}
        doc_dict: Doc = Doc(doc_tree)
        node: Doc = doc_dict.get("Node[Namespace:TypeA]")

        self.assertIsNotNone(node)
        self.assertIsInstance(node, Doc)
        self.assertEqual({"doc": ""}, node.data)

    def test_get_shallow_node_wildcard_generic_bracket_multi(self) -> None:
        doc_tree: Mapping[str, Any] = {"Node[$K, $V]": {"doc": ""}}
        doc_dict: Doc = Doc(doc_tree)
        node: Doc = doc_dict.get("Node[Namespace:TypeA, Namespace:TypeB]")

        self.assertIsNotNone(node)
        self.assertIsInstance(node, Doc)
        self.assertEqual({"doc": ""}, node.data)

    def test_get_shallow_node_wildcard_generic_parenthesis(self) -> None:
        doc_tree: Mapping[str, Any] = {"Node($T)": {"doc": ""}}
        doc_dict: Doc = Doc(doc_tree)
        node: Doc = doc_dict.get("Node(Namespace:TypeA)")

        self.assertIsNotNone(node)
        self.assertIsInstance(node, Doc)
        self.assertEqual({"doc": ""}, node.data)

    def test_get_shallow_node_wildcard_generic_parenthesis_multi(self) -> None:
        doc_tree: Mapping[str, Any] = {"Node($K, $V)": {"doc": ""}}
        doc_dict: Doc = Doc(doc_tree)
        node: Doc = doc_dict.get("Node(Namespace:TypeA, Namespace:TypeB)")

        self.assertIsNotNone(node)
        self.assertIsInstance(node, Doc)
        self.assertEqual({"doc": ""}, node.data)

    def test_get_deep_node(self) -> None:
        doc_tree: Mapping[str, Any] = {"NodeA": {"NodeB": {"NodeC": {"NodeD": {"doc": ""}}}}}
        doc_dict: Doc = Doc(doc_tree)
        node: Doc = doc_dict.get("NodeA.NodeB.NodeC.NodeD")

        self.assertIsNotNone(node)
        self.assertIsInstance(node, Doc)
        self.assertEqual({"doc": ""}, node.data)

    def test_get_deep_node_missing(self) -> None:
        doc_tree: Mapping[str, Any] = {"NodeA": {"NodeB": {"NodeC": {"NodeD": {"doc": ""}}}}}
        doc_dict: Doc = Doc(doc_tree)
        node: Doc = doc_dict.get("NodeA.NodeB.NodeC.Not Present")

        self.assertIsNone(node)

    def test_get_deep_node_wildcard(self) -> None:
        doc_tree: Mapping[str, Any] = {"NodeA": {"NodeB": {"NodeC": {"Node[*]": {"doc": ""}}}}}
        doc_dict: Doc = Doc(doc_tree)
        node: Doc = doc_dict.get("NodeA.NodeB.NodeC.Node[Namespace:TypeA]")

        self.assertIsNotNone(node)
        self.assertIsInstance(node, Doc)
        self.assertEqual({"doc": ""}, node.data)

    def test_get_deep_node_wildcard_generic_bracket(self) -> None:
        doc_tree: Mapping[str, Any] = {"NodeA": {"NodeB": {"NodeC": {"Node[$T]": {"doc": ""}}}}}
        doc_dict: Doc = Doc(doc_tree)
        node: Doc = doc_dict.get("NodeA.NodeB.NodeC.Node[Namespace:TypeA]")

        self.assertIsNotNone(node)
        self.assertIsInstance(node, Doc)
        self.assertEqual({"doc": ""}, node.data)

    def test_get_deep_node_wildcard_generic_bracket_multi(self) -> None:
        doc_tree: Mapping[str, Any] = {"NodeA": {"NodeB": {"NodeC": {"Node[$K, $V]": {"doc": ""}}}}}
        doc_dict: Doc = Doc(doc_tree)
        node: Doc = doc_dict.get("NodeA.NodeB.NodeC.Node[Namespace:TypeA, Namespace:TypeB]")

        self.assertIsNotNone(node)
        self.assertIsInstance(node, Doc)
        self.assertEqual({"doc": ""}, node.data)

    def test_get_deep_node_wildcard_generic_parenthesis(self) -> None:
        doc_tree: Mapping[str, Any] = {"NodeA": {"NodeB": {"NodeC": {"Node($T)": {"doc": ""}}}}}
        doc_dict: Doc = Doc(doc_tree)
        node: Doc = doc_dict.get("NodeA.NodeB.NodeC.Node(Namespace:TypeA)")

        self.assertIsNotNone(node)
        self.assertIsInstance(node, Doc)
        self.assertEqual({"doc": ""}, node.data)

    def test_get_deep_node_wildcard_generic_parenthesis_multi(self) -> None:
        doc_tree: Mapping[str, Any] = {"NodeA": {"NodeB": {"NodeC": {"Node($K, $V)": {"doc": ""}}}}}
        doc_dict: Doc = Doc(doc_tree)
        node: Doc = doc_dict.get("NodeA.NodeB.NodeC.Node(Namespace:TypeA, Namespace:TypeB)")

        self.assertIsNotNone(node)
        self.assertIsInstance(node, Doc)
        self.assertEqual({"doc": ""}, node.data)

    def test_doc_string_empty(self) -> None:
        doc_tree: Mapping[str, Any] = {}
        doc_dict: Doc = Doc(doc_tree)
        doc_string: Sequence[str] = doc_dict.doc_string()

        self.assertIsNotNone(doc_string)
        self.assertIsInstance(doc_string, Sequence)
        self.assertEqual(('""""""',), doc_string)

    def test_doc_string_single_line(self) -> None:
        doc_tree: Mapping[str, Any] = {
            "doc": "This is a doc string that is exactly 57 characters long.",
        }
        doc_dict: Doc = Doc(doc_tree)
        doc_string: Sequence[str] = doc_dict.doc_string()

        self.assertIsNotNone(doc_string)
        self.assertIsInstance(doc_string, Sequence)
        self.assertEqual(
            ('"""This is a doc string that is exactly 57 characters long."""',),
            doc_string,
        )

    def test_doc_string_empty_indent(self) -> None:
        doc_tree: Mapping[str, Any] = {}
        doc_dict: Doc = Doc(doc_tree)
        doc_string: Sequence[str] = doc_dict.doc_string(indent=1)

        self.assertIsNotNone(doc_string)
        self.assertIsInstance(doc_string, Sequence)
        self.assertEqual(('    """"""',), doc_string)

    def test_doc_string_single_line_indent(self) -> None:
        doc_tree: Mapping[str, Any] = {
            "doc": "This is a doc string that is exactly 57 characters long.",
        }
        doc_dict: Doc = Doc(doc_tree)
        doc_string: Sequence[str] = doc_dict.doc_string(indent=1)

        self.assertIsNotNone(doc_string)
        self.assertIsInstance(doc_string, Sequence)
        self.assertEqual(
            ('    """This is a doc string that is exactly 57 characters long."""',),
            doc_string,
        )

    def test_doc_string_long_line(self) -> None:
        doc_tree: Mapping[str, Any] = {
            "doc": (
                "This is a longer doc string that is even longer at a "
                "whopping, super mind-numbing length of 112 characters long."
            ),
        }
        doc_dict: Doc = Doc(doc_tree)
        doc_string: Sequence[str] = doc_dict.doc_string()

        self.assertIsNotNone(doc_string)
        self.assertIsInstance(doc_string, Sequence)
        self.assertEqual(
            (
                '"""This is a longer doc string that is even longer at a whopping, super mind-numbing length of 112',
                "characters long.",
                '"""',
            ),
            doc_string,
        )

    def test_doc_string_multi_line(self) -> None:
        doc_tree: Mapping[str, Any] = {
            "doc": "This is one line.\nThis is another line",
        }
        doc_dict: Doc = Doc(doc_tree)
        doc_string: Sequence[str] = doc_dict.doc_string()

        self.assertIsNotNone(doc_string)
        self.assertIsInstance(doc_string, Sequence)
        self.assertEqual(
            ('"""This is one line.', "", "This is another line", '"""'),
            doc_string,
        )

    def test_doc_string_parameters(self) -> None:
        doc_tree: Mapping[str, Any] = {
            "doc": "This is a doc string with parameters.",
            "parameters": {
                "param0": "This is parameter 0.",
                "param1": "This is parameter 1.",
            },
        }
        doc_dict: Doc = Doc(doc_tree)
        doc_string: Sequence[str] = doc_dict.doc_string()

        self.assertIsNotNone(doc_string)
        self.assertIsInstance(doc_string, Sequence)
        self.assertEqual(
            (
                '"""This is a doc string with parameters.',
                "",
                ":param param0: This is parameter 0.",
                ":param param1: This is parameter 1.",
                '"""',
            ),
            doc_string,
        )

    def test_doc_string_parameter_long(self) -> None:
        doc_tree: Mapping[str, Any] = {
            "doc": "This is a doc string with parameters.",
            "parameters": {
                "param0": (
                    "This is a parameter that has a doc string that is so long that it to need to "
                    "be split into multiple lines to prevent it from soft wrapping in editors."
                ),
            },
        }
        doc_dict: Doc = Doc(doc_tree)
        doc_string: Sequence[str] = doc_dict.doc_string()

        self.assertIsNotNone(doc_string)
        self.assertIsInstance(doc_string, Sequence)
        self.assertEqual(
            (
                '"""This is a doc string with parameters.',
                "",
                ":param param0: This is a parameter that has a doc string that is so long that it to need to be split",
                "  into multiple lines to prevent it from soft wrapping in editors.",
                '"""',
            ),
            doc_string,
        )

    def test_doc_string_return(self) -> None:
        doc_tree: Mapping[str, Any] = {
            "doc": "This is a doc string with a return.",
            "return": "This is the return string.",
        }
        doc_dict: Doc = Doc(doc_tree)
        doc_string: Sequence[str] = doc_dict.doc_string()

        self.assertIsNotNone(doc_string)
        self.assertIsInstance(doc_string, Sequence)
        self.assertEqual(
            (
                '"""This is a doc string with a return.',
                "",
                ":return: This is the return string.",
                '"""',
            ),
            doc_string,
        )

    def test_doc_string_return_long(self) -> None:
        doc_tree: Mapping[str, Any] = {
            "doc": "This is a doc string with a return.",
            "return": (
                "This is a return string that has a doc string that is so long that it needs "
                "to be split into multiple lines to prevent it from soft wrapping in editors."
            ),
        }
        doc_dict: Doc = Doc(doc_tree)
        doc_string: Sequence[str] = doc_dict.doc_string()

        self.assertIsNotNone(doc_string)
        self.assertIsInstance(doc_string, Sequence)
        self.assertEqual(
            (
                '"""This is a doc string with a return.',
                "",
                ":return: This is a return string that has a doc string that is so long that it needs to be split",
                "  into multiple lines to prevent it from soft wrapping in editors.",
                '"""',
            ),
            doc_string,
        )

    def test_doc_string_except(self) -> None:
        doc_tree: Mapping[str, Any] = {
            "doc": "This is a doc string with a return.",
            "exceptions": {
                "ExceptionA": "This is the first exception.",
                "ExceptionB": "This is the second exception.",
            },
        }
        doc_dict: Doc = Doc(doc_tree)
        doc_string: Sequence[str] = doc_dict.doc_string()

        self.assertIsNotNone(doc_string)
        self.assertIsInstance(doc_string, Sequence)
        self.assertEqual(
            (
                '"""This is a doc string with a return.',
                "",
                ":except ExceptionA: This is the first exception.",
                ":except ExceptionB: This is the second exception.",
                '"""',
            ),
            doc_string,
        )

    def test_doc_string_except_long(self) -> None:
        doc_tree: Mapping[str, Any] = {
            "doc": "This is a doc string with a return.",
            "exceptions": {
                "Exception": (
                    "This is an exception string that has a doc string that is so long that it "
                    "needs to be split into multiple lines to prevent it from soft wrapping in "
                    "editors."
                ),
            },
        }
        doc_dict: Doc = Doc(doc_tree)
        doc_string: Sequence[str] = doc_dict.doc_string()

        self.assertIsNotNone(doc_string)
        self.assertIsInstance(doc_string, Sequence)
        self.assertEqual(
            (
                '"""This is a doc string with a return.',
                "",
                ":except Exception: This is an exception string that has a doc string that is so long that it needs",
                "  to be split into multiple lines to prevent it from soft wrapping in editors.",
                '"""',
            ),
            doc_string,
        )

    def test_doc_string_formatted(self) -> None:
        doc_tree: Mapping[str, Any] = {
            "doc": "This is a doc string with a format block.\n%replace%",
            "doc_formatted": {
                "replace": (
                    "       | Column 1 | Column 2 | Column 3 | Column 4",
                    "-------|----------|----------|----------|----------",
                    " Row 1 |   R1C1   |   R1C2   |   R1C3   |   R1C4",
                    "-------|----------|----------|----------|----------",
                    " Row 2 |   R2C1   |   R2C2   |   R2C3   |   R2C4",
                    "-------|----------|----------|----------|----------",
                    " Row 3 |   R3C1   |   R3C2   |   R3C3   |   R3C4",
                    "-------|----------|----------|----------|----------",
                    " Row 4 |   R4C1   |   R4C2   |   R4C3   |   R4C4",
                    "-------|----------|----------|----------|----------",
                ),
            },
        }
        doc_dict: Doc = Doc(doc_tree)
        doc_string: Sequence[str] = doc_dict.doc_string()

        self.assertIsNotNone(doc_string)
        self.assertIsInstance(doc_string, Sequence)
        self.assertEqual(
            (
                '"""This is a doc string with a format block.',
                "",
                "       | Column 1 | Column 2 | Column 3 | Column 4",
                "-------|----------|----------|----------|----------",
                " Row 1 |   R1C1   |   R1C2   |   R1C3   |   R1C4",
                "-------|----------|----------|----------|----------",
                " Row 2 |   R2C1   |   R2C2   |   R2C3   |   R2C4",
                "-------|----------|----------|----------|----------",
                " Row 3 |   R3C1   |   R3C2   |   R3C3   |   R3C4",
                "-------|----------|----------|----------|----------",
                " Row 4 |   R4C1   |   R4C2   |   R4C3   |   R4C4",
                "-------|----------|----------|----------|----------",
                '"""',
            ),
            doc_string,
        )


class TestMergeDoc(TestBase):
    def test_merge(self) -> None:
        tree0: Mapping[str, Any] = {
            "doc": "",
            "doc_formatted": {},
            "parameters": {},
            "return": "",
            "exceptions": {},
        }
        tree1: Mapping[str, Any] = {
            "doc": "Doc String\n%format0%",
            "doc_formatted": {
                "format0": ("0", "1", "2", "3"),
                "format1": ("0", "2", "4", "6"),
            },
            "parameters": {
                "param0": "Parameter 0.",
                "param1": "Parameter 1.",
            },
            "return": "Return String",
            "exceptions": {
                "Exception0": "Exception 0.",
                "Exception1": "Exception 1.",
            },
        }

        doc_dict0: Doc = Doc(tree0)
        doc_dict1: Doc = Doc(tree1)

        merged: Doc = merge_doc(doc_dict0, doc_dict1)

        self.assertIsNotNone(merged)
        self.assertIsInstance(merged, Doc)
        self.assertEqual(
            {
                "doc": "Doc String\n%format0%",
                "doc_formatted": {
                    "format0": ("0", "1", "2", "3"),
                    "format1": ("0", "2", "4", "6"),
                },
                "parameters": {
                    "param0": "Parameter 0.",
                    "param1": "Parameter 1.",
                },
                "return": "Return String",
                "exceptions": {
                    "Exception0": "Exception 0.",
                    "Exception1": "Exception 1.",
                },
            },
            merged.data,
        )

    def test_merge_doc_empty(self) -> None:
        tree0: Mapping[str, Any] = {"doc": "Doc0"}
        tree1: Mapping[str, Any] = {"doc": ""}

        doc_dict0: Doc = Doc(tree0)
        doc_dict1: Doc = Doc(tree1)

        merged: Doc = merge_doc(doc_dict0, doc_dict1)

        self.assertIsNotNone(merged)
        self.assertIsInstance(merged, Doc)
        self.assertEqual({"doc": "Doc0"}, merged.data)

    def test_merge_doc_both(self) -> None:
        tree0: Mapping[str, Any] = {"doc": "Doc0"}
        tree1: Mapping[str, Any] = {"doc": "Doc1"}

        doc_dict0: Doc = Doc(tree0)
        doc_dict1: Doc = Doc(tree1)

        merged: Doc = merge_doc(doc_dict0, doc_dict1)

        self.assertIsNotNone(merged)
        self.assertIsInstance(merged, Doc)
        self.assertEqual({"doc": "Doc0\nDoc1"}, merged.data)

    def test_merge_doc_formatted_empty(self) -> None:
        tree0: Mapping[str, Any] = {
            "doc_formatted": {
                "format0": ("0", "1", "2", "3"),
                "format1": ("0", "2", "4", "6"),
            },
        }
        tree1: Mapping[str, Any] = {
            "doc_formatted": {
                "format0": (),
            },
        }

        doc_dict0: Doc = Doc(tree0)
        doc_dict1: Doc = Doc(tree1)

        merged: Doc = merge_doc(doc_dict0, doc_dict1)

        self.assertIsNotNone(merged)
        self.assertIsInstance(merged, Doc)
        self.assertEqual(
            {
                "doc_formatted": {
                    "format0": ("0", "1", "2", "3"),
                    "format1": ("0", "2", "4", "6"),
                },
            },
            merged.data,
        )

    def test_merge_doc_formatted_both(self) -> None:
        tree0: Mapping[str, Any] = {
            "doc_formatted": {
                "format0": ("0", "1", "2", "3"),
                "format1": ("0", "2", "4", "6"),
                "format2": ("0", "3", "6", "9"),
            },
        }
        tree1: Mapping[str, Any] = {
            "doc_formatted": {
                "format0": ("0", "1", "2", "3"),
                "format1": ("0", "2", "4", "6"),
                "format3": ("0", "4", "8", "12"),
            },
        }

        doc_dict0: Doc = Doc(tree0)
        doc_dict1: Doc = Doc(tree1)

        merged: Doc = merge_doc(doc_dict0, doc_dict1)

        self.assertIsNotNone(merged)
        self.assertIsInstance(merged, Doc)
        self.assertEqual(
            {
                "doc_formatted": {
                    "format0": ("0", "1", "2", "3", "0", "1", "2", "3"),
                    "format1": ("0", "2", "4", "6", "0", "2", "4", "6"),
                    "format2": ("0", "3", "6", "9"),
                    "format3": ("0", "4", "8", "12"),
                },
            },
            merged.data,
        )

    def test_merge_parameters_empty(self) -> None:
        tree0: Mapping[str, Any] = {
            "parameters": {
                "param0": "Parameter 0.",
                "param1": "Parameter 1.",
            },
        }
        tree1: Mapping[str, Any] = {
            "parameters": {
                "param0": "",
            },
        }

        doc_dict0: Doc = Doc(tree0)
        doc_dict1: Doc = Doc(tree1)

        merged: Doc = merge_doc(doc_dict0, doc_dict1)

        self.assertIsNotNone(merged)
        self.assertIsInstance(merged, Doc)
        self.assertEqual(
            {
                "parameters": {
                    "param0": "Parameter 0.",
                    "param1": "Parameter 1.",
                },
            },
            merged.data,
        )

    def test_merge_parameters_both(self) -> None:
        tree0: Mapping[str, Any] = {
            "parameters": {
                "param0": "Parameter 0.",
                "param1": "Parameter 1.",
                "param2": "Parameter 2.",
            },
        }
        tree1: Mapping[str, Any] = {
            "parameters": {
                "param0": "Parameter 0.",
                "param1": "Parameter 1.",
                "param3": "Parameter 3.",
            },
        }

        doc_dict0: Doc = Doc(tree0)
        doc_dict1: Doc = Doc(tree1)

        merged: Doc = merge_doc(doc_dict0, doc_dict1)

        self.assertIsNotNone(merged)
        self.assertIsInstance(merged, Doc)
        self.assertEqual(
            {
                "parameters": {
                    "param0": "Parameter 0.\nParameter 0.",
                    "param1": "Parameter 1.\nParameter 1.",
                    "param2": "Parameter 2.",
                    "param3": "Parameter 3.",
                },
            },
            merged.data,
        )

    def test_merge_return_empty(self) -> None:
        tree0: Mapping[str, Any] = {"return": "Return0"}
        tree1: Mapping[str, Any] = {"return": ""}

        doc_dict0: Doc = Doc(tree0)
        doc_dict1: Doc = Doc(tree1)

        merged: Doc = merge_doc(doc_dict0, doc_dict1)

        self.assertIsNotNone(merged)
        self.assertIsInstance(merged, Doc)
        self.assertEqual({"return": "Return0"}, merged.data)

    def test_merge_return_both(self) -> None:
        tree0: Mapping[str, Any] = {"return": "Return0"}
        tree1: Mapping[str, Any] = {"return": "Return1"}

        doc_dict0: Doc = Doc(tree0)
        doc_dict1: Doc = Doc(tree1)

        merged: Doc = merge_doc(doc_dict0, doc_dict1)

        self.assertIsNotNone(merged)
        self.assertIsInstance(merged, Doc)
        self.assertEqual({"return": "Return0\nReturn1"}, merged.data)

    def test_merge_exceptions_empty(self) -> None:
        tree0: Mapping[str, Any] = {
            "exceptions": {
                "Exception0": "Exception 0.",
                "Exception1": "Exception 1.",
            },
        }
        tree1: Mapping[str, Any] = {
            "exceptions": {
                "Exception0": "",
            },
        }

        doc_dict0: Doc = Doc(tree0)
        doc_dict1: Doc = Doc(tree1)

        merged: Doc = merge_doc(doc_dict0, doc_dict1)

        self.assertIsNotNone(merged)
        self.assertIsInstance(merged, Doc)
        self.assertEqual(
            {
                "exceptions": {
                    "Exception0": "Exception 0.",
                    "Exception1": "Exception 1.",
                },
            },
            merged.data,
        )

    def test_merge_exceptions_both(self) -> None:
        tree0: Mapping[str, Any] = {
            "exceptions": {
                "Exception0": "Exception 0.",
                "Exception1": "Exception 1.",
                "Exception2": "Exception 2.",
            },
        }
        tree1: Mapping[str, Any] = {
            "exceptions": {
                "Exception0": "Exception 0.",
                "Exception1": "Exception 1.",
                "Exception3": "Exception 3.",
            },
        }

        doc_dict0: Doc = Doc(tree0)
        doc_dict1: Doc = Doc(tree1)

        merged: Doc = merge_doc(doc_dict0, doc_dict1)

        self.assertIsNotNone(merged)
        self.assertIsInstance(merged, Doc)
        self.assertEqual(
            {
                "exceptions": {
                    "Exception0": "Exception 0.\nException 0.",
                    "Exception1": "Exception 1.\nException 1.",
                    "Exception2": "Exception 2.",
                    "Exception3": "Exception 3.",
                },
            },
            merged.data,
        )

    def test_merge_tree(self) -> None:
        tree0: Mapping[str, Any] = {"NodeA": {}}
        tree1: Mapping[str, Any] = {"NodeB": {}}

        doc_dict0: Doc = Doc(tree0)
        doc_dict1: Doc = Doc(tree1)

        merged: Doc = merge_doc(doc_dict0, doc_dict1)

        self.assertIsNotNone(merged)
        self.assertIsInstance(merged, Doc)
        self.assertEqual(
            {
                "NodeA": {},
                "NodeB": {},
            },
            merged.data,
        )

    def test_merge_tree_deep(self) -> None:
        tree0: Mapping[str, Any] = {"NodeA": {"NodeB": {"NodeC": {"NodeD": {}}}}}
        tree1: Mapping[str, Any] = {"NodeA": {"NodeB": {"NodeC": {"NodeE": {}}}}}

        doc_dict0: Doc = Doc(tree0)
        doc_dict1: Doc = Doc(tree1)

        merged: Doc = merge_doc(doc_dict0, doc_dict1)

        self.assertIsNotNone(merged)
        self.assertIsInstance(merged, Doc)
        self.assertEqual(
            {"NodeA": {"NodeB": {"NodeC": {"NodeD": {}, "NodeE": {}}}}},
            merged.data,
        )


class TestBuildClass(TestBase):
    def test_build(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Class:",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_abstract(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=True,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Class(ABC):",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_generic(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(
                CType(name="K", namespace="Namespace", generic=True),
                CType(name="V", namespace="Namespace", generic=True),
            ),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Class(Generic[K, V]):",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_super(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=CType(name="Super", namespace="Namespace"),
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Class(Super):",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_interfaces(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(
                CType(name="InterfaceA", namespace="Namespace"),
                CType(name="InterfaceB", namespace="Namespace"),
            ),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Class(InterfaceA, InterfaceB):",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_fields(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={
                "Namespace:Class.FieldA": CField(
                    name="FieldA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    return_type=CType(name="FieldType", namespace="Namespace"),
                ),
                "Namespace:Class.FieldB": CField(
                    name="FieldB",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    return_type=CType(name="FieldType", namespace="Namespace"),
                ),
            },
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Class:",
            '    """"""',
            "    FieldA: Final[FieldType] = ...",
            '    """"""',
            "    FieldB: Final[FieldType] = ...",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_constructors(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={
                "Namespace:Class.__init__()": CConstructor(
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(),
                ),
            },
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Class:",
            '    """"""',
            "    def __init__(self):",
            '        """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_constructors_overload(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={
                "Namespace:Class.__init__()": CConstructor(
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(),
                ),
                "Namespace:Class.__init__(Namespace:Type)": CConstructor(
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                    ),
                ),
            },
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Class:",
            '    """"""',
            "    @overload",
            "    def __init__(self):",
            '        """"""',
            "    @overload",
            "    def __init__(self, param0: Type):",
            '        """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_properties(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={
                "Namespace:Class.PropertyA": CProperty(
                    name="PropertyA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="PropertyType", namespace="Namespace"),
                ),
                "Namespace:Class.PropertyB": CProperty(
                    name="PropertyB",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="PropertyType", namespace="Namespace"),
                ),
            },
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Class:",
            '    """"""',
            "    @property",
            "    def PropertyA(self) -> PropertyType:",
            '        """"""',
            "    @property",
            "    def PropertyB(self) -> PropertyType:",
            '        """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_methods(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={
                "Namespace:Class.MethodA(Namespace:ParamType, Namespace:ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                        CParameter(
                            name="param1", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
                "Namespace:Class.MethodB(Namespace:ParamType, Namespace:ParamType)": CMethod(
                    name="MethodB",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                        CParameter(
                            name="param1", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
            },
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Class:",
            '    """"""',
            "    def MethodA(self, param0: ParamType, param1: ParamType) -> MethodType:",
            '        """"""',
            "    def MethodB(self, param0: ParamType, param1: ParamType) -> MethodType:",
            '        """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_methods_overload(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={
                "Namespace:Class.MethodA(Namespace:ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
                "Namespace:Class.MethodA(Namespace:ParamType, Namespace:ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                        CParameter(
                            name="param1", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
            },
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Class:",
            '    """"""',
            "    @overload",
            "    def MethodA(self, param0: ParamType) -> MethodType:",
            '        """"""',
            "    @overload",
            "    def MethodA(self, param0: ParamType, param1: ParamType) -> MethodType:",
            '        """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_events(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={
                "Namespace:Class.EventA": CEvent(
                    name="EventA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="EventHandler", namespace="Namespace"),
                ),
                "Namespace:Class.EventB": CEvent(
                    name="EventB",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="EventHandler", namespace="Namespace"),
                ),
            },
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Class:",
            '    """"""',
            "    EventA: EventType[EventHandler] = ...",
            '    """"""',
            "    EventB: EventType[EventHandler] = ...",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_nested_types(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={
                "Namespace:Class.NestedClass": CClass(
                    name="NestedClass",
                    namespace="Namespace",
                    nested=CType(name="Class", namespace="Namespace"),
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "Namespace:Class.NestedStruct": CStruct(
                    name="NestedStruct",
                    namespace="Namespace",
                    nested=CType(name="Class", namespace="Namespace"),
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "Namespace:Class.INestedInterface": CInterface(
                    name="INestedInterface",
                    namespace="Namespace",
                    nested=CType(name="Class", namespace="Namespace"),
                    generic_args=(),
                    interfaces=(),
                    fields={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "Namespace:Class.NestedEnum": CEnum(
                    name="NestedEnum",
                    namespace="Namespace",
                    nested=CType(name="Class", namespace="Namespace"),
                    fields=(),
                ),
                "Namespace:Class.NestedDelegate": CDelegate(
                    name="NestedDelegate",
                    namespace="Namespace",
                    nested=CType(name="Class", namespace="Namespace"),
                    parameters=(),
                    return_type=CType(name="DelegateType", namespace="Namespace"),
                ),
            },
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Class:",
            '    """"""',
            "    class NestedClass:",
            '        """"""',
            "    class NestedStruct:",
            '        """"""',
            "    class INestedInterface:",
            '        """"""',
            "    class NestedEnum(Enum):",
            '        """"""',
            "    NestedDelegate: Callable[[], DelegateType] = ...",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_py_imports(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_py_imports_abstract(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=True,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"abc.ABC"}

        self.assertEqual(manual, imports.py)

    def test_py_imports_generic(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(
                CType(name="K", namespace="Namespace", generic=True),
                CType(name="V", namespace="Namespace", generic=True),
            ),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"typing.Generic", "typing.TypeVar"}

        self.assertEqual(manual, imports.py)

    def test_py_imports_super(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=CType(name="Super", namespace="Namespace"),
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_py_imports_interfaces(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(
                CType(name="InterfaceA", namespace="Namespace"),
                CType(name="InterfaceB", namespace="Namespace"),
            ),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_py_imports_fields(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={
                "Namespace:Class.FieldA": CField(
                    name="FieldA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    return_type=CType(name="FieldType", namespace="Namespace"),
                ),
                "Namespace:Class.FieldB": CField(
                    name="FieldB",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    return_type=CType(name="FieldType", namespace="Namespace"),
                ),
            },
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"typing.Final"}

        self.assertEqual(manual, imports.py)

    def test_py_imports_constructors(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={
                "Namespace:Class.__init__()": CConstructor(
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(),
                ),
            },
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_py_imports_constructors_overload(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={
                "Namespace:Class.__init__()": CConstructor(
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(),
                ),
                "Namespace:Class.__init__(Namespace:Type)": CConstructor(
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                    ),
                ),
            },
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"typing.overload"}

        self.assertEqual(manual, imports.py)

    def test_py_imports_properties(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={
                "Namespace:Class.PropertyA": CProperty(
                    name="PropertyA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="PropertyType", namespace="Namespace"),
                ),
                "Namespace:Class.PropertyB": CProperty(
                    name="PropertyB",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="PropertyType", namespace="Namespace"),
                ),
            },
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_py_imports_methods(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={
                "Namespace:Class.MethodA(Namespace:ParamType, Namespace:ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                        CParameter(
                            name="param1", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
                "Namespace:Class.MethodB(Namespace:ParamType, Namespace:ParamType)": CMethod(
                    name="MethodB",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                        CParameter(
                            name="param1", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
            },
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_py_imports_methods_overload(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={
                "Namespace:Class.MethodA(Namespace:ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
                "Namespace:Class.MethodA(Namespace:ParamType, Namespace:ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                        CParameter(
                            name="param1", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
            },
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"typing.overload"}

        self.assertEqual(manual, imports.py)

    def test_py_imports_events(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={
                "Namespace:Class.EventA": CEvent(
                    name="EventA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="EventHandler", namespace="Namespace"),
                ),
                "Namespace:Class.EventB": CEvent(
                    name="EventB",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="EventHandler", namespace="Namespace"),
                ),
            },
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_py_imports_nested(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={
                "Namespace:Class.NestedClass": CClass(
                    name="NestedClass",
                    namespace="Namespace",
                    nested=CType(name="Class", namespace="Namespace"),
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "Namespace:Class.NestedStruct": CStruct(
                    name="NestedStruct",
                    namespace="Namespace",
                    nested=CType(name="Class", namespace="Namespace"),
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "Namespace:Class.INestedInterface": CInterface(
                    name="INestedInterface",
                    namespace="Namespace",
                    nested=CType(name="Class", namespace="Namespace"),
                    generic_args=(),
                    interfaces=(),
                    fields={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "Namespace:Class.NestedEnum": CEnum(
                    name="NestedEnum",
                    namespace="Namespace",
                    nested=CType(name="Class", namespace="Namespace"),
                    fields=(),
                ),
                "Namespace:Class.NestedDelegate": CDelegate(
                    name="NestedDelegate",
                    namespace="Namespace",
                    nested=CType(name="Class", namespace="Namespace"),
                    parameters=(),
                    return_type=CType(name="DelegateType", namespace="Namespace"),
                ),
            },
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"typing.Callable"}

        self.assertEqual(manual, imports.py)

    def test_c_imports(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.c)

    def test_c_imports_abstract(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=True,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.c)

    def test_c_imports_generic(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(
                CType(name="K", namespace="Namespace", generic=True),
                CType(name="V", namespace="Namespace", generic=True),
            ),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.c)

    def test_c_imports_super(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=CType(name="Super", namespace="Namespace"),
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"Namespace.Super"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_interfaces(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(
                CType(name="InterfaceA", namespace="Namespace"),
                CType(name="InterfaceB", namespace="Namespace"),
            ),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"Namespace.InterfaceA", "Namespace.InterfaceB"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_fields(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={
                "Namespace:Class.FieldA": CField(
                    name="FieldA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    return_type=CType(name="FieldType", namespace="Namespace"),
                ),
                "Namespace:Class.FieldB": CField(
                    name="FieldB",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    return_type=CType(name="FieldType", namespace="Namespace"),
                ),
            },
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"Namespace.FieldType"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_constructors(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={
                "Namespace:Class.__init__()": CConstructor(
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(),
                ),
            },
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.c)

    def test_c_imports_constructors_overload(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={
                "Namespace:Class.__init__()": CConstructor(
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(),
                ),
                "Namespace:Class.__init__(Namespace:Type)": CConstructor(
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                    ),
                ),
            },
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"Namespace.Type"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_properties(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={
                "Namespace:Class.PropertyA": CProperty(
                    name="PropertyA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="PropertyType", namespace="Namespace"),
                ),
                "Namespace:Class.PropertyB": CProperty(
                    name="PropertyB",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="PropertyType", namespace="Namespace"),
                ),
            },
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"Namespace.PropertyType"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_methods(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={
                "Namespace:Class.MethodA(Namespace:ParamType, Namespace:ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                        CParameter(
                            name="param1", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
                "Namespace:Class.MethodB(Namespace:ParamType, Namespace:ParamType)": CMethod(
                    name="MethodB",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                        CParameter(
                            name="param1", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
            },
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"Namespace.MethodType", "Namespace.ParamType"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_methods_overload(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={
                "Namespace:Class.MethodA(Namespace:ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
                "Namespace:Class.MethodA(Namespace:ParamType, Namespace:ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                        CParameter(
                            name="param1", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
            },
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"Namespace.MethodType", "Namespace.ParamType"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_events(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={
                "Namespace:Class.EventA": CEvent(
                    name="EventA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="EventHandler", namespace="Namespace"),
                ),
                "Namespace:Class.EventB": CEvent(
                    name="EventB",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="EventHandler", namespace="Namespace"),
                ),
            },
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"Namespace.EventHandler"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_nested(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={
                "Namespace:Class.NestedClass": CClass(
                    name="NestedClass",
                    namespace="Namespace",
                    nested=CType(name="Class", namespace="Namespace"),
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "Namespace:Class.NestedStruct": CStruct(
                    name="NestedStruct",
                    namespace="Namespace",
                    nested=CType(name="Class", namespace="Namespace"),
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "Namespace:Class.INestedInterface": CInterface(
                    name="INestedInterface",
                    namespace="Namespace",
                    nested=CType(name="Class", namespace="Namespace"),
                    generic_args=(),
                    interfaces=(),
                    fields={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "Namespace:Class.NestedEnum": CEnum(
                    name="NestedEnum",
                    namespace="Namespace",
                    nested=CType(name="Class", namespace="Namespace"),
                    fields=(),
                ),
                "Namespace:Class.NestedDelegate": CDelegate(
                    name="NestedDelegate",
                    namespace="Namespace",
                    nested=CType(name="Class", namespace="Namespace"),
                    parameters=(),
                    return_type=CType(name="DelegateType", namespace="Namespace"),
                ),
            },
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"System.Enum", "Namespace.DelegateType"}

        self.assertEqual(manual, imports.c)

    def test_doc(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Class": {
                        "doc": "Class doc string.",
                    },
                },
            }
        )

        lines: Sequence[str] = build_class(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Class:",
            '    """Class doc string."""',
        )

        self.assertEqual(manual, lines)


class TestBuildStruct(TestBase):
    def test_build(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Struct:",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_abstract(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=True,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Struct(ABC):",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_generic(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(
                CType(name="K", namespace="Namespace", generic=True),
                CType(name="V", namespace="Namespace", generic=True),
            ),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Struct(Generic[K, V]):",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_super(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=CType(name="Super", namespace="Namespace"),
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Struct(Super):",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_interfaces(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(
                CType(name="InterfaceA", namespace="Namespace"),
                CType(name="InterfaceB", namespace="Namespace"),
            ),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Struct(InterfaceA, InterfaceB):",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_fields(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={
                "Namespace:Struct.FieldA": CField(
                    name="FieldA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    return_type=CType(name="FieldType", namespace="Namespace"),
                ),
                "Namespace:Struct.FieldB": CField(
                    name="FieldB",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    return_type=CType(name="FieldType", namespace="Namespace"),
                ),
            },
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Struct:",
            '    """"""',
            "    FieldA: Final[FieldType] = ...",
            '    """"""',
            "    FieldB: Final[FieldType] = ...",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_constructors(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={
                "Namespace:Struct.__init__()": CConstructor(
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(),
                ),
            },
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Struct:",
            '    """"""',
            "    def __init__(self):",
            '        """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_constructors_overload(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={
                "Namespace:Struct.__init__()": CConstructor(
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(),
                ),
                "Namespace:Struct.__init__(Namespace:Type)": CConstructor(
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                    ),
                ),
            },
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Struct:",
            '    """"""',
            "    @overload",
            "    def __init__(self):",
            '        """"""',
            "    @overload",
            "    def __init__(self, param0: Type):",
            '        """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_properties(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={
                "Namespace:Struct.PropertyA": CProperty(
                    name="PropertyA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="PropertyType", namespace="Namespace"),
                ),
                "Namespace:Struct.PropertyB": CProperty(
                    name="PropertyB",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="PropertyType", namespace="Namespace"),
                ),
            },
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Struct:",
            '    """"""',
            "    @property",
            "    def PropertyA(self) -> PropertyType:",
            '        """"""',
            "    @property",
            "    def PropertyB(self) -> PropertyType:",
            '        """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_methods(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={
                "Namespace:Struct.MethodA(Namespace:ParamType, Namespace:ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                        CParameter(
                            name="param1", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
                "Namespace:Struct.MethodB(Namespace:ParamType, Namespace:ParamType)": CMethod(
                    name="MethodB",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                        CParameter(
                            name="param1", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
            },
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Struct:",
            '    """"""',
            "    def MethodA(self, param0: ParamType, param1: ParamType) -> MethodType:",
            '        """"""',
            "    def MethodB(self, param0: ParamType, param1: ParamType) -> MethodType:",
            '        """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_methods_overload(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={
                "Namespace:Struct.MethodA(Namespace:ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
                "Namespace:Struct.MethodA(Namespace:ParamType, Namespace:ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                        CParameter(
                            name="param1", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
            },
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Struct:",
            '    """"""',
            "    @overload",
            "    def MethodA(self, param0: ParamType) -> MethodType:",
            '        """"""',
            "    @overload",
            "    def MethodA(self, param0: ParamType, param1: ParamType) -> MethodType:",
            '        """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_events(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={
                "Namespace:Struct.EventA": CEvent(
                    name="EventA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="EventHandler", namespace="Namespace"),
                ),
                "Namespace:Struct.EventB": CEvent(
                    name="EventB",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="EventHandler", namespace="Namespace"),
                ),
            },
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Struct:",
            '    """"""',
            "    EventA: EventType[EventHandler] = ...",
            '    """"""',
            "    EventB: EventType[EventHandler] = ...",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_nested(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={
                "Namespace:Struct.NestedClass": CClass(
                    name="NestedClass",
                    namespace="Namespace",
                    nested=CType(name="Struct", namespace="Namespace"),
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "Namespace:Struct.NestedStruct": CStruct(
                    name="NestedStruct",
                    namespace="Namespace",
                    nested=CType(name="Struct", namespace="Namespace"),
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "Namespace:Struct.INestedInterface": CInterface(
                    name="INestedInterface",
                    namespace="Namespace",
                    nested=CType(name="Struct", namespace="Namespace"),
                    generic_args=(),
                    interfaces=(),
                    fields={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "Namespace:Struct.NestedEnum": CEnum(
                    name="NestedEnum",
                    namespace="Namespace",
                    nested=CType(name="Struct", namespace="Namespace"),
                    fields=(),
                ),
                "Namespace:Struct.NestedDelegate": CDelegate(
                    name="NestedDelegate",
                    namespace="Namespace",
                    nested=CType(name="Struct", namespace="Namespace"),
                    parameters=(),
                    return_type=CType(name="DelegateType", namespace="Namespace"),
                ),
            },
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Struct:",
            '    """"""',
            "    class NestedClass:",
            '        """"""',
            "    class NestedStruct:",
            '        """"""',
            "    class INestedInterface:",
            '        """"""',
            "    class NestedEnum(Enum):",
            '        """"""',
            "    NestedDelegate: Callable[[], DelegateType] = ...",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_py_imports(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_py_imports_abstract(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=True,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"abc.ABC"}

        self.assertEqual(manual, imports.py)

    def test_py_imports_generic(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(
                CType(name="K", namespace="Namespace", generic=True),
                CType(name="V", namespace="Namespace", generic=True),
            ),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"typing.Generic", "typing.TypeVar"}

        self.assertEqual(manual, imports.py)

    def test_py_imports_super(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=CType(name="Super", namespace="Namespace"),
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_py_imports_interfaces(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(
                CType(name="InterfaceA", namespace="Namespace"),
                CType(name="InterfaceB", namespace="Namespace"),
            ),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_py_imports_fields(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={
                "Namespace:Struct.FieldA": CField(
                    name="FieldA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    return_type=CType(name="FieldType", namespace="Namespace"),
                ),
                "Namespace:Struct.FieldB": CField(
                    name="FieldB",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    return_type=CType(name="FieldType", namespace="Namespace"),
                ),
            },
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"typing.Final"}

        self.assertEqual(manual, imports.py)

    def test_py_imports_constructors(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={
                "Namespace:Struct.__init__()": CConstructor(
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(),
                ),
            },
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_py_imports_constructors_overload(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={
                "Namespace:Struct.__init__()": CConstructor(
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(),
                ),
                "Namespace:Struct.__init__(Namespace:Type)": CConstructor(
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                    ),
                ),
            },
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"typing.overload"}

        self.assertEqual(manual, imports.py)

    def test_py_imports_properties(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={
                "Namespace:Struct.PropertyA": CProperty(
                    name="PropertyA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="PropertyType", namespace="Namespace"),
                ),
                "Namespace:Struct.PropertyB": CProperty(
                    name="PropertyB",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="PropertyType", namespace="Namespace"),
                ),
            },
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_py_imports_methods(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={
                "Namespace:Struct.MethodA(Namespace:ParamType, Namespace:ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                        CParameter(
                            name="param1", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
                "Namespace:Struct.MethodB(Namespace:ParamType, Namespace:ParamType)": CMethod(
                    name="MethodB",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                        CParameter(
                            name="param1", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
            },
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_py_imports_methods_overload(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={
                "Namespace:Struct.MethodA(Namespace:ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
                "Namespace:Struct.MethodA(Namespace:ParamType, Namespace:ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                        CParameter(
                            name="param1", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
            },
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"typing.overload"}

        self.assertEqual(manual, imports.py)

    def test_py_imports_events(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={
                "Namespace:Struct.EventA": CEvent(
                    name="EventA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="EventHandler", namespace="Namespace"),
                ),
                "Namespace:Struct.EventB": CEvent(
                    name="EventB",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="EventHandler", namespace="Namespace"),
                ),
            },
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_py_imports_nested(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={
                "Namespace:Struct.NestedClass": CClass(
                    name="NestedClass",
                    namespace="Namespace",
                    nested=CType(name="Struct", namespace="Namespace"),
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "Namespace:Struct.NestedStruct": CStruct(
                    name="NestedStruct",
                    namespace="Namespace",
                    nested=CType(name="Struct", namespace="Namespace"),
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "Namespace:Struct.INestedInterface": CInterface(
                    name="INestedInterface",
                    namespace="Namespace",
                    nested=CType(name="Struct", namespace="Namespace"),
                    generic_args=(),
                    interfaces=(),
                    fields={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "Namespace:Struct.NestedEnum": CEnum(
                    name="NestedEnum",
                    namespace="Namespace",
                    nested=CType(name="Struct", namespace="Namespace"),
                    fields=(),
                ),
                "Namespace:Struct.NestedDelegate": CDelegate(
                    name="NestedDelegate",
                    namespace="Namespace",
                    nested=CType(name="Struct", namespace="Namespace"),
                    parameters=(),
                    return_type=CType(name="DelegateType", namespace="Namespace"),
                ),
            },
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"typing.Callable"}

        self.assertEqual(manual, imports.py)

    def test_c_imports(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.c)

    def test_c_imports_abstract(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=True,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.c)

    def test_c_imports_generic(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(
                CType(name="K", namespace="Namespace", generic=True),
                CType(name="V", namespace="Namespace", generic=True),
            ),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.c)

    def test_c_imports_super(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=CType(name="Super", namespace="Namespace"),
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"Namespace.Super"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_interfaces(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(
                CType(name="InterfaceA", namespace="Namespace"),
                CType(name="InterfaceB", namespace="Namespace"),
            ),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"Namespace.InterfaceA", "Namespace.InterfaceB"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_fields(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={
                "Namespace:Struct.FieldA": CField(
                    name="FieldA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    return_type=CType(name="FieldType", namespace="Namespace"),
                ),
                "Namespace:Struct.FieldB": CField(
                    name="FieldB",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    return_type=CType(name="FieldType", namespace="Namespace"),
                ),
            },
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"Namespace.FieldType"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_constructors(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={
                "Namespace:Struct.__init__()": CConstructor(
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(),
                ),
            },
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.c)

    def test_c_imports_constructors_overload(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={
                "Namespace:Struct.__init__()": CConstructor(
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(),
                ),
                "Namespace:Struct.__init__(Namespace:Type)": CConstructor(
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                    ),
                ),
            },
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"Namespace.Type"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_properties(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={
                "Namespace:Struct.PropertyA": CProperty(
                    name="PropertyA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="PropertyType", namespace="Namespace"),
                ),
                "Namespace:Struct.PropertyB": CProperty(
                    name="PropertyB",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="PropertyType", namespace="Namespace"),
                ),
            },
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"Namespace.PropertyType"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_methods(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={
                "Namespace:Struct.MethodA(Namespace:ParamType, Namespace:ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                        CParameter(
                            name="param1", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
                "Namespace:Struct.MethodB(Namespace:ParamType, Namespace:ParamType)": CMethod(
                    name="MethodB",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                        CParameter(
                            name="param1", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
            },
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"Namespace.MethodType", "Namespace.ParamType"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_methods_overload(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={
                "Namespace:Struct.MethodA(Namespace:ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
                "Namespace:Struct.MethodA(Namespace:ParamType, Namespace:ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                        CParameter(
                            name="param1", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
            },
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"Namespace.MethodType", "Namespace.ParamType"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_events(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={
                "Namespace:Struct.EventA": CEvent(
                    name="EventA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="EventHandler", namespace="Namespace"),
                ),
                "Namespace:Struct.EventB": CEvent(
                    name="EventB",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="EventHandler", namespace="Namespace"),
                ),
            },
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"Namespace.EventHandler"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_nested(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={
                "Namespace:Struct.NestedClass": CClass(
                    name="NestedClass",
                    namespace="Namespace",
                    nested=CType(name="Struct", namespace="Namespace"),
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "Namespace:Struct.NestedStruct": CStruct(
                    name="NestedStruct",
                    namespace="Namespace",
                    nested=CType(name="Struct", namespace="Namespace"),
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "Namespace:Struct.INestedInterface": CInterface(
                    name="INestedInterface",
                    namespace="Namespace",
                    nested=CType(name="Struct", namespace="Namespace"),
                    generic_args=(),
                    interfaces=(),
                    fields={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "Namespace:Struct.NestedEnum": CEnum(
                    name="NestedEnum",
                    namespace="Namespace",
                    nested=CType(name="Struct", namespace="Namespace"),
                    fields=(),
                ),
                "Namespace:Struct.NestedDelegate": CDelegate(
                    name="NestedDelegate",
                    namespace="Namespace",
                    nested=CType(name="Struct", namespace="Namespace"),
                    parameters=(),
                    return_type=CType(name="DelegateType", namespace="Namespace"),
                ),
            },
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"System.Enum", "Namespace.DelegateType"}

        self.assertEqual(manual, imports.c)

    def test_doc(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Struct": {
                        "doc": "Struct doc string.",
                    },
                },
            }
        )

        lines: Sequence[str] = build_struct(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Struct:",
            '    """Struct doc string."""',
        )

        self.assertEqual(manual, lines)


class TestBuildInterface(TestBase):
    def test_build(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_interface(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Interface:",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_generic(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(
                CType(name="K", namespace="Namespace", generic=True),
                CType(name="V", namespace="Namespace", generic=True),
            ),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_interface(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Interface(Generic[K, V]):",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_interfaces(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(
                CType(name="InterfaceA", namespace="Namespace"),
                CType(name="InterfaceB", namespace="Namespace"),
            ),
            fields={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_interface(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Interface(InterfaceA, InterfaceB):",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_fields(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={
                "Namespace:Interface.FieldA": CField(
                    name="FieldA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    return_type=CType(name="FieldType", namespace="Namespace"),
                ),
                "Namespace:Interface.FieldB": CField(
                    name="FieldB",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    return_type=CType(name="FieldType", namespace="Namespace"),
                ),
            },
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_interface(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Interface:",
            '    """"""',
            "    FieldA: Final[FieldType] = ...",
            '    """"""',
            "    FieldB: Final[FieldType] = ...",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_properties(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={
                "Namespace:Interface.PropertyA": CProperty(
                    name="PropertyA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="PropertyType", namespace="Namespace"),
                ),
                "Namespace:Interface.PropertyB": CProperty(
                    name="PropertyB",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="PropertyType", namespace="Namespace"),
                ),
            },
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_interface(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Interface:",
            '    """"""',
            "    @property",
            "    def PropertyA(self) -> PropertyType:",
            '        """"""',
            "    @property",
            "    def PropertyB(self) -> PropertyType:",
            '        """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_methods(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={
                "Namespace:Interface.MethodA(Namespace:ParamType, Namespace:ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                        CParameter(
                            name="param1", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
                "Namespace:Interface.MethodB(Namespace:ParamType, Namespace:ParamType)": CMethod(
                    name="MethodB",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                        CParameter(
                            name="param1", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
            },
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_interface(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Interface:",
            '    """"""',
            "    def MethodA(self, param0: ParamType, param1: ParamType) -> MethodType:",
            '        """"""',
            "    def MethodB(self, param0: ParamType, param1: ParamType) -> MethodType:",
            '        """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_methods_overload(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={
                "Namespace:Interface.MethodA(Namespace:ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
                "Namespace:Interface.MethodA(Namespace:ParamType, Namespace:ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                        CParameter(
                            name="param1", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
            },
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_interface(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Interface:",
            '    """"""',
            "    @overload",
            "    def MethodA(self, param0: ParamType) -> MethodType:",
            '        """"""',
            "    @overload",
            "    def MethodA(self, param0: ParamType, param1: ParamType) -> MethodType:",
            '        """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_events(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            events={
                "Namespace:Interface.EventA": CEvent(
                    name="EventA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="EventHandler", namespace="Namespace"),
                ),
                "Namespace:Interface.EventB": CEvent(
                    name="EventB",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="EventHandler", namespace="Namespace"),
                ),
            },
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_interface(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Interface:",
            '    """"""',
            "    EventA: EventType[EventHandler] = ...",
            '    """"""',
            "    EventB: EventType[EventHandler] = ...",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_nested(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            events={},
            nested_types={
                "Namespace:Interface.NestedClass": CClass(
                    name="NestedClass",
                    namespace="Namespace",
                    nested=CType(name="Interface", namespace="Namespace"),
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "Namespace:Interface.NestedStruct": CStruct(
                    name="NestedStruct",
                    namespace="Namespace",
                    nested=CType(name="Interface", namespace="Namespace"),
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "Namespace:Interface.INestedInterface": CInterface(
                    name="INestedInterface",
                    namespace="Namespace",
                    nested=CType(name="Interface", namespace="Namespace"),
                    generic_args=(),
                    interfaces=(),
                    fields={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "Namespace:Interface.NestedEnum": CEnum(
                    name="NestedEnum",
                    namespace="Namespace",
                    nested=CType(name="Interface", namespace="Namespace"),
                    fields=(),
                ),
                "Namespace:Interface.NestedDelegate": CDelegate(
                    name="NestedDelegate",
                    namespace="Namespace",
                    nested=CType(name="Interface", namespace="Namespace"),
                    parameters=(),
                    return_type=CType(name="DelegateType", namespace="Namespace"),
                ),
            },
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_interface(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Interface:",
            '    """"""',
            "    class NestedClass:",
            '        """"""',
            "    class NestedStruct:",
            '        """"""',
            "    class INestedInterface:",
            '        """"""',
            "    class NestedEnum(Enum):",
            '        """"""',
            "    NestedDelegate: Callable[[], DelegateType] = ...",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_py_imports(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_interface(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_py_imports_generic(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(
                CType(name="K", namespace="Namespace", generic=True),
                CType(name="V", namespace="Namespace", generic=True),
            ),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_interface(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"typing.Generic", "typing.TypeVar"}

        self.assertEqual(manual, imports.py)

    def test_py_imports_interfaces(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(
                CType(name="InterfaceA", namespace="Namespace"),
                CType(name="InterfaceB", namespace="Namespace"),
            ),
            fields={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_interface(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_py_imports_fields(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={
                "Namespace:Interface.FieldA": CField(
                    name="FieldA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    return_type=CType(name="FieldType", namespace="Namespace"),
                ),
                "Namespace:Interface.FieldB": CField(
                    name="FieldB",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    return_type=CType(name="FieldType", namespace="Namespace"),
                ),
            },
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_interface(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"typing.Final"}

        self.assertEqual(manual, imports.py)

    def test_py_imports_properties(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={
                "Namespace:Interface.PropertyA": CProperty(
                    name="PropertyA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="PropertyType", namespace="Namespace"),
                ),
                "Namespace:Interface.PropertyB": CProperty(
                    name="PropertyB",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="PropertyType", namespace="Namespace"),
                ),
            },
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_interface(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_py_imports_methods(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={
                "Namespace:Interface.MethodA(Namespace:ParamType, Namespace:ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                        CParameter(
                            name="param1", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
                "Namespace:Interface.MethodB(Namespace:ParamType, Namespace:ParamType)": CMethod(
                    name="MethodB",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                        CParameter(
                            name="param1", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
            },
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_interface(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_py_imports_methods_overload(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={
                "Namespace:Interface.MethodA(Namespace:ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
                "Namespace:Interface.MethodA(Namespace:ParamType, Namespace:ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                        CParameter(
                            name="param1", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
            },
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_interface(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"typing.overload"}

        self.assertEqual(manual, imports.py)

    def test_py_imports_events(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            events={
                "Namespace:Interface.EventA": CEvent(
                    name="EventA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="EventHandler", namespace="Namespace"),
                ),
                "Namespace:Interface.EventB": CEvent(
                    name="EventB",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="EventHandler", namespace="Namespace"),
                ),
            },
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_interface(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_py_imports_nested(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            events={},
            nested_types={
                "Namespace:Interface.NestedClass": CClass(
                    name="NestedClass",
                    namespace="Namespace",
                    nested=CType(name="Interface", namespace="Namespace"),
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "Namespace:Interface.NestedStruct": CStruct(
                    name="NestedStruct",
                    namespace="Namespace",
                    nested=CType(name="Interface", namespace="Namespace"),
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "Namespace:Interface.INestedInterface": CInterface(
                    name="INestedInterface",
                    namespace="Namespace",
                    nested=CType(name="Interface", namespace="Namespace"),
                    generic_args=(),
                    interfaces=(),
                    fields={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "Namespace:Interface.NestedEnum": CEnum(
                    name="NestedEnum",
                    namespace="Namespace",
                    nested=CType(name="Interface", namespace="Namespace"),
                    fields=(),
                ),
                "Namespace:Interface.NestedDelegate": CDelegate(
                    name="NestedDelegate",
                    namespace="Namespace",
                    nested=CType(name="Interface", namespace="Namespace"),
                    parameters=(),
                    return_type=CType(name="DelegateType", namespace="Namespace"),
                ),
            },
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_interface(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"typing.Callable"}

        self.assertEqual(manual, imports.py)

    def test_c_imports(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_interface(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.c)

    def test_c_imports_generic(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(
                CType(name="K", namespace="Namespace", generic=True),
                CType(name="V", namespace="Namespace", generic=True),
            ),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_interface(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.c)

    def test_c_imports_interfaces(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(
                CType(name="InterfaceA", namespace="Namespace"),
                CType(name="InterfaceB", namespace="Namespace"),
            ),
            fields={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_interface(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"Namespace.InterfaceA", "Namespace.InterfaceB"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_fields(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={
                "Namespace:Interface.FieldA": CField(
                    name="FieldA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    return_type=CType(name="FieldType", namespace="Namespace"),
                ),
                "Namespace:Interface.FieldB": CField(
                    name="FieldB",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    return_type=CType(name="FieldType", namespace="Namespace"),
                ),
            },
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_interface(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"Namespace.FieldType"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_properties(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={
                "Namespace:Interface.PropertyA": CProperty(
                    name="PropertyA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="PropertyType", namespace="Namespace"),
                ),
                "Namespace:Interface.PropertyB": CProperty(
                    name="PropertyB",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="PropertyType", namespace="Namespace"),
                ),
            },
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_interface(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"Namespace.PropertyType"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_methods(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={
                "Namespace:Interface.MethodA(Namespace:ParamType, Namespace:ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                        CParameter(
                            name="param1", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
                "Namespace:Interface.MethodB(Namespace:ParamType, Namespace:ParamType)": CMethod(
                    name="MethodB",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                        CParameter(
                            name="param1", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
            },
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_interface(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"Namespace.MethodType", "Namespace.ParamType"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_methods_overload(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={
                "Namespace:Interface.MethodA(Namespace:ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
                "Namespace:Interface.MethodA(Namespace:ParamType, Namespace:ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0", type=CType(name="ParamType", namespace="Namespace")
                        ),
                        CParameter(
                            name="param1", type=CType(name="ParamType", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="MethodType", namespace="Namespace"),),
                ),
            },
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_interface(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"Namespace.MethodType", "Namespace.ParamType"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_events(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            events={
                "Namespace:Interface.EventA": CEvent(
                    name="EventA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="EventHandler", namespace="Namespace"),
                ),
                "Namespace:Interface.EventB": CEvent(
                    name="EventB",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="EventHandler", namespace="Namespace"),
                ),
            },
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_interface(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"Namespace.EventHandler"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_nested(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            events={},
            nested_types={
                "Namespace:Interface.NestedClass": CClass(
                    name="NestedClass",
                    namespace="Namespace",
                    nested=CType(name="Interface", namespace="Namespace"),
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "Namespace:Interface.NestedStruct": CStruct(
                    name="NestedStruct",
                    namespace="Namespace",
                    nested=CType(name="Interface", namespace="Namespace"),
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "Namespace:Interface.INestedInterface": CInterface(
                    name="INestedInterface",
                    namespace="Namespace",
                    nested=CType(name="Interface", namespace="Namespace"),
                    generic_args=(),
                    interfaces=(),
                    fields={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "Namespace:Interface.NestedEnum": CEnum(
                    name="NestedEnum",
                    namespace="Namespace",
                    nested=CType(name="Interface", namespace="Namespace"),
                    fields=(),
                ),
                "Namespace:Interface.NestedDelegate": CDelegate(
                    name="NestedDelegate",
                    namespace="Namespace",
                    nested=CType(name="Interface", namespace="Namespace"),
                    parameters=(),
                    return_type=CType(name="DelegateType", namespace="Namespace"),
                ),
            },
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_interface(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"System.Enum", "Namespace.DelegateType"}

        self.assertEqual(manual, imports.c)

    def test_doc(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Interface": {
                        "doc": "Interface doc string.",
                    },
                },
            }
        )

        lines: Sequence[str] = build_interface(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Interface:",
            '    """Interface doc string."""',
        )

        self.assertEqual(manual, lines)


class TestBuildEnum(TestBase):
    def test_build(self) -> None:
        type_def: CEnum = CEnum(
            name="Enum",
            namespace="Namespace",
            nested=None,
            fields=("FieldA", "FieldB", "FieldC", "FieldD"),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_enum(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Enum(Enum):",
            '    """"""',
            "    FieldA: Enum = ...",
            '    """"""',
            "    FieldB: Enum = ...",
            '    """"""',
            "    FieldC: Enum = ...",
            '    """"""',
            "    FieldD: Enum = ...",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_no_fields(self) -> None:
        type_def: CEnum = CEnum(
            name="Enum",
            namespace="Namespace",
            nested=None,
            fields=(),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_enum(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Enum(Enum):",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_py_imports(self) -> None:
        type_def: CEnum = CEnum(
            name="Enum",
            namespace="Namespace",
            nested=None,
            fields=("FieldA", "FieldB", "FieldC", "FieldD"),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_enum(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_py_imports_no_fields(self) -> None:
        type_def: CEnum = CEnum(
            name="Enum",
            namespace="Namespace",
            nested=None,
            fields=(),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_enum(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_c_imports(self) -> None:
        type_def: CEnum = CEnum(
            name="Enum",
            namespace="Namespace",
            nested=None,
            fields=("FieldA", "FieldB", "FieldC", "FieldD"),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_enum(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"System.Enum"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_no_fields(self) -> None:
        type_def: CEnum = CEnum(
            name="Enum",
            namespace="Namespace",
            nested=None,
            fields=(),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_enum(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"System.Enum"}

        self.assertEqual(manual, imports.c)

    def test_doc(self) -> None:
        type_def: CEnum = CEnum(
            name="Enum",
            namespace="Namespace",
            nested=None,
            fields=("FieldA", "FieldB", "FieldC", "FieldD"),
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Enum": {
                        "doc": "Enum doc string.",
                        "FieldA": {"doc": "FieldA doc string."},
                        "FieldB": {"doc": "FieldB doc string."},
                        "FieldC": {"doc": "FieldC doc string."},
                        "FieldD": {"doc": "FieldD doc string."},
                    },
                },
            }
        )

        lines: Sequence[str] = build_enum(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Enum(Enum):",
            '    """Enum doc string."""',
            "    FieldA: Enum = ...",
            '    """FieldA doc string."""',
            "    FieldB: Enum = ...",
            '    """FieldB doc string."""',
            "    FieldC: Enum = ...",
            '    """FieldC doc string."""',
            "    FieldD: Enum = ...",
            '    """FieldD doc string."""',
        )

        self.assertEqual(manual, lines)

    def test_doc_no_fields(self) -> None:
        type_def: CEnum = CEnum(
            name="Enum",
            namespace="Namespace",
            nested=None,
            fields=(),
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Enum": {
                        "doc": "Enum doc string.",
                    },
                },
            }
        )

        lines: Sequence[str] = build_enum(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "class Enum(Enum):",
            '    """Enum doc string."""',
        )

        self.assertEqual(manual, lines)


class TestBuildDelegate(TestBase):
    def test_build(self) -> None:
        type_def: CDelegate = CDelegate(
            name="Delegate",
            namespace="Namespace",
            nested=None,
            parameters=(
                CParameter(name="param0", type=CType(name="ParamType", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="ParamType", namespace="Namespace")),
            ),
            return_type=CType(name="ReturnType", namespace="Namespace"),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_delegate(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "Delegate: Callable[[ParamType, ParamType], ReturnType] = ...",
            '""""""',
        )

        self.assertEqual(manual, lines)

    def test_build_no_params(self) -> None:
        type_def: CDelegate = CDelegate(
            name="Delegate",
            namespace="Namespace",
            nested=None,
            parameters=(),
            return_type=CType(name="ReturnType", namespace="Namespace"),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_delegate(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "Delegate: Callable[[], ReturnType] = ...",
            '""""""',
        )

        self.assertEqual(manual, lines)

    def test_py_imports(self) -> None:
        type_def: CDelegate = CDelegate(
            name="Delegate",
            namespace="Namespace",
            nested=None,
            parameters=(
                CParameter(name="param0", type=CType(name="ParamType", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="ParamType", namespace="Namespace")),
            ),
            return_type=CType(name="ReturnType", namespace="Namespace"),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_delegate(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"typing.Callable"}

        self.assertEqual(manual, imports.py)

    def test_py_imports_no_params(self) -> None:
        type_def: CDelegate = CDelegate(
            name="Delegate",
            namespace="Namespace",
            nested=None,
            parameters=(),
            return_type=CType(name="ReturnType", namespace="Namespace"),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_delegate(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"typing.Callable"}

        self.assertEqual(manual, imports.py)

    def test_c_imports(self) -> None:
        type_def: CDelegate = CDelegate(
            name="Delegate",
            namespace="Namespace",
            nested=None,
            parameters=(
                CParameter(name="param0", type=CType(name="ParamType", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="ParamType", namespace="Namespace")),
            ),
            return_type=CType(name="ReturnType", namespace="Namespace"),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_delegate(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"Namespace.ParamType", "Namespace.ReturnType"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_no_params(self) -> None:
        type_def: CDelegate = CDelegate(
            name="Delegate",
            namespace="Namespace",
            nested=None,
            parameters=(),
            return_type=CType(name="ReturnType", namespace="Namespace"),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_delegate(type_def=type_def, imports=imports, doc=doc)
        manual: Set[str] = {"Namespace.ReturnType"}

        self.assertEqual(manual, imports.c)

    def test_doc(self) -> None:
        type_def: CDelegate = CDelegate(
            name="Delegate",
            namespace="Namespace",
            nested=None,
            parameters=(
                CParameter(name="param0", type=CType(name="ParamType", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="ParamType", namespace="Namespace")),
            ),
            return_type=CType(name="ReturnType", namespace="Namespace"),
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Delegate": {
                        "doc": "Delegate doc string.",
                        "parameters": {
                            "param0": "Parameter 0 doc string.",
                            "param1": "Parameter 1 doc string.",
                        },
                        "return": "Return doc string.",
                    },
                },
            }
        )

        lines: Sequence[str] = build_delegate(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "Delegate: Callable[[ParamType, ParamType], ReturnType] = ...",
            '"""Delegate doc string.',
            "",
            ":param param0: Parameter 0 doc string.",
            ":param param1: Parameter 1 doc string.",
            ":return: Return doc string.",
            '"""',
        )

        self.assertEqual(manual, lines)

    def test_doc_no_params(self) -> None:
        type_def: CDelegate = CDelegate(
            name="Delegate",
            namespace="Namespace",
            nested=None,
            parameters=(),
            return_type=CType(name="ReturnType", namespace="Namespace"),
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Delegate": {
                        "doc": "Delegate doc string.",
                        "return": "Return doc string.",
                    },
                },
            }
        )

        lines: Sequence[str] = build_delegate(type_def=type_def, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "Delegate: Callable[[], ReturnType] = ...",
            '"""Delegate doc string.',
            "",
            ":return: Return doc string.",
            '"""',
        )

        self.assertEqual(manual, lines)


class TestBuildField(TestBase):
    def test_build(self) -> None:
        field: CField = CField(
            name="Field",
            declaring_type=CType(name="Type", namespace="Namespace"),
            return_type=CType(name="ReturnType", namespace="Namespace"),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_field(field=field, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "Field: Final[ReturnType] = ...",
            '""""""',
        )

        self.assertEqual(manual, lines)

    def test_build_static(self) -> None:
        field: CField = CField(
            name="Field",
            declaring_type=CType(name="Type", namespace="Namespace"),
            return_type=CType(name="ReturnType", namespace="Namespace"),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_field(field=field, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "Field: Final[ClassVar[ReturnType]] = ...",
            '""""""',
        )

        self.assertEqual(manual, lines)

    def test_py_imports(self) -> None:
        field: CField = CField(
            name="Field",
            declaring_type=CType(name="Type", namespace="Namespace"),
            return_type=CType(name="ReturnType", namespace="Namespace"),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_field(field=field, imports=imports, doc=doc)
        manual: Set[str] = {"typing.Final"}

        self.assertEqual(manual, imports.py)

    def test_py_imports_static(self) -> None:
        field: CField = CField(
            name="Field",
            declaring_type=CType(name="Type", namespace="Namespace"),
            return_type=CType(name="ReturnType", namespace="Namespace"),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_field(field=field, imports=imports, doc=doc)
        manual: Set[str] = {"typing.Final", "typing.ClassVar"}

        self.assertEqual(manual, imports.py)

    def test_c_imports(self) -> None:
        field: CField = CField(
            name="Field",
            declaring_type=CType(name="Type", namespace="Namespace"),
            return_type=CType(name="ReturnType", namespace="Namespace"),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_field(field=field, imports=imports, doc=doc)
        manual: Set[str] = {"Namespace.ReturnType"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_static(self) -> None:
        field: CField = CField(
            name="Field",
            declaring_type=CType(name="Type", namespace="Namespace"),
            return_type=CType(name="ReturnType", namespace="Namespace"),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_field(field=field, imports=imports, doc=doc)
        manual: Set[str] = {"Namespace.ReturnType"}

        self.assertEqual(manual, imports.c)

    def test_doc(self) -> None:
        field: CField = CField(
            name="Field",
            declaring_type=CType(name="Type", namespace="Namespace"),
            return_type=CType(name="ReturnType", namespace="Namespace"),
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Type": {"Field": {"doc": "Field doc string."}},
                },
            },
        )

        lines: Sequence[str] = build_field(field=field, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "Field: Final[ReturnType] = ...",
            '"""Field doc string."""',
        )

        self.assertEqual(manual, lines)

    def test_doc_static(self) -> None:
        field: CField = CField(
            name="Field",
            declaring_type=CType(name="Type", namespace="Namespace"),
            return_type=CType(name="ReturnType", namespace="Namespace"),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Type": {"Field": {"doc": "Field doc string."}},
                },
            },
        )

        lines: Sequence[str] = build_field(field=field, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "Field: Final[ClassVar[ReturnType]] = ...",
            '"""Field doc string."""',
        )

        self.assertEqual(manual, lines)


class TestBuildConstructor(TestBase):
    def test_build(self) -> None:
        constructor: CConstructor = CConstructor(
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_constructor(
            constructor=constructor,
            imports=imports,
            doc=doc,
            overload=False,
        )
        manual: Sequence[str] = (
            "def __init__(self, param0: Param, param1: Param):",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_overload(self) -> None:
        constructor: CConstructor = CConstructor(
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_constructor(
            constructor=constructor,
            imports=imports,
            doc=doc,
            overload=True,
        )
        manual: Sequence[str] = (
            "@overload",
            "def __init__(self, param0: Param, param1: Param):",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_no_parameters(self) -> None:
        constructor: CConstructor = CConstructor(
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_constructor(
            constructor=constructor,
            imports=imports,
            doc=doc,
            overload=False,
        )
        manual: Sequence[str] = (
            "def __init__(self):",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_no_parameters_overload(self) -> None:
        constructor: CConstructor = CConstructor(
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_constructor(
            constructor=constructor,
            imports=imports,
            doc=doc,
            overload=True,
        )
        manual: Sequence[str] = (
            "@overload",
            "def __init__(self):",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_py_imports_parameters(self) -> None:
        constructor: CConstructor = CConstructor(
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_constructor(
            constructor=constructor,
            imports=imports,
            doc=doc,
            overload=False,
        )
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_py_imports_parameters_overload(self) -> None:
        constructor: CConstructor = CConstructor(
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_constructor(
            constructor=constructor,
            imports=imports,
            doc=doc,
            overload=True,
        )
        manual: Set[str] = {"typing.overload"}

        self.assertEqual(manual, imports.py)

    def test_py_imports_parameters_none(self) -> None:
        constructor: CConstructor = CConstructor(
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_constructor(
            constructor=constructor,
            imports=imports,
            doc=doc,
            overload=False,
        )
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_py_imports_parameters_none_overload(self) -> None:
        constructor: CConstructor = CConstructor(
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_constructor(
            constructor=constructor,
            imports=imports,
            doc=doc,
            overload=True,
        )
        manual: Set[str] = {"typing.overload"}

        self.assertEqual(manual, imports.py)

    def test_c_imports_parameters(self) -> None:
        constructor: CConstructor = CConstructor(
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_constructor(
            constructor=constructor,
            imports=imports,
            doc=doc,
            overload=False,
        )
        manual: Set[str] = {"Namespace.Param"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_parameters_overload(self) -> None:
        constructor: CConstructor = CConstructor(
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_constructor(
            constructor=constructor,
            imports=imports,
            doc=doc,
            overload=True,
        )
        manual: Set[str] = {"Namespace.Param"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_parameters_none(self) -> None:
        constructor: CConstructor = CConstructor(
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_constructor(
            constructor=constructor,
            imports=imports,
            doc=doc,
            overload=False,
        )
        manual: Set[str] = set()

        self.assertEqual(manual, imports.c)

    def test_c_imports_parameters_none_overload(self) -> None:
        constructor: CConstructor = CConstructor(
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_constructor(
            constructor=constructor,
            imports=imports,
            doc=doc,
            overload=True,
        )
        manual: Set[str] = set()

        self.assertEqual(manual, imports.c)

    def test_doc_parameters(self) -> None:
        constructor: CConstructor = CConstructor(
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Type": {
                        "__init__(Namespace:Param, Namespace:Param)": {
                            "doc": "Constructor doc string.",
                            "parameters": {
                                "param0": "Parameter 0 doc string.",
                                "param1": "Parameter 1 doc string.",
                            },
                        }
                    },
                },
            },
        )

        lines: Sequence[str] = build_constructor(
            constructor=constructor,
            imports=imports,
            doc=doc,
            overload=False,
        )
        manual: Sequence[str] = (
            "def __init__(self, param0: Param, param1: Param):",
            '    """Constructor doc string.',
            "    ",
            "    :param param0: Parameter 0 doc string.",
            "    :param param1: Parameter 1 doc string.",
            '    """',
        )

        self.assertEqual(manual, lines)

    def test_doc_parameters_overload(self) -> None:
        constructor: CConstructor = CConstructor(
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Type": {
                        "__init__(Namespace:Param, Namespace:Param)": {
                            "doc": "Constructor doc string.",
                            "parameters": {
                                "param0": "Parameter 0 doc string.",
                                "param1": "Parameter 1 doc string.",
                            },
                        }
                    },
                },
            },
        )

        lines: Sequence[str] = build_constructor(
            constructor=constructor,
            imports=imports,
            doc=doc,
            overload=True,
        )
        manual: Sequence[str] = (
            "@overload",
            "def __init__(self, param0: Param, param1: Param):",
            '    """Constructor doc string.',
            "    ",
            "    :param param0: Parameter 0 doc string.",
            "    :param param1: Parameter 1 doc string.",
            '    """',
        )

        self.assertEqual(manual, lines)

    def test_doc_parameters_none(self) -> None:
        constructor: CConstructor = CConstructor(
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Type": {
                        "__init__()": {
                            "doc": "Constructor doc string.",
                        }
                    },
                },
            },
        )

        lines: Sequence[str] = build_constructor(
            constructor=constructor,
            imports=imports,
            doc=doc,
            overload=False,
        )
        manual: Sequence[str] = (
            "def __init__(self):",
            '    """Constructor doc string."""',
        )

        self.assertEqual(manual, lines)

    def test_doc_parameters_none_overload(self) -> None:
        constructor: CConstructor = CConstructor(
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Type": {
                        "__init__()": {
                            "doc": "Constructor doc string.",
                        }
                    },
                },
            },
        )

        lines: Sequence[str] = build_constructor(
            constructor=constructor,
            imports=imports,
            doc=doc,
            overload=True,
        )
        manual: Sequence[str] = (
            "@overload",
            "def __init__(self):",
            '    """Constructor doc string."""',
        )

        self.assertEqual(manual, lines)


class TestBuildProperty(TestBase):
    def test_build(self) -> None:
        property: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="PropertyType", namespace="Namespace"),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_property(property=property, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "@property",
            "def Property(self) -> PropertyType:",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_setter(self) -> None:
        property: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="PropertyType", namespace="Namespace"),
            setter=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_property(property=property, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "@property",
            "def Property(self) -> PropertyType:",
            '    """"""',
            "@Property.setter",
            "def Property(self, value: PropertyType) -> None: ...",
        )

        self.assertEqual(manual, lines)

    def test_build_static(self) -> None:
        property: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="PropertyType", namespace="Namespace"),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_property(property=property, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "@classmethod",
            "@property",
            "def Property(cls) -> PropertyType:",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_setter_static(self) -> None:
        property: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="PropertyType", namespace="Namespace"),
            setter=True,
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_property(property=property, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "@classmethod",
            "@property",
            "def Property(cls) -> PropertyType:",
            '    """"""',
            "@classmethod",
            "@Property.setter",
            "def Property(cls, value: PropertyType) -> None: ...",
        )

        self.assertEqual(manual, lines)

    def test_py_imports(self) -> None:
        property: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="PropertyType", namespace="Namespace"),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_property(property=property, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_py_imports_setter(self) -> None:
        property: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="PropertyType", namespace="Namespace"),
            setter=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_property(property=property, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_py_imports_static(self) -> None:
        property: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="PropertyType", namespace="Namespace"),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_property(property=property, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_py_imports_setter_static(self) -> None:
        property: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="PropertyType", namespace="Namespace"),
            setter=True,
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_property(property=property, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_c_imports(self) -> None:
        property: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="PropertyType", namespace="Namespace"),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_property(property=property, imports=imports, doc=doc)
        manual: Set[str] = {"Namespace.PropertyType"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_setter(self) -> None:
        property: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="PropertyType", namespace="Namespace"),
            setter=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_property(property=property, imports=imports, doc=doc)
        manual: Set[str] = {"Namespace.PropertyType"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_static(self) -> None:
        property: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="PropertyType", namespace="Namespace"),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_property(property=property, imports=imports, doc=doc)
        manual: Set[str] = {"Namespace.PropertyType"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_setter_static(self) -> None:
        property: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="PropertyType", namespace="Namespace"),
            setter=True,
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_property(property=property, imports=imports, doc=doc)
        manual: Set[str] = {"Namespace.PropertyType"}

        self.assertEqual(manual, imports.c)

    def test_doc(self) -> None:
        property: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="PropertyType", namespace="Namespace"),
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Type": {
                        "Property": {
                            "doc": "Property doc string.",
                            "return": "Property return string.",
                        },
                    },
                },
            }
        )

        lines: Sequence[str] = build_property(property=property, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "@property",
            "def Property(self) -> PropertyType:",
            '    """Property doc string.',
            "    ",
            "    :return: Property return string.",
            '    """',
        )

        self.assertEqual(manual, lines)

    def test_doc_setter(self) -> None:
        property: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="PropertyType", namespace="Namespace"),
            setter=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Type": {
                        "Property": {
                            "doc": "Property doc string.",
                            "return": "Property return string.",
                        },
                    },
                },
            }
        )

        lines: Sequence[str] = build_property(property=property, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "@property",
            "def Property(self) -> PropertyType:",
            '    """Property doc string.',
            "    ",
            "    :return: Property return string.",
            '    """',
            "@Property.setter",
            "def Property(self, value: PropertyType) -> None: ...",
        )

        self.assertEqual(manual, lines)

    def test_doc_static(self) -> None:
        property: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="PropertyType", namespace="Namespace"),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Type": {
                        "Property": {
                            "doc": "Property doc string.",
                            "return": "Property return string.",
                        },
                    },
                },
            }
        )

        lines: Sequence[str] = build_property(property=property, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "@classmethod",
            "@property",
            "def Property(cls) -> PropertyType:",
            '    """Property doc string.',
            "    ",
            "    :return: Property return string.",
            '    """',
        )

        self.assertEqual(manual, lines)

    def test_doc_setter_static(self) -> None:
        property: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="PropertyType", namespace="Namespace"),
            setter=True,
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Type": {
                        "Property": {
                            "doc": "Property doc string.",
                            "return": "Property return string.",
                        },
                    },
                },
            }
        )

        lines: Sequence[str] = build_property(property=property, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "@classmethod",
            "@property",
            "def Property(cls) -> PropertyType:",
            '    """Property doc string.',
            "    ",
            "    :return: Property return string.",
            '    """',
            "@classmethod",
            "@Property.setter",
            "def Property(cls, value: PropertyType) -> None: ...",
        )

        self.assertEqual(manual, lines)


class TestBuildMethod(TestBase):
    def test_build(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(CType(name="Return", namespace="Namespace"),),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Sequence[str] = (
            "def Method(self, param0: Param, param1: Param) -> Return:",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(CType(name="Return", namespace="Namespace"),),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Sequence[str] = (
            "@classmethod",
            "def Method(cls, param0: Param, param1: Param) -> Return:",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_overload(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(CType(name="Return", namespace="Namespace"),),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Sequence[str] = (
            "@overload",
            "def Method(self, param0: Param, param1: Param) -> Return:",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_overload_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(CType(name="Return", namespace="Namespace"),),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Sequence[str] = (
            "@classmethod",
            "@overload",
            "def Method(cls, param0: Param, param1: Param) -> Return:",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_no_params(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(CType(name="Return", namespace="Namespace"),),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Sequence[str] = (
            "def Method(self) -> Return:",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_no_params_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(CType(name="Return", namespace="Namespace"),),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Sequence[str] = (
            "@classmethod",
            "def Method(cls) -> Return:",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_no_params_overload(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(CType(name="Return", namespace="Namespace"),),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Sequence[str] = (
            "@overload",
            "def Method(self) -> Return:",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_no_params_overload_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(CType(name="Return", namespace="Namespace"),),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Sequence[str] = (
            "@classmethod",
            "@overload",
            "def Method(cls) -> Return:",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_returns(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Sequence[str] = (
            "def Method(self, param0: Param, param1: Param) -> Tuple[Return, Return]:",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_returns_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Sequence[str] = (
            "@classmethod",
            "def Method(cls, param0: Param, param1: Param) -> Tuple[Return, Return]:",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_returns_overload(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Sequence[str] = (
            "@overload",
            "def Method(self, param0: Param, param1: Param) -> Tuple[Return, Return]:",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_returns_overload_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Sequence[str] = (
            "@classmethod",
            "@overload",
            "def Method(cls, param0: Param, param1: Param) -> Tuple[Return, Return]:",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_returns_no_params(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Sequence[str] = (
            "def Method(self) -> Tuple[Return, Return]:",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_returns_no_params_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Sequence[str] = (
            "@classmethod",
            "def Method(cls) -> Tuple[Return, Return]:",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_returns_no_params_overload(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Sequence[str] = (
            "@overload",
            "def Method(self) -> Tuple[Return, Return]:",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_build_returns_no_params_overload_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Sequence[str] = (
            "@classmethod",
            "@overload",
            "def Method(cls) -> Tuple[Return, Return]:",
            '    """"""',
        )

        self.assertEqual(manual, lines)

    def test_py_imports(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(CType(name="Return", namespace="Namespace"),),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_py_imports_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(CType(name="Return", namespace="Namespace"),),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_py_imports_overload(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(CType(name="Return", namespace="Namespace"),),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Set[str] = {"typing.overload"}

        self.assertEqual(manual, imports.py)

    def test_py_imports_overload_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(CType(name="Return", namespace="Namespace"),),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Set[str] = {"typing.overload"}

        self.assertEqual(manual, imports.py)

    def test_py_imports_no_params(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(CType(name="Return", namespace="Namespace"),),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_py_imports_no_params_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(CType(name="Return", namespace="Namespace"),),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_py_imports_no_params_overload(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(CType(name="Return", namespace="Namespace"),),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Set[str] = {"typing.overload"}

        self.assertEqual(manual, imports.py)

    def test_py_imports_no_params_overload_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(CType(name="Return", namespace="Namespace"),),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Set[str] = {"typing.overload"}

        self.assertEqual(manual, imports.py)

    def test_py_imports_returns(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Set[str] = {"typing.Tuple"}

        self.assertEqual(manual, imports.py)

    def test_py_imports_returns_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Set[str] = {"typing.Tuple"}

        self.assertEqual(manual, imports.py)

    def test_py_imports_returns_overload(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Set[str] = {"typing.overload", "typing.Tuple"}

        self.assertEqual(manual, imports.py)

    def test_py_imports_returns_overload_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Set[str] = {"typing.overload", "typing.Tuple"}

        self.assertEqual(manual, imports.py)

    def test_py_imports_returns_no_params(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Set[str] = {"typing.Tuple"}

        self.assertEqual(manual, imports.py)

    def test_py_imports_returns_no_params_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Set[str] = {"typing.Tuple"}

        self.assertEqual(manual, imports.py)

    def test_py_imports_returns_no_params_overload(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Set[str] = {"typing.overload", "typing.Tuple"}

        self.assertEqual(manual, imports.py)

    def test_py_imports_returns_no_params_overload_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Set[str] = {"typing.overload", "typing.Tuple"}

        self.assertEqual(manual, imports.py)

    def test_c_imports(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(CType(name="Return", namespace="Namespace"),),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Set[str] = {"Namespace.Param", "Namespace.Return"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(CType(name="Return", namespace="Namespace"),),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Set[str] = {"Namespace.Param", "Namespace.Return"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_overload(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(CType(name="Return", namespace="Namespace"),),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Set[str] = {"Namespace.Param", "Namespace.Return"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_overload_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(CType(name="Return", namespace="Namespace"),),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Set[str] = {"Namespace.Param", "Namespace.Return"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_no_params(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(CType(name="Return", namespace="Namespace"),),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Set[str] = {"Namespace.Return"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_no_params_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(CType(name="Return", namespace="Namespace"),),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Set[str] = {"Namespace.Return"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_no_params_overload(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(CType(name="Return", namespace="Namespace"),),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Set[str] = {"Namespace.Return"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_no_params_overload_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(CType(name="Return", namespace="Namespace"),),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Set[str] = {"Namespace.Return"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_returns(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Set[str] = {"Namespace.Param", "Namespace.Return"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_returns_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Set[str] = {"Namespace.Param", "Namespace.Return"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_returns_overload(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Set[str] = {"Namespace.Param", "Namespace.Return"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_returns_overload_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Set[str] = {"Namespace.Param", "Namespace.Return"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_returns_no_params(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Set[str] = {"Namespace.Return"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_returns_no_params_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Set[str] = {"Namespace.Return"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_returns_no_params_overload(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Set[str] = {"Namespace.Return"}

        self.assertEqual(manual, imports.c)

    def test_c_imports_returns_no_params_overload_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Set[str] = {"Namespace.Return"}

        self.assertEqual(manual, imports.c)

    def test_doc(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(CType(name="Return", namespace="Namespace"),),
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Type": {
                        "Method(Namespace:Param, Namespace:Param)": {
                            "doc": "Method doc string.",
                            "parameters": {
                                "param0": "Parameter 0 doc string.",
                                "param1": "Parameter 1 doc string.",
                            },
                            "return": "Return doc string.",
                        },
                    },
                },
            }
        )

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Sequence[str] = (
            "def Method(self, param0: Param, param1: Param) -> Return:",
            '    """Method doc string.',
            "    ",
            "    :param param0: Parameter 0 doc string.",
            "    :param param1: Parameter 1 doc string.",
            "    :return: Return doc string.",
            '    """',
        )

        self.assertEqual(manual, lines)

    def test_doc_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(CType(name="Return", namespace="Namespace"),),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Type": {
                        "Method(Namespace:Param, Namespace:Param)": {
                            "doc": "Method doc string.",
                            "parameters": {
                                "param0": "Parameter 0 doc string.",
                                "param1": "Parameter 1 doc string.",
                            },
                            "return": "Return doc string.",
                        },
                    },
                },
            }
        )

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Sequence[str] = (
            "@classmethod",
            "def Method(cls, param0: Param, param1: Param) -> Return:",
            '    """Method doc string.',
            "    ",
            "    :param param0: Parameter 0 doc string.",
            "    :param param1: Parameter 1 doc string.",
            "    :return: Return doc string.",
            '    """',
        )

        self.assertEqual(manual, lines)

    def test_doc_overload(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(CType(name="Return", namespace="Namespace"),),
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Type": {
                        "Method(Namespace:Param, Namespace:Param)": {
                            "doc": "Method doc string.",
                            "parameters": {
                                "param0": "Parameter 0 doc string.",
                                "param1": "Parameter 1 doc string.",
                            },
                            "return": "Return doc string.",
                        },
                    },
                },
            }
        )

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Sequence[str] = (
            "@overload",
            "def Method(self, param0: Param, param1: Param) -> Return:",
            '    """Method doc string.',
            "    ",
            "    :param param0: Parameter 0 doc string.",
            "    :param param1: Parameter 1 doc string.",
            "    :return: Return doc string.",
            '    """',
        )

        self.assertEqual(manual, lines)

    def test_doc_overload_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(CType(name="Return", namespace="Namespace"),),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Type": {
                        "Method(Namespace:Param, Namespace:Param)": {
                            "doc": "Method doc string.",
                            "parameters": {
                                "param0": "Parameter 0 doc string.",
                                "param1": "Parameter 1 doc string.",
                            },
                            "return": "Return doc string.",
                        },
                    },
                },
            }
        )

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Sequence[str] = (
            "@classmethod",
            "@overload",
            "def Method(cls, param0: Param, param1: Param) -> Return:",
            '    """Method doc string.',
            "    ",
            "    :param param0: Parameter 0 doc string.",
            "    :param param1: Parameter 1 doc string.",
            "    :return: Return doc string.",
            '    """',
        )

        self.assertEqual(manual, lines)

    def test_doc_no_params(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(CType(name="Return", namespace="Namespace"),),
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Type": {
                        "Method()": {
                            "doc": "Method doc string.",
                            "return": "Return doc string.",
                        },
                    },
                },
            }
        )

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Sequence[str] = (
            "def Method(self) -> Return:",
            '    """Method doc string.',
            "    ",
            "    :return: Return doc string.",
            '    """',
        )

        self.assertEqual(manual, lines)

    def test_doc_no_params_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(CType(name="Return", namespace="Namespace"),),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Type": {
                        "Method()": {
                            "doc": "Method doc string.",
                            "return": "Return doc string.",
                        },
                    },
                },
            }
        )

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Sequence[str] = (
            "@classmethod",
            "def Method(cls) -> Return:",
            '    """Method doc string.',
            "    ",
            "    :return: Return doc string.",
            '    """',
        )

        self.assertEqual(manual, lines)

    def test_doc_no_params_overload(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(CType(name="Return", namespace="Namespace"),),
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Type": {
                        "Method()": {
                            "doc": "Method doc string.",
                            "return": "Return doc string.",
                        },
                    },
                },
            }
        )

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Sequence[str] = (
            "@overload",
            "def Method(self) -> Return:",
            '    """Method doc string.',
            "    ",
            "    :return: Return doc string.",
            '    """',
        )

        self.assertEqual(manual, lines)

    def test_doc_no_params_overload_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(CType(name="Return", namespace="Namespace"),),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Type": {
                        "Method()": {
                            "doc": "Method doc string.",
                            "return": "Return doc string.",
                        },
                    },
                },
            }
        )

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Sequence[str] = (
            "@classmethod",
            "@overload",
            "def Method(cls) -> Return:",
            '    """Method doc string.',
            "    ",
            "    :return: Return doc string.",
            '    """',
        )

        self.assertEqual(manual, lines)

    def test_doc_returns(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Type": {
                        "Method(Namespace:Param, Namespace:Param)": {
                            "doc": "Method doc string.",
                            "parameters": {
                                "param0": "Parameter 0 doc string.",
                                "param1": "Parameter 1 doc string.",
                            },
                            "return": "Return doc string.",
                        },
                    },
                },
            }
        )

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Sequence[str] = (
            "def Method(self, param0: Param, param1: Param) -> Tuple[Return, Return]:",
            '    """Method doc string.',
            "    ",
            "    :param param0: Parameter 0 doc string.",
            "    :param param1: Parameter 1 doc string.",
            "    :return: Return doc string.",
            '    """',
        )

        self.assertEqual(manual, lines)

    def test_doc_returns_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Type": {
                        "Method(Namespace:Param, Namespace:Param)": {
                            "doc": "Method doc string.",
                            "parameters": {
                                "param0": "Parameter 0 doc string.",
                                "param1": "Parameter 1 doc string.",
                            },
                            "return": "Return doc string.",
                        },
                    },
                },
            }
        )

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Sequence[str] = (
            "@classmethod",
            "def Method(cls, param0: Param, param1: Param) -> Tuple[Return, Return]:",
            '    """Method doc string.',
            "    ",
            "    :param param0: Parameter 0 doc string.",
            "    :param param1: Parameter 1 doc string.",
            "    :return: Return doc string.",
            '    """',
        )

        self.assertEqual(manual, lines)

    def test_doc_returns_overload(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Type": {
                        "Method(Namespace:Param, Namespace:Param)": {
                            "doc": "Method doc string.",
                            "parameters": {
                                "param0": "Parameter 0 doc string.",
                                "param1": "Parameter 1 doc string.",
                            },
                            "return": "Return doc string.",
                        },
                    },
                },
            }
        )

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Sequence[str] = (
            "@overload",
            "def Method(self, param0: Param, param1: Param) -> Tuple[Return, Return]:",
            '    """Method doc string.',
            "    ",
            "    :param param0: Parameter 0 doc string.",
            "    :param param1: Parameter 1 doc string.",
            "    :return: Return doc string.",
            '    """',
        )

        self.assertEqual(manual, lines)

    def test_doc_returns_overload_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Param", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Param", namespace="Namespace")),
            ),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Type": {
                        "Method(Namespace:Param, Namespace:Param)": {
                            "doc": "Method doc string.",
                            "parameters": {
                                "param0": "Parameter 0 doc string.",
                                "param1": "Parameter 1 doc string.",
                            },
                            "return": "Return doc string.",
                        },
                    },
                },
            }
        )

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Sequence[str] = (
            "@classmethod",
            "@overload",
            "def Method(cls, param0: Param, param1: Param) -> Tuple[Return, Return]:",
            '    """Method doc string.',
            "    ",
            "    :param param0: Parameter 0 doc string.",
            "    :param param1: Parameter 1 doc string.",
            "    :return: Return doc string.",
            '    """',
        )

        self.assertEqual(manual, lines)

    def test_doc_returns_no_params(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Type": {
                        "Method()": {
                            "doc": "Method doc string.",
                            "return": "Return doc string.",
                        },
                    },
                },
            }
        )

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Sequence[str] = (
            "def Method(self) -> Tuple[Return, Return]:",
            '    """Method doc string.',
            "    ",
            "    :return: Return doc string.",
            '    """',
        )

        self.assertEqual(manual, lines)

    def test_doc_returns_no_params_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Type": {
                        "Method()": {
                            "doc": "Method doc string.",
                            "return": "Return doc string.",
                        },
                    },
                },
            }
        )

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=False)
        manual: Sequence[str] = (
            "@classmethod",
            "def Method(cls) -> Tuple[Return, Return]:",
            '    """Method doc string.',
            "    ",
            "    :return: Return doc string.",
            '    """',
        )

        self.assertEqual(manual, lines)

    def test_doc_returns_no_params_overload(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Type": {
                        "Method()": {
                            "doc": "Method doc string.",
                            "return": "Return doc string.",
                        },
                    },
                },
            }
        )

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Sequence[str] = (
            "@overload",
            "def Method(self) -> Tuple[Return, Return]:",
            '    """Method doc string.',
            "    ",
            "    :return: Return doc string.",
            '    """',
        )

        self.assertEqual(manual, lines)

    def test_doc_returns_no_params_overload_static(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(
                CType(name="Return", namespace="Namespace"),
                CType(name="Return", namespace="Namespace"),
            ),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Type": {
                        "Method()": {
                            "doc": "Method doc string.",
                            "return": "Return doc string.",
                        },
                    },
                },
            }
        )

        lines: Sequence[str] = build_method(method=method, imports=imports, doc=doc, overload=True)
        manual: Sequence[str] = (
            "@classmethod",
            "@overload",
            "def Method(cls) -> Tuple[Return, Return]:",
            '    """Method doc string.',
            "    ",
            "    :return: Return doc string.",
            '    """',
        )

        self.assertEqual(manual, lines)


class TestBuildEvent(TestBase):
    def test_build(self) -> None:
        event: CEvent = CEvent(
            name="Event",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="Event", namespace="Namespace"),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        lines: Sequence[str] = build_event(event=event, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "Event: EventType[Event] = ...",
            '""""""',
        )

        self.assertEqual(manual, lines)

    def test_py_imports(self) -> None:
        event: CEvent = CEvent(
            name="Event",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="Event", namespace="Namespace"),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_event(event=event, imports=imports, doc=doc)
        manual: Set[str] = set()

        self.assertEqual(manual, imports.py)

    def test_c_imports(self) -> None:
        event: CEvent = CEvent(
            name="Event",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="Event", namespace="Namespace"),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_event(event=event, imports=imports, doc=doc)
        manual: Set[str] = {"Namespace.Event"}

        self.assertEqual(manual, imports.c)

    def test_doc(self) -> None:
        event: CEvent = CEvent(
            name="Event",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="Event", namespace="Namespace"),
        )
        imports: Imports = Imports()
        doc: Doc = Doc(
            {
                "Namespace": {
                    "Type": {
                        "Event": {
                            "doc": "Event doc string.",
                        },
                    },
                },
            }
        )

        lines: Sequence[str] = build_event(event=event, imports=imports, doc=doc)
        manual: Sequence[str] = (
            "Event: EventType[Event] = ...",
            '"""Event doc string."""',
        )

        self.assertEqual(manual, lines)


class TestBuildStubs(TestBase):
    output_dir: Path

    @classmethod
    def setUpClass(cls) -> None:
        cls.output_dir = Path("output")
        cls.output_dir.mkdir(parents=True, exist_ok=True)

    def test_build_test_lib(self) -> None:
        skeleton_name: str = "TestLib_1.0.0.0_skeleton.json"
        doc_name: str = "TestLib_1.0.0.0_doc.json"

        result = build_stubs(
            skeleton_files=(Path(skeleton_name),),
            doc_files=(Path(doc_name),),
            output_dir=self.output_dir,
            line_length=100,
        )

        self.assertEqual(0, result)


if __name__ == "__main__":
    unittest.main()
