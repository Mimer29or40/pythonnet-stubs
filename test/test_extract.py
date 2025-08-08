"""Tests for stubgen.extract_stubs.py."""

from __future__ import annotations

import functools
from dataclasses import replace
from pprint import pprint
from typing import TYPE_CHECKING
from typing import override

import clr
import pytest
from conftest import TEST_LIB
from conftest import TL_DOC
from conftest import TL_SKELETON
from conftest import generic
from System import Int32
from System import Type
from System.Reflection import ReflectionTypeLoadException

from stubgen.extract_stubs import extract_assemblies
from stubgen.extract_stubs import extract_class
from stubgen.extract_stubs import extract_constructor
from stubgen.extract_stubs import extract_delegate
from stubgen.extract_stubs import extract_enum
from stubgen.extract_stubs import extract_event
from stubgen.extract_stubs import extract_field
from stubgen.extract_stubs import extract_method
from stubgen.extract_stubs import extract_parameter
from stubgen.extract_stubs import extract_property
from stubgen.extract_stubs import extract_type
from stubgen.extract_stubs import extract_type_def
from stubgen.model import CClass
from stubgen.model import CConstructor
from stubgen.model import CDelegate
from stubgen.model import CEnum
from stubgen.model import CEvent
from stubgen.model import CField
from stubgen.model import CMethod
from stubgen.model import CParameter
from stubgen.model import CProperty
from stubgen.model import CType
from stubgen.model import CTypeDefinition
from stubgen.util import make_python_name
from stubgen.util import to_c_array

if TYPE_CHECKING:  # pragma: no cover
    from collections.abc import Mapping
    from collections.abc import Sequence
    from pathlib import Path

    from System.Reflection import Assembly
    from System.Reflection import ConstructorInfo
    from System.Reflection import EventInfo
    from System.Reflection import FieldInfo
    from System.Reflection import MethodInfo
    from System.Reflection import ParameterInfo
    from System.Reflection import PropertyInfo
    from System.Reflection import TypeInfo

OBJECT: CType = CType(name="Object", namespace="System")
STRUCT: CType = CType(name="ValueType", namespace="System")
INT32: CType = CType(name="Int32", namespace="System")
BOOLEAN: CType = CType(name="Boolean", namespace="System")
EVENT_HANDLER: CType = CType(name="EventHandler", namespace="System")
EVENT_HANDLER_ARGS: CType = replace(
    EVENT_HANDLER,
    inner=[CType(name="EventArgs", namespace="System")],
)

COMPARABLE: CType = CType(name="IComparable", namespace="System", inner=[generic("T")])
EQUATABLE: CType = CType(name="IEquatable", namespace="System", inner=[generic("T")])
COLLECTION = CType(name="ICollection", namespace="System.Collections.Generic", inner=[generic("T")])
ENUMERABLE = CType(name="IEnumerable", namespace="System.Collections.Generic", inner=[generic("T")])
LIST = CType(name="IList", namespace="System.Collections.Generic", inner=[generic("T")])


@pytest.fixture(scope="session")
def assembly() -> Assembly:
    """Assembly fixture."""
    # noinspection PyUnresolvedReferences
    return clr.AddReference(TEST_LIB)


class _Base:
    @staticmethod
    def get_type(assembly: Assembly, name: str) -> TypeInfo:
        try:
            type_info: TypeInfo
            for type_info in assembly.GetTypes():
                if type_info.Namespace is None or type_info.IsNested:
                    continue
                if make_python_name(type_info.Name) == name:
                    return type_info
        except ReflectionTypeLoadException as e:
            pprint([_e.Message for _e in e.LoaderExceptions])
        raise NameError(f"Unable to find type named {name!r}")

    @classmethod
    def basic_class(cls, declaring_type: CType, parent: CType | None = None) -> CClass:
        name: str = declaring_type.name
        namespace: str = declaring_type.namespace
        generic_args: Sequence[CType] = declaring_type.inner
        if parent is not None:
            declaring_type = replace(declaring_type, name=f"{parent.name}.{declaring_type.name}")
        return CClass(
            name=name,
            namespace=namespace,
            parent=parent,
            generic_args=generic_args,
            super_class=OBJECT,
            constructors={"__init__()": CConstructor(declaring_type=declaring_type)},
            methods={
                "Equals(System:Object)": CMethod(
                    name="Equals",
                    declaring_type=OBJECT,
                    parameters=[CParameter(name="obj", type=OBJECT)],
                    return_types=[BOOLEAN],
                ),
                "GetHashCode()": CMethod(
                    name="GetHashCode",
                    declaring_type=OBJECT,
                    return_types=[INT32],
                ),
                "GetType()": CMethod(
                    name="GetType",
                    declaring_type=OBJECT,
                    return_types=[CType(name="Type", namespace="System")],
                ),
                "ToString()": CMethod(
                    name="ToString",
                    declaring_type=OBJECT,
                    return_types=[CType(name="String", namespace="System")],
                ),
            },
        )

    @classmethod
    def basic_struct(cls, declaring_type: CType, parent: CType | None = None) -> CClass:
        name: str = declaring_type.name
        namespace: str = declaring_type.namespace
        generic_args: Sequence[CType] = declaring_type.inner
        return CClass(
            name=name,
            namespace=namespace,
            parent=parent,
            generic_args=generic_args,
            super_class=STRUCT,
            methods={
                "Equals(System:Object)": CMethod(
                    name="Equals",
                    declaring_type=OBJECT,
                    parameters=[CParameter(name="obj", type=OBJECT)],
                    return_types=[BOOLEAN],
                ),
                "GetHashCode()": CMethod(
                    name="GetHashCode",
                    declaring_type=OBJECT,
                    return_types=[INT32],
                ),
                "GetType()": CMethod(
                    name="GetType",
                    declaring_type=OBJECT,
                    return_types=[CType(name="Type", namespace="System")],
                ),
                "ToString()": CMethod(
                    name="ToString",
                    declaring_type=OBJECT,
                    return_types=[CType(name="String", namespace="System")],
                ),
            },
        )

    @classmethod
    def basic_record(cls, declaring_type: CType, parent: CType | None = None) -> CClass:
        name: str = declaring_type.name
        namespace: str = declaring_type.namespace
        generic_args: Sequence[CType] = declaring_type.inner
        if parent is not None:
            declaring_type = replace(declaring_type, name=f"{parent.name}.{declaring_type.name}")
        return CClass(
            name=name,
            namespace=namespace,
            parent=parent,
            generic_args=generic_args,
            super_class=OBJECT,
            interfaces=[replace(EQUATABLE, inner=[declaring_type])],
            constructors={"__init__()": CConstructor(declaring_type=declaring_type)},
            methods={
                "Clone()": CMethod(
                    name="Clone",
                    declaring_type=declaring_type,
                    return_types=[declaring_type],
                ),
                "Equals(System:Object)": CMethod(
                    name="Equals",
                    declaring_type=OBJECT,
                    parameters=[CParameter(name="obj", type=OBJECT)],
                    return_types=[BOOLEAN],
                ),
                f"Equals({declaring_type.full_name})": CMethod(
                    name="Equals",
                    declaring_type=EQUATABLE,
                    parameters=[CParameter(name="other", type=declaring_type)],
                    return_types=[BOOLEAN],
                    static=False,
                ),
                "GetHashCode()": CMethod(
                    name="GetHashCode",
                    declaring_type=OBJECT,
                    return_types=[INT32],
                ),
                "GetType()": CMethod(
                    name="GetType",
                    declaring_type=OBJECT,
                    return_types=[CType(name="Type", namespace="System")],
                ),
                "ToString()": CMethod(
                    name="ToString",
                    declaring_type=OBJECT,
                    return_types=[CType(name="String", namespace="System")],
                ),
                f"op_Equality({declaring_type.full_name}, {declaring_type.full_name})": CMethod(
                    name="op_Equality",
                    declaring_type=declaring_type,
                    parameters=[
                        CParameter(name="left", type=declaring_type),
                        CParameter(name="right", type=declaring_type),
                    ],
                    return_types=[BOOLEAN],
                    static=True,
                ),
                f"op_Inequality({declaring_type.full_name}, {declaring_type.full_name})": CMethod(
                    name="op_Inequality",
                    declaring_type=declaring_type,
                    parameters=[
                        CParameter(name="left", type=declaring_type),
                        CParameter(name="right", type=declaring_type),
                    ],
                    return_types=[BOOLEAN],
                    static=True,
                ),
                f"__eq__({declaring_type.full_name})": CMethod(
                    name="__eq__",
                    declaring_type=declaring_type,
                    parameters=[CParameter(name="other", type=declaring_type)],
                    return_types=[BOOLEAN],
                ),
                f"__ne__({declaring_type.full_name})": CMethod(
                    name="__ne__",
                    declaring_type=declaring_type,
                    parameters=[CParameter(name="other", type=declaring_type)],
                    return_types=[BOOLEAN],
                ),
            },
        )

    @classmethod
    def basic_interface(cls, declaring_type: CType, parent: CType | None = None) -> CClass:
        return CClass(
            name=declaring_type.name,
            namespace=declaring_type.namespace,
            parent=parent,
            abstract=True,
            generic_args=declaring_type.inner,
        )

    @classmethod
    def basic_enum(cls, declaring_type: CType, parent: CType | None = None) -> CEnum:
        return CEnum(name=declaring_type.name, namespace=declaring_type.namespace, parent=parent)

    @classmethod
    def basic_delegate(cls, declaring_type: CType, parent: CType | None = None) -> CDelegate:
        return CDelegate(
            name=declaring_type.name,
            namespace=declaring_type.namespace,
            parent=parent,
        )

    @classmethod
    def dunder_methods(cls, declaring_type: CType) -> Mapping[str, CMethod]:
        full_name: str = declaring_type.full_name
        base: CMethod = CMethod(name="TEMP", declaring_type=declaring_type)
        param_self: CMethod = replace(
            base,
            parameters=[CParameter(name="self", type=declaring_type)],
        )
        param_other: CMethod = replace(
            base,
            parameters=[CParameter(name="other", type=declaring_type)],
        )
        param_lr: CMethod = replace(
            base,
            parameters=[
                CParameter(name="left", type=declaring_type),
                CParameter(name="right", type=declaring_type),
            ],
        )
        return {
            f"op_Addition({full_name}, {full_name})": replace(
                param_lr,
                name="op_Addition",
                return_types=[declaring_type],
                static=True,
            ),
            f"op_BitwiseAnd({full_name}, {full_name})": replace(
                param_lr,
                name="op_BitwiseAnd",
                return_types=[declaring_type],
                static=True,
            ),
            f"op_BitwiseOr({full_name}, {full_name})": replace(
                param_lr,
                name="op_BitwiseOr",
                return_types=[declaring_type],
                static=True,
            ),
            f"op_Decrement({full_name})": replace(
                param_self,
                name="op_Decrement",
                return_types=[declaring_type],
                static=True,
            ),
            f"op_Division({full_name}, {full_name})": replace(
                param_lr,
                name="op_Division",
                return_types=[declaring_type],
                static=True,
            ),
            f"op_Equality({full_name}, {full_name})": replace(
                param_lr,
                name="op_Equality",
                return_types=[BOOLEAN],
                static=True,
            ),
            f"op_ExclusiveOr({full_name}, {full_name})": replace(
                param_lr,
                name="op_ExclusiveOr",
                return_types=[declaring_type],
                static=True,
            ),
            f"op_False({full_name})": replace(
                param_self,
                name="op_False",
                return_types=[BOOLEAN],
                static=True,
            ),
            f"op_GreaterThan({full_name}, {full_name})": replace(
                param_lr,
                name="op_GreaterThan",
                return_types=[BOOLEAN],
                static=True,
            ),
            f"op_GreaterThanOrEqual({full_name}, {full_name})": replace(
                param_lr,
                name="op_GreaterThanOrEqual",
                return_types=[BOOLEAN],
                static=True,
            ),
            f"op_Increment({full_name})": replace(
                param_self,
                name="op_Increment",
                return_types=[declaring_type],
                static=True,
            ),
            f"op_Inequality({full_name}, {full_name})": replace(
                param_lr,
                name="op_Inequality",
                return_types=[BOOLEAN],
                static=True,
            ),
            f"op_LeftShift({full_name}, {full_name})": replace(
                param_lr,
                name="op_LeftShift",
                return_types=[declaring_type],
                static=True,
            ),
            f"op_LessThan({full_name}, {full_name})": replace(
                param_lr,
                name="op_LessThan",
                return_types=[BOOLEAN],
                static=True,
            ),
            f"op_LessThanOrEqual({full_name}, {full_name})": replace(
                param_lr,
                name="op_LessThanOrEqual",
                return_types=[BOOLEAN],
                static=True,
            ),
            f"op_LogicalNot({full_name})": replace(
                param_self,
                name="op_LogicalNot",
                return_types=[BOOLEAN],
                static=True,
            ),
            f"op_Modulus({full_name}, {full_name})": replace(
                param_lr,
                name="op_Modulus",
                return_types=[declaring_type],
                static=True,
            ),
            f"op_Multiply({full_name}, {full_name})": replace(
                param_lr,
                name="op_Multiply",
                return_types=[declaring_type],
                static=True,
            ),
            f"op_OnesComplement({full_name})": replace(
                param_self,
                name="op_OnesComplement",
                return_types=[declaring_type],
                static=True,
            ),
            f"op_Subtraction({full_name}, {full_name})": replace(
                param_lr,
                name="op_Subtraction",
                return_types=[declaring_type],
                static=True,
            ),
            f"op_True({full_name})": replace(
                param_self,
                name="op_True",
                return_types=[BOOLEAN],
                static=True,
            ),
            f"op_UnaryNegation({full_name})": replace(
                param_self,
                name="op_UnaryNegation",
                return_types=[declaring_type],
                static=True,
            ),
            f"op_UnaryPlus({full_name})": replace(
                param_self,
                name="op_UnaryPlus",
                return_types=[declaring_type],
                static=True,
            ),
            f"op_UnsignedRightShift({full_name}, {full_name})": replace(
                param_lr,
                name="op_UnsignedRightShift",
                return_types=[declaring_type],
                static=True,
            ),
            f"__add__({full_name})": replace(
                param_other,
                name="__add__",
                return_types=[declaring_type],
            ),
            f"__and__({full_name})": replace(
                param_other,
                name="__and__",
                return_types=[declaring_type],
            ),
            f"__eq__({full_name})": replace(
                param_other,
                name="__eq__",
                return_types=[BOOLEAN],
            ),
            f"__ge__({full_name})": replace(
                param_other,
                name="__ge__",
                return_types=[BOOLEAN],
            ),
            f"__gt__({full_name})": replace(
                param_other,
                name="__gt__",
                return_types=[BOOLEAN],
            ),
            "__invert__()": CMethod(
                name="__invert__",
                declaring_type=declaring_type,
                return_types=[declaring_type],
            ),
            f"__le__({full_name})": replace(
                param_other,
                name="__le__",
                return_types=[BOOLEAN],
            ),
            f"__lshift__({full_name})": replace(
                param_other,
                name="__lshift__",
                return_types=[declaring_type],
            ),
            f"__lt__({full_name})": replace(
                param_other,
                name="__lt__",
                return_types=[BOOLEAN],
            ),
            f"__mod__({full_name})": replace(
                param_other,
                name="__mod__",
                return_types=[declaring_type],
            ),
            f"__mul__({full_name})": replace(
                param_other,
                name="__mul__",
                return_types=[declaring_type],
            ),
            f"__ne__({full_name})": replace(
                param_other,
                name="__ne__",
                return_types=[BOOLEAN],
            ),
            "__neg__()": CMethod(
                name="__neg__",
                declaring_type=declaring_type,
                parameters=[],
                return_types=[declaring_type],
            ),
            f"__or__({full_name})": replace(
                param_other,
                name="__or__",
                return_types=[declaring_type],
            ),
            "__pos__()": CMethod(
                name="__pos__",
                declaring_type=declaring_type,
                parameters=[],
                return_types=[declaring_type],
            ),
            f"__sub__({full_name})": replace(
                param_other,
                name="__sub__",
                return_types=[declaring_type],
            ),
            f"__truediv__({full_name})": replace(
                param_other,
                name="__truediv__",
                return_types=[declaring_type],
            ),
            f"__xor__({full_name})": replace(
                param_other,
                name="__xor__",
                return_types=[declaring_type],
            ),
        }

    @classmethod
    def list_properties(cls) -> Mapping[str, CProperty]:
        return {
            "Count": CProperty(name="Count", declaring_type=COLLECTION, type=INT32),
            "IsReadOnly": CProperty(name="IsReadOnly", declaring_type=COLLECTION, type=BOOLEAN),
            "Item": CProperty(name="Item", declaring_type=LIST, type=INT32, setter=True),
        }

    @classmethod
    def list_methods(cls, type_var: CType) -> Mapping[str, CMethod]:
        return {
            f"Add({type_var.full_name})": CMethod(
                name="Add",
                declaring_type=COLLECTION,
                parameters=[CParameter(name="item", type=type_var)],
                return_types=[CType.VOID],
            ),
            "Clear()": CMethod(
                name="Clear",
                declaring_type=COLLECTION,
                return_types=[CType.VOID],
            ),
            f"Contains({type_var.full_name})": CMethod(
                name="Contains",
                declaring_type=COLLECTION,
                parameters=[CParameter(name="item", type=type_var)],
                return_types=[BOOLEAN],
            ),
            f"CopyTo(System:Array[{type_var.full_name}], System:Int32)": CMethod(
                name="CopyTo",
                declaring_type=COLLECTION,
                parameters=[
                    CParameter(
                        name="array",
                        type=CType(name="Array", namespace="System", inner=[type_var]),
                    ),
                    CParameter(name="arrayIndex", type=INT32),
                ],
                return_types=[CType.VOID],
            ),
            "GetEnumerator()": CMethod(
                name="GetEnumerator",
                declaring_type=CType(name="IEnumerable", namespace="System.Collections"),
                return_types=[
                    CType(
                        name="IEnumerator",
                        namespace="System.Collections.Generic",
                        inner=[type_var],
                    ),
                ],
            ),
            f"IndexOf({type_var.full_name})": CMethod(
                name="IndexOf",
                declaring_type=LIST,
                parameters=[CParameter(name="item", type=type_var)],
                return_types=[INT32],
            ),
            f"Insert(System:Int32, {type_var.full_name})": CMethod(
                name="Insert",
                declaring_type=LIST,
                parameters=[
                    CParameter(name="index", type=INT32),
                    CParameter(name="item", type=type_var),
                ],
                return_types=[CType.VOID],
            ),
            f"Remove({type_var.full_name})": CMethod(
                name="Remove",
                declaring_type=COLLECTION,
                parameters=[CParameter(name="item", type=type_var)],
                return_types=[BOOLEAN],
            ),
            "RemoveAt(System:Int32)": CMethod(
                name="RemoveAt",
                declaring_type=LIST,
                parameters=[CParameter(name="index", type=INT32)],
                return_types=[CType.VOID],
            ),
            f"__contains__({type_var.full_name})": CMethod(
                name="__contains__",
                declaring_type=COLLECTION,
                parameters=[CParameter(name="item", type=type_var)],
                return_types=[BOOLEAN],
            ),
            f"__delitem__({type_var.full_name})": CMethod(
                name="__delitem__",
                declaring_type=COLLECTION,
                parameters=[CParameter(name="item", type=type_var)],
                return_types=[BOOLEAN],
            ),
            "__getitem__(System:Int32)": CMethod(
                name="__getitem__",
                declaring_type=LIST,
                parameters=[CParameter(name="index", type=INT32)],
                return_types=[INT32],
            ),
            "__iter__()": CMethod(
                name="__iter__",
                declaring_type=CType(name="IEnumerable", namespace="System.Collections"),
                return_types=[
                    CType(name="Iterator", namespace="collections.abc", inner=[type_var])
                ],
            ),
            "__len__()": CMethod(
                name="__len__",
                declaring_type=COLLECTION,
                return_types=[INT32],
            ),
            f"__setitem__(System:Int32, {type_var.full_name})": CMethod(
                name="__setitem__",
                declaring_type=LIST,
                parameters=[
                    CParameter(name="index", type=INT32),
                    CParameter(name="value", type=type_var),
                ],
                return_types=[CType.VOID],
            ),
        }

    @classmethod
    def nested_types(cls, parent: CType) -> Mapping[str, CTypeDefinition]:
        base: CType = CType(name="TEMP", namespace=TEST_LIB)
        return {
            obj.unique_name: obj
            for obj in [
                cls.basic_interface(replace(base, name="INested"), parent=parent),
                cls.basic_delegate(replace(base, name="NestedDelegate"), parent=parent),
                cls.basic_enum(replace(base, name="NestedEnum"), parent=parent),
                cls.basic_class(replace(base, name="NestedClass"), parent=parent),
                cls.basic_record(replace(base, name="NestedRecord"), parent=parent),
                cls.basic_struct(replace(base, name="NestedStruct"), parent=parent),
            ]
        }


class _MemberBase(_Base):
    type_name: str

    @pytest.fixture(scope="class")
    def type_info(self, assembly: Assembly) -> TypeInfo:
        return self.get_type(assembly, self.type_name)

    @classmethod
    @functools.cache
    def parent(cls) -> CType:
        return CType(name=cls.type_name, namespace=TEST_LIB)


class TestExtractType(_MemberBase):
    """Tests for extract_type()."""

    type_name: str = "ExtractType"

    def test_none(self) -> None:
        """Tests for extract_type() with None."""
        expected: CType | None = None
        actual: CType | None = extract_type(None)

        assert actual == expected

    def test_basic(self, type_info: TypeInfo) -> None:
        """Tests for extract_type() with a basic type."""
        method: MethodInfo = type_info.GetMethod("Basic")
        parameter: ParameterInfo = method.GetParameters()[0]

        expected: CType | None = INT32
        actual: CType | None = extract_type(parameter.ParameterType)

        assert actual == expected

    def test_reference(self, type_info: TypeInfo) -> None:
        """Tests for extract_type() with a reference type."""
        method: MethodInfo = type_info.GetMethod("Reference")
        parameter: ParameterInfo = method.GetParameters()[0]

        expected: CType | None = replace(INT32, reference=True)
        actual: CType | None = extract_type(parameter.ParameterType)

        assert actual == expected

    def test_generic(self, type_info: TypeInfo) -> None:
        """Tests for extract_type() with a generic type."""
        method: MethodInfo = type_info.GetMethod("Generic")
        parameter: ParameterInfo = method.GetParameters()[0]

        expected: CType | None = generic("T")
        actual: CType | None = extract_type(parameter.ParameterType)

        assert actual == expected

    def test_nullable(self, type_info: TypeInfo) -> None:
        """Tests for extract_type() with a nullable type."""
        method: MethodInfo = type_info.GetMethod("Nullable")
        parameter: ParameterInfo = method.GetParameters()[0]

        expected: CType | None = replace(INT32, nullable=True)
        actual: CType | None = extract_type(parameter.ParameterType)

        assert actual == expected

    def test_array(self, type_info: TypeInfo) -> None:
        """Tests for extract_type() with an array type."""
        method: MethodInfo = type_info.GetMethod("Array")
        parameter: ParameterInfo = method.GetParameters()[0]

        expected: CType | None = CType(name="Array", namespace="System", inner=[INT32])
        actual: CType | None = extract_type(parameter.ParameterType)

        assert actual == expected

    def test_use_generic(self, type_info: TypeInfo) -> None:
        """Tests for extract_type() with a reference type."""
        method: MethodInfo = type_info.GetMethod("UseGeneric")
        parameter: ParameterInfo = method.GetParameters()[0]

        expected: CType | None = EQUATABLE
        actual: CType | None = extract_type(parameter.ParameterType, use_generic=True)

        assert actual == expected

    def test_nested(self, type_info: TypeInfo) -> None:
        """Tests for extract_type() with a reference type."""
        type_info = type_info.GetNestedType("Nested")

        expected: CType | None = CType(name="ExtractType.Nested", namespace="TestLib")
        actual: CType | None = extract_type(type_info)

        assert actual == expected


class TestExtractParameter(_MemberBase):
    """Tests for extract_parameter()."""

    type_name: str = "ExtractParameter"

    def test_basic(self, type_info: TypeInfo) -> None:
        """Tests for extract_parameter() with a basic parameter."""
        method: MethodInfo = type_info.GetMethod("Basic")
        parameter: ParameterInfo = method.GetParameters()[0]

        expected: CParameter | None = CParameter(name="param", type=INT32)
        actual: CParameter | None = extract_parameter(parameter)

        assert actual == expected

    def test_default(self, type_info: TypeInfo) -> None:
        """Tests for extract_parameter() with a default parameter."""
        method: MethodInfo = type_info.GetMethod("Default")
        parameter: ParameterInfo = method.GetParameters()[0]

        expected: CParameter | None = CParameter(name="param", type=INT32, default=True)
        actual: CParameter | None = extract_parameter(parameter)

        assert actual == expected

    def test_out(self, type_info: TypeInfo) -> None:
        """Tests for extract_parameter() with an out parameter."""
        method: MethodInfo = type_info.GetMethod("Out")
        parameter: ParameterInfo = method.GetParameters()[0]

        expected: CParameter | None = CParameter(
            name="param",
            type=replace(INT32, reference=True),
            out=True,
        )
        actual: CParameter | None = extract_parameter(parameter)

        assert actual == expected


class TestExtractField(_MemberBase):
    """Tests for extract_field()."""

    type_name: str = "ExtractField"

    def test_basic(self, type_info: TypeInfo) -> None:
        """Tests for extract_field() with a basic field."""
        name: str = "Basic"
        field: FieldInfo = type_info.GetField(name)

        expected: CField | None = CField(
            name=name,
            declaring_type=self.parent(),
            return_type=INT32,
        )
        actual: CField | None = extract_field(field)

        assert actual == expected

    def test_readonly(self, type_info: TypeInfo) -> None:
        """Tests for extract_field() with a readonly field."""
        name: str = "Readonly"
        field: FieldInfo = type_info.GetField(name)

        expected: CField | None = CField(
            name=name,
            declaring_type=self.parent(),
            return_type=INT32,
        )
        actual: CField | None = extract_field(field)

        assert actual == expected

    def test_static(self, type_info: TypeInfo) -> None:
        """Tests for extract_field() with a static field."""
        name: str = "Static"
        field: FieldInfo = type_info.GetField(name)

        expected: CField | None = CField(
            name=name,
            declaring_type=self.parent(),
            return_type=INT32,
            static=True,
        )
        actual: CField | None = extract_field(field)

        assert actual == expected


class TestExtractConstructor(_MemberBase):
    """Tests for extract_field()."""

    type_name: str = "ExtractConstructor"

    @classmethod
    @functools.cache
    @override
    def parent(cls) -> CType:
        return replace(super().parent(), inner=[generic("T")])

    def test_basic(self, type_info: TypeInfo) -> None:
        """Tests for extract_constructor() with a basic constructor."""
        constructor: ConstructorInfo = type_info.GetConstructor(to_c_array(Type, []))

        expected: CConstructor | None = CConstructor(declaring_type=self.parent())
        actual: CConstructor | None = extract_constructor(constructor)

        assert actual == expected

    def test_parameters(self, type_info: TypeInfo) -> None:
        """Tests for extract_constructor() with a constructor with parameters."""
        constructor: ConstructorInfo = type_info.GetConstructor(to_c_array(Type, [Int32, Int32]))

        expected: CConstructor | None = CConstructor(
            declaring_type=self.parent(),
            parameters=[
                CParameter(name="param0", type=INT32),
                CParameter(name="param1", type=INT32),
            ],
        )
        actual: CConstructor | None = extract_constructor(constructor)

        assert actual == expected


class TestExtractProperty(_MemberBase):
    """Tests for extract_property()."""

    type_name: str = "ExtractProperty"

    def test_basic(self, type_info: TypeInfo) -> None:
        """Tests for extract_property() with a basic property."""
        name: str = "Basic"
        property: PropertyInfo = type_info.GetProperty(name)  # noqa: A001

        expected: CProperty | None = CProperty(
            name=name,
            declaring_type=self.parent(),
            type=INT32,
            setter=True,
        )
        actual: CProperty | None = extract_property(property)

        assert actual == expected

    def test_readonly(self, type_info: TypeInfo) -> None:
        """Tests for extract_property() with a readonly property."""
        name: str = "Readonly"
        property: PropertyInfo = type_info.GetProperty(name)  # noqa: A001

        expected: CProperty | None = CProperty(
            name=name,
            declaring_type=self.parent(),
            type=INT32,
        )
        actual: CProperty | None = extract_property(property)

        assert actual == expected

    def test_static(self, type_info: TypeInfo) -> None:
        """Tests for extract_property() with a static property."""
        name: str = "Static"
        property: PropertyInfo = type_info.GetProperty(name)  # noqa: A001

        expected: CProperty | None = CProperty(
            name=name,
            declaring_type=self.parent(),
            type=INT32,
            setter=True,
            static=True,
        )
        actual: CProperty | None = extract_property(property)

        assert actual == expected

    def test_static_readonly(self, type_info: TypeInfo) -> None:
        """Tests for extract_property() with a static, readonly property."""
        name: str = "StaticReadOnly"
        property: PropertyInfo = type_info.GetProperty(name)  # noqa: A001

        expected: CProperty | None = CProperty(
            name=name,
            declaring_type=self.parent(),
            type=INT32,
            static=True,
        )
        actual: CProperty | None = extract_property(property)

        assert actual == expected


class TestExtractMethod(_MemberBase):
    """Tests for extract_method()."""

    type_name: str = "ExtractMethod"

    @classmethod
    @functools.cache
    @override
    def parent(cls) -> CType:
        return replace(super().parent(), inner=[generic("T")])

    def test_basic(self, type_info: TypeInfo) -> None:
        """Tests for extract_method() with a basic method."""
        name: str = "Basic"
        method: MethodInfo = type_info.GetMethod(name)

        expected: CMethod | None = CMethod(
            name=name,
            declaring_type=self.parent(),
            return_types=[CType.VOID],
        )
        actual: CMethod | None = extract_method(method)

        assert actual == expected

    def test_parameters(self, type_info: TypeInfo) -> None:
        """Tests for extract_method() with a method with parameters."""
        name: str = "Parameters"
        method: MethodInfo = type_info.GetMethod(name)

        expected: CMethod | None = CMethod(
            name=name,
            declaring_type=self.parent(),
            parameters=[
                CParameter(name="param0", type=INT32),
                CParameter(name="param1", type=INT32),
            ],
            return_types=[CType.VOID],
        )
        actual: CMethod | None = extract_method(method)

        assert actual == expected

    def test_out(self, type_info: TypeInfo) -> None:
        """Tests for extract_method() with a method with an out parameter."""
        name: str = "Out"
        method: MethodInfo = type_info.GetMethod(name)

        expected: CMethod | None = CMethod(
            name=name,
            declaring_type=self.parent(),
            parameters=[
                CParameter(name="param", type=replace(INT32, reference=True), out=True),
            ],
            return_types=[INT32, replace(INT32, reference=True)],
        )
        actual: CMethod | None = extract_method(method)

        assert actual == expected

    def test_void_out(self, type_info: TypeInfo) -> None:
        """Tests for extract_method() with a method with an out parameter."""
        name: str = "VoidOut"
        method: MethodInfo = type_info.GetMethod(name)

        expected: CMethod | None = CMethod(
            name=name,
            declaring_type=self.parent(),
            parameters=[
                CParameter(name="param", type=replace(INT32, reference=True), out=True),
            ],
            return_types=[CType.VOID, replace(INT32, reference=True)],
        )
        actual: CMethod | None = extract_method(method)

        assert actual == expected

    def test_static(self, type_info: TypeInfo) -> None:
        """Tests for extract_method() with a static method."""
        name: str = "Static"
        method: MethodInfo = type_info.GetMethod(name)

        expected: CMethod | None = CMethod(
            name=name,
            declaring_type=self.parent(),
            return_types=[CType.VOID],
            static=True,
        )
        actual: CMethod | None = extract_method(method)

        assert actual == expected

    def test_generic_class(self, type_info: TypeInfo) -> None:
        """Tests for extract_method() with a method with a generic class param."""
        name: str = "GenericClass"
        method: MethodInfo = type_info.GetMethod(name)

        expected: CMethod | None = CMethod(
            name=name,
            declaring_type=self.parent(),
            parameters=[CParameter(name="param", type=generic("T"))],
            return_types=[CType.VOID],
        )
        actual: CMethod | None = extract_method(method)

        assert actual == expected

    def test_generic_method(self, type_info: TypeInfo) -> None:
        """Tests for extract_method() with a method with a generic method param."""
        name: str = "GenericMethod"
        method: MethodInfo = type_info.GetMethod(name)

        expected: CMethod | None = CMethod(
            name=name,
            declaring_type=self.parent(),
            parameters=[
                CParameter(name="param0", type=generic("T0")),
                CParameter(name="param1", type=generic("T1")),
            ],
            return_types=[CType.VOID],
        )
        actual: CMethod | None = extract_method(method)

        assert actual == expected

    def test_generic_both(self, type_info: TypeInfo) -> None:
        """Tests for extract_method() with a method with a generic class and method params."""
        name: str = "GenericBoth"
        method: MethodInfo = type_info.GetMethod(name)

        expected: CMethod | None = CMethod(
            name=name,
            declaring_type=self.parent(),
            parameters=[
                CParameter(name="param", type=generic("T")),
                CParameter(name="param0", type=generic("T0")),
                CParameter(name="param1", type=generic("T1")),
            ],
            return_types=[CType.VOID],
        )
        actual: CMethod | None = extract_method(method)

        assert actual == expected


class TestExtractEvent(_MemberBase):
    """Tests for extract_event()."""

    type_name: str = "ExtractEvent"

    def test_basic(self, type_info: TypeInfo) -> None:
        """Tests for extract_event() with a basic event."""
        name: str = "Basic"
        event: EventInfo = type_info.GetEvent(name)

        expected: CEvent | None = CEvent(
            name=name,
            declaring_type=self.parent(),
            type=EVENT_HANDLER,
        )
        actual: CEvent | None = extract_event(event)

        assert actual == expected

    def test_arguments(self, type_info: TypeInfo) -> None:
        """Tests for extract_event() with an event with ."""
        name: str = "Arguments"
        event: EventInfo = type_info.GetEvent(name)

        expected: CEvent | None = CEvent(
            name=name,
            declaring_type=self.parent(),
            type=EVENT_HANDLER_ARGS,
        )
        actual: CEvent | None = extract_event(event)

        assert actual == expected


class TestExtractTypeDef(_Base):
    """Tests for extract_type_def()."""

    def test_class(self, assembly: Assembly) -> None:
        """Test for extract_type_def() with a class."""
        name: str = "ClassBasic"
        _class: TypeInfo = self.get_type(assembly, name)

        actual: CTypeDefinition | None = extract_type_def(_class)

        assert isinstance(actual, CClass)

    def test_struct(self, assembly: Assembly) -> None:
        """Tests for extract_type_def() with a struct."""
        name: str = "StructBasic"
        struct: TypeInfo = self.get_type(assembly, name)

        actual: CTypeDefinition | None = extract_type_def(struct)

        assert isinstance(actual, CClass)

    def test_record(self, assembly: Assembly) -> None:
        """Tests for extract_type_def() with a record."""
        name: str = "RecordBasic"
        record: TypeInfo = self.get_type(assembly, name)

        actual: CTypeDefinition | None = extract_type_def(record)

        assert isinstance(actual, CClass)

    def test_interface(self, assembly: Assembly) -> None:
        """Tests for extract_type_def() with an interface."""
        name: str = "IBasic"
        interface: TypeInfo = self.get_type(assembly, name)

        actual: CTypeDefinition | None = extract_type_def(interface)

        assert isinstance(actual, CClass)

    def test_enum(self, assembly: Assembly) -> None:
        """Tests for extract_type_def() with an enum."""
        name: str = "EnumBasic"
        enum: TypeInfo = self.get_type(assembly, name)

        actual: CTypeDefinition | None = extract_type_def(enum)

        assert isinstance(actual, CEnum)

    def test_delegate(self, assembly: Assembly) -> None:
        """Tests for extract_type_def() with a delegate."""
        name: str = "DelegateBasic"
        delegate: TypeInfo = self.get_type(assembly, name)

        actual: CTypeDefinition | None = extract_type_def(delegate)

        assert isinstance(actual, CDelegate)


class TestExtractClass(_Base):
    """Tests for extract_class()."""

    def test_basic(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a basic class."""
        name: str = "ClassBasic"
        _class: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        expected: CClass | None = self.basic_class(declaring_type)
        actual: CClass | None = extract_class(_class)

        assert actual == expected

    def test_abstract(self, assembly: Assembly) -> None:
        """Tests for extract_class() with an abstract class."""
        name: str = "ClassAbstract"
        _class: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        expected: CClass | None = replace(
            self.basic_class(declaring_type),
            abstract=True,
            constructors={},
        )
        actual: CClass | None = extract_class(_class)

        assert actual == expected

    def test_generic(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a generic class."""
        name: str = "ClassGeneric"
        _class: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(
            name=name,
            namespace=TEST_LIB,
            inner=[generic("TA"), generic("TB")],
        )

        expected: CClass | None = self.basic_class(declaring_type)
        actual: CClass | None = extract_class(_class)

        assert actual == expected

    def test_interfaces(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a class with interfaces."""
        name: str = "ClassInterfaces"
        _class: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        basic: CClass = self.basic_class(declaring_type)
        expected: CClass | None = replace(
            basic,
            interfaces=[replace(COMPARABLE, inner=[OBJECT]), replace(EQUATABLE, inner=[OBJECT])],
            methods={
                **basic.methods,
                "CompareTo(System:Object)": CMethod(
                    name="CompareTo",
                    declaring_type=COMPARABLE,
                    parameters=[CParameter(name="other", type=OBJECT)],
                    return_types=[INT32],
                ),
                "Equals(System:Object)": replace(
                    CMethod(
                        name="Equals",
                        declaring_type=EQUATABLE,
                        parameters=[CParameter(name="obj", type=OBJECT)],
                        return_types=[BOOLEAN],
                    ),
                ),
            },
        )
        actual: CClass | None = extract_class(_class)

        assert actual == expected

    def test_fields(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a class with fields."""
        name: str = "ClassFields"
        _class: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        expected: CClass | None = replace(
            self.basic_class(declaring_type),
            fields={
                "A": CField(name="A", declaring_type=declaring_type, return_type=INT32),
                "B": CField(name="B", declaring_type=declaring_type, return_type=INT32),
            },
        )
        actual: CClass | None = extract_class(_class)

        assert actual == expected

    def test_constructors(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a class with constructors."""
        name: str = "ClassConstructors"
        _class: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        basic: CClass = self.basic_class(declaring_type)
        expected: CClass | None = replace(
            basic,
            constructors={
                **basic.constructors,
                "__init__(System:Int32, System:Int32)": CConstructor(
                    declaring_type=declaring_type,
                    parameters=[
                        CParameter(name="param0", type=INT32),
                        CParameter(name="param1", type=INT32),
                    ],
                ),
            },
        )
        actual: CClass | None = extract_class(_class)

        assert actual == expected

    def test_properties(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a class with properties."""
        name: str = "ClassProperties"
        _class: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        expected: CClass | None = replace(
            self.basic_class(declaring_type),
            properties={
                "A": CProperty(name="A", declaring_type=declaring_type, type=INT32),
                "B": CProperty(name="B", declaring_type=declaring_type, type=INT32, setter=True),
            },
        )
        actual: CClass | None = extract_class(_class)

        assert actual == expected

    def test_methods(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a class with methods."""
        name: str = "ClassMethods"
        _class: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        basic: CClass = self.basic_class(declaring_type)
        expected: CClass | None = replace(
            basic,
            methods={
                **basic.methods,
                "A()": CMethod(name="A", declaring_type=declaring_type, return_types=[CType.VOID]),
                "B()": CMethod(name="B", declaring_type=declaring_type, return_types=[INT32]),
            },
        )
        actual: CClass | None = extract_class(_class)

        assert actual == expected

    def test_dunder_methods(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a class with dunder methods."""
        name: str = "ClassDunderMethods"
        _class: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        basic: CClass = self.basic_class(declaring_type)
        expected: CClass | None = replace(
            basic,
            methods={**basic.methods, **self.dunder_methods(declaring_type)},
        )
        actual: CClass | None = extract_class(_class)

        assert actual == expected

    def test_list_methods(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a class with list methods."""
        name: str = "ClassListMethods"
        _class: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        basic: CClass = self.basic_class(declaring_type)
        expected: CClass | None = replace(
            basic,
            interfaces=[
                CType(name="IEnumerable", namespace="System.Collections"),
                replace(COLLECTION, inner=[INT32]),
                replace(ENUMERABLE, inner=[INT32]),
                replace(LIST, inner=[INT32]),
            ],
            properties=self.list_properties(),
            methods={**basic.methods, **self.list_methods(INT32)},
        )
        actual: CClass | None = extract_class(_class)

        assert actual == expected

    def test_events(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a class with events."""
        name: str = "ClassEvents"
        _class: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        expected: CClass | None = replace(
            self.basic_class(declaring_type),
            events={
                "A": CEvent(name="A", declaring_type=declaring_type, type=EVENT_HANDLER),
                "B": CEvent(name="B", declaring_type=declaring_type, type=EVENT_HANDLER_ARGS),
            },
        )
        actual: CClass | None = extract_class(_class)

        assert actual == expected

    def test_nested(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a class with events."""
        name: str = "ClassNested"
        _class: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        expected: CClass | None = replace(
            self.basic_class(declaring_type),
            nested_types=self.nested_types(declaring_type),
        )
        actual: CClass | None = extract_class(_class)

        assert actual == expected


class TestExtractStruct(_Base):
    """Tests for extract_class() with structs."""

    def test_basic(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a basic struct."""
        name: str = "StructBasic"
        struct: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        expected: CClass | None = self.basic_struct(declaring_type)
        actual: CClass | None = extract_class(struct)

        assert actual == expected

    def test_generic(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a generic struct."""
        name: str = "StructGeneric"
        struct: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(
            name=name,
            namespace=TEST_LIB,
            inner=[generic("TA"), generic("TB")],
        )

        expected: CClass | None = self.basic_struct(declaring_type)
        actual: CClass | None = extract_class(struct)

        assert actual == expected

    def test_interfaces(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a struct with interfaces."""
        name: str = "StructInterfaces"
        struct: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        basic: CClass = self.basic_struct(declaring_type)
        expected: CClass | None = replace(
            basic,
            interfaces=[replace(COMPARABLE, inner=[OBJECT]), replace(EQUATABLE, inner=[OBJECT])],
            methods={
                **basic.methods,
                "CompareTo(System:Object)": CMethod(
                    name="CompareTo",
                    declaring_type=COMPARABLE,
                    parameters=[CParameter(name="other", type=OBJECT)],
                    return_types=[INT32],
                ),
                "Equals(System:Object)": CMethod(
                    name="Equals",
                    declaring_type=EQUATABLE,
                    parameters=[CParameter(name="obj", type=OBJECT)],
                    return_types=[BOOLEAN],
                ),
            },
        )
        actual: CClass | None = extract_class(struct)

        assert actual == expected

    def test_fields(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a struct with fields."""
        name: str = "StructFields"
        struct: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        expected: CClass | None = replace(
            self.basic_struct(declaring_type),
            constructors={"__init__()": CConstructor(declaring_type=declaring_type)},
            fields={
                "A": CField(name="A", declaring_type=declaring_type, return_type=INT32),
                "B": CField(name="B", declaring_type=declaring_type, return_type=INT32),
            },
        )
        actual: CClass | None = extract_class(struct)

        assert actual == expected

    def test_constructors(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a struct with constructors."""
        name: str = "StructConstructors"
        struct: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        expected: CClass | None = replace(
            self.basic_struct(declaring_type),
            constructors={
                "__init__()": CConstructor(declaring_type=declaring_type),
                "__init__(System:Int32, System:Int32)": CConstructor(
                    declaring_type=declaring_type,
                    parameters=[
                        CParameter(name="param0", type=INT32),
                        CParameter(name="param1", type=INT32),
                    ],
                ),
            },
        )
        actual: CClass | None = extract_class(struct)

        assert actual == expected

    def test_properties(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a struct with properties."""
        name: str = "StructProperties"
        struct: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        expected: CClass | None = replace(
            self.basic_struct(declaring_type),
            properties={
                "A": CProperty(name="A", declaring_type=declaring_type, type=INT32),
                "B": CProperty(name="B", declaring_type=declaring_type, type=INT32, setter=True),
            },
        )
        actual: CClass | None = extract_class(struct)

        assert actual == expected

    def test_methods(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a struct with methods."""
        name: str = "StructMethods"
        struct: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        basic: CClass = self.basic_struct(declaring_type)
        expected: CClass | None = replace(
            basic,
            methods={
                **basic.methods,
                "A()": CMethod(name="A", declaring_type=declaring_type, return_types=[CType.VOID]),
                "B()": CMethod(name="B", declaring_type=declaring_type, return_types=[INT32]),
            },
        )
        actual: CClass | None = extract_class(struct)

        assert actual == expected

    def test_dunder_methods(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a struct with dunder methods."""
        name: str = "StructDunderMethods"
        struct: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        basic: CClass = self.basic_struct(declaring_type)
        expected: CClass | None = replace(
            basic,
            methods={**basic.methods, **self.dunder_methods(declaring_type)},
        )
        actual: CClass | None = extract_class(struct)

        assert actual == expected

    def test_list_methods(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a struct with list methods."""
        name: str = "StructListMethods"
        struct: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        basic: CClass = self.basic_struct(declaring_type)
        expected: CClass | None = replace(
            basic,
            interfaces=[
                CType(name="IEnumerable", namespace="System.Collections"),
                replace(COLLECTION, inner=[INT32]),
                replace(ENUMERABLE, inner=[INT32]),
                replace(LIST, inner=[INT32]),
            ],
            properties=self.list_properties(),
            methods={**basic.methods, **self.list_methods(INT32)},
        )
        actual: CClass | None = extract_class(struct)

        assert actual == expected

    def test_events(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a struct with events."""
        name: str = "StructEvents"
        struct: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        expected: CClass | None = replace(
            self.basic_struct(declaring_type),
            events={
                "A": CEvent(name="A", declaring_type=declaring_type, type=EVENT_HANDLER),
                "B": CEvent(name="B", declaring_type=declaring_type, type=EVENT_HANDLER_ARGS),
            },
        )
        actual: CClass | None = extract_class(struct)

        assert actual == expected

    def test_nested(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a struct with events."""
        name: str = "StructNested"
        struct: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        expected: CClass | None = replace(
            self.basic_struct(declaring_type),
            nested_types=self.nested_types(declaring_type),
        )
        actual: CClass | None = extract_class(struct)

        assert actual == expected


class TestExtractRecord(_Base):
    """Tests for extract_class() with records."""

    def test_basic(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a basic record."""
        name: str = "RecordBasic"
        record: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        expected: CClass | None = self.basic_record(declaring_type)
        actual: CClass | None = extract_class(record)

        assert actual == expected

    def test_generic(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a generic record."""
        name: str = "RecordGeneric"
        record: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(
            name=name,
            namespace=TEST_LIB,
            inner=[generic("TA"), generic("TB")],
        )

        expected: CClass | None = self.basic_record(declaring_type)
        actual: CClass | None = extract_class(record)

        assert actual == expected

    def test_interfaces(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a record with interfaces."""
        name: str = "RecordInterfaces"
        record: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        basic: CClass = self.basic_record(declaring_type)
        expected: CClass | None = replace(
            basic,
            interfaces=[
                replace(COMPARABLE, inner=[OBJECT]),
                *basic.interfaces,
            ],
            methods={
                **basic.methods,
                "CompareTo(System:Object)": CMethod(
                    name="CompareTo",
                    declaring_type=COMPARABLE,
                    parameters=[CParameter(name="other", type=OBJECT)],
                    return_types=[INT32],
                ),
            },
        )
        actual: CClass | None = extract_class(record)

        assert actual == expected

    def test_fields(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a record with fields."""
        name: str = "RecordFields"
        record: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        expected: CClass | None = replace(
            self.basic_record(declaring_type),
            fields={
                "A": CField(name="A", declaring_type=declaring_type, return_type=INT32),
                "B": CField(name="B", declaring_type=declaring_type, return_type=INT32),
            },
        )
        actual: CClass | None = extract_class(record)

        assert actual == expected

    def test_constructors(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a record with constructors."""
        name: str = "RecordConstructors"
        record: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        basic: CClass = self.basic_record(declaring_type)
        expected: CClass | None = replace(
            basic,
            constructors={
                **basic.constructors,
                "__init__(System:Int32, System:Int32)": CConstructor(
                    declaring_type=declaring_type,
                    parameters=[
                        CParameter(name="param0", type=INT32),
                        CParameter(name="param1", type=INT32),
                    ],
                ),
            },
        )
        actual: CClass | None = extract_class(record)

        assert actual == expected

    def test_properties(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a record with properties."""
        name: str = "RecordProperties"
        record: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        expected: CClass | None = replace(
            self.basic_record(declaring_type),
            properties={
                "A": CProperty(name="A", declaring_type=declaring_type, type=INT32),
                "B": CProperty(name="B", declaring_type=declaring_type, type=INT32, setter=True),
            },
        )
        actual: CClass | None = extract_class(record)

        assert actual == expected

    def test_methods(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a record with methods."""
        name: str = "RecordMethods"
        record: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        basic: CClass = self.basic_record(declaring_type)
        expected: CClass | None = replace(
            basic,
            methods={
                **basic.methods,
                "A()": CMethod(name="A", declaring_type=declaring_type, return_types=[CType.VOID]),
                "B()": CMethod(name="B", declaring_type=declaring_type, return_types=[INT32]),
            },
        )
        actual: CClass | None = extract_class(record)

        assert actual == expected

    def test_dunder_methods(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a record with dunder methods."""
        name: str = "RecordDunderMethods"
        record: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        basic: CClass = self.basic_record(declaring_type)
        expected: CClass | None = replace(
            basic,
            methods={**basic.methods, **self.dunder_methods(declaring_type)},
        )
        actual: CClass | None = extract_class(record)

        assert actual == expected

    def test_list_methods(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a record with list methods."""
        name: str = "RecordListMethods"
        record: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        basic: CClass = self.basic_record(declaring_type)
        expected: CClass | None = replace(
            basic,
            interfaces=[
                *basic.interfaces,
                CType(name="IEnumerable", namespace="System.Collections"),
                replace(COLLECTION, inner=[INT32]),
                replace(ENUMERABLE, inner=[INT32]),
                replace(LIST, inner=[INT32]),
            ],
            properties=self.list_properties(),
            methods={**basic.methods, **self.list_methods(INT32)},
        )
        actual: CClass | None = extract_class(record)

        assert actual == expected

    def test_events(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a record with events."""
        name: str = "RecordEvents"
        record: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        expected: CClass | None = replace(
            self.basic_record(declaring_type),
            events={
                "A": CEvent(name="A", declaring_type=declaring_type, type=EVENT_HANDLER),
                "B": CEvent(name="B", declaring_type=declaring_type, type=EVENT_HANDLER_ARGS),
            },
        )
        actual: CClass | None = extract_class(record)

        assert actual == expected

    def test_nested(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a record with events."""
        name: str = "RecordNested"
        record: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        expected: CClass | None = replace(
            self.basic_record(declaring_type),
            nested_types=self.nested_types(declaring_type),
        )
        actual: CClass | None = extract_class(record)

        assert actual == expected


class TestExtractInterface(_Base):
    """Tests for extract_class() with interfaces."""

    def test_basic(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a basic interface."""
        name: str = "IBasic"
        interface: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        expected: CClass | None = self.basic_interface(declaring_type)
        actual: CClass | None = extract_class(interface)

        assert actual == expected

    def test_generic(self, assembly: Assembly) -> None:
        """Tests for extract_class() with a generic record."""
        name: str = "IGeneric"
        interface: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(
            name=name,
            namespace=TEST_LIB,
            inner=[generic("TA"), generic("TB")],
        )

        expected: CClass | None = self.basic_interface(declaring_type)
        actual: CClass | None = extract_class(interface)

        assert actual == expected

    def test_interfaces(self, assembly: Assembly) -> None:
        """Tests for extract_class() with an interface with interfaces."""
        name: str = "IInterfaces"
        interface: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        basic: CClass = self.basic_interface(declaring_type)
        expected: CClass | None = replace(
            basic,
            interfaces=[replace(COMPARABLE, inner=[OBJECT]), replace(EQUATABLE, inner=[OBJECT])],
            methods={
                **basic.methods,
                "CompareTo(System:Object)": CMethod(
                    name="CompareTo",
                    declaring_type=COMPARABLE,
                    parameters=[CParameter(name="other", type=OBJECT)],
                    return_types=[INT32],
                ),
                "Equals(System:Object)": replace(
                    CMethod(
                        name="Equals",
                        declaring_type=EQUATABLE,
                        parameters=[CParameter(name="other", type=OBJECT)],
                        return_types=[BOOLEAN],
                    ),
                ),
            },
        )
        actual: CClass | None = extract_class(interface)

        assert actual == expected

    def test_fields(self, assembly: Assembly) -> None:
        """Tests for extract_class() with an interface with fields."""
        name: str = "IFields"
        interface: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        expected: CClass | None = replace(
            self.basic_interface(declaring_type),
            fields={
                "A": CField(
                    name="A",
                    declaring_type=declaring_type,
                    return_type=INT32,
                    static=True,
                ),
                "B": CField(
                    name="B",
                    declaring_type=declaring_type,
                    return_type=INT32,
                    static=True,
                ),
            },
        )
        actual: CClass | None = extract_class(interface)

        assert actual == expected

    def test_properties(self, assembly: Assembly) -> None:
        """Tests for extract_class() with an interface with properties."""
        name: str = "IProperties"
        interface: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        expected: CClass | None = replace(
            self.basic_interface(declaring_type),
            properties={
                "A": CProperty(name="A", declaring_type=declaring_type, type=INT32),
                "B": CProperty(name="B", declaring_type=declaring_type, type=INT32, setter=True),
            },
        )
        actual: CClass | None = extract_class(interface)

        assert actual == expected

    def test_methods(self, assembly: Assembly) -> None:
        """Tests for extract_class() with an interface with methods."""
        name: str = "IMethods"
        interface: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        basic: CClass = self.basic_interface(declaring_type)
        expected: CClass | None = replace(
            basic,
            methods={
                **basic.methods,
                "A()": CMethod(name="A", declaring_type=declaring_type, return_types=[CType.VOID]),
                "B()": CMethod(name="B", declaring_type=declaring_type, return_types=[INT32]),
            },
        )
        actual: CClass | None = extract_class(interface)

        assert actual == expected

    def test_dunder_methods(self, assembly: Assembly) -> None:
        """Tests for extract_class() with an interface with dunder methods."""
        name: str = "IDunderMethods"
        interface: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        basic: CClass = self.basic_interface(declaring_type)
        methods: dict[str, CMethod] = {**basic.methods, **self.dunder_methods(declaring_type)}
        del methods[f"op_Equality({declaring_type.full_name}, {declaring_type.full_name})"]
        del methods[f"op_Inequality({declaring_type.full_name}, {declaring_type.full_name})"]
        del methods[f"__eq__({declaring_type.full_name})"]
        del methods[f"__ne__({declaring_type.full_name})"]
        expected: CClass | None = replace(basic, methods=methods)
        actual: CClass | None = extract_class(interface)

        assert actual == expected

    def test_list_methods(self, assembly: Assembly) -> None:
        """Tests for extract_class() with an interface with list methods."""
        name: str = "IListMethods"
        interface: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        basic: CClass = self.basic_interface(declaring_type)
        expected: CClass | None = replace(
            basic,
            interfaces=[
                CType(name="IEnumerable", namespace="System.Collections"),
                replace(COLLECTION, inner=[INT32]),
                replace(ENUMERABLE, inner=[INT32]),
                replace(LIST, inner=[INT32]),
            ],
            properties=self.list_properties(),
            methods={**basic.methods, **self.list_methods(INT32)},
        )
        actual: CClass | None = extract_class(interface)

        assert actual == expected

    def test_events(self, assembly: Assembly) -> None:
        """Tests for extract_class() with an interface with events."""
        name: str = "IEvents"
        interface: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        expected: CClass | None = replace(
            self.basic_interface(declaring_type),
            events={
                "A": CEvent(name="A", declaring_type=declaring_type, type=EVENT_HANDLER),
                "B": CEvent(name="B", declaring_type=declaring_type, type=EVENT_HANDLER_ARGS),
            },
        )
        actual: CClass | None = extract_class(interface)

        assert actual == expected

    def test_nested(self, assembly: Assembly) -> None:
        """Tests for extract_class() with an interface with events."""
        name: str = "INested"
        interface: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        expected: CClass | None = replace(
            self.basic_interface(declaring_type),
            nested_types=self.nested_types(declaring_type),
        )
        actual: CClass | None = extract_class(interface)

        assert actual == expected


class TestExtractEnum(_Base):
    """Tests for extract_enum()."""

    def test_basic(self, assembly: Assembly) -> None:
        """Tests for extract_enum() with a basic enum."""
        name: str = "EnumBasic"
        enum: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        expected: CEnum | None = self.basic_enum(declaring_type)
        actual: CEnum | None = extract_enum(enum)

        assert actual == expected

    def test_fields(self, assembly: Assembly) -> None:
        """Tests for extract_enum() with an enum with fields."""
        name: str = "EnumFields"
        enum: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        expected: CEnum | None = replace(
            self.basic_enum(declaring_type),
            fields=["Field0", "Field1", "Field2", "Field3"],
        )
        actual: CEnum | None = extract_enum(enum)

        assert actual == expected


class TestExtractDelegate(_Base):
    """Tests for extract_delegate()."""

    def test_basic(self, assembly: Assembly) -> None:
        """Tests for extract_delegate() with a basic delegate."""
        name: str = "DelegateBasic"
        delegate: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        expected: CDelegate | None = self.basic_delegate(declaring_type)
        actual: CDelegate | None = extract_delegate(delegate)

        assert actual == expected

    def test_parameters(self, assembly: Assembly) -> None:
        """Tests for extract_delegate() with a delegate with parameters."""
        name: str = "DelegateParameters"
        delegate: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        expected: CDelegate | None = replace(
            self.basic_delegate(declaring_type),
            parameters=[
                CParameter(name="param0", type=INT32),
                CParameter(name="param1", type=INT32),
            ],
        )
        actual: CDelegate | None = extract_delegate(delegate)

        assert actual == expected

    def test_return(self, assembly: Assembly) -> None:
        """Tests for extract_delegate() with a delegate with a return."""
        name: str = "DelegateReturn"
        delegate: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        expected: CDelegate | None = replace(
            self.basic_delegate(declaring_type),
            return_type=INT32,
        )
        actual: CDelegate | None = extract_delegate(delegate)

        assert actual == expected

    def test_generic(self, assembly: Assembly) -> None:
        """Tests for extract_delegate() with a delegate with generic parameters."""
        name: str = "DelegateGeneric"
        delegate: TypeInfo = self.get_type(assembly, name)
        declaring_type: CType = CType(name=name, namespace=TEST_LIB)

        expected: CDelegate | None = replace(
            self.basic_delegate(declaring_type),
            parameters=[
                CParameter(name="param0", type=generic("T0")),
                CParameter(name="param1", type=generic("T1")),
            ],
            return_type=generic("T"),
        )
        actual: CDelegate | None = extract_delegate(delegate)

        assert actual == expected


class TestExtractAssembly:
    """Tests for extract_assemblies()."""

    def test_test_lib(self, output_dir: Path) -> None:
        """Test for extract_assemblies() with TestLib."""
        extract_assemblies([TEST_LIB], output_dir=output_dir, threads=0)

        skeleton_file: Path = output_dir / TL_SKELETON
        doc_file: Path = output_dir / TL_DOC

        assert skeleton_file.exists()
        assert doc_file.exists()


if __name__ == "__main__":
    pytest.main()
