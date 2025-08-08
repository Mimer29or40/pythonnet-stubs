"""Tests for stubgen.build_stubs.py."""

from __future__ import annotations

import json
from dataclasses import replace
from typing import TYPE_CHECKING

import pytest
from conftest import TL_SKELETON
from conftest import generic
from conftest import make_params

from stubgen.build_stubs import BuildArguments
from stubgen.build_stubs import Builder
from stubgen.build_stubs import build_stubs
from stubgen.build_stubs import format_stubs
from stubgen.model import CAssembly
from stubgen.model import CClass
from stubgen.model import CConstructor
from stubgen.model import CDelegate
from stubgen.model import CEnum
from stubgen.model import CEvent
from stubgen.model import CField
from stubgen.model import CMethod
from stubgen.model import CNamespace
from stubgen.model import CParameter
from stubgen.model import CProperty
from stubgen.model import CType

if TYPE_CHECKING:  # pragma: no cover
    from collections.abc import Sequence
    from pathlib import Path


LINE_LENGTH: int = 100


@pytest.fixture
def builder() -> Builder:
    """Builder fixture."""
    return Builder(line_length=LINE_LENGTH)


@pytest.fixture
def args() -> BuildArguments:
    """BuildArguments fixture."""
    return BuildArguments(line_length=LINE_LENGTH, format_files=True, skeletons="", docs="")


class TestImportType:
    """Tests for NamespaceBuilder.import_type()."""

    def test_basic(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.import_type() with a basic type."""
        obj: CType = CType(name="Type")

        builder.import_type(obj)

        expected: set[str] = {"Type"}

        assert builder.import_set == expected

    def test_generic(self, builder: Builder) -> None:
        """Test for ImportList.add_type() with a generic type."""
        obj: CType = generic("Type")

        builder.import_type(obj)

        expected: set[str] = set()

        assert builder.import_set == expected

    def test_inner(self, builder: Builder) -> None:
        """Test for ImportList.add_type() with inner types."""
        obj: CType = CType(name="Type", inner=[CType(name="InnerA"), CType(name="InnerB")])

        builder.import_type(obj)

        expected: set[str] = {"Type", "InnerA", "InnerB"}

        assert builder.import_set == expected

    def test_void(self, builder: Builder) -> None:
        """Test for ImportList.add_type() with CType.VOID."""
        obj: CType = CType.VOID

        builder.import_type(obj)

        expected: set[str] = set()

        assert builder.import_set == expected


class TestBuildType:
    """Tests for NamespaceBuilder.build_type()."""

    @pytest.mark.parametrize(
        ("obj", "expected", "imported"),
        **make_params(
            [
                ("basic", (CType(name="Type"), "Type", {"Type"})),
                ("void", (CType.VOID, "None", set())),
            ]
        ),
    )
    def test_basic(self, obj: CType, expected: str, imported: set[str], builder: Builder) -> None:
        """Test for NamespaceBuilder.build_type() with native types."""
        actual: str = builder.build_type(obj, convert=False)

        assert actual == expected
        assert builder.import_set == imported

    @pytest.mark.parametrize(
        ("obj", "expected", "imported"),
        **make_params(
            [
                ("Boolean", (CType(name="Boolean"), "bool", set())),
                ("SByte", (CType(name="SByte"), "int", set())),
                ("Byte", (CType(name="Byte"), "int", set())),
                ("Int16", (CType(name="Int16"), "int", set())),
                ("UInt16", (CType(name="UInt16"), "int", set())),
                ("Int32", (CType(name="Int32"), "int", set())),
                ("UInt32", (CType(name="UInt32"), "int", set())),
                ("Int64", (CType(name="Int64"), "int", set())),
                ("UInt64", (CType(name="UInt64"), "int", set())),
                ("Single", (CType(name="Single"), "float", set())),
                ("Double", (CType(name="Double"), "float", set())),
                ("String", (CType(name="String"), "str", set())),
                ("Object", (CType(name="Object"), "object", set())),
                ("Void", (CType(name="Void"), "None", set())),
                ("basic", (CType(name="Type"), "Type", {"Type"})),
            ]
        ),
    )
    def test_convert(self, obj: CType, expected: str, imported: set[str], builder: Builder) -> None:
        """Test for NamespaceBuilder.build_type() when convert is True."""
        actual: str = builder.build_type(obj, convert=True)

        assert actual == expected
        assert builder.import_set == imported

    @pytest.mark.parametrize(
        ("obj", "expected", "imported"),
        **make_params(
            [
                (
                    "inner",
                    (
                        CType(name="Type", inner=[CType(name="Inner")]),
                        "Type[Inner]",
                        {"Type", "Inner"},
                    ),
                )
            ]
        ),
    )
    def test_inner(self, obj: CType, expected: str, imported: set[str], builder: Builder) -> None:
        """Test for NamespaceBuilder.build_type() when convert is True."""
        actual: str = builder.build_type(obj, convert=False)

        assert actual == expected
        assert builder.import_set == imported

    @pytest.mark.parametrize(
        ("obj", "expected"),
        **make_params([("basic", (CType(name="Type", nullable=True), "Type | None"))]),
    )
    def test_nullable(self, obj: CType, expected: str, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_type() when convert is True."""
        actual: str = builder.build_type(obj, convert=False)

        assert actual == expected


class TestBuildParameter:
    """Tests for NamespaceBuilder.build_parameter()."""

    def test_simple(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_parameter() with a simple parameter."""
        obj: CParameter = CParameter(name="name", type=CType(name="Type"))

        expected: str = "name: Type"
        actual: str = builder.build_parameter(obj)

        assert actual == expected
        assert builder.import_set == {"Type"}

    def test_default(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_parameter() with a parameter with a default value."""
        obj: CParameter = CParameter(name="name", type=CType(name="Type"), default=True)

        expected: str = "name: Type = ..."
        actual: str = builder.build_parameter(obj)

        assert actual == expected
        assert builder.import_set == {"Type"}


class TestBuildField:
    """Tests for NamespaceBuilder.build_field()."""

    def test_basic(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_field() with a basic field."""
        obj: CField = CField(
            name="Name",
            declaring_type=CType(name="Type", namespace="Namespace"),
            return_type=CType(name="Type", namespace="Namespace"),
        )

        expected: Sequence[str] = [
            "Name: Final[Type]",
            '""""""',
        ]
        actual: Sequence[str] = builder.build_field(obj)

        assert actual == expected
        assert builder.import_set == {Builder.FINAL, "Namespace.Type"}

    def test_static(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_field() with a static field."""
        obj: CField = CField(
            name="Name",
            declaring_type=CType(name="Type", namespace="Namespace"),
            return_type=CType(name="Type", namespace="Namespace"),
            static=True,
        )

        expected: Sequence[str] = [
            "Name: ClassVar[Type]",
            '""""""',
        ]
        actual: Sequence[str] = builder.build_field(obj)

        assert actual == expected
        assert builder.import_set == {
            Builder.CLASS_VAR,
            "Namespace.Type",
        }


class TestBuildConstructor:
    """Tests for NamespaceBuilder.build_constructor()."""

    def test_basic(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_constructor() with a basic constructor."""
        obj: CConstructor = CConstructor(declaring_type=CType(name="Type", namespace="Namespace"))

        expected: Sequence[str] = [
            "def __init__(self) -> None:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_constructor(obj, overload=False)

        assert actual == expected
        assert builder.import_set == set()

    def test_parameters(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_constructor() with a constructor with parameters."""
        obj: CConstructor = CConstructor(
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=[
                CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
            ],
        )

        expected: Sequence[str] = [
            "def __init__(self, param0: Type, param1: Type) -> None:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_constructor(obj, overload=False)

        assert actual == expected
        assert builder.import_set == {"Namespace.Type"}

    def test_overload(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_constructor() with an overloaded constructor."""
        obj: CConstructor = CConstructor(declaring_type=CType(name="Type", namespace="Namespace"))

        expected: Sequence[str] = [
            "@overload",
            "def __init__(self) -> None:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_constructor(obj, overload=True)

        assert actual == expected
        assert builder.import_set == {Builder.OVERLOAD}

    def test_generic_class(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_constructor() with a generic class param."""
        obj: CConstructor = CConstructor(
            declaring_type=CType(name="Type", inner=[generic("T")]),
            parameters=[CParameter(name="param", type=generic("T"))],
        )

        expected: Sequence[str] = [
            "def __init__(self, param: T) -> None:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_constructor(obj, overload=False)

        assert actual == expected
        assert builder.import_set == set()


class TestBuildProperty:
    """Tests for NamespaceBuilder.build_property()."""

    def test_basic(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_property() with a basic property."""
        obj: CProperty = CProperty(
            name="Name",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="Type", namespace="Namespace"),
        )

        expected: Sequence[str] = [
            "@property",
            "def Name(self) -> Type:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_property(obj)

        assert actual == expected
        assert builder.import_set == {"Namespace.Type"}

    def test_setter(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_property() with a property with a setter."""
        obj: CProperty = CProperty(
            name="Name",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="Type", namespace="Namespace"),
            setter=True,
        )

        expected: Sequence[str] = [
            "@property",
            "def Name(self) -> Type:",
            '    """"""',
            "@Name.setter",
            "def Name(self, value: Type) -> None: ...",
        ]
        actual: Sequence[str] = builder.build_property(obj)

        assert actual == expected
        assert builder.import_set == {"Namespace.Type"}

    def test_static(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_property() with a static property."""
        obj: CProperty = CProperty(
            name="Name",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="Type", namespace="Namespace"),
            static=True,
        )

        expected: Sequence[str] = [
            "@classmethod",
            "@property",
            "def Name(cls) -> Type:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_property(obj)

        assert actual == expected
        assert builder.import_set == {"Namespace.Type"}

    def test_static_setter(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_property() with a static property with a setter."""
        obj: CProperty = CProperty(
            name="Name",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="Type", namespace="Namespace"),
            setter=True,
            static=True,
        )

        expected: Sequence[str] = [
            "@classmethod",
            "@property",
            "def Name(cls) -> Type:",
            '    """"""',
            "@classmethod",
            "@Name.setter",
            "def Name(cls, value: Type) -> None: ...",
        ]
        actual: Sequence[str] = builder.build_property(obj)

        assert actual == expected
        assert builder.import_set == {"Namespace.Type"}


class TestBuildMethod:
    """Tests for NamespaceBuilder.build_method()."""

    def test_basic(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_method() with a basic method."""
        obj: CMethod = CMethod(
            name="Name",
            declaring_type=CType(name="Type", namespace="Namespace"),
            return_types=[CType.VOID],
        )

        expected: Sequence[str] = [
            "def Name(self) -> None:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_method(obj, overload=False)

        assert actual == expected
        assert builder.import_set == set()

    def test_parameters(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_method() with a method with parameters."""
        obj: CMethod = CMethod(
            name="Name",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=[
                CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
            ],
            return_types=[CType.VOID],
        )

        expected: Sequence[str] = [
            "def Name(self, param0: Type, param1: Type) -> None:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_method(obj, overload=False)

        assert actual == expected
        assert builder.import_set == {"Namespace.Type"}

    def test_return(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_method() with a method with multiple returns."""
        obj: CMethod = CMethod(
            name="Name",
            declaring_type=CType(name="Type", namespace="Namespace"),
            return_types=[
                CType(name="Type", namespace="Namespace"),
                CType(name="Type", namespace="Namespace"),
            ],
        )

        expected: Sequence[str] = [
            "def Name(self) -> tuple[Type, Type]:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_method(obj, overload=False)

        assert actual == expected
        assert builder.import_set == {"Namespace.Type"}

    def test_overload(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_method() with an overloaded method."""
        obj: CMethod = CMethod(
            name="Name",
            declaring_type=CType(name="Type", namespace="Namespace"),
            return_types=[CType.VOID],
        )

        expected: Sequence[str] = [
            "@overload",
            "def Name(self) -> None:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_method(obj, overload=True)

        assert actual == expected
        assert builder.import_set == {Builder.OVERLOAD}

    def test_static(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_method() with a static method."""
        obj: CMethod = CMethod(
            name="Name",
            declaring_type=CType(name="Type", namespace="Namespace"),
            return_types=[CType.VOID],
            static=True,
        )

        expected: Sequence[str] = [
            "@classmethod",
            "def Name(cls) -> None:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_method(obj, overload=False)

        assert actual == expected
        assert builder.import_set == set()

    def test_static_parameters(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_method() with a static method with parameters."""
        obj: CMethod = CMethod(
            name="Name",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=[
                CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
            ],
            return_types=[CType.VOID],
            static=True,
        )

        expected: Sequence[str] = [
            "@classmethod",
            "def Name(cls, param0: Type, param1: Type) -> None:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_method(obj, overload=False)

        assert actual == expected
        assert builder.import_set == {"Namespace.Type"}

    def test_static_returns(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_method() with a static method with multiple returns."""
        obj: CMethod = CMethod(
            name="Name",
            declaring_type=CType(name="Type", namespace="Namespace"),
            return_types=[
                CType(name="Type", namespace="Namespace"),
                CType(name="Type", namespace="Namespace"),
            ],
            static=True,
        )

        expected: Sequence[str] = [
            "@classmethod",
            "def Name(cls) -> tuple[Type, Type]:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_method(obj, overload=False)

        assert actual == expected
        assert builder.import_set == {"Namespace.Type"}

    def test_static_overload(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_method() with an overloaded static method."""
        obj: CMethod = CMethod(
            name="Name",
            declaring_type=CType(name="Type", namespace="Namespace"),
            return_types=[CType.VOID],
            static=True,
        )

        expected: Sequence[str] = [
            "@classmethod",
            "@overload",
            "def Name(cls) -> None:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_method(obj, overload=True)

        assert actual == expected
        assert builder.import_set == {Builder.OVERLOAD}

    def test_generic_class(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_method() with a method with a generic class param."""
        obj: CMethod = CMethod(
            name="Name",
            declaring_type=CType(name="Type", inner=[generic("T")]),
            parameters=[CParameter(name="param", type=generic("T"))],
            return_types=[CType.VOID],
        )

        expected: Sequence[str] = [
            "def Name(self, param: T) -> None:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_method(obj, overload=False)

        assert actual == expected
        assert builder.import_set == set()

    def test_generic_method(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_method() with a method with a generic method param."""
        obj: CMethod = CMethod(
            name="Name",
            declaring_type=CType(name="Type", inner=[generic("T")]),
            parameters=[
                CParameter(name="param0", type=generic("T0")),
                CParameter(name="param1", type=generic("T1")),
            ],
            return_types=[CType.VOID],
        )

        expected: Sequence[str] = [
            "def Name[T0, T1](self, param0: T0, param1: T1) -> None:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_method(obj, overload=False)

        assert actual == expected
        assert builder.import_set == set()

    def test_generic_both(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_method() with a method with a both generic params."""
        obj: CMethod = CMethod(
            name="Name",
            declaring_type=CType(name="Type", inner=[generic("T")]),
            parameters=[
                CParameter(name="param", type=generic("T")),
                CParameter(name="param0", type=generic("T0")),
                CParameter(name="param1", type=generic("T1")),
            ],
            return_types=[CType.VOID],
        )

        expected: Sequence[str] = [
            "def Name[T0, T1](self, param: T, param0: T0, param1: T1) -> None:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_method(obj, overload=False)

        assert actual == expected
        assert builder.import_set == set()


class TestBuildEvent:
    """Tests for NamespaceBuilder.build_event()."""

    def test_basic(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_event() with a basic event."""
        obj: CEvent = CEvent(
            name="Event",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="Type", namespace="Namespace"),
        )

        expected: Sequence[str] = [
            "Event: EventType[Type] = ...",
            '""""""',
        ]
        actual: Sequence[str] = builder.build_event(obj)

        assert actual == expected
        assert builder.import_set == {
            "Namespace.Type",
            Builder.SELF,
            Builder.EVENT_TYPE,
        }


class TestBuildClass:
    """Tests for NamespaceBuilder.build_class()."""

    def test_basic(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_class() with a basic class."""
        obj: CClass = CClass(name="Name", namespace="Namespace")

        expected: Sequence[str] = [
            "class Name:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_class(obj)

        assert actual == expected

    def test_abstract(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_class() with an abstract class."""
        obj: CClass = CClass(name="Name", namespace="Namespace", abstract=True)

        expected: Sequence[str] = [
            "class Name(ABC):",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_class(obj)

        assert actual == expected
        assert builder.import_set == {Builder.ABC}

    def test_generic(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_class() with a class with generic arguments."""
        obj: CClass = CClass(
            name="Name",
            namespace="Namespace",
            generic_args=[generic("A"), generic("B")],
        )

        expected: Sequence[str] = [
            "class Name[A, B]:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_class(obj)

        assert actual == expected

    def test_super(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_class() with a class with a suber class."""
        obj: CClass = CClass(
            name="Name",
            namespace="Namespace",
            super_class=CType(name="Super", namespace="Namespace"),
        )

        expected: Sequence[str] = [
            "class Name(Super):",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_class(obj)

        assert actual == expected
        assert builder.import_set == {"Namespace.Super"}

    def test_interfaces(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_class() with a class with interfaces."""
        obj: CClass = CClass(
            name="Name",
            namespace="Namespace",
            interfaces=[
                CType(name="InterfaceA", namespace="Namespace"),
                CType(name="InterfaceB", namespace="Namespace"),
            ],
        )

        expected: Sequence[str] = [
            "class Name(InterfaceA, InterfaceB):",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_class(obj)

        assert actual == expected
        assert builder.import_set == {"Namespace.InterfaceA", "Namespace.InterfaceB"}

    def test_fields(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_class() with a class with fields."""
        obj: CClass = CClass(
            name="Name",
            namespace="Namespace",
            fields={
                "FieldA": CField(
                    name="FieldA",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    return_type=CType(name="Type", namespace="Namespace"),
                ),
                "FieldB": CField(
                    name="FieldB",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    return_type=CType(name="Type", namespace="Namespace"),
                ),
            },
        )

        expected: Sequence[str] = [
            "class Name:",
            '    """"""',
            "    FieldA: Final[Type]",
            '    """"""',
            "    FieldB: Final[Type]",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_class(obj)

        assert actual == expected
        assert builder.import_set == {Builder.FINAL, "Namespace.Type"}

    def test_constructor(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_class() with a class with a constructor."""
        obj: CClass = CClass(
            name="Name",
            namespace="Namespace",
            constructors={
                "__init__()": CConstructor(
                    declaring_type=CType(name="Name", namespace="Namespace"),
                ),
            },
        )

        expected: Sequence[str] = [
            "class Name:",
            '    """"""',
            "    def __init__(self) -> None:",
            '        """"""',
        ]
        actual: Sequence[str] = builder.build_class(obj)

        assert actual == expected
        assert builder.import_set == set()

    def test_constructors(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_class() with a class with constructors."""
        obj: CClass = CClass(
            name="Name",
            namespace="Namespace",
            constructors={
                "__init__()": CConstructor(
                    declaring_type=CType(name="Name", namespace="Namespace"),
                ),
                "__init__(Namespace:Type)": CConstructor(
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    parameters=[
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                    ],
                ),
            },
        )

        expected: Sequence[str] = [
            "class Name:",
            '    """"""',
            "    @overload",
            "    def __init__(self) -> None:",
            '        """"""',
            "    @overload",
            "    def __init__(self, param0: Type) -> None:",
            '        """"""',
        ]
        actual: Sequence[str] = builder.build_class(obj)

        assert actual == expected
        assert builder.import_set == {Builder.OVERLOAD, "Namespace.Type"}

    def test_properties(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_class() with a class with properties."""
        obj: CClass = CClass(
            name="Name",
            namespace="Namespace",
            properties={
                "PropertyA": CProperty(
                    name="PropertyA",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                ),
                "PropertyB": CProperty(
                    name="PropertyB",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                ),
            },
        )

        expected: Sequence[str] = [
            "class Name:",
            '    """"""',
            "    @property",
            "    def PropertyA(self) -> Type:",
            '        """"""',
            "    @property",
            "    def PropertyB(self) -> Type:",
            '        """"""',
        ]
        actual: Sequence[str] = builder.build_class(obj)

        assert actual == expected
        assert builder.import_set == {"Namespace.Type"}

    def test_methods(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_class() with a class with methods."""
        obj: CClass = CClass(
            name="Name",
            namespace="Namespace",
            methods={
                "MethodA(Namespace:Type, Namespace:Type)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    parameters=[
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                        CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
                    ],
                    return_types=[CType(name="Type", namespace="Namespace")],
                ),
                "MethodB(Namespace:Type, Namespace:Type)": CMethod(
                    name="MethodB",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    parameters=[
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                        CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
                    ],
                    return_types=[CType(name="Type", namespace="Namespace")],
                ),
            },
        )

        expected: Sequence[str] = [
            "class Name:",
            '    """"""',
            "    def MethodA(self, param0: Type, param1: Type) -> Type:",
            '        """"""',
            "    def MethodB(self, param0: Type, param1: Type) -> Type:",
            '        """"""',
        ]
        actual: Sequence[str] = builder.build_class(obj)

        assert actual == expected
        assert builder.import_set == {"Namespace.Type"}

    def test_methods_overload(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_class() with a class with overloaded methods."""
        obj: CClass = CClass(
            name="Name",
            namespace="Namespace",
            methods={
                "Method(Namespace:Type)": CMethod(
                    name="Method",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    parameters=[
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                    ],
                    return_types=[CType(name="Type", namespace="Namespace")],
                ),
                "Method(Namespace:Type, Namespace:Type)": CMethod(
                    name="Method",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    parameters=[
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                        CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
                    ],
                    return_types=[CType(name="Type", namespace="Namespace")],
                ),
            },
        )

        expected: Sequence[str] = [
            "class Name:",
            '    """"""',
            "    @overload",
            "    def Method(self, param0: Type) -> Type:",
            '        """"""',
            "    @overload",
            "    def Method(self, param0: Type, param1: Type) -> Type:",
            '        """"""',
        ]
        actual: Sequence[str] = builder.build_class(obj)

        assert actual == expected
        assert builder.import_set == {Builder.OVERLOAD, "Namespace.Type"}

    def test_events(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_class() with a class with events."""
        obj: CClass = CClass(
            name="Name",
            namespace="Namespace",
            events={
                "EventA": CEvent(
                    name="EventA",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                ),
                "EventB": CEvent(
                    name="EventB",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                ),
            },
        )

        expected: Sequence[str] = [
            "class Name:",
            '    """"""',
            "    EventA: EventType[Type] = ...",
            '    """"""',
            "    EventB: EventType[Type] = ...",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_class(obj)

        assert actual == expected
        assert builder.import_set == {
            "Namespace.Type",
            Builder.SELF,
            Builder.EVENT_TYPE,
        }

    def test_nested_types(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_class() with a class with nested types."""
        obj: CClass = CClass(
            name="Name",
            namespace="Namespace",
            nested_types={
                "NestedClass": CClass(
                    name="NestedClass",
                    namespace="Namespace",
                    parent=CType(name="Name", namespace="Namespace"),
                ),
                "INestedInterface": CClass(
                    name="INestedInterface",
                    namespace="Namespace",
                    parent=CType(name="Name", namespace="Namespace"),
                ),
                "NestedEnum": CEnum(
                    name="NestedEnum",
                    namespace="Namespace",
                    parent=CType(name="Name", namespace="Namespace"),
                    fields=[],
                ),
                "NestedDelegate": CDelegate(
                    name="NestedDelegate",
                    namespace="Namespace",
                    parent=CType(name="Name", namespace="Namespace"),
                    return_type=CType(name="Type", namespace="Namespace"),
                ),
            },
        )

        expected: Sequence[str] = [
            "class Name:",
            '    """"""',
            "    class NestedClass:",
            '        """"""',
            "    class INestedInterface:",
            '        """"""',
            "    class NestedEnum(Enum):",
            '        """"""',
            "    type NestedDelegate = Callable[[], Type]",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_class(obj)

        assert actual == expected
        assert builder.import_set == {
            Builder.CALLABLE,
            Builder.ENUM,
            "Namespace.Type",
        }


class TestBuildInterface:
    """Tests for NamespaceBuilder.build_class() with interfaces."""

    def test_basic(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_class() with a basic interface."""
        obj: CClass = CClass(name="Name", namespace="Namespace")

        expected: Sequence[str] = [
            "class Name:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_class(obj)

        assert actual == expected

    def test_generic(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_class() with an interface with generic arguments."""
        obj: CClass = CClass(
            name="Name",
            namespace="Namespace",
            generic_args=[generic("A"), generic("B")],
        )

        expected: Sequence[str] = [
            "class Name[A, B]:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_class(obj)

        assert actual == expected

    def test_interfaces(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_class() with an interface with interfaces."""
        obj: CClass = CClass(
            name="Name",
            namespace="Namespace",
            interfaces=[
                CType(name="InterfaceA", namespace="Namespace"),
                CType(name="InterfaceB", namespace="Namespace"),
            ],
        )

        expected: Sequence[str] = [
            "class Name(InterfaceA, InterfaceB):",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_class(obj)

        assert actual == expected
        assert builder.import_set == {"Namespace.InterfaceA", "Namespace.InterfaceB"}

    def test_fields(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_class() with an interface with fields."""
        obj: CClass = CClass(
            name="Name",
            namespace="Namespace",
            fields={
                "FieldA": CField(
                    name="FieldA",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    return_type=CType(name="Type", namespace="Namespace"),
                ),
                "FieldB": CField(
                    name="FieldB",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    return_type=CType(name="Type", namespace="Namespace"),
                ),
            },
        )

        expected: Sequence[str] = [
            "class Name:",
            '    """"""',
            "    FieldA: Final[Type]",
            '    """"""',
            "    FieldB: Final[Type]",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_class(obj)

        assert actual == expected
        assert builder.import_set == {Builder.FINAL, "Namespace.Type"}

    def test_properties(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_class() with an interface with properties."""
        obj: CClass = CClass(
            name="Name",
            namespace="Namespace",
            properties={
                "PropertyA": CProperty(
                    name="PropertyA",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                ),
                "PropertyB": CProperty(
                    name="PropertyB",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                ),
            },
        )

        expected: Sequence[str] = [
            "class Name:",
            '    """"""',
            "    @property",
            "    def PropertyA(self) -> Type:",
            '        """"""',
            "    @property",
            "    def PropertyB(self) -> Type:",
            '        """"""',
        ]
        actual: Sequence[str] = builder.build_class(obj)

        assert actual == expected
        assert builder.import_set == {"Namespace.Type"}

    def test_methods(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_class() with an interface with methods."""
        obj: CClass = CClass(
            name="Name",
            namespace="Namespace",
            methods={
                "MethodA(Namespace:Type, Namespace:Type)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    parameters=[
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                        CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
                    ],
                    return_types=[CType(name="Type", namespace="Namespace")],
                ),
                "MethodB(Namespace:Type, Namespace:Type)": CMethod(
                    name="MethodB",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    parameters=[
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                        CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
                    ],
                    return_types=[CType(name="Type", namespace="Namespace")],
                ),
            },
        )

        expected: Sequence[str] = [
            "class Name:",
            '    """"""',
            "    def MethodA(self, param0: Type, param1: Type) -> Type:",
            '        """"""',
            "    def MethodB(self, param0: Type, param1: Type) -> Type:",
            '        """"""',
        ]
        actual: Sequence[str] = builder.build_class(obj)

        assert actual == expected
        assert builder.import_set == {"Namespace.Type"}

    def test_methods_overload(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_class() with an interface with overloaded methods."""
        obj: CClass = CClass(
            name="Name",
            namespace="Namespace",
            methods={
                "Namespace:Name.Method(Namespace:Type)": CMethod(
                    name="Method",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    parameters=[
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                    ],
                    return_types=[CType(name="Type", namespace="Namespace")],
                ),
                "Namespace:Name.Method(Namespace:Type, Namespace:Type)": CMethod(
                    name="Method",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    parameters=[
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                        CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
                    ],
                    return_types=[CType(name="Type", namespace="Namespace")],
                ),
            },
        )

        expected: Sequence[str] = [
            "class Name:",
            '    """"""',
            "    @overload",
            "    def Method(self, param0: Type) -> Type:",
            '        """"""',
            "    @overload",
            "    def Method(self, param0: Type, param1: Type) -> Type:",
            '        """"""',
        ]
        actual: Sequence[str] = builder.build_class(obj)

        assert actual == expected
        assert builder.import_set == {Builder.OVERLOAD, "Namespace.Type"}

    def test_events(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_class() with an interface with events."""
        obj: CClass = CClass(
            name="Name",
            namespace="Namespace",
            events={
                "EventA": CEvent(
                    name="EventA",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                ),
                "EventB": CEvent(
                    name="EventB",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                ),
            },
        )

        expected: Sequence[str] = [
            "class Name:",
            '    """"""',
            "    EventA: EventType[Type] = ...",
            '    """"""',
            "    EventB: EventType[Type] = ...",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_class(obj)

        assert actual == expected
        assert builder.import_set == {
            "Namespace.Type",
            Builder.SELF,
            Builder.EVENT_TYPE,
        }

    def test_nested_types(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_class() with an interface with nested types."""
        obj: CClass = CClass(
            name="Name",
            namespace="Namespace",
            nested_types={
                "NestedClass": CClass(
                    name="NestedClass",
                    namespace="Namespace",
                    parent=CType(name="Name", namespace="Namespace"),
                ),
                "NestedStruct": CClass(
                    name="NestedStruct",
                    namespace="Namespace",
                    parent=CType(name="Name", namespace="Namespace"),
                ),
                "INestedInterface": CClass(
                    name="INestedInterface",
                    namespace="Namespace",
                    parent=CType(name="Name", namespace="Namespace"),
                ),
                "NestedEnum": CEnum(
                    name="NestedEnum",
                    namespace="Namespace",
                    parent=CType(name="Name", namespace="Namespace"),
                    fields=[],
                ),
                "NestedDelegate": CDelegate(
                    name="NestedDelegate",
                    namespace="Namespace",
                    parent=CType(name="Name", namespace="Namespace"),
                    return_type=CType(name="Type", namespace="Namespace"),
                ),
            },
        )

        expected: Sequence[str] = [
            "class Name:",
            '    """"""',
            "    class NestedClass:",
            '        """"""',
            "    class NestedStruct:",
            '        """"""',
            "    class INestedInterface:",
            '        """"""',
            "    class NestedEnum(Enum):",
            '        """"""',
            "    type NestedDelegate = Callable[[], Type]",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_class(obj)

        assert actual == expected
        assert builder.import_set == {
            Builder.CALLABLE,
            Builder.ENUM,
            "Namespace.Type",
        }


class TestBuildEnum:
    """Tests for NamespaceBuilder.build_enum()."""

    def test_basic(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_enum() with a basic enum."""
        obj: CEnum = CEnum(name="Name", namespace="Namespace")

        expected: Sequence[str] = [
            "class Name(Enum):",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_enum(obj)

        assert actual == expected
        assert builder.import_set == {Builder.ENUM}

    def test_fields(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_enum() with an enum with multiple fields."""
        obj: CEnum = CEnum(
            name="Enum",
            namespace="Namespace",
            fields=["FieldA", "FieldB", "FieldC", "FieldD"],
        )

        expected: Sequence[str] = [
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
        ]
        actual: Sequence[str] = builder.build_enum(obj)

        assert actual == expected
        assert builder.import_set == {Builder.ENUM}


class TestBuildDelegate:
    """Tests for NamespaceBuilder.build_delegate()."""

    def test_basic(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_delegate() with a basic delegate."""
        obj: CDelegate = CDelegate(name="Name", namespace="Namespace")

        expected: Sequence[str] = [
            "type Name = Callable[[], None]",
            '""""""',
        ]
        actual: Sequence[str] = builder.build_delegate(obj)

        assert actual == expected
        assert builder.import_set == {Builder.CALLABLE}

    def test_parameters(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_delegate() with a delegate with parameters."""
        obj: CDelegate = CDelegate(
            name="Name",
            namespace="Namespace",
            parameters=[
                CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
            ],
        )

        expected: Sequence[str] = [
            "type Name = Callable[[Type, Type], None]",
            '""""""',
        ]
        actual: Sequence[str] = builder.build_delegate(obj)

        assert actual == expected
        assert builder.import_set == {Builder.CALLABLE, "Namespace.Type"}

    def test_return(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_delegate() with a delegate with parameters."""
        obj: CDelegate = CDelegate(
            name="Name",
            namespace="Namespace",
            return_type=CType(name="Type", namespace="Namespace"),
        )

        expected: Sequence[str] = [
            "type Name = Callable[[], Type]",
            '""""""',
        ]
        actual: Sequence[str] = builder.build_delegate(obj)

        assert actual == expected
        assert builder.import_set == {Builder.CALLABLE, "Namespace.Type"}

    def test_generic(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_delegate() with a delegate with generic parameters."""
        obj: CDelegate = CDelegate(
            name="Name",
            namespace="Namespace",
            parameters=[
                CParameter(name="param0", type=generic("T0")),
                CParameter(name="param1", type=generic("T1")),
            ],
            return_type=generic("T"),
        )

        expected: Sequence[str] = [
            "type Name[T0, T1, T] = Callable[[T0, T1], T]",
            '""""""',
        ]
        actual: Sequence[str] = builder.build_delegate(obj)

        assert actual == expected
        assert builder.import_set == {Builder.CALLABLE}


class TestBuildImportSet:
    """Tests for NamespaceBuilder.build_import_set()."""

    def test_basic(self, builder: Builder) -> None:
        """Test for ImportList.build_import_set() with basic types."""
        builder.import_type(CType(name="TypeA", namespace="Namespace"))
        builder.import_type(CType(name="TypeB", namespace="Namespace"))
        builder.import_type(CType(name="TypeC", namespace="Namespace"))
        builder.import_type(CType(name="TypeD", namespace="Namespace"))

        expected: Sequence[str] = [
            "from Namespace import TypeA",
            "from Namespace import TypeB",
            "from Namespace import TypeC",
            "from Namespace import TypeD",
        ]
        actual: Sequence[str] = builder.build_import_set("")

        assert actual == expected

    def test_namespace(self, builder: Builder) -> None:
        """Test for ImportList.build_import_set()."""
        builder.import_type(CType(name="TypeA", namespace="Namespace"))
        builder.import_type(CType(name="TypeB", namespace="Namespace"))
        builder.import_type(CType(name="TypeC", namespace="Namespace.Namespace"))
        builder.import_type(CType(name="TypeD", namespace="Namespace.Namespace"))

        expected: Sequence[str] = [
            "from Namespace.Namespace import TypeC",
            "from Namespace.Namespace import TypeD",
        ]
        actual: Sequence[str] = builder.build_import_set("Namespace")

        assert actual == expected

    def test_event_type(self, builder: Builder) -> None:
        """Test for ImportList.build_import_set()."""
        builder.import_type(CType(name="TypeA", namespace="Namespace"))
        builder.import_type(CType(name="TypeB", namespace="Namespace"))
        builder.import_type(CType(name="TypeC", namespace="Namespace"))
        builder.import_type(CType(name="TypeD", namespace="Namespace"))
        builder.import_set.add(Builder.EVENT_TYPE)

        expected: Sequence[str] = [
            "from Namespace import TypeA",
            "from Namespace import TypeB",
            "from Namespace import TypeC",
            "from Namespace import TypeD",
            "class EventType[T]:",
            "    def __iadd__(self, other: T) -> Self: ...",
            "    def __isub__(self, other: T) -> Self: ...",
        ]
        actual: Sequence[str] = builder.build_import_set("")

        assert actual == expected


class TestBuildNamespace:
    """Tests for NamespaceBuilder.build_namespace()."""

    def test_basic(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_namespace() with a basic namespace."""
        obj: CNamespace = CNamespace(
            name="Name",
            types={},
        )

        expected: Sequence[str] = [
            '"""Automatically generated stubs for C# namespace: Name."""',
            "",
        ]
        actual: Sequence[str] = builder.build(obj)

        assert actual == expected

    def test_types(self, builder: Builder) -> None:
        """Test for NamespaceBuilder.build_namespace() with a basic namespace."""
        obj: CNamespace = CNamespace(
            name="Name",
            types={
                "Name:Class": CClass(name="Class", namespace="Name"),
                "Name:IInterface": CClass(name="IInterface", namespace="Name"),
                "Name:Enum": CEnum(name="Enum", namespace="Name"),
                "Name:Delegate": CDelegate(name="Delegate", namespace="Name"),
            },
        )

        expected: Sequence[str] = [
            '"""Automatically generated stubs for C# namespace: Name."""',
            "",
            "from System import Enum",
            "from collections.abc import Callable",
            "class Class:",
            '    """"""',
            "type Delegate = Callable[[], None]",
            '""""""',
            "class Enum(Enum):",
            '    """"""',
            "class IInterface:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build(obj)

        assert actual == expected


class TestBuildStubs:
    """Tests for build_stubs()."""

    namespaces_list: Sequence[tuple[str, tuple[Sequence[CNamespace], Sequence[str]]]] = [
        ("basic", ([CNamespace(name="NS")], ["NS-stubs"])),
        (
            "nested",
            (
                [CNamespace(name="NS.NS1.NS2")],
                ["NS-stubs", "NS-stubs/NS1", "NS-stubs/NS1/NS2"],
            ),
        ),
        (
            "multiple",
            (
                [CNamespace(name="NS1"), CNamespace(name="NS2"), CNamespace(name="NS3")],
                ["NS1-stubs", "NS2-stubs", "NS3-stubs"],
            ),
        ),
    ]

    @pytest.mark.parametrize(("namespaces", "files"), **make_params(namespaces_list))
    def test_basic(
        self,
        builder: Builder,
        namespaces: Sequence[CNamespace],
        tmp_path: Path,
        files: Sequence[str],
    ) -> None:
        """Test for build_stubs()."""
        build_stubs(builder, namespaces, tmp_path, threads=1)

        for file in files:
            stub_file: Path = tmp_path / file / "__init__.pyi"

            assert stub_file.exists()

    @pytest.mark.parametrize(("namespaces", "files"), **make_params(namespaces_list))
    def test_multi_threaded(
        self,
        builder: Builder,
        namespaces: Sequence[CNamespace],
        tmp_path: Path,
        files: Sequence[str],
    ) -> None:
        """Test for build_stubs()."""
        build_stubs(builder, namespaces, tmp_path, threads=4)

        for file in files:
            stub_file: Path = tmp_path / file / "__init__.pyi"

            assert stub_file.exists()

    def test_test_lib(self, builder: Builder, output_dir: Path) -> None:
        """Test for build_stubs() with TestLib."""
        skeleton_file: Path = output_dir / TL_SKELETON
        skeleton: CAssembly = CAssembly.from_json(json.loads(skeleton_file.read_text()))
        build_stubs(builder, list(skeleton.namespaces.values()), output_dir, threads=1)


class TestFormatStubs:
    """Tests for format_stubs()."""

    def test_basic(self, args: BuildArguments) -> None:
        """Test for format_stubs()."""
        format_stubs(args)

    def test_multi_threaded(self, args: BuildArguments) -> None:
        """Test for format_stubs()."""
        format_stubs(replace(args, threads=4))


class TestCommandBuild:
    """Tests for command_build()."""

    # TODO(Ryan): Monkey patch build_stubs and format_stubs to test command


if __name__ == "__main__":
    pytest.main()
