"""Tests for stubgen.model."""

from __future__ import annotations

from typing import TYPE_CHECKING
from typing import ClassVar

import pytest

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

if TYPE_CHECKING:  # pragma: no cover
    from collections.abc import Mapping
    from collections.abc import Sequence

    from stubgen.model import CWrapper
    from stubgen.model import JsonType


def _make_json_params[T: CWrapper](params: Sequence[tuple[str, T, JsonType]]) -> Mapping[str, ...]:
    return {
        "argnames": ("obj", "json"),
        "argvalues": [(obj, json) for _, obj, json in params],
        "ids": [name for name, _, _ in params],
    }


def _make_doc_params[T: CWrapper](params: Sequence[tuple[str, T, JsonType]]) -> Mapping[str, ...]:
    return {
        "argnames": ("obj", "doc"),
        "argvalues": [(obj, doc) for _, obj, doc in params],
        "ids": [name for name, _, _ in params],
    }


def _make_compare_parameters[T: CWrapper](params: Sequence[tuple[str, T, T]]) -> Mapping[str, ...]:
    return {
        "argnames": ("x", "y"),
        "argvalues": [(x, y) for _, x, y in params],
        "ids": [name for name, _, _ in params],
    }


class TestCType:
    """Tests for CType."""

    json_objects: ClassVar[Sequence[tuple[str, CType, JsonType]]] = [
        ("basic", CType(name="Name"), "Name"),
        ("namespace", CType(name="Name", namespace="Namespace"), "Namespace:Name"),
        ("nested", CType(name="Nested.Name"), "Nested.Name"),
        ("reference", CType(name="Name", reference=True), "*Name"),
        ("generic", CType(name="Name", generic=True), "$Name"),
        ("nullable", CType(name="Name", nullable=True), "Name?"),
        ("reference_generic", CType(name="Name", reference=True, generic=True), "$*Name"),
        ("reference_nullable", CType(name="Name", reference=True, nullable=True), "*Name?"),
        ("generic_nullable", CType(name="Name", generic=True, nullable=True), "$Name?"),
        (
            "reference_generic_nullable",
            CType(name="Name", reference=True, generic=True, nullable=True),
            "$*Name?",
        ),
        ("inner", CType(name="Name", inner=(CType(name="A"), CType(name="B"))), "Name[A, B]"),
    ]

    @pytest.mark.parametrize(**_make_json_params(json_objects))
    def test_to_json(self, obj: CType, json: JsonType) -> None:
        """Test for CType.to_json()."""
        expected: JsonType = json
        actual: JsonType = obj.to_json()

        assert actual == expected

    @pytest.mark.parametrize(**_make_json_params(json_objects))
    def test_from_json(self, obj: CType, json: JsonType) -> None:
        """Test for CType.from_json()."""
        expected: CType = obj
        actual: CType = CType.from_json(json)

        assert actual == expected

    def test_to_doc_json(self) -> None:
        """Test for CType.to_doc_json()."""
        with pytest.raises(NotImplementedError):
            CType(name="Name").to_doc_json()

    compare_list: ClassVar[Sequence[tuple[str, CType, CType]]] = [
        ("namespace", CType(name="Name", namespace="A"), CType(name="Name", namespace="B")),
        ("namespace_none", CType(name="Name", namespace=None), CType(name="Name", namespace="A")),
        ("name", CType(name="NameA"), CType(name="NameB")),
        (
            "inner",
            CType(name="Name", inner=(CType(name="A"),)),
            CType(name="Name", inner=(CType(name="B"),)),
        ),
        ("reference", CType(name="Name", reference=False), CType(name="Name", reference=True)),
        ("generic", CType(name="Name", generic=False), CType(name="Name", generic=True)),
        ("nullable", CType(name="Name", nullable=False), CType(name="Name", nullable=True)),
    ]

    @pytest.mark.parametrize(**_make_compare_parameters(compare_list))
    def test_compare(self, x: CType, y: CType) -> None:
        """Test for CType.compare()."""
        assert CType.compare(x, y) == -1
        assert CType.compare(y, x) == 1

    @pytest.mark.parametrize(**_make_compare_parameters(compare_list))
    def test_compare_seq(self, x: CType, y: CType) -> None:
        """Test for CType.compare_seq()."""
        assert CType.compare_seq([], [y]) == -1
        assert CType.compare_seq([x], []) == 1
        assert CType.compare_seq([x], [y]) == -1


class TestCParameter:
    """Tests for CParameter."""

    json_objects: ClassVar[Sequence[tuple[str, CParameter, JsonType]]] = [
        (
            "basic",
            CParameter(name="Name", type=CType(name="Type")),
            {"name": "Name", "type": "Type", "default": False, "out": False},
        ),
        (
            "default",
            CParameter(name="Name", type=CType(name="Type"), default=True),
            {"name": "Name", "type": "Type", "default": True, "out": False},
        ),
        (
            "out",
            CParameter(name="Name", type=CType(name="Type"), out=True),
            {"name": "Name", "type": "Type", "default": False, "out": True},
        ),
    ]

    @pytest.mark.parametrize(**_make_json_params(json_objects))
    def test_to_json(self, obj: CParameter, json: JsonType) -> None:
        """Test for CParameter.to_json()."""
        expected: JsonType = json
        actual: JsonType = obj.to_json()

        assert actual == expected

    @pytest.mark.parametrize(**_make_json_params(json_objects))
    def test_from_json(self, obj: CParameter, json: JsonType) -> None:
        """Test for CParameter.from_json()."""
        expected: CParameter = obj
        actual: CParameter = CParameter.from_json(json)

        assert actual == expected

    def test_to_doc_json(self) -> None:
        """Test for CParameter.to_doc_json()."""
        with pytest.raises(NotImplementedError):
            CParameter(name="Name", type=CType(name="Type")).to_doc_json()

    compare_list: ClassVar[Sequence[tuple[str, CParameter, CParameter]]] = [
        (
            "name",
            CParameter(name="Name", type=CType(name="A")),
            CParameter(name="Name", type=CType(name="B")),
        ),
    ]

    @pytest.mark.parametrize(**_make_compare_parameters(compare_list))
    def test_compare(self, x: CParameter, y: CParameter) -> None:
        """Test for CParameter.compare()."""
        assert CParameter.compare(x, y) == -1
        assert CParameter.compare(y, x) == 1

    @pytest.mark.parametrize(**_make_compare_parameters(compare_list))
    def test_compare_seq(self, x: CParameter, y: CParameter) -> None:
        """Test for CParameter.compare_seq()."""
        assert CParameter.compare_seq([], [y]) == -1
        assert CParameter.compare_seq([x], []) == 1
        assert CParameter.compare_seq([x], [y]) == -1


class TestCField:
    """Tests for CField."""

    json_objects: ClassVar[Sequence[tuple[str, CField, JsonType]]] = [
        (
            "basic",
            CField(name="Name", declaring_type=CType(name="Type"), return_type=CType(name="Type")),
            {"name": "Name", "declaring_type": "Type", "return_type": "Type", "static": False},
        ),
        (
            "static",
            CField(
                name="Name",
                declaring_type=CType(name="Type"),
                return_type=CType(name="Type"),
                static=True,
            ),
            {"name": "Name", "declaring_type": "Type", "return_type": "Type", "static": True},
        ),
    ]

    @pytest.mark.parametrize(**_make_json_params(json_objects))
    def test_to_json(self, obj: CField, json: JsonType) -> None:
        """Test for CField.to_json()."""
        expected: JsonType = json
        actual: JsonType = obj.to_json()

        assert actual == expected

    @pytest.mark.parametrize(**_make_json_params(json_objects))
    def test_from_json(self, obj: CField, json: JsonType) -> None:
        """Test for CField.from_json()."""
        expected: CField = obj
        actual: CField = CField.from_json(json)

        assert actual == expected

    doc_objects: ClassVar[Sequence[tuple[str, CField, JsonType]]] = [
        (
            "basic",
            CField(name="Name", declaring_type=CType(name="Type"), return_type=CType.VOID),
            {"doc": "", "doc_formatted": {}},
        ),
        (
            "return",
            CField(name="Name", declaring_type=CType(name="Type"), return_type=CType(name="Type")),
            {"doc": "", "doc_formatted": {}, "return": ""},
        ),
    ]

    @pytest.mark.parametrize(**_make_doc_params(doc_objects))
    def test_to_doc_json(self, obj: CField, doc: JsonType) -> None:
        """Test for CField.to_doc_json()."""
        expected_name: str = obj.doc_name
        expected_doc: JsonType = doc

        actual_name: str
        actual_doc: JsonType
        actual_name, actual_doc = obj.to_doc_json()

        assert actual_name == expected_name
        assert actual_doc == expected_doc

    compare_list: ClassVar[Sequence[tuple[str, CField, CField]]] = [
        (
            "name",
            CField(name="A", declaring_type=CType(name="Type"), return_type=CType(name="Type")),
            CField(name="B", declaring_type=CType(name="Type"), return_type=CType(name="Type")),
        ),
    ]

    @pytest.mark.parametrize(**_make_compare_parameters(compare_list))
    def test_compare(self, x: CField, y: CField) -> None:
        """Test for CField.compare()."""
        assert CField.compare(x, y) == -1
        assert CField.compare(y, x) == 1

    @pytest.mark.parametrize(**_make_compare_parameters(compare_list))
    def test_compare_seq(self, x: CField, y: CField) -> None:
        """Test for CField.compare_seq()."""
        assert CField.compare_seq([], [y]) == -1
        assert CField.compare_seq([x], []) == 1
        assert CField.compare_seq([x], [y]) == -1


class TestCConstructor:
    """Tests for CConstructor."""

    json_objects: ClassVar[Sequence[tuple[str, CConstructor, JsonType]]] = [
        (
            "basic",
            CConstructor(declaring_type=CType(name="Type")),
            {"declaring_type": "Type", "parameters": ()},
        ),
        (
            "parameters",
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
    ]

    @pytest.mark.parametrize(**_make_json_params(json_objects))
    def test_to_json(self, obj: CConstructor, json: JsonType) -> None:
        """Test for CConstructor.to_json()."""
        expected: JsonType = json
        actual: JsonType = obj.to_json()

        assert actual == expected

    @pytest.mark.parametrize(**_make_json_params(json_objects))
    def test_from_json(self, obj: CConstructor, json: JsonType) -> None:
        """Test for CConstructor.from_json()."""
        expected: CConstructor = obj
        actual: CConstructor = CConstructor.from_json(json)

        assert actual == expected

    doc_objects: ClassVar[Sequence[tuple[str, CConstructor, JsonType]]] = [
        (
            "basic",
            CConstructor(declaring_type=CType(name="Type")),
            {"doc": "", "doc_formatted": {}},
        ),
        (
            "parameters",
            CConstructor(
                declaring_type=CType(name="Type"),
                parameters=(
                    CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                    CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
                ),
            ),
            {"doc": "", "doc_formatted": {}, "parameters": {"param0": "", "param1": ""}},
        ),
    ]

    @pytest.mark.parametrize(**_make_doc_params(doc_objects))
    def test_to_doc_json(self, obj: CConstructor, doc: JsonType) -> None:
        """Test for CConstructor.to_doc_json()."""
        expected_name: str = obj.doc_name
        expected_doc: JsonType = doc

        actual_name: str
        actual_doc: JsonType
        actual_name, actual_doc = obj.to_doc_json()

        assert actual_name == expected_name
        assert actual_doc == expected_doc

    compare_list: ClassVar[Sequence[tuple[str, CConstructor, CConstructor]]] = [
        (
            "name",
            CConstructor(
                declaring_type=CType(name="Type"),
                parameters=(CParameter(name="Name", type=CType(name="A")),),
            ),
            CConstructor(
                declaring_type=CType(name="Type"),
                parameters=(CParameter(name="Name", type=CType(name="B")),),
            ),
        ),
        (
            "parameter_length",
            CConstructor(declaring_type=CType(name="Type")),
            CConstructor(
                declaring_type=CType(name="Type"),
                parameters=(CParameter(name="Name", type=CType(name="Type")),),
            ),
        ),
    ]

    @pytest.mark.parametrize(**_make_compare_parameters(compare_list))
    def test_compare(self, x: CConstructor, y: CConstructor) -> None:
        """Test for CConstructor.compare()."""
        assert CConstructor.compare(x, y) == -1
        assert CConstructor.compare(y, x) == 1

    @pytest.mark.parametrize(**_make_compare_parameters(compare_list))
    def test_compare_seq(self, x: CConstructor, y: CConstructor) -> None:
        """Test for CConstructor.compare_seq()."""
        assert CConstructor.compare_seq([], [y]) == -1
        assert CConstructor.compare_seq([x], []) == 1
        assert CConstructor.compare_seq([x], [y]) == -1


class TestCProperty:
    """Tests for CProperty."""

    json_objects: ClassVar[Sequence[tuple[str, CProperty, JsonType]]] = [
        (
            "basic",
            CProperty(name="Name", declaring_type=CType(name="Type"), type=CType(name="Type")),
            {
                "name": "Name",
                "declaring_type": "Type",
                "type": "Type",
                "setter": False,
                "static": False,
            },
        ),
        (
            "setter",
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
        (
            "static",
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
    ]

    @pytest.mark.parametrize(**_make_json_params(json_objects))
    def test_to_json(self, obj: CProperty, json: JsonType) -> None:
        """Test for CProperty.to_json()."""
        expected: JsonType = json
        actual: JsonType = obj.to_json()

        assert actual == expected

    @pytest.mark.parametrize(**_make_json_params(json_objects))
    def test_from_json(self, obj: CProperty, json: JsonType) -> None:
        """Test for CProperty.from_json()."""
        expected: CProperty = obj
        actual: CProperty = CProperty.from_json(json)

        assert actual == expected

    doc_objects: ClassVar[Sequence[tuple[str, CProperty, JsonType]]] = [
        (
            "basic",
            CProperty(name="Name", declaring_type=CType(name="Type"), type=CType.VOID),
            {"doc": "", "doc_formatted": {}},
        ),
        (
            "return",
            CProperty(name="Name", declaring_type=CType(name="Type"), type=CType(name="Type")),
            {"doc": "", "doc_formatted": {}, "return": ""},
        ),
    ]

    @pytest.mark.parametrize(**_make_doc_params(doc_objects))
    def test_to_doc_json(self, obj: CProperty, doc: JsonType) -> None:
        """Test for CProperty.to_doc_json()."""
        expected_name: str = obj.doc_name
        expected_doc: JsonType = doc

        actual_name: str
        actual_doc: JsonType
        actual_name, actual_doc = obj.to_doc_json()

        assert actual_name == expected_name
        assert actual_doc == expected_doc

    compare_list: ClassVar[Sequence[tuple[str, CProperty, CProperty]]] = [
        (
            "name",
            CProperty(name="A", declaring_type=CType(name="Type"), type=CType(name="Type")),
            CProperty(name="B", declaring_type=CType(name="Type"), type=CType(name="Type")),
        ),
    ]

    @pytest.mark.parametrize(**_make_compare_parameters(compare_list))
    def test_compare(self, x: CProperty, y: CProperty) -> None:
        """Test for CProperty.compare()."""
        assert CProperty.compare(x, y) == -1
        assert CProperty.compare(y, x) == 1

    @pytest.mark.parametrize(**_make_compare_parameters(compare_list))
    def test_compare_seq(self, x: CProperty, y: CProperty) -> None:
        """Test for CProperty.compare_seq()."""
        assert CProperty.compare_seq([], [y]) == -1
        assert CProperty.compare_seq([x], []) == 1
        assert CProperty.compare_seq([x], [y]) == -1


class TestCMethod:
    """Tests for CMethod."""

    json_objects: ClassVar[Sequence[tuple[str, CMethod, JsonType]]] = [
        (
            "basic",
            CMethod(name="Name", declaring_type=CType(name="Type")),
            {
                "name": "Name",
                "declaring_type": "Type",
                "parameters": (),
                "return_types": (),
                "static": False,
            },
        ),
        (
            "parameters",
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
        (
            "return_types",
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
        (
            "static",
            CMethod(name="Name", declaring_type=CType(name="Type"), static=True),
            {
                "name": "Name",
                "declaring_type": "Type",
                "parameters": (),
                "return_types": (),
                "static": True,
            },
        ),
    ]

    @pytest.mark.parametrize(**_make_json_params(json_objects))
    def test_to_json(self, obj: CMethod, json: JsonType) -> None:
        """Test for CMethod.to_json()."""
        expected: JsonType = json
        actual: JsonType = obj.to_json()

        assert actual == expected

    @pytest.mark.parametrize(**_make_json_params(json_objects))
    def test_from_json(self, obj: CMethod, json: JsonType) -> None:
        """Test for CMethod.from_json()."""
        expected: CMethod = obj
        actual: CMethod = CMethod.from_json(json)

        assert actual == expected

    doc_objects: ClassVar[Sequence[tuple[str, CMethod, JsonType]]] = [
        (
            "basic",
            CMethod(name="Name", declaring_type=CType(name="Type")),
            {"doc": "", "doc_formatted": {}, "exceptions": {}},
        ),
        (
            "parameters",
            CMethod(
                name="Name",
                declaring_type=CType(name="Type"),
                parameters=(
                    CParameter(name="param0", type=CType(name="Type")),
                    CParameter(name="param1", type=CType(name="Type")),
                ),
            ),
            {
                "doc": "",
                "doc_formatted": {},
                "exceptions": {},
                "parameters": {"param0": "", "param1": ""},
            },
        ),
        (
            "return_types",
            CMethod(
                name="Name",
                declaring_type=CType(name="Type"),
                return_types=(CType(name="Type"), CType(name="Type")),
            ),
            {"doc": "", "doc_formatted": {}, "exceptions": {}, "return": ""},
        ),
        (
            "static",
            CMethod(
                name="Name",
                declaring_type=CType(name="Type"),
                static=True,
            ),
            {"doc": "", "doc_formatted": {}, "exceptions": {}},
        ),
    ]

    @pytest.mark.parametrize(**_make_doc_params(doc_objects))
    def test_to_doc_json(self, obj: CMethod, doc: JsonType) -> None:
        """Test for CMethod.to_doc_json()."""
        expected_name: str = obj.doc_name
        expected_doc: JsonType = doc

        actual_name: str
        actual_doc: JsonType
        actual_name, actual_doc = obj.to_doc_json()

        assert actual_name == expected_name
        assert actual_doc == expected_doc

    compare_list: ClassVar[Sequence[tuple[str, CMethod, CMethod]]] = [
        (
            "name",
            CMethod(name="A", declaring_type=CType(name="Type")),
            CMethod(name="B", declaring_type=CType(name="Type")),
        ),
        (
            "parameters",
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
        (
            "parameter_length",
            CMethod(name="Name", declaring_type=CType(name="Type")),
            CMethod(
                name="Name",
                declaring_type=CType(name="Type"),
                parameters=(CParameter(name="Name", type=CType(name="A")),),
            ),
        ),
    ]

    @pytest.mark.parametrize(**_make_compare_parameters(compare_list))
    def test_compare(self, x: CMethod, y: CMethod) -> None:
        """Test for CMethod.compare()."""
        assert CMethod.compare(x, y) == -1
        assert CMethod.compare(y, x) == 1

    @pytest.mark.parametrize(**_make_compare_parameters(compare_list))
    def test_compare_seq(self, x: CMethod, y: CMethod) -> None:
        """Test for CMethod.compare_seq()."""
        assert CMethod.compare_seq([], [y]) == -1
        assert CMethod.compare_seq([x], []) == 1
        assert CMethod.compare_seq([x], [y]) == -1


class TestCEvent:
    """Tests for CEvent."""

    json_objects: ClassVar[Sequence[tuple[str, CEvent, JsonType]]] = [
        (
            "basic",
            CEvent(name="Name", declaring_type=CType(name="Type"), type=CType(name="Type")),
            {"name": "Name", "declaring_type": "Type", "type": "Type"},
        ),
    ]

    @pytest.mark.parametrize(**_make_json_params(json_objects))
    def test_to_json(self, obj: CEvent, json: JsonType) -> None:
        """Test for CEvent.to_json()."""
        expected: JsonType = json
        actual: JsonType = obj.to_json()

        assert actual == expected

    @pytest.mark.parametrize(**_make_json_params(json_objects))
    def test_from_json(self, obj: CEvent, json: JsonType) -> None:
        """Test for CEvent.from_json()."""
        expected: CEvent = obj
        actual: CEvent = CEvent.from_json(json)

        assert actual == expected

    doc_objects: ClassVar[Sequence[tuple[str, CEvent, JsonType]]] = [
        (
            "basic",
            CEvent(name="Name", declaring_type=CType(name="Type"), type=CType(name="Type")),
            {"doc": "", "doc_formatted": {}},
        ),
    ]

    @pytest.mark.parametrize(**_make_doc_params(doc_objects))
    def test_to_doc_json(self, obj: CEvent, doc: JsonType) -> None:
        """Test for CEvent.to_doc_json()."""
        expected_name: str = obj.doc_name
        expected_doc: JsonType = doc

        actual_name: str
        actual_doc: JsonType
        actual_name, actual_doc = obj.to_doc_json()

        assert actual_name == expected_name
        assert actual_doc == expected_doc

    compare_list: ClassVar[Sequence[tuple[str, CEvent, CEvent]]] = [
        (
            "name",
            CEvent(name="A", declaring_type=CType(name="Type"), type=CType(name="Type")),
            CEvent(name="B", declaring_type=CType(name="Type"), type=CType(name="Type")),
        ),
    ]

    @pytest.mark.parametrize(**_make_compare_parameters(compare_list))
    def test_compare(self, x: CEvent, y: CEvent) -> None:
        """Test for CEvent.compare()."""
        assert CEvent.compare(x, y) == -1
        assert CEvent.compare(y, x) == 1

    @pytest.mark.parametrize(**_make_compare_parameters(compare_list))
    def test_compare_seq(self, x: CEvent, y: CEvent) -> None:
        """Test for CEvent.compare_seq()."""
        assert CEvent.compare_seq([], [y]) == -1
        assert CEvent.compare_seq([x], []) == 1
        assert CEvent.compare_seq([x], [y]) == -1


class TestCNamespace:
    """Tests for CNamespace."""

    json_objects: ClassVar[Sequence[tuple[str, CNamespace, JsonType]]] = [
        (
            "basic",
            CNamespace(
                name="Namespace",
                types={
                    "Namespace:IInterface": CInterface(name="IInterface", namespace="Namespace"),
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
    ]

    @pytest.mark.parametrize(**_make_json_params(json_objects))
    def test_to_json(self, obj: CNamespace, json: JsonType) -> None:
        """Test for CNamespace.to_json()."""
        expected: JsonType = json
        actual: JsonType = obj.to_json()

        assert actual == expected

    @pytest.mark.parametrize(**_make_json_params(json_objects))
    def test_from_json(self, obj: CNamespace, json: JsonType) -> None:
        """Test for CNamespace.from_json()."""
        expected: CNamespace = obj
        actual: CNamespace = CNamespace.from_json(json)

        assert actual == expected

    def test_to_doc_json(self) -> None:
        """Test for CNamespace.to_doc_json()."""
        with pytest.raises(NotImplementedError):
            CNamespace(name="Name").to_doc_json()

    compare_list: ClassVar[Sequence[tuple[str, CNamespace, CNamespace]]] = [
        ("name", CNamespace(name="A"), CNamespace(name="B")),
    ]

    @pytest.mark.parametrize(**_make_compare_parameters(compare_list))
    def test_compare(self, x: CNamespace, y: CNamespace) -> None:
        """Test for CNamespace.compare()."""
        assert CNamespace.compare(x, y) == -1
        assert CNamespace.compare(y, x) == 1

    @pytest.mark.parametrize(**_make_compare_parameters(compare_list))
    def test_compare_seq(self, x: CNamespace, y: CNamespace) -> None:
        """Test for CNamespace.compare_seq()."""
        assert CNamespace.compare_seq([], [y]) == -1
        assert CNamespace.compare_seq([x], []) == 1
        assert CNamespace.compare_seq([x], [y]) == -1


class TestCClass:
    """Tests for CClass."""

    json_objects: ClassVar[Sequence[tuple[str, CClass, JsonType]]] = [
        (
            "basic",
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
        (
            "abstract",
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
        (
            "generic_args",
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
        (
            "super_class",
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
        (
            "interfaces",
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
        (
            "fields",
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
        (
            "constructors",
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
        (
            "properties",
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
        (
            "methods",
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
        (
            "events",
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
        (
            "nested_types",
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
    ]

    @pytest.mark.parametrize(**_make_json_params(json_objects))
    def test_to_json(self, obj: CClass, json: JsonType) -> None:
        """Test for CClass.to_json()."""
        expected: JsonType = json
        actual: JsonType = obj.to_json()

        assert actual == expected

    @pytest.mark.parametrize(**_make_json_params(json_objects))
    def test_from_json(self, obj: CClass, json: JsonType) -> None:
        """Test for CClass.from_json()."""
        expected: CClass = obj
        actual: CClass = CClass.from_json(json)

        assert actual == expected

    doc_objects: ClassVar[Sequence[tuple[str, CClass, JsonType]]] = [
        ("basic", CClass(name="Name"), {"doc": "", "doc_formatted": {}}),
        ("abstract", CClass(name="Name", abstract=True), {"doc": "", "doc_formatted": {}}),
        (
            "generic_args",
            CClass(
                name="Name",
                generic_args=(CType(name="A", generic=True), CType(name="B", generic=True)),
            ),
            {"doc": "", "doc_formatted": {}},
        ),
        (
            "super_class",
            CClass(name="Name", super_class=CType(name="Name")),
            {"doc": "", "doc_formatted": {}},
        ),
        (
            "interfaces",
            CClass(name="Name", interfaces=(CType(name="A"), CType(name="B"))),
            {"doc": "", "doc_formatted": {}},
        ),
        (
            "fields",
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
                "doc": "",
                "doc_formatted": {},
                "A": {"doc": "", "doc_formatted": {}, "return": ""},
                "B": {"doc": "", "doc_formatted": {}, "return": ""},
            },
        ),
        (
            "constructors",
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
                "doc": "",
                "doc_formatted": {},
                "__init__()": {"doc": "", "doc_formatted": {}},
                "__init__(Type)": {"doc": "", "doc_formatted": {}, "parameters": {"param0": ""}},
            },
        ),
        (
            "properties",
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
                "doc": "",
                "doc_formatted": {},
                "A": {"doc": "", "doc_formatted": {}, "return": ""},
                "B": {"doc": "", "doc_formatted": {}, "return": ""},
            },
        ),
        (
            "methods",
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
                "doc": "",
                "doc_formatted": {},
                "A(Type)": {
                    "doc": "",
                    "doc_formatted": {},
                    "exceptions": {},
                    "parameters": {"param0": ""},
                    "return": "",
                },
                "B(Type)": {
                    "doc": "",
                    "doc_formatted": {},
                    "exceptions": {},
                    "parameters": {"param0": ""},
                    "return": "",
                },
            },
        ),
        (
            "events",
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
                "doc": "",
                "doc_formatted": {},
                "A": {"doc": "", "doc_formatted": {}},
                "B": {"doc": "", "doc_formatted": {}},
            },
        ),
        (
            "nested_types",
            CClass(
                name="Name",
                nested_types={
                    "Name.A": CClass(name="A", nested=CType(name="Name")),
                    "Name.B": CClass(name="B", nested=CType(name="Name")),
                },
            ),
            {
                "doc": "",
                "doc_formatted": {},
                "A": {"doc": "", "doc_formatted": {}},
                "B": {"doc": "", "doc_formatted": {}},
            },
        ),
    ]

    @pytest.mark.parametrize(**_make_doc_params(doc_objects))
    def test_to_doc_json(self, obj: CClass, doc: JsonType) -> None:
        """Test for CClass.to_doc_json()."""
        expected_name: str = obj.doc_name
        expected_doc: JsonType = doc

        actual_name: str
        actual_doc: JsonType
        actual_name, actual_doc = obj.to_doc_json()

        assert actual_name == expected_name
        assert actual_doc == expected_doc

    compare_list: ClassVar[Sequence[tuple[str, CClass, CClass]]] = [
        ("name", CClass(name="A"), CClass(name="B")),
    ]

    @pytest.mark.parametrize(**_make_compare_parameters(compare_list))
    def test_compare(self, x: CClass, y: CClass) -> None:
        """Test for CClass.compare()."""
        assert CClass.compare(x, y) == -1
        assert CClass.compare(y, x) == 1

    @pytest.mark.parametrize(**_make_compare_parameters(compare_list))
    def test_compare_seq(self, x: CClass, y: CClass) -> None:
        """Test for CClass.compare_seq()."""
        assert CClass.compare_seq([], [y]) == -1
        assert CClass.compare_seq([x], []) == 1
        assert CClass.compare_seq([x], [y]) == -1


class TestCStruct:
    """Tests for CStruct."""

    json_objects: ClassVar[Sequence[tuple[str, CStruct, JsonType]]] = [
        (
            "basic",
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
        (
            "abstract",
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
        (
            "generic_args",
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
        (
            "super_class",
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
        (
            "interfaces",
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
        (
            "fields",
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
        (
            "constructors",
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
        (
            "properties",
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
        (
            "methods",
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
        (
            "events",
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
        (
            "nested_types",
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
    ]

    @pytest.mark.parametrize(**_make_json_params(json_objects))
    def test_to_json(self, obj: CStruct, json: JsonType) -> None:
        """Test for CStruct.to_json()."""
        expected: JsonType = json
        actual: JsonType = obj.to_json()

        assert actual == expected

    @pytest.mark.parametrize(**_make_json_params(json_objects))
    def test_from_json(self, obj: CStruct, json: JsonType) -> None:
        """Test for CStruct.from_json()."""
        expected: CStruct = obj
        actual: CStruct = CStruct.from_json(json)

        assert actual == expected

    doc_objects: ClassVar[Sequence[tuple[str, CStruct, JsonType]]] = [
        ("basic", CStruct(name="Name"), {"doc": "", "doc_formatted": {}}),
        ("abstract", CStruct(name="Name", abstract=True), {"doc": "", "doc_formatted": {}}),
        (
            "generic_args",
            CStruct(
                name="Name",
                generic_args=(CType(name="A", generic=True), CType(name="B", generic=True)),
            ),
            {"doc": "", "doc_formatted": {}},
        ),
        (
            "super_class",
            CStruct(name="Name", super_class=CType(name="Name")),
            {"doc": "", "doc_formatted": {}},
        ),
        (
            "interfaces",
            CStruct(name="Name", interfaces=(CType(name="A"), CType(name="B"))),
            {"doc": "", "doc_formatted": {}},
        ),
        (
            "fields",
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
                "doc": "",
                "doc_formatted": {},
                "A": {"doc": "", "doc_formatted": {}, "return": ""},
                "B": {"doc": "", "doc_formatted": {}, "return": ""},
            },
        ),
        (
            "constructors",
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
                "doc": "",
                "doc_formatted": {},
                "__init__()": {"doc": "", "doc_formatted": {}},
                "__init__(Type)": {"doc": "", "doc_formatted": {}, "parameters": {"param0": ""}},
            },
        ),
        (
            "properties",
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
                "doc": "",
                "doc_formatted": {},
                "A": {"doc": "", "doc_formatted": {}, "return": ""},
                "B": {"doc": "", "doc_formatted": {}, "return": ""},
            },
        ),
        (
            "methods",
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
                "doc": "",
                "doc_formatted": {},
                "A(Type)": {
                    "doc": "",
                    "doc_formatted": {},
                    "exceptions": {},
                    "parameters": {"param0": ""},
                    "return": "",
                },
                "B(Type)": {
                    "doc": "",
                    "doc_formatted": {},
                    "exceptions": {},
                    "parameters": {"param0": ""},
                    "return": "",
                },
            },
        ),
        (
            "events",
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
                "doc": "",
                "doc_formatted": {},
                "A": {"doc": "", "doc_formatted": {}},
                "B": {"doc": "", "doc_formatted": {}},
            },
        ),
        (
            "nested_types",
            CStruct(
                name="Name",
                nested_types={
                    "Name.A": CStruct(name="A", nested=CType(name="Name")),
                    "Name.B": CStruct(name="B", nested=CType(name="Name")),
                },
            ),
            {
                "doc": "",
                "doc_formatted": {},
                "A": {"doc": "", "doc_formatted": {}},
                "B": {"doc": "", "doc_formatted": {}},
            },
        ),
    ]

    @pytest.mark.parametrize(**_make_doc_params(doc_objects))
    def test_to_doc_json(self, obj: CStruct, doc: JsonType) -> None:
        """Test for CStruct.to_doc_json()."""
        expected_name: str = obj.doc_name
        expected_doc: JsonType = doc

        actual_name: str
        actual_doc: JsonType
        actual_name, actual_doc = obj.to_doc_json()

        assert actual_name == expected_name
        assert actual_doc == expected_doc

    compare_list: ClassVar[Sequence[tuple[str, CStruct, CStruct]]] = [
        ("name", CStruct(name="A"), CStruct(name="B")),
    ]

    @pytest.mark.parametrize(**_make_compare_parameters(compare_list))
    def test_compare(self, x: CStruct, y: CStruct) -> None:
        """Test for CStruct.compare()."""
        assert CStruct.compare(x, y) == -1
        assert CStruct.compare(y, x) == 1

    @pytest.mark.parametrize(**_make_compare_parameters(compare_list))
    def test_compare_seq(self, x: CStruct, y: CStruct) -> None:
        """Test for CStruct.compare_seq()."""
        assert CStruct.compare_seq([], [y]) == -1
        assert CStruct.compare_seq([x], []) == 1
        assert CStruct.compare_seq([x], [y]) == -1


class TestCInterface:
    """Tests for CInterface."""

    json_objects: ClassVar[Sequence[tuple[str, CInterface, JsonType]]] = [
        (
            "basic",
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
        (
            "generic_args",
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
        (
            "interfaces",
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
        (
            "fields",
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
        (
            "properties",
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
        (
            "methods",
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
        (
            "events",
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
        (
            "nested_types",
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
    ]

    @pytest.mark.parametrize(**_make_json_params(json_objects))
    def test_to_json(self, obj: CInterface, json: JsonType) -> None:
        """Test for CInterface.to_json()."""
        expected: JsonType = json
        actual: JsonType = obj.to_json()

        assert actual == expected

    @pytest.mark.parametrize(**_make_json_params(json_objects))
    def test_from_json(self, obj: CInterface, json: JsonType) -> None:
        """Test for CInterface.from_json()."""
        expected: CInterface = obj
        actual: CInterface = CInterface.from_json(json)

        assert actual == expected

    doc_objects: ClassVar[Sequence[tuple[str, CInterface, JsonType]]] = [
        ("basic", CInterface(name="Name"), {"doc": "", "doc_formatted": {}}),
        (
            "generic_args",
            CInterface(
                name="Name",
                generic_args=(CType(name="A", generic=True), CType(name="B", generic=True)),
            ),
            {"doc": "", "doc_formatted": {}},
        ),
        (
            "interfaces",
            CInterface(name="Name", interfaces=(CType(name="A"), CType(name="B"))),
            {"doc": "", "doc_formatted": {}},
        ),
        (
            "fields",
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
                "doc": "",
                "doc_formatted": {},
                "A": {"doc": "", "doc_formatted": {}, "return": ""},
                "B": {"doc": "", "doc_formatted": {}, "return": ""},
            },
        ),
        (
            "properties",
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
                "doc": "",
                "doc_formatted": {},
                "A": {"doc": "", "doc_formatted": {}, "return": ""},
                "B": {"doc": "", "doc_formatted": {}, "return": ""},
            },
        ),
        (
            "methods",
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
                "doc": "",
                "doc_formatted": {},
                "A(Type)": {
                    "doc": "",
                    "doc_formatted": {},
                    "exceptions": {},
                    "parameters": {"param0": ""},
                    "return": "",
                },
                "B(Type)": {
                    "doc": "",
                    "doc_formatted": {},
                    "exceptions": {},
                    "parameters": {"param0": ""},
                    "return": "",
                },
            },
        ),
        (
            "events",
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
                "doc": "",
                "doc_formatted": {},
                "A": {"doc": "", "doc_formatted": {}},
                "B": {"doc": "", "doc_formatted": {}},
            },
        ),
        (
            "nested_types",
            CInterface(
                name="Name",
                nested_types={
                    "Name.A": CInterface(name="A", nested=CType(name="Name")),
                    "Name.B": CInterface(name="B", nested=CType(name="Name")),
                },
            ),
            {
                "doc": "",
                "doc_formatted": {},
                "A": {"doc": "", "doc_formatted": {}},
                "B": {"doc": "", "doc_formatted": {}},
            },
        ),
    ]

    @pytest.mark.parametrize(**_make_doc_params(doc_objects))
    def test_to_doc_json(self, obj: CInterface, doc: JsonType) -> None:
        """Test for CInterface.to_doc_json()."""
        expected_name: str = obj.doc_name
        expected_doc: JsonType = doc

        actual_name: str
        actual_doc: JsonType
        actual_name, actual_doc = obj.to_doc_json()

        assert actual_name == expected_name
        assert actual_doc == expected_doc

    compare_list: ClassVar[Sequence[tuple[str, CInterface, CInterface]]] = [
        ("name", CInterface(name="A"), CInterface(name="B")),
    ]

    @pytest.mark.parametrize(**_make_compare_parameters(compare_list))
    def test_compare(self, x: CInterface, y: CInterface) -> None:
        """Test for CInterface.compare()."""
        assert CInterface.compare(x, y) == -1
        assert CInterface.compare(y, x) == 1

    @pytest.mark.parametrize(**_make_compare_parameters(compare_list))
    def test_compare_seq(self, x: CInterface, y: CInterface) -> None:
        """Test for CInterface.compare_seq()."""
        assert CInterface.compare_seq([], [y]) == -1
        assert CInterface.compare_seq([x], []) == 1
        assert CInterface.compare_seq([x], [y]) == -1


class TestCEnum:
    """Tests for CEnum."""

    json_objects: ClassVar[Sequence[tuple[str, CEnum, JsonType]]] = [
        (
            "basic",
            CEnum(name="Name"),
            {"type": "enum", "name": "Name", "namespace": None, "nested": None, "fields": ()},
        ),
        (
            "fields",
            CEnum(name="Name", fields=("Field0", "Field1", "Field2", "Field3")),
            {
                "type": "enum",
                "name": "Name",
                "namespace": None,
                "nested": None,
                "fields": ("Field0", "Field1", "Field2", "Field3"),
            },
        ),
    ]

    @pytest.mark.parametrize(**_make_json_params(json_objects))
    def test_to_json(self, obj: CEnum, json: JsonType) -> None:
        """Test for CEnum.to_json()."""
        expected: JsonType = json
        actual: JsonType = obj.to_json()

        assert actual == expected

    @pytest.mark.parametrize(**_make_json_params(json_objects))
    def test_from_json(self, obj: CEnum, json: JsonType) -> None:
        """Test for CEnum.from_json()."""
        expected: CEnum = obj
        actual: CEnum = CEnum.from_json(json)

        assert actual == expected

    doc_objects: ClassVar[Sequence[tuple[str, CEnum, JsonType]]] = [
        ("basic", CEnum(name="Name"), {"doc": "", "doc_formatted": {}}),
        (
            "fields",
            CEnum(name="Name", fields=("Field0", "Field1", "Field2", "Field3")),
            {
                "doc": "",
                "doc_formatted": {},
                "Field0": {"doc": ""},
                "Field1": {"doc": ""},
                "Field2": {"doc": ""},
                "Field3": {"doc": ""},
            },
        ),
    ]

    @pytest.mark.parametrize(**_make_doc_params(doc_objects))
    def test_to_doc_json(self, obj: CEnum, doc: JsonType) -> None:
        """Test for CEnum.to_doc_json()."""
        expected_name: str = obj.doc_name
        expected_doc: JsonType = doc

        actual_name: str
        actual_doc: JsonType
        actual_name, actual_doc = obj.to_doc_json()

        assert actual_name == expected_name
        assert actual_doc == expected_doc

    compare_list: ClassVar[Sequence[tuple[str, CEnum, CEnum]]] = [
        ("name", CEnum(name="A"), CEnum(name="B")),
    ]

    @pytest.mark.parametrize(**_make_compare_parameters(compare_list))
    def test_compare(self, x: CEnum, y: CEnum) -> None:
        """Test for CEnum.compare()."""
        assert CEnum.compare(x, y) == -1
        assert CEnum.compare(y, x) == 1

    @pytest.mark.parametrize(**_make_compare_parameters(compare_list))
    def test_compare_seq(self, x: CEnum, y: CEnum) -> None:
        """Test for CEnum.compare_seq()."""
        assert CEnum.compare_seq([], [y]) == -1
        assert CEnum.compare_seq([x], []) == 1
        assert CEnum.compare_seq([x], [y]) == -1


class TestCDelegate:
    """Tests for CDelegate."""

    json_objects: ClassVar[Sequence[tuple[str, CDelegate, JsonType]]] = [
        (
            "basic",
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
        (
            "parameters",
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
        (
            "return_type",
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
    ]

    @pytest.mark.parametrize(**_make_json_params(json_objects))
    def test_to_json(self, obj: CDelegate, json: JsonType) -> None:
        """Test for CDelegate.to_json()."""
        expected: JsonType = json
        actual: JsonType = obj.to_json()

        assert actual == expected

    @pytest.mark.parametrize(**_make_json_params(json_objects))
    def test_from_json(self, obj: CDelegate, json: JsonType) -> None:
        """Test for CDelegate.from_json()."""
        expected: CDelegate = obj
        actual: CDelegate = CDelegate.from_json(json)

        assert actual == expected

    doc_objects: ClassVar[Sequence[tuple[str, CDelegate, JsonType]]] = [
        (
            "basic",
            CDelegate(name="Name"),
            {"doc": "", "doc_formatted": {}},
        ),
        (
            "parameters",
            CDelegate(
                name="Name",
                parameters=(
                    CParameter(name="param0", type=CType(name="Type")),
                    CParameter(name="param1", type=CType(name="Type")),
                ),
            ),
            {"doc": "", "doc_formatted": {}, "parameters": {"param0": "", "param1": ""}},
        ),
        (
            "return_type",
            CDelegate(name="Name", return_type=CType(name="Type")),
            {"doc": "", "doc_formatted": {}, "return": ""},
        ),
    ]

    @pytest.mark.parametrize(**_make_doc_params(doc_objects))
    def test_to_doc_json(self, obj: CDelegate, doc: JsonType) -> None:
        """Test for CDelegate.to_doc_json()."""
        expected_name: str = obj.doc_name
        expected_doc: JsonType = doc

        actual_name: str
        actual_doc: JsonType
        actual_name, actual_doc = obj.to_doc_json()

        assert actual_name == expected_name
        assert actual_doc == expected_doc

    compare_list: ClassVar[Sequence[tuple[str, CDelegate, CDelegate]]] = [
        ("name", CDelegate(name="A"), CDelegate(name="B")),
    ]

    @pytest.mark.parametrize(**_make_compare_parameters(compare_list))
    def test_compare(self, x: CDelegate, y: CDelegate) -> None:
        """Test for CDelegate.compare()."""
        assert CDelegate.compare(x, y) == -1
        assert CDelegate.compare(y, x) == 1

    @pytest.mark.parametrize(**_make_compare_parameters(compare_list))
    def test_compare_seq(self, x: CDelegate, y: CDelegate) -> None:
        """Test for CDelegate.compare_seq()."""
        assert CDelegate.compare_seq([], [y]) == -1
        assert CDelegate.compare_seq([x], []) == 1
        assert CDelegate.compare_seq([x], [y]) == -1


if __name__ == "__main__":
    pytest.main()
