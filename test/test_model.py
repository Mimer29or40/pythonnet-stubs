"""Tests for stubgen.model.py."""

from __future__ import annotations

from typing import TYPE_CHECKING
from typing import ClassVar

import pytest
from conftest import make_params

from stubgen.model import CAssembly
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
from stubgen.model import CType
from stubgen.model import DocNode
from stubgen.model import DocTree

if TYPE_CHECKING:  # pragma: no cover
    from collections.abc import Mapping
    from collections.abc import Sequence

    from conftest import ParamSequence

    from stubgen.model import CWrapper
    from stubgen.model import JsonType


# noinspection PyTypeChecker
def _compare[T: CWrapper](cls: type[T], x: T, y: T) -> None:
    assert x < y
    assert x <= y
    assert x == x
    assert y == y
    assert y > x
    assert y >= x
    assert cls.compare(x, y) == -1
    assert cls.compare(x, x) == 0
    assert cls.compare(y, y) == 0
    assert cls.compare(y, x) == 1


# noinspection PyTypeChecker
def _compare_seq[T: CWrapper](cls: type[T], x: T, y: T) -> None:
    assert cls.compare_seq([], [y]) == -1
    assert cls.compare_seq([x], [y]) == -1
    assert cls.compare_seq([], []) == 0
    assert cls.compare_seq([x], [x]) == 0
    assert cls.compare_seq([y], [y]) == 0
    assert cls.compare_seq([x], []) == 1
    assert cls.compare_seq([y], [x]) == 1


class TestDocTree:
    """Tests for DocTree."""

    @pytest.mark.parametrize(
        ("string", "expected"),
        **make_params(
            [
                ("namespace", ("A", ["A"])),
                ("namespace_type", ("A:B", ["A", "B"])),
                ("namespace_nested_type", ("A:B.C", ["A", "B", "C"])),
                ("namespace_type_generic", ("A:B[$C]", ["A", "B[$C]"])),
                ("namespace_nested_type_generic", ("A:B.C[$D]", ["A", "B", "C[$D]"])),
                ("nested_namespace", ("A.B", ["A", "B"])),
                (
                    "complex",
                    (
                        "A.B:C.D[E:F].G[H, I:J[K]].L().M(N, O:P[Q])",
                        ["A", "B", "C", "D[E:F]", "G[H, I:J[K]]", "L()", "M(N, O:P[Q])"],
                    ),
                ),
            ]
        ),
    )
    def test_split_node_string(self, string: str, expected: Sequence[str]) -> None:
        """Test for DocTree._split_node_string()."""
        actual: Sequence[str] = DocTree._split_node_string(string)  # noqa: SLF001

        assert actual == expected

    class TestGetItem:
        """Tests for DocTree.__getitem__()."""

        def test_empty(self) -> None:
            """Test for DocTree.__getitem__() with an empty string."""
            doc: DocTree = DocTree()

            expected: DocNode | None = None
            actual: DocNode | None = doc[""]

            assert actual == expected

        def test_child(self) -> None:
            """Test for DocTree.__getitem__()."""
            child: DocNode = DocNode("Child")
            doc: DocTree = DocTree(children=(child,))

            expected: DocNode | None = child
            actual: DocNode | None = doc["Child"]

            assert actual == expected

        def test_grandchild(self) -> None:
            """Test for DocTree.__getitem__()."""
            grandchild: DocNode = DocNode("Grandchild")
            child: DocNode = DocNode("Child", children=[grandchild])
            doc: DocTree = DocTree(children=(child,))

            expected: DocNode | None = grandchild
            actual: DocNode | None = doc["Child.Grandchild"]

            assert actual == expected

        def test_missing(self) -> None:
            """Test for DocTree.__getitem__() with a missing child."""
            child: DocNode = DocNode("Child")
            doc: DocTree = DocTree()

            expected: DocNode | None = child
            actual: DocNode | None = doc["Child"]

            assert actual == expected

    json_list: ClassVar[ParamSequence[tuple[DocTree, JsonType]]] = [
        ("basic", (DocTree(), {})),
        (
            "children",
            (
                DocTree(children=[DocNode("A"), DocNode("B")]),
                {"A": {"doc": "", "doc_formatted": {}}, "B": {"doc": "", "doc_formatted": {}}},
            ),
        ),
    ]

    @pytest.mark.parametrize(("doc", "json"), **make_params(json_list))
    def test_to_json(self, doc: DocTree, json: Mapping[str, ...]) -> None:
        """Test for DocTree.to_json()."""
        expected: JsonType = json
        actual: JsonType = doc.to_json()

        assert actual == expected

    @pytest.mark.parametrize(("doc", "json"), **make_params(json_list))
    def test_from_json(self, doc: DocTree, json: Mapping[str, ...]) -> None:
        """Test for DocTree.from_json()."""
        expected: DocTree = doc
        actual: DocTree = DocTree.from_json(json)

        assert actual == expected

    @pytest.mark.parametrize(
        ("obj1", "obj2", "expected"),
        **make_params(
            [
                ("basic", (DocTree(), DocTree(), DocTree())),
                (
                    "children_A",
                    (DocTree(children=[DocNode("A")]), DocTree(), DocTree(children=[DocNode("A")])),
                ),
                (
                    "children_B",
                    (DocTree(), DocTree(children=[DocNode("B")]), DocTree(children=[DocNode("B")])),
                ),
                (
                    "children_both",
                    (
                        DocTree(children=[DocNode("A")]),
                        DocTree(children=[DocNode("B")]),
                        DocTree(children=[DocNode("A"), DocNode("B")]),
                    ),
                ),
            ]
        ),
    )
    def test_merge(self, obj1: DocTree, obj2: DocTree, expected: DocTree) -> None:
        """Test for DocTree.merge()."""
        actual: DocTree = DocTree.merge(obj1, obj2)

        assert actual == expected


class TestDocNode:
    """Tests for DocNode."""

    @pytest.mark.parametrize(
        ("doc", "indent", "expected"),
        **make_params(
            [
                ("empty", (DocNode("A"), 0, ['""""""'])),
                ("empty_indent", (DocNode("A"), 1, ['    """"""'])),
                ("single_line", (DocNode("A", doc="Summary line."), 0, ['"""Summary line."""'])),
                (
                    "single_line_indent",
                    (
                        DocNode("A", doc="Summary line."),
                        1,
                        ['    """Summary line."""   # noqa: E501'],
                    ),
                ),
                (
                    "paragraph",
                    (
                        DocNode("A", doc="Summary line.\nParagraph line."),
                        0,
                        [
                            '"""Summary line.',
                            "",
                            "Paragraph line.",
                            '"""',
                        ],
                    ),
                ),
                (
                    "paragraph_indent",
                    (
                        DocNode("A", doc="Summary line.\nParagraph line."),
                        1,
                        [
                            '    """Summary line.',
                            "",
                            "    Paragraph line.",
                            '    """',
                        ],
                    ),
                ),
                (
                    "long_paragraph",
                    (
                        DocNode("A", doc="Summary line.\nLong paragraph line."),
                        0,
                        [
                            '"""Summary line.',
                            "",
                            "Long paragraph line.",
                            '"""',
                        ],
                    ),
                ),
                (
                    "long_paragraph_indent",
                    (
                        DocNode("A", doc="Summary line.\nLong paragraph line."),
                        1,
                        [
                            '    """Summary line.',
                            "",
                            "    Long paragraph",
                            "    line.",
                            '    """',
                        ],
                    ),
                ),
                (
                    "parameters",
                    (
                        DocNode("A", parameter_docs={f"p{i}": f"Parameter {i}" for i in range(2)}),
                        0,
                        [
                            '"""',
                            "",
                            ":param p0: Parameter",
                            "  0",
                            ":param p1: Parameter",
                            "  1",
                            '"""',
                        ],
                    ),
                ),
                (
                    "parameters_indent",
                    (
                        DocNode("A", parameter_docs={f"p{i}": f"Parameter {i}" for i in range(2)}),
                        1,
                        [
                            '    """',
                            "",
                            "    :param p0:",
                            "      Parameter 0",
                            "    :param p1:",
                            "      Parameter 1",
                            '    """',
                        ],
                    ),
                ),
                (
                    "return",
                    (
                        DocNode("A", return_doc="Return string."),
                        0,
                        [
                            '"""',
                            "",
                            ":return: Return",
                            "  string.",
                            '"""',
                        ],
                    ),
                ),
                (
                    "return_indent",
                    (
                        DocNode("A", return_doc="Return string."),
                        1,
                        [
                            '    """',
                            "",
                            "    :return: Return",
                            "      string.",
                            '    """',
                        ],
                    ),
                ),
                (
                    "exceptions",
                    (
                        DocNode("A", exception_docs={f"E{i}": f"Except {i}" for i in range(2)}),
                        0,
                        [
                            '"""',
                            "",
                            ":except E0: Except 0",
                            ":except E1: Except 1",
                            '"""',
                        ],
                    ),
                ),
                (
                    "exceptions_indent",
                    (
                        DocNode("A", exception_docs={f"E{i}": f"Except {i}" for i in range(2)}),
                        1,
                        [
                            '    """',
                            "",
                            "    :except E0:",
                            "      Except 0",
                            "    :except E1:",
                            "      Except 1",
                            '    """',
                        ],
                    ),
                ),
                (
                    "doc_formatted",
                    (
                        DocNode(
                            "A",
                            doc="\n%replace%",
                            doc_formatted={
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
                        ),
                        0,
                        [
                            '"""',
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
                        ],
                    ),
                ),
                (
                    "doc_formatted_indent",
                    (
                        DocNode(
                            "A",
                            doc="\n%replace%",
                            doc_formatted={
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
                        ),
                        1,
                        [
                            '    """',
                            "",
                            "           | Column 1 | Column 2 | Column 3 | Column 4",
                            "    -------|----------|----------|----------|----------",
                            "     Row 1 |   R1C1   |   R1C2   |   R1C3   |   R1C4",
                            "    -------|----------|----------|----------|----------",
                            "     Row 2 |   R2C1   |   R2C2   |   R2C3   |   R2C4",
                            "    -------|----------|----------|----------|----------",
                            "     Row 3 |   R3C1   |   R3C2   |   R3C3   |   R3C4",
                            "    -------|----------|----------|----------|----------",
                            "     Row 4 |   R4C1   |   R4C2   |   R4C3   |   R4C4",
                            "    -------|----------|----------|----------|----------",
                            '    """',
                        ],
                    ),
                ),
            ]
        ),
    )
    def test_doc_string(self, doc: DocNode, indent: int, expected: Sequence[str]) -> None:
        """Test for DocNode.doc_string()."""
        actual: Sequence[str] = doc.doc_string(20, indent=indent)

        assert actual == expected

    json_list: ClassVar[ParamSequence[tuple[DocNode, JsonType]]] = [
        ("basic", (DocNode("A"), {"doc": "", "doc_formatted": {}})),
        (
            "parameters",
            (
                DocNode("A", parameter_docs={f"p{i}": "" for i in range(2)}),
                {"doc": "", "doc_formatted": {}, "parameters": {"p0": "", "p1": ""}},
            ),
        ),
        (
            "parameters_empty",
            (
                DocNode("A", parameter_docs={}),
                {"doc": "", "doc_formatted": {}, "parameters": {}},
            ),
        ),
        (
            "return",
            (
                DocNode("A", return_doc=""),
                {"doc": "", "doc_formatted": {}, "return": ""},
            ),
        ),
        (
            "exceptions",
            (
                DocNode("A", exception_docs={f"e{i}": "" for i in range(2)}),
                {"doc": "", "doc_formatted": {}, "exceptions": {"e0": "", "e1": ""}},
            ),
        ),
        (
            "exceptions_empty",
            (
                DocNode("A", exception_docs={}),
                {"doc": "", "doc_formatted": {}, "exceptions": {}},
            ),
        ),
        (
            "children",
            (
                DocNode("A", children=[DocNode("B")]),
                {"doc": "", "doc_formatted": {}, "B": {"doc": "", "doc_formatted": {}}},
            ),
        ),
    ]

    @pytest.mark.parametrize(("doc", "json"), **make_params(json_list))
    def test_to_json(self, doc: DocNode, json: Mapping[str, ...]) -> None:
        """Test for DocNode.to_json()."""
        expected: JsonType = json
        actual: JsonType = doc.to_json()

        assert actual == expected

    @pytest.mark.parametrize(("doc", "json"), **make_params(json_list))
    def test_from_json(self, doc: DocNode, json: Mapping[str, ...]) -> None:
        """Test for DocNode.from_json()."""
        expected: DocNode = doc
        actual: DocNode = DocNode.from_json("A", json)

        assert actual == expected

    @pytest.mark.parametrize(
        ("obj1", "obj2", "expected"),
        **make_params(
            [
                ("basic", (DocNode(name="A"), DocNode(name="B"), DocNode(name="A"))),
                ("basic_rev", (DocNode(name="B"), DocNode(name="A"), DocNode(name="B"))),
                (
                    "doc_A",
                    (DocNode(name="A", doc="A"), DocNode(name="B"), DocNode(name="A", doc="A")),
                ),
                (
                    "doc_B",
                    (DocNode(name="A"), DocNode(name="B", doc="B"), DocNode(name="A", doc="B")),
                ),
                (
                    "doc_formatted_both",
                    (
                        DocNode(name="A", doc="A"),
                        DocNode(name="B", doc="B"),
                        DocNode(name="A", doc="A\nB"),
                    ),
                ),
                (
                    "doc_formatted_A",
                    (
                        DocNode(name="A", doc_formatted={"A": ["A"]}),
                        DocNode(name="B"),
                        DocNode(name="A", doc_formatted={"A": ["A"]}),
                    ),
                ),
                (
                    "doc_formatted_B",
                    (
                        DocNode(name="A"),
                        DocNode(name="B", doc_formatted={"B": ["B"]}),
                        DocNode(name="A", doc_formatted={"B": ["B"]}),
                    ),
                ),
                (
                    "doc_formatted_both",
                    (
                        DocNode(name="A", doc_formatted={"A": ["A"]}),
                        DocNode(name="B", doc_formatted={"B": ["B"]}),
                        DocNode(name="A", doc_formatted={"A": ["A"], "B": ["B"]}),
                    ),
                ),
                (
                    "doc_formatted_merge",
                    (
                        DocNode(name="A", doc_formatted={"A": ["A"]}),
                        DocNode(name="B", doc_formatted={"A": ["B"]}),
                        DocNode(name="A", doc_formatted={"A": ["A", "B"]}),
                    ),
                ),
                (
                    "parameter_docs_A",
                    (
                        DocNode(name="A", parameter_docs={"A": "A"}),
                        DocNode(name="B"),
                        DocNode(name="A", parameter_docs={"A": "A"}),
                    ),
                ),
                (
                    "parameter_docs_B",
                    (
                        DocNode(name="A"),
                        DocNode(name="B", parameter_docs={"B": "B"}),
                        DocNode(name="A", parameter_docs={"B": "B"}),
                    ),
                ),
                (
                    "parameter_docs_both",
                    (
                        DocNode(name="A", parameter_docs={"A": "A"}),
                        DocNode(name="B", parameter_docs={"B": "B"}),
                        DocNode(name="A", parameter_docs={"A": "A", "B": "B"}),
                    ),
                ),
                (
                    "parameter_docs_merge",
                    (
                        DocNode(name="A", parameter_docs={"A": "A"}),
                        DocNode(name="B", parameter_docs={"A": "B"}),
                        DocNode(name="A", parameter_docs={"A": "A\nB"}),
                    ),
                ),
                (
                    "return_A",
                    (
                        DocNode(name="A", return_doc="A"),
                        DocNode(name="B"),
                        DocNode(name="A", return_doc="A"),
                    ),
                ),
                (
                    "return_B",
                    (
                        DocNode(name="A"),
                        DocNode(name="B", return_doc="B"),
                        DocNode(name="A", return_doc="B"),
                    ),
                ),
                (
                    "return_formatted_both",
                    (
                        DocNode(name="A", return_doc="A"),
                        DocNode(name="B", return_doc="B"),
                        DocNode(name="A", return_doc="A\nB"),
                    ),
                ),
                (
                    "exception_docs_A",
                    (
                        DocNode(name="A", exception_docs={"A": "A"}),
                        DocNode(name="B"),
                        DocNode(name="A", exception_docs={"A": "A"}),
                    ),
                ),
                (
                    "exception_docs_B",
                    (
                        DocNode(name="A"),
                        DocNode(name="B", exception_docs={"B": "B"}),
                        DocNode(name="A", exception_docs={"B": "B"}),
                    ),
                ),
                (
                    "exception_docs_both",
                    (
                        DocNode(name="A", exception_docs={"A": "A"}),
                        DocNode(name="B", exception_docs={"B": "B"}),
                        DocNode(name="A", exception_docs={"A": "A", "B": "B"}),
                    ),
                ),
                (
                    "exception_docs_merge",
                    (
                        DocNode(name="A", exception_docs={"A": "A"}),
                        DocNode(name="B", exception_docs={"A": "B"}),
                        DocNode(name="A", exception_docs={"A": "A\nB"}),
                    ),
                ),
                (
                    "children_A",
                    (
                        DocNode(name="A", children=[DocNode("A")]),
                        DocNode(name="B"),
                        DocNode(name="A", children=[DocNode("A")]),
                    ),
                ),
                (
                    "children_B",
                    (
                        DocNode(name="A"),
                        DocNode(name="B", children=[DocNode("B")]),
                        DocNode(name="A", children=[DocNode("B")]),
                    ),
                ),
                (
                    "children_both",
                    (
                        DocNode(name="A", children=[DocNode("A")]),
                        DocNode(name="B", children=[DocNode("B")]),
                        DocNode(name="A", children=[DocNode("A"), DocNode("B")]),
                    ),
                ),
            ]
        ),
    )
    def test_merge(self, obj1: DocNode, obj2: DocNode, expected: DocNode) -> None:
        """Test for DocNode.merge()."""
        actual: DocNode = DocNode.merge(obj1, obj2)

        assert actual == expected


class TestCType:
    """Tests for CType."""

    import_name_objects: ClassVar[ParamSequence[tuple[CType, str]]] = [
        ("basic", (CType(name="Name"), "Name")),
        ("namespace", (CType(name="Name", namespace="Namespace"), "Namespace.Name")),
    ]

    @pytest.mark.parametrize(("obj", "expected"), **make_params(import_name_objects))
    def test_import_name(self, obj: CType, expected: str) -> None:
        """Test for CType.import_name."""
        actual: str = obj.import_name

        assert actual == expected

    unique_name_objects: ClassVar[ParamSequence[tuple[CType, str]]] = [
        ("basic", (CType(name="Name"), "Name")),
        ("inner", (CType(name="Name", inner=[CType(name="A"), CType(name="B")]), "Name[A, B]")),
    ]

    @pytest.mark.parametrize(("obj", "expected"), **make_params(unique_name_objects))
    def test_unique_name(self, obj: CType, expected: str) -> None:
        """Test for CType.unique_name."""
        actual: str = obj.unique_name

        assert actual == expected

    json_objects: ClassVar[ParamSequence[tuple[CType, JsonType]]] = [
        ("basic", (CType(name="Name"), "Name")),
        ("namespace", (CType(name="Name", namespace="Namespace"), "Namespace:Name")),
        ("nested", (CType(name="Nested.Name"), "Nested.Name")),
        ("reference", (CType(name="Name", reference=True), "*Name")),
        ("generic", (CType(name="Name", generic=True), "$Name")),
        ("nullable", (CType(name="Name", nullable=True), "Name?")),
        ("reference_generic", (CType(name="Name", reference=True, generic=True), "$*Name")),
        ("reference_nullable", (CType(name="Name", reference=True, nullable=True), "*Name?")),
        ("generic_nullable", (CType(name="Name", generic=True, nullable=True), "$Name?")),
        (
            "reference_generic_nullable",
            (CType(name="Name", reference=True, generic=True, nullable=True), "$*Name?"),
        ),
        ("inner", (CType(name="Name", inner=[CType(name="A"), CType(name="B")]), "Name[A, B]")),
    ]

    @pytest.mark.parametrize(("obj", "json"), **make_params(json_objects))
    def test_to_json(self, obj: CType, json: JsonType) -> None:
        """Test for CType.to_json()."""
        expected: JsonType = json
        actual: JsonType = obj.to_json()

        assert actual == expected

    @pytest.mark.parametrize(("obj", "json"), **make_params(json_objects))
    def test_from_json(self, obj: CType, json: JsonType) -> None:
        """Test for CType.from_json()."""
        expected: CType = obj
        actual: CType = CType.from_json(json)

        assert actual == expected

    compare_list: ClassVar[ParamSequence[tuple[CType, CType]]] = [
        ("namespace", (CType(name="Name", namespace="A"), CType(name="Name", namespace="B"))),
        ("namespace_none", (CType(name="Name", namespace=None), CType(name="Name", namespace="A"))),
        ("name", (CType(name="NameA"), CType(name="NameB"))),
        (
            "inner",
            (
                CType(name="Name", inner=(CType(name="A"),)),
                CType(name="Name", inner=(CType(name="B"),)),
            ),
        ),
        ("reference", (CType(name="Name", reference=False), CType(name="Name", reference=True))),
        ("generic", (CType(name="Name", generic=False), CType(name="Name", generic=True))),
        ("nullable", (CType(name="Name", nullable=False), CType(name="Name", nullable=True))),
    ]

    @pytest.mark.parametrize(("x", "y"), **make_params(compare_list))
    def test_compare(self, x: CType, y: CType) -> None:
        """Test for CType.compare()."""
        _compare(CType, x, y)

    @pytest.mark.parametrize(("x", "y"), **make_params(compare_list))
    def test_compare_seq(self, x: CType, y: CType) -> None:
        """Test for CType.compare_seq()."""
        _compare_seq(CType, x, y)


class TestCParameter:
    """Tests for CParameter."""

    unique_name_objects: ClassVar[ParamSequence[tuple[CParameter, str]]] = [
        ("basic", (CParameter(name="Name", type=CType(name="Type")), "Name")),
    ]

    @pytest.mark.parametrize(("obj", "expected"), **make_params(unique_name_objects))
    def test_unique_name(self, obj: CParameter, expected: str) -> None:
        """Test for CParameter.unique_name."""
        actual: str = obj.unique_name

        assert actual == expected

    json_objects: ClassVar[ParamSequence[tuple[CParameter, JsonType]]] = [
        (
            "basic",
            (
                CParameter(name="Name", type=CType(name="Type")),
                {"name": "Name", "type": "Type", "default": False, "out": False},
            ),
        ),
        (
            "default",
            (
                CParameter(name="Name", type=CType(name="Type"), default=True),
                {"name": "Name", "type": "Type", "default": True, "out": False},
            ),
        ),
        (
            "out",
            (
                CParameter(name="Name", type=CType(name="Type"), out=True),
                {"name": "Name", "type": "Type", "default": False, "out": True},
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "json"), **make_params(json_objects))
    def test_to_json(self, obj: CParameter, json: JsonType) -> None:
        """Test for CParameter.to_json()."""
        expected: JsonType = json
        actual: JsonType = obj.to_json()

        assert actual == expected

    @pytest.mark.parametrize(("obj", "json"), **make_params(json_objects))
    def test_from_json(self, obj: CParameter, json: JsonType) -> None:
        """Test for CParameter.from_json()."""
        expected: CParameter = obj
        actual: CParameter = CParameter.from_json(json)

        assert actual == expected

    compare_list: ClassVar[ParamSequence[tuple[CParameter, CParameter]]] = [
        (
            "name",
            (
                CParameter(name="Name", type=CType(name="A")),
                CParameter(name="Name", type=CType(name="B")),
            ),
        ),
    ]

    @pytest.mark.parametrize(("x", "y"), **make_params(compare_list))
    def test_compare(self, x: CParameter, y: CParameter) -> None:
        """Test for CParameter.compare()."""
        _compare(CParameter, x, y)

    @pytest.mark.parametrize(("x", "y"), **make_params(compare_list))
    def test_compare_seq(self, x: CParameter, y: CParameter) -> None:
        """Test for CParameter.compare_seq()."""
        _compare_seq(CParameter, x, y)


class TestCField:
    """Tests for CField."""

    unique_name_objects: ClassVar[ParamSequence[tuple[CField, str]]] = [
        (
            "basic",
            (
                CField(
                    name="Name",
                    declaring_type=CType(name="Type"),
                    return_type=CType(name="Type"),
                ),
                "Name",
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "expected"), **make_params(unique_name_objects))
    def test_unique_name(self, obj: CField, expected: str) -> None:
        """Test for CField.unique_name."""
        actual: str = obj.unique_name

        assert actual == expected

    json_objects: ClassVar[ParamSequence[tuple[CField, JsonType]]] = [
        (
            "basic",
            (
                CField(
                    name="Name", declaring_type=CType(name="Type"), return_type=CType(name="Type")
                ),
                {"name": "Name", "declaring_type": "Type", "return_type": "Type", "static": False},
            ),
        ),
        (
            "static",
            (
                CField(
                    name="Name",
                    declaring_type=CType(name="Type"),
                    return_type=CType(name="Type"),
                    static=True,
                ),
                {"name": "Name", "declaring_type": "Type", "return_type": "Type", "static": True},
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "json"), **make_params(json_objects))
    def test_to_json(self, obj: CField, json: JsonType) -> None:
        """Test for CField.to_json()."""
        expected: JsonType = json
        actual: JsonType = obj.to_json()

        assert actual == expected

    @pytest.mark.parametrize(("obj", "json"), **make_params(json_objects))
    def test_from_json(self, obj: CField, json: JsonType) -> None:
        """Test for CField.from_json()."""
        expected: CField = obj
        actual: CField = CField.from_json(json)

        assert actual == expected

    doc_objects: ClassVar[ParamSequence[tuple[CField, DocNode]]] = [
        (
            "basic",
            (
                CField(name="Name", declaring_type=CType(name="Type"), return_type=CType.VOID),
                DocNode(name="Name"),
            ),
        ),
        (
            "return",
            (
                CField(
                    name="Name", declaring_type=CType(name="Type"), return_type=CType(name="Type")
                ),
                DocNode(name="Name", return_doc=""),
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "doc"), **make_params(doc_objects))
    def test_doc_node(self, obj: CField, doc: DocNode) -> None:
        """Test for CField.doc_node()."""
        expected: DocNode = doc
        actual: DocNode = obj.doc_node()

        assert actual == expected

    compare_list: ClassVar[ParamSequence[tuple[CField, CField]]] = [
        (
            "name",
            (
                CField(name="A", declaring_type=CType(name="Type"), return_type=CType(name="Type")),
                CField(name="B", declaring_type=CType(name="Type"), return_type=CType(name="Type")),
            ),
        ),
    ]

    @pytest.mark.parametrize(("x", "y"), **make_params(compare_list))
    def test_compare(self, x: CField, y: CField) -> None:
        """Test for CField.compare()."""
        _compare(CField, x, y)

    @pytest.mark.parametrize(("x", "y"), **make_params(compare_list))
    def test_compare_seq(self, x: CField, y: CField) -> None:
        """Test for CField.compare_seq()."""
        _compare_seq(CField, x, y)


class TestCConstructor:
    """Tests for CConstructor."""

    unique_name_objects: ClassVar[ParamSequence[tuple[CConstructor, str]]] = [
        ("0_params", (CConstructor(declaring_type=CType(name="Type")), "__init__()")),
        (
            "2_params",
            (
                CConstructor(
                    declaring_type=CType(name="Type"),
                    parameters=[
                        CParameter(name="param0", type=CType(name="Type")),
                        CParameter(name="param0", type=CType(name="Type")),
                    ],
                ),
                "__init__(Type, Type)",
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "expected"), **make_params(unique_name_objects))
    def test_unique_name(self, obj: CConstructor, expected: str) -> None:
        """Test for CConstructor.unique_name."""
        actual: str = obj.unique_name

        assert actual == expected

    json_objects: ClassVar[ParamSequence[tuple[CConstructor, JsonType]]] = [
        (
            "basic",
            (
                CConstructor(declaring_type=CType(name="Type")),
                {"declaring_type": "Type", "parameters": []},
            ),
        ),
        (
            "parameters",
            (
                CConstructor(
                    declaring_type=CType(name="Type"),
                    parameters=[
                        CParameter(name="param0", type=CType(name="Type")),
                        CParameter(name="param1", type=CType(name="Type")),
                    ],
                ),
                {
                    "declaring_type": "Type",
                    "parameters": [
                        {"name": "param0", "type": "Type", "default": False, "out": False},
                        {"name": "param1", "type": "Type", "default": False, "out": False},
                    ],
                },
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "json"), **make_params(json_objects))
    def test_to_json(self, obj: CConstructor, json: JsonType) -> None:
        """Test for CConstructor.to_json()."""
        expected: JsonType = json
        actual: JsonType = obj.to_json()

        assert actual == expected

    @pytest.mark.parametrize(("obj", "json"), **make_params(json_objects))
    def test_from_json(self, obj: CConstructor, json: JsonType) -> None:
        """Test for CConstructor.from_json()."""
        expected: CConstructor = obj
        actual: CConstructor = CConstructor.from_json(json)

        assert actual == expected

    doc_objects: ClassVar[ParamSequence[tuple[CConstructor, DocNode]]] = [
        (
            "basic",
            (CConstructor(declaring_type=CType(name="Type")), DocNode("__init__()")),
        ),
        (
            "parameters",
            (
                CConstructor(
                    declaring_type=CType(name="Type"),
                    parameters=[
                        CParameter(name="param0", type=CType(name="Type")),
                        CParameter(name="param1", type=CType(name="Type")),
                    ],
                ),
                DocNode(
                    "__init__(Type, Type)",
                    parameter_docs={"param0": "", "param1": ""},
                ),
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "doc"), **make_params(doc_objects))
    def test_doc_node(self, obj: CConstructor, doc: DocNode) -> None:
        """Test for CConstructor.doc_node()."""
        expected: DocNode = doc
        actual: DocNode = obj.doc_node()

        assert actual == expected

    compare_list: ClassVar[ParamSequence[tuple[CConstructor, CConstructor]]] = [
        (
            "name",
            (
                CConstructor(
                    declaring_type=CType(name="Type"),
                    parameters=[CParameter(name="Name", type=CType(name="A"))],
                ),
                CConstructor(
                    declaring_type=CType(name="Type"),
                    parameters=[CParameter(name="Name", type=CType(name="B"))],
                ),
            ),
        ),
        (
            "parameter_length",
            (
                CConstructor(declaring_type=CType(name="Type")),
                CConstructor(
                    declaring_type=CType(name="Type"),
                    parameters=[CParameter(name="Name", type=CType(name="Type"))],
                ),
            ),
        ),
    ]

    @pytest.mark.parametrize(("x", "y"), **make_params(compare_list))
    def test_compare(self, x: CConstructor, y: CConstructor) -> None:
        """Test for CConstructor.compare()."""
        _compare(CConstructor, x, y)

    @pytest.mark.parametrize(("x", "y"), **make_params(compare_list))
    def test_compare_seq(self, x: CConstructor, y: CConstructor) -> None:
        """Test for CConstructor.compare_seq()."""
        _compare_seq(CConstructor, x, y)


class TestCProperty:
    """Tests for CProperty."""

    unique_name_objects: ClassVar[ParamSequence[tuple[CProperty, str]]] = [
        (
            "basic",
            (
                CProperty(name="Name", declaring_type=CType(name="Type"), type=CType(name="Type")),
                "Name",
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "expected"), **make_params(unique_name_objects))
    def test_unique_name(self, obj: CProperty, expected: str) -> None:
        """Test for CProperty.unique_name."""
        actual: str = obj.unique_name

        assert actual == expected

    json_objects: ClassVar[ParamSequence[tuple[CProperty, JsonType]]] = [
        (
            "basic",
            (
                CProperty(name="Name", declaring_type=CType(name="Type"), type=CType(name="Type")),
                {
                    "name": "Name",
                    "declaring_type": "Type",
                    "type": "Type",
                    "setter": False,
                    "static": False,
                },
            ),
        ),
        (
            "setter",
            (
                CProperty(
                    name="Name",
                    declaring_type=CType(name="Type"),
                    type=CType(name="Type"),
                    setter=True,
                ),
                {
                    "name": "Name",
                    "declaring_type": "Type",
                    "type": "Type",
                    "setter": True,
                    "static": False,
                },
            ),
        ),
        (
            "static",
            (
                CProperty(
                    name="Name",
                    declaring_type=CType(name="Type"),
                    type=CType(name="Type"),
                    static=True,
                ),
                {
                    "name": "Name",
                    "declaring_type": "Type",
                    "type": "Type",
                    "setter": False,
                    "static": True,
                },
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "json"), **make_params(json_objects))
    def test_to_json(self, obj: CProperty, json: JsonType) -> None:
        """Test for CProperty.to_json()."""
        expected: JsonType = json
        actual: JsonType = obj.to_json()

        assert actual == expected

    @pytest.mark.parametrize(("obj", "json"), **make_params(json_objects))
    def test_from_json(self, obj: CProperty, json: JsonType) -> None:
        """Test for CProperty.from_json()."""
        expected: CProperty = obj
        actual: CProperty = CProperty.from_json(json)

        assert actual == expected

    doc_objects: ClassVar[ParamSequence[tuple[CProperty, DocNode]]] = [
        (
            "basic",
            (
                CProperty(name="Name", declaring_type=CType(name="Type"), type=CType.VOID),
                DocNode(name="Name"),
            ),
        ),
        (
            "return",
            (
                CProperty(name="Name", declaring_type=CType(name="Type"), type=CType(name="Type")),
                DocNode(name="Name", return_doc=""),
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "doc"), **make_params(doc_objects))
    def test_doc_node(self, obj: CProperty, doc: DocNode) -> None:
        """Test for CProperty.doc_node()."""
        expected: DocNode = doc
        actual: DocNode = obj.doc_node()

        assert actual == expected

    compare_list: ClassVar[ParamSequence[tuple[CProperty, CProperty]]] = [
        (
            "name",
            (
                CProperty(name="A", declaring_type=CType(name="Type"), type=CType(name="Type")),
                CProperty(name="B", declaring_type=CType(name="Type"), type=CType(name="Type")),
            ),
        ),
    ]

    @pytest.mark.parametrize(("x", "y"), **make_params(compare_list))
    def test_compare(self, x: CProperty, y: CProperty) -> None:
        """Test for CProperty.compare()."""
        _compare(CProperty, x, y)

    @pytest.mark.parametrize(("x", "y"), **make_params(compare_list))
    def test_compare_seq(self, x: CProperty, y: CProperty) -> None:
        """Test for CProperty.compare_seq()."""
        _compare_seq(CProperty, x, y)


class TestCMethod:
    """Tests for CMethod."""

    unique_name_objects: ClassVar[ParamSequence[tuple[CMethod, str]]] = [
        ("0_params", (CMethod(name="Name", declaring_type=CType(name="Type")), "Name()")),
        (
            "2_params",
            (
                CMethod(
                    name="Name",
                    declaring_type=CType(name="Type"),
                    parameters=[
                        CParameter(name="param0", type=CType(name="Type")),
                        CParameter(name="param0", type=CType(name="Type")),
                    ],
                ),
                "Name(Type, Type)",
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "expected"), **make_params(unique_name_objects))
    def test_unique_name(self, obj: CMethod, expected: str) -> None:
        """Test for CMethod.unique_name."""
        actual: str = obj.unique_name

        assert actual == expected

    json_objects: ClassVar[ParamSequence[tuple[CMethod, JsonType]]] = [
        (
            "basic",
            (
                CMethod(name="Name", declaring_type=CType(name="Type")),
                {
                    "name": "Name",
                    "declaring_type": "Type",
                    "parameters": [],
                    "return_types": [],
                    "static": False,
                },
            ),
        ),
        (
            "parameters",
            (
                CMethod(
                    name="Name",
                    declaring_type=CType(name="Type"),
                    parameters=[
                        CParameter(name="param0", type=CType(name="Type")),
                        CParameter(name="param1", type=CType(name="Type")),
                    ],
                ),
                {
                    "name": "Name",
                    "declaring_type": "Type",
                    "parameters": [
                        {"name": "param0", "type": "Type", "default": False, "out": False},
                        {"name": "param1", "type": "Type", "default": False, "out": False},
                    ],
                    "return_types": [],
                    "static": False,
                },
            ),
        ),
        (
            "return_types",
            (
                CMethod(
                    name="Name",
                    declaring_type=CType(name="Type"),
                    return_types=[CType(name="Type"), CType(name="Type")],
                ),
                {
                    "name": "Name",
                    "declaring_type": "Type",
                    "parameters": [],
                    "return_types": ["Type", "Type"],
                    "static": False,
                },
            ),
        ),
        (
            "static",
            (
                CMethod(name="Name", declaring_type=CType(name="Type"), static=True),
                {
                    "name": "Name",
                    "declaring_type": "Type",
                    "parameters": [],
                    "return_types": [],
                    "static": True,
                },
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "json"), **make_params(json_objects))
    def test_to_json(self, obj: CMethod, json: JsonType) -> None:
        """Test for CMethod.to_json()."""
        expected: JsonType = json
        actual: JsonType = obj.to_json()

        assert actual == expected

    @pytest.mark.parametrize(("obj", "json"), **make_params(json_objects))
    def test_from_json(self, obj: CMethod, json: JsonType) -> None:
        """Test for CMethod.from_json()."""
        expected: CMethod = obj
        actual: CMethod = CMethod.from_json(json)

        assert actual == expected

    doc_objects: ClassVar[ParamSequence[tuple[CMethod, DocNode]]] = [
        (
            "basic",
            (
                CMethod(name="Name", declaring_type=CType(name="Type")),
                DocNode(name="Name()", exception_docs={}),
            ),
        ),
        (
            "parameters",
            (
                CMethod(
                    name="Name",
                    declaring_type=CType(name="Type"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type")),
                        CParameter(name="param1", type=CType(name="Type")),
                    ),
                ),
                DocNode(
                    name="Name(Type, Type)",
                    parameter_docs={"param0": "", "param1": ""},
                    exception_docs={},
                ),
            ),
        ),
        (
            "return_types",
            (
                CMethod(
                    name="Name",
                    declaring_type=CType(name="Type"),
                    return_types=(CType(name="Type"), CType(name="Type")),
                ),
                DocNode(name="Name()", return_doc="", exception_docs={}),
            ),
        ),
        (
            "static",
            (
                CMethod(
                    name="Name",
                    declaring_type=CType(name="Type"),
                    static=True,
                ),
                DocNode(name="Name()", exception_docs={}),
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "doc"), **make_params(doc_objects))
    def test_doc_node(self, obj: CMethod, doc: DocNode) -> None:
        """Test for CMethod.doc_node()."""
        expected: DocNode = doc
        actual: DocNode = obj.doc_node()

        assert actual == expected

    compare_list: ClassVar[ParamSequence[tuple[CMethod, CMethod]]] = [
        (
            "name",
            (
                CMethod(name="A", declaring_type=CType(name="Type")),
                CMethod(name="B", declaring_type=CType(name="Type")),
            ),
        ),
        (
            "parameters",
            (
                CMethod(
                    name="Name",
                    declaring_type=CType(name="Type"),
                    parameters=(CParameter(name="Name", type=CType(name="A")),),
                ),
                CMethod(
                    name="Name",
                    declaring_type=CType(name="Type"),
                    parameters=(CParameter(name="Name", type=CType(name="B")),),
                ),
            ),
        ),
        (
            "parameter_length",
            (
                CMethod(name="Name", declaring_type=CType(name="Type")),
                CMethod(
                    name="Name",
                    declaring_type=CType(name="Type"),
                    parameters=(CParameter(name="Name", type=CType(name="A")),),
                ),
            ),
        ),
    ]

    @pytest.mark.parametrize(("x", "y"), **make_params(compare_list))
    def test_compare(self, x: CMethod, y: CMethod) -> None:
        """Test for CMethod.compare()."""
        _compare(CMethod, x, y)

    @pytest.mark.parametrize(("x", "y"), **make_params(compare_list))
    def test_compare_seq(self, x: CMethod, y: CMethod) -> None:
        """Test for CMethod.compare_seq()."""
        _compare_seq(CMethod, x, y)


class TestCEvent:
    """Tests for CEvent."""

    unique_name_objects: ClassVar[ParamSequence[tuple[CEvent, str]]] = [
        (
            "basic",
            (
                CEvent(name="Name", declaring_type=CType(name="Type"), type=CType(name="Type")),
                "Name",
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "expected"), **make_params(unique_name_objects))
    def test_unique_name(self, obj: CEvent, expected: str) -> None:
        """Test for CEvent.unique_name."""
        actual: str = obj.unique_name

        assert actual == expected

    json_objects: ClassVar[ParamSequence[tuple[CEvent, JsonType]]] = [
        (
            "basic",
            (
                CEvent(name="Name", declaring_type=CType(name="Type"), type=CType(name="Type")),
                {"name": "Name", "declaring_type": "Type", "type": "Type"},
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "json"), **make_params(json_objects))
    def test_to_json(self, obj: CEvent, json: JsonType) -> None:
        """Test for CEvent.to_json()."""
        expected: JsonType = json
        actual: JsonType = obj.to_json()

        assert actual == expected

    @pytest.mark.parametrize(("obj", "json"), **make_params(json_objects))
    def test_from_json(self, obj: CEvent, json: JsonType) -> None:
        """Test for CEvent.from_json()."""
        expected: CEvent = obj
        actual: CEvent = CEvent.from_json(json)

        assert actual == expected

    doc_objects: ClassVar[ParamSequence[tuple[CEvent, DocNode]]] = [
        (
            "basic",
            (
                CEvent(name="Name", declaring_type=CType(name="Type"), type=CType(name="Type")),
                DocNode(name="Name"),
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "doc"), **make_params(doc_objects))
    def test_doc_node(self, obj: CEvent, doc: DocNode) -> None:
        """Test for CEvent.doc_node()."""
        expected: DocNode = doc
        actual: DocNode = obj.doc_node()

        assert actual == expected

    compare_list: ClassVar[ParamSequence[tuple[CEvent, CEvent]]] = [
        (
            "name",
            (
                CEvent(name="A", declaring_type=CType(name="Type"), type=CType(name="Type")),
                CEvent(name="B", declaring_type=CType(name="Type"), type=CType(name="Type")),
            ),
        ),
    ]

    @pytest.mark.parametrize(("x", "y"), **make_params(compare_list))
    def test_compare(self, x: CEvent, y: CEvent) -> None:
        """Test for CEvent.compare()."""
        _compare(CEvent, x, y)

    @pytest.mark.parametrize(("x", "y"), **make_params(compare_list))
    def test_compare_seq(self, x: CEvent, y: CEvent) -> None:
        """Test for CEvent.compare_seq()."""
        _compare_seq(CEvent, x, y)


class TestCClass:
    """Tests for CClass."""

    unique_name_objects: ClassVar[ParamSequence[tuple[CClass, str]]] = [
        ("basic", (CClass(name="Name"), "Name")),
        (
            "generic_args",
            (
                CClass(
                    name="Name",
                    generic_args=[CType(name="A", generic=True), CType(name="B", generic=True)],
                ),
                "Name[$A, $B]",
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "expected"), **make_params(unique_name_objects))
    def test_unique_name(self, obj: CClass, expected: str) -> None:
        """Test for CClass.unique_name."""
        actual: str = obj.unique_name

        assert actual == expected

    json_objects: ClassVar[ParamSequence[tuple[CClass, JsonType]]] = [
        (
            "basic",
            (
                CClass(name="Name"),
                {
                    "abstract": False,
                    "constructors": {},
                    "events": {},
                    "fields": {},
                    "generic_args": [],
                    "interfaces": [],
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "parent": None,
                    "nested_types": {},
                    "properties": {},
                    "super_class": None,
                    "type": "class",
                },
            ),
        ),
        (
            "abstract",
            (
                CClass(name="Name", abstract=True),
                {
                    "type": "class",
                    "name": "Name",
                    "namespace": None,
                    "parent": None,
                    "abstract": True,
                    "generic_args": [],
                    "super_class": None,
                    "interfaces": [],
                    "fields": {},
                    "constructors": {},
                    "properties": {},
                    "methods": {},
                    "events": {},
                    "nested_types": {},
                },
            ),
        ),
        (
            "generic_args",
            (
                CClass(
                    name="Name",
                    generic_args=[CType(name="A", generic=True), CType(name="B", generic=True)],
                ),
                {
                    "type": "class",
                    "name": "Name",
                    "namespace": None,
                    "parent": None,
                    "abstract": False,
                    "generic_args": ["$A", "$B"],
                    "super_class": None,
                    "interfaces": [],
                    "fields": {},
                    "constructors": {},
                    "properties": {},
                    "methods": {},
                    "events": {},
                    "nested_types": {},
                },
            ),
        ),
        (
            "super_class",
            (
                CClass(name="Name", super_class=CType(name="Name")),
                {
                    "abstract": False,
                    "constructors": {},
                    "events": {},
                    "fields": {},
                    "generic_args": [],
                    "interfaces": [],
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "parent": None,
                    "nested_types": {},
                    "properties": {},
                    "super_class": "Name",
                    "type": "class",
                },
            ),
        ),
        (
            "interfaces",
            (
                CClass(name="Name", interfaces=[CType(name="A"), CType(name="B")]),
                {
                    "abstract": False,
                    "constructors": {},
                    "events": {},
                    "fields": {},
                    "generic_args": [],
                    "interfaces": ["A", "B"],
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "parent": None,
                    "nested_types": {},
                    "properties": {},
                    "super_class": None,
                    "type": "class",
                },
            ),
        ),
        (
            "fields",
            (
                CClass(
                    name="Name",
                    fields={
                        "A": CField(
                            name="A",
                            declaring_type=CType(name="Name"),
                            return_type=CType(name="Type"),
                        ),
                        "B": CField(
                            name="B",
                            declaring_type=CType(name="Name"),
                            return_type=CType(name="Type"),
                        ),
                    },
                ),
                {
                    "abstract": False,
                    "constructors": {},
                    "events": {},
                    "fields": {
                        "A": {
                            "name": "A",
                            "declaring_type": "Name",
                            "return_type": "Type",
                            "static": False,
                        },
                        "B": {
                            "name": "B",
                            "declaring_type": "Name",
                            "return_type": "Type",
                            "static": False,
                        },
                    },
                    "generic_args": [],
                    "interfaces": [],
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "parent": None,
                    "nested_types": {},
                    "properties": {},
                    "super_class": None,
                    "type": "class",
                },
            ),
        ),
        (
            "constructors",
            (
                CClass(
                    name="Name",
                    constructors={
                        "__init__()": CConstructor(declaring_type=CType(name="Name")),
                        "__init__(Namespace:Type)": CConstructor(
                            declaring_type=CType(name="Name"),
                            parameters=[CParameter(name="param0", type=CType(name="Type"))],
                        ),
                    },
                ),
                {
                    "abstract": False,
                    "constructors": {
                        "__init__()": {"declaring_type": "Name", "parameters": []},
                        "__init__(Namespace:Type)": {
                            "declaring_type": "Name",
                            "parameters": [
                                {"name": "param0", "type": "Type", "default": False, "out": False},
                            ],
                        },
                    },
                    "events": {},
                    "fields": {},
                    "generic_args": [],
                    "interfaces": [],
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "parent": None,
                    "nested_types": {},
                    "properties": {},
                    "super_class": None,
                    "type": "class",
                },
            ),
        ),
        (
            "properties",
            (
                CClass(
                    name="Name",
                    properties={
                        "A": CProperty(
                            name="A",
                            declaring_type=CType(name="Name"),
                            type=CType(name="Type"),
                            setter=True,
                        ),
                        "B": CProperty(
                            name="B",
                            declaring_type=CType(name="Name"),
                            type=CType(name="Type"),
                            setter=True,
                        ),
                    },
                ),
                {
                    "abstract": False,
                    "constructors": {},
                    "events": {},
                    "fields": {},
                    "generic_args": [],
                    "interfaces": [],
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "parent": None,
                    "nested_types": {},
                    "properties": {
                        "B": {
                            "name": "B",
                            "declaring_type": "Name",
                            "type": "Type",
                            "setter": True,
                            "static": False,
                        },
                        "A": {
                            "name": "A",
                            "declaring_type": "Name",
                            "type": "Type",
                            "setter": True,
                            "static": False,
                        },
                    },
                    "super_class": None,
                    "type": "class",
                },
            ),
        ),
        (
            "methods",
            (
                CClass(
                    name="Name",
                    methods={
                        "A(Type) -> Type": CMethod(
                            name="A",
                            declaring_type=CType(name="Name"),
                            parameters=[CParameter(name="param0", type=CType(name="Type"))],
                            return_types=[CType(name="Type")],
                        ),
                        "B(Type) -> Type": CMethod(
                            name="B",
                            declaring_type=CType(name="Name"),
                            parameters=[CParameter(name="param0", type=CType(name="Type"))],
                            return_types=[CType(name="Type")],
                        ),
                    },
                ),
                {
                    "abstract": False,
                    "constructors": {},
                    "events": {},
                    "fields": {},
                    "generic_args": [],
                    "interfaces": [],
                    "methods": {
                        "A(Type) -> Type": {
                            "name": "A",
                            "declaring_type": "Name",
                            "parameters": [
                                {
                                    "name": "param0",
                                    "type": "Type",
                                    "default": False,
                                    "out": False,
                                },
                            ],
                            "return_types": ["Type"],
                            "static": False,
                        },
                        "B(Type) -> Type": {
                            "name": "B",
                            "declaring_type": "Name",
                            "parameters": [
                                {
                                    "name": "param0",
                                    "type": "Type",
                                    "default": False,
                                    "out": False,
                                },
                            ],
                            "return_types": ["Type"],
                            "static": False,
                        },
                    },
                    "name": "Name",
                    "namespace": None,
                    "parent": None,
                    "nested_types": {},
                    "properties": {},
                    "super_class": None,
                    "type": "class",
                },
            ),
        ),
        (
            "events",
            (
                CClass(
                    name="Name",
                    events={
                        "A -> (Type)": CEvent(
                            name="A", declaring_type=CType(name="Name"), type=CType(name="Type")
                        ),
                        "B -> (Type)": CEvent(
                            name="B", declaring_type=CType(name="Name"), type=CType(name="Type")
                        ),
                    },
                ),
                {
                    "abstract": False,
                    "constructors": {},
                    "events": {
                        "A -> (Type)": {"name": "A", "declaring_type": "Name", "type": "Type"},
                        "B -> (Type)": {"name": "B", "declaring_type": "Name", "type": "Type"},
                    },
                    "fields": {},
                    "generic_args": [],
                    "interfaces": [],
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "parent": None,
                    "nested_types": {},
                    "properties": {},
                    "super_class": None,
                    "type": "class",
                },
            ),
        ),
        (
            "nested_types",
            (
                CClass(
                    name="Name",
                    nested_types={
                        "A": CClass(name="A", parent=CType(name="Name")),
                        "B": CClass(name="B", parent=CType(name="Name")),
                    },
                ),
                {
                    "abstract": False,
                    "constructors": {},
                    "events": {},
                    "fields": {},
                    "generic_args": [],
                    "interfaces": [],
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "parent": None,
                    "nested_types": {
                        "A": {
                            "abstract": False,
                            "constructors": {},
                            "events": {},
                            "fields": {},
                            "generic_args": [],
                            "interfaces": [],
                            "methods": {},
                            "name": "A",
                            "namespace": None,
                            "parent": "Name",
                            "nested_types": {},
                            "properties": {},
                            "super_class": None,
                            "type": "class",
                        },
                        "B": {
                            "abstract": False,
                            "constructors": {},
                            "events": {},
                            "fields": {},
                            "generic_args": [],
                            "interfaces": [],
                            "methods": {},
                            "name": "B",
                            "namespace": None,
                            "parent": "Name",
                            "nested_types": {},
                            "properties": {},
                            "super_class": None,
                            "type": "class",
                        },
                    },
                    "properties": {},
                    "super_class": None,
                    "type": "class",
                },
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "json"), **make_params(json_objects))
    def test_to_json(self, obj: CClass, json: JsonType) -> None:
        """Test for CClass.to_json()."""
        expected: JsonType = json
        actual: JsonType = obj.to_json()

        assert actual == expected

    @pytest.mark.parametrize(("obj", "json"), **make_params(json_objects))
    def test_from_json(self, obj: CClass, json: JsonType) -> None:
        """Test for CClass.from_json()."""
        expected: CClass = obj
        actual: CClass = CClass.from_json(json)

        assert actual == expected

    doc_objects: ClassVar[ParamSequence[tuple[CClass, DocNode]]] = [
        ("basic", (CClass(name="Name"), DocNode(name="Name"))),
        ("abstract", (CClass(name="Name", abstract=True), DocNode(name="Name"))),
        (
            "generic_args",
            (
                CClass(
                    name="Name",
                    generic_args=[CType(name="A", generic=True), CType(name="B", generic=True)],
                ),
                DocNode(name="Name[$A, $B]"),
            ),
        ),
        (
            "super_class",
            (CClass(name="Name", super_class=CType(name="Name")), DocNode(name="Name")),
        ),
        (
            "interfaces",
            (
                CClass(name="Name", interfaces=(CType(name="A"), CType(name="B"))),
                DocNode(name="Name"),
            ),
        ),
        (
            "fields",
            (
                CClass(
                    name="Name",
                    fields={
                        "A": CField(
                            name="A",
                            declaring_type=CType(name="Name"),
                            return_type=CType(name="Type"),
                        ),
                        "B": CField(
                            name="B",
                            declaring_type=CType(name="Name"),
                            return_type=CType(name="Type"),
                        ),
                    },
                ),
                DocNode(
                    name="Name",
                    children=[DocNode(name="A", return_doc=""), DocNode(name="B", return_doc="")],
                ),
            ),
        ),
        (
            "constructors",
            (
                CClass(
                    name="Name",
                    constructors={
                        "__init__()": CConstructor(declaring_type=CType(name="Name")),
                        "__init__(Namespace:Type)": CConstructor(
                            declaring_type=CType(name="Name"),
                            parameters=[CParameter(name="param0", type=CType(name="Type"))],
                        ),
                    },
                ),
                DocNode(
                    name="Name",
                    children=[
                        DocNode(name="__init__()"),
                        DocNode(name="__init__(Type)", parameter_docs={"param0": ""}),
                    ],
                ),
            ),
        ),
        (
            "properties",
            (
                CClass(
                    name="Name",
                    properties={
                        "A": CProperty(
                            name="A",
                            declaring_type=CType(name="Name"),
                            type=CType(name="Type"),
                            setter=True,
                        ),
                        "B": CProperty(
                            name="B",
                            declaring_type=CType(name="Name"),
                            type=CType(name="Type"),
                            setter=True,
                        ),
                    },
                ),
                DocNode(
                    name="Name",
                    children=[DocNode(name="A", return_doc=""), DocNode(name="B", return_doc="")],
                ),
            ),
        ),
        (
            "methods",
            (
                CClass(
                    name="Name",
                    methods={
                        "A(Type) -> Type": CMethod(
                            name="A",
                            declaring_type=CType(name="Name"),
                            parameters=[CParameter(name="param0", type=CType(name="Type"))],
                            return_types=[CType(name="Type")],
                        ),
                        "B(Type) -> Type": CMethod(
                            name="B",
                            declaring_type=CType(name="Name"),
                            parameters=[CParameter(name="param0", type=CType(name="Type"))],
                            return_types=[CType(name="Type")],
                        ),
                    },
                ),
                DocNode(
                    name="Name",
                    children=[
                        DocNode(
                            name="A(Type)",
                            parameter_docs={"param0": ""},
                            return_doc="",
                            exception_docs={},
                        ),
                        DocNode(
                            name="B(Type)",
                            parameter_docs={"param0": ""},
                            return_doc="",
                            exception_docs={},
                        ),
                    ],
                ),
            ),
        ),
        (
            "events",
            (
                CClass(
                    name="Name",
                    events={
                        "A -> (Type)": CEvent(
                            name="A", declaring_type=CType(name="Name"), type=CType(name="Type")
                        ),
                        "B -> (Type)": CEvent(
                            name="B", declaring_type=CType(name="Name"), type=CType(name="Type")
                        ),
                    },
                ),
                DocNode(
                    name="Name",
                    children=[DocNode(name="A"), DocNode(name="B")],
                ),
            ),
        ),
        (
            "nested_types",
            (
                CClass(
                    name="Name",
                    nested_types={
                        "A": CClass(name="A", parent=CType(name="Name")),
                        "B": CClass(name="B", parent=CType(name="Name")),
                    },
                ),
                DocNode(
                    name="Name",
                    children=[DocNode(name="A"), DocNode(name="B")],
                ),
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "doc"), **make_params(doc_objects))
    def test_doc_node(self, obj: CClass, doc: DocNode) -> None:
        """Test for CClass.doc_node()."""
        expected: DocNode = doc
        actual: DocNode = obj.doc_node()

        assert actual == expected

    compare_list: ClassVar[ParamSequence[tuple[CClass, CClass]]] = [
        ("name", (CClass(name="A"), CClass(name="B"))),
    ]

    @pytest.mark.parametrize(("x", "y"), **make_params(compare_list))
    def test_compare(self, x: CClass, y: CClass) -> None:
        """Test for CClass.compare()."""
        _compare(CClass, x, y)

    @pytest.mark.parametrize(("x", "y"), **make_params(compare_list))
    def test_compare_seq(self, x: CClass, y: CClass) -> None:
        """Test for CClass.compare_seq()."""
        _compare_seq(CClass, x, y)

    @pytest.mark.parametrize(
        ("obj1", "obj2", "expected"),
        **make_params(
            [
                ("basic", (CClass(name="A"), CClass(name="B"), CClass(name="A"))),
                (
                    "interfaces",
                    (
                        CClass(name="A", interfaces=[CType(name="A")]),
                        CClass(name="A", interfaces=[CType(name="B")]),
                        CClass(name="A", interfaces=[CType(name="A"), CType(name="B")]),
                    ),
                ),
                (
                    "fields",
                    (
                        CClass(
                            name="A",
                            fields={
                                "A": CField(
                                    name="A",
                                    declaring_type=CType(name="T"),
                                    return_type=CType(name="T"),
                                ),
                            },
                        ),
                        CClass(
                            name="A",
                            fields={
                                "B": CField(
                                    name="B",
                                    declaring_type=CType(name="T"),
                                    return_type=CType(name="T"),
                                ),
                            },
                        ),
                        CClass(
                            name="A",
                            fields={
                                "A": CField(
                                    name="A",
                                    declaring_type=CType(name="T"),
                                    return_type=CType(name="T"),
                                ),
                                "B": CField(
                                    name="B",
                                    declaring_type=CType(name="T"),
                                    return_type=CType(name="T"),
                                ),
                            },
                        ),
                    ),
                ),
                (
                    "constructors",
                    (
                        CClass(
                            name="A",
                            constructors={
                                "__init__()": CConstructor(
                                    declaring_type=CType(name="T"),
                                ),
                            },
                        ),
                        CClass(
                            name="A",
                            constructors={
                                "__init__(param: T)": CConstructor(
                                    declaring_type=CType(name="T"),
                                    parameters=[CParameter(name="param", type=CType(name="T"))],
                                ),
                            },
                        ),
                        CClass(
                            name="A",
                            constructors={
                                "__init__()": CConstructor(
                                    declaring_type=CType(name="T"),
                                ),
                                "__init__(param: T)": CConstructor(
                                    declaring_type=CType(name="T"),
                                    parameters=[CParameter(name="param", type=CType(name="T"))],
                                ),
                            },
                        ),
                    ),
                ),
                (
                    "properties",
                    (
                        CClass(
                            name="A",
                            properties={
                                "A": CProperty(
                                    name="A",
                                    declaring_type=CType(name="T"),
                                    type=CType(name="T"),
                                ),
                            },
                        ),
                        CClass(
                            name="A",
                            properties={
                                "B": CProperty(
                                    name="B",
                                    declaring_type=CType(name="T"),
                                    type=CType(name="T"),
                                ),
                            },
                        ),
                        CClass(
                            name="A",
                            properties={
                                "A": CProperty(
                                    name="A",
                                    declaring_type=CType(name="T"),
                                    type=CType(name="T"),
                                ),
                                "B": CProperty(
                                    name="B",
                                    declaring_type=CType(name="T"),
                                    type=CType(name="T"),
                                ),
                            },
                        ),
                    ),
                ),
                (
                    "methods",
                    (
                        CClass(
                            name="A",
                            methods={
                                "A()": CMethod(name="A", declaring_type=CType(name="T")),
                            },
                        ),
                        CClass(
                            name="A",
                            methods={
                                "B()": CMethod(name="B", declaring_type=CType(name="T")),
                            },
                        ),
                        CClass(
                            name="A",
                            methods={
                                "A()": CMethod(name="A", declaring_type=CType(name="T")),
                                "B()": CMethod(name="B", declaring_type=CType(name="T")),
                            },
                        ),
                    ),
                ),
                (
                    "events",
                    (
                        CClass(
                            name="A",
                            events={
                                "A": CEvent(
                                    name="A",
                                    declaring_type=CType(name="T"),
                                    type=CType(name="T"),
                                ),
                            },
                        ),
                        CClass(
                            name="A",
                            events={
                                "B": CEvent(
                                    name="B",
                                    declaring_type=CType(name="T"),
                                    type=CType(name="T"),
                                ),
                            },
                        ),
                        CClass(
                            name="A",
                            events={
                                "A": CEvent(
                                    name="A",
                                    declaring_type=CType(name="T"),
                                    type=CType(name="T"),
                                ),
                                "B": CEvent(
                                    name="B",
                                    declaring_type=CType(name="T"),
                                    type=CType(name="T"),
                                ),
                            },
                        ),
                    ),
                ),
                (
                    "nested_types",
                    (
                        CClass(
                            name="A",
                            nested_types={"A": CClass(name="A")},
                        ),
                        CClass(
                            name="A",
                            nested_types={"B": CClass(name="B")},
                        ),
                        CClass(
                            name="A",
                            nested_types={"A": CClass(name="A"), "B": CClass(name="B")},
                        ),
                    ),
                ),
            ]
        ),
    )
    def test_merge(self, obj1: CClass, obj2: CClass, expected: CClass) -> None:
        """Test for CClass.merge()."""
        actual: CClass = CClass.merge(obj1, obj2)

        assert actual == expected


class TestCInterface:
    """Tests for CInterface."""

    unique_name_objects: ClassVar[ParamSequence[tuple[CInterface, str]]] = [
        ("basic", (CInterface(name="Name"), "Name")),
        (
            "generic_args",
            (
                CInterface(
                    name="Name",
                    generic_args=[CType(name="A", generic=True), CType(name="B", generic=True)],
                ),
                "Name[$A, $B]",
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "expected"), **make_params(unique_name_objects))
    def test_unique_name(self, obj: CInterface, expected: str) -> None:
        """Test for CInterface.unique_name."""
        actual: str = obj.unique_name

        assert actual == expected

    json_objects: ClassVar[ParamSequence[tuple[CInterface, JsonType]]] = [
        (
            "basic",
            (
                CInterface(name="Name"),
                {
                    "events": {},
                    "fields": {},
                    "generic_args": [],
                    "interfaces": [],
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "parent": None,
                    "nested_types": {},
                    "properties": {},
                    "type": "interface",
                },
            ),
        ),
        (
            "generic_args",
            (
                CInterface(
                    name="Name",
                    generic_args=[CType(name="A", generic=True), CType(name="B", generic=True)],
                ),
                {
                    "type": "interface",
                    "name": "Name",
                    "namespace": None,
                    "parent": None,
                    "generic_args": ["$A", "$B"],
                    "interfaces": [],
                    "fields": {},
                    "properties": {},
                    "methods": {},
                    "events": {},
                    "nested_types": {},
                },
            ),
        ),
        (
            "interfaces",
            (
                CInterface(name="Name", interfaces=[CType(name="A"), CType(name="B")]),
                {
                    "events": {},
                    "fields": {},
                    "generic_args": [],
                    "interfaces": ["A", "B"],
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "parent": None,
                    "nested_types": {},
                    "properties": {},
                    "type": "interface",
                },
            ),
        ),
        (
            "fields",
            (
                CInterface(
                    name="Name",
                    fields={
                        "A": CField(
                            name="A",
                            declaring_type=CType(name="Name"),
                            return_type=CType(name="Type"),
                        ),
                        "B": CField(
                            name="B",
                            declaring_type=CType(name="Name"),
                            return_type=CType(name="Type"),
                        ),
                    },
                ),
                {
                    "events": {},
                    "fields": {
                        "A": {
                            "name": "A",
                            "declaring_type": "Name",
                            "return_type": "Type",
                            "static": False,
                        },
                        "B": {
                            "name": "B",
                            "declaring_type": "Name",
                            "return_type": "Type",
                            "static": False,
                        },
                    },
                    "generic_args": [],
                    "interfaces": [],
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "parent": None,
                    "nested_types": {},
                    "properties": {},
                    "type": "interface",
                },
            ),
        ),
        (
            "properties",
            (
                CInterface(
                    name="Name",
                    properties={
                        "A": CProperty(
                            name="A",
                            declaring_type=CType(name="Name"),
                            type=CType(name="Type"),
                            setter=True,
                        ),
                        "B": CProperty(
                            name="B",
                            declaring_type=CType(name="Name"),
                            type=CType(name="Type"),
                            setter=True,
                        ),
                    },
                ),
                {
                    "events": {},
                    "fields": {},
                    "generic_args": [],
                    "interfaces": [],
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "parent": None,
                    "nested_types": {},
                    "properties": {
                        "B": {
                            "name": "B",
                            "declaring_type": "Name",
                            "type": "Type",
                            "setter": True,
                            "static": False,
                        },
                        "A": {
                            "name": "A",
                            "declaring_type": "Name",
                            "type": "Type",
                            "setter": True,
                            "static": False,
                        },
                    },
                    "type": "interface",
                },
            ),
        ),
        (
            "methods",
            (
                CInterface(
                    name="Name",
                    methods={
                        "A(Type) -> Type": CMethod(
                            name="A",
                            declaring_type=CType(name="Name"),
                            parameters=[CParameter(name="param0", type=CType(name="Type"))],
                            return_types=[CType(name="Type")],
                        ),
                        "B(Type) -> Type": CMethod(
                            name="B",
                            declaring_type=CType(name="Name"),
                            parameters=[CParameter(name="param0", type=CType(name="Type"))],
                            return_types=[CType(name="Type")],
                        ),
                    },
                ),
                {
                    "events": {},
                    "fields": {},
                    "generic_args": [],
                    "interfaces": [],
                    "methods": {
                        "A(Type) -> Type": {
                            "name": "A",
                            "declaring_type": "Name",
                            "parameters": [
                                {
                                    "name": "param0",
                                    "type": "Type",
                                    "default": False,
                                    "out": False,
                                },
                            ],
                            "return_types": ["Type"],
                            "static": False,
                        },
                        "B(Type) -> Type": {
                            "name": "B",
                            "declaring_type": "Name",
                            "parameters": [
                                {
                                    "name": "param0",
                                    "type": "Type",
                                    "default": False,
                                    "out": False,
                                },
                            ],
                            "return_types": ["Type"],
                            "static": False,
                        },
                    },
                    "name": "Name",
                    "namespace": None,
                    "parent": None,
                    "nested_types": {},
                    "properties": {},
                    "type": "interface",
                },
            ),
        ),
        (
            "events",
            (
                CInterface(
                    name="Name",
                    events={
                        "A -> (Type)": CEvent(
                            name="A", declaring_type=CType(name="Name"), type=CType(name="Type")
                        ),
                        "B -> (Type)": CEvent(
                            name="B", declaring_type=CType(name="Name"), type=CType(name="Type")
                        ),
                    },
                ),
                {
                    "events": {
                        "A -> (Type)": {"name": "A", "declaring_type": "Name", "type": "Type"},
                        "B -> (Type)": {"name": "B", "declaring_type": "Name", "type": "Type"},
                    },
                    "fields": {},
                    "generic_args": [],
                    "interfaces": [],
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "parent": None,
                    "nested_types": {},
                    "properties": {},
                    "type": "interface",
                },
            ),
        ),
        (
            "nested_types",
            (
                CInterface(
                    name="Name",
                    nested_types={
                        "A": CInterface(name="A", parent=CType(name="Name")),
                        "B": CInterface(name="B", parent=CType(name="Name")),
                    },
                ),
                {
                    "events": {},
                    "fields": {},
                    "generic_args": [],
                    "interfaces": [],
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "parent": None,
                    "nested_types": {
                        "A": {
                            "events": {},
                            "fields": {},
                            "generic_args": [],
                            "interfaces": [],
                            "methods": {},
                            "name": "A",
                            "namespace": None,
                            "parent": "Name",
                            "nested_types": {},
                            "properties": {},
                            "type": "interface",
                        },
                        "B": {
                            "events": {},
                            "fields": {},
                            "generic_args": [],
                            "interfaces": [],
                            "methods": {},
                            "name": "B",
                            "namespace": None,
                            "parent": "Name",
                            "nested_types": {},
                            "properties": {},
                            "type": "interface",
                        },
                    },
                    "properties": {},
                    "type": "interface",
                },
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "json"), **make_params(json_objects))
    def test_to_json(self, obj: CInterface, json: JsonType) -> None:
        """Test for CInterface.to_json()."""
        expected: JsonType = json
        actual: JsonType = obj.to_json()

        assert actual == expected

    @pytest.mark.parametrize(("obj", "json"), **make_params(json_objects))
    def test_from_json(self, obj: CInterface, json: JsonType) -> None:
        """Test for CInterface.from_json()."""
        expected: CInterface = obj
        actual: CInterface = CInterface.from_json(json)

        assert actual == expected

    doc_objects: ClassVar[ParamSequence[tuple[CInterface, DocNode]]] = [
        ("basic", (CInterface(name="Name"), DocNode(name="Name"))),
        (
            "generic_args",
            (
                CInterface(
                    name="Name",
                    generic_args=[CType(name="A", generic=True), CType(name="B", generic=True)],
                ),
                DocNode(name="Name[$A, $B]"),
            ),
        ),
        (
            "interfaces",
            (
                CInterface(name="Name", interfaces=[CType(name="A"), CType(name="B")]),
                DocNode(name="Name"),
            ),
        ),
        (
            "fields",
            (
                CInterface(
                    name="Name",
                    fields={
                        "A": CField(
                            name="A",
                            declaring_type=CType(name="Name"),
                            return_type=CType(name="Type"),
                        ),
                        "B": CField(
                            name="B",
                            declaring_type=CType(name="Name"),
                            return_type=CType(name="Type"),
                        ),
                    },
                ),
                DocNode(
                    name="Name",
                    children=[DocNode(name="A", return_doc=""), DocNode(name="B", return_doc="")],
                ),
            ),
        ),
        (
            "properties",
            (
                CInterface(
                    name="Name",
                    properties={
                        "A": CProperty(
                            name="A",
                            declaring_type=CType(name="Name"),
                            type=CType(name="Type"),
                            setter=True,
                        ),
                        "B": CProperty(
                            name="B",
                            declaring_type=CType(name="Name"),
                            type=CType(name="Type"),
                            setter=True,
                        ),
                    },
                ),
                DocNode(
                    name="Name",
                    children=[DocNode(name="A", return_doc=""), DocNode(name="B", return_doc="")],
                ),
            ),
        ),
        (
            "methods",
            (
                CInterface(
                    name="Name",
                    methods={
                        "A(Type) -> Type": CMethod(
                            name="A",
                            declaring_type=CType(name="Name"),
                            parameters=[CParameter(name="param0", type=CType(name="Type"))],
                            return_types=[CType(name="Type")],
                        ),
                        "B(Type) -> Type": CMethod(
                            name="B",
                            declaring_type=CType(name="Name"),
                            parameters=[CParameter(name="param0", type=CType(name="Type"))],
                            return_types=[CType(name="Type")],
                        ),
                    },
                ),
                DocNode(
                    name="Name",
                    children=[
                        DocNode(
                            name="A(Type)",
                            parameter_docs={"param0": ""},
                            return_doc="",
                            exception_docs={},
                        ),
                        DocNode(
                            name="B(Type)",
                            parameter_docs={"param0": ""},
                            return_doc="",
                            exception_docs={},
                        ),
                    ],
                ),
            ),
        ),
        (
            "events",
            (
                CInterface(
                    name="Name",
                    events={
                        "A -> (Type)": CEvent(
                            name="A", declaring_type=CType(name="Name"), type=CType(name="Type")
                        ),
                        "B -> (Type)": CEvent(
                            name="B", declaring_type=CType(name="Name"), type=CType(name="Type")
                        ),
                    },
                ),
                DocNode(name="Name", children=[DocNode(name="A"), DocNode(name="B")]),
            ),
        ),
        (
            "nested_types",
            (
                CInterface(
                    name="Name",
                    nested_types={
                        "A": CInterface(name="A", parent=CType(name="Name")),
                        "B": CInterface(name="B", parent=CType(name="Name")),
                    },
                ),
                DocNode(name="Name", children=[DocNode(name="A"), DocNode(name="B")]),
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "doc"), **make_params(doc_objects))
    def test_doc_node(self, obj: CInterface, doc: DocNode) -> None:
        """Test for CInterface.doc_node()."""
        expected: DocNode = doc
        actual: DocNode = obj.doc_node()

        assert actual == expected

    compare_list: ClassVar[ParamSequence[tuple[CInterface, CInterface]]] = [
        ("name", (CInterface(name="A"), CInterface(name="B"))),
    ]

    @pytest.mark.parametrize(("x", "y"), **make_params(compare_list))
    def test_compare(self, x: CInterface, y: CInterface) -> None:
        """Test for CInterface.compare()."""
        _compare(CInterface, x, y)

    @pytest.mark.parametrize(("x", "y"), **make_params(compare_list))
    def test_compare_seq(self, x: CInterface, y: CInterface) -> None:
        """Test for CInterface.compare_seq()."""
        _compare_seq(CInterface, x, y)

    @pytest.mark.parametrize(
        ("obj1", "obj2", "expected"),
        **make_params(
            [
                ("basic", (CInterface(name="A"), CInterface(name="B"), CInterface(name="A"))),
                (
                    "interfaces",
                    (
                        CInterface(name="A", interfaces=[CType(name="A")]),
                        CInterface(name="A", interfaces=[CType(name="B")]),
                        CInterface(name="A", interfaces=[CType(name="A"), CType(name="B")]),
                    ),
                ),
                (
                    "fields",
                    (
                        CInterface(
                            name="A",
                            fields={
                                "A": CField(
                                    name="A",
                                    declaring_type=CType(name="T"),
                                    return_type=CType(name="T"),
                                ),
                            },
                        ),
                        CInterface(
                            name="A",
                            fields={
                                "B": CField(
                                    name="B",
                                    declaring_type=CType(name="T"),
                                    return_type=CType(name="T"),
                                ),
                            },
                        ),
                        CInterface(
                            name="A",
                            fields={
                                "A": CField(
                                    name="A",
                                    declaring_type=CType(name="T"),
                                    return_type=CType(name="T"),
                                ),
                                "B": CField(
                                    name="B",
                                    declaring_type=CType(name="T"),
                                    return_type=CType(name="T"),
                                ),
                            },
                        ),
                    ),
                ),
                (
                    "properties",
                    (
                        CInterface(
                            name="A",
                            properties={
                                "A": CProperty(
                                    name="A",
                                    declaring_type=CType(name="T"),
                                    type=CType(name="T"),
                                ),
                            },
                        ),
                        CInterface(
                            name="A",
                            properties={
                                "B": CProperty(
                                    name="B",
                                    declaring_type=CType(name="T"),
                                    type=CType(name="T"),
                                ),
                            },
                        ),
                        CInterface(
                            name="A",
                            properties={
                                "A": CProperty(
                                    name="A",
                                    declaring_type=CType(name="T"),
                                    type=CType(name="T"),
                                ),
                                "B": CProperty(
                                    name="B",
                                    declaring_type=CType(name="T"),
                                    type=CType(name="T"),
                                ),
                            },
                        ),
                    ),
                ),
                (
                    "methods",
                    (
                        CInterface(
                            name="A",
                            methods={
                                "A()": CMethod(name="A", declaring_type=CType(name="T")),
                            },
                        ),
                        CInterface(
                            name="A",
                            methods={
                                "B()": CMethod(name="B", declaring_type=CType(name="T")),
                            },
                        ),
                        CInterface(
                            name="A",
                            methods={
                                "A()": CMethod(name="A", declaring_type=CType(name="T")),
                                "B()": CMethod(name="B", declaring_type=CType(name="T")),
                            },
                        ),
                    ),
                ),
                (
                    "events",
                    (
                        CInterface(
                            name="A",
                            events={
                                "A": CEvent(
                                    name="A",
                                    declaring_type=CType(name="T"),
                                    type=CType(name="T"),
                                ),
                            },
                        ),
                        CInterface(
                            name="A",
                            events={
                                "B": CEvent(
                                    name="B",
                                    declaring_type=CType(name="T"),
                                    type=CType(name="T"),
                                ),
                            },
                        ),
                        CInterface(
                            name="A",
                            events={
                                "A": CEvent(
                                    name="A",
                                    declaring_type=CType(name="T"),
                                    type=CType(name="T"),
                                ),
                                "B": CEvent(
                                    name="B",
                                    declaring_type=CType(name="T"),
                                    type=CType(name="T"),
                                ),
                            },
                        ),
                    ),
                ),
                (
                    "nested_types",
                    (
                        CInterface(
                            name="A",
                            nested_types={"A": CInterface(name="A")},
                        ),
                        CInterface(
                            name="A",
                            nested_types={"B": CInterface(name="B")},
                        ),
                        CInterface(
                            name="A",
                            nested_types={"A": CInterface(name="A"), "B": CInterface(name="B")},
                        ),
                    ),
                ),
            ]
        ),
    )
    def test_merge(self, obj1: CInterface, obj2: CInterface, expected: CInterface) -> None:
        """Test for CInterface.merge()."""
        actual: CInterface = CInterface.merge(obj1, obj2)

        assert actual == expected


class TestCEnum:
    """Tests for CEnum."""

    unique_name_objects: ClassVar[ParamSequence[tuple[CEnum, str]]] = [
        ("basic", (CEnum(name="Name"), "Name")),
    ]

    @pytest.mark.parametrize(("obj", "expected"), **make_params(unique_name_objects))
    def test_unique_name(self, obj: CEnum, expected: str) -> None:
        """Test for CEnum.unique_name."""
        actual: str = obj.unique_name

        assert actual == expected

    json_objects: ClassVar[ParamSequence[tuple[CEnum, JsonType]]] = [
        (
            "basic",
            (
                CEnum(name="Name"),
                {"type": "enum", "name": "Name", "namespace": None, "parent": None, "fields": []},
            ),
        ),
        (
            "fields",
            (
                CEnum(name="Name", fields=["Field0", "Field1", "Field2", "Field3"]),
                {
                    "type": "enum",
                    "name": "Name",
                    "namespace": None,
                    "parent": None,
                    "fields": ["Field0", "Field1", "Field2", "Field3"],
                },
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "json"), **make_params(json_objects))
    def test_to_json(self, obj: CEnum, json: JsonType) -> None:
        """Test for CEnum.to_json()."""
        expected: JsonType = json
        actual: JsonType = obj.to_json()

        assert actual == expected

    @pytest.mark.parametrize(("obj", "json"), **make_params(json_objects))
    def test_from_json(self, obj: CEnum, json: JsonType) -> None:
        """Test for CEnum.from_json()."""
        expected: CEnum = obj
        actual: CEnum = CEnum.from_json(json)

        assert actual == expected

    doc_objects: ClassVar[ParamSequence[tuple[CEnum, DocNode]]] = [
        ("basic", (CEnum(name="Name"), DocNode(name="Name"))),
        (
            "fields",
            (
                CEnum(name="Name", fields=["Field0", "Field1", "Field2", "Field3"]),
                DocNode(
                    name="Name",
                    children=[
                        DocNode(name="Field0"),
                        DocNode(name="Field1"),
                        DocNode(name="Field2"),
                        DocNode(name="Field3"),
                    ],
                ),
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "doc"), **make_params(doc_objects))
    def test_doc_node(self, obj: CEnum, doc: DocNode) -> None:
        """Test for CEnum.doc_node()."""
        expected: DocNode = doc
        actual: DocNode = obj.doc_node()

        assert actual == expected

    compare_list: ClassVar[ParamSequence[tuple[CEnum, CEnum]]] = [
        ("name", (CEnum(name="A"), CEnum(name="B"))),
    ]

    @pytest.mark.parametrize(("x", "y"), **make_params(compare_list))
    def test_compare(self, x: CEnum, y: CEnum) -> None:
        """Test for CEnum.compare()."""
        _compare(CEnum, x, y)

    @pytest.mark.parametrize(("x", "y"), **make_params(compare_list))
    def test_compare_seq(self, x: CEnum, y: CEnum) -> None:
        """Test for CEnum.compare_seq()."""
        _compare_seq(CEnum, x, y)

    @pytest.mark.parametrize(
        ("obj1", "obj2", "expected"),
        **make_params([("basic", (CEnum(name="A"), CEnum(name="B"), CEnum(name="A")))]),
    )
    def test_merge(self, obj1: CEnum, obj2: CEnum, expected: CEnum) -> None:
        """Test for CEnum.merge()."""
        actual: CEnum = CEnum.merge(obj1, obj2)

        assert actual == expected


class TestCDelegate:
    """Tests for CDelegate."""

    unique_name_objects: ClassVar[ParamSequence[tuple[CDelegate, str]]] = [
        ("basic", (CDelegate(name="Name"), "Name()")),
        (
            "parameters",
            (
                CDelegate(
                    name="Name",
                    parameters=[
                        CParameter(name="param0", type=CType(name="A")),
                        CParameter(name="param1", type=CType(name="B")),
                    ],
                ),
                "Name(A, B)",
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "expected"), **make_params(unique_name_objects))
    def test_unique_name(self, obj: CDelegate, expected: str) -> None:
        """Test for CDelegate.unique_name."""
        actual: str = obj.unique_name

        assert actual == expected

    json_objects: ClassVar[ParamSequence[tuple[CDelegate, JsonType]]] = [
        (
            "basic",
            (
                CDelegate(name="Name"),
                {
                    "type": "delegate",
                    "name": "Name",
                    "namespace": None,
                    "parent": None,
                    "parameters": [],
                    "return_type": "System:Void",
                },
            ),
        ),
        (
            "parameters",
            (
                CDelegate(
                    name="Name",
                    parameters=[
                        CParameter(name="param0", type=CType(name="Type")),
                        CParameter(name="param1", type=CType(name="Type")),
                    ],
                ),
                {
                    "type": "delegate",
                    "name": "Name",
                    "namespace": None,
                    "parent": None,
                    "parameters": [
                        {"name": "param0", "type": "Type", "default": False, "out": False},
                        {"name": "param1", "type": "Type", "default": False, "out": False},
                    ],
                    "return_type": "System:Void",
                },
            ),
        ),
        (
            "return_type",
            (
                CDelegate(name="Name", return_type=CType(name="Type")),
                {
                    "type": "delegate",
                    "name": "Name",
                    "namespace": None,
                    "parent": None,
                    "parameters": [],
                    "return_type": "Type",
                },
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "json"), **make_params(json_objects))
    def test_to_json(self, obj: CDelegate, json: JsonType) -> None:
        """Test for CDelegate.to_json()."""
        expected: JsonType = json
        actual: JsonType = obj.to_json()

        assert actual == expected

    @pytest.mark.parametrize(("obj", "json"), **make_params(json_objects))
    def test_from_json(self, obj: CDelegate, json: JsonType) -> None:
        """Test for CDelegate.from_json()."""
        expected: CDelegate = obj
        actual: CDelegate = CDelegate.from_json(json)

        assert actual == expected

    doc_objects: ClassVar[ParamSequence[tuple[CDelegate, DocNode]]] = [
        ("basic", (CDelegate(name="Name"), DocNode(name="Name()"))),
        (
            "parameters",
            (
                CDelegate(
                    name="Name",
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type")),
                        CParameter(name="param1", type=CType(name="Type")),
                    ),
                ),
                DocNode(name="Name(Type, Type)", parameter_docs={"param0": "", "param1": ""}),
            ),
        ),
        (
            "return_type",
            (
                CDelegate(name="Name", return_type=CType(name="Type")),
                DocNode(name="Name()", doc="", return_doc=""),
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "doc"), **make_params(doc_objects))
    def test_doc_node(self, obj: CDelegate, doc: DocNode) -> None:
        """Test for CDelegate.doc_node()."""
        expected: DocNode = doc
        actual: DocNode = obj.doc_node()

        assert actual == expected

    compare_list: ClassVar[ParamSequence[tuple[CDelegate, CDelegate]]] = [
        ("name", (CDelegate(name="A"), CDelegate(name="B"))),
    ]

    @pytest.mark.parametrize(("x", "y"), **make_params(compare_list))
    def test_compare(self, x: CDelegate, y: CDelegate) -> None:
        """Test for CDelegate.compare()."""
        _compare(CDelegate, x, y)

    @pytest.mark.parametrize(("x", "y"), **make_params(compare_list))
    def test_compare_seq(self, x: CDelegate, y: CDelegate) -> None:
        """Test for CDelegate.compare_seq()."""
        _compare_seq(CDelegate, x, y)

    @pytest.mark.parametrize(
        ("obj1", "obj2", "expected"),
        **make_params([("basic", (CDelegate(name="A"), CDelegate(name="B"), CDelegate(name="A")))]),
    )
    def test_merge(self, obj1: CDelegate, obj2: CDelegate, expected: CDelegate) -> None:
        """Test for CDelegate.merge()."""
        actual: CDelegate = CDelegate.merge(obj1, obj2)

        assert actual == expected


class TestCNamespace:
    """Tests for CNamespace."""

    unique_name_objects: ClassVar[ParamSequence[tuple[CNamespace, str]]] = [
        ("basic", (CNamespace(name="Name"), "Name")),
    ]

    @pytest.mark.parametrize(("obj", "expected"), **make_params(unique_name_objects))
    def test_unique_name(self, obj: CNamespace, expected: str) -> None:
        """Test for CNamespace.unique_name."""
        actual: str = obj.unique_name

        assert actual == expected

    json_objects: ClassVar[ParamSequence[tuple[CNamespace, JsonType]]] = [
        (
            "basic",
            (
                CNamespace(
                    name="Namespace",
                    types={
                        "Namespace:IInterface": CInterface(
                            name="IInterface", namespace="Namespace"
                        ),
                        "Namespace:Class": CClass(name="Class", namespace="Namespace"),
                        "Namespace:Delegate": CDelegate(name="Delegate", namespace="Namespace"),
                        "Namespace:Enum": CEnum(name="Enum", namespace="Namespace"),
                    },
                ),
                {
                    "name": "Namespace",
                    "types": {
                        "Namespace:IInterface": {
                            "type": "interface",
                            "name": "IInterface",
                            "namespace": "Namespace",
                            "parent": None,
                            "generic_args": [],
                            "interfaces": [],
                            "fields": {},
                            "properties": {},
                            "methods": {},
                            "events": {},
                            "nested_types": {},
                        },
                        "Namespace:Class": {
                            "type": "class",
                            "name": "Class",
                            "namespace": "Namespace",
                            "parent": None,
                            "abstract": False,
                            "generic_args": [],
                            "super_class": None,
                            "interfaces": [],
                            "fields": {},
                            "constructors": {},
                            "properties": {},
                            "methods": {},
                            "events": {},
                            "nested_types": {},
                        },
                        "Namespace:Delegate": {
                            "type": "delegate",
                            "name": "Delegate",
                            "namespace": "Namespace",
                            "parent": None,
                            "parameters": [],
                            "return_type": "System:Void",
                        },
                        "Namespace:Enum": {
                            "type": "enum",
                            "name": "Enum",
                            "namespace": "Namespace",
                            "parent": None,
                            "fields": [],
                        },
                    },
                },
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "json"), **make_params(json_objects))
    def test_to_json(self, obj: CNamespace, json: JsonType) -> None:
        """Test for CNamespace.to_json()."""
        expected: JsonType = json
        actual: JsonType = obj.to_json()

        assert actual == expected

    @pytest.mark.parametrize(("obj", "json"), **make_params(json_objects))
    def test_from_json(self, obj: CNamespace, json: JsonType) -> None:
        """Test for CNamespace.from_json()."""
        expected: CNamespace = obj
        actual: CNamespace = CNamespace.from_json(json)

        assert actual == expected

    compare_list: ClassVar[ParamSequence[tuple[CNamespace, CNamespace]]] = [
        ("name", (CNamespace(name="A"), CNamespace(name="B"))),
    ]

    @pytest.mark.parametrize(("x", "y"), **make_params(compare_list))
    def test_compare(self, x: CNamespace, y: CNamespace) -> None:
        """Test for CNamespace.compare()."""
        _compare(CNamespace, x, y)

    @pytest.mark.parametrize(("x", "y"), **make_params(compare_list))
    def test_compare_seq(self, x: CNamespace, y: CNamespace) -> None:
        """Test for CNamespace.compare_seq()."""
        _compare_seq(CNamespace, x, y)

    @pytest.mark.parametrize(
        ("obj1", "obj2", "expected"),
        **make_params(
            [
                ("basic", (CNamespace(name="A"), CNamespace(name="B"), CNamespace(name="A"))),
                (
                    "class",
                    (
                        CNamespace(name="A", types={"A": CClass(name="A")}),
                        CNamespace(name="A", types={"A": CClass(name="A")}),
                        CNamespace(name="A", types={"A": CClass(name="A")}),
                    ),
                ),
                (
                    "interface",
                    (
                        CNamespace(name="A", types={"A": CInterface(name="A")}),
                        CNamespace(name="A", types={"A": CInterface(name="A")}),
                        CNamespace(name="A", types={"A": CInterface(name="A")}),
                    ),
                ),
                (
                    "enum",
                    (
                        CNamespace(name="A", types={"A": CEnum(name="A")}),
                        CNamespace(name="A", types={"A": CEnum(name="A")}),
                        CNamespace(name="A", types={"A": CEnum(name="A")}),
                    ),
                ),
                (
                    "delegate",
                    (
                        CNamespace(name="A", types={"A": CDelegate(name="A")}),
                        CNamespace(name="A", types={"A": CDelegate(name="A")}),
                        CNamespace(name="A", types={"A": CDelegate(name="A")}),
                    ),
                ),
            ]
        ),
    )
    def test_merge(self, obj1: CNamespace, obj2: CNamespace, expected: CNamespace) -> None:
        """Test for CNamespace.merge()."""
        actual: CNamespace = CNamespace.merge(obj1, obj2)

        assert actual == expected


class TestCAssembly:
    """Tests for CAssembly."""

    unique_name_objects: ClassVar[ParamSequence[tuple[CNamespace, str]]] = [
        ("basic", (CAssembly(name="Name", version="0.0.0.0"), "Name")),
    ]

    @pytest.mark.parametrize(("obj", "expected"), **make_params(unique_name_objects))
    def test_unique_name(self, obj: CAssembly, expected: str) -> None:
        """Test for CAssembly.unique_name."""
        actual: str = obj.unique_name

        assert actual == expected

    json_objects: ClassVar[ParamSequence[tuple[CAssembly, JsonType]]] = [
        (
            "basic",
            (
                CAssembly(
                    name="Name",
                    version="0.0.0.0",
                    namespaces={
                        "A": CNamespace(name="A"),
                        "B": CNamespace(name="B"),
                        "C": CNamespace(name="C"),
                        "D": CNamespace(name="D"),
                    },
                ),
                {
                    "name": "Name",
                    "version": "0.0.0.0",
                    "namespaces": {
                        "A": {"name": "A", "types": {}},
                        "B": {"name": "B", "types": {}},
                        "C": {"name": "C", "types": {}},
                        "D": {"name": "D", "types": {}},
                    },
                },
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "json"), **make_params(json_objects))
    def test_to_json(self, obj: CAssembly, json: JsonType) -> None:
        """Test for CAssembly.to_json()."""
        expected: JsonType = json
        actual: JsonType = obj.to_json()

        assert actual == expected

    @pytest.mark.parametrize(("obj", "json"), **make_params(json_objects))
    def test_from_json(self, obj: CAssembly, json: JsonType) -> None:
        """Test for CAssembly.from_json()."""
        expected: CAssembly = obj
        actual: CAssembly = CAssembly.from_json(json)

        assert actual == expected

    compare_list: ClassVar[ParamSequence[tuple[CAssembly, CAssembly]]] = [
        ("name", (CAssembly(name="A", version="0.0.0.0"), CAssembly(name="B", version="0.0.0.0"))),
        (
            "version",
            (CAssembly(name="A", version="0.0.0.0"), CAssembly(name="A", version="1.0.0.0")),
        ),
    ]

    @pytest.mark.parametrize(("x", "y"), **make_params(compare_list))
    def test_compare(self, x: CAssembly, y: CAssembly) -> None:
        """Test for CAssembly.compare()."""
        _compare(CAssembly, x, y)

    @pytest.mark.parametrize(("x", "y"), **make_params(compare_list))
    def test_compare_seq(self, x: CAssembly, y: CAssembly) -> None:
        """Test for CAssembly.compare_seq()."""
        _compare_seq(CAssembly, x, y)


if __name__ == "__main__":
    pytest.main()
