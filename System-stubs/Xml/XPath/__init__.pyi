from __future__ import annotations

from abc import ABC
from typing import List, Protocol, Union, overload

from System import Array, Boolean, Byte, DateTime, Double, Enum, Exception, ICloneable, IDisposable, Int32, Int64, Object, String, SystemException, Type, Void
from System.Collections import IComparer, IEnumerable, IEnumerator, IEqualityComparer
from System.Collections.Generic import IDictionary
from System.IO import Stream, TextReader
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import ISerializable, SerializationInfo, StreamingContext
from System.Xml import IXmlNamespaceResolver, ReadState, XmlNameTable, XmlNamespaceManager, XmlNamespaceScope, XmlNodeOrder, XmlNodeType, XmlReader, XmlReaderSettings, XmlSpace, XmlWriter
from System.Xml.Schema import IXmlSchemaInfo, ValidationEventHandler, XmlSchemaAttribute, XmlSchemaElement, XmlSchemaSet, XmlSchemaSimpleType, XmlSchemaType, XmlSchemaValidity

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
DoubleType = Union[float, Double]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class XPathDocument(ObjectType, IXPathNavigable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, reader: XmlReader): ...
    
    @overload
    def __init__(self, reader: XmlReader, space: XmlSpace): ...
    
    @overload
    def __init__(self, textReader: TextReader): ...
    
    @overload
    def __init__(self, stream: Stream): ...
    
    @overload
    def __init__(self, uri: StringType): ...
    
    @overload
    def __init__(self, uri: StringType, space: XmlSpace): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CreateNavigator(self) -> XPathNavigator: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathDocument(ObjectType, IXPathNavigable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, reader: XmlReader): ...
    
    @overload
    def __init__(self, reader: XmlReader, space: XmlSpace): ...
    
    @overload
    def __init__(self, textReader: TextReader): ...
    
    @overload
    def __init__(self, stream: Stream): ...
    
    @overload
    def __init__(self, uri: StringType): ...
    
    @overload
    def __init__(self, uri: StringType, space: XmlSpace): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CreateNavigator(self) -> XPathNavigator: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Message(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def get_Message(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Message(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def get_Message(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathExpression(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Expression(self) -> StringType: ...
    
    @property
    def ReturnType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def AddSort(self, expr: ObjectType, comparer: IComparer) -> VoidType: ...
    
    @overload
    def AddSort(self, expr: ObjectType, order: XmlSortOrder, caseOrder: XmlCaseOrder, lang: StringType, dataType: XmlDataType) -> VoidType: ...
    
    def Clone(self) -> XPathExpression: ...
    
    @staticmethod
    @overload
    def Compile(xpath: StringType) -> XPathExpression: ...
    
    @staticmethod
    @overload
    def Compile(xpath: StringType, nsResolver: IXmlNamespaceResolver) -> XPathExpression: ...
    
    @overload
    def SetContext(self, nsManager: XmlNamespaceManager) -> VoidType: ...
    
    @overload
    def SetContext(self, nsResolver: IXmlNamespaceResolver) -> VoidType: ...
    
    def get_Expression(self) -> StringType: ...
    
    def get_ReturnType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathExpression(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Expression(self) -> StringType: ...
    
    @property
    def ReturnType(self) -> XPathResultType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def AddSort(self, expr: ObjectType, comparer: IComparer) -> VoidType: ...
    
    @overload
    def AddSort(self, expr: ObjectType, order: XmlSortOrder, caseOrder: XmlCaseOrder, lang: StringType, dataType: XmlDataType) -> VoidType: ...
    
    def Clone(self) -> XPathExpression: ...
    
    @staticmethod
    @overload
    def Compile(xpath: StringType) -> XPathExpression: ...
    
    @staticmethod
    @overload
    def Compile(xpath: StringType, nsResolver: IXmlNamespaceResolver) -> XPathExpression: ...
    
    @overload
    def SetContext(self, nsManager: XmlNamespaceManager) -> VoidType: ...
    
    @overload
    def SetContext(self, nsResolver: IXmlNamespaceResolver) -> VoidType: ...
    
    def get_Expression(self) -> StringType: ...
    
    def get_ReturnType(self) -> XPathResultType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathItem(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsNode(self) -> BooleanType: ...
    
    @property
    def TypedValue(self) -> ObjectType: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def ValueAsBoolean(self) -> BooleanType: ...
    
    @property
    def ValueAsDateTime(self) -> DateTime: ...
    
    @property
    def ValueAsDouble(self) -> DoubleType: ...
    
    @property
    def ValueAsInt(self) -> IntType: ...
    
    @property
    def ValueAsLong(self) -> LongType: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    @property
    def XmlType(self) -> XmlSchemaType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def ValueAs(self, returnType: TypeType) -> ObjectType: ...
    
    @overload
    def ValueAs(self, returnType: TypeType, nsResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    def get_IsNode(self) -> BooleanType: ...
    
    def get_TypedValue(self) -> ObjectType: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_ValueAsBoolean(self) -> BooleanType: ...
    
    def get_ValueAsDateTime(self) -> DateTime: ...
    
    def get_ValueAsDouble(self) -> DoubleType: ...
    
    def get_ValueAsInt(self) -> IntType: ...
    
    def get_ValueAsLong(self) -> LongType: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    def get_XmlType(self) -> XmlSchemaType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathItem(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsNode(self) -> BooleanType: ...
    
    @property
    def TypedValue(self) -> ObjectType: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def ValueAsBoolean(self) -> BooleanType: ...
    
    @property
    def ValueAsDateTime(self) -> DateTime: ...
    
    @property
    def ValueAsDouble(self) -> DoubleType: ...
    
    @property
    def ValueAsInt(self) -> IntType: ...
    
    @property
    def ValueAsLong(self) -> LongType: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    @property
    def XmlType(self) -> XmlSchemaType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def ValueAs(self, returnType: TypeType) -> ObjectType: ...
    
    @overload
    def ValueAs(self, returnType: TypeType, nsResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    def get_IsNode(self) -> BooleanType: ...
    
    def get_TypedValue(self) -> ObjectType: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_ValueAsBoolean(self) -> BooleanType: ...
    
    def get_ValueAsDateTime(self) -> DateTime: ...
    
    def get_ValueAsDouble(self) -> DoubleType: ...
    
    def get_ValueAsInt(self) -> IntType: ...
    
    def get_ValueAsLong(self) -> LongType: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    def get_XmlType(self) -> XmlSchemaType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathNavigator(ABC, XPathItem, ICloneable, IXPathNavigable, IXmlNamespaceResolver):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def CanEdit(self) -> BooleanType: ...
    
    @property
    def HasAttributes(self) -> BooleanType: ...
    
    @property
    def HasChildren(self) -> BooleanType: ...
    
    @property
    def InnerXml(self) -> StringType: ...
    
    @InnerXml.setter
    def InnerXml(self, value: StringType) -> None: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    @property
    def IsNode(self) -> BooleanType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @staticmethod
    @property
    def NavigatorComparer() -> IEqualityComparer: ...
    
    @property
    def NodeType(self) -> XPathNodeType: ...
    
    @property
    def OuterXml(self) -> StringType: ...
    
    @OuterXml.setter
    def OuterXml(self, value: StringType) -> None: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    @property
    def TypedValue(self) -> ObjectType: ...
    
    @property
    def UnderlyingObject(self) -> ObjectType: ...
    
    @property
    def ValueAsBoolean(self) -> BooleanType: ...
    
    @property
    def ValueAsDateTime(self) -> DateTime: ...
    
    @property
    def ValueAsDouble(self) -> DoubleType: ...
    
    @property
    def ValueAsInt(self) -> IntType: ...
    
    @property
    def ValueAsLong(self) -> LongType: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlType(self) -> XmlSchemaType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def AppendChild(self) -> XmlWriter: ...
    
    @overload
    def AppendChild(self, newChild: StringType) -> VoidType: ...
    
    @overload
    def AppendChild(self, newChild: XmlReader) -> VoidType: ...
    
    @overload
    def AppendChild(self, newChild: XPathNavigator) -> VoidType: ...
    
    def AppendChildElement(self, prefix: StringType, localName: StringType, namespaceURI: StringType, value: StringType) -> VoidType: ...
    
    def CheckValidity(self, schemas: XmlSchemaSet, validationEventHandler: ValidationEventHandler) -> BooleanType: ...
    
    def Clone(self) -> XPathNavigator: ...
    
    def ComparePosition(self, nav: XPathNavigator) -> XmlNodeOrder: ...
    
    def Compile(self, xpath: StringType) -> XPathExpression: ...
    
    def CreateAttribute(self, prefix: StringType, localName: StringType, namespaceURI: StringType, value: StringType) -> VoidType: ...
    
    def CreateAttributes(self) -> XmlWriter: ...
    
    def CreateNavigator(self) -> XPathNavigator: ...
    
    def DeleteRange(self, lastSiblingToDelete: XPathNavigator) -> VoidType: ...
    
    def DeleteSelf(self) -> VoidType: ...
    
    @overload
    def Evaluate(self, xpath: StringType) -> ObjectType: ...
    
    @overload
    def Evaluate(self, xpath: StringType, resolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    @overload
    def Evaluate(self, expr: XPathExpression) -> ObjectType: ...
    
    @overload
    def Evaluate(self, expr: XPathExpression, context: XPathNodeIterator) -> ObjectType: ...
    
    def GetAttribute(self, localName: StringType, namespaceURI: StringType) -> StringType: ...
    
    def GetNamespace(self, name: StringType) -> StringType: ...
    
    def GetNamespacesInScope(self, scope: XmlNamespaceScope) -> IDictionary[StringType, StringType]: ...
    
    @overload
    def InsertAfter(self) -> XmlWriter: ...
    
    @overload
    def InsertAfter(self, newSibling: StringType) -> VoidType: ...
    
    @overload
    def InsertAfter(self, newSibling: XmlReader) -> VoidType: ...
    
    @overload
    def InsertAfter(self, newSibling: XPathNavigator) -> VoidType: ...
    
    @overload
    def InsertBefore(self) -> XmlWriter: ...
    
    @overload
    def InsertBefore(self, newSibling: StringType) -> VoidType: ...
    
    @overload
    def InsertBefore(self, newSibling: XmlReader) -> VoidType: ...
    
    @overload
    def InsertBefore(self, newSibling: XPathNavigator) -> VoidType: ...
    
    def InsertElementAfter(self, prefix: StringType, localName: StringType, namespaceURI: StringType, value: StringType) -> VoidType: ...
    
    def InsertElementBefore(self, prefix: StringType, localName: StringType, namespaceURI: StringType, value: StringType) -> VoidType: ...
    
    def IsDescendant(self, nav: XPathNavigator) -> BooleanType: ...
    
    def IsSamePosition(self, other: XPathNavigator) -> BooleanType: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    def LookupPrefix(self, namespaceURI: StringType) -> StringType: ...
    
    @overload
    def Matches(self, expr: XPathExpression) -> BooleanType: ...
    
    @overload
    def Matches(self, xpath: StringType) -> BooleanType: ...
    
    def MoveTo(self, other: XPathNavigator) -> BooleanType: ...
    
    def MoveToAttribute(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def MoveToChild(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def MoveToChild(self, type: XPathNodeType) -> BooleanType: ...
    
    def MoveToFirst(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToFirstChild(self) -> BooleanType: ...
    
    @overload
    def MoveToFirstNamespace(self) -> BooleanType: ...
    
    @overload
    def MoveToFirstNamespace(self, namespaceScope: XPathNamespaceScope) -> BooleanType: ...
    
    @overload
    def MoveToFollowing(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def MoveToFollowing(self, localName: StringType, namespaceURI: StringType, end: XPathNavigator) -> BooleanType: ...
    
    @overload
    def MoveToFollowing(self, type: XPathNodeType) -> BooleanType: ...
    
    @overload
    def MoveToFollowing(self, type: XPathNodeType, end: XPathNavigator) -> BooleanType: ...
    
    def MoveToId(self, id: StringType) -> BooleanType: ...
    
    def MoveToNamespace(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToNext(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def MoveToNext(self, type: XPathNodeType) -> BooleanType: ...
    
    @overload
    def MoveToNext(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    @overload
    def MoveToNextNamespace(self) -> BooleanType: ...
    
    @overload
    def MoveToNextNamespace(self, namespaceScope: XPathNamespaceScope) -> BooleanType: ...
    
    def MoveToParent(self) -> BooleanType: ...
    
    def MoveToPrevious(self) -> BooleanType: ...
    
    def MoveToRoot(self) -> VoidType: ...
    
    @overload
    def PrependChild(self) -> XmlWriter: ...
    
    @overload
    def PrependChild(self, newChild: StringType) -> VoidType: ...
    
    @overload
    def PrependChild(self, newChild: XmlReader) -> VoidType: ...
    
    @overload
    def PrependChild(self, newChild: XPathNavigator) -> VoidType: ...
    
    def PrependChildElement(self, prefix: StringType, localName: StringType, namespaceURI: StringType, value: StringType) -> VoidType: ...
    
    def ReadSubtree(self) -> XmlReader: ...
    
    def ReplaceRange(self, lastSiblingToReplace: XPathNavigator) -> XmlWriter: ...
    
    @overload
    def ReplaceSelf(self, newNode: StringType) -> VoidType: ...
    
    @overload
    def ReplaceSelf(self, newNode: XmlReader) -> VoidType: ...
    
    @overload
    def ReplaceSelf(self, newNode: XPathNavigator) -> VoidType: ...
    
    @overload
    def Select(self, xpath: StringType) -> XPathNodeIterator: ...
    
    @overload
    def Select(self, xpath: StringType, resolver: IXmlNamespaceResolver) -> XPathNodeIterator: ...
    
    @overload
    def Select(self, expr: XPathExpression) -> XPathNodeIterator: ...
    
    @overload
    def SelectAncestors(self, type: XPathNodeType, matchSelf: BooleanType) -> XPathNodeIterator: ...
    
    @overload
    def SelectAncestors(self, name: StringType, namespaceURI: StringType, matchSelf: BooleanType) -> XPathNodeIterator: ...
    
    @overload
    def SelectChildren(self, type: XPathNodeType) -> XPathNodeIterator: ...
    
    @overload
    def SelectChildren(self, name: StringType, namespaceURI: StringType) -> XPathNodeIterator: ...
    
    @overload
    def SelectDescendants(self, type: XPathNodeType, matchSelf: BooleanType) -> XPathNodeIterator: ...
    
    @overload
    def SelectDescendants(self, name: StringType, namespaceURI: StringType, matchSelf: BooleanType) -> XPathNodeIterator: ...
    
    @overload
    def SelectSingleNode(self, xpath: StringType) -> XPathNavigator: ...
    
    @overload
    def SelectSingleNode(self, xpath: StringType, resolver: IXmlNamespaceResolver) -> XPathNavigator: ...
    
    @overload
    def SelectSingleNode(self, expression: XPathExpression) -> XPathNavigator: ...
    
    def SetTypedValue(self, typedValue: ObjectType) -> VoidType: ...
    
    def SetValue(self, value: StringType) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def ValueAs(self, returnType: TypeType, nsResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    def WriteSubtree(self, writer: XmlWriter) -> VoidType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_CanEdit(self) -> BooleanType: ...
    
    def get_HasAttributes(self) -> BooleanType: ...
    
    def get_HasChildren(self) -> BooleanType: ...
    
    def get_InnerXml(self) -> StringType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    def get_IsNode(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    @staticmethod
    def get_NavigatorComparer() -> IEqualityComparer: ...
    
    def get_NodeType(self) -> XPathNodeType: ...
    
    def get_OuterXml(self) -> StringType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    def get_TypedValue(self) -> ObjectType: ...
    
    def get_UnderlyingObject(self) -> ObjectType: ...
    
    def get_ValueAsBoolean(self) -> BooleanType: ...
    
    def get_ValueAsDateTime(self) -> DateTime: ...
    
    def get_ValueAsDouble(self) -> DoubleType: ...
    
    def get_ValueAsInt(self) -> IntType: ...
    
    def get_ValueAsLong(self) -> LongType: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlType(self) -> XmlSchemaType: ...
    
    def set_InnerXml(self, value: StringType) -> VoidType: ...
    
    def set_OuterXml(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathNavigator(ABC, XPathItem, ICloneable, IXPathNavigable, IXmlNamespaceResolver):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def CanEdit(self) -> BooleanType: ...
    
    @property
    def HasAttributes(self) -> BooleanType: ...
    
    @property
    def HasChildren(self) -> BooleanType: ...
    
    @property
    def InnerXml(self) -> StringType: ...
    
    @InnerXml.setter
    def InnerXml(self, value: StringType) -> None: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    @property
    def IsNode(self) -> BooleanType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @staticmethod
    @property
    def NavigatorComparer() -> IEqualityComparer: ...
    
    @property
    def NodeType(self) -> XPathNodeType: ...
    
    @property
    def OuterXml(self) -> StringType: ...
    
    @OuterXml.setter
    def OuterXml(self, value: StringType) -> None: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    @property
    def TypedValue(self) -> ObjectType: ...
    
    @property
    def UnderlyingObject(self) -> ObjectType: ...
    
    @property
    def ValueAsBoolean(self) -> BooleanType: ...
    
    @property
    def ValueAsDateTime(self) -> DateTime: ...
    
    @property
    def ValueAsDouble(self) -> DoubleType: ...
    
    @property
    def ValueAsInt(self) -> IntType: ...
    
    @property
    def ValueAsLong(self) -> LongType: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlType(self) -> XmlSchemaType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def AppendChild(self) -> XmlWriter: ...
    
    @overload
    def AppendChild(self, newChild: StringType) -> VoidType: ...
    
    @overload
    def AppendChild(self, newChild: XmlReader) -> VoidType: ...
    
    @overload
    def AppendChild(self, newChild: XPathNavigator) -> VoidType: ...
    
    def AppendChildElement(self, prefix: StringType, localName: StringType, namespaceURI: StringType, value: StringType) -> VoidType: ...
    
    def CheckValidity(self, schemas: XmlSchemaSet, validationEventHandler: ValidationEventHandler) -> BooleanType: ...
    
    def Clone(self) -> XPathNavigator: ...
    
    def ComparePosition(self, nav: XPathNavigator) -> XmlNodeOrder: ...
    
    def Compile(self, xpath: StringType) -> XPathExpression: ...
    
    def CreateAttribute(self, prefix: StringType, localName: StringType, namespaceURI: StringType, value: StringType) -> VoidType: ...
    
    def CreateAttributes(self) -> XmlWriter: ...
    
    def CreateNavigator(self) -> XPathNavigator: ...
    
    def DeleteRange(self, lastSiblingToDelete: XPathNavigator) -> VoidType: ...
    
    def DeleteSelf(self) -> VoidType: ...
    
    @overload
    def Evaluate(self, xpath: StringType) -> ObjectType: ...
    
    @overload
    def Evaluate(self, xpath: StringType, resolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    @overload
    def Evaluate(self, expr: XPathExpression) -> ObjectType: ...
    
    @overload
    def Evaluate(self, expr: XPathExpression, context: XPathNodeIterator) -> ObjectType: ...
    
    def GetAttribute(self, localName: StringType, namespaceURI: StringType) -> StringType: ...
    
    def GetNamespace(self, name: StringType) -> StringType: ...
    
    def GetNamespacesInScope(self, scope: XmlNamespaceScope) -> IDictionary[StringType, StringType]: ...
    
    @overload
    def InsertAfter(self) -> XmlWriter: ...
    
    @overload
    def InsertAfter(self, newSibling: StringType) -> VoidType: ...
    
    @overload
    def InsertAfter(self, newSibling: XmlReader) -> VoidType: ...
    
    @overload
    def InsertAfter(self, newSibling: XPathNavigator) -> VoidType: ...
    
    @overload
    def InsertBefore(self) -> XmlWriter: ...
    
    @overload
    def InsertBefore(self, newSibling: StringType) -> VoidType: ...
    
    @overload
    def InsertBefore(self, newSibling: XmlReader) -> VoidType: ...
    
    @overload
    def InsertBefore(self, newSibling: XPathNavigator) -> VoidType: ...
    
    def InsertElementAfter(self, prefix: StringType, localName: StringType, namespaceURI: StringType, value: StringType) -> VoidType: ...
    
    def InsertElementBefore(self, prefix: StringType, localName: StringType, namespaceURI: StringType, value: StringType) -> VoidType: ...
    
    def IsDescendant(self, nav: XPathNavigator) -> BooleanType: ...
    
    def IsSamePosition(self, other: XPathNavigator) -> BooleanType: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    def LookupPrefix(self, namespaceURI: StringType) -> StringType: ...
    
    @overload
    def Matches(self, expr: XPathExpression) -> BooleanType: ...
    
    @overload
    def Matches(self, xpath: StringType) -> BooleanType: ...
    
    def MoveTo(self, other: XPathNavigator) -> BooleanType: ...
    
    def MoveToAttribute(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def MoveToChild(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def MoveToChild(self, type: XPathNodeType) -> BooleanType: ...
    
    def MoveToFirst(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToFirstChild(self) -> BooleanType: ...
    
    @overload
    def MoveToFirstNamespace(self) -> BooleanType: ...
    
    @overload
    def MoveToFirstNamespace(self, namespaceScope: XPathNamespaceScope) -> BooleanType: ...
    
    @overload
    def MoveToFollowing(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def MoveToFollowing(self, localName: StringType, namespaceURI: StringType, end: XPathNavigator) -> BooleanType: ...
    
    @overload
    def MoveToFollowing(self, type: XPathNodeType) -> BooleanType: ...
    
    @overload
    def MoveToFollowing(self, type: XPathNodeType, end: XPathNavigator) -> BooleanType: ...
    
    def MoveToId(self, id: StringType) -> BooleanType: ...
    
    def MoveToNamespace(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToNext(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def MoveToNext(self, type: XPathNodeType) -> BooleanType: ...
    
    @overload
    def MoveToNext(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    @overload
    def MoveToNextNamespace(self) -> BooleanType: ...
    
    @overload
    def MoveToNextNamespace(self, namespaceScope: XPathNamespaceScope) -> BooleanType: ...
    
    def MoveToParent(self) -> BooleanType: ...
    
    def MoveToPrevious(self) -> BooleanType: ...
    
    def MoveToRoot(self) -> VoidType: ...
    
    @overload
    def PrependChild(self) -> XmlWriter: ...
    
    @overload
    def PrependChild(self, newChild: StringType) -> VoidType: ...
    
    @overload
    def PrependChild(self, newChild: XmlReader) -> VoidType: ...
    
    @overload
    def PrependChild(self, newChild: XPathNavigator) -> VoidType: ...
    
    def PrependChildElement(self, prefix: StringType, localName: StringType, namespaceURI: StringType, value: StringType) -> VoidType: ...
    
    def ReadSubtree(self) -> XmlReader: ...
    
    def ReplaceRange(self, lastSiblingToReplace: XPathNavigator) -> XmlWriter: ...
    
    @overload
    def ReplaceSelf(self, newNode: StringType) -> VoidType: ...
    
    @overload
    def ReplaceSelf(self, newNode: XmlReader) -> VoidType: ...
    
    @overload
    def ReplaceSelf(self, newNode: XPathNavigator) -> VoidType: ...
    
    @overload
    def Select(self, xpath: StringType) -> XPathNodeIterator: ...
    
    @overload
    def Select(self, xpath: StringType, resolver: IXmlNamespaceResolver) -> XPathNodeIterator: ...
    
    @overload
    def Select(self, expr: XPathExpression) -> XPathNodeIterator: ...
    
    @overload
    def SelectAncestors(self, type: XPathNodeType, matchSelf: BooleanType) -> XPathNodeIterator: ...
    
    @overload
    def SelectAncestors(self, name: StringType, namespaceURI: StringType, matchSelf: BooleanType) -> XPathNodeIterator: ...
    
    @overload
    def SelectChildren(self, type: XPathNodeType) -> XPathNodeIterator: ...
    
    @overload
    def SelectChildren(self, name: StringType, namespaceURI: StringType) -> XPathNodeIterator: ...
    
    @overload
    def SelectDescendants(self, type: XPathNodeType, matchSelf: BooleanType) -> XPathNodeIterator: ...
    
    @overload
    def SelectDescendants(self, name: StringType, namespaceURI: StringType, matchSelf: BooleanType) -> XPathNodeIterator: ...
    
    @overload
    def SelectSingleNode(self, xpath: StringType) -> XPathNavigator: ...
    
    @overload
    def SelectSingleNode(self, xpath: StringType, resolver: IXmlNamespaceResolver) -> XPathNavigator: ...
    
    @overload
    def SelectSingleNode(self, expression: XPathExpression) -> XPathNavigator: ...
    
    def SetTypedValue(self, typedValue: ObjectType) -> VoidType: ...
    
    def SetValue(self, value: StringType) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    @overload
    def ValueAs(self, returnType: TypeType, nsResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    def WriteSubtree(self, writer: XmlWriter) -> VoidType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_CanEdit(self) -> BooleanType: ...
    
    def get_HasAttributes(self) -> BooleanType: ...
    
    def get_HasChildren(self) -> BooleanType: ...
    
    def get_InnerXml(self) -> StringType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    def get_IsNode(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    @staticmethod
    def get_NavigatorComparer() -> IEqualityComparer: ...
    
    def get_NodeType(self) -> XPathNodeType: ...
    
    def get_OuterXml(self) -> StringType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    def get_TypedValue(self) -> ObjectType: ...
    
    def get_UnderlyingObject(self) -> ObjectType: ...
    
    def get_ValueAsBoolean(self) -> BooleanType: ...
    
    def get_ValueAsDateTime(self) -> DateTime: ...
    
    def get_ValueAsDouble(self) -> DoubleType: ...
    
    def get_ValueAsInt(self) -> IntType: ...
    
    def get_ValueAsLong(self) -> LongType: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlType(self) -> XmlSchemaType: ...
    
    def set_InnerXml(self, value: StringType) -> VoidType: ...
    
    def set_OuterXml(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathNavigatorKeyComparer(ObjectType, IEqualityComparer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathNavigatorKeyComparer(ObjectType, IEqualityComparer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathNavigatorReader(XmlReader, IDisposable, IXmlNamespaceResolver):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeCount(self) -> IntType: ...
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def CanReadBinaryContent(self) -> BooleanType: ...
    
    @property
    def Depth(self) -> IntType: ...
    
    @property
    def EOF(self) -> BooleanType: ...
    
    @property
    def HasValue(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def ReadState(self) -> ReadState: ...
    
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    @property
    def Settings(self) -> XmlReaderSettings: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @staticmethod
    def Create(navToRead: XPathNavigator) -> XPathNavigatorReader: ...
    
    @overload
    def GetAttribute(self, index: IntType) -> StringType: ...
    
    @overload
    def GetAttribute(self, name: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, localName: StringType, namespaceURI: StringType) -> StringType: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    @overload
    def MoveToAttribute(self, localName: StringType, namespaceName: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType) -> BooleanType: ...
    
    def MoveToElement(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    def Read(self) -> BooleanType: ...
    
    def ReadAttributeValue(self) -> BooleanType: ...
    
    def ReadContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ResolveEntity(self) -> VoidType: ...
    
    def get_AttributeCount(self) -> IntType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_CanReadBinaryContent(self) -> BooleanType: ...
    
    def get_Depth(self) -> IntType: ...
    
    def get_EOF(self) -> BooleanType: ...
    
    def get_HasValue(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_ReadState(self) -> ReadState: ...
    
    def get_SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    def get_Settings(self) -> XmlReaderSettings: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathNavigatorReader(XmlReader, IDisposable, IXmlNamespaceResolver):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeCount(self) -> IntType: ...
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def CanReadBinaryContent(self) -> BooleanType: ...
    
    @property
    def Depth(self) -> IntType: ...
    
    @property
    def EOF(self) -> BooleanType: ...
    
    @property
    def HasValue(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def ReadState(self) -> ReadState: ...
    
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    @property
    def Settings(self) -> XmlReaderSettings: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @staticmethod
    def Create(navToRead: XPathNavigator) -> XPathNavigatorReader: ...
    
    @overload
    def GetAttribute(self, index: IntType) -> StringType: ...
    
    @overload
    def GetAttribute(self, name: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, localName: StringType, namespaceURI: StringType) -> StringType: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    @overload
    def MoveToAttribute(self, localName: StringType, namespaceName: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType) -> BooleanType: ...
    
    def MoveToElement(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    def Read(self) -> BooleanType: ...
    
    def ReadAttributeValue(self) -> BooleanType: ...
    
    def ReadContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ResolveEntity(self) -> VoidType: ...
    
    def get_AttributeCount(self) -> IntType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_CanReadBinaryContent(self) -> BooleanType: ...
    
    def get_Depth(self) -> IntType: ...
    
    def get_EOF(self) -> BooleanType: ...
    
    def get_HasValue(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_ReadState(self) -> ReadState: ...
    
    def get_SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    def get_Settings(self) -> XmlReaderSettings: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathNavigatorReaderWithSI(XPathNavigatorReader, IDisposable, IXmlNamespaceResolver, IXmlSchemaInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def IsNil(self) -> BooleanType: ...
    
    @property
    def MemberType(self) -> XmlSchemaSimpleType: ...
    
    @property
    def SchemaAttribute(self) -> XmlSchemaAttribute: ...
    
    @property
    def SchemaElement(self) -> XmlSchemaElement: ...
    
    @property
    def SchemaType(self) -> XmlSchemaType: ...
    
    @property
    def Validity(self) -> XmlSchemaValidity: ...
    
    # ---------- Methods ---------- #
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_IsNil(self) -> BooleanType: ...
    
    def get_MemberType(self) -> XmlSchemaSimpleType: ...
    
    def get_SchemaAttribute(self) -> XmlSchemaAttribute: ...
    
    def get_SchemaElement(self) -> XmlSchemaElement: ...
    
    def get_SchemaType(self) -> XmlSchemaType: ...
    
    def get_Validity(self) -> XmlSchemaValidity: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathNavigatorReaderWithSI(XPathNavigatorReader, IDisposable, IXmlNamespaceResolver, IXmlSchemaInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def IsNil(self) -> BooleanType: ...
    
    @property
    def MemberType(self) -> XmlSchemaSimpleType: ...
    
    @property
    def SchemaAttribute(self) -> XmlSchemaAttribute: ...
    
    @property
    def SchemaElement(self) -> XmlSchemaElement: ...
    
    @property
    def SchemaType(self) -> XmlSchemaType: ...
    
    @property
    def Validity(self) -> XmlSchemaValidity: ...
    
    # ---------- Methods ---------- #
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_IsNil(self) -> BooleanType: ...
    
    def get_MemberType(self) -> XmlSchemaSimpleType: ...
    
    def get_SchemaAttribute(self) -> XmlSchemaAttribute: ...
    
    def get_SchemaElement(self) -> XmlSchemaElement: ...
    
    def get_SchemaType(self) -> XmlSchemaType: ...
    
    def get_Validity(self) -> XmlSchemaValidity: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathNodeIterator(ABC, ObjectType, ICloneable, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathNodeIterator(ABC, ObjectType, ICloneable, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlEmptyNavigator(XPathNavigator, ICloneable, IXPathNavigable, IXmlNamespaceResolver):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def HasAttributes(self) -> BooleanType: ...
    
    @property
    def HasChildren(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XPathNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @staticmethod
    @property
    def Singleton() -> XmlEmptyNavigator: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNavigator: ...
    
    def ComparePosition(self, other: XPathNavigator) -> XmlNodeOrder: ...
    
    def GetAttribute(self, localName: StringType, namespaceName: StringType) -> StringType: ...
    
    def GetNamespace(self, name: StringType) -> StringType: ...
    
    def IsSamePosition(self, other: XPathNavigator) -> BooleanType: ...
    
    def MoveTo(self, other: XPathNavigator) -> BooleanType: ...
    
    def MoveToAttribute(self, localName: StringType, namespaceName: StringType) -> BooleanType: ...
    
    def MoveToFirst(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToFirstChild(self) -> BooleanType: ...
    
    @overload
    def MoveToFirstNamespace(self, scope: XPathNamespaceScope) -> BooleanType: ...
    
    def MoveToId(self, id: StringType) -> BooleanType: ...
    
    def MoveToNamespace(self, prefix: StringType) -> BooleanType: ...
    
    @overload
    def MoveToNext(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    @overload
    def MoveToNextNamespace(self, scope: XPathNamespaceScope) -> BooleanType: ...
    
    def MoveToParent(self) -> BooleanType: ...
    
    def MoveToPrevious(self) -> BooleanType: ...
    
    def MoveToRoot(self) -> VoidType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_HasAttributes(self) -> BooleanType: ...
    
    def get_HasChildren(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XPathNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    @staticmethod
    def get_Singleton() -> XmlEmptyNavigator: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlEmptyNavigator(XPathNavigator, ICloneable, IXPathNavigable, IXmlNamespaceResolver):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def HasAttributes(self) -> BooleanType: ...
    
    @property
    def HasChildren(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XPathNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @staticmethod
    @property
    def Singleton() -> XmlEmptyNavigator: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNavigator: ...
    
    def ComparePosition(self, other: XPathNavigator) -> XmlNodeOrder: ...
    
    def GetAttribute(self, localName: StringType, namespaceName: StringType) -> StringType: ...
    
    def GetNamespace(self, name: StringType) -> StringType: ...
    
    def IsSamePosition(self, other: XPathNavigator) -> BooleanType: ...
    
    def MoveTo(self, other: XPathNavigator) -> BooleanType: ...
    
    def MoveToAttribute(self, localName: StringType, namespaceName: StringType) -> BooleanType: ...
    
    def MoveToFirst(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToFirstChild(self) -> BooleanType: ...
    
    @overload
    def MoveToFirstNamespace(self, scope: XPathNamespaceScope) -> BooleanType: ...
    
    def MoveToId(self, id: StringType) -> BooleanType: ...
    
    def MoveToNamespace(self, prefix: StringType) -> BooleanType: ...
    
    @overload
    def MoveToNext(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    @overload
    def MoveToNextNamespace(self, scope: XPathNamespaceScope) -> BooleanType: ...
    
    def MoveToParent(self) -> BooleanType: ...
    
    def MoveToPrevious(self) -> BooleanType: ...
    
    def MoveToRoot(self) -> VoidType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_HasAttributes(self) -> BooleanType: ...
    
    def get_HasChildren(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XPathNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    @staticmethod
    def get_Singleton() -> XmlEmptyNavigator: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# ---------- Interfaces ---------- #

class IXPathNavigable(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CreateNavigator(self) -> XPathNavigator: ...
    
    # No Events


class IXPathNavigable(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CreateNavigator(self) -> XPathNavigator: ...
    
    # No Events


# ---------- Enums ---------- #

class XPathNamespaceScope(Enum):
    All: IntType = 0
    ExcludeXml: IntType = 1
    Local: IntType = 2


class XPathNamespaceScope(Enum):
    All: IntType = 0
    ExcludeXml: IntType = 1
    Local: IntType = 2


class XPathNodeType(Enum):
    Root: IntType = 0
    Element: IntType = 1
    Attribute: IntType = 2
    Namespace: IntType = 3
    Text: IntType = 4
    SignificantWhitespace: IntType = 5
    Whitespace: IntType = 6
    ProcessingInstruction: IntType = 7
    Comment: IntType = 8
    All: IntType = 9


class XPathNodeType(Enum):
    Root: IntType = 0
    Element: IntType = 1
    Attribute: IntType = 2
    Namespace: IntType = 3
    Text: IntType = 4
    SignificantWhitespace: IntType = 5
    Whitespace: IntType = 6
    ProcessingInstruction: IntType = 7
    Comment: IntType = 8
    All: IntType = 9


class XPathResultType(Enum):
    Number: IntType = 0
    String: IntType = 1
    Navigator: IntType = 1
    Boolean: IntType = 2
    NodeSet: IntType = 3
    Any: IntType = 5
    Error: IntType = 6


class XPathResultType(Enum):
    Number: IntType = 0
    String: IntType = 1
    Navigator: IntType = 1
    Boolean: IntType = 2
    NodeSet: IntType = 3
    Any: IntType = 5
    Error: IntType = 6


class XmlCaseOrder(Enum):
    #None: IntType = 0
    UpperFirst: IntType = 1
    LowerFirst: IntType = 2


class XmlCaseOrder(Enum):
    #None: IntType = 0
    UpperFirst: IntType = 1
    LowerFirst: IntType = 2


class XmlDataType(Enum):
    Text: IntType = 1
    Number: IntType = 2


class XmlDataType(Enum):
    Text: IntType = 1
    Number: IntType = 2


class XmlSortOrder(Enum):
    Ascending: IntType = 1
    Descending: IntType = 2


class XmlSortOrder(Enum):
    Ascending: IntType = 1
    Descending: IntType = 2


# No Delegates

__all__ = [
    XPathDocument,
    XPathException,
    XPathExpression,
    XPathItem,
    XPathNavigator,
    XPathNavigatorKeyComparer,
    XPathNavigatorReader,
    XPathNavigatorReaderWithSI,
    XPathNodeIterator,
    XmlEmptyNavigator,
    IXPathNavigable,
    XPathNamespaceScope,
    XPathNodeType,
    XPathResultType,
    XmlCaseOrder,
    XmlDataType,
    XmlSortOrder,
]
