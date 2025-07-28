"""Tests for stubgen.build_stubs.py."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import pytest
from conftest import make_params

from stubgen.build_stubs import NamespaceBuilder
from stubgen.build_stubs import build_stubs
from stubgen.build_stubs import format_stubs
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
    from collections.abc import Sequence


@pytest.fixture
def builder() -> NamespaceBuilder:
    """NamespaceBuilder fixture."""
    return NamespaceBuilder(line_length=100)


@pytest.fixture
def output_dir() -> Path:
    """Output directory fixture."""
    output_dir: Path = Path("output")
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


class TestImportType:
    """Tests for NamespaceBuilder.import_type()."""

    def test_basic(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.import_type() with a basic type."""
        obj: CType = CType(name="Type")

        builder.import_type(obj)

        expected: set[str] = {"Type"}

        assert builder.import_set == expected

    def test_generic(self, builder: NamespaceBuilder) -> None:
        """Test for ImportList.add_type() with a generic type."""
        obj: CType = CType(name="Type", generic=True)

        builder.import_type(obj)

        expected: set[str] = set()

        assert builder.import_set == expected

    def test_inner(self, builder: NamespaceBuilder) -> None:
        """Test for ImportList.add_type() with inner types."""
        obj: CType = CType(name="Type", inner=[CType(name="InnerA"), CType(name="InnerB")])

        builder.import_type(obj)

        expected: set[str] = {"Type", "InnerA", "InnerB"}

        assert builder.import_set == expected

    def test_void(self, builder: NamespaceBuilder) -> None:
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
    def test_basic(
        self, obj: CType, expected: str, imported: set[str], builder: NamespaceBuilder
    ) -> None:
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
    def test_convert(
        self, obj: CType, expected: str, imported: set[str], builder: NamespaceBuilder
    ) -> None:
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
                        CType(name="Type", inner=(CType(name="Inner"),)),
                        "Type[Inner]",
                        {"Type", "Inner"},
                    ),
                )
            ]
        ),
    )
    def test_inner(
        self, obj: CType, expected: str, imported: set[str], builder: NamespaceBuilder
    ) -> None:
        """Test for NamespaceBuilder.build_type() when convert is True."""
        actual: str = builder.build_type(obj, convert=False)

        assert actual == expected
        assert builder.import_set == imported

    @pytest.mark.parametrize(
        ("obj", "expected"),
        **make_params([("basic", (CType(name="Type", nullable=True), "Type | None"))]),
    )
    def test_nullable(self, obj: CType, expected: str, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_type() when convert is True."""
        actual: str = builder.build_type(obj, convert=False)

        assert actual == expected


class TestBuildParameter:
    """Tests for NamespaceBuilder.build_parameter()."""

    def test_simple(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_parameter() with a simple parameter."""
        obj: CParameter = CParameter(name="name", type=CType(name="Type"))

        expected: str = "name: Type"
        actual: str = builder.build_parameter(obj)

        assert actual == expected
        assert builder.import_set == {"Type"}

    def test_default(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_parameter() with a parameter with a default value."""
        obj: CParameter = CParameter(name="name", type=CType(name="Type"), default=True)

        expected: str = "name: Type = ..."
        actual: str = builder.build_parameter(obj)

        assert actual == expected
        assert builder.import_set == {"Type"}


class TestBuildField:
    """Tests for NamespaceBuilder.build_field()."""

    def test_basic(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_field() with a basic field."""
        obj: CField = CField(
            name="Name",
            declaring_type=CType(name="Type", namespace="Namespace"),
            return_type=CType(name="Type", namespace="Namespace"),
        )

        expected: Sequence[str] = [
            "Name: Final[Type] = ...",
            '""""""',
        ]
        actual: Sequence[str] = builder.build_field(obj)

        assert actual == expected
        assert builder.import_set == {NamespaceBuilder.FINAL, "Namespace.Type"}

    def test_static(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_field() with a static field."""
        obj: CField = CField(
            name="Name",
            declaring_type=CType(name="Type", namespace="Namespace"),
            return_type=CType(name="Type", namespace="Namespace"),
            static=True,
        )

        expected: Sequence[str] = [
            "Name: Final[ClassVar[Type]] = ...",
            '""""""',
        ]
        actual: Sequence[str] = builder.build_field(obj)

        assert actual == expected
        assert builder.import_set == {
            NamespaceBuilder.FINAL,
            NamespaceBuilder.CLASS_VAR,
            "Namespace.Type",
        }


class TestBuildConstructor:
    """Tests for NamespaceBuilder.build_constructor()."""

    def test_basic(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_constructor() with a basic constructor."""
        obj: CConstructor = CConstructor(declaring_type=CType(name="Type", namespace="Namespace"))

        expected: Sequence[str] = [
            "def __init__(self) -> None:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_constructor(obj, overload=False)

        assert actual == expected
        assert builder.import_set == set()

    def test_parameters(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_constructor() with a constructor with parameters."""
        obj: CConstructor = CConstructor(
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
            ),
        )

        expected: Sequence[str] = [
            "def __init__(self, param0: Type, param1: Type) -> None:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_constructor(obj, overload=False)

        assert actual == expected
        assert builder.import_set == {"Namespace.Type"}

    def test_overload(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_constructor() with an overloaded constructor."""
        obj: CConstructor = CConstructor(declaring_type=CType(name="Type", namespace="Namespace"))

        expected: Sequence[str] = [
            "@overload",
            "def __init__(self) -> None:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_constructor(obj, overload=True)

        assert actual == expected
        assert builder.import_set == {NamespaceBuilder.OVERLOAD}


class TestBuildProperty:
    """Tests for NamespaceBuilder.build_property()."""

    def test_basic(self, builder: NamespaceBuilder) -> None:
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

    def test_setter(self, builder: NamespaceBuilder) -> None:
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

    def test_static(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_property() with a static property."""
        obj: CProperty = CProperty(
            name="Name",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="Type", namespace="Namespace"),
            static=True,
        )

        expected: Sequence[str] = [
            "Name: Final[ClassVar[Type]] = ...",
            '""""""',
        ]
        actual: Sequence[str] = builder.build_property(obj)

        assert actual == expected
        assert builder.import_set == {
            NamespaceBuilder.CLASS_VAR,
            "Namespace.Type",
            NamespaceBuilder.FINAL,
        }

    def test_static_setter(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_property() with a static property with a setter."""
        obj: CProperty = CProperty(
            name="Name",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="Type", namespace="Namespace"),
            setter=True,
            static=True,
        )

        expected: Sequence[str] = [
            "Name: ClassVar[Type] = ...",
            '""""""',
        ]
        actual: Sequence[str] = builder.build_property(obj)

        assert actual == expected
        assert builder.import_set == {NamespaceBuilder.CLASS_VAR, "Namespace.Type"}


class TestBuildMethod:
    """Tests for NamespaceBuilder.build_method()."""

    def test_basic(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_method() with a basic method."""
        obj: CMethod = CMethod(
            name="Name",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(CType.VOID,),
        )

        expected: Sequence[str] = [
            "def Name(self) -> None:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_method(obj, overload=False)

        assert actual == expected
        assert builder.import_set == set()

    def test_parameters(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_method() with a method with parameters."""
        obj: CMethod = CMethod(
            name="Name",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
            ),
            return_types=(CType.VOID,),
        )

        expected: Sequence[str] = [
            "def Name(self, param0: Type, param1: Type) -> None:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_method(obj, overload=False)

        assert actual == expected
        assert builder.import_set == {"Namespace.Type"}

    def test_return(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_method() with a method with multiple returns."""
        obj: CMethod = CMethod(
            name="Name",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(
                CType(name="Type", namespace="Namespace"),
                CType(name="Type", namespace="Namespace"),
            ),
        )

        expected: Sequence[str] = [
            "def Name(self) -> tuple[Type, Type]:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_method(obj, overload=False)

        assert actual == expected
        assert builder.import_set == {"Namespace.Type"}

    def test_overload(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_method() with an overloaded method."""
        obj: CMethod = CMethod(
            name="Name",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(CType.VOID,),
        )

        expected: Sequence[str] = [
            "@overload",
            "def Name(self) -> None:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_method(obj, overload=True)

        assert actual == expected
        assert builder.import_set == {NamespaceBuilder.OVERLOAD}

    def test_static(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_method() with a static method."""
        obj: CMethod = CMethod(
            name="Name",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(CType.VOID,),
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

    def test_static_parameters(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_method() with a static method with parameters."""
        obj: CMethod = CMethod(
            name="Name",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
            ),
            return_types=(CType.VOID,),
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

    def test_static_returns(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_method() with a static method with multiple returns."""
        obj: CMethod = CMethod(
            name="Name",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(
                CType(name="Type", namespace="Namespace"),
                CType(name="Type", namespace="Namespace"),
            ),
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

    def test_static_overload(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_method() with an overloaded static method."""
        obj: CMethod = CMethod(
            name="Name",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(CType.VOID,),
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
        assert builder.import_set == {NamespaceBuilder.OVERLOAD}


class TestBuildEvent:
    """Tests for NamespaceBuilder.build_event()."""

    def test_basic(self, builder: NamespaceBuilder) -> None:
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
        assert builder.import_set == {"Namespace.Type", NamespaceBuilder.EVENT_TYPE}


class TestBuildClass:
    """Tests for NamespaceBuilder.build_class()."""

    def test_basic(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_class() with a basic class."""
        obj: CClass = CClass(name="Name", namespace="Namespace")

        expected: Sequence[str] = [
            "class Name:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_class(obj)

        assert actual == expected

    def test_abstract(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_class() with an abstract class."""
        obj: CClass = CClass(name="Name", namespace="Namespace", abstract=True)

        expected: Sequence[str] = [
            "class Name(ABC):",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_class(obj)

        assert actual == expected
        assert builder.import_set == {NamespaceBuilder.ABC}

    def test_generic(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_class() with a class with generic arguments."""
        obj: CClass = CClass(
            name="Name",
            namespace="Namespace",
            generic_args=(CType(name="A", generic=True), CType(name="B", generic=True)),
        )

        expected: Sequence[str] = [
            "class Name[A, B]:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_class(obj)

        assert actual == expected

    def test_super(self, builder: NamespaceBuilder) -> None:
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

    def test_interfaces(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_class() with a class with interfaces."""
        obj: CClass = CClass(
            name="Name",
            namespace="Namespace",
            interfaces=(
                CType(name="InterfaceA", namespace="Namespace"),
                CType(name="InterfaceB", namespace="Namespace"),
            ),
        )

        expected: Sequence[str] = [
            "class Name(InterfaceA, InterfaceB):",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_class(obj)

        assert actual == expected
        assert builder.import_set == {"Namespace.InterfaceA", "Namespace.InterfaceB"}

    def test_fields(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_class() with a class with fields."""
        obj: CClass = CClass(
            name="Name",
            namespace="Namespace",
            fields={
                "Namespace:Class.FieldA": CField(
                    name="FieldA",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    return_type=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace:Class.FieldB": CField(
                    name="FieldB",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    return_type=CType(name="Type", namespace="Namespace"),
                ),
            },
        )

        expected: Sequence[str] = [
            "class Name:",
            '    """"""',
            "    FieldA: Final[Type] = ...",
            '    """"""',
            "    FieldB: Final[Type] = ...",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_class(obj)

        assert actual == expected
        assert builder.import_set == {NamespaceBuilder.FINAL, "Namespace.Type"}

    def test_constructor(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_class() with a class with a constructor."""
        obj: CClass = CClass(
            name="Name",
            namespace="Namespace",
            constructors={
                "Namespace:Name.__init__()": CConstructor(
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    parameters=(),
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

    def test_constructors(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_class() with a class with constructors."""
        obj: CClass = CClass(
            name="Name",
            namespace="Namespace",
            constructors={
                "Namespace:Name.__init__()": CConstructor(
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    parameters=(),
                ),
                "Namespace:Name.__init__(Namespace:Type)": CConstructor(
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                    ),
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
        assert builder.import_set == {NamespaceBuilder.OVERLOAD, "Namespace.Type"}

    def test_properties(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_class() with a class with properties."""
        obj: CClass = CClass(
            name="Name",
            namespace="Namespace",
            properties={
                "Namespace:Name.PropertyA": CProperty(
                    name="PropertyA",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace:Name.PropertyB": CProperty(
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

    def test_methods(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_class() with a class with methods."""
        obj: CClass = CClass(
            name="Name",
            namespace="Namespace",
            methods={
                "Namespace:Name.MethodA(Namespace:Type, Namespace:Type)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                        CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace:Name.MethodB(Namespace:Type, Namespace:Type)": CMethod(
                    name="MethodB",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                        CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
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

    def test_methods_overload(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_class() with a class with overloaded methods."""
        obj: CClass = CClass(
            name="Name",
            namespace="Namespace",
            methods={
                "Namespace:Name.Method(Namespace:Type)": CMethod(
                    name="Method",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace:Name.Method(Namespace:Type, Namespace:Type)": CMethod(
                    name="Method",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                        CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
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
        assert builder.import_set == {NamespaceBuilder.OVERLOAD, "Namespace.Type"}

    def test_events(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_class() with a class with events."""
        obj: CClass = CClass(
            name="Name",
            namespace="Namespace",
            events={
                "Namespace:Name.EventA": CEvent(
                    name="EventA",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace:Name.EventB": CEvent(
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
        assert builder.import_set == {"Namespace.Type", NamespaceBuilder.EVENT_TYPE}

    def test_nested_types(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_class() with a class with nested types."""
        obj: CClass = CClass(
            name="Name",
            namespace="Namespace",
            nested_types={
                "Namespace:Name.NestedClass": CClass(
                    name="NestedClass",
                    namespace="Namespace",
                    nested=CType(name="Name", namespace="Namespace"),
                ),
                "Namespace:Name.NestedStruct": CStruct(
                    name="NestedStruct",
                    namespace="Namespace",
                    nested=CType(name="Name", namespace="Namespace"),
                ),
                "Namespace:Name.INestedInterface": CInterface(
                    name="INestedInterface",
                    namespace="Namespace",
                    nested=CType(name="Name", namespace="Namespace"),
                ),
                "Namespace:Name.NestedEnum": CEnum(
                    name="NestedEnum",
                    namespace="Namespace",
                    nested=CType(name="Name", namespace="Namespace"),
                    fields=(),
                ),
                "Namespace:Name.NestedDelegate": CDelegate(
                    name="NestedDelegate",
                    namespace="Namespace",
                    nested=CType(name="Name", namespace="Namespace"),
                    parameters=(),
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
            "    NestedDelegate: Callable[[], Type] = ...",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_class(obj)

        assert actual == expected
        assert builder.import_set == {
            NamespaceBuilder.CALLABLE,
            NamespaceBuilder.ENUM,
            "Namespace.Type",
        }


class TestBuildStruct:
    """Tests for NamespaceBuilder.build_struct()."""

    def test_basic(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_struct() with a basic struct."""
        obj: CStruct = CStruct(name="Name", namespace="Namespace")

        expected: Sequence[str] = [
            "class Name:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_struct(obj)

        assert actual == expected

    def test_abstract(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_struct() with an abstract struct."""
        obj: CStruct = CStruct(name="Name", namespace="Namespace", abstract=True)

        expected: Sequence[str] = [
            "class Name(ABC):",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_struct(obj)

        assert actual == expected
        assert builder.import_set == {NamespaceBuilder.ABC}

    def test_generic(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_struct() with a struct with generic arguments."""
        obj: CStruct = CStruct(
            name="Name",
            namespace="Namespace",
            generic_args=(CType(name="A", generic=True), CType(name="B", generic=True)),
        )

        expected: Sequence[str] = [
            "class Name[A, B]:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_struct(obj)

        assert actual == expected

    def test_super(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_struct() with a struct with a suber class."""
        obj: CStruct = CStruct(
            name="Name",
            namespace="Namespace",
            super_class=CType(name="Super", namespace="Namespace"),
        )

        expected: Sequence[str] = [
            "class Name(Super):",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_struct(obj)

        assert actual == expected
        assert builder.import_set == {"Namespace.Super"}

    def test_interfaces(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_struct() with a struct with interfaces."""
        obj: CStruct = CStruct(
            name="Name",
            namespace="Namespace",
            interfaces=(
                CType(name="InterfaceA", namespace="Namespace"),
                CType(name="InterfaceB", namespace="Namespace"),
            ),
        )

        expected: Sequence[str] = [
            "class Name(InterfaceA, InterfaceB):",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_struct(obj)

        assert actual == expected
        assert builder.import_set == {"Namespace.InterfaceA", "Namespace.InterfaceB"}

    def test_fields(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_struct() with a struct with fields."""
        obj: CStruct = CStruct(
            name="Name",
            namespace="Namespace",
            fields={
                "Namespace:Class.FieldA": CField(
                    name="FieldA",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    return_type=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace:Class.FieldB": CField(
                    name="FieldB",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    return_type=CType(name="Type", namespace="Namespace"),
                ),
            },
        )

        expected: Sequence[str] = [
            "class Name:",
            '    """"""',
            "    FieldA: Final[Type] = ...",
            '    """"""',
            "    FieldB: Final[Type] = ...",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_struct(obj)

        assert actual == expected
        assert builder.import_set == {NamespaceBuilder.FINAL, "Namespace.Type"}

    def test_constructor(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_struct() with a struct with a constructor."""
        obj: CStruct = CStruct(
            name="Name",
            namespace="Namespace",
            constructors={
                "Namespace:Name.__init__()": CConstructor(
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    parameters=(),
                ),
            },
        )

        expected: Sequence[str] = [
            "class Name:",
            '    """"""',
            "    def __init__(self) -> None:",
            '        """"""',
        ]
        actual: Sequence[str] = builder.build_struct(obj)

        assert actual == expected
        assert builder.import_set == set()

    def test_constructors(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_struct() with a struct with constructors."""
        obj: CStruct = CStruct(
            name="Name",
            namespace="Namespace",
            constructors={
                "Namespace:Name.__init__()": CConstructor(
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    parameters=(),
                ),
                "Namespace:Name.__init__(Namespace:Type)": CConstructor(
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                    ),
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
        actual: Sequence[str] = builder.build_struct(obj)

        assert actual == expected
        assert builder.import_set == {NamespaceBuilder.OVERLOAD, "Namespace.Type"}

    def test_properties(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_struct() with a struct with properties."""
        obj: CStruct = CStruct(
            name="Name",
            namespace="Namespace",
            properties={
                "Namespace:Name.PropertyA": CProperty(
                    name="PropertyA",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace:Name.PropertyB": CProperty(
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
        actual: Sequence[str] = builder.build_struct(obj)

        assert actual == expected
        assert builder.import_set == {"Namespace.Type"}

    def test_methods(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_struct() with a struct with methods."""
        obj: CStruct = CStruct(
            name="Name",
            namespace="Namespace",
            methods={
                "Namespace:Name.MethodA(Namespace:Type, Namespace:Type)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                        CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace:Name.MethodB(Namespace:Type, Namespace:Type)": CMethod(
                    name="MethodB",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                        CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
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
        actual: Sequence[str] = builder.build_struct(obj)

        assert actual == expected
        assert builder.import_set == {"Namespace.Type"}

    def test_methods_overload(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_struct() with a struct with overloaded methods."""
        obj: CStruct = CStruct(
            name="Name",
            namespace="Namespace",
            methods={
                "Namespace:Name.Method(Namespace:Type)": CMethod(
                    name="Method",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace:Name.Method(Namespace:Type, Namespace:Type)": CMethod(
                    name="Method",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                        CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
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
        actual: Sequence[str] = builder.build_struct(obj)

        assert actual == expected
        assert builder.import_set == {NamespaceBuilder.OVERLOAD, "Namespace.Type"}

    def test_events(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_struct() with a struct with events."""
        obj: CStruct = CStruct(
            name="Name",
            namespace="Namespace",
            events={
                "Namespace:Name.EventA": CEvent(
                    name="EventA",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace:Name.EventB": CEvent(
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
        actual: Sequence[str] = builder.build_struct(obj)

        assert actual == expected
        assert builder.import_set == {"Namespace.Type", NamespaceBuilder.EVENT_TYPE}

    def test_nested_types(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_struct() with a struct with nested types."""
        obj: CStruct = CStruct(
            name="Name",
            namespace="Namespace",
            nested_types={
                "Namespace:Name.NestedClass": CClass(
                    name="NestedClass",
                    namespace="Namespace",
                    nested=CType(name="Name", namespace="Namespace"),
                ),
                "Namespace:Name.NestedStruct": CStruct(
                    name="NestedStruct",
                    namespace="Namespace",
                    nested=CType(name="Name", namespace="Namespace"),
                ),
                "Namespace:Name.INestedInterface": CInterface(
                    name="INestedInterface",
                    namespace="Namespace",
                    nested=CType(name="Name", namespace="Namespace"),
                ),
                "Namespace:Name.NestedEnum": CEnum(
                    name="NestedEnum",
                    namespace="Namespace",
                    nested=CType(name="Name", namespace="Namespace"),
                    fields=(),
                ),
                "Namespace:Name.NestedDelegate": CDelegate(
                    name="NestedDelegate",
                    namespace="Namespace",
                    nested=CType(name="Name", namespace="Namespace"),
                    parameters=(),
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
            "    NestedDelegate: Callable[[], Type] = ...",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_struct(obj)

        assert actual == expected
        assert builder.import_set == {
            NamespaceBuilder.CALLABLE,
            NamespaceBuilder.ENUM,
            "Namespace.Type",
        }


class TestBuildInterface:
    """Tests for NamespaceBuilder.build_interface()."""

    def test_basic(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_interface() with a basic interface."""
        obj: CInterface = CInterface(name="Name", namespace="Namespace")

        expected: Sequence[str] = [
            "class Name:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_interface(obj)

        assert actual == expected

    def test_generic(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_interface() with an interface with generic arguments."""
        obj: CInterface = CInterface(
            name="Name",
            namespace="Namespace",
            generic_args=(CType(name="A", generic=True), CType(name="B", generic=True)),
        )

        expected: Sequence[str] = [
            "class Name[A, B]:",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_interface(obj)

        assert actual == expected

    def test_interfaces(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_interface() with an interface with interfaces."""
        obj: CInterface = CInterface(
            name="Name",
            namespace="Namespace",
            interfaces=(
                CType(name="InterfaceA", namespace="Namespace"),
                CType(name="InterfaceB", namespace="Namespace"),
            ),
        )

        expected: Sequence[str] = [
            "class Name(InterfaceA, InterfaceB):",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_interface(obj)

        assert actual == expected
        assert builder.import_set == {"Namespace.InterfaceA", "Namespace.InterfaceB"}

    def test_fields(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_interface() with an interface with fields."""
        obj: CInterface = CInterface(
            name="Name",
            namespace="Namespace",
            fields={
                "Namespace:Class.FieldA": CField(
                    name="FieldA",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    return_type=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace:Class.FieldB": CField(
                    name="FieldB",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    return_type=CType(name="Type", namespace="Namespace"),
                ),
            },
        )

        expected: Sequence[str] = [
            "class Name:",
            '    """"""',
            "    FieldA: Final[Type] = ...",
            '    """"""',
            "    FieldB: Final[Type] = ...",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_interface(obj)

        assert actual == expected
        assert builder.import_set == {NamespaceBuilder.FINAL, "Namespace.Type"}

    def test_properties(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_interface() with an interface with properties."""
        obj: CInterface = CInterface(
            name="Name",
            namespace="Namespace",
            properties={
                "Namespace:Name.PropertyA": CProperty(
                    name="PropertyA",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace:Name.PropertyB": CProperty(
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
        actual: Sequence[str] = builder.build_interface(obj)

        assert actual == expected
        assert builder.import_set == {"Namespace.Type"}

    def test_methods(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_interface() with an interface with methods."""
        obj: CInterface = CInterface(
            name="Name",
            namespace="Namespace",
            methods={
                "Namespace:Name.MethodA(Namespace:Type, Namespace:Type)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                        CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace:Name.MethodB(Namespace:Type, Namespace:Type)": CMethod(
                    name="MethodB",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                        CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
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
        actual: Sequence[str] = builder.build_interface(obj)

        assert actual == expected
        assert builder.import_set == {"Namespace.Type"}

    def test_methods_overload(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_interface() with an interface with overloaded methods."""
        obj: CInterface = CInterface(
            name="Name",
            namespace="Namespace",
            methods={
                "Namespace:Name.Method(Namespace:Type)": CMethod(
                    name="Method",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace:Name.Method(Namespace:Type, Namespace:Type)": CMethod(
                    name="Method",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                        CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
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
        actual: Sequence[str] = builder.build_interface(obj)

        assert actual == expected
        assert builder.import_set == {NamespaceBuilder.OVERLOAD, "Namespace.Type"}

    def test_events(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_interface() with an interface with events."""
        obj: CInterface = CInterface(
            name="Name",
            namespace="Namespace",
            events={
                "Namespace:Name.EventA": CEvent(
                    name="EventA",
                    declaring_type=CType(name="Name", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace:Name.EventB": CEvent(
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
        actual: Sequence[str] = builder.build_interface(obj)

        assert actual == expected
        assert builder.import_set == {"Namespace.Type", NamespaceBuilder.EVENT_TYPE}

    def test_nested_types(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_interface() with an interface with nested types."""
        obj: CInterface = CInterface(
            name="Name",
            namespace="Namespace",
            nested_types={
                "Namespace:Name.NestedClass": CClass(
                    name="NestedClass",
                    namespace="Namespace",
                    nested=CType(name="Name", namespace="Namespace"),
                ),
                "Namespace:Name.NestedStruct": CStruct(
                    name="NestedStruct",
                    namespace="Namespace",
                    nested=CType(name="Name", namespace="Namespace"),
                ),
                "Namespace:Name.INestedInterface": CInterface(
                    name="INestedInterface",
                    namespace="Namespace",
                    nested=CType(name="Name", namespace="Namespace"),
                ),
                "Namespace:Name.NestedEnum": CEnum(
                    name="NestedEnum",
                    namespace="Namespace",
                    nested=CType(name="Name", namespace="Namespace"),
                    fields=(),
                ),
                "Namespace:Name.NestedDelegate": CDelegate(
                    name="NestedDelegate",
                    namespace="Namespace",
                    nested=CType(name="Name", namespace="Namespace"),
                    parameters=(),
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
            "    NestedDelegate: Callable[[], Type] = ...",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_interface(obj)

        assert actual == expected
        assert builder.import_set == {
            NamespaceBuilder.CALLABLE,
            NamespaceBuilder.ENUM,
            "Namespace.Type",
        }


class TestBuildEnum:
    """Tests for NamespaceBuilder.build_enum()."""

    def test_basic(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_enum() with a basic enum."""
        obj: CEnum = CEnum(name="Name", namespace="Namespace")

        expected: Sequence[str] = [
            "class Name(Enum):",
            '    """"""',
        ]
        actual: Sequence[str] = builder.build_enum(obj)

        assert actual == expected
        assert builder.import_set == {NamespaceBuilder.ENUM}

    def test_fields(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_enum() with an enum with multiple fields."""
        obj: CEnum = CEnum(
            name="Enum",
            namespace="Namespace",
            fields=("FieldA", "FieldB", "FieldC", "FieldD"),
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
        assert builder.import_set == {NamespaceBuilder.ENUM}


class TestBuildDelegate:
    """Tests for NamespaceBuilder.build_delegate()."""

    def test_basic(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_delegate() with a basic delegate."""
        obj: CDelegate = CDelegate(name="Name", namespace="Namespace")

        expected: Sequence[str] = [
            "Name: Callable[[], None] = ...",
            '""""""',
        ]
        actual: Sequence[str] = builder.build_delegate(obj)

        assert actual == expected
        assert builder.import_set == {NamespaceBuilder.CALLABLE}

    def test_parameters(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_delegate() with a delegate with parameters."""
        obj: CDelegate = CDelegate(
            name="Name",
            namespace="Namespace",
            parameters=(
                CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
            ),
        )

        expected: Sequence[str] = [
            "Name: Callable[[Type, Type], None] = ...",
            '""""""',
        ]
        actual: Sequence[str] = builder.build_delegate(obj)

        assert actual == expected
        assert builder.import_set == {NamespaceBuilder.CALLABLE, "Namespace.Type"}

    def test_return(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_delegate() with a delegate with parameters."""
        obj: CDelegate = CDelegate(
            name="Name",
            namespace="Namespace",
            return_type=CType(name="Type", namespace="Namespace"),
        )

        expected: Sequence[str] = [
            "Name: Callable[[], Type] = ...",
            '""""""',
        ]
        actual: Sequence[str] = builder.build_delegate(obj)

        assert actual == expected
        assert builder.import_set == {NamespaceBuilder.CALLABLE, "Namespace.Type"}


class TestBuildImportSet:
    """Tests for NamespaceBuilder.build_import_set()."""

    def test_basic(self, builder: NamespaceBuilder) -> None:
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

    def test_namespace(self, builder: NamespaceBuilder) -> None:
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

    def test_event_type(self, builder: NamespaceBuilder) -> None:
        """Test for ImportList.build_import_set()."""
        builder.import_type(CType(name="TypeA", namespace="Namespace"))
        builder.import_type(CType(name="TypeB", namespace="Namespace"))
        builder.import_type(CType(name="TypeC", namespace="Namespace"))
        builder.import_type(CType(name="TypeD", namespace="Namespace"))
        builder.import_set.add(NamespaceBuilder.EVENT_TYPE)

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

    def test_basic(self, builder: NamespaceBuilder) -> None:
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

    def test_types(self, builder: NamespaceBuilder) -> None:
        """Test for NamespaceBuilder.build_namespace() with a basic namespace."""
        obj: CNamespace = CNamespace(
            name="Name",
            types={
                "Name:Class": CClass(name="Class", namespace="Name"),
                "Name:Struct": CStruct(name="Struct", namespace="Name"),
                "Name:IInterface": CInterface(name="IInterface", namespace="Name"),
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
            "Delegate: Callable[[], None] = ...",
            '""""""',
            "class Enum(Enum):",
            '    """"""',
            "class IInterface:",
            '    """"""',
            "class Struct:",
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
        builder: NamespaceBuilder,
        namespaces: Sequence[CNamespace],
        tmp_path: Path,
        files: Sequence[str],
    ) -> None:
        """Test for build_stubs()."""
        build_stubs(builder, namespaces, tmp_path)

        for file in files:
            stub_file: Path = tmp_path / file / "__init__.pyi"

            assert stub_file.exists()

    @pytest.mark.parametrize(("namespaces", "files"), **make_params(namespaces_list))
    def test_multi_threaded(
        self,
        builder: NamespaceBuilder,
        namespaces: Sequence[CNamespace],
        tmp_path: Path,
        files: Sequence[str],
    ) -> None:
        """Test for build_stubs()."""
        build_stubs(builder, namespaces, tmp_path, threads=4)

        for file in files:
            stub_file: Path = tmp_path / file / "__init__.pyi"

            assert stub_file.exists()

    # def test_build_test_lib(self) -> None:
    #     skeleton_name: str = "TestLib_1.0.0.0_skeleton.json"
    #     doc_name: str = "TestLib_1.0.0.0_doc.json"
    #
    #     result = build_stubs(
    #         skeleton_files=(Path(skeleton_name),),
    #         doc_files=(Path(doc_name),),
    #         output_dir=self.output_dir,
    #         line_length=100,
    #         multi_threaded=False,
    #         format_files=True,
    #     )
    #
    #     self.assertEqual(0, result)


class TestFormatStubs:
    """Tests for format_stubs()."""

    def test_basic(self, output_dir: Path) -> None:
        """Test for format_stubs()."""
        format_stubs(100, output_dir)

    def test_multi_threaded(self, output_dir: Path) -> None:
        """Test for format_stubs()."""
        format_stubs(100, output_dir, threads=4)


class TestCommandBuild:
    """Tests for command_build()."""

    # TODO(Ryan): Monkey patch build_stubs and format_stubs to test command


if __name__ == "__main__":
    pytest.main()
