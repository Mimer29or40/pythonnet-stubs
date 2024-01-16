import random
import unittest
from typing import Dict
from typing import Mapping
from typing import MutableSequence
from typing import Optional
from typing import Sequence
from typing import cast

import clr
from System.Reflection import Assembly
from System.Reflection import EventInfo
from System.Reflection import FieldInfo
from System.Reflection import MethodInfo
from System.Reflection import ParameterInfo
from System.Reflection import PropertyInfo
from System.Reflection import TypeInfo

from stubgen.model import CClass
from stubgen.model import CConstructor
from stubgen.model import CDelegate
from stubgen.model import CEnum
from stubgen.model import CEvent
from stubgen.model import CField
from stubgen.model import CInterface
from stubgen.model import CMethod
from stubgen.model import CParameter
from stubgen.model import CProperty
from stubgen.model import CStruct
from stubgen.model import CType
from stubgen.model import CTypeDefinition
from stubgen.model import JsonType
from stubgen.util import make_python_name


class TestBase(unittest.TestCase):
    assembly: Assembly

    @classmethod
    def setUpClass(cls) -> None:
        cls.assembly = clr.AddReference("TestLib")

    @classmethod
    def get_type(cls, type_name: str) -> TypeInfo:
        type_info: TypeInfo
        for type_info in cls.assembly.GetTypes():
            if type_info.Namespace is None or type_info.IsNested:
                continue
            if make_python_name(type_info.Name) == type_name:
                return type_info
        raise NameError(f"Unable to find type named {type_name!r}")

    @classmethod
    def get_types(cls, *type_names: str) -> Mapping[str, TypeInfo]:
        type_map: Dict[str, TypeInfo] = dict.fromkeys(type_names)
        type_name: str
        type_info: TypeInfo
        for type_info in cls.assembly.GetTypes():
            if type_info.Namespace is None or type_info.IsNested:
                continue
            type_name = make_python_name(type_info.Name)
            if type_name in type_names:
                type_map[type_name] = type_info
        for type_name, type_info in type_map.items():
            if type_info is None:
                raise NameError(f"Unable to find type named {type_name!r}")
        return type_map

    def assertCClass(
        self,
        struct: CClass,
        name: str,
        namespace: str,
        abstract: bool,
        generic_args: Sequence[CType],
        super_class: Optional[CType],
        interfaces: Sequence[CType],
        fields: Mapping[str, CField],
        constructors: Mapping[str, CConstructor],
        properties: Mapping[str, CProperty],
        methods: Mapping[str, CMethod],
        dunder_methods: Mapping[str, CMethod],
        events: Mapping[str, CEvent],
        nested: Mapping[str, CTypeDefinition],
    ) -> None:
        self.assertIsNotNone(struct)
        self.assertIsInstance(struct, CClass)
        self.assertEqual(name, struct.name)
        self.assertEqual(namespace, struct.namespace)
        self.assertEqual(abstract, struct.abstract)
        self.assertSequenceEqual(generic_args, struct.generic_args)
        self.assertEqual(super_class, struct.super_class)
        self.assertSequenceEqual(interfaces, struct.interfaces)
        self.assertDictEqual(fields, struct.fields)
        self.assertDictEqual(constructors, struct.constructors)
        self.assertDictEqual(properties, struct.properties)
        self.assertDictEqual(methods, struct.methods)
        self.assertDictEqual(dunder_methods, struct.dunder_methods)
        self.assertDictEqual(events, struct.events)
        self.assertDictEqual(nested, struct.nested)

    def assertCStruct(
        self,
        struct: CStruct,
        name: str,
        namespace: str,
        abstract: bool,
        generic_args: Sequence[CType],
        super_class: Optional[CType],
        interfaces: Sequence[CType],
        fields: Mapping[str, CField],
        constructors: Mapping[str, CConstructor],
        properties: Mapping[str, CProperty],
        methods: Mapping[str, CMethod],
        dunder_methods: Mapping[str, CMethod],
        events: Mapping[str, CEvent],
        nested: Mapping[str, CTypeDefinition],
    ) -> None:
        self.assertIsNotNone(struct)
        self.assertIsInstance(struct, CStruct)
        self.assertEqual(name, struct.name)
        self.assertEqual(namespace, struct.namespace)
        self.assertEqual(abstract, struct.abstract)
        self.assertSequenceEqual(generic_args, struct.generic_args)
        self.assertEqual(super_class, struct.super_class)
        self.assertSequenceEqual(interfaces, struct.interfaces)
        self.assertDictEqual(fields, struct.fields)
        self.assertDictEqual(constructors, struct.constructors)
        self.assertDictEqual(properties, struct.properties)
        self.assertDictEqual(methods, struct.methods)
        self.assertDictEqual(dunder_methods, struct.dunder_methods)
        self.assertDictEqual(events, struct.events)
        self.assertDictEqual(nested, struct.nested)

    def assertCInterface(
        self,
        interface: CInterface,
        name: str,
        namespace: str,
        generic_args: Sequence[CType],
        interfaces: Sequence[CType],
        fields: Mapping[str, CField],
        properties: Mapping[str, CProperty],
        methods: Mapping[str, CMethod],
        dunder_methods: Mapping[str, CMethod],
        events: Mapping[str, CEvent],
        nested: Mapping[str, CTypeDefinition],
    ) -> None:
        self.assertIsNotNone(interface)
        self.assertIsInstance(interface, CInterface)
        self.assertEqual(name, interface.name)
        self.assertEqual(namespace, interface.namespace)
        self.assertSequenceEqual(generic_args, interface.generic_args)
        self.assertSequenceEqual(interfaces, interface.interfaces)
        self.assertDictEqual(fields, interface.fields)
        self.assertDictEqual(properties, interface.properties)
        self.assertDictEqual(methods, interface.methods)
        self.assertDictEqual(dunder_methods, interface.dunder_methods)
        self.assertDictEqual(events, interface.events)
        self.assertDictEqual(nested, interface.nested)

    def assertCEnum(self, enum: CEnum, name: str, namespace: str, fields: Sequence[str]) -> None:
        self.assertIsNotNone(enum)
        self.assertIsInstance(enum, CEnum)
        self.assertEqual(name, enum.name)
        self.assertEqual(namespace, enum.namespace)
        self.assertSequenceEqual(fields, enum.fields)

    def assertCDelegate(
        self,
        delegate: CDelegate,
        name: str,
        namespace: str,
        parameters: Sequence[CParameter],
        return_type: CType,
    ) -> None:
        self.assertIsNotNone(delegate)
        self.assertIsInstance(delegate, CDelegate)
        self.assertEqual(name, delegate.name)
        self.assertEqual(namespace, delegate.namespace)
        self.assertSequenceEqual(parameters, delegate.parameters)
        self.assertEqual(return_type, delegate.return_type)

    def assertCType(
        self,
        type: CType,
        name: str,
        namespace: str,
        inner: Sequence[CType],
        reference: bool,
        generic: bool,
        nullable: bool,
    ) -> None:
        self.assertIsNotNone(type)
        self.assertIsInstance(type, CType)
        self.assertEqual(name, type.name)
        self.assertEqual(namespace, type.namespace)
        self.assertSequenceEqual(inner, type.inner)
        self.assertEqual(reference, type.reference)
        self.assertEqual(generic, type.generic)
        self.assertEqual(nullable, type.nullable)

    def assertCParameter(
        self, parameter: CParameter, name: str, type: CType, default: bool, out: bool
    ) -> None:
        self.assertIsNotNone(parameter)
        self.assertIsInstance(parameter, CParameter)
        self.assertEqual(name, parameter.name)
        self.assertEqual(type, parameter.type)
        self.assertEqual(default, parameter.default)
        self.assertEqual(out, parameter.out)

    def assertCField(
        self, field: CField, name: str, declaring_type: CType, returns: CType, static: bool
    ) -> None:
        self.assertIsNotNone(field)
        self.assertIsInstance(field, CField)
        self.assertEqual(name, field.name)
        self.assertEqual(declaring_type, field.declaring_type)
        self.assertEqual(returns, field.returns)
        self.assertEqual(static, field.static)

    def assertCConstructor(
        self, constructor: CConstructor, declaring_type: CType, parameters: Sequence[CParameter]
    ) -> None:
        self.assertIsNotNone(constructor)
        self.assertIsInstance(constructor, CConstructor)
        self.assertEqual(declaring_type, constructor.declaring_type)
        self.assertSequenceEqual(parameters, constructor.parameters)

    def assertCProperty(
        self,
        property: CProperty,
        name: str,
        declaring_type: CType,
        type: CType,
        setter: bool,
        static: bool,
    ) -> None:
        self.assertIsNotNone(property)
        self.assertIsInstance(property, CProperty)
        self.assertEqual(name, property.name)
        self.assertEqual(declaring_type, property.declaring_type)
        self.assertEqual(type, property.type)
        self.assertEqual(setter, property.setter)
        self.assertEqual(static, property.static)

    def assertCMethod(
        self,
        method: CMethod,
        name: str,
        declaring_type: CType,
        parameters: Sequence[CParameter],
        returns: Sequence[CType],
        static: bool,
    ) -> None:
        self.assertIsNotNone(method)
        self.assertIsInstance(method, CMethod)
        self.assertEqual(name, method.name)
        self.assertEqual(declaring_type, method.declaring_type)
        self.assertSequenceEqual(parameters, method.parameters)
        self.assertSequenceEqual(returns, method.returns)
        self.assertEqual(static, method.static)

    def assertCEvent(self, event: CEvent, name: str, declaring_type: CType, type: CType) -> None:
        self.assertIsNotNone(event)
        self.assertIsInstance(event, CEvent)
        self.assertEqual(name, event.name)
        self.assertEqual(declaring_type, event.declaring_type)
        self.assertEqual(type, event.type)


class TestCClass(TestBase):
    def test_from_info_generic(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithGeneric")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCClass(
            struct=cast(CClass, type_def),
            name="ClassWithGeneric",
            namespace="TestLib",
            abstract=False,
            generic_args=(CType(name="T", namespace="TestLib", generic=True),),
            super_class=CType(name="Object", namespace="System"),
            interfaces=(),
            fields={},
            constructors={
                "TestLib.ClassWithGeneric[TestLib.$T].__init__()": CConstructor(
                    declaring_type=CType(
                        name="ClassWithGeneric",
                        namespace="TestLib",
                        inner=(CType(name="T", namespace="TestLib", generic=True),),
                    ),
                    parameters=(),
                ),
            },
            properties={},
            methods={
                "System.Object.Equals(System.Object) -> System.Boolean": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Object.GetHashCode() -> System.Int32": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "System.Object.GetType() -> System.Type": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Type", namespace="System"),),
                ),
                "System.Object.ToString() -> System.String": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="String", namespace="System"),),
                ),
            },
            dunder_methods={},
            events={},
            nested={},
        )

    def test_from_info_generic_multi(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithMultiGeneric")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCClass(
            struct=cast(CClass, type_def),
            name="ClassWithMultiGeneric",
            namespace="TestLib",
            abstract=False,
            generic_args=(
                CType(name="U", namespace="TestLib", generic=True),
                CType(name="V", namespace="TestLib", generic=True),
            ),
            super_class=CType(name="Object", namespace="System"),
            interfaces=(),
            fields={},
            constructors={
                "TestLib.ClassWithMultiGeneric[TestLib.$U, TestLib.$V].__init__()": CConstructor(
                    declaring_type=CType(
                        name="ClassWithMultiGeneric",
                        namespace="TestLib",
                        inner=(
                            CType(name="U", namespace="TestLib", generic=True),
                            CType(name="V", namespace="TestLib", generic=True),
                        ),
                    ),
                    parameters=(),
                ),
            },
            properties={},
            methods={
                "System.Object.Equals(System.Object) -> System.Boolean": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Object.GetHashCode() -> System.Int32": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "System.Object.GetType() -> System.Type": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Type", namespace="System"),),
                ),
                "System.Object.ToString() -> System.String": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="String", namespace="System"),),
                ),
            },
            dunder_methods={},
            events={},
            nested={},
        )

    def test_from_info_interfaces(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithInterface")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCClass(
            struct=cast(CClass, type_def),
            name="ClassWithInterface",
            namespace="TestLib",
            abstract=False,
            generic_args=(),
            super_class=CType(name="Object", namespace="System"),
            interfaces=(
                CType(
                    name="IEquatable",
                    namespace="System",
                    inner=(CType(name="ClassWithInterface", namespace="TestLib"),),
                ),
            ),
            fields={},
            constructors={
                "TestLib.ClassWithInterface.__init__()": CConstructor(
                    declaring_type=CType(name="ClassWithInterface", namespace="TestLib"),
                    parameters=(),
                ),
            },
            properties={},
            methods={
                "System.Object.Equals(System.Object) -> System.Boolean": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "System.IEquatable[TestLib.ClassWithInterface].Equals(TestLib.ClassWithInterface) -> System.Boolean": CMethod(
                    name="Equals",
                    declaring_type=CType(
                        name="IEquatable",
                        namespace="System",
                        inner=(CType(name="ClassWithInterface", namespace="TestLib"),),
                    ),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithInterface", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Object.GetHashCode() -> System.Int32": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "System.Object.GetType() -> System.Type": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Type", namespace="System"),),
                ),
                "System.Object.ToString() -> System.String": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="String", namespace="System"),),
                ),
            },
            dunder_methods={},
            events={},
            nested={},
        )

    def test_from_info_fields(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithFields")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCClass(
            struct=cast(CClass, type_def),
            name="ClassWithFields",
            namespace="TestLib",
            abstract=False,
            generic_args=(),
            super_class=CType(name="Object", namespace="System"),
            interfaces=(),
            fields={
                "TestLib.ClassWithFields.InstanceFieldA": CField(
                    name="InstanceFieldA",
                    declaring_type=CType(name="ClassWithFields", namespace="TestLib"),
                    returns=CType(name="Int32", namespace="System"),
                ),
                "TestLib.ClassWithFields.InstanceFieldB": CField(
                    name="InstanceFieldB",
                    declaring_type=CType(name="ClassWithFields", namespace="TestLib"),
                    returns=CType(name="Int32", namespace="System"),
                ),
                "TestLib.ClassWithFields.InstanceFieldC": CField(
                    name="InstanceFieldC",
                    declaring_type=CType(name="ClassWithFields", namespace="TestLib"),
                    returns=CType(name="Int32", namespace="System"),
                ),
                "TestLib.ClassWithFields.StaticFieldA": CField(
                    name="StaticFieldA",
                    declaring_type=CType(name="ClassWithFields", namespace="TestLib"),
                    returns=CType(name="Int32", namespace="System"),
                    static=True,
                ),
                "TestLib.ClassWithFields.StaticFieldB": CField(
                    name="StaticFieldB",
                    declaring_type=CType(name="ClassWithFields", namespace="TestLib"),
                    returns=CType(name="Int32", namespace="System"),
                    static=True,
                ),
                "TestLib.ClassWithFields.StaticFieldC": CField(
                    name="StaticFieldC",
                    declaring_type=CType(name="ClassWithFields", namespace="TestLib"),
                    returns=CType(name="Int32", namespace="System"),
                    static=True,
                ),
            },
            constructors={
                "TestLib.ClassWithFields.__init__()": CConstructor(
                    declaring_type=CType(name="ClassWithFields", namespace="TestLib"),
                    parameters=(),
                ),
            },
            properties={},
            methods={
                "System.Object.Equals(System.Object) -> System.Boolean": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Object.GetHashCode() -> System.Int32": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "System.Object.GetType() -> System.Type": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Type", namespace="System"),),
                ),
                "System.Object.ToString() -> System.String": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="String", namespace="System"),),
                ),
            },
            dunder_methods={},
            events={},
            nested={},
        )

    def test_from_info_constructors(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithConstructors")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCClass(
            struct=cast(CClass, type_def),
            name="ClassWithConstructors",
            namespace="TestLib",
            abstract=False,
            generic_args=(),
            super_class=CType(name="Object", namespace="System"),
            interfaces=(),
            fields={},
            constructors={
                "TestLib.ClassWithConstructors.__init__()": CConstructor(
                    declaring_type=CType(name="ClassWithConstructors", namespace="TestLib"),
                    parameters=(),
                ),
                "TestLib.ClassWithConstructors.__init__(System.Int32)": CConstructor(
                    declaring_type=CType(name="ClassWithConstructors", namespace="TestLib"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                    ),
                ),
                "TestLib.ClassWithConstructors.__init__(System.Int32, System.Int32)": CConstructor(
                    declaring_type=CType(name="ClassWithConstructors", namespace="TestLib"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                        CParameter(name="param1", type=CType(name="Int32", namespace="System")),
                    ),
                ),
                "TestLib.ClassWithConstructors.__init__(System.Int32, System.Int32, System.Int32)": CConstructor(
                    declaring_type=CType(name="ClassWithConstructors", namespace="TestLib"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                        CParameter(name="param1", type=CType(name="Int32", namespace="System")),
                        CParameter(name="param2", type=CType(name="Int32", namespace="System")),
                    ),
                ),
            },
            properties={},
            methods={
                "System.Object.Equals(System.Object) -> System.Boolean": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Object.GetHashCode() -> System.Int32": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "System.Object.GetType() -> System.Type": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Type", namespace="System"),),
                ),
                "System.Object.ToString() -> System.String": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="String", namespace="System"),),
                ),
            },
            dunder_methods={},
            events={},
            nested={},
        )

    def test_from_info_properties(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithProperties")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCClass(
            struct=cast(CClass, type_def),
            name="ClassWithProperties",
            namespace="TestLib",
            abstract=False,
            generic_args=(),
            super_class=CType(name="Object", namespace="System"),
            interfaces=(),
            fields={},
            constructors={
                "TestLib.ClassWithProperties.__init__()": CConstructor(
                    declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                    parameters=(),
                ),
            },
            properties={
                "TestLib.ClassWithProperties.InstanceProperty0": CProperty(
                    name="InstanceProperty0",
                    declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                ),
                "TestLib.ClassWithProperties.InstanceProperty1": CProperty(
                    name="InstanceProperty1",
                    declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                ),
                "TestLib.ClassWithProperties.InstanceProperty2": CProperty(
                    name="InstanceProperty2",
                    declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                ),
                "TestLib.ClassWithProperties.InstanceReadOnlyProperty0": CProperty(
                    name="InstanceReadOnlyProperty0",
                    declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                ),
                "TestLib.ClassWithProperties.InstanceReadOnlyProperty1": CProperty(
                    name="InstanceReadOnlyProperty1",
                    declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                ),
                "TestLib.ClassWithProperties.InstanceReadOnlyProperty2": CProperty(
                    name="InstanceReadOnlyProperty2",
                    declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                ),
                "TestLib.ClassWithProperties.StaticProperty0": CProperty(
                    name="StaticProperty0",
                    declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                    static=True,
                ),
                "TestLib.ClassWithProperties.StaticProperty1": CProperty(
                    name="StaticProperty1",
                    declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                    static=True,
                ),
                "TestLib.ClassWithProperties.StaticProperty2": CProperty(
                    name="StaticProperty2",
                    declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                    static=True,
                ),
                "TestLib.ClassWithProperties.StaticReadOnlyProperty0": CProperty(
                    name="StaticReadOnlyProperty0",
                    declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
                "TestLib.ClassWithProperties.StaticReadOnlyProperty1": CProperty(
                    name="StaticReadOnlyProperty1",
                    declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
                "TestLib.ClassWithProperties.StaticReadOnlyProperty2": CProperty(
                    name="StaticReadOnlyProperty2",
                    declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
            },
            methods={
                "System.Object.Equals(System.Object) -> System.Boolean": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Object.GetHashCode() -> System.Int32": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "System.Object.GetType() -> System.Type": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Type", namespace="System"),),
                ),
                "System.Object.ToString() -> System.String": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="String", namespace="System"),),
                ),
            },
            dunder_methods={},
            events={},
            nested={},
        )

    def test_from_info_methods(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithMethods")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCClass(
            struct=cast(CClass, type_def),
            name="ClassWithMethods",
            namespace="TestLib",
            abstract=False,
            generic_args=(),
            super_class=CType(name="Object", namespace="System"),
            interfaces=(),
            fields={},
            constructors={
                "TestLib.ClassWithMethods.__init__()": CConstructor(
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                    parameters=(),
                ),
            },
            properties={},
            methods={
                "System.Object.Equals(System.Object) -> System.Boolean": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Object.GetHashCode() -> System.Int32": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "System.Object.GetType() -> System.Type": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Type", namespace="System"),),
                ),
                "TestLib.ClassWithMethods.InstanceMethodWithDefaultParam(System.Int32) -> System.Int32": CMethod(
                    name="InstanceMethodWithDefaultParam",
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System"),
                            default=True,
                        ),
                    ),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib.ClassWithMethods.InstanceMethodWithNullableDefaultParam(System.Int32?) -> System.Int32": CMethod(
                    name="InstanceMethodWithNullableDefaultParam",
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System", nullable=True),
                            default=True,
                        ),
                    ),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib.ClassWithMethods.InstanceMethodWithNullableOutParam(System.*Int32?) -> System.Int32, System.*Int32?": CMethod(
                    name="InstanceMethodWithNullableOutParam",
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(
                                name="Int32", namespace="System", reference=True, nullable=True
                            ),
                            out=True,
                        ),
                    ),
                    returns=(
                        CType(name="Int32", namespace="System"),
                        CType(name="Int32", namespace="System", reference=True, nullable=True),
                    ),
                ),
                "TestLib.ClassWithMethods.InstanceMethodWithNullableParam(System.Int32?) -> System.Int32": CMethod(
                    name="InstanceMethodWithNullableParam",
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System", nullable=True),
                        ),
                    ),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib.ClassWithMethods.InstanceMethodWithOutParam(System.*Int32) -> System.Int32, System.*Int32": CMethod(
                    name="InstanceMethodWithOutParam",
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System", reference=True),
                            out=True,
                        ),
                    ),
                    returns=(
                        CType(name="Int32", namespace="System"),
                        CType(name="Int32", namespace="System", reference=True),
                    ),
                ),
                "TestLib.ClassWithMethods.InstanceMethodWithParams0() -> System.Int32": CMethod(
                    name="InstanceMethodWithParams0",
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                    parameters=(),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib.ClassWithMethods.InstanceMethodWithParams1(System.Int32) -> System.Int32": CMethod(
                    name="InstanceMethodWithParams1",
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                    ),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib.ClassWithMethods.InstanceMethodWithParams2(System.Int32, System.Int32) -> System.Int32": CMethod(
                    name="InstanceMethodWithParams2",
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                        CParameter(name="param1", type=CType(name="Int32", namespace="System")),
                    ),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib.ClassWithMethods.StaticMethodWithDefaultParam(System.Int32) -> System.Int32": CMethod(
                    name="StaticMethodWithDefaultParam",
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System"),
                            default=True,
                        ),
                    ),
                    returns=(CType(name="Int32", namespace="System"),),
                    static=True,
                ),
                "TestLib.ClassWithMethods.StaticMethodWithNullableDefaultParam(System.Int32?) -> System.Int32": CMethod(
                    name="StaticMethodWithNullableDefaultParam",
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System", nullable=True),
                            default=True,
                        ),
                    ),
                    returns=(CType(name="Int32", namespace="System"),),
                    static=True,
                ),
                "TestLib.ClassWithMethods.StaticMethodWithNullableOutParam(System.*Int32?) -> System.Int32, System.*Int32?": CMethod(
                    name="StaticMethodWithNullableOutParam",
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(
                                name="Int32", namespace="System", reference=True, nullable=True
                            ),
                            out=True,
                        ),
                    ),
                    returns=(
                        CType(name="Int32", namespace="System"),
                        CType(name="Int32", namespace="System", reference=True, nullable=True),
                    ),
                    static=True,
                ),
                "TestLib.ClassWithMethods.StaticMethodWithNullableParam(System.Int32?) -> System.Int32": CMethod(
                    name="StaticMethodWithNullableParam",
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System", nullable=True),
                        ),
                    ),
                    returns=(CType(name="Int32", namespace="System"),),
                    static=True,
                ),
                "TestLib.ClassWithMethods.StaticMethodWithOutParam(System.*Int32) -> System.Int32, System.*Int32": CMethod(
                    name="StaticMethodWithOutParam",
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System", reference=True),
                            out=True,
                        ),
                    ),
                    returns=(
                        CType(name="Int32", namespace="System"),
                        CType(name="Int32", namespace="System", reference=True),
                    ),
                    static=True,
                ),
                "TestLib.ClassWithMethods.StaticMethodWithParams0() -> System.Int32": CMethod(
                    name="StaticMethodWithParams0",
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                    parameters=(),
                    returns=(CType(name="Int32", namespace="System"),),
                    static=True,
                ),
                "TestLib.ClassWithMethods.StaticMethodWithParams1(System.Int32) -> System.Int32": CMethod(
                    name="StaticMethodWithParams1",
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                    ),
                    returns=(CType(name="Int32", namespace="System"),),
                    static=True,
                ),
                "TestLib.ClassWithMethods.StaticMethodWithParams2(System.Int32, System.Int32) -> System.Int32": CMethod(
                    name="StaticMethodWithParams2",
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                        CParameter(name="param1", type=CType(name="Int32", namespace="System")),
                    ),
                    returns=(CType(name="Int32", namespace="System"),),
                    static=True,
                ),
                "System.Object.ToString() -> System.String": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="String", namespace="System"),),
                ),
            },
            dunder_methods={},
            events={},
            nested={},
        )

    def test_from_info_methods_dunder(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithOperatorMethods")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCClass(
            struct=cast(CClass, type_def),
            name="ClassWithOperatorMethods",
            namespace="TestLib",
            abstract=False,
            generic_args=(),
            super_class=CType(name="Object", namespace="System"),
            interfaces=(),
            fields={},
            constructors={
                "TestLib.ClassWithOperatorMethods.__init__()": CConstructor(
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(),
                ),
            },
            properties={},
            methods={
                "System.Object.Equals(System.Object) -> System.Boolean": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(
                            name="obj",
                            type=CType(name="Object", namespace="System"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Object.GetHashCode() -> System.Int32": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "System.Object.GetType() -> System.Type": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Type", namespace="System"),),
                ),
                "System.Object.ToString() -> System.String": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="String", namespace="System"),),
                ),
                "TestLib.ClassWithOperatorMethods.op_Addition(TestLib.ClassWithOperatorMethods, TestLib.ClassWithOperatorMethods) -> TestLib.ClassWithOperatorMethods": CMethod(
                    name="op_Addition",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.ClassWithOperatorMethods.op_BitwiseAnd(TestLib.ClassWithOperatorMethods, TestLib.ClassWithOperatorMethods) -> TestLib.ClassWithOperatorMethods": CMethod(
                    name="op_BitwiseAnd",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.ClassWithOperatorMethods.op_BitwiseOr(TestLib.ClassWithOperatorMethods, TestLib.ClassWithOperatorMethods) -> TestLib.ClassWithOperatorMethods": CMethod(
                    name="op_BitwiseOr",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.ClassWithOperatorMethods.op_Decrement(TestLib.ClassWithOperatorMethods) -> TestLib.ClassWithOperatorMethods": CMethod(
                    name="op_Decrement",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.ClassWithOperatorMethods.op_Division(TestLib.ClassWithOperatorMethods, TestLib.ClassWithOperatorMethods) -> TestLib.ClassWithOperatorMethods": CMethod(
                    name="op_Division",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.ClassWithOperatorMethods.op_Equality(TestLib.ClassWithOperatorMethods, TestLib.ClassWithOperatorMethods) -> System.Boolean": CMethod(
                    name="op_Equality",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib.ClassWithOperatorMethods.op_ExclusiveOr(TestLib.ClassWithOperatorMethods, TestLib.ClassWithOperatorMethods) -> TestLib.ClassWithOperatorMethods": CMethod(
                    name="op_ExclusiveOr",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.ClassWithOperatorMethods.op_False(TestLib.ClassWithOperatorMethods) -> System.Boolean": CMethod(
                    name="op_False",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib.ClassWithOperatorMethods.op_GreaterThan(TestLib.ClassWithOperatorMethods, TestLib.ClassWithOperatorMethods) -> System.Boolean": CMethod(
                    name="op_GreaterThan",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib.ClassWithOperatorMethods.op_GreaterThanOrEqual(TestLib.ClassWithOperatorMethods, TestLib.ClassWithOperatorMethods) -> System.Boolean": CMethod(
                    name="op_GreaterThanOrEqual",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib.ClassWithOperatorMethods.op_Increment(TestLib.ClassWithOperatorMethods) -> TestLib.ClassWithOperatorMethods": CMethod(
                    name="op_Increment",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.ClassWithOperatorMethods.op_Inequality(TestLib.ClassWithOperatorMethods, TestLib.ClassWithOperatorMethods) -> System.Boolean": CMethod(
                    name="op_Inequality",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib.ClassWithOperatorMethods.op_LessThan(TestLib.ClassWithOperatorMethods, TestLib.ClassWithOperatorMethods) -> System.Boolean": CMethod(
                    name="op_LessThan",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib.ClassWithOperatorMethods.op_LessThanOrEqual(TestLib.ClassWithOperatorMethods, TestLib.ClassWithOperatorMethods) -> System.Boolean": CMethod(
                    name="op_LessThanOrEqual",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib.ClassWithOperatorMethods.op_LogicalNot(TestLib.ClassWithOperatorMethods) -> System.Boolean": CMethod(
                    name="op_LogicalNot",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib.ClassWithOperatorMethods.op_Modulus(TestLib.ClassWithOperatorMethods, TestLib.ClassWithOperatorMethods) -> TestLib.ClassWithOperatorMethods": CMethod(
                    name="op_Modulus",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.ClassWithOperatorMethods.op_Multiply(TestLib.ClassWithOperatorMethods, TestLib.ClassWithOperatorMethods) -> TestLib.ClassWithOperatorMethods": CMethod(
                    name="op_Multiply",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.ClassWithOperatorMethods.op_OnesComplement(TestLib.ClassWithOperatorMethods) -> TestLib.ClassWithOperatorMethods": CMethod(
                    name="op_OnesComplement",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.ClassWithOperatorMethods.op_Subtraction(TestLib.ClassWithOperatorMethods, TestLib.ClassWithOperatorMethods) -> TestLib.ClassWithOperatorMethods": CMethod(
                    name="op_Subtraction",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.ClassWithOperatorMethods.op_True(TestLib.ClassWithOperatorMethods) -> System.Boolean": CMethod(
                    name="op_True",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib.ClassWithOperatorMethods.op_UnaryNegation(TestLib.ClassWithOperatorMethods) -> TestLib.ClassWithOperatorMethods": CMethod(
                    name="op_UnaryNegation",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.ClassWithOperatorMethods.op_UnaryPlus(TestLib.ClassWithOperatorMethods) -> TestLib.ClassWithOperatorMethods": CMethod(
                    name="op_UnaryPlus",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
            },
            dunder_methods={
                "TestLib.ClassWithOperatorMethods.__add__(TestLib.ClassWithOperatorMethods) -> TestLib.ClassWithOperatorMethods": CMethod(
                    name="__add__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib.ClassWithOperatorMethods.__and__(TestLib.ClassWithOperatorMethods) -> TestLib.ClassWithOperatorMethods": CMethod(
                    name="__and__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib.ClassWithOperatorMethods.__eq__(TestLib.ClassWithOperatorMethods) -> System.Boolean": CMethod(
                    name="__eq__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib.ClassWithOperatorMethods.__ge__(TestLib.ClassWithOperatorMethods) -> System.Boolean": CMethod(
                    name="__ge__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib.ClassWithOperatorMethods.__gt__(TestLib.ClassWithOperatorMethods) -> System.Boolean": CMethod(
                    name="__gt__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib.ClassWithOperatorMethods.__invert__() -> TestLib.ClassWithOperatorMethods": CMethod(
                    name="__invert__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(),
                    returns=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib.ClassWithOperatorMethods.__le__(TestLib.ClassWithOperatorMethods) -> System.Boolean": CMethod(
                    name="__le__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib.ClassWithOperatorMethods.__lt__(TestLib.ClassWithOperatorMethods) -> System.Boolean": CMethod(
                    name="__lt__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib.ClassWithOperatorMethods.__mod__(TestLib.ClassWithOperatorMethods) -> TestLib.ClassWithOperatorMethods": CMethod(
                    name="__mod__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib.ClassWithOperatorMethods.__mul__(TestLib.ClassWithOperatorMethods) -> TestLib.ClassWithOperatorMethods": CMethod(
                    name="__mul__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib.ClassWithOperatorMethods.__ne__(TestLib.ClassWithOperatorMethods) -> System.Boolean": CMethod(
                    name="__ne__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib.ClassWithOperatorMethods.__neg__() -> TestLib.ClassWithOperatorMethods": CMethod(
                    name="__neg__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(),
                    returns=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib.ClassWithOperatorMethods.__or__(TestLib.ClassWithOperatorMethods) -> TestLib.ClassWithOperatorMethods": CMethod(
                    name="__or__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib.ClassWithOperatorMethods.__pos__() -> TestLib.ClassWithOperatorMethods": CMethod(
                    name="__pos__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(),
                    returns=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib.ClassWithOperatorMethods.__sub__(TestLib.ClassWithOperatorMethods) -> TestLib.ClassWithOperatorMethods": CMethod(
                    name="__sub__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib.ClassWithOperatorMethods.__truediv__(TestLib.ClassWithOperatorMethods) -> TestLib.ClassWithOperatorMethods": CMethod(
                    name="__truediv__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib.ClassWithOperatorMethods.__xor__(TestLib.ClassWithOperatorMethods) -> TestLib.ClassWithOperatorMethods": CMethod(
                    name="__xor__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                ),
            },
            events={},
            nested={},
        )

    def test_from_info_events(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithEvents")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCClass(
            struct=cast(CClass, type_def),
            name="ClassWithEvents",
            namespace="TestLib",
            abstract=False,
            generic_args=(),
            super_class=CType(name="Object", namespace="System"),
            interfaces=(),
            fields={},
            constructors={
                "TestLib.ClassWithEvents.__init__()": CConstructor(
                    declaring_type=CType(name="ClassWithEvents", namespace="TestLib"),
                    parameters=(),
                ),
            },
            properties={},
            methods={
                "System.Object.Equals(System.Object) -> System.Boolean": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Object.GetHashCode() -> System.Int32": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "System.Object.GetType() -> System.Type": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Type", namespace="System"),),
                ),
                "System.Object.ToString() -> System.String": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="String", namespace="System"),),
                ),
            },
            dunder_methods={},
            events={
                "TestLib.ClassWithEvents.Event -> (System.EventHandler)": CEvent(
                    name="Event",
                    declaring_type=CType(name="ClassWithEvents", namespace="TestLib"),
                    type=CType(name="EventHandler", namespace="System"),
                ),
                "TestLib.ClassWithEvents.EventWithArgs -> (System.EventHandler[System.EventArgs])": CEvent(
                    name="EventWithArgs",
                    declaring_type=CType(name="ClassWithEvents", namespace="TestLib"),
                    type=CType(
                        name="EventHandler",
                        namespace="System",
                        inner=(CType(name="EventArgs", namespace="System"),),
                    ),
                ),
            },
            nested={},
        )

    def test_from_info_nested(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithNested")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCClass(
            struct=cast(CClass, type_def),
            name="ClassWithNested",
            namespace="TestLib",
            abstract=False,
            generic_args=(),
            super_class=CType(name="Object", namespace="System"),
            interfaces=(),
            fields={},
            constructors={
                "TestLib.ClassWithNested.__init__()": CConstructor(
                    declaring_type=CType(name="ClassWithNested", namespace="TestLib"),
                    parameters=(),
                ),
            },
            properties={},
            methods={
                "System.Object.Equals(System.Object) -> System.Boolean": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Object.GetHashCode() -> System.Int32": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "System.Object.GetType() -> System.Type": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Type", namespace="System"),),
                ),
                "System.Object.ToString() -> System.String": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="String", namespace="System"),),
                ),
            },
            dunder_methods={},
            events={},
            nested={
                "TestLib.INestedInterface": CInterface(
                    name="INestedInterface",
                    namespace="TestLib",
                    generic_args=(),
                    interfaces=(),
                    fields={},
                    properties={},
                    methods={},
                    dunder_methods={},
                    events={},
                    nested={},
                ),
                "TestLib.NestedClass": CClass(
                    name="NestedClass",
                    namespace="TestLib",
                    abstract=False,
                    generic_args=(),
                    super_class=CType(name="Object", namespace="System"),
                    interfaces=(),
                    fields={},
                    constructors={
                        "TestLib.NestedClass.__init__()": CConstructor(
                            declaring_type=CType(name="NestedClass", namespace="TestLib"),
                            parameters=(),
                        )
                    },
                    properties={},
                    methods={
                        "System.Object.Equals(System.Object) -> System.Boolean": CMethod(
                            name="Equals",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(
                                CParameter(
                                    name="obj",
                                    type=CType(name="Object", namespace="System"),
                                ),
                            ),
                            returns=(CType(name="Boolean", namespace="System"),),
                        ),
                        "System.Object.GetHashCode() -> System.Int32": CMethod(
                            name="GetHashCode",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            returns=(CType(name="Int32", namespace="System"),),
                        ),
                        "System.Object.GetType() -> System.Type": CMethod(
                            name="GetType",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            returns=(CType(name="Type", namespace="System"),),
                        ),
                        "System.Object.ToString() -> System.String": CMethod(
                            name="ToString",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            returns=(CType(name="String", namespace="System"),),
                        ),
                    },
                    dunder_methods={},
                    events={},
                    nested={},
                ),
                "TestLib.NestedDelegate": CDelegate(
                    name="NestedDelegate",
                    namespace="TestLib",
                    parameters=(),
                    return_type=CType(name="Void", namespace="System"),
                ),
                "TestLib.NestedEnum": CEnum(name="NestedEnum", namespace="TestLib", fields=()),
                "TestLib.NestedStruct": CStruct(
                    name="NestedStruct",
                    namespace="TestLib",
                    abstract=False,
                    generic_args=(),
                    super_class=CType(name="ValueType", namespace="System"),
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={
                        "System.Object.Equals(System.Object) -> System.Boolean": CMethod(
                            name="Equals",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(
                                CParameter(
                                    name="obj",
                                    type=CType(name="Object", namespace="System"),
                                ),
                            ),
                            returns=(CType(name="Boolean", namespace="System"),),
                        ),
                        "System.Object.GetHashCode() -> System.Int32": CMethod(
                            name="GetHashCode",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            returns=(CType(name="Int32", namespace="System"),),
                        ),
                        "System.Object.GetType() -> System.Type": CMethod(
                            name="GetType",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            returns=(CType(name="Type", namespace="System"),),
                        ),
                        "System.Object.ToString() -> System.String": CMethod(
                            name="ToString",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            returns=(CType(name="String", namespace="System"),),
                        ),
                    },
                    dunder_methods={},
                    events={},
                    nested={},
                ),
            },
        )

    def test_json_generic(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            abstract=False,
            generic_args=(CType(name="T", namespace="Namespace", generic=True),),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            dunder_methods={},
            events={},
            nested={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "class",
                "name": "Class",
                "namespace": "Namespace",
                "abstract": False,
                "generic_args": ("Namespace.$T",),
                "super_class": None,
                "interfaces": (),
                "fields": {},
                "constructors": {},
                "properties": {},
                "methods": {},
                "dunder_methods": {},
                "events": {},
                "nested": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_generic_multi(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            abstract=False,
            generic_args=(
                CType(name="U", namespace="Namespace", generic=True),
                CType(name="V", namespace="Namespace", generic=True),
            ),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            dunder_methods={},
            events={},
            nested={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "class",
                "name": "Class",
                "namespace": "Namespace",
                "abstract": False,
                "generic_args": ("Namespace.$U", "Namespace.$V"),
                "super_class": None,
                "interfaces": (),
                "fields": {},
                "constructors": {},
                "properties": {},
                "methods": {},
                "dunder_methods": {},
                "events": {},
                "nested": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_interfaces(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
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
            dunder_methods={},
            events={},
            nested={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "class",
                "name": "Class",
                "namespace": "Namespace",
                "abstract": False,
                "generic_args": (),
                "super_class": None,
                "interfaces": ("Namespace.InterfaceA", "Namespace.InterfaceB"),
                "fields": {},
                "constructors": {},
                "properties": {},
                "methods": {},
                "dunder_methods": {},
                "events": {},
                "nested": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_fields(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={
                "Namespace.Class.InstanceFieldA": CField(
                    name="InstanceFieldA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    returns=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace.Class.InstanceFieldB": CField(
                    name="InstanceFieldB",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    returns=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace.Class.InstanceFieldC": CField(
                    name="InstanceFieldC",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    returns=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace.Class.StaticFieldA": CField(
                    name="StaticFieldA",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    returns=CType(name="Type", namespace="Namespace"),
                    static=True,
                ),
                "Namespace.Class.StaticFieldB": CField(
                    name="StaticFieldB",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    returns=CType(name="Type", namespace="Namespace"),
                    static=True,
                ),
                "Namespace.Class.StaticFieldC": CField(
                    name="StaticFieldC",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    returns=CType(name="Type", namespace="Namespace"),
                    static=True,
                ),
            },
            constructors={},
            properties={},
            methods={},
            dunder_methods={},
            events={},
            nested={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "class",
                "name": "Class",
                "namespace": "Namespace",
                "abstract": False,
                "generic_args": (),
                "super_class": None,
                "interfaces": (),
                "fields": {
                    "Namespace.Class.InstanceFieldA": {
                        "name": "InstanceFieldA",
                        "declaring_type": "Namespace.Class",
                        "returns": "Namespace.Type",
                        "static": False,
                    },
                    "Namespace.Class.InstanceFieldB": {
                        "name": "InstanceFieldB",
                        "declaring_type": "Namespace.Class",
                        "returns": "Namespace.Type",
                        "static": False,
                    },
                    "Namespace.Class.InstanceFieldC": {
                        "name": "InstanceFieldC",
                        "declaring_type": "Namespace.Class",
                        "returns": "Namespace.Type",
                        "static": False,
                    },
                    "Namespace.Class.StaticFieldA": {
                        "name": "StaticFieldA",
                        "declaring_type": "Namespace.Class",
                        "returns": "Namespace.Type",
                        "static": True,
                    },
                    "Namespace.Class.StaticFieldB": {
                        "name": "StaticFieldB",
                        "declaring_type": "Namespace.Class",
                        "returns": "Namespace.Type",
                        "static": True,
                    },
                    "Namespace.Class.StaticFieldC": {
                        "name": "StaticFieldC",
                        "declaring_type": "Namespace.Class",
                        "returns": "Namespace.Type",
                        "static": True,
                    },
                },
                "constructors": {},
                "properties": {},
                "methods": {},
                "dunder_methods": {},
                "events": {},
                "nested": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_constructors(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
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
                "Namespace.Class.__init__(Namespace.Type)": CConstructor(
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                    ),
                ),
                "Namespace.Class.__init__(Namespace.Type, Namespace.Type)": CConstructor(
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                        CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
                    ),
                ),
                "Namespace.Class.__init__(Namespace.Type, Namespace.Type, Namespace.Type)": CConstructor(
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
            dunder_methods={},
            events={},
            nested={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "class",
                "name": "Class",
                "namespace": "Namespace",
                "abstract": False,
                "generic_args": (),
                "super_class": None,
                "interfaces": (),
                "fields": {},
                "constructors": {
                    "Namespace.Class.__init__()": {
                        "declaring_type": "Namespace.Class",
                        "parameters": (),
                    },
                    "Namespace.Class.__init__(Namespace.Type)": {
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.Type",
                                "default": False,
                                "out": False,
                            },
                        ),
                    },
                    "Namespace.Class.__init__(Namespace.Type, Namespace.Type)": {
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.Type",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "param1",
                                "type": "Namespace.Type",
                                "default": False,
                                "out": False,
                            },
                        ),
                    },
                    "Namespace.Class.__init__(Namespace.Type, Namespace.Type, Namespace.Type)": {
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.Type",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "param1",
                                "type": "Namespace.Type",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "param2",
                                "type": "Namespace.Type",
                                "default": False,
                                "out": False,
                            },
                        ),
                    },
                },
                "properties": {},
                "methods": {},
                "dunder_methods": {},
                "events": {},
                "nested": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_properties(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={
                "Namespace.Class.InstanceProperty0": CProperty(
                    name="InstanceProperty0",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    setter=True,
                ),
                "Namespace.Class.InstanceProperty1": CProperty(
                    name="InstanceProperty1",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    setter=True,
                ),
                "Namespace.Class.InstanceProperty2": CProperty(
                    name="InstanceProperty2",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    setter=True,
                ),
                "Namespace.Class.InstanceReadOnlyProperty0": CProperty(
                    name="InstanceReadOnlyProperty0",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace.Class.InstanceReadOnlyProperty1": CProperty(
                    name="InstanceReadOnlyProperty1",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace.Class.InstanceReadOnlyProperty2": CProperty(
                    name="InstanceReadOnlyProperty2",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace.Class.StaticProperty0": CProperty(
                    name="StaticProperty0",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    setter=True,
                    static=True,
                ),
                "Namespace.Class.StaticProperty1": CProperty(
                    name="StaticProperty1",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    setter=True,
                    static=True,
                ),
                "Namespace.Class.StaticProperty2": CProperty(
                    name="StaticProperty2",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    setter=True,
                    static=True,
                ),
                "Namespace.Class.StaticReadOnlyProperty0": CProperty(
                    name="StaticReadOnlyProperty0",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    static=True,
                ),
                "Namespace.Class.StaticReadOnlyProperty1": CProperty(
                    name="StaticReadOnlyProperty1",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    static=True,
                ),
                "Namespace.Class.StaticReadOnlyProperty2": CProperty(
                    name="StaticReadOnlyProperty2",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    static=True,
                ),
            },
            methods={},
            dunder_methods={},
            events={},
            nested={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "class",
                "name": "Class",
                "namespace": "Namespace",
                "abstract": False,
                "generic_args": (),
                "super_class": None,
                "interfaces": (),
                "fields": {},
                "constructors": {},
                "properties": {
                    "Namespace.Class.InstanceProperty0": {
                        "name": "InstanceProperty0",
                        "declaring_type": "Namespace.Class",
                        "type": "Namespace.Type",
                        "setter": True,
                        "static": False,
                    },
                    "Namespace.Class.InstanceProperty1": {
                        "name": "InstanceProperty1",
                        "declaring_type": "Namespace.Class",
                        "type": "Namespace.Type",
                        "setter": True,
                        "static": False,
                    },
                    "Namespace.Class.InstanceProperty2": {
                        "name": "InstanceProperty2",
                        "declaring_type": "Namespace.Class",
                        "type": "Namespace.Type",
                        "setter": True,
                        "static": False,
                    },
                    "Namespace.Class.InstanceReadOnlyProperty0": {
                        "name": "InstanceReadOnlyProperty0",
                        "declaring_type": "Namespace.Class",
                        "type": "Namespace.Type",
                        "setter": False,
                        "static": False,
                    },
                    "Namespace.Class.InstanceReadOnlyProperty1": {
                        "name": "InstanceReadOnlyProperty1",
                        "declaring_type": "Namespace.Class",
                        "type": "Namespace.Type",
                        "setter": False,
                        "static": False,
                    },
                    "Namespace.Class.InstanceReadOnlyProperty2": {
                        "name": "InstanceReadOnlyProperty2",
                        "declaring_type": "Namespace.Class",
                        "type": "Namespace.Type",
                        "setter": False,
                        "static": False,
                    },
                    "Namespace.Class.StaticProperty0": {
                        "name": "StaticProperty0",
                        "declaring_type": "Namespace.Class",
                        "type": "Namespace.Type",
                        "setter": True,
                        "static": True,
                    },
                    "Namespace.Class.StaticProperty1": {
                        "name": "StaticProperty1",
                        "declaring_type": "Namespace.Class",
                        "type": "Namespace.Type",
                        "setter": True,
                        "static": True,
                    },
                    "Namespace.Class.StaticProperty2": {
                        "name": "StaticProperty2",
                        "declaring_type": "Namespace.Class",
                        "type": "Namespace.Type",
                        "setter": True,
                        "static": True,
                    },
                    "Namespace.Class.StaticReadOnlyProperty0": {
                        "name": "StaticReadOnlyProperty0",
                        "declaring_type": "Namespace.Class",
                        "type": "Namespace.Type",
                        "setter": False,
                        "static": True,
                    },
                    "Namespace.Class.StaticReadOnlyProperty1": {
                        "name": "StaticReadOnlyProperty1",
                        "declaring_type": "Namespace.Class",
                        "type": "Namespace.Type",
                        "setter": False,
                        "static": True,
                    },
                    "Namespace.Class.StaticReadOnlyProperty2": {
                        "name": "StaticReadOnlyProperty2",
                        "declaring_type": "Namespace.Class",
                        "type": "Namespace.Type",
                        "setter": False,
                        "static": True,
                    },
                },
                "methods": {},
                "dunder_methods": {},
                "events": {},
                "nested": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_methods(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={
                "Namespace.Class.InstanceMethodWithDefaultParam(Namespace.Type) -> Namespace.Type": CMethod(
                    name="InstanceMethodWithDefaultParam",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace"),
                            default=True,
                        ),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace.Class.InstanceMethodWithNullableDefaultParam(Namespace.Type?) -> Namespace.Type": CMethod(
                    name="InstanceMethodWithNullableDefaultParam",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace", nullable=True),
                            default=True,
                        ),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace.Class.InstanceMethodWithNullableOutParam(Namespace.*Type?) -> Namespace.Type, Namespace.*Type?": CMethod(
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
                    returns=(
                        CType(name="Type", namespace="Namespace"),
                        CType(name="Type", namespace="Namespace", reference=True, nullable=True),
                    ),
                ),
                "Namespace.Class.InstanceMethodWithNullableParam(Namespace.Type?) -> Namespace.Type": CMethod(
                    name="InstanceMethodWithNullableParam",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace", nullable=True),
                        ),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace.Class.InstanceMethodWithOutParam(Namespace.*Type) -> Namespace.Type, Namespace.*Type": CMethod(
                    name="InstanceMethodWithOutParam",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace", reference=True),
                            out=True,
                        ),
                    ),
                    returns=(
                        CType(name="Type", namespace="Namespace"),
                        CType(name="Type", namespace="Namespace", reference=True),
                    ),
                ),
                "Namespace.Class.InstanceMethodWithParams0() -> Namespace.Type": CMethod(
                    name="InstanceMethodWithParams0",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(),
                    returns=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace.Class.InstanceMethodWithParams1(Namespace.Type) -> Namespace.Type": CMethod(
                    name="InstanceMethodWithParams1",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace.Class.InstanceMethodWithParams2(Namespace.Type, Namespace.Type) -> Namespace.Type": CMethod(
                    name="InstanceMethodWithParams2",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                        CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace.Class.StaticMethodWithDefaultParam(Namespace.Type) -> Namespace.Type": CMethod(
                    name="StaticMethodWithDefaultParam",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace"),
                            default=True,
                        ),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Class.StaticMethodWithNullableDefaultParam(Namespace.Type?) -> Namespace.Type": CMethod(
                    name="StaticMethodWithNullableDefaultParam",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace", nullable=True),
                            default=True,
                        ),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Class.StaticMethodWithNullableOutParam(Namespace.*Type?) -> Namespace.Type, Namespace.*Type?": CMethod(
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
                    returns=(
                        CType(name="Type", namespace="Namespace"),
                        CType(name="Type", namespace="Namespace", reference=True, nullable=True),
                    ),
                    static=True,
                ),
                "Namespace.Class.StaticMethodWithNullableParam(Namespace.Type?) -> Namespace.Type": CMethod(
                    name="StaticMethodWithNullableParam",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace", nullable=True),
                        ),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Class.StaticMethodWithOutParam(Namespace.*Type) -> Namespace.Type, Namespace.*Type": CMethod(
                    name="StaticMethodWithOutParam",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace", reference=True),
                            out=True,
                        ),
                    ),
                    returns=(
                        CType(name="Type", namespace="Namespace"),
                        CType(name="Type", namespace="Namespace", reference=True),
                    ),
                    static=True,
                ),
                "Namespace.Class.StaticMethodWithParams0() -> Namespace.Type": CMethod(
                    name="StaticMethodWithParams0",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(),
                    returns=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Class.StaticMethodWithParams1(Namespace.Type) -> Namespace.Type": CMethod(
                    name="StaticMethodWithParams1",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Class.StaticMethodWithParams2(Namespace.Type, Namespace.Type) -> Namespace.Type": CMethod(
                    name="StaticMethodWithParams2",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                        CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
            },
            dunder_methods={},
            events={},
            nested={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "class",
                "name": "Class",
                "namespace": "Namespace",
                "abstract": False,
                "generic_args": (),
                "super_class": None,
                "interfaces": (),
                "fields": {},
                "constructors": {},
                "properties": {},
                "methods": {
                    "Namespace.Class.InstanceMethodWithDefaultParam(Namespace.Type) -> Namespace.Type": {
                        "name": "InstanceMethodWithDefaultParam",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.Type",
                                "default": True,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": False,
                    },
                    "Namespace.Class.InstanceMethodWithNullableDefaultParam(Namespace.Type?) -> Namespace.Type": {
                        "name": "InstanceMethodWithNullableDefaultParam",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.Type?",
                                "default": True,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": False,
                    },
                    "Namespace.Class.InstanceMethodWithNullableOutParam(Namespace.*Type?) -> Namespace.Type, Namespace.*Type?": {
                        "name": "InstanceMethodWithNullableOutParam",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.*Type?",
                                "default": False,
                                "out": True,
                            },
                        ),
                        "returns": ("Namespace.Type", "Namespace.*Type?"),
                        "static": False,
                    },
                    "Namespace.Class.InstanceMethodWithNullableParam(Namespace.Type?) -> Namespace.Type": {
                        "name": "InstanceMethodWithNullableParam",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.Type?",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": False,
                    },
                    "Namespace.Class.InstanceMethodWithOutParam(Namespace.*Type) -> Namespace.Type, Namespace.*Type": {
                        "name": "InstanceMethodWithOutParam",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.*Type",
                                "default": False,
                                "out": True,
                            },
                        ),
                        "returns": ("Namespace.Type", "Namespace.*Type"),
                        "static": False,
                    },
                    "Namespace.Class.InstanceMethodWithParams0() -> Namespace.Type": {
                        "name": "InstanceMethodWithParams0",
                        "declaring_type": "Namespace.Class",
                        "parameters": (),
                        "returns": ("Namespace.Type",),
                        "static": False,
                    },
                    "Namespace.Class.InstanceMethodWithParams1(Namespace.Type) -> Namespace.Type": {
                        "name": "InstanceMethodWithParams1",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.Type",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": False,
                    },
                    "Namespace.Class.InstanceMethodWithParams2(Namespace.Type, Namespace.Type) -> Namespace.Type": {
                        "name": "InstanceMethodWithParams2",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.Type",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "param1",
                                "type": "Namespace.Type",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": False,
                    },
                    "Namespace.Class.StaticMethodWithDefaultParam(Namespace.Type) -> Namespace.Type": {
                        "name": "StaticMethodWithDefaultParam",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.Type",
                                "default": True,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": True,
                    },
                    "Namespace.Class.StaticMethodWithNullableDefaultParam(Namespace.Type?) -> Namespace.Type": {
                        "name": "StaticMethodWithNullableDefaultParam",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.Type?",
                                "default": True,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": True,
                    },
                    "Namespace.Class.StaticMethodWithNullableOutParam(Namespace.*Type?) -> Namespace.Type, Namespace.*Type?": {
                        "name": "StaticMethodWithNullableOutParam",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.*Type?",
                                "default": False,
                                "out": True,
                            },
                        ),
                        "returns": ("Namespace.Type", "Namespace.*Type?"),
                        "static": True,
                    },
                    "Namespace.Class.StaticMethodWithNullableParam(Namespace.Type?) -> Namespace.Type": {
                        "name": "StaticMethodWithNullableParam",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.Type?",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": True,
                    },
                    "Namespace.Class.StaticMethodWithOutParam(Namespace.*Type) -> Namespace.Type, Namespace.*Type": {
                        "name": "StaticMethodWithOutParam",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.*Type",
                                "default": False,
                                "out": True,
                            },
                        ),
                        "returns": ("Namespace.Type", "Namespace.*Type"),
                        "static": True,
                    },
                    "Namespace.Class.StaticMethodWithParams0() -> Namespace.Type": {
                        "name": "StaticMethodWithParams0",
                        "declaring_type": "Namespace.Class",
                        "parameters": (),
                        "returns": ("Namespace.Type",),
                        "static": True,
                    },
                    "Namespace.Class.StaticMethodWithParams1(Namespace.Type) -> Namespace.Type": {
                        "name": "StaticMethodWithParams1",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.Type",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": True,
                    },
                    "Namespace.Class.StaticMethodWithParams2(Namespace.Type, Namespace.Type) -> Namespace.Type": {
                        "name": "StaticMethodWithParams2",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.Type",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "param1",
                                "type": "Namespace.Type",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": True,
                    },
                },
                "dunder_methods": {},
                "events": {},
                "nested": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_methods_dunder(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={
                "Namespace.Class.op_Addition(Namespace.Class, Namespace.Class) -> Namespace.Class": CMethod(
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
                    returns=(CType(name="Class", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Class.op_BitwiseAnd(Namespace.Class, Namespace.Class) -> Namespace.Class": CMethod(
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
                    returns=(CType(name="Class", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Class.op_BitwiseOr(Namespace.Class, Namespace.Class) -> Namespace.Class": CMethod(
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
                    returns=(CType(name="Class", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Class.op_Decrement(Namespace.Class) -> Namespace.Class": CMethod(
                    name="op_Decrement",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Class", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Class.op_Division(Namespace.Class, Namespace.Class) -> Namespace.Class": CMethod(
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
                    returns=(CType(name="Class", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Class.op_Equality(Namespace.Class, Namespace.Class) -> Namespace.Type": CMethod(
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
                    returns=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Class.op_ExclusiveOr(Namespace.Class, Namespace.Class) -> Namespace.Class": CMethod(
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
                    returns=(CType(name="Class", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Class.op_False(Namespace.Class) -> Namespace.Type": CMethod(
                    name="op_False",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(name="self", type=CType(name="Class", namespace="Namespace")),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Class.op_GreaterThan(Namespace.Class, Namespace.Class) -> Namespace.Type": CMethod(
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
                    returns=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Class.op_GreaterThanOrEqual(Namespace.Class, Namespace.Class) -> Namespace.Type": CMethod(
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
                    returns=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Class.op_Increment(Namespace.Class) -> Namespace.Class": CMethod(
                    name="op_Increment",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Class", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Class.op_Inequality(Namespace.Class, Namespace.Class) -> Namespace.Type": CMethod(
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
                    returns=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Class.op_LessThan(Namespace.Class, Namespace.Class) -> Namespace.Type": CMethod(
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
                    returns=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Class.op_LessThanOrEqual(Namespace.Class, Namespace.Class) -> Namespace.Type": CMethod(
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
                    returns=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Class.op_LogicalNot(Namespace.Class) -> Namespace.Type": CMethod(
                    name="op_LogicalNot",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Class.op_Modulus(Namespace.Class, Namespace.Class) -> Namespace.Class": CMethod(
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
                    returns=(CType(name="Class", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Class.op_Multiply(Namespace.Class, Namespace.Class) -> Namespace.Class": CMethod(
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
                    returns=(CType(name="Class", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Class.op_OnesComplement(Namespace.Class) -> Namespace.Class": CMethod(
                    name="op_OnesComplement",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Class", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Class.op_Subtraction(Namespace.Class, Namespace.Class) -> Namespace.Class": CMethod(
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
                    returns=(CType(name="Class", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Class.op_True(Namespace.Class) -> Namespace.Type": CMethod(
                    name="op_True",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Class.op_UnaryNegation(Namespace.Class) -> Namespace.Class": CMethod(
                    name="op_UnaryNegation",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Class", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Class.op_UnaryPlus(Namespace.Class) -> Namespace.Class": CMethod(
                    name="op_UnaryPlus",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Class", namespace="Namespace"),),
                    static=True,
                ),
            },
            dunder_methods={
                "Namespace.Class.__add__(Namespace.Class) -> Namespace.Class": CMethod(
                    name="__add__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Class", namespace="Namespace"),),
                ),
                "Namespace.Class.__and__(Namespace.Class) -> Namespace.Class": CMethod(
                    name="__and__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Class", namespace="Namespace"),),
                ),
                "Namespace.Class.__eq__(Namespace.Class) -> Namespace.Type": CMethod(
                    name="__eq__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace.Class.__ge__(Namespace.Class) -> Namespace.Type": CMethod(
                    name="__ge__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace.Class.__gt__(Namespace.Class) -> Namespace.Type": CMethod(
                    name="__gt__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace.Class.__invert__() -> Namespace.Class": CMethod(
                    name="__invert__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(),
                    returns=(CType(name="Class", namespace="Namespace"),),
                ),
                "Namespace.Class.__le__(Namespace.Class) -> Namespace.Type": CMethod(
                    name="__le__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace.Class.__lt__(Namespace.Class) -> Namespace.Type": CMethod(
                    name="__lt__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace.Class.__mod__(Namespace.Class) -> Namespace.Class": CMethod(
                    name="__mod__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Class", namespace="Namespace"),),
                ),
                "Namespace.Class.__mul__(Namespace.Class) -> Namespace.Class": CMethod(
                    name="__mul__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Class", namespace="Namespace"),),
                ),
                "Namespace.Class.__ne__(Namespace.Class) -> Namespace.Type": CMethod(
                    name="__ne__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Type", namespace="System"),),
                ),
                "Namespace.Class.__neg__() -> Namespace.Class": CMethod(
                    name="__neg__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(),
                    returns=(CType(name="Class", namespace="Namespace"),),
                ),
                "Namespace.Class.__or__(Namespace.Class) -> Namespace.Class": CMethod(
                    name="__or__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Class", namespace="Namespace"),),
                ),
                "Namespace.Class.__pos__() -> Namespace.Class": CMethod(
                    name="__pos__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(),
                    returns=(CType(name="Class", namespace="Namespace"),),
                ),
                "Namespace.Class.__sub__(Namespace.Class) -> Namespace.Class": CMethod(
                    name="__sub__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Class", namespace="Namespace"),),
                ),
                "Namespace.Class.__truediv__(Namespace.Class) -> Namespace.Class": CMethod(
                    name="__truediv__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Class", namespace="Namespace"),),
                ),
                "Namespace.Class.__xor__(Namespace.Class) -> Namespace.Class": CMethod(
                    name="__xor__",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Class", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Class", namespace="Namespace"),),
                ),
            },
            events={},
            nested={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "class",
                "name": "Class",
                "namespace": "Namespace",
                "abstract": False,
                "generic_args": (),
                "super_class": None,
                "interfaces": (),
                "fields": {},
                "constructors": {},
                "properties": {},
                "methods": {
                    "Namespace.Class.op_Addition(Namespace.Class, Namespace.Class) -> Namespace.Class": {
                        "name": "op_Addition",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Class",),
                        "static": True,
                    },
                    "Namespace.Class.op_BitwiseAnd(Namespace.Class, Namespace.Class) -> Namespace.Class": {
                        "name": "op_BitwiseAnd",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Class",),
                        "static": True,
                    },
                    "Namespace.Class.op_BitwiseOr(Namespace.Class, Namespace.Class) -> Namespace.Class": {
                        "name": "op_BitwiseOr",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Class",),
                        "static": True,
                    },
                    "Namespace.Class.op_Decrement(Namespace.Class) -> Namespace.Class": {
                        "name": "op_Decrement",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Class",),
                        "static": True,
                    },
                    "Namespace.Class.op_Division(Namespace.Class, Namespace.Class) -> Namespace.Class": {
                        "name": "op_Division",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Class",),
                        "static": True,
                    },
                    "Namespace.Class.op_Equality(Namespace.Class, Namespace.Class) -> Namespace.Type": {
                        "name": "op_Equality",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": True,
                    },
                    "Namespace.Class.op_ExclusiveOr(Namespace.Class, Namespace.Class) -> Namespace.Class": {
                        "name": "op_ExclusiveOr",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Class",),
                        "static": True,
                    },
                    "Namespace.Class.op_False(Namespace.Class) -> Namespace.Type": {
                        "name": "op_False",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": True,
                    },
                    "Namespace.Class.op_GreaterThan(Namespace.Class, Namespace.Class) -> Namespace.Type": {
                        "name": "op_GreaterThan",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": True,
                    },
                    "Namespace.Class.op_GreaterThanOrEqual(Namespace.Class, Namespace.Class) -> Namespace.Type": {
                        "name": "op_GreaterThanOrEqual",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": True,
                    },
                    "Namespace.Class.op_Increment(Namespace.Class) -> Namespace.Class": {
                        "name": "op_Increment",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Class",),
                        "static": True,
                    },
                    "Namespace.Class.op_Inequality(Namespace.Class, Namespace.Class) -> Namespace.Type": {
                        "name": "op_Inequality",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": True,
                    },
                    "Namespace.Class.op_LessThan(Namespace.Class, Namespace.Class) -> Namespace.Type": {
                        "name": "op_LessThan",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": True,
                    },
                    "Namespace.Class.op_LessThanOrEqual(Namespace.Class, Namespace.Class) -> Namespace.Type": {
                        "name": "op_LessThanOrEqual",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": True,
                    },
                    "Namespace.Class.op_LogicalNot(Namespace.Class) -> Namespace.Type": {
                        "name": "op_LogicalNot",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": True,
                    },
                    "Namespace.Class.op_Modulus(Namespace.Class, Namespace.Class) -> Namespace.Class": {
                        "name": "op_Modulus",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Class",),
                        "static": True,
                    },
                    "Namespace.Class.op_Multiply(Namespace.Class, Namespace.Class) -> Namespace.Class": {
                        "name": "op_Multiply",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Class",),
                        "static": True,
                    },
                    "Namespace.Class.op_OnesComplement(Namespace.Class) -> Namespace.Class": {
                        "name": "op_OnesComplement",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Class",),
                        "static": True,
                    },
                    "Namespace.Class.op_Subtraction(Namespace.Class, Namespace.Class) -> Namespace.Class": {
                        "name": "op_Subtraction",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Class",),
                        "static": True,
                    },
                    "Namespace.Class.op_True(Namespace.Class) -> Namespace.Type": {
                        "name": "op_True",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": True,
                    },
                    "Namespace.Class.op_UnaryNegation(Namespace.Class) -> Namespace.Class": {
                        "name": "op_UnaryNegation",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Class",),
                        "static": True,
                    },
                    "Namespace.Class.op_UnaryPlus(Namespace.Class) -> Namespace.Class": {
                        "name": "op_UnaryPlus",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Class",),
                        "static": True,
                    },
                },
                "dunder_methods": {
                    "Namespace.Class.__add__(Namespace.Class) -> Namespace.Class": {
                        "name": "__add__",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Class",),
                        "static": False,
                    },
                    "Namespace.Class.__and__(Namespace.Class) -> Namespace.Class": {
                        "name": "__and__",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Class",),
                        "static": False,
                    },
                    "Namespace.Class.__eq__(Namespace.Class) -> Namespace.Type": {
                        "name": "__eq__",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": False,
                    },
                    "Namespace.Class.__ge__(Namespace.Class) -> Namespace.Type": {
                        "name": "__ge__",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": False,
                    },
                    "Namespace.Class.__gt__(Namespace.Class) -> Namespace.Type": {
                        "name": "__gt__",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": False,
                    },
                    "Namespace.Class.__invert__() -> Namespace.Class": {
                        "name": "__invert__",
                        "declaring_type": "Namespace.Class",
                        "parameters": (),
                        "returns": ("Namespace.Class",),
                        "static": False,
                    },
                    "Namespace.Class.__le__(Namespace.Class) -> Namespace.Type": {
                        "name": "__le__",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": False,
                    },
                    "Namespace.Class.__lt__(Namespace.Class) -> Namespace.Type": {
                        "name": "__lt__",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": False,
                    },
                    "Namespace.Class.__mod__(Namespace.Class) -> Namespace.Class": {
                        "name": "__mod__",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Class",),
                        "static": False,
                    },
                    "Namespace.Class.__mul__(Namespace.Class) -> Namespace.Class": {
                        "name": "__mul__",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Class",),
                        "static": False,
                    },
                    "Namespace.Class.__ne__(Namespace.Class) -> Namespace.Type": {
                        "name": "__ne__",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("System.Type",),
                        "static": False,
                    },
                    "Namespace.Class.__neg__() -> Namespace.Class": {
                        "name": "__neg__",
                        "declaring_type": "Namespace.Class",
                        "parameters": (),
                        "returns": ("Namespace.Class",),
                        "static": False,
                    },
                    "Namespace.Class.__or__(Namespace.Class) -> Namespace.Class": {
                        "name": "__or__",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Class",),
                        "static": False,
                    },
                    "Namespace.Class.__pos__() -> Namespace.Class": {
                        "name": "__pos__",
                        "declaring_type": "Namespace.Class",
                        "parameters": (),
                        "returns": ("Namespace.Class",),
                        "static": False,
                    },
                    "Namespace.Class.__sub__(Namespace.Class) -> Namespace.Class": {
                        "name": "__sub__",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Class",),
                        "static": False,
                    },
                    "Namespace.Class.__truediv__(Namespace.Class) -> Namespace.Class": {
                        "name": "__truediv__",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Class",),
                        "static": False,
                    },
                    "Namespace.Class.__xor__(Namespace.Class) -> Namespace.Class": {
                        "name": "__xor__",
                        "declaring_type": "Namespace.Class",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Class",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Class",),
                        "static": False,
                    },
                },
                "events": {},
                "nested": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_events(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            dunder_methods={},
            events={
                "Namespace.Class.Event -> (System.EventHandler)": CEvent(
                    name="Event",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(name="EventHandler", namespace="System"),
                ),
                "Namespace.Class.EventWithArgs -> (System.EventHandler[System.EventArgs])": CEvent(
                    name="EventWithArgs",
                    declaring_type=CType(name="Class", namespace="Namespace"),
                    type=CType(
                        name="EventHandler",
                        namespace="System",
                        inner=(CType(name="EventArgs", namespace="System"),),
                    ),
                ),
            },
            nested={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "class",
                "name": "Class",
                "namespace": "Namespace",
                "abstract": False,
                "generic_args": (),
                "super_class": None,
                "interfaces": (),
                "fields": {},
                "constructors": {},
                "properties": {},
                "methods": {},
                "dunder_methods": {},
                "events": {
                    "Namespace.Class.Event -> (System.EventHandler)": {
                        "name": "Event",
                        "declaring_type": "Namespace.Class",
                        "type": "System.EventHandler",
                    },
                    "Namespace.Class.EventWithArgs -> (System.EventHandler[System.EventArgs])": {
                        "name": "EventWithArgs",
                        "declaring_type": "Namespace.Class",
                        "type": "System.EventHandler[System.EventArgs]",
                    },
                },
                "nested": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_nested(self) -> None:
        type_def: CClass = CClass(
            name="Class",
            namespace="Namespace",
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            dunder_methods={},
            events={},
            nested={
                "Namespace.INestedInterface": CInterface(
                    name="INestedInterface",
                    namespace="Namespace",
                    generic_args=(),
                    interfaces=(),
                    fields={},
                    properties={},
                    methods={},
                    dunder_methods={},
                    events={},
                    nested={},
                ),
                "Namespace.NestedClass": CClass(
                    name="NestedClass",
                    namespace="Namespace",
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    dunder_methods={},
                    events={},
                    nested={},
                ),
                "Namespace.NestedDelegate": CDelegate(
                    name="NestedDelegate",
                    namespace="Namespace",
                    parameters=(),
                    return_type=CType(name="Void", namespace="System"),
                ),
                "Namespace.NestedEnum": CEnum(name="NestedEnum", namespace="Namespace", fields=()),
                "Namespace.NestedStruct": CStruct(
                    name="NestedStruct",
                    namespace="Namespace",
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    dunder_methods={},
                    events={},
                    nested={},
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
                "abstract": False,
                "generic_args": (),
                "super_class": None,
                "interfaces": (),
                "fields": {},
                "constructors": {},
                "properties": {},
                "methods": {},
                "dunder_methods": {},
                "events": {},
                "nested": {
                    "Namespace.INestedInterface": {
                        "type": "interface",
                        "name": "INestedInterface",
                        "namespace": "Namespace",
                        "generic_args": (),
                        "interfaces": (),
                        "fields": {},
                        "properties": {},
                        "methods": {},
                        "dunder_methods": {},
                        "events": {},
                        "nested": {},
                    },
                    "Namespace.NestedClass": {
                        "type": "class",
                        "name": "NestedClass",
                        "namespace": "Namespace",
                        "abstract": False,
                        "generic_args": (),
                        "super_class": None,
                        "interfaces": (),
                        "fields": {},
                        "constructors": {},
                        "properties": {},
                        "methods": {},
                        "dunder_methods": {},
                        "events": {},
                        "nested": {},
                    },
                    "Namespace.NestedDelegate": {
                        "type": "delegate",
                        "name": "NestedDelegate",
                        "namespace": "Namespace",
                        "parameters": (),
                        "return_type": "System.Void",
                    },
                    "Namespace.NestedEnum": {
                        "type": "enum",
                        "name": "NestedEnum",
                        "namespace": "Namespace",
                        "fields": (),
                    },
                    "Namespace.NestedStruct": {
                        "type": "struct",
                        "name": "NestedStruct",
                        "namespace": "Namespace",
                        "abstract": False,
                        "generic_args": (),
                        "super_class": None,
                        "interfaces": (),
                        "fields": {},
                        "constructors": {},
                        "properties": {},
                        "methods": {},
                        "dunder_methods": {},
                        "events": {},
                        "nested": {},
                    },
                },
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_compare(self) -> None:
        struct0: CClass = CClass(
            name="ClassA",
            namespace="Namespace",
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            dunder_methods={},
            events={},
            nested={},
        )
        struct1: CClass = CClass(
            name="ClassB",
            namespace="Namespace",
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            dunder_methods={},
            events={},
            nested={},
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
                abstract=False,
                generic_args=(),
                super_class=None,
                interfaces=(),
                fields={},
                constructors={},
                properties={},
                methods={},
                dunder_methods={},
                events={},
                nested={},
            ),
            CClass(
                name="ClassB",
                namespace="Namespace",
                abstract=False,
                generic_args=(),
                super_class=None,
                interfaces=(),
                fields={},
                constructors={},
                properties={},
                methods={},
                dunder_methods={},
                events={},
                nested={},
            ),
            CClass(
                name="ClassC",
                namespace="Namespace",
                abstract=False,
                generic_args=(),
                super_class=None,
                interfaces=(),
                fields={},
                constructors={},
                properties={},
                methods={},
                dunder_methods={},
                events={},
                nested={},
            ),
            CClass(
                name="ClassD",
                namespace="Namespace",
                abstract=False,
                generic_args=(),
                super_class=None,
                interfaces=(),
                fields={},
                constructors={},
                properties={},
                methods={},
                dunder_methods={},
                events={},
                nested={},
            ),
        )
        unordered: MutableSequence[CClass] = list(ordered)
        random.shuffle(unordered)

        self.assertSequenceEqual(ordered, sorted(unordered))


class TestCStruct(TestBase):
    def test_from_info_generic(self) -> None:
        type_info: TypeInfo = self.get_type("StructWithGeneric")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCStruct(
            struct=cast(CStruct, type_def),
            name="StructWithGeneric",
            namespace="TestLib",
            abstract=False,
            generic_args=(CType(name="T", namespace="TestLib", generic=True),),
            super_class=CType(name="ValueType", namespace="System"),
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={
                "System.Object.Equals(System.Object) -> System.Boolean": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Object.GetHashCode() -> System.Int32": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "System.Object.GetType() -> System.Type": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Type", namespace="System"),),
                ),
                "System.Object.ToString() -> System.String": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="String", namespace="System"),),
                ),
            },
            dunder_methods={},
            events={},
            nested={},
        )

    def test_from_info_generic_multi(self) -> None:
        type_info: TypeInfo = self.get_type("StructWithMultiGeneric")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCStruct(
            struct=cast(CStruct, type_def),
            name="StructWithMultiGeneric",
            namespace="TestLib",
            abstract=False,
            generic_args=(
                CType(name="U", namespace="TestLib", generic=True),
                CType(name="V", namespace="TestLib", generic=True),
            ),
            super_class=CType(name="ValueType", namespace="System"),
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={
                "System.Object.Equals(System.Object) -> System.Boolean": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Object.GetHashCode() -> System.Int32": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "System.Object.GetType() -> System.Type": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Type", namespace="System"),),
                ),
                "System.Object.ToString() -> System.String": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="String", namespace="System"),),
                ),
            },
            dunder_methods={},
            events={},
            nested={},
        )

    def test_from_info_interfaces(self) -> None:
        type_info: TypeInfo = self.get_type("StructWithInterface")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCStruct(
            struct=cast(CStruct, type_def),
            name="StructWithInterface",
            namespace="TestLib",
            abstract=False,
            generic_args=(),
            super_class=CType(name="ValueType", namespace="System"),
            interfaces=(
                CType(
                    name="IEquatable",
                    namespace="System",
                    inner=(CType(name="StructWithInterface", namespace="TestLib"),),
                ),
            ),
            fields={},
            constructors={},
            properties={},
            methods={
                "System.Object.Equals(System.Object) -> System.Boolean": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "System.IEquatable[TestLib.StructWithInterface].Equals(TestLib.StructWithInterface) -> System.Boolean": CMethod(
                    name="Equals",
                    declaring_type=CType(
                        name="IEquatable",
                        namespace="System",
                        inner=(CType(name="StructWithInterface", namespace="TestLib"),),
                    ),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithInterface", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib.StructWithInterface.Equals(TestLib.StructWithInterface?) -> System.Boolean": CMethod(
                    name="Equals",
                    declaring_type=CType(name="StructWithInterface", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(
                                name="StructWithInterface",
                                namespace="TestLib",
                                nullable=True,
                            ),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Object.GetHashCode() -> System.Int32": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "System.Object.GetType() -> System.Type": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Type", namespace="System"),),
                ),
                "System.Object.ToString() -> System.String": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="String", namespace="System"),),
                ),
                "TestLib.StructWithInterface.op_Equality(TestLib.StructWithInterface, TestLib.StructWithInterface) -> System.Boolean": CMethod(
                    name="op_Equality",
                    declaring_type=CType(name="StructWithInterface", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="left",
                            type=CType(name="StructWithInterface", namespace="TestLib"),
                        ),
                        CParameter(
                            name="right",
                            type=CType(name="StructWithInterface", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib.StructWithInterface.op_Inequality(TestLib.StructWithInterface, TestLib.StructWithInterface) -> System.Boolean": CMethod(
                    name="op_Inequality",
                    declaring_type=CType(name="StructWithInterface", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="left",
                            type=CType(name="StructWithInterface", namespace="TestLib"),
                        ),
                        CParameter(
                            name="right",
                            type=CType(name="StructWithInterface", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
            },
            dunder_methods={
                "TestLib.StructWithInterface.__eq__(TestLib.StructWithInterface) -> System.Boolean": CMethod(
                    name="__eq__",
                    declaring_type=CType(name="StructWithInterface", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithInterface", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib.StructWithInterface.__ne__(TestLib.StructWithInterface) -> System.Boolean": CMethod(
                    name="__ne__",
                    declaring_type=CType(name="StructWithInterface", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithInterface", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
            },
            events={},
            nested={},
        )

    def test_from_info_fields(self) -> None:
        type_info: TypeInfo = self.get_type("StructWithFields")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCStruct(
            struct=cast(CStruct, type_def),
            name="StructWithFields",
            namespace="TestLib",
            abstract=False,
            generic_args=(),
            super_class=CType(name="ValueType", namespace="System"),
            interfaces=(),
            fields={
                "TestLib.StructWithFields.InstanceFieldA": CField(
                    name="InstanceFieldA",
                    declaring_type=CType(name="StructWithFields", namespace="TestLib"),
                    returns=CType(name="Int32", namespace="System"),
                ),
                "TestLib.StructWithFields.InstanceFieldB": CField(
                    name="InstanceFieldB",
                    declaring_type=CType(name="StructWithFields", namespace="TestLib"),
                    returns=CType(name="Int32", namespace="System"),
                ),
                "TestLib.StructWithFields.InstanceFieldC": CField(
                    name="InstanceFieldC",
                    declaring_type=CType(name="StructWithFields", namespace="TestLib"),
                    returns=CType(name="Int32", namespace="System"),
                ),
                "TestLib.StructWithFields.StaticFieldA": CField(
                    name="StaticFieldA",
                    declaring_type=CType(name="StructWithFields", namespace="TestLib"),
                    returns=CType(name="Int32", namespace="System"),
                    static=True,
                ),
                "TestLib.StructWithFields.StaticFieldB": CField(
                    name="StaticFieldB",
                    declaring_type=CType(name="StructWithFields", namespace="TestLib"),
                    returns=CType(name="Int32", namespace="System"),
                    static=True,
                ),
                "TestLib.StructWithFields.StaticFieldC": CField(
                    name="StaticFieldC",
                    declaring_type=CType(name="StructWithFields", namespace="TestLib"),
                    returns=CType(name="Int32", namespace="System"),
                    static=True,
                ),
            },
            constructors={
                "TestLib.StructWithFields.__init__()": CConstructor(
                    declaring_type=CType(name="StructWithFields", namespace="TestLib"),
                    parameters=(),
                ),
            },
            properties={},
            methods={
                "System.Object.Equals(System.Object) -> System.Boolean": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Object.GetHashCode() -> System.Int32": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "System.Object.GetType() -> System.Type": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Type", namespace="System"),),
                ),
                "System.Object.ToString() -> System.String": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="String", namespace="System"),),
                ),
            },
            dunder_methods={},
            events={},
            nested={},
        )

    def test_from_info_constructors(self) -> None:
        type_info: TypeInfo = self.get_type("StructWithConstructors")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCStruct(
            struct=cast(CStruct, type_def),
            name="StructWithConstructors",
            namespace="TestLib",
            abstract=False,
            generic_args=(),
            super_class=CType(name="ValueType", namespace="System"),
            interfaces=(),
            fields={},
            constructors={
                "TestLib.StructWithConstructors.__init__()": CConstructor(
                    declaring_type=CType(name="StructWithConstructors", namespace="TestLib"),
                    parameters=(),
                ),
                "TestLib.StructWithConstructors.__init__(System.Int32)": CConstructor(
                    declaring_type=CType(name="StructWithConstructors", namespace="TestLib"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                    ),
                ),
                "TestLib.StructWithConstructors.__init__(System.Int32, System.Int32)": CConstructor(
                    declaring_type=CType(name="StructWithConstructors", namespace="TestLib"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                        CParameter(name="param1", type=CType(name="Int32", namespace="System")),
                    ),
                ),
                "TestLib.StructWithConstructors.__init__(System.Int32, System.Int32, System.Int32)": CConstructor(
                    declaring_type=CType(name="StructWithConstructors", namespace="TestLib"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                        CParameter(name="param1", type=CType(name="Int32", namespace="System")),
                        CParameter(name="param2", type=CType(name="Int32", namespace="System")),
                    ),
                ),
            },
            properties={},
            methods={
                "System.Object.Equals(System.Object) -> System.Boolean": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Object.GetHashCode() -> System.Int32": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "System.Object.GetType() -> System.Type": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Type", namespace="System"),),
                ),
                "System.Object.ToString() -> System.String": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="String", namespace="System"),),
                ),
            },
            dunder_methods={},
            events={},
            nested={},
        )

    def test_from_info_properties(self) -> None:
        type_info: TypeInfo = self.get_type("StructWithProperties")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCStruct(
            struct=cast(CStruct, type_def),
            name="StructWithProperties",
            namespace="TestLib",
            abstract=False,
            generic_args=(),
            super_class=CType(name="ValueType", namespace="System"),
            interfaces=(),
            fields={},
            constructors={},
            properties={
                "TestLib.StructWithProperties.InstanceProperty0": CProperty(
                    name="InstanceProperty0",
                    declaring_type=CType(name="StructWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                ),
                "TestLib.StructWithProperties.InstanceProperty1": CProperty(
                    name="InstanceProperty1",
                    declaring_type=CType(name="StructWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                ),
                "TestLib.StructWithProperties.InstanceProperty2": CProperty(
                    name="InstanceProperty2",
                    declaring_type=CType(name="StructWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                ),
                "TestLib.StructWithProperties.InstanceReadOnlyProperty0": CProperty(
                    name="InstanceReadOnlyProperty0",
                    declaring_type=CType(name="StructWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                ),
                "TestLib.StructWithProperties.InstanceReadOnlyProperty1": CProperty(
                    name="InstanceReadOnlyProperty1",
                    declaring_type=CType(name="StructWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                ),
                "TestLib.StructWithProperties.InstanceReadOnlyProperty2": CProperty(
                    name="InstanceReadOnlyProperty2",
                    declaring_type=CType(name="StructWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                ),
                "TestLib.StructWithProperties.StaticProperty0": CProperty(
                    name="StaticProperty0",
                    declaring_type=CType(name="StructWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                    static=True,
                ),
                "TestLib.StructWithProperties.StaticProperty1": CProperty(
                    name="StaticProperty1",
                    declaring_type=CType(name="StructWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                    static=True,
                ),
                "TestLib.StructWithProperties.StaticProperty2": CProperty(
                    name="StaticProperty2",
                    declaring_type=CType(name="StructWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                    static=True,
                ),
                "TestLib.StructWithProperties.StaticReadOnlyProperty0": CProperty(
                    name="StaticReadOnlyProperty0",
                    declaring_type=CType(name="StructWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
                "TestLib.StructWithProperties.StaticReadOnlyProperty1": CProperty(
                    name="StaticReadOnlyProperty1",
                    declaring_type=CType(name="StructWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
                "TestLib.StructWithProperties.StaticReadOnlyProperty2": CProperty(
                    name="StaticReadOnlyProperty2",
                    declaring_type=CType(name="StructWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
            },
            methods={
                "System.Object.Equals(System.Object) -> System.Boolean": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Object.GetHashCode() -> System.Int32": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "System.Object.GetType() -> System.Type": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Type", namespace="System"),),
                ),
                "System.Object.ToString() -> System.String": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="String", namespace="System"),),
                ),
            },
            dunder_methods={},
            events={},
            nested={},
        )

    def test_from_info_methods(self) -> None:
        type_info: TypeInfo = self.get_type("StructWithMethods")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCStruct(
            struct=cast(CStruct, type_def),
            name="StructWithMethods",
            namespace="TestLib",
            abstract=False,
            generic_args=(),
            super_class=CType(name="ValueType", namespace="System"),
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={
                "System.Object.Equals(System.Object) -> System.Boolean": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Object.GetHashCode() -> System.Int32": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "System.Object.GetType() -> System.Type": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Type", namespace="System"),),
                ),
                "TestLib.StructWithMethods.InstanceMethodWithDefaultParam(System.Int32) -> System.Int32": CMethod(
                    name="InstanceMethodWithDefaultParam",
                    declaring_type=CType(name="StructWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System"),
                            default=True,
                        ),
                    ),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib.StructWithMethods.InstanceMethodWithNullableDefaultParam(System.Int32?) -> System.Int32": CMethod(
                    name="InstanceMethodWithNullableDefaultParam",
                    declaring_type=CType(name="StructWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System", nullable=True),
                            default=True,
                        ),
                    ),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib.StructWithMethods.InstanceMethodWithNullableOutParam(System.*Int32?) -> System.Int32, System.*Int32?": CMethod(
                    name="InstanceMethodWithNullableOutParam",
                    declaring_type=CType(name="StructWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(
                                name="Int32", namespace="System", reference=True, nullable=True
                            ),
                            out=True,
                        ),
                    ),
                    returns=(
                        CType(name="Int32", namespace="System"),
                        CType(name="Int32", namespace="System", reference=True, nullable=True),
                    ),
                ),
                "TestLib.StructWithMethods.InstanceMethodWithNullableParam(System.Int32?) -> System.Int32": CMethod(
                    name="InstanceMethodWithNullableParam",
                    declaring_type=CType(name="StructWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System", nullable=True),
                        ),
                    ),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib.StructWithMethods.InstanceMethodWithOutParam(System.*Int32) -> System.Int32, System.*Int32": CMethod(
                    name="InstanceMethodWithOutParam",
                    declaring_type=CType(name="StructWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System", reference=True),
                            out=True,
                        ),
                    ),
                    returns=(
                        CType(name="Int32", namespace="System"),
                        CType(name="Int32", namespace="System", reference=True),
                    ),
                ),
                "TestLib.StructWithMethods.InstanceMethodWithParams0() -> System.Int32": CMethod(
                    name="InstanceMethodWithParams0",
                    declaring_type=CType(name="StructWithMethods", namespace="TestLib"),
                    parameters=(),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib.StructWithMethods.InstanceMethodWithParams1(System.Int32) -> System.Int32": CMethod(
                    name="InstanceMethodWithParams1",
                    declaring_type=CType(name="StructWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                    ),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib.StructWithMethods.InstanceMethodWithParams2(System.Int32, System.Int32) -> System.Int32": CMethod(
                    name="InstanceMethodWithParams2",
                    declaring_type=CType(name="StructWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                        CParameter(name="param1", type=CType(name="Int32", namespace="System")),
                    ),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib.StructWithMethods.StaticMethodWithDefaultParam(System.Int32) -> System.Int32": CMethod(
                    name="StaticMethodWithDefaultParam",
                    declaring_type=CType(name="StructWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System"),
                            default=True,
                        ),
                    ),
                    returns=(CType(name="Int32", namespace="System"),),
                    static=True,
                ),
                "TestLib.StructWithMethods.StaticMethodWithNullableDefaultParam(System.Int32?) -> System.Int32": CMethod(
                    name="StaticMethodWithNullableDefaultParam",
                    declaring_type=CType(name="StructWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System", nullable=True),
                            default=True,
                        ),
                    ),
                    returns=(CType(name="Int32", namespace="System"),),
                    static=True,
                ),
                "TestLib.StructWithMethods.StaticMethodWithNullableOutParam(System.*Int32?) -> System.Int32, System.*Int32?": CMethod(
                    name="StaticMethodWithNullableOutParam",
                    declaring_type=CType(name="StructWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(
                                name="Int32", namespace="System", reference=True, nullable=True
                            ),
                            out=True,
                        ),
                    ),
                    returns=(
                        CType(name="Int32", namespace="System"),
                        CType(name="Int32", namespace="System", reference=True, nullable=True),
                    ),
                    static=True,
                ),
                "TestLib.StructWithMethods.StaticMethodWithNullableParam(System.Int32?) -> System.Int32": CMethod(
                    name="StaticMethodWithNullableParam",
                    declaring_type=CType(name="StructWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System", nullable=True),
                        ),
                    ),
                    returns=(CType(name="Int32", namespace="System"),),
                    static=True,
                ),
                "TestLib.StructWithMethods.StaticMethodWithOutParam(System.*Int32) -> System.Int32, System.*Int32": CMethod(
                    name="StaticMethodWithOutParam",
                    declaring_type=CType(name="StructWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System", reference=True),
                            out=True,
                        ),
                    ),
                    returns=(
                        CType(name="Int32", namespace="System"),
                        CType(name="Int32", namespace="System", reference=True),
                    ),
                    static=True,
                ),
                "TestLib.StructWithMethods.StaticMethodWithParams0() -> System.Int32": CMethod(
                    name="StaticMethodWithParams0",
                    declaring_type=CType(name="StructWithMethods", namespace="TestLib"),
                    parameters=(),
                    returns=(CType(name="Int32", namespace="System"),),
                    static=True,
                ),
                "TestLib.StructWithMethods.StaticMethodWithParams1(System.Int32) -> System.Int32": CMethod(
                    name="StaticMethodWithParams1",
                    declaring_type=CType(name="StructWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                    ),
                    returns=(CType(name="Int32", namespace="System"),),
                    static=True,
                ),
                "TestLib.StructWithMethods.StaticMethodWithParams2(System.Int32, System.Int32) -> System.Int32": CMethod(
                    name="StaticMethodWithParams2",
                    declaring_type=CType(name="StructWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                        CParameter(name="param1", type=CType(name="Int32", namespace="System")),
                    ),
                    returns=(CType(name="Int32", namespace="System"),),
                    static=True,
                ),
                "System.Object.ToString() -> System.String": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="String", namespace="System"),),
                ),
            },
            dunder_methods={},
            events={},
            nested={},
        )

    def test_from_info_methods_dunder(self) -> None:
        type_info: TypeInfo = self.get_type("StructWithOperatorMethods")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCStruct(
            struct=cast(CStruct, type_def),
            name="StructWithOperatorMethods",
            namespace="TestLib",
            abstract=False,
            generic_args=(),
            super_class=CType(name="ValueType", namespace="System"),
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={
                "System.Object.Equals(System.Object) -> System.Boolean": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(
                            name="obj",
                            type=CType(name="Object", namespace="System"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Object.GetHashCode() -> System.Int32": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "System.Object.GetType() -> System.Type": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Type", namespace="System"),),
                ),
                "System.Object.ToString() -> System.String": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="String", namespace="System"),),
                ),
                "TestLib.StructWithOperatorMethods.op_Addition(TestLib.StructWithOperatorMethods, TestLib.StructWithOperatorMethods) -> TestLib.StructWithOperatorMethods": CMethod(
                    name="op_Addition",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.StructWithOperatorMethods.op_BitwiseAnd(TestLib.StructWithOperatorMethods, TestLib.StructWithOperatorMethods) -> TestLib.StructWithOperatorMethods": CMethod(
                    name="op_BitwiseAnd",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.StructWithOperatorMethods.op_BitwiseOr(TestLib.StructWithOperatorMethods, TestLib.StructWithOperatorMethods) -> TestLib.StructWithOperatorMethods": CMethod(
                    name="op_BitwiseOr",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.StructWithOperatorMethods.op_Decrement(TestLib.StructWithOperatorMethods) -> TestLib.StructWithOperatorMethods": CMethod(
                    name="op_Decrement",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.StructWithOperatorMethods.op_Division(TestLib.StructWithOperatorMethods, TestLib.StructWithOperatorMethods) -> TestLib.StructWithOperatorMethods": CMethod(
                    name="op_Division",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.StructWithOperatorMethods.op_Equality(TestLib.StructWithOperatorMethods, TestLib.StructWithOperatorMethods) -> System.Boolean": CMethod(
                    name="op_Equality",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib.StructWithOperatorMethods.op_ExclusiveOr(TestLib.StructWithOperatorMethods, TestLib.StructWithOperatorMethods) -> TestLib.StructWithOperatorMethods": CMethod(
                    name="op_ExclusiveOr",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.StructWithOperatorMethods.op_False(TestLib.StructWithOperatorMethods) -> System.Boolean": CMethod(
                    name="op_False",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib.StructWithOperatorMethods.op_GreaterThan(TestLib.StructWithOperatorMethods, TestLib.StructWithOperatorMethods) -> System.Boolean": CMethod(
                    name="op_GreaterThan",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib.StructWithOperatorMethods.op_GreaterThanOrEqual(TestLib.StructWithOperatorMethods, TestLib.StructWithOperatorMethods) -> System.Boolean": CMethod(
                    name="op_GreaterThanOrEqual",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib.StructWithOperatorMethods.op_Increment(TestLib.StructWithOperatorMethods) -> TestLib.StructWithOperatorMethods": CMethod(
                    name="op_Increment",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.StructWithOperatorMethods.op_Inequality(TestLib.StructWithOperatorMethods, TestLib.StructWithOperatorMethods) -> System.Boolean": CMethod(
                    name="op_Inequality",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib.StructWithOperatorMethods.op_LessThan(TestLib.StructWithOperatorMethods, TestLib.StructWithOperatorMethods) -> System.Boolean": CMethod(
                    name="op_LessThan",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib.StructWithOperatorMethods.op_LessThanOrEqual(TestLib.StructWithOperatorMethods, TestLib.StructWithOperatorMethods) -> System.Boolean": CMethod(
                    name="op_LessThanOrEqual",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib.StructWithOperatorMethods.op_LogicalNot(TestLib.StructWithOperatorMethods) -> System.Boolean": CMethod(
                    name="op_LogicalNot",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib.StructWithOperatorMethods.op_Modulus(TestLib.StructWithOperatorMethods, TestLib.StructWithOperatorMethods) -> TestLib.StructWithOperatorMethods": CMethod(
                    name="op_Modulus",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.StructWithOperatorMethods.op_Multiply(TestLib.StructWithOperatorMethods, TestLib.StructWithOperatorMethods) -> TestLib.StructWithOperatorMethods": CMethod(
                    name="op_Multiply",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.StructWithOperatorMethods.op_OnesComplement(TestLib.StructWithOperatorMethods) -> TestLib.StructWithOperatorMethods": CMethod(
                    name="op_OnesComplement",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.StructWithOperatorMethods.op_Subtraction(TestLib.StructWithOperatorMethods, TestLib.StructWithOperatorMethods) -> TestLib.StructWithOperatorMethods": CMethod(
                    name="op_Subtraction",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.StructWithOperatorMethods.op_True(TestLib.StructWithOperatorMethods) -> System.Boolean": CMethod(
                    name="op_True",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib.StructWithOperatorMethods.op_UnaryNegation(TestLib.StructWithOperatorMethods) -> TestLib.StructWithOperatorMethods": CMethod(
                    name="op_UnaryNegation",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.StructWithOperatorMethods.op_UnaryPlus(TestLib.StructWithOperatorMethods) -> TestLib.StructWithOperatorMethods": CMethod(
                    name="op_UnaryPlus",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
            },
            dunder_methods={
                "TestLib.StructWithOperatorMethods.__add__(TestLib.StructWithOperatorMethods) -> TestLib.StructWithOperatorMethods": CMethod(
                    name="__add__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib.StructWithOperatorMethods.__and__(TestLib.StructWithOperatorMethods) -> TestLib.StructWithOperatorMethods": CMethod(
                    name="__and__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib.StructWithOperatorMethods.__eq__(TestLib.StructWithOperatorMethods) -> System.Boolean": CMethod(
                    name="__eq__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib.StructWithOperatorMethods.__ge__(TestLib.StructWithOperatorMethods) -> System.Boolean": CMethod(
                    name="__ge__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib.StructWithOperatorMethods.__gt__(TestLib.StructWithOperatorMethods) -> System.Boolean": CMethod(
                    name="__gt__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib.StructWithOperatorMethods.__invert__() -> TestLib.StructWithOperatorMethods": CMethod(
                    name="__invert__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(),
                    returns=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib.StructWithOperatorMethods.__le__(TestLib.StructWithOperatorMethods) -> System.Boolean": CMethod(
                    name="__le__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib.StructWithOperatorMethods.__lt__(TestLib.StructWithOperatorMethods) -> System.Boolean": CMethod(
                    name="__lt__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib.StructWithOperatorMethods.__mod__(TestLib.StructWithOperatorMethods) -> TestLib.StructWithOperatorMethods": CMethod(
                    name="__mod__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib.StructWithOperatorMethods.__mul__(TestLib.StructWithOperatorMethods) -> TestLib.StructWithOperatorMethods": CMethod(
                    name="__mul__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib.StructWithOperatorMethods.__ne__(TestLib.StructWithOperatorMethods) -> System.Boolean": CMethod(
                    name="__ne__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib.StructWithOperatorMethods.__neg__() -> TestLib.StructWithOperatorMethods": CMethod(
                    name="__neg__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(),
                    returns=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib.StructWithOperatorMethods.__or__(TestLib.StructWithOperatorMethods) -> TestLib.StructWithOperatorMethods": CMethod(
                    name="__or__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib.StructWithOperatorMethods.__pos__() -> TestLib.StructWithOperatorMethods": CMethod(
                    name="__pos__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(),
                    returns=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib.StructWithOperatorMethods.__sub__(TestLib.StructWithOperatorMethods) -> TestLib.StructWithOperatorMethods": CMethod(
                    name="__sub__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib.StructWithOperatorMethods.__truediv__(TestLib.StructWithOperatorMethods) -> TestLib.StructWithOperatorMethods": CMethod(
                    name="__truediv__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib.StructWithOperatorMethods.__xor__(TestLib.StructWithOperatorMethods) -> TestLib.StructWithOperatorMethods": CMethod(
                    name="__xor__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                ),
            },
            events={},
            nested={},
        )

    def test_from_info_events(self) -> None:
        type_info: TypeInfo = self.get_type("StructWithEvents")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCStruct(
            struct=cast(CStruct, type_def),
            name="StructWithEvents",
            namespace="TestLib",
            abstract=False,
            generic_args=(),
            super_class=CType(name="ValueType", namespace="System"),
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={
                "System.Object.Equals(System.Object) -> System.Boolean": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Object.GetHashCode() -> System.Int32": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "System.Object.GetType() -> System.Type": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Type", namespace="System"),),
                ),
                "System.Object.ToString() -> System.String": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="String", namespace="System"),),
                ),
            },
            dunder_methods={},
            events={
                "TestLib.StructWithEvents.Event -> (System.EventHandler)": CEvent(
                    name="Event",
                    declaring_type=CType(name="StructWithEvents", namespace="TestLib"),
                    type=CType(name="EventHandler", namespace="System"),
                ),
                "TestLib.StructWithEvents.EventWithArgs -> (System.EventHandler[System.EventArgs])": CEvent(
                    name="EventWithArgs",
                    declaring_type=CType(name="StructWithEvents", namespace="TestLib"),
                    type=CType(
                        name="EventHandler",
                        namespace="System",
                        inner=(CType(name="EventArgs", namespace="System"),),
                    ),
                ),
            },
            nested={},
        )

    def test_from_info_nested(self) -> None:
        type_info: TypeInfo = self.get_type("StructWithNested")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCStruct(
            struct=cast(CStruct, type_def),
            name="StructWithNested",
            namespace="TestLib",
            abstract=False,
            generic_args=(),
            super_class=CType(name="ValueType", namespace="System"),
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={
                "System.Object.Equals(System.Object) -> System.Boolean": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Object.GetHashCode() -> System.Int32": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "System.Object.GetType() -> System.Type": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="Type", namespace="System"),),
                ),
                "System.Object.ToString() -> System.String": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    returns=(CType(name="String", namespace="System"),),
                ),
            },
            dunder_methods={},
            events={},
            nested={
                "TestLib.INestedInterface": CInterface(
                    name="INestedInterface",
                    namespace="TestLib",
                    generic_args=(),
                    interfaces=(),
                    fields={},
                    properties={},
                    methods={},
                    dunder_methods={},
                    events={},
                    nested={},
                ),
                "TestLib.NestedClass": CClass(
                    name="NestedClass",
                    namespace="TestLib",
                    abstract=False,
                    generic_args=(),
                    super_class=CType(name="Object", namespace="System"),
                    interfaces=(),
                    fields={},
                    constructors={
                        "TestLib.NestedClass.__init__()": CConstructor(
                            declaring_type=CType(name="NestedClass", namespace="TestLib"),
                            parameters=(),
                        )
                    },
                    properties={},
                    methods={
                        "System.Object.Equals(System.Object) -> System.Boolean": CMethod(
                            name="Equals",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(
                                CParameter(
                                    name="obj",
                                    type=CType(name="Object", namespace="System"),
                                ),
                            ),
                            returns=(CType(name="Boolean", namespace="System"),),
                        ),
                        "System.Object.GetHashCode() -> System.Int32": CMethod(
                            name="GetHashCode",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            returns=(CType(name="Int32", namespace="System"),),
                        ),
                        "System.Object.GetType() -> System.Type": CMethod(
                            name="GetType",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            returns=(CType(name="Type", namespace="System"),),
                        ),
                        "System.Object.ToString() -> System.String": CMethod(
                            name="ToString",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            returns=(CType(name="String", namespace="System"),),
                        ),
                    },
                    dunder_methods={},
                    events={},
                    nested={},
                ),
                "TestLib.NestedDelegate": CDelegate(
                    name="NestedDelegate",
                    namespace="TestLib",
                    parameters=(),
                    return_type=CType(name="Void", namespace="System"),
                ),
                "TestLib.NestedEnum": CEnum(name="NestedEnum", namespace="TestLib", fields=()),
                "TestLib.NestedStruct": CStruct(
                    name="NestedStruct",
                    namespace="TestLib",
                    abstract=False,
                    generic_args=(),
                    super_class=CType(name="ValueType", namespace="System"),
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={
                        "System.Object.Equals(System.Object) -> System.Boolean": CMethod(
                            name="Equals",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(
                                CParameter(
                                    name="obj",
                                    type=CType(name="Object", namespace="System"),
                                ),
                            ),
                            returns=(CType(name="Boolean", namespace="System"),),
                        ),
                        "System.Object.GetHashCode() -> System.Int32": CMethod(
                            name="GetHashCode",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            returns=(CType(name="Int32", namespace="System"),),
                        ),
                        "System.Object.GetType() -> System.Type": CMethod(
                            name="GetType",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            returns=(CType(name="Type", namespace="System"),),
                        ),
                        "System.Object.ToString() -> System.String": CMethod(
                            name="ToString",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            returns=(CType(name="String", namespace="System"),),
                        ),
                    },
                    dunder_methods={},
                    events={},
                    nested={},
                ),
            },
        )

    def test_json_generic(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            abstract=False,
            generic_args=(CType(name="T", namespace="Namespace", generic=True),),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            dunder_methods={},
            events={},
            nested={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "struct",
                "name": "Struct",
                "namespace": "Namespace",
                "abstract": False,
                "generic_args": ("Namespace.$T",),
                "super_class": None,
                "interfaces": (),
                "fields": {},
                "constructors": {},
                "properties": {},
                "methods": {},
                "dunder_methods": {},
                "events": {},
                "nested": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_generic_multi(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            abstract=False,
            generic_args=(
                CType(name="U", namespace="Namespace", generic=True),
                CType(name="V", namespace="Namespace", generic=True),
            ),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            dunder_methods={},
            events={},
            nested={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "struct",
                "name": "Struct",
                "namespace": "Namespace",
                "abstract": False,
                "generic_args": ("Namespace.$U", "Namespace.$V"),
                "super_class": None,
                "interfaces": (),
                "fields": {},
                "constructors": {},
                "properties": {},
                "methods": {},
                "dunder_methods": {},
                "events": {},
                "nested": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_interfaces(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
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
            dunder_methods={},
            events={},
            nested={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "struct",
                "name": "Struct",
                "namespace": "Namespace",
                "abstract": False,
                "generic_args": (),
                "super_class": None,
                "interfaces": ("Namespace.InterfaceA", "Namespace.InterfaceB"),
                "fields": {},
                "constructors": {},
                "properties": {},
                "methods": {},
                "dunder_methods": {},
                "events": {},
                "nested": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_fields(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={
                "Namespace.Struct.InstanceFieldA": CField(
                    name="InstanceFieldA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    returns=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace.Struct.InstanceFieldB": CField(
                    name="InstanceFieldB",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    returns=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace.Struct.InstanceFieldC": CField(
                    name="InstanceFieldC",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    returns=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace.Struct.StaticFieldA": CField(
                    name="StaticFieldA",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    returns=CType(name="Type", namespace="Namespace"),
                    static=True,
                ),
                "Namespace.Struct.StaticFieldB": CField(
                    name="StaticFieldB",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    returns=CType(name="Type", namespace="Namespace"),
                    static=True,
                ),
                "Namespace.Struct.StaticFieldC": CField(
                    name="StaticFieldC",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    returns=CType(name="Type", namespace="Namespace"),
                    static=True,
                ),
            },
            constructors={},
            properties={},
            methods={},
            dunder_methods={},
            events={},
            nested={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "struct",
                "name": "Struct",
                "namespace": "Namespace",
                "abstract": False,
                "generic_args": (),
                "super_class": None,
                "interfaces": (),
                "fields": {
                    "Namespace.Struct.InstanceFieldA": {
                        "name": "InstanceFieldA",
                        "declaring_type": "Namespace.Struct",
                        "returns": "Namespace.Type",
                        "static": False,
                    },
                    "Namespace.Struct.InstanceFieldB": {
                        "name": "InstanceFieldB",
                        "declaring_type": "Namespace.Struct",
                        "returns": "Namespace.Type",
                        "static": False,
                    },
                    "Namespace.Struct.InstanceFieldC": {
                        "name": "InstanceFieldC",
                        "declaring_type": "Namespace.Struct",
                        "returns": "Namespace.Type",
                        "static": False,
                    },
                    "Namespace.Struct.StaticFieldA": {
                        "name": "StaticFieldA",
                        "declaring_type": "Namespace.Struct",
                        "returns": "Namespace.Type",
                        "static": True,
                    },
                    "Namespace.Struct.StaticFieldB": {
                        "name": "StaticFieldB",
                        "declaring_type": "Namespace.Struct",
                        "returns": "Namespace.Type",
                        "static": True,
                    },
                    "Namespace.Struct.StaticFieldC": {
                        "name": "StaticFieldC",
                        "declaring_type": "Namespace.Struct",
                        "returns": "Namespace.Type",
                        "static": True,
                    },
                },
                "constructors": {},
                "properties": {},
                "methods": {},
                "dunder_methods": {},
                "events": {},
                "nested": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_constructors(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
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
                "Namespace.Struct.__init__(Namespace.Type)": CConstructor(
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                    ),
                ),
                "Namespace.Struct.__init__(Namespace.Type, Namespace.Type)": CConstructor(
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                        CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
                    ),
                ),
                "Namespace.Struct.__init__(Namespace.Type, Namespace.Type, Namespace.Type)": CConstructor(
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
            dunder_methods={},
            events={},
            nested={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "struct",
                "name": "Struct",
                "namespace": "Namespace",
                "abstract": False,
                "generic_args": (),
                "super_class": None,
                "interfaces": (),
                "fields": {},
                "constructors": {
                    "Namespace.Struct.__init__()": {
                        "declaring_type": "Namespace.Struct",
                        "parameters": (),
                    },
                    "Namespace.Struct.__init__(Namespace.Type)": {
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.Type",
                                "default": False,
                                "out": False,
                            },
                        ),
                    },
                    "Namespace.Struct.__init__(Namespace.Type, Namespace.Type)": {
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.Type",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "param1",
                                "type": "Namespace.Type",
                                "default": False,
                                "out": False,
                            },
                        ),
                    },
                    "Namespace.Struct.__init__(Namespace.Type, Namespace.Type, Namespace.Type)": {
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.Type",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "param1",
                                "type": "Namespace.Type",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "param2",
                                "type": "Namespace.Type",
                                "default": False,
                                "out": False,
                            },
                        ),
                    },
                },
                "properties": {},
                "methods": {},
                "dunder_methods": {},
                "events": {},
                "nested": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_properties(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={
                "Namespace.Struct.InstanceProperty0": CProperty(
                    name="InstanceProperty0",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    setter=True,
                ),
                "Namespace.Struct.InstanceProperty1": CProperty(
                    name="InstanceProperty1",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    setter=True,
                ),
                "Namespace.Struct.InstanceProperty2": CProperty(
                    name="InstanceProperty2",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    setter=True,
                ),
                "Namespace.Struct.InstanceReadOnlyProperty0": CProperty(
                    name="InstanceReadOnlyProperty0",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace.Struct.InstanceReadOnlyProperty1": CProperty(
                    name="InstanceReadOnlyProperty1",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace.Struct.InstanceReadOnlyProperty2": CProperty(
                    name="InstanceReadOnlyProperty2",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                ),
                "Namespace.Struct.StaticProperty0": CProperty(
                    name="StaticProperty0",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    setter=True,
                    static=True,
                ),
                "Namespace.Struct.StaticProperty1": CProperty(
                    name="StaticProperty1",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    setter=True,
                    static=True,
                ),
                "Namespace.Struct.StaticProperty2": CProperty(
                    name="StaticProperty2",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    setter=True,
                    static=True,
                ),
                "Namespace.Struct.StaticReadOnlyProperty0": CProperty(
                    name="StaticReadOnlyProperty0",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    static=True,
                ),
                "Namespace.Struct.StaticReadOnlyProperty1": CProperty(
                    name="StaticReadOnlyProperty1",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    static=True,
                ),
                "Namespace.Struct.StaticReadOnlyProperty2": CProperty(
                    name="StaticReadOnlyProperty2",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="Type", namespace="Namespace"),
                    static=True,
                ),
            },
            methods={},
            dunder_methods={},
            events={},
            nested={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "struct",
                "name": "Struct",
                "namespace": "Namespace",
                "abstract": False,
                "generic_args": (),
                "super_class": None,
                "interfaces": (),
                "fields": {},
                "constructors": {},
                "properties": {
                    "Namespace.Struct.InstanceProperty0": {
                        "name": "InstanceProperty0",
                        "declaring_type": "Namespace.Struct",
                        "type": "Namespace.Type",
                        "setter": True,
                        "static": False,
                    },
                    "Namespace.Struct.InstanceProperty1": {
                        "name": "InstanceProperty1",
                        "declaring_type": "Namespace.Struct",
                        "type": "Namespace.Type",
                        "setter": True,
                        "static": False,
                    },
                    "Namespace.Struct.InstanceProperty2": {
                        "name": "InstanceProperty2",
                        "declaring_type": "Namespace.Struct",
                        "type": "Namespace.Type",
                        "setter": True,
                        "static": False,
                    },
                    "Namespace.Struct.InstanceReadOnlyProperty0": {
                        "name": "InstanceReadOnlyProperty0",
                        "declaring_type": "Namespace.Struct",
                        "type": "Namespace.Type",
                        "setter": False,
                        "static": False,
                    },
                    "Namespace.Struct.InstanceReadOnlyProperty1": {
                        "name": "InstanceReadOnlyProperty1",
                        "declaring_type": "Namespace.Struct",
                        "type": "Namespace.Type",
                        "setter": False,
                        "static": False,
                    },
                    "Namespace.Struct.InstanceReadOnlyProperty2": {
                        "name": "InstanceReadOnlyProperty2",
                        "declaring_type": "Namespace.Struct",
                        "type": "Namespace.Type",
                        "setter": False,
                        "static": False,
                    },
                    "Namespace.Struct.StaticProperty0": {
                        "name": "StaticProperty0",
                        "declaring_type": "Namespace.Struct",
                        "type": "Namespace.Type",
                        "setter": True,
                        "static": True,
                    },
                    "Namespace.Struct.StaticProperty1": {
                        "name": "StaticProperty1",
                        "declaring_type": "Namespace.Struct",
                        "type": "Namespace.Type",
                        "setter": True,
                        "static": True,
                    },
                    "Namespace.Struct.StaticProperty2": {
                        "name": "StaticProperty2",
                        "declaring_type": "Namespace.Struct",
                        "type": "Namespace.Type",
                        "setter": True,
                        "static": True,
                    },
                    "Namespace.Struct.StaticReadOnlyProperty0": {
                        "name": "StaticReadOnlyProperty0",
                        "declaring_type": "Namespace.Struct",
                        "type": "Namespace.Type",
                        "setter": False,
                        "static": True,
                    },
                    "Namespace.Struct.StaticReadOnlyProperty1": {
                        "name": "StaticReadOnlyProperty1",
                        "declaring_type": "Namespace.Struct",
                        "type": "Namespace.Type",
                        "setter": False,
                        "static": True,
                    },
                    "Namespace.Struct.StaticReadOnlyProperty2": {
                        "name": "StaticReadOnlyProperty2",
                        "declaring_type": "Namespace.Struct",
                        "type": "Namespace.Type",
                        "setter": False,
                        "static": True,
                    },
                },
                "methods": {},
                "dunder_methods": {},
                "events": {},
                "nested": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_methods(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={
                "Namespace.Struct.InstanceMethodWithDefaultParam(Namespace.Type) -> Namespace.Type": CMethod(
                    name="InstanceMethodWithDefaultParam",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace"),
                            default=True,
                        ),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace.Struct.InstanceMethodWithNullableDefaultParam(Namespace.Type?) -> Namespace.Type": CMethod(
                    name="InstanceMethodWithNullableDefaultParam",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace", nullable=True),
                            default=True,
                        ),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace.Struct.InstanceMethodWithNullableOutParam(Namespace.*Type?) -> Namespace.Type, Namespace.*Type?": CMethod(
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
                    returns=(
                        CType(name="Type", namespace="Namespace"),
                        CType(name="Type", namespace="Namespace", reference=True, nullable=True),
                    ),
                ),
                "Namespace.Struct.InstanceMethodWithNullableParam(Namespace.Type?) -> Namespace.Type": CMethod(
                    name="InstanceMethodWithNullableParam",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace", nullable=True),
                        ),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace.Struct.InstanceMethodWithOutParam(Namespace.*Type) -> Namespace.Type, Namespace.*Type": CMethod(
                    name="InstanceMethodWithOutParam",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace", reference=True),
                            out=True,
                        ),
                    ),
                    returns=(
                        CType(name="Type", namespace="Namespace"),
                        CType(name="Type", namespace="Namespace", reference=True),
                    ),
                ),
                "Namespace.Struct.InstanceMethodWithParams0() -> Namespace.Type": CMethod(
                    name="InstanceMethodWithParams0",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(),
                    returns=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace.Struct.InstanceMethodWithParams1(Namespace.Type) -> Namespace.Type": CMethod(
                    name="InstanceMethodWithParams1",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace.Struct.InstanceMethodWithParams2(Namespace.Type, Namespace.Type) -> Namespace.Type": CMethod(
                    name="InstanceMethodWithParams2",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                        CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace.Struct.StaticMethodWithDefaultParam(Namespace.Type) -> Namespace.Type": CMethod(
                    name="StaticMethodWithDefaultParam",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace"),
                            default=True,
                        ),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Struct.StaticMethodWithNullableDefaultParam(Namespace.Type?) -> Namespace.Type": CMethod(
                    name="StaticMethodWithNullableDefaultParam",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace", nullable=True),
                            default=True,
                        ),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Struct.StaticMethodWithNullableOutParam(Namespace.*Type?) -> Namespace.Type, Namespace.*Type?": CMethod(
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
                    returns=(
                        CType(name="Type", namespace="Namespace"),
                        CType(name="Type", namespace="Namespace", reference=True, nullable=True),
                    ),
                    static=True,
                ),
                "Namespace.Struct.StaticMethodWithNullableParam(Namespace.Type?) -> Namespace.Type": CMethod(
                    name="StaticMethodWithNullableParam",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace", nullable=True),
                        ),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Struct.StaticMethodWithOutParam(Namespace.*Type) -> Namespace.Type, Namespace.*Type": CMethod(
                    name="StaticMethodWithOutParam",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Type", namespace="Namespace", reference=True),
                            out=True,
                        ),
                    ),
                    returns=(
                        CType(name="Type", namespace="Namespace"),
                        CType(name="Type", namespace="Namespace", reference=True),
                    ),
                    static=True,
                ),
                "Namespace.Struct.StaticMethodWithParams0() -> Namespace.Type": CMethod(
                    name="StaticMethodWithParams0",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(),
                    returns=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Struct.StaticMethodWithParams1(Namespace.Type) -> Namespace.Type": CMethod(
                    name="StaticMethodWithParams1",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Struct.StaticMethodWithParams2(Namespace.Type, Namespace.Type) -> Namespace.Type": CMethod(
                    name="StaticMethodWithParams2",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),
                        CParameter(name="param1", type=CType(name="Type", namespace="Namespace")),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
            },
            dunder_methods={},
            events={},
            nested={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "struct",
                "name": "Struct",
                "namespace": "Namespace",
                "abstract": False,
                "generic_args": (),
                "super_class": None,
                "interfaces": (),
                "fields": {},
                "constructors": {},
                "properties": {},
                "methods": {
                    "Namespace.Struct.InstanceMethodWithDefaultParam(Namespace.Type) -> Namespace.Type": {
                        "name": "InstanceMethodWithDefaultParam",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.Type",
                                "default": True,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": False,
                    },
                    "Namespace.Struct.InstanceMethodWithNullableDefaultParam(Namespace.Type?) -> Namespace.Type": {
                        "name": "InstanceMethodWithNullableDefaultParam",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.Type?",
                                "default": True,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": False,
                    },
                    "Namespace.Struct.InstanceMethodWithNullableOutParam(Namespace.*Type?) -> Namespace.Type, Namespace.*Type?": {
                        "name": "InstanceMethodWithNullableOutParam",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.*Type?",
                                "default": False,
                                "out": True,
                            },
                        ),
                        "returns": ("Namespace.Type", "Namespace.*Type?"),
                        "static": False,
                    },
                    "Namespace.Struct.InstanceMethodWithNullableParam(Namespace.Type?) -> Namespace.Type": {
                        "name": "InstanceMethodWithNullableParam",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.Type?",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": False,
                    },
                    "Namespace.Struct.InstanceMethodWithOutParam(Namespace.*Type) -> Namespace.Type, Namespace.*Type": {
                        "name": "InstanceMethodWithOutParam",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.*Type",
                                "default": False,
                                "out": True,
                            },
                        ),
                        "returns": ("Namespace.Type", "Namespace.*Type"),
                        "static": False,
                    },
                    "Namespace.Struct.InstanceMethodWithParams0() -> Namespace.Type": {
                        "name": "InstanceMethodWithParams0",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (),
                        "returns": ("Namespace.Type",),
                        "static": False,
                    },
                    "Namespace.Struct.InstanceMethodWithParams1(Namespace.Type) -> Namespace.Type": {
                        "name": "InstanceMethodWithParams1",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.Type",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": False,
                    },
                    "Namespace.Struct.InstanceMethodWithParams2(Namespace.Type, Namespace.Type) -> Namespace.Type": {
                        "name": "InstanceMethodWithParams2",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.Type",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "param1",
                                "type": "Namespace.Type",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": False,
                    },
                    "Namespace.Struct.StaticMethodWithDefaultParam(Namespace.Type) -> Namespace.Type": {
                        "name": "StaticMethodWithDefaultParam",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.Type",
                                "default": True,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": True,
                    },
                    "Namespace.Struct.StaticMethodWithNullableDefaultParam(Namespace.Type?) -> Namespace.Type": {
                        "name": "StaticMethodWithNullableDefaultParam",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.Type?",
                                "default": True,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": True,
                    },
                    "Namespace.Struct.StaticMethodWithNullableOutParam(Namespace.*Type?) -> Namespace.Type, Namespace.*Type?": {
                        "name": "StaticMethodWithNullableOutParam",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.*Type?",
                                "default": False,
                                "out": True,
                            },
                        ),
                        "returns": ("Namespace.Type", "Namespace.*Type?"),
                        "static": True,
                    },
                    "Namespace.Struct.StaticMethodWithNullableParam(Namespace.Type?) -> Namespace.Type": {
                        "name": "StaticMethodWithNullableParam",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.Type?",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": True,
                    },
                    "Namespace.Struct.StaticMethodWithOutParam(Namespace.*Type) -> Namespace.Type, Namespace.*Type": {
                        "name": "StaticMethodWithOutParam",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.*Type",
                                "default": False,
                                "out": True,
                            },
                        ),
                        "returns": ("Namespace.Type", "Namespace.*Type"),
                        "static": True,
                    },
                    "Namespace.Struct.StaticMethodWithParams0() -> Namespace.Type": {
                        "name": "StaticMethodWithParams0",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (),
                        "returns": ("Namespace.Type",),
                        "static": True,
                    },
                    "Namespace.Struct.StaticMethodWithParams1(Namespace.Type) -> Namespace.Type": {
                        "name": "StaticMethodWithParams1",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.Type",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": True,
                    },
                    "Namespace.Struct.StaticMethodWithParams2(Namespace.Type, Namespace.Type) -> Namespace.Type": {
                        "name": "StaticMethodWithParams2",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "Namespace.Type",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "param1",
                                "type": "Namespace.Type",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": True,
                    },
                },
                "dunder_methods": {},
                "events": {},
                "nested": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_methods_dunder(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={
                "Namespace.Struct.op_Addition(Namespace.Struct, Namespace.Struct) -> Namespace.Struct": CMethod(
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
                    returns=(CType(name="Struct", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Struct.op_BitwiseAnd(Namespace.Struct, Namespace.Struct) -> Namespace.Struct": CMethod(
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
                    returns=(CType(name="Struct", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Struct.op_BitwiseOr(Namespace.Struct, Namespace.Struct) -> Namespace.Struct": CMethod(
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
                    returns=(CType(name="Struct", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Struct.op_Decrement(Namespace.Struct) -> Namespace.Struct": CMethod(
                    name="op_Decrement",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Struct", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Struct.op_Division(Namespace.Struct, Namespace.Struct) -> Namespace.Struct": CMethod(
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
                    returns=(CType(name="Struct", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Struct.op_Equality(Namespace.Struct, Namespace.Struct) -> Namespace.Type": CMethod(
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
                    returns=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Struct.op_ExclusiveOr(Namespace.Struct, Namespace.Struct) -> Namespace.Struct": CMethod(
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
                    returns=(CType(name="Struct", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Struct.op_False(Namespace.Struct) -> Namespace.Type": CMethod(
                    name="op_False",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(name="self", type=CType(name="Struct", namespace="Namespace")),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Struct.op_GreaterThan(Namespace.Struct, Namespace.Struct) -> Namespace.Type": CMethod(
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
                    returns=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Struct.op_GreaterThanOrEqual(Namespace.Struct, Namespace.Struct) -> Namespace.Type": CMethod(
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
                    returns=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Struct.op_Increment(Namespace.Struct) -> Namespace.Struct": CMethod(
                    name="op_Increment",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Struct", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Struct.op_Inequality(Namespace.Struct, Namespace.Struct) -> Namespace.Type": CMethod(
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
                    returns=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Struct.op_LessThan(Namespace.Struct, Namespace.Struct) -> Namespace.Type": CMethod(
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
                    returns=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Struct.op_LessThanOrEqual(Namespace.Struct, Namespace.Struct) -> Namespace.Type": CMethod(
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
                    returns=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Struct.op_LogicalNot(Namespace.Struct) -> Namespace.Type": CMethod(
                    name="op_LogicalNot",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Struct.op_Modulus(Namespace.Struct, Namespace.Struct) -> Namespace.Struct": CMethod(
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
                    returns=(CType(name="Struct", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Struct.op_Multiply(Namespace.Struct, Namespace.Struct) -> Namespace.Struct": CMethod(
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
                    returns=(CType(name="Struct", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Struct.op_OnesComplement(Namespace.Struct) -> Namespace.Struct": CMethod(
                    name="op_OnesComplement",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Struct", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Struct.op_Subtraction(Namespace.Struct, Namespace.Struct) -> Namespace.Struct": CMethod(
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
                    returns=(CType(name="Struct", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Struct.op_True(Namespace.Struct) -> Namespace.Type": CMethod(
                    name="op_True",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Struct.op_UnaryNegation(Namespace.Struct) -> Namespace.Struct": CMethod(
                    name="op_UnaryNegation",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Struct", namespace="Namespace"),),
                    static=True,
                ),
                "Namespace.Struct.op_UnaryPlus(Namespace.Struct) -> Namespace.Struct": CMethod(
                    name="op_UnaryPlus",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Struct", namespace="Namespace"),),
                    static=True,
                ),
            },
            dunder_methods={
                "Namespace.Struct.__add__(Namespace.Struct) -> Namespace.Struct": CMethod(
                    name="__add__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Struct", namespace="Namespace"),),
                ),
                "Namespace.Struct.__and__(Namespace.Struct) -> Namespace.Struct": CMethod(
                    name="__and__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Struct", namespace="Namespace"),),
                ),
                "Namespace.Struct.__eq__(Namespace.Struct) -> Namespace.Type": CMethod(
                    name="__eq__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace.Struct.__ge__(Namespace.Struct) -> Namespace.Type": CMethod(
                    name="__ge__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace.Struct.__gt__(Namespace.Struct) -> Namespace.Type": CMethod(
                    name="__gt__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace.Struct.__invert__() -> Namespace.Struct": CMethod(
                    name="__invert__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(),
                    returns=(CType(name="Struct", namespace="Namespace"),),
                ),
                "Namespace.Struct.__le__(Namespace.Struct) -> Namespace.Type": CMethod(
                    name="__le__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace.Struct.__lt__(Namespace.Struct) -> Namespace.Type": CMethod(
                    name="__lt__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Type", namespace="Namespace"),),
                ),
                "Namespace.Struct.__mod__(Namespace.Struct) -> Namespace.Struct": CMethod(
                    name="__mod__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Struct", namespace="Namespace"),),
                ),
                "Namespace.Struct.__mul__(Namespace.Struct) -> Namespace.Struct": CMethod(
                    name="__mul__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Struct", namespace="Namespace"),),
                ),
                "Namespace.Struct.__ne__(Namespace.Struct) -> Namespace.Type": CMethod(
                    name="__ne__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Type", namespace="System"),),
                ),
                "Namespace.Struct.__neg__() -> Namespace.Struct": CMethod(
                    name="__neg__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(),
                    returns=(CType(name="Struct", namespace="Namespace"),),
                ),
                "Namespace.Struct.__or__(Namespace.Struct) -> Namespace.Struct": CMethod(
                    name="__or__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Struct", namespace="Namespace"),),
                ),
                "Namespace.Struct.__pos__() -> Namespace.Struct": CMethod(
                    name="__pos__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(),
                    returns=(CType(name="Struct", namespace="Namespace"),),
                ),
                "Namespace.Struct.__sub__(Namespace.Struct) -> Namespace.Struct": CMethod(
                    name="__sub__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Struct", namespace="Namespace"),),
                ),
                "Namespace.Struct.__truediv__(Namespace.Struct) -> Namespace.Struct": CMethod(
                    name="__truediv__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Struct", namespace="Namespace"),),
                ),
                "Namespace.Struct.__xor__(Namespace.Struct) -> Namespace.Struct": CMethod(
                    name="__xor__",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="Struct", namespace="Namespace"),
                        ),
                    ),
                    returns=(CType(name="Struct", namespace="Namespace"),),
                ),
            },
            events={},
            nested={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "struct",
                "name": "Struct",
                "namespace": "Namespace",
                "abstract": False,
                "generic_args": (),
                "super_class": None,
                "interfaces": (),
                "fields": {},
                "constructors": {},
                "properties": {},
                "methods": {
                    "Namespace.Struct.op_Addition(Namespace.Struct, Namespace.Struct) -> Namespace.Struct": {
                        "name": "op_Addition",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Struct",),
                        "static": True,
                    },
                    "Namespace.Struct.op_BitwiseAnd(Namespace.Struct, Namespace.Struct) -> Namespace.Struct": {
                        "name": "op_BitwiseAnd",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Struct",),
                        "static": True,
                    },
                    "Namespace.Struct.op_BitwiseOr(Namespace.Struct, Namespace.Struct) -> Namespace.Struct": {
                        "name": "op_BitwiseOr",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Struct",),
                        "static": True,
                    },
                    "Namespace.Struct.op_Decrement(Namespace.Struct) -> Namespace.Struct": {
                        "name": "op_Decrement",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Struct",),
                        "static": True,
                    },
                    "Namespace.Struct.op_Division(Namespace.Struct, Namespace.Struct) -> Namespace.Struct": {
                        "name": "op_Division",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Struct",),
                        "static": True,
                    },
                    "Namespace.Struct.op_Equality(Namespace.Struct, Namespace.Struct) -> Namespace.Type": {
                        "name": "op_Equality",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": True,
                    },
                    "Namespace.Struct.op_ExclusiveOr(Namespace.Struct, Namespace.Struct) -> Namespace.Struct": {
                        "name": "op_ExclusiveOr",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Struct",),
                        "static": True,
                    },
                    "Namespace.Struct.op_False(Namespace.Struct) -> Namespace.Type": {
                        "name": "op_False",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": True,
                    },
                    "Namespace.Struct.op_GreaterThan(Namespace.Struct, Namespace.Struct) -> Namespace.Type": {
                        "name": "op_GreaterThan",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": True,
                    },
                    "Namespace.Struct.op_GreaterThanOrEqual(Namespace.Struct, Namespace.Struct) -> Namespace.Type": {
                        "name": "op_GreaterThanOrEqual",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": True,
                    },
                    "Namespace.Struct.op_Increment(Namespace.Struct) -> Namespace.Struct": {
                        "name": "op_Increment",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Struct",),
                        "static": True,
                    },
                    "Namespace.Struct.op_Inequality(Namespace.Struct, Namespace.Struct) -> Namespace.Type": {
                        "name": "op_Inequality",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": True,
                    },
                    "Namespace.Struct.op_LessThan(Namespace.Struct, Namespace.Struct) -> Namespace.Type": {
                        "name": "op_LessThan",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": True,
                    },
                    "Namespace.Struct.op_LessThanOrEqual(Namespace.Struct, Namespace.Struct) -> Namespace.Type": {
                        "name": "op_LessThanOrEqual",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": True,
                    },
                    "Namespace.Struct.op_LogicalNot(Namespace.Struct) -> Namespace.Type": {
                        "name": "op_LogicalNot",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": True,
                    },
                    "Namespace.Struct.op_Modulus(Namespace.Struct, Namespace.Struct) -> Namespace.Struct": {
                        "name": "op_Modulus",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Struct",),
                        "static": True,
                    },
                    "Namespace.Struct.op_Multiply(Namespace.Struct, Namespace.Struct) -> Namespace.Struct": {
                        "name": "op_Multiply",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Struct",),
                        "static": True,
                    },
                    "Namespace.Struct.op_OnesComplement(Namespace.Struct) -> Namespace.Struct": {
                        "name": "op_OnesComplement",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Struct",),
                        "static": True,
                    },
                    "Namespace.Struct.op_Subtraction(Namespace.Struct, Namespace.Struct) -> Namespace.Struct": {
                        "name": "op_Subtraction",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "other",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Struct",),
                        "static": True,
                    },
                    "Namespace.Struct.op_True(Namespace.Struct) -> Namespace.Type": {
                        "name": "op_True",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": True,
                    },
                    "Namespace.Struct.op_UnaryNegation(Namespace.Struct) -> Namespace.Struct": {
                        "name": "op_UnaryNegation",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Struct",),
                        "static": True,
                    },
                    "Namespace.Struct.op_UnaryPlus(Namespace.Struct) -> Namespace.Struct": {
                        "name": "op_UnaryPlus",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "self",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Struct",),
                        "static": True,
                    },
                },
                "dunder_methods": {
                    "Namespace.Struct.__add__(Namespace.Struct) -> Namespace.Struct": {
                        "name": "__add__",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Struct",),
                        "static": False,
                    },
                    "Namespace.Struct.__and__(Namespace.Struct) -> Namespace.Struct": {
                        "name": "__and__",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Struct",),
                        "static": False,
                    },
                    "Namespace.Struct.__eq__(Namespace.Struct) -> Namespace.Type": {
                        "name": "__eq__",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": False,
                    },
                    "Namespace.Struct.__ge__(Namespace.Struct) -> Namespace.Type": {
                        "name": "__ge__",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": False,
                    },
                    "Namespace.Struct.__gt__(Namespace.Struct) -> Namespace.Type": {
                        "name": "__gt__",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": False,
                    },
                    "Namespace.Struct.__invert__() -> Namespace.Struct": {
                        "name": "__invert__",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (),
                        "returns": ("Namespace.Struct",),
                        "static": False,
                    },
                    "Namespace.Struct.__le__(Namespace.Struct) -> Namespace.Type": {
                        "name": "__le__",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": False,
                    },
                    "Namespace.Struct.__lt__(Namespace.Struct) -> Namespace.Type": {
                        "name": "__lt__",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Type",),
                        "static": False,
                    },
                    "Namespace.Struct.__mod__(Namespace.Struct) -> Namespace.Struct": {
                        "name": "__mod__",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Struct",),
                        "static": False,
                    },
                    "Namespace.Struct.__mul__(Namespace.Struct) -> Namespace.Struct": {
                        "name": "__mul__",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Struct",),
                        "static": False,
                    },
                    "Namespace.Struct.__ne__(Namespace.Struct) -> Namespace.Type": {
                        "name": "__ne__",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("System.Type",),
                        "static": False,
                    },
                    "Namespace.Struct.__neg__() -> Namespace.Struct": {
                        "name": "__neg__",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (),
                        "returns": ("Namespace.Struct",),
                        "static": False,
                    },
                    "Namespace.Struct.__or__(Namespace.Struct) -> Namespace.Struct": {
                        "name": "__or__",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Struct",),
                        "static": False,
                    },
                    "Namespace.Struct.__pos__() -> Namespace.Struct": {
                        "name": "__pos__",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (),
                        "returns": ("Namespace.Struct",),
                        "static": False,
                    },
                    "Namespace.Struct.__sub__(Namespace.Struct) -> Namespace.Struct": {
                        "name": "__sub__",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Struct",),
                        "static": False,
                    },
                    "Namespace.Struct.__truediv__(Namespace.Struct) -> Namespace.Struct": {
                        "name": "__truediv__",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Struct",),
                        "static": False,
                    },
                    "Namespace.Struct.__xor__(Namespace.Struct) -> Namespace.Struct": {
                        "name": "__xor__",
                        "declaring_type": "Namespace.Struct",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Struct",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Struct",),
                        "static": False,
                    },
                },
                "events": {},
                "nested": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_events(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            dunder_methods={},
            events={
                "Namespace.Struct.Event -> (System.EventHandler)": CEvent(
                    name="Event",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(name="EventHandler", namespace="System"),
                ),
                "Namespace.Struct.EventWithArgs -> (System.EventHandler[System.EventArgs])": CEvent(
                    name="EventWithArgs",
                    declaring_type=CType(name="Struct", namespace="Namespace"),
                    type=CType(
                        name="EventHandler",
                        namespace="System",
                        inner=(CType(name="EventArgs", namespace="System"),),
                    ),
                ),
            },
            nested={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "struct",
                "name": "Struct",
                "namespace": "Namespace",
                "abstract": False,
                "generic_args": (),
                "super_class": None,
                "interfaces": (),
                "fields": {},
                "constructors": {},
                "properties": {},
                "methods": {},
                "dunder_methods": {},
                "events": {
                    "Namespace.Struct.Event -> (System.EventHandler)": {
                        "name": "Event",
                        "declaring_type": "Namespace.Struct",
                        "type": "System.EventHandler",
                    },
                    "Namespace.Struct.EventWithArgs -> (System.EventHandler[System.EventArgs])": {
                        "name": "EventWithArgs",
                        "declaring_type": "Namespace.Struct",
                        "type": "System.EventHandler[System.EventArgs]",
                    },
                },
                "nested": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_nested(self) -> None:
        type_def: CStruct = CStruct(
            name="Struct",
            namespace="Namespace",
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            dunder_methods={},
            events={},
            nested={
                "Namespace.INestedInterface": CInterface(
                    name="INestedInterface",
                    namespace="Namespace",
                    generic_args=(),
                    interfaces=(),
                    fields={},
                    properties={},
                    methods={},
                    dunder_methods={},
                    events={},
                    nested={},
                ),
                "Namespace.NestedClass": CClass(
                    name="NestedClass",
                    namespace="Namespace",
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    dunder_methods={},
                    events={},
                    nested={},
                ),
                "Namespace.NestedDelegate": CDelegate(
                    name="NestedDelegate",
                    namespace="Namespace",
                    parameters=(),
                    return_type=CType(name="Void", namespace="System"),
                ),
                "Namespace.NestedEnum": CEnum(name="NestedEnum", namespace="Namespace", fields=()),
                "Namespace.NestedStruct": CStruct(
                    name="NestedStruct",
                    namespace="Namespace",
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    dunder_methods={},
                    events={},
                    nested={},
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
                "abstract": False,
                "generic_args": (),
                "super_class": None,
                "interfaces": (),
                "fields": {},
                "constructors": {},
                "properties": {},
                "methods": {},
                "dunder_methods": {},
                "events": {},
                "nested": {
                    "Namespace.INestedInterface": {
                        "type": "interface",
                        "name": "INestedInterface",
                        "namespace": "Namespace",
                        "generic_args": (),
                        "interfaces": (),
                        "fields": {},
                        "properties": {},
                        "methods": {},
                        "dunder_methods": {},
                        "events": {},
                        "nested": {},
                    },
                    "Namespace.NestedClass": {
                        "type": "class",
                        "name": "NestedClass",
                        "namespace": "Namespace",
                        "abstract": False,
                        "generic_args": (),
                        "super_class": None,
                        "interfaces": (),
                        "fields": {},
                        "constructors": {},
                        "properties": {},
                        "methods": {},
                        "dunder_methods": {},
                        "events": {},
                        "nested": {},
                    },
                    "Namespace.NestedDelegate": {
                        "type": "delegate",
                        "name": "NestedDelegate",
                        "namespace": "Namespace",
                        "parameters": (),
                        "return_type": "System.Void",
                    },
                    "Namespace.NestedEnum": {
                        "type": "enum",
                        "name": "NestedEnum",
                        "namespace": "Namespace",
                        "fields": (),
                    },
                    "Namespace.NestedStruct": {
                        "type": "struct",
                        "name": "NestedStruct",
                        "namespace": "Namespace",
                        "abstract": False,
                        "generic_args": (),
                        "super_class": None,
                        "interfaces": (),
                        "fields": {},
                        "constructors": {},
                        "properties": {},
                        "methods": {},
                        "dunder_methods": {},
                        "events": {},
                        "nested": {},
                    },
                },
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_compare(self) -> None:
        struct0: CStruct = CStruct(
            name="StructA",
            namespace="Namespace",
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            dunder_methods={},
            events={},
            nested={},
        )
        struct1: CStruct = CStruct(
            name="StructB",
            namespace="Namespace",
            abstract=False,
            generic_args=(),
            super_class=None,
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={},
            dunder_methods={},
            events={},
            nested={},
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
                abstract=False,
                generic_args=(),
                super_class=None,
                interfaces=(),
                fields={},
                constructors={},
                properties={},
                methods={},
                dunder_methods={},
                events={},
                nested={},
            ),
            CStruct(
                name="StructB",
                namespace="Namespace",
                abstract=False,
                generic_args=(),
                super_class=None,
                interfaces=(),
                fields={},
                constructors={},
                properties={},
                methods={},
                dunder_methods={},
                events={},
                nested={},
            ),
            CStruct(
                name="StructC",
                namespace="Namespace",
                abstract=False,
                generic_args=(),
                super_class=None,
                interfaces=(),
                fields={},
                constructors={},
                properties={},
                methods={},
                dunder_methods={},
                events={},
                nested={},
            ),
            CStruct(
                name="StructD",
                namespace="Namespace",
                abstract=False,
                generic_args=(),
                super_class=None,
                interfaces=(),
                fields={},
                constructors={},
                properties={},
                methods={},
                dunder_methods={},
                events={},
                nested={},
            ),
        )
        unordered: MutableSequence[CStruct] = list(ordered)
        random.shuffle(unordered)

        self.assertSequenceEqual(ordered, sorted(unordered))


class TestCInterface(TestBase):
    def test_from_info_generic(self) -> None:
        type_info: TypeInfo = self.get_type("IInterfaceWithGeneric")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCInterface(
            interface=cast(CInterface, type_def),
            name="IInterfaceWithGeneric",
            namespace="TestLib",
            generic_args=(CType(name="T", namespace="TestLib", generic=True),),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            dunder_methods={},
            events={},
            nested={},
        )

    def test_from_info_generic_multi(self) -> None:
        type_info: TypeInfo = self.get_type("IInterfaceWithMultiGeneric")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCInterface(
            interface=cast(CInterface, type_def),
            name="IInterfaceWithMultiGeneric",
            namespace="TestLib",
            generic_args=(
                CType(name="U", namespace="TestLib", generic=True),
                CType(name="V", namespace="TestLib", generic=True),
            ),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            dunder_methods={},
            events={},
            nested={},
        )

    def test_from_info_interfaces(self) -> None:
        type_info: TypeInfo = self.get_type("IInterfaceWithInterface")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCInterface(
            interface=cast(CInterface, type_def),
            name="IInterfaceWithInterface",
            namespace="TestLib",
            generic_args=(),
            interfaces=(
                CType(
                    name="IEquatable",
                    namespace="System",
                    inner=(CType(name="IInterfaceWithInterface", namespace="TestLib"),),
                ),
            ),
            fields={},
            properties={},
            methods={
                "System.IEquatable[TestLib.IInterfaceWithInterface].Equals(TestLib.IInterfaceWithInterface) -> System.Boolean": CMethod(
                    name="Equals",
                    declaring_type=CType(
                        name="IEquatable",
                        namespace="System",
                        inner=(CType(name="IInterfaceWithInterface", namespace="TestLib"),),
                    ),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithInterface", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
            },
            dunder_methods={},
            events={},
            nested={},
        )

    def test_from_info_fields(self) -> None:
        type_info: TypeInfo = self.get_type("IInterfaceWithFields")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCInterface(
            interface=cast(CInterface, type_def),
            name="IInterfaceWithFields",
            namespace="TestLib",
            generic_args=(),
            interfaces=(),
            fields={
                "TestLib.IInterfaceWithFields.StaticFieldA": CField(
                    name="StaticFieldA",
                    declaring_type=CType(name="IInterfaceWithFields", namespace="TestLib"),
                    returns=CType(name="Int32", namespace="System"),
                    static=True,
                ),
                "TestLib.IInterfaceWithFields.StaticFieldB": CField(
                    name="StaticFieldB",
                    declaring_type=CType(name="IInterfaceWithFields", namespace="TestLib"),
                    returns=CType(name="Int32", namespace="System"),
                    static=True,
                ),
                "TestLib.IInterfaceWithFields.StaticFieldC": CField(
                    name="StaticFieldC",
                    declaring_type=CType(name="IInterfaceWithFields", namespace="TestLib"),
                    returns=CType(name="Int32", namespace="System"),
                    static=True,
                ),
            },
            properties={},
            methods={},
            dunder_methods={},
            events={},
            nested={},
        )

    def test_from_info_properties(self) -> None:
        type_info: TypeInfo = self.get_type("IInterfaceWithProperties")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCInterface(
            interface=cast(CInterface, type_def),
            name="IInterfaceWithProperties",
            namespace="TestLib",
            generic_args=(),
            interfaces=(),
            fields={},
            properties={
                "TestLib.IInterfaceWithProperties.InstanceProperty0": CProperty(
                    name="InstanceProperty0",
                    declaring_type=CType(name="IInterfaceWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                ),
                "TestLib.IInterfaceWithProperties.InstanceProperty1": CProperty(
                    name="InstanceProperty1",
                    declaring_type=CType(name="IInterfaceWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                ),
                "TestLib.IInterfaceWithProperties.InstanceProperty2": CProperty(
                    name="InstanceProperty2",
                    declaring_type=CType(name="IInterfaceWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                ),
                "TestLib.IInterfaceWithProperties.InstanceReadOnlyProperty0": CProperty(
                    name="InstanceReadOnlyProperty0",
                    declaring_type=CType(name="IInterfaceWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                ),
                "TestLib.IInterfaceWithProperties.InstanceReadOnlyProperty1": CProperty(
                    name="InstanceReadOnlyProperty1",
                    declaring_type=CType(name="IInterfaceWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                ),
                "TestLib.IInterfaceWithProperties.InstanceReadOnlyProperty2": CProperty(
                    name="InstanceReadOnlyProperty2",
                    declaring_type=CType(name="IInterfaceWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                ),
                "TestLib.IInterfaceWithProperties.StaticProperty0": CProperty(
                    name="StaticProperty0",
                    declaring_type=CType(name="IInterfaceWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                    static=True,
                ),
                "TestLib.IInterfaceWithProperties.StaticProperty1": CProperty(
                    name="StaticProperty1",
                    declaring_type=CType(name="IInterfaceWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                    static=True,
                ),
                "TestLib.IInterfaceWithProperties.StaticProperty2": CProperty(
                    name="StaticProperty2",
                    declaring_type=CType(name="IInterfaceWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                    static=True,
                ),
                "TestLib.IInterfaceWithProperties.StaticReadOnlyProperty0": CProperty(
                    name="StaticReadOnlyProperty0",
                    declaring_type=CType(name="IInterfaceWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
                "TestLib.IInterfaceWithProperties.StaticReadOnlyProperty1": CProperty(
                    name="StaticReadOnlyProperty1",
                    declaring_type=CType(name="IInterfaceWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
                "TestLib.IInterfaceWithProperties.StaticReadOnlyProperty2": CProperty(
                    name="StaticReadOnlyProperty2",
                    declaring_type=CType(name="IInterfaceWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
            },
            methods={},
            dunder_methods={},
            events={},
            nested={},
        )

    def test_from_info_methods(self) -> None:
        type_info: TypeInfo = self.get_type("IInterfaceWithMethods")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCInterface(
            interface=cast(CInterface, type_def),
            name="IInterfaceWithMethods",
            namespace="TestLib",
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={
                "TestLib.IInterfaceWithMethods.InstanceMethodWithDefaultParam(System.Int32) -> System.Int32": CMethod(
                    name="InstanceMethodWithDefaultParam",
                    declaring_type=CType(name="IInterfaceWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System"),
                            default=True,
                        ),
                    ),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib.IInterfaceWithMethods.InstanceMethodWithNullableDefaultParam(System.Int32?) -> System.Int32": CMethod(
                    name="InstanceMethodWithNullableDefaultParam",
                    declaring_type=CType(name="IInterfaceWithMethods", namespace="TestLib"),
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
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib.IInterfaceWithMethods.InstanceMethodWithNullableOutParam(System.*Int32?) -> System.Int32, System.*Int32?": CMethod(
                    name="InstanceMethodWithNullableOutParam",
                    declaring_type=CType(name="IInterfaceWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(
                                name="Int32", namespace="System", reference=True, nullable=True
                            ),
                            out=True,
                        ),
                    ),
                    returns=(
                        CType(name="Int32", namespace="System"),
                        CType(name="Int32", namespace="System", reference=True, nullable=True),
                    ),
                ),
                "TestLib.IInterfaceWithMethods.InstanceMethodWithNullableParam(System.Int32?) -> System.Int32": CMethod(
                    name="InstanceMethodWithNullableParam",
                    declaring_type=CType(name="IInterfaceWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System", nullable=True),
                        ),
                    ),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib.IInterfaceWithMethods.InstanceMethodWithOutParam(System.*Int32) -> System.Int32, System.*Int32": CMethod(
                    name="InstanceMethodWithOutParam",
                    declaring_type=CType(name="IInterfaceWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System", reference=True),
                            out=True,
                        ),
                    ),
                    returns=(
                        CType(name="Int32", namespace="System"),
                        CType(name="Int32", namespace="System", reference=True),
                    ),
                ),
                "TestLib.IInterfaceWithMethods.InstanceMethodWithParams() -> System.Int32": CMethod(
                    name="InstanceMethodWithParams",
                    declaring_type=CType(name="IInterfaceWithMethods", namespace="TestLib"),
                    parameters=(),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib.IInterfaceWithMethods.InstanceMethodWithParams(System.Int32) -> System.Int32": CMethod(
                    name="InstanceMethodWithParams",
                    declaring_type=CType(name="IInterfaceWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                    ),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib.IInterfaceWithMethods.InstanceMethodWithParams(System.Int32, System.Int32) -> System.Int32": CMethod(
                    name="InstanceMethodWithParams",
                    declaring_type=CType(name="IInterfaceWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                        CParameter(name="param1", type=CType(name="Int32", namespace="System")),
                    ),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
            },
            dunder_methods={},
            events={},
            nested={},
        )

    def test_from_info_methods_dunder(self) -> None:
        type_info: TypeInfo = self.get_type("IInterfaceWithOperatorMethods")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCInterface(
            interface=cast(CInterface, type_def),
            name="IInterfaceWithOperatorMethods",
            namespace="TestLib",
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={
                "TestLib.IInterfaceWithOperatorMethods.op_Addition(TestLib.IInterfaceWithOperatorMethods, TestLib.IInterfaceWithOperatorMethods) -> TestLib.IInterfaceWithOperatorMethods": CMethod(
                    name="op_Addition",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.IInterfaceWithOperatorMethods.op_BitwiseAnd(TestLib.IInterfaceWithOperatorMethods, TestLib.IInterfaceWithOperatorMethods) -> TestLib.IInterfaceWithOperatorMethods": CMethod(
                    name="op_BitwiseAnd",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.IInterfaceWithOperatorMethods.op_BitwiseOr(TestLib.IInterfaceWithOperatorMethods, TestLib.IInterfaceWithOperatorMethods) -> TestLib.IInterfaceWithOperatorMethods": CMethod(
                    name="op_BitwiseOr",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.IInterfaceWithOperatorMethods.op_Decrement(TestLib.IInterfaceWithOperatorMethods) -> TestLib.IInterfaceWithOperatorMethods": CMethod(
                    name="op_Decrement",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.IInterfaceWithOperatorMethods.op_Division(TestLib.IInterfaceWithOperatorMethods, TestLib.IInterfaceWithOperatorMethods) -> TestLib.IInterfaceWithOperatorMethods": CMethod(
                    name="op_Division",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.IInterfaceWithOperatorMethods.op_ExclusiveOr(TestLib.IInterfaceWithOperatorMethods, TestLib.IInterfaceWithOperatorMethods) -> TestLib.IInterfaceWithOperatorMethods": CMethod(
                    name="op_ExclusiveOr",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.IInterfaceWithOperatorMethods.op_False(TestLib.IInterfaceWithOperatorMethods) -> System.Boolean": CMethod(
                    name="op_False",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib.IInterfaceWithOperatorMethods.op_GreaterThan(TestLib.IInterfaceWithOperatorMethods, TestLib.IInterfaceWithOperatorMethods) -> System.Boolean": CMethod(
                    name="op_GreaterThan",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib.IInterfaceWithOperatorMethods.op_GreaterThanOrEqual(TestLib.IInterfaceWithOperatorMethods, TestLib.IInterfaceWithOperatorMethods) -> System.Boolean": CMethod(
                    name="op_GreaterThanOrEqual",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib.IInterfaceWithOperatorMethods.op_Increment(TestLib.IInterfaceWithOperatorMethods) -> TestLib.IInterfaceWithOperatorMethods": CMethod(
                    name="op_Increment",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.IInterfaceWithOperatorMethods.op_LessThan(TestLib.IInterfaceWithOperatorMethods, TestLib.IInterfaceWithOperatorMethods) -> System.Boolean": CMethod(
                    name="op_LessThan",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib.IInterfaceWithOperatorMethods.op_LessThanOrEqual(TestLib.IInterfaceWithOperatorMethods, TestLib.IInterfaceWithOperatorMethods) -> System.Boolean": CMethod(
                    name="op_LessThanOrEqual",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib.IInterfaceWithOperatorMethods.op_LogicalNot(TestLib.IInterfaceWithOperatorMethods) -> System.Boolean": CMethod(
                    name="op_LogicalNot",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib.IInterfaceWithOperatorMethods.op_Modulus(TestLib.IInterfaceWithOperatorMethods, TestLib.IInterfaceWithOperatorMethods) -> TestLib.IInterfaceWithOperatorMethods": CMethod(
                    name="op_Modulus",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.IInterfaceWithOperatorMethods.op_Multiply(TestLib.IInterfaceWithOperatorMethods, TestLib.IInterfaceWithOperatorMethods) -> TestLib.IInterfaceWithOperatorMethods": CMethod(
                    name="op_Multiply",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.IInterfaceWithOperatorMethods.op_OnesComplement(TestLib.IInterfaceWithOperatorMethods) -> TestLib.IInterfaceWithOperatorMethods": CMethod(
                    name="op_OnesComplement",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.IInterfaceWithOperatorMethods.op_Subtraction(TestLib.IInterfaceWithOperatorMethods, TestLib.IInterfaceWithOperatorMethods) -> TestLib.IInterfaceWithOperatorMethods": CMethod(
                    name="op_Subtraction",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.IInterfaceWithOperatorMethods.op_True(TestLib.IInterfaceWithOperatorMethods) -> System.Boolean": CMethod(
                    name="op_True",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib.IInterfaceWithOperatorMethods.op_UnaryNegation(TestLib.IInterfaceWithOperatorMethods) -> TestLib.IInterfaceWithOperatorMethods": CMethod(
                    name="op_UnaryNegation",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib.IInterfaceWithOperatorMethods.op_UnaryPlus(TestLib.IInterfaceWithOperatorMethods) -> TestLib.IInterfaceWithOperatorMethods": CMethod(
                    name="op_UnaryPlus",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
            },
            dunder_methods={
                "TestLib.IInterfaceWithOperatorMethods.__add__(TestLib.IInterfaceWithOperatorMethods) -> TestLib.IInterfaceWithOperatorMethods": CMethod(
                    name="__add__",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib.IInterfaceWithOperatorMethods.__and__(TestLib.IInterfaceWithOperatorMethods) -> TestLib.IInterfaceWithOperatorMethods": CMethod(
                    name="__and__",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib.IInterfaceWithOperatorMethods.__ge__(TestLib.IInterfaceWithOperatorMethods) -> System.Boolean": CMethod(
                    name="__ge__",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib.IInterfaceWithOperatorMethods.__gt__(TestLib.IInterfaceWithOperatorMethods) -> System.Boolean": CMethod(
                    name="__gt__",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib.IInterfaceWithOperatorMethods.__invert__() -> TestLib.IInterfaceWithOperatorMethods": CMethod(
                    name="__invert__",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(),
                    returns=(CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib.IInterfaceWithOperatorMethods.__le__(TestLib.IInterfaceWithOperatorMethods) -> System.Boolean": CMethod(
                    name="__le__",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib.IInterfaceWithOperatorMethods.__lt__(TestLib.IInterfaceWithOperatorMethods) -> System.Boolean": CMethod(
                    name="__lt__",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib.IInterfaceWithOperatorMethods.__mod__(TestLib.IInterfaceWithOperatorMethods) -> TestLib.IInterfaceWithOperatorMethods": CMethod(
                    name="__mod__",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib.IInterfaceWithOperatorMethods.__mul__(TestLib.IInterfaceWithOperatorMethods) -> TestLib.IInterfaceWithOperatorMethods": CMethod(
                    name="__mul__",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib.IInterfaceWithOperatorMethods.__neg__() -> TestLib.IInterfaceWithOperatorMethods": CMethod(
                    name="__neg__",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(),
                    returns=(CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib.IInterfaceWithOperatorMethods.__or__(TestLib.IInterfaceWithOperatorMethods) -> TestLib.IInterfaceWithOperatorMethods": CMethod(
                    name="__or__",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib.IInterfaceWithOperatorMethods.__pos__() -> TestLib.IInterfaceWithOperatorMethods": CMethod(
                    name="__pos__",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(),
                    returns=(CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib.IInterfaceWithOperatorMethods.__sub__(TestLib.IInterfaceWithOperatorMethods) -> TestLib.IInterfaceWithOperatorMethods": CMethod(
                    name="__sub__",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib.IInterfaceWithOperatorMethods.__truediv__(TestLib.IInterfaceWithOperatorMethods) -> TestLib.IInterfaceWithOperatorMethods": CMethod(
                    name="__truediv__",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib.IInterfaceWithOperatorMethods.__xor__(TestLib.IInterfaceWithOperatorMethods) -> TestLib.IInterfaceWithOperatorMethods": CMethod(
                    name="__xor__",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    returns=(CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),),
                ),
            },
            events={},
            nested={},
        )

    def test_from_info_methods_collection(self) -> None:
        type_info: TypeInfo = self.get_type("IInterfaceWithCollectionMethods")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCInterface(
            interface=cast(CInterface, type_def),
            name="IInterfaceWithCollectionMethods",
            namespace="TestLib",
            generic_args=(),
            interfaces=(
                CType(name="IEnumerable", namespace="System.Collections"),
                CType(
                    name="ICollection",
                    namespace="System.Collections.Generic",
                    inner=(CType(name="Int32", namespace="System"),),
                ),
                CType(
                    name="IEnumerable",
                    namespace="System.Collections.Generic",
                    inner=(CType(name="Int32", namespace="System"),),
                ),
            ),
            fields={},
            properties={
                "System.Collections.Generic.ICollection[System.Int32].Count": CProperty(
                    name="Count",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="Int32", namespace="System"),),
                    ),
                    type=CType(name="Int32", namespace="System"),
                ),
                "System.Collections.Generic.ICollection[System.Int32].IsReadOnly": CProperty(
                    name="IsReadOnly",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="Int32", namespace="System"),),
                    ),
                    type=CType(name="Boolean", namespace="System"),
                ),
            },
            methods={
                "System.Collections.Generic.ICollection[System.Int32].Add(System.Int32) -> System.Void": CMethod(
                    name="Add",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="Int32", namespace="System"),),
                    ),
                    parameters=(
                        CParameter(name="item", type=CType(name="Int32", namespace="System")),
                    ),
                    returns=(CType(name="Void", namespace="System"),),
                ),
                "System.Collections.Generic.ICollection[System.Int32].Clear() -> System.Void": CMethod(
                    name="Clear",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="Int32", namespace="System"),),
                    ),
                    parameters=(),
                    returns=(CType(name="Void", namespace="System"),),
                ),
                "System.Collections.Generic.ICollection[System.Int32].Contains(System.Int32) -> System.Boolean": CMethod(
                    name="Contains",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="Int32", namespace="System"),),
                    ),
                    parameters=(
                        CParameter(name="item", type=CType(name="Int32", namespace="System")),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Collections.Generic.ICollection[System.Int32].CopyTo(System.Int32, System.Int32) -> System.Void": CMethod(
                    name="CopyTo",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="Int32", namespace="System"),),
                    ),
                    parameters=(
                        CParameter(name="array", type=CType(name="Int32", namespace="System")),
                        CParameter(name="arrayIndex", type=CType(name="Int32", namespace="System")),
                    ),
                    returns=(CType(name="Void", namespace="System"),),
                ),
                "System.Collections.IEnumerable.GetEnumerator() -> System.Collections.IEnumerator": CMethod(
                    name="GetEnumerator",
                    declaring_type=CType(name="IEnumerable", namespace="System.Collections"),
                    parameters=(),
                    returns=(CType(name="IEnumerator", namespace="System.Collections"),),
                ),
                "System.Collections.Generic.ICollection[System.Int32].Remove(System.Int32) -> System.Boolean": CMethod(
                    name="Remove",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="Int32", namespace="System"),),
                    ),
                    parameters=(
                        CParameter(name="item", type=CType(name="Int32", namespace="System")),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
            },
            dunder_methods={
                "TestLib.IInterfaceWithCollectionMethods.__contains__(System.Int32) -> bool": CMethod(
                    name="__contains__",
                    declaring_type=CType(
                        name="IInterfaceWithCollectionMethods",
                        namespace="TestLib",
                    ),
                    parameters=(
                        CParameter(name="value", type=CType(name="Int32", namespace="System")),
                    ),
                    returns=(CType(name="bool"),),
                ),
                "TestLib.IInterfaceWithCollectionMethods.__iter__() -> typing.Iterator[System.Int32]": CMethod(
                    name="__iter__",
                    declaring_type=CType(
                        name="IInterfaceWithCollectionMethods", namespace="TestLib"
                    ),
                    parameters=(),
                    returns=(
                        CType(
                            name="Iterator",
                            namespace="typing",
                            inner=(CType(name="Int32", namespace="System"),),
                        ),
                    ),
                ),
                "TestLib.IInterfaceWithCollectionMethods.__iter__() -> typing.Iterator[object]": CMethod(
                    name="__iter__",
                    declaring_type=CType(
                        name="IInterfaceWithCollectionMethods", namespace="TestLib"
                    ),
                    parameters=(),
                    returns=(
                        CType(
                            name="Iterator",
                            namespace="typing",
                            inner=(CType(name="object"),),
                        ),
                    ),
                ),
                "TestLib.IInterfaceWithCollectionMethods.__len__() -> int": CMethod(
                    name="__len__",
                    declaring_type=CType(
                        name="IInterfaceWithCollectionMethods", namespace="TestLib"
                    ),
                    parameters=(),
                    returns=(CType(name="int"),),
                ),
            },
            events={},
            nested={},
        )

    def test_from_info_events(self) -> None:
        type_info: TypeInfo = self.get_type("IInterfaceWithEvents")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCInterface(
            interface=cast(CInterface, type_def),
            name="IInterfaceWithEvents",
            namespace="TestLib",
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            dunder_methods={},
            events={
                "TestLib.IInterfaceWithEvents.Event -> (System.EventHandler)": CEvent(
                    name="Event",
                    declaring_type=CType(name="IInterfaceWithEvents", namespace="TestLib"),
                    type=CType(name="EventHandler", namespace="System"),
                ),
                "TestLib.IInterfaceWithEvents.EventWithArgs -> (System.EventHandler[System.EventArgs])": CEvent(
                    name="EventWithArgs",
                    declaring_type=CType(name="IInterfaceWithEvents", namespace="TestLib"),
                    type=CType(
                        name="EventHandler",
                        namespace="System",
                        inner=(CType(name="EventArgs", namespace="System"),),
                    ),
                ),
            },
            nested={},
        )

    def test_from_info_nested(self) -> None:
        type_info: TypeInfo = self.get_type("IInterfaceWithNested")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCInterface(
            interface=cast(CInterface, type_def),
            name="IInterfaceWithNested",
            namespace="TestLib",
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            dunder_methods={},
            events={},
            nested={
                "TestLib.INestedInterface": CInterface(
                    name="INestedInterface",
                    namespace="TestLib",
                    generic_args=(),
                    interfaces=(),
                    fields={},
                    properties={},
                    methods={},
                    dunder_methods={},
                    events={},
                    nested={},
                ),
                "TestLib.NestedClass": CClass(
                    name="NestedClass",
                    namespace="TestLib",
                    abstract=False,
                    generic_args=(),
                    super_class=CType(name="Object", namespace="System"),
                    interfaces=(),
                    fields={},
                    constructors={
                        "TestLib.NestedClass.__init__()": CConstructor(
                            declaring_type=CType(name="NestedClass", namespace="TestLib"),
                            parameters=(),
                        ),
                    },
                    properties={},
                    methods={
                        "System.Object.Equals(System.Object) -> System.Boolean": CMethod(
                            name="Equals",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(
                                CParameter(
                                    name="obj",
                                    type=CType(name="Object", namespace="System"),
                                ),
                            ),
                            returns=(CType(name="Boolean", namespace="System"),),
                        ),
                        "System.Object.GetHashCode() -> System.Int32": CMethod(
                            name="GetHashCode",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            returns=(CType(name="Int32", namespace="System"),),
                        ),
                        "System.Object.GetType() -> System.Type": CMethod(
                            name="GetType",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            returns=(CType(name="Type", namespace="System"),),
                        ),
                        "System.Object.ToString() -> System.String": CMethod(
                            name="ToString",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            returns=(CType(name="String", namespace="System"),),
                        ),
                    },
                    dunder_methods={},
                    events={},
                    nested={},
                ),
                "TestLib.NestedDelegate": CDelegate(
                    name="NestedDelegate",
                    namespace="TestLib",
                    parameters=(),
                    return_type=CType(name="Void", namespace="System"),
                ),
                "TestLib.NestedEnum": CEnum(
                    name="NestedEnum",
                    namespace="TestLib",
                    fields=(),
                ),
                "TestLib.NestedStruct": CStruct(
                    name="NestedStruct",
                    namespace="TestLib",
                    abstract=False,
                    generic_args=(),
                    super_class=CType(name="ValueType", namespace="System"),
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={
                        "System.Object.Equals(System.Object) -> System.Boolean": CMethod(
                            name="Equals",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(
                                CParameter(
                                    name="obj",
                                    type=CType(name="Object", namespace="System"),
                                ),
                            ),
                            returns=(CType(name="Boolean", namespace="System"),),
                        ),
                        "System.Object.GetHashCode() -> System.Int32": CMethod(
                            name="GetHashCode",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            returns=(CType(name="Int32", namespace="System"),),
                        ),
                        "System.Object.GetType() -> System.Type": CMethod(
                            name="GetType",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            returns=(CType(name="Type", namespace="System"),),
                        ),
                        "System.Object.ToString() -> System.String": CMethod(
                            name="ToString",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            returns=(CType(name="String", namespace="System"),),
                        ),
                    },
                    dunder_methods={},
                    events={},
                    nested={},
                ),
            },
        )

    def test_json_generic(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            generic_args=(CType(name="T", namespace="Namespace", generic=True),),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            dunder_methods={},
            events={},
            nested={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "interface",
                "name": "Interface",
                "namespace": "Namespace",
                "generic_args": ("Namespace.$T",),
                "interfaces": (),
                "fields": {},
                "properties": {},
                "methods": {},
                "dunder_methods": {},
                "events": {},
                "nested": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_generic_multi(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            generic_args=(
                CType(name="U", namespace="Namespace", generic=True),
                CType(name="V", namespace="Namespace", generic=True),
            ),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            dunder_methods={},
            events={},
            nested={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "interface",
                "name": "Interface",
                "namespace": "Namespace",
                "generic_args": ("Namespace.$U", "Namespace.$V"),
                "interfaces": (),
                "fields": {},
                "properties": {},
                "methods": {},
                "dunder_methods": {},
                "events": {},
                "nested": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_generic_interfaces(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            generic_args=(),
            interfaces=(
                CType(name="InterfaceA", namespace="Namespace"),
                CType(name="InterfaceB", namespace="Namespace"),
            ),
            fields={},
            properties={},
            methods={},
            dunder_methods={},
            events={},
            nested={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "interface",
                "name": "Interface",
                "namespace": "Namespace",
                "generic_args": (),
                "interfaces": ("Namespace.InterfaceA", "Namespace.InterfaceB"),
                "fields": {},
                "properties": {},
                "methods": {},
                "dunder_methods": {},
                "events": {},
                "nested": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_generic_fields(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            generic_args=(),
            interfaces=(),
            fields={
                "Namespace.Interface.StaticFieldA": CField(
                    name="StaticFieldA",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    returns=CType(name="Type", namespace="Namespace"),
                    static=True,
                ),
                "Namespace.Interface.StaticFieldB": CField(
                    name="StaticFieldB",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    returns=CType(name="Type", namespace="Namespace"),
                    static=True,
                ),
                "Namespace.Interface.StaticFieldC": CField(
                    name="StaticFieldC",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    returns=CType(name="Type", namespace="Namespace"),
                    static=True,
                ),
            },
            properties={},
            methods={},
            dunder_methods={},
            events={},
            nested={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "interface",
                "name": "Interface",
                "namespace": "Namespace",
                "generic_args": (),
                "interfaces": (),
                "fields": {
                    "Namespace.Interface.StaticFieldA": {
                        "name": "StaticFieldA",
                        "declaring_type": "Namespace.Interface",
                        "returns": "Namespace.Type",
                        "static": True,
                    },
                    "Namespace.Interface.StaticFieldB": {
                        "name": "StaticFieldB",
                        "declaring_type": "Namespace.Interface",
                        "returns": "Namespace.Type",
                        "static": True,
                    },
                    "Namespace.Interface.StaticFieldC": {
                        "name": "StaticFieldC",
                        "declaring_type": "Namespace.Interface",
                        "returns": "Namespace.Type",
                        "static": True,
                    },
                },
                "properties": {},
                "methods": {},
                "dunder_methods": {},
                "events": {},
                "nested": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_generic_properties(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            generic_args=(),
            interfaces=(),
            fields={},
            properties={
                "Namespace.Interface.InstanceProperty0": CProperty(
                    name="InstanceProperty0",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                ),
                "Namespace.Interface.InstanceProperty1": CProperty(
                    name="InstanceProperty1",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                ),
                "Namespace.Interface.InstanceProperty2": CProperty(
                    name="InstanceProperty2",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                ),
                "Namespace.Interface.InstanceReadOnlyProperty0": CProperty(
                    name="InstanceReadOnlyProperty0",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="Int32", namespace="System"),
                ),
                "Namespace.Interface.InstanceReadOnlyProperty1": CProperty(
                    name="InstanceReadOnlyProperty1",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="Int32", namespace="System"),
                ),
                "Namespace.Interface.InstanceReadOnlyProperty2": CProperty(
                    name="InstanceReadOnlyProperty2",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="Int32", namespace="System"),
                ),
                "Namespace.Interface.StaticProperty0": CProperty(
                    name="StaticProperty0",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                    static=True,
                ),
                "Namespace.Interface.StaticProperty1": CProperty(
                    name="StaticProperty1",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                    static=True,
                ),
                "Namespace.Interface.StaticProperty2": CProperty(
                    name="StaticProperty2",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                    static=True,
                ),
                "Namespace.Interface.StaticReadOnlyProperty0": CProperty(
                    name="StaticReadOnlyProperty0",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
                "Namespace.Interface.StaticReadOnlyProperty1": CProperty(
                    name="StaticReadOnlyProperty1",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
                "Namespace.Interface.StaticReadOnlyProperty2": CProperty(
                    name="StaticReadOnlyProperty2",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
            },
            methods={},
            dunder_methods={},
            events={},
            nested={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "interface",
                "name": "Interface",
                "namespace": "Namespace",
                "generic_args": (),
                "interfaces": (),
                "fields": {},
                "properties": {
                    "Namespace.Interface.InstanceProperty0": {
                        "name": "InstanceProperty0",
                        "declaring_type": "Namespace.Interface",
                        "type": "System.Int32",
                        "setter": True,
                        "static": False,
                    },
                    "Namespace.Interface.InstanceProperty1": {
                        "name": "InstanceProperty1",
                        "declaring_type": "Namespace.Interface",
                        "type": "System.Int32",
                        "setter": True,
                        "static": False,
                    },
                    "Namespace.Interface.InstanceProperty2": {
                        "name": "InstanceProperty2",
                        "declaring_type": "Namespace.Interface",
                        "type": "System.Int32",
                        "setter": True,
                        "static": False,
                    },
                    "Namespace.Interface.InstanceReadOnlyProperty0": {
                        "name": "InstanceReadOnlyProperty0",
                        "declaring_type": "Namespace.Interface",
                        "type": "System.Int32",
                        "setter": False,
                        "static": False,
                    },
                    "Namespace.Interface.InstanceReadOnlyProperty1": {
                        "name": "InstanceReadOnlyProperty1",
                        "declaring_type": "Namespace.Interface",
                        "type": "System.Int32",
                        "setter": False,
                        "static": False,
                    },
                    "Namespace.Interface.InstanceReadOnlyProperty2": {
                        "name": "InstanceReadOnlyProperty2",
                        "declaring_type": "Namespace.Interface",
                        "type": "System.Int32",
                        "setter": False,
                        "static": False,
                    },
                    "Namespace.Interface.StaticProperty0": {
                        "name": "StaticProperty0",
                        "declaring_type": "Namespace.Interface",
                        "type": "System.Int32",
                        "setter": True,
                        "static": True,
                    },
                    "Namespace.Interface.StaticProperty1": {
                        "name": "StaticProperty1",
                        "declaring_type": "Namespace.Interface",
                        "type": "System.Int32",
                        "setter": True,
                        "static": True,
                    },
                    "Namespace.Interface.StaticProperty2": {
                        "name": "StaticProperty2",
                        "declaring_type": "Namespace.Interface",
                        "type": "System.Int32",
                        "setter": True,
                        "static": True,
                    },
                    "Namespace.Interface.StaticReadOnlyProperty0": {
                        "name": "StaticReadOnlyProperty0",
                        "declaring_type": "Namespace.Interface",
                        "type": "System.Int32",
                        "setter": False,
                        "static": True,
                    },
                    "Namespace.Interface.StaticReadOnlyProperty1": {
                        "name": "StaticReadOnlyProperty1",
                        "declaring_type": "Namespace.Interface",
                        "type": "System.Int32",
                        "setter": False,
                        "static": True,
                    },
                    "Namespace.Interface.StaticReadOnlyProperty2": {
                        "name": "StaticReadOnlyProperty2",
                        "declaring_type": "Namespace.Interface",
                        "type": "System.Int32",
                        "setter": False,
                        "static": True,
                    },
                },
                "methods": {},
                "dunder_methods": {},
                "events": {},
                "nested": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_generic_methods(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={
                "Namespace.Interface.InstanceMethodWithDefaultParam(System.Int32) -> System.Int32": CMethod(
                    name="InstanceMethodWithDefaultParam",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System"),
                            default=True,
                        ),
                    ),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "Namespace.Interface.InstanceMethodWithNullableDefaultParam(System.Int32?) -> System.Int32": CMethod(
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
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "Namespace.Interface.InstanceMethodWithNullableOutParam(System.*Int32?) -> System.Int32, System.*Int32?": CMethod(
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
                    returns=(
                        CType(name="Int32", namespace="System"),
                        CType(name="Int32", namespace="System", reference=True, nullable=True),
                    ),
                ),
                "Namespace.Interface.InstanceMethodWithNullableParam(System.Int32?) -> System.Int32": CMethod(
                    name="InstanceMethodWithNullableParam",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System", nullable=True),
                        ),
                    ),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "Namespace.Interface.InstanceMethodWithOutParam(System.*Int32) -> System.Int32, System.*Int32": CMethod(
                    name="InstanceMethodWithOutParam",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System", reference=True),
                            out=True,
                        ),
                    ),
                    returns=(
                        CType(name="Int32", namespace="System"),
                        CType(name="Int32", namespace="System", reference=True),
                    ),
                ),
                "Namespace.Interface.InstanceMethodWithParams() -> System.Int32": CMethod(
                    name="InstanceMethodWithParams",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "Namespace.Interface.InstanceMethodWithParams(System.Int32) -> System.Int32": CMethod(
                    name="InstanceMethodWithParams",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                    ),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
                "Namespace.Interface.InstanceMethodWithParams(System.Int32, System.Int32) -> System.Int32": CMethod(
                    name="InstanceMethodWithParams",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                        CParameter(name="param1", type=CType(name="Int32", namespace="System")),
                    ),
                    returns=(CType(name="Int32", namespace="System"),),
                ),
            },
            dunder_methods={},
            events={},
            nested={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "interface",
                "name": "Interface",
                "namespace": "Namespace",
                "generic_args": (),
                "interfaces": (),
                "fields": {},
                "properties": {},
                "methods": {
                    "Namespace.Interface.InstanceMethodWithDefaultParam(System.Int32) -> System.Int32": {
                        "name": "InstanceMethodWithDefaultParam",
                        "declaring_type": "Namespace.Interface",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "System.Int32",
                                "default": True,
                                "out": False,
                            },
                        ),
                        "returns": ("System.Int32",),
                        "static": False,
                    },
                    "Namespace.Interface.InstanceMethodWithNullableDefaultParam(System.Int32?) -> System.Int32": {
                        "name": "InstanceMethodWithNullableDefaultParam",
                        "declaring_type": "Namespace.Interface",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "System.Int32?",
                                "default": True,
                                "out": False,
                            },
                        ),
                        "returns": ("System.Int32",),
                        "static": False,
                    },
                    "Namespace.Interface.InstanceMethodWithNullableOutParam(System.*Int32?) -> System.Int32, System.*Int32?": {
                        "name": "InstanceMethodWithNullableOutParam",
                        "declaring_type": "Namespace.Interface",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "System.*Int32?",
                                "default": False,
                                "out": True,
                            },
                        ),
                        "returns": ("System.Int32", "System.*Int32?"),
                        "static": False,
                    },
                    "Namespace.Interface.InstanceMethodWithNullableParam(System.Int32?) -> System.Int32": {
                        "name": "InstanceMethodWithNullableParam",
                        "declaring_type": "Namespace.Interface",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "System.Int32?",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("System.Int32",),
                        "static": False,
                    },
                    "Namespace.Interface.InstanceMethodWithOutParam(System.*Int32) -> System.Int32, System.*Int32": {
                        "name": "InstanceMethodWithOutParam",
                        "declaring_type": "Namespace.Interface",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "System.*Int32",
                                "default": False,
                                "out": True,
                            },
                        ),
                        "returns": ("System.Int32", "System.*Int32"),
                        "static": False,
                    },
                    "Namespace.Interface.InstanceMethodWithParams() -> System.Int32": {
                        "name": "InstanceMethodWithParams",
                        "declaring_type": "Namespace.Interface",
                        "parameters": (),
                        "returns": ("System.Int32",),
                        "static": False,
                    },
                    "Namespace.Interface.InstanceMethodWithParams(System.Int32) -> System.Int32": {
                        "name": "InstanceMethodWithParams",
                        "declaring_type": "Namespace.Interface",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "System.Int32",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("System.Int32",),
                        "static": False,
                    },
                    "Namespace.Interface.InstanceMethodWithParams(System.Int32, System.Int32) -> System.Int32": {
                        "name": "InstanceMethodWithParams",
                        "declaring_type": "Namespace.Interface",
                        "parameters": (
                            {
                                "name": "param0",
                                "type": "System.Int32",
                                "default": False,
                                "out": False,
                            },
                            {
                                "name": "param1",
                                "type": "System.Int32",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("System.Int32",),
                        "static": False,
                    },
                },
                "dunder_methods": {},
                "events": {},
                "nested": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_generic_methods_dunder(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            dunder_methods={
                "Namespace.Interface.__add__(Namespace.Interface) -> Namespace.Interface": CMethod(
                    name="__add__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other", type=CType(name="Interface", namespace="Namespace")
                        ),
                    ),
                    returns=(CType(name="Interface", namespace="Namespace"),),
                ),
                "Namespace.Interface.__and__(Namespace.Interface) -> Namespace.Interface": CMethod(
                    name="__and__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other", type=CType(name="Interface", namespace="Namespace")
                        ),
                    ),
                    returns=(CType(name="Interface", namespace="Namespace"),),
                ),
                "Namespace.Interface.__ge__(Namespace.Interface) -> System.Boolean": CMethod(
                    name="__ge__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other", type=CType(name="Interface", namespace="Namespace")
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "Namespace.Interface.__gt__(Namespace.Interface) -> System.Boolean": CMethod(
                    name="__gt__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other", type=CType(name="Interface", namespace="Namespace")
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "Namespace.Interface.__invert__() -> Namespace.Interface": CMethod(
                    name="__invert__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(),
                    returns=(CType(name="Interface", namespace="Namespace"),),
                ),
                "Namespace.Interface.__le__(Namespace.Interface) -> System.Boolean": CMethod(
                    name="__le__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other", type=CType(name="Interface", namespace="Namespace")
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "Namespace.Interface.__lt__(Namespace.Interface) -> System.Boolean": CMethod(
                    name="__lt__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other", type=CType(name="Interface", namespace="Namespace")
                        ),
                    ),
                    returns=(CType(name="Boolean", namespace="System"),),
                ),
                "Namespace.Interface.__mod__(Namespace.Interface) -> Namespace.Interface": CMethod(
                    name="__mod__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other", type=CType(name="Interface", namespace="Namespace")
                        ),
                    ),
                    returns=(CType(name="Interface", namespace="Namespace"),),
                ),
                "Namespace.Interface.__mul__(Namespace.Interface) -> Namespace.Interface": CMethod(
                    name="__mul__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other", type=CType(name="Interface", namespace="Namespace")
                        ),
                    ),
                    returns=(CType(name="Interface", namespace="Namespace"),),
                ),
                "Namespace.Interface.__neg__() -> Namespace.Interface": CMethod(
                    name="__neg__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(),
                    returns=(CType(name="Interface", namespace="Namespace"),),
                ),
                "Namespace.Interface.__or__(Namespace.Interface) -> Namespace.Interface": CMethod(
                    name="__or__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other", type=CType(name="Interface", namespace="Namespace")
                        ),
                    ),
                    returns=(CType(name="Interface", namespace="Namespace"),),
                ),
                "Namespace.Interface.__pos__() -> Namespace.Interface": CMethod(
                    name="__pos__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(),
                    returns=(CType(name="Interface", namespace="Namespace"),),
                ),
                "Namespace.Interface.__sub__(Namespace.Interface) -> Namespace.Interface": CMethod(
                    name="__sub__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other", type=CType(name="Interface", namespace="Namespace")
                        ),
                    ),
                    returns=(CType(name="Interface", namespace="Namespace"),),
                ),
                "Namespace.Interface.__truediv__(Namespace.Interface) -> Namespace.Interface": CMethod(
                    name="__truediv__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other", type=CType(name="Interface", namespace="Namespace")
                        ),
                    ),
                    returns=(CType(name="Interface", namespace="Namespace"),),
                ),
                "Namespace.Interface.__xor__(Namespace.Interface) -> Namespace.Interface": CMethod(
                    name="__xor__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(
                            name="other", type=CType(name="Interface", namespace="Namespace")
                        ),
                    ),
                    returns=(CType(name="Interface", namespace="Namespace"),),
                ),
            },
            events={},
            nested={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "interface",
                "name": "Interface",
                "namespace": "Namespace",
                "generic_args": (),
                "interfaces": (),
                "fields": {},
                "properties": {},
                "methods": {},
                "dunder_methods": {
                    "Namespace.Interface.__add__(Namespace.Interface) -> Namespace.Interface": {
                        "name": "__add__",
                        "declaring_type": "Namespace.Interface",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Interface",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Interface",),
                        "static": False,
                    },
                    "Namespace.Interface.__and__(Namespace.Interface) -> Namespace.Interface": {
                        "name": "__and__",
                        "declaring_type": "Namespace.Interface",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Interface",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Interface",),
                        "static": False,
                    },
                    "Namespace.Interface.__ge__(Namespace.Interface) -> System.Boolean": {
                        "name": "__ge__",
                        "declaring_type": "Namespace.Interface",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Interface",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("System.Boolean",),
                        "static": False,
                    },
                    "Namespace.Interface.__gt__(Namespace.Interface) -> System.Boolean": {
                        "name": "__gt__",
                        "declaring_type": "Namespace.Interface",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Interface",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("System.Boolean",),
                        "static": False,
                    },
                    "Namespace.Interface.__invert__() -> Namespace.Interface": {
                        "name": "__invert__",
                        "declaring_type": "Namespace.Interface",
                        "parameters": (),
                        "returns": ("Namespace.Interface",),
                        "static": False,
                    },
                    "Namespace.Interface.__le__(Namespace.Interface) -> System.Boolean": {
                        "name": "__le__",
                        "declaring_type": "Namespace.Interface",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Interface",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("System.Boolean",),
                        "static": False,
                    },
                    "Namespace.Interface.__lt__(Namespace.Interface) -> System.Boolean": {
                        "name": "__lt__",
                        "declaring_type": "Namespace.Interface",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Interface",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("System.Boolean",),
                        "static": False,
                    },
                    "Namespace.Interface.__mod__(Namespace.Interface) -> Namespace.Interface": {
                        "name": "__mod__",
                        "declaring_type": "Namespace.Interface",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Interface",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Interface",),
                        "static": False,
                    },
                    "Namespace.Interface.__mul__(Namespace.Interface) -> Namespace.Interface": {
                        "name": "__mul__",
                        "declaring_type": "Namespace.Interface",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Interface",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Interface",),
                        "static": False,
                    },
                    "Namespace.Interface.__neg__() -> Namespace.Interface": {
                        "name": "__neg__",
                        "declaring_type": "Namespace.Interface",
                        "parameters": (),
                        "returns": ("Namespace.Interface",),
                        "static": False,
                    },
                    "Namespace.Interface.__or__(Namespace.Interface) -> Namespace.Interface": {
                        "name": "__or__",
                        "declaring_type": "Namespace.Interface",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Interface",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Interface",),
                        "static": False,
                    },
                    "Namespace.Interface.__pos__() -> Namespace.Interface": {
                        "name": "__pos__",
                        "declaring_type": "Namespace.Interface",
                        "parameters": (),
                        "returns": ("Namespace.Interface",),
                        "static": False,
                    },
                    "Namespace.Interface.__sub__(Namespace.Interface) -> Namespace.Interface": {
                        "name": "__sub__",
                        "declaring_type": "Namespace.Interface",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Interface",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Interface",),
                        "static": False,
                    },
                    "Namespace.Interface.__truediv__(Namespace.Interface) -> Namespace.Interface": {
                        "name": "__truediv__",
                        "declaring_type": "Namespace.Interface",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Interface",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Interface",),
                        "static": False,
                    },
                    "Namespace.Interface.__xor__(Namespace.Interface) -> Namespace.Interface": {
                        "name": "__xor__",
                        "declaring_type": "Namespace.Interface",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "Namespace.Interface",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("Namespace.Interface",),
                        "static": False,
                    },
                },
                "events": {},
                "nested": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_generic_methods_collection(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            dunder_methods={
                "Namespace.Interface.__contains__(System.Int32) -> bool": CMethod(
                    name="__contains__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(
                        CParameter(name="value", type=CType(name="Int32", namespace="System")),
                    ),
                    returns=(CType(name="bool"),),
                ),
                "Namespace.Interface.__iter__() -> typing.Iterator[System.Int32]": CMethod(
                    name="__iter__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(),
                    returns=(
                        CType(
                            name="Iterator",
                            namespace="typing",
                            inner=(CType(name="Int32", namespace="System"),),
                        ),
                    ),
                ),
                "Namespace.Interface.__iter__() -> typing.Iterator[object]": CMethod(
                    name="__iter__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(),
                    returns=(
                        CType(name="Iterator", namespace="typing", inner=(CType(name="object"),)),
                    ),
                ),
                "Namespace.Interface.__len__() -> int": CMethod(
                    name="__len__",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    parameters=(),
                    returns=(CType(name="int"),),
                ),
            },
            events={},
            nested={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "interface",
                "name": "Interface",
                "namespace": "Namespace",
                "generic_args": (),
                "interfaces": (),
                "fields": {},
                "properties": {},
                "methods": {},
                "dunder_methods": {
                    "Namespace.Interface.__contains__(System.Int32) -> bool": {
                        "name": "__contains__",
                        "declaring_type": "Namespace.Interface",
                        "parameters": (
                            {
                                "name": "value",
                                "type": "System.Int32",
                                "default": False,
                                "out": False,
                            },
                        ),
                        "returns": ("bool",),
                        "static": False,
                    },
                    "Namespace.Interface.__iter__() -> typing.Iterator[System.Int32]": {
                        "name": "__iter__",
                        "declaring_type": "Namespace.Interface",
                        "parameters": (),
                        "returns": ("typing.Iterator[System.Int32]",),
                        "static": False,
                    },
                    "Namespace.Interface.__iter__() -> typing.Iterator[object]": {
                        "name": "__iter__",
                        "declaring_type": "Namespace.Interface",
                        "parameters": (),
                        "returns": ("typing.Iterator[object]",),
                        "static": False,
                    },
                    "Namespace.Interface.__len__() -> int": {
                        "name": "__len__",
                        "declaring_type": "Namespace.Interface",
                        "parameters": (),
                        "returns": ("int",),
                        "static": False,
                    },
                },
                "events": {},
                "nested": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_generic_events(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            dunder_methods={},
            events={
                "Namespace.Interface.Event -> (System.EventHandler)": CEvent(
                    name="Event",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(name="EventHandler", namespace="System"),
                ),
                "Namespace.Interface.EventWithArgs -> (System.EventHandler[System.EventArgs])": CEvent(
                    name="EventWithArgs",
                    declaring_type=CType(name="Interface", namespace="Namespace"),
                    type=CType(
                        name="EventHandler",
                        namespace="System",
                        inner=(CType(name="EventArgs", namespace="System"),),
                    ),
                ),
            },
            nested={},
        )
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "type": "interface",
                "name": "Interface",
                "namespace": "Namespace",
                "generic_args": (),
                "interfaces": (),
                "fields": {},
                "properties": {},
                "methods": {},
                "dunder_methods": {},
                "events": {
                    "Namespace.Interface.Event -> (System.EventHandler)": {
                        "name": "Event",
                        "declaring_type": "Namespace.Interface",
                        "type": "System.EventHandler",
                    },
                    "Namespace.Interface.EventWithArgs -> (System.EventHandler[System.EventArgs])": {
                        "name": "EventWithArgs",
                        "declaring_type": "Namespace.Interface",
                        "type": "System.EventHandler[System.EventArgs]",
                    },
                },
                "nested": {},
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_json_generic_nested(self) -> None:
        type_def: CInterface = CInterface(
            name="Interface",
            namespace="Namespace",
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            dunder_methods={},
            events={},
            nested={
                "Namespace.INestedInterface": CInterface(
                    name="INestedInterface",
                    namespace="Namespace",
                    generic_args=(),
                    interfaces=(),
                    fields={},
                    properties={},
                    methods={},
                    dunder_methods={},
                    events={},
                    nested={},
                ),
                "Namespace.NestedClass": CClass(
                    name="NestedClass",
                    namespace="Namespace",
                    abstract=False,
                    generic_args=(),
                    super_class=None,
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    dunder_methods={},
                    events={},
                    nested={},
                ),
                "Namespace.NestedDelegate": CDelegate(
                    name="NestedDelegate",
                    namespace="Namespace",
                    parameters=(),
                    return_type=CType(name="Void", namespace="System"),
                ),
                "Namespace.NestedEnum": CEnum(
                    name="NestedEnum",
                    namespace="Namespace",
                    fields=(),
                ),
                "Namespace.NestedStruct": CStruct(
                    name="NestedStruct",
                    namespace="Namespace",
                    abstract=False,
                    generic_args=(),
                    super_class=CType(name="ValueType", namespace="System"),
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={},
                    dunder_methods={},
                    events={},
                    nested={},
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
                "generic_args": (),
                "interfaces": (),
                "fields": {},
                "properties": {},
                "methods": {},
                "dunder_methods": {},
                "events": {},
                "nested": {
                    "Namespace.INestedInterface": {
                        "type": "interface",
                        "name": "INestedInterface",
                        "namespace": "Namespace",
                        "generic_args": (),
                        "interfaces": (),
                        "fields": {},
                        "properties": {},
                        "methods": {},
                        "dunder_methods": {},
                        "events": {},
                        "nested": {},
                    },
                    "Namespace.NestedClass": {
                        "type": "class",
                        "name": "NestedClass",
                        "namespace": "Namespace",
                        "abstract": False,
                        "generic_args": (),
                        "super_class": None,
                        "interfaces": (),
                        "fields": {},
                        "constructors": {},
                        "properties": {},
                        "methods": {},
                        "dunder_methods": {},
                        "events": {},
                        "nested": {},
                    },
                    "Namespace.NestedDelegate": {
                        "type": "delegate",
                        "name": "NestedDelegate",
                        "namespace": "Namespace",
                        "parameters": (),
                        "return_type": "System.Void",
                    },
                    "Namespace.NestedEnum": {
                        "type": "enum",
                        "name": "NestedEnum",
                        "namespace": "Namespace",
                        "fields": (),
                    },
                    "Namespace.NestedStruct": {
                        "type": "struct",
                        "name": "NestedStruct",
                        "namespace": "Namespace",
                        "abstract": False,
                        "generic_args": (),
                        "super_class": "System.ValueType",
                        "interfaces": (),
                        "fields": {},
                        "constructors": {},
                        "properties": {},
                        "methods": {},
                        "dunder_methods": {},
                        "events": {},
                        "nested": {},
                    },
                },
            },
            json,
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(type_def, from_json)

    def test_compare(self) -> None:
        interface0: CInterface = CInterface(
            name="InterfaceA",
            namespace="Namespace",
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            dunder_methods={},
            events={},
            nested={},
        )
        interface1: CInterface = CInterface(
            name="InterfaceB",
            namespace="Namespace",
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            dunder_methods={},
            events={},
            nested={},
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
                generic_args=(),
                interfaces=(),
                fields={},
                properties={},
                methods={},
                dunder_methods={},
                events={},
                nested={},
            ),
            CInterface(
                name="InterfaceB",
                namespace="Namespace",
                generic_args=(),
                interfaces=(),
                fields={},
                properties={},
                methods={},
                dunder_methods={},
                events={},
                nested={},
            ),
            CInterface(
                name="InterfaceC",
                namespace="Namespace",
                generic_args=(),
                interfaces=(),
                fields={},
                properties={},
                methods={},
                dunder_methods={},
                events={},
                nested={},
            ),
            CInterface(
                name="InterfaceD",
                namespace="Namespace",
                generic_args=(),
                interfaces=(),
                fields={},
                properties={},
                methods={},
                dunder_methods={},
                events={},
                nested={},
            ),
        )
        unordered: MutableSequence[CInterface] = list(ordered)
        random.shuffle(unordered)

        self.assertSequenceEqual(ordered, sorted(unordered))


class TestCEnum(TestBase):
    def test_from_info(self) -> None:
        type_info: TypeInfo = self.get_type("EnumWithFields")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCEnum(
            enum=cast(CEnum, type_def),
            name="EnumWithFields",
            namespace="TestLib",
            fields=("Field0", "Field1", "Field2", "Field3"),
        )

    def test_from_info_no_fields(self) -> None:
        type_info: TypeInfo = self.get_type("EnumWithNoFields")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCEnum(
            enum=cast(CEnum, type_def),
            name="EnumWithNoFields",
            namespace="TestLib",
            fields=(),
        )

    def test_json(self) -> None:
        enum: CEnum = CEnum(
            name="Enum",
            namespace="Namespace",
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

    def test_compare(self) -> None:
        enum0: CEnum = CEnum(
            name="EnumA",
            namespace="Namespace",
            fields=("Field0", "Field1", "Field2", "Field3"),
        )
        enum1: CEnum = CEnum(
            name="EnumB",
            namespace="Namespace",
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
                fields=("Field0", "Field1", "Field2", "Field3"),
            ),
            CEnum(
                name="EnumB",
                namespace="Namespace",
                fields=("Field0", "Field1", "Field2", "Field3"),
            ),
            CEnum(
                name="EnumC",
                namespace="Namespace",
                fields=("Field0", "Field1", "Field2", "Field3"),
            ),
            CEnum(
                name="EnumD",
                namespace="Namespace",
                fields=("Field0", "Field1", "Field2", "Field3"),
            ),
        )
        unordered: MutableSequence[CEnum] = list(ordered)
        random.shuffle(unordered)

        self.assertSequenceEqual(ordered, sorted(unordered))


class TestCDelegate(TestBase):
    def test_from_info_no_params_no_return(self) -> None:
        type_info: TypeInfo = self.get_type("DelegateWithNoParametersNoReturn")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCDelegate(
            delegate=cast(CDelegate, type_def),
            name="DelegateWithNoParametersNoReturn",
            namespace="TestLib",
            parameters=(),
            return_type=CType(name="Void", namespace="System"),
        )

    def test_from_info_no_params_return(self) -> None:
        type_info: TypeInfo = self.get_type("DelegateWithNoParametersReturn")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCDelegate(
            delegate=cast(CDelegate, type_def),
            name="DelegateWithNoParametersReturn",
            namespace="TestLib",
            parameters=(),
            return_type=CType(name="Int32", namespace="System"),
        )

    def test_from_info_params_no_return(self) -> None:
        type_info: TypeInfo = self.get_type("DelegateWithParametersNoReturn")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCDelegate(
            delegate=cast(CDelegate, type_def),
            name="DelegateWithParametersNoReturn",
            namespace="TestLib",
            parameters=(
                CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                CParameter(name="param1", type=CType(name="Int32", namespace="System")),
            ),
            return_type=CType(name="Void", namespace="System"),
        )

    def test_from_info_params_return(self) -> None:
        type_info: TypeInfo = self.get_type("DelegateWithParametersReturn")
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCDelegate(
            delegate=cast(CDelegate, type_def),
            name="DelegateWithParametersReturn",
            namespace="TestLib",
            parameters=(
                CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                CParameter(name="param1", type=CType(name="Int32", namespace="System")),
            ),
            return_type=CType(name="Int32", namespace="System"),
        )

    def test_json(self) -> None:
        delegate: CDelegate = CDelegate(
            name="Delegate",
            namespace="Namespace",
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
                "parameters": (
                    {
                        "name": "param0",
                        "type": "Namespace.Type0",
                        "default": False,
                        "out": False,
                    },
                    {
                        "name": "param1",
                        "type": "Namespace.Type1",
                        "default": False,
                        "out": False,
                    },
                ),
                "return_type": "Namespace.Type",
            },
            json,
        )

        from_json: CDelegate = CDelegate.from_json(json)

        self.assertEqual(delegate, from_json)

    def test_compare_namespace(self) -> None:
        delegate0: CDelegate = CDelegate(
            name="DelegateA",
            namespace="Namespace",
            parameters=(),
            return_type=CType(name="Type", namespace="Namespace"),
        )
        delegate1: CDelegate = CDelegate(
            name="DelegateB",
            namespace="Namespace",
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
                parameters=(),
                return_type=CType(name="Type", namespace="Namespace"),
            ),
            CDelegate(
                name="DelegateB",
                namespace="Namespace",
                parameters=(),
                return_type=CType(name="Type", namespace="Namespace"),
            ),
            CDelegate(
                name="DelegateC",
                namespace="Namespace",
                parameters=(),
                return_type=CType(name="Type", namespace="Namespace"),
            ),
            CDelegate(
                name="DelegateD",
                namespace="Namespace",
                parameters=(),
                return_type=CType(name="Type", namespace="Namespace"),
            ),
        )
        unordered: MutableSequence[CDelegate] = list(ordered)
        random.shuffle(unordered)

        self.assertSequenceEqual(ordered, sorted(unordered))


class TestCType(TestBase):
    def test_from_info_simple(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithSuper")
        c_type: CType = CType.from_info(type_info)

        self.assertCType(
            type=c_type,
            name="ClassWithSuper",
            namespace="TestLib",
            inner=(),
            reference=False,
            generic=False,
            nullable=False,
        )

    def test_from_info_inner(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithGeneric")
        c_type: CType = CType.from_info(type_info)

        self.assertCType(
            type=c_type,
            name="ClassWithGeneric",
            namespace="TestLib",
            inner=(CType(name="T", namespace="TestLib", generic=True),),
            reference=False,
            generic=False,
            nullable=False,
        )

    def test_from_info_inner_multi(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithMultiGeneric")
        c_type: CType = CType.from_info(type_info)

        self.assertCType(
            type=c_type,
            name="ClassWithMultiGeneric",
            namespace="TestLib",
            inner=(
                CType(name="U", namespace="TestLib", generic=True),
                CType(name="V", namespace="TestLib", generic=True),
            ),
            reference=False,
            generic=False,
            nullable=False,
        )

    def test_from_info_reference(self) -> None:
        type_info: TypeInfo = self.get_type("ClassThatsAbstract").MakeByRefType()
        c_type: CType = CType.from_info(type_info)

        self.assertCType(
            type=c_type,
            name="ClassThatsAbstract",
            namespace="TestLib",
            inner=(),
            reference=True,
            generic=False,
            nullable=False,
        )

    def test_from_info_generic(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithGeneric")
        c_type: CType = CType.from_info(type_info.GenericTypeParameters[0])

        self.assertCType(
            type=c_type,
            name="T",
            namespace="TestLib",
            inner=(),
            reference=False,
            generic=True,
            nullable=False,
        )

    def test_from_info_nullable(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithMethods")
        method_info: MethodInfo = type_info.GetMethod("InstanceMethodWithNullableParam")
        parameter_info: ParameterInfo = method_info.GetParameters()[0]
        c_type: CType = CType.from_info(parameter_info.ParameterType)

        self.assertCType(
            type=c_type,
            name="Int32",
            namespace="System",
            inner=(),
            reference=False,
            generic=False,
            nullable=True,
        )

    def test_from_info_reference_nullable(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithMethods")
        method_info: MethodInfo = type_info.GetMethod("InstanceMethodWithNullableOutParam")
        parameter_info: ParameterInfo = method_info.GetParameters()[0]
        c_type: CType = CType.from_info(parameter_info.ParameterType)

        self.assertCType(
            type=c_type,
            name="Int32",
            namespace="System",
            inner=(),
            reference=True,
            generic=False,
            nullable=True,
        )

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
        self.assertEqual("Namespace.Type", json)

        from_json: CType = CType.from_json(json)

        self.assertEqual(c_type, from_json)

    def test_json_reference(self) -> None:
        c_type: CType = CType(name="Type", namespace="Namespace", reference=True)
        json: JsonType = c_type.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, str)
        self.assertEqual("Namespace.*Type", json)

        from_json: CType = CType.from_json(json)

        self.assertEqual(c_type, from_json)

    def test_json_generic(self) -> None:
        c_type: CType = CType(name="Type", namespace="Namespace", generic=True)
        json: JsonType = c_type.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, str)
        self.assertEqual("Namespace.$Type", json)

        from_json: CType = CType.from_json(json)

        self.assertEqual(c_type, from_json)

    def test_json_nullable(self) -> None:
        c_type: CType = CType(name="Type", namespace="Namespace", nullable=True)
        json: JsonType = c_type.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, str)
        self.assertEqual("Namespace.Type?", json)

        from_json: CType = CType.from_json(json)

        self.assertEqual(c_type, from_json)

    def test_json_reference_generic(self) -> None:
        c_type: CType = CType(name="Type", namespace="Namespace", reference=True, generic=True)
        json: JsonType = c_type.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, str)
        self.assertEqual("Namespace.$*Type", json)

        from_json: CType = CType.from_json(json)

        self.assertEqual(c_type, from_json)

    def test_json_reference_nullable(self) -> None:
        c_type: CType = CType(name="Type", namespace="Namespace", reference=True, nullable=True)
        json: JsonType = c_type.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, str)
        self.assertEqual("Namespace.*Type?", json)

        from_json: CType = CType.from_json(json)

        self.assertEqual(c_type, from_json)

    def test_json_generic_nullable(self) -> None:
        c_type: CType = CType(name="Type", namespace="Namespace", generic=True, nullable=True)
        json: JsonType = c_type.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, str)
        self.assertEqual("Namespace.$Type?", json)

        from_json: CType = CType.from_json(json)

        self.assertEqual(c_type, from_json)

    def test_json_reference_generic_nullable(self) -> None:
        c_type: CType = CType(
            name="Type",
            namespace="Namespace",
            reference=True,
            generic=True,
            nullable=True,
        )
        json: JsonType = c_type.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, str)
        self.assertEqual("Namespace.$*Type?", json)

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
        self.assertEqual("Namespace.Type[Namespace.InnerA, Namespace.InnerB]", json)

        from_json: CType = CType.from_json(json)

        self.assertEqual(c_type, from_json)

    def test_compare_namespace(self) -> None:
        type0: CType = CType("Type", "NamespaceA")
        type1: CType = CType("Type", "NamespaceB")

        self.assertLess(type0, type1)

        self.assertLessEqual(type0, type1)

        self.assertLessEqual(type0, type0)
        self.assertLessEqual(type1, type1)

        self.assertGreater(type1, type0)

        self.assertGreaterEqual(type1, type0)

        self.assertGreaterEqual(type0, type0)
        self.assertGreaterEqual(type1, type1)

    def test_compare_name(self) -> None:
        type0: CType = CType("A", "Namespace")
        type1: CType = CType("B", "Namespace")

        self.assertLess(type0, type1)

        self.assertLessEqual(type0, type1)

        self.assertLessEqual(type0, type0)
        self.assertLessEqual(type1, type1)

        self.assertGreater(type1, type0)

        self.assertGreaterEqual(type1, type0)

        self.assertGreaterEqual(type0, type0)
        self.assertGreaterEqual(type1, type1)

    def test_compare_inner_len(self) -> None:
        type0: CType = CType("Type", "Namespace", ())
        type1: CType = CType("Type", "Namespace", (CType("T", "Namespace"),))

        self.assertLess(type0, type1)

        self.assertLessEqual(type0, type1)

        self.assertLessEqual(type0, type0)
        self.assertLessEqual(type1, type1)

        self.assertGreater(type1, type0)

        self.assertGreaterEqual(type1, type0)

        self.assertGreaterEqual(type0, type0)
        self.assertGreaterEqual(type1, type1)

    def test_compare_inner(self) -> None:
        type0: CType = CType("Type", "Namespace", (CType("A", "Namespace"),))
        type1: CType = CType("Type", "Namespace", (CType("B", "Namespace"),))

        self.assertLess(type0, type1)

        self.assertLessEqual(type0, type1)

        self.assertLessEqual(type0, type0)
        self.assertLessEqual(type1, type1)

        self.assertGreater(type1, type0)

        self.assertGreaterEqual(type1, type0)

        self.assertGreaterEqual(type0, type0)
        self.assertGreaterEqual(type1, type1)

    def test_compare_generic(self) -> None:
        type0: CType = CType("Type", "Namespace", (CType("T", "Namespace"),), False)
        type1: CType = CType("Type", "Namespace", (CType("T", "Namespace"),), True)

        self.assertLess(type0, type1)

        self.assertLessEqual(type0, type1)

        self.assertLessEqual(type0, type0)
        self.assertLessEqual(type1, type1)

        self.assertGreater(type1, type0)

        self.assertGreaterEqual(type1, type0)

        self.assertGreaterEqual(type0, type0)
        self.assertGreaterEqual(type1, type1)

    def test_compare_nullable(self) -> None:
        type0: CType = CType("Type", "Namespace", (CType("T", "Namespace"),), False, False)
        type1: CType = CType("Type", "Namespace", (CType("T", "Namespace"),), False, True)

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
            CType("TypeA", "NamespaceA"),
            CType("TypeA", "NamespaceB"),
            CType("TypeB", "NamespaceB"),
            CType("TypeB", "NamespaceB", (CType("Type"),)),
            CType("TypeB", "NamespaceB", (CType("Type"),), generic=True),
            CType("TypeB", "NamespaceB", (CType("Type"),), generic=True, nullable=True),
        )
        unordered: MutableSequence[CType] = list(ordered)
        random.shuffle(unordered)

        self.assertSequenceEqual(ordered, sorted(unordered))


class TestCParameter(TestBase):
    def test_from_info_simple(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithMethods")
        method_info: MethodInfo = type_info.GetMethod("InstanceMethodWithParams1")
        c_parameter: CParameter = CParameter.from_info(method_info.GetParameters()[0])

        self.assertCParameter(
            parameter=c_parameter,
            name="param0",
            type=CType(name="Int32", namespace="System"),
            default=False,
            out=False,
        )

    def test_from_info_default(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithMethods")
        method_info: MethodInfo = type_info.GetMethod("InstanceMethodWithDefaultParam")
        c_parameter: CParameter = CParameter.from_info(method_info.GetParameters()[0])

        self.assertCParameter(
            parameter=c_parameter,
            name="param0",
            type=CType(name="Int32", namespace="System"),
            default=True,
            out=False,
        )

    def test_from_info_out(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithMethods")
        method_info: MethodInfo = type_info.GetMethod("InstanceMethodWithOutParam")
        c_parameter: CParameter = CParameter.from_info(method_info.GetParameters()[0])

        self.assertCParameter(
            parameter=c_parameter,
            name="param0",
            type=CType(name="Int32", namespace="System", reference=True),
            default=False,
            out=True,
        )

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
                "type": "Namespace.Type",
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
                "type": "Namespace.Type",
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
                "type": "Namespace.Type",
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
                "type": "Namespace.Type",
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
    def test_from_info(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithFields")
        field_info: FieldInfo = type_info.GetField("InstanceFieldA")
        c_field: CField = CField.from_info(field_info)

        self.assertCField(
            field=c_field,
            name="InstanceFieldA",
            declaring_type=CType(name="ClassWithFields", namespace="TestLib"),
            returns=CType(name="Int32", namespace="System"),
            static=False,
        )

    def test_from_info_static(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithFields")
        field_info: FieldInfo = type_info.GetField("StaticFieldA")
        c_field: CField = CField.from_info(field_info)

        self.assertCField(
            field=c_field,
            name="StaticFieldA",
            declaring_type=CType(name="ClassWithFields", namespace="TestLib"),
            returns=CType(name="Int32", namespace="System"),
            static=True,
        )

    def test_json(self) -> None:
        c_field: CField = CField(
            name="Field",
            declaring_type=CType(name="Type", namespace="Namespace"),
            returns=CType(name="Type", namespace="Namespace"),
        )
        json: JsonType = c_field.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "name": "Field",
                "declaring_type": "Namespace.Type",
                "returns": "Namespace.Type",
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
            returns=CType(name="Type", namespace="Namespace"),
            static=True,
        )
        json: JsonType = c_field.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "name": "Field",
                "declaring_type": "Namespace.Type",
                "returns": "Namespace.Type",
                "static": True,
            },
            json,
        )

        from_json: CField = CField.from_json(json)

        self.assertEqual(c_field, from_json)

    def test_compare(self) -> None:
        field0: CField = CField(
            name="FieldA",
            declaring_type=CType(name="Type", namespace="Namespace"),
            returns=CType(name="Type", namespace="Namespace"),
        )
        field1: CField = CField(
            name="FieldB",
            declaring_type=CType(name="Type", namespace="Namespace"),
            returns=CType(name="Type", namespace="Namespace"),
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
        type_info: TypeInfo = self.get_type("ClassWithFields")

        ordered: Sequence[CField] = (
            CField.from_info(type_info.GetField("InstanceFieldA")),
            CField.from_info(type_info.GetField("InstanceFieldB")),
            CField.from_info(type_info.GetField("InstanceFieldC")),
            CField.from_info(type_info.GetField("StaticFieldA")),
            CField.from_info(type_info.GetField("StaticFieldB")),
            CField.from_info(type_info.GetField("StaticFieldC")),
        )
        unordered: MutableSequence[CField] = list(ordered)
        random.shuffle(unordered)

        self.assertSequenceEqual(ordered, sorted(unordered))

    def test_get(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithFields")
        fields: Sequence[CField] = CField.get(type_info)
        manual_fields: Sequence[CField] = sorted(
            (
                CField.from_info(type_info.GetField("InstanceFieldA")),
                CField.from_info(type_info.GetField("InstanceFieldB")),
                CField.from_info(type_info.GetField("InstanceFieldC")),
                CField.from_info(type_info.GetField("StaticFieldA")),
                CField.from_info(type_info.GetField("StaticFieldB")),
                CField.from_info(type_info.GetField("StaticFieldC")),
            )
        )

        self.assertIsNotNone(fields)
        self.assertIsInstance(fields, Sequence)
        self.assertSequenceEqual(manual_fields, fields)


class TestCConstructor(TestBase):
    def test_from_info(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithConstructors")
        constructors: Sequence[CConstructor] = list(
            map(CConstructor.from_info, type_info.GetConstructors())
        )

        self.assertCConstructor(
            constructor=constructors[0],
            declaring_type=CType(name="ClassWithConstructors", namespace="TestLib"),
            parameters=(),
        )
        self.assertCConstructor(
            constructor=constructors[1],
            declaring_type=CType(name="ClassWithConstructors", namespace="TestLib"),
            parameters=(CParameter(name="param0", type=CType(name="Int32", namespace="System")),),
        )
        self.assertCConstructor(
            constructor=constructors[2],
            declaring_type=CType(name="ClassWithConstructors", namespace="TestLib"),
            parameters=(
                CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                CParameter(name="param1", type=CType(name="Int32", namespace="System")),
            ),
        )
        self.assertCConstructor(
            constructor=constructors[3],
            declaring_type=CType(name="ClassWithConstructors", namespace="TestLib"),
            parameters=(
                CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                CParameter(name="param1", type=CType(name="Int32", namespace="System")),
                CParameter(name="param2", type=CType(name="Int32", namespace="System")),
            ),
        )

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
                "declaring_type": "Namespace.Type",
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
                "declaring_type": "Namespace.Type",
                "parameters": (
                    {
                        "name": "param0",
                        "type": "Namespace.Type",
                        "default": False,
                        "out": False,
                    },
                    {
                        "name": "param1",
                        "type": "Namespace.Type",
                        "default": False,
                        "out": False,
                    },
                ),
            },
            json,
        )

        from_json: CConstructor = CConstructor.from_json(json)

        self.assertEqual(c_constructor, from_json)

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

    def test_get(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithConstructors")
        constructors: Sequence[CConstructor] = CConstructor.get(type_info)
        manual_constructors: Sequence[CConstructor] = sorted(
            map(CConstructor.from_info, type_info.GetConstructors())
        )

        self.assertIsNotNone(constructors)
        self.assertIsInstance(constructors, Sequence)
        self.assertSequenceEqual(manual_constructors, constructors)


class TestCProperty(TestBase):
    def test_from_info(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithProperties")
        property_info: PropertyInfo = type_info.GetProperty("InstanceReadOnlyProperty0")
        c_property: CProperty = CProperty.from_info(property_info)

        self.assertCProperty(
            property=c_property,
            name="InstanceReadOnlyProperty0",
            declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
            type=CType(name="Int32", namespace="System"),
            setter=False,
            static=False,
        )

    def test_from_info_setter(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithProperties")
        property_info: PropertyInfo = type_info.GetProperty("InstanceProperty0")
        c_property: CProperty = CProperty.from_info(property_info)

        self.assertCProperty(
            property=c_property,
            name="InstanceProperty0",
            declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
            type=CType(name="Int32", namespace="System"),
            setter=True,
            static=False,
        )

    def test_from_info_static(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithProperties")
        property_info: PropertyInfo = type_info.GetProperty("StaticReadOnlyProperty0")
        c_property: CProperty = CProperty.from_info(property_info)

        self.assertCProperty(
            property=c_property,
            name="StaticReadOnlyProperty0",
            declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
            type=CType(name="Int32", namespace="System"),
            setter=False,
            static=True,
        )

    def test_from_info_setter_static(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithProperties")
        property_info: PropertyInfo = type_info.GetProperty("StaticProperty0")
        c_property: CProperty = CProperty.from_info(property_info)

        self.assertCProperty(
            property=c_property,
            name="StaticProperty0",
            declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
            type=CType(name="Int32", namespace="System"),
            setter=True,
            static=True,
        )

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
                "declaring_type": "Namespace.Type",
                "type": "Namespace.Type",
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
                "declaring_type": "Namespace.Type",
                "type": "Namespace.Type",
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
                "declaring_type": "Namespace.Type",
                "type": "Namespace.Type",
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
                "declaring_type": "Namespace.Type",
                "type": "Namespace.Type",
                "setter": True,
                "static": True,
            },
            json,
        )

        from_json: CProperty = CProperty.from_json(json)

        self.assertEqual(c_property, from_json)

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

    def test_get(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithProperties")
        properties: Sequence[CProperty] = CProperty.get(type_info)
        manual_properties: Sequence[CProperty] = sorted(
            (
                CProperty.from_info(type_info.GetProperty("InstanceProperty0")),
                CProperty.from_info(type_info.GetProperty("InstanceProperty1")),
                CProperty.from_info(type_info.GetProperty("InstanceProperty2")),
                CProperty.from_info(type_info.GetProperty("InstanceReadOnlyProperty0")),
                CProperty.from_info(type_info.GetProperty("InstanceReadOnlyProperty1")),
                CProperty.from_info(type_info.GetProperty("InstanceReadOnlyProperty2")),
                CProperty.from_info(type_info.GetProperty("StaticProperty0")),
                CProperty.from_info(type_info.GetProperty("StaticProperty1")),
                CProperty.from_info(type_info.GetProperty("StaticProperty2")),
                CProperty.from_info(type_info.GetProperty("StaticReadOnlyProperty0")),
                CProperty.from_info(type_info.GetProperty("StaticReadOnlyProperty1")),
                CProperty.from_info(type_info.GetProperty("StaticReadOnlyProperty2")),
            )
        )

        self.assertIsNotNone(properties)
        self.assertIsInstance(properties, Sequence)
        self.assertSequenceEqual(manual_properties, properties)


class TestCMethod(TestBase):
    def test_from_info(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithMethods")
        method_info: MethodInfo = type_info.GetMethod("InstanceMethodWithParams1")
        c_method: CMethod = CMethod.from_info(method_info)

        self.assertCMethod(
            method=c_method,
            name="InstanceMethodWithParams1",
            declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
            parameters=(CParameter(name="param0", type=CType(name="Int32", namespace="System")),),
            returns=(CType(name="Int32", namespace="System"),),
            static=False,
        )

    def test_from_info_static(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithMethods")
        method_info: MethodInfo = type_info.GetMethod("StaticMethodWithParams1")
        c_method: CMethod = CMethod.from_info(method_info)

        self.assertCMethod(
            method=c_method,
            name="StaticMethodWithParams1",
            declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
            parameters=(CParameter(name="param0", type=CType(name="Int32", namespace="System")),),
            returns=(CType("Int32", "System"),),
            static=True,
        )

    def test_from_info_out(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithMethods")
        method_info: MethodInfo = type_info.GetMethod("InstanceMethodWithOutParam")
        c_method: CMethod = CMethod.from_info(method_info)

        self.assertCMethod(
            method=c_method,
            name="InstanceMethodWithOutParam",
            declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
            parameters=(
                CParameter(
                    name="param0",
                    type=CType(name="Int32", namespace="System", reference=True),
                    out=True,
                ),
            ),
            returns=(
                CType(name="Int32", namespace="System"),
                CType(name="Int32", namespace="System", reference=True),
            ),
            static=False,
        )

    def test_json(self) -> None:
        c_method: CMethod = CMethod(
            name="Method",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(CParameter(name="param0", type=CType(name="Type", namespace="Namespace")),),
            returns=(CType(name="Type", namespace="Namespace"),),
        )
        json: JsonType = c_method.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "name": "Method",
                "declaring_type": "Namespace.Type",
                "parameters": (
                    {
                        "name": "param0",
                        "type": "Namespace.Type",
                        "default": False,
                        "out": False,
                    },
                ),
                "returns": ("Namespace.Type",),
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
            returns=(),
        )
        json: JsonType = c_method.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "name": "Method",
                "declaring_type": "Namespace.Type",
                "parameters": (
                    {
                        "name": "param0",
                        "type": "Namespace.Type",
                        "default": False,
                        "out": False,
                    },
                ),
                "returns": (),
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
            returns=(CType(name="Type", namespace="Namespace"),),
            static=True,
        )
        json: JsonType = c_method.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            {
                "name": "Method",
                "declaring_type": "Namespace.Type",
                "parameters": (
                    {
                        "name": "param0",
                        "type": "Namespace.Type",
                        "default": False,
                        "out": False,
                    },
                ),
                "returns": ("Namespace.Type",),
                "static": True,
            },
            json,
        )

        from_json: CMethod = CMethod.from_json(json)

        self.assertEqual(c_method, from_json)

    def test_compare(self) -> None:
        method0: CMethod = CMethod(
            name="MethodA",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            returns=(),
        )
        method1: CMethod = CMethod(
            name="MethodB",
            declaring_type=CType(name="Type", namespace="Namespace"),
            parameters=(),
            returns=(),
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
        type_info: TypeInfo = self.get_type("ClassWithMethods")

        ordered: Sequence[CMethod] = (
            CMethod.from_info(type_info.GetMethod("InstanceMethodWithDefaultParam")),
            CMethod.from_info(type_info.GetMethod("InstanceMethodWithNullableDefaultParam")),
            CMethod.from_info(type_info.GetMethod("InstanceMethodWithNullableOutParam")),
            CMethod.from_info(type_info.GetMethod("InstanceMethodWithNullableParam")),
            CMethod.from_info(type_info.GetMethod("InstanceMethodWithOutParam")),
            CMethod.from_info(type_info.GetMethod("InstanceMethodWithParams0")),
            CMethod.from_info(type_info.GetMethod("InstanceMethodWithParams1")),
            CMethod.from_info(type_info.GetMethod("InstanceMethodWithParams2")),
            CMethod.from_info(type_info.GetMethod("StaticMethodWithDefaultParam")),
            CMethod.from_info(type_info.GetMethod("StaticMethodWithNullableDefaultParam")),
            CMethod.from_info(type_info.GetMethod("StaticMethodWithNullableOutParam")),
            CMethod.from_info(type_info.GetMethod("StaticMethodWithNullableParam")),
            CMethod.from_info(type_info.GetMethod("StaticMethodWithOutParam")),
            CMethod.from_info(type_info.GetMethod("StaticMethodWithParams0")),
            CMethod.from_info(type_info.GetMethod("StaticMethodWithParams1")),
            CMethod.from_info(type_info.GetMethod("StaticMethodWithParams2")),
        )
        unordered: MutableSequence[CMethod] = list(ordered)
        random.shuffle(unordered)

        self.assertSequenceEqual(ordered, sorted(unordered))

    def test_get(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithMethods")
        methods: Sequence[CMethod] = CMethod.get(type_info)
        manual_methods: Sequence[CMethod] = sorted(
            (
                CMethod.from_info(type_info.GetMethod("Equals")),
                CMethod.from_info(type_info.GetMethod("GetHashCode")),
                CMethod.from_info(type_info.GetMethod("GetType")),
                CMethod.from_info(type_info.GetMethod("InstanceMethodWithDefaultParam")),
                CMethod.from_info(type_info.GetMethod("InstanceMethodWithNullableDefaultParam")),
                CMethod.from_info(type_info.GetMethod("InstanceMethodWithNullableOutParam")),
                CMethod.from_info(type_info.GetMethod("InstanceMethodWithNullableParam")),
                CMethod.from_info(type_info.GetMethod("InstanceMethodWithOutParam")),
                CMethod.from_info(type_info.GetMethod("InstanceMethodWithParams0")),
                CMethod.from_info(type_info.GetMethod("InstanceMethodWithParams1")),
                CMethod.from_info(type_info.GetMethod("InstanceMethodWithParams2")),
                CMethod.from_info(type_info.GetMethod("StaticMethodWithDefaultParam")),
                CMethod.from_info(type_info.GetMethod("StaticMethodWithNullableDefaultParam")),
                CMethod.from_info(type_info.GetMethod("StaticMethodWithNullableOutParam")),
                CMethod.from_info(type_info.GetMethod("StaticMethodWithNullableParam")),
                CMethod.from_info(type_info.GetMethod("StaticMethodWithOutParam")),
                CMethod.from_info(type_info.GetMethod("StaticMethodWithParams0")),
                CMethod.from_info(type_info.GetMethod("StaticMethodWithParams1")),
                CMethod.from_info(type_info.GetMethod("StaticMethodWithParams2")),
                CMethod.from_info(type_info.GetMethod("ToString")),
            )
        )

        self.assertIsNotNone(methods)
        self.assertIsInstance(methods, Sequence)
        self.assertSequenceEqual(manual_methods, methods)


class TestCEvent(TestBase):
    def test_from_info(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithEvents")
        event_info: EventInfo = type_info.GetEvent("Event")
        c_event: CEvent = CEvent.from_info(event_info)

        self.assertCEvent(
            event=c_event,
            name="Event",
            declaring_type=CType(name="ClassWithEvents", namespace="TestLib"),
            type=CType(name="EventHandler", namespace="System"),
        )

    def test_from_info_args(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithEvents")
        event_info: EventInfo = type_info.GetEvent("EventWithArgs")
        c_event: CEvent = CEvent.from_info(event_info)

        self.assertCEvent(
            event=c_event,
            name="EventWithArgs",
            declaring_type=CType(name="ClassWithEvents", namespace="TestLib"),
            type=CType(
                name="EventHandler",
                namespace="System",
                inner=(CType(name="EventArgs", namespace="System"),),
            ),
        )

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
                "declaring_type": "Namespace.Type",
                "type": "Namespace.Type",
            },
            json,
        )

        from_json: CEvent = CEvent.from_json(json)

        self.assertEqual(c_event, from_json)

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

    def test_get(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithEvents")
        events: Sequence[CEvent] = CEvent.get(type_info)
        manual_events: Sequence[CEvent] = sorted(
            (
                CEvent.from_info(type_info.GetEvent("Event")),
                CEvent.from_info(type_info.GetEvent("EventWithArgs")),
            )
        )

        self.assertIsNotNone(events)
        self.assertIsInstance(events, Sequence)
        self.assertSequenceEqual(manual_events, events)


if __name__ == "__main__":
    unittest.main()
