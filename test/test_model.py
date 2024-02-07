import random
import unittest
from typing import MutableSequence
from typing import Sequence

from test_base import TestBase

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
from stubgen.model import CTypeDefinition
from stubgen.model import JsonType


class TestCNamespace(TestBase):
    def test_json(self) -> None:
        namespace: CNamespace = CNamespace(
            name="Namespace",
            types={
                "Namespace:IInterface": CInterface(
                    name="IInterface",
                    namespace="Namespace",
                    nested=None,
                    generic_args=(),
                    interfaces=(),
                    fields={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "Namespace:Class": CClass(
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
                ),
                "Namespace:Delegate": CDelegate(
                    name="Delegate",
                    namespace="Namespace",
                    nested=None,
                    parameters=(),
                    return_type=CType(name="Void", namespace="System"),
                ),
                "Namespace:Enum": CEnum(
                    name="Enum",
                    namespace="Namespace",
                    nested=None,
                    fields=(),
                ),
                "Namespace:Struct": CStruct(
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
                ),
            },
        )
        json: JsonType = namespace.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
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
            json,
        )

        from_json: CNamespace = CNamespace.from_json(json)

        self.assertEqual(namespace, from_json)

    def test_compare(self) -> None:
        namespace0: CNamespace = CNamespace(name="NamespaceA", types={})
        namespace1: CNamespace = CNamespace(name="NamespaceB", types={})

        self.assertLess(namespace0, namespace1)

        self.assertLessEqual(namespace0, namespace1)

        self.assertLessEqual(namespace0, namespace0)
        self.assertLessEqual(namespace1, namespace1)

        self.assertGreater(namespace1, namespace0)

        self.assertGreaterEqual(namespace1, namespace0)

        self.assertGreaterEqual(namespace0, namespace0)
        self.assertGreaterEqual(namespace1, namespace1)

    def test_sorted(self) -> None:
        ordered: Sequence[CNamespace] = (
            CNamespace(name="NamespaceA", types={}),
            CNamespace(name="NamespaceB", types={}),
            CNamespace(name="NamespaceC", types={}),
            CNamespace(name="NamespaceD", types={}),
        )
        unordered: MutableSequence[CNamespace] = list(ordered)
        random.shuffle(unordered)

        self.assertSequenceEqual(ordered, sorted(unordered))


class TestCClass(TestBase):
    def test_json_generic(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(CType(name="T", generic=True),),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "class",
                "name": "Class",
                "namespace": "Namespace",
                "nested": None,
                "abstract": False,
                "generic_args": ("$T",),
                "super_class": None,
                "interfaces": (),
                "fields": {},
                "constructors": {},
                "properties": {},
                "methods": {},
                "events": {},
                "nested_types": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_generic_multi(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(
                CType(name="U", generic=True),
                CType(name="V", generic=True),
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
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "class",
                "name": "Class",
                "namespace": "Namespace",
                "nested": None,
                "abstract": False,
                "generic_args": ("$U", "$V"),
                "super_class": None,
                "interfaces": (),
                "fields": {},
                "constructors": {},
                "properties": {},
                "methods": {},
                "events": {},
                "nested_types": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_interfaces(self) -> None:
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
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "class",
                "name": "Class",
                "namespace": "Namespace",
                "nested": None,
                "abstract": False,
                "generic_args": (),
                "super_class": None,
                "interfaces": ("Namespace:InterfaceA", "Namespace:InterfaceB"),
                "fields": {},
                "constructors": {},
                "properties": {},
                "methods": {},
                "events": {},
                "nested_types": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_fields(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={
                "Namespace:Class.InstanceFieldA": CField(
                    name="InstanceFieldA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    return_type=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace:Class.InstanceFieldB": CField(
                    name="InstanceFieldB",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    return_type=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace:Class.InstanceFieldC": CField(
                    name="InstanceFieldC",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    return_type=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace:Class.StaticFieldA": CField(
                    name="StaticFieldA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    return_type=CType(name="Type", namespace="Namespace"),
                    static=True,
                ),
                "Namespace:Class.StaticFieldB": CField(
                    name="StaticFieldB",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    return_type=CType(name="Type", namespace="Namespace"),
                    static=True,
                ),
                "Namespace:Class.StaticFieldC": CField(
                    name="StaticFieldC",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    return_type=CType(name="Type", namespace="Namespace"),
                    static=True,
                ),
            },
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "class",
                "name": "Class",
                "namespace": "Namespace",
                "nested": None,
                "abstract": False,
                "generic_args": (),
                "super_class": None,
                "interfaces": (),
                "fields": {
                    "Namespace:Class.InstanceFieldA": {
                        "name": "InstanceFieldA",
                        "declaring_type": "Namespace:Class",
                        "return_type": "Namespace:Type",
                        "static": False,
                    },
                    "Namespace:Class.InstanceFieldB": {
                        "name": "InstanceFieldB",
                        "declaring_type": "Namespace:Class",
                        "return_type": "Namespace:Type",
                        "static": False,
                    },
                    "Namespace:Class.InstanceFieldC": {
                        "name": "InstanceFieldC",
                        "declaring_type": "Namespace:Class",
                        "return_type": "Namespace:Type",
                        "static": False,
                    },
                    "Namespace:Class.StaticFieldA": {
                        "name": "StaticFieldA",
                        "declaring_type": "Namespace:Class",
                        "return_type": "Namespace:Type",
                        "static": True,
                    },
                    "Namespace:Class.StaticFieldB": {
                        "name": "StaticFieldB",
                        "declaring_type": "Namespace:Class",
                        "return_type": "Namespace:Type",
                        "static": True,
                    },
                    "Namespace:Class.StaticFieldC": {
                        "name": "StaticFieldC",
                        "declaring_type": "Namespace:Class",
                        "return_type": "Namespace:Type",
                        "static": True,
                    },
                },
                "constructors": {},
                "properties": {},
                "methods": {},
                "events": {},
                "nested_types": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_constructors(self) -> None:
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
                "Namespace:Class.__init__(Namespace:Type, Namespace:Type)": CConstructor(
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                        CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
                    ),
                ),
                "Namespace:Class.__init__(Namespace:Type, Namespace:Type, Namespace:Type)": CConstructor(
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                        CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
                        CParameter(name="param2", type=CType(name="Type", namespace="Namespace")),
                    ),
                ),
            },
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "class",
                "name": "Class",
                "namespace": "Namespace",
                "nested": None,
                "abstract": False,
                "generic_args": (),
                "super_class": None,
                "interfaces": (),
                "fields": {},
                "constructors": {
                    "Namespace:Class.__init__()": {
                        "declaring_type": "Namespace:Class",
                        "parameters": (),
                    },
                    "Namespace:Class.__init__(Namespace:Type)": {
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:Type",
                                "default": False,
                                "out": False,
                            },
                        ),
                    },
                    "Namespace:Class.__init__(Namespace:Type, Namespace:Type)": {
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:Type",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "param1",
                                "type": "Namespace:Type",
                                "default": False,
                                "out": False,
                            },
                        ),
                    },
                    "Namespace:Class.__init__(Namespace:Type, Namespace:Type, Namespace:Type)": {
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:Type",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "param1",
                                "type": "Namespace:Type",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "param2",
                                "type": "Namespace:Type",
                                "default": False,
                                "out": False,
                            },
                        ),
                    },
                },
                "properties": {},
                "methods": {},
                "events": {},
                "nested_types": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_properties(self) -> None:
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
                "Namespace:Class.InstanceProperty0": CProperty(
                    name="InstanceProperty0",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    setter=True,
                ),
                "Namespace:Class.InstanceProperty1": CProperty(
                    name="InstanceProperty1",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    setter=True,
                ),
                "Namespace:Class.InstanceProperty2": CProperty(
                    name="InstanceProperty2",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    setter=True,
                ),
                "Namespace:Class.InstanceReadOnlyProperty0": CProperty(
                    name="InstanceReadOnlyProperty0",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace:Class.InstanceReadOnlyProperty1": CProperty(
                    name="InstanceReadOnlyProperty1",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace:Class.InstanceReadOnlyProperty2": CProperty(
                    name="InstanceReadOnlyProperty2",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace:Class.StaticProperty0": CProperty(
                    name="StaticProperty0",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    setter=True,
                    static=True,
                ),
                "Namespace:Class.StaticProperty1": CProperty(
                    name="StaticProperty1",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    setter=True,
                    static=True,
                ),
                "Namespace:Class.StaticProperty2": CProperty(
                    name="StaticProperty2",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    setter=True,
                    static=True,
                ),
                "Namespace:Class.StaticReadOnlyProperty0": CProperty(
                    name="StaticReadOnlyProperty0",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    static=True,
                ),
                "Namespace:Class.StaticReadOnlyProperty1": CProperty(
                    name="StaticReadOnlyProperty1",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    static=True,
                ),
                "Namespace:Class.StaticReadOnlyProperty2": CProperty(
                    name="StaticReadOnlyProperty2",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    static=True,
                ),
            },
            methods={},
            events={},
            nested_types={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
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
                "properties": {
                    "Namespace:Class.InstanceProperty0": {
                        "name": "InstanceProperty0",
                        "declaring_type": "Namespace:Class",
                        "type": "Namespace:Type",
                        "setter": True,
                        "static": False,
                    },
                    "Namespace:Class.InstanceProperty1": {
                        "name": "InstanceProperty1",
                        "declaring_type": "Namespace:Class",
                        "type": "Namespace:Type",
                        "setter": True,
                        "static": False,
                    },
                    "Namespace:Class.InstanceProperty2": {
                        "name": "InstanceProperty2",
                        "declaring_type": "Namespace:Class",
                        "type": "Namespace:Type",
                        "setter": True,
                        "static": False,
                    },
                    "Namespace:Class.InstanceReadOnlyProperty0": {
                        "name": "InstanceReadOnlyProperty0",
                        "declaring_type": "Namespace:Class",
                        "type": "Namespace:Type",
                        "setter": False,
                        "static": False,
                    },
                    "Namespace:Class.InstanceReadOnlyProperty1": {
                        "name": "InstanceReadOnlyProperty1",
                        "declaring_type": "Namespace:Class",
                        "type": "Namespace:Type",
                        "setter": False,
                        "static": False,
                    },
                    "Namespace:Class.InstanceReadOnlyProperty2": {
                        "name": "InstanceReadOnlyProperty2",
                        "declaring_type": "Namespace:Class",
                        "type": "Namespace:Type",
                        "setter": False,
                        "static": False,
                    },
                    "Namespace:Class.StaticProperty0": {
                        "name": "StaticProperty0",
                        "declaring_type": "Namespace:Class",
                        "type": "Namespace:Type",
                        "setter": True,
                        "static": True,
                    },
                    "Namespace:Class.StaticProperty1": {
                        "name": "StaticProperty1",
                        "declaring_type": "Namespace:Class",
                        "type": "Namespace:Type",
                        "setter": True,
                        "static": True,
                    },
                    "Namespace:Class.StaticProperty2": {
                        "name": "StaticProperty2",
                        "declaring_type": "Namespace:Class",
                        "type": "Namespace:Type",
                        "setter": True,
                        "static": True,
                    },
                    "Namespace:Class.StaticReadOnlyProperty0": {
                        "name": "StaticReadOnlyProperty0",
                        "declaring_type": "Namespace:Class",
                        "type": "Namespace:Type",
                        "setter": False,
                        "static": True,
                    },
                    "Namespace:Class.StaticReadOnlyProperty1": {
                        "name": "StaticReadOnlyProperty1",
                        "declaring_type": "Namespace:Class",
                        "type": "Namespace:Type",
                        "setter": False,
                        "static": True,
                    },
                    "Namespace:Class.StaticReadOnlyProperty2": {
                        "name": "StaticReadOnlyProperty2",
                        "declaring_type": "Namespace:Class",
                        "type": "Namespace:Type",
                        "setter": False,
                        "static": True,
                    },
                },
                "methods": {},
                "events": {},
                "nested_types": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_methods(self) -> None:
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
                "Namespace:Class.InstanceMethodWithDefaultParam(Namespace:Type) -> Namespace:Type": CMethod(
                    name="InstanceMethodWithDefaultParam",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace"),
                            default=True,
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace:Class.InstanceMethodWithNullableDefaultParam(Namespace:Type?) -> Namespace:Type": CMethod(
                    name="InstanceMethodWithNullableDefaultParam",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace", nullable=True),
                            default=True,
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace:Class.InstanceMethodWithNullableOutParam(Namespace:*Type?) -> Namespace:Type, Namespace:*Type?": CMethod(
                    name="InstanceMethodWithNullableOutParam",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(
                                name="Type", namespace="Namespace", reference=True, nullable=True
                            ),
                            out=True,
                        ),
                    ),
                    return_types=(
                        CType(name="Type", namespace="Namespace"),
                        CType(name="Type", namespace="Namespace", reference=True, nullable=True),
                    ),
                ),
                "Namespace:Class.InstanceMethodWithNullableParam(Namespace:Type?) -> Namespace:Type": CMethod(
                    name="InstanceMethodWithNullableParam",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace", nullable=True),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace:Class.InstanceMethodWithOutParam(Namespace:*Type) -> Namespace:Type, Namespace:*Type": CMethod(
                    name="InstanceMethodWithOutParam",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace", reference=True),
                            out=True,
                        ),
                    ),
                    return_types=(
                        CType(name="Type", namespace="Namespace"),
                        CType(name="Type", namespace="Namespace", reference=True),
                    ),
                ),
                "Namespace:Class.InstanceMethodWithParams0() -> Namespace:Type": CMethod(
                    name="InstanceMethodWithParams0",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace:Class.InstanceMethodWithParams1(Namespace:Type) -> Namespace:Type": CMethod(
                    name="InstanceMethodWithParams1",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace:Class.InstanceMethodWithParams2(Namespace:Type, Namespace:Type) -> Namespace:Type": CMethod(
                    name="InstanceMethodWithParams2",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                        CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace:Class.StaticMethodWithDefaultParam(Namespace:Type) -> Namespace:Type": CMethod(
                    name="StaticMethodWithDefaultParam",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace"),
                            default=True,
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Class.StaticMethodWithNullableDefaultParam(Namespace:Type?) -> Namespace:Type": CMethod(
                    name="StaticMethodWithNullableDefaultParam",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace", nullable=True),
                            default=True,
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Class.StaticMethodWithNullableOutParam(Namespace:*Type?) -> Namespace:Type, Namespace:*Type?": CMethod(
                    name="StaticMethodWithNullableOutParam",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(
                                name="Type", namespace="Namespace", reference=True, nullable=True
                            ),
                            out=True,
                        ),
                    ),
                    return_types=(
                        CType(name="Type", namespace="Namespace"),
                        CType(name="Type", namespace="Namespace", reference=True, nullable=True),
                    ),
                    static=True,
                ),
                "Namespace:Class.StaticMethodWithNullableParam(Namespace:Type?) -> Namespace:Type": CMethod(
                    name="StaticMethodWithNullableParam",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace", nullable=True),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Class.StaticMethodWithOutParam(Namespace:*Type) -> Namespace:Type, Namespace:*Type": CMethod(
                    name="StaticMethodWithOutParam",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace", reference=True),
                            out=True,
                        ),
                    ),
                    return_types=(
                        CType(name="Type", namespace="Namespace"),
                        CType(name="Type", namespace="Namespace", reference=True),
                    ),
                    static=True,
                ),
                "Namespace:Class.StaticMethodWithParams0() -> Namespace:Type": CMethod(
                    name="StaticMethodWithParams0",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Class.StaticMethodWithParams1(Namespace:Type) -> Namespace:Type": CMethod(
                    name="StaticMethodWithParams1",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Class.StaticMethodWithParams2(Namespace:Type, Namespace:Type) -> Namespace:Type": CMethod(
                    name="StaticMethodWithParams2",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                        CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
            },
            events={},
            nested_types={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
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
                "methods": {
                    "Namespace:Class.InstanceMethodWithDefaultParam(Namespace:Type) -> Namespace:Type": {
                        "name": "InstanceMethodWithDefaultParam",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:Type",
                                "default": True,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": False,
                    },
                    "Namespace:Class.InstanceMethodWithNullableDefaultParam(Namespace:Type?) -> Namespace:Type": {
                        "name": "InstanceMethodWithNullableDefaultParam",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:Type?",
                                "default": True,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": False,
                    },
                    "Namespace:Class.InstanceMethodWithNullableOutParam(Namespace:*Type?) -> Namespace:Type, Namespace:*Type?": {
                        "name": "InstanceMethodWithNullableOutParam",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:*Type?",
                                "default": False,
                                "out": True,
                            },
                        ),
                        "return_types": ("Namespace:Type", "Namespace:*Type?"),
                        "static": False,
                    },
                    "Namespace:Class.InstanceMethodWithNullableParam(Namespace:Type?) -> Namespace:Type": {
                        "name": "InstanceMethodWithNullableParam",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:Type?",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": False,
                    },
                    "Namespace:Class.InstanceMethodWithOutParam(Namespace:*Type) -> Namespace:Type, Namespace:*Type": {
                        "name": "InstanceMethodWithOutParam",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:*Type",
                                "default": False,
                                "out": True,
                            },
                        ),
                        "return_types": ("Namespace:Type", "Namespace:*Type"),
                        "static": False,
                    },
                    "Namespace:Class.InstanceMethodWithParams0() -> Namespace:Type": {
                        "name": "InstanceMethodWithParams0",
                        "declaring_type": "Namespace:Class",
                        "parameters": (),
                        "return_types": ("Namespace:Type",),
                        "static": False,
                    },
                    "Namespace:Class.InstanceMethodWithParams1(Namespace:Type) -> Namespace:Type": {
                        "name": "InstanceMethodWithParams1",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:Type",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": False,
                    },
                    "Namespace:Class.InstanceMethodWithParams2(Namespace:Type, Namespace:Type) -> Namespace:Type": {
                        "name": "InstanceMethodWithParams2",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:Type",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "param1",
                                "type": "Namespace:Type",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": False,
                    },
                    "Namespace:Class.StaticMethodWithDefaultParam(Namespace:Type) -> Namespace:Type": {
                        "name": "StaticMethodWithDefaultParam",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:Type",
                                "default": True,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": True,
                    },
                    "Namespace:Class.StaticMethodWithNullableDefaultParam(Namespace:Type?) -> Namespace:Type": {
                        "name": "StaticMethodWithNullableDefaultParam",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:Type?",
                                "default": True,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": True,
                    },
                    "Namespace:Class.StaticMethodWithNullableOutParam(Namespace:*Type?) -> Namespace:Type, Namespace:*Type?": {
                        "name": "StaticMethodWithNullableOutParam",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:*Type?",
                                "default": False,
                                "out": True,
                            },
                        ),
                        "return_types": ("Namespace:Type", "Namespace:*Type?"),
                        "static": True,
                    },
                    "Namespace:Class.StaticMethodWithNullableParam(Namespace:Type?) -> Namespace:Type": {
                        "name": "StaticMethodWithNullableParam",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:Type?",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": True,
                    },
                    "Namespace:Class.StaticMethodWithOutParam(Namespace:*Type) -> Namespace:Type, Namespace:*Type": {
                        "name": "StaticMethodWithOutParam",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:*Type",
                                "default": False,
                                "out": True,
                            },
                        ),
                        "return_types": ("Namespace:Type", "Namespace:*Type"),
                        "static": True,
                    },
                    "Namespace:Class.StaticMethodWithParams0() -> Namespace:Type": {
                        "name": "StaticMethodWithParams0",
                        "declaring_type": "Namespace:Class",
                        "parameters": (),
                        "return_types": ("Namespace:Type",),
                        "static": True,
                    },
                    "Namespace:Class.StaticMethodWithParams1(Namespace:Type) -> Namespace:Type": {
                        "name": "StaticMethodWithParams1",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:Type",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": True,
                    },
                    "Namespace:Class.StaticMethodWithParams2(Namespace:Type, Namespace:Type) -> Namespace:Type": {
                        "name": "StaticMethodWithParams2",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:Type",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "param1",
                                "type": "Namespace:Type",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": True,
                    },
                },
                "events": {},
                "nested_types": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_methods_dunder(self) -> None:
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
                "Namespace:Class.op_Addition(Namespace:Class, Namespace:Class) -> Namespace:Class": CMethod(
                    name="op_Addition",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Class", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Class.op_BitwiseAnd(Namespace:Class, Namespace:Class) -> Namespace:Class": CMethod(
                    name="op_BitwiseAnd",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Class", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Class.op_BitwiseOr(Namespace:Class, Namespace:Class) -> Namespace:Class": CMethod(
                    name="op_BitwiseOr",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Class", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Class.op_Decrement(Namespace:Class) -> Namespace:Class": CMethod(
                    name="op_Decrement",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Class", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Class.op_Division(Namespace:Class, Namespace:Class) -> Namespace:Class": CMethod(
                    name="op_Division",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Class", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Class.op_Equality(Namespace:Class, Namespace:Class) -> Namespace:Type": CMethod(
                    name="op_Equality",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Class.op_ExclusiveOr(Namespace:Class, Namespace:Class) -> Namespace:Class": CMethod(
                    name="op_ExclusiveOr",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Class", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Class.op_False(Namespace:Class) -> Namespace:Type": CMethod(
                    name="op_False",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(name="self", type=CType(name="Class", namespace="Namespace")),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Class.op_GreaterThan(Namespace:Class, Namespace:Class) -> Namespace:Type": CMethod(
                    name="op_GreaterThan",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Class.op_GreaterThanOrEqual(Namespace:Class, Namespace:Class) -> Namespace:Type": CMethod(
                    name="op_GreaterThanOrEqual",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Class.op_Increment(Namespace:Class) -> Namespace:Class": CMethod(
                    name="op_Increment",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Class", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Class.op_Inequality(Namespace:Class, Namespace:Class) -> Namespace:Type": CMethod(
                    name="op_Inequality",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Class.op_LessThan(Namespace:Class, Namespace:Class) -> Namespace:Type": CMethod(
                    name="op_LessThan",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Class.op_LessThanOrEqual(Namespace:Class, Namespace:Class) -> Namespace:Type": CMethod(
                    name="op_LessThanOrEqual",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Class.op_LogicalNot(Namespace:Class) -> Namespace:Type": CMethod(
                    name="op_LogicalNot",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Class.op_Modulus(Namespace:Class, Namespace:Class) -> Namespace:Class": CMethod(
                    name="op_Modulus",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Class", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Class.op_Multiply(Namespace:Class, Namespace:Class) -> Namespace:Class": CMethod(
                    name="op_Multiply",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Class", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Class.op_OnesComplement(Namespace:Class) -> Namespace:Class": CMethod(
                    name="op_OnesComplement",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Class", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Class.op_Subtraction(Namespace:Class, Namespace:Class) -> Namespace:Class": CMethod(
                    name="op_Subtraction",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Class", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Class.op_True(Namespace:Class) -> Namespace:Type": CMethod(
                    name="op_True",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Class.op_UnaryNegation(Namespace:Class) -> Namespace:Class": CMethod(
                    name="op_UnaryNegation",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Class", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Class.op_UnaryPlus(Namespace:Class) -> Namespace:Class": CMethod(
                    name="op_UnaryPlus",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Class", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Class.__add__(Namespace:Class) -> Namespace:Class": CMethod(
                    name="__add__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Class", namespace="Namespace"),),
                ),
                "Namespace:Class.__and__(Namespace:Class) -> Namespace:Class": CMethod(
                    name="__and__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Class", namespace="Namespace"),),
                ),
                "Namespace:Class.__eq__(Namespace:Class) -> Namespace:Type": CMethod(
                    name="__eq__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace:Class.__ge__(Namespace:Class) -> Namespace:Type": CMethod(
                    name="__ge__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace:Class.__gt__(Namespace:Class) -> Namespace:Type": CMethod(
                    name="__gt__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace:Class.__invert__() -> Namespace:Class": CMethod(
                    name="__invert__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(),
                    return_types=(CType(name="Class", namespace="Namespace"),),
                ),
                "Namespace:Class.__le__(Namespace:Class) -> Namespace:Type": CMethod(
                    name="__le__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace:Class.__lt__(Namespace:Class) -> Namespace:Type": CMethod(
                    name="__lt__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace:Class.__mod__(Namespace:Class) -> Namespace:Class": CMethod(
                    name="__mod__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Class", namespace="Namespace"),),
                ),
                "Namespace:Class.__mul__(Namespace:Class) -> Namespace:Class": CMethod(
                    name="__mul__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Class", namespace="Namespace"),),
                ),
                "Namespace:Class.__ne__(Namespace:Class) -> Namespace:Type": CMethod(
                    name="__ne__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="System"),),
                ),
                "Namespace:Class.__neg__() -> Namespace:Class": CMethod(
                    name="__neg__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(),
                    return_types=(CType(name="Class", namespace="Namespace"),),
                ),
                "Namespace:Class.__or__(Namespace:Class) -> Namespace:Class": CMethod(
                    name="__or__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Class", namespace="Namespace"),),
                ),
                "Namespace:Class.__pos__() -> Namespace:Class": CMethod(
                    name="__pos__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(),
                    return_types=(CType(name="Class", namespace="Namespace"),),
                ),
                "Namespace:Class.__sub__(Namespace:Class) -> Namespace:Class": CMethod(
                    name="__sub__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Class", namespace="Namespace"),),
                ),
                "Namespace:Class.__truediv__(Namespace:Class) -> Namespace:Class": CMethod(
                    name="__truediv__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Class", namespace="Namespace"),),
                ),
                "Namespace:Class.__xor__(Namespace:Class) -> Namespace:Class": CMethod(
                    name="__xor__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Class", namespace="Namespace"),),
                ),
            },
            events={},
            nested_types={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
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
                "methods": {
                    "Namespace:Class.op_Addition(Namespace:Class, Namespace:Class) -> Namespace:Class": {
                        "name": "op_Addition",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Class",),
                        "static": True,
                    },
                    "Namespace:Class.op_BitwiseAnd(Namespace:Class, Namespace:Class) -> Namespace:Class": {
                        "name": "op_BitwiseAnd",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Class",),
                        "static": True,
                    },
                    "Namespace:Class.op_BitwiseOr(Namespace:Class, Namespace:Class) -> Namespace:Class": {
                        "name": "op_BitwiseOr",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Class",),
                        "static": True,
                    },
                    "Namespace:Class.op_Decrement(Namespace:Class) -> Namespace:Class": {
                        "name": "op_Decrement",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Class",),
                        "static": True,
                    },
                    "Namespace:Class.op_Division(Namespace:Class, Namespace:Class) -> Namespace:Class": {
                        "name": "op_Division",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Class",),
                        "static": True,
                    },
                    "Namespace:Class.op_Equality(Namespace:Class, Namespace:Class) -> Namespace:Type": {
                        "name": "op_Equality",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": True,
                    },
                    "Namespace:Class.op_ExclusiveOr(Namespace:Class, Namespace:Class) -> Namespace:Class": {
                        "name": "op_ExclusiveOr",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Class",),
                        "static": True,
                    },
                    "Namespace:Class.op_False(Namespace:Class) -> Namespace:Type": {
                        "name": "op_False",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": True,
                    },
                    "Namespace:Class.op_GreaterThan(Namespace:Class, Namespace:Class) -> Namespace:Type": {
                        "name": "op_GreaterThan",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": True,
                    },
                    "Namespace:Class.op_GreaterThanOrEqual(Namespace:Class, Namespace:Class) -> Namespace:Type": {
                        "name": "op_GreaterThanOrEqual",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": True,
                    },
                    "Namespace:Class.op_Increment(Namespace:Class) -> Namespace:Class": {
                        "name": "op_Increment",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Class",),
                        "static": True,
                    },
                    "Namespace:Class.op_Inequality(Namespace:Class, Namespace:Class) -> Namespace:Type": {
                        "name": "op_Inequality",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": True,
                    },
                    "Namespace:Class.op_LessThan(Namespace:Class, Namespace:Class) -> Namespace:Type": {
                        "name": "op_LessThan",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": True,
                    },
                    "Namespace:Class.op_LessThanOrEqual(Namespace:Class, Namespace:Class) -> Namespace:Type": {
                        "name": "op_LessThanOrEqual",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": True,
                    },
                    "Namespace:Class.op_LogicalNot(Namespace:Class) -> Namespace:Type": {
                        "name": "op_LogicalNot",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": True,
                    },
                    "Namespace:Class.op_Modulus(Namespace:Class, Namespace:Class) -> Namespace:Class": {
                        "name": "op_Modulus",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Class",),
                        "static": True,
                    },
                    "Namespace:Class.op_Multiply(Namespace:Class, Namespace:Class) -> Namespace:Class": {
                        "name": "op_Multiply",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Class",),
                        "static": True,
                    },
                    "Namespace:Class.op_OnesComplement(Namespace:Class) -> Namespace:Class": {
                        "name": "op_OnesComplement",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Class",),
                        "static": True,
                    },
                    "Namespace:Class.op_Subtraction(Namespace:Class, Namespace:Class) -> Namespace:Class": {
                        "name": "op_Subtraction",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Class",),
                        "static": True,
                    },
                    "Namespace:Class.op_True(Namespace:Class) -> Namespace:Type": {
                        "name": "op_True",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": True,
                    },
                    "Namespace:Class.op_UnaryNegation(Namespace:Class) -> Namespace:Class": {
                        "name": "op_UnaryNegation",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Class",),
                        "static": True,
                    },
                    "Namespace:Class.op_UnaryPlus(Namespace:Class) -> Namespace:Class": {
                        "name": "op_UnaryPlus",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Class",),
                        "static": True,
                    },
                    "Namespace:Class.__add__(Namespace:Class) -> Namespace:Class": {
                        "name": "__add__",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Class",),
                        "static": False,
                    },
                    "Namespace:Class.__and__(Namespace:Class) -> Namespace:Class": {
                        "name": "__and__",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Class",),
                        "static": False,
                    },
                    "Namespace:Class.__eq__(Namespace:Class) -> Namespace:Type": {
                        "name": "__eq__",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": False,
                    },
                    "Namespace:Class.__ge__(Namespace:Class) -> Namespace:Type": {
                        "name": "__ge__",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": False,
                    },
                    "Namespace:Class.__gt__(Namespace:Class) -> Namespace:Type": {
                        "name": "__gt__",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": False,
                    },
                    "Namespace:Class.__invert__() -> Namespace:Class": {
                        "name": "__invert__",
                        "declaring_type": "Namespace:Class",
                        "parameters": (),
                        "return_types": ("Namespace:Class",),
                        "static": False,
                    },
                    "Namespace:Class.__le__(Namespace:Class) -> Namespace:Type": {
                        "name": "__le__",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": False,
                    },
                    "Namespace:Class.__lt__(Namespace:Class) -> Namespace:Type": {
                        "name": "__lt__",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": False,
                    },
                    "Namespace:Class.__mod__(Namespace:Class) -> Namespace:Class": {
                        "name": "__mod__",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Class",),
                        "static": False,
                    },
                    "Namespace:Class.__mul__(Namespace:Class) -> Namespace:Class": {
                        "name": "__mul__",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Class",),
                        "static": False,
                    },
                    "Namespace:Class.__ne__(Namespace:Class) -> Namespace:Type": {
                        "name": "__ne__",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("System:Type",),
                        "static": False,
                    },
                    "Namespace:Class.__neg__() -> Namespace:Class": {
                        "name": "__neg__",
                        "declaring_type": "Namespace:Class",
                        "parameters": (),
                        "return_types": ("Namespace:Class",),
                        "static": False,
                    },
                    "Namespace:Class.__or__(Namespace:Class) -> Namespace:Class": {
                        "name": "__or__",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Class",),
                        "static": False,
                    },
                    "Namespace:Class.__pos__() -> Namespace:Class": {
                        "name": "__pos__",
                        "declaring_type": "Namespace:Class",
                        "parameters": (),
                        "return_types": ("Namespace:Class",),
                        "static": False,
                    },
                    "Namespace:Class.__sub__(Namespace:Class) -> Namespace:Class": {
                        "name": "__sub__",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Class",),
                        "static": False,
                    },
                    "Namespace:Class.__truediv__(Namespace:Class) -> Namespace:Class": {
                        "name": "__truediv__",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Class",),
                        "static": False,
                    },
                    "Namespace:Class.__xor__(Namespace:Class) -> Namespace:Class": {
                        "name": "__xor__",
                        "declaring_type": "Namespace:Class",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Class",),
                        "static": False,
                    },
                },
                "events": {},
                "nested_types": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_events(self) -> None:
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
                "Namespace:Class.Event -> (System:EventHandler)": CEvent(
                    name="Event",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="EventHandler", namespace="System"),
                ),
                "Namespace:Class.EventWithArgs -> (System:EventHandler[System:EventArgs])": CEvent(
                    name="EventWithArgs",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(
                        name="EventHandler",
                        namespace="System",
                        inner=(CType(name="EventArgs", namespace="System"),),
                    ),
                ),
            },
            nested_types={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
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
                "events": {
                    "Namespace:Class.Event -> (System:EventHandler)": {
                        "name": "Event",
                        "declaring_type": "Namespace:Class",
                        "type": "System:EventHandler",
                    },
                    "Namespace:Class.EventWithArgs -> (System:EventHandler[System:EventArgs])": {
                        "name": "EventWithArgs",
                        "declaring_type": "Namespace:Class",
                        "type": "System:EventHandler[System:EventArgs]",
                    },
                },
                "nested_types": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_nested(self) -> None:
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
                "Namespace:Class.NestedDelegate": CDelegate(
                    name="NestedDelegate",
                    namespace="Namespace",
                    nested=CType(name="Class", namespace="Namespace"),
                    parameters=(),
                    return_type=CType(name="Void", namespace="System"),
                ),
                "Namespace:Class.NestedEnum": CEnum(
                    name="NestedEnum",
                    namespace="Namespace",
                    nested=CType(name="Class", namespace="Namespace"),
                    fields=(),
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
            },
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
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
                "nested_types": {
                    "Namespace:Class.INestedInterface": {
                        "type": "interface",
                        "name": "INestedInterface",
                        "namespace": "Namespace",
                        "nested": "Namespace:Class",
                        "generic_args": (),
                        "interfaces": (),
                        "fields": {},
                        "properties": {},
                        "methods": {},
                        "events": {},
                        "nested_types": {},
                    },
                    "Namespace:Class.NestedClass": {
                        "type": "class",
                        "name": "NestedClass",
                        "namespace": "Namespace",
                        "nested": "Namespace:Class",
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
                    "Namespace:Class.NestedDelegate": {
                        "type": "delegate",
                        "name": "NestedDelegate",
                        "namespace": "Namespace",
                        "nested": "Namespace:Class",
                        "parameters": (),
                        "return_type": "System:Void",
                    },
                    "Namespace:Class.NestedEnum": {
                        "type": "enum",
                        "name": "NestedEnum",
                        "namespace": "Namespace",
                        "nested": "Namespace:Class",
                        "fields": (),
                    },
                    "Namespace:Class.NestedStruct": {
                        "type": "struct",
                        "name": "NestedStruct",
                        "namespace": "Namespace",
                        "nested": "Namespace:Class",
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
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_doc_json(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={
                "Namespace:Class.Field": CField(
                    name="Field",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    return_type=CType(name="Type", namespace="Namespace"),
                )
            },
            constructors={
                "Namespace:Class.__init__(Namespace:Type)": CConstructor(
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                    ),
                ),
            },
            properties={
                "Namespace:Class.Property": CProperty(
                    name="Property",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                ),
            },
            methods={
                "Namespace:Class.Method": CMethod(
                    name="Method",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                ),
            },
            events={
                "Namespace:Class.Event": CEvent(
                    name="Event",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="EventHandler", namespace="System"),
                ),
            },
            nested_types={
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
                "Namespace:Class.NestedDelegate": CDelegate(
                    name="NestedDelegate",
                    namespace="Namespace",
                    nested=CType(name="Class", namespace="Namespace"),
                    parameters=(),
                    return_type=CType(name="Void", namespace="System"),
                ),
                "Namespace:Class.NestedEnum": CEnum(
                    name="NestedEnum",
                    namespace="Namespace",
                    nested=CType(name="Class", namespace="Namespace"),
                    fields=(),
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
            },
        )
        name: str
        json: JsonType
        name, json = type_def.to_doc_json()

        self.assertIsNotNone(name)
        self.assertIsInstance(name, str)
        self.assertEqual("Class", name)

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "doc": "",
                "doc_formatted": {},
                "Field": {"doc": "", "doc_formatted": {}, "return": ""},
                "__init__(Namespace:Type)": {
                    "doc": "",
                    "doc_formatted": {},
                    "parameters": {"param0": ""},
                },
                "Property": {"doc": "", "doc_formatted": {}, "return": ""},
                "Method(Namespace:Type)": {
                    "doc": "",
                    "doc_formatted": {},
                    "exceptions": {},
                    "parameters": {"param0": ""},
                    "return": "",
                },
                "Event": {"doc": "", "doc_formatted": {}},
                "INestedInterface": {"doc": "", "doc_formatted": {}},
                "NestedClass": {"doc": "", "doc_formatted": {}},
                "NestedDelegate()": {"doc": "", "doc_formatted": {}},
                "NestedEnum": {"doc": "", "doc_formatted": {}},
                "NestedStruct": {"doc": "", "doc_formatted": {}},
            },
            json,
        )

    def test_compare(self) -> None:
        struct0: CClass = CClass(
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
        struct1: CClass = CClass(
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

        self.assertLess(struct0, struct1)

        self.assertLessEqual(struct0, struct1)

        self.assertLessEqual(struct0, struct0)
        self.assertLessEqual(struct1, struct1)

        self.assertGreater(struct1, struct0)

        self.assertGreaterEqual(struct1, struct0)

        self.assertGreaterEqual(struct0, struct0)
        self.assertGreaterEqual(struct1, struct1)

    def test_sorted(self) -> None:
        ordered: Sequence[CClass] = (
            CClass(
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
            CClass(
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
            CClass(
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
            CClass(
                name="ClassD",
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
        )
        unordered: MutableSequence[CClass] = list(ordered)
        random.shuffle(unordered)

        self.assertSequenceEqual(ordered, sorted(unordered))


class TestCStruct(TestBase):
    def test_json_generic(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(CType(name="T", generic=True),),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "struct",
                "name": "Struct",
                "namespace": "Namespace",
                "nested": None,
                "abstract": False,
                "generic_args": ("$T",),
                "super_class": None,
                "interfaces": (),
                "fields": {},
                "constructors": {},
                "properties": {},
                "methods": {},
                "events": {},
                "nested_types": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_generic_multi(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(
                CType(name="U", generic=True),
                CType(name="V", generic=True),
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
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "struct",
                "name": "Struct",
                "namespace": "Namespace",
                "nested": None,
                "abstract": False,
                "generic_args": ("$U", "$V"),
                "super_class": None,
                "interfaces": (),
                "fields": {},
                "constructors": {},
                "properties": {},
                "methods": {},
                "events": {},
                "nested_types": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_interfaces(self) -> None:
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
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "struct",
                "name": "Struct",
                "namespace": "Namespace",
                "nested": None,
                "abstract": False,
                "generic_args": (),
                "super_class": None,
                "interfaces": ("Namespace:InterfaceA", "Namespace:InterfaceB"),
                "fields": {},
                "constructors": {},
                "properties": {},
                "methods": {},
                "events": {},
                "nested_types": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_fields(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={
                "Namespace:Struct.InstanceFieldA": CField(
                    name="InstanceFieldA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    return_type=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace:Struct.InstanceFieldB": CField(
                    name="InstanceFieldB",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    return_type=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace:Struct.InstanceFieldC": CField(
                    name="InstanceFieldC",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    return_type=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace:Struct.StaticFieldA": CField(
                    name="StaticFieldA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    return_type=CType(name="Type", namespace="Namespace"),
                    static=True,
                ),
                "Namespace:Struct.StaticFieldB": CField(
                    name="StaticFieldB",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    return_type=CType(name="Type", namespace="Namespace"),
                    static=True,
                ),
                "Namespace:Struct.StaticFieldC": CField(
                    name="StaticFieldC",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    return_type=CType(name="Type", namespace="Namespace"),
                    static=True,
                ),
            },
            constructors={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "struct",
                "name": "Struct",
                "namespace": "Namespace",
                "nested": None,
                "abstract": False,
                "generic_args": (),
                "super_class": None,
                "interfaces": (),
                "fields": {
                    "Namespace:Struct.InstanceFieldA": {
                        "name": "InstanceFieldA",
                        "declaring_type": "Namespace:Struct",
                        "return_type": "Namespace:Type",
                        "static": False,
                    },
                    "Namespace:Struct.InstanceFieldB": {
                        "name": "InstanceFieldB",
                        "declaring_type": "Namespace:Struct",
                        "return_type": "Namespace:Type",
                        "static": False,
                    },
                    "Namespace:Struct.InstanceFieldC": {
                        "name": "InstanceFieldC",
                        "declaring_type": "Namespace:Struct",
                        "return_type": "Namespace:Type",
                        "static": False,
                    },
                    "Namespace:Struct.StaticFieldA": {
                        "name": "StaticFieldA",
                        "declaring_type": "Namespace:Struct",
                        "return_type": "Namespace:Type",
                        "static": True,
                    },
                    "Namespace:Struct.StaticFieldB": {
                        "name": "StaticFieldB",
                        "declaring_type": "Namespace:Struct",
                        "return_type": "Namespace:Type",
                        "static": True,
                    },
                    "Namespace:Struct.StaticFieldC": {
                        "name": "StaticFieldC",
                        "declaring_type": "Namespace:Struct",
                        "return_type": "Namespace:Type",
                        "static": True,
                    },
                },
                "constructors": {},
                "properties": {},
                "methods": {},
                "events": {},
                "nested_types": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_constructors(self) -> None:
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
                "Namespace:Struct.__init__(Namespace:Type, Namespace:Type)": CConstructor(
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                        CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
                    ),
                ),
                "Namespace:Struct.__init__(Namespace:Type, Namespace:Type, Namespace:Type)": CConstructor(
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                        CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
                        CParameter(name="param2", type=CType(name="Type", namespace="Namespace")),
                    ),
                ),
            },
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "struct",
                "name": "Struct",
                "namespace": "Namespace",
                "nested": None,
                "abstract": False,
                "generic_args": (),
                "super_class": None,
                "interfaces": (),
                "fields": {},
                "constructors": {
                    "Namespace:Struct.__init__()": {
                        "declaring_type": "Namespace:Struct",
                        "parameters": (),
                    },
                    "Namespace:Struct.__init__(Namespace:Type)": {
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:Type",
                                "default": False,
                                "out": False,
                            },
                        ),
                    },
                    "Namespace:Struct.__init__(Namespace:Type, Namespace:Type)": {
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:Type",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "param1",
                                "type": "Namespace:Type",
                                "default": False,
                                "out": False,
                            },
                        ),
                    },
                    "Namespace:Struct.__init__(Namespace:Type, Namespace:Type, Namespace:Type)": {
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:Type",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "param1",
                                "type": "Namespace:Type",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "param2",
                                "type": "Namespace:Type",
                                "default": False,
                                "out": False,
                            },
                        ),
                    },
                },
                "properties": {},
                "methods": {},
                "events": {},
                "nested_types": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_properties(self) -> None:
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
                "Namespace:Struct.InstanceProperty0": CProperty(
                    name="InstanceProperty0",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    setter=True,
                ),
                "Namespace:Struct.InstanceProperty1": CProperty(
                    name="InstanceProperty1",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    setter=True,
                ),
                "Namespace:Struct.InstanceProperty2": CProperty(
                    name="InstanceProperty2",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    setter=True,
                ),
                "Namespace:Struct.InstanceReadOnlyProperty0": CProperty(
                    name="InstanceReadOnlyProperty0",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace:Struct.InstanceReadOnlyProperty1": CProperty(
                    name="InstanceReadOnlyProperty1",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace:Struct.InstanceReadOnlyProperty2": CProperty(
                    name="InstanceReadOnlyProperty2",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace:Struct.StaticProperty0": CProperty(
                    name="StaticProperty0",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    setter=True,
                    static=True,
                ),
                "Namespace:Struct.StaticProperty1": CProperty(
                    name="StaticProperty1",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    setter=True,
                    static=True,
                ),
                "Namespace:Struct.StaticProperty2": CProperty(
                    name="StaticProperty2",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    setter=True,
                    static=True,
                ),
                "Namespace:Struct.StaticReadOnlyProperty0": CProperty(
                    name="StaticReadOnlyProperty0",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    static=True,
                ),
                "Namespace:Struct.StaticReadOnlyProperty1": CProperty(
                    name="StaticReadOnlyProperty1",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    static=True,
                ),
                "Namespace:Struct.StaticReadOnlyProperty2": CProperty(
                    name="StaticReadOnlyProperty2",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    static=True,
                ),
            },
            methods={},
            events={},
            nested_types={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
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
                "properties": {
                    "Namespace:Struct.InstanceProperty0": {
                        "name": "InstanceProperty0",
                        "declaring_type": "Namespace:Struct",
                        "type": "Namespace:Type",
                        "setter": True,
                        "static": False,
                    },
                    "Namespace:Struct.InstanceProperty1": {
                        "name": "InstanceProperty1",
                        "declaring_type": "Namespace:Struct",
                        "type": "Namespace:Type",
                        "setter": True,
                        "static": False,
                    },
                    "Namespace:Struct.InstanceProperty2": {
                        "name": "InstanceProperty2",
                        "declaring_type": "Namespace:Struct",
                        "type": "Namespace:Type",
                        "setter": True,
                        "static": False,
                    },
                    "Namespace:Struct.InstanceReadOnlyProperty0": {
                        "name": "InstanceReadOnlyProperty0",
                        "declaring_type": "Namespace:Struct",
                        "type": "Namespace:Type",
                        "setter": False,
                        "static": False,
                    },
                    "Namespace:Struct.InstanceReadOnlyProperty1": {
                        "name": "InstanceReadOnlyProperty1",
                        "declaring_type": "Namespace:Struct",
                        "type": "Namespace:Type",
                        "setter": False,
                        "static": False,
                    },
                    "Namespace:Struct.InstanceReadOnlyProperty2": {
                        "name": "InstanceReadOnlyProperty2",
                        "declaring_type": "Namespace:Struct",
                        "type": "Namespace:Type",
                        "setter": False,
                        "static": False,
                    },
                    "Namespace:Struct.StaticProperty0": {
                        "name": "StaticProperty0",
                        "declaring_type": "Namespace:Struct",
                        "type": "Namespace:Type",
                        "setter": True,
                        "static": True,
                    },
                    "Namespace:Struct.StaticProperty1": {
                        "name": "StaticProperty1",
                        "declaring_type": "Namespace:Struct",
                        "type": "Namespace:Type",
                        "setter": True,
                        "static": True,
                    },
                    "Namespace:Struct.StaticProperty2": {
                        "name": "StaticProperty2",
                        "declaring_type": "Namespace:Struct",
                        "type": "Namespace:Type",
                        "setter": True,
                        "static": True,
                    },
                    "Namespace:Struct.StaticReadOnlyProperty0": {
                        "name": "StaticReadOnlyProperty0",
                        "declaring_type": "Namespace:Struct",
                        "type": "Namespace:Type",
                        "setter": False,
                        "static": True,
                    },
                    "Namespace:Struct.StaticReadOnlyProperty1": {
                        "name": "StaticReadOnlyProperty1",
                        "declaring_type": "Namespace:Struct",
                        "type": "Namespace:Type",
                        "setter": False,
                        "static": True,
                    },
                    "Namespace:Struct.StaticReadOnlyProperty2": {
                        "name": "StaticReadOnlyProperty2",
                        "declaring_type": "Namespace:Struct",
                        "type": "Namespace:Type",
                        "setter": False,
                        "static": True,
                    },
                },
                "methods": {},
                "events": {},
                "nested_types": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_methods(self) -> None:
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
                "Namespace:Struct.InstanceMethodWithDefaultParam(Namespace:Type) -> Namespace:Type": CMethod(
                    name="InstanceMethodWithDefaultParam",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace"),
                            default=True,
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace:Struct.InstanceMethodWithNullableDefaultParam(Namespace:Type?) -> Namespace:Type": CMethod(
                    name="InstanceMethodWithNullableDefaultParam",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace", nullable=True),
                            default=True,
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace:Struct.InstanceMethodWithNullableOutParam(Namespace:*Type?) -> Namespace:Type, Namespace:*Type?": CMethod(
                    name="InstanceMethodWithNullableOutParam",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(
                                name="Type", namespace="Namespace", reference=True, nullable=True
                            ),
                            out=True,
                        ),
                    ),
                    return_types=(
                        CType(name="Type", namespace="Namespace"),
                        CType(name="Type", namespace="Namespace", reference=True, nullable=True),
                    ),
                ),
                "Namespace:Struct.InstanceMethodWithNullableParam(Namespace:Type?) -> Namespace:Type": CMethod(
                    name="InstanceMethodWithNullableParam",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace", nullable=True),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace:Struct.InstanceMethodWithOutParam(Namespace:*Type) -> Namespace:Type, Namespace:*Type": CMethod(
                    name="InstanceMethodWithOutParam",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace", reference=True),
                            out=True,
                        ),
                    ),
                    return_types=(
                        CType(name="Type", namespace="Namespace"),
                        CType(name="Type", namespace="Namespace", reference=True),
                    ),
                ),
                "Namespace:Struct.InstanceMethodWithParams0() -> Namespace:Type": CMethod(
                    name="InstanceMethodWithParams0",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace:Struct.InstanceMethodWithParams1(Namespace:Type) -> Namespace:Type": CMethod(
                    name="InstanceMethodWithParams1",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace:Struct.InstanceMethodWithParams2(Namespace:Type, Namespace:Type) -> Namespace:Type": CMethod(
                    name="InstanceMethodWithParams2",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                        CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace:Struct.StaticMethodWithDefaultParam(Namespace:Type) -> Namespace:Type": CMethod(
                    name="StaticMethodWithDefaultParam",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace"),
                            default=True,
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Struct.StaticMethodWithNullableDefaultParam(Namespace:Type?) -> Namespace:Type": CMethod(
                    name="StaticMethodWithNullableDefaultParam",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace", nullable=True),
                            default=True,
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Struct.StaticMethodWithNullableOutParam(Namespace:*Type?) -> Namespace:Type, Namespace:*Type?": CMethod(
                    name="StaticMethodWithNullableOutParam",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(
                                name="Type", namespace="Namespace", reference=True, nullable=True
                            ),
                            out=True,
                        ),
                    ),
                    return_types=(
                        CType(name="Type", namespace="Namespace"),
                        CType(name="Type", namespace="Namespace", reference=True, nullable=True),
                    ),
                    static=True,
                ),
                "Namespace:Struct.StaticMethodWithNullableParam(Namespace:Type?) -> Namespace:Type": CMethod(
                    name="StaticMethodWithNullableParam",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace", nullable=True),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Struct.StaticMethodWithOutParam(Namespace:*Type) -> Namespace:Type, Namespace:*Type": CMethod(
                    name="StaticMethodWithOutParam",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace", reference=True),
                            out=True,
                        ),
                    ),
                    return_types=(
                        CType(name="Type", namespace="Namespace"),
                        CType(name="Type", namespace="Namespace", reference=True),
                    ),
                    static=True,
                ),
                "Namespace:Struct.StaticMethodWithParams0() -> Namespace:Type": CMethod(
                    name="StaticMethodWithParams0",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Struct.StaticMethodWithParams1(Namespace:Type) -> Namespace:Type": CMethod(
                    name="StaticMethodWithParams1",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Struct.StaticMethodWithParams2(Namespace:Type, Namespace:Type) -> Namespace:Type": CMethod(
                    name="StaticMethodWithParams2",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                        CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
            },
            events={},
            nested_types={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
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
                "methods": {
                    "Namespace:Struct.InstanceMethodWithDefaultParam(Namespace:Type) -> Namespace:Type": {
                        "name": "InstanceMethodWithDefaultParam",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:Type",
                                "default": True,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": False,
                    },
                    "Namespace:Struct.InstanceMethodWithNullableDefaultParam(Namespace:Type?) -> Namespace:Type": {
                        "name": "InstanceMethodWithNullableDefaultParam",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:Type?",
                                "default": True,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": False,
                    },
                    "Namespace:Struct.InstanceMethodWithNullableOutParam(Namespace:*Type?) -> Namespace:Type, Namespace:*Type?": {
                        "name": "InstanceMethodWithNullableOutParam",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:*Type?",
                                "default": False,
                                "out": True,
                            },
                        ),
                        "return_types": ("Namespace:Type", "Namespace:*Type?"),
                        "static": False,
                    },
                    "Namespace:Struct.InstanceMethodWithNullableParam(Namespace:Type?) -> Namespace:Type": {
                        "name": "InstanceMethodWithNullableParam",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:Type?",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": False,
                    },
                    "Namespace:Struct.InstanceMethodWithOutParam(Namespace:*Type) -> Namespace:Type, Namespace:*Type": {
                        "name": "InstanceMethodWithOutParam",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:*Type",
                                "default": False,
                                "out": True,
                            },
                        ),
                        "return_types": ("Namespace:Type", "Namespace:*Type"),
                        "static": False,
                    },
                    "Namespace:Struct.InstanceMethodWithParams0() -> Namespace:Type": {
                        "name": "InstanceMethodWithParams0",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (),
                        "return_types": ("Namespace:Type",),
                        "static": False,
                    },
                    "Namespace:Struct.InstanceMethodWithParams1(Namespace:Type) -> Namespace:Type": {
                        "name": "InstanceMethodWithParams1",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:Type",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": False,
                    },
                    "Namespace:Struct.InstanceMethodWithParams2(Namespace:Type, Namespace:Type) -> Namespace:Type": {
                        "name": "InstanceMethodWithParams2",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:Type",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "param1",
                                "type": "Namespace:Type",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": False,
                    },
                    "Namespace:Struct.StaticMethodWithDefaultParam(Namespace:Type) -> Namespace:Type": {
                        "name": "StaticMethodWithDefaultParam",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:Type",
                                "default": True,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": True,
                    },
                    "Namespace:Struct.StaticMethodWithNullableDefaultParam(Namespace:Type?) -> Namespace:Type": {
                        "name": "StaticMethodWithNullableDefaultParam",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:Type?",
                                "default": True,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": True,
                    },
                    "Namespace:Struct.StaticMethodWithNullableOutParam(Namespace:*Type?) -> Namespace:Type, Namespace:*Type?": {
                        "name": "StaticMethodWithNullableOutParam",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:*Type?",
                                "default": False,
                                "out": True,
                            },
                        ),
                        "return_types": ("Namespace:Type", "Namespace:*Type?"),
                        "static": True,
                    },
                    "Namespace:Struct.StaticMethodWithNullableParam(Namespace:Type?) -> Namespace:Type": {
                        "name": "StaticMethodWithNullableParam",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:Type?",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": True,
                    },
                    "Namespace:Struct.StaticMethodWithOutParam(Namespace:*Type) -> Namespace:Type, Namespace:*Type": {
                        "name": "StaticMethodWithOutParam",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:*Type",
                                "default": False,
                                "out": True,
                            },
                        ),
                        "return_types": ("Namespace:Type", "Namespace:*Type"),
                        "static": True,
                    },
                    "Namespace:Struct.StaticMethodWithParams0() -> Namespace:Type": {
                        "name": "StaticMethodWithParams0",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (),
                        "return_types": ("Namespace:Type",),
                        "static": True,
                    },
                    "Namespace:Struct.StaticMethodWithParams1(Namespace:Type) -> Namespace:Type": {
                        "name": "StaticMethodWithParams1",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:Type",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": True,
                    },
                    "Namespace:Struct.StaticMethodWithParams2(Namespace:Type, Namespace:Type) -> Namespace:Type": {
                        "name": "StaticMethodWithParams2",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace:Type",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "param1",
                                "type": "Namespace:Type",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": True,
                    },
                },
                "events": {},
                "nested_types": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_methods_dunder(self) -> None:
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
                "Namespace:Struct.op_Addition(Namespace:Struct, Namespace:Struct) -> Namespace:Struct": CMethod(
                    name="op_Addition",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Struct", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Struct.op_BitwiseAnd(Namespace:Struct, Namespace:Struct) -> Namespace:Struct": CMethod(
                    name="op_BitwiseAnd",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Struct", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Struct.op_BitwiseOr(Namespace:Struct, Namespace:Struct) -> Namespace:Struct": CMethod(
                    name="op_BitwiseOr",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Struct", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Struct.op_Decrement(Namespace:Struct) -> Namespace:Struct": CMethod(
                    name="op_Decrement",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Struct", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Struct.op_Division(Namespace:Struct, Namespace:Struct) -> Namespace:Struct": CMethod(
                    name="op_Division",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Struct", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Struct.op_Equality(Namespace:Struct, Namespace:Struct) -> Namespace:Type": CMethod(
                    name="op_Equality",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Struct.op_ExclusiveOr(Namespace:Struct, Namespace:Struct) -> Namespace:Struct": CMethod(
                    name="op_ExclusiveOr",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Struct", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Struct.op_False(Namespace:Struct) -> Namespace:Type": CMethod(
                    name="op_False",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(name="self", type=CType(name="Struct", namespace="Namespace")),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Struct.op_GreaterThan(Namespace:Struct, Namespace:Struct) -> Namespace:Type": CMethod(
                    name="op_GreaterThan",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Struct.op_GreaterThanOrEqual(Namespace:Struct, Namespace:Struct) -> Namespace:Type": CMethod(
                    name="op_GreaterThanOrEqual",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Struct.op_Increment(Namespace:Struct) -> Namespace:Struct": CMethod(
                    name="op_Increment",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Struct", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Struct.op_Inequality(Namespace:Struct, Namespace:Struct) -> Namespace:Type": CMethod(
                    name="op_Inequality",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Struct.op_LessThan(Namespace:Struct, Namespace:Struct) -> Namespace:Type": CMethod(
                    name="op_LessThan",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Struct.op_LessThanOrEqual(Namespace:Struct, Namespace:Struct) -> Namespace:Type": CMethod(
                    name="op_LessThanOrEqual",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Struct.op_LogicalNot(Namespace:Struct) -> Namespace:Type": CMethod(
                    name="op_LogicalNot",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Struct.op_Modulus(Namespace:Struct, Namespace:Struct) -> Namespace:Struct": CMethod(
                    name="op_Modulus",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Struct", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Struct.op_Multiply(Namespace:Struct, Namespace:Struct) -> Namespace:Struct": CMethod(
                    name="op_Multiply",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Struct", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Struct.op_OnesComplement(Namespace:Struct) -> Namespace:Struct": CMethod(
                    name="op_OnesComplement",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Struct", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Struct.op_Subtraction(Namespace:Struct, Namespace:Struct) -> Namespace:Struct": CMethod(
                    name="op_Subtraction",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Struct", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Struct.op_True(Namespace:Struct) -> Namespace:Type": CMethod(
                    name="op_True",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Struct.op_UnaryNegation(Namespace:Struct) -> Namespace:Struct": CMethod(
                    name="op_UnaryNegation",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Struct", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Struct.op_UnaryPlus(Namespace:Struct) -> Namespace:Struct": CMethod(
                    name="op_UnaryPlus",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Struct", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace:Struct.__add__(Namespace:Struct) -> Namespace:Struct": CMethod(
                    name="__add__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Struct", namespace="Namespace"),),
                ),
                "Namespace:Struct.__and__(Namespace:Struct) -> Namespace:Struct": CMethod(
                    name="__and__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Struct", namespace="Namespace"),),
                ),
                "Namespace:Struct.__eq__(Namespace:Struct) -> Namespace:Type": CMethod(
                    name="__eq__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace:Struct.__ge__(Namespace:Struct) -> Namespace:Type": CMethod(
                    name="__ge__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace:Struct.__gt__(Namespace:Struct) -> Namespace:Type": CMethod(
                    name="__gt__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace:Struct.__invert__() -> Namespace:Struct": CMethod(
                    name="__invert__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(),
                    return_types=(CType(name="Struct", namespace="Namespace"),),
                ),
                "Namespace:Struct.__le__(Namespace:Struct) -> Namespace:Type": CMethod(
                    name="__le__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace:Struct.__lt__(Namespace:Struct) -> Namespace:Type": CMethod(
                    name="__lt__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace:Struct.__mod__(Namespace:Struct) -> Namespace:Struct": CMethod(
                    name="__mod__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Struct", namespace="Namespace"),),
                ),
                "Namespace:Struct.__mul__(Namespace:Struct) -> Namespace:Struct": CMethod(
                    name="__mul__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Struct", namespace="Namespace"),),
                ),
                "Namespace:Struct.__ne__(Namespace:Struct) -> Namespace:Type": CMethod(
                    name="__ne__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Type", namespace="System"),),
                ),
                "Namespace:Struct.__neg__() -> Namespace:Struct": CMethod(
                    name="__neg__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(),
                    return_types=(CType(name="Struct", namespace="Namespace"),),
                ),
                "Namespace:Struct.__or__(Namespace:Struct) -> Namespace:Struct": CMethod(
                    name="__or__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Struct", namespace="Namespace"),),
                ),
                "Namespace:Struct.__pos__() -> Namespace:Struct": CMethod(
                    name="__pos__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(),
                    return_types=(CType(name="Struct", namespace="Namespace"),),
                ),
                "Namespace:Struct.__sub__(Namespace:Struct) -> Namespace:Struct": CMethod(
                    name="__sub__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Struct", namespace="Namespace"),),
                ),
                "Namespace:Struct.__truediv__(Namespace:Struct) -> Namespace:Struct": CMethod(
                    name="__truediv__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Struct", namespace="Namespace"),),
                ),
                "Namespace:Struct.__xor__(Namespace:Struct) -> Namespace:Struct": CMethod(
                    name="__xor__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    return_types=(CType(name="Struct", namespace="Namespace"),),
                ),
            },
            events={},
            nested_types={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
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
                "methods": {
                    "Namespace:Struct.op_Addition(Namespace:Struct, Namespace:Struct) -> Namespace:Struct": {
                        "name": "op_Addition",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Struct",),
                        "static": True,
                    },
                    "Namespace:Struct.op_BitwiseAnd(Namespace:Struct, Namespace:Struct) -> Namespace:Struct": {
                        "name": "op_BitwiseAnd",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Struct",),
                        "static": True,
                    },
                    "Namespace:Struct.op_BitwiseOr(Namespace:Struct, Namespace:Struct) -> Namespace:Struct": {
                        "name": "op_BitwiseOr",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Struct",),
                        "static": True,
                    },
                    "Namespace:Struct.op_Decrement(Namespace:Struct) -> Namespace:Struct": {
                        "name": "op_Decrement",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Struct",),
                        "static": True,
                    },
                    "Namespace:Struct.op_Division(Namespace:Struct, Namespace:Struct) -> Namespace:Struct": {
                        "name": "op_Division",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Struct",),
                        "static": True,
                    },
                    "Namespace:Struct.op_Equality(Namespace:Struct, Namespace:Struct) -> Namespace:Type": {
                        "name": "op_Equality",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": True,
                    },
                    "Namespace:Struct.op_ExclusiveOr(Namespace:Struct, Namespace:Struct) -> Namespace:Struct": {
                        "name": "op_ExclusiveOr",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Struct",),
                        "static": True,
                    },
                    "Namespace:Struct.op_False(Namespace:Struct) -> Namespace:Type": {
                        "name": "op_False",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": True,
                    },
                    "Namespace:Struct.op_GreaterThan(Namespace:Struct, Namespace:Struct) -> Namespace:Type": {
                        "name": "op_GreaterThan",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": True,
                    },
                    "Namespace:Struct.op_GreaterThanOrEqual(Namespace:Struct, Namespace:Struct) -> Namespace:Type": {
                        "name": "op_GreaterThanOrEqual",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": True,
                    },
                    "Namespace:Struct.op_Increment(Namespace:Struct) -> Namespace:Struct": {
                        "name": "op_Increment",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Struct",),
                        "static": True,
                    },
                    "Namespace:Struct.op_Inequality(Namespace:Struct, Namespace:Struct) -> Namespace:Type": {
                        "name": "op_Inequality",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": True,
                    },
                    "Namespace:Struct.op_LessThan(Namespace:Struct, Namespace:Struct) -> Namespace:Type": {
                        "name": "op_LessThan",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": True,
                    },
                    "Namespace:Struct.op_LessThanOrEqual(Namespace:Struct, Namespace:Struct) -> Namespace:Type": {
                        "name": "op_LessThanOrEqual",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": True,
                    },
                    "Namespace:Struct.op_LogicalNot(Namespace:Struct) -> Namespace:Type": {
                        "name": "op_LogicalNot",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": True,
                    },
                    "Namespace:Struct.op_Modulus(Namespace:Struct, Namespace:Struct) -> Namespace:Struct": {
                        "name": "op_Modulus",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Struct",),
                        "static": True,
                    },
                    "Namespace:Struct.op_Multiply(Namespace:Struct, Namespace:Struct) -> Namespace:Struct": {
                        "name": "op_Multiply",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Struct",),
                        "static": True,
                    },
                    "Namespace:Struct.op_OnesComplement(Namespace:Struct) -> Namespace:Struct": {
                        "name": "op_OnesComplement",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Struct",),
                        "static": True,
                    },
                    "Namespace:Struct.op_Subtraction(Namespace:Struct, Namespace:Struct) -> Namespace:Struct": {
                        "name": "op_Subtraction",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Struct",),
                        "static": True,
                    },
                    "Namespace:Struct.op_True(Namespace:Struct) -> Namespace:Type": {
                        "name": "op_True",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": True,
                    },
                    "Namespace:Struct.op_UnaryNegation(Namespace:Struct) -> Namespace:Struct": {
                        "name": "op_UnaryNegation",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Struct",),
                        "static": True,
                    },
                    "Namespace:Struct.op_UnaryPlus(Namespace:Struct) -> Namespace:Struct": {
                        "name": "op_UnaryPlus",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Struct",),
                        "static": True,
                    },
                    "Namespace:Struct.__add__(Namespace:Struct) -> Namespace:Struct": {
                        "name": "__add__",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Struct",),
                        "static": False,
                    },
                    "Namespace:Struct.__and__(Namespace:Struct) -> Namespace:Struct": {
                        "name": "__and__",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Struct",),
                        "static": False,
                    },
                    "Namespace:Struct.__eq__(Namespace:Struct) -> Namespace:Type": {
                        "name": "__eq__",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": False,
                    },
                    "Namespace:Struct.__ge__(Namespace:Struct) -> Namespace:Type": {
                        "name": "__ge__",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": False,
                    },
                    "Namespace:Struct.__gt__(Namespace:Struct) -> Namespace:Type": {
                        "name": "__gt__",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": False,
                    },
                    "Namespace:Struct.__invert__() -> Namespace:Struct": {
                        "name": "__invert__",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (),
                        "return_types": ("Namespace:Struct",),
                        "static": False,
                    },
                    "Namespace:Struct.__le__(Namespace:Struct) -> Namespace:Type": {
                        "name": "__le__",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": False,
                    },
                    "Namespace:Struct.__lt__(Namespace:Struct) -> Namespace:Type": {
                        "name": "__lt__",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Type",),
                        "static": False,
                    },
                    "Namespace:Struct.__mod__(Namespace:Struct) -> Namespace:Struct": {
                        "name": "__mod__",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Struct",),
                        "static": False,
                    },
                    "Namespace:Struct.__mul__(Namespace:Struct) -> Namespace:Struct": {
                        "name": "__mul__",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Struct",),
                        "static": False,
                    },
                    "Namespace:Struct.__ne__(Namespace:Struct) -> Namespace:Type": {
                        "name": "__ne__",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("System:Type",),
                        "static": False,
                    },
                    "Namespace:Struct.__neg__() -> Namespace:Struct": {
                        "name": "__neg__",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (),
                        "return_types": ("Namespace:Struct",),
                        "static": False,
                    },
                    "Namespace:Struct.__or__(Namespace:Struct) -> Namespace:Struct": {
                        "name": "__or__",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Struct",),
                        "static": False,
                    },
                    "Namespace:Struct.__pos__() -> Namespace:Struct": {
                        "name": "__pos__",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (),
                        "return_types": ("Namespace:Struct",),
                        "static": False,
                    },
                    "Namespace:Struct.__sub__(Namespace:Struct) -> Namespace:Struct": {
                        "name": "__sub__",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Struct",),
                        "static": False,
                    },
                    "Namespace:Struct.__truediv__(Namespace:Struct) -> Namespace:Struct": {
                        "name": "__truediv__",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Struct",),
                        "static": False,
                    },
                    "Namespace:Struct.__xor__(Namespace:Struct) -> Namespace:Struct": {
                        "name": "__xor__",
                        "declaring_type": "Namespace:Struct",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Struct",),
                        "static": False,
                    },
                },
                "events": {},
                "nested_types": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_events(self) -> None:
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
                "Namespace:Struct.Event -> (System:EventHandler)": CEvent(
                    name="Event",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="EventHandler", namespace="System"),
                ),
                "Namespace:Struct.EventWithArgs -> (System:EventHandler[System:EventArgs])": CEvent(
                    name="EventWithArgs",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(
                        name="EventHandler",
                        namespace="System",
                        inner=(CType(name="EventArgs", namespace="System"),),
                    ),
                ),
            },
            nested_types={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
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
                "events": {
                    "Namespace:Struct.Event -> (System:EventHandler)": {
                        "name": "Event",
                        "declaring_type": "Namespace:Struct",
                        "type": "System:EventHandler",
                    },
                    "Namespace:Struct.EventWithArgs -> (System:EventHandler[System:EventArgs])": {
                        "name": "EventWithArgs",
                        "declaring_type": "Namespace:Struct",
                        "type": "System:EventHandler[System:EventArgs]",
                    },
                },
                "nested_types": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_nested(self) -> None:
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
                "Namespace:Struct.NestedDelegate": CDelegate(
                    name="NestedDelegate",
                    namespace="Namespace",
                    nested=CType(name="Struct", namespace="Namespace"),
                    parameters=(),
                    return_type=CType(name="Void", namespace="System"),
                ),
                "Namespace:Struct.NestedEnum": CEnum(
                    name="NestedEnum",
                    namespace="Namespace",
                    nested=CType(name="Struct", namespace="Namespace"),
                    fields=(),
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
            },
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
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
                "nested_types": {
                    "Namespace:Struct.INestedInterface": {
                        "type": "interface",
                        "name": "INestedInterface",
                        "namespace": "Namespace",
                        "nested": "Namespace:Struct",
                        "generic_args": (),
                        "interfaces": (),
                        "fields": {},
                        "properties": {},
                        "methods": {},
                        "events": {},
                        "nested_types": {},
                    },
                    "Namespace:Struct.NestedClass": {
                        "type": "class",
                        "name": "NestedClass",
                        "namespace": "Namespace",
                        "nested": "Namespace:Struct",
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
                    "Namespace:Struct.NestedDelegate": {
                        "type": "delegate",
                        "name": "NestedDelegate",
                        "namespace": "Namespace",
                        "nested": "Namespace:Struct",
                        "parameters": (),
                        "return_type": "System:Void",
                    },
                    "Namespace:Struct.NestedEnum": {
                        "type": "enum",
                        "name": "NestedEnum",
                        "namespace": "Namespace",
                        "nested": "Namespace:Struct",
                        "fields": (),
                    },
                    "Namespace:Struct.NestedStruct": {
                        "type": "struct",
                        "name": "NestedStruct",
                        "namespace": "Namespace",
                        "nested": "Namespace:Struct",
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
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_doc_json(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={
                "Namespace:Struct.Field": CField(
                    name="Field",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    return_type=CType(name="Type", namespace="Namespace"),
                )
            },
            constructors={
                "Namespace:Struct.__init__(Namespace:Type)": CConstructor(
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                    ),
                ),
            },
            properties={
                "Namespace:Struct.Property": CProperty(
                    name="Property",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                ),
            },
            methods={
                "Namespace:Struct.Method": CMethod(
                    name="Method",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                ),
            },
            events={
                "Namespace:Struct.Event": CEvent(
                    name="Event",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="EventHandler", namespace="System"),
                ),
            },
            nested_types={
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
                "Namespace:Struct.NestedDelegate": CDelegate(
                    name="NestedDelegate",
                    namespace="Namespace",
                    nested=CType(name="Struct", namespace="Namespace"),
                    parameters=(),
                    return_type=CType(name="Void", namespace="System"),
                ),
                "Namespace:Struct.NestedEnum": CEnum(
                    name="NestedEnum",
                    namespace="Namespace",
                    nested=CType(name="Struct", namespace="Namespace"),
                    fields=(),
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
            },
        )
        name: str
        json: JsonType
        name, json = type_def.to_doc_json()

        self.assertIsNotNone(name)
        self.assertIsInstance(name, str)
        self.assertEqual("Struct", name)

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "doc": "",
                "doc_formatted": {},
                "Field": {"doc": "", "doc_formatted": {}, "return": ""},
                "__init__(Namespace:Type)": {
                    "doc": "",
                    "doc_formatted": {},
                    "parameters": {"param0": ""},
                },
                "Property": {"doc": "", "doc_formatted": {}, "return": ""},
                "Method(Namespace:Type)": {
                    "doc": "",
                    "doc_formatted": {},
                    "exceptions": {},
                    "parameters": {"param0": ""},
                    "return": "",
                },
                "Event": {"doc": "", "doc_formatted": {}},
                "INestedInterface": {"doc": "", "doc_formatted": {}},
                "NestedClass": {"doc": "", "doc_formatted": {}},
                "NestedDelegate()": {"doc": "", "doc_formatted": {}},
                "NestedEnum": {"doc": "", "doc_formatted": {}},
                "NestedStruct": {"doc": "", "doc_formatted": {}},
            },
            json,
        )

    def test_compare(self) -> None:
        struct0: CStruct = CStruct(
            name="StructA",
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
        struct1: CStruct = CStruct(
            name="StructB",
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

        self.assertLess(struct0, struct1)

        self.assertLessEqual(struct0, struct1)

        self.assertLessEqual(struct0, struct0)
        self.assertLessEqual(struct1, struct1)

        self.assertGreater(struct1, struct0)

        self.assertGreaterEqual(struct1, struct0)

        self.assertGreaterEqual(struct0, struct0)
        self.assertGreaterEqual(struct1, struct1)

    def test_sorted(self) -> None:
        ordered: Sequence[CStruct] = (
            CStruct(
                name="StructA",
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
            CStruct(
                name="StructB",
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
            CStruct(
                name="StructC",
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
            CStruct(
                name="StructD",
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
        )
        unordered: MutableSequence[CStruct] = list(ordered)
        random.shuffle(unordered)

        self.assertSequenceEqual(ordered, sorted(unordered))


class TestCInterface(TestBase):
    def test_json_generic(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(CType(name="T", generic=True),),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "interface",
                "name": "Interface",
                "namespace": "Namespace",
                "nested": None,
                "generic_args": ("$T",),
                "interfaces": (),
                "fields": {},
                "properties": {},
                "methods": {},
                "events": {},
                "nested_types": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_generic_multi(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(
                CType(name="U", generic=True),
                CType(name="V", generic=True),
            ),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "interface",
                "name": "Interface",
                "namespace": "Namespace",
                "nested": None,
                "generic_args": ("$U", "$V"),
                "interfaces": (),
                "fields": {},
                "properties": {},
                "methods": {},
                "events": {},
                "nested_types": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_generic_interfaces(self) -> None:
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
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "interface",
                "name": "Interface",
                "namespace": "Namespace",
                "nested": None,
                "generic_args": (),
                "interfaces": ("Namespace:InterfaceA", "Namespace:InterfaceB"),
                "fields": {},
                "properties": {},
                "methods": {},
                "events": {},
                "nested_types": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_generic_fields(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={
                "Namespace:Interface.StaticFieldA": CField(
                    name="StaticFieldA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    return_type=CType(name="Type", namespace="Namespace"),
                    static=True,
                ),
                "Namespace:Interface.StaticFieldB": CField(
                    name="StaticFieldB",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    return_type=CType(name="Type", namespace="Namespace"),
                    static=True,
                ),
                "Namespace:Interface.StaticFieldC": CField(
                    name="StaticFieldC",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    return_type=CType(name="Type", namespace="Namespace"),
                    static=True,
                ),
            },
            properties={},
            methods={},
            events={},
            nested_types={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "interface",
                "name": "Interface",
                "namespace": "Namespace",
                "nested": None,
                "generic_args": (),
                "interfaces": (),
                "fields": {
                    "Namespace:Interface.StaticFieldA": {
                        "name": "StaticFieldA",
                        "declaring_type": "Namespace:Interface",
                        "return_type": "Namespace:Type",
                        "static": True,
                    },
                    "Namespace:Interface.StaticFieldB": {
                        "name": "StaticFieldB",
                        "declaring_type": "Namespace:Interface",
                        "return_type": "Namespace:Type",
                        "static": True,
                    },
                    "Namespace:Interface.StaticFieldC": {
                        "name": "StaticFieldC",
                        "declaring_type": "Namespace:Interface",
                        "return_type": "Namespace:Type",
                        "static": True,
                    },
                },
                "properties": {},
                "methods": {},
                "events": {},
                "nested_types": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_generic_properties(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={
                "Namespace:Interface.InstanceProperty0": CProperty(
                    name="InstanceProperty0",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                ),
                "Namespace:Interface.InstanceProperty1": CProperty(
                    name="InstanceProperty1",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                ),
                "Namespace:Interface.InstanceProperty2": CProperty(
                    name="InstanceProperty2",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                ),
                "Namespace:Interface.InstanceReadOnlyProperty0": CProperty(
                    name="InstanceReadOnlyProperty0",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="Int32", namespace="System"),
                ),
                "Namespace:Interface.InstanceReadOnlyProperty1": CProperty(
                    name="InstanceReadOnlyProperty1",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="Int32", namespace="System"),
                ),
                "Namespace:Interface.InstanceReadOnlyProperty2": CProperty(
                    name="InstanceReadOnlyProperty2",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="Int32", namespace="System"),
                ),
                "Namespace:Interface.StaticProperty0": CProperty(
                    name="StaticProperty0",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                    static=True,
                ),
                "Namespace:Interface.StaticProperty1": CProperty(
                    name="StaticProperty1",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                    static=True,
                ),
                "Namespace:Interface.StaticProperty2": CProperty(
                    name="StaticProperty2",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                    static=True,
                ),
                "Namespace:Interface.StaticReadOnlyProperty0": CProperty(
                    name="StaticReadOnlyProperty0",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
                "Namespace:Interface.StaticReadOnlyProperty1": CProperty(
                    name="StaticReadOnlyProperty1",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
                "Namespace:Interface.StaticReadOnlyProperty2": CProperty(
                    name="StaticReadOnlyProperty2",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
            },
            methods={},
            events={},
            nested_types={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "interface",
                "name": "Interface",
                "namespace": "Namespace",
                "nested": None,
                "generic_args": (),
                "interfaces": (),
                "fields": {},
                "properties": {
                    "Namespace:Interface.InstanceProperty0": {
                        "name": "InstanceProperty0",
                        "declaring_type": "Namespace:Interface",
                        "type": "System:Int32",
                        "setter": True,
                        "static": False,
                    },
                    "Namespace:Interface.InstanceProperty1": {
                        "name": "InstanceProperty1",
                        "declaring_type": "Namespace:Interface",
                        "type": "System:Int32",
                        "setter": True,
                        "static": False,
                    },
                    "Namespace:Interface.InstanceProperty2": {
                        "name": "InstanceProperty2",
                        "declaring_type": "Namespace:Interface",
                        "type": "System:Int32",
                        "setter": True,
                        "static": False,
                    },
                    "Namespace:Interface.InstanceReadOnlyProperty0": {
                        "name": "InstanceReadOnlyProperty0",
                        "declaring_type": "Namespace:Interface",
                        "type": "System:Int32",
                        "setter": False,
                        "static": False,
                    },
                    "Namespace:Interface.InstanceReadOnlyProperty1": {
                        "name": "InstanceReadOnlyProperty1",
                        "declaring_type": "Namespace:Interface",
                        "type": "System:Int32",
                        "setter": False,
                        "static": False,
                    },
                    "Namespace:Interface.InstanceReadOnlyProperty2": {
                        "name": "InstanceReadOnlyProperty2",
                        "declaring_type": "Namespace:Interface",
                        "type": "System:Int32",
                        "setter": False,
                        "static": False,
                    },
                    "Namespace:Interface.StaticProperty0": {
                        "name": "StaticProperty0",
                        "declaring_type": "Namespace:Interface",
                        "type": "System:Int32",
                        "setter": True,
                        "static": True,
                    },
                    "Namespace:Interface.StaticProperty1": {
                        "name": "StaticProperty1",
                        "declaring_type": "Namespace:Interface",
                        "type": "System:Int32",
                        "setter": True,
                        "static": True,
                    },
                    "Namespace:Interface.StaticProperty2": {
                        "name": "StaticProperty2",
                        "declaring_type": "Namespace:Interface",
                        "type": "System:Int32",
                        "setter": True,
                        "static": True,
                    },
                    "Namespace:Interface.StaticReadOnlyProperty0": {
                        "name": "StaticReadOnlyProperty0",
                        "declaring_type": "Namespace:Interface",
                        "type": "System:Int32",
                        "setter": False,
                        "static": True,
                    },
                    "Namespace:Interface.StaticReadOnlyProperty1": {
                        "name": "StaticReadOnlyProperty1",
                        "declaring_type": "Namespace:Interface",
                        "type": "System:Int32",
                        "setter": False,
                        "static": True,
                    },
                    "Namespace:Interface.StaticReadOnlyProperty2": {
                        "name": "StaticReadOnlyProperty2",
                        "declaring_type": "Namespace:Interface",
                        "type": "System:Int32",
                        "setter": False,
                        "static": True,
                    },
                },
                "methods": {},
                "events": {},
                "nested_types": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_generic_methods(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={
                "Namespace:Interface.InstanceMethodWithDefaultParam(System:Int32) -> System:Int32": CMethod(
                    name="InstanceMethodWithDefaultParam",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System"),
                            default=True,
                        ),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "Namespace:Interface.InstanceMethodWithNullableDefaultParam(System:Int32?) -> System:Int32": CMethod(
                    name="InstanceMethodWithNullableDefaultParam",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(
                                name="Int32",
                                namespace="System",
                                nullable=True,
                            ),
                            default=True,
                        ),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "Namespace:Interface.InstanceMethodWithNullableOutParam(System:*Int32?) -> System:Int32, System:*Int32?": CMethod(
                    name="InstanceMethodWithNullableOutParam",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(
                                name="Int32", namespace="System", reference=True, nullable=True
                            ),
                            out=True,
                        ),
                    ),
                    return_types=(
                        CType(name="Int32", namespace="System"),
                        CType(name="Int32", namespace="System", reference=True, nullable=True),
                    ),
                ),
                "Namespace:Interface.InstanceMethodWithNullableParam(System:Int32?) -> System:Int32": CMethod(
                    name="InstanceMethodWithNullableParam",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System", nullable=True),
                        ),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "Namespace:Interface.InstanceMethodWithOutParam(System:*Int32) -> System:Int32, System:*Int32": CMethod(
                    name="InstanceMethodWithOutParam",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System", reference=True),
                            out=True,
                        ),
                    ),
                    return_types=(
                        CType(name="Int32", namespace="System"),
                        CType(name="Int32", namespace="System", reference=True),
                    ),
                ),
                "Namespace:Interface.InstanceMethodWithParams() -> System:Int32": CMethod(
                    name="InstanceMethodWithParams",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "Namespace:Interface.InstanceMethodWithParams(System:Int32) -> System:Int32": CMethod(
                    name="InstanceMethodWithParams",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "Namespace:Interface.InstanceMethodWithParams(System:Int32, System:Int32) -> System:Int32": CMethod(
                    name="InstanceMethodWithParams",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                        CParameter(name="param1", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
            },
            events={},
            nested_types={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "interface",
                "name": "Interface",
                "namespace": "Namespace",
                "nested": None,
                "generic_args": (),
                "interfaces": (),
                "fields": {},
                "properties": {},
                "methods": {
                    "Namespace:Interface.InstanceMethodWithDefaultParam(System:Int32) -> System:Int32": {
                        "name": "InstanceMethodWithDefaultParam",
                        "declaring_type": "Namespace:Interface",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "System:Int32",
                                "default": True,
                                "out": False,
                            },
                        ),
                        "return_types": ("System:Int32",),
                        "static": False,
                    },
                    "Namespace:Interface.InstanceMethodWithNullableDefaultParam(System:Int32?) -> System:Int32": {
                        "name": "InstanceMethodWithNullableDefaultParam",
                        "declaring_type": "Namespace:Interface",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "System:Int32?",
                                "default": True,
                                "out": False,
                            },
                        ),
                        "return_types": ("System:Int32",),
                        "static": False,
                    },
                    "Namespace:Interface.InstanceMethodWithNullableOutParam(System:*Int32?) -> System:Int32, System:*Int32?": {
                        "name": "InstanceMethodWithNullableOutParam",
                        "declaring_type": "Namespace:Interface",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "System:*Int32?",
                                "default": False,
                                "out": True,
                            },
                        ),
                        "return_types": ("System:Int32", "System:*Int32?"),
                        "static": False,
                    },
                    "Namespace:Interface.InstanceMethodWithNullableParam(System:Int32?) -> System:Int32": {
                        "name": "InstanceMethodWithNullableParam",
                        "declaring_type": "Namespace:Interface",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "System:Int32?",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("System:Int32",),
                        "static": False,
                    },
                    "Namespace:Interface.InstanceMethodWithOutParam(System:*Int32) -> System:Int32, System:*Int32": {
                        "name": "InstanceMethodWithOutParam",
                        "declaring_type": "Namespace:Interface",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "System:*Int32",
                                "default": False,
                                "out": True,
                            },
                        ),
                        "return_types": ("System:Int32", "System:*Int32"),
                        "static": False,
                    },
                    "Namespace:Interface.InstanceMethodWithParams() -> System:Int32": {
                        "name": "InstanceMethodWithParams",
                        "declaring_type": "Namespace:Interface",
                        "parameters": (),
                        "return_types": ("System:Int32",),
                        "static": False,
                    },
                    "Namespace:Interface.InstanceMethodWithParams(System:Int32) -> System:Int32": {
                        "name": "InstanceMethodWithParams",
                        "declaring_type": "Namespace:Interface",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "System:Int32",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("System:Int32",),
                        "static": False,
                    },
                    "Namespace:Interface.InstanceMethodWithParams(System:Int32, System:Int32) -> System:Int32": {
                        "name": "InstanceMethodWithParams",
                        "declaring_type": "Namespace:Interface",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "System:Int32",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "param1",
                                "type": "System:Int32",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("System:Int32",),
                        "static": False,
                    },
                },
                "events": {},
                "nested_types": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_generic_methods_dunder(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={
                "Namespace:Interface.__add__(Namespace:Interface) -> Namespace:Interface": CMethod(
                    name="__add__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other", type=CType(name="Interface", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="Interface", namespace="Namespace"),),
                ),
                "Namespace:Interface.__and__(Namespace:Interface) -> Namespace:Interface": CMethod(
                    name="__and__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other", type=CType(name="Interface", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="Interface", namespace="Namespace"),),
                ),
                "Namespace:Interface.__ge__(Namespace:Interface) -> System:Boolean": CMethod(
                    name="__ge__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other", type=CType(name="Interface", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "Namespace:Interface.__gt__(Namespace:Interface) -> System:Boolean": CMethod(
                    name="__gt__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other", type=CType(name="Interface", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "Namespace:Interface.__invert__() -> Namespace:Interface": CMethod(
                    name="__invert__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(),
                    return_types=(CType(name="Interface", namespace="Namespace"),),
                ),
                "Namespace:Interface.__le__(Namespace:Interface) -> System:Boolean": CMethod(
                    name="__le__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other", type=CType(name="Interface", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "Namespace:Interface.__lt__(Namespace:Interface) -> System:Boolean": CMethod(
                    name="__lt__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other", type=CType(name="Interface", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "Namespace:Interface.__mod__(Namespace:Interface) -> Namespace:Interface": CMethod(
                    name="__mod__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other", type=CType(name="Interface", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="Interface", namespace="Namespace"),),
                ),
                "Namespace:Interface.__mul__(Namespace:Interface) -> Namespace:Interface": CMethod(
                    name="__mul__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other", type=CType(name="Interface", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="Interface", namespace="Namespace"),),
                ),
                "Namespace:Interface.__neg__() -> Namespace:Interface": CMethod(
                    name="__neg__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(),
                    return_types=(CType(name="Interface", namespace="Namespace"),),
                ),
                "Namespace:Interface.__or__(Namespace:Interface) -> Namespace:Interface": CMethod(
                    name="__or__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other", type=CType(name="Interface", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="Interface", namespace="Namespace"),),
                ),
                "Namespace:Interface.__pos__() -> Namespace:Interface": CMethod(
                    name="__pos__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(),
                    return_types=(CType(name="Interface", namespace="Namespace"),),
                ),
                "Namespace:Interface.__sub__(Namespace:Interface) -> Namespace:Interface": CMethod(
                    name="__sub__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other", type=CType(name="Interface", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="Interface", namespace="Namespace"),),
                ),
                "Namespace:Interface.__truediv__(Namespace:Interface) -> Namespace:Interface": CMethod(
                    name="__truediv__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other", type=CType(name="Interface", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="Interface", namespace="Namespace"),),
                ),
                "Namespace:Interface.__xor__(Namespace:Interface) -> Namespace:Interface": CMethod(
                    name="__xor__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other", type=CType(name="Interface", namespace="Namespace")
                        ),
                    ),
                    return_types=(CType(name="Interface", namespace="Namespace"),),
                ),
            },
            events={},
            nested_types={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "interface",
                "name": "Interface",
                "namespace": "Namespace",
                "nested": None,
                "generic_args": (),
                "interfaces": (),
                "fields": {},
                "properties": {},
                "methods": {
                    "Namespace:Interface.__add__(Namespace:Interface) -> Namespace:Interface": {
                        "name": "__add__",
                        "declaring_type": "Namespace:Interface",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Interface",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Interface",),
                        "static": False,
                    },
                    "Namespace:Interface.__and__(Namespace:Interface) -> Namespace:Interface": {
                        "name": "__and__",
                        "declaring_type": "Namespace:Interface",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Interface",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Interface",),
                        "static": False,
                    },
                    "Namespace:Interface.__ge__(Namespace:Interface) -> System:Boolean": {
                        "name": "__ge__",
                        "declaring_type": "Namespace:Interface",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Interface",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("System:Boolean",),
                        "static": False,
                    },
                    "Namespace:Interface.__gt__(Namespace:Interface) -> System:Boolean": {
                        "name": "__gt__",
                        "declaring_type": "Namespace:Interface",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Interface",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("System:Boolean",),
                        "static": False,
                    },
                    "Namespace:Interface.__invert__() -> Namespace:Interface": {
                        "name": "__invert__",
                        "declaring_type": "Namespace:Interface",
                        "parameters": (),
                        "return_types": ("Namespace:Interface",),
                        "static": False,
                    },
                    "Namespace:Interface.__le__(Namespace:Interface) -> System:Boolean": {
                        "name": "__le__",
                        "declaring_type": "Namespace:Interface",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Interface",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("System:Boolean",),
                        "static": False,
                    },
                    "Namespace:Interface.__lt__(Namespace:Interface) -> System:Boolean": {
                        "name": "__lt__",
                        "declaring_type": "Namespace:Interface",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Interface",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("System:Boolean",),
                        "static": False,
                    },
                    "Namespace:Interface.__mod__(Namespace:Interface) -> Namespace:Interface": {
                        "name": "__mod__",
                        "declaring_type": "Namespace:Interface",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Interface",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Interface",),
                        "static": False,
                    },
                    "Namespace:Interface.__mul__(Namespace:Interface) -> Namespace:Interface": {
                        "name": "__mul__",
                        "declaring_type": "Namespace:Interface",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Interface",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Interface",),
                        "static": False,
                    },
                    "Namespace:Interface.__neg__() -> Namespace:Interface": {
                        "name": "__neg__",
                        "declaring_type": "Namespace:Interface",
                        "parameters": (),
                        "return_types": ("Namespace:Interface",),
                        "static": False,
                    },
                    "Namespace:Interface.__or__(Namespace:Interface) -> Namespace:Interface": {
                        "name": "__or__",
                        "declaring_type": "Namespace:Interface",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Interface",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Interface",),
                        "static": False,
                    },
                    "Namespace:Interface.__pos__() -> Namespace:Interface": {
                        "name": "__pos__",
                        "declaring_type": "Namespace:Interface",
                        "parameters": (),
                        "return_types": ("Namespace:Interface",),
                        "static": False,
                    },
                    "Namespace:Interface.__sub__(Namespace:Interface) -> Namespace:Interface": {
                        "name": "__sub__",
                        "declaring_type": "Namespace:Interface",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Interface",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Interface",),
                        "static": False,
                    },
                    "Namespace:Interface.__truediv__(Namespace:Interface) -> Namespace:Interface": {
                        "name": "__truediv__",
                        "declaring_type": "Namespace:Interface",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Interface",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Interface",),
                        "static": False,
                    },
                    "Namespace:Interface.__xor__(Namespace:Interface) -> Namespace:Interface": {
                        "name": "__xor__",
                        "declaring_type": "Namespace:Interface",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace:Interface",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("Namespace:Interface",),
                        "static": False,
                    },
                },
                "events": {},
                "nested_types": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_generic_methods_collection(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={
                "Namespace:Interface.__contains__(System:Int32) -> bool": CMethod(
                    name="__contains__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(name="value", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="bool"),),
                ),
                "Namespace:Interface.__iter__() -> typing:Iterator[System:Int32]": CMethod(
                    name="__iter__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(),
                    return_types=(
                        CType(
                            name="Iterator",
                            namespace="typing",
                            inner=(CType(name="Int32", namespace="System"),),
                        ),
                    ),
                ),
                "Namespace:Interface.__iter__() -> typing:Iterator[object]": CMethod(
                    name="__iter__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(),
                    return_types=(
                        CType(name="Iterator", namespace="typing", inner=(CType(name="object"),)),
                    ),
                ),
                "Namespace:Interface.__len__() -> int": CMethod(
                    name="__len__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(),
                    return_types=(CType(name="int"),),
                ),
            },
            events={},
            nested_types={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "interface",
                "name": "Interface",
                "namespace": "Namespace",
                "nested": None,
                "generic_args": (),
                "interfaces": (),
                "fields": {},
                "properties": {},
                "methods": {
                    "Namespace:Interface.__contains__(System:Int32) -> bool": {
                        "name": "__contains__",
                        "declaring_type": "Namespace:Interface",
                        "parameters": (
                            {
                                "name": "value",
                                "type": "System:Int32",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "return_types": ("bool",),
                        "static": False,
                    },
                    "Namespace:Interface.__iter__() -> typing:Iterator[System:Int32]": {
                        "name": "__iter__",
                        "declaring_type": "Namespace:Interface",
                        "parameters": (),
                        "return_types": ("typing:Iterator[System:Int32]",),
                        "static": False,
                    },
                    "Namespace:Interface.__iter__() -> typing:Iterator[object]": {
                        "name": "__iter__",
                        "declaring_type": "Namespace:Interface",
                        "parameters": (),
                        "return_types": ("typing:Iterator[object]",),
                        "static": False,
                    },
                    "Namespace:Interface.__len__() -> int": {
                        "name": "__len__",
                        "declaring_type": "Namespace:Interface",
                        "parameters": (),
                        "return_types": ("int",),
                        "static": False,
                    },
                },
                "events": {},
                "nested_types": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_generic_events(self) -> None:
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
                "Namespace:Interface.Event -> (System:EventHandler)": CEvent(
                    name="Event",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="EventHandler", namespace="System"),
                ),
                "Namespace:Interface.EventWithArgs -> (System:EventHandler[System:EventArgs])": CEvent(
                    name="EventWithArgs",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(
                        name="EventHandler",
                        namespace="System",
                        inner=(CType(name="EventArgs", namespace="System"),),
                    ),
                ),
            },
            nested_types={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "interface",
                "name": "Interface",
                "namespace": "Namespace",
                "nested": None,
                "generic_args": (),
                "interfaces": (),
                "fields": {},
                "properties": {},
                "methods": {},
                "events": {
                    "Namespace:Interface.Event -> (System:EventHandler)": {
                        "name": "Event",
                        "declaring_type": "Namespace:Interface",
                        "type": "System:EventHandler",
                    },
                    "Namespace:Interface.EventWithArgs -> (System:EventHandler[System:EventArgs])": {
                        "name": "EventWithArgs",
                        "declaring_type": "Namespace:Interface",
                        "type": "System:EventHandler[System:EventArgs]",
                    },
                },
                "nested_types": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_generic_nested(self) -> None:
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
                "Namespace:Interface.NestedDelegate": CDelegate(
                    name="NestedDelegate",
                    namespace="Namespace",
                    nested=CType(name="Interface", namespace="Namespace"),
                    parameters=(),
                    return_type=CType(name="Void", namespace="System"),
                ),
                "Namespace:Interface.NestedEnum": CEnum(
                    name="NestedEnum",
                    namespace="Namespace",
                    nested=CType(name="Interface", namespace="Namespace"),
                    fields=(),
                ),
                "Namespace:Interface.NestedStruct": CStruct(
                    name="NestedStruct",
                    namespace="Namespace",
                    nested=CType(name="Interface", namespace="Namespace"),
                    abstract=False,
                    generic_args=(),
                    super_class=CType(name="ValueType", namespace="System"),
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
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "interface",
                "name": "Interface",
                "namespace": "Namespace",
                "nested": None,
                "generic_args": (),
                "interfaces": (),
                "fields": {},
                "properties": {},
                "methods": {},
                "events": {},
                "nested_types": {
                    "Namespace:Interface.INestedInterface": {
                        "type": "interface",
                        "name": "INestedInterface",
                        "namespace": "Namespace",
                        "nested": "Namespace:Interface",
                        "generic_args": (),
                        "interfaces": (),
                        "fields": {},
                        "properties": {},
                        "methods": {},
                        "events": {},
                        "nested_types": {},
                    },
                    "Namespace:Interface.NestedClass": {
                        "type": "class",
                        "name": "NestedClass",
                        "namespace": "Namespace",
                        "nested": "Namespace:Interface",
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
                    "Namespace:Interface.NestedDelegate": {
                        "type": "delegate",
                        "name": "NestedDelegate",
                        "namespace": "Namespace",
                        "nested": "Namespace:Interface",
                        "parameters": (),
                        "return_type": "System:Void",
                    },
                    "Namespace:Interface.NestedEnum": {
                        "type": "enum",
                        "name": "NestedEnum",
                        "namespace": "Namespace",
                        "nested": "Namespace:Interface",
                        "fields": (),
                    },
                    "Namespace:Interface.NestedStruct": {
                        "type": "struct",
                        "name": "NestedStruct",
                        "namespace": "Namespace",
                        "nested": "Namespace:Interface",
                        "abstract": False,
                        "generic_args": (),
                        "super_class": "System:ValueType",
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
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_doc_json(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={
                "Namespace:Interface.Field": CField(
                    name="Field",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    return_type=CType(name="Type", namespace="Namespace"),
                )
            },
            properties={
                "Namespace:Interface.Property": CProperty(
                    name="Property",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                ),
            },
            methods={
                "Namespace:Interface.Method": CMethod(
                    name="Method",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                    ),
                    return_types=(CType(name="Type", namespace="Namespace"),),
                ),
            },
            events={
                "Namespace:Interface.Event": CEvent(
                    name="Event",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="EventHandler", namespace="System"),
                ),
            },
            nested_types={
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
                "Namespace:Interface.NestedDelegate": CDelegate(
                    name="NestedDelegate",
                    namespace="Namespace",
                    nested=CType(name="Interface", namespace="Namespace"),
                    parameters=(),
                    return_type=CType(name="Void", namespace="System"),
                ),
                "Namespace:Interface.NestedEnum": CEnum(
                    name="NestedEnum",
                    namespace="Namespace",
                    nested=CType(name="Interface", namespace="Namespace"),
                    fields=(),
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
            },
        )
        name: str
        json: JsonType
        name, json = type_def.to_doc_json()

        self.assertIsNotNone(name)
        self.assertIsInstance(name, str)
        self.assertEqual("Interface", name)

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "doc": "",
                "doc_formatted": {},
                "Field": {"doc": "", "doc_formatted": {}, "return": ""},
                "Property": {"doc": "", "doc_formatted": {}, "return": ""},
                "Method(Namespace:Type)": {
                    "doc": "",
                    "doc_formatted": {},
                    "exceptions": {},
                    "parameters": {"param0": ""},
                    "return": "",
                },
                "Event": {"doc": "", "doc_formatted": {}},
                "INestedInterface": {"doc": "", "doc_formatted": {}},
                "NestedClass": {"doc": "", "doc_formatted": {}},
                "NestedDelegate()": {"doc": "", "doc_formatted": {}},
                "NestedEnum": {"doc": "", "doc_formatted": {}},
                "NestedStruct": {"doc": "", "doc_formatted": {}},
            },
            json,
        )

    def test_compare(self) -> None:
        interface0: CInterface = CInterface(
            name="InterfaceA",
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
        interface1: CInterface = CInterface(
            name="InterfaceB",
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

        self.assertLess(interface0, interface1)

        self.assertLessEqual(interface0, interface1)

        self.assertLessEqual(interface0, interface0)
        self.assertLessEqual(interface1, interface1)

        self.assertGreater(interface1, interface0)

        self.assertGreaterEqual(interface1, interface0)

        self.assertGreaterEqual(interface0, interface0)
        self.assertGreaterEqual(interface1, interface1)

    def test_sorted(self) -> None:
        ordered: Sequence[CInterface] = (
            CInterface(
                name="InterfaceA",
                namespace="Namespace",
                nested=None,
                generic_args=(),
                interfaces=(),
                fields={},
                properties={},
                methods={},
                events={},
                nested_types={},
            ),
            CInterface(
                name="InterfaceB",
                namespace="Namespace",
                nested=None,
                generic_args=(),
                interfaces=(),
                fields={},
                properties={},
                methods={},
                events={},
                nested_types={},
            ),
            CInterface(
                name="InterfaceC",
                namespace="Namespace",
                nested=None,
                generic_args=(),
                interfaces=(),
                fields={},
                properties={},
                methods={},
                events={},
                nested_types={},
            ),
            CInterface(
                name="InterfaceD",
                namespace="Namespace",
                nested=None,
                generic_args=(),
                interfaces=(),
                fields={},
                properties={},
                methods={},
                events={},
                nested_types={},
            ),
        )
        unordered: MutableSequence[CInterface] = list(ordered)
        random.shuffle(unordered)

        self.assertSequenceEqual(ordered, sorted(unordered))


class TestCEnum(TestBase):
    def test_json(self) -> None:
        enum: CEnum = CEnum(
            name="Enum",
            namespace="Namespace",
            nested=None,
            fields=(
                "Field0",
                "Field1",
                "Field2",
                "Field3",
            ),
        )
        json: JsonType = enum.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "enum",
                "name": "Enum",
                "namespace": "Namespace",
                "nested": None,
                "fields": (
                    "Field0",
                    "Field1",
                    "Field2",
                    "Field3",
                ),
            },
            json,
        )

        from_json: CEnum = CEnum.from_json(json)

        self.assertEqual(enum, from_json)

    def test_doc_json(self) -> None:
        type_def: CEnum = CEnum(
            name="Enum",
            namespace="Namespace",
            nested=None,
            fields=("Field0", "Field1", "Field2", "Field3"),
        )
        name: str
        json: JsonType
        name, json = type_def.to_doc_json()

        self.assertIsNotNone(name)
        self.assertIsInstance(name, str)
        self.assertEqual("Enum", name)

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "doc": "",
                "doc_formatted": {},
                "Field0": {"doc": ""},
                "Field1": {"doc": ""},
                "Field2": {"doc": ""},
                "Field3": {"doc": ""},
            },
            json,
        )

    def test_compare(self) -> None:
        enum0: CEnum = CEnum(
            name="EnumA",
            namespace="Namespace",
            nested=None,
            fields=("Field0", "Field1", "Field2", "Field3"),
        )
        enum1: CEnum = CEnum(
            name="EnumB",
            namespace="Namespace",
            nested=None,
            fields=("Field0", "Field1", "Field2", "Field3"),
        )

        self.assertLess(enum0, enum1)

        self.assertLessEqual(enum0, enum1)

        self.assertLessEqual(enum0, enum0)
        self.assertLessEqual(enum1, enum1)

        self.assertGreater(enum1, enum0)

        self.assertGreaterEqual(enum1, enum0)

        self.assertGreaterEqual(enum0, enum0)
        self.assertGreaterEqual(enum1, enum1)

    def test_sorted(self) -> None:
        ordered: Sequence[CEnum] = (
            CEnum(
                name="EnumA",
                namespace="Namespace",
                nested=None,
                fields=("Field0", "Field1", "Field2", "Field3"),
            ),
            CEnum(
                name="EnumB",
                namespace="Namespace",
                nested=None,
                fields=("Field0", "Field1", "Field2", "Field3"),
            ),
            CEnum(
                name="EnumC",
                namespace="Namespace",
                nested=None,
                fields=("Field0", "Field1", "Field2", "Field3"),
            ),
            CEnum(
                name="EnumD",
                namespace="Namespace",
                nested=None,
                fields=("Field0", "Field1", "Field2", "Field3"),
            ),
        )
        unordered: MutableSequence[CEnum] = list(ordered)
        random.shuffle(unordered)

        self.assertSequenceEqual(ordered, sorted(unordered))


class TestCDelegate(TestBase):
    def test_json(self) -> None:
        delegate: CDelegate = CDelegate(
            name="Delegate",
            namespace="Namespace",
            nested=None,
            parameters=(
                CParameter(name="param0", type=CType(name="Type0", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Type1", namespace="Namespace")),
            ),
            return_type=CType(name="Type", namespace="Namespace"),
        )
        json: JsonType = delegate.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "delegate",
                "name": "Delegate",
                "namespace": "Namespace",
                "nested": None,
                "parameters": (
                    {
                        "name": "param0",
                        "type": "Namespace:Type0",
                        "default": False,
                        "out": False,
                    },
                    {
                        "name": "param1",
                        "type": "Namespace:Type1",
                        "default": False,
                        "out": False,
                    },
                ),
                "return_type": "Namespace:Type",
            },
            json,
        )

        from_json: CDelegate = CDelegate.from_json(json)

        self.assertEqual(delegate, from_json)

    def test_doc_json(self) -> None:
        type_def: CDelegate = CDelegate(
            name="Delegate",
            namespace="Namespace",
            nested=None,
            parameters=(
                CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
            ),
            return_type=CType(name="Type", namespace="Namespace"),
        )
        name: str
        json: JsonType
        name, json = type_def.to_doc_json()

        self.assertIsNotNone(name)
        self.assertIsInstance(name, str)
        self.assertEqual("Delegate(Namespace:Type, Namespace:Type)", name)

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "doc": "",
                "doc_formatted": {},
                "parameters": {
                    "param0": "",
                    "param1": "",
                },
                "return": "",
            },
            json,
        )

    def test_doc_json_no_parameters(self) -> None:
        type_def: CDelegate = CDelegate(
            name="Delegate",
            namespace="Namespace",
            nested=None,
            parameters=(),
            return_type=CType(name="Type", namespace="Namespace"),
        )
        name: str
        json: JsonType
        name, json = type_def.to_doc_json()

        self.assertIsNotNone(name)
        self.assertIsInstance(name, str)
        self.assertEqual("Delegate()", name)

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "doc": "",
                "doc_formatted": {},
                "return": "",
            },
            json,
        )

    def test_doc_json_no_return(self) -> None:
        type_def: CDelegate = CDelegate(
            name="Delegate",
            namespace="Namespace",
            nested=None,
            parameters=(
                CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
            ),
            return_type=CType(name="Void", namespace="System"),
        )
        name: str
        json: JsonType
        name, json = type_def.to_doc_json()

        self.assertIsNotNone(name)
        self.assertIsInstance(name, str)
        self.assertEqual("Delegate(Namespace:Type, Namespace:Type)", name)

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "doc": "",
                "doc_formatted": {},
                "parameters": {
                    "param0": "",
                    "param1": "",
                },
            },
            json,
        )

    def test_compare_namespace(self) -> None:
        delegate0: CDelegate = CDelegate(
            name="DelegateA",
            namespace="Namespace",
            nested=None,
            parameters=(),
            return_type=CType(name="Type", namespace="Namespace"),
        )
        delegate1: CDelegate = CDelegate(
            name="DelegateB",
            namespace="Namespace",
            nested=None,
            parameters=(),
            return_type=CType(name="Type", namespace="Namespace"),
        )

        self.assertLess(delegate0, delegate1)

        self.assertLessEqual(delegate0, delegate1)

        self.assertLessEqual(delegate0, delegate0)
        self.assertLessEqual(delegate1, delegate1)

        self.assertGreater(delegate1, delegate0)

        self.assertGreaterEqual(delegate1, delegate0)

        self.assertGreaterEqual(delegate0, delegate0)
        self.assertGreaterEqual(delegate1, delegate1)

    def test_sorted(self) -> None:
        ordered: Sequence[CDelegate] = (
            CDelegate(
                name="DelegateA",
                namespace="Namespace",
                nested=None,
                parameters=(),
                return_type=CType(name="Type", namespace="Namespace"),
            ),
            CDelegate(
                name="DelegateB",
                namespace="Namespace",
                nested=None,
                parameters=(),
                return_type=CType(name="Type", namespace="Namespace"),
            ),
            CDelegate(
                name="DelegateC",
                namespace="Namespace",
                nested=None,
                parameters=(),
                return_type=CType(name="Type", namespace="Namespace"),
            ),
            CDelegate(
                name="DelegateD",
                namespace="Namespace",
                nested=None,
                parameters=(),
                return_type=CType(name="Type", namespace="Namespace"),
            ),
        )
        unordered: MutableSequence[CDelegate] = list(ordered)
        random.shuffle(unordered)

        self.assertSequenceEqual(ordered, sorted(unordered))


class TestCType(TestBase):
    def test_json_no_namespace(self) -> None:
        c_type: CType = CType(name="Type")
        json: JsonType = c_type.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, str)
        self.assertEqual("Type", json)

        from_json: CType = CType.from_json(json)

        self.assertEqual(c_type, from_json)

    def test_json_simple(self) -> None:
        c_type: CType = CType(name="Type", namespace="Namespace")
        json: JsonType = c_type.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, str)
        self.assertEqual("Namespace:Type", json)

        from_json: CType = CType.from_json(json)

        self.assertEqual(c_type, from_json)

    def test_json_nested(self) -> None:
        c_type: CType = CType(name="Type.Nested", namespace="Namespace")
        json: JsonType = c_type.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, str)
        self.assertEqual("Namespace:Type.Nested", json)

        from_json: CType = CType.from_json(json)

        self.assertEqual(c_type, from_json)

    def test_json_reference(self) -> None:
        c_type: CType = CType(name="Type", namespace="Namespace", reference=True)
        json: JsonType = c_type.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, str)
        self.assertEqual("Namespace:*Type", json)

        from_json: CType = CType.from_json(json)

        self.assertEqual(c_type, from_json)

    def test_json_generic(self) -> None:
        c_type: CType = CType(name="Type", generic=True)
        json: JsonType = c_type.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, str)
        self.assertEqual("$Type", json)

        from_json: CType = CType.from_json(json)

        self.assertEqual(c_type, from_json)

    def test_json_nullable(self) -> None:
        c_type: CType = CType(name="Type", namespace="Namespace", nullable=True)
        json: JsonType = c_type.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, str)
        self.assertEqual("Namespace:Type?", json)

        from_json: CType = CType.from_json(json)

        self.assertEqual(c_type, from_json)

    def test_json_reference_generic(self) -> None:
        c_type: CType = CType(name="Type", reference=True, generic=True)
        json: JsonType = c_type.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, str)
        self.assertEqual("$*Type", json)

        from_json: CType = CType.from_json(json)

        self.assertEqual(c_type, from_json)

    def test_json_reference_nullable(self) -> None:
        c_type: CType = CType(name="Type", namespace="Namespace", reference=True, nullable=True)
        json: JsonType = c_type.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, str)
        self.assertEqual("Namespace:*Type?", json)

        from_json: CType = CType.from_json(json)

        self.assertEqual(c_type, from_json)

    def test_json_generic_nullable(self) -> None:
        c_type: CType = CType(name="Type", generic=True, nullable=True)
        json: JsonType = c_type.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, str)
        self.assertEqual("$Type?", json)

        from_json: CType = CType.from_json(json)

        self.assertEqual(c_type, from_json)

    def test_json_reference_generic_nullable(self) -> None:
        c_type: CType = CType(name="Type", reference=True, generic=True, nullable=True)
        json: JsonType = c_type.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, str)
        self.assertEqual("$*Type?", json)

        from_json: CType = CType.from_json(json)

        self.assertEqual(c_type, from_json)

    def test_json_inner(self) -> None:
        c_type: CType = CType(
            name="Type",
            namespace="Namespace",
            inner=(
                CType(name="InnerA", namespace="Namespace"),
                CType(name="InnerB", namespace="Namespace"),
            ),
        )
        json: JsonType = c_type.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, str)
        self.assertEqual("Namespace:Type[Namespace:InnerA, Namespace:InnerB]", json)

        from_json: CType = CType.from_json(json)

        self.assertEqual(c_type, from_json)

    def test_compare_name(self) -> None:
        type0: CType = CType(name="A")
        type1: CType = CType(name="B")

        self.assertLess(type0, type1)

        self.assertLessEqual(type0, type1)

        self.assertLessEqual(type0, type0)
        self.assertLessEqual(type1, type1)

        self.assertGreater(type1, type0)

        self.assertGreaterEqual(type1, type0)

        self.assertGreaterEqual(type0, type0)
        self.assertGreaterEqual(type1, type1)

    def test_compare_namespace(self) -> None:
        type0: CType = CType(name="Type", namespace="NamespaceA")
        type1: CType = CType(name="Type", namespace="NamespaceB")

        self.assertLess(type0, type1)

        self.assertLessEqual(type0, type1)

        self.assertLessEqual(type0, type0)
        self.assertLessEqual(type1, type1)

        self.assertGreater(type1, type0)

        self.assertGreaterEqual(type1, type0)

        self.assertGreaterEqual(type0, type0)
        self.assertGreaterEqual(type1, type1)

    def test_compare_namespace_none(self) -> None:
        type0: CType = CType(name="Type")
        type1: CType = CType(name="Type", namespace="NamespaceA")

        self.assertLess(type0, type1)

        self.assertLessEqual(type0, type1)

        self.assertLessEqual(type0, type0)
        self.assertLessEqual(type1, type1)

        self.assertGreater(type1, type0)

        self.assertGreaterEqual(type1, type0)

        self.assertGreaterEqual(type0, type0)
        self.assertGreaterEqual(type1, type1)

    def test_compare_inner_len(self) -> None:
        type0: CType = CType(name="Type", inner=())
        type1: CType = CType(name="Type", inner=(CType(name="T"),))

        self.assertLess(type0, type1)

        self.assertLessEqual(type0, type1)

        self.assertLessEqual(type0, type0)
        self.assertLessEqual(type1, type1)

        self.assertGreater(type1, type0)

        self.assertGreaterEqual(type1, type0)

        self.assertGreaterEqual(type0, type0)
        self.assertGreaterEqual(type1, type1)

    def test_compare_inner(self) -> None:
        type0: CType = CType(name="Type", inner=(CType(name="A"),))
        type1: CType = CType(name="Type", inner=(CType(name="B"),))

        self.assertLess(type0, type1)

        self.assertLessEqual(type0, type1)

        self.assertLessEqual(type0, type0)
        self.assertLessEqual(type1, type1)

        self.assertGreater(type1, type0)

        self.assertGreaterEqual(type1, type0)

        self.assertGreaterEqual(type0, type0)
        self.assertGreaterEqual(type1, type1)

    def test_compare_reference(self) -> None:
        type0: CType = CType(name="Type", reference=False)
        type1: CType = CType(name="Type", reference=True)

        self.assertLess(type0, type1)

        self.assertLessEqual(type0, type1)

        self.assertLessEqual(type0, type0)
        self.assertLessEqual(type1, type1)

        self.assertGreater(type1, type0)

        self.assertGreaterEqual(type1, type0)

        self.assertGreaterEqual(type0, type0)
        self.assertGreaterEqual(type1, type1)

    def test_compare_generic(self) -> None:
        type0: CType = CType(name="Type", generic=False)
        type1: CType = CType(name="Type", generic=True)

        self.assertLess(type0, type1)

        self.assertLessEqual(type0, type1)

        self.assertLessEqual(type0, type0)
        self.assertLessEqual(type1, type1)

        self.assertGreater(type1, type0)

        self.assertGreaterEqual(type1, type0)

        self.assertGreaterEqual(type0, type0)
        self.assertGreaterEqual(type1, type1)

    def test_compare_nullable(self) -> None:
        type0: CType = CType(name="Type", nullable=False)
        type1: CType = CType(name="Type", nullable=True)

        self.assertLess(type0, type1)

        self.assertLessEqual(type0, type1)

        self.assertLessEqual(type0, type0)
        self.assertLessEqual(type1, type1)

        self.assertGreater(type1, type0)

        self.assertGreaterEqual(type1, type0)

        self.assertGreaterEqual(type0, type0)
        self.assertGreaterEqual(type1, type1)

    def test_sorted(self) -> None:
        ordered: Sequence[CType] = (
            CType(name="TypeA", namespace="NamespaceA"),
            CType(name="TypeA", namespace="NamespaceB"),
            CType(name="TypeB", namespace="NamespaceB"),
            CType(name="TypeB", namespace="NamespaceB", inner=(CType(name="T"),)),
            CType(name="TypeB", namespace="NamespaceB", inner=(CType(name="T"),), reference=True),
            CType(
                name="TypeB",
                namespace="NamespaceB",
                inner=(CType(name="T"),),
                reference=True,
                generic=True,
            ),
            CType(
                name="TypeB",
                namespace="NamespaceB",
                inner=(CType(name="T"),),
                reference=True,
                generic=True,
                nullable=True,
            ),
        )
        unordered: MutableSequence[CType] = list(ordered)
        random.shuffle(unordered)

        self.assertSequenceEqual(ordered, sorted(unordered))


class TestCParameter(TestBase):
    def test_json(self) -> None:
        parameter: CParameter = CParameter(
            name="Parameter",
            type=CType(name="Type", namespace="Namespace"),
            default=False,
            out=False,
        )
        json: JsonType = parameter.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "name": "Parameter",
                "type": "Namespace:Type",
                "default": False,
                "out": False,
            },
            json,
        )

        from_json: CParameter = CParameter.from_json(json)

        self.assertEqual(parameter, from_json)

    def test_json_default(self) -> None:
        parameter: CParameter = CParameter(
            name="Parameter",
            type=CType(name="Type", namespace="Namespace"),
            default=True,
            out=False,
        )
        json: JsonType = parameter.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "name": "Parameter",
                "type": "Namespace:Type",
                "default": True,
                "out": False,
            },
            json,
        )

        from_json: CParameter = CParameter.from_json(json)

        self.assertEqual(parameter, from_json)

    def test_json_out(self) -> None:
        parameter: CParameter = CParameter(
            name="Parameter",
            type=CType(name="Type", namespace="Namespace"),
            default=False,
            out=True,
        )
        json: JsonType = parameter.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "name": "Parameter",
                "type": "Namespace:Type",
                "default": False,
                "out": True,
            },
            json,
        )

        from_json: CParameter = CParameter.from_json(json)

        self.assertEqual(parameter, from_json)

    def test_json_default_out(self) -> None:
        parameter: CParameter = CParameter(
            name="Parameter",
            type=CType(name="Type", namespace="Namespace"),
            default=True,
            out=True,
        )
        json: JsonType = parameter.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "name": "Parameter",
                "type": "Namespace:Type",
                "default": True,
                "out": True,
            },
            json,
        )

        from_json: CParameter = CParameter.from_json(json)

        self.assertEqual(parameter, from_json)

    def test_compare(self) -> None:
        message: CParameter = CParameter(
            name="message",
            type=CType("String", "System"),
            default=False,
            out=False,
        )
        param_name: CParameter = CParameter(
            name="paramName",
            type=CType("String", "System"),
            default=False,
            out=False,
        )
        inner_exception: CParameter = CParameter(
            name="innerException",
            type=CType("Exception", "System"),
            default=False,
            out=False,
        )

        params0: Sequence[CParameter] = []
        params1: Sequence[CParameter] = [message]
        params2: Sequence[CParameter] = [message, inner_exception]
        params3: Sequence[CParameter] = [message, param_name]
        params4: Sequence[CParameter] = [message, param_name, inner_exception]

        self.assertEqual(CParameter.compare(params0, params1), -1)
        self.assertEqual(CParameter.compare(params1, params2), -1)
        self.assertEqual(CParameter.compare(params2, params3), -1)
        self.assertEqual(CParameter.compare(params3, params4), -1)

        self.assertEqual(CParameter.compare(params0, params0), +0)
        self.assertEqual(CParameter.compare(params1, params1), +0)
        self.assertEqual(CParameter.compare(params2, params2), +0)
        self.assertEqual(CParameter.compare(params3, params3), +0)
        self.assertEqual(CParameter.compare(params4, params4), +0)

        self.assertEqual(CParameter.compare(params1, params0), +1)
        self.assertEqual(CParameter.compare(params2, params1), +1)
        self.assertEqual(CParameter.compare(params3, params2), +1)
        self.assertEqual(CParameter.compare(params4, params3), +1)


class TestCField(TestBase):
    def test_json(self) -> None:
        c_field: CField = CField(
            name="Field",
            declaring_type=CType(name="Type", namespace="Namespace"),
            return_type=CType(name="Type", namespace="Namespace"),
        )
        json: JsonType = c_field.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "name": "Field",
                "declaring_type": "Namespace:Type",
                "return_type": "Namespace:Type",
                "static": False,
            },
            json,
        )

        from_json: CField = CField.from_json(json)

        self.assertEqual(c_field, from_json)

    def test_json_static(self) -> None:
        c_field: CField = CField(
            name="Field",
            declaring_type=CType(name="Type", namespace="Namespace"),
            return_type=CType(name="Type", namespace="Namespace"),
            static=True,
        )
        json: JsonType = c_field.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "name": "Field",
                "declaring_type": "Namespace:Type",
                "return_type": "Namespace:Type",
                "static": True,
            },
            json,
        )

        from_json: CField = CField.from_json(json)

        self.assertEqual(c_field, from_json)

    def test_doc_json(self) -> None:
        type_def: CField = CField(
            name="Field",
            declaring_type=CType(name="Type", namespace="Namespace"),
            return_type=CType(name="Type", namespace="Namespace"),
        )
        name: str
        json: JsonType
        name, json = type_def.to_doc_json()

        self.assertIsNotNone(name)
        self.assertIsInstance(name, str)
        self.assertEqual("Field", name)

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {"doc": "", "doc_formatted": {}, "return": ""},
            json,
        )

    def test_doc_json_no_return(self) -> None:
        type_def: CField = CField(
            name="Field",
            declaring_type=CType(name="Type", namespace="Namespace"),
            return_type=CType(name="Void", namespace="System"),
        )
        name: str
        json: JsonType
        name, json = type_def.to_doc_json()

        self.assertIsNotNone(name)
        self.assertIsInstance(name, str)
        self.assertEqual("Field", name)

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {"doc": "", "doc_formatted": {}},
            json,
        )

    def test_compare(self) -> None:
        field0: CField = CField(
            name="FieldA",
            declaring_type=CType(name="Type", namespace="Namespace"),
            return_type=CType(name="Type", namespace="Namespace"),
        )
        field1: CField = CField(
            name="FieldB",
            declaring_type=CType(name="Type", namespace="Namespace"),
            return_type=CType(name="Type", namespace="Namespace"),
        )

        self.assertLess(field0, field1)

        self.assertLessEqual(field0, field1)

        self.assertLessEqual(field0, field0)
        self.assertLessEqual(field1, field1)

        self.assertGreater(field1, field0)

        self.assertGreaterEqual(field1, field0)

        self.assertGreaterEqual(field0, field0)
        self.assertGreaterEqual(field1, field1)

    def test_sorted(self) -> None:
        declaring_type: CType = CType(name="Type", namespace="Namespace")
        return_type: CType = CType(name="Type", namespace="Namespace")
        ordered: Sequence[CField] = (
            CField(name="FieldA", declaring_type=declaring_type, return_type=return_type),
            CField(name="FieldB", declaring_type=declaring_type, return_type=return_type),
            CField(name="FieldC", declaring_type=declaring_type, return_type=return_type),
            CField(name="FieldD", declaring_type=declaring_type, return_type=return_type),
        )
        unordered: MutableSequence[CField] = list(ordered)
        random.shuffle(unordered)

        self.assertSequenceEqual(ordered, sorted(unordered))


class TestCConstructor(TestBase):
    def test_json(self) -> None:
        c_constructor: CConstructor = CConstructor(
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
        )
        json: JsonType = c_constructor.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "declaring_type": "Namespace:Type",
                "parameters": (),
            },
            json,
        )

        from_json: CConstructor = CConstructor.from_json(json)

        self.assertEqual(c_constructor, from_json)

    def test_json_params(self) -> None:
        c_constructor: CConstructor = CConstructor(
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
            ),
        )
        json: JsonType = c_constructor.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "declaring_type": "Namespace:Type",
                "parameters": (
                    {
                        "name": "param0",
                        "type": "Namespace:Type",
                        "default": False,
                        "out": False,
                    },
                    {
                        "name": "param1",
                        "type": "Namespace:Type",
                        "default": False,
                        "out": False,
                    },
                ),
            },
            json,
        )

        from_json: CConstructor = CConstructor.from_json(json)

        self.assertEqual(c_constructor, from_json)

    def test_doc_json(self) -> None:
        type_def: CConstructor = CConstructor(
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
            ),
        )
        name: str
        json: JsonType
        name, json = type_def.to_doc_json()

        self.assertIsNotNone(name)
        self.assertIsInstance(name, str)
        self.assertEqual("__init__(Namespace:Type, Namespace:Type)", name)

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {"doc": "", "doc_formatted": {}, "parameters": {"param0": "", "param1": ""}},
            json,
        )

    def test_doc_json_no_parameters(self) -> None:
        type_def: CConstructor = CConstructor(
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
        )
        name: str
        json: JsonType
        name, json = type_def.to_doc_json()

        self.assertIsNotNone(name)
        self.assertIsInstance(name, str)
        self.assertEqual("__init__()", name)

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {"doc": "", "doc_formatted": {}},
            json,
        )

    def test_compare(self) -> None:
        ctor0: CConstructor = CConstructor(
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
        )
        ctor1: CConstructor = CConstructor(
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),),
        )

        self.assertLess(ctor0, ctor1)

        self.assertLessEqual(ctor0, ctor1)

        self.assertLessEqual(ctor0, ctor0)
        self.assertLessEqual(ctor1, ctor1)

        self.assertGreater(ctor1, ctor0)

        self.assertGreaterEqual(ctor1, ctor0)

        self.assertGreaterEqual(ctor0, ctor0)
        self.assertGreaterEqual(ctor1, ctor1)

    def test_sorted(self) -> None:
        ordered: Sequence[CConstructor] = (
            CConstructor(
                declaring_type=CType(name="Type", namespace="Namespace"),
                parameters=(),
            ),
            CConstructor(
                declaring_type=CType(name="Type", namespace="Namespace"),
                parameters=(
                    CParameter(name="param0", type=CType(name="TypeA", namespace="Namespace")),
                ),
            ),
            CConstructor(
                declaring_type=CType(name="Type", namespace="Namespace"),
                parameters=(
                    CParameter(name="param0", type=CType(name="TypeB", namespace="Namespace")),
                ),
            ),
            CConstructor(
                declaring_type=CType(name="Type", namespace="Namespace"),
                parameters=(
                    CParameter(name="param0", type=CType(name="TypeA", namespace="Namespace")),
                    CParameter(name="param1", type=CType(name="TypeB", namespace="Namespace")),
                ),
            ),
        )
        unordered: MutableSequence[CConstructor] = list(ordered)
        random.shuffle(unordered)

        self.assertSequenceEqual(ordered, sorted(unordered))


class TestCProperty(TestBase):
    def test_json(self) -> None:
        c_property: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="Type", namespace="Namespace"),
        )
        json: JsonType = c_property.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "name": "Property",
                "declaring_type": "Namespace:Type",
                "type": "Namespace:Type",
                "setter": False,
                "static": False,
            },
            json,
        )

        from_json: CProperty = CProperty.from_json(json)

        self.assertEqual(c_property, from_json)

    def test_json_setter(self) -> None:
        c_property: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="Type", namespace="Namespace"),
            setter=True,
        )
        json: JsonType = c_property.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "name": "Property",
                "declaring_type": "Namespace:Type",
                "type": "Namespace:Type",
                "setter": True,
                "static": False,
            },
            json,
        )

        from_json: CProperty = CProperty.from_json(json)

        self.assertEqual(c_property, from_json)

    def test_json_static(self) -> None:
        c_property: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="Type", namespace="Namespace"),
            static=True,
        )
        json: JsonType = c_property.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "name": "Property",
                "declaring_type": "Namespace:Type",
                "type": "Namespace:Type",
                "setter": False,
                "static": True,
            },
            json,
        )

        from_json: CProperty = CProperty.from_json(json)

        self.assertEqual(c_property, from_json)

    def test_json_setter_static(self) -> None:
        c_property: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="Type", namespace="Namespace"),
            setter=True,
            static=True,
        )
        json: JsonType = c_property.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "name": "Property",
                "declaring_type": "Namespace:Type",
                "type": "Namespace:Type",
                "setter": True,
                "static": True,
            },
            json,
        )

        from_json: CProperty = CProperty.from_json(json)

        self.assertEqual(c_property, from_json)

    def test_doc_json(self) -> None:
        type_def: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="Type", namespace="Namespace"),
        )
        name: str
        json: JsonType
        name, json = type_def.to_doc_json()

        self.assertIsNotNone(name)
        self.assertIsInstance(name, str)
        self.assertEqual("Property", name)

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {"doc": "", "doc_formatted": {}, "return": ""},
            json,
        )

    def test_doc_json_no_return(self) -> None:
        type_def: CProperty = CProperty(
            name="Property",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="Void", namespace="System"),
        )
        name: str
        json: JsonType
        name, json = type_def.to_doc_json()

        self.assertIsNotNone(name)
        self.assertIsInstance(name, str)
        self.assertEqual("Property", name)

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {"doc": "", "doc_formatted": {}},
            json,
        )

    def test_compare(self) -> None:
        prop0: CProperty = CProperty(
            name="PropertyA",
            declaring_type=CType(name="Type"),
            type=CType(name="Type"),
            setter=True,
        )
        prop1: CProperty = CProperty(
            name="PropertyB",
            declaring_type=CType(name="Type"),
            type=CType(name="Type"),
            setter=True,
        )

        self.assertLess(prop0, prop1)

        self.assertLessEqual(prop0, prop1)

        self.assertLessEqual(prop0, prop0)
        self.assertLessEqual(prop1, prop1)

        self.assertGreater(prop1, prop0)

        self.assertGreaterEqual(prop1, prop0)

        self.assertGreaterEqual(prop0, prop0)
        self.assertGreaterEqual(prop1, prop1)

    def test_sorted(self) -> None:
        ordered: Sequence[CProperty] = (
            CProperty(
                name="PropertyA",
                declaring_type=CType(name="Type"),
                type=CType(name="Type"),
            ),
            CProperty(
                name="PropertyB",
                declaring_type=CType(name="Type"),
                type=CType(name="Type"),
            ),
            CProperty(
                name="PropertyC",
                declaring_type=CType(name="Type"),
                type=CType(name="Type"),
            ),
            CProperty(
                name="PropertyD",
                declaring_type=CType(name="Type"),
                type=CType(name="Type"),
            ),
            CProperty(
                name="PropertyE",
                declaring_type=CType(name="Type"),
                type=CType(name="Type"),
            ),
        )
        unordered: MutableSequence[CProperty] = list(ordered)
        random.shuffle(unordered)

        self.assertSequenceEqual(ordered, sorted(unordered))


class TestCMethod(TestBase):
    def test_json(self) -> None:
        c_method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),),
            return_types=(CType(name="Type", namespace="Namespace"),),
        )
        json: JsonType = c_method.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "name": "Method",
                "declaring_type": "Namespace:Type",
                "parameters": (
                    {
                        "name": "param0",
                        "type": "Namespace:Type",
                        "default": False,
                        "out": False,
                    },
                ),
                "return_types": ("Namespace:Type",),
                "static": False,
            },
            json,
        )

        from_json: CMethod = CMethod.from_json(json)

        self.assertEqual(c_method, from_json)

    def test_json_no_return(self) -> None:
        c_method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),),
            return_types=(),
        )
        json: JsonType = c_method.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "name": "Method",
                "declaring_type": "Namespace:Type",
                "parameters": (
                    {
                        "name": "param0",
                        "type": "Namespace:Type",
                        "default": False,
                        "out": False,
                    },
                ),
                "return_types": (),
                "static": False,
            },
            json,
        )

        from_json: CMethod = CMethod.from_json(json)

        self.assertEqual(c_method, from_json)

    def test_json_static(self) -> None:
        c_method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),),
            return_types=(CType(name="Type", namespace="Namespace"),),
            static=True,
        )
        json: JsonType = c_method.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "name": "Method",
                "declaring_type": "Namespace:Type",
                "parameters": (
                    {
                        "name": "param0",
                        "type": "Namespace:Type",
                        "default": False,
                        "out": False,
                    },
                ),
                "return_types": ("Namespace:Type",),
                "static": True,
            },
            json,
        )

        from_json: CMethod = CMethod.from_json(json)

        self.assertEqual(c_method, from_json)

    def test_doc_json(self) -> None:
        type_def: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
            ),
            return_types=(CType(name="Type", namespace="Namespace"),),
        )
        name: str
        json: JsonType
        name, json = type_def.to_doc_json()

        self.assertIsNotNone(name)
        self.assertIsInstance(name, str)
        self.assertEqual("Method(Namespace:Type, Namespace:Type)", name)

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "doc": "",
                "doc_formatted": {},
                "parameters": {"param0": "", "param1": ""},
                "return": "",
                "exceptions": {},
            },
            json,
        )

    def test_doc_json_no_parameters(self) -> None:
        type_def: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(CType(name="Type", namespace="Namespace"),),
        )
        name: str
        json: JsonType
        name, json = type_def.to_doc_json()

        self.assertIsNotNone(name)
        self.assertIsInstance(name, str)
        self.assertEqual("Method()", name)

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "doc": "",
                "doc_formatted": {},
                "exceptions": {},
                "return": "",
            },
            json,
        )

    def test_doc_json_no_return(self) -> None:
        type_def: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
            ),
            return_types=(CType(name="Void", namespace="System"),),
        )
        name: str
        json: JsonType
        name, json = type_def.to_doc_json()

        self.assertIsNotNone(name)
        self.assertIsInstance(name, str)
        self.assertEqual("Method(Namespace:Type, Namespace:Type)", name)

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "doc": "",
                "doc_formatted": {},
                "exceptions": {},
                "parameters": {"param0": "", "param1": ""},
            },
            json,
        )

    def test_compare_name(self) -> None:
        method0: CMethod = CMethod(
            name="MethodA",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(),
        )
        method1: CMethod = CMethod(
            name="MethodB",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            return_types=(),
        )

        self.assertLess(method0, method1)

        self.assertLessEqual(method0, method1)

        self.assertLessEqual(method0, method0)
        self.assertLessEqual(method1, method1)

        self.assertGreater(method1, method0)

        self.assertGreaterEqual(method1, method0)

        self.assertGreaterEqual(method0, method0)
        self.assertGreaterEqual(method1, method1)

    def test_compare_parameter_type(self) -> None:
        method0: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="TypeA", namespace="Namespace")),
            ),
            return_types=(),
        )
        method1: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="TypeB", namespace="Namespace")),
            ),
            return_types=(),
        )

        self.assertLess(method0, method1)

        self.assertLessEqual(method0, method1)

        self.assertLessEqual(method0, method0)
        self.assertLessEqual(method1, method1)

        self.assertGreater(method1, method0)

        self.assertGreaterEqual(method1, method0)

        self.assertGreaterEqual(method0, method0)
        self.assertGreaterEqual(method1, method1)

    def test_compare_parameter_count(self) -> None:
        method0: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),),
            return_types=(),
        )
        method1: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(
                CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
            ),
            return_types=(),
        )

        self.assertLess(method0, method1)

        self.assertLessEqual(method0, method1)

        self.assertLessEqual(method0, method0)
        self.assertLessEqual(method1, method1)

        self.assertGreater(method1, method0)

        self.assertGreaterEqual(method1, method0)

        self.assertGreaterEqual(method0, method0)
        self.assertGreaterEqual(method1, method1)

    def test_sorted(self) -> None:
        ordered: Sequence[CMethod] = (
            CMethod(
                name="MethodA",
                declaring_type=CType(name="Type", namespace="Namespace"),
                parameters=(),
                return_types=(),
            ),
            CMethod(
                name="MethodB",
                declaring_type=CType(name="Type", namespace="Namespace"),
                parameters=(),
                return_types=(),
            ),
            CMethod(
                name="MethodB",
                declaring_type=CType(name="Type", namespace="Namespace"),
                parameters=(
                    CParameter(name="param0", type=CType(name="TypeA", namespace="Namespace")),
                ),
                return_types=(),
            ),
            CMethod(
                name="MethodB",
                declaring_type=CType(name="Type", namespace="Namespace"),
                parameters=(
                    CParameter(name="param0", type=CType(name="TypeB", namespace="Namespace")),
                ),
                return_types=(),
            ),
            CMethod(
                name="MethodB",
                declaring_type=CType(name="Type", namespace="Namespace"),
                parameters=(
                    CParameter(name="param0", type=CType(name="TypeB", namespace="Namespace")),
                    CParameter(name="param0", type=CType(name="TypeB", namespace="Namespace")),
                ),
                return_types=(),
            ),
        )
        unordered: MutableSequence[CMethod] = list(ordered)
        random.shuffle(unordered)

        self.assertSequenceEqual(ordered, sorted(unordered))


class TestCEvent(TestBase):
    def test_json(self) -> None:
        c_event: CEvent = CEvent(
            name="Event",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="Type", namespace="Namespace"),
        )
        json: JsonType = c_event.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "name": "Event",
                "declaring_type": "Namespace:Type",
                "type": "Namespace:Type",
            },
            json,
        )

        from_json: CEvent = CEvent.from_json(json)

        self.assertEqual(c_event, from_json)

    def test_doc_json(self) -> None:
        type_def: CEvent = CEvent(
            name="Event",
            declaring_type=CType(name="Type", namespace="Namespace"),
            type=CType(name="Type", namespace="Namespace"),
        )
        name: str
        json: JsonType
        name, json = type_def.to_doc_json()

        self.assertIsNotNone(name)
        self.assertIsInstance(name, str)
        self.assertEqual("Event", name)

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {"doc": "", "doc_formatted": {}},
            json,
        )

    def test_compare(self) -> None:
        event0: CEvent = CEvent(
            name="EventA",
            declaring_type=CType(name="Type"),
            type=CType(name="Type"),
        )
        event1: CEvent = CEvent(
            name="EventB",
            declaring_type=CType(name="Type"),
            type=CType(name="Type"),
        )

        self.assertLess(event0, event1)

        self.assertLessEqual(event0, event1)

        self.assertLessEqual(event0, event0)
        self.assertLessEqual(event1, event1)

        self.assertGreater(event1, event0)

        self.assertGreaterEqual(event1, event0)

        self.assertGreaterEqual(event0, event0)
        self.assertGreaterEqual(event1, event1)

    def test_sorted(self) -> None:
        ordered: Sequence[CEvent] = (
            CEvent(
                name="EventA",
                declaring_type=CType(name="Type"),
                type=CType(name="Type"),
            ),
            CEvent(
                name="EventB",
                declaring_type=CType(name="Type"),
                type=CType(name="Type"),
            ),
            CEvent(
                name="EventC",
                declaring_type=CType(name="Type"),
                type=CType(name="Type"),
            ),
        )
        unordered: MutableSequence[CEvent] = list(ordered)
        random.shuffle(unordered)

        self.assertSequenceEqual(ordered, sorted(unordered))


if __name__ == "__main__":
    unittest.main()
