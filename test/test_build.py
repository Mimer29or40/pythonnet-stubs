import unittest
from pathlib import Path
from typing import Any
from typing import Mapping
from typing import Sequence
from typing import Set
from typing import Tuple

from stubgen.build_stubs import merge_class
from stubgen.build_stubs import merge_constructor
from stubgen.build_stubs import merge_delegate
from stubgen.build_stubs import merge_enum
from stubgen.build_stubs import merge_event
from stubgen.build_stubs import merge_field
from stubgen.build_stubs import merge_interface
from stubgen.build_stubs import merge_method
from stubgen.build_stubs import merge_property
from stubgen.build_stubs import merge_struct
from stubgen.build_stubs import merge_type_def
from stubgen.model import CTypeDefinition
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
from stubgen.build_stubs import build_parameter
from stubgen.build_stubs import build_property
from stubgen.build_stubs import build_struct
from stubgen.build_stubs import build_stubs
from stubgen.build_stubs import build_type
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
    def test_merge(self) -> None:
        namespace1: CNamespace = CNamespace(
            name="Namespace",
            types={},
        )
        namespace2: CNamespace = CNamespace(
            name="Namespace",
            types={},
        )

        merged: CNamespace = merge_namespace(namespace1, namespace2)
        expected: CNamespace = CNamespace(
            name="Namespace",
            types={},
        )

        self.assertEqual(expected, merged)

    def test_merge_types(self) -> None:
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
                "Namespace:ClassC": CClass(
                    name="ClassC",
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
        expected: CNamespace = CNamespace(
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
                "Namespace:ClassC": CClass(
                    name="ClassC",
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

        self.assertEqual(expected, merged)

    def test_merge_error_name(self) -> None:
        namespace1: CNamespace = CNamespace(name="NamespaceA", types={})
        namespace2: CNamespace = CNamespace(name="NamespaceB", types={})

        self.assertRaises(AttributeError, lambda: merge_namespace(namespace1, namespace2))


class TestMergeTypeDefinition(TestBase):
    def test_merge_error_type(self) -> None:
        type_def1: CTypeDefinition = CClass(
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
        type_def2: CTypeDefinition = CStruct(
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

        self.assertRaises(TypeError, lambda: merge_type_def(type_def1, type_def2))

    def test_merge_error_name(self) -> None:
        type_def1: CTypeDefinition = CClass(
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
        )
        type_def2: CTypeDefinition = CClass(
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
        )

        self.assertRaises(AttributeError, lambda: merge_type_def(type_def1, type_def2))

    def test_merge_error_namespace(self) -> None:
        type_def1: CTypeDefinition = CClass(
            name="Class",
            namespace="NamespaceA",
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
        type_def2: CTypeDefinition = CClass(
            name="Class",
            namespace="NamespaceB",
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

        self.assertRaises(AttributeError, lambda: merge_type_def(type_def1, type_def2))

    def test_merge_error_nested(self) -> None:
        type_def1: CTypeDefinition = CClass(
            name="Class",
            namespace="Namespace",
            nested=CType(name="TypeA"),
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
        type_def2: CTypeDefinition = CClass(
            name="Class",
            namespace="Namespace",
            nested=CType(name="TypeB"),
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

        self.assertRaises(AttributeError, lambda: merge_type_def(type_def1, type_def2))


class TestMergeClass(TestBase):
    def test_merge_fields(self) -> None:
        class1: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={
                "Namespace.Class.FieldA": CField(
                    name="FieldA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    return_type=CType(name="ReturnType"),
                ),
                "Namespace.Class.FieldB": CField(
                    name="FieldB",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    return_type=CType(name="ReturnType"),
                ),
            },
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        class2: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={
                "Namespace.Class.FieldA": CField(
                    name="FieldA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    return_type=CType(name="ReturnType"),
                ),
                "Namespace.Class.FieldC": CField(
                    name="FieldC",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    return_type=CType(name="ReturnType"),
                ),
            },
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )

        result: CTypeDefinition = merge_class(class1, class2)
        expected: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=True,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={
                "Namespace.Class.FieldA": CField(
                    name="FieldA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    return_type=CType(name="ReturnType"),
                ),
                "Namespace.Class.FieldB": CField(
                    name="FieldB",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    return_type=CType(name="ReturnType"),
                ),
                "Namespace.Class.FieldC": CField(
                    name="FieldC",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    return_type=CType(name="ReturnType"),
                ),
            },
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )

        self.assertEqual(expected, result)

    def test_merge_constructors(self) -> None:
        class1: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={
                "Namespace.Class.__init__()": CConstructor(
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(),
                ),
                "Namespace.Class.__init__(ParamType)": CConstructor(
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="ParamType")),
                    ),
                ),
            },
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        class2: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={
                "Namespace.Class.__init__()": CConstructor(
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(),
                ),
                "Namespace.Class.__init__(ParamType, ParamType)": CConstructor(
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="ParamType")),
                        CParameter(name="param1", type=CType(name="ParamType")),
                    ),
                ),
            },
            properties={},
            methods={},
            events={},
            nested_types={},
        )

        result: CTypeDefinition = merge_class(class1, class2)
        expected: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=True,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={
                "Namespace.Class.__init__()": CConstructor(
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(),
                ),
                "Namespace.Class.__init__(ParamType)": CConstructor(
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="ParamType")),
                    ),
                ),
                "Namespace.Class.__init__(ParamType, ParamType)": CConstructor(
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="ParamType")),
                        CParameter(name="param1", type=CType(name="ParamType")),
                    ),
                ),
            },
            properties={},
            methods={},
            events={},
            nested_types={},
        )

        self.assertEqual(expected, result)

    def test_merge_properties(self) -> None:
        class1: CClass = CClass(
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
                "Namespace.Class.PropertyA": CProperty(
                    name="PropertyA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="PropertyType"),
                ),
                "Namespace.Class.PropertyB": CProperty(
                    name="PropertyB",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="PropertyType"),
                ),
            },
            methods={},
            events={},
            nested_types={},
        )
        class2: CClass = CClass(
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
                "Namespace.Class.PropertyA": CProperty(
                    name="PropertyA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="PropertyType"),
                ),
                "Namespace.Class.PropertyC": CProperty(
                    name="PropertyC",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="PropertyType"),
                ),
            },
            methods={},
            events={},
            nested_types={},
        )

        result: CTypeDefinition = merge_class(class1, class2)
        expected: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=True,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={
                "Namespace.Class.PropertyA": CProperty(
                    name="PropertyA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="PropertyType"),
                ),
                "Namespace.Class.PropertyB": CProperty(
                    name="PropertyB",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="PropertyType"),
                ),
                "Namespace.Class.PropertyC": CProperty(
                    name="PropertyC",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="PropertyType"),
                ),
            },
            methods={},
            events={},
            nested_types={},
        )

        self.assertEqual(expected, result)

    def test_merge_methods(self) -> None:
        class1: CClass = CClass(
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
                "Namespace.Class.MethodA(ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="ParamType")),
                    ),
                    return_types=(CType(name="PropertyType"),),
                ),
                "Namespace.Class.MethodB(ParamType)": CMethod(
                    name="MethodB",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="ParamType")),
                    ),
                    return_types=(CType(name="PropertyType"),),
                ),
            },
            events={},
            nested_types={},
        )
        class2: CClass = CClass(
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
                "Namespace.Class.MethodA(ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="ParamType")),
                    ),
                    return_types=(CType(name="PropertyType"),),
                ),
                "Namespace.Class.MethodC(ParamType)": CMethod(
                    name="MethodC",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="ParamType")),
                    ),
                    return_types=(CType(name="PropertyType"),),
                ),
            },
            events={},
            nested_types={},
        )

        result: CTypeDefinition = merge_class(class1, class2)
        expected: CClass = CClass(
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
                "Namespace.Class.MethodA(ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="ParamType")),
                    ),
                    return_types=(CType(name="PropertyType"),),
                ),
                "Namespace.Class.MethodB(ParamType)": CMethod(
                    name="MethodB",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="ParamType")),
                    ),
                    return_types=(CType(name="PropertyType"),),
                ),
                "Namespace.Class.MethodC(ParamType)": CMethod(
                    name="MethodC",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="ParamType")),
                    ),
                    return_types=(CType(name="PropertyType"),),
                ),
            },
            events={},
            nested_types={},
        )

        self.assertEqual(expected, result)

    def test_merge_events(self) -> None:
        class1: CClass = CClass(
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
                "Namespace.Class.EventA": CEvent(
                    name="EventA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="EventType"),
                ),
                "Namespace.Class.EventB": CEvent(
                    name="EventB",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="EventType"),
                ),
            },
            nested_types={},
        )
        class2: CClass = CClass(
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
                "Namespace.Class.EventA": CEvent(
                    name="EventA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="EventType"),
                ),
                "Namespace.Class.EventC": CEvent(
                    name="EventC",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="EventType"),
                ),
            },
            nested_types={},
        )

        result: CTypeDefinition = merge_class(class1, class2)
        expected: CClass = CClass(
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
                "Namespace.Class.EventA": CEvent(
                    name="EventA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="EventType"),
                ),
                "Namespace.Class.EventB": CEvent(
                    name="EventB",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="EventType"),
                ),
                "Namespace.Class.EventC": CEvent(
                    name="EventC",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="EventType"),
                ),
            },
            nested_types={},
        )

        self.assertEqual(expected, result)

    def test_merge_nested(self) -> None:
        class1: CClass = CClass(
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
                "Namespace:Class.NestedClassA": CClass(
                    name="NestedClassA",
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
                "Namespace:Class.NestedClassB": CClass(
                    name="NestedClassB",
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
            },
        )
        class2: CClass = CClass(
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
                "Namespace:Class.NestedClassA": CClass(
                    name="NestedClassA",
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
                "Namespace:Class.NestedClassC": CClass(
                    name="NestedClassC",
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
            },
        )

        result: CTypeDefinition = merge_class(class1, class2)
        expected: CClass = CClass(
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
                "Namespace:Class.NestedClassA": CClass(
                    name="NestedClassA",
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
                "Namespace:Class.NestedClassB": CClass(
                    name="NestedClassB",
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
                "Namespace:Class.NestedClassC": CClass(
                    name="NestedClassC",
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
            },
        )

        self.assertEqual(expected, result)

    def test_merge_error_abstract(self) -> None:
        class1: CClass = CClass(
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
        class2: CClass = CClass(
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

        self.assertRaises(AttributeError, lambda: merge_class(class1, class2))

    def test_merge_error_generic_args(self) -> None:
        class1: CClass = CClass(
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
        class2: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(CType(name="T"),),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )

        self.assertRaises(AttributeError, lambda: merge_class(class1, class2))

    def test_merge_error_super_class(self) -> None:
        class1: CClass = CClass(
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
        class2: CClass = CClass(
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

        self.assertRaises(AttributeError, lambda: merge_class(class1, class2))

    def test_merge_error_interfaces(self) -> None:
        class1: CClass = CClass(
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
        class2: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(CType(name="Interface", namespace="Namespace"),),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )

        self.assertRaises(AttributeError, lambda: merge_class(class1, class2))


class TestMergeStruct(TestBase):
    def test_merge_fields(self) -> None:
        struct1: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={
                "Namespace.Struct.FieldA": CField(
                    name="FieldA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    return_type=CType(name="ReturnType"),
                ),
                "Namespace.Struct.FieldB": CField(
                    name="FieldB",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    return_type=CType(name="ReturnType"),
                ),
            },
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        struct2: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={
                "Namespace.Struct.FieldA": CField(
                    name="FieldA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    return_type=CType(name="ReturnType"),
                ),
                "Namespace.Struct.FieldC": CField(
                    name="FieldC",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    return_type=CType(name="ReturnType"),
                ),
            },
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )

        result: CTypeDefinition = merge_struct(struct1, struct2)
        expected: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={
                "Namespace.Struct.FieldA": CField(
                    name="FieldA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    return_type=CType(name="ReturnType"),
                ),
                "Namespace.Struct.FieldB": CField(
                    name="FieldB",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    return_type=CType(name="ReturnType"),
                ),
                "Namespace.Struct.FieldC": CField(
                    name="FieldC",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    return_type=CType(name="ReturnType"),
                ),
            },
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )

        self.assertEqual(expected, result)

    def test_merge_constructors(self) -> None:
        struct1: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={
                "Namespace.Struct.__init__()": CConstructor(
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(),
                ),
                "Namespace.Struct.__init__(ParamType)": CConstructor(
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="ParamType")),
                    ),
                ),
            },
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        struct2: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={
                "Namespace.Struct.__init__()": CConstructor(
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(),
                ),
                "Namespace.Struct.__init__(ParamType, ParamType)": CConstructor(
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="ParamType")),
                        CParameter(name="param1", type=CType(name="ParamType")),
                    ),
                ),
            },
            properties={},
            methods={},
            events={},
            nested_types={},
        )

        result: CTypeDefinition = merge_struct(struct1, struct2)
        expected: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=True,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={
                "Namespace.Struct.__init__()": CConstructor(
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(),
                ),
                "Namespace.Struct.__init__(ParamType)": CConstructor(
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="ParamType")),
                    ),
                ),
                "Namespace.Struct.__init__(ParamType, ParamType)": CConstructor(
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="ParamType")),
                        CParameter(name="param1", type=CType(name="ParamType")),
                    ),
                ),
            },
            properties={},
            methods={},
            events={},
            nested_types={},
        )

        self.assertEqual(expected, result)

    def test_merge_properties(self) -> None:
        struct1: CStruct = CStruct(
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
                "Namespace.Struct.PropertyA": CProperty(
                    name="PropertyA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="PropertyType"),
                ),
                "Namespace.Struct.PropertyB": CProperty(
                    name="PropertyB",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="PropertyType"),
                ),
            },
            methods={},
            events={},
            nested_types={},
        )
        struct2: CStruct = CStruct(
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
                "Namespace.Struct.PropertyA": CProperty(
                    name="PropertyA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="PropertyType"),
                ),
                "Namespace.Struct.PropertyC": CProperty(
                    name="PropertyC",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="PropertyType"),
                ),
            },
            methods={},
            events={},
            nested_types={},
        )

        result: CTypeDefinition = merge_struct(struct1, struct2)
        expected: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=True,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={
                "Namespace.Struct.PropertyA": CProperty(
                    name="PropertyA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="PropertyType"),
                ),
                "Namespace.Struct.PropertyB": CProperty(
                    name="PropertyB",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="PropertyType"),
                ),
                "Namespace.Struct.PropertyC": CProperty(
                    name="PropertyC",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="PropertyType"),
                ),
            },
            methods={},
            events={},
            nested_types={},
        )

        self.assertEqual(expected, result)

    def test_merge_methods(self) -> None:
        struct1: CStruct = CStruct(
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
                "Namespace.Struct.MethodA(ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="ParamType")),
                    ),
                    return_types=(CType(name="PropertyType"),),
                ),
                "Namespace.Struct.MethodB(ParamType)": CMethod(
                    name="MethodB",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="ParamType")),
                    ),
                    return_types=(CType(name="PropertyType"),),
                ),
            },
            events={},
            nested_types={},
        )
        struct2: CStruct = CStruct(
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
                "Namespace.Struct.MethodA(ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="ParamType")),
                    ),
                    return_types=(CType(name="PropertyType"),),
                ),
                "Namespace.Struct.MethodC(ParamType)": CMethod(
                    name="MethodC",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="ParamType")),
                    ),
                    return_types=(CType(name="PropertyType"),),
                ),
            },
            events={},
            nested_types={},
        )

        result: CTypeDefinition = merge_struct(struct1, struct2)
        expected: CStruct = CStruct(
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
                "Namespace.Struct.MethodA(ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="ParamType")),
                    ),
                    return_types=(CType(name="PropertyType"),),
                ),
                "Namespace.Struct.MethodB(ParamType)": CMethod(
                    name="MethodB",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="ParamType")),
                    ),
                    return_types=(CType(name="PropertyType"),),
                ),
                "Namespace.Struct.MethodC(ParamType)": CMethod(
                    name="MethodC",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="ParamType")),
                    ),
                    return_types=(CType(name="PropertyType"),),
                ),
            },
            events={},
            nested_types={},
        )

        self.assertEqual(expected, result)

    def test_merge_events(self) -> None:
        struct1: CStruct = CStruct(
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
                "Namespace.Struct.EventA": CEvent(
                    name="EventA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="EventType"),
                ),
                "Namespace.Struct.EventB": CEvent(
                    name="EventB",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="EventType"),
                ),
            },
            nested_types={},
        )
        struct2: CStruct = CStruct(
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
                "Namespace.Struct.EventA": CEvent(
                    name="EventA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="EventType"),
                ),
                "Namespace.Struct.EventC": CEvent(
                    name="EventC",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="EventType"),
                ),
            },
            nested_types={},
        )

        result: CTypeDefinition = merge_struct(struct1, struct2)
        expected: CStruct = CStruct(
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
                "Namespace.Struct.EventA": CEvent(
                    name="EventA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="EventType"),
                ),
                "Namespace.Struct.EventB": CEvent(
                    name="EventB",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="EventType"),
                ),
                "Namespace.Struct.EventC": CEvent(
                    name="EventC",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="EventType"),
                ),
            },
            nested_types={},
        )

        self.assertEqual(expected, result)

    def test_merge_nested(self) -> None:
        struct1: CStruct = CStruct(
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
                "Namespace:Struct.NestedClassA": CClass(
                    name="NestedClassA",
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
                "Namespace:Struct.NestedClassB": CClass(
                    name="NestedClassB",
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
            },
        )
        struct2: CStruct = CStruct(
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
                "Namespace:Struct.NestedClassA": CClass(
                    name="NestedClassA",
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
                "Namespace:Struct.NestedClassC": CClass(
                    name="NestedClassC",
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
            },
        )

        result: CTypeDefinition = merge_struct(struct1, struct2)
        expected: CStruct = CStruct(
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
                "Namespace:Struct.NestedClassA": CClass(
                    name="NestedClassA",
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
                "Namespace:Struct.NestedClassB": CClass(
                    name="NestedClassB",
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
                "Namespace:Struct.NestedClassC": CClass(
                    name="NestedClassC",
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
            },
        )

        self.assertEqual(expected, result)

    def test_merge_error_abstract(self) -> None:
        struct1: CStruct = CStruct(
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
        struct2: CStruct = CStruct(
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

        self.assertRaises(AttributeError, lambda: merge_struct(struct1, struct2))

    def test_merge_error_generic_args(self) -> None:
        struct1: CStruct = CStruct(
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
        struct2: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(CType(name="T"),),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )

        self.assertRaises(AttributeError, lambda: merge_struct(struct1, struct2))

    def test_merge_error_super_class(self) -> None:
        struct1: CStruct = CStruct(
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
        struct2: CStruct = CStruct(
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

        self.assertRaises(AttributeError, lambda: merge_struct(struct1, struct2))

    def test_merge_error_interfaces(self) -> None:
        struct1: CStruct = CStruct(
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
        struct2: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(CType(name="Interface", namespace="Namespace"),),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )

        self.assertRaises(AttributeError, lambda: merge_struct(struct1, struct2))


class TestMergeInterface(TestBase):
    def test_merge_fields(self) -> None:
        interface1: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={
                "Namespace.Interface.FieldA": CField(
                    name="FieldA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    return_type=CType(name="ReturnType"),
                ),
                "Namespace.Interface.FieldB": CField(
                    name="FieldB",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    return_type=CType(name="ReturnType"),
                ),
            },
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        interface2: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={
                "Namespace.Interface.FieldA": CField(
                    name="FieldA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    return_type=CType(name="ReturnType"),
                ),
                "Namespace.Interface.FieldC": CField(
                    name="FieldC",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    return_type=CType(name="ReturnType"),
                ),
            },
            properties={},
            methods={},
            events={},
            nested_types={},
        )

        result: CTypeDefinition = merge_interface(interface1, interface2)
        expected: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={
                "Namespace.Interface.FieldA": CField(
                    name="FieldA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    return_type=CType(name="ReturnType"),
                ),
                "Namespace.Interface.FieldB": CField(
                    name="FieldB",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    return_type=CType(name="ReturnType"),
                ),
                "Namespace.Interface.FieldC": CField(
                    name="FieldC",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    return_type=CType(name="ReturnType"),
                ),
            },
            properties={},
            methods={},
            events={},
            nested_types={},
        )

        self.assertEqual(expected, result)

    def test_merge_properties(self) -> None:
        interface1: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={
                "Namespace.Interface.PropertyA": CProperty(
                    name="PropertyA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="PropertyType"),
                ),
                "Namespace.Interface.PropertyB": CProperty(
                    name="PropertyB",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="PropertyType"),
                ),
            },
            methods={},
            events={},
            nested_types={},
        )
        interface2: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={
                "Namespace.Interface.PropertyA": CProperty(
                    name="PropertyA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="PropertyType"),
                ),
                "Namespace.Interface.PropertyC": CProperty(
                    name="PropertyC",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="PropertyType"),
                ),
            },
            methods={},
            events={},
            nested_types={},
        )

        result: CTypeDefinition = merge_interface(interface1, interface2)
        expected: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={
                "Namespace.Interface.PropertyA": CProperty(
                    name="PropertyA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="PropertyType"),
                ),
                "Namespace.Interface.PropertyB": CProperty(
                    name="PropertyB",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="PropertyType"),
                ),
                "Namespace.Interface.PropertyC": CProperty(
                    name="PropertyC",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="PropertyType"),
                ),
            },
            methods={},
            events={},
            nested_types={},
        )

        self.assertEqual(expected, result)

    def test_merge_methods(self) -> None:
        interface1: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={
                "Namespace.Interface.MethodA(ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="ParamType")),
                    ),
                    return_types=(CType(name="PropertyType"),),
                ),
                "Namespace.Interface.MethodB(ParamType)": CMethod(
                    name="MethodB",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="ParamType")),
                    ),
                    return_types=(CType(name="PropertyType"),),
                ),
            },
            events={},
            nested_types={},
        )
        interface2: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={
                "Namespace.Interface.MethodA(ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="ParamType")),
                    ),
                    return_types=(CType(name="PropertyType"),),
                ),
                "Namespace.Interface.MethodC(ParamType)": CMethod(
                    name="MethodC",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="ParamType")),
                    ),
                    return_types=(CType(name="PropertyType"),),
                ),
            },
            events={},
            nested_types={},
        )

        result: CTypeDefinition = merge_interface(interface1, interface2)
        expected: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={
                "Namespace.Interface.MethodA(ParamType)": CMethod(
                    name="MethodA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="ParamType")),
                    ),
                    return_types=(CType(name="PropertyType"),),
                ),
                "Namespace.Interface.MethodB(ParamType)": CMethod(
                    name="MethodB",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="ParamType")),
                    ),
                    return_types=(CType(name="PropertyType"),),
                ),
                "Namespace.Interface.MethodC(ParamType)": CMethod(
                    name="MethodC",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="ParamType")),
                    ),
                    return_types=(CType(name="PropertyType"),),
                ),
            },
            events={},
            nested_types={},
        )

        self.assertEqual(expected, result)

    def test_merge_events(self) -> None:
        interface1: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            events={
                "Namespace.Interface.EventA": CEvent(
                    name="EventA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="EventType"),
                ),
                "Namespace.Interface.EventB": CEvent(
                    name="EventB",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="EventType"),
                ),
            },
            nested_types={},
        )
        interface2: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            events={
                "Namespace.Interface.EventA": CEvent(
                    name="EventA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="EventType"),
                ),
                "Namespace.Interface.EventC": CEvent(
                    name="EventC",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="EventType"),
                ),
            },
            nested_types={},
        )

        result: CTypeDefinition = merge_interface(interface1, interface2)
        expected: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            events={
                "Namespace.Interface.EventA": CEvent(
                    name="EventA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="EventType"),
                ),
                "Namespace.Interface.EventB": CEvent(
                    name="EventB",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="EventType"),
                ),
                "Namespace.Interface.EventC": CEvent(
                    name="EventC",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="EventType"),
                ),
            },
            nested_types={},
        )

        self.assertEqual(expected, result)

    def test_merge_nested(self) -> None:
        interface1: CInterface = CInterface(
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
                "Namespace:Interface.NestedClassA": CClass(
                    name="NestedClassA",
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
                "Namespace:Interface.NestedClassB": CClass(
                    name="NestedClassB",
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
            },
        )
        interface2: CInterface = CInterface(
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
                "Namespace:Interface.NestedClassA": CClass(
                    name="NestedClassA",
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
                "Namespace:Interface.NestedClassC": CClass(
                    name="NestedClassC",
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
            },
        )

        result: CTypeDefinition = merge_interface(interface1, interface2)
        expected: CInterface = CInterface(
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
                "Namespace:Interface.NestedClassA": CClass(
                    name="NestedClassA",
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
                "Namespace:Interface.NestedClassB": CClass(
                    name="NestedClassB",
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
                "Namespace:Interface.NestedClassC": CClass(
                    name="NestedClassC",
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
            },
        )

        self.assertEqual(expected, result)

    def test_merge_error_generic_args(self) -> None:
        interface1: CInterface = CInterface(
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
        interface2: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(CType(name="T"),),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )

        self.assertRaises(AttributeError, lambda: merge_interface(interface1, interface2))

    def test_merge_error_interfaces(self) -> None:
        interface1: CInterface = CInterface(
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
        interface2: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(CType(name="Interface", namespace="Namespace"),),
            fields={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )

        self.assertRaises(AttributeError, lambda: merge_interface(interface1, interface2))


class TestMergeEnum(TestBase):
    def test_merge(self) -> None:
        enum1: CEnum = CEnum(
            name="Enum",
            namespace="Namespace",
            nested=None,
            fields=("FieldA", "FieldB", "FieldC", "FieldD"),
        )
        enum2: CEnum = CEnum(
            name="Enum",
            namespace="Namespace",
            nested=None,
            fields=("FieldA", "FieldB", "FieldC", "FieldD"),
        )

        result: CTypeDefinition = merge_type_def(enum1, enum2)
        expected: CEnum = CEnum(
            name="Enum",
            namespace="Namespace",
            nested=None,
            fields=("FieldA", "FieldB", "FieldC", "FieldD"),
        )

        self.assertEqual(expected, result)

    def test_merge_error_fields(self) -> None:
        enum1: CEnum = CEnum(
            name="Enum",
            namespace="Namespace",
            nested=None,
            fields=("FieldA", "FieldB", "FieldC", "FieldD"),
        )
        enum2: CEnum = CEnum(
            name="Enum",
            namespace="Namespace",
            nested=None,
            fields=("FieldA", "FieldB", "FieldC", "FieldD", "FieldE"),
        )

        self.assertRaises(AttributeError, lambda: merge_enum(enum1, enum2))


class TestMergeDelegate(TestBase):
    def test_merge(self) -> None:
        delegate1: CDelegate = CDelegate(
            name="Delegate",
            namespace="Namespace",
            nested=None,
            parameters=(
                CParameter(name="param0", type=CType(name="ParamType")),
            ),
            return_type=CType(name="ReturnType"),
        )
        delegate2: CDelegate = CDelegate(
            name="Delegate",
            namespace="Namespace",
            nested=None,
            parameters=(
                CParameter(name="param0", type=CType(name="ParamType")),
            ),
            return_type=CType(name="ReturnType"),
        )

        result: CTypeDefinition = merge_type_def(delegate1, delegate2)
        expected: CDelegate = CDelegate(
            name="Delegate",
            namespace="Namespace",
            nested=None,
            parameters=(
                CParameter(name="param0", type=CType(name="ParamType")),
            ),
            return_type=CType(name="ReturnType"),
        )

        self.assertEqual(expected, result)

    def test_merge_error_parameters(self) -> None:
        delegate1: CDelegate = CDelegate(
            name="Delegate",
            namespace="Namespace",
            nested=None,
            parameters=(
                CParameter(name="param0", type=CType(name="ParamType")),
            ),
            return_type=CType(name="ReturnType"),
        )
        delegate2: CDelegate = CDelegate(
            name="Delegate",
            namespace="Namespace",
            nested=None,
            parameters=(
                CParameter(name="param0", type=CType(name="ParamType")),
                CParameter(name="param1", type=CType(name="ParamType")),
            ),
            return_type=CType(name="ReturnType"),
        )

        self.assertRaises(AttributeError, lambda: merge_delegate(delegate1, delegate2))

    def test_merge_error_return_type(self) -> None:
        delegate1: CDelegate = CDelegate(
            name="Delegate",
            namespace="Namespace",
            nested=None,
            parameters=(
                CParameter(name="param0", type=CType(name="ParamType")),
            ),
            return_type=CType(name="ReturnTypeA"),
        )
        delegate2: CDelegate = CDelegate(
            name="Delegate",
            namespace="Namespace",
            nested=None,
            parameters=(
                CParameter(name="param0", type=CType(name="ParamType")),
            ),
            return_type=CType(name="ReturnTypeB"),
        )

        self.assertRaises(AttributeError, lambda: merge_delegate(delegate1, delegate2))


class TestMergeField(TestBase):
    def test_merge(self) -> None:
        field1: CField = CField(
            name="Field",
            declaring_type=CType(name="DeclaringType"),
            return_type=CType(name="ReturnType"),
        )
        field2: CField = CField(
            name="Field",
            declaring_type=CType(name="DeclaringType"),
            return_type=CType(name="ReturnType"),
        )

        result: CField = merge_field(field1, field2)
        expected: CField = CField(
            name="Field",
            declaring_type=CType(name="DeclaringType"),
            return_type=CType(name="ReturnType"),
        )

        self.assertEqual(expected, result)

    def test_merge_error_name(self) -> None:
        field1: CField = CField(
            name="FieldA",
            declaring_type=CType(name="DeclaringType"),
            return_type=CType(name="ReturnType"),
        )
        field2: CField = CField(
            name="FieldB",
            declaring_type=CType(name="DeclaringType"),
            return_type=CType(name="ReturnType"),
        )

        self.assertRaises(AttributeError, lambda: merge_field(field1, field2))

    def test_merge_error_declaring_type(self) -> None:
        field1: CField = CField(
            name="Field",
            declaring_type=CType(name="DeclaringTypeA"),
            return_type=CType(name="ReturnType"),
        )
        field2: CField = CField(
            name="Field",
            declaring_type=CType(name="DeclaringTypeB"),
            return_type=CType(name="ReturnType"),
        )

        self.assertRaises(AttributeError, lambda: merge_field(field1, field2))

    def test_merge_error_return_type(self) -> None:
        field1: CField = CField(
            name="Field",
            declaring_type=CType(name="DeclaringType"),
            return_type=CType(name="ReturnTypeA"),
        )
        field2: CField = CField(
            name="Field",
            declaring_type=CType(name="DeclaringType"),
            return_type=CType(name="ReturnTypeB"),
        )

        self.assertRaises(AttributeError, lambda: merge_field(field1, field2))

    def test_merge_error_static(self) -> None:
        field1: CField = CField(
            name="Field",
            declaring_type=CType(name="DeclaringType"),
            return_type=CType(name="ReturnType"),
        )
        field2: CField = CField(
            name="Field",
            declaring_type=CType(name="DeclaringType"),
            return_type=CType(name="ReturnType"),
            static=True,
        )

        self.assertRaises(AttributeError, lambda: merge_field(field1, field2))


class TestMergeConstructor(TestBase):
    def test_merge(self) -> None:
        constructor1: CConstructor = CConstructor(
            declaring_type=CType(name="DeclaringType"),
            parameters=(
                CParameter(name="param0", type=CType(name="ParamType")),
            ),
        )
        constructor2: CConstructor = CConstructor(
            declaring_type=CType(name="DeclaringType"),
            parameters=(
                CParameter(name="param0", type=CType(name="ParamType")),
            ),
        )

        result: CConstructor = merge_constructor(constructor1, constructor2)
        expected: CConstructor = CConstructor(
            declaring_type=CType(name="DeclaringType"),
            parameters=(
                CParameter(name="param0", type=CType(name="ParamType")),
            ),
        )

        self.assertEqual(expected, result)

    def test_merge_error_declaring_type(self) -> None:
        constructor1: CConstructor = CConstructor(
            declaring_type=CType(name="DeclaringTypeA"),
            parameters=(
                CParameter(name="param0", type=CType(name="ParamType")),
            ),
        )
        constructor2: CConstructor = CConstructor(
            declaring_type=CType(name="DeclaringTypeB"),
            parameters=(
                CParameter(name="param0", type=CType(name="ParamType")),
            ),
        )

        self.assertRaises(AttributeError, lambda: merge_constructor(constructor1, constructor2))

    def test_merge_error_parameters(self) -> None:
        constructor1: CConstructor = CConstructor(
            declaring_type=CType(name="DeclaringType"),
            parameters=(
                CParameter(name="param0", type=CType(name="ParamType")),
            ),
        )
        constructor2: CConstructor = CConstructor(
            declaring_type=CType(name="DeclaringType"),
            parameters=(
                CParameter(name="param0", type=CType(name="ParamType")),
                CParameter(name="param1", type=CType(name="ParamType")),
            ),
        )

        self.assertRaises(AttributeError, lambda: merge_constructor(constructor1, constructor2))


class TestMergeProperty(TestBase):
    def test_merge(self) -> None:
        property1: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="DeclaringType"),
            type=CType(name="Type"),
        )
        property2: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="DeclaringType"),
            type=CType(name="Type"),
        )

        result: CProperty = merge_property(property1, property2)
        expected: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="DeclaringType"),
            type=CType(name="Type"),
        )

        self.assertEqual(expected, result)

    def test_merge_error_name(self) -> None:
        property1: CProperty = CProperty(
            name="PropertyA",
            declaring_type=CType(name="DeclaringType"),
            type=CType(name="Type"),
        )
        property2: CProperty = CProperty(
            name="PropertyB",
            declaring_type=CType(name="DeclaringType"),
            type=CType(name="Type"),
        )

        self.assertRaises(AttributeError, lambda: merge_property(property1, property2))

    def test_merge_error_declaring_type(self) -> None:
        property1: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="DeclaringTypeA"),
            type=CType(name="Type"),
        )
        property2: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="DeclaringTypeB"),
            type=CType(name="Type"),
        )

        self.assertRaises(AttributeError, lambda: merge_property(property1, property2))

    def test_merge_error_type(self) -> None:
        property1: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="DeclaringType"),
            type=CType(name="TypeA"),
        )
        property2: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="DeclaringType"),
            type=CType(name="TypeB"),
        )

        self.assertRaises(AttributeError, lambda: merge_property(property1, property2))

    def test_merge_error_setter(self) -> None:
        property1: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="DeclaringType"),
            type=CType(name="Type"),
        )
        property2: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="DeclaringType"),
            type=CType(name="Type"),
            setter=True,
        )

        self.assertRaises(AttributeError, lambda: merge_property(property1, property2))

    def test_merge_error_static(self) -> None:
        property1: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="DeclaringType"),
            type=CType(name="Type"),
        )
        property2: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="DeclaringType"),
            type=CType(name="Type"),
            static=True,
        )

        self.assertRaises(AttributeError, lambda: merge_property(property1, property2))


class TestMergeMethod(TestBase):
    def test_merge(self) -> None:
        method1: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="DeclaringType"),
            parameters=(
                CParameter(name="param0", type=CType(name="ParamType")),
            ),
            return_types=(CType(name="ReturnType"),),
        )
        method2: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="DeclaringType"),
            parameters=(
                CParameter(name="param0", type=CType(name="ParamType")),
            ),
            return_types=(CType(name="ReturnType"),),
        )

        result: CMethod = merge_method(method1, method2)
        expected: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="DeclaringType"),
            parameters=(
                CParameter(name="param0", type=CType(name="ParamType")),
            ),
            return_types=(CType(name="ReturnType"),),
        )

        self.assertEqual(expected, result)

    def test_merge_error_name(self) -> None:
        method1: CMethod = CMethod(
            name="MethodA",
            declaring_type=CType(name="DeclaringType"),
            parameters=(
                CParameter(name="param0", type=CType(name="ParamType")),
            ),
            return_types=(CType(name="ReturnType"),),
        )
        method2: CMethod = CMethod(
            name="MethodB",
            declaring_type=CType(name="DeclaringType"),
            parameters=(
                CParameter(name="param0", type=CType(name="ParamType")),
            ),
            return_types=(CType(name="ReturnType"),),
        )

        self.assertRaises(AttributeError, lambda: merge_method(method1, method2))

    def test_merge_error_declaring_type(self) -> None:
        method1: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="DeclaringTypeA"),
            parameters=(
                CParameter(name="param0", type=CType(name="ParamType")),
            ),
            return_types=(CType(name="ReturnType"),),
        )
        method2: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="DeclaringTypeB"),
            parameters=(
                CParameter(name="param0", type=CType(name="ParamType")),
            ),
            return_types=(CType(name="ReturnType"),),
        )

        self.assertRaises(AttributeError, lambda: merge_method(method1, method2))

    def test_merge_error_parameters(self) -> None:
        method1: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="DeclaringType"),
            parameters=(
                CParameter(name="param0", type=CType(name="ParamType")),
            ),
            return_types=(CType(name="ReturnTypeA"),),
        )
        method2: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="DeclaringType"),
            parameters=(
                CParameter(name="param0", type=CType(name="ParamType")),
                CParameter(name="param1", type=CType(name="ParamType")),
            ),
            return_types=(CType(name="ReturnTypeB"),),
        )

        self.assertRaises(AttributeError, lambda: merge_method(method1, method2))

    def test_merge_error_return_types(self) -> None:
        method1: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="DeclaringType"),
            parameters=(
                CParameter(name="param0", type=CType(name="ParamType")),
            ),
            return_types=(CType(name="ReturnTypeA"),),
        )
        method2: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="DeclaringType"),
            parameters=(
                CParameter(name="param0", type=CType(name="ParamType")),
            ),
            return_types=(CType(name="ReturnTypeB"),),
        )

        self.assertRaises(AttributeError, lambda: merge_method(method1, method2))

    def test_merge_error_static(self) -> None:
        method1: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="DeclaringType"),
            parameters=(
                CParameter(name="param0", type=CType(name="ParamType")),
            ),
            return_types=(CType(name="ReturnTypeA"),),
        )
        method2: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="DeclaringType"),
            parameters=(
                CParameter(name="param0", type=CType(name="ParamType")),
            ),
            return_types=(CType(name="ReturnTypeB"),),
            static=True,
        )

        self.assertRaises(AttributeError, lambda: merge_method(method1, method2))


class TestMergeEvent(TestBase):
    def test_merge(self) -> None:
        event1: CEvent = CEvent(
            name="Event",
            declaring_type=CType(name="DeclaringType"),
            type=CType(name="Type"),
        )
        event2: CEvent = CEvent(
            name="Event",
            declaring_type=CType(name="DeclaringType"),
            type=CType(name="Type"),
        )

        result: CEvent = merge_event(event1, event2)
        expected: CEvent = CEvent(
            name="Event",
            declaring_type=CType(name="DeclaringType"),
            type=CType(name="Type"),
        )

        self.assertEqual(expected, result)

    def test_merge_error_name(self) -> None:
        event1: CEvent = CEvent(
            name="EventA",
            declaring_type=CType(name="DeclaringType"),
            type=CType(name="Type"),
        )
        event2: CEvent = CEvent(
            name="EventB",
            declaring_type=CType(name="DeclaringType"),
            type=CType(name="Type"),
        )

        self.assertRaises(AttributeError, lambda: merge_event(event1, event2))

    def test_merge_error_declaring_type(self) -> None:
        event1: CEvent = CEvent(
            name="Event",
            declaring_type=CType(name="DeclaringTypeA"),
            type=CType(name="Type"),
        )
        event2: CEvent = CEvent(
            name="Event",
            declaring_type=CType(name="DeclaringTypeB"),
            type=CType(name="Type"),
        )

        self.assertRaises(AttributeError, lambda: merge_event(event1, event2))

    def test_merge_error_type(self) -> None:
        event1: CEvent = CEvent(
            name="Event",
            declaring_type=CType(name="DeclaringType"),
            type=CType(name="TypeA"),
        )
        event2: CEvent = CEvent(
            name="Event",
            declaring_type=CType(name="DeclaringType"),
            type=CType(name="TypeB"),
        )

        self.assertRaises(AttributeError, lambda: merge_event(event1, event2))


class TestImports(TestBase):
    def test_add_type(self) -> None:
        imports = Imports()
        imports.add_type(CType(name="TypeA", namespace="NamespaceA"))
        imports.add_type(CType(name="TypeA", namespace="NamespaceA"))
        imports.add_type(CType(name="TypeB", namespace="NamespaceA"))
        imports.add_type(CType(name="TypeA", namespace="NamespaceB"))
        imports.add_type(CType(name="TypeA", namespace="NamespaceB"))
        imports.add_type(CType(name="TypeB", namespace="NamespaceB"))

        expected: Set[str] = {
            "NamespaceA.TypeA",
            "NamespaceA.TypeB",
            "NamespaceB.TypeA",
            "NamespaceB.TypeB",
        }

        self.assertEqual(expected, imports.types)

    def test_add_type_inner(self) -> None:
        imports = Imports()

        types: Sequence[CType] = (
            CType(
                name="Type",
                namespace="Namespace",
                inner=(CType(name="InnerA", namespace="Namespace"),),
            ),
            CType(
                name="Type",
                namespace="Namespace",
                inner=(CType(name="InnerB", namespace="Namespace"),),
            ),
        )
        for type in types:
            imports.add_type(type)

        expected: Set[str] = {"Namespace.Type", "Namespace.InnerA", "Namespace.InnerB"}

        self.assertEqual(expected, imports.types)

    def test_add_type_inner_false(self) -> None:
        imports = Imports()

        types: Sequence[CType] = (
            CType(
                name="Type",
                namespace="Namespace",
                inner=(CType(name="InnerA", namespace="Namespace"),),
            ),
            CType(
                name="Type",
                namespace="Namespace",
                inner=(CType(name="InnerB", namespace="Namespace"),),
            ),
        )
        for type in types:
            imports.add_type(type, inner=False)

        expected: Set[str] = {"Namespace.Type"}

        self.assertEqual(expected, imports.types)

    def test_add_type_type_var(self) -> None:
        imports = Imports()

        types: Sequence[CType] = (
            CType(name="T", namespace="Namespace", generic=True),
            CType(name="U", namespace="Namespace", generic=True),
            CType(name="V", namespace="Namespace", generic=True),
        )
        for type in types:
            imports.add_type(type)

        expected_types: Set[str] = {"typing.TypeVar"}
        expected_type_vars: Set[str] = {"T", "U", "V"}

        self.assertEqual(expected_types, imports.types)
        self.assertEqual(expected_type_vars, imports.type_vars)

    def test_build_empty(self) -> None:
        imports = Imports()

        lines: Sequence[str] = imports.build("Namespace")
        expected: Sequence[str] = ()

        self.assertEqual(expected, lines)

    def test_build(self) -> None:
        imports = Imports()
        imports.add_type(CType(name="TypeA", namespace="namespace"))
        imports.add_type(CType(name="TypeB", namespace="namespace"))
        imports.add_type(CType(name="TypeC", namespace="namespace"))
        imports.add_type(CType(name="TypeD", namespace="namespace"))

        lines: Sequence[str] = imports.build()
        expected: Sequence[str] = (
            "from namespace import TypeA",
            "from namespace import TypeB",
            "from namespace import TypeC",
            "from namespace import TypeD",
        )

        self.assertEqual(expected, lines)

    def test_build_namespace(self) -> None:
        imports = Imports()
        imports.add_type(CType(name="TypeA", namespace="Namespace"))
        imports.add_type(CType(name="TypeB", namespace="Namespace.Namespace"))
        imports.add_type(CType(name="TypeC", namespace="Namespace.Namespace"))
        imports.add_type(CType(name="TypeD", namespace="Namespace.Namespace.Namespace"))

        lines: Sequence[str] = imports.build("Namespace.Namespace")
        expected: Sequence[str] = (
            "from Namespace.Namespace.Namespace import TypeD",
            "from Namespace import TypeA",
        )

        self.assertEqual(expected, lines)

    def test_build_type_vars(self) -> None:
        imports = Imports()
        imports.add_type(CType(name="T", namespace="Namespace", generic=True))
        imports.add_type(CType(name="U", namespace="Namespace", generic=True))
        imports.add_type(CType(name="V", namespace="Namespace", generic=True))

        lines: Sequence[str] = imports.build()
        expected: Sequence[str] = (
            "from typing import TypeVar",
            f'T = TypeVar("T")',
            f'U = TypeVar("U")',
            f'V = TypeVar("V")',
        )

        self.assertEqual(expected, lines)

    def test_build_include_event_type(self) -> None:
        imports = Imports()
        imports.include_event_type = True

        lines: Sequence[str] = imports.build()
        expected: Sequence[str] = (
            "from typing import Generic",
            "from typing import TypeVar",
            f'T = TypeVar("T")',
            "class EventType(Generic[T]):",
            "    def __iadd__(self, other: T): ...",
            "    def __isub__(self, other: T): ...",
        )

        self.assertEqual(expected, lines)


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
        expected: Sequence[str] = (
            "class Class:",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "class Class(ABC):",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "class Class(Generic[K, V]):",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "class Class(Super):",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "class Class(InterfaceA, InterfaceB):",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "class Class:",
            '    """"""',
            "    FieldA: Final[FieldType] = ...",
            '    """"""',
            "    FieldB: Final[FieldType] = ...",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "class Class:",
            '    """"""',
            "    def __init__(self):",
            '        """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "class Class:",
            '    """"""',
            "    @overload",
            "    def __init__(self):",
            '        """"""',
            "    @overload",
            "    def __init__(self, param0: Type):",
            '        """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "class Class:",
            '    """"""',
            "    @property",
            "    def PropertyA(self) -> PropertyType:",
            '        """"""',
            "    @property",
            "    def PropertyB(self) -> PropertyType:",
            '        """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "class Class:",
            '    """"""',
            "    def MethodA(self, param0: ParamType, param1: ParamType) -> MethodType:",
            '        """"""',
            "    def MethodB(self, param0: ParamType, param1: ParamType) -> MethodType:",
            '        """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "class Class:",
            '    """"""',
            "    @overload",
            "    def MethodA(self, param0: ParamType) -> MethodType:",
            '        """"""',
            "    @overload",
            "    def MethodA(self, param0: ParamType, param1: ParamType) -> MethodType:",
            '        """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "class Class:",
            '    """"""',
            "    EventA: EventType[EventHandler] = ...",
            '    """"""',
            "    EventB: EventType[EventHandler] = ...",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
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

        self.assertEqual(expected, lines)

    def test_imports(self) -> None:
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
        expected: Set[str] = set()

        self.assertEqual(expected, imports.types)

    def test_imports_abstract(self) -> None:
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
        expected: Set[str] = {"abc.ABC"}

        self.assertEqual(expected, imports.types)

    def test_imports_generic(self) -> None:
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
        expected: Set[str] = {"typing.Generic", "typing.TypeVar"}

        self.assertEqual(expected, imports.types)

    def test_imports_super(self) -> None:
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
        expected: Set[str] = {"Namespace.Super"}

        self.assertEqual(expected, imports.types)

    def test_imports_interfaces(self) -> None:
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
        expected: Set[str] = {"Namespace.InterfaceA", "Namespace.InterfaceB"}

        self.assertEqual(expected, imports.types)

    def test_imports_fields(self) -> None:
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
        expected: Set[str] = {"typing.Final", "Namespace.FieldType"}

        self.assertEqual(expected, imports.types)

    def test_imports_constructors(self) -> None:
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
        expected: Set[str] = set()

        self.assertEqual(expected, imports.types)

    def test_imports_constructors_overload(self) -> None:
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
        expected: Set[str] = {"typing.overload", "Namespace.Type"}

        self.assertEqual(expected, imports.types)

    def test_imports_properties(self) -> None:
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
        expected: Set[str] = {"Namespace.PropertyType"}

        self.assertEqual(expected, imports.types)

    def test_imports_methods(self) -> None:
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
        expected: Set[str] = {"Namespace.ParamType", "Namespace.MethodType"}

        self.assertEqual(expected, imports.types)

    def test_imports_methods_overload(self) -> None:
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
        expected: Set[str] = {"typing.overload", "Namespace.ParamType", "Namespace.MethodType"}

        self.assertEqual(expected, imports.types)

    def test_imports_events(self) -> None:
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
        expected: Set[str] = {"Namespace.EventHandler"}

        self.assertEqual(expected, imports.types)

    def test_imports_nested(self) -> None:
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
        expected: Set[str] = {"typing.Callable", "System.Enum", "Namespace.DelegateType"}

        self.assertEqual(expected, imports.types)

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
        expected: Sequence[str] = (
            "class Class:",
            '    """Class doc string."""',
        )

        self.assertEqual(expected, lines)


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
        expected: Sequence[str] = (
            "class Struct:",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "class Struct(ABC):",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "class Struct(Generic[K, V]):",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "class Struct(Super):",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "class Struct(InterfaceA, InterfaceB):",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "class Struct:",
            '    """"""',
            "    FieldA: Final[FieldType] = ...",
            '    """"""',
            "    FieldB: Final[FieldType] = ...",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "class Struct:",
            '    """"""',
            "    def __init__(self):",
            '        """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "class Struct:",
            '    """"""',
            "    @overload",
            "    def __init__(self):",
            '        """"""',
            "    @overload",
            "    def __init__(self, param0: Type):",
            '        """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "class Struct:",
            '    """"""',
            "    @property",
            "    def PropertyA(self) -> PropertyType:",
            '        """"""',
            "    @property",
            "    def PropertyB(self) -> PropertyType:",
            '        """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "class Struct:",
            '    """"""',
            "    def MethodA(self, param0: ParamType, param1: ParamType) -> MethodType:",
            '        """"""',
            "    def MethodB(self, param0: ParamType, param1: ParamType) -> MethodType:",
            '        """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "class Struct:",
            '    """"""',
            "    @overload",
            "    def MethodA(self, param0: ParamType) -> MethodType:",
            '        """"""',
            "    @overload",
            "    def MethodA(self, param0: ParamType, param1: ParamType) -> MethodType:",
            '        """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "class Struct:",
            '    """"""',
            "    EventA: EventType[EventHandler] = ...",
            '    """"""',
            "    EventB: EventType[EventHandler] = ...",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
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

        self.assertEqual(expected, lines)

    def test_imports(self) -> None:
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
        expected: Set[str] = set()

        self.assertEqual(expected, imports.types)

    def test_imports_abstract(self) -> None:
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
        expected: Set[str] = {"abc.ABC"}

        self.assertEqual(expected, imports.types)

    def test_imports_generic(self) -> None:
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
        expected: Set[str] = {"typing.Generic", "typing.TypeVar"}

        self.assertEqual(expected, imports.types)

    def test_imports_super(self) -> None:
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
        expected: Set[str] = {"Namespace.Super"}

        self.assertEqual(expected, imports.types)

    def test_imports_interfaces(self) -> None:
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
        expected: Set[str] = {"Namespace.InterfaceA", "Namespace.InterfaceB"}

        self.assertEqual(expected, imports.types)

    def test_imports_fields(self) -> None:
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
        expected: Set[str] = {"typing.Final", "Namespace.FieldType"}

        self.assertEqual(expected, imports.types)

    def test_imports_constructors(self) -> None:
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
        expected: Set[str] = set()

        self.assertEqual(expected, imports.types)

    def test_imports_constructors_overload(self) -> None:
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
        expected: Set[str] = {"typing.overload", "Namespace.Type"}

        self.assertEqual(expected, imports.types)

    def test_imports_properties(self) -> None:
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
        expected: Set[str] = {"Namespace.PropertyType"}

        self.assertEqual(expected, imports.types)

    def test_imports_methods(self) -> None:
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
        expected: Set[str] = {"Namespace.MethodType", "Namespace.ParamType"}

        self.assertEqual(expected, imports.types)

    def test_imports_methods_overload(self) -> None:
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
        expected: Set[str] = {"typing.overload", "Namespace.MethodType", "Namespace.ParamType"}

        self.assertEqual(expected, imports.types)

    def test_imports_events(self) -> None:
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
        expected: Set[str] = {"Namespace.EventHandler"}

        self.assertEqual(expected, imports.types)

    def test_imports_nested(self) -> None:
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
        expected: Set[str] = {"typing.Callable", "Namespace.DelegateType", "System.Enum"}

        self.assertEqual(expected, imports.types)

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
        expected: Sequence[str] = (
            "class Struct:",
            '    """Struct doc string."""',
        )

        self.assertEqual(expected, lines)


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
        expected: Sequence[str] = (
            "class Interface:",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "class Interface(Generic[K, V]):",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "class Interface(InterfaceA, InterfaceB):",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "class Interface:",
            '    """"""',
            "    FieldA: Final[FieldType] = ...",
            '    """"""',
            "    FieldB: Final[FieldType] = ...",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "class Interface:",
            '    """"""',
            "    @property",
            "    def PropertyA(self) -> PropertyType:",
            '        """"""',
            "    @property",
            "    def PropertyB(self) -> PropertyType:",
            '        """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "class Interface:",
            '    """"""',
            "    def MethodA(self, param0: ParamType, param1: ParamType) -> MethodType:",
            '        """"""',
            "    def MethodB(self, param0: ParamType, param1: ParamType) -> MethodType:",
            '        """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "class Interface:",
            '    """"""',
            "    @overload",
            "    def MethodA(self, param0: ParamType) -> MethodType:",
            '        """"""',
            "    @overload",
            "    def MethodA(self, param0: ParamType, param1: ParamType) -> MethodType:",
            '        """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "class Interface:",
            '    """"""',
            "    EventA: EventType[EventHandler] = ...",
            '    """"""',
            "    EventB: EventType[EventHandler] = ...",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
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

        self.assertEqual(expected, lines)

    def test_imports(self) -> None:
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
        expected: Set[str] = set()

        self.assertEqual(expected, imports.types)

    def test_imports_generic(self) -> None:
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
        expected: Set[str] = {"typing.Generic", "typing.TypeVar"}

        self.assertEqual(expected, imports.types)

    def test_imports_interfaces(self) -> None:
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
        expected: Set[str] = {"Namespace.InterfaceA", "Namespace.InterfaceB"}

        self.assertEqual(expected, imports.types)

    def test_imports_fields(self) -> None:
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
        expected: Set[str] = {"typing.Final", "Namespace.FieldType"}

        self.assertEqual(expected, imports.types)

    def test_imports_properties(self) -> None:
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
        expected: Set[str] = {"Namespace.PropertyType"}

        self.assertEqual(expected, imports.types)

    def test_imports_methods(self) -> None:
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
        expected: Set[str] = {"Namespace.ParamType", "Namespace.MethodType"}

        self.assertEqual(expected, imports.types)

    def test_imports_methods_overload(self) -> None:
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
        expected: Set[str] = {"typing.overload", "Namespace.ParamType", "Namespace.MethodType"}

        self.assertEqual(expected, imports.types)

    def test_imports_events(self) -> None:
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
        expected: Set[str] = {"Namespace.EventHandler"}

        self.assertEqual(expected, imports.types)

    def test_imports_nested(self) -> None:
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
        expected: Set[str] = {"typing.Callable", "Namespace.DelegateType", "System.Enum"}

        self.assertEqual(expected, imports.types)

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
        expected: Sequence[str] = (
            "class Interface:",
            '    """Interface doc string."""',
        )

        self.assertEqual(expected, lines)


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
        expected: Sequence[str] = (
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

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "class Enum(Enum):",
            '    """"""',
        )

        self.assertEqual(expected, lines)

    def test_imports(self) -> None:
        type_def: CEnum = CEnum(
            name="Enum",
            namespace="Namespace",
            nested=None,
            fields=("FieldA", "FieldB", "FieldC", "FieldD"),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_enum(type_def=type_def, imports=imports, doc=doc)
        expected: Set[str] = {"System.Enum"}

        self.assertEqual(expected, imports.types)

    def test_imports_no_fields(self) -> None:
        type_def: CEnum = CEnum(
            name="Enum",
            namespace="Namespace",
            nested=None,
            fields=(),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_enum(type_def=type_def, imports=imports, doc=doc)
        expected: Set[str] = {"System.Enum"}

        self.assertEqual(expected, imports.types)

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
        expected: Sequence[str] = (
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

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "class Enum(Enum):",
            '    """Enum doc string."""',
        )

        self.assertEqual(expected, lines)


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
        expected: Sequence[str] = (
            "Delegate: Callable[[ParamType, ParamType], ReturnType] = ...",
            '""""""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "Delegate: Callable[[], ReturnType] = ...",
            '""""""',
        )

        self.assertEqual(expected, lines)

    def test_imports(self) -> None:
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
        expected: Set[str] = {"typing.Callable", "Namespace.ReturnType", "Namespace.ParamType"}

        self.assertEqual(expected, imports.types)

    def test_imports_no_params(self) -> None:
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
        expected: Set[str] = {"typing.Callable", "Namespace.ReturnType"}

        self.assertEqual(expected, imports.types)

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
        expected: Sequence[str] = (
            "Delegate: Callable[[ParamType, ParamType], ReturnType] = ...",
            '"""Delegate doc string.',
            "",
            ":param param0: Parameter 0 doc string.",
            ":param param1: Parameter 1 doc string.",
            ":return: Return doc string.",
            '"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "Delegate: Callable[[], ReturnType] = ...",
            '"""Delegate doc string.',
            "",
            ":return: Return doc string.",
            '"""',
        )

        self.assertEqual(expected, lines)


class TestBuildType(TestBase):
    def test_build(self) -> None:
        tests: Sequence[Tuple[CType, str, Set[str]]] = (
            (CType(name="Boolean", namespace="System"), "Boolean", {"System.Boolean"}),
            (CType(name="SByte", namespace="System"), "SByte", {"System.SByte"}),
            (CType(name="Byte", namespace="System"), "Byte", {"System.Byte"}),
            (CType(name="Int16", namespace="System"), "Int16", {"System.Int16"}),
            (CType(name="UInt16", namespace="System"), "UInt16", {"System.UInt16"}),
            (CType(name="Int32", namespace="System"), "Int32", {"System.Int32"}),
            (CType(name="UInt32", namespace="System"), "UInt32", {"System.UInt32"}),
            (CType(name="Int64", namespace="System"), "Int64", {"System.Int64"}),
            (CType(name="UInt64", namespace="System"), "UInt64", {"System.UInt64"}),
            (CType(name="Single", namespace="System"), "Single", {"System.Single"}),
            (CType(name="Double", namespace="System"), "Double", {"System.Double"}),
            (CType(name="String", namespace="System"), "String", {"System.String"}),
            (CType(name="Object", namespace="System"), "Object", {"System.Object"}),
            (CType(name="Void", namespace="System"), "Void", {"System.Void"}),
            (CType(name="T", generic=True), "T", {"typing.TypeVar"}),
        )
        for test in tests:
            imports = Imports()

            type: CType = test[0]
            expected: str = test[1]
            expected_types: Set[str] = test[2]

            with self.subTest(type=type.name):
                result: str = build_type(type, imports)

                self.assertEqual(expected, result)
                self.assertEqual(expected_types, imports.types)

    def test_build_nullable(self) -> None:
        tests: Sequence[Tuple[CType, str, Set[str]]] = (
            (
                CType(name="Boolean", namespace="System", nullable=True),
                "Optional[Boolean]",
                {"typing.Optional", "System.Boolean"},
            ),
            (
                CType(name="SByte", namespace="System", nullable=True),
                "Optional[SByte]",
                {"typing.Optional", "System.SByte"},
            ),
            (
                CType(name="Byte", namespace="System", nullable=True),
                "Optional[Byte]",
                {"typing.Optional", "System.Byte"},
            ),
            (
                CType(name="Int16", namespace="System", nullable=True),
                "Optional[Int16]",
                {"typing.Optional", "System.Int16"},
            ),
            (
                CType(name="UInt16", namespace="System", nullable=True),
                "Optional[UInt16]",
                {"typing.Optional", "System.UInt16"},
            ),
            (
                CType(name="Int32", namespace="System", nullable=True),
                "Optional[Int32]",
                {"typing.Optional", "System.Int32"},
            ),
            (
                CType(name="UInt32", namespace="System", nullable=True),
                "Optional[UInt32]",
                {"typing.Optional", "System.UInt32"},
            ),
            (
                CType(name="Int64", namespace="System", nullable=True),
                "Optional[Int64]",
                {"typing.Optional", "System.Int64"},
            ),
            (
                CType(name="UInt64", namespace="System", nullable=True),
                "Optional[UInt64]",
                {"typing.Optional", "System.UInt64"},
            ),
            (
                CType(name="Single", namespace="System", nullable=True),
                "Optional[Single]",
                {"typing.Optional", "System.Single"},
            ),
            (
                CType(name="Double", namespace="System", nullable=True),
                "Optional[Double]",
                {"typing.Optional", "System.Double"},
            ),
            (
                CType(name="String", namespace="System", nullable=True),
                "Optional[String]",
                {"typing.Optional", "System.String"},
            ),
            (
                CType(name="Object", namespace="System", nullable=True),
                "Optional[Object]",
                {"typing.Optional", "System.Object"},
            ),
            (
                CType(name="Void", namespace="System", nullable=True),
                "Optional[Void]",
                {"typing.Optional", "System.Void"},
            ),
            (
                CType(name="T", generic=True, nullable=True),
                "Optional[T]",
                {"typing.Optional", "typing.TypeVar"},
            ),
        )
        for test in tests:
            imports = Imports()

            type: CType = test[0]
            expected: str = test[1]
            expected_types: Set[str] = test[2]

            with self.subTest(type=type.name):
                result: str = build_type(type, imports)

                self.assertEqual(expected, result)
                self.assertEqual(expected_types, imports.types)

    def test_build_convert(self) -> None:
        tests: Sequence[Tuple[CType, str, Set[str]]] = (
            (CType(name="Boolean", namespace="System"), "bool", set()),
            (CType(name="SByte", namespace="System"), "int", set()),
            (CType(name="Byte", namespace="System"), "int", set()),
            (CType(name="Int16", namespace="System"), "int", set()),
            (CType(name="UInt16", namespace="System"), "int", set()),
            (CType(name="Int32", namespace="System"), "int", set()),
            (CType(name="UInt32", namespace="System"), "int", set()),
            (CType(name="Int64", namespace="System"), "int", set()),
            (CType(name="UInt64", namespace="System"), "int", set()),
            (CType(name="Single", namespace="System"), "float", set()),
            (CType(name="Double", namespace="System"), "float", set()),
            (CType(name="String", namespace="System"), "str", set()),
            (CType(name="Object", namespace="System"), "object", set()),
            (CType(name="Void", namespace="System"), "None", set()),
        )
        for test in tests:
            imports = Imports()

            type: CType = test[0]
            expected: str = test[1]
            expected_types: Set[str] = test[2]

            with self.subTest(type=type.name):
                result: str = build_type(type, imports, convert=True)

                self.assertEqual(expected, result)
                self.assertEqual(expected_types, imports.types)

    def test_build_convert_nullable(self) -> None:
        tests: Sequence[Tuple[CType, str, Set[str]]] = (
            (
                CType(name="Boolean", namespace="System", nullable=True),
                "Optional[bool]",
                {"typing.Optional"},
            ),
            (
                CType(name="SByte", namespace="System", nullable=True),
                "Optional[int]",
                {"typing.Optional"},
            ),
            (
                CType(name="Byte", namespace="System", nullable=True),
                "Optional[int]",
                {"typing.Optional"},
            ),
            (
                CType(name="Int16", namespace="System", nullable=True),
                "Optional[int]",
                {"typing.Optional"},
            ),
            (
                CType(name="UInt16", namespace="System", nullable=True),
                "Optional[int]",
                {"typing.Optional"},
            ),
            (
                CType(name="Int32", namespace="System", nullable=True),
                "Optional[int]",
                {"typing.Optional"},
            ),
            (
                CType(name="UInt32", namespace="System", nullable=True),
                "Optional[int]",
                {"typing.Optional"},
            ),
            (
                CType(name="Int64", namespace="System", nullable=True),
                "Optional[int]",
                {"typing.Optional"},
            ),
            (
                CType(name="UInt64", namespace="System", nullable=True),
                "Optional[int]",
                {"typing.Optional"},
            ),
            (
                CType(name="Single", namespace="System", nullable=True),
                "Optional[float]",
                {"typing.Optional"},
            ),
            (
                CType(name="Double", namespace="System", nullable=True),
                "Optional[float]",
                {"typing.Optional"},
            ),
            (
                CType(name="String", namespace="System", nullable=True),
                "Optional[str]",
                {"typing.Optional"},
            ),
            (
                CType(name="Object", namespace="System", nullable=True),
                "Optional[object]",
                {"typing.Optional"},
            ),
        )
        for test in tests:
            imports = Imports()

            type: CType = test[0]
            expected: str = test[1]
            expected_types: Set[str] = test[2]

            with self.subTest(type=type.name):
                result: str = build_type(type, imports, convert=True)

                self.assertEqual(expected, result)
                self.assertEqual(expected_types, imports.types)


class TestBuildParameter(TestBase):
    def test_build(self) -> None:
        parameter: CParameter = CParameter(
            name="param",
            type=CType(name="Type", namespace="Namespace"),
        )
        imports: Imports = Imports()

        lines: Sequence[str] = build_parameter(parameter=parameter, imports=imports)
        expected: str = ", param: Type"

        self.assertEqual(expected, lines)

    def test_build_default(self) -> None:
        parameter: CParameter = CParameter(
            name="param",
            type=CType(name="Type", namespace="Namespace"),
            default=True,
        )
        imports: Imports = Imports()

        lines: Sequence[str] = build_parameter(parameter=parameter, imports=imports)
        expected: str = ", param: Type = ..."

        self.assertEqual(expected, lines)

    def test_build_out(self) -> None:
        parameter: CParameter = CParameter(
            name="param",
            type=CType(name="Type", namespace="Namespace"),
            out=True,
        )
        imports: Imports = Imports()

        lines: Sequence[str] = build_parameter(parameter=parameter, imports=imports)
        expected: str = ", param: Type"

        self.assertEqual(expected, lines)

    def test_build_default_out(self) -> None:
        parameter: CParameter = CParameter(
            name="param",
            type=CType(name="Type", namespace="Namespace"),
            default=True,
            out=True,
        )
        imports: Imports = Imports()

        lines: Sequence[str] = build_parameter(parameter=parameter, imports=imports)
        expected: str = ", param: Type = ..."

        self.assertEqual(expected, lines)


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
        expected: Sequence[str] = (
            "Field: Final[ReturnType] = ...",
            '""""""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "Field: Final[ClassVar[ReturnType]] = ...",
            '""""""',
        )

        self.assertEqual(expected, lines)

    def test_imports(self) -> None:
        field: CField = CField(
            name="Field",
            declaring_type=CType(name="Type", namespace="Namespace"),
            return_type=CType(name="ReturnType", namespace="Namespace"),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_field(field=field, imports=imports, doc=doc)
        expected: Set[str] = {"typing.Final", "Namespace.ReturnType"}

        self.assertEqual(expected, imports.types)

    def test_imports_static(self) -> None:
        field: CField = CField(
            name="Field",
            declaring_type=CType(name="Type", namespace="Namespace"),
            return_type=CType(name="ReturnType", namespace="Namespace"),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_field(field=field, imports=imports, doc=doc)
        expected: Set[str] = {"typing.Final", "typing.ClassVar", "Namespace.ReturnType"}

        self.assertEqual(expected, imports.types)

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
        expected: Sequence[str] = (
            "Field: Final[ReturnType] = ...",
            '"""Field doc string."""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "Field: Final[ClassVar[ReturnType]] = ...",
            '"""Field doc string."""',
        )

        self.assertEqual(expected, lines)


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
        expected: Sequence[str] = (
            "def __init__(self, param0: Param, param1: Param):",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "@overload",
            "def __init__(self, param0: Param, param1: Param):",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "def __init__(self):",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "@overload",
            "def __init__(self):",
            '    """"""',
        )

        self.assertEqual(expected, lines)

    def test_imports(self) -> None:
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
        expected: Set[str] = {"Namespace.Param"}

        self.assertEqual(expected, imports.types)

    def test_imports_overload(self) -> None:
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
        expected: Set[str] = {"typing.overload", "Namespace.Param"}

        self.assertEqual(expected, imports.types)

    def test_imports_no_parameters(self) -> None:
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
        expected: Set[str] = set()

        self.assertEqual(expected, imports.types)

    def test_imports_no_parameters_overload(self) -> None:
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
        expected: Set[str] = {"typing.overload"}

        self.assertEqual(expected, imports.types)

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
        expected: Sequence[str] = (
            "def __init__(self, param0: Param, param1: Param):",
            '    """Constructor doc string.',
            "    ",
            "    :param param0: Parameter 0 doc string.",
            "    :param param1: Parameter 1 doc string.",
            '    """',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "@overload",
            "def __init__(self, param0: Param, param1: Param):",
            '    """Constructor doc string.',
            "    ",
            "    :param param0: Parameter 0 doc string.",
            "    :param param1: Parameter 1 doc string.",
            '    """',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "def __init__(self):",
            '    """Constructor doc string."""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "@overload",
            "def __init__(self):",
            '    """Constructor doc string."""',
        )

        self.assertEqual(expected, lines)


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
        expected: Sequence[str] = (
            "@property",
            "def Property(self) -> PropertyType:",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "@property",
            "def Property(self) -> PropertyType:",
            '    """"""',
            "@Property.setter",
            "def Property(self, value: PropertyType) -> None: ...",
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "@classmethod",
            "@property",
            "def Property(cls) -> PropertyType:",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "@classmethod",
            "@property",
            "def Property(cls) -> PropertyType:",
            '    """"""',
            "@classmethod",
            "@Property.setter",
            "def Property(cls, value: PropertyType) -> None: ...",
        )

        self.assertEqual(expected, lines)

    def test_imports(self) -> None:
        property: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="PropertyType", namespace="Namespace"),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_property(property=property, imports=imports, doc=doc)
        expected: Set[str] = {"Namespace.PropertyType"}

        self.assertEqual(expected, imports.types)

    def test_imports_setter(self) -> None:
        property: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="PropertyType", namespace="Namespace"),
            setter=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_property(property=property, imports=imports, doc=doc)
        expected: Set[str] = {"Namespace.PropertyType"}

        self.assertEqual(expected, imports.types)

    def test_imports_static(self) -> None:
        property: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="PropertyType", namespace="Namespace"),
            static=True,
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_property(property=property, imports=imports, doc=doc)
        expected: Set[str] = {"Namespace.PropertyType"}

        self.assertEqual(expected, imports.types)

    def test_imports_setter_static(self) -> None:
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
        expected: Set[str] = {"Namespace.PropertyType"}

        self.assertEqual(expected, imports.types)

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
        expected: Sequence[str] = (
            "@property",
            "def Property(self) -> PropertyType:",
            '    """Property doc string.',
            "    ",
            "    :return: Property return string.",
            '    """',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "@property",
            "def Property(self) -> PropertyType:",
            '    """Property doc string.',
            "    ",
            "    :return: Property return string.",
            '    """',
            "@Property.setter",
            "def Property(self, value: PropertyType) -> None: ...",
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "@classmethod",
            "@property",
            "def Property(cls) -> PropertyType:",
            '    """Property doc string.',
            "    ",
            "    :return: Property return string.",
            '    """',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
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

        self.assertEqual(expected, lines)


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
        expected: Sequence[str] = (
            "def Method(self, param0: Param, param1: Param) -> Return:",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "@classmethod",
            "def Method(cls, param0: Param, param1: Param) -> Return:",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "@overload",
            "def Method(self, param0: Param, param1: Param) -> Return:",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "@classmethod",
            "@overload",
            "def Method(cls, param0: Param, param1: Param) -> Return:",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "def Method(self) -> Return:",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "@classmethod",
            "def Method(cls) -> Return:",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "@overload",
            "def Method(self) -> Return:",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "@classmethod",
            "@overload",
            "def Method(cls) -> Return:",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "def Method(self, param0: Param, param1: Param) -> Tuple[Return, Return]:",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "@classmethod",
            "def Method(cls, param0: Param, param1: Param) -> Tuple[Return, Return]:",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "@overload",
            "def Method(self, param0: Param, param1: Param) -> Tuple[Return, Return]:",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "@classmethod",
            "@overload",
            "def Method(cls, param0: Param, param1: Param) -> Tuple[Return, Return]:",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "def Method(self) -> Tuple[Return, Return]:",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "@classmethod",
            "def Method(cls) -> Tuple[Return, Return]:",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "@overload",
            "def Method(self) -> Tuple[Return, Return]:",
            '    """"""',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "@classmethod",
            "@overload",
            "def Method(cls) -> Tuple[Return, Return]:",
            '    """"""',
        )

        self.assertEqual(expected, lines)

    def test_imports(self) -> None:
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
        expected: Set[str] = {"Namespace.Param", "Namespace.Return"}

        self.assertEqual(expected, imports.types)

    def test_imports_static(self) -> None:
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
        expected: Set[str] = {"Namespace.Param", "Namespace.Return"}

        self.assertEqual(expected, imports.types)

    def test_imports_overload(self) -> None:
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
        expected: Set[str] = {"typing.overload", "Namespace.Param", "Namespace.Return"}

        self.assertEqual(expected, imports.types)

    def test_imports_overload_static(self) -> None:
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
        expected: Set[str] = {"typing.overload", "Namespace.Param", "Namespace.Return"}

        self.assertEqual(expected, imports.types)

    def test_imports_no_params(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(CType(name="Return", namespace="Namespace"),),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=False)
        expected: Set[str] = {"Namespace.Return"}

        self.assertEqual(expected, imports.types)

    def test_imports_no_params_static(self) -> None:
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
        expected: Set[str] = {"Namespace.Return"}

        self.assertEqual(expected, imports.types)

    def test_imports_no_params_overload(self) -> None:
        method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(CType(name="Return", namespace="Namespace"),),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_method(method=method, imports=imports, doc=doc, overload=True)
        expected: Set[str] = {"typing.overload", "Namespace.Return"}

        self.assertEqual(expected, imports.types)

    def test_imports_no_params_overload_static(self) -> None:
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
        expected: Set[str] = {"typing.overload", "Namespace.Return"}

        self.assertEqual(expected, imports.types)

    def test_imports_returns(self) -> None:
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
        expected: Set[str] = {"typing.Tuple", "Namespace.Param", "Namespace.Return"}

        self.assertEqual(expected, imports.types)

    def test_imports_returns_static(self) -> None:
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
        expected: Set[str] = {"typing.Tuple", "Namespace.Param", "Namespace.Return"}

        self.assertEqual(expected, imports.types)

    def test_imports_returns_overload(self) -> None:
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
        expected: Set[str] = {
            "typing.overload",
            "typing.Tuple",
            "Namespace.Param",
            "Namespace.Return",
        }

        self.assertEqual(expected, imports.types)

    def test_imports_returns_overload_static(self) -> None:
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
        expected: Set[str] = {
            "typing.overload",
            "typing.Tuple",
            "Namespace.Param",
            "Namespace.Return",
        }

        self.assertEqual(expected, imports.types)

    def test_imports_returns_no_params(self) -> None:
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
        expected: Set[str] = {"typing.Tuple", "Namespace.Return"}

        self.assertEqual(expected, imports.types)

    def test_imports_returns_no_params_static(self) -> None:
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
        expected: Set[str] = {"typing.Tuple", "Namespace.Return"}

        self.assertEqual(expected, imports.types)

    def test_imports_returns_no_params_overload(self) -> None:
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
        expected: Set[str] = {"typing.overload", "typing.Tuple", "Namespace.Return"}

        self.assertEqual(expected, imports.types)

    def test_imports_returns_no_params_overload_static(self) -> None:
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
        expected: Set[str] = {"typing.overload", "typing.Tuple", "Namespace.Return"}

        self.assertEqual(expected, imports.types)

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
        expected: Sequence[str] = (
            "def Method(self, param0: Param, param1: Param) -> Return:",
            '    """Method doc string.',
            "    ",
            "    :param param0: Parameter 0 doc string.",
            "    :param param1: Parameter 1 doc string.",
            "    :return: Return doc string.",
            '    """',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "@classmethod",
            "def Method(cls, param0: Param, param1: Param) -> Return:",
            '    """Method doc string.',
            "    ",
            "    :param param0: Parameter 0 doc string.",
            "    :param param1: Parameter 1 doc string.",
            "    :return: Return doc string.",
            '    """',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "@overload",
            "def Method(self, param0: Param, param1: Param) -> Return:",
            '    """Method doc string.',
            "    ",
            "    :param param0: Parameter 0 doc string.",
            "    :param param1: Parameter 1 doc string.",
            "    :return: Return doc string.",
            '    """',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
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

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "def Method(self) -> Return:",
            '    """Method doc string.',
            "    ",
            "    :return: Return doc string.",
            '    """',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "@classmethod",
            "def Method(cls) -> Return:",
            '    """Method doc string.',
            "    ",
            "    :return: Return doc string.",
            '    """',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "@overload",
            "def Method(self) -> Return:",
            '    """Method doc string.',
            "    ",
            "    :return: Return doc string.",
            '    """',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "@classmethod",
            "@overload",
            "def Method(cls) -> Return:",
            '    """Method doc string.',
            "    ",
            "    :return: Return doc string.",
            '    """',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "def Method(self, param0: Param, param1: Param) -> Tuple[Return, Return]:",
            '    """Method doc string.',
            "    ",
            "    :param param0: Parameter 0 doc string.",
            "    :param param1: Parameter 1 doc string.",
            "    :return: Return doc string.",
            '    """',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "@classmethod",
            "def Method(cls, param0: Param, param1: Param) -> Tuple[Return, Return]:",
            '    """Method doc string.',
            "    ",
            "    :param param0: Parameter 0 doc string.",
            "    :param param1: Parameter 1 doc string.",
            "    :return: Return doc string.",
            '    """',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "@overload",
            "def Method(self, param0: Param, param1: Param) -> Tuple[Return, Return]:",
            '    """Method doc string.',
            "    ",
            "    :param param0: Parameter 0 doc string.",
            "    :param param1: Parameter 1 doc string.",
            "    :return: Return doc string.",
            '    """',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
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

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "def Method(self) -> Tuple[Return, Return]:",
            '    """Method doc string.',
            "    ",
            "    :return: Return doc string.",
            '    """',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "@classmethod",
            "def Method(cls) -> Tuple[Return, Return]:",
            '    """Method doc string.',
            "    ",
            "    :return: Return doc string.",
            '    """',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "@overload",
            "def Method(self) -> Tuple[Return, Return]:",
            '    """Method doc string.',
            "    ",
            "    :return: Return doc string.",
            '    """',
        )

        self.assertEqual(expected, lines)

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
        expected: Sequence[str] = (
            "@classmethod",
            "@overload",
            "def Method(cls) -> Tuple[Return, Return]:",
            '    """Method doc string.',
            "    ",
            "    :return: Return doc string.",
            '    """',
        )

        self.assertEqual(expected, lines)


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
        expected: Sequence[str] = (
            "Event: EventType[Event] = ...",
            '""""""',
        )

        self.assertEqual(expected, lines)

    def test_imports(self) -> None:
        event: CEvent = CEvent(
            name="Event",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="Event", namespace="Namespace"),
        )
        imports: Imports = Imports()
        doc: Doc = Doc({})

        build_event(event=event, imports=imports, doc=doc)
        expected: Set[str] = {"Namespace.Event"}

        self.assertEqual(expected, imports.types)

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
        expected: Sequence[str] = (
            "Event: EventType[Event] = ...",
            '"""Event doc string."""',
        )

        self.assertEqual(expected, lines)


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
