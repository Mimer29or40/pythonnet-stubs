"""Tests for stubgen.build_stubs.py."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from conftest import make_params

from stubgen.build_stubs import build_class
from stubgen.build_stubs import build_constructor
from stubgen.build_stubs import build_delegate
from stubgen.build_stubs import build_enum
from stubgen.build_stubs import build_event
from stubgen.build_stubs import build_field
from stubgen.build_stubs import build_interface
from stubgen.build_stubs import build_method
from stubgen.build_stubs import build_namespace
from stubgen.build_stubs import build_parameter
from stubgen.build_stubs import build_property
from stubgen.build_stubs import build_struct
from stubgen.build_stubs import build_type
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
from stubgen.model import DocNode
from stubgen.model import ImportList

if TYPE_CHECKING:  # pragma: no cover
    from collections.abc import Sequence


@pytest.fixture
def doc() -> DocNode:
    """DocNode fixture."""
    return DocNode(name="Test")


@pytest.fixture
def imports() -> ImportList:
    """ImportList fixture."""
    return ImportList()


@pytest.fixture
def line_length() -> int:
    """Line length fixture."""
    return 100


# class TestMergeParameter:
#     def test_merge(self) -> None:
#         parameter1: CParameter = CParameter(name="param0", type=CType(name="ParamType"))
#         parameter2: CParameter = CParameter(name="param0", type=CType(name="ParamType"))
#
#         result: CParameter = merge_parameter(parameter1, parameter2)
#         expected: CParameter = CParameter(name="param0", type=CType(name="ParamType"))
#
#         self.assertEqual(expected, result)
#
#     def test_merge_names(self) -> None:
#         parameter1: CParameter = CParameter(name="param0", type=CType(name="ParamType"))
#         parameter2: CParameter = CParameter(name="paramA", type=CType(name="ParamType"))
#
#         result: CParameter = merge_parameter(parameter1, parameter2)
#         expected: CParameter = CParameter(name="param0", type=CType(name="ParamType"))
#
#         self.assertEqual(expected, result)
#
#     def test_merge_error_type(self) -> None:
#         parameter1: CParameter = CParameter(name="param0", type=CType(name="ParamTypeA"))
#         parameter2: CParameter = CParameter(name="param0", type=CType(name="ParamTypeB"))
#
#         self.assertRaises(AttributeError, lambda: merge_parameter(parameter1, parameter2))
#
#     def test_merge_error_default(self) -> None:
#         parameter1: CParameter = CParameter(
#             name="param0",
#             type=CType(name="ParamTypeA"),
#         )
#         parameter2: CParameter = CParameter(
#             name="param0",
#             type=CType(name="ParamTypeB"),
#             default=True,
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_parameter(parameter1, parameter2))
#
#     def test_merge_error_out(self) -> None:
#         parameter1: CParameter = CParameter(
#             name="param0",
#             type=CType(name="ParamTypeA"),
#         )
#         parameter2: CParameter = CParameter(
#             name="param0",
#             type=CType(name="ParamTypeB"),
#             out=True,
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_parameter(parameter1, parameter2))
#
#
# class TestMergeParameters:
#     def test_merge(self) -> None:
#         parameters1: Sequence[CParameter] = (
#             CParameter(name="param0", type=CType(name="ParamType")),
#             CParameter(name="param1", type=CType(name="ParamType")),
#         )
#         parameters2: Sequence[CParameter] = (
#             CParameter(name="param0", type=CType(name="ParamType")),
#             CParameter(name="param1", type=CType(name="ParamType")),
#         )
#
#         result: Sequence[CParameter] = merge_parameters(parameters1, parameters2)
#         expected: Sequence[CParameter] = (
#             CParameter(name="param0", type=CType(name="ParamType")),
#             CParameter(name="param1", type=CType(name="ParamType")),
#         )
#
#         self.assertEqual(expected, result)
#
#     def test_merge_names(self) -> None:
#         parameters1: Sequence[CParameter] = (
#             CParameter(name="param0", type=CType(name="ParamType")),
#             CParameter(name="param1", type=CType(name="ParamType")),
#         )
#         parameters2: Sequence[CParameter] = (
#             CParameter(name="paramA", type=CType(name="ParamType")),
#             CParameter(name="paramB", type=CType(name="ParamType")),
#         )
#
#         result: Sequence[CParameter] = merge_parameters(parameters1, parameters2)
#         expected: Sequence[CParameter] = (
#             CParameter(name="param0", type=CType(name="ParamType")),
#             CParameter(name="param1", type=CType(name="ParamType")),
#         )
#
#         self.assertEqual(expected, result)
#
#     def test_merge_error_len(self) -> None:
#         parameters1: Sequence[CParameter] = (
#             CParameter(name="param0", type=CType(name="ParamType")),
#             CParameter(name="param1", type=CType(name="ParamType")),
#         )
#         parameters2: Sequence[CParameter] = (
#             CParameter(name="param0", type=CType(name="ParamType")),
#             CParameter(name="param1", type=CType(name="ParamType")),
#             CParameter(name="param2", type=CType(name="ParamType")),
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_parameters(parameters1, parameters2))
#
#
# class TestMergeField:
#     def test_merge(self) -> None:
#         field1: CField = CField(
#             name="Field",
#             declaring_type=CType(name="DeclaringType"),
#             return_type=CType(name="ReturnType"),
#         )
#         field2: CField = CField(
#             name="Field",
#             declaring_type=CType(name="DeclaringType"),
#             return_type=CType(name="ReturnType"),
#         )
#
#         result: CField = merge_field(field1, field2)
#         expected: CField = CField(
#             name="Field",
#             declaring_type=CType(name="DeclaringType"),
#             return_type=CType(name="ReturnType"),
#         )
#
#         self.assertEqual(expected, result)
#
#     def test_merge_error_name(self) -> None:
#         field1: CField = CField(
#             name="FieldA",
#             declaring_type=CType(name="DeclaringType"),
#             return_type=CType(name="ReturnType"),
#         )
#         field2: CField = CField(
#             name="FieldB",
#             declaring_type=CType(name="DeclaringType"),
#             return_type=CType(name="ReturnType"),
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_field(field1, field2))
#
#     def test_merge_error_declaring_type(self) -> None:
#         field1: CField = CField(
#             name="Field",
#             declaring_type=CType(name="DeclaringTypeA"),
#             return_type=CType(name="ReturnType"),
#         )
#         field2: CField = CField(
#             name="Field",
#             declaring_type=CType(name="DeclaringTypeB"),
#             return_type=CType(name="ReturnType"),
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_field(field1, field2))
#
#     def test_merge_error_return_type(self) -> None:
#         field1: CField = CField(
#             name="Field",
#             declaring_type=CType(name="DeclaringType"),
#             return_type=CType(name="ReturnTypeA"),
#         )
#         field2: CField = CField(
#             name="Field",
#             declaring_type=CType(name="DeclaringType"),
#             return_type=CType(name="ReturnTypeB"),
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_field(field1, field2))
#
#     def test_merge_error_static(self) -> None:
#         field1: CField = CField(
#             name="Field",
#             declaring_type=CType(name="DeclaringType"),
#             return_type=CType(name="ReturnType"),
#         )
#         field2: CField = CField(
#             name="Field",
#             declaring_type=CType(name="DeclaringType"),
#             return_type=CType(name="ReturnType"),
#             static=True,
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_field(field1, field2))
#
#
# class TestMergeConstructor:
#     def test_merge(self) -> None:
#         constructor1: CConstructor = CConstructor(
#             declaring_type=CType(name="DeclaringType"),
#             parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#         )
#         constructor2: CConstructor = CConstructor(
#             declaring_type=CType(name="DeclaringType"),
#             parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#         )
#
#         result: CConstructor = merge_constructor(constructor1, constructor2)
#         expected: CConstructor = CConstructor(
#             declaring_type=CType(name="DeclaringType"),
#             parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#         )
#
#         self.assertEqual(expected, result)
#
#     def test_merge_error_declaring_type(self) -> None:
#         constructor1: CConstructor = CConstructor(
#             declaring_type=CType(name="DeclaringTypeA"),
#             parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#         )
#         constructor2: CConstructor = CConstructor(
#             declaring_type=CType(name="DeclaringTypeB"),
#             parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_constructor(constructor1, constructor2))
#
#     def test_merge_error_parameters(self) -> None:
#         constructor1: CConstructor = CConstructor(
#             declaring_type=CType(name="DeclaringType"),
#             parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#         )
#         constructor2: CConstructor = CConstructor(
#             declaring_type=CType(name="DeclaringType"),
#             parameters=(
#                 CParameter(name="param0", type=CType(name="ParamType")),
#                 CParameter(name="param1", type=CType(name="ParamType")),
#             ),
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_constructor(constructor1, constructor2))
#
#
# class TestMergeProperty:
#     def test_merge(self) -> None:
#         property1: CProperty = CProperty(
#             name="Property",
#             declaring_type=CType(name="DeclaringType"),
#             type=CType(name="Type"),
#         )
#         property2: CProperty = CProperty(
#             name="Property",
#             declaring_type=CType(name="DeclaringType"),
#             type=CType(name="Type"),
#         )
#
#         result: CProperty = merge_property(property1, property2)
#         expected: CProperty = CProperty(
#             name="Property",
#             declaring_type=CType(name="DeclaringType"),
#             type=CType(name="Type"),
#         )
#
#         self.assertEqual(expected, result)
#
#     def test_merge_setter(self) -> None:
#         property1: CProperty = CProperty(
#             name="Property",
#             declaring_type=CType(name="DeclaringType"),
#             type=CType(name="Type"),
#         )
#         property2: CProperty = CProperty(
#             name="Property",
#             declaring_type=CType(name="DeclaringType"),
#             type=CType(name="Type"),
#             setter=True,
#         )
#
#         result: CProperty = merge_property(property1, property2)
#         expected: CProperty = CProperty(
#             name="Property",
#             declaring_type=CType(name="DeclaringType"),
#             type=CType(name="Type"),
#             setter=True,
#         )
#
#         self.assertEqual(expected, result)
#
#     def test_merge_error_name(self) -> None:
#         property1: CProperty = CProperty(
#             name="PropertyA",
#             declaring_type=CType(name="DeclaringType"),
#             type=CType(name="Type"),
#         )
#         property2: CProperty = CProperty(
#             name="PropertyB",
#             declaring_type=CType(name="DeclaringType"),
#             type=CType(name="Type"),
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_property(property1, property2))
#
#     def test_merge_error_declaring_type(self) -> None:
#         property1: CProperty = CProperty(
#             name="Property",
#             declaring_type=CType(name="DeclaringTypeA"),
#             type=CType(name="Type"),
#         )
#         property2: CProperty = CProperty(
#             name="Property",
#             declaring_type=CType(name="DeclaringTypeB"),
#             type=CType(name="Type"),
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_property(property1, property2))
#
#     def test_merge_error_type(self) -> None:
#         property1: CProperty = CProperty(
#             name="Property",
#             declaring_type=CType(name="DeclaringType"),
#             type=CType(name="TypeA"),
#         )
#         property2: CProperty = CProperty(
#             name="Property",
#             declaring_type=CType(name="DeclaringType"),
#             type=CType(name="TypeB"),
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_property(property1, property2))
#
#     def test_merge_error_static(self) -> None:
#         property1: CProperty = CProperty(
#             name="Property",
#             declaring_type=CType(name="DeclaringType"),
#             type=CType(name="Type"),
#         )
#         property2: CProperty = CProperty(
#             name="Property",
#             declaring_type=CType(name="DeclaringType"),
#             type=CType(name="Type"),
#             static=True,
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_property(property1, property2))
#
#
# class TestMergeMethod:
#     def test_merge(self) -> None:
#         method1: CMethod = CMethod(
#             name="Method",
#             declaring_type=CType(name="DeclaringType"),
#             parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#             return_types=(CType(name="ReturnType"),),
#         )
#         method2: CMethod = CMethod(
#             name="Method",
#             declaring_type=CType(name="DeclaringType"),
#             parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#             return_types=(CType(name="ReturnType"),),
#         )
#
#         result: CMethod = merge_method(method1, method2)
#         expected: CMethod = CMethod(
#             name="Method",
#             declaring_type=CType(name="DeclaringType"),
#             parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#             return_types=(CType(name="ReturnType"),),
#         )
#
#         self.assertEqual(expected, result)
#
#     def test_merge_error_name(self) -> None:
#         method1: CMethod = CMethod(
#             name="MethodA",
#             declaring_type=CType(name="DeclaringType"),
#             parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#             return_types=(CType(name="ReturnType"),),
#         )
#         method2: CMethod = CMethod(
#             name="MethodB",
#             declaring_type=CType(name="DeclaringType"),
#             parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#             return_types=(CType(name="ReturnType"),),
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_method(method1, method2))
#
#     def test_merge_error_declaring_type(self) -> None:
#         method1: CMethod = CMethod(
#             name="Method",
#             declaring_type=CType(name="DeclaringTypeA"),
#             parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#             return_types=(CType(name="ReturnType"),),
#         )
#         method2: CMethod = CMethod(
#             name="Method",
#             declaring_type=CType(name="DeclaringTypeB"),
#             parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#             return_types=(CType(name="ReturnType"),),
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_method(method1, method2))
#
#     def test_merge_error_parameters(self) -> None:
#         method1: CMethod = CMethod(
#             name="Method",
#             declaring_type=CType(name="DeclaringType"),
#             parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#             return_types=(CType(name="ReturnTypeA"),),
#         )
#         method2: CMethod = CMethod(
#             name="Method",
#             declaring_type=CType(name="DeclaringType"),
#             parameters=(
#                 CParameter(name="param0", type=CType(name="ParamType")),
#                 CParameter(name="param1", type=CType(name="ParamType")),
#             ),
#             return_types=(CType(name="ReturnTypeB"),),
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_method(method1, method2))
#
#     def test_merge_error_return_types(self) -> None:
#         method1: CMethod = CMethod(
#             name="Method",
#             declaring_type=CType(name="DeclaringType"),
#             parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#             return_types=(CType(name="ReturnTypeA"),),
#         )
#         method2: CMethod = CMethod(
#             name="Method",
#             declaring_type=CType(name="DeclaringType"),
#             parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#             return_types=(CType(name="ReturnTypeB"),),
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_method(method1, method2))
#
#     def test_merge_error_static(self) -> None:
#         method1: CMethod = CMethod(
#             name="Method",
#             declaring_type=CType(name="DeclaringType"),
#             parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#             return_types=(CType(name="ReturnTypeA"),),
#         )
#         method2: CMethod = CMethod(
#             name="Method",
#             declaring_type=CType(name="DeclaringType"),
#             parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#             return_types=(CType(name="ReturnTypeB"),),
#             static=True,
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_method(method1, method2))
#
#
# class TestMergeEvent:
#     def test_merge(self) -> None:
#         event1: CEvent = CEvent(
#             name="Event",
#             declaring_type=CType(name="DeclaringType"),
#             type=CType(name="Type"),
#         )
#         event2: CEvent = CEvent(
#             name="Event",
#             declaring_type=CType(name="DeclaringType"),
#             type=CType(name="Type"),
#         )
#
#         result: CEvent = merge_event(event1, event2)
#         expected: CEvent = CEvent(
#             name="Event",
#             declaring_type=CType(name="DeclaringType"),
#             type=CType(name="Type"),
#         )
#
#         self.assertEqual(expected, result)
#
#     def test_merge_error_name(self) -> None:
#         event1: CEvent = CEvent(
#             name="EventA",
#             declaring_type=CType(name="DeclaringType"),
#             type=CType(name="Type"),
#         )
#         event2: CEvent = CEvent(
#             name="EventB",
#             declaring_type=CType(name="DeclaringType"),
#             type=CType(name="Type"),
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_event(event1, event2))
#
#     def test_merge_error_declaring_type(self) -> None:
#         event1: CEvent = CEvent(
#             name="Event",
#             declaring_type=CType(name="DeclaringTypeA"),
#             type=CType(name="Type"),
#         )
#         event2: CEvent = CEvent(
#             name="Event",
#             declaring_type=CType(name="DeclaringTypeB"),
#             type=CType(name="Type"),
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_event(event1, event2))
#
#     def test_merge_error_type(self) -> None:
#         event1: CEvent = CEvent(
#             name="Event",
#             declaring_type=CType(name="DeclaringType"),
#             type=CType(name="TypeA"),
#         )
#         event2: CEvent = CEvent(
#             name="Event",
#             declaring_type=CType(name="DeclaringType"),
#             type=CType(name="TypeB"),
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_event(event1, event2))
#
#
# class TestMergeNamespace:
#     def test_merge(self) -> None:
#         namespace1: CNamespace = CNamespace(
#             name="Namespace",
#             types={},
#         )
#         namespace2: CNamespace = CNamespace(
#             name="Namespace",
#             types={},
#         )
#
#         merged: CNamespace = merge_namespace(namespace1, namespace2)
#         expected: CNamespace = CNamespace(
#             name="Namespace",
#             types={},
#         )
#
#         self.assertEqual(expected, merged)
#
#     def test_merge_types(self) -> None:
#         namespace1: CNamespace = CNamespace(
#             name="Namespace",
#             types={
#                 "Namespace:ClassA": CClass(
#                     name="ClassA",
#                     namespace="Namespace",
#                     nested=None,
#                     abstract=False,
#                     generic_args=(),
#                     super_class=None,
#                     interfaces=(),
#                     fields={},
#                     constructors={},
#                     properties={},
#                     methods={},
#                     events={},
#                     nested_types={},
#                 ),
#                 "Namespace:ClassB": CClass(
#                     name="ClassB",
#                     namespace="Namespace",
#                     nested=None,
#                     abstract=False,
#                     generic_args=(),
#                     super_class=None,
#                     interfaces=(),
#                     fields={},
#                     constructors={},
#                     properties={},
#                     methods={},
#                     events={},
#                     nested_types={},
#                 ),
#             },
#         )
#         namespace2: CNamespace = CNamespace(
#             name="Namespace",
#             types={
#                 "Namespace:ClassA": CClass(
#                     name="ClassA",
#                     namespace="Namespace",
#                     nested=None,
#                     abstract=False,
#                     generic_args=(),
#                     super_class=None,
#                     interfaces=(),
#                     fields={},
#                     constructors={},
#                     properties={},
#                     methods={},
#                     events={},
#                     nested_types={},
#                 ),
#                 "Namespace:ClassC": CClass(
#                     name="ClassC",
#                     namespace="Namespace",
#                     nested=None,
#                     abstract=False,
#                     generic_args=(),
#                     super_class=None,
#                     interfaces=(),
#                     fields={},
#                     constructors={},
#                     properties={},
#                     methods={},
#                     events={},
#                     nested_types={},
#                 ),
#             },
#         )
#
#         merged: CNamespace = merge_namespace(namespace1, namespace2)
#         expected: CNamespace = CNamespace(
#             name="Namespace",
#             types={
#                 "Namespace:ClassA": CClass(
#                     name="ClassA",
#                     namespace="Namespace",
#                     nested=None,
#                     abstract=False,
#                     generic_args=(),
#                     super_class=None,
#                     interfaces=(),
#                     fields={},
#                     constructors={},
#                     properties={},
#                     methods={},
#                     events={},
#                     nested_types={},
#                 ),
#                 "Namespace:ClassB": CClass(
#                     name="ClassB",
#                     namespace="Namespace",
#                     nested=None,
#                     abstract=False,
#                     generic_args=(),
#                     super_class=None,
#                     interfaces=(),
#                     fields={},
#                     constructors={},
#                     properties={},
#                     methods={},
#                     events={},
#                     nested_types={},
#                 ),
#                 "Namespace:ClassC": CClass(
#                     name="ClassC",
#                     namespace="Namespace",
#                     nested=None,
#                     abstract=False,
#                     generic_args=(),
#                     super_class=None,
#                     interfaces=(),
#                     fields={},
#                     constructors={},
#                     properties={},
#                     methods={},
#                     events={},
#                     nested_types={},
#                 ),
#             },
#         )
#
#         self.assertEqual(expected, merged)
#
#     def test_merge_error_name(self) -> None:
#         namespace1: CNamespace = CNamespace(name="NamespaceA", types={})
#         namespace2: CNamespace = CNamespace(name="NamespaceB", types={})
#
#         self.assertRaises(AttributeError, lambda: merge_namespace(namespace1, namespace2))
#
#
# class TestMergeTypeDefinition:
#     def test_merge_error_type(self) -> None:
#         type_def1: CTypeDefinition = CClass(
#             name="Class",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#         type_def2: CTypeDefinition = CStruct(
#             name="Struct",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         self.assertRaises(TypeError, lambda: merge_type_def(type_def1, type_def2))
#
#     def test_merge_error_name(self) -> None:
#         type_def1: CTypeDefinition = CClass(
#             name="ClassA",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#         type_def2: CTypeDefinition = CClass(
#             name="ClassB",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_type_def(type_def1, type_def2))
#
#     def test_merge_error_namespace(self) -> None:
#         type_def1: CTypeDefinition = CClass(
#             name="Class",
#             namespace="NamespaceA",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#         type_def2: CTypeDefinition = CClass(
#             name="Class",
#             namespace="NamespaceB",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_type_def(type_def1, type_def2))
#
#     def test_merge_error_nested(self) -> None:
#         type_def1: CTypeDefinition = CClass(
#             name="Class",
#             namespace="Namespace",
#             nested=CType(name="TypeA"),
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#         type_def2: CTypeDefinition = CClass(
#             name="Class",
#             namespace="Namespace",
#             nested=CType(name="TypeB"),
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_type_def(type_def1, type_def2))
#
#
# class TestMergeClass:
#     def test_merge_interfaces(self) -> None:
#         class1: CClass = CClass(
#             name="Class",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(
#                 CType(name="InterfaceA", namespace="Namespace"),
#                 CType(name="InterfaceB", namespace="Namespace"),
#             ),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#         class2: CClass = CClass(
#             name="Class",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(
#                 CType(name="InterfaceA", namespace="Namespace"),
#                 CType(name="InterfaceC", namespace="Namespace"),
#             ),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         result: CTypeDefinition = merge_class(class1, class2)
#         expected: CClass = CClass(
#             name="Class",
#             namespace="Namespace",
#             nested=None,
#             abstract=True,
#             generic_args=(),
#             super_class=None,
#             interfaces=(
#                 CType(name="InterfaceA", namespace="Namespace"),
#                 CType(name="InterfaceB", namespace="Namespace"),
#                 CType(name="InterfaceC", namespace="Namespace"),
#             ),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         self.assertEqual(expected, result)
#
#     def test_merge_fields(self) -> None:
#         class1: CClass = CClass(
#             name="Class",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={
#                 "Namespace.Class.FieldA": CField(
#                     name="FieldA",
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     return_type=CType(name="ReturnType"),
#                 ),
#                 "Namespace.Class.FieldB": CField(
#                     name="FieldB",
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     return_type=CType(name="ReturnType"),
#                 ),
#             },
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#         class2: CClass = CClass(
#             name="Class",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={
#                 "Namespace.Class.FieldA": CField(
#                     name="FieldA",
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     return_type=CType(name="ReturnType"),
#                 ),
#                 "Namespace.Class.FieldC": CField(
#                     name="FieldC",
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     return_type=CType(name="ReturnType"),
#                 ),
#             },
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         result: CTypeDefinition = merge_class(class1, class2)
#         expected: CClass = CClass(
#             name="Class",
#             namespace="Namespace",
#             nested=None,
#             abstract=True,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={
#                 "Namespace.Class.FieldA": CField(
#                     name="FieldA",
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     return_type=CType(name="ReturnType"),
#                 ),
#                 "Namespace.Class.FieldB": CField(
#                     name="FieldB",
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     return_type=CType(name="ReturnType"),
#                 ),
#                 "Namespace.Class.FieldC": CField(
#                     name="FieldC",
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     return_type=CType(name="ReturnType"),
#                 ),
#             },
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         self.assertEqual(expected, result)
#
#     def test_merge_constructors(self) -> None:
#         class1: CClass = CClass(
#             name="Class",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={
#                 "Namespace.Class.__init__()": CConstructor(
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     parameters=(),
#                 ),
#                 "Namespace.Class.__init__(ParamType)": CConstructor(
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#                 ),
#             },
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#         class2: CClass = CClass(
#             name="Class",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={
#                 "Namespace.Class.__init__()": CConstructor(
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     parameters=(),
#                 ),
#                 "Namespace.Class.__init__(ParamType, ParamType)": CConstructor(
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     parameters=(
#                         CParameter(name="param0", type=CType(name="ParamType")),
#                         CParameter(name="param1", type=CType(name="ParamType")),
#                     ),
#                 ),
#             },
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         result: CTypeDefinition = merge_class(class1, class2)
#         expected: CClass = CClass(
#             name="Class",
#             namespace="Namespace",
#             nested=None,
#             abstract=True,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={
#                 "Namespace.Class.__init__()": CConstructor(
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     parameters=(),
#                 ),
#                 "Namespace.Class.__init__(ParamType)": CConstructor(
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#                 ),
#                 "Namespace.Class.__init__(ParamType, ParamType)": CConstructor(
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     parameters=(
#                         CParameter(name="param0", type=CType(name="ParamType")),
#                         CParameter(name="param1", type=CType(name="ParamType")),
#                     ),
#                 ),
#             },
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         self.assertEqual(expected, result)
#
#     def test_merge_properties(self) -> None:
#         class1: CClass = CClass(
#             name="Class",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={
#                 "Namespace.Class.PropertyA": CProperty(
#                     name="PropertyA",
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     type=CType(name="PropertyType"),
#                 ),
#                 "Namespace.Class.PropertyB": CProperty(
#                     name="PropertyB",
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     type=CType(name="PropertyType"),
#                 ),
#             },
#             methods={},
#             events={},
#             nested_types={},
#         )
#         class2: CClass = CClass(
#             name="Class",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={
#                 "Namespace.Class.PropertyA": CProperty(
#                     name="PropertyA",
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     type=CType(name="PropertyType"),
#                 ),
#                 "Namespace.Class.PropertyC": CProperty(
#                     name="PropertyC",
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     type=CType(name="PropertyType"),
#                 ),
#             },
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         result: CTypeDefinition = merge_class(class1, class2)
#         expected: CClass = CClass(
#             name="Class",
#             namespace="Namespace",
#             nested=None,
#             abstract=True,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={
#                 "Namespace.Class.PropertyA": CProperty(
#                     name="PropertyA",
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     type=CType(name="PropertyType"),
#                 ),
#                 "Namespace.Class.PropertyB": CProperty(
#                     name="PropertyB",
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     type=CType(name="PropertyType"),
#                 ),
#                 "Namespace.Class.PropertyC": CProperty(
#                     name="PropertyC",
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     type=CType(name="PropertyType"),
#                 ),
#             },
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         self.assertEqual(expected, result)
#
#     def test_merge_methods(self) -> None:
#         class1: CClass = CClass(
#             name="Class",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={
#                 "Namespace.Class.MethodA(ParamType)": CMethod(
#                     name="MethodA",
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#                     return_types=(CType(name="PropertyType"),),
#                 ),
#                 "Namespace.Class.MethodB(ParamType)": CMethod(
#                     name="MethodB",
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#                     return_types=(CType(name="PropertyType"),),
#                 ),
#             },
#             events={},
#             nested_types={},
#         )
#         class2: CClass = CClass(
#             name="Class",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={
#                 "Namespace.Class.MethodA(ParamType)": CMethod(
#                     name="MethodA",
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#                     return_types=(CType(name="PropertyType"),),
#                 ),
#                 "Namespace.Class.MethodC(ParamType)": CMethod(
#                     name="MethodC",
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#                     return_types=(CType(name="PropertyType"),),
#                 ),
#             },
#             events={},
#             nested_types={},
#         )
#
#         result: CTypeDefinition = merge_class(class1, class2)
#         expected: CClass = CClass(
#             name="Class",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={
#                 "Namespace.Class.MethodA(ParamType)": CMethod(
#                     name="MethodA",
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#                     return_types=(CType(name="PropertyType"),),
#                 ),
#                 "Namespace.Class.MethodB(ParamType)": CMethod(
#                     name="MethodB",
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#                     return_types=(CType(name="PropertyType"),),
#                 ),
#                 "Namespace.Class.MethodC(ParamType)": CMethod(
#                     name="MethodC",
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#                     return_types=(CType(name="PropertyType"),),
#                 ),
#             },
#             events={},
#             nested_types={},
#         )
#
#         self.assertEqual(expected, result)
#
#     def test_merge_events(self) -> None:
#         class1: CClass = CClass(
#             name="Class",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={
#                 "Namespace.Class.EventA": CEvent(
#                     name="EventA",
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     type=CType(name="EventType"),
#                 ),
#                 "Namespace.Class.EventB": CEvent(
#                     name="EventB",
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     type=CType(name="EventType"),
#                 ),
#             },
#             nested_types={},
#         )
#         class2: CClass = CClass(
#             name="Class",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={
#                 "Namespace.Class.EventA": CEvent(
#                     name="EventA",
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     type=CType(name="EventType"),
#                 ),
#                 "Namespace.Class.EventC": CEvent(
#                     name="EventC",
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     type=CType(name="EventType"),
#                 ),
#             },
#             nested_types={},
#         )
#
#         result: CTypeDefinition = merge_class(class1, class2)
#         expected: CClass = CClass(
#             name="Class",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={
#                 "Namespace.Class.EventA": CEvent(
#                     name="EventA",
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     type=CType(name="EventType"),
#                 ),
#                 "Namespace.Class.EventB": CEvent(
#                     name="EventB",
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     type=CType(name="EventType"),
#                 ),
#                 "Namespace.Class.EventC": CEvent(
#                     name="EventC",
#                     declaring_type=CType(name="Class", namespace="Namespace"),
#                     type=CType(name="EventType"),
#                 ),
#             },
#             nested_types={},
#         )
#
#         self.assertEqual(expected, result)
#
#     def test_merge_nested(self) -> None:
#         class1: CClass = CClass(
#             name="Class",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={
#                 "Namespace:Class.NestedClassA": CClass(
#                     name="NestedClassA",
#                     namespace="Namespace",
#                     nested=CType(name="Class", namespace="Namespace"),
#                     abstract=False,
#                     generic_args=(),
#                     super_class=None,
#                     interfaces=(),
#                     fields={},
#                     constructors={},
#                     properties={},
#                     methods={},
#                     events={},
#                     nested_types={},
#                 ),
#                 "Namespace:Class.NestedClassB": CClass(
#                     name="NestedClassB",
#                     namespace="Namespace",
#                     nested=CType(name="Class", namespace="Namespace"),
#                     abstract=False,
#                     generic_args=(),
#                     super_class=None,
#                     interfaces=(),
#                     fields={},
#                     constructors={},
#                     properties={},
#                     methods={},
#                     events={},
#                     nested_types={},
#                 ),
#             },
#         )
#         class2: CClass = CClass(
#             name="Class",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={
#                 "Namespace:Class.NestedClassA": CClass(
#                     name="NestedClassA",
#                     namespace="Namespace",
#                     nested=CType(name="Class", namespace="Namespace"),
#                     abstract=False,
#                     generic_args=(),
#                     super_class=None,
#                     interfaces=(),
#                     fields={},
#                     constructors={},
#                     properties={},
#                     methods={},
#                     events={},
#                     nested_types={},
#                 ),
#                 "Namespace:Class.NestedClassC": CClass(
#                     name="NestedClassC",
#                     namespace="Namespace",
#                     nested=CType(name="Class", namespace="Namespace"),
#                     abstract=False,
#                     generic_args=(),
#                     super_class=None,
#                     interfaces=(),
#                     fields={},
#                     constructors={},
#                     properties={},
#                     methods={},
#                     events={},
#                     nested_types={},
#                 ),
#             },
#         )
#
#         result: CTypeDefinition = merge_class(class1, class2)
#         expected: CClass = CClass(
#             name="Class",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={
#                 "Namespace:Class.NestedClassA": CClass(
#                     name="NestedClassA",
#                     namespace="Namespace",
#                     nested=CType(name="Class", namespace="Namespace"),
#                     abstract=False,
#                     generic_args=(),
#                     super_class=None,
#                     interfaces=(),
#                     fields={},
#                     constructors={},
#                     properties={},
#                     methods={},
#                     events={},
#                     nested_types={},
#                 ),
#                 "Namespace:Class.NestedClassB": CClass(
#                     name="NestedClassB",
#                     namespace="Namespace",
#                     nested=CType(name="Class", namespace="Namespace"),
#                     abstract=False,
#                     generic_args=(),
#                     super_class=None,
#                     interfaces=(),
#                     fields={},
#                     constructors={},
#                     properties={},
#                     methods={},
#                     events={},
#                     nested_types={},
#                 ),
#                 "Namespace:Class.NestedClassC": CClass(
#                     name="NestedClassC",
#                     namespace="Namespace",
#                     nested=CType(name="Class", namespace="Namespace"),
#                     abstract=False,
#                     generic_args=(),
#                     super_class=None,
#                     interfaces=(),
#                     fields={},
#                     constructors={},
#                     properties={},
#                     methods={},
#                     events={},
#                     nested_types={},
#                 ),
#             },
#         )
#
#         self.assertEqual(expected, result)
#
#     def test_merge_error_abstract(self) -> None:
#         class1: CClass = CClass(
#             name="Class",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#         class2: CClass = CClass(
#             name="Class",
#             namespace="Namespace",
#             nested=None,
#             abstract=True,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_class(class1, class2))
#
#     def test_merge_error_generic_args(self) -> None:
#         class1: CClass = CClass(
#             name="Class",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#         class2: CClass = CClass(
#             name="Class",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(CType(name="T"),),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_class(class1, class2))
#
#     def test_merge_error_super_class(self) -> None:
#         class1: CClass = CClass(
#             name="Class",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#         class2: CClass = CClass(
#             name="Class",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=CType(name="Super", namespace="Namespace"),
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_class(class1, class2))
#
#
# class TestMergeStruct:
#     def test_merge_interfaces(self) -> None:
#         struct1: CStruct = CStruct(
#             name="Struct",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(
#                 CType(name="InterfaceA", namespace="Namespace"),
#                 CType(name="InterfaceB", namespace="Namespace"),
#             ),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#         struct2: CStruct = CStruct(
#             name="Struct",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(
#                 CType(name="InterfaceA", namespace="Namespace"),
#                 CType(name="InterfaceC", namespace="Namespace"),
#             ),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         result: CTypeDefinition = merge_struct(struct1, struct2)
#         expected: CStruct = CStruct(
#             name="Struct",
#             namespace="Namespace",
#             nested=None,
#             abstract=True,
#             generic_args=(),
#             super_class=None,
#             interfaces=(
#                 CType(name="InterfaceA", namespace="Namespace"),
#                 CType(name="InterfaceB", namespace="Namespace"),
#                 CType(name="InterfaceC", namespace="Namespace"),
#             ),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         self.assertEqual(expected, result)
#
#     def test_merge_fields(self) -> None:
#         struct1: CStruct = CStruct(
#             name="Struct",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={
#                 "Namespace.Struct.FieldA": CField(
#                     name="FieldA",
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     return_type=CType(name="ReturnType"),
#                 ),
#                 "Namespace.Struct.FieldB": CField(
#                     name="FieldB",
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     return_type=CType(name="ReturnType"),
#                 ),
#             },
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#         struct2: CStruct = CStruct(
#             name="Struct",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={
#                 "Namespace.Struct.FieldA": CField(
#                     name="FieldA",
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     return_type=CType(name="ReturnType"),
#                 ),
#                 "Namespace.Struct.FieldC": CField(
#                     name="FieldC",
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     return_type=CType(name="ReturnType"),
#                 ),
#             },
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         result: CTypeDefinition = merge_struct(struct1, struct2)
#         expected: CStruct = CStruct(
#             name="Struct",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={
#                 "Namespace.Struct.FieldA": CField(
#                     name="FieldA",
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     return_type=CType(name="ReturnType"),
#                 ),
#                 "Namespace.Struct.FieldB": CField(
#                     name="FieldB",
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     return_type=CType(name="ReturnType"),
#                 ),
#                 "Namespace.Struct.FieldC": CField(
#                     name="FieldC",
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     return_type=CType(name="ReturnType"),
#                 ),
#             },
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         self.assertEqual(expected, result)
#
#     def test_merge_constructors(self) -> None:
#         struct1: CStruct = CStruct(
#             name="Struct",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={
#                 "Namespace.Struct.__init__()": CConstructor(
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     parameters=(),
#                 ),
#                 "Namespace.Struct.__init__(ParamType)": CConstructor(
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#                 ),
#             },
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#         struct2: CStruct = CStruct(
#             name="Struct",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={
#                 "Namespace.Struct.__init__()": CConstructor(
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     parameters=(),
#                 ),
#                 "Namespace.Struct.__init__(ParamType, ParamType)": CConstructor(
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     parameters=(
#                         CParameter(name="param0", type=CType(name="ParamType")),
#                         CParameter(name="param1", type=CType(name="ParamType")),
#                     ),
#                 ),
#             },
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         result: CTypeDefinition = merge_struct(struct1, struct2)
#         expected: CStruct = CStruct(
#             name="Struct",
#             namespace="Namespace",
#             nested=None,
#             abstract=True,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={
#                 "Namespace.Struct.__init__()": CConstructor(
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     parameters=(),
#                 ),
#                 "Namespace.Struct.__init__(ParamType)": CConstructor(
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#                 ),
#                 "Namespace.Struct.__init__(ParamType, ParamType)": CConstructor(
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     parameters=(
#                         CParameter(name="param0", type=CType(name="ParamType")),
#                         CParameter(name="param1", type=CType(name="ParamType")),
#                     ),
#                 ),
#             },
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         self.assertEqual(expected, result)
#
#     def test_merge_properties(self) -> None:
#         struct1: CStruct = CStruct(
#             name="Struct",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={
#                 "Namespace.Struct.PropertyA": CProperty(
#                     name="PropertyA",
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     type=CType(name="PropertyType"),
#                 ),
#                 "Namespace.Struct.PropertyB": CProperty(
#                     name="PropertyB",
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     type=CType(name="PropertyType"),
#                 ),
#             },
#             methods={},
#             events={},
#             nested_types={},
#         )
#         struct2: CStruct = CStruct(
#             name="Struct",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={
#                 "Namespace.Struct.PropertyA": CProperty(
#                     name="PropertyA",
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     type=CType(name="PropertyType"),
#                 ),
#                 "Namespace.Struct.PropertyC": CProperty(
#                     name="PropertyC",
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     type=CType(name="PropertyType"),
#                 ),
#             },
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         result: CTypeDefinition = merge_struct(struct1, struct2)
#         expected: CStruct = CStruct(
#             name="Struct",
#             namespace="Namespace",
#             nested=None,
#             abstract=True,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={
#                 "Namespace.Struct.PropertyA": CProperty(
#                     name="PropertyA",
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     type=CType(name="PropertyType"),
#                 ),
#                 "Namespace.Struct.PropertyB": CProperty(
#                     name="PropertyB",
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     type=CType(name="PropertyType"),
#                 ),
#                 "Namespace.Struct.PropertyC": CProperty(
#                     name="PropertyC",
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     type=CType(name="PropertyType"),
#                 ),
#             },
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         self.assertEqual(expected, result)
#
#     def test_merge_methods(self) -> None:
#         struct1: CStruct = CStruct(
#             name="Struct",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={
#                 "Namespace.Struct.MethodA(ParamType)": CMethod(
#                     name="MethodA",
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#                     return_types=(CType(name="PropertyType"),),
#                 ),
#                 "Namespace.Struct.MethodB(ParamType)": CMethod(
#                     name="MethodB",
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#                     return_types=(CType(name="PropertyType"),),
#                 ),
#             },
#             events={},
#             nested_types={},
#         )
#         struct2: CStruct = CStruct(
#             name="Struct",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={
#                 "Namespace.Struct.MethodA(ParamType)": CMethod(
#                     name="MethodA",
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#                     return_types=(CType(name="PropertyType"),),
#                 ),
#                 "Namespace.Struct.MethodC(ParamType)": CMethod(
#                     name="MethodC",
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#                     return_types=(CType(name="PropertyType"),),
#                 ),
#             },
#             events={},
#             nested_types={},
#         )
#
#         result: CTypeDefinition = merge_struct(struct1, struct2)
#         expected: CStruct = CStruct(
#             name="Struct",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={
#                 "Namespace.Struct.MethodA(ParamType)": CMethod(
#                     name="MethodA",
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#                     return_types=(CType(name="PropertyType"),),
#                 ),
#                 "Namespace.Struct.MethodB(ParamType)": CMethod(
#                     name="MethodB",
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#                     return_types=(CType(name="PropertyType"),),
#                 ),
#                 "Namespace.Struct.MethodC(ParamType)": CMethod(
#                     name="MethodC",
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#                     return_types=(CType(name="PropertyType"),),
#                 ),
#             },
#             events={},
#             nested_types={},
#         )
#
#         self.assertEqual(expected, result)
#
#     def test_merge_events(self) -> None:
#         struct1: CStruct = CStruct(
#             name="Struct",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={
#                 "Namespace.Struct.EventA": CEvent(
#                     name="EventA",
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     type=CType(name="EventType"),
#                 ),
#                 "Namespace.Struct.EventB": CEvent(
#                     name="EventB",
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     type=CType(name="EventType"),
#                 ),
#             },
#             nested_types={},
#         )
#         struct2: CStruct = CStruct(
#             name="Struct",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={
#                 "Namespace.Struct.EventA": CEvent(
#                     name="EventA",
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     type=CType(name="EventType"),
#                 ),
#                 "Namespace.Struct.EventC": CEvent(
#                     name="EventC",
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     type=CType(name="EventType"),
#                 ),
#             },
#             nested_types={},
#         )
#
#         result: CTypeDefinition = merge_struct(struct1, struct2)
#         expected: CStruct = CStruct(
#             name="Struct",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={
#                 "Namespace.Struct.EventA": CEvent(
#                     name="EventA",
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     type=CType(name="EventType"),
#                 ),
#                 "Namespace.Struct.EventB": CEvent(
#                     name="EventB",
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     type=CType(name="EventType"),
#                 ),
#                 "Namespace.Struct.EventC": CEvent(
#                     name="EventC",
#                     declaring_type=CType(name="Struct", namespace="Namespace"),
#                     type=CType(name="EventType"),
#                 ),
#             },
#             nested_types={},
#         )
#
#         self.assertEqual(expected, result)
#
#     def test_merge_nested(self) -> None:
#         struct1: CStruct = CStruct(
#             name="Struct",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={
#                 "Namespace:Struct.NestedClassA": CClass(
#                     name="NestedClassA",
#                     namespace="Namespace",
#                     nested=CType(name="Struct", namespace="Namespace"),
#                     abstract=False,
#                     generic_args=(),
#                     super_class=None,
#                     interfaces=(),
#                     fields={},
#                     constructors={},
#                     properties={},
#                     methods={},
#                     events={},
#                     nested_types={},
#                 ),
#                 "Namespace:Struct.NestedClassB": CClass(
#                     name="NestedClassB",
#                     namespace="Namespace",
#                     nested=CType(name="Struct", namespace="Namespace"),
#                     abstract=False,
#                     generic_args=(),
#                     super_class=None,
#                     interfaces=(),
#                     fields={},
#                     constructors={},
#                     properties={},
#                     methods={},
#                     events={},
#                     nested_types={},
#                 ),
#             },
#         )
#         struct2: CStruct = CStruct(
#             name="Struct",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={
#                 "Namespace:Struct.NestedClassA": CClass(
#                     name="NestedClassA",
#                     namespace="Namespace",
#                     nested=CType(name="Struct", namespace="Namespace"),
#                     abstract=False,
#                     generic_args=(),
#                     super_class=None,
#                     interfaces=(),
#                     fields={},
#                     constructors={},
#                     properties={},
#                     methods={},
#                     events={},
#                     nested_types={},
#                 ),
#                 "Namespace:Struct.NestedClassC": CClass(
#                     name="NestedClassC",
#                     namespace="Namespace",
#                     nested=CType(name="Struct", namespace="Namespace"),
#                     abstract=False,
#                     generic_args=(),
#                     super_class=None,
#                     interfaces=(),
#                     fields={},
#                     constructors={},
#                     properties={},
#                     methods={},
#                     events={},
#                     nested_types={},
#                 ),
#             },
#         )
#
#         result: CTypeDefinition = merge_struct(struct1, struct2)
#         expected: CStruct = CStruct(
#             name="Struct",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={
#                 "Namespace:Struct.NestedClassA": CClass(
#                     name="NestedClassA",
#                     namespace="Namespace",
#                     nested=CType(name="Struct", namespace="Namespace"),
#                     abstract=False,
#                     generic_args=(),
#                     super_class=None,
#                     interfaces=(),
#                     fields={},
#                     constructors={},
#                     properties={},
#                     methods={},
#                     events={},
#                     nested_types={},
#                 ),
#                 "Namespace:Struct.NestedClassB": CClass(
#                     name="NestedClassB",
#                     namespace="Namespace",
#                     nested=CType(name="Struct", namespace="Namespace"),
#                     abstract=False,
#                     generic_args=(),
#                     super_class=None,
#                     interfaces=(),
#                     fields={},
#                     constructors={},
#                     properties={},
#                     methods={},
#                     events={},
#                     nested_types={},
#                 ),
#                 "Namespace:Struct.NestedClassC": CClass(
#                     name="NestedClassC",
#                     namespace="Namespace",
#                     nested=CType(name="Struct", namespace="Namespace"),
#                     abstract=False,
#                     generic_args=(),
#                     super_class=None,
#                     interfaces=(),
#                     fields={},
#                     constructors={},
#                     properties={},
#                     methods={},
#                     events={},
#                     nested_types={},
#                 ),
#             },
#         )
#
#         self.assertEqual(expected, result)
#
#     def test_merge_error_abstract(self) -> None:
#         struct1: CStruct = CStruct(
#             name="Struct",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#         struct2: CStruct = CStruct(
#             name="Struct",
#             namespace="Namespace",
#             nested=None,
#             abstract=True,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_struct(struct1, struct2))
#
#     def test_merge_error_generic_args(self) -> None:
#         struct1: CStruct = CStruct(
#             name="Struct",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#         struct2: CStruct = CStruct(
#             name="Struct",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(CType(name="T"),),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_struct(struct1, struct2))
#
#     def test_merge_error_super_class(self) -> None:
#         struct1: CStruct = CStruct(
#             name="Struct",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=None,
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#         struct2: CStruct = CStruct(
#             name="Struct",
#             namespace="Namespace",
#             nested=None,
#             abstract=False,
#             generic_args=(),
#             super_class=CType(name="Super", namespace="Namespace"),
#             interfaces=(),
#             fields={},
#             constructors={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_struct(struct1, struct2))
#
#
# class TestMergeInterface:
#     def test_merge_interfaces(self) -> None:
#         interface1: CInterface = CInterface(
#             name="Interface",
#             namespace="Namespace",
#             nested=None,
#             generic_args=(),
#             interfaces=(
#                 CType(name="InterfaceA", namespace="Namespace"),
#                 CType(name="InterfaceB", namespace="Namespace"),
#             ),
#             fields={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#         interface2: CInterface = CInterface(
#             name="Interface",
#             namespace="Namespace",
#             nested=None,
#             generic_args=(),
#             interfaces=(
#                 CType(name="InterfaceA", namespace="Namespace"),
#                 CType(name="InterfaceC", namespace="Namespace"),
#             ),
#             fields={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         result: CTypeDefinition = merge_interface(interface1, interface2)
#         expected: CInterface = CInterface(
#             name="Interface",
#             namespace="Namespace",
#             nested=None,
#             generic_args=(),
#             interfaces=(
#                 CType(name="InterfaceA", namespace="Namespace"),
#                 CType(name="InterfaceB", namespace="Namespace"),
#                 CType(name="InterfaceC", namespace="Namespace"),
#             ),
#             fields={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         self.assertEqual(expected, result)
#
#     def test_merge_fields(self) -> None:
#         interface1: CInterface = CInterface(
#             name="Interface",
#             namespace="Namespace",
#             nested=None,
#             generic_args=(),
#             interfaces=(),
#             fields={
#                 "Namespace.Interface.FieldA": CField(
#                     name="FieldA",
#                     declaring_type=CType(name="Interface", namespace="Namespace"),
#                     return_type=CType(name="ReturnType"),
#                 ),
#                 "Namespace.Interface.FieldB": CField(
#                     name="FieldB",
#                     declaring_type=CType(name="Interface", namespace="Namespace"),
#                     return_type=CType(name="ReturnType"),
#                 ),
#             },
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#         interface2: CInterface = CInterface(
#             name="Interface",
#             namespace="Namespace",
#             nested=None,
#             generic_args=(),
#             interfaces=(),
#             fields={
#                 "Namespace.Interface.FieldA": CField(
#                     name="FieldA",
#                     declaring_type=CType(name="Interface", namespace="Namespace"),
#                     return_type=CType(name="ReturnType"),
#                 ),
#                 "Namespace.Interface.FieldC": CField(
#                     name="FieldC",
#                     declaring_type=CType(name="Interface", namespace="Namespace"),
#                     return_type=CType(name="ReturnType"),
#                 ),
#             },
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         result: CTypeDefinition = merge_interface(interface1, interface2)
#         expected: CInterface = CInterface(
#             name="Interface",
#             namespace="Namespace",
#             nested=None,
#             generic_args=(),
#             interfaces=(),
#             fields={
#                 "Namespace.Interface.FieldA": CField(
#                     name="FieldA",
#                     declaring_type=CType(name="Interface", namespace="Namespace"),
#                     return_type=CType(name="ReturnType"),
#                 ),
#                 "Namespace.Interface.FieldB": CField(
#                     name="FieldB",
#                     declaring_type=CType(name="Interface", namespace="Namespace"),
#                     return_type=CType(name="ReturnType"),
#                 ),
#                 "Namespace.Interface.FieldC": CField(
#                     name="FieldC",
#                     declaring_type=CType(name="Interface", namespace="Namespace"),
#                     return_type=CType(name="ReturnType"),
#                 ),
#             },
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         self.assertEqual(expected, result)
#
#     def test_merge_properties(self) -> None:
#         interface1: CInterface = CInterface(
#             name="Interface",
#             namespace="Namespace",
#             nested=None,
#             generic_args=(),
#             interfaces=(),
#             fields={},
#             properties={
#                 "Namespace.Interface.PropertyA": CProperty(
#                     name="PropertyA",
#                     declaring_type=CType(name="Interface", namespace="Namespace"),
#                     type=CType(name="PropertyType"),
#                 ),
#                 "Namespace.Interface.PropertyB": CProperty(
#                     name="PropertyB",
#                     declaring_type=CType(name="Interface", namespace="Namespace"),
#                     type=CType(name="PropertyType"),
#                 ),
#             },
#             methods={},
#             events={},
#             nested_types={},
#         )
#         interface2: CInterface = CInterface(
#             name="Interface",
#             namespace="Namespace",
#             nested=None,
#             generic_args=(),
#             interfaces=(),
#             fields={},
#             properties={
#                 "Namespace.Interface.PropertyA": CProperty(
#                     name="PropertyA",
#                     declaring_type=CType(name="Interface", namespace="Namespace"),
#                     type=CType(name="PropertyType"),
#                 ),
#                 "Namespace.Interface.PropertyC": CProperty(
#                     name="PropertyC",
#                     declaring_type=CType(name="Interface", namespace="Namespace"),
#                     type=CType(name="PropertyType"),
#                 ),
#             },
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         result: CTypeDefinition = merge_interface(interface1, interface2)
#         expected: CInterface = CInterface(
#             name="Interface",
#             namespace="Namespace",
#             nested=None,
#             generic_args=(),
#             interfaces=(),
#             fields={},
#             properties={
#                 "Namespace.Interface.PropertyA": CProperty(
#                     name="PropertyA",
#                     declaring_type=CType(name="Interface", namespace="Namespace"),
#                     type=CType(name="PropertyType"),
#                 ),
#                 "Namespace.Interface.PropertyB": CProperty(
#                     name="PropertyB",
#                     declaring_type=CType(name="Interface", namespace="Namespace"),
#                     type=CType(name="PropertyType"),
#                 ),
#                 "Namespace.Interface.PropertyC": CProperty(
#                     name="PropertyC",
#                     declaring_type=CType(name="Interface", namespace="Namespace"),
#                     type=CType(name="PropertyType"),
#                 ),
#             },
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         self.assertEqual(expected, result)
#
#     def test_merge_methods(self) -> None:
#         interface1: CInterface = CInterface(
#             name="Interface",
#             namespace="Namespace",
#             nested=None,
#             generic_args=(),
#             interfaces=(),
#             fields={},
#             properties={},
#             methods={
#                 "Namespace.Interface.MethodA(ParamType)": CMethod(
#                     name="MethodA",
#                     declaring_type=CType(name="Interface", namespace="Namespace"),
#                     parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#                     return_types=(CType(name="PropertyType"),),
#                 ),
#                 "Namespace.Interface.MethodB(ParamType)": CMethod(
#                     name="MethodB",
#                     declaring_type=CType(name="Interface", namespace="Namespace"),
#                     parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#                     return_types=(CType(name="PropertyType"),),
#                 ),
#             },
#             events={},
#             nested_types={},
#         )
#         interface2: CInterface = CInterface(
#             name="Interface",
#             namespace="Namespace",
#             nested=None,
#             generic_args=(),
#             interfaces=(),
#             fields={},
#             properties={},
#             methods={
#                 "Namespace.Interface.MethodA(ParamType)": CMethod(
#                     name="MethodA",
#                     declaring_type=CType(name="Interface", namespace="Namespace"),
#                     parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#                     return_types=(CType(name="PropertyType"),),
#                 ),
#                 "Namespace.Interface.MethodC(ParamType)": CMethod(
#                     name="MethodC",
#                     declaring_type=CType(name="Interface", namespace="Namespace"),
#                     parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#                     return_types=(CType(name="PropertyType"),),
#                 ),
#             },
#             events={},
#             nested_types={},
#         )
#
#         result: CTypeDefinition = merge_interface(interface1, interface2)
#         expected: CInterface = CInterface(
#             name="Interface",
#             namespace="Namespace",
#             nested=None,
#             generic_args=(),
#             interfaces=(),
#             fields={},
#             properties={},
#             methods={
#                 "Namespace.Interface.MethodA(ParamType)": CMethod(
#                     name="MethodA",
#                     declaring_type=CType(name="Interface", namespace="Namespace"),
#                     parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#                     return_types=(CType(name="PropertyType"),),
#                 ),
#                 "Namespace.Interface.MethodB(ParamType)": CMethod(
#                     name="MethodB",
#                     declaring_type=CType(name="Interface", namespace="Namespace"),
#                     parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#                     return_types=(CType(name="PropertyType"),),
#                 ),
#                 "Namespace.Interface.MethodC(ParamType)": CMethod(
#                     name="MethodC",
#                     declaring_type=CType(name="Interface", namespace="Namespace"),
#                     parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#                     return_types=(CType(name="PropertyType"),),
#                 ),
#             },
#             events={},
#             nested_types={},
#         )
#
#         self.assertEqual(expected, result)
#
#     def test_merge_events(self) -> None:
#         interface1: CInterface = CInterface(
#             name="Interface",
#             namespace="Namespace",
#             nested=None,
#             generic_args=(),
#             interfaces=(),
#             fields={},
#             properties={},
#             methods={},
#             events={
#                 "Namespace.Interface.EventA": CEvent(
#                     name="EventA",
#                     declaring_type=CType(name="Interface", namespace="Namespace"),
#                     type=CType(name="EventType"),
#                 ),
#                 "Namespace.Interface.EventB": CEvent(
#                     name="EventB",
#                     declaring_type=CType(name="Interface", namespace="Namespace"),
#                     type=CType(name="EventType"),
#                 ),
#             },
#             nested_types={},
#         )
#         interface2: CInterface = CInterface(
#             name="Interface",
#             namespace="Namespace",
#             nested=None,
#             generic_args=(),
#             interfaces=(),
#             fields={},
#             properties={},
#             methods={},
#             events={
#                 "Namespace.Interface.EventA": CEvent(
#                     name="EventA",
#                     declaring_type=CType(name="Interface", namespace="Namespace"),
#                     type=CType(name="EventType"),
#                 ),
#                 "Namespace.Interface.EventC": CEvent(
#                     name="EventC",
#                     declaring_type=CType(name="Interface", namespace="Namespace"),
#                     type=CType(name="EventType"),
#                 ),
#             },
#             nested_types={},
#         )
#
#         result: CTypeDefinition = merge_interface(interface1, interface2)
#         expected: CInterface = CInterface(
#             name="Interface",
#             namespace="Namespace",
#             nested=None,
#             generic_args=(),
#             interfaces=(),
#             fields={},
#             properties={},
#             methods={},
#             events={
#                 "Namespace.Interface.EventA": CEvent(
#                     name="EventA",
#                     declaring_type=CType(name="Interface", namespace="Namespace"),
#                     type=CType(name="EventType"),
#                 ),
#                 "Namespace.Interface.EventB": CEvent(
#                     name="EventB",
#                     declaring_type=CType(name="Interface", namespace="Namespace"),
#                     type=CType(name="EventType"),
#                 ),
#                 "Namespace.Interface.EventC": CEvent(
#                     name="EventC",
#                     declaring_type=CType(name="Interface", namespace="Namespace"),
#                     type=CType(name="EventType"),
#                 ),
#             },
#             nested_types={},
#         )
#
#         self.assertEqual(expected, result)
#
#     def test_merge_nested(self) -> None:
#         interface1: CInterface = CInterface(
#             name="Interface",
#             namespace="Namespace",
#             nested=None,
#             generic_args=(),
#             interfaces=(),
#             fields={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={
#                 "Namespace:Interface.NestedClassA": CClass(
#                     name="NestedClassA",
#                     namespace="Namespace",
#                     nested=CType(name="Interface", namespace="Namespace"),
#                     abstract=False,
#                     generic_args=(),
#                     super_class=None,
#                     interfaces=(),
#                     fields={},
#                     constructors={},
#                     properties={},
#                     methods={},
#                     events={},
#                     nested_types={},
#                 ),
#                 "Namespace:Interface.NestedClassB": CClass(
#                     name="NestedClassB",
#                     namespace="Namespace",
#                     nested=CType(name="Interface", namespace="Namespace"),
#                     abstract=False,
#                     generic_args=(),
#                     super_class=None,
#                     interfaces=(),
#                     fields={},
#                     constructors={},
#                     properties={},
#                     methods={},
#                     events={},
#                     nested_types={},
#                 ),
#             },
#         )
#         interface2: CInterface = CInterface(
#             name="Interface",
#             namespace="Namespace",
#             nested=None,
#             generic_args=(),
#             interfaces=(),
#             fields={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={
#                 "Namespace:Interface.NestedClassA": CClass(
#                     name="NestedClassA",
#                     namespace="Namespace",
#                     nested=CType(name="Interface", namespace="Namespace"),
#                     abstract=False,
#                     generic_args=(),
#                     super_class=None,
#                     interfaces=(),
#                     fields={},
#                     constructors={},
#                     properties={},
#                     methods={},
#                     events={},
#                     nested_types={},
#                 ),
#                 "Namespace:Interface.NestedClassC": CClass(
#                     name="NestedClassC",
#                     namespace="Namespace",
#                     nested=CType(name="Interface", namespace="Namespace"),
#                     abstract=False,
#                     generic_args=(),
#                     super_class=None,
#                     interfaces=(),
#                     fields={},
#                     constructors={},
#                     properties={},
#                     methods={},
#                     events={},
#                     nested_types={},
#                 ),
#             },
#         )
#
#         result: CTypeDefinition = merge_interface(interface1, interface2)
#         expected: CInterface = CInterface(
#             name="Interface",
#             namespace="Namespace",
#             nested=None,
#             generic_args=(),
#             interfaces=(),
#             fields={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={
#                 "Namespace:Interface.NestedClassA": CClass(
#                     name="NestedClassA",
#                     namespace="Namespace",
#                     nested=CType(name="Interface", namespace="Namespace"),
#                     abstract=False,
#                     generic_args=(),
#                     super_class=None,
#                     interfaces=(),
#                     fields={},
#                     constructors={},
#                     properties={},
#                     methods={},
#                     events={},
#                     nested_types={},
#                 ),
#                 "Namespace:Interface.NestedClassB": CClass(
#                     name="NestedClassB",
#                     namespace="Namespace",
#                     nested=CType(name="Interface", namespace="Namespace"),
#                     abstract=False,
#                     generic_args=(),
#                     super_class=None,
#                     interfaces=(),
#                     fields={},
#                     constructors={},
#                     properties={},
#                     methods={},
#                     events={},
#                     nested_types={},
#                 ),
#                 "Namespace:Interface.NestedClassC": CClass(
#                     name="NestedClassC",
#                     namespace="Namespace",
#                     nested=CType(name="Interface", namespace="Namespace"),
#                     abstract=False,
#                     generic_args=(),
#                     super_class=None,
#                     interfaces=(),
#                     fields={},
#                     constructors={},
#                     properties={},
#                     methods={},
#                     events={},
#                     nested_types={},
#                 ),
#             },
#         )
#
#         self.assertEqual(expected, result)
#
#     def test_merge_error_generic_args(self) -> None:
#         interface1: CInterface = CInterface(
#             name="Interface",
#             namespace="Namespace",
#             nested=None,
#             generic_args=(),
#             interfaces=(),
#             fields={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#         interface2: CInterface = CInterface(
#             name="Interface",
#             namespace="Namespace",
#             nested=None,
#             generic_args=(CType(name="T"),),
#             interfaces=(),
#             fields={},
#             properties={},
#             methods={},
#             events={},
#             nested_types={},
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_interface(interface1, interface2))
#
#
# class TestMergeEnum:
#     def test_merge(self) -> None:
#         enum1: CEnum = CEnum(
#             name="Enum",
#             namespace="Namespace",
#             nested=None,
#             fields=("FieldA", "FieldB", "FieldC", "FieldD"),
#         )
#         enum2: CEnum = CEnum(
#             name="Enum",
#             namespace="Namespace",
#             nested=None,
#             fields=("FieldA", "FieldB", "FieldC", "FieldD"),
#         )
#
#         result: CTypeDefinition = merge_type_def(enum1, enum2)
#         expected: CEnum = CEnum(
#             name="Enum",
#             namespace="Namespace",
#             nested=None,
#             fields=("FieldA", "FieldB", "FieldC", "FieldD"),
#         )
#
#         self.assertEqual(expected, result)
#
#     def test_merge_error_fields(self) -> None:
#         enum1: CEnum = CEnum(
#             name="Enum",
#             namespace="Namespace",
#             nested=None,
#             fields=("FieldA", "FieldB", "FieldC", "FieldD"),
#         )
#         enum2: CEnum = CEnum(
#             name="Enum",
#             namespace="Namespace",
#             nested=None,
#             fields=("FieldA", "FieldB", "FieldC", "FieldD", "FieldE"),
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_enum(enum1, enum2))
#
#
# class TestMergeDelegate:
#     def test_merge(self) -> None:
#         delegate1: CDelegate = CDelegate(
#             name="Delegate",
#             namespace="Namespace",
#             nested=None,
#             parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#             return_type=CType(name="ReturnType"),
#         )
#         delegate2: CDelegate = CDelegate(
#             name="Delegate",
#             namespace="Namespace",
#             nested=None,
#             parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#             return_type=CType(name="ReturnType"),
#         )
#
#         result: CTypeDefinition = merge_type_def(delegate1, delegate2)
#         expected: CDelegate = CDelegate(
#             name="Delegate",
#             namespace="Namespace",
#             nested=None,
#             parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#             return_type=CType(name="ReturnType"),
#         )
#
#         self.assertEqual(expected, result)
#
#     def test_merge_error_parameters(self) -> None:
#         delegate1: CDelegate = CDelegate(
#             name="Delegate",
#             namespace="Namespace",
#             nested=None,
#             parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#             return_type=CType(name="ReturnType"),
#         )
#         delegate2: CDelegate = CDelegate(
#             name="Delegate",
#             namespace="Namespace",
#             nested=None,
#             parameters=(
#                 CParameter(name="param0", type=CType(name="ParamType")),
#                 CParameter(name="param1", type=CType(name="ParamType")),
#             ),
#             return_type=CType(name="ReturnType"),
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_delegate(delegate1, delegate2))
#
#     def test_merge_error_return_type(self) -> None:
#         delegate1: CDelegate = CDelegate(
#             name="Delegate",
#             namespace="Namespace",
#             nested=None,
#             parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#             return_type=CType(name="ReturnTypeA"),
#         )
#         delegate2: CDelegate = CDelegate(
#             name="Delegate",
#             namespace="Namespace",
#             nested=None,
#             parameters=(CParameter(name="param0", type=CType(name="ParamType")),),
#             return_type=CType(name="ReturnTypeB"),
#         )
#
#         self.assertRaises(AttributeError, lambda: merge_delegate(delegate1, delegate2))


# class TestMergeDoc:
#     def test_merge(self) -> None:
#         tree0: Mapping[str, Any] = {
#             "doc": "",
#             "doc_formatted": {},
#             "parameters": {},
#             "return": "",
#             "exceptions": {},
#         }
#         tree1: Mapping[str, Any] = {
#             "doc": "DocNode String\n%format0%",
#             "doc_formatted": {
#                 "format0": ("0", "1", "2", "3"),
#                 "format1": ("0", "2", "4", "6"),
#             },
#             "parameters": {
#                 "param0": "Parameter 0.",
#                 "param1": "Parameter 1.",
#             },
#             "return": "Return String",
#             "exceptions": {
#                 "Exception0": "Exception 0.",
#                 "Exception1": "Exception 1.",
#             },
#         }
#
#         doc_dict0: DocNode = DocNode(tree0)
#         doc_dict1: DocNode = DocNode(tree1)
#
#         merged: DocNode = merge_doc(doc_dict0, doc_dict1)
#
#         self.assertIsNotNone(merged)
#         self.assertIsInstance(merged, DocNode)
#         self.assertEqual(
#             {
#                 "doc": "DocNode String\n%format0%",
#                 "doc_formatted": {
#                     "format0": ("0", "1", "2", "3"),
#                     "format1": ("0", "2", "4", "6"),
#                 },
#                 "parameters": {
#                     "param0": "Parameter 0.",
#                     "param1": "Parameter 1.",
#                 },
#                 "return": "Return String",
#                 "exceptions": {
#                     "Exception0": "Exception 0.",
#                     "Exception1": "Exception 1.",
#                 },
#             },
#             merged.data,
#         )
#
#     def test_merge_doc_empty(self) -> None:
#         tree0: Mapping[str, Any] = {"doc": "Doc0"}
#         tree1: Mapping[str, Any] = {"doc": ""}
#
#         doc_dict0: DocNode = DocNode(tree0)
#         doc_dict1: DocNode = DocNode(tree1)
#
#         merged: DocNode = merge_doc(doc_dict0, doc_dict1)
#
#         self.assertIsNotNone(merged)
#         self.assertIsInstance(merged, DocNode)
#         self.assertEqual({"doc": "Doc0"}, merged.data)
#
#     def test_merge_doc_both(self) -> None:
#         tree0: Mapping[str, Any] = {"doc": "Doc0"}
#         tree1: Mapping[str, Any] = {"doc": "Doc1"}
#
#         doc_dict0: DocNode = DocNode(tree0)
#         doc_dict1: DocNode = DocNode(tree1)
#
#         merged: DocNode = merge_doc(doc_dict0, doc_dict1)
#
#         self.assertIsNotNone(merged)
#         self.assertIsInstance(merged, DocNode)
#         self.assertEqual({"doc": "Doc0\nDoc1"}, merged.data)
#
#     def test_merge_doc_formatted_empty(self) -> None:
#         tree0: Mapping[str, Any] = {
#             "doc_formatted": {
#                 "format0": ("0", "1", "2", "3"),
#                 "format1": ("0", "2", "4", "6"),
#             },
#         }
#         tree1: Mapping[str, Any] = {
#             "doc_formatted": {
#                 "format0": (),
#             },
#         }
#
#         doc_dict0: DocNode = DocNode(tree0)
#         doc_dict1: DocNode = DocNode(tree1)
#
#         merged: DocNode = merge_doc(doc_dict0, doc_dict1)
#
#         self.assertIsNotNone(merged)
#         self.assertIsInstance(merged, DocNode)
#         self.assertEqual(
#             {
#                 "doc_formatted": {
#                     "format0": ("0", "1", "2", "3"),
#                     "format1": ("0", "2", "4", "6"),
#                 },
#             },
#             merged.data,
#         )
#
#     def test_merge_doc_formatted_both(self) -> None:
#         tree0: Mapping[str, Any] = {
#             "doc_formatted": {
#                 "format0": ("0", "1", "2", "3"),
#                 "format1": ("0", "2", "4", "6"),
#                 "format2": ("0", "3", "6", "9"),
#             },
#         }
#         tree1: Mapping[str, Any] = {
#             "doc_formatted": {
#                 "format0": ("0", "1", "2", "3"),
#                 "format1": ("0", "2", "4", "6"),
#                 "format3": ("0", "4", "8", "12"),
#             },
#         }
#
#         doc_dict0: DocNode = DocNode(tree0)
#         doc_dict1: DocNode = DocNode(tree1)
#
#         merged: DocNode = merge_doc(doc_dict0, doc_dict1)
#
#         self.assertIsNotNone(merged)
#         self.assertIsInstance(merged, DocNode)
#         self.assertEqual(
#             {
#                 "doc_formatted": {
#                     "format0": ("0", "1", "2", "3", "0", "1", "2", "3"),
#                     "format1": ("0", "2", "4", "6", "0", "2", "4", "6"),
#                     "format2": ("0", "3", "6", "9"),
#                     "format3": ("0", "4", "8", "12"),
#                 },
#             },
#             merged.data,
#         )
#
#     def test_merge_parameters_empty(self) -> None:
#         tree0: Mapping[str, Any] = {
#             "parameters": {
#                 "param0": "Parameter 0.",
#                 "param1": "Parameter 1.",
#             },
#         }
#         tree1: Mapping[str, Any] = {
#             "parameters": {
#                 "param0": "",
#             },
#         }
#
#         doc_dict0: DocNode = DocNode(tree0)
#         doc_dict1: DocNode = DocNode(tree1)
#
#         merged: DocNode = merge_doc(doc_dict0, doc_dict1)
#
#         self.assertIsNotNone(merged)
#         self.assertIsInstance(merged, DocNode)
#         self.assertEqual(
#             {
#                 "parameters": {
#                     "param0": "Parameter 0.",
#                     "param1": "Parameter 1.",
#                 },
#             },
#             merged.data,
#         )
#
#     def test_merge_parameters_both(self) -> None:
#         tree0: Mapping[str, Any] = {
#             "parameters": {
#                 "param0": "Parameter 0.",
#                 "param1": "Parameter 1.",
#                 "param2": "Parameter 2.",
#             },
#         }
#         tree1: Mapping[str, Any] = {
#             "parameters": {
#                 "param0": "Parameter 0.",
#                 "param1": "Parameter 1.",
#                 "param3": "Parameter 3.",
#             },
#         }
#
#         doc_dict0: DocNode = DocNode(tree0)
#         doc_dict1: DocNode = DocNode(tree1)
#
#         merged: DocNode = merge_doc(doc_dict0, doc_dict1)
#
#         self.assertIsNotNone(merged)
#         self.assertIsInstance(merged, DocNode)
#         self.assertEqual(
#             {
#                 "parameters": {
#                     "param0": "Parameter 0.\nParameter 0.",
#                     "param1": "Parameter 1.\nParameter 1.",
#                     "param2": "Parameter 2.",
#                     "param3": "Parameter 3.",
#                 },
#             },
#             merged.data,
#         )
#
#     def test_merge_return_empty(self) -> None:
#         tree0: Mapping[str, Any] = {"return": "Return0"}
#         tree1: Mapping[str, Any] = {"return": ""}
#
#         doc_dict0: DocNode = DocNode(tree0)
#         doc_dict1: DocNode = DocNode(tree1)
#
#         merged: DocNode = merge_doc(doc_dict0, doc_dict1)
#
#         self.assertIsNotNone(merged)
#         self.assertIsInstance(merged, DocNode)
#         self.assertEqual({"return": "Return0"}, merged.data)
#
#     def test_merge_return_both(self) -> None:
#         tree0: Mapping[str, Any] = {"return": "Return0"}
#         tree1: Mapping[str, Any] = {"return": "Return1"}
#
#         doc_dict0: DocNode = DocNode(tree0)
#         doc_dict1: DocNode = DocNode(tree1)
#
#         merged: DocNode = merge_doc(doc_dict0, doc_dict1)
#
#         self.assertIsNotNone(merged)
#         self.assertIsInstance(merged, DocNode)
#         self.assertEqual({"return": "Return0\nReturn1"}, merged.data)
#
#     def test_merge_exceptions_empty(self) -> None:
#         tree0: Mapping[str, Any] = {
#             "exceptions": {
#                 "Exception0": "Exception 0.",
#                 "Exception1": "Exception 1.",
#             },
#         }
#         tree1: Mapping[str, Any] = {
#             "exceptions": {
#                 "Exception0": "",
#             },
#         }
#
#         doc_dict0: DocNode = DocNode(tree0)
#         doc_dict1: DocNode = DocNode(tree1)
#
#         merged: DocNode = merge_doc(doc_dict0, doc_dict1)
#
#         self.assertIsNotNone(merged)
#         self.assertIsInstance(merged, DocNode)
#         self.assertEqual(
#             {
#                 "exceptions": {
#                     "Exception0": "Exception 0.",
#                     "Exception1": "Exception 1.",
#                 },
#             },
#             merged.data,
#         )
#
#     def test_merge_exceptions_both(self) -> None:
#         tree0: Mapping[str, Any] = {
#             "exceptions": {
#                 "Exception0": "Exception 0.",
#                 "Exception1": "Exception 1.",
#                 "Exception2": "Exception 2.",
#             },
#         }
#         tree1: Mapping[str, Any] = {
#             "exceptions": {
#                 "Exception0": "Exception 0.",
#                 "Exception1": "Exception 1.",
#                 "Exception3": "Exception 3.",
#             },
#         }
#
#         doc_dict0: DocNode = DocNode(tree0)
#         doc_dict1: DocNode = DocNode(tree1)
#
#         merged: DocNode = merge_doc(doc_dict0, doc_dict1)
#
#         self.assertIsNotNone(merged)
#         self.assertIsInstance(merged, DocNode)
#         self.assertEqual(
#             {
#                 "exceptions": {
#                     "Exception0": "Exception 0.\nException 0.",
#                     "Exception1": "Exception 1.\nException 1.",
#                     "Exception2": "Exception 2.",
#                     "Exception3": "Exception 3.",
#                 },
#             },
#             merged.data,
#         )
#
#     def test_merge_tree(self) -> None:
#         tree0: Mapping[str, Any] = {"NodeA": {}}
#         tree1: Mapping[str, Any] = {"NodeB": {}}
#
#         doc_dict0: DocNode = DocNode(tree0)
#         doc_dict1: DocNode = DocNode(tree1)
#
#         merged: DocNode = merge_doc(doc_dict0, doc_dict1)
#
#         self.assertIsNotNone(merged)
#         self.assertIsInstance(merged, DocNode)
#         self.assertEqual(
#             {
#                 "NodeA": {},
#                 "NodeB": {},
#             },
#             merged.data,
#         )
#
#     def test_merge_tree_deep(self) -> None:
#         tree0: Mapping[str, Any] = {"NodeA": {"NodeB": {"NodeC": {"NodeD": {}}}}}
#         tree1: Mapping[str, Any] = {"NodeA": {"NodeB": {"NodeC": {"NodeE": {}}}}}
#
#         doc_dict0: DocNode = DocNode(tree0)
#         doc_dict1: DocNode = DocNode(tree1)
#
#         merged: DocNode = merge_doc(doc_dict0, doc_dict1)
#
#         self.assertIsNotNone(merged)
#         self.assertIsInstance(merged, DocNode)
#         self.assertEqual(
#             {"NodeA": {"NodeB": {"NodeC": {"NodeD": {}, "NodeE": {}}}}},
#             merged.data,
#         )


class TestBuildType:
    """Tests for build_type()."""

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
        self, obj: CType, expected: str, imported: set[str], imports: ImportList
    ) -> None:
        """Test for build_type() with native types."""
        actual: str = build_type(obj=obj, import_list=imports, convert=False)

        assert actual == expected
        assert imports.types == imported

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
        self, obj: CType, expected: str, imported: set[str], imports: ImportList
    ) -> None:
        """Test for build_type() when convert is True."""
        actual: str = build_type(obj=obj, import_list=imports, convert=True)

        assert actual == expected
        assert imports.types == imported

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
        self, obj: CType, expected: str, imported: set[str], imports: ImportList
    ) -> None:
        """Test for build_type() when convert is True."""
        actual: str = build_type(obj=obj, import_list=imports, convert=False)

        assert actual == expected
        assert imports.types == imported

    @pytest.mark.parametrize(
        ("obj", "expected"),
        **make_params([("basic", (CType(name="Type", nullable=True), "Type | None"))]),
    )
    def test_nullable(self, obj: CType, expected: str, imports: ImportList) -> None:
        """Test for build_type() when convert is True."""
        actual: str = build_type(obj=obj, import_list=imports, convert=False)

        assert actual == expected


class TestBuildParameter:
    """Tests for build_parameter()."""

    def test_simple(self, imports: ImportList) -> None:
        """Test for build_parameter() with a simple parameter."""
        obj: CParameter = CParameter(name="name", type=CType(name="Type"))

        expected: str = "name: Type"
        actual: str = build_parameter(obj=obj, import_list=imports)

        assert actual == expected

    def test_default(self, imports: ImportList) -> None:
        """Test for build_parameter() with a parameter with a default value."""
        obj: CParameter = CParameter(name="name", type=CType(name="Type"), default=True)

        expected: str = "name: Type = ..."
        actual: str = build_parameter(obj=obj, import_list=imports)

        assert actual == expected


class TestBuildField:
    """Tests for build_field()."""

    def test_basic(self, imports: ImportList, doc: DocNode, line_length: int) -> None:
        """Test for build_field() with a basic field."""
        obj: CField = CField(
            name="Name",
            declaring_type=CType(name="Type", namespace="Namespace"),
            return_type=CType(name="Type", namespace="Namespace"),
        )

        expected: Sequence[str] = [
            "Name: Final[Type] = ...",
            '""""""',
        ]
        actual: Sequence[str] = build_field(
            obj=obj,
            import_list=imports,
            doc_tree=doc,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {ImportList.FINAL, "Namespace.Type"}

    def test_static(self, imports: ImportList, doc: DocNode, line_length: int) -> None:
        """Test for build_field() with a static field."""
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
        actual: Sequence[str] = build_field(
            obj=obj,
            import_list=imports,
            doc_tree=doc,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {ImportList.FINAL, ImportList.CLASS_VAR, "Namespace.Type"}


class TestBuildConstructor:
    """Tests for build_constructor()."""

    def test_basic(self, imports: ImportList, doc: DocNode, line_length: int) -> None:
        """Test for build_constructor() with a basic constructor."""
        obj: CConstructor = CConstructor(declaring_type=CType(name="Type", namespace="Namespace"))

        expected: Sequence[str] = [
            "def __init__(self) -> None:",
            '    """"""',
        ]
        actual: Sequence[str] = build_constructor(
            obj=obj,
            import_list=imports,
            doc_tree=doc,
            overload=False,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == set()

    def test_parameters(self, imports: ImportList, doc: DocNode, line_length: int) -> None:
        """Test for build_constructor() with a constructor with parameters."""
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
        actual: Sequence[str] = build_constructor(
            obj=obj,
            import_list=imports,
            doc_tree=doc,
            overload=False,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {"Namespace.Type"}

    def test_overload(self, imports: ImportList, doc: DocNode, line_length: int) -> None:
        """Test for build_constructor() with an overloaded constructor."""
        obj: CConstructor = CConstructor(declaring_type=CType(name="Type", namespace="Namespace"))

        expected: Sequence[str] = [
            "@overload",
            "def __init__(self) -> None:",
            '    """"""',
        ]
        actual: Sequence[str] = build_constructor(
            obj=obj,
            import_list=imports,
            doc_tree=doc,
            overload=True,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {ImportList.OVERLOAD}


class TestBuildProperty:
    """Tests for build_property()."""

    def test_basic(self, imports: ImportList, doc: DocNode, line_length: int) -> None:
        """Test for build_property() with a basic property."""
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
        actual: Sequence[str] = build_property(
            obj=obj, import_list=imports, doc_tree=doc, line_length=line_length
        )

        assert actual == expected
        assert imports.types == {"Namespace.Type"}

    def test_setter(self, imports: ImportList, doc: DocNode, line_length: int) -> None:
        """Test for build_property() with a property with a setter."""
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
        actual: Sequence[str] = build_property(
            obj=obj, import_list=imports, doc_tree=doc, line_length=line_length
        )

        assert actual == expected
        assert imports.types == {"Namespace.Type"}

    def test_static(self, imports: ImportList, doc: DocNode, line_length: int) -> None:
        """Test for build_property() with a static property."""
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
        actual: Sequence[str] = build_property(
            obj=obj, import_list=imports, doc_tree=doc, line_length=line_length
        )

        assert actual == expected
        assert imports.types == {ImportList.CLASS_VAR, "Namespace.Type", ImportList.FINAL}

    def test_static_setter(self, imports: ImportList, doc: DocNode, line_length: int) -> None:
        """Test for build_property() with a static property with a setter."""
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
        actual: Sequence[str] = build_property(
            obj=obj, import_list=imports, doc_tree=doc, line_length=line_length
        )

        assert actual == expected
        assert imports.types == {ImportList.CLASS_VAR, "Namespace.Type"}


class TestBuildMethod:
    """Tests for build_method()."""

    def test_basic(self, imports: ImportList, doc: DocNode, line_length: int) -> None:
        """Test for build_method() with a basic method."""
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
        actual: Sequence[str] = build_method(
            obj=obj,
            import_list=imports,
            doc_tree=doc,
            overload=False,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == set()

    def test_parameters(self, imports: ImportList, doc: DocNode, line_length: int) -> None:
        """Test for build_method() with a method with parameters."""
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
        actual: Sequence[str] = build_method(
            obj=obj,
            import_list=imports,
            doc_tree=doc,
            overload=False,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {"Namespace.Type"}

    def test_return(self, imports: ImportList, doc: DocNode, line_length: int) -> None:
        """Test for build_method() with a method with multiple returns."""
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
        actual: Sequence[str] = build_method(
            obj=obj,
            import_list=imports,
            doc_tree=doc,
            overload=False,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {"Namespace.Type"}

    def test_overload(self, imports: ImportList, doc: DocNode, line_length: int) -> None:
        """Test for build_method() with an overloaded method."""
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
        actual: Sequence[str] = build_method(
            obj=obj,
            import_list=imports,
            doc_tree=doc,
            overload=True,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {ImportList.OVERLOAD}

    def test_static(self, imports: ImportList, doc: DocNode, line_length: int) -> None:
        """Test for build_method() with a static method."""
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
        actual: Sequence[str] = build_method(
            obj=obj,
            import_list=imports,
            doc_tree=doc,
            overload=False,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == set()

    def test_static_parameters(self, imports: ImportList, doc: DocNode, line_length: int) -> None:
        """Test for build_method() with a static method with parameters."""
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
        actual: Sequence[str] = build_method(
            obj=obj,
            import_list=imports,
            doc_tree=doc,
            overload=False,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {"Namespace.Type"}

    def test_static_returns(self, imports: ImportList, doc: DocNode, line_length: int) -> None:
        """Test for build_method() with a static method with multiple returns."""
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
        actual: Sequence[str] = build_method(
            obj=obj,
            import_list=imports,
            doc_tree=doc,
            overload=False,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {"Namespace.Type"}

    def test_static_overload(self, imports: ImportList, doc: DocNode, line_length: int) -> None:
        """Test for build_method() with an overloaded static method."""
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
        actual: Sequence[str] = build_method(
            obj=obj,
            import_list=imports,
            doc_tree=doc,
            overload=True,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {ImportList.OVERLOAD}


class TestBuildEvent:
    """Tests for build_event()."""

    def test_basic(self, imports: ImportList, doc: DocNode, line_length: int) -> None:
        """Test for build_event() with a basic event."""
        obj: CEvent = CEvent(
            name="Event",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="Type", namespace="Namespace"),
        )

        expected: Sequence[str] = [
            "Event: EventType[Type] = ...",
            '""""""',
        ]
        actual: Sequence[str] = build_event(
            obj=obj,
            import_list=imports,
            doc_tree=doc,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {"Namespace.Type", ImportList.EVENT_TYPE}


class TestBuildClass:
    """Tests for build_class()."""

    def test_basic(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_class() with a basic class."""
        obj: CClass = CClass(name="Name", namespace="Namespace")

        expected: Sequence[str] = [
            "class Name:",
            '    """"""',
        ]
        actual: Sequence[str] = build_class(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected

    def test_abstract(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_class() with an abstract class."""
        obj: CClass = CClass(name="Name", namespace="Namespace", abstract=True)

        expected: Sequence[str] = [
            "class Name(ABC):",
            '    """"""',
        ]
        actual: Sequence[str] = build_class(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {ImportList.ABC}

    def test_generic(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_class() with a class with generic arguments."""
        obj: CClass = CClass(
            name="Name",
            namespace="Namespace",
            generic_args=(CType(name="A", generic=True), CType(name="B", generic=True)),
        )

        expected: Sequence[str] = [
            "class Name[A, B]:",
            '    """"""',
        ]
        actual: Sequence[str] = build_class(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected

    def test_super(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_class() with a class with a suber class."""
        obj: CClass = CClass(
            name="Name",
            namespace="Namespace",
            super_class=CType(name="Super", namespace="Namespace"),
        )

        expected: Sequence[str] = [
            "class Name(Super):",
            '    """"""',
        ]
        actual: Sequence[str] = build_class(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {"Namespace.Super"}

    def test_interfaces(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_class() with a class with interfaces."""
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
        actual: Sequence[str] = build_class(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {"Namespace.InterfaceA", "Namespace.InterfaceB"}

    def test_fields(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_class() with a class with fields."""
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
        actual: Sequence[str] = build_class(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {ImportList.FINAL, "Namespace.Type"}

    def test_constructor(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_class() with a class with a constructor."""
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
        actual: Sequence[str] = build_class(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == set()

    def test_constructors(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_class() with a class with constructors."""
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
        actual: Sequence[str] = build_class(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {ImportList.OVERLOAD, "Namespace.Type"}

    def test_properties(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_class() with a class with properties."""
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
        actual: Sequence[str] = build_class(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {"Namespace.Type"}

    def test_methods(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_class() with a class with methods."""
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
        actual: Sequence[str] = build_class(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {"Namespace.Type"}

    def test_methods_overload(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_class() with a class with overloaded methods."""
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
        actual: Sequence[str] = build_class(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {ImportList.OVERLOAD, "Namespace.Type"}

    def test_events(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_class() with a class with events."""
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
        actual: Sequence[str] = build_class(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {"Namespace.Type", ImportList.EVENT_TYPE}

    def test_nested_types(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_class() with a class with nested types."""
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
        actual: Sequence[str] = build_class(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {ImportList.CALLABLE, ImportList.ENUM, "Namespace.Type"}


class TestBuildStruct:
    """Tests for build_struct()."""

    def test_basic(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_struct() with a basic struct."""
        obj: CStruct = CStruct(name="Name", namespace="Namespace")

        expected: Sequence[str] = [
            "class Name:",
            '    """"""',
        ]
        actual: Sequence[str] = build_struct(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected

    def test_abstract(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_struct() with an abstract struct."""
        obj: CStruct = CStruct(name="Name", namespace="Namespace", abstract=True)

        expected: Sequence[str] = [
            "class Name(ABC):",
            '    """"""',
        ]
        actual: Sequence[str] = build_struct(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {ImportList.ABC}

    def test_generic(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_struct() with a struct with generic arguments."""
        obj: CStruct = CStruct(
            name="Name",
            namespace="Namespace",
            generic_args=(CType(name="A", generic=True), CType(name="B", generic=True)),
        )

        expected: Sequence[str] = [
            "class Name[A, B]:",
            '    """"""',
        ]
        actual: Sequence[str] = build_struct(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected

    def test_super(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_struct() with a struct with a suber class."""
        obj: CStruct = CStruct(
            name="Name",
            namespace="Namespace",
            super_class=CType(name="Super", namespace="Namespace"),
        )

        expected: Sequence[str] = [
            "class Name(Super):",
            '    """"""',
        ]
        actual: Sequence[str] = build_struct(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {"Namespace.Super"}

    def test_interfaces(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_struct() with a struct with interfaces."""
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
        actual: Sequence[str] = build_struct(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {"Namespace.InterfaceA", "Namespace.InterfaceB"}

    def test_fields(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_struct() with a struct with fields."""
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
        actual: Sequence[str] = build_struct(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {ImportList.FINAL, "Namespace.Type"}

    def test_constructor(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_struct() with a struct with a constructor."""
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
        actual: Sequence[str] = build_struct(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == set()

    def test_constructors(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_struct() with a struct with constructors."""
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
        actual: Sequence[str] = build_struct(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {ImportList.OVERLOAD, "Namespace.Type"}

    def test_properties(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_struct() with a struct with properties."""
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
        actual: Sequence[str] = build_struct(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {"Namespace.Type"}

    def test_methods(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_struct() with a struct with methods."""
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
        actual: Sequence[str] = build_struct(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {"Namespace.Type"}

    def test_methods_overload(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_struct() with a struct with overloaded methods."""
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
        actual: Sequence[str] = build_struct(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {ImportList.OVERLOAD, "Namespace.Type"}

    def test_events(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_struct() with a struct with events."""
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
        actual: Sequence[str] = build_struct(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {"Namespace.Type", ImportList.EVENT_TYPE}

    def test_nested_types(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_struct() with a struct with nested types."""
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
        actual: Sequence[str] = build_struct(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {ImportList.CALLABLE, ImportList.ENUM, "Namespace.Type"}


class TestBuildInterface:
    """Tests for build_interface()."""

    def test_basic(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_interface() with a basic interface."""
        obj: CInterface = CInterface(name="Name", namespace="Namespace")

        expected: Sequence[str] = [
            "class Name:",
            '    """"""',
        ]
        actual: Sequence[str] = build_interface(
            obj=obj, doc_tree=doc, import_list=imports, line_length=line_length
        )

        assert actual == expected

    def test_generic(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_interface() with an interface with generic arguments."""
        obj: CInterface = CInterface(
            name="Name",
            namespace="Namespace",
            generic_args=(CType(name="A", generic=True), CType(name="B", generic=True)),
        )

        expected: Sequence[str] = [
            "class Name[A, B]:",
            '    """"""',
        ]
        actual: Sequence[str] = build_interface(
            obj=obj, doc_tree=doc, import_list=imports, line_length=line_length
        )

        assert actual == expected

    def test_interfaces(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_interface() with an interface with interfaces."""
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
        actual: Sequence[str] = build_interface(
            obj=obj, doc_tree=doc, import_list=imports, line_length=line_length
        )

        assert actual == expected
        assert imports.types == {"Namespace.InterfaceA", "Namespace.InterfaceB"}

    def test_fields(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_interface() with an interface with fields."""
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
        actual: Sequence[str] = build_interface(
            obj=obj, doc_tree=doc, import_list=imports, line_length=line_length
        )

        assert actual == expected
        assert imports.types == {ImportList.FINAL, "Namespace.Type"}

    def test_properties(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_interface() with an interface with properties."""
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
        actual: Sequence[str] = build_interface(
            obj=obj, doc_tree=doc, import_list=imports, line_length=line_length
        )

        assert actual == expected
        assert imports.types == {"Namespace.Type"}

    def test_methods(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_interface() with an interface with methods."""
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
        actual: Sequence[str] = build_interface(
            obj=obj, doc_tree=doc, import_list=imports, line_length=line_length
        )

        assert actual == expected
        assert imports.types == {"Namespace.Type"}

    def test_methods_overload(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_interface() with an interface with overloaded methods."""
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
        actual: Sequence[str] = build_interface(
            obj=obj, doc_tree=doc, import_list=imports, line_length=line_length
        )

        assert actual == expected
        assert imports.types == {ImportList.OVERLOAD, "Namespace.Type"}

    def test_events(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_interface() with an interface with events."""
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
        actual: Sequence[str] = build_interface(
            obj=obj, doc_tree=doc, import_list=imports, line_length=line_length
        )

        assert actual == expected
        assert imports.types == {"Namespace.Type", ImportList.EVENT_TYPE}

    def test_nested_types(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_interface() with an interface with nested types."""
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
        actual: Sequence[str] = build_interface(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {ImportList.CALLABLE, ImportList.ENUM, "Namespace.Type"}


class TestBuildEnum:
    """Tests for build_enum()."""

    def test_basic(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_enum() with a basic enum."""
        obj: CEnum = CEnum(name="Name", namespace="Namespace")

        expected: Sequence[str] = [
            "class Name(Enum):",
            '    """"""',
        ]
        actual: Sequence[str] = build_enum(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {ImportList.ENUM}

    def test_fields(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_enum() with an enum with multiple fields."""
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
        actual: Sequence[str] = build_enum(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {ImportList.ENUM}


class TestBuildDelegate:
    """Tests for build_delegate()."""

    def test_basic(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_delegate() with a basic delegate."""
        obj: CDelegate = CDelegate(name="Name", namespace="Namespace")

        expected: Sequence[str] = [
            "Name: Callable[[], None] = ...",
            '""""""',
        ]
        actual: Sequence[str] = build_delegate(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {ImportList.CALLABLE}

    def test_parameters(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_delegate() with a delegate with parameters."""
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
        actual: Sequence[str] = build_delegate(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {ImportList.CALLABLE, "Namespace.Type"}

    def test_return(self, doc: DocNode, imports: ImportList, line_length: int) -> None:
        """Test for build_delegate() with a delegate with parameters."""
        obj: CDelegate = CDelegate(
            name="Name",
            namespace="Namespace",
            return_type=CType(name="Type", namespace="Namespace"),
        )

        expected: Sequence[str] = [
            "Name: Callable[[], Type] = ...",
            '""""""',
        ]
        actual: Sequence[str] = build_delegate(
            obj=obj,
            doc_tree=doc,
            import_list=imports,
            line_length=line_length,
        )

        assert actual == expected
        assert imports.types == {ImportList.CALLABLE, "Namespace.Type"}


class TestBuildNamespace:
    """Tests for build_namespace()."""

    def test_basic(self, doc: DocNode, line_length: int) -> None:
        """Test for build_namespace() with a basic namespace."""
        obj: CNamespace = CNamespace(
            name="Name",
            types={},
        )

        expected: Sequence[str] = [
            '"""Automatically generated stubs for C# namespace: Name."""',
            "",
        ]
        actual: Sequence[str] = build_namespace(
            obj=obj,
            doc_tree=doc,
            line_length=line_length,
        )

        assert actual == expected

    def test_types(self, doc: DocNode, line_length: int) -> None:
        """Test for build_namespace() with a basic namespace."""
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
        actual: Sequence[str] = build_namespace(
            obj=obj,
            doc_tree=doc,
            line_length=line_length,
        )

        assert actual == expected


# class TestBuildStubs:
#     output_dir: Path
#
#     @classmethod
#     def setUpClass(cls) -> None:
#         cls.output_dir = Path("output")
#         cls.output_dir.mkdir(parents=True, exist_ok=True)
#
#     def test_build_test_lib(self) -> None:
#         skeleton_name: str = "TestLib_1.0.0.0_skeleton.json"
#         doc_name: str = "TestLib_1.0.0.0_doc.json"
#
#         result = build_stubs(
#             skeleton_files=(Path(skeleton_name),),
#             doc_files=(Path(doc_name),),
#             output_dir=self.output_dir,
#             line_length=100,
#             multi_threaded=False,
#             format_files=True,
#         )
#
#         self.assertEqual(0, result)


if __name__ == "__main__":
    pytest.main()
