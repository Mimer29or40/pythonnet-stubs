"""Tests for stubgen.model.py."""

from __future__ import annotations

from typing import TYPE_CHECKING
from typing import ClassVar

import pytest
from conftest import make_params

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
from stubgen.model import DocTree
from stubgen.model import ImportList

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
        """Test for DocTree.pattern."""
        actual: Sequence[str] = DocTree._split_node_string(string)  # noqa: SLF001

        assert actual == expected

    class TestGetItem:
        """Tests for DocTree.__getitem__()."""

        def test_empty(self) -> None:
            """Test for DocTree.__getitem__() with an empty string."""
            doc: DocTree = DocTree("Test")

            expected: DocTree | None = None
            actual: DocTree | None = doc[""]

            assert actual == expected

        def test_child(self) -> None:
            """Test for DocTree.__getitem__()."""
            child: DocTree = DocTree("Child")
            doc: DocTree = DocTree("Test", children=[child])

            expected: DocTree | None = child
            actual: DocTree | None = doc["Child"]

            assert actual == expected

        def test_grandchild(self) -> None:
            """Test for DocTree.__getitem__()."""
            grandchild: DocTree = DocTree("Grandchild")
            child: DocTree = DocTree("Child", children=[grandchild])
            doc: DocTree = DocTree("Test", children=[child])

            expected: DocTree | None = grandchild
            actual: DocTree | None = doc["Child.Grandchild"]

            assert actual == expected

        def test_missing(self) -> None:
            """Test for DocTree.__getitem__() with a missing child."""
            doc: DocTree = DocTree("Test")

            expected: DocTree | None = None
            actual: DocTree | None = doc["Child"]

            assert actual == expected

    @pytest.mark.parametrize(
        ("doc", "indent", "expected"),
        **make_params(
            [
                ("empty", (DocTree("A"), 0, ['""""""'])),
                ("empty_indent", (DocTree("A"), 1, ['    """"""'])),
                ("single_line", (DocTree("A", doc="Summary line."), 0, ['"""Summary line."""'])),
                (
                    "single_line_indent",
                    (
                        DocTree("A", doc="Summary line."),
                        1,
                        ['    """Summary line."""   # noqa: E501'],
                    ),
                ),
                (
                    "paragraph",
                    (
                        DocTree("A", doc="Summary line.\nParagraph line."),
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
                        DocTree("A", doc="Summary line.\nParagraph line."),
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
                        DocTree("A", doc="Summary line.\nLong paragraph line."),
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
                        DocTree("A", doc="Summary line.\nLong paragraph line."),
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
                        DocTree("A", parameter_docs={f"p{i}": f"Parameter {i}" for i in range(2)}),
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
                        DocTree("A", parameter_docs={f"p{i}": f"Parameter {i}" for i in range(2)}),
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
                        DocTree("A", return_doc="Return string."),
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
                        DocTree("A", return_doc="Return string."),
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
                        DocTree("A", exception_docs={f"E{i}": f"Except {i}" for i in range(2)}),
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
                        DocTree("A", exception_docs={f"E{i}": f"Except {i}" for i in range(2)}),
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
                        DocTree(
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
                        DocTree(
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
    def test_doc_string(self, doc: DocTree, indent: int, expected: Sequence[str]) -> None:
        """Test for DocTree.doc_string()."""
        actual: Sequence[str] = doc.doc_string(20, indent=indent)

        assert actual == expected

    json_list: ClassVar[ParamSequence[tuple[DocTree, JsonType]]] = [
        ("basic", (DocTree("A"), {"doc": "", "doc_formatted": {}})),
        (
            "parameters",
            (
                DocTree("A", parameter_docs={f"p{i}": "" for i in range(2)}),
                {"doc": "", "doc_formatted": {}, "parameters": {"p0": "", "p1": ""}},
            ),
        ),
        (
            "parameters_empty",
            (
                DocTree("A", parameter_docs={}),
                {"doc": "", "doc_formatted": {}, "parameters": {}},
            ),
        ),
        (
            "return",
            (
                DocTree("A", return_doc=""),
                {"doc": "", "doc_formatted": {}, "return": ""},
            ),
        ),
        (
            "exceptions",
            (
                DocTree("A", exception_docs={f"e{i}": "" for i in range(2)}),
                {"doc": "", "doc_formatted": {}, "exceptions": {"e0": "", "e1": ""}},
            ),
        ),
        (
            "exceptions_empty",
            (
                DocTree("A", exception_docs={}),
                {"doc": "", "doc_formatted": {}, "exceptions": {}},
            ),
        ),
        (
            "exceptions_children",
            (
                DocTree("A", children=(DocTree("B"),)),
                {"doc": "", "doc_formatted": {}, "B": {"doc": "", "doc_formatted": {}}},
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
        actual: DocTree = DocTree.from_json("A", json)

        assert actual == expected


class TestImportList:
    """Tests for ImportList."""

    @pytest.fixture
    def import_list(self) -> ImportList:
        """ImportList fixture."""
        return ImportList()

    class TestAddType:
        """Tests for ImportList.add_type()."""

        def test_basic(self, import_list: ImportList) -> None:
            """Test for ImportList.add_type()."""
            obj: CType = CType(name="Type")

            import_list.add_type(obj)

            expected: set[str] = {"Type"}

            assert import_list.types == expected

        def test_generic(self, import_list: ImportList) -> None:
            """Test for ImportList.add_type() with a generic type."""
            obj: CType = CType(name="Type", generic=True)

            import_list.add_type(obj)

            expected: set[str] = set()

            assert import_list.types == expected

        def test_inner(self, import_list: ImportList) -> None:
            """Test for ImportList.add_type() with inner types."""
            obj: CType = CType(name="Type", inner=(CType(name="InnerA"), CType(name="InnerB")))

            import_list.add_type(obj)

            expected: set[str] = {"Type", "InnerA", "InnerB"}

            assert import_list.types == expected

    def test_add_event_type(self, import_list: ImportList) -> None:
        """Test for ImportList.add_event_type()."""
        import_list.add_event_type()

        expected: set[str] = {ImportList.EVENT_TYPE}

        assert import_list.types == expected

    def test_build(self, import_list: ImportList) -> None:
        """Test for ImportList.build()."""
        import_list.add_type(CType(name="TypeA", namespace="Namespace"))
        import_list.add_type(CType(name="TypeB", namespace="Namespace"))
        import_list.add_type(CType(name="TypeC", namespace="Namespace"))
        import_list.add_type(CType(name="TypeD", namespace="Namespace"))

        expected: Sequence[str] = [
            "from Namespace import TypeA",
            "from Namespace import TypeB",
            "from Namespace import TypeC",
            "from Namespace import TypeD",
        ]
        actual: Sequence[str] = import_list.build("")

        assert actual == expected

    def test_build_namespace(self, import_list: ImportList) -> None:
        """Test for ImportList.build()."""
        import_list.add_type(CType(name="TypeA", namespace="Namespace"))
        import_list.add_type(CType(name="TypeB", namespace="Namespace"))
        import_list.add_type(CType(name="TypeC", namespace="Namespace.Namespace"))
        import_list.add_type(CType(name="TypeD", namespace="Namespace.Namespace"))

        expected: Sequence[str] = [
            "from Namespace.Namespace import TypeC",
            "from Namespace.Namespace import TypeD",
        ]
        actual: Sequence[str] = import_list.build("Namespace")

        assert actual == expected

    def test_build_event_type(self, import_list: ImportList) -> None:
        """Test for ImportList.build()."""
        import_list.add_type(CType(name="TypeA", namespace="Namespace"))
        import_list.add_type(CType(name="TypeB", namespace="Namespace"))
        import_list.add_type(CType(name="TypeC", namespace="Namespace"))
        import_list.add_type(CType(name="TypeD", namespace="Namespace"))
        import_list.add_event_type()

        expected: Sequence[str] = [
            "from Namespace import TypeA",
            "from Namespace import TypeB",
            "from Namespace import TypeC",
            "from Namespace import TypeD",
            "class EventType[T]:",
            "    def __iadd__(self, other: T) -> Self: ...",
            "    def __isub__(self, other: T) -> Self: ...",
        ]
        actual: Sequence[str] = import_list.build("")

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
        ("inner", (CType(name="Name", inner=(CType(name="A"), CType(name="B"))), "Name[A, B]")),
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
        ("inner", (CType(name="Name", inner=(CType(name="A"), CType(name="B"))), "Name[A, B]")),
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

    def test_to_doc_tree(self) -> None:
        """Test for CType.to_doc_json()."""
        with pytest.raises(NotImplementedError):
            CType(name="Name").to_doc_tree()

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

    def test_to_doc_tree(self) -> None:
        """Test for CParameter.to_doc_json()."""
        with pytest.raises(NotImplementedError):
            CParameter(name="Name", type=CType(name="Type")).to_doc_tree()

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

    doc_objects: ClassVar[ParamSequence[tuple[CField, DocTree]]] = [
        (
            "basic",
            (
                CField(name="Name", declaring_type=CType(name="Type"), return_type=CType.VOID),
                DocTree(name="Name"),
            ),
        ),
        (
            "return",
            (
                CField(
                    name="Name", declaring_type=CType(name="Type"), return_type=CType(name="Type")
                ),
                DocTree(name="Name", return_doc=""),
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "doc"), **make_params(doc_objects))
    def test_to_doc_tree(self, obj: CField, doc: DocTree) -> None:
        """Test for CField.to_doc_json()."""
        expected: DocTree = doc
        actual: DocTree = obj.to_doc_tree()

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
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type")),
                        CParameter(name="param0", type=CType(name="Type")),
                    ),
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
                {"declaring_type": "Type", "parameters": ()},
            ),
        ),
        (
            "parameters",
            (
                CConstructor(
                    declaring_type=CType(name="Type"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type")),
                        CParameter(name="param1", type=CType(name="Type")),
                    ),
                ),
                {
                    "declaring_type": "Type",
                    "parameters": (
                        {"name": "param0", "type": "Type", "default": False, "out": False},
                        {"name": "param1", "type": "Type", "default": False, "out": False},
                    ),
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

    doc_objects: ClassVar[ParamSequence[tuple[CConstructor, DocTree]]] = [
        (
            "basic",
            (CConstructor(declaring_type=CType(name="Type")), DocTree("__init__()")),
        ),
        (
            "parameters",
            (
                CConstructor(
                    declaring_type=CType(name="Type"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type")),
                        CParameter(name="param1", type=CType(name="Type")),
                    ),
                ),
                DocTree(
                    "__init__(Type, Type)",
                    parameter_docs={"param0": "", "param1": ""},
                ),
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "doc"), **make_params(doc_objects))
    def test_to_doc_tree(self, obj: CConstructor, doc: DocTree) -> None:
        """Test for CConstructor.to_doc_json()."""
        expected: DocTree = doc
        actual: DocTree = obj.to_doc_tree()

        assert actual == expected

    compare_list: ClassVar[ParamSequence[tuple[CConstructor, CConstructor]]] = [
        (
            "name",
            (
                CConstructor(
                    declaring_type=CType(name="Type"),
                    parameters=(CParameter(name="Name", type=CType(name="A")),),
                ),
                CConstructor(
                    declaring_type=CType(name="Type"),
                    parameters=(CParameter(name="Name", type=CType(name="B")),),
                ),
            ),
        ),
        (
            "parameter_length",
            (
                CConstructor(declaring_type=CType(name="Type")),
                CConstructor(
                    declaring_type=CType(name="Type"),
                    parameters=(CParameter(name="Name", type=CType(name="Type")),),
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

    doc_objects: ClassVar[ParamSequence[tuple[CProperty, DocTree]]] = [
        (
            "basic",
            (
                CProperty(name="Name", declaring_type=CType(name="Type"), type=CType.VOID),
                DocTree(name="Name"),
            ),
        ),
        (
            "return",
            (
                CProperty(name="Name", declaring_type=CType(name="Type"), type=CType(name="Type")),
                DocTree(name="Name", return_doc=""),
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "doc"), **make_params(doc_objects))
    def test_to_doc_tree(self, obj: CProperty, doc: DocTree) -> None:
        """Test for CProperty.to_doc_json()."""
        expected: DocTree = doc
        actual: DocTree = obj.to_doc_tree()

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
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type")),
                        CParameter(name="param0", type=CType(name="Type")),
                    ),
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
                    "parameters": (),
                    "return_types": (),
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
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type")),
                        CParameter(name="param1", type=CType(name="Type")),
                    ),
                ),
                {
                    "name": "Name",
                    "declaring_type": "Type",
                    "parameters": (
                        {"name": "param0", "type": "Type", "default": False, "out": False},
                        {"name": "param1", "type": "Type", "default": False, "out": False},
                    ),
                    "return_types": (),
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
                    return_types=(CType(name="Type"), CType(name="Type")),
                ),
                {
                    "name": "Name",
                    "declaring_type": "Type",
                    "parameters": (),
                    "return_types": ("Type", "Type"),
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
                    "parameters": (),
                    "return_types": (),
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

    doc_objects: ClassVar[ParamSequence[tuple[CMethod, DocTree]]] = [
        (
            "basic",
            (
                CMethod(name="Name", declaring_type=CType(name="Type")),
                DocTree(name="Name()", exception_docs={}),
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
                DocTree(
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
                DocTree(name="Name()", return_doc="", exception_docs={}),
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
                DocTree(name="Name()", exception_docs={}),
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "doc"), **make_params(doc_objects))
    def test_to_doc_tree(self, obj: CMethod, doc: DocTree) -> None:
        """Test for CMethod.to_doc_json()."""
        expected: DocTree = doc
        actual: DocTree = obj.to_doc_tree()

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

    doc_objects: ClassVar[ParamSequence[tuple[CEvent, DocTree]]] = [
        (
            "basic",
            (
                CEvent(name="Name", declaring_type=CType(name="Type"), type=CType(name="Type")),
                DocTree(name="Name"),
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "doc"), **make_params(doc_objects))
    def test_to_doc_tree(self, obj: CEvent, doc: DocTree) -> None:
        """Test for CEvent.to_doc_json()."""
        expected: DocTree = doc
        actual: DocTree = obj.to_doc_tree()

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
                        "Namespace:Struct": CStruct(name="Struct", namespace="Namespace"),
                    },
                ),
                {
                    "name": "Namespace",
                    "types": {
                        "Namespace:IInterface": {
                            "type": "interface",
                            "name": "IInterface",
                            "namespace": "Namespace",
                            "nested": None,
                            "generic_args": (),
                            "interfaces": (),
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
                            "nested": None,
                            "abstract": False,
                            "generic_args": (),
                            "super_class": None,
                            "interfaces": (),
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
                            "nested": None,
                            "parameters": (),
                            "return_type": "System:Void",
                        },
                        "Namespace:Enum": {
                            "type": "enum",
                            "name": "Enum",
                            "namespace": "Namespace",
                            "nested": None,
                            "fields": (),
                        },
                        "Namespace:Struct": {
                            "type": "struct",
                            "name": "Struct",
                            "namespace": "Namespace",
                            "nested": None,
                            "abstract": False,
                            "generic_args": (),
                            "super_class": None,
                            "interfaces": (),
                            "fields": {},
                            "constructors": {},
                            "properties": {},
                            "methods": {},
                            "events": {},
                            "nested_types": {},
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

    def test_to_doc_tree(self) -> None:
        """Test for CNamespace.to_doc_json()."""
        with pytest.raises(NotImplementedError):
            CNamespace(name="Name").to_doc_tree()

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


class TestCClass:
    """Tests for CClass."""

    unique_name_objects: ClassVar[ParamSequence[tuple[CClass, str]]] = [
        ("basic", (CClass(name="Name"), "Name")),
        (
            "generic_args",
            (
                CClass(
                    name="Name",
                    generic_args=(CType(name="A", generic=True), CType(name="B", generic=True)),
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
                    "generic_args": (),
                    "interfaces": (),
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "nested": None,
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
                    "nested": None,
                    "abstract": True,
                    "generic_args": (),
                    "super_class": None,
                    "interfaces": (),
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
                    generic_args=(CType(name="A", generic=True), CType(name="B", generic=True)),
                ),
                {
                    "type": "class",
                    "name": "Name",
                    "namespace": None,
                    "nested": None,
                    "abstract": False,
                    "generic_args": ("$A", "$B"),
                    "super_class": None,
                    "interfaces": (),
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
                    "generic_args": (),
                    "interfaces": (),
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "nested": None,
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
                CClass(name="Name", interfaces=(CType(name="A"), CType(name="B"))),
                {
                    "abstract": False,
                    "constructors": {},
                    "events": {},
                    "fields": {},
                    "generic_args": (),
                    "interfaces": ("A", "B"),
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "nested": None,
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
                        "Name.A": CField(
                            name="A",
                            declaring_type=CType(name="Name"),
                            return_type=CType(name="Type"),
                        ),
                        "Name.B": CField(
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
                        "Name.A": {
                            "name": "A",
                            "declaring_type": "Name",
                            "return_type": "Type",
                            "static": False,
                        },
                        "Name.B": {
                            "name": "B",
                            "declaring_type": "Name",
                            "return_type": "Type",
                            "static": False,
                        },
                    },
                    "generic_args": (),
                    "interfaces": (),
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "nested": None,
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
                        "Name.__init__()": CConstructor(declaring_type=CType(name="Name")),
                        "Name.__init__(Namespace:Type)": CConstructor(
                            declaring_type=CType(name="Name"),
                            parameters=(CParameter(name="param0", type=CType(name="Type")),),
                        ),
                    },
                ),
                {
                    "abstract": False,
                    "constructors": {
                        "Name.__init__()": {"declaring_type": "Name", "parameters": ()},
                        "Name.__init__(Namespace:Type)": {
                            "declaring_type": "Name",
                            "parameters": (
                                {"name": "param0", "type": "Type", "default": False, "out": False},
                            ),
                        },
                    },
                    "events": {},
                    "fields": {},
                    "generic_args": (),
                    "interfaces": (),
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "nested": None,
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
                        "Name.A": CProperty(
                            name="A",
                            declaring_type=CType(name="Name"),
                            type=CType(name="Type"),
                            setter=True,
                        ),
                        "Name.B": CProperty(
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
                    "generic_args": (),
                    "interfaces": (),
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "nested": None,
                    "nested_types": {},
                    "properties": {
                        "Name.B": {
                            "name": "B",
                            "declaring_type": "Name",
                            "type": "Type",
                            "setter": True,
                            "static": False,
                        },
                        "Name.A": {
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
                        "Name.A(Type) -> Type": CMethod(
                            name="A",
                            declaring_type=CType(name="Name"),
                            parameters=(CParameter(name="param0", type=CType(name="Type")),),
                            return_types=(CType(name="Type"),),
                        ),
                        "Name.B(Type) -> Type": CMethod(
                            name="B",
                            declaring_type=CType(name="Name"),
                            parameters=(CParameter(name="param0", type=CType(name="Type")),),
                            return_types=(CType(name="Type"),),
                        ),
                    },
                ),
                {
                    "abstract": False,
                    "constructors": {},
                    "events": {},
                    "fields": {},
                    "generic_args": (),
                    "interfaces": (),
                    "methods": {
                        "Name.A(Type) -> Type": {
                            "name": "A",
                            "declaring_type": "Name",
                            "parameters": (
                                {
                                    "name": "param0",
                                    "type": "Type",
                                    "default": False,
                                    "out": False,
                                },
                            ),
                            "return_types": ("Type",),
                            "static": False,
                        },
                        "Name.B(Type) -> Type": {
                            "name": "B",
                            "declaring_type": "Name",
                            "parameters": (
                                {
                                    "name": "param0",
                                    "type": "Type",
                                    "default": False,
                                    "out": False,
                                },
                            ),
                            "return_types": ("Type",),
                            "static": False,
                        },
                    },
                    "name": "Name",
                    "namespace": None,
                    "nested": None,
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
                        "Name.A -> (Type)": CEvent(
                            name="A", declaring_type=CType(name="Name"), type=CType(name="Type")
                        ),
                        "Name.B -> (Type)": CEvent(
                            name="B", declaring_type=CType(name="Name"), type=CType(name="Type")
                        ),
                    },
                ),
                {
                    "abstract": False,
                    "constructors": {},
                    "events": {
                        "Name.A -> (Type)": {"name": "A", "declaring_type": "Name", "type": "Type"},
                        "Name.B -> (Type)": {"name": "B", "declaring_type": "Name", "type": "Type"},
                    },
                    "fields": {},
                    "generic_args": (),
                    "interfaces": (),
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "nested": None,
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
                        "Name.A": CClass(name="A", nested=CType(name="Name")),
                        "Name.B": CClass(name="B", nested=CType(name="Name")),
                    },
                ),
                {
                    "abstract": False,
                    "constructors": {},
                    "events": {},
                    "fields": {},
                    "generic_args": (),
                    "interfaces": (),
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "nested": None,
                    "nested_types": {
                        "Name.A": {
                            "abstract": False,
                            "constructors": {},
                            "events": {},
                            "fields": {},
                            "generic_args": (),
                            "interfaces": (),
                            "methods": {},
                            "name": "A",
                            "namespace": None,
                            "nested": "Name",
                            "nested_types": {},
                            "properties": {},
                            "super_class": None,
                            "type": "class",
                        },
                        "Name.B": {
                            "abstract": False,
                            "constructors": {},
                            "events": {},
                            "fields": {},
                            "generic_args": (),
                            "interfaces": (),
                            "methods": {},
                            "name": "B",
                            "namespace": None,
                            "nested": "Name",
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

    doc_objects: ClassVar[ParamSequence[tuple[CClass, DocTree]]] = [
        ("basic", (CClass(name="Name"), DocTree(name="Name"))),
        ("abstract", (CClass(name="Name", abstract=True), DocTree(name="Name"))),
        (
            "generic_args",
            (
                CClass(
                    name="Name",
                    generic_args=(CType(name="A", generic=True), CType(name="B", generic=True)),
                ),
                DocTree(name="Name[$A, $B]"),
            ),
        ),
        (
            "super_class",
            (CClass(name="Name", super_class=CType(name="Name")), DocTree(name="Name")),
        ),
        (
            "interfaces",
            (
                CClass(name="Name", interfaces=(CType(name="A"), CType(name="B"))),
                DocTree(name="Name"),
            ),
        ),
        (
            "fields",
            (
                CClass(
                    name="Name",
                    fields={
                        "Name.A": CField(
                            name="A",
                            declaring_type=CType(name="Name"),
                            return_type=CType(name="Type"),
                        ),
                        "Name.B": CField(
                            name="B",
                            declaring_type=CType(name="Name"),
                            return_type=CType(name="Type"),
                        ),
                    },
                ),
                DocTree(
                    name="Name",
                    children=(DocTree(name="A", return_doc=""), DocTree(name="B", return_doc="")),
                ),
            ),
        ),
        (
            "constructors",
            (
                CClass(
                    name="Name",
                    constructors={
                        "Name.__init__()": CConstructor(declaring_type=CType(name="Name")),
                        "Name.__init__(Namespace:Type)": CConstructor(
                            declaring_type=CType(name="Name"),
                            parameters=(CParameter(name="param0", type=CType(name="Type")),),
                        ),
                    },
                ),
                DocTree(
                    name="Name",
                    children=(
                        DocTree(name="__init__()"),
                        DocTree(name="__init__(Type)", parameter_docs={"param0": ""}),
                    ),
                ),
            ),
        ),
        (
            "properties",
            (
                CClass(
                    name="Name",
                    properties={
                        "Name.A": CProperty(
                            name="A",
                            declaring_type=CType(name="Name"),
                            type=CType(name="Type"),
                            setter=True,
                        ),
                        "Name.B": CProperty(
                            name="B",
                            declaring_type=CType(name="Name"),
                            type=CType(name="Type"),
                            setter=True,
                        ),
                    },
                ),
                DocTree(
                    name="Name",
                    children=(DocTree(name="A", return_doc=""), DocTree(name="B", return_doc="")),
                ),
            ),
        ),
        (
            "methods",
            (
                CClass(
                    name="Name",
                    methods={
                        "Name.A(Type) -> Type": CMethod(
                            name="A",
                            declaring_type=CType(name="Name"),
                            parameters=(CParameter(name="param0", type=CType(name="Type")),),
                            return_types=(CType(name="Type"),),
                        ),
                        "Name.B(Type) -> Type": CMethod(
                            name="B",
                            declaring_type=CType(name="Name"),
                            parameters=(CParameter(name="param0", type=CType(name="Type")),),
                            return_types=(CType(name="Type"),),
                        ),
                    },
                ),
                DocTree(
                    name="Name",
                    children=(
                        DocTree(
                            name="A(Type)",
                            parameter_docs={"param0": ""},
                            return_doc="",
                            exception_docs={},
                        ),
                        DocTree(
                            name="B(Type)",
                            parameter_docs={"param0": ""},
                            return_doc="",
                            exception_docs={},
                        ),
                    ),
                ),
            ),
        ),
        (
            "events",
            (
                CClass(
                    name="Name",
                    events={
                        "Name.A -> (Type)": CEvent(
                            name="A", declaring_type=CType(name="Name"), type=CType(name="Type")
                        ),
                        "Name.B -> (Type)": CEvent(
                            name="B", declaring_type=CType(name="Name"), type=CType(name="Type")
                        ),
                    },
                ),
                DocTree(
                    name="Name",
                    children=(DocTree(name="A"), DocTree(name="B")),
                ),
            ),
        ),
        (
            "nested_types",
            (
                CClass(
                    name="Name",
                    nested_types={
                        "Name.A": CClass(name="A", nested=CType(name="Name")),
                        "Name.B": CClass(name="B", nested=CType(name="Name")),
                    },
                ),
                DocTree(
                    name="Name",
                    children=(DocTree(name="A"), DocTree(name="B")),
                ),
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "doc"), **make_params(doc_objects))
    def test_to_doc_tree(self, obj: CClass, doc: DocTree) -> None:
        """Test for CClass.to_doc_json()."""
        expected: DocTree = doc
        actual: DocTree = obj.to_doc_tree()

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


class TestCStruct:
    """Tests for CStruct."""

    unique_name_objects: ClassVar[ParamSequence[tuple[CStruct, str]]] = [
        ("basic", (CStruct(name="Name"), "Name")),
        (
            "generic_args",
            (
                CStruct(
                    name="Name",
                    generic_args=(CType(name="A", generic=True), CType(name="B", generic=True)),
                ),
                "Name[$A, $B]",
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "expected"), **make_params(unique_name_objects))
    def test_unique_name(self, obj: CStruct, expected: str) -> None:
        """Test for CStruct.unique_name."""
        actual: str = obj.unique_name

        assert actual == expected

    json_objects: ClassVar[ParamSequence[tuple[CStruct, JsonType]]] = [
        (
            "basic",
            (
                CStruct(name="Name"),
                {
                    "abstract": False,
                    "constructors": {},
                    "events": {},
                    "fields": {},
                    "generic_args": (),
                    "interfaces": (),
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "nested": None,
                    "nested_types": {},
                    "properties": {},
                    "super_class": None,
                    "type": "struct",
                },
            ),
        ),
        (
            "abstract",
            (
                CStruct(name="Name", abstract=True),
                {
                    "type": "struct",
                    "name": "Name",
                    "namespace": None,
                    "nested": None,
                    "abstract": True,
                    "generic_args": (),
                    "super_class": None,
                    "interfaces": (),
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
                CStruct(
                    name="Name",
                    generic_args=(CType(name="A", generic=True), CType(name="B", generic=True)),
                ),
                {
                    "type": "struct",
                    "name": "Name",
                    "namespace": None,
                    "nested": None,
                    "abstract": False,
                    "generic_args": ("$A", "$B"),
                    "super_class": None,
                    "interfaces": (),
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
                CStruct(name="Name", super_class=CType(name="Name")),
                {
                    "abstract": False,
                    "constructors": {},
                    "events": {},
                    "fields": {},
                    "generic_args": (),
                    "interfaces": (),
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "nested": None,
                    "nested_types": {},
                    "properties": {},
                    "super_class": "Name",
                    "type": "struct",
                },
            ),
        ),
        (
            "interfaces",
            (
                CStruct(name="Name", interfaces=(CType(name="A"), CType(name="B"))),
                {
                    "abstract": False,
                    "constructors": {},
                    "events": {},
                    "fields": {},
                    "generic_args": (),
                    "interfaces": ("A", "B"),
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "nested": None,
                    "nested_types": {},
                    "properties": {},
                    "super_class": None,
                    "type": "struct",
                },
            ),
        ),
        (
            "fields",
            (
                CStruct(
                    name="Name",
                    fields={
                        "Name.A": CField(
                            name="A",
                            declaring_type=CType(name="Name"),
                            return_type=CType(name="Type"),
                        ),
                        "Name.B": CField(
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
                        "Name.A": {
                            "name": "A",
                            "declaring_type": "Name",
                            "return_type": "Type",
                            "static": False,
                        },
                        "Name.B": {
                            "name": "B",
                            "declaring_type": "Name",
                            "return_type": "Type",
                            "static": False,
                        },
                    },
                    "generic_args": (),
                    "interfaces": (),
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "nested": None,
                    "nested_types": {},
                    "properties": {},
                    "super_class": None,
                    "type": "struct",
                },
            ),
        ),
        (
            "constructors",
            (
                CStruct(
                    name="Name",
                    constructors={
                        "Name.__init__()": CConstructor(declaring_type=CType(name="Name")),
                        "Name.__init__(Namespace:Type)": CConstructor(
                            declaring_type=CType(name="Name"),
                            parameters=(CParameter(name="param0", type=CType(name="Type")),),
                        ),
                    },
                ),
                {
                    "abstract": False,
                    "constructors": {
                        "Name.__init__()": {"declaring_type": "Name", "parameters": ()},
                        "Name.__init__(Namespace:Type)": {
                            "declaring_type": "Name",
                            "parameters": (
                                {"name": "param0", "type": "Type", "default": False, "out": False},
                            ),
                        },
                    },
                    "events": {},
                    "fields": {},
                    "generic_args": (),
                    "interfaces": (),
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "nested": None,
                    "nested_types": {},
                    "properties": {},
                    "super_class": None,
                    "type": "struct",
                },
            ),
        ),
        (
            "properties",
            (
                CStruct(
                    name="Name",
                    properties={
                        "Name.A": CProperty(
                            name="A",
                            declaring_type=CType(name="Name"),
                            type=CType(name="Type"),
                            setter=True,
                        ),
                        "Name.B": CProperty(
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
                    "generic_args": (),
                    "interfaces": (),
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "nested": None,
                    "nested_types": {},
                    "properties": {
                        "Name.B": {
                            "name": "B",
                            "declaring_type": "Name",
                            "type": "Type",
                            "setter": True,
                            "static": False,
                        },
                        "Name.A": {
                            "name": "A",
                            "declaring_type": "Name",
                            "type": "Type",
                            "setter": True,
                            "static": False,
                        },
                    },
                    "super_class": None,
                    "type": "struct",
                },
            ),
        ),
        (
            "methods",
            (
                CStruct(
                    name="Name",
                    methods={
                        "Name.A(Type) -> Type": CMethod(
                            name="A",
                            declaring_type=CType(name="Name"),
                            parameters=(CParameter(name="param0", type=CType(name="Type")),),
                            return_types=(CType(name="Type"),),
                        ),
                        "Name.B(Type) -> Type": CMethod(
                            name="B",
                            declaring_type=CType(name="Name"),
                            parameters=(CParameter(name="param0", type=CType(name="Type")),),
                            return_types=(CType(name="Type"),),
                        ),
                    },
                ),
                {
                    "abstract": False,
                    "constructors": {},
                    "events": {},
                    "fields": {},
                    "generic_args": (),
                    "interfaces": (),
                    "methods": {
                        "Name.A(Type) -> Type": {
                            "name": "A",
                            "declaring_type": "Name",
                            "parameters": (
                                {
                                    "name": "param0",
                                    "type": "Type",
                                    "default": False,
                                    "out": False,
                                },
                            ),
                            "return_types": ("Type",),
                            "static": False,
                        },
                        "Name.B(Type) -> Type": {
                            "name": "B",
                            "declaring_type": "Name",
                            "parameters": (
                                {
                                    "name": "param0",
                                    "type": "Type",
                                    "default": False,
                                    "out": False,
                                },
                            ),
                            "return_types": ("Type",),
                            "static": False,
                        },
                    },
                    "name": "Name",
                    "namespace": None,
                    "nested": None,
                    "nested_types": {},
                    "properties": {},
                    "super_class": None,
                    "type": "struct",
                },
            ),
        ),
        (
            "events",
            (
                CStruct(
                    name="Name",
                    events={
                        "Name.A -> (Type)": CEvent(
                            name="A", declaring_type=CType(name="Name"), type=CType(name="Type")
                        ),
                        "Name.B -> (Type)": CEvent(
                            name="B", declaring_type=CType(name="Name"), type=CType(name="Type")
                        ),
                    },
                ),
                {
                    "abstract": False,
                    "constructors": {},
                    "events": {
                        "Name.A -> (Type)": {"name": "A", "declaring_type": "Name", "type": "Type"},
                        "Name.B -> (Type)": {"name": "B", "declaring_type": "Name", "type": "Type"},
                    },
                    "fields": {},
                    "generic_args": (),
                    "interfaces": (),
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "nested": None,
                    "nested_types": {},
                    "properties": {},
                    "super_class": None,
                    "type": "struct",
                },
            ),
        ),
        (
            "nested_types",
            (
                CStruct(
                    name="Name",
                    nested_types={
                        "Name.A": CStruct(name="A", nested=CType(name="Name")),
                        "Name.B": CStruct(name="B", nested=CType(name="Name")),
                    },
                ),
                {
                    "abstract": False,
                    "constructors": {},
                    "events": {},
                    "fields": {},
                    "generic_args": (),
                    "interfaces": (),
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "nested": None,
                    "nested_types": {
                        "Name.A": {
                            "abstract": False,
                            "constructors": {},
                            "events": {},
                            "fields": {},
                            "generic_args": (),
                            "interfaces": (),
                            "methods": {},
                            "name": "A",
                            "namespace": None,
                            "nested": "Name",
                            "nested_types": {},
                            "properties": {},
                            "super_class": None,
                            "type": "struct",
                        },
                        "Name.B": {
                            "abstract": False,
                            "constructors": {},
                            "events": {},
                            "fields": {},
                            "generic_args": (),
                            "interfaces": (),
                            "methods": {},
                            "name": "B",
                            "namespace": None,
                            "nested": "Name",
                            "nested_types": {},
                            "properties": {},
                            "super_class": None,
                            "type": "struct",
                        },
                    },
                    "properties": {},
                    "super_class": None,
                    "type": "struct",
                },
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "json"), **make_params(json_objects))
    def test_to_json(self, obj: CStruct, json: JsonType) -> None:
        """Test for CStruct.to_json()."""
        expected: JsonType = json
        actual: JsonType = obj.to_json()

        assert actual == expected

    @pytest.mark.parametrize(("obj", "json"), **make_params(json_objects))
    def test_from_json(self, obj: CStruct, json: JsonType) -> None:
        """Test for CStruct.from_json()."""
        expected: CStruct = obj
        actual: CStruct = CStruct.from_json(json)

        assert actual == expected

    doc_objects: ClassVar[ParamSequence[tuple[CStruct, DocTree]]] = [
        ("basic", (CStruct(name="Name"), DocTree(name="Name"))),
        ("abstract", (CStruct(name="Name", abstract=True), DocTree(name="Name"))),
        (
            "generic_args",
            (
                CStruct(
                    name="Name",
                    generic_args=(CType(name="A", generic=True), CType(name="B", generic=True)),
                ),
                DocTree(name="Name[$A, $B]"),
            ),
        ),
        (
            "super_class",
            (CStruct(name="Name", super_class=CType(name="Name")), DocTree(name="Name")),
        ),
        (
            "interfaces",
            (
                CStruct(name="Name", interfaces=(CType(name="A"), CType(name="B"))),
                DocTree(name="Name"),
            ),
        ),
        (
            "fields",
            (
                CStruct(
                    name="Name",
                    fields={
                        "Name.A": CField(
                            name="A",
                            declaring_type=CType(name="Name"),
                            return_type=CType(name="Type"),
                        ),
                        "Name.B": CField(
                            name="B",
                            declaring_type=CType(name="Name"),
                            return_type=CType(name="Type"),
                        ),
                    },
                ),
                DocTree(
                    name="Name",
                    children=(DocTree(name="A", return_doc=""), DocTree(name="B", return_doc="")),
                ),
            ),
        ),
        (
            "constructors",
            (
                CStruct(
                    name="Name",
                    constructors={
                        "Name.__init__()": CConstructor(declaring_type=CType(name="Name")),
                        "Name.__init__(Namespace:Type)": CConstructor(
                            declaring_type=CType(name="Name"),
                            parameters=(CParameter(name="param0", type=CType(name="Type")),),
                        ),
                    },
                ),
                DocTree(
                    name="Name",
                    children=(
                        DocTree(name="__init__()"),
                        DocTree(name="__init__(Type)", parameter_docs={"param0": ""}),
                    ),
                ),
            ),
        ),
        (
            "properties",
            (
                CStruct(
                    name="Name",
                    properties={
                        "Name.A": CProperty(
                            name="A",
                            declaring_type=CType(name="Name"),
                            type=CType(name="Type"),
                            setter=True,
                        ),
                        "Name.B": CProperty(
                            name="B",
                            declaring_type=CType(name="Name"),
                            type=CType(name="Type"),
                            setter=True,
                        ),
                    },
                ),
                DocTree(
                    name="Name",
                    children=(DocTree(name="A", return_doc=""), DocTree(name="B", return_doc="")),
                ),
            ),
        ),
        (
            "methods",
            (
                CStruct(
                    name="Name",
                    methods={
                        "Name.A(Type) -> Type": CMethod(
                            name="A",
                            declaring_type=CType(name="Name"),
                            parameters=(CParameter(name="param0", type=CType(name="Type")),),
                            return_types=(CType(name="Type"),),
                        ),
                        "Name.B(Type) -> Type": CMethod(
                            name="B",
                            declaring_type=CType(name="Name"),
                            parameters=(CParameter(name="param0", type=CType(name="Type")),),
                            return_types=(CType(name="Type"),),
                        ),
                    },
                ),
                DocTree(
                    name="Name",
                    children=(
                        DocTree(
                            name="A(Type)",
                            parameter_docs={"param0": ""},
                            return_doc="",
                            exception_docs={},
                        ),
                        DocTree(
                            name="B(Type)",
                            parameter_docs={"param0": ""},
                            return_doc="",
                            exception_docs={},
                        ),
                    ),
                ),
            ),
        ),
        (
            "events",
            (
                CStruct(
                    name="Name",
                    events={
                        "Name.A -> (Type)": CEvent(
                            name="A", declaring_type=CType(name="Name"), type=CType(name="Type")
                        ),
                        "Name.B -> (Type)": CEvent(
                            name="B", declaring_type=CType(name="Name"), type=CType(name="Type")
                        ),
                    },
                ),
                DocTree(
                    name="Name",
                    children=(DocTree(name="A"), DocTree(name="B")),
                ),
            ),
        ),
        (
            "nested_types",
            (
                CStruct(
                    name="Name",
                    nested_types={
                        "Name.A": CStruct(name="A", nested=CType(name="Name")),
                        "Name.B": CStruct(name="B", nested=CType(name="Name")),
                    },
                ),
                DocTree(
                    name="Name",
                    children=(DocTree(name="A"), DocTree(name="B")),
                ),
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "doc"), **make_params(doc_objects))
    def test_to_doc_tree(self, obj: CStruct, doc: DocTree) -> None:
        """Test for CStruct.to_doc_json()."""
        expected: DocTree = doc
        actual: DocTree = obj.to_doc_tree()

        assert actual == expected

    compare_list: ClassVar[ParamSequence[tuple[CStruct, CStruct]]] = [
        ("name", (CStruct(name="A"), CStruct(name="B"))),
    ]

    @pytest.mark.parametrize(("x", "y"), **make_params(compare_list))
    def test_compare(self, x: CStruct, y: CStruct) -> None:
        """Test for CStruct.compare()."""
        _compare(CStruct, x, y)

    @pytest.mark.parametrize(("x", "y"), **make_params(compare_list))
    def test_compare_seq(self, x: CStruct, y: CStruct) -> None:
        """Test for CStruct.compare_seq()."""
        _compare_seq(CStruct, x, y)


class TestCInterface:
    """Tests for CInterface."""

    unique_name_objects: ClassVar[ParamSequence[tuple[CInterface, str]]] = [
        ("basic", (CInterface(name="Name"), "Name")),
        (
            "generic_args",
            (
                CInterface(
                    name="Name",
                    generic_args=(CType(name="A", generic=True), CType(name="B", generic=True)),
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
                    "generic_args": (),
                    "interfaces": (),
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "nested": None,
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
                    generic_args=(CType(name="A", generic=True), CType(name="B", generic=True)),
                ),
                {
                    "type": "interface",
                    "name": "Name",
                    "namespace": None,
                    "nested": None,
                    "generic_args": ("$A", "$B"),
                    "interfaces": (),
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
                CInterface(name="Name", interfaces=(CType(name="A"), CType(name="B"))),
                {
                    "events": {},
                    "fields": {},
                    "generic_args": (),
                    "interfaces": ("A", "B"),
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "nested": None,
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
                        "Name.A": CField(
                            name="A",
                            declaring_type=CType(name="Name"),
                            return_type=CType(name="Type"),
                        ),
                        "Name.B": CField(
                            name="B",
                            declaring_type=CType(name="Name"),
                            return_type=CType(name="Type"),
                        ),
                    },
                ),
                {
                    "events": {},
                    "fields": {
                        "Name.A": {
                            "name": "A",
                            "declaring_type": "Name",
                            "return_type": "Type",
                            "static": False,
                        },
                        "Name.B": {
                            "name": "B",
                            "declaring_type": "Name",
                            "return_type": "Type",
                            "static": False,
                        },
                    },
                    "generic_args": (),
                    "interfaces": (),
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "nested": None,
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
                        "Name.A": CProperty(
                            name="A",
                            declaring_type=CType(name="Name"),
                            type=CType(name="Type"),
                            setter=True,
                        ),
                        "Name.B": CProperty(
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
                    "generic_args": (),
                    "interfaces": (),
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "nested": None,
                    "nested_types": {},
                    "properties": {
                        "Name.B": {
                            "name": "B",
                            "declaring_type": "Name",
                            "type": "Type",
                            "setter": True,
                            "static": False,
                        },
                        "Name.A": {
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
                        "Name.A(Type) -> Type": CMethod(
                            name="A",
                            declaring_type=CType(name="Name"),
                            parameters=(CParameter(name="param0", type=CType(name="Type")),),
                            return_types=(CType(name="Type"),),
                        ),
                        "Name.B(Type) -> Type": CMethod(
                            name="B",
                            declaring_type=CType(name="Name"),
                            parameters=(CParameter(name="param0", type=CType(name="Type")),),
                            return_types=(CType(name="Type"),),
                        ),
                    },
                ),
                {
                    "events": {},
                    "fields": {},
                    "generic_args": (),
                    "interfaces": (),
                    "methods": {
                        "Name.A(Type) -> Type": {
                            "name": "A",
                            "declaring_type": "Name",
                            "parameters": (
                                {
                                    "name": "param0",
                                    "type": "Type",
                                    "default": False,
                                    "out": False,
                                },
                            ),
                            "return_types": ("Type",),
                            "static": False,
                        },
                        "Name.B(Type) -> Type": {
                            "name": "B",
                            "declaring_type": "Name",
                            "parameters": (
                                {
                                    "name": "param0",
                                    "type": "Type",
                                    "default": False,
                                    "out": False,
                                },
                            ),
                            "return_types": ("Type",),
                            "static": False,
                        },
                    },
                    "name": "Name",
                    "namespace": None,
                    "nested": None,
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
                        "Name.A -> (Type)": CEvent(
                            name="A", declaring_type=CType(name="Name"), type=CType(name="Type")
                        ),
                        "Name.B -> (Type)": CEvent(
                            name="B", declaring_type=CType(name="Name"), type=CType(name="Type")
                        ),
                    },
                ),
                {
                    "events": {
                        "Name.A -> (Type)": {"name": "A", "declaring_type": "Name", "type": "Type"},
                        "Name.B -> (Type)": {"name": "B", "declaring_type": "Name", "type": "Type"},
                    },
                    "fields": {},
                    "generic_args": (),
                    "interfaces": (),
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "nested": None,
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
                        "Name.A": CInterface(name="A", nested=CType(name="Name")),
                        "Name.B": CInterface(name="B", nested=CType(name="Name")),
                    },
                ),
                {
                    "events": {},
                    "fields": {},
                    "generic_args": (),
                    "interfaces": (),
                    "methods": {},
                    "name": "Name",
                    "namespace": None,
                    "nested": None,
                    "nested_types": {
                        "Name.A": {
                            "events": {},
                            "fields": {},
                            "generic_args": (),
                            "interfaces": (),
                            "methods": {},
                            "name": "A",
                            "namespace": None,
                            "nested": "Name",
                            "nested_types": {},
                            "properties": {},
                            "type": "interface",
                        },
                        "Name.B": {
                            "events": {},
                            "fields": {},
                            "generic_args": (),
                            "interfaces": (),
                            "methods": {},
                            "name": "B",
                            "namespace": None,
                            "nested": "Name",
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

    doc_objects: ClassVar[ParamSequence[tuple[CInterface, DocTree]]] = [
        ("basic", (CInterface(name="Name"), DocTree(name="Name"))),
        (
            "generic_args",
            (
                CInterface(
                    name="Name",
                    generic_args=(CType(name="A", generic=True), CType(name="B", generic=True)),
                ),
                DocTree(name="Name[$A, $B]"),
            ),
        ),
        (
            "interfaces",
            (
                CInterface(name="Name", interfaces=(CType(name="A"), CType(name="B"))),
                DocTree(name="Name"),
            ),
        ),
        (
            "fields",
            (
                CInterface(
                    name="Name",
                    fields={
                        "Name.A": CField(
                            name="A",
                            declaring_type=CType(name="Name"),
                            return_type=CType(name="Type"),
                        ),
                        "Name.B": CField(
                            name="B",
                            declaring_type=CType(name="Name"),
                            return_type=CType(name="Type"),
                        ),
                    },
                ),
                DocTree(
                    name="Name",
                    children=(DocTree(name="A", return_doc=""), DocTree(name="B", return_doc="")),
                ),
            ),
        ),
        (
            "properties",
            (
                CInterface(
                    name="Name",
                    properties={
                        "Name.A": CProperty(
                            name="A",
                            declaring_type=CType(name="Name"),
                            type=CType(name="Type"),
                            setter=True,
                        ),
                        "Name.B": CProperty(
                            name="B",
                            declaring_type=CType(name="Name"),
                            type=CType(name="Type"),
                            setter=True,
                        ),
                    },
                ),
                DocTree(
                    name="Name",
                    children=(DocTree(name="A", return_doc=""), DocTree(name="B", return_doc="")),
                ),
            ),
        ),
        (
            "methods",
            (
                CInterface(
                    name="Name",
                    methods={
                        "Name.A(Type) -> Type": CMethod(
                            name="A",
                            declaring_type=CType(name="Name"),
                            parameters=(CParameter(name="param0", type=CType(name="Type")),),
                            return_types=(CType(name="Type"),),
                        ),
                        "Name.B(Type) -> Type": CMethod(
                            name="B",
                            declaring_type=CType(name="Name"),
                            parameters=(CParameter(name="param0", type=CType(name="Type")),),
                            return_types=(CType(name="Type"),),
                        ),
                    },
                ),
                DocTree(
                    name="Name",
                    children=(
                        DocTree(
                            name="A(Type)",
                            parameter_docs={"param0": ""},
                            return_doc="",
                            exception_docs={},
                        ),
                        DocTree(
                            name="B(Type)",
                            parameter_docs={"param0": ""},
                            return_doc="",
                            exception_docs={},
                        ),
                    ),
                ),
            ),
        ),
        (
            "events",
            (
                CInterface(
                    name="Name",
                    events={
                        "Name.A -> (Type)": CEvent(
                            name="A", declaring_type=CType(name="Name"), type=CType(name="Type")
                        ),
                        "Name.B -> (Type)": CEvent(
                            name="B", declaring_type=CType(name="Name"), type=CType(name="Type")
                        ),
                    },
                ),
                DocTree(name="Name", children=(DocTree(name="A"), DocTree(name="B"))),
            ),
        ),
        (
            "nested_types",
            (
                CInterface(
                    name="Name",
                    nested_types={
                        "Name.A": CInterface(name="A", nested=CType(name="Name")),
                        "Name.B": CInterface(name="B", nested=CType(name="Name")),
                    },
                ),
                DocTree(name="Name", children=(DocTree(name="A"), DocTree(name="B"))),
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "doc"), **make_params(doc_objects))
    def test_to_doc_tree(self, obj: CInterface, doc: DocTree) -> None:
        """Test for CInterface.to_doc_json()."""
        expected: DocTree = doc
        actual: DocTree = obj.to_doc_tree()

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
                {"type": "enum", "name": "Name", "namespace": None, "nested": None, "fields": ()},
            ),
        ),
        (
            "fields",
            (
                CEnum(name="Name", fields=("Field0", "Field1", "Field2", "Field3")),
                {
                    "type": "enum",
                    "name": "Name",
                    "namespace": None,
                    "nested": None,
                    "fields": ("Field0", "Field1", "Field2", "Field3"),
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

    doc_objects: ClassVar[ParamSequence[tuple[CEnum, DocTree]]] = [
        ("basic", (CEnum(name="Name"), DocTree(name="Name"))),
        (
            "fields",
            (
                CEnum(name="Name", fields=("Field0", "Field1", "Field2", "Field3")),
                DocTree(
                    name="Name",
                    children=(
                        DocTree(name="Field0"),
                        DocTree(name="Field1"),
                        DocTree(name="Field2"),
                        DocTree(name="Field3"),
                    ),
                ),
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "doc"), **make_params(doc_objects))
    def test_to_doc_tree(self, obj: CEnum, doc: DocTree) -> None:
        """Test for CEnum.to_doc_json()."""
        expected: DocTree = doc
        actual: DocTree = obj.to_doc_tree()

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


class TestCDelegate:
    """Tests for CDelegate."""

    unique_name_objects: ClassVar[ParamSequence[tuple[CDelegate, str]]] = [
        ("basic", (CDelegate(name="Name"), "Name()")),
        (
            "parameters",
            (
                CDelegate(
                    name="Name",
                    parameters=(
                        CParameter(name="param0", type=CType(name="A")),
                        CParameter(name="param1", type=CType(name="B")),
                    ),
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
                    "nested": None,
                    "parameters": (),
                    "return_type": "System:Void",
                },
            ),
        ),
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
                {
                    "type": "delegate",
                    "name": "Name",
                    "namespace": None,
                    "nested": None,
                    "parameters": (
                        {"name": "param0", "type": "Type", "default": False, "out": False},
                        {"name": "param1", "type": "Type", "default": False, "out": False},
                    ),
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
                    "nested": None,
                    "parameters": (),
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

    doc_objects: ClassVar[ParamSequence[tuple[CDelegate, DocTree]]] = [
        ("basic", (CDelegate(name="Name"), DocTree(name="Name()"))),
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
                DocTree(name="Name(Type, Type)", parameter_docs={"param0": "", "param1": ""}),
            ),
        ),
        (
            "return_type",
            (
                CDelegate(name="Name", return_type=CType(name="Type")),
                DocTree(name="Name()", doc="", return_doc=""),
            ),
        ),
    ]

    @pytest.mark.parametrize(("obj", "doc"), **make_params(doc_objects))
    def test_to_doc_tree(self, obj: CDelegate, doc: DocTree) -> None:
        """Test for CDelegate.to_doc_json()."""
        expected: DocTree = doc
        actual: DocTree = obj.to_doc_tree()

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


if __name__ == "__main__":
    pytest.main()
