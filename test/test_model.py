import random
import unittest
from typing import Mapping
from typing import MutableSequence
from typing import Sequence
from typing import cast

import clr
from System import ArgumentException
from System import Array
from System import AsyncCallback
from System import Comparison
from System import Convert
from System import DateTime
from System import DateTimeKind
from System import DayOfWeek
from System import Double
from System import EventHandler
from System import IConvertible
from System import IDisposable
from System import IEquatable
from System import IFormatProvider
from System import IFormattable
from System import Int32
from System import Math
from System import Nullable
from System import Object
from System import PlatformID
from System import Predicate
from System import Random
from System import Single
from System import String
from System import TimeSpan
from System import TimeZone
from System import Type
from System import TypeCode
from System import UInt32
from System import UnhandledExceptionEventHandler
from System import UriBuilder
from System import UriParser
from System.Collections.Generic import Dictionary
from System.Collections.Generic import IEnumerable
from System.ComponentModel import IComponent
from System.Net import DownloadDataCompletedEventHandler
from System.Net import WebClient
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


class TestCClass(unittest.TestCase):
    def assertCClass(
        self,
        struct: CClass,
        name: str,
        namespace: str,
        abstract: bool,
        generic_args: Sequence[CType],
        super_class: CType,
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
        self.assertEqual(struct.name, name)
        self.assertEqual(struct.namespace, namespace)
        self.assertEqual(struct.abstract, abstract)
        self.assertSequenceEqual(struct.generic_args, generic_args)
        self.assertEqual(struct.super_class, super_class)
        self.assertSequenceEqual(struct.interfaces, interfaces)
        self.assertDictEqual(struct.fields, fields)
        self.assertDictEqual(struct.constructors, constructors)
        self.assertDictEqual(struct.properties, properties)
        self.assertDictEqual(struct.methods, methods)
        self.assertDictEqual(struct.dunder_methods, dunder_methods)
        self.assertDictEqual(struct.events, events)
        self.assertDictEqual(struct.nested, nested)

    def test_from_info(self) -> None:
        type_info: TypeInfo = clr.GetClrType(Random)
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)
        self.maxDiff = None

        self.assertCClass(
            struct=cast(CClass, type_def),
            name="Random",
            namespace="System",
            abstract=False,
            generic_args=(),
            super_class=CType("Object", "System"),
            interfaces=(),
            fields={},
            constructors={
                "System.Random.__init__()": CConstructor(CType("Random", "System"), ()),
                "System.Random.__init__(System.Int32)": CConstructor(
                    CType("Random", "System"),
                    (CParameter("Seed", CType("Int32", "System"), False, False),),
                ),
            },
            properties={},
            methods={
                "System.Object.Equals(System.Object)": CMethod(
                    "Equals",
                    CType("Object", "System"),
                    (CParameter("obj", CType("Object", "System"), False, False),),
                    (CType("Boolean", "System"),),
                    False,
                ),
                "System.Object.GetHashCode()": CMethod(
                    "GetHashCode",
                    CType("Object", "System"),
                    (),
                    (CType("Int32", "System"),),
                    False,
                ),
                "System.Object.GetType()": CMethod(
                    "GetType",
                    CType("Object", "System"),
                    (),
                    (CType("Type", "System"),),
                    False,
                ),
                "System.Random.Next()": CMethod(
                    "Next",
                    CType("Random", "System"),
                    (),
                    (CType("Int32", "System"),),
                    False,
                ),
                "System.Random.Next(System.Int32)": CMethod(
                    "Next",
                    CType("Random", "System"),
                    (CParameter("maxValue", CType("Int32", "System"), False, False),),
                    (CType("Int32", "System"),),
                    False,
                ),
                "System.Random.Next(System.Int32, System.Int32)": CMethod(
                    "Next",
                    CType("Random", "System"),
                    (
                        CParameter("minValue", CType("Int32", "System"), False, False),
                        CParameter("maxValue", CType("Int32", "System"), False, False),
                    ),
                    (CType("Int32", "System"),),
                    False,
                ),
                "System.Random.NextBytes(System.Byte)": CMethod(
                    "NextBytes",
                    CType("Random", "System"),
                    (CParameter("buffer", CType("Byte", "System"), False, False),),
                    (CType("Void", "System"),),
                    False,
                ),
                "System.Random.NextDouble()": CMethod(
                    "NextDouble",
                    CType("Random", "System"),
                    (),
                    (CType("Double", "System"),),
                    False,
                ),
                "System.Object.ToString()": CMethod(
                    "ToString",
                    CType("Object", "System"),
                    (),
                    (CType("String", "System"),),
                    False,
                ),
            },
            dunder_methods={},
            events={},
            nested={},
        )

    def test_json(self) -> None:
        type_info: TypeInfo = clr.GetClrType(Nullable)
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            json,
            {
                "type": "class",
                "name": "Nullable",
                "namespace": "System",
                "abstract": True,
                "generic_args": (),
                "super_class": "System.Object",
                "interfaces": (),
                "fields": {},
                "constructors": {},
                "properties": {},
                "methods": {
                    "System.Nullable.Compare(System.Nullable[System.$T], System.Nullable[System.$T])": {
                        "name": "Compare",
                        "declaring_type": "System.Nullable",
                        "parameters": (
                            {
                                "name": "n1",
                                "type": "System.Nullable[System.$T]",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "n2",
                                "type": "System.Nullable[System.$T]",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Int32",),
                        "static": True,
                    },
                    "System.Object.Equals(System.Object)": {
                        "name": "Equals",
                        "declaring_type": "System.Object",
                        "parameters": (
                            {
                                "name": "obj",
                                "type": "System.Object",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Boolean",),
                        "static": False,
                    },
                    "System.Nullable.Equals(System.Nullable[System.$T], System.Nullable[System.$T])": {
                        "name": "Equals",
                        "declaring_type": "System.Nullable",
                        "parameters": (
                            {
                                "name": "n1",
                                "type": "System.Nullable[System.$T]",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "n2",
                                "type": "System.Nullable[System.$T]",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Boolean",),
                        "static": True,
                    },
                    "System.Object.GetHashCode()": {
                        "name": "GetHashCode",
                        "declaring_type": "System.Object",
                        "parameters": (),
                        "returns": ("System.Int32",),
                        "static": False,
                    },
                    "System.Object.GetType()": {
                        "name": "GetType",
                        "declaring_type": "System.Object",
                        "parameters": (),
                        "returns": ("System.Type",),
                        "static": False,
                    },
                    "System.Nullable.GetUnderlyingType(System.Type)": {
                        "name": "GetUnderlyingType",
                        "declaring_type": "System.Nullable",
                        "parameters": (
                            {
                                "name": "nullableType",
                                "type": "System.Type",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Type",),
                        "static": True,
                    },
                    "System.Object.ToString()": {
                        "name": "ToString",
                        "declaring_type": "System.Object",
                        "parameters": (),
                        "returns": ("System.String",),
                        "static": False,
                    },
                },
                "dunder_methods": {},
                "events": {},
                "nested": {},
            },
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(from_json, type_def)

    def test_compare(self) -> None:
        class0: CClass = CClass.from_info(clr.GetClrType(Array))
        class1: CClass = CClass.from_info(clr.GetClrType(Convert))
        class2: CClass = CClass.from_info(clr.GetClrType(Type))
        class3: CClass = CClass.from_info(clr.GetClrType(UriParser))

        self.assertLess(class0, class1)
        self.assertLess(class1, class2)
        self.assertLess(class2, class3)

        self.assertLessEqual(class0, class1)
        self.assertLessEqual(class1, class2)
        self.assertLessEqual(class2, class3)

        self.assertLessEqual(class0, class0)
        self.assertLessEqual(class1, class1)
        self.assertLessEqual(class2, class2)
        self.assertLessEqual(class3, class3)

        self.assertGreater(class1, class0)
        self.assertGreater(class2, class1)
        self.assertGreater(class3, class2)

        self.assertGreaterEqual(class1, class0)
        self.assertGreaterEqual(class2, class1)
        self.assertGreaterEqual(class3, class2)

        self.assertGreaterEqual(class0, class0)
        self.assertGreaterEqual(class1, class1)
        self.assertGreaterEqual(class2, class2)
        self.assertGreaterEqual(class3, class3)

    def test_sorted(self) -> None:
        class0: CClass = CClass.from_info(clr.GetClrType(Array))
        class1: CClass = CClass.from_info(clr.GetClrType(Convert))
        class2: CClass = CClass.from_info(clr.GetClrType(Type))
        class3: CClass = CClass.from_info(clr.GetClrType(UriParser))

        ordered: Sequence[CClass] = (class0, class1, class2, class3)
        unordered: MutableSequence[CClass] = list(ordered)
        random.shuffle(unordered)

        self.assertSequenceEqual(sorted(unordered), ordered)


class TestCStruct(unittest.TestCase):
    def assertCStruct(
        self,
        struct: CStruct,
        name: str,
        namespace: str,
        abstract: bool,
        generic_args: Sequence[CType],
        super_class: CType,
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
        self.assertEqual(struct.name, name)
        self.assertEqual(struct.namespace, namespace)
        self.assertEqual(struct.abstract, abstract)
        self.assertSequenceEqual(struct.generic_args, generic_args)
        self.assertEqual(struct.super_class, super_class)
        self.assertSequenceEqual(struct.interfaces, interfaces)
        self.assertDictEqual(struct.fields, fields)
        self.assertDictEqual(struct.constructors, constructors)
        self.assertDictEqual(struct.properties, properties)
        self.assertDictEqual(struct.methods, methods)
        self.assertDictEqual(struct.dunder_methods, dunder_methods)
        self.assertDictEqual(struct.events, events)
        self.assertDictEqual(struct.nested, nested)

    def test_from_info(self) -> None:
        type_info: TypeInfo = clr.GetClrType(Int32)
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCStruct(
            struct=cast(CStruct, type_def),
            name="Int32",
            namespace="System",
            abstract=False,
            generic_args=(),
            super_class=CType("ValueType", "System"),
            interfaces=(
                CType("IComparable", "System"),
                CType("IComparable", "System", (CType("Int32", "System"),)),
                CType("IConvertible", "System"),
                CType("IEquatable", "System", (CType("Int32", "System"),)),
                CType("IFormattable", "System"),
            ),
            fields={
                "System.Int32.MaxValue": CField(
                    "MaxValue",
                    CType("Int32", "System"),
                    CType("Int32", "System"),
                    True,
                ),
                "System.Int32.MinValue": CField(
                    "MinValue",
                    CType("Int32", "System"),
                    CType("Int32", "System"),
                    True,
                ),
            },
            constructors={},
            properties={},
            methods={
                "System.IComparable[System.Int32].CompareTo(System.Int32)": CMethod(
                    "CompareTo",
                    CType("IComparable", "System", (CType("Int32", "System"),)),
                    (CParameter("other", CType("Int32", "System"), False, False),),
                    (CType("Int32", "System"),),
                    False,
                ),
                "System.IComparable.CompareTo(System.Object)": CMethod(
                    "CompareTo",
                    CType("IComparable", "System"),
                    (CParameter("obj", CType("Object", "System"), False, False),),
                    (CType("Int32", "System"),),
                    False,
                ),
                "System.IEquatable[System.Int32].Equals(System.Int32)": CMethod(
                    "Equals",
                    CType("IEquatable", "System", (CType("Int32", "System"),)),
                    (CParameter("other", CType("Int32", "System"), False, False),),
                    (CType("Boolean", "System"),),
                    False,
                ),
                "System.Object.Equals(System.Object)": CMethod(
                    "Equals",
                    CType("Object", "System"),
                    (CParameter("obj", CType("Object", "System"), False, False),),
                    (CType("Boolean", "System"),),
                    False,
                ),
                "System.Object.GetHashCode()": CMethod(
                    "GetHashCode",
                    CType("Object", "System"),
                    (),
                    (CType("Int32", "System"),),
                    False,
                ),
                "System.Object.GetType()": CMethod(
                    "GetType",
                    CType("Object", "System"),
                    (),
                    (CType("Type", "System"),),
                    False,
                ),
                "System.IConvertible.GetTypeCode()": CMethod(
                    "GetTypeCode",
                    CType("IConvertible", "System"),
                    (),
                    (CType("TypeCode", "System"),),
                    False,
                ),
                "System.Int32.Parse(System.String)": CMethod(
                    "Parse",
                    CType("Int32", "System"),
                    (CParameter("s", CType("String", "System"), False, False),),
                    (CType("Int32", "System"),),
                    True,
                ),
                "System.Int32.Parse(System.String, System.Globalization.NumberStyles)": CMethod(
                    "Parse",
                    CType("Int32", "System"),
                    (
                        CParameter("s", CType("String", "System"), False, False),
                        CParameter(
                            "style",
                            CType("NumberStyles", "System.Globalization"),
                            False,
                            False,
                        ),
                    ),
                    (CType("Int32", "System"),),
                    True,
                ),
                "System.Int32.Parse(System.String, System.IFormatProvider)": CMethod(
                    "Parse",
                    CType("Int32", "System"),
                    (
                        CParameter("s", CType("String", "System"), False, False),
                        CParameter(
                            "provider", CType("IFormatProvider", "System"), False, False
                        ),
                    ),
                    (CType("Int32", "System"),),
                    True,
                ),
                "System.Int32.Parse(System.String, System.Globalization.NumberStyles, System.IFormatProvider)": CMethod(
                    "Parse",
                    CType("Int32", "System"),
                    (
                        CParameter("s", CType("String", "System"), False, False),
                        CParameter(
                            "style",
                            CType("NumberStyles", "System.Globalization"),
                            False,
                            False,
                        ),
                        CParameter(
                            "provider", CType("IFormatProvider", "System"), False, False
                        ),
                    ),
                    (CType("Int32", "System"),),
                    True,
                ),
                "System.IConvertible.ToBoolean(System.IFormatProvider)": CMethod(
                    "ToBoolean",
                    CType("IConvertible", "System"),
                    (
                        CParameter(
                            "provider", CType("IFormatProvider", "System"), False, False
                        ),
                    ),
                    (CType("Boolean", "System"),),
                    False,
                ),
                "System.IConvertible.ToByte(System.IFormatProvider)": CMethod(
                    "ToByte",
                    CType("IConvertible", "System"),
                    (
                        CParameter(
                            "provider", CType("IFormatProvider", "System"), False, False
                        ),
                    ),
                    (CType("Byte", "System"),),
                    False,
                ),
                "System.IConvertible.ToChar(System.IFormatProvider)": CMethod(
                    "ToChar",
                    CType("IConvertible", "System"),
                    (
                        CParameter(
                            "provider", CType("IFormatProvider", "System"), False, False
                        ),
                    ),
                    (CType("Char", "System"),),
                    False,
                ),
                "System.IConvertible.ToDateTime(System.IFormatProvider)": CMethod(
                    "ToDateTime",
                    CType("IConvertible", "System"),
                    (
                        CParameter(
                            "provider", CType("IFormatProvider", "System"), False, False
                        ),
                    ),
                    (CType("DateTime", "System"),),
                    False,
                ),
                "System.IConvertible.ToDecimal(System.IFormatProvider)": CMethod(
                    "ToDecimal",
                    CType("IConvertible", "System"),
                    (
                        CParameter(
                            "provider", CType("IFormatProvider", "System"), False, False
                        ),
                    ),
                    (CType("Decimal", "System"),),
                    False,
                ),
                "System.IConvertible.ToDouble(System.IFormatProvider)": CMethod(
                    "ToDouble",
                    CType("IConvertible", "System"),
                    (
                        CParameter(
                            "provider", CType("IFormatProvider", "System"), False, False
                        ),
                    ),
                    (CType("Double", "System"),),
                    False,
                ),
                "System.IConvertible.ToInt16(System.IFormatProvider)": CMethod(
                    "ToInt16",
                    CType("IConvertible", "System"),
                    (
                        CParameter(
                            "provider", CType("IFormatProvider", "System"), False, False
                        ),
                    ),
                    (CType("Int16", "System"),),
                    False,
                ),
                "System.IConvertible.ToInt32(System.IFormatProvider)": CMethod(
                    "ToInt32",
                    CType("IConvertible", "System"),
                    (
                        CParameter(
                            "provider", CType("IFormatProvider", "System"), False, False
                        ),
                    ),
                    (CType("Int32", "System"),),
                    False,
                ),
                "System.IConvertible.ToInt64(System.IFormatProvider)": CMethod(
                    "ToInt64",
                    CType("IConvertible", "System"),
                    (
                        CParameter(
                            "provider", CType("IFormatProvider", "System"), False, False
                        ),
                    ),
                    (CType("Int64", "System"),),
                    False,
                ),
                "System.IConvertible.ToSByte(System.IFormatProvider)": CMethod(
                    "ToSByte",
                    CType("IConvertible", "System"),
                    (
                        CParameter(
                            "provider", CType("IFormatProvider", "System"), False, False
                        ),
                    ),
                    (CType("SByte", "System"),),
                    False,
                ),
                "System.IConvertible.ToSingle(System.IFormatProvider)": CMethod(
                    "ToSingle",
                    CType("IConvertible", "System"),
                    (
                        CParameter(
                            "provider", CType("IFormatProvider", "System"), False, False
                        ),
                    ),
                    (CType("Single", "System"),),
                    False,
                ),
                "System.Object.ToString()": CMethod(
                    "ToString",
                    CType("Object", "System"),
                    (),
                    (CType("String", "System"),),
                    False,
                ),
                "System.IConvertible.ToString(System.IFormatProvider)": CMethod(
                    "ToString",
                    CType("IConvertible", "System"),
                    (
                        CParameter(
                            "provider", CType("IFormatProvider", "System"), False, False
                        ),
                    ),
                    (CType("String", "System"),),
                    False,
                ),
                "System.Int32.ToString(System.String)": CMethod(
                    "ToString",
                    CType("Int32", "System"),
                    (
                        CParameter(
                            "format",
                            CType("String", "System"),
                            False,
                            False,
                        ),
                    ),
                    (CType("String", "System"),),
                    False,
                ),
                "System.IFormattable.ToString(System.String, System.IFormatProvider)": CMethod(
                    "ToString",
                    CType("IFormattable", "System"),
                    (
                        CParameter(
                            "format",
                            CType("String", "System"),
                            False,
                            False,
                        ),
                        CParameter(
                            "formatProvider",
                            CType("IFormatProvider", "System"),
                            False,
                            False,
                        ),
                    ),
                    (CType("String", "System"),),
                    False,
                ),
                "System.IConvertible.ToType(System.Type, System.IFormatProvider)": CMethod(
                    "ToType",
                    CType("IConvertible", "System"),
                    (
                        CParameter(
                            "conversionType", CType("Type", "System"), False, False
                        ),
                        CParameter(
                            "provider", CType("IFormatProvider", "System"), False, False
                        ),
                    ),
                    (CType("Object", "System"),),
                    False,
                ),
                "System.IConvertible.ToUInt16(System.IFormatProvider)": CMethod(
                    "ToUInt16",
                    CType("IConvertible", "System"),
                    (
                        CParameter(
                            "provider", CType("IFormatProvider", "System"), False, False
                        ),
                    ),
                    (CType("UInt16", "System"),),
                    False,
                ),
                "System.IConvertible.ToUInt32(System.IFormatProvider)": CMethod(
                    "ToUInt32",
                    CType("IConvertible", "System"),
                    (
                        CParameter(
                            "provider", CType("IFormatProvider", "System"), False, False
                        ),
                    ),
                    (CType("UInt32", "System"),),
                    False,
                ),
                "System.IConvertible.ToUInt64(System.IFormatProvider)": CMethod(
                    "ToUInt64",
                    CType("IConvertible", "System"),
                    (
                        CParameter(
                            "provider", CType("IFormatProvider", "System"), False, False
                        ),
                    ),
                    (CType("UInt64", "System"),),
                    False,
                ),
                "System.Int32.TryParse(System.String, System.Globalization.NumberStyles, System.IFormatProvider, System.Int32)": CMethod(
                    "TryParse",
                    CType("Int32", "System"),
                    (
                        CParameter("s", CType("String", "System"), False, False),
                        CParameter(
                            "style",
                            CType(
                                "NumberStyles",
                                "System.Globalization",
                                (),
                                False,
                            ),
                            False,
                            False,
                        ),
                        CParameter(
                            "provider", CType("IFormatProvider", "System"), False, False
                        ),
                        CParameter("result", CType("Int32", "System"), False, True),
                    ),
                    (
                        CType("Boolean", "System"),
                        CType("Int32", "System"),
                    ),
                    True,
                ),
                "System.Int32.TryParse(System.String, System.Int32)": CMethod(
                    "TryParse",
                    CType("Int32", "System"),
                    (
                        CParameter("s", CType("String", "System"), False, False),
                        CParameter("result", CType("Int32", "System"), False, True),
                    ),
                    (
                        CType("Boolean", "System"),
                        CType("Int32", "System"),
                    ),
                    True,
                ),
            },
            dunder_methods={},
            events={},
            nested={},
        )

    def test_json(self) -> None:
        type_info: TypeInfo = clr.GetClrType(DateTime)
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            json,
            {
                "type": "struct",
                "name": "DateTime",
                "namespace": "System",
                "abstract": False,
                "generic_args": (),
                "super_class": "System.ValueType",
                "interfaces": (
                    "System.IComparable",
                    "System.IComparable[System.DateTime]",
                    "System.IConvertible",
                    "System.IEquatable[System.DateTime]",
                    "System.IFormattable",
                    "System.Runtime.Serialization.ISerializable",
                ),
                "fields": {
                    "System.DateTime.MaxValue": {
                        "name": "MaxValue",
                        "declaring_type": "System.DateTime",
                        "returns": "System.DateTime",
                        "static": True,
                    },
                    "System.DateTime.MinValue": {
                        "name": "MinValue",
                        "declaring_type": "System.DateTime",
                        "returns": "System.DateTime",
                        "static": True,
                    },
                },
                "constructors": {
                    "System.DateTime.__init__(System.Int64)": {
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "ticks",
                                "type": "System.Int64",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                    },
                    "System.DateTime.__init__(System.Int64, System.DateTimeKind)": {
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "ticks",
                                "type": "System.Int64",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "kind",
                                "type": "System.DateTimeKind",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                    },
                    "System.DateTime.__init__(System.Int32, System.Int32, System.Int32)": {
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "year",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "month",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "day",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                    },
                    "System.DateTime.__init__(System.Int32, System.Int32, System.Int32, System.Globalization.Calendar)": {
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "year",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "month",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "day",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "calendar",
                                "type": "System.Globalization.Calendar",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                    },
                    "System.DateTime.__init__(System.Int32, System.Int32, System.Int32, System.Int32, System.Int32, System.Int32)": {
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "year",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "month",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "day",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "hour",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "minute",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "second",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                    },
                    "System.DateTime.__init__(System.Int32, System.Int32, System.Int32, System.Int32, System.Int32, System.Int32, System.DateTimeKind)": {
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "year",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "month",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "day",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "hour",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "minute",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "second",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "kind",
                                "type": "System.DateTimeKind",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                    },
                    "System.DateTime.__init__(System.Int32, System.Int32, System.Int32, System.Int32, System.Int32, System.Int32, System.Globalization.Calendar)": {
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "year",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "month",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "day",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "hour",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "minute",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "second",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "calendar",
                                "type": "System.Globalization.Calendar",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                    },
                    "System.DateTime.__init__(System.Int32, System.Int32, System.Int32, System.Int32, System.Int32, System.Int32, System.Int32)": {
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "year",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "month",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "day",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "hour",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "minute",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "second",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "millisecond",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                    },
                    "System.DateTime.__init__(System.Int32, System.Int32, System.Int32, System.Int32, System.Int32, System.Int32, System.Int32, System.DateTimeKind)": {
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "year",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "month",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "day",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "hour",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "minute",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "second",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "millisecond",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "kind",
                                "type": "System.DateTimeKind",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                    },
                    "System.DateTime.__init__(System.Int32, System.Int32, System.Int32, System.Int32, System.Int32, System.Int32, System.Int32, System.Globalization.Calendar)": {
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "year",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "month",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "day",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "hour",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "minute",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "second",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "millisecond",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "calendar",
                                "type": "System.Globalization.Calendar",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                    },
                    "System.DateTime.__init__(System.Int32, System.Int32, System.Int32, System.Int32, System.Int32, System.Int32, System.Int32, System.Globalization.Calendar, System.DateTimeKind)": {
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "year",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "month",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "day",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "hour",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "minute",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "second",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "millisecond",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "calendar",
                                "type": "System.Globalization.Calendar",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "kind",
                                "type": "System.DateTimeKind",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                    },
                },
                "properties": {
                    "System.DateTime.Date": {
                        "name": "Date",
                        "declaring_type": "System.DateTime",
                        "type": "System.DateTime",
                        "setter": False,
                        "static": False,
                    },
                    "System.DateTime.Day": {
                        "name": "Day",
                        "declaring_type": "System.DateTime",
                        "type": "System.Int32",
                        "setter": False,
                        "static": False,
                    },
                    "System.DateTime.DayOfWeek": {
                        "name": "DayOfWeek",
                        "declaring_type": "System.DateTime",
                        "type": "System.DayOfWeek",
                        "setter": False,
                        "static": False,
                    },
                    "System.DateTime.DayOfYear": {
                        "name": "DayOfYear",
                        "declaring_type": "System.DateTime",
                        "type": "System.Int32",
                        "setter": False,
                        "static": False,
                    },
                    "System.DateTime.Hour": {
                        "name": "Hour",
                        "declaring_type": "System.DateTime",
                        "type": "System.Int32",
                        "setter": False,
                        "static": False,
                    },
                    "System.DateTime.Kind": {
                        "name": "Kind",
                        "declaring_type": "System.DateTime",
                        "type": "System.DateTimeKind",
                        "setter": False,
                        "static": False,
                    },
                    "System.DateTime.Millisecond": {
                        "name": "Millisecond",
                        "declaring_type": "System.DateTime",
                        "type": "System.Int32",
                        "setter": False,
                        "static": False,
                    },
                    "System.DateTime.Minute": {
                        "name": "Minute",
                        "declaring_type": "System.DateTime",
                        "type": "System.Int32",
                        "setter": False,
                        "static": False,
                    },
                    "System.DateTime.Month": {
                        "name": "Month",
                        "declaring_type": "System.DateTime",
                        "type": "System.Int32",
                        "setter": False,
                        "static": False,
                    },
                    "System.DateTime.Now": {
                        "name": "Now",
                        "declaring_type": "System.DateTime",
                        "type": "System.DateTime",
                        "setter": False,
                        "static": True,
                    },
                    "System.DateTime.Second": {
                        "name": "Second",
                        "declaring_type": "System.DateTime",
                        "type": "System.Int32",
                        "setter": False,
                        "static": False,
                    },
                    "System.DateTime.Ticks": {
                        "name": "Ticks",
                        "declaring_type": "System.DateTime",
                        "type": "System.Int64",
                        "setter": False,
                        "static": False,
                    },
                    "System.DateTime.TimeOfDay": {
                        "name": "TimeOfDay",
                        "declaring_type": "System.DateTime",
                        "type": "System.TimeSpan",
                        "setter": False,
                        "static": False,
                    },
                    "System.DateTime.Today": {
                        "name": "Today",
                        "declaring_type": "System.DateTime",
                        "type": "System.DateTime",
                        "setter": False,
                        "static": True,
                    },
                    "System.DateTime.UtcNow": {
                        "name": "UtcNow",
                        "declaring_type": "System.DateTime",
                        "type": "System.DateTime",
                        "setter": False,
                        "static": True,
                    },
                    "System.DateTime.Year": {
                        "name": "Year",
                        "declaring_type": "System.DateTime",
                        "type": "System.Int32",
                        "setter": False,
                        "static": False,
                    },
                },
                "methods": {
                    "System.DateTime.Add(System.TimeSpan)": {
                        "name": "Add",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "value",
                                "type": "System.TimeSpan",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.DateTime",),
                        "static": False,
                    },
                    "System.DateTime.AddDays(System.Double)": {
                        "name": "AddDays",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "value",
                                "type": "System.Double",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.DateTime",),
                        "static": False,
                    },
                    "System.DateTime.AddHours(System.Double)": {
                        "name": "AddHours",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "value",
                                "type": "System.Double",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.DateTime",),
                        "static": False,
                    },
                    "System.DateTime.AddMilliseconds(System.Double)": {
                        "name": "AddMilliseconds",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "value",
                                "type": "System.Double",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.DateTime",),
                        "static": False,
                    },
                    "System.DateTime.AddMinutes(System.Double)": {
                        "name": "AddMinutes",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "value",
                                "type": "System.Double",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.DateTime",),
                        "static": False,
                    },
                    "System.DateTime.AddMonths(System.Int32)": {
                        "name": "AddMonths",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "months",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.DateTime",),
                        "static": False,
                    },
                    "System.DateTime.AddSeconds(System.Double)": {
                        "name": "AddSeconds",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "value",
                                "type": "System.Double",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.DateTime",),
                        "static": False,
                    },
                    "System.DateTime.AddTicks(System.Int64)": {
                        "name": "AddTicks",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "value",
                                "type": "System.Int64",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.DateTime",),
                        "static": False,
                    },
                    "System.DateTime.AddYears(System.Int32)": {
                        "name": "AddYears",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "value",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.DateTime",),
                        "static": False,
                    },
                    "System.DateTime.Compare(System.DateTime, System.DateTime)": {
                        "name": "Compare",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "t1",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "t2",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Int32",),
                        "static": True,
                    },
                    "System.IComparable[System.DateTime].CompareTo(System.DateTime)": {
                        "name": "CompareTo",
                        "declaring_type": "System.IComparable[System.DateTime]",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Int32",),
                        "static": False,
                    },
                    "System.IComparable.CompareTo(System.Object)": {
                        "name": "CompareTo",
                        "declaring_type": "System.IComparable",
                        "parameters": (
                            {
                                "name": "obj",
                                "type": "System.Object",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Int32",),
                        "static": False,
                    },
                    "System.DateTime.DaysInMonth(System.Int32, System.Int32)": {
                        "name": "DaysInMonth",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "year",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "month",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Int32",),
                        "static": True,
                    },
                    "System.IEquatable[System.DateTime].Equals(System.DateTime)": {
                        "name": "Equals",
                        "declaring_type": "System.IEquatable[System.DateTime]",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Boolean",),
                        "static": False,
                    },
                    "System.Object.Equals(System.Object)": {
                        "name": "Equals",
                        "declaring_type": "System.Object",
                        "parameters": (
                            {
                                "name": "obj",
                                "type": "System.Object",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Boolean",),
                        "static": False,
                    },
                    "System.DateTime.Equals(System.DateTime, System.DateTime)": {
                        "name": "Equals",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "t1",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "t2",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Boolean",),
                        "static": True,
                    },
                    "System.DateTime.FromBinary(System.Int64)": {
                        "name": "FromBinary",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "dateData",
                                "type": "System.Int64",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.DateTime",),
                        "static": True,
                    },
                    "System.DateTime.FromFileTime(System.Int64)": {
                        "name": "FromFileTime",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "fileTime",
                                "type": "System.Int64",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.DateTime",),
                        "static": True,
                    },
                    "System.DateTime.FromFileTimeUtc(System.Int64)": {
                        "name": "FromFileTimeUtc",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "fileTime",
                                "type": "System.Int64",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.DateTime",),
                        "static": True,
                    },
                    "System.DateTime.FromOADate(System.Double)": {
                        "name": "FromOADate",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "d",
                                "type": "System.Double",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.DateTime",),
                        "static": True,
                    },
                    "System.DateTime.GetDateTimeFormats()": {
                        "name": "GetDateTimeFormats",
                        "declaring_type": "System.DateTime",
                        "parameters": (),
                        "returns": ("System.String",),
                        "static": False,
                    },
                    "System.DateTime.GetDateTimeFormats(System.Char)": {
                        "name": "GetDateTimeFormats",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "format",
                                "type": "System.Char",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.String",),
                        "static": False,
                    },
                    "System.DateTime.GetDateTimeFormats(System.IFormatProvider)": {
                        "name": "GetDateTimeFormats",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "provider",
                                "type": "System.IFormatProvider",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.String",),
                        "static": False,
                    },
                    "System.DateTime.GetDateTimeFormats(System.Char, System.IFormatProvider)": {
                        "name": "GetDateTimeFormats",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "format",
                                "type": "System.Char",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "provider",
                                "type": "System.IFormatProvider",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.String",),
                        "static": False,
                    },
                    "System.Object.GetHashCode()": {
                        "name": "GetHashCode",
                        "declaring_type": "System.Object",
                        "parameters": (),
                        "returns": ("System.Int32",),
                        "static": False,
                    },
                    "System.Runtime.Serialization.ISerializable.GetObjectData(System.Runtime.Serialization.SerializationInfo, System.Runtime.Serialization.StreamingContext)": {
                        "name": "GetObjectData",
                        "declaring_type": "System.Runtime.Serialization.ISerializable",
                        "parameters": (
                            {
                                "name": "info",
                                "type": "System.Runtime.Serialization.SerializationInfo",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "context",
                                "type": "System.Runtime.Serialization.StreamingContext",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Void",),
                        "static": False,
                    },
                    "System.Object.GetType()": {
                        "name": "GetType",
                        "declaring_type": "System.Object",
                        "parameters": (),
                        "returns": ("System.Type",),
                        "static": False,
                    },
                    "System.IConvertible.GetTypeCode()": {
                        "name": "GetTypeCode",
                        "declaring_type": "System.IConvertible",
                        "parameters": (),
                        "returns": ("System.TypeCode",),
                        "static": False,
                    },
                    "System.DateTime.IsDaylightSavingTime()": {
                        "name": "IsDaylightSavingTime",
                        "declaring_type": "System.DateTime",
                        "parameters": (),
                        "returns": ("System.Boolean",),
                        "static": False,
                    },
                    "System.DateTime.IsLeapYear(System.Int32)": {
                        "name": "IsLeapYear",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "year",
                                "type": "System.Int32",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Boolean",),
                        "static": True,
                    },
                    "System.DateTime.Parse(System.String)": {
                        "name": "Parse",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "s",
                                "type": "System.String",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.DateTime",),
                        "static": True,
                    },
                    "System.DateTime.Parse(System.String, System.IFormatProvider)": {
                        "name": "Parse",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "s",
                                "type": "System.String",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "provider",
                                "type": "System.IFormatProvider",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.DateTime",),
                        "static": True,
                    },
                    "System.DateTime.Parse(System.String, System.IFormatProvider, System.Globalization.DateTimeStyles)": {
                        "name": "Parse",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "s",
                                "type": "System.String",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "provider",
                                "type": "System.IFormatProvider",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "styles",
                                "type": "System.Globalization.DateTimeStyles",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.DateTime",),
                        "static": True,
                    },
                    "System.DateTime.ParseExact(System.String, System.String, System.IFormatProvider)": {
                        "name": "ParseExact",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "s",
                                "type": "System.String",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "format",
                                "type": "System.String",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "provider",
                                "type": "System.IFormatProvider",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.DateTime",),
                        "static": True,
                    },
                    "System.DateTime.ParseExact(System.String, System.String, System.IFormatProvider, System.Globalization.DateTimeStyles)": {
                        "name": "ParseExact",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "s",
                                "type": "System.String",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "formats",
                                "type": "System.String",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "provider",
                                "type": "System.IFormatProvider",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "style",
                                "type": "System.Globalization.DateTimeStyles",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.DateTime",),
                        "static": True,
                    },
                    "System.DateTime.SpecifyKind(System.DateTime, System.DateTimeKind)": {
                        "name": "SpecifyKind",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "value",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "kind",
                                "type": "System.DateTimeKind",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.DateTime",),
                        "static": True,
                    },
                    "System.DateTime.Subtract(System.DateTime)": {
                        "name": "Subtract",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "value",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.TimeSpan",),
                        "static": False,
                    },
                    "System.DateTime.Subtract(System.TimeSpan)": {
                        "name": "Subtract",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "value",
                                "type": "System.TimeSpan",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.DateTime",),
                        "static": False,
                    },
                    "System.DateTime.ToBinary()": {
                        "name": "ToBinary",
                        "declaring_type": "System.DateTime",
                        "parameters": (),
                        "returns": ("System.Int64",),
                        "static": False,
                    },
                    "System.IConvertible.ToBoolean(System.IFormatProvider)": {
                        "name": "ToBoolean",
                        "declaring_type": "System.IConvertible",
                        "parameters": (
                            {
                                "name": "provider",
                                "type": "System.IFormatProvider",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Boolean",),
                        "static": False,
                    },
                    "System.IConvertible.ToByte(System.IFormatProvider)": {
                        "name": "ToByte",
                        "declaring_type": "System.IConvertible",
                        "parameters": (
                            {
                                "name": "provider",
                                "type": "System.IFormatProvider",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Byte",),
                        "static": False,
                    },
                    "System.IConvertible.ToChar(System.IFormatProvider)": {
                        "name": "ToChar",
                        "declaring_type": "System.IConvertible",
                        "parameters": (
                            {
                                "name": "provider",
                                "type": "System.IFormatProvider",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Char",),
                        "static": False,
                    },
                    "System.IConvertible.ToDateTime(System.IFormatProvider)": {
                        "name": "ToDateTime",
                        "declaring_type": "System.IConvertible",
                        "parameters": (
                            {
                                "name": "provider",
                                "type": "System.IFormatProvider",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.DateTime",),
                        "static": False,
                    },
                    "System.IConvertible.ToDecimal(System.IFormatProvider)": {
                        "name": "ToDecimal",
                        "declaring_type": "System.IConvertible",
                        "parameters": (
                            {
                                "name": "provider",
                                "type": "System.IFormatProvider",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Decimal",),
                        "static": False,
                    },
                    "System.IConvertible.ToDouble(System.IFormatProvider)": {
                        "name": "ToDouble",
                        "declaring_type": "System.IConvertible",
                        "parameters": (
                            {
                                "name": "provider",
                                "type": "System.IFormatProvider",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Double",),
                        "static": False,
                    },
                    "System.DateTime.ToFileTime()": {
                        "name": "ToFileTime",
                        "declaring_type": "System.DateTime",
                        "parameters": (),
                        "returns": ("System.Int64",),
                        "static": False,
                    },
                    "System.DateTime.ToFileTimeUtc()": {
                        "name": "ToFileTimeUtc",
                        "declaring_type": "System.DateTime",
                        "parameters": (),
                        "returns": ("System.Int64",),
                        "static": False,
                    },
                    "System.IConvertible.ToInt16(System.IFormatProvider)": {
                        "name": "ToInt16",
                        "declaring_type": "System.IConvertible",
                        "parameters": (
                            {
                                "name": "provider",
                                "type": "System.IFormatProvider",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Int16",),
                        "static": False,
                    },
                    "System.IConvertible.ToInt32(System.IFormatProvider)": {
                        "name": "ToInt32",
                        "declaring_type": "System.IConvertible",
                        "parameters": (
                            {
                                "name": "provider",
                                "type": "System.IFormatProvider",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Int32",),
                        "static": False,
                    },
                    "System.IConvertible.ToInt64(System.IFormatProvider)": {
                        "name": "ToInt64",
                        "declaring_type": "System.IConvertible",
                        "parameters": (
                            {
                                "name": "provider",
                                "type": "System.IFormatProvider",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Int64",),
                        "static": False,
                    },
                    "System.DateTime.ToLocalTime()": {
                        "name": "ToLocalTime",
                        "declaring_type": "System.DateTime",
                        "parameters": (),
                        "returns": ("System.DateTime",),
                        "static": False,
                    },
                    "System.DateTime.ToLongDateString()": {
                        "name": "ToLongDateString",
                        "declaring_type": "System.DateTime",
                        "parameters": (),
                        "returns": ("System.String",),
                        "static": False,
                    },
                    "System.DateTime.ToLongTimeString()": {
                        "name": "ToLongTimeString",
                        "declaring_type": "System.DateTime",
                        "parameters": (),
                        "returns": ("System.String",),
                        "static": False,
                    },
                    "System.DateTime.ToOADate()": {
                        "name": "ToOADate",
                        "declaring_type": "System.DateTime",
                        "parameters": (),
                        "returns": ("System.Double",),
                        "static": False,
                    },
                    "System.IConvertible.ToSByte(System.IFormatProvider)": {
                        "name": "ToSByte",
                        "declaring_type": "System.IConvertible",
                        "parameters": (
                            {
                                "name": "provider",
                                "type": "System.IFormatProvider",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.SByte",),
                        "static": False,
                    },
                    "System.DateTime.ToShortDateString()": {
                        "name": "ToShortDateString",
                        "declaring_type": "System.DateTime",
                        "parameters": (),
                        "returns": ("System.String",),
                        "static": False,
                    },
                    "System.DateTime.ToShortTimeString()": {
                        "name": "ToShortTimeString",
                        "declaring_type": "System.DateTime",
                        "parameters": (),
                        "returns": ("System.String",),
                        "static": False,
                    },
                    "System.IConvertible.ToSingle(System.IFormatProvider)": {
                        "name": "ToSingle",
                        "declaring_type": "System.IConvertible",
                        "parameters": (
                            {
                                "name": "provider",
                                "type": "System.IFormatProvider",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Single",),
                        "static": False,
                    },
                    "System.Object.ToString()": {
                        "name": "ToString",
                        "declaring_type": "System.Object",
                        "parameters": (),
                        "returns": ("System.String",),
                        "static": False,
                    },
                    "System.IConvertible.ToString(System.IFormatProvider)": {
                        "name": "ToString",
                        "declaring_type": "System.IConvertible",
                        "parameters": (
                            {
                                "name": "provider",
                                "type": "System.IFormatProvider",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.String",),
                        "static": False,
                    },
                    "System.DateTime.ToString(System.String)": {
                        "name": "ToString",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "format",
                                "type": "System.String",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.String",),
                        "static": False,
                    },
                    "System.IFormattable.ToString(System.String, System.IFormatProvider)": {
                        "name": "ToString",
                        "declaring_type": "System.IFormattable",
                        "parameters": (
                            {
                                "name": "format",
                                "type": "System.String",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "formatProvider",
                                "type": "System.IFormatProvider",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.String",),
                        "static": False,
                    },
                    "System.IConvertible.ToType(System.Type, System.IFormatProvider)": {
                        "name": "ToType",
                        "declaring_type": "System.IConvertible",
                        "parameters": (
                            {
                                "name": "conversionType",
                                "type": "System.Type",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "provider",
                                "type": "System.IFormatProvider",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Object",),
                        "static": False,
                    },
                    "System.IConvertible.ToUInt16(System.IFormatProvider)": {
                        "name": "ToUInt16",
                        "declaring_type": "System.IConvertible",
                        "parameters": (
                            {
                                "name": "provider",
                                "type": "System.IFormatProvider",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.UInt16",),
                        "static": False,
                    },
                    "System.IConvertible.ToUInt32(System.IFormatProvider)": {
                        "name": "ToUInt32",
                        "declaring_type": "System.IConvertible",
                        "parameters": (
                            {
                                "name": "provider",
                                "type": "System.IFormatProvider",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.UInt32",),
                        "static": False,
                    },
                    "System.IConvertible.ToUInt64(System.IFormatProvider)": {
                        "name": "ToUInt64",
                        "declaring_type": "System.IConvertible",
                        "parameters": (
                            {
                                "name": "provider",
                                "type": "System.IFormatProvider",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.UInt64",),
                        "static": False,
                    },
                    "System.DateTime.ToUniversalTime()": {
                        "name": "ToUniversalTime",
                        "declaring_type": "System.DateTime",
                        "parameters": (),
                        "returns": ("System.DateTime",),
                        "static": False,
                    },
                    "System.DateTime.TryParse(System.String, System.DateTime)": {
                        "name": "TryParse",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "s",
                                "type": "System.String",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "result",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": True,
                            },
                        ),
                        "returns": ("System.Boolean", "System.DateTime"),
                        "static": True,
                    },
                    "System.DateTime.TryParse(System.String, System.IFormatProvider, System.Globalization.DateTimeStyles, System.DateTime)": {
                        "name": "TryParse",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "s",
                                "type": "System.String",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "provider",
                                "type": "System.IFormatProvider",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "styles",
                                "type": "System.Globalization.DateTimeStyles",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "result",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": True,
                            },
                        ),
                        "returns": ("System.Boolean", "System.DateTime"),
                        "static": True,
                    },
                    "System.DateTime.TryParseExact(System.String, System.String, System.IFormatProvider, System.Globalization.DateTimeStyles, System.DateTime)": {
                        "name": "TryParseExact",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "s",
                                "type": "System.String",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "formats",
                                "type": "System.String",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "provider",
                                "type": "System.IFormatProvider",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "style",
                                "type": "System.Globalization.DateTimeStyles",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "result",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": True,
                            },
                        ),
                        "returns": ("System.Boolean", "System.DateTime"),
                        "static": True,
                    },
                    "System.DateTime.op_Addition(System.DateTime, System.TimeSpan)": {
                        "name": "op_Addition",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "d",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "t",
                                "type": "System.TimeSpan",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.DateTime",),
                        "static": True,
                    },
                    "System.DateTime.op_Equality(System.DateTime, System.DateTime)": {
                        "name": "op_Equality",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "d1",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "d2",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Boolean",),
                        "static": True,
                    },
                    "System.DateTime.op_GreaterThan(System.DateTime, System.DateTime)": {
                        "name": "op_GreaterThan",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "t1",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "t2",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Boolean",),
                        "static": True,
                    },
                    "System.DateTime.op_GreaterThanOrEqual(System.DateTime, System.DateTime)": {
                        "name": "op_GreaterThanOrEqual",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "t1",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "t2",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Boolean",),
                        "static": True,
                    },
                    "System.DateTime.op_Inequality(System.DateTime, System.DateTime)": {
                        "name": "op_Inequality",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "d1",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "d2",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Boolean",),
                        "static": True,
                    },
                    "System.DateTime.op_LessThan(System.DateTime, System.DateTime)": {
                        "name": "op_LessThan",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "t1",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "t2",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Boolean",),
                        "static": True,
                    },
                    "System.DateTime.op_LessThanOrEqual(System.DateTime, System.DateTime)": {
                        "name": "op_LessThanOrEqual",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "t1",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "t2",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Boolean",),
                        "static": True,
                    },
                    "System.DateTime.op_Subtraction(System.DateTime, System.DateTime)": {
                        "name": "op_Subtraction",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "d1",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "d2",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.TimeSpan",),
                        "static": True,
                    },
                    "System.DateTime.op_Subtraction(System.DateTime, System.TimeSpan)": {
                        "name": "op_Subtraction",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "d",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "t",
                                "type": "System.TimeSpan",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.DateTime",),
                        "static": True,
                    },
                },
                "dunder_methods": {
                    "System.DateTime.__add__(System.TimeSpan)": {
                        "name": "__add__",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "System.TimeSpan",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.DateTime",),
                        "static": False,
                    },
                    "System.DateTime.__eq__(System.DateTime)": {
                        "name": "__eq__",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Boolean",),
                        "static": False,
                    },
                    "System.DateTime.__ge__(System.DateTime)": {
                        "name": "__ge__",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Boolean",),
                        "static": False,
                    },
                    "System.DateTime.__gt__(System.DateTime)": {
                        "name": "__gt__",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Boolean",),
                        "static": False,
                    },
                    "System.DateTime.__le__(System.DateTime)": {
                        "name": "__le__",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Boolean",),
                        "static": False,
                    },
                    "System.DateTime.__lt__(System.DateTime)": {
                        "name": "__lt__",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Boolean",),
                        "static": False,
                    },
                    "System.DateTime.__ne__(System.DateTime)": {
                        "name": "__ne__",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.Boolean",),
                        "static": False,
                    },
                    "System.DateTime.__sub__(System.DateTime)": {
                        "name": "__sub__",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "System.DateTime",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.TimeSpan",),
                        "static": False,
                    },
                    "System.DateTime.__sub__(System.TimeSpan)": {
                        "name": "__sub__",
                        "declaring_type": "System.DateTime",
                        "parameters": (
                            {
                                "name": "other",
                                "type": "System.TimeSpan",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.DateTime",),
                        "static": False,
                    },
                },
                "events": {},
                "nested": {},
            },
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(from_json, type_def)

    def test_compare(self) -> None:
        struct0: CStruct = CStruct.from_info(clr.GetClrType(Int32))
        struct1: CStruct = CStruct.from_info(clr.GetClrType(Single))
        struct2: CStruct = CStruct.from_info(clr.GetClrType(TimeSpan))
        struct3: CStruct = CStruct.from_info(clr.GetClrType(UInt32))

        self.assertLess(struct0, struct1)
        self.assertLess(struct1, struct2)
        self.assertLess(struct2, struct3)

        self.assertLessEqual(struct0, struct1)
        self.assertLessEqual(struct1, struct2)
        self.assertLessEqual(struct2, struct3)

        self.assertLessEqual(struct0, struct0)
        self.assertLessEqual(struct1, struct1)
        self.assertLessEqual(struct2, struct2)
        self.assertLessEqual(struct3, struct3)

        self.assertGreater(struct1, struct0)
        self.assertGreater(struct2, struct1)
        self.assertGreater(struct3, struct2)

        self.assertGreaterEqual(struct1, struct0)
        self.assertGreaterEqual(struct2, struct1)
        self.assertGreaterEqual(struct3, struct2)

        self.assertGreaterEqual(struct0, struct0)
        self.assertGreaterEqual(struct1, struct1)
        self.assertGreaterEqual(struct2, struct2)
        self.assertGreaterEqual(struct3, struct3)

    def test_sorted(self) -> None:
        struct0: CStruct = CStruct.from_info(clr.GetClrType(DateTimeKind))
        struct1: CStruct = CStruct.from_info(clr.GetClrType(DayOfWeek))
        struct2: CStruct = CStruct.from_info(clr.GetClrType(PlatformID))
        struct3: CStruct = CStruct.from_info(clr.GetClrType(TypeCode))

        ordered: Sequence[CStruct] = (struct0, struct1, struct2, struct3)
        unordered: MutableSequence[CStruct] = list(ordered)
        random.shuffle(unordered)

        self.assertSequenceEqual(sorted(unordered), ordered)


class TestCInterface(unittest.TestCase):
    def assertCInterface(
        self,
        interface: CInterface,
        name: str,
        namespace: str,
        generic_args: Sequence[CType],
        super_class: CType,
        properties: Mapping[str, CProperty],
        methods: Mapping[str, CMethod],
        dunder_methods: Mapping[str, CMethod],
        events: Mapping[str, CEvent],
    ) -> None:
        self.assertIsNotNone(interface)
        self.assertIsInstance(interface, CInterface)
        self.assertEqual(interface.name, name)
        self.assertEqual(interface.namespace, namespace)
        self.assertSequenceEqual(interface.generic_args, generic_args)
        self.assertEqual(interface.super_class, super_class)
        self.assertDictEqual(interface.properties, properties)
        self.assertDictEqual(interface.methods, methods)
        self.assertDictEqual(interface.dunder_methods, dunder_methods)
        self.assertDictEqual(interface.events, events)

    def test_from_info(self) -> None:
        type_info: TypeInfo = clr.GetClrType(IEquatable)
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCInterface(
            interface=cast(CInterface, type_def),
            name="IEquatable",
            namespace="System",
            generic_args=(CType("T", "System", (), True),),
            super_class=cast(CType, None),
            properties={},
            methods={
                "System.IEquatable[System.$T].Equals(System.$T)": CMethod(
                    "Equals",
                    CType("IEquatable", "System", (CType("T", "System", (), True),)),
                    (CParameter("other", CType("T", "System", (), True), False, False),),
                    (CType("Boolean", "System"),),
                    False,
                ),
            },
            dunder_methods={},
            events={},
        )

    def test_json(self) -> None:
        type_info: TypeInfo = clr.GetClrType(IFormattable)
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            json,
            {
                "type": "interface",
                "name": "IFormattable",
                "namespace": "System",
                "generic_args": (),
                "super_class": None,
                "properties": {},
                "methods": {
                    "System.IFormattable.ToString(System.String, System.IFormatProvider)": {
                        "name": "ToString",
                        "declaring_type": "System.IFormattable",
                        "parameters": (
                            {
                                "name": "format",
                                "type": "System.String",
                                "has_default": False,
                                "is_out": False,
                            },
                            {
                                "name": "formatProvider",
                                "type": "System.IFormatProvider",
                                "has_default": False,
                                "is_out": False,
                            },
                        ),
                        "returns": ("System.String",),
                        "static": False,
                    }
                },
                "dunder_methods": {},
                "events": {},
            },
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(from_json, type_def)

    def test_compare(self) -> None:
        interface0: CInterface = CInterface.from_info(clr.GetClrType(IConvertible))
        interface1: CInterface = CInterface.from_info(clr.GetClrType(IDisposable))
        interface2: CInterface = CInterface.from_info(clr.GetClrType(IEquatable))
        interface3: CInterface = CInterface.from_info(clr.GetClrType(IFormatProvider))

        self.assertLess(interface0, interface1)
        self.assertLess(interface1, interface2)
        self.assertLess(interface2, interface3)

        self.assertLessEqual(interface0, interface1)
        self.assertLessEqual(interface1, interface2)
        self.assertLessEqual(interface2, interface3)

        self.assertLessEqual(interface0, interface0)
        self.assertLessEqual(interface1, interface1)
        self.assertLessEqual(interface2, interface2)
        self.assertLessEqual(interface3, interface3)

        self.assertGreater(interface1, interface0)
        self.assertGreater(interface2, interface1)
        self.assertGreater(interface3, interface2)

        self.assertGreaterEqual(interface1, interface0)
        self.assertGreaterEqual(interface2, interface1)
        self.assertGreaterEqual(interface3, interface2)

        self.assertGreaterEqual(interface0, interface0)
        self.assertGreaterEqual(interface1, interface1)
        self.assertGreaterEqual(interface2, interface2)
        self.assertGreaterEqual(interface3, interface3)

    def test_sorted(self) -> None:
        interface0: CInterface = CInterface.from_info(clr.GetClrType(DateTimeKind))
        interface1: CInterface = CInterface.from_info(clr.GetClrType(DayOfWeek))
        interface2: CInterface = CInterface.from_info(clr.GetClrType(PlatformID))
        interface3: CInterface = CInterface.from_info(clr.GetClrType(TypeCode))

        ordered: Sequence[CInterface] = (interface0, interface1, interface2, interface3)
        unordered: MutableSequence[CInterface] = list(ordered)
        random.shuffle(unordered)

        self.assertSequenceEqual(sorted(unordered), ordered)


class TestCEnum(unittest.TestCase):
    def assertCEnum(self, enum: CEnum, name: str, namespace: str, fields: Sequence[str]) -> None:
        self.assertIsNotNone(enum)
        self.assertIsInstance(enum, CEnum)
        self.assertEqual(enum.name, name)
        self.assertEqual(enum.namespace, namespace)
        self.assertSequenceEqual(enum.fields, fields)

    def test_from_info(self) -> None:
        type_info: TypeInfo = clr.GetClrType(DayOfWeek)
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCEnum(
            enum=cast(CEnum, type_def),
            name="DayOfWeek",
            namespace="System",
            fields=("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"),
        )

    def test_json(self) -> None:
        type_info: TypeInfo = clr.GetClrType(DayOfWeek)
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            json,
            {
                "type": "enum",
                "name": "DayOfWeek",
                "namespace": "System",
                "fields": (
                    "Sunday",
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Saturday",
                ),
            },
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(from_json, type_def)

    def test_compare(self) -> None:
        enum0: CEnum = CEnum.from_info(clr.GetClrType(DateTimeKind))
        enum1: CEnum = CEnum.from_info(clr.GetClrType(DayOfWeek))
        enum2: CEnum = CEnum.from_info(clr.GetClrType(PlatformID))
        enum3: CEnum = CEnum.from_info(clr.GetClrType(TypeCode))

        self.assertLess(enum0, enum1)
        self.assertLess(enum1, enum2)
        self.assertLess(enum2, enum3)

        self.assertLessEqual(enum0, enum1)
        self.assertLessEqual(enum1, enum2)
        self.assertLessEqual(enum2, enum3)

        self.assertLessEqual(enum0, enum0)
        self.assertLessEqual(enum1, enum1)
        self.assertLessEqual(enum2, enum2)
        self.assertLessEqual(enum3, enum3)

        self.assertGreater(enum1, enum0)
        self.assertGreater(enum2, enum1)
        self.assertGreater(enum3, enum2)

        self.assertGreaterEqual(enum1, enum0)
        self.assertGreaterEqual(enum2, enum1)
        self.assertGreaterEqual(enum3, enum2)

        self.assertGreaterEqual(enum0, enum0)
        self.assertGreaterEqual(enum1, enum1)
        self.assertGreaterEqual(enum2, enum2)
        self.assertGreaterEqual(enum3, enum3)

    def test_sorted(self) -> None:
        enum0: CEnum = CEnum.from_info(clr.GetClrType(DateTimeKind))
        enum1: CEnum = CEnum.from_info(clr.GetClrType(DayOfWeek))
        enum2: CEnum = CEnum.from_info(clr.GetClrType(PlatformID))
        enum3: CEnum = CEnum.from_info(clr.GetClrType(TypeCode))

        ordered: Sequence[CEnum] = (enum0, enum1, enum2, enum3)
        unordered: MutableSequence[CEnum] = list(ordered)
        random.shuffle(unordered)

        self.assertSequenceEqual(sorted(unordered), ordered)


class TestCDelegate(unittest.TestCase):
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
        self.assertEqual(delegate.name, name)
        self.assertEqual(delegate.namespace, namespace)
        self.assertSequenceEqual(delegate.parameters, parameters)
        self.assertEqual(delegate.return_type, return_type)

    def test_from_info(self) -> None:
        type_info: TypeInfo = clr.GetClrType(Predicate)
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCDelegate(
            delegate=cast(CDelegate, type_def),
            name="Predicate",
            namespace="System",
            parameters=(CParameter("obj", CType("T", "System", (), True), False, False),),
            return_type=CType("Boolean", "System"),
        )

        type_info: TypeInfo = clr.GetClrType(Comparison)
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)

        self.assertCDelegate(
            delegate=cast(CDelegate, type_def),
            name="Comparison",
            namespace="System",
            parameters=(
                CParameter("x", CType("T", "System", (), True), False, False),
                CParameter("y", CType("T", "System", (), True), False, False),
            ),
            return_type=CType("Int32", "System"),
        )

    def test_json(self) -> None:
        type_info: TypeInfo = clr.GetClrType(Predicate)
        type_def: CTypeDefinition = CTypeDefinition.from_info(type_info)
        json: JsonType = type_def.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            json,
            {
                "type": "delegate",
                "name": "Predicate",
                "namespace": "System",
                "parameters": (
                    {
                        "name": "obj",
                        "type": "System.$T",
                        "has_default": False,
                        "is_out": False,
                    },
                ),
                "return_type": "System.Boolean",
            },
        )

        from_json: CTypeDefinition = CTypeDefinition.from_json(json)

        self.assertEqual(from_json, type_def)

    def test_compare(self) -> None:
        delegate0: CDelegate = CDelegate.from_info(clr.GetClrType(AsyncCallback))
        delegate1: CDelegate = CDelegate.from_info(clr.GetClrType(Comparison))
        delegate2: CDelegate = CDelegate.from_info(clr.GetClrType(Predicate))
        delegate3: CDelegate = CDelegate.from_info(clr.GetClrType(UnhandledExceptionEventHandler))

        self.assertLess(delegate0, delegate1)
        self.assertLess(delegate1, delegate2)
        self.assertLess(delegate2, delegate3)

        self.assertLessEqual(delegate0, delegate1)
        self.assertLessEqual(delegate1, delegate2)
        self.assertLessEqual(delegate2, delegate3)

        self.assertLessEqual(delegate0, delegate0)
        self.assertLessEqual(delegate1, delegate1)
        self.assertLessEqual(delegate2, delegate2)
        self.assertLessEqual(delegate3, delegate3)

        self.assertGreater(delegate1, delegate0)
        self.assertGreater(delegate2, delegate1)
        self.assertGreater(delegate3, delegate2)

        self.assertGreaterEqual(delegate1, delegate0)
        self.assertGreaterEqual(delegate2, delegate1)
        self.assertGreaterEqual(delegate3, delegate2)

        self.assertGreaterEqual(delegate0, delegate0)
        self.assertGreaterEqual(delegate1, delegate1)
        self.assertGreaterEqual(delegate2, delegate2)
        self.assertGreaterEqual(delegate3, delegate3)

    def test_sorted(self) -> None:
        delegate0: CDelegate = CDelegate.from_info(clr.GetClrType(AsyncCallback))
        delegate1: CDelegate = CDelegate.from_info(clr.GetClrType(Comparison))
        delegate2: CDelegate = CDelegate.from_info(clr.GetClrType(Predicate))
        delegate3: CDelegate = CDelegate.from_info(clr.GetClrType(UnhandledExceptionEventHandler))

        ordered: Sequence[CDelegate] = (delegate0, delegate1, delegate2, delegate3)
        unordered: MutableSequence[CDelegate] = list(ordered)
        random.shuffle(unordered)

        self.assertSequenceEqual(sorted(unordered), ordered)


class TestCType(unittest.TestCase):
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
        self.assertEqual(type.name, name)
        self.assertEqual(type.namespace, namespace)
        self.assertSequenceEqual(type.inner, inner)
        self.assertEqual(type.reference, reference)
        self.assertEqual(type.generic, generic)
        self.assertEqual(type.nullable, nullable)

    def test_from_info_simple(self) -> None:
        type_info: TypeInfo = clr.GetClrType(String)
        c_type: CType = CType.from_info(type_info)

        self.assertCType(
            type=c_type,
            name="String",
            namespace="System",
            inner=(),
            reference=False,
            generic=False,
            nullable=False,
        )

    def test_from_info_inner(self) -> None:
        type_info: TypeInfo = clr.GetClrType(Dictionary)
        c_type: CType = CType.from_info(type_info)

        self.assertCType(
            type=c_type,
            name="Dictionary",
            namespace="System.Collections.Generic",
            inner=(
                CType("TKey", "System.Collections.Generic", generic=True),
                CType("TValue", "System.Collections.Generic", generic=True),
            ),
            reference=False,
            generic=False,
            nullable=False,
        )

    def test_from_info_reference(self) -> None:
        type_info: TypeInfo = clr.GetClrType(Int32).MakeByRefType()
        c_type: CType = CType.from_info(type_info)

        self.assertCType(
            type=c_type,
            name="Int32",
            namespace="System",
            inner=(),
            reference=True,
            generic=False,
            nullable=False,
        )

    def test_from_info_generic(self) -> None:
        type_info: TypeInfo = clr.GetClrType(IEnumerable)
        c_type: CType = CType.from_info(type_info)

        self.assertCType(
            type=c_type,
            name="IEnumerable",
            namespace="System.Collections.Generic",
            inner=(CType("T", "System.Collections.Generic", generic=True),),
            reference=False,
            generic=False,
            nullable=False,
        )

    def test_from_info_nullable(self) -> None:
        type_info: TypeInfo = clr.GetClrType(Nullable)
        method_info: MethodInfo = type_info.GetMethod("Compare")
        parameter_info: ParameterInfo = method_info.GetParameters()[0]
        c_type: CType = CType.from_info(parameter_info.ParameterType)

        self.assertCType(
            type=c_type,
            name="T",
            namespace="System",
            inner=(),
            reference=False,
            generic=True,
            nullable=True,
        )

    def test_json_no_namespace(self) -> None:
        c_type: CType = CType("String")
        json: JsonType = c_type.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, str)
        self.assertEqual(json, "String")

        from_json: CType = CType.from_json(json)

        self.assertEqual(from_json, c_type)

    def test_json_simple(self) -> None:
        c_type: CType = CType("String", "Namespace")
        json: JsonType = c_type.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, str)
        self.assertEqual(json, "Namespace.String")

        from_json: CType = CType.from_json(json)

        self.assertEqual(from_json, c_type)

    def test_json_reference(self) -> None:
        c_type: CType = CType("T", "Namespace", reference=True)
        json: JsonType = c_type.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, str)
        self.assertEqual(json, "Namespace.*T")

        from_json: CType = CType.from_json(json)

        self.assertEqual(from_json, c_type)

    def test_json_generic(self) -> None:
        c_type: CType = CType("T", "Namespace", generic=True)
        json: JsonType = c_type.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, str)
        self.assertEqual(json, "Namespace.$T")

        from_json: CType = CType.from_json(json)

        self.assertEqual(from_json, c_type)

    def test_json_nullable(self) -> None:
        c_type: CType = CType("String", "Namespace", nullable=True)
        json: JsonType = c_type.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, str)
        self.assertEqual(json, "Namespace.?String")

        from_json: CType = CType.from_json(json)

        self.assertEqual(from_json, c_type)

    def test_json_generic_nullable(self) -> None:
        c_type: CType = CType("String", "Namespace", generic=True, nullable=True)
        json: JsonType = c_type.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, str)
        self.assertEqual(json, "Namespace.?$String")

        from_json: CType = CType.from_json(json)

        self.assertEqual(from_json, c_type)

    def test_json_inner(self) -> None:
        c_type: CType = CType(
            name="Dict",
            namespace="Namespace",
            inner=(
                CType("TKey", "Namespace", generic=True),
                CType("TValue", "Namespace", generic=True),
            ),
        )
        json: JsonType = c_type.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, str)
        self.assertEqual(json, "Namespace.Dict[Namespace.$TKey, Namespace.$TValue]")

        from_json: CType = CType.from_json(json)

        self.assertEqual(from_json, c_type)

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

        self.assertSequenceEqual(sorted(unordered), ordered)


class TestCParameter(unittest.TestCase):
    def assertCParameter(
        self, parameter: CParameter, name: str, type: CType, has_default: bool, is_out: bool
    ) -> None:
        self.assertIsNotNone(parameter)
        self.assertIsInstance(parameter, CParameter)
        self.assertEqual(parameter.name, name)
        self.assertEqual(parameter.type, type)
        self.assertEqual(parameter.has_default, has_default)
        self.assertEqual(parameter.is_out, is_out)

    def test_from_info(self) -> None:
        type_info: TypeInfo = clr.GetClrType(Math)
        method_info: MethodInfo = type_info.GetMethod("Atan2")
        parameters: Sequence[CParameter] = list(
            map(CParameter.from_info, method_info.GetParameters())
        )

        self.assertCParameter(
            parameter=parameters[0],
            name="y",
            type=CType("Double", "System"),
            has_default=False,
            is_out=False,
        )
        self.assertCParameter(
            parameter=parameters[1],
            name="x",
            type=CType("Double", "System"),
            has_default=False,
            is_out=False,
        )

    def test_from_info_is_out(self) -> None:
        type_info: TypeInfo = clr.GetClrType(Math)
        params: Array[Type] = Array[Type]((Int32, Int32, clr.GetClrType(Int32).MakeByRefType()))
        method_info: MethodInfo = type_info.GetMethod("DivRem", params)
        parameter_info: ParameterInfo = method_info.GetParameters()[2]
        c_parameter: CParameter = CParameter.from_info(parameter_info)

        self.assertCParameter(
            parameter=c_parameter,
            name="result",
            type=CType("Int32", "System", reference=True),
            has_default=False,
            is_out=True,
        )

    def test_json(self) -> None:
        type_info: TypeInfo = clr.GetClrType(Math)
        method_info: MethodInfo = type_info.GetMethod("BigMul")
        parameters: Sequence[CParameter] = list(
            map(CParameter.from_info, method_info.GetParameters())
        )
        json: JsonType = parameters[0].to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            json,
            {
                "name": "a",
                "type": "System.Int32",
                "has_default": False,
                "is_out": False,
            },
        )

        from_json: CParameter = CParameter.from_json(json)

        self.assertEqual(from_json, parameters[0])

    def test_compare(self) -> None:
        message: CParameter = CParameter(
            name="message",
            type=CType("String", "System"),
            has_default=False,
            is_out=False,
        )
        param_name: CParameter = CParameter(
            name="paramName",
            type=CType("String", "System"),
            has_default=False,
            is_out=False,
        )
        inner_exception: CParameter = CParameter(
            name="innerException",
            type=CType("Exception", "System"),
            has_default=False,
            is_out=False,
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

    def test_compare_other_attributes(self) -> None:
        params0: Sequence[CParameter]
        params1: Sequence[CParameter]

        with self.subTest("name"):
            params0 = [
                CParameter(
                    name="params0",
                    type=CType("String", "System"),
                    has_default=False,
                    is_out=False,
                )
            ]
            params1 = [
                CParameter(
                    name="params1",
                    type=CType("String", "System"),
                    has_default=False,
                    is_out=False,
                )
            ]

            self.assertEqual(CParameter.compare(params0, params1), 0)

        with self.subTest("has_default"):
            params0 = [
                CParameter(
                    name="name",
                    type=CType("String", "System"),
                    has_default=True,
                    is_out=False,
                )
            ]
            params1 = [
                CParameter(
                    name="name",
                    type=CType("String", "System"),
                    has_default=False,
                    is_out=False,
                )
            ]

            self.assertEqual(CParameter.compare(params0, params1), 0)

        with self.subTest("has_default"):
            params0 = [
                CParameter(
                    name="name",
                    type=CType("String", "System"),
                    has_default=False,
                    is_out=True,
                )
            ]
            params1 = [
                CParameter(
                    name="name",
                    type=CType("String", "System"),
                    has_default=False,
                    is_out=False,
                )
            ]

            self.assertEqual(CParameter.compare(params0, params1), 0)


class TestCField(unittest.TestCase):
    def assertCField(
        self, field: CField, name: str, declaring_type: CType, returns: CType, static: bool
    ) -> None:
        self.assertIsNotNone(field)
        self.assertIsInstance(field, CField)
        self.assertEqual(field.name, name)
        self.assertEqual(field.declaring_type, declaring_type)
        self.assertEqual(field.returns, returns)
        self.assertEqual(field.static, static)

    def test_from_info(self) -> None:
        type_info: TypeInfo = clr.GetClrType(Math)
        field_info: FieldInfo = type_info.GetField("E")
        c_type: CType = CType.from_info(type_info)
        c_field: CField = CField.from_info(field_info)

        self.assertCField(
            field=c_field,
            name="E",
            declaring_type=c_type,
            returns=CType.from_info(clr.GetClrType(Double)),
            static=True,
        )

    def test_json(self) -> None:
        type_info: TypeInfo = clr.GetClrType(Math)
        field_info: FieldInfo = type_info.GetField("PI")
        c_field: CField = CField.from_info(field_info)
        json: JsonType = c_field.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            json,
            {
                "name": "PI",
                "declaring_type": "System.Math",
                "returns": "System.Double",
                "static": True,
            },
        )

        from_json: CField = CField.from_json(json)

        self.assertEqual(from_json, c_field)

    def test_compare(self) -> None:
        type_info: TypeInfo = clr.GetClrType(Double)
        field0: CField = CField.from_info(type_info.GetField("Epsilon"))
        field1: CField = CField.from_info(type_info.GetField("MaxValue"))
        field2: CField = CField.from_info(type_info.GetField("NaN"))
        field3: CField = CField.from_info(type_info.GetField("MinValue"))

        self.assertLess(field0, field1)
        self.assertLessEqual(field0, field1)
        self.assertLessEqual(field0, field0)
        self.assertGreater(field2, field3)
        self.assertGreaterEqual(field2, field3)
        self.assertGreaterEqual(field2, field2)

    def test_sorted(self) -> None:
        type_info: TypeInfo = clr.GetClrType(Double)

        ordered: Sequence[CField] = (
            CField.from_info(type_info.GetField("Epsilon")),
            CField.from_info(type_info.GetField("MaxValue")),
            CField.from_info(type_info.GetField("MinValue")),
            CField.from_info(type_info.GetField("NaN")),
            CField.from_info(type_info.GetField("NegativeInfinity")),
            CField.from_info(type_info.GetField("PositiveInfinity")),
        )
        unordered: MutableSequence[CField] = list(ordered)
        random.shuffle(unordered)

        self.assertSequenceEqual(sorted(unordered), ordered)

    def test_get(self) -> None:
        type_info: TypeInfo = clr.GetClrType(TimeSpan)
        fields: Sequence[CField] = CField.get(type_info)
        manual_fields: Sequence[CField] = sorted(
            (
                CField.from_info(type_info.GetField("MaxValue")),
                CField.from_info(type_info.GetField("MinValue")),
                CField.from_info(type_info.GetField("TicksPerDay")),
                CField.from_info(type_info.GetField("TicksPerHour")),
                CField.from_info(type_info.GetField("TicksPerMillisecond")),
                CField.from_info(type_info.GetField("TicksPerMinute")),
                CField.from_info(type_info.GetField("TicksPerSecond")),
                CField.from_info(type_info.GetField("Zero")),
            )
        )

        self.assertIsNotNone(fields)
        self.assertIsInstance(fields, Sequence)
        self.assertSequenceEqual(fields, manual_fields)


class TestCConstructor(unittest.TestCase):
    def assertCConstructor(
        self, constructor: CConstructor, declaring_type: CType, parameters: Sequence[CParameter]
    ) -> None:
        self.assertIsNotNone(constructor)
        self.assertIsInstance(constructor, CConstructor)
        self.assertEqual(constructor.declaring_type, declaring_type)
        self.assertSequenceEqual(constructor.parameters, parameters)

    def test_from_info(self) -> None:
        type_info: TypeInfo = clr.GetClrType(ArgumentException)
        c_type: CType = CType.from_info(type_info)
        constructors: Sequence[CConstructor] = list(
            map(CConstructor.from_info, type_info.GetConstructors())
        )

        self.assertCConstructor(
            constructor=constructors[0],
            declaring_type=c_type,
            parameters=(),
        )
        self.assertCConstructor(
            constructor=constructors[1],
            declaring_type=c_type,
            parameters=(CParameter("message", CType("String", "System"), False, False),),
        )
        self.assertCConstructor(
            constructor=constructors[2],
            declaring_type=c_type,
            parameters=(
                CParameter("message", CType("String", "System"), False, False),
                CParameter("innerException", CType("Exception", "System"), False, False),
            ),
        )
        self.assertCConstructor(
            constructor=constructors[3],
            declaring_type=c_type,
            parameters=(
                CParameter("message", CType("String", "System"), False, False),
                CParameter("paramName", CType("String", "System"), False, False),
                CParameter("innerException", CType("Exception", "System"), False, False),
            ),
        )
        self.assertCConstructor(
            constructor=constructors[4],
            declaring_type=c_type,
            parameters=(
                CParameter("message", CType("String", "System"), False, False),
                CParameter("paramName", CType("String", "System"), False, False),
            ),
        )

    def test_json(self) -> None:
        type_info: TypeInfo = clr.GetClrType(ArgumentException)
        constructors: Sequence[CConstructor] = list(
            map(CConstructor.from_info, type_info.GetConstructors())
        )
        json: JsonType = constructors[3].to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            json,
            {
                "declaring_type": "System.ArgumentException",
                "parameters": (
                    {
                        "name": "message",
                        "type": "System.String",
                        "has_default": False,
                        "is_out": False,
                    },
                    {
                        "name": "paramName",
                        "type": "System.String",
                        "has_default": False,
                        "is_out": False,
                    },
                    {
                        "name": "innerException",
                        "type": "System.Exception",
                        "has_default": False,
                        "is_out": False,
                    },
                ),
            },
        )

        from_json: CConstructor = CConstructor.from_json(json)

        self.assertEqual(from_json, constructors[3])

    def test_compare(self) -> None:
        type_info: TypeInfo = clr.GetClrType(ArgumentException)
        constructors: Sequence[CConstructor] = list(
            map(CConstructor.from_info, type_info.GetConstructors())
        )

        ctor0: CConstructor = constructors[0]
        ctor1: CConstructor = constructors[1]
        ctor2: CConstructor = constructors[2]
        ctor3: CConstructor = constructors[4]
        ctor4: CConstructor = constructors[3]

        self.assertLess(ctor0, ctor1)
        self.assertLess(ctor1, ctor2)
        self.assertLess(ctor2, ctor3)
        self.assertLess(ctor3, ctor4)

        self.assertLessEqual(ctor0, ctor1)
        self.assertLessEqual(ctor1, ctor2)
        self.assertLessEqual(ctor2, ctor3)
        self.assertLessEqual(ctor3, ctor4)

        self.assertLessEqual(ctor0, ctor0)
        self.assertLessEqual(ctor1, ctor1)
        self.assertLessEqual(ctor2, ctor2)
        self.assertLessEqual(ctor3, ctor3)
        self.assertLessEqual(ctor4, ctor4)

        self.assertGreater(ctor1, ctor0)
        self.assertGreater(ctor2, ctor1)
        self.assertGreater(ctor3, ctor2)
        self.assertGreater(ctor4, ctor3)

        self.assertGreaterEqual(ctor1, ctor0)
        self.assertGreaterEqual(ctor2, ctor1)
        self.assertGreaterEqual(ctor3, ctor2)
        self.assertGreaterEqual(ctor4, ctor3)

        self.assertGreaterEqual(ctor0, ctor0)
        self.assertGreaterEqual(ctor1, ctor1)
        self.assertGreaterEqual(ctor2, ctor2)
        self.assertGreaterEqual(ctor3, ctor3)
        self.assertGreaterEqual(ctor4, ctor4)

    def test_sorted(self) -> None:
        type_info: TypeInfo = clr.GetClrType(ArgumentException)
        constructors: Sequence[CConstructor] = list(
            map(CConstructor.from_info, type_info.GetConstructors())
        )

        ordered: Sequence[CConstructor] = (
            constructors[0],
            constructors[1],
            constructors[2],
            constructors[4],
            constructors[3],
        )
        unordered: MutableSequence[CConstructor] = list(ordered)
        random.shuffle(unordered)

        self.assertSequenceEqual(sorted(unordered), ordered)

    def test_get(self) -> None:
        type_info: TypeInfo = clr.GetClrType(ArgumentException)
        constructors: Sequence[CConstructor] = CConstructor.get(type_info)
        manual_constructors: Sequence[CConstructor] = sorted(
            map(CConstructor.from_info, type_info.GetConstructors())
        )

        self.assertIsNotNone(constructors)
        self.assertIsInstance(constructors, Sequence)
        self.assertSequenceEqual(constructors, manual_constructors)


class TestCProperty(unittest.TestCase):
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
        self.assertEqual(property.name, name)
        self.assertEqual(property.declaring_type, declaring_type)
        self.assertEqual(property.type, type)
        self.assertEqual(property.setter, setter)
        self.assertEqual(property.static, static)

    def test_from_info(self) -> None:
        type_info: TypeInfo = clr.GetClrType(TimeZone)
        c_type: CType = CType.from_info(type_info)

        property_info: PropertyInfo = type_info.GetProperty("CurrentTimeZone")
        c_property: CProperty = CProperty.from_info(property_info)

        self.assertCProperty(
            property=c_property,
            name="CurrentTimeZone",
            declaring_type=c_type,
            type=CType.from_info(clr.GetClrType(TimeZone)),
            setter=False,
            static=True,
        )

        property_info: PropertyInfo = type_info.GetProperty("DaylightName")
        c_property: CProperty = CProperty.from_info(property_info)

        self.assertCProperty(
            property=c_property,
            name="DaylightName",
            declaring_type=c_type,
            type=CType.from_info(clr.GetClrType(String)),
            setter=False,
            static=False,
        )

        property_info: PropertyInfo = type_info.GetProperty("StandardName")
        c_property: CProperty = CProperty.from_info(property_info)

        self.assertCProperty(
            property=c_property,
            name="StandardName",
            declaring_type=c_type,
            type=CType.from_info(clr.GetClrType(String)),
            setter=False,
            static=False,
        )

    def test_json(self) -> None:
        type_info: TypeInfo = clr.GetClrType(UriBuilder)
        property_info: PropertyInfo = type_info.GetProperty("Fragment")
        c_property: CProperty = CProperty.from_info(property_info)
        json: JsonType = c_property.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            json,
            {
                "name": "Fragment",
                "declaring_type": "System.UriBuilder",
                "type": "System.String",
                "setter": True,
                "static": False,
            },
        )

        from_json: CProperty = CProperty.from_json(json)

        self.assertEqual(from_json, c_property)

    def test_compare(self) -> None:
        type_info: TypeInfo = clr.GetClrType(UriBuilder)
        prop0: CProperty = CProperty.from_info(type_info.GetProperty("Fragment"))
        prop1: CProperty = CProperty.from_info(type_info.GetProperty("Host"))
        prop2: CProperty = CProperty.from_info(type_info.GetProperty("Password"))
        prop3: CProperty = CProperty.from_info(type_info.GetProperty("Path"))
        prop4: CProperty = CProperty.from_info(type_info.GetProperty("Port"))

        self.assertLess(prop0, prop1)
        self.assertLess(prop1, prop2)
        self.assertLess(prop2, prop3)
        self.assertLess(prop3, prop4)

        self.assertLessEqual(prop0, prop1)
        self.assertLessEqual(prop1, prop2)
        self.assertLessEqual(prop2, prop3)
        self.assertLessEqual(prop3, prop4)

        self.assertLessEqual(prop0, prop0)
        self.assertLessEqual(prop1, prop1)
        self.assertLessEqual(prop2, prop2)
        self.assertLessEqual(prop3, prop3)
        self.assertLessEqual(prop4, prop4)

        self.assertGreater(prop1, prop0)
        self.assertGreater(prop2, prop1)
        self.assertGreater(prop3, prop2)
        self.assertGreater(prop4, prop3)

        self.assertGreaterEqual(prop1, prop0)
        self.assertGreaterEqual(prop2, prop1)
        self.assertGreaterEqual(prop3, prop2)
        self.assertGreaterEqual(prop4, prop3)

        self.assertGreaterEqual(prop0, prop0)
        self.assertGreaterEqual(prop1, prop1)
        self.assertGreaterEqual(prop2, prop2)
        self.assertGreaterEqual(prop3, prop3)
        self.assertGreaterEqual(prop4, prop4)

    def test_sorted(self) -> None:
        type_info: TypeInfo = clr.GetClrType(UriBuilder)

        ordered: Sequence[CProperty] = (
            CProperty.from_info(type_info.GetProperty("Fragment")),
            CProperty.from_info(type_info.GetProperty("Host")),
            CProperty.from_info(type_info.GetProperty("Password")),
            CProperty.from_info(type_info.GetProperty("Path")),
            CProperty.from_info(type_info.GetProperty("Port")),
        )
        unordered: MutableSequence[CProperty] = list(ordered)
        random.shuffle(unordered)

        self.assertSequenceEqual(sorted(unordered), ordered)

    def test_get(self) -> None:
        type_info: TypeInfo = clr.GetClrType(UriBuilder)
        properties: Sequence[CProperty] = CProperty.get(type_info)
        manual_properties: Sequence[CProperty] = sorted(
            (
                CProperty.from_info(type_info.GetProperty("Fragment")),
                CProperty.from_info(type_info.GetProperty("Host")),
                CProperty.from_info(type_info.GetProperty("Password")),
                CProperty.from_info(type_info.GetProperty("Path")),
                CProperty.from_info(type_info.GetProperty("Port")),
                CProperty.from_info(type_info.GetProperty("Query")),
                CProperty.from_info(type_info.GetProperty("Scheme")),
                CProperty.from_info(type_info.GetProperty("Uri")),
                CProperty.from_info(type_info.GetProperty("UserName")),
            )
        )

        self.assertIsNotNone(properties)
        self.assertIsInstance(properties, Sequence)
        self.assertSequenceEqual(properties, manual_properties)


class TestCMethod(unittest.TestCase):
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
        self.assertEqual(method.name, name)
        self.assertEqual(method.declaring_type, declaring_type)
        self.assertSequenceEqual(method.parameters, parameters)
        self.assertSequenceEqual(method.returns, returns)
        self.assertEqual(method.static, static)

    def test_from_info(self) -> None:
        type_info: TypeInfo = clr.GetClrType(Object)
        c_type: CType = CType.from_info(type_info)

        method_info: MethodInfo = type_info.GetMethod("GetHashCode")
        c_method: CMethod = CMethod.from_info(method_info)

        self.assertCMethod(
            method=c_method,
            name="GetHashCode",
            declaring_type=c_type,
            parameters=(),
            returns=(CType("Int32", "System"),),
            static=False,
        )

        method_info: PropertyInfo = type_info.GetMethod("ReferenceEquals")
        c_method: CMethod = CMethod.from_info(method_info)

        self.assertCMethod(
            method=c_method,
            name="ReferenceEquals",
            declaring_type=c_type,
            parameters=(
                CParameter("objA", CType("Object", "System"), False, False),
                CParameter("objB", CType("Object", "System"), False, False),
            ),
            returns=(CType("Boolean", "System"),),
            static=True,
        )

    def test_json(self) -> None:
        type_info: TypeInfo = clr.GetClrType(Object)
        method_info: MethodInfo = type_info.GetMethod("GetType")
        c_method: CMethod = CMethod.from_info(method_info)
        json: JsonType = c_method.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            json,
            {
                "name": "GetType",
                "declaring_type": "System.Object",
                "parameters": (),
                "returns": ("System.Type",),
                "static": False,
            },
        )

        from_json: CMethod = CMethod.from_json(json)

        self.assertEqual(from_json, c_method)

    def test_compare(self) -> None:
        type_info: TypeInfo = clr.GetClrType(Object)
        method0: CMethod = CMethod.from_info(type_info.GetMethod("Equals", Array[Type]([Object])))
        method1: CMethod = CMethod.from_info(
            type_info.GetMethod("Equals", Array[Type]([Object, Object]))
        )
        method2: CMethod = CMethod.from_info(type_info.GetMethod("GetHashCode"))
        method3: CMethod = CMethod.from_info(type_info.GetMethod("GetType"))
        method4: CMethod = CMethod.from_info(type_info.GetMethod("ReferenceEquals"))
        method5: CMethod = CMethod.from_info(type_info.GetMethod("ToString"))

        self.assertLess(method0, method1)
        self.assertLess(method1, method2)
        self.assertLess(method2, method3)
        self.assertLess(method3, method4)
        self.assertLess(method4, method5)

        self.assertLessEqual(method0, method1)
        self.assertLessEqual(method1, method2)
        self.assertLessEqual(method2, method3)
        self.assertLessEqual(method3, method4)
        self.assertLessEqual(method4, method5)

        self.assertLessEqual(method0, method0)
        self.assertLessEqual(method1, method1)
        self.assertLessEqual(method2, method2)
        self.assertLessEqual(method3, method3)
        self.assertLessEqual(method4, method4)
        self.assertLessEqual(method5, method5)

        self.assertGreater(method1, method0)
        self.assertGreater(method2, method1)
        self.assertGreater(method3, method2)
        self.assertGreater(method4, method3)
        self.assertGreater(method5, method4)

        self.assertGreaterEqual(method1, method0)
        self.assertGreaterEqual(method2, method1)
        self.assertGreaterEqual(method3, method2)
        self.assertGreaterEqual(method4, method3)
        self.assertGreaterEqual(method5, method4)

        self.assertGreaterEqual(method0, method0)
        self.assertGreaterEqual(method1, method1)
        self.assertGreaterEqual(method2, method2)
        self.assertGreaterEqual(method3, method3)
        self.assertGreaterEqual(method4, method4)
        self.assertGreaterEqual(method5, method5)

    def test_sorted(self) -> None:
        type_info: TypeInfo = clr.GetClrType(Object)

        ordered: Sequence[CMethod] = (
            CMethod.from_info(type_info.GetMethod("Equals", Array[Type]([Object]))),
            CMethod.from_info(type_info.GetMethod("Equals", Array[Type]([Object, Object]))),
            CMethod.from_info(type_info.GetMethod("GetHashCode")),
            CMethod.from_info(type_info.GetMethod("GetType")),
            CMethod.from_info(type_info.GetMethod("ReferenceEquals")),
            CMethod.from_info(type_info.GetMethod("ToString")),
        )
        unordered: MutableSequence[CMethod] = list(ordered)
        random.shuffle(unordered)

        self.assertSequenceEqual(sorted(unordered), ordered)

    def test_get(self) -> None:
        type_info: TypeInfo = clr.GetClrType(Object)
        methods: Sequence[CMethod] = CMethod.get(type_info)
        manual_methods: Sequence[CMethod] = sorted(
            (
                CMethod.from_info(type_info.GetMethod("Equals", Array[Type]([Object]))),
                CMethod.from_info(type_info.GetMethod("Equals", Array[Type]([Object, Object]))),
                CMethod.from_info(type_info.GetMethod("GetHashCode")),
                CMethod.from_info(type_info.GetMethod("GetType")),
                CMethod.from_info(type_info.GetMethod("ReferenceEquals")),
                CMethod.from_info(type_info.GetMethod("ToString")),
            )
        )

        self.assertIsNotNone(methods)
        self.assertIsInstance(methods, Sequence)
        self.assertSequenceEqual(methods, manual_methods)


class TestCEvent(unittest.TestCase):
    def assertCEvent(self, event: CEvent, name: str, declaring_type: CType, type: CType) -> None:
        self.assertIsNotNone(event)
        self.assertIsInstance(event, CEvent)
        self.assertEqual(event.name, name)
        self.assertEqual(event.declaring_type, declaring_type)
        self.assertEqual(event.type, type)

    def test_from_info(self) -> None:
        type_info: TypeInfo = clr.GetClrType(WebClient)
        c_type: CType = CType.from_info(type_info)

        event_info: EventInfo = type_info.GetEvent("DownloadDataCompleted")
        c_event: CEvent = CEvent.from_info(event_info)

        self.assertCEvent(
            event=c_event,
            name="DownloadDataCompleted",
            declaring_type=c_type,
            type=CType.from_info(clr.GetClrType(DownloadDataCompletedEventHandler)),
        )

    def test_json(self) -> None:
        type_info: TypeInfo = clr.GetClrType(WebClient)
        event_info: EventInfo = type_info.GetEvent("DownloadFileCompleted")
        c_event: CEvent = CEvent.from_info(event_info)
        json: JsonType = c_event.to_json()

        self.assertIsNotNone(json)
        self.assertIsInstance(json, dict)
        self.assertDictEqual(
            json,
            {
                "name": "DownloadFileCompleted",
                "declaring_type": "System.Net.WebClient",
                "type": "System.ComponentModel.AsyncCompletedEventHandler",
            },
        )

        from_json: CEvent = CEvent.from_json(json)

        self.assertEqual(from_json, c_event)

    def test_compare(self) -> None:
        type_info: TypeInfo = clr.GetClrType(WebClient)
        event0: CEvent = CEvent.from_info(type_info.GetEvent("DownloadDataCompleted"))
        event1: CEvent = CEvent.from_info(type_info.GetEvent("DownloadFileCompleted"))
        event2: CEvent = CEvent.from_info(type_info.GetEvent("DownloadProgressChanged"))
        event3: CEvent = CEvent.from_info(type_info.GetEvent("DownloadStringCompleted"))
        event4: CEvent = CEvent.from_info(type_info.GetEvent("OpenReadCompleted"))
        event5: CEvent = CEvent.from_info(type_info.GetEvent("OpenWriteCompleted"))

        self.assertLess(event0, event1)
        self.assertLess(event1, event2)
        self.assertLess(event2, event3)
        self.assertLess(event3, event4)
        self.assertLess(event4, event5)

        self.assertLessEqual(event0, event1)
        self.assertLessEqual(event1, event2)
        self.assertLessEqual(event2, event3)
        self.assertLessEqual(event3, event4)
        self.assertLessEqual(event4, event5)

        self.assertLessEqual(event0, event0)
        self.assertLessEqual(event1, event1)
        self.assertLessEqual(event2, event2)
        self.assertLessEqual(event3, event3)
        self.assertLessEqual(event4, event4)
        self.assertLessEqual(event5, event5)

        self.assertGreater(event1, event0)
        self.assertGreater(event2, event1)
        self.assertGreater(event3, event2)
        self.assertGreater(event4, event3)
        self.assertGreater(event5, event4)

        self.assertGreaterEqual(event1, event0)
        self.assertGreaterEqual(event2, event1)
        self.assertGreaterEqual(event3, event2)
        self.assertGreaterEqual(event4, event3)
        self.assertGreaterEqual(event5, event4)

        self.assertGreaterEqual(event0, event0)
        self.assertGreaterEqual(event1, event1)
        self.assertGreaterEqual(event2, event2)
        self.assertGreaterEqual(event3, event3)
        self.assertGreaterEqual(event4, event4)
        self.assertGreaterEqual(event5, event5)

    def test_sorted(self) -> None:
        type_info: TypeInfo = clr.GetClrType(WebClient)

        ordered: Sequence[CEvent] = (
            CEvent.from_info(type_info.GetEvent("DownloadDataCompleted")),
            CEvent.from_info(type_info.GetEvent("DownloadFileCompleted")),
            CEvent.from_info(type_info.GetEvent("DownloadProgressChanged")),
            CEvent.from_info(type_info.GetEvent("DownloadStringCompleted")),
            CEvent.from_info(type_info.GetEvent("OpenReadCompleted")),
            CEvent.from_info(type_info.GetEvent("OpenWriteCompleted")),
        )
        unordered: MutableSequence[CEvent] = list(ordered)
        random.shuffle(unordered)

        self.assertSequenceEqual(sorted(unordered), ordered)

    def test_get(self) -> None:
        type_info: TypeInfo = clr.GetClrType(WebClient)
        events: Sequence[CEvent] = CEvent.get(type_info)
        manual_events: Sequence[CEvent] = sorted(
            (
                CEvent(
                    "Disposed",
                    CType.from_info(clr.GetClrType(IComponent)),
                    CType.from_info(clr.GetClrType(EventHandler)),
                ),
                CEvent.from_info(type_info.GetEvent("DownloadDataCompleted")),
                CEvent.from_info(type_info.GetEvent("DownloadFileCompleted")),
                CEvent.from_info(type_info.GetEvent("DownloadProgressChanged")),
                CEvent.from_info(type_info.GetEvent("DownloadStringCompleted")),
                CEvent.from_info(type_info.GetEvent("OpenReadCompleted")),
                CEvent.from_info(type_info.GetEvent("OpenWriteCompleted")),
                CEvent.from_info(type_info.GetEvent("UploadDataCompleted")),
                CEvent.from_info(type_info.GetEvent("UploadFileCompleted")),
                CEvent.from_info(type_info.GetEvent("UploadProgressChanged")),
                CEvent.from_info(type_info.GetEvent("UploadStringCompleted")),
                CEvent.from_info(type_info.GetEvent("UploadValuesCompleted")),
                CEvent.from_info(type_info.GetEvent("WriteStreamClosed")),
            )
        )

        self.assertIsNotNone(events)
        self.assertIsInstance(events, Sequence)
        self.assertSequenceEqual(events, manual_events)


if __name__ == "__main__":
    unittest.main()
