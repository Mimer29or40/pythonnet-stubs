from __future__ import annotations

from abc import ABC
from typing import List, Tuple, Union, overload

from System import Array, Boolean, Char, Enum, ICloneable, IDisposable, Int32, Object, String, ValueType, Void
from System.Collections import IEnumerable
from System.Xml import IDtdInfo, IXmlLineInfo, IXmlNamespaceResolver, XmlNameTable, XmlNodeOrder, XmlRawWriter
from System.Xml.XPath import IXPathNavigable, XPathDocument, XPathNamespaceScope, XPathNavigator, XPathNodeIterator, XPathNodeType

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
CharType = Union[str, Char]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class XPathDocumentBaseIterator(ABC, XPathNodeIterator, ICloneable, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathDocumentBaseIterator(ABC, XPathNodeIterator, ICloneable, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> XPathNavigator: ...
    
    @property
    def CurrentPosition(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_Current(self) -> XPathNavigator: ...
    
    def get_CurrentPosition(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathDocumentBuilder(XmlRawWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, doc: XPathDocument, lineInfo: IXmlLineInfo, baseUri: StringType, flags: LoadFlags): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def CreateIdTables(self, dtdInfo: IDtdInfo) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def Initialize(self, doc: XPathDocument, lineInfo: IXmlLineInfo, baseUri: StringType, flags: LoadFlags) -> VoidType: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    @overload
    def WriteEndElement(self) -> VoidType: ...
    
    @overload
    def WriteEndElement(self, allowShortcutTag: BooleanType) -> VoidType: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteFullEndElement(self) -> VoidType: ...
    
    @overload
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    @overload
    def WriteProcessingInstruction(self, name: StringType, text: StringType, baseUri: StringType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, namespaceName: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType, baseUri: StringType) -> VoidType: ...
    
    @overload
    def WriteString(self, text: StringType) -> VoidType: ...
    
    @overload
    def WriteString(self, text: StringType, textType: TextBlockType) -> VoidType: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathDocumentBuilder(XmlRawWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, doc: XPathDocument, lineInfo: IXmlLineInfo, baseUri: StringType, flags: LoadFlags): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def CreateIdTables(self, dtdInfo: IDtdInfo) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def Initialize(self, doc: XPathDocument, lineInfo: IXmlLineInfo, baseUri: StringType, flags: LoadFlags) -> VoidType: ...
    
    def WriteCData(self, text: StringType) -> VoidType: ...
    
    def WriteCharEntity(self, ch: CharType) -> VoidType: ...
    
    def WriteChars(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    def WriteComment(self, text: StringType) -> VoidType: ...
    
    def WriteDocType(self, name: StringType, pubid: StringType, sysid: StringType, subset: StringType) -> VoidType: ...
    
    def WriteEndAttribute(self) -> VoidType: ...
    
    @overload
    def WriteEndElement(self) -> VoidType: ...
    
    @overload
    def WriteEndElement(self, allowShortcutTag: BooleanType) -> VoidType: ...
    
    def WriteEntityRef(self, name: StringType) -> VoidType: ...
    
    def WriteFullEndElement(self) -> VoidType: ...
    
    @overload
    def WriteProcessingInstruction(self, name: StringType, text: StringType) -> VoidType: ...
    
    @overload
    def WriteProcessingInstruction(self, name: StringType, text: StringType, baseUri: StringType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, data: StringType) -> VoidType: ...
    
    @overload
    def WriteRaw(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteStartAttribute(self, prefix: StringType, localName: StringType, namespaceName: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType) -> VoidType: ...
    
    @overload
    def WriteStartElement(self, prefix: StringType, localName: StringType, ns: StringType, baseUri: StringType) -> VoidType: ...
    
    @overload
    def WriteString(self, text: StringType) -> VoidType: ...
    
    @overload
    def WriteString(self, text: StringType, textType: TextBlockType) -> VoidType: ...
    
    def WriteSurrogateCharEntity(self, lowChar: CharType, highChar: CharType) -> VoidType: ...
    
    def WriteWhitespace(self, ws: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathDocumentElementChildIterator(XPathDocumentBaseIterator, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, parent: XPathDocumentNavigator, name: StringType, namespaceURI: StringType): ...
    
    @overload
    def __init__(self, iter: XPathDocumentElementChildIterator): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathDocumentElementChildIterator(XPathDocumentBaseIterator, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, parent: XPathDocumentNavigator, name: StringType, namespaceURI: StringType): ...
    
    @overload
    def __init__(self, iter: XPathDocumentElementChildIterator): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathDocumentElementDescendantIterator(XPathDocumentBaseIterator, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, root: XPathDocumentNavigator, name: StringType, namespaceURI: StringType, matchSelf: BooleanType): ...
    
    @overload
    def __init__(self, iter: XPathDocumentElementDescendantIterator): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathDocumentElementDescendantIterator(XPathDocumentBaseIterator, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, root: XPathDocumentNavigator, name: StringType, namespaceURI: StringType, matchSelf: BooleanType): ...
    
    @overload
    def __init__(self, iter: XPathDocumentElementDescendantIterator): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathDocumentKindChildIterator(XPathDocumentBaseIterator, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, parent: XPathDocumentNavigator, typ: XPathNodeType): ...
    
    @overload
    def __init__(self, iter: XPathDocumentKindChildIterator): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathDocumentKindChildIterator(XPathDocumentBaseIterator, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, parent: XPathDocumentNavigator, typ: XPathNodeType): ...
    
    @overload
    def __init__(self, iter: XPathDocumentKindChildIterator): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathDocumentKindDescendantIterator(XPathDocumentBaseIterator, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, root: XPathDocumentNavigator, typ: XPathNodeType, matchSelf: BooleanType): ...
    
    @overload
    def __init__(self, iter: XPathDocumentKindDescendantIterator): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathDocumentKindDescendantIterator(XPathDocumentBaseIterator, ICloneable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, root: XPathDocumentNavigator, typ: XPathNodeType, matchSelf: BooleanType): ...
    
    @overload
    def __init__(self, iter: XPathDocumentKindDescendantIterator): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNodeIterator: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathDocumentNavigator(XPathNavigator, ICloneable, IXPathNavigable, IXmlNamespaceResolver, IXmlLineInfo):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, pageCurrent: ArrayType[XPathNode], idxCurrent: IntType, pageParent: ArrayType[XPathNode], idxParent: IntType): ...
    
    @overload
    def __init__(self, nav: XPathDocumentNavigator): ...
    
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
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
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
    
    @property
    def UnderlyingObject(self) -> ObjectType: ...
    
    @property
    def Value(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNavigator: ...
    
    def ComparePosition(self, other: XPathNavigator) -> XmlNodeOrder: ...
    
    def GetPositionHashCode(self) -> IntType: ...
    
    def HasLineInfo(self) -> BooleanType: ...
    
    def IsContentKindMatch(self, typ: XPathNodeType) -> BooleanType: ...
    
    def IsDescendant(self, other: XPathNavigator) -> BooleanType: ...
    
    def IsElementMatch(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    def IsKindMatch(self, typ: XPathNodeType) -> BooleanType: ...
    
    def IsSamePosition(self, other: XPathNavigator) -> BooleanType: ...
    
    def MoveTo(self, other: XPathNavigator) -> BooleanType: ...
    
    def MoveToAttribute(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def MoveToChild(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def MoveToChild(self, type: XPathNodeType) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToFirstChild(self) -> BooleanType: ...
    
    @overload
    def MoveToFirstNamespace(self, namespaceScope: XPathNamespaceScope) -> BooleanType: ...
    
    @overload
    def MoveToFollowing(self, localName: StringType, namespaceURI: StringType, end: XPathNavigator) -> BooleanType: ...
    
    @overload
    def MoveToFollowing(self, type: XPathNodeType, end: XPathNavigator) -> BooleanType: ...
    
    def MoveToId(self, id: StringType) -> BooleanType: ...
    
    @overload
    def MoveToNext(self) -> BooleanType: ...
    
    @overload
    def MoveToNext(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def MoveToNext(self, type: XPathNodeType) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    @overload
    def MoveToNextNamespace(self, scope: XPathNamespaceScope) -> BooleanType: ...
    
    def MoveToParent(self) -> BooleanType: ...
    
    def MoveToPrevious(self) -> BooleanType: ...
    
    def MoveToRoot(self) -> VoidType: ...
    
    @overload
    def SelectChildren(self, type: XPathNodeType) -> XPathNodeIterator: ...
    
    @overload
    def SelectChildren(self, name: StringType, namespaceURI: StringType) -> XPathNodeIterator: ...
    
    @overload
    def SelectDescendants(self, type: XPathNodeType, matchSelf: BooleanType) -> XPathNodeIterator: ...
    
    @overload
    def SelectDescendants(self, name: StringType, namespaceURI: StringType, matchSelf: BooleanType) -> XPathNodeIterator: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_HasAttributes(self) -> BooleanType: ...
    
    def get_HasChildren(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XPathNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_UnderlyingObject(self) -> ObjectType: ...
    
    def get_Value(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathDocumentNavigator(XPathNavigator, ICloneable, IXPathNavigable, IXmlNamespaceResolver, IXmlLineInfo):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, pageCurrent: ArrayType[XPathNode], idxCurrent: IntType, pageParent: ArrayType[XPathNode], idxParent: IntType): ...
    
    @overload
    def __init__(self, nav: XPathDocumentNavigator): ...
    
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
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
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
    
    @property
    def UnderlyingObject(self) -> ObjectType: ...
    
    @property
    def Value(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> XPathNavigator: ...
    
    def ComparePosition(self, other: XPathNavigator) -> XmlNodeOrder: ...
    
    def GetPositionHashCode(self) -> IntType: ...
    
    def HasLineInfo(self) -> BooleanType: ...
    
    def IsContentKindMatch(self, typ: XPathNodeType) -> BooleanType: ...
    
    def IsDescendant(self, other: XPathNavigator) -> BooleanType: ...
    
    def IsElementMatch(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    def IsKindMatch(self, typ: XPathNodeType) -> BooleanType: ...
    
    def IsSamePosition(self, other: XPathNavigator) -> BooleanType: ...
    
    def MoveTo(self, other: XPathNavigator) -> BooleanType: ...
    
    def MoveToAttribute(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def MoveToChild(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def MoveToChild(self, type: XPathNodeType) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToFirstChild(self) -> BooleanType: ...
    
    @overload
    def MoveToFirstNamespace(self, namespaceScope: XPathNamespaceScope) -> BooleanType: ...
    
    @overload
    def MoveToFollowing(self, localName: StringType, namespaceURI: StringType, end: XPathNavigator) -> BooleanType: ...
    
    @overload
    def MoveToFollowing(self, type: XPathNodeType, end: XPathNavigator) -> BooleanType: ...
    
    def MoveToId(self, id: StringType) -> BooleanType: ...
    
    @overload
    def MoveToNext(self) -> BooleanType: ...
    
    @overload
    def MoveToNext(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def MoveToNext(self, type: XPathNodeType) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    @overload
    def MoveToNextNamespace(self, scope: XPathNamespaceScope) -> BooleanType: ...
    
    def MoveToParent(self) -> BooleanType: ...
    
    def MoveToPrevious(self) -> BooleanType: ...
    
    def MoveToRoot(self) -> VoidType: ...
    
    @overload
    def SelectChildren(self, type: XPathNodeType) -> XPathNodeIterator: ...
    
    @overload
    def SelectChildren(self, name: StringType, namespaceURI: StringType) -> XPathNodeIterator: ...
    
    @overload
    def SelectDescendants(self, type: XPathNodeType, matchSelf: BooleanType) -> XPathNodeIterator: ...
    
    @overload
    def SelectDescendants(self, name: StringType, namespaceURI: StringType, matchSelf: BooleanType) -> XPathNodeIterator: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_HasAttributes(self) -> BooleanType: ...
    
    def get_HasChildren(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XPathNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_UnderlyingObject(self) -> ObjectType: ...
    
    def get_Value(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathNodeHelper(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetAttribute(pageNode: XPathNode, idxNode: IntType, localName: StringType, namespaceName: StringType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    @overload
    def GetContentChild(pageNode: XPathNode, idxNode: IntType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    @overload
    def GetContentChild(pageNode: XPathNode, idxNode: IntType, typ: XPathNodeType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    def GetContentFollowing(pageCurrent: XPathNode, idxCurrent: IntType, pageEnd: ArrayType[XPathNode], idxEnd: IntType, typ: XPathNodeType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    @overload
    def GetContentSibling(pageNode: XPathNode, idxNode: IntType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    @overload
    def GetContentSibling(pageNode: XPathNode, idxNode: IntType, typ: XPathNodeType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    def GetElementChild(pageNode: XPathNode, idxNode: IntType, localName: StringType, namespaceName: StringType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    def GetElementFollowing(pageCurrent: XPathNode, idxCurrent: IntType, pageEnd: ArrayType[XPathNode], idxEnd: IntType, localName: StringType, namespaceName: StringType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    def GetElementSibling(pageNode: XPathNode, idxNode: IntType, localName: StringType, namespaceName: StringType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    def GetFirstAttribute(pageNode: XPathNode, idxNode: IntType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    def GetFollowing(pageNode: XPathNode, idxNode: IntType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    def GetInScopeNamespaces(pageElem: ArrayType[XPathNode], idxElem: IntType, pageNmsp: XPathNode) -> Tuple[IntType, XPathNode]: ...
    
    @staticmethod
    def GetLocalNamespaces(pageElem: ArrayType[XPathNode], idxElem: IntType, pageNmsp: XPathNode) -> Tuple[IntType, XPathNode]: ...
    
    @staticmethod
    def GetLocation(pageNode: ArrayType[XPathNode], idxNode: IntType) -> IntType: ...
    
    @staticmethod
    def GetNextAttribute(pageNode: XPathNode, idxNode: IntType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    def GetNonDescendant(pageNode: XPathNode, idxNode: IntType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    def GetParent(pageNode: XPathNode, idxNode: IntType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    @overload
    def GetPreviousContentSibling(pageNode: XPathNode, idxNode: IntType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    @overload
    def GetPreviousContentSibling(pageNode: XPathNode, idxNode: IntType, typ: XPathNodeType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    def GetPreviousElementSibling(pageNode: XPathNode, idxNode: IntType, localName: StringType, namespaceName: StringType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    def GetTextFollowing(pageCurrent: XPathNode, idxCurrent: IntType, pageEnd: ArrayType[XPathNode], idxEnd: IntType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathNodeHelper(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetAttribute(pageNode: XPathNode, idxNode: IntType, localName: StringType, namespaceName: StringType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    @overload
    def GetContentChild(pageNode: XPathNode, idxNode: IntType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    @overload
    def GetContentChild(pageNode: XPathNode, idxNode: IntType, typ: XPathNodeType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    def GetContentFollowing(pageCurrent: XPathNode, idxCurrent: IntType, pageEnd: ArrayType[XPathNode], idxEnd: IntType, typ: XPathNodeType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    @overload
    def GetContentSibling(pageNode: XPathNode, idxNode: IntType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    @overload
    def GetContentSibling(pageNode: XPathNode, idxNode: IntType, typ: XPathNodeType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    def GetElementChild(pageNode: XPathNode, idxNode: IntType, localName: StringType, namespaceName: StringType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    def GetElementFollowing(pageCurrent: XPathNode, idxCurrent: IntType, pageEnd: ArrayType[XPathNode], idxEnd: IntType, localName: StringType, namespaceName: StringType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    def GetElementSibling(pageNode: XPathNode, idxNode: IntType, localName: StringType, namespaceName: StringType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    def GetFirstAttribute(pageNode: XPathNode, idxNode: IntType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    def GetFollowing(pageNode: XPathNode, idxNode: IntType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    def GetInScopeNamespaces(pageElem: ArrayType[XPathNode], idxElem: IntType, pageNmsp: XPathNode) -> Tuple[IntType, XPathNode]: ...
    
    @staticmethod
    def GetLocalNamespaces(pageElem: ArrayType[XPathNode], idxElem: IntType, pageNmsp: XPathNode) -> Tuple[IntType, XPathNode]: ...
    
    @staticmethod
    def GetLocation(pageNode: ArrayType[XPathNode], idxNode: IntType) -> IntType: ...
    
    @staticmethod
    def GetNextAttribute(pageNode: XPathNode, idxNode: IntType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    def GetNonDescendant(pageNode: XPathNode, idxNode: IntType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    def GetParent(pageNode: XPathNode, idxNode: IntType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    @overload
    def GetPreviousContentSibling(pageNode: XPathNode, idxNode: IntType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    @overload
    def GetPreviousContentSibling(pageNode: XPathNode, idxNode: IntType, typ: XPathNodeType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    def GetPreviousElementSibling(pageNode: XPathNode, idxNode: IntType, localName: StringType, namespaceName: StringType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    @staticmethod
    def GetTextFollowing(pageCurrent: XPathNode, idxCurrent: IntType, pageEnd: ArrayType[XPathNode], idxEnd: IntType) -> Tuple[BooleanType, XPathNode, IntType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathNodeInfoAtom(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, pageInfo: XPathNodePageInfo): ...
    
    @overload
    def __init__(self, localName: StringType, namespaceUri: StringType, prefix: StringType, baseUri: StringType, pageParent: ArrayType[XPathNode], pageSibling: ArrayType[XPathNode], pageSimilar: ArrayType[XPathNode], doc: XPathDocument, lineNumBase: IntType, linePosBase: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BaseUri(self) -> StringType: ...
    
    @property
    def Document(self) -> XPathDocument: ...
    
    @property
    def LineNumberBase(self) -> IntType: ...
    
    @property
    def LinePositionBase(self) -> IntType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def LocalNameHashCode(self) -> IntType: ...
    
    @property
    def NamespaceUri(self) -> StringType: ...
    
    @property
    def Next(self) -> XPathNodeInfoAtom: ...
    
    @Next.setter
    def Next(self, value: XPathNodeInfoAtom) -> None: ...
    
    @property
    def PageInfo(self) -> XPathNodePageInfo: ...
    
    @property
    def ParentPage(self) -> ArrayType[XPathNode]: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def SiblingPage(self) -> ArrayType[XPathNode]: ...
    
    @property
    def SimilarElementPage(self) -> ArrayType[XPathNode]: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, other: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def Init(self, localName: StringType, namespaceUri: StringType, prefix: StringType, baseUri: StringType, pageParent: ArrayType[XPathNode], pageSibling: ArrayType[XPathNode], pageSimilar: ArrayType[XPathNode], doc: XPathDocument, lineNumBase: IntType, linePosBase: IntType) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_BaseUri(self) -> StringType: ...
    
    def get_Document(self) -> XPathDocument: ...
    
    def get_LineNumberBase(self) -> IntType: ...
    
    def get_LinePositionBase(self) -> IntType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_LocalNameHashCode(self) -> IntType: ...
    
    def get_NamespaceUri(self) -> StringType: ...
    
    def get_Next(self) -> XPathNodeInfoAtom: ...
    
    def get_PageInfo(self) -> XPathNodePageInfo: ...
    
    def get_ParentPage(self) -> ArrayType[XPathNode]: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_SiblingPage(self) -> ArrayType[XPathNode]: ...
    
    def get_SimilarElementPage(self) -> ArrayType[XPathNode]: ...
    
    def set_Next(self, value: XPathNodeInfoAtom) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathNodeInfoAtom(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, pageInfo: XPathNodePageInfo): ...
    
    @overload
    def __init__(self, localName: StringType, namespaceUri: StringType, prefix: StringType, baseUri: StringType, pageParent: ArrayType[XPathNode], pageSibling: ArrayType[XPathNode], pageSimilar: ArrayType[XPathNode], doc: XPathDocument, lineNumBase: IntType, linePosBase: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BaseUri(self) -> StringType: ...
    
    @property
    def Document(self) -> XPathDocument: ...
    
    @property
    def LineNumberBase(self) -> IntType: ...
    
    @property
    def LinePositionBase(self) -> IntType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def LocalNameHashCode(self) -> IntType: ...
    
    @property
    def NamespaceUri(self) -> StringType: ...
    
    @property
    def Next(self) -> XPathNodeInfoAtom: ...
    
    @Next.setter
    def Next(self, value: XPathNodeInfoAtom) -> None: ...
    
    @property
    def PageInfo(self) -> XPathNodePageInfo: ...
    
    @property
    def ParentPage(self) -> ArrayType[XPathNode]: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def SiblingPage(self) -> ArrayType[XPathNode]: ...
    
    @property
    def SimilarElementPage(self) -> ArrayType[XPathNode]: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, other: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def Init(self, localName: StringType, namespaceUri: StringType, prefix: StringType, baseUri: StringType, pageParent: ArrayType[XPathNode], pageSibling: ArrayType[XPathNode], pageSimilar: ArrayType[XPathNode], doc: XPathDocument, lineNumBase: IntType, linePosBase: IntType) -> VoidType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_BaseUri(self) -> StringType: ...
    
    def get_Document(self) -> XPathDocument: ...
    
    def get_LineNumberBase(self) -> IntType: ...
    
    def get_LinePositionBase(self) -> IntType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_LocalNameHashCode(self) -> IntType: ...
    
    def get_NamespaceUri(self) -> StringType: ...
    
    def get_Next(self) -> XPathNodeInfoAtom: ...
    
    def get_PageInfo(self) -> XPathNodePageInfo: ...
    
    def get_ParentPage(self) -> ArrayType[XPathNode]: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_SiblingPage(self) -> ArrayType[XPathNode]: ...
    
    def get_SimilarElementPage(self) -> ArrayType[XPathNode]: ...
    
    def set_Next(self, value: XPathNodeInfoAtom) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathNodeInfoTable(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Create(self, localName: StringType, namespaceUri: StringType, prefix: StringType, baseUri: StringType, pageParent: ArrayType[XPathNode], pageSibling: ArrayType[XPathNode], pageSimilar: ArrayType[XPathNode], doc: XPathDocument, lineNumBase: IntType, linePosBase: IntType) -> XPathNodeInfoAtom: ...
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathNodeInfoTable(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Create(self, localName: StringType, namespaceUri: StringType, prefix: StringType, baseUri: StringType, pageParent: ArrayType[XPathNode], pageSibling: ArrayType[XPathNode], pageSimilar: ArrayType[XPathNode], doc: XPathDocument, lineNumBase: IntType, linePosBase: IntType) -> XPathNodeInfoAtom: ...
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathNodePageInfo(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, pagePrev: ArrayType[XPathNode], pageNum: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def NextPage(self) -> ArrayType[XPathNode]: ...
    
    @NextPage.setter
    def NextPage(self, value: ArrayType[XPathNode]) -> None: ...
    
    @property
    def NodeCount(self) -> IntType: ...
    
    @NodeCount.setter
    def NodeCount(self, value: IntType) -> None: ...
    
    @property
    def PageNumber(self) -> IntType: ...
    
    @property
    def PreviousPage(self) -> ArrayType[XPathNode]: ...
    
    # ---------- Methods ---------- #
    
    def get_NextPage(self) -> ArrayType[XPathNode]: ...
    
    def get_NodeCount(self) -> IntType: ...
    
    def get_PageNumber(self) -> IntType: ...
    
    def get_PreviousPage(self) -> ArrayType[XPathNode]: ...
    
    def set_NextPage(self, value: ArrayType[XPathNode]) -> VoidType: ...
    
    def set_NodeCount(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathNodePageInfo(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, pagePrev: ArrayType[XPathNode], pageNum: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def NextPage(self) -> ArrayType[XPathNode]: ...
    
    @NextPage.setter
    def NextPage(self, value: ArrayType[XPathNode]) -> None: ...
    
    @property
    def NodeCount(self) -> IntType: ...
    
    @NodeCount.setter
    def NodeCount(self, value: IntType) -> None: ...
    
    @property
    def PageNumber(self) -> IntType: ...
    
    @property
    def PreviousPage(self) -> ArrayType[XPathNode]: ...
    
    # ---------- Methods ---------- #
    
    def get_NextPage(self) -> ArrayType[XPathNode]: ...
    
    def get_NodeCount(self) -> IntType: ...
    
    def get_PageNumber(self) -> IntType: ...
    
    def get_PreviousPage(self) -> ArrayType[XPathNode]: ...
    
    def set_NextPage(self, value: ArrayType[XPathNode]) -> VoidType: ...
    
    def set_NodeCount(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Structs ---------- #

class XPathNode(ValueType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def MaxCollapsedPositionOffset() -> IntType: ...
    
    @staticmethod
    @property
    def MaxLineNumberOffset() -> IntType: ...
    
    @staticmethod
    @property
    def MaxLinePositionOffset() -> IntType: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AllowShortcutTag(self) -> BooleanType: ...
    
    @property
    def BaseUri(self) -> StringType: ...
    
    @property
    def CollapsedLinePosition(self) -> IntType: ...
    
    @property
    def Document(self) -> XPathDocument: ...
    
    @property
    def HasAttribute(self) -> BooleanType: ...
    
    @property
    def HasCollapsedText(self) -> BooleanType: ...
    
    @property
    def HasContentChild(self) -> BooleanType: ...
    
    @property
    def HasElementChild(self) -> BooleanType: ...
    
    @property
    def HasNamespaceDecls(self) -> BooleanType: ...
    
    @HasNamespaceDecls.setter
    def HasNamespaceDecls(self, value: BooleanType) -> None: ...
    
    @property
    def HasSibling(self) -> BooleanType: ...
    
    @property
    def IsAttrNmsp(self) -> BooleanType: ...
    
    @property
    def IsText(self) -> BooleanType: ...
    
    @property
    def IsXmlNamespaceNode(self) -> BooleanType: ...
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def LocalNameHashCode(self) -> IntType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NamespaceUri(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XPathNodeType: ...
    
    @property
    def PageInfo(self) -> XPathNodePageInfo: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def Value(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Create(self, pageInfo: XPathNodePageInfo) -> VoidType: ...
    
    @overload
    def Create(self, info: XPathNodeInfoAtom, xptyp: XPathNodeType, idxParent: IntType) -> VoidType: ...
    
    def ElementMatch(self, localName: StringType, namespaceName: StringType) -> BooleanType: ...
    
    def GetParent(self, pageNode: XPathNode) -> Tuple[IntType, XPathNode]: ...
    
    def GetRoot(self, pageNode: XPathNode) -> Tuple[IntType, XPathNode]: ...
    
    def GetSibling(self, pageNode: XPathNode) -> Tuple[IntType, XPathNode]: ...
    
    def GetSimilarElement(self, pageNode: XPathNode) -> Tuple[IntType, XPathNode]: ...
    
    def NameMatch(self, localName: StringType, namespaceName: StringType) -> BooleanType: ...
    
    def SetCollapsedLineInfoOffset(self, posOffset: IntType) -> VoidType: ...
    
    def SetCollapsedValue(self, value: StringType) -> VoidType: ...
    
    def SetEmptyValue(self, allowShortcutTag: BooleanType) -> VoidType: ...
    
    def SetLineInfoOffsets(self, lineNumOffset: IntType, linePosOffset: IntType) -> VoidType: ...
    
    def SetParentProperties(self, xptyp: XPathNodeType) -> VoidType: ...
    
    def SetSibling(self, infoTable: XPathNodeInfoTable, pageSibling: ArrayType[XPathNode], idxSibling: IntType) -> VoidType: ...
    
    def SetSimilarElement(self, infoTable: XPathNodeInfoTable, pageSimilar: ArrayType[XPathNode], idxSimilar: IntType) -> VoidType: ...
    
    def SetValue(self, value: StringType) -> VoidType: ...
    
    def get_AllowShortcutTag(self) -> BooleanType: ...
    
    def get_BaseUri(self) -> StringType: ...
    
    def get_CollapsedLinePosition(self) -> IntType: ...
    
    def get_Document(self) -> XPathDocument: ...
    
    def get_HasAttribute(self) -> BooleanType: ...
    
    def get_HasCollapsedText(self) -> BooleanType: ...
    
    def get_HasContentChild(self) -> BooleanType: ...
    
    def get_HasElementChild(self) -> BooleanType: ...
    
    def get_HasNamespaceDecls(self) -> BooleanType: ...
    
    def get_HasSibling(self) -> BooleanType: ...
    
    def get_IsAttrNmsp(self) -> BooleanType: ...
    
    def get_IsText(self) -> BooleanType: ...
    
    def get_IsXmlNamespaceNode(self) -> BooleanType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_LocalNameHashCode(self) -> IntType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NamespaceUri(self) -> StringType: ...
    
    def get_NodeType(self) -> XPathNodeType: ...
    
    def get_PageInfo(self) -> XPathNodePageInfo: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    def set_HasNamespaceDecls(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathNode(ValueType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def MaxCollapsedPositionOffset() -> IntType: ...
    
    @staticmethod
    @property
    def MaxLineNumberOffset() -> IntType: ...
    
    @staticmethod
    @property
    def MaxLinePositionOffset() -> IntType: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AllowShortcutTag(self) -> BooleanType: ...
    
    @property
    def BaseUri(self) -> StringType: ...
    
    @property
    def CollapsedLinePosition(self) -> IntType: ...
    
    @property
    def Document(self) -> XPathDocument: ...
    
    @property
    def HasAttribute(self) -> BooleanType: ...
    
    @property
    def HasCollapsedText(self) -> BooleanType: ...
    
    @property
    def HasContentChild(self) -> BooleanType: ...
    
    @property
    def HasElementChild(self) -> BooleanType: ...
    
    @property
    def HasNamespaceDecls(self) -> BooleanType: ...
    
    @HasNamespaceDecls.setter
    def HasNamespaceDecls(self, value: BooleanType) -> None: ...
    
    @property
    def HasSibling(self) -> BooleanType: ...
    
    @property
    def IsAttrNmsp(self) -> BooleanType: ...
    
    @property
    def IsText(self) -> BooleanType: ...
    
    @property
    def IsXmlNamespaceNode(self) -> BooleanType: ...
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def LocalNameHashCode(self) -> IntType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NamespaceUri(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XPathNodeType: ...
    
    @property
    def PageInfo(self) -> XPathNodePageInfo: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def Value(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Create(self, pageInfo: XPathNodePageInfo) -> VoidType: ...
    
    @overload
    def Create(self, info: XPathNodeInfoAtom, xptyp: XPathNodeType, idxParent: IntType) -> VoidType: ...
    
    def ElementMatch(self, localName: StringType, namespaceName: StringType) -> BooleanType: ...
    
    def GetParent(self, pageNode: XPathNode) -> Tuple[IntType, XPathNode]: ...
    
    def GetRoot(self, pageNode: XPathNode) -> Tuple[IntType, XPathNode]: ...
    
    def GetSibling(self, pageNode: XPathNode) -> Tuple[IntType, XPathNode]: ...
    
    def GetSimilarElement(self, pageNode: XPathNode) -> Tuple[IntType, XPathNode]: ...
    
    def NameMatch(self, localName: StringType, namespaceName: StringType) -> BooleanType: ...
    
    def SetCollapsedLineInfoOffset(self, posOffset: IntType) -> VoidType: ...
    
    def SetCollapsedValue(self, value: StringType) -> VoidType: ...
    
    def SetEmptyValue(self, allowShortcutTag: BooleanType) -> VoidType: ...
    
    def SetLineInfoOffsets(self, lineNumOffset: IntType, linePosOffset: IntType) -> VoidType: ...
    
    def SetParentProperties(self, xptyp: XPathNodeType) -> VoidType: ...
    
    def SetSibling(self, infoTable: XPathNodeInfoTable, pageSibling: ArrayType[XPathNode], idxSibling: IntType) -> VoidType: ...
    
    def SetSimilarElement(self, infoTable: XPathNodeInfoTable, pageSimilar: ArrayType[XPathNode], idxSimilar: IntType) -> VoidType: ...
    
    def SetValue(self, value: StringType) -> VoidType: ...
    
    def get_AllowShortcutTag(self) -> BooleanType: ...
    
    def get_BaseUri(self) -> StringType: ...
    
    def get_CollapsedLinePosition(self) -> IntType: ...
    
    def get_Document(self) -> XPathDocument: ...
    
    def get_HasAttribute(self) -> BooleanType: ...
    
    def get_HasCollapsedText(self) -> BooleanType: ...
    
    def get_HasContentChild(self) -> BooleanType: ...
    
    def get_HasElementChild(self) -> BooleanType: ...
    
    def get_HasNamespaceDecls(self) -> BooleanType: ...
    
    def get_HasSibling(self) -> BooleanType: ...
    
    def get_IsAttrNmsp(self) -> BooleanType: ...
    
    def get_IsText(self) -> BooleanType: ...
    
    def get_IsXmlNamespaceNode(self) -> BooleanType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_LocalNameHashCode(self) -> IntType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NamespaceUri(self) -> StringType: ...
    
    def get_NodeType(self) -> XPathNodeType: ...
    
    def get_PageInfo(self) -> XPathNodePageInfo: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_Value(self) -> StringType: ...
    
    def set_HasNamespaceDecls(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathNodeRef(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, page: ArrayType[XPathNode], idx: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Index(self) -> IntType: ...
    
    @property
    def IsNull(self) -> BooleanType: ...
    
    @staticmethod
    @property
    def Null() -> XPathNodeRef: ...
    
    @property
    def Page(self) -> ArrayType[XPathNode]: ...
    
    # ---------- Methods ---------- #
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Index(self) -> IntType: ...
    
    def get_IsNull(self) -> BooleanType: ...
    
    @staticmethod
    def get_Null() -> XPathNodeRef: ...
    
    def get_Page(self) -> ArrayType[XPathNode]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XPathNodeRef(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, page: ArrayType[XPathNode], idx: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Index(self) -> IntType: ...
    
    @property
    def IsNull(self) -> BooleanType: ...
    
    @staticmethod
    @property
    def Null() -> XPathNodeRef: ...
    
    @property
    def Page(self) -> ArrayType[XPathNode]: ...
    
    # ---------- Methods ---------- #
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Index(self) -> IntType: ...
    
    def get_IsNull(self) -> BooleanType: ...
    
    @staticmethod
    def get_Null() -> XPathNodeRef: ...
    
    def get_Page(self) -> ArrayType[XPathNode]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Interfaces

# ---------- Enums ---------- #

class TextBlockType(Enum):
    #None: IntType = 0
    Text: IntType = 4
    SignificantWhitespace: IntType = 5
    Whitespace: IntType = 6


class TextBlockType(Enum):
    #None: IntType = 0
    Text: IntType = 4
    SignificantWhitespace: IntType = 5
    Whitespace: IntType = 6


# No Delegates

__all__ = [
    XPathDocumentBaseIterator,
    XPathDocumentBuilder,
    XPathDocumentElementChildIterator,
    XPathDocumentElementDescendantIterator,
    XPathDocumentKindChildIterator,
    XPathDocumentKindDescendantIterator,
    XPathDocumentNavigator,
    XPathNodeHelper,
    XPathNodeInfoAtom,
    XPathNodeInfoTable,
    XPathNodePageInfo,
    XPathNode,
    XPathNodeRef,
    TextBlockType,
]
