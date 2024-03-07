import json
import unittest
from pathlib import Path
from typing import Any
from typing import Dict
from typing import Mapping
from typing import Sequence

import clr
from System.Reflection import Assembly
from System.Reflection import EventInfo
from System.Reflection import FieldInfo
from System.Reflection import MethodInfo
from System.Reflection import ParameterInfo
from System.Reflection import PropertyInfo
from System.Reflection import TypeInfo
from test_base import TestBase

from stubgen.extract_stubs import extract_assembly
from stubgen.extract_stubs import extract_constructor
from stubgen.extract_stubs import extract_constructors
from stubgen.extract_stubs import extract_event
from stubgen.extract_stubs import extract_events
from stubgen.extract_stubs import extract_field
from stubgen.extract_stubs import extract_fields
from stubgen.extract_stubs import extract_method
from stubgen.extract_stubs import extract_methods
from stubgen.extract_stubs import extract_parameter
from stubgen.extract_stubs import extract_properties
from stubgen.extract_stubs import extract_property
from stubgen.extract_stubs import extract_type
from stubgen.extract_stubs import extract_type_def
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
from stubgen.util import make_python_name


class TestExtractBase(TestBase):
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


class TestCClass(TestExtractBase):
    def test_extract_class_generic(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithGeneric")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CClass = CClass(
            name="ClassWithGeneric",
            namespace="TestLib",
            nested=None,
            abstract=False,
            generic_args=(CType(name="T", generic=True),),
            super_class=CType(name="Object", namespace="System"),
            interfaces=(),
            fields={},
            constructors={
                "TestLib:ClassWithGeneric[$T].__init__()": CConstructor(
                    declaring_type=CType(
                        name="ClassWithGeneric",
                        namespace="TestLib",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(),
                ),
            },
            properties={},
            methods={
                "System:Object.Equals(System:Object)": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System:Object.GetHashCode()": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "System:Object.GetType()": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Type", namespace="System"),),
                ),
                "TestLib:ClassWithGeneric[$T].MethodWithGeneric($T)": CMethod(
                    name="MethodWithGeneric",
                    declaring_type=CType(
                        name="ClassWithGeneric",
                        namespace="TestLib",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(CParameter(name="param0", type=CType("T", generic=True)),),
                    return_types=(CType(name="Void", namespace="System"),),
                ),
                "System:Object.ToString()": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="String", namespace="System"),),
                ),
            },
            events={},
            nested_types={},
        )

        self.assertEqual(expected, extracted)

    def test_extract_class_generic_multi(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithMultiGeneric")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CClass = CClass(
            name="ClassWithMultiGeneric",
            namespace="TestLib",
            nested=None,
            abstract=False,
            generic_args=(
                CType(name="U", generic=True),
                CType(name="V", generic=True),
            ),
            super_class=CType(name="Object", namespace="System"),
            interfaces=(),
            fields={},
            constructors={
                "TestLib:ClassWithMultiGeneric[$U, $V].__init__()": CConstructor(
                    declaring_type=CType(
                        name="ClassWithMultiGeneric",
                        namespace="TestLib",
                        inner=(
                            CType(name="U", generic=True),
                            CType(name="V", generic=True),
                        ),
                    ),
                    parameters=(),
                ),
            },
            properties={},
            methods={
                "System:Object.Equals(System:Object)": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System:Object.GetHashCode()": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "System:Object.GetType()": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Type", namespace="System"),),
                ),
                "System:Object.ToString()": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="String", namespace="System"),),
                ),
            },
            events={},
            nested_types={},
        )

        self.assertEqual(expected, extracted)

    def test_extract_class_interfaces(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithInterface")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CClass = CClass(
            name="ClassWithInterface",
            namespace="TestLib",
            nested=None,
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
                "TestLib:ClassWithInterface.__init__()": CConstructor(
                    declaring_type=CType(name="ClassWithInterface", namespace="TestLib"),
                    parameters=(),
                ),
            },
            properties={},
            methods={
                "System:Object.Equals(System:Object)": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System:IEquatable[$T].Equals(TestLib:ClassWithInterface)": CMethod(
                    name="Equals",
                    declaring_type=CType(
                        name="IEquatable",
                        namespace="System",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithInterface", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System:Object.GetHashCode()": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "System:Object.GetType()": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Type", namespace="System"),),
                ),
                "System:Object.ToString()": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="String", namespace="System"),),
                ),
            },
            events={},
            nested_types={},
        )

        self.assertEqual(expected, extracted)

    def test_extract_class_fields(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithFields")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CClass = CClass(
            name="ClassWithFields",
            namespace="TestLib",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=CType(name="Object", namespace="System"),
            interfaces=(),
            fields={
                "TestLib:ClassWithFields.InstanceFieldA": CField(
                    name="InstanceFieldA",
                    declaring_type=CType(name="ClassWithFields", namespace="TestLib"),
                    return_type=CType(name="Int32", namespace="System"),
                ),
                "TestLib:ClassWithFields.InstanceFieldB": CField(
                    name="InstanceFieldB",
                    declaring_type=CType(name="ClassWithFields", namespace="TestLib"),
                    return_type=CType(name="Int32", namespace="System"),
                ),
                "TestLib:ClassWithFields.InstanceFieldC": CField(
                    name="InstanceFieldC",
                    declaring_type=CType(name="ClassWithFields", namespace="TestLib"),
                    return_type=CType(name="Int32", namespace="System"),
                ),
                "TestLib:ClassWithFields.StaticFieldA": CField(
                    name="StaticFieldA",
                    declaring_type=CType(name="ClassWithFields", namespace="TestLib"),
                    return_type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
                "TestLib:ClassWithFields.StaticFieldB": CField(
                    name="StaticFieldB",
                    declaring_type=CType(name="ClassWithFields", namespace="TestLib"),
                    return_type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
                "TestLib:ClassWithFields.StaticFieldC": CField(
                    name="StaticFieldC",
                    declaring_type=CType(name="ClassWithFields", namespace="TestLib"),
                    return_type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
            },
            constructors={
                "TestLib:ClassWithFields.__init__()": CConstructor(
                    declaring_type=CType(name="ClassWithFields", namespace="TestLib"),
                    parameters=(),
                ),
            },
            properties={},
            methods={
                "System:Object.Equals(System:Object)": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System:Object.GetHashCode()": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "System:Object.GetType()": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Type", namespace="System"),),
                ),
                "System:Object.ToString()": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="String", namespace="System"),),
                ),
            },
            events={},
            nested_types={},
        )

        self.assertEqual(expected, extracted)

    def test_extract_class_constructors(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithConstructors")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CClass = CClass(
            name="ClassWithConstructors",
            namespace="TestLib",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=CType(name="Object", namespace="System"),
            interfaces=(),
            fields={},
            constructors={
                "TestLib:ClassWithConstructors.__init__()": CConstructor(
                    declaring_type=CType(name="ClassWithConstructors", namespace="TestLib"),
                    parameters=(),
                ),
                "TestLib:ClassWithConstructors.__init__(System:Int32)": CConstructor(
                    declaring_type=CType(name="ClassWithConstructors", namespace="TestLib"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                    ),
                ),
                "TestLib:ClassWithConstructors.__init__(System:Int32, System:Int32)": CConstructor(
                    declaring_type=CType(name="ClassWithConstructors", namespace="TestLib"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                        CParameter(name="param1", type=CType(name="Int32", namespace="System")),
                    ),
                ),
                "TestLib:ClassWithConstructors.__init__(System:Int32, System:Int32, System:Int32)": CConstructor(
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
                "System:Object.Equals(System:Object)": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System:Object.GetHashCode()": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "System:Object.GetType()": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Type", namespace="System"),),
                ),
                "System:Object.ToString()": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="String", namespace="System"),),
                ),
            },
            events={},
            nested_types={},
        )

        self.assertEqual(expected, extracted)

    def test_extract_class_properties(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithProperties")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CClass = CClass(
            name="ClassWithProperties",
            namespace="TestLib",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=CType(name="Object", namespace="System"),
            interfaces=(),
            fields={},
            constructors={
                "TestLib:ClassWithProperties.__init__()": CConstructor(
                    declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                    parameters=(),
                ),
            },
            properties={
                "TestLib:ClassWithProperties.InstanceProperty0": CProperty(
                    name="InstanceProperty0",
                    declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                ),
                "TestLib:ClassWithProperties.InstanceProperty1": CProperty(
                    name="InstanceProperty1",
                    declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                ),
                "TestLib:ClassWithProperties.InstanceProperty2": CProperty(
                    name="InstanceProperty2",
                    declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                ),
                "TestLib:ClassWithProperties.InstanceReadOnlyProperty0": CProperty(
                    name="InstanceReadOnlyProperty0",
                    declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                ),
                "TestLib:ClassWithProperties.InstanceReadOnlyProperty1": CProperty(
                    name="InstanceReadOnlyProperty1",
                    declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                ),
                "TestLib:ClassWithProperties.InstanceReadOnlyProperty2": CProperty(
                    name="InstanceReadOnlyProperty2",
                    declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                ),
                "TestLib:ClassWithProperties.StaticProperty0": CProperty(
                    name="StaticProperty0",
                    declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                    static=True,
                ),
                "TestLib:ClassWithProperties.StaticProperty1": CProperty(
                    name="StaticProperty1",
                    declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                    static=True,
                ),
                "TestLib:ClassWithProperties.StaticProperty2": CProperty(
                    name="StaticProperty2",
                    declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                    static=True,
                ),
                "TestLib:ClassWithProperties.StaticReadOnlyProperty0": CProperty(
                    name="StaticReadOnlyProperty0",
                    declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
                "TestLib:ClassWithProperties.StaticReadOnlyProperty1": CProperty(
                    name="StaticReadOnlyProperty1",
                    declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
                "TestLib:ClassWithProperties.StaticReadOnlyProperty2": CProperty(
                    name="StaticReadOnlyProperty2",
                    declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
            },
            methods={
                "System:Object.Equals(System:Object)": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System:Object.GetHashCode()": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "System:Object.GetType()": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Type", namespace="System"),),
                ),
                "System:Object.ToString()": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="String", namespace="System"),),
                ),
            },
            events={},
            nested_types={},
        )

        self.assertEqual(expected, extracted)

    def test_extract_class_methods(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithMethods")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CClass = CClass(
            name="ClassWithMethods",
            namespace="TestLib",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=CType(name="Object", namespace="System"),
            interfaces=(),
            fields={},
            constructors={
                "TestLib:ClassWithMethods.__init__()": CConstructor(
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                    parameters=(),
                ),
            },
            properties={},
            methods={
                "System:Object.Equals(System:Object)": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System:Object.GetHashCode()": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "System:Object.GetType()": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Type", namespace="System"),),
                ),
                "TestLib:ClassWithMethods.InstanceMethodWithDefaultParam(System:Int32)": CMethod(
                    name="InstanceMethodWithDefaultParam",
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System"),
                            default=True,
                        ),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib:ClassWithMethods.InstanceMethodWithNullableDefaultParam(System:Int32?)": CMethod(
                    name="InstanceMethodWithNullableDefaultParam",
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System", nullable=True),
                            default=True,
                        ),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib:ClassWithMethods.InstanceMethodWithNullableOutParam(System:*Int32?)": CMethod(
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
                    return_types=(
                        CType(name="Int32", namespace="System"),
                        CType(name="Int32", namespace="System", reference=True, nullable=True),
                    ),
                ),
                "TestLib:ClassWithMethods.InstanceMethodWithNullableParam(System:Int32?)": CMethod(
                    name="InstanceMethodWithNullableParam",
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System", nullable=True),
                        ),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib:ClassWithMethods.InstanceMethodWithOutParam(System:*Int32)": CMethod(
                    name="InstanceMethodWithOutParam",
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
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
                "TestLib:ClassWithMethods.InstanceMethodWithParams0()": CMethod(
                    name="InstanceMethodWithParams0",
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                    parameters=(),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib:ClassWithMethods.InstanceMethodWithParams1(System:Int32)": CMethod(
                    name="InstanceMethodWithParams1",
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib:ClassWithMethods.InstanceMethodWithParams2(System:Int32, System:Int32)": CMethod(
                    name="InstanceMethodWithParams2",
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                        CParameter(name="param1", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib:ClassWithMethods.StaticMethodWithDefaultParam(System:Int32)": CMethod(
                    name="StaticMethodWithDefaultParam",
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System"),
                            default=True,
                        ),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                    static=True,
                ),
                "TestLib:ClassWithMethods.StaticMethodWithNullableDefaultParam(System:Int32?)": CMethod(
                    name="StaticMethodWithNullableDefaultParam",
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System", nullable=True),
                            default=True,
                        ),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                    static=True,
                ),
                "TestLib:ClassWithMethods.StaticMethodWithNullableOutParam(System:*Int32?)": CMethod(
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
                    return_types=(
                        CType(name="Int32", namespace="System"),
                        CType(name="Int32", namespace="System", reference=True, nullable=True),
                    ),
                    static=True,
                ),
                "TestLib:ClassWithMethods.StaticMethodWithNullableParam(System:Int32?)": CMethod(
                    name="StaticMethodWithNullableParam",
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System", nullable=True),
                        ),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                    static=True,
                ),
                "TestLib:ClassWithMethods.StaticMethodWithOutParam(System:*Int32)": CMethod(
                    name="StaticMethodWithOutParam",
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
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
                    static=True,
                ),
                "TestLib:ClassWithMethods.StaticMethodWithParams0()": CMethod(
                    name="StaticMethodWithParams0",
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                    parameters=(),
                    return_types=(CType(name="Int32", namespace="System"),),
                    static=True,
                ),
                "TestLib:ClassWithMethods.StaticMethodWithParams1(System:Int32)": CMethod(
                    name="StaticMethodWithParams1",
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                    static=True,
                ),
                "TestLib:ClassWithMethods.StaticMethodWithParams2(System:Int32, System:Int32)": CMethod(
                    name="StaticMethodWithParams2",
                    declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                        CParameter(name="param1", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                    static=True,
                ),
                "System:Object.ToString()": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="String", namespace="System"),),
                ),
            },
            events={},
            nested_types={},
        )

        self.assertEqual(expected, extracted)

    def test_extract_class_methods_dunder(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithOperatorMethods")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CClass = CClass(
            name="ClassWithOperatorMethods",
            namespace="TestLib",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=CType(name="Object", namespace="System"),
            interfaces=(),
            fields={},
            constructors={
                "TestLib:ClassWithOperatorMethods.__init__()": CConstructor(
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(),
                ),
            },
            properties={},
            methods={
                "System:Object.Equals(System:Object)": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(
                            name="obj",
                            type=CType(name="Object", namespace="System"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System:Object.GetHashCode()": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "System:Object.GetType()": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Type", namespace="System"),),
                ),
                "System:Object.ToString()": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="String", namespace="System"),),
                ),
                "TestLib:ClassWithOperatorMethods.__add__(TestLib:ClassWithOperatorMethods)": CMethod(
                    name="__add__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib:ClassWithOperatorMethods.__and__(TestLib:ClassWithOperatorMethods)": CMethod(
                    name="__and__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib:ClassWithOperatorMethods.__eq__(TestLib:ClassWithOperatorMethods)": CMethod(
                    name="__eq__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib:ClassWithOperatorMethods.__ge__(TestLib:ClassWithOperatorMethods)": CMethod(
                    name="__ge__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib:ClassWithOperatorMethods.__gt__(TestLib:ClassWithOperatorMethods)": CMethod(
                    name="__gt__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib:ClassWithOperatorMethods.__invert__()": CMethod(
                    name="__invert__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(),
                    return_types=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib:ClassWithOperatorMethods.__le__(TestLib:ClassWithOperatorMethods)": CMethod(
                    name="__le__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib:ClassWithOperatorMethods.__lt__(TestLib:ClassWithOperatorMethods)": CMethod(
                    name="__lt__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib:ClassWithOperatorMethods.__mod__(TestLib:ClassWithOperatorMethods)": CMethod(
                    name="__mod__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib:ClassWithOperatorMethods.__mul__(TestLib:ClassWithOperatorMethods)": CMethod(
                    name="__mul__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib:ClassWithOperatorMethods.__ne__(TestLib:ClassWithOperatorMethods)": CMethod(
                    name="__ne__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib:ClassWithOperatorMethods.__neg__()": CMethod(
                    name="__neg__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(),
                    return_types=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib:ClassWithOperatorMethods.__or__(TestLib:ClassWithOperatorMethods)": CMethod(
                    name="__or__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib:ClassWithOperatorMethods.__pos__()": CMethod(
                    name="__pos__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(),
                    return_types=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib:ClassWithOperatorMethods.__sub__(TestLib:ClassWithOperatorMethods)": CMethod(
                    name="__sub__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib:ClassWithOperatorMethods.__truediv__(TestLib:ClassWithOperatorMethods)": CMethod(
                    name="__truediv__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib:ClassWithOperatorMethods.__xor__(TestLib:ClassWithOperatorMethods)": CMethod(
                    name="__xor__",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib:ClassWithOperatorMethods.op_Addition(TestLib:ClassWithOperatorMethods, TestLib:ClassWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib:ClassWithOperatorMethods.op_BitwiseAnd(TestLib:ClassWithOperatorMethods, TestLib:ClassWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib:ClassWithOperatorMethods.op_BitwiseOr(TestLib:ClassWithOperatorMethods, TestLib:ClassWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib:ClassWithOperatorMethods.op_Decrement(TestLib:ClassWithOperatorMethods)": CMethod(
                    name="op_Decrement",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib:ClassWithOperatorMethods.op_Division(TestLib:ClassWithOperatorMethods, TestLib:ClassWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib:ClassWithOperatorMethods.op_Equality(TestLib:ClassWithOperatorMethods, TestLib:ClassWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib:ClassWithOperatorMethods.op_ExclusiveOr(TestLib:ClassWithOperatorMethods, TestLib:ClassWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib:ClassWithOperatorMethods.op_False(TestLib:ClassWithOperatorMethods)": CMethod(
                    name="op_False",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib:ClassWithOperatorMethods.op_GreaterThan(TestLib:ClassWithOperatorMethods, TestLib:ClassWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib:ClassWithOperatorMethods.op_GreaterThanOrEqual(TestLib:ClassWithOperatorMethods, TestLib:ClassWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib:ClassWithOperatorMethods.op_Increment(TestLib:ClassWithOperatorMethods)": CMethod(
                    name="op_Increment",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib:ClassWithOperatorMethods.op_Inequality(TestLib:ClassWithOperatorMethods, TestLib:ClassWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib:ClassWithOperatorMethods.op_LessThan(TestLib:ClassWithOperatorMethods, TestLib:ClassWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib:ClassWithOperatorMethods.op_LessThanOrEqual(TestLib:ClassWithOperatorMethods, TestLib:ClassWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib:ClassWithOperatorMethods.op_LogicalNot(TestLib:ClassWithOperatorMethods)": CMethod(
                    name="op_LogicalNot",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib:ClassWithOperatorMethods.op_Modulus(TestLib:ClassWithOperatorMethods, TestLib:ClassWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib:ClassWithOperatorMethods.op_Multiply(TestLib:ClassWithOperatorMethods, TestLib:ClassWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib:ClassWithOperatorMethods.op_OnesComplement(TestLib:ClassWithOperatorMethods)": CMethod(
                    name="op_OnesComplement",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib:ClassWithOperatorMethods.op_Subtraction(TestLib:ClassWithOperatorMethods, TestLib:ClassWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib:ClassWithOperatorMethods.op_True(TestLib:ClassWithOperatorMethods)": CMethod(
                    name="op_True",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib:ClassWithOperatorMethods.op_UnaryNegation(TestLib:ClassWithOperatorMethods)": CMethod(
                    name="op_UnaryNegation",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib:ClassWithOperatorMethods.op_UnaryPlus(TestLib:ClassWithOperatorMethods)": CMethod(
                    name="op_UnaryPlus",
                    declaring_type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="ClassWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="ClassWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
            },
            events={},
            nested_types={},
        )

        self.assertEqual(expected, extracted)

    def test_extract_class_methods_list(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithListMethods")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CClass = CClass(
            name="ClassWithListMethods",
            namespace="TestLib",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=CType(name="Object", namespace="System"),
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
                CType(
                    name="IList",
                    namespace="System.Collections.Generic",
                    inner=(CType(name="Int32", namespace="System"),),
                ),
            ),
            fields={},
            constructors={
                "TestLib:ClassWithListMethods.__init__()": CConstructor(
                    declaring_type=CType(name="ClassWithListMethods", namespace="TestLib"),
                    parameters=(),
                ),
            },
            properties={
                "System.Collections.Generic:ICollection[$T].Count": CProperty(
                    name="Count",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    type=CType(name="Int32", namespace="System"),
                ),
                "System.Collections.Generic:ICollection[$T].IsReadOnly": CProperty(
                    name="IsReadOnly",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    type=CType(name="Boolean", namespace="System"),
                ),
            },
            methods={
                "System.Collections.Generic:ICollection[$T].Add(System:Int32)": CMethod(
                    name="Add",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(name="item", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Void", namespace="System"),),
                ),
                "System.Collections.Generic:ICollection[$T].Clear()": CMethod(
                    name="Clear",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(),
                    return_types=(CType(name="Void", namespace="System"),),
                ),
                "System.Collections.Generic:ICollection[$T].Contains(System:Int32)": CMethod(
                    name="Contains",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(name="item", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Collections.Generic:ICollection[$T].CopyTo(System:Array[System:Int32], System:Int32)": CMethod(
                    name="CopyTo",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(
                            name="array",
                            type=CType(
                                name="Array",
                                namespace="System",
                                inner=(CType(name="Int32", namespace="System"),),
                            ),
                        ),
                        CParameter(name="arrayIndex", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Void", namespace="System"),),
                ),
                "System:Object.Equals(System:Object)": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Collections:IEnumerable.GetEnumerator()": CMethod(
                    name="GetEnumerator",
                    declaring_type=CType(name="IEnumerable", namespace="System.Collections"),
                    parameters=(),
                    return_types=(
                        CType(
                            name="IEnumerator",
                            namespace="System.Collections.Generic",
                            inner=(CType(name="Int32", namespace="System"),),
                        ),
                    ),
                ),
                "System:Object.GetHashCode()": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "System:Object.GetType()": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Type", namespace="System"),),
                ),
                "System.Collections.Generic:IList[$T].IndexOf(System:Int32)": CMethod(
                    name="IndexOf",
                    declaring_type=CType(
                        name="IList",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(name="item", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "System.Collections.Generic:IList[$T].Insert(System:Int32, System:Int32)": CMethod(
                    name="Insert",
                    declaring_type=CType(
                        name="IList",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(name="index", type=CType(name="Int32", namespace="System")),
                        CParameter(name="item", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Void", namespace="System"),),
                ),
                "System.Collections.Generic:ICollection[$T].Remove(System:Int32)": CMethod(
                    name="Remove",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(name="item", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Collections.Generic:IList[$T].RemoveAt(System:Int32)": CMethod(
                    name="RemoveAt",
                    declaring_type=CType(
                        name="IList",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(name="index", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Void", namespace="System"),),
                ),
                "System:Object.ToString()": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="String", namespace="System"),),
                ),
                "System.Collections.Generic:ICollection[$T].__contains__(System:Int32)": CMethod(
                    name="__contains__",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(name="item", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Collections.Generic:ICollection[$T].__delitem__(System:Int32)": CMethod(
                    name="__delitem__",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(name="item", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Collections.Generic:IList[$T].__getitem__(System:Int32)": CMethod(
                    name="__getitem__",
                    declaring_type=CType(
                        name="IList",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(name="index", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "System.Collections:IEnumerable.__iter__()": CMethod(
                    name="__iter__",
                    declaring_type=CType(name="IEnumerable", namespace="System.Collections"),
                    parameters=(),
                    return_types=(
                        CType(
                            name="Iterator",
                            namespace="typing",
                            inner=(CType(name="Int32", namespace="System"),),
                        ),
                    ),
                ),
                "System.Collections.Generic:ICollection[$T].__len__()": CMethod(
                    name="__len__",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "System.Collections.Generic:IList[$T].__setitem__(System:Int32, System:Int32)": CMethod(
                    name="__setitem__",
                    declaring_type=CType(
                        name="IList",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(name="index", type=CType(name="Int32", namespace="System")),
                        CParameter(name="value", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Void", namespace="System"),),
                ),
            },
            events={},
            nested_types={},
        )

        self.assertEqual(expected, extracted)

    def test_extract_class_events(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithEvents")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CClass = CClass(
            name="ClassWithEvents",
            namespace="TestLib",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=CType(name="Object", namespace="System"),
            interfaces=(),
            fields={},
            constructors={
                "TestLib:ClassWithEvents.__init__()": CConstructor(
                    declaring_type=CType(name="ClassWithEvents", namespace="TestLib"),
                    parameters=(),
                ),
            },
            properties={},
            methods={
                "System:Object.Equals(System:Object)": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System:Object.GetHashCode()": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "System:Object.GetType()": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Type", namespace="System"),),
                ),
                "System:Object.ToString()": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="String", namespace="System"),),
                ),
            },
            events={
                "TestLib:ClassWithEvents.Event": CEvent(
                    name="Event",
                    declaring_type=CType(name="ClassWithEvents", namespace="TestLib"),
                    type=CType(name="EventHandler", namespace="System"),
                ),
                "TestLib:ClassWithEvents.EventWithArgs": CEvent(
                    name="EventWithArgs",
                    declaring_type=CType(name="ClassWithEvents", namespace="TestLib"),
                    type=CType(
                        name="EventHandler",
                        namespace="System",
                        inner=(CType(name="EventArgs", namespace="System"),),
                    ),
                ),
            },
            nested_types={},
        )

        self.assertEqual(expected, extracted)

    def test_extract_class_nested(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithNested")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CClass = CClass(
            name="ClassWithNested",
            namespace="TestLib",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=CType(name="Object", namespace="System"),
            interfaces=(),
            fields={},
            constructors={
                "TestLib:ClassWithNested.__init__()": CConstructor(
                    declaring_type=CType(name="ClassWithNested", namespace="TestLib"),
                    parameters=(),
                ),
            },
            properties={},
            methods={
                "System:Object.Equals(System:Object)": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System:Object.GetHashCode()": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "System:Object.GetType()": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Type", namespace="System"),),
                ),
                "System:Object.ToString()": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="String", namespace="System"),),
                ),
            },
            events={},
            nested_types={
                "TestLib:ClassWithNested.INestedInterface": CInterface(
                    name="INestedInterface",
                    namespace="TestLib",
                    nested=CType(name="ClassWithNested", namespace="TestLib"),
                    generic_args=(),
                    interfaces=(),
                    fields={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "TestLib:ClassWithNested.NestedClass": CClass(
                    name="NestedClass",
                    namespace="TestLib",
                    nested=CType(name="ClassWithNested", namespace="TestLib"),
                    abstract=False,
                    generic_args=(),
                    super_class=CType(name="Object", namespace="System"),
                    interfaces=(),
                    fields={},
                    constructors={
                        "TestLib:ClassWithNested.NestedClass.__init__()": CConstructor(
                            declaring_type=CType(
                                name="ClassWithNested.NestedClass",
                                namespace="TestLib",
                            ),
                            parameters=(),
                        )
                    },
                    properties={},
                    methods={
                        "System:Object.Equals(System:Object)": CMethod(
                            name="Equals",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(
                                CParameter(
                                    name="obj",
                                    type=CType(name="Object", namespace="System"),
                                ),
                            ),
                            return_types=(CType(name="Boolean", namespace="System"),),
                        ),
                        "System:Object.GetHashCode()": CMethod(
                            name="GetHashCode",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            return_types=(CType(name="Int32", namespace="System"),),
                        ),
                        "System:Object.GetType()": CMethod(
                            name="GetType",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            return_types=(CType(name="Type", namespace="System"),),
                        ),
                        "System:Object.ToString()": CMethod(
                            name="ToString",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            return_types=(CType(name="String", namespace="System"),),
                        ),
                    },
                    events={},
                    nested_types={},
                ),
                "TestLib:ClassWithNested.NestedDelegate()": CDelegate(
                    name="NestedDelegate",
                    namespace="TestLib",
                    nested=CType(name="ClassWithNested", namespace="TestLib"),
                    parameters=(),
                    return_type=CType(name="Void", namespace="System"),
                ),
                "TestLib:ClassWithNested.NestedEnum": CEnum(
                    name="NestedEnum",
                    namespace="TestLib",
                    nested=CType(name="ClassWithNested", namespace="TestLib"),
                    fields=(),
                ),
                "TestLib:ClassWithNested.NestedStruct": CStruct(
                    name="NestedStruct",
                    namespace="TestLib",
                    nested=CType(name="ClassWithNested", namespace="TestLib"),
                    abstract=False,
                    generic_args=(),
                    super_class=CType(name="ValueType", namespace="System"),
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={
                        "System:Object.Equals(System:Object)": CMethod(
                            name="Equals",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(
                                CParameter(
                                    name="obj",
                                    type=CType(name="Object", namespace="System"),
                                ),
                            ),
                            return_types=(CType(name="Boolean", namespace="System"),),
                        ),
                        "System:Object.GetHashCode()": CMethod(
                            name="GetHashCode",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            return_types=(CType(name="Int32", namespace="System"),),
                        ),
                        "System:Object.GetType()": CMethod(
                            name="GetType",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            return_types=(CType(name="Type", namespace="System"),),
                        ),
                        "System:Object.ToString()": CMethod(
                            name="ToString",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            return_types=(CType(name="String", namespace="System"),),
                        ),
                    },
                    events={},
                    nested_types={},
                ),
            },
        )

        self.assertEqual(expected, extracted)


class TestCStruct(TestExtractBase):
    def test_extract_struct_generic(self) -> None:
        type_info: TypeInfo = self.get_type("StructWithGeneric")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CStruct = CStruct(
            name="StructWithGeneric",
            namespace="TestLib",
            nested=None,
            abstract=False,
            generic_args=(CType(name="T", generic=True),),
            super_class=CType(name="ValueType", namespace="System"),
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={
                "System:Object.Equals(System:Object)": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System:Object.GetHashCode()": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "System:Object.GetType()": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Type", namespace="System"),),
                ),
                "TestLib:StructWithGeneric[$T].MethodWithGeneric($T)": CMethod(
                    name="MethodWithGeneric",
                    declaring_type=CType(
                        name="StructWithGeneric",
                        namespace="TestLib",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(CParameter(name="param0", type=CType("T", generic=True)),),
                    return_types=(CType(name="Void", namespace="System"),),
                ),
                "System:Object.ToString()": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="String", namespace="System"),),
                ),
            },
            events={},
            nested_types={},
        )

        self.assertEqual(expected, extracted)

    def test_extract_struct_generic_multi(self) -> None:
        type_info: TypeInfo = self.get_type("StructWithMultiGeneric")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CStruct = CStruct(
            name="StructWithMultiGeneric",
            namespace="TestLib",
            nested=None,
            abstract=False,
            generic_args=(
                CType(name="U", generic=True),
                CType(name="V", generic=True),
            ),
            super_class=CType(name="ValueType", namespace="System"),
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={
                "System:Object.Equals(System:Object)": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System:Object.GetHashCode()": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "System:Object.GetType()": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Type", namespace="System"),),
                ),
                "System:Object.ToString()": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="String", namespace="System"),),
                ),
            },
            events={},
            nested_types={},
        )

        self.assertEqual(expected, extracted)

    def test_extract_struct_interfaces(self) -> None:
        type_info: TypeInfo = self.get_type("StructWithInterface")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CStruct = CStruct(
            name="StructWithInterface",
            namespace="TestLib",
            nested=None,
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
                "System:Object.Equals(System:Object)": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System:IEquatable[$T].Equals(TestLib:StructWithInterface)": CMethod(
                    name="Equals",
                    declaring_type=CType(
                        name="IEquatable",
                        namespace="System",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithInterface", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib:StructWithInterface.Equals(TestLib:StructWithInterface?)": CMethod(
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
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System:Object.GetHashCode()": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "System:Object.GetType()": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Type", namespace="System"),),
                ),
                "System:Object.ToString()": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="String", namespace="System"),),
                ),
                "TestLib:StructWithInterface.op_Equality(TestLib:StructWithInterface, TestLib:StructWithInterface)": CMethod(
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
                    return_types=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib:StructWithInterface.op_Inequality(TestLib:StructWithInterface, TestLib:StructWithInterface)": CMethod(
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
                    return_types=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib:StructWithInterface.__eq__(TestLib:StructWithInterface)": CMethod(
                    name="__eq__",
                    declaring_type=CType(name="StructWithInterface", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithInterface", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib:StructWithInterface.__ne__(TestLib:StructWithInterface)": CMethod(
                    name="__ne__",
                    declaring_type=CType(name="StructWithInterface", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithInterface", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
            },
            events={},
            nested_types={},
        )

        self.assertEqual(expected, extracted)

    def test_extract_struct_fields(self) -> None:
        type_info: TypeInfo = self.get_type("StructWithFields")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CStruct = CStruct(
            name="StructWithFields",
            namespace="TestLib",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=CType(name="ValueType", namespace="System"),
            interfaces=(),
            fields={
                "TestLib:StructWithFields.InstanceFieldA": CField(
                    name="InstanceFieldA",
                    declaring_type=CType(name="StructWithFields", namespace="TestLib"),
                    return_type=CType(name="Int32", namespace="System"),
                ),
                "TestLib:StructWithFields.InstanceFieldB": CField(
                    name="InstanceFieldB",
                    declaring_type=CType(name="StructWithFields", namespace="TestLib"),
                    return_type=CType(name="Int32", namespace="System"),
                ),
                "TestLib:StructWithFields.InstanceFieldC": CField(
                    name="InstanceFieldC",
                    declaring_type=CType(name="StructWithFields", namespace="TestLib"),
                    return_type=CType(name="Int32", namespace="System"),
                ),
                "TestLib:StructWithFields.StaticFieldA": CField(
                    name="StaticFieldA",
                    declaring_type=CType(name="StructWithFields", namespace="TestLib"),
                    return_type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
                "TestLib:StructWithFields.StaticFieldB": CField(
                    name="StaticFieldB",
                    declaring_type=CType(name="StructWithFields", namespace="TestLib"),
                    return_type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
                "TestLib:StructWithFields.StaticFieldC": CField(
                    name="StaticFieldC",
                    declaring_type=CType(name="StructWithFields", namespace="TestLib"),
                    return_type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
            },
            constructors={
                "TestLib:StructWithFields.__init__()": CConstructor(
                    declaring_type=CType(name="StructWithFields", namespace="TestLib"),
                    parameters=(),
                ),
            },
            properties={},
            methods={
                "System:Object.Equals(System:Object)": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System:Object.GetHashCode()": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "System:Object.GetType()": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Type", namespace="System"),),
                ),
                "System:Object.ToString()": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="String", namespace="System"),),
                ),
            },
            events={},
            nested_types={},
        )

        self.assertEqual(expected, extracted)

    def test_extract_struct_constructors(self) -> None:
        type_info: TypeInfo = self.get_type("StructWithConstructors")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CStruct = CStruct(
            name="StructWithConstructors",
            namespace="TestLib",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=CType(name="ValueType", namespace="System"),
            interfaces=(),
            fields={},
            constructors={
                "TestLib:StructWithConstructors.__init__()": CConstructor(
                    declaring_type=CType(name="StructWithConstructors", namespace="TestLib"),
                    parameters=(),
                ),
                "TestLib:StructWithConstructors.__init__(System:Int32)": CConstructor(
                    declaring_type=CType(name="StructWithConstructors", namespace="TestLib"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                    ),
                ),
                "TestLib:StructWithConstructors.__init__(System:Int32, System:Int32)": CConstructor(
                    declaring_type=CType(name="StructWithConstructors", namespace="TestLib"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                        CParameter(name="param1", type=CType(name="Int32", namespace="System")),
                    ),
                ),
                "TestLib:StructWithConstructors.__init__(System:Int32, System:Int32, System:Int32)": CConstructor(
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
                "System:Object.Equals(System:Object)": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System:Object.GetHashCode()": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "System:Object.GetType()": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Type", namespace="System"),),
                ),
                "System:Object.ToString()": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="String", namespace="System"),),
                ),
            },
            events={},
            nested_types={},
        )

        self.assertEqual(expected, extracted)

    def test_extract_struct_properties(self) -> None:
        type_info: TypeInfo = self.get_type("StructWithProperties")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CStruct = CStruct(
            name="StructWithProperties",
            namespace="TestLib",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=CType(name="ValueType", namespace="System"),
            interfaces=(),
            fields={},
            constructors={},
            properties={
                "TestLib:StructWithProperties.InstanceProperty0": CProperty(
                    name="InstanceProperty0",
                    declaring_type=CType(name="StructWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                ),
                "TestLib:StructWithProperties.InstanceProperty1": CProperty(
                    name="InstanceProperty1",
                    declaring_type=CType(name="StructWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                ),
                "TestLib:StructWithProperties.InstanceProperty2": CProperty(
                    name="InstanceProperty2",
                    declaring_type=CType(name="StructWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                ),
                "TestLib:StructWithProperties.InstanceReadOnlyProperty0": CProperty(
                    name="InstanceReadOnlyProperty0",
                    declaring_type=CType(name="StructWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                ),
                "TestLib:StructWithProperties.InstanceReadOnlyProperty1": CProperty(
                    name="InstanceReadOnlyProperty1",
                    declaring_type=CType(name="StructWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                ),
                "TestLib:StructWithProperties.InstanceReadOnlyProperty2": CProperty(
                    name="InstanceReadOnlyProperty2",
                    declaring_type=CType(name="StructWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                ),
                "TestLib:StructWithProperties.StaticProperty0": CProperty(
                    name="StaticProperty0",
                    declaring_type=CType(name="StructWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                    static=True,
                ),
                "TestLib:StructWithProperties.StaticProperty1": CProperty(
                    name="StaticProperty1",
                    declaring_type=CType(name="StructWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                    static=True,
                ),
                "TestLib:StructWithProperties.StaticProperty2": CProperty(
                    name="StaticProperty2",
                    declaring_type=CType(name="StructWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                    static=True,
                ),
                "TestLib:StructWithProperties.StaticReadOnlyProperty0": CProperty(
                    name="StaticReadOnlyProperty0",
                    declaring_type=CType(name="StructWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
                "TestLib:StructWithProperties.StaticReadOnlyProperty1": CProperty(
                    name="StaticReadOnlyProperty1",
                    declaring_type=CType(name="StructWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
                "TestLib:StructWithProperties.StaticReadOnlyProperty2": CProperty(
                    name="StaticReadOnlyProperty2",
                    declaring_type=CType(name="StructWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
            },
            methods={
                "System:Object.Equals(System:Object)": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System:Object.GetHashCode()": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "System:Object.GetType()": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Type", namespace="System"),),
                ),
                "System:Object.ToString()": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="String", namespace="System"),),
                ),
            },
            events={},
            nested_types={},
        )

        self.assertEqual(expected, extracted)

    def test_extract_struct_methods(self) -> None:
        type_info: TypeInfo = self.get_type("StructWithMethods")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CStruct = CStruct(
            name="StructWithMethods",
            namespace="TestLib",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=CType(name="ValueType", namespace="System"),
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={
                "System:Object.Equals(System:Object)": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System:Object.GetHashCode()": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "System:Object.GetType()": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Type", namespace="System"),),
                ),
                "TestLib:StructWithMethods.InstanceMethodWithDefaultParam(System:Int32)": CMethod(
                    name="InstanceMethodWithDefaultParam",
                    declaring_type=CType(name="StructWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System"),
                            default=True,
                        ),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib:StructWithMethods.InstanceMethodWithNullableDefaultParam(System:Int32?)": CMethod(
                    name="InstanceMethodWithNullableDefaultParam",
                    declaring_type=CType(name="StructWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System", nullable=True),
                            default=True,
                        ),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib:StructWithMethods.InstanceMethodWithNullableOutParam(System:*Int32?)": CMethod(
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
                    return_types=(
                        CType(name="Int32", namespace="System"),
                        CType(name="Int32", namespace="System", reference=True, nullable=True),
                    ),
                ),
                "TestLib:StructWithMethods.InstanceMethodWithNullableParam(System:Int32?)": CMethod(
                    name="InstanceMethodWithNullableParam",
                    declaring_type=CType(name="StructWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System", nullable=True),
                        ),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib:StructWithMethods.InstanceMethodWithOutParam(System:*Int32)": CMethod(
                    name="InstanceMethodWithOutParam",
                    declaring_type=CType(name="StructWithMethods", namespace="TestLib"),
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
                "TestLib:StructWithMethods.InstanceMethodWithParams0()": CMethod(
                    name="InstanceMethodWithParams0",
                    declaring_type=CType(name="StructWithMethods", namespace="TestLib"),
                    parameters=(),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib:StructWithMethods.InstanceMethodWithParams1(System:Int32)": CMethod(
                    name="InstanceMethodWithParams1",
                    declaring_type=CType(name="StructWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib:StructWithMethods.InstanceMethodWithParams2(System:Int32, System:Int32)": CMethod(
                    name="InstanceMethodWithParams2",
                    declaring_type=CType(name="StructWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                        CParameter(name="param1", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib:StructWithMethods.StaticMethodWithDefaultParam(System:Int32)": CMethod(
                    name="StaticMethodWithDefaultParam",
                    declaring_type=CType(name="StructWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System"),
                            default=True,
                        ),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                    static=True,
                ),
                "TestLib:StructWithMethods.StaticMethodWithNullableDefaultParam(System:Int32?)": CMethod(
                    name="StaticMethodWithNullableDefaultParam",
                    declaring_type=CType(name="StructWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System", nullable=True),
                            default=True,
                        ),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                    static=True,
                ),
                "TestLib:StructWithMethods.StaticMethodWithNullableOutParam(System:*Int32?)": CMethod(
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
                    return_types=(
                        CType(name="Int32", namespace="System"),
                        CType(name="Int32", namespace="System", reference=True, nullable=True),
                    ),
                    static=True,
                ),
                "TestLib:StructWithMethods.StaticMethodWithNullableParam(System:Int32?)": CMethod(
                    name="StaticMethodWithNullableParam",
                    declaring_type=CType(name="StructWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System", nullable=True),
                        ),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                    static=True,
                ),
                "TestLib:StructWithMethods.StaticMethodWithOutParam(System:*Int32)": CMethod(
                    name="StaticMethodWithOutParam",
                    declaring_type=CType(name="StructWithMethods", namespace="TestLib"),
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
                    static=True,
                ),
                "TestLib:StructWithMethods.StaticMethodWithParams0()": CMethod(
                    name="StaticMethodWithParams0",
                    declaring_type=CType(name="StructWithMethods", namespace="TestLib"),
                    parameters=(),
                    return_types=(CType(name="Int32", namespace="System"),),
                    static=True,
                ),
                "TestLib:StructWithMethods.StaticMethodWithParams1(System:Int32)": CMethod(
                    name="StaticMethodWithParams1",
                    declaring_type=CType(name="StructWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                    static=True,
                ),
                "TestLib:StructWithMethods.StaticMethodWithParams2(System:Int32, System:Int32)": CMethod(
                    name="StaticMethodWithParams2",
                    declaring_type=CType(name="StructWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                        CParameter(name="param1", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                    static=True,
                ),
                "System:Object.ToString()": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="String", namespace="System"),),
                ),
            },
            events={},
            nested_types={},
        )

        self.assertEqual(expected, extracted)

    def test_extract_struct_methods_dunder(self) -> None:
        type_info: TypeInfo = self.get_type("StructWithOperatorMethods")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CStruct = CStruct(
            name="StructWithOperatorMethods",
            namespace="TestLib",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=CType(name="ValueType", namespace="System"),
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={
                "System:Object.Equals(System:Object)": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(
                            name="obj",
                            type=CType(name="Object", namespace="System"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System:Object.GetHashCode()": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "System:Object.GetType()": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Type", namespace="System"),),
                ),
                "System:Object.ToString()": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="String", namespace="System"),),
                ),
                "TestLib:StructWithOperatorMethods.op_Addition(TestLib:StructWithOperatorMethods, TestLib:StructWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib:StructWithOperatorMethods.op_BitwiseAnd(TestLib:StructWithOperatorMethods, TestLib:StructWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib:StructWithOperatorMethods.op_BitwiseOr(TestLib:StructWithOperatorMethods, TestLib:StructWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib:StructWithOperatorMethods.op_Decrement(TestLib:StructWithOperatorMethods)": CMethod(
                    name="op_Decrement",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib:StructWithOperatorMethods.op_Division(TestLib:StructWithOperatorMethods, TestLib:StructWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib:StructWithOperatorMethods.op_Equality(TestLib:StructWithOperatorMethods, TestLib:StructWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib:StructWithOperatorMethods.op_ExclusiveOr(TestLib:StructWithOperatorMethods, TestLib:StructWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib:StructWithOperatorMethods.op_False(TestLib:StructWithOperatorMethods)": CMethod(
                    name="op_False",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib:StructWithOperatorMethods.op_GreaterThan(TestLib:StructWithOperatorMethods, TestLib:StructWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib:StructWithOperatorMethods.op_GreaterThanOrEqual(TestLib:StructWithOperatorMethods, TestLib:StructWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib:StructWithOperatorMethods.op_Increment(TestLib:StructWithOperatorMethods)": CMethod(
                    name="op_Increment",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib:StructWithOperatorMethods.op_Inequality(TestLib:StructWithOperatorMethods, TestLib:StructWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib:StructWithOperatorMethods.op_LessThan(TestLib:StructWithOperatorMethods, TestLib:StructWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib:StructWithOperatorMethods.op_LessThanOrEqual(TestLib:StructWithOperatorMethods, TestLib:StructWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib:StructWithOperatorMethods.op_LogicalNot(TestLib:StructWithOperatorMethods)": CMethod(
                    name="op_LogicalNot",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib:StructWithOperatorMethods.op_Modulus(TestLib:StructWithOperatorMethods, TestLib:StructWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib:StructWithOperatorMethods.op_Multiply(TestLib:StructWithOperatorMethods, TestLib:StructWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib:StructWithOperatorMethods.op_OnesComplement(TestLib:StructWithOperatorMethods)": CMethod(
                    name="op_OnesComplement",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib:StructWithOperatorMethods.op_Subtraction(TestLib:StructWithOperatorMethods, TestLib:StructWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib:StructWithOperatorMethods.op_True(TestLib:StructWithOperatorMethods)": CMethod(
                    name="op_True",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib:StructWithOperatorMethods.op_UnaryNegation(TestLib:StructWithOperatorMethods)": CMethod(
                    name="op_UnaryNegation",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib:StructWithOperatorMethods.op_UnaryPlus(TestLib:StructWithOperatorMethods)": CMethod(
                    name="op_UnaryPlus",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                    static=True,
                ),
                "TestLib:StructWithOperatorMethods.__add__(TestLib:StructWithOperatorMethods)": CMethod(
                    name="__add__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib:StructWithOperatorMethods.__and__(TestLib:StructWithOperatorMethods)": CMethod(
                    name="__and__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib:StructWithOperatorMethods.__eq__(TestLib:StructWithOperatorMethods)": CMethod(
                    name="__eq__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib:StructWithOperatorMethods.__ge__(TestLib:StructWithOperatorMethods)": CMethod(
                    name="__ge__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib:StructWithOperatorMethods.__gt__(TestLib:StructWithOperatorMethods)": CMethod(
                    name="__gt__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib:StructWithOperatorMethods.__invert__()": CMethod(
                    name="__invert__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(),
                    return_types=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib:StructWithOperatorMethods.__le__(TestLib:StructWithOperatorMethods)": CMethod(
                    name="__le__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib:StructWithOperatorMethods.__lt__(TestLib:StructWithOperatorMethods)": CMethod(
                    name="__lt__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib:StructWithOperatorMethods.__mod__(TestLib:StructWithOperatorMethods)": CMethod(
                    name="__mod__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib:StructWithOperatorMethods.__mul__(TestLib:StructWithOperatorMethods)": CMethod(
                    name="__mul__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib:StructWithOperatorMethods.__ne__(TestLib:StructWithOperatorMethods)": CMethod(
                    name="__ne__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib:StructWithOperatorMethods.__neg__()": CMethod(
                    name="__neg__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(),
                    return_types=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib:StructWithOperatorMethods.__or__(TestLib:StructWithOperatorMethods)": CMethod(
                    name="__or__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib:StructWithOperatorMethods.__pos__()": CMethod(
                    name="__pos__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(),
                    return_types=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib:StructWithOperatorMethods.__sub__(TestLib:StructWithOperatorMethods)": CMethod(
                    name="__sub__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib:StructWithOperatorMethods.__truediv__(TestLib:StructWithOperatorMethods)": CMethod(
                    name="__truediv__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                ),
                "TestLib:StructWithOperatorMethods.__xor__(TestLib:StructWithOperatorMethods)": CMethod(
                    name="__xor__",
                    declaring_type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="StructWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="StructWithOperatorMethods", namespace="TestLib"),),
                ),
            },
            events={},
            nested_types={},
        )

        self.assertEqual(expected, extracted)

    def test_extract_struct_methods_list(self) -> None:
        type_info: TypeInfo = self.get_type("StructWithListMethods")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CStruct = CStruct(
            name="StructWithListMethods",
            namespace="TestLib",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=CType(name="ValueType", namespace="System"),
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
                CType(
                    name="IList",
                    namespace="System.Collections.Generic",
                    inner=(CType(name="Int32", namespace="System"),),
                ),
            ),
            fields={},
            constructors={},
            properties={
                "System.Collections.Generic:ICollection[$T].Count": CProperty(
                    name="Count",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    type=CType(name="Int32", namespace="System"),
                ),
                "System.Collections.Generic:ICollection[$T].IsReadOnly": CProperty(
                    name="IsReadOnly",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    type=CType(name="Boolean", namespace="System"),
                ),
            },
            methods={
                "System.Collections.Generic:ICollection[$T].Add(System:Int32)": CMethod(
                    name="Add",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(name="item", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Void", namespace="System"),),
                ),
                "System.Collections.Generic:ICollection[$T].Clear()": CMethod(
                    name="Clear",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(),
                    return_types=(CType(name="Void", namespace="System"),),
                ),
                "System.Collections.Generic:ICollection[$T].Contains(System:Int32)": CMethod(
                    name="Contains",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(name="item", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Collections.Generic:ICollection[$T].CopyTo(System:Array[System:Int32], System:Int32)": CMethod(
                    name="CopyTo",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(
                            name="array",
                            type=CType(
                                name="Array",
                                namespace="System",
                                inner=(CType(name="Int32", namespace="System"),),
                            ),
                        ),
                        CParameter(name="arrayIndex", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Void", namespace="System"),),
                ),
                "System:Object.Equals(System:Object)": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Collections:IEnumerable.GetEnumerator()": CMethod(
                    name="GetEnumerator",
                    declaring_type=CType(name="IEnumerable", namespace="System.Collections"),
                    parameters=(),
                    return_types=(
                        CType(
                            name="IEnumerator",
                            namespace="System.Collections.Generic",
                            inner=(CType(name="Int32", namespace="System"),),
                        ),
                    ),
                ),
                "System:Object.GetHashCode()": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "System:Object.GetType()": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Type", namespace="System"),),
                ),
                "System.Collections.Generic:IList[$T].IndexOf(System:Int32)": CMethod(
                    name="IndexOf",
                    declaring_type=CType(
                        name="IList",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(name="item", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "System.Collections.Generic:IList[$T].Insert(System:Int32, System:Int32)": CMethod(
                    name="Insert",
                    declaring_type=CType(
                        name="IList",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(name="index", type=CType(name="Int32", namespace="System")),
                        CParameter(name="item", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Void", namespace="System"),),
                ),
                "System.Collections.Generic:ICollection[$T].Remove(System:Int32)": CMethod(
                    name="Remove",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(name="item", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Collections.Generic:IList[$T].RemoveAt(System:Int32)": CMethod(
                    name="RemoveAt",
                    declaring_type=CType(
                        name="IList",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(name="index", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Void", namespace="System"),),
                ),
                "System:Object.ToString()": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="String", namespace="System"),),
                ),
                "System.Collections.Generic:ICollection[$T].__contains__(System:Int32)": CMethod(
                    name="__contains__",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(name="item", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Collections.Generic:ICollection[$T].__delitem__(System:Int32)": CMethod(
                    name="__delitem__",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(name="item", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Collections.Generic:IList[$T].__getitem__(System:Int32)": CMethod(
                    name="__getitem__",
                    declaring_type=CType(
                        name="IList",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(name="index", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "System.Collections:IEnumerable.__iter__()": CMethod(
                    name="__iter__",
                    declaring_type=CType(name="IEnumerable", namespace="System.Collections"),
                    parameters=(),
                    return_types=(
                        CType(
                            name="Iterator",
                            namespace="typing",
                            inner=(CType(name="Int32", namespace="System"),),
                        ),
                    ),
                ),
                "System.Collections.Generic:ICollection[$T].__len__()": CMethod(
                    name="__len__",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "System.Collections.Generic:IList[$T].__setitem__(System:Int32, System:Int32)": CMethod(
                    name="__setitem__",
                    declaring_type=CType(
                        name="IList",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(name="index", type=CType(name="Int32", namespace="System")),
                        CParameter(name="value", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Void", namespace="System"),),
                ),
            },
            events={},
            nested_types={},
        )

        self.assertEqual(expected, extracted)

    def test_extract_struct_events(self) -> None:
        type_info: TypeInfo = self.get_type("StructWithEvents")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CStruct = CStruct(
            name="StructWithEvents",
            namespace="TestLib",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=CType(name="ValueType", namespace="System"),
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={
                "System:Object.Equals(System:Object)": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System:Object.GetHashCode()": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "System:Object.GetType()": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Type", namespace="System"),),
                ),
                "System:Object.ToString()": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="String", namespace="System"),),
                ),
            },
            events={
                "TestLib:StructWithEvents.Event": CEvent(
                    name="Event",
                    declaring_type=CType(name="StructWithEvents", namespace="TestLib"),
                    type=CType(name="EventHandler", namespace="System"),
                ),
                "TestLib:StructWithEvents.EventWithArgs": CEvent(
                    name="EventWithArgs",
                    declaring_type=CType(name="StructWithEvents", namespace="TestLib"),
                    type=CType(
                        name="EventHandler",
                        namespace="System",
                        inner=(CType(name="EventArgs", namespace="System"),),
                    ),
                ),
            },
            nested_types={},
        )

        self.assertEqual(expected, extracted)

    def test_extract_struct_nested(self) -> None:
        type_info: TypeInfo = self.get_type("StructWithNested")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CStruct = CStruct(
            name="StructWithNested",
            namespace="TestLib",
            nested=None,
            abstract=False,
            generic_args=(),
            super_class=CType(name="ValueType", namespace="System"),
            interfaces=(),
            fields={},
            constructors={},
            properties={},
            methods={
                "System:Object.Equals(System:Object)": CMethod(
                    name="Equals",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(
                        CParameter(name="obj", type=CType(name="Object", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System:Object.GetHashCode()": CMethod(
                    name="GetHashCode",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "System:Object.GetType()": CMethod(
                    name="GetType",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="Type", namespace="System"),),
                ),
                "System:Object.ToString()": CMethod(
                    name="ToString",
                    declaring_type=CType(name="Object", namespace="System"),
                    parameters=(),
                    return_types=(CType(name="String", namespace="System"),),
                ),
            },
            events={},
            nested_types={
                "TestLib:StructWithNested.INestedInterface": CInterface(
                    name="INestedInterface",
                    namespace="TestLib",
                    nested=CType(name="StructWithNested", namespace="TestLib"),
                    generic_args=(),
                    interfaces=(),
                    fields={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "TestLib:StructWithNested.NestedClass": CClass(
                    name="NestedClass",
                    namespace="TestLib",
                    nested=CType(name="StructWithNested", namespace="TestLib"),
                    abstract=False,
                    generic_args=(),
                    super_class=CType(name="Object", namespace="System"),
                    interfaces=(),
                    fields={},
                    constructors={
                        "TestLib:StructWithNested.NestedClass.__init__()": CConstructor(
                            declaring_type=CType(
                                name="StructWithNested.NestedClass",
                                namespace="TestLib",
                            ),
                            parameters=(),
                        )
                    },
                    properties={},
                    methods={
                        "System:Object.Equals(System:Object)": CMethod(
                            name="Equals",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(
                                CParameter(
                                    name="obj",
                                    type=CType(name="Object", namespace="System"),
                                ),
                            ),
                            return_types=(CType(name="Boolean", namespace="System"),),
                        ),
                        "System:Object.GetHashCode()": CMethod(
                            name="GetHashCode",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            return_types=(CType(name="Int32", namespace="System"),),
                        ),
                        "System:Object.GetType()": CMethod(
                            name="GetType",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            return_types=(CType(name="Type", namespace="System"),),
                        ),
                        "System:Object.ToString()": CMethod(
                            name="ToString",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            return_types=(CType(name="String", namespace="System"),),
                        ),
                    },
                    events={},
                    nested_types={},
                ),
                "TestLib:StructWithNested.NestedDelegate()": CDelegate(
                    name="NestedDelegate",
                    namespace="TestLib",
                    nested=CType(name="StructWithNested", namespace="TestLib"),
                    parameters=(),
                    return_type=CType(name="Void", namespace="System"),
                ),
                "TestLib:StructWithNested.NestedEnum": CEnum(
                    name="NestedEnum",
                    namespace="TestLib",
                    nested=CType(name="StructWithNested", namespace="TestLib"),
                    fields=(),
                ),
                "TestLib:StructWithNested.NestedStruct": CStruct(
                    name="NestedStruct",
                    namespace="TestLib",
                    nested=CType(name="StructWithNested", namespace="TestLib"),
                    abstract=False,
                    generic_args=(),
                    super_class=CType(name="ValueType", namespace="System"),
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={
                        "System:Object.Equals(System:Object)": CMethod(
                            name="Equals",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(
                                CParameter(
                                    name="obj",
                                    type=CType(name="Object", namespace="System"),
                                ),
                            ),
                            return_types=(CType(name="Boolean", namespace="System"),),
                        ),
                        "System:Object.GetHashCode()": CMethod(
                            name="GetHashCode",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            return_types=(CType(name="Int32", namespace="System"),),
                        ),
                        "System:Object.GetType()": CMethod(
                            name="GetType",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            return_types=(CType(name="Type", namespace="System"),),
                        ),
                        "System:Object.ToString()": CMethod(
                            name="ToString",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            return_types=(CType(name="String", namespace="System"),),
                        ),
                    },
                    events={},
                    nested_types={},
                ),
            },
        )

        self.assertEqual(expected, extracted)


class TestCInterface(TestExtractBase):
    def test_extract_interface_generic(self) -> None:
        type_info: TypeInfo = self.get_type("IInterfaceWithGeneric")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CInterface = CInterface(
            name="IInterfaceWithGeneric",
            namespace="TestLib",
            nested=None,
            generic_args=(CType(name="T", generic=True),),
            interfaces=(),
            fields={},
            properties={},
            methods={
                "TestLib:IInterfaceWithGeneric[$T].MethodWithGeneric($T)": CMethod(
                    name="MethodWithGeneric",
                    declaring_type=CType(
                        name="IInterfaceWithGeneric",
                        namespace="TestLib",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(CParameter(name="param0", type=CType("T", generic=True)),),
                    return_types=(CType(name="Void", namespace="System"),),
                ),
            },
            events={},
            nested_types={},
        )

        self.assertEqual(expected, extracted)

    def test_extract_interface_generic_multi(self) -> None:
        type_info: TypeInfo = self.get_type("IInterfaceWithMultiGeneric")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CInterface = CInterface(
            name="IInterfaceWithMultiGeneric",
            namespace="TestLib",
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

        self.assertEqual(expected, extracted)

    def test_extract_interface_interfaces(self) -> None:
        type_info: TypeInfo = self.get_type("IInterfaceWithInterface")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CInterface = CInterface(
            name="IInterfaceWithInterface",
            namespace="TestLib",
            nested=None,
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
                "System:IEquatable[$T].Equals(TestLib:IInterfaceWithInterface)": CMethod(
                    name="Equals",
                    declaring_type=CType(
                        name="IEquatable",
                        namespace="System",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithInterface", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
            },
            events={},
            nested_types={},
        )

        self.assertEqual(expected, extracted)

    def test_extract_interface_fields(self) -> None:
        type_info: TypeInfo = self.get_type("IInterfaceWithFields")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CInterface = CInterface(
            name="IInterfaceWithFields",
            namespace="TestLib",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={
                "TestLib:IInterfaceWithFields.StaticFieldA": CField(
                    name="StaticFieldA",
                    declaring_type=CType(name="IInterfaceWithFields", namespace="TestLib"),
                    return_type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
                "TestLib:IInterfaceWithFields.StaticFieldB": CField(
                    name="StaticFieldB",
                    declaring_type=CType(name="IInterfaceWithFields", namespace="TestLib"),
                    return_type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
                "TestLib:IInterfaceWithFields.StaticFieldC": CField(
                    name="StaticFieldC",
                    declaring_type=CType(name="IInterfaceWithFields", namespace="TestLib"),
                    return_type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
            },
            properties={},
            methods={},
            events={},
            nested_types={},
        )

        self.assertEqual(expected, extracted)

    def test_extract_interface_properties(self) -> None:
        type_info: TypeInfo = self.get_type("IInterfaceWithProperties")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CInterface = CInterface(
            name="IInterfaceWithProperties",
            namespace="TestLib",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={
                "TestLib:IInterfaceWithProperties.InstanceProperty0": CProperty(
                    name="InstanceProperty0",
                    declaring_type=CType(name="IInterfaceWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                ),
                "TestLib:IInterfaceWithProperties.InstanceProperty1": CProperty(
                    name="InstanceProperty1",
                    declaring_type=CType(name="IInterfaceWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                ),
                "TestLib:IInterfaceWithProperties.InstanceProperty2": CProperty(
                    name="InstanceProperty2",
                    declaring_type=CType(name="IInterfaceWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                ),
                "TestLib:IInterfaceWithProperties.InstanceReadOnlyProperty0": CProperty(
                    name="InstanceReadOnlyProperty0",
                    declaring_type=CType(name="IInterfaceWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                ),
                "TestLib:IInterfaceWithProperties.InstanceReadOnlyProperty1": CProperty(
                    name="InstanceReadOnlyProperty1",
                    declaring_type=CType(name="IInterfaceWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                ),
                "TestLib:IInterfaceWithProperties.InstanceReadOnlyProperty2": CProperty(
                    name="InstanceReadOnlyProperty2",
                    declaring_type=CType(name="IInterfaceWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                ),
                "TestLib:IInterfaceWithProperties.StaticProperty0": CProperty(
                    name="StaticProperty0",
                    declaring_type=CType(name="IInterfaceWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                    static=True,
                ),
                "TestLib:IInterfaceWithProperties.StaticProperty1": CProperty(
                    name="StaticProperty1",
                    declaring_type=CType(name="IInterfaceWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                    static=True,
                ),
                "TestLib:IInterfaceWithProperties.StaticProperty2": CProperty(
                    name="StaticProperty2",
                    declaring_type=CType(name="IInterfaceWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    setter=True,
                    static=True,
                ),
                "TestLib:IInterfaceWithProperties.StaticReadOnlyProperty0": CProperty(
                    name="StaticReadOnlyProperty0",
                    declaring_type=CType(name="IInterfaceWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
                "TestLib:IInterfaceWithProperties.StaticReadOnlyProperty1": CProperty(
                    name="StaticReadOnlyProperty1",
                    declaring_type=CType(name="IInterfaceWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
                "TestLib:IInterfaceWithProperties.StaticReadOnlyProperty2": CProperty(
                    name="StaticReadOnlyProperty2",
                    declaring_type=CType(name="IInterfaceWithProperties", namespace="TestLib"),
                    type=CType(name="Int32", namespace="System"),
                    static=True,
                ),
            },
            methods={},
            events={},
            nested_types={},
        )

        self.assertEqual(expected, extracted)

    def test_extract_interface_methods(self) -> None:
        type_info: TypeInfo = self.get_type("IInterfaceWithMethods")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CInterface = CInterface(
            name="IInterfaceWithMethods",
            namespace="TestLib",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={
                "TestLib:IInterfaceWithMethods.InstanceMethodWithDefaultParam(System:Int32)": CMethod(
                    name="InstanceMethodWithDefaultParam",
                    declaring_type=CType(name="IInterfaceWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System"),
                            default=True,
                        ),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib:IInterfaceWithMethods.InstanceMethodWithNullableDefaultParam(System:Int32?)": CMethod(
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
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib:IInterfaceWithMethods.InstanceMethodWithNullableOutParam(System:*Int32?)": CMethod(
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
                    return_types=(
                        CType(name="Int32", namespace="System"),
                        CType(name="Int32", namespace="System", reference=True, nullable=True),
                    ),
                ),
                "TestLib:IInterfaceWithMethods.InstanceMethodWithNullableParam(System:Int32?)": CMethod(
                    name="InstanceMethodWithNullableParam",
                    declaring_type=CType(name="IInterfaceWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="param0",
                            type=CType(name="Int32", namespace="System", nullable=True),
                        ),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib:IInterfaceWithMethods.InstanceMethodWithOutParam(System:*Int32)": CMethod(
                    name="InstanceMethodWithOutParam",
                    declaring_type=CType(name="IInterfaceWithMethods", namespace="TestLib"),
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
                "TestLib:IInterfaceWithMethods.InstanceMethodWithParams()": CMethod(
                    name="InstanceMethodWithParams",
                    declaring_type=CType(name="IInterfaceWithMethods", namespace="TestLib"),
                    parameters=(),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib:IInterfaceWithMethods.InstanceMethodWithParams(System:Int32)": CMethod(
                    name="InstanceMethodWithParams",
                    declaring_type=CType(name="IInterfaceWithMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "TestLib:IInterfaceWithMethods.InstanceMethodWithParams(System:Int32, System:Int32)": CMethod(
                    name="InstanceMethodWithParams",
                    declaring_type=CType(name="IInterfaceWithMethods", namespace="TestLib"),
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

        self.assertEqual(expected, extracted)

    def test_extract_interface_methods_dunder(self) -> None:
        type_info: TypeInfo = self.get_type("IInterfaceWithOperatorMethods")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CInterface = CInterface(
            name="IInterfaceWithOperatorMethods",
            namespace="TestLib",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={
                "TestLib:IInterfaceWithOperatorMethods.op_Addition(TestLib:IInterfaceWithOperatorMethods, TestLib:IInterfaceWithOperatorMethods)": CMethod(
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
                    return_types=(
                        CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    ),
                    static=True,
                ),
                "TestLib:IInterfaceWithOperatorMethods.op_BitwiseAnd(TestLib:IInterfaceWithOperatorMethods, TestLib:IInterfaceWithOperatorMethods)": CMethod(
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
                    return_types=(
                        CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    ),
                    static=True,
                ),
                "TestLib:IInterfaceWithOperatorMethods.op_BitwiseOr(TestLib:IInterfaceWithOperatorMethods, TestLib:IInterfaceWithOperatorMethods)": CMethod(
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
                    return_types=(
                        CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    ),
                    static=True,
                ),
                "TestLib:IInterfaceWithOperatorMethods.op_Decrement(TestLib:IInterfaceWithOperatorMethods)": CMethod(
                    name="op_Decrement",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(
                        CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    ),
                    static=True,
                ),
                "TestLib:IInterfaceWithOperatorMethods.op_Division(TestLib:IInterfaceWithOperatorMethods, TestLib:IInterfaceWithOperatorMethods)": CMethod(
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
                    return_types=(
                        CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    ),
                    static=True,
                ),
                "TestLib:IInterfaceWithOperatorMethods.op_ExclusiveOr(TestLib:IInterfaceWithOperatorMethods, TestLib:IInterfaceWithOperatorMethods)": CMethod(
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
                    return_types=(
                        CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    ),
                    static=True,
                ),
                "TestLib:IInterfaceWithOperatorMethods.op_False(TestLib:IInterfaceWithOperatorMethods)": CMethod(
                    name="op_False",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib:IInterfaceWithOperatorMethods.op_GreaterThan(TestLib:IInterfaceWithOperatorMethods, TestLib:IInterfaceWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib:IInterfaceWithOperatorMethods.op_GreaterThanOrEqual(TestLib:IInterfaceWithOperatorMethods, TestLib:IInterfaceWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib:IInterfaceWithOperatorMethods.op_Increment(TestLib:IInterfaceWithOperatorMethods)": CMethod(
                    name="op_Increment",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(
                        CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    ),
                    static=True,
                ),
                "TestLib:IInterfaceWithOperatorMethods.op_LessThan(TestLib:IInterfaceWithOperatorMethods, TestLib:IInterfaceWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib:IInterfaceWithOperatorMethods.op_LessThanOrEqual(TestLib:IInterfaceWithOperatorMethods, TestLib:IInterfaceWithOperatorMethods)": CMethod(
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
                    return_types=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib:IInterfaceWithOperatorMethods.op_LogicalNot(TestLib:IInterfaceWithOperatorMethods)": CMethod(
                    name="op_LogicalNot",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib:IInterfaceWithOperatorMethods.op_Modulus(TestLib:IInterfaceWithOperatorMethods, TestLib:IInterfaceWithOperatorMethods)": CMethod(
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
                    return_types=(
                        CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    ),
                    static=True,
                ),
                "TestLib:IInterfaceWithOperatorMethods.op_Multiply(TestLib:IInterfaceWithOperatorMethods, TestLib:IInterfaceWithOperatorMethods)": CMethod(
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
                    return_types=(
                        CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    ),
                    static=True,
                ),
                "TestLib:IInterfaceWithOperatorMethods.op_OnesComplement(TestLib:IInterfaceWithOperatorMethods)": CMethod(
                    name="op_OnesComplement",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(
                        CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    ),
                    static=True,
                ),
                "TestLib:IInterfaceWithOperatorMethods.op_Subtraction(TestLib:IInterfaceWithOperatorMethods, TestLib:IInterfaceWithOperatorMethods)": CMethod(
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
                    return_types=(
                        CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    ),
                    static=True,
                ),
                "TestLib:IInterfaceWithOperatorMethods.op_True(TestLib:IInterfaceWithOperatorMethods)": CMethod(
                    name="op_True",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                    static=True,
                ),
                "TestLib:IInterfaceWithOperatorMethods.op_UnaryNegation(TestLib:IInterfaceWithOperatorMethods)": CMethod(
                    name="op_UnaryNegation",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(
                        CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    ),
                    static=True,
                ),
                "TestLib:IInterfaceWithOperatorMethods.op_UnaryPlus(TestLib:IInterfaceWithOperatorMethods)": CMethod(
                    name="op_UnaryPlus",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="self",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(
                        CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    ),
                    static=True,
                ),
                "TestLib:IInterfaceWithOperatorMethods.__add__(TestLib:IInterfaceWithOperatorMethods)": CMethod(
                    name="__add__",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(
                        CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    ),
                ),
                "TestLib:IInterfaceWithOperatorMethods.__and__(TestLib:IInterfaceWithOperatorMethods)": CMethod(
                    name="__and__",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(
                        CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    ),
                ),
                "TestLib:IInterfaceWithOperatorMethods.__ge__(TestLib:IInterfaceWithOperatorMethods)": CMethod(
                    name="__ge__",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib:IInterfaceWithOperatorMethods.__gt__(TestLib:IInterfaceWithOperatorMethods)": CMethod(
                    name="__gt__",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib:IInterfaceWithOperatorMethods.__invert__()": CMethod(
                    name="__invert__",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(),
                    return_types=(
                        CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    ),
                ),
                "TestLib:IInterfaceWithOperatorMethods.__le__(TestLib:IInterfaceWithOperatorMethods)": CMethod(
                    name="__le__",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib:IInterfaceWithOperatorMethods.__lt__(TestLib:IInterfaceWithOperatorMethods)": CMethod(
                    name="__lt__",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "TestLib:IInterfaceWithOperatorMethods.__mod__(TestLib:IInterfaceWithOperatorMethods)": CMethod(
                    name="__mod__",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(
                        CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    ),
                ),
                "TestLib:IInterfaceWithOperatorMethods.__mul__(TestLib:IInterfaceWithOperatorMethods)": CMethod(
                    name="__mul__",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(
                        CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    ),
                ),
                "TestLib:IInterfaceWithOperatorMethods.__neg__()": CMethod(
                    name="__neg__",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(),
                    return_types=(
                        CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    ),
                ),
                "TestLib:IInterfaceWithOperatorMethods.__or__(TestLib:IInterfaceWithOperatorMethods)": CMethod(
                    name="__or__",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(
                        CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    ),
                ),
                "TestLib:IInterfaceWithOperatorMethods.__pos__()": CMethod(
                    name="__pos__",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(),
                    return_types=(
                        CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    ),
                ),
                "TestLib:IInterfaceWithOperatorMethods.__sub__(TestLib:IInterfaceWithOperatorMethods)": CMethod(
                    name="__sub__",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(
                        CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    ),
                ),
                "TestLib:IInterfaceWithOperatorMethods.__truediv__(TestLib:IInterfaceWithOperatorMethods)": CMethod(
                    name="__truediv__",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(
                        CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    ),
                ),
                "TestLib:IInterfaceWithOperatorMethods.__xor__(TestLib:IInterfaceWithOperatorMethods)": CMethod(
                    name="__xor__",
                    declaring_type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    parameters=(
                        CParameter(
                            name="other",
                            type=CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                        ),
                    ),
                    return_types=(
                        CType(name="IInterfaceWithOperatorMethods", namespace="TestLib"),
                    ),
                ),
            },
            events={},
            nested_types={},
        )

        self.assertEqual(expected, extracted)

    def test_extract_interface_methods_list(self) -> None:
        type_info: TypeInfo = self.get_type("IInterfaceWithListMethods")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CInterface = CInterface(
            name="IInterfaceWithListMethods",
            namespace="TestLib",
            nested=None,
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
                CType(
                    name="IList",
                    namespace="System.Collections.Generic",
                    inner=(CType(name="Int32", namespace="System"),),
                ),
            ),
            fields={},
            properties={
                "System.Collections.Generic:ICollection[$T].Count": CProperty(
                    name="Count",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    type=CType(name="Int32", namespace="System"),
                ),
                "System.Collections.Generic:ICollection[$T].IsReadOnly": CProperty(
                    name="IsReadOnly",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    type=CType(name="Boolean", namespace="System"),
                ),
            },
            methods={
                "System.Collections.Generic:ICollection[$T].Add(System:Int32)": CMethod(
                    name="Add",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(name="item", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Void", namespace="System"),),
                ),
                "System.Collections.Generic:ICollection[$T].Clear()": CMethod(
                    name="Clear",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(),
                    return_types=(CType(name="Void", namespace="System"),),
                ),
                "System.Collections.Generic:ICollection[$T].Contains(System:Int32)": CMethod(
                    name="Contains",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(name="item", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Collections.Generic:ICollection[$T].CopyTo(System:Array[System:Int32], System:Int32)": CMethod(
                    name="CopyTo",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(
                            name="array",
                            type=CType(
                                name="Array",
                                namespace="System",
                                inner=(CType(name="Int32", namespace="System"),),
                            ),
                        ),
                        CParameter(name="arrayIndex", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Void", namespace="System"),),
                ),
                "System.Collections:IEnumerable.GetEnumerator()": CMethod(
                    name="GetEnumerator",
                    declaring_type=CType(name="IEnumerable", namespace="System.Collections"),
                    parameters=(),
                    return_types=(
                        CType(
                            name="IEnumerator",
                            namespace="System.Collections.Generic",
                            inner=(CType(name="Int32", namespace="System"),),
                        ),
                    ),
                ),
                "System.Collections.Generic:IList[$T].IndexOf(System:Int32)": CMethod(
                    name="IndexOf",
                    declaring_type=CType(
                        name="IList",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(name="item", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "System.Collections.Generic:IList[$T].Insert(System:Int32, System:Int32)": CMethod(
                    name="Insert",
                    declaring_type=CType(
                        name="IList",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(name="index", type=CType(name="Int32", namespace="System")),
                        CParameter(name="item", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Void", namespace="System"),),
                ),
                "System.Collections.Generic:ICollection[$T].Remove(System:Int32)": CMethod(
                    name="Remove",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(name="item", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Collections.Generic:IList[$T].RemoveAt(System:Int32)": CMethod(
                    name="RemoveAt",
                    declaring_type=CType(
                        name="IList",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(name="index", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Void", namespace="System"),),
                ),
                "System.Collections.Generic:ICollection[$T].__contains__(System:Int32)": CMethod(
                    name="__contains__",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(name="item", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Collections.Generic:ICollection[$T].__delitem__(System:Int32)": CMethod(
                    name="__delitem__",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(name="item", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Boolean", namespace="System"),),
                ),
                "System.Collections.Generic:IList[$T].__getitem__(System:Int32)": CMethod(
                    name="__getitem__",
                    declaring_type=CType(
                        name="IList",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(name="index", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "System.Collections:IEnumerable.__iter__()": CMethod(
                    name="__iter__",
                    declaring_type=CType(name="IEnumerable", namespace="System.Collections"),
                    parameters=(),
                    return_types=(
                        CType(
                            name="Iterator",
                            namespace="typing",
                            inner=(CType(name="Int32", namespace="System"),),
                        ),
                    ),
                ),
                "System.Collections.Generic:ICollection[$T].__len__()": CMethod(
                    name="__len__",
                    declaring_type=CType(
                        name="ICollection",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(),
                    return_types=(CType(name="Int32", namespace="System"),),
                ),
                "System.Collections.Generic:IList[$T].__setitem__(System:Int32, System:Int32)": CMethod(
                    name="__setitem__",
                    declaring_type=CType(
                        name="IList",
                        namespace="System.Collections.Generic",
                        inner=(CType(name="T", generic=True),),
                    ),
                    parameters=(
                        CParameter(name="index", type=CType(name="Int32", namespace="System")),
                        CParameter(name="value", type=CType(name="Int32", namespace="System")),
                    ),
                    return_types=(CType(name="Void", namespace="System"),),
                ),
            },
            events={},
            nested_types={},
        )

        self.assertEqual(expected, extracted)

    def test_extract_interface_events(self) -> None:
        type_info: TypeInfo = self.get_type("IInterfaceWithEvents")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CInterface = CInterface(
            name="IInterfaceWithEvents",
            namespace="TestLib",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            events={
                "TestLib:IInterfaceWithEvents.Event": CEvent(
                    name="Event",
                    declaring_type=CType(name="IInterfaceWithEvents", namespace="TestLib"),
                    type=CType(name="EventHandler", namespace="System"),
                ),
                "TestLib:IInterfaceWithEvents.EventWithArgs": CEvent(
                    name="EventWithArgs",
                    declaring_type=CType(name="IInterfaceWithEvents", namespace="TestLib"),
                    type=CType(
                        name="EventHandler",
                        namespace="System",
                        inner=(CType(name="EventArgs", namespace="System"),),
                    ),
                ),
            },
            nested_types={},
        )

        self.assertEqual(expected, extracted)

    def test_extract_interface_nested(self) -> None:
        type_info: TypeInfo = self.get_type("IInterfaceWithNested")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CInterface = CInterface(
            name="IInterfaceWithNested",
            namespace="TestLib",
            nested=None,
            generic_args=(),
            interfaces=(),
            fields={},
            properties={},
            methods={},
            events={},
            nested_types={
                "TestLib:IInterfaceWithNested.INestedInterface": CInterface(
                    name="INestedInterface",
                    namespace="TestLib",
                    nested=CType(name="IInterfaceWithNested", namespace="TestLib"),
                    generic_args=(),
                    interfaces=(),
                    fields={},
                    properties={},
                    methods={},
                    events={},
                    nested_types={},
                ),
                "TestLib:IInterfaceWithNested.NestedClass": CClass(
                    name="NestedClass",
                    namespace="TestLib",
                    nested=CType(name="IInterfaceWithNested", namespace="TestLib"),
                    abstract=False,
                    generic_args=(),
                    super_class=CType(name="Object", namespace="System"),
                    interfaces=(),
                    fields={},
                    constructors={
                        "TestLib:IInterfaceWithNested.NestedClass.__init__()": CConstructor(
                            declaring_type=CType(
                                name="IInterfaceWithNested.NestedClass",
                                namespace="TestLib",
                            ),
                            parameters=(),
                        ),
                    },
                    properties={},
                    methods={
                        "System:Object.Equals(System:Object)": CMethod(
                            name="Equals",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(
                                CParameter(
                                    name="obj",
                                    type=CType(name="Object", namespace="System"),
                                ),
                            ),
                            return_types=(CType(name="Boolean", namespace="System"),),
                        ),
                        "System:Object.GetHashCode()": CMethod(
                            name="GetHashCode",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            return_types=(CType(name="Int32", namespace="System"),),
                        ),
                        "System:Object.GetType()": CMethod(
                            name="GetType",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            return_types=(CType(name="Type", namespace="System"),),
                        ),
                        "System:Object.ToString()": CMethod(
                            name="ToString",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            return_types=(CType(name="String", namespace="System"),),
                        ),
                    },
                    events={},
                    nested_types={},
                ),
                "TestLib:IInterfaceWithNested.NestedDelegate()": CDelegate(
                    name="NestedDelegate",
                    namespace="TestLib",
                    nested=CType(name="IInterfaceWithNested", namespace="TestLib"),
                    parameters=(),
                    return_type=CType(name="Void", namespace="System"),
                ),
                "TestLib:IInterfaceWithNested.NestedEnum": CEnum(
                    name="NestedEnum",
                    namespace="TestLib",
                    nested=CType(name="IInterfaceWithNested", namespace="TestLib"),
                    fields=(),
                ),
                "TestLib:IInterfaceWithNested.NestedStruct": CStruct(
                    name="NestedStruct",
                    namespace="TestLib",
                    nested=CType(name="IInterfaceWithNested", namespace="TestLib"),
                    abstract=False,
                    generic_args=(),
                    super_class=CType(name="ValueType", namespace="System"),
                    interfaces=(),
                    fields={},
                    constructors={},
                    properties={},
                    methods={
                        "System:Object.Equals(System:Object)": CMethod(
                            name="Equals",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(
                                CParameter(
                                    name="obj",
                                    type=CType(name="Object", namespace="System"),
                                ),
                            ),
                            return_types=(CType(name="Boolean", namespace="System"),),
                        ),
                        "System:Object.GetHashCode()": CMethod(
                            name="GetHashCode",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            return_types=(CType(name="Int32", namespace="System"),),
                        ),
                        "System:Object.GetType()": CMethod(
                            name="GetType",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            return_types=(CType(name="Type", namespace="System"),),
                        ),
                        "System:Object.ToString()": CMethod(
                            name="ToString",
                            declaring_type=CType(name="Object", namespace="System"),
                            parameters=(),
                            return_types=(CType(name="String", namespace="System"),),
                        ),
                    },
                    events={},
                    nested_types={},
                ),
            },
        )

        self.assertEqual(expected, extracted)


class TestCEnum(TestExtractBase):
    def test_extract_enum(self) -> None:
        type_info: TypeInfo = self.get_type("EnumWithFields")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CEnum = CEnum(
            name="EnumWithFields",
            namespace="TestLib",
            nested=None,
            fields=("Field0", "Field1", "Field2", "Field3"),
        )

        self.assertEqual(expected, extracted)

    def test_extract_enum_no_fields(self) -> None:
        type_info: TypeInfo = self.get_type("EnumWithNoFields")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CEnum = CEnum(
            name="EnumWithNoFields",
            namespace="TestLib",
            nested=None,
            fields=(),
        )

        self.assertEqual(expected, extracted)


class TestCDelegate(TestExtractBase):
    def test_extract_delegate_no_params_no_return(self) -> None:
        type_info: TypeInfo = self.get_type("DelegateWithNoParametersNoReturn")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CDelegate = CDelegate(
            name="DelegateWithNoParametersNoReturn",
            namespace="TestLib",
            nested=None,
            parameters=(),
            return_type=CType(name="Void", namespace="System"),
        )

        self.assertEqual(expected, extracted)

    def test_extract_delegate_no_params_return(self) -> None:
        type_info: TypeInfo = self.get_type("DelegateWithNoParametersReturn")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CDelegate = CDelegate(
            name="DelegateWithNoParametersReturn",
            namespace="TestLib",
            nested=None,
            parameters=(),
            return_type=CType(name="Int32", namespace="System"),
        )

        self.assertEqual(expected, extracted)

    def test_extract_delegate_params_no_return(self) -> None:
        type_info: TypeInfo = self.get_type("DelegateWithParametersNoReturn")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CDelegate = CDelegate(
            name="DelegateWithParametersNoReturn",
            namespace="TestLib",
            nested=None,
            parameters=(
                CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                CParameter(name="param1", type=CType(name="Int32", namespace="System")),
            ),
            return_type=CType(name="Void", namespace="System"),
        )

        self.assertEqual(expected, extracted)

    def test_extract_delegate_params_return(self) -> None:
        type_info: TypeInfo = self.get_type("DelegateWithParametersReturn")

        extracted: CTypeDefinition = extract_type_def(type_info)
        expected: CDelegate = CDelegate(
            name="DelegateWithParametersReturn",
            namespace="TestLib",
            nested=None,
            parameters=(
                CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                CParameter(name="param1", type=CType(name="Int32", namespace="System")),
            ),
            return_type=CType(name="Int32", namespace="System"),
        )

        self.assertEqual(expected, extracted)


class TestCType(TestExtractBase):
    def test_extract_type_simple(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithSuper")

        extracted: CType = extract_type(type_info)
        expected: CType = CType(name="ClassWithSuper", namespace="TestLib")

        self.assertEqual(expected, extracted)

    def test_extract_type_inner(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithGeneric")

        extracted: CType = extract_type(type_info)
        expected: CType = CType(
            name="ClassWithGeneric",
            namespace="TestLib",
            inner=(CType(name="T", generic=True),),
        )

        self.assertEqual(expected, extracted)

    def test_extract_type_inner_multi(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithMultiGeneric")

        extracted: CType = extract_type(type_info)
        expected: CType = CType(
            name="ClassWithMultiGeneric",
            namespace="TestLib",
            inner=(
                CType(name="U", generic=True),
                CType(name="V", generic=True),
            ),
        )

        self.assertEqual(expected, extracted)

    def test_extract_type_reference(self) -> None:
        type_info: TypeInfo = self.get_type("ClassThatsAbstract").MakeByRefType()

        extracted: CType = extract_type(type_info)
        expected: CType = CType(name="ClassThatsAbstract", namespace="TestLib", reference=True)

        self.assertEqual(expected, extracted)

    def test_extract_type_generic(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithGeneric")

        extracted: CType = extract_type(type_info.GenericTypeParameters[0])
        expected: CType = CType(name="T", generic=True)

        self.assertEqual(expected, extracted)

    def test_extract_type_nullable(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithMethods")
        method_info: MethodInfo = type_info.GetMethod("InstanceMethodWithNullableParam")
        parameter_info: ParameterInfo = method_info.GetParameters()[0]

        extracted: CType = extract_type(parameter_info.ParameterType)
        expected: CType = CType(name="Int32", namespace="System", nullable=True)

        self.assertEqual(expected, extracted)

    def test_extract_type_reference_nullable(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithMethods")
        method_info: MethodInfo = type_info.GetMethod("InstanceMethodWithNullableOutParam")
        parameter_info: ParameterInfo = method_info.GetParameters()[0]

        extracted: CType = extract_type(parameter_info.ParameterType)
        expected: CType = CType(name="Int32", namespace="System", reference=True, nullable=True)

        self.assertEqual(expected, extracted)


class TestCParameter(TestExtractBase):
    def test_extract_parameter_simple(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithMethods")
        method_info: MethodInfo = type_info.GetMethod("InstanceMethodWithParams1")

        extracted: CParameter = extract_parameter(method_info.GetParameters()[0])
        expected: CParameter = CParameter(
            name="param0",
            type=CType(name="Int32", namespace="System"),
        )

        self.assertEqual(expected, extracted)

    def test_extract_parameter_default(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithMethods")
        method_info: MethodInfo = type_info.GetMethod("InstanceMethodWithDefaultParam")

        extracted: CParameter = extract_parameter(method_info.GetParameters()[0])
        expected: CParameter = CParameter(
            name="param0",
            type=CType(name="Int32", namespace="System"),
            default=True,
        )

        self.assertEqual(expected, extracted)

    def test_extract_parameter_out(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithMethods")
        method_info: MethodInfo = type_info.GetMethod("InstanceMethodWithOutParam")

        extracted: CParameter = extract_parameter(method_info.GetParameters()[0])
        expected: CParameter = CParameter(
            name="param0",
            type=CType(name="Int32", namespace="System", reference=True),
            out=True,
        )

        self.assertEqual(expected, extracted)


class TestCField(TestExtractBase):
    def test_extract_field(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithFields")
        field_info: FieldInfo = type_info.GetField("InstanceFieldA")

        extracted: CField = extract_field(field_info)
        expected: CField = CField(
            name="InstanceFieldA",
            declaring_type=CType(name="ClassWithFields", namespace="TestLib"),
            return_type=CType(name="Int32", namespace="System"),
        )

        self.assertEqual(expected, extracted)

    def test_extract_field_static(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithFields")
        field_info: FieldInfo = type_info.GetField("StaticFieldA")

        extracted: CField = extract_field(field_info)
        expected: CField = CField(
            name="StaticFieldA",
            declaring_type=CType(name="ClassWithFields", namespace="TestLib"),
            return_type=CType(name="Int32", namespace="System"),
            static=True,
        )

        self.assertEqual(expected, extracted)

    def test_extract_fields(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithFields")
        extracted: Mapping[str, CField] = extract_fields(type_info)
        expected: Mapping[str, CField] = {
            "TestLib:ClassWithFields.InstanceFieldA": CField(
                name="InstanceFieldA",
                declaring_type=CType(name="ClassWithFields", namespace="TestLib"),
                return_type=CType(name="Int32", namespace="System"),
            ),
            "TestLib:ClassWithFields.InstanceFieldB": CField(
                name="InstanceFieldB",
                declaring_type=CType(name="ClassWithFields", namespace="TestLib"),
                return_type=CType(name="Int32", namespace="System"),
            ),
            "TestLib:ClassWithFields.InstanceFieldC": CField(
                name="InstanceFieldC",
                declaring_type=CType(name="ClassWithFields", namespace="TestLib"),
                return_type=CType(name="Int32", namespace="System"),
            ),
            "TestLib:ClassWithFields.StaticFieldA": CField(
                name="StaticFieldA",
                declaring_type=CType(name="ClassWithFields", namespace="TestLib"),
                return_type=CType(name="Int32", namespace="System"),
                static=True,
            ),
            "TestLib:ClassWithFields.StaticFieldB": CField(
                name="StaticFieldB",
                declaring_type=CType(name="ClassWithFields", namespace="TestLib"),
                return_type=CType(name="Int32", namespace="System"),
                static=True,
            ),
            "TestLib:ClassWithFields.StaticFieldC": CField(
                name="StaticFieldC",
                declaring_type=CType(name="ClassWithFields", namespace="TestLib"),
                return_type=CType(name="Int32", namespace="System"),
                static=True,
            ),
        }

        self.assertDictEqual(expected, extracted)


class TestCConstructor(TestExtractBase):
    def test_extract_constructor(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithConstructors")
        extracted: Sequence[CConstructor] = list(
            map(extract_constructor, type_info.GetConstructors())
        )

        expected: CConstructor = CConstructor(
            declaring_type=CType(name="ClassWithConstructors", namespace="TestLib"),
            parameters=(),
        )

        self.assertEqual(expected, extracted[0])

        expected: CConstructor = CConstructor(
            declaring_type=CType(name="ClassWithConstructors", namespace="TestLib"),
            parameters=(CParameter(name="param0", type=CType(name="Int32", namespace="System")),),
        )

        self.assertEqual(expected, extracted[1])

        expected: CConstructor = CConstructor(
            declaring_type=CType(name="ClassWithConstructors", namespace="TestLib"),
            parameters=(
                CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                CParameter(name="param1", type=CType(name="Int32", namespace="System")),
            ),
        )

        self.assertEqual(expected, extracted[2])

        expected: CConstructor = CConstructor(
            declaring_type=CType(name="ClassWithConstructors", namespace="TestLib"),
            parameters=(
                CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                CParameter(name="param1", type=CType(name="Int32", namespace="System")),
                CParameter(name="param2", type=CType(name="Int32", namespace="System")),
            ),
        )

        self.assertEqual(expected, extracted[3])

    def test_extract_constructors(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithConstructors")
        extracted: Mapping[str, CConstructor] = extract_constructors(type_info)
        expected: Mapping[str, CConstructor] = {
            "TestLib:ClassWithConstructors.__init__()": CConstructor(
                declaring_type=CType(name="ClassWithConstructors", namespace="TestLib"),
                parameters=(),
            ),
            "TestLib:ClassWithConstructors.__init__(System:Int32)": CConstructor(
                declaring_type=CType(name="ClassWithConstructors", namespace="TestLib"),
                parameters=(
                    CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                ),
            ),
            "TestLib:ClassWithConstructors.__init__(System:Int32, System:Int32)": CConstructor(
                declaring_type=CType(name="ClassWithConstructors", namespace="TestLib"),
                parameters=(
                    CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                    CParameter(name="param1", type=CType(name="Int32", namespace="System")),
                ),
            ),
            "TestLib:ClassWithConstructors.__init__(System:Int32, System:Int32, System:Int32)": CConstructor(
                declaring_type=CType(name="ClassWithConstructors", namespace="TestLib"),
                parameters=(
                    CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                    CParameter(name="param1", type=CType(name="Int32", namespace="System")),
                    CParameter(name="param2", type=CType(name="Int32", namespace="System")),
                ),
            ),
        }

        self.assertDictEqual(expected, extracted)


class TestCProperty(TestExtractBase):
    def test_extract_property(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithProperties")
        property_info: PropertyInfo = type_info.GetProperty("InstanceReadOnlyProperty0")

        extracted: CProperty = extract_property(property_info)
        expected: CProperty = CProperty(
            name="InstanceReadOnlyProperty0",
            declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
            type=CType(name="Int32", namespace="System"),
        )

        self.assertEqual(expected, extracted)

    def test_extract_property_setter(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithProperties")
        property_info: PropertyInfo = type_info.GetProperty("InstanceProperty0")

        extracted: CProperty = extract_property(property_info)
        expected: CProperty = CProperty(
            name="InstanceProperty0",
            declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
            type=CType(name="Int32", namespace="System"),
            setter=True,
        )

        self.assertEqual(expected, extracted)

    def test_extract_property_static(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithProperties")
        property_info: PropertyInfo = type_info.GetProperty("StaticReadOnlyProperty0")

        extracted: CProperty = extract_property(property_info)
        expected: CProperty = CProperty(
            name="StaticReadOnlyProperty0",
            declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
            type=CType(name="Int32", namespace="System"),
            static=True,
        )

        self.assertEqual(expected, extracted)

    def test_extract_property_setter_static(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithProperties")
        property_info: PropertyInfo = type_info.GetProperty("StaticProperty0")

        extracted: CProperty = extract_property(property_info)
        expected: CProperty = CProperty(
            name="StaticProperty0",
            declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
            type=CType(name="Int32", namespace="System"),
            setter=True,
            static=True,
        )

        self.assertEqual(expected, extracted)

    def test_extract_properties(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithProperties")
        extracted: Mapping[str, CProperty] = extract_properties(type_info)
        expected: Mapping[str, CProperty] = {
            "TestLib:ClassWithProperties.InstanceProperty0": CProperty(
                name="InstanceProperty0",
                declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                type=CType(name="Int32", namespace="System"),
                setter=True,
            ),
            "TestLib:ClassWithProperties.InstanceProperty1": CProperty(
                name="InstanceProperty1",
                declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                type=CType(name="Int32", namespace="System"),
                setter=True,
            ),
            "TestLib:ClassWithProperties.InstanceProperty2": CProperty(
                name="InstanceProperty2",
                declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                type=CType(name="Int32", namespace="System"),
                setter=True,
            ),
            "TestLib:ClassWithProperties.InstanceReadOnlyProperty0": CProperty(
                name="InstanceReadOnlyProperty0",
                declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                type=CType(name="Int32", namespace="System"),
            ),
            "TestLib:ClassWithProperties.InstanceReadOnlyProperty1": CProperty(
                name="InstanceReadOnlyProperty1",
                declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                type=CType(name="Int32", namespace="System"),
            ),
            "TestLib:ClassWithProperties.InstanceReadOnlyProperty2": CProperty(
                name="InstanceReadOnlyProperty2",
                declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                type=CType(name="Int32", namespace="System"),
            ),
            "TestLib:ClassWithProperties.StaticProperty0": CProperty(
                name="StaticProperty0",
                declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                type=CType(name="Int32", namespace="System"),
                setter=True,
                static=True,
            ),
            "TestLib:ClassWithProperties.StaticProperty1": CProperty(
                name="StaticProperty1",
                declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                type=CType(name="Int32", namespace="System"),
                setter=True,
                static=True,
            ),
            "TestLib:ClassWithProperties.StaticProperty2": CProperty(
                name="StaticProperty2",
                declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                type=CType(name="Int32", namespace="System"),
                setter=True,
                static=True,
            ),
            "TestLib:ClassWithProperties.StaticReadOnlyProperty0": CProperty(
                name="StaticReadOnlyProperty0",
                declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                type=CType(name="Int32", namespace="System"),
                static=True,
            ),
            "TestLib:ClassWithProperties.StaticReadOnlyProperty1": CProperty(
                name="StaticReadOnlyProperty1",
                declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                type=CType(name="Int32", namespace="System"),
                static=True,
            ),
            "TestLib:ClassWithProperties.StaticReadOnlyProperty2": CProperty(
                name="StaticReadOnlyProperty2",
                declaring_type=CType(name="ClassWithProperties", namespace="TestLib"),
                type=CType(name="Int32", namespace="System"),
                static=True,
            ),
        }

        self.assertDictEqual(expected, extracted)


class TestCMethod(TestExtractBase):
    def test_extract_method(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithMethods")
        method_info: MethodInfo = type_info.GetMethod("InstanceMethodWithParams1")

        extracted: CMethod = extract_method(method_info)
        expected: CMethod = CMethod(
            name="InstanceMethodWithParams1",
            declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
            parameters=(CParameter(name="param0", type=CType(name="Int32", namespace="System")),),
            return_types=(CType(name="Int32", namespace="System"),),
        )

        self.assertEqual(expected, extracted)

    def test_extract_method_static(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithMethods")
        method_info: MethodInfo = type_info.GetMethod("StaticMethodWithParams1")

        extracted: CMethod = extract_method(method_info)
        expected: CMethod = CMethod(
            name="StaticMethodWithParams1",
            declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
            parameters=(CParameter(name="param0", type=CType(name="Int32", namespace="System")),),
            return_types=(CType("Int32", "System"),),
            static=True,
        )

        self.assertEqual(expected, extracted)

    def test_extract_method_out(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithMethods")
        method_info: MethodInfo = type_info.GetMethod("InstanceMethodWithOutParam")

        extracted: CMethod = extract_method(method_info)
        expected: CMethod = CMethod(
            name="InstanceMethodWithOutParam",
            declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
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
        )

        self.assertEqual(expected, extracted)

    def test_extract_methods(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithMethods")
        extracted: Mapping[str, CMethod] = extract_methods(type_info)
        expected: Mapping[str, CMethod] = {
            "System:Object.Equals(System:Object)": CMethod(
                name="Equals",
                declaring_type=CType(name="Object", namespace="System"),
                parameters=(CParameter(name="obj", type=CType(name="Object", namespace="System")),),
                return_types=(CType(name="Boolean", namespace="System"),),
            ),
            "System:Object.GetHashCode()": CMethod(
                name="GetHashCode",
                declaring_type=CType(name="Object", namespace="System"),
                parameters=(),
                return_types=(CType(name="Int32", namespace="System"),),
            ),
            "System:Object.GetType()": CMethod(
                name="GetType",
                declaring_type=CType(name="Object", namespace="System"),
                parameters=(),
                return_types=(CType(name="Type", namespace="System"),),
            ),
            "TestLib:ClassWithMethods.InstanceMethodWithDefaultParam(System:Int32)": CMethod(
                name="InstanceMethodWithDefaultParam",
                declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                parameters=(
                    CParameter(
                        name="param0", type=CType(name="Int32", namespace="System"), default=True
                    ),
                ),
                return_types=(CType(name="Int32", namespace="System"),),
            ),
            "TestLib:ClassWithMethods.InstanceMethodWithNullableDefaultParam(System:Int32?)": CMethod(
                name="InstanceMethodWithNullableDefaultParam",
                declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                parameters=(
                    CParameter(
                        name="param0",
                        type=CType(name="Int32", namespace="System", nullable=True),
                        default=True,
                    ),
                ),
                return_types=(CType(name="Int32", namespace="System"),),
            ),
            "TestLib:ClassWithMethods.InstanceMethodWithNullableOutParam(System:*Int32?)": CMethod(
                name="InstanceMethodWithNullableOutParam",
                declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                parameters=(
                    CParameter(
                        name="param0",
                        type=CType(name="Int32", namespace="System", reference=True, nullable=True),
                        out=True,
                    ),
                ),
                return_types=(
                    CType(name="Int32", namespace="System"),
                    CType(name="Int32", namespace="System", reference=True, nullable=True),
                ),
            ),
            "TestLib:ClassWithMethods.InstanceMethodWithNullableParam(System:Int32?)": CMethod(
                name="InstanceMethodWithNullableParam",
                declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                parameters=(
                    CParameter(
                        name="param0", type=CType(name="Int32", namespace="System", nullable=True)
                    ),
                ),
                return_types=(CType(name="Int32", namespace="System"),),
            ),
            "TestLib:ClassWithMethods.InstanceMethodWithOutParam(System:*Int32)": CMethod(
                name="InstanceMethodWithOutParam",
                declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
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
            "TestLib:ClassWithMethods.InstanceMethodWithParams0()": CMethod(
                name="InstanceMethodWithParams0",
                declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                parameters=(),
                return_types=(CType(name="Int32", namespace="System"),),
            ),
            "TestLib:ClassWithMethods.InstanceMethodWithParams1(System:Int32)": CMethod(
                name="InstanceMethodWithParams1",
                declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                parameters=(
                    CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                ),
                return_types=(CType(name="Int32", namespace="System"),),
            ),
            "TestLib:ClassWithMethods.InstanceMethodWithParams2(System:Int32, System:Int32)": CMethod(
                name="InstanceMethodWithParams2",
                declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                parameters=(
                    CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                    CParameter(name="param1", type=CType(name="Int32", namespace="System")),
                ),
                return_types=(CType(name="Int32", namespace="System"),),
            ),
            "TestLib:ClassWithMethods.StaticMethodWithDefaultParam(System:Int32)": CMethod(
                name="StaticMethodWithDefaultParam",
                declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                parameters=(
                    CParameter(
                        name="param0", type=CType(name="Int32", namespace="System"), default=True
                    ),
                ),
                return_types=(CType(name="Int32", namespace="System"),),
                static=True,
            ),
            "TestLib:ClassWithMethods.StaticMethodWithNullableDefaultParam(System:Int32?)": CMethod(
                name="StaticMethodWithNullableDefaultParam",
                declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                parameters=(
                    CParameter(
                        name="param0",
                        type=CType(name="Int32", namespace="System", nullable=True),
                        default=True,
                    ),
                ),
                return_types=(CType(name="Int32", namespace="System"),),
                static=True,
            ),
            "TestLib:ClassWithMethods.StaticMethodWithNullableOutParam(System:*Int32?)": CMethod(
                name="StaticMethodWithNullableOutParam",
                declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                parameters=(
                    CParameter(
                        name="param0",
                        type=CType(name="Int32", namespace="System", reference=True, nullable=True),
                        out=True,
                    ),
                ),
                return_types=(
                    CType(name="Int32", namespace="System"),
                    CType(name="Int32", namespace="System", reference=True, nullable=True),
                ),
                static=True,
            ),
            "TestLib:ClassWithMethods.StaticMethodWithNullableParam(System:Int32?)": CMethod(
                name="StaticMethodWithNullableParam",
                declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                parameters=(
                    CParameter(
                        name="param0", type=CType(name="Int32", namespace="System", nullable=True)
                    ),
                ),
                return_types=(CType(name="Int32", namespace="System"),),
                static=True,
            ),
            "TestLib:ClassWithMethods.StaticMethodWithOutParam(System:*Int32)": CMethod(
                name="StaticMethodWithOutParam",
                declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
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
                static=True,
            ),
            "TestLib:ClassWithMethods.StaticMethodWithParams0()": CMethod(
                name="StaticMethodWithParams0",
                declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                parameters=(),
                return_types=(CType(name="Int32", namespace="System"),),
                static=True,
            ),
            "TestLib:ClassWithMethods.StaticMethodWithParams1(System:Int32)": CMethod(
                name="StaticMethodWithParams1",
                declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                parameters=(
                    CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                ),
                return_types=(CType(name="Int32", namespace="System"),),
                static=True,
            ),
            "TestLib:ClassWithMethods.StaticMethodWithParams2(System:Int32, System:Int32)": CMethod(
                name="StaticMethodWithParams2",
                declaring_type=CType(name="ClassWithMethods", namespace="TestLib"),
                parameters=(
                    CParameter(name="param0", type=CType(name="Int32", namespace="System")),
                    CParameter(name="param1", type=CType(name="Int32", namespace="System")),
                ),
                return_types=(CType(name="Int32", namespace="System"),),
                static=True,
            ),
            "System:Object.ToString()": CMethod(
                name="ToString",
                declaring_type=CType(name="Object", namespace="System"),
                parameters=(),
                return_types=(CType(name="String", namespace="System"),),
            ),
        }

        self.assertDictEqual(expected, extracted)


class TestCEvent(TestExtractBase):
    def test_extract_event(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithEvents")
        event_info: EventInfo = type_info.GetEvent("Event")

        extracted: CEvent = extract_event(event_info)
        expected: CEvent = CEvent(
            name="Event",
            declaring_type=CType(name="ClassWithEvents", namespace="TestLib"),
            type=CType(name="EventHandler", namespace="System"),
        )

        self.assertEqual(expected, extracted)

    def test_extract_event_args(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithEvents")
        event_info: EventInfo = type_info.GetEvent("EventWithArgs")

        extracted: CEvent = extract_event(event_info)
        expected: CEvent = CEvent(
            name="EventWithArgs",
            declaring_type=CType(name="ClassWithEvents", namespace="TestLib"),
            type=CType(
                name="EventHandler",
                namespace="System",
                inner=(CType(name="EventArgs", namespace="System"),),
            ),
        )

        self.assertEqual(expected, extracted)

    def test_extract_events(self) -> None:
        type_info: TypeInfo = self.get_type("ClassWithEvents")
        extracted: Mapping[str, CEvent] = extract_events(type_info)
        expected: Mapping[str, CEvent] = {
            "TestLib:ClassWithEvents.Event": CEvent(
                name="Event",
                declaring_type=CType(name="ClassWithEvents", namespace="TestLib"),
                type=CType(name="EventHandler", namespace="System"),
            ),
            "TestLib:ClassWithEvents.EventWithArgs": CEvent(
                name="EventWithArgs",
                declaring_type=CType(name="ClassWithEvents", namespace="TestLib"),
                type=CType(
                    name="EventHandler",
                    namespace="System",
                    inner=(CType(name="EventArgs", namespace="System"),),
                ),
            ),
        }

        self.assertDictEqual(expected, extracted)


class TestExtractAssembly(TestBase):
    output_dir: Path

    @classmethod
    def setUpClass(cls) -> None:
        cls.output_dir = Path("output")
        cls.output_dir.mkdir(parents=True, exist_ok=True)

    def test_extract_test_lib(self) -> None:
        skeleton_name: str = "TestLib_1.0.0.0_skeleton.json"
        doc_name: str = "TestLib_1.0.0.0_doc.json"

        result = extract_assembly(
            assembly_name="TestLib",
            output_dir=self.output_dir,
            overwrite=True,
        )

        skeleton_path: Path = self.output_dir / skeleton_name
        doc_path: Path = self.output_dir / doc_name

        self.assertEqual(0, result)

        self.assertTrue(skeleton_path.exists())
        self.assertTrue(doc_path.exists())

        skeleton_dict: Mapping[str, Any]
        with skeleton_path.open("r") as skeleton_file:
            skeleton_dict = json.load(skeleton_file)

        self.assertEqual("TestLib", skeleton_dict.get("name", None))
        self.assertEqual("1.0.0.0", skeleton_dict.get("version", None))

        namespaces: Mapping[str, Any] = skeleton_dict.get("namespaces", None)
        self.assertIsNotNone(namespaces)

        test_lib: Mapping[str, Any] = namespaces.get("TestLib", None)
        self.assertIsNotNone(test_lib)

        self.assertEqual("TestLib", test_lib.get("name", None))

        type_map: Mapping[str, Any] = test_lib.get("types", None)
        self.assertIsNotNone(type_map)

        types: Sequence[str] = (
            "TestLib.ClassThatsAbstract",
            "TestLib.ClassWithConstructors",
            "TestLib.ClassWithEvents",
            "TestLib.ClassWithFields",
            "TestLib.ClassWithGeneric[$T]",
            "TestLib.ClassWithInterface",
            "TestLib.ClassWithListMethods",
            "TestLib.ClassWithMethods",
            "TestLib.ClassWithMultiGeneric[$U, $V]",
            "TestLib.ClassWithNested",
            "TestLib.ClassWithOperatorMethods",
            "TestLib.ClassWithProperties",
            "TestLib.ClassWithSuper",
            "TestLib.ClassWithTypes",
            "TestLib.DelegateWithNoParametersNoReturn()",
            "TestLib.DelegateWithNoParametersReturn()",
            "TestLib.DelegateWithParametersNoReturn(System:Int32, System:Int32)",
            "TestLib.DelegateWithParametersReturn(System:Int32, System:Int32)",
            "TestLib.EnumWithFields",
            "TestLib.EnumWithNoFields",
            "TestLib.IInterfaceWithEvents",
            "TestLib.IInterfaceWithFields",
            "TestLib.IInterfaceWithGeneric[$T]",
            "TestLib.IInterfaceWithInterface",
            "TestLib.IInterfaceWithListMethods",
            "TestLib.IInterfaceWithMethods",
            "TestLib.IInterfaceWithMultiGeneric[$U, $V]",
            "TestLib.IInterfaceWithNested",
            "TestLib.IInterfaceWithOperatorMethods",
            "TestLib.IInterfaceWithProperties",
            "TestLib.OverriddenProperty",
            "TestLib.StructWithConstructors",
            "TestLib.StructWithEvents",
            "TestLib.StructWithFields",
            "TestLib.StructWithGeneric[$T]",
            "TestLib.StructWithInterface",
            "TestLib.StructWithListMethods",
            "TestLib.StructWithMethods",
            "TestLib.StructWithMultiGeneric[$U, $V]",
            "TestLib.StructWithNested",
            "TestLib.StructWithOperatorMethods",
            "TestLib.StructWithProperties",
        )
        for type_str in types:
            with self.subTest(type_str=type_str):
                type_def: Mapping[str, Any] = type_map.get(type_str, None)
                self.assertIsNotNone(type_def)


if __name__ == "__main__":
    unittest.main()
