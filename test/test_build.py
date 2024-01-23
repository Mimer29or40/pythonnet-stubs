import unittest
from typing import Any
from typing import Mapping
from typing import Sequence

from stubgen.build_stubs import DocDict


class TestDocDict(unittest.TestCase):
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

        doc_dict0: DocDict = DocDict(tree0)
        doc_dict1: DocDict = DocDict(tree1)

        merged: DocDict = doc_dict0.merge(doc_dict1)

        self.assertIsNotNone(merged)
        self.assertIsInstance(merged, DocDict)
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

        doc_dict0: DocDict = DocDict(tree0)
        doc_dict1: DocDict = DocDict(tree1)

        merged: DocDict = doc_dict0.merge(doc_dict1)

        self.assertIsNotNone(merged)
        self.assertIsInstance(merged, DocDict)
        self.assertEqual({"doc": "Doc0"}, merged.data)

    def test_merge_doc_both(self) -> None:
        tree0: Mapping[str, Any] = {"doc": "Doc0"}
        tree1: Mapping[str, Any] = {"doc": "Doc1"}

        doc_dict0: DocDict = DocDict(tree0)
        doc_dict1: DocDict = DocDict(tree1)

        merged: DocDict = doc_dict0.merge(doc_dict1)

        self.assertIsNotNone(merged)
        self.assertIsInstance(merged, DocDict)
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

        doc_dict0: DocDict = DocDict(tree0)
        doc_dict1: DocDict = DocDict(tree1)

        merged: DocDict = doc_dict0.merge(doc_dict1)

        self.assertIsNotNone(merged)
        self.assertIsInstance(merged, DocDict)
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

        doc_dict0: DocDict = DocDict(tree0)
        doc_dict1: DocDict = DocDict(tree1)

        merged: DocDict = doc_dict0.merge(doc_dict1)

        self.assertIsNotNone(merged)
        self.assertIsInstance(merged, DocDict)
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

        doc_dict0: DocDict = DocDict(tree0)
        doc_dict1: DocDict = DocDict(tree1)

        merged: DocDict = doc_dict0.merge(doc_dict1)

        self.assertIsNotNone(merged)
        self.assertIsInstance(merged, DocDict)
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

        doc_dict0: DocDict = DocDict(tree0)
        doc_dict1: DocDict = DocDict(tree1)

        merged: DocDict = doc_dict0.merge(doc_dict1)

        self.assertIsNotNone(merged)
        self.assertIsInstance(merged, DocDict)
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

        doc_dict0: DocDict = DocDict(tree0)
        doc_dict1: DocDict = DocDict(tree1)

        merged: DocDict = doc_dict0.merge(doc_dict1)

        self.assertIsNotNone(merged)
        self.assertIsInstance(merged, DocDict)
        self.assertEqual({"return": "Return0"}, merged.data)

    def test_merge_return_both(self) -> None:
        tree0: Mapping[str, Any] = {"return": "Return0"}
        tree1: Mapping[str, Any] = {"return": "Return1"}

        doc_dict0: DocDict = DocDict(tree0)
        doc_dict1: DocDict = DocDict(tree1)

        merged: DocDict = doc_dict0.merge(doc_dict1)

        self.assertIsNotNone(merged)
        self.assertIsInstance(merged, DocDict)
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

        doc_dict0: DocDict = DocDict(tree0)
        doc_dict1: DocDict = DocDict(tree1)

        merged: DocDict = doc_dict0.merge(doc_dict1)

        self.assertIsNotNone(merged)
        self.assertIsInstance(merged, DocDict)
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

        doc_dict0: DocDict = DocDict(tree0)
        doc_dict1: DocDict = DocDict(tree1)

        merged: DocDict = doc_dict0.merge(doc_dict1)

        self.assertIsNotNone(merged)
        self.assertIsInstance(merged, DocDict)
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

        doc_dict0: DocDict = DocDict(tree0)
        doc_dict1: DocDict = DocDict(tree1)

        merged: DocDict = doc_dict0.merge(doc_dict1)

        self.assertIsNotNone(merged)
        self.assertIsInstance(merged, DocDict)
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

        doc_dict0: DocDict = DocDict(tree0)
        doc_dict1: DocDict = DocDict(tree1)

        merged: DocDict = doc_dict0.merge(doc_dict1)

        self.assertIsNotNone(merged)
        self.assertIsInstance(merged, DocDict)
        self.assertEqual(
            {"NodeA": {"NodeB": {"NodeC": {"NodeD": {}, "NodeE": {}}}}},
            merged.data,
        )

    def test_get_shallow_node(self) -> None:
        doc_tree: Mapping[str, Any] = {"Node": {"doc": ""}}
        doc_dict: DocDict = DocDict(doc_tree)
        node: DocDict = doc_dict.get("Node")

        self.assertIsNotNone(node)
        self.assertIsInstance(node, DocDict)
        self.assertEqual({"doc": ""}, node.data)

    def test_get_shallow_node_missing(self) -> None:
        doc_tree: Mapping[str, Any] = {"Node": {"doc": ""}}
        doc_dict: DocDict = DocDict(doc_tree)
        node: DocDict = doc_dict.get("Not Present")

        self.assertIsNone(node)

    def test_get_deep_node(self) -> None:
        doc_tree: Mapping[str, Any] = {"NodeA": {"NodeB": {"NodeC": {"NodeD": {"doc": ""}}}}}
        doc_dict: DocDict = DocDict(doc_tree)
        node: DocDict = doc_dict.get("NodeA.NodeB.NodeC.NodeD")

        self.assertIsNotNone(node)
        self.assertIsInstance(node, DocDict)
        self.assertEqual({"doc": ""}, node.data)

    def test_get_deep_node_missing(self) -> None:
        doc_tree: Mapping[str, Any] = {"NodeA": {"NodeB": {"NodeC": {"NodeD": {"doc": ""}}}}}
        doc_dict: DocDict = DocDict(doc_tree)
        node: DocDict = doc_dict.get("NodeA.NodeB.NodeC.Not Present")

        self.assertIsNone(node)

    def test_doc_string_empty(self) -> None:
        doc_tree: Mapping[str, Any] = {}
        doc_dict: DocDict = DocDict(doc_tree)
        doc_string: Sequence[str] = doc_dict.doc_string()

        self.assertIsNotNone(doc_string)
        self.assertIsInstance(doc_string, Sequence)
        self.assertEqual(('""""""',), doc_string)

    def test_doc_string_single_line(self) -> None:
        doc_tree: Mapping[str, Any] = {
            "doc": "This is a doc string that is exactly 57 characters long.",
        }
        doc_dict: DocDict = DocDict(doc_tree)
        doc_string: Sequence[str] = doc_dict.doc_string()

        self.assertIsNotNone(doc_string)
        self.assertIsInstance(doc_string, Sequence)
        self.assertEqual(
            ('"""This is a doc string that is exactly 57 characters long."""',),
            doc_string,
        )

    def test_doc_string_empty_indent(self) -> None:
        doc_tree: Mapping[str, Any] = {}
        doc_dict: DocDict = DocDict(doc_tree)
        doc_string: Sequence[str] = doc_dict.doc_string(indent=1)

        self.assertIsNotNone(doc_string)
        self.assertIsInstance(doc_string, Sequence)
        self.assertEqual(('    """"""',), doc_string)

    def test_doc_string_single_line_indent(self) -> None:
        doc_tree: Mapping[str, Any] = {
            "doc": "This is a doc string that is exactly 57 characters long.",
        }
        doc_dict: DocDict = DocDict(doc_tree)
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
        doc_dict: DocDict = DocDict(doc_tree)
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
        doc_dict: DocDict = DocDict(doc_tree)
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
        doc_dict: DocDict = DocDict(doc_tree)
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
        doc_dict: DocDict = DocDict(doc_tree)
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
        doc_dict: DocDict = DocDict(doc_tree)
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
        doc_dict: DocDict = DocDict(doc_tree)
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
        doc_dict: DocDict = DocDict(doc_tree)
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
        doc_dict: DocDict = DocDict(doc_tree)
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
        doc_dict: DocDict = DocDict(doc_tree)
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


if __name__ == "__main__":
    unittest.main()
