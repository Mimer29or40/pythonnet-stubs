"""Automatically generated stubs for C# namespace: System.Configuration."""

from abc import ABC
from collections.abc import Callable
from collections.abc import Iterator
from typing import Self
from typing import overload

from System import Array
from System import Attribute
from System import Enum
from System import EventArgs
from System import Exception
from System import GenericUriParserOptions
from System import Guid
from System import ICloneable
from System import IntPtr
from System import Object
from System import SystemException
from System import Type
from System import UInt32
from System import UriIdnScope
from System import ValueType
from System.Collections import Hashtable
from System.Collections import ICollection
from System.Collections import IDictionary
from System.Collections import IDictionaryEnumerator
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections.Generic import Dictionary
from System.Collections.Specialized import NameValueCollection
from System.ComponentModel import CancelEventArgs
from System.ComponentModel import INotifyPropertyChanged
from System.ComponentModel import PropertyChangedEventHandler
from System.Configuration.Internal import IConfigErrorInfo
from System.Configuration.Provider import ProviderBase
from System.Configuration.Provider import ProviderCollection
from System.IO import Stream
from System.IO import TextReader
from System.IO import TextWriter
from System.Reflection import MethodBase
from System.Runtime.InteropServices import _Attribute
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import IDeserializationCallback
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Xml import XmlAttribute
from System.Xml import XmlAttributeCollection
from System.Xml import XmlCDataSection
from System.Xml import XmlComment
from System.Xml import XmlDeclaration
from System.Xml import XmlDocument
from System.Xml import XmlDocumentFragment
from System.Xml import XmlDocumentType
from System.Xml import XmlElement
from System.Xml import XmlEntityReference
from System.Xml import XmlImplementation
from System.Xml import XmlNamespaceManager
from System.Xml import XmlNameTable
from System.Xml import XmlNode
from System.Xml import XmlNodeChangedEventHandler
from System.Xml import XmlNodeList
from System.Xml import XmlNodeType
from System.Xml import XmlProcessingInstruction
from System.Xml import XmlReader
from System.Xml import XmlResolver
from System.Xml import XmlSignificantWhitespace
from System.Xml import XmlText
from System.Xml import XmlTextReader
from System.Xml import XmlWhitespace
from System.Xml import XmlWriter
from System.Xml.Schema import IXmlSchemaInfo
from System.Xml.Schema import ValidationEventHandler
from System.Xml.Schema import XmlSchemaSet
from System.Xml.XPath import IXPathNavigable
from System.Xml.XPath import XPathNavigator

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

class AppSettingsReader(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetValue(self, key: str, type: Type) -> object:
        """"""
    def ToString(self) -> str:
        """"""

class ApplicationScopedSettingAttribute(SettingAttribute, _Attribute):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class ApplicationSettingsBase(ABC, SettingsBase, INotifyPropertyChanged):
    """"""
    @property
    def Context(self) -> SettingsContext:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Properties(self) -> SettingsPropertyCollection:
        """"""
    @property
    def PropertyValues(self) -> SettingsPropertyValueCollection:
        """"""
    @property
    def Providers(self) -> SettingsProviderCollection:
        """"""
    @property
    def SettingsKey(self) -> str:
        """"""
    @SettingsKey.setter
    def SettingsKey(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetPreviousVersion(self, propertyName: str) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(
        self,
        context: SettingsContext,
        properties: SettingsPropertyCollection,
        providers: SettingsProviderCollection,
    ) -> None:
        """"""
    def Reload(self) -> None:
        """"""
    def Reset(self) -> None:
        """"""
    def Save(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Upgrade(self) -> None:
        """"""
    def __getitem__(self, propertyName: str) -> object:
        """"""
    def __setitem__(self, propertyName: str, value: object) -> None:
        """"""
    PropertyChanged: EventType[PropertyChangedEventHandler] = ...
    """"""
    SettingChanging: EventType[SettingChangingEventHandler] = ...
    """"""
    SettingsLoaded: EventType[SettingsLoadedEventHandler] = ...
    """"""
    SettingsSaving: EventType[SettingsSavingEventHandler] = ...
    """"""

class ApplicationSettingsGroup(ConfigurationSectionGroup):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def IsDeclarationRequired(self) -> bool:
        """"""
    @property
    def IsDeclared(self) -> bool:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def SectionGroupName(self) -> str:
        """"""
    @property
    def SectionGroups(self) -> ConfigurationSectionGroupCollection:
        """"""
    @property
    def Sections(self) -> ConfigurationSectionCollection:
        """"""
    @property
    def Type(self) -> str:
        """"""
    @Type.setter
    def Type(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def ForceDeclaration(self) -> None:
        """"""
    @overload
    def ForceDeclaration(self, force: bool) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ClientSettingsSection(ConfigurationSection):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def LockAllAttributesExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAllElementsExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAttributes(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockElements(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockItem(self) -> bool:
        """"""
    @LockItem.setter
    def LockItem(self, value: bool) -> None: ...
    @property
    def SectionInformation(self) -> SectionInformation:
        """"""
    @property
    def Settings(self) -> SettingElementCollection:
        """"""
    def Equals(self, compareTo: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class ClientSettingsStore(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CommonConfigurationStrings(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ConfigXmlAttribute(XmlAttribute, IEnumerable, IConfigErrorInfo, IXPathNavigable, ICloneable):
    """"""
    def __init__(
        self,
        filename: str,
        line: int,
        prefix: str,
        localName: str,
        namespaceUri: str,
        doc: XmlDocument,
    ) -> None:
        """"""
    @property
    def Attributes(self) -> XmlAttributeCollection:
        """"""
    @property
    def BaseURI(self) -> str:
        """"""
    @property
    def ChildNodes(self) -> XmlNodeList:
        """"""
    @property
    def Filename(self) -> str:
        """"""
    @property
    def FirstChild(self) -> XmlNode:
        """"""
    @property
    def HasChildNodes(self) -> bool:
        """"""
    @property
    def InnerText(self) -> str:
        """"""
    @InnerText.setter
    def InnerText(self, value: str) -> None: ...
    @property
    def InnerXml(self) -> str:
        """"""
    @InnerXml.setter
    def InnerXml(self, value: str) -> None: ...
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def Item(self) -> XmlElement:
        """"""
    @property
    def LastChild(self) -> XmlNode:
        """"""
    @property
    def LineNumber(self) -> int:
        """"""
    @property
    def LocalName(self) -> str:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def NamespaceURI(self) -> str:
        """"""
    @property
    def NextSibling(self) -> XmlNode:
        """"""
    @property
    def NodeType(self) -> XmlNodeType:
        """"""
    @property
    def OuterXml(self) -> str:
        """"""
    @property
    def OwnerDocument(self) -> XmlDocument:
        """"""
    @property
    def OwnerElement(self) -> XmlElement:
        """"""
    @property
    def ParentNode(self) -> XmlNode:
        """"""
    @property
    def Prefix(self) -> str:
        """"""
    @Prefix.setter
    def Prefix(self, value: str) -> None: ...
    @property
    def PreviousSibling(self) -> XmlNode:
        """"""
    @property
    def PreviousText(self) -> XmlNode:
        """"""
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo:
        """"""
    @property
    def Specified(self) -> bool:
        """"""
    @property
    def Value(self) -> str:
        """"""
    @Value.setter
    def Value(self, value: str) -> None: ...
    def AppendChild(self, newChild: XmlNode) -> XmlNode:
        """"""
    def Clone(self) -> XmlNode:
        """"""
    def CloneNode(self, deep: bool) -> XmlNode:
        """"""
    def CreateNavigator(self) -> XPathNavigator:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetNamespaceOfPrefix(self, prefix: str) -> str:
        """"""
    def GetPrefixOfNamespace(self, namespaceURI: str) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def InsertAfter(self, newChild: XmlNode, refChild: XmlNode) -> XmlNode:
        """"""
    def InsertBefore(self, newChild: XmlNode, refChild: XmlNode) -> XmlNode:
        """"""
    def Normalize(self) -> None:
        """"""
    def PrependChild(self, newChild: XmlNode) -> XmlNode:
        """"""
    def RemoveAll(self) -> None:
        """"""
    def RemoveChild(self, oldChild: XmlNode) -> XmlNode:
        """"""
    def ReplaceChild(self, newChild: XmlNode, oldChild: XmlNode) -> XmlNode:
        """"""
    @overload
    def SelectNodes(self, xpath: str) -> XmlNodeList:
        """"""
    @overload
    def SelectNodes(self, xpath: str, nsmgr: XmlNamespaceManager) -> XmlNodeList:
        """"""
    @overload
    def SelectSingleNode(self, xpath: str) -> XmlNode:
        """"""
    @overload
    def SelectSingleNode(self, xpath: str, nsmgr: XmlNamespaceManager) -> XmlNode:
        """"""
    def Supports(self, feature: str, version: str) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteContentTo(self, w: XmlWriter) -> None:
        """"""
    def WriteTo(self, w: XmlWriter) -> None:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __getitem__(self, name: str) -> XmlElement:
        """"""
    @overload
    def __getitem__(self, localname: str, ns: str) -> XmlElement:
        """"""

class ConfigXmlCDataSection(
    XmlCDataSection, IEnumerable, IConfigErrorInfo, IXPathNavigable, ICloneable
):
    """"""
    def __init__(self, filename: str, line: int, data: str, doc: XmlDocument) -> None:
        """"""
    @property
    def Attributes(self) -> XmlAttributeCollection:
        """"""
    @property
    def BaseURI(self) -> str:
        """"""
    @property
    def ChildNodes(self) -> XmlNodeList:
        """"""
    @property
    def Data(self) -> str:
        """"""
    @Data.setter
    def Data(self, value: str) -> None: ...
    @property
    def Filename(self) -> str:
        """"""
    @property
    def FirstChild(self) -> XmlNode:
        """"""
    @property
    def HasChildNodes(self) -> bool:
        """"""
    @property
    def InnerText(self) -> str:
        """"""
    @InnerText.setter
    def InnerText(self, value: str) -> None: ...
    @property
    def InnerXml(self) -> str:
        """"""
    @InnerXml.setter
    def InnerXml(self, value: str) -> None: ...
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def Item(self) -> XmlElement:
        """"""
    @property
    def LastChild(self) -> XmlNode:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def LineNumber(self) -> int:
        """"""
    @property
    def LocalName(self) -> str:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def NamespaceURI(self) -> str:
        """"""
    @property
    def NextSibling(self) -> XmlNode:
        """"""
    @property
    def NodeType(self) -> XmlNodeType:
        """"""
    @property
    def OuterXml(self) -> str:
        """"""
    @property
    def OwnerDocument(self) -> XmlDocument:
        """"""
    @property
    def ParentNode(self) -> XmlNode:
        """"""
    @property
    def Prefix(self) -> str:
        """"""
    @Prefix.setter
    def Prefix(self, value: str) -> None: ...
    @property
    def PreviousSibling(self) -> XmlNode:
        """"""
    @property
    def PreviousText(self) -> XmlNode:
        """"""
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo:
        """"""
    @property
    def Value(self) -> str:
        """"""
    @Value.setter
    def Value(self, value: str) -> None: ...
    def AppendChild(self, newChild: XmlNode) -> XmlNode:
        """"""
    def AppendData(self, strData: str) -> None:
        """"""
    def Clone(self) -> XmlNode:
        """"""
    def CloneNode(self, deep: bool) -> XmlNode:
        """"""
    def CreateNavigator(self) -> XPathNavigator:
        """"""
    def DeleteData(self, offset: int, count: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetNamespaceOfPrefix(self, prefix: str) -> str:
        """"""
    def GetPrefixOfNamespace(self, namespaceURI: str) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def InsertAfter(self, newChild: XmlNode, refChild: XmlNode) -> XmlNode:
        """"""
    def InsertBefore(self, newChild: XmlNode, refChild: XmlNode) -> XmlNode:
        """"""
    def InsertData(self, offset: int, strData: str) -> None:
        """"""
    def Normalize(self) -> None:
        """"""
    def PrependChild(self, newChild: XmlNode) -> XmlNode:
        """"""
    def RemoveAll(self) -> None:
        """"""
    def RemoveChild(self, oldChild: XmlNode) -> XmlNode:
        """"""
    def ReplaceChild(self, newChild: XmlNode, oldChild: XmlNode) -> XmlNode:
        """"""
    def ReplaceData(self, offset: int, count: int, strData: str) -> None:
        """"""
    @overload
    def SelectNodes(self, xpath: str) -> XmlNodeList:
        """"""
    @overload
    def SelectNodes(self, xpath: str, nsmgr: XmlNamespaceManager) -> XmlNodeList:
        """"""
    @overload
    def SelectSingleNode(self, xpath: str) -> XmlNode:
        """"""
    @overload
    def SelectSingleNode(self, xpath: str, nsmgr: XmlNamespaceManager) -> XmlNode:
        """"""
    def Substring(self, offset: int, count: int) -> str:
        """"""
    def Supports(self, feature: str, version: str) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteContentTo(self, w: XmlWriter) -> None:
        """"""
    def WriteTo(self, w: XmlWriter) -> None:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __getitem__(self, name: str) -> XmlElement:
        """"""
    @overload
    def __getitem__(self, localname: str, ns: str) -> XmlElement:
        """"""

class ConfigXmlComment(XmlComment, IEnumerable, IConfigErrorInfo, IXPathNavigable, ICloneable):
    """"""
    def __init__(self, filename: str, line: int, comment: str, doc: XmlDocument) -> None:
        """"""
    @property
    def Attributes(self) -> XmlAttributeCollection:
        """"""
    @property
    def BaseURI(self) -> str:
        """"""
    @property
    def ChildNodes(self) -> XmlNodeList:
        """"""
    @property
    def Data(self) -> str:
        """"""
    @Data.setter
    def Data(self, value: str) -> None: ...
    @property
    def Filename(self) -> str:
        """"""
    @property
    def FirstChild(self) -> XmlNode:
        """"""
    @property
    def HasChildNodes(self) -> bool:
        """"""
    @property
    def InnerText(self) -> str:
        """"""
    @InnerText.setter
    def InnerText(self, value: str) -> None: ...
    @property
    def InnerXml(self) -> str:
        """"""
    @InnerXml.setter
    def InnerXml(self, value: str) -> None: ...
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def Item(self) -> XmlElement:
        """"""
    @property
    def LastChild(self) -> XmlNode:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def LineNumber(self) -> int:
        """"""
    @property
    def LocalName(self) -> str:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def NamespaceURI(self) -> str:
        """"""
    @property
    def NextSibling(self) -> XmlNode:
        """"""
    @property
    def NodeType(self) -> XmlNodeType:
        """"""
    @property
    def OuterXml(self) -> str:
        """"""
    @property
    def OwnerDocument(self) -> XmlDocument:
        """"""
    @property
    def ParentNode(self) -> XmlNode:
        """"""
    @property
    def Prefix(self) -> str:
        """"""
    @Prefix.setter
    def Prefix(self, value: str) -> None: ...
    @property
    def PreviousSibling(self) -> XmlNode:
        """"""
    @property
    def PreviousText(self) -> XmlNode:
        """"""
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo:
        """"""
    @property
    def Value(self) -> str:
        """"""
    @Value.setter
    def Value(self, value: str) -> None: ...
    def AppendChild(self, newChild: XmlNode) -> XmlNode:
        """"""
    def AppendData(self, strData: str) -> None:
        """"""
    def Clone(self) -> XmlNode:
        """"""
    def CloneNode(self, deep: bool) -> XmlNode:
        """"""
    def CreateNavigator(self) -> XPathNavigator:
        """"""
    def DeleteData(self, offset: int, count: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetNamespaceOfPrefix(self, prefix: str) -> str:
        """"""
    def GetPrefixOfNamespace(self, namespaceURI: str) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def InsertAfter(self, newChild: XmlNode, refChild: XmlNode) -> XmlNode:
        """"""
    def InsertBefore(self, newChild: XmlNode, refChild: XmlNode) -> XmlNode:
        """"""
    def InsertData(self, offset: int, strData: str) -> None:
        """"""
    def Normalize(self) -> None:
        """"""
    def PrependChild(self, newChild: XmlNode) -> XmlNode:
        """"""
    def RemoveAll(self) -> None:
        """"""
    def RemoveChild(self, oldChild: XmlNode) -> XmlNode:
        """"""
    def ReplaceChild(self, newChild: XmlNode, oldChild: XmlNode) -> XmlNode:
        """"""
    def ReplaceData(self, offset: int, count: int, strData: str) -> None:
        """"""
    @overload
    def SelectNodes(self, xpath: str) -> XmlNodeList:
        """"""
    @overload
    def SelectNodes(self, xpath: str, nsmgr: XmlNamespaceManager) -> XmlNodeList:
        """"""
    @overload
    def SelectSingleNode(self, xpath: str) -> XmlNode:
        """"""
    @overload
    def SelectSingleNode(self, xpath: str, nsmgr: XmlNamespaceManager) -> XmlNode:
        """"""
    def Substring(self, offset: int, count: int) -> str:
        """"""
    def Supports(self, feature: str, version: str) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteContentTo(self, w: XmlWriter) -> None:
        """"""
    def WriteTo(self, w: XmlWriter) -> None:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __getitem__(self, name: str) -> XmlElement:
        """"""
    @overload
    def __getitem__(self, localname: str, ns: str) -> XmlElement:
        """"""

class ConfigXmlDocument(XmlDocument, IEnumerable, IConfigErrorInfo, IXPathNavigable, ICloneable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Attributes(self) -> XmlAttributeCollection:
        """"""
    @property
    def BaseURI(self) -> str:
        """"""
    @property
    def ChildNodes(self) -> XmlNodeList:
        """"""
    @property
    def DocumentElement(self) -> XmlElement:
        """"""
    @property
    def DocumentType(self) -> XmlDocumentType:
        """"""
    @property
    def Filename(self) -> str:
        """"""
    @property
    def FirstChild(self) -> XmlNode:
        """"""
    @property
    def HasChildNodes(self) -> bool:
        """"""
    @property
    def Implementation(self) -> XmlImplementation:
        """"""
    @property
    def InnerText(self) -> str:
        """"""
    @InnerText.setter
    def InnerText(self, value: str) -> None: ...
    @property
    def InnerXml(self) -> str:
        """"""
    @InnerXml.setter
    def InnerXml(self, value: str) -> None: ...
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def Item(self) -> XmlElement:
        """"""
    @property
    def LastChild(self) -> XmlNode:
        """"""
    @property
    def LineNumber(self) -> int:
        """"""
    @property
    def LocalName(self) -> str:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def NameTable(self) -> XmlNameTable:
        """"""
    @property
    def NamespaceURI(self) -> str:
        """"""
    @property
    def NextSibling(self) -> XmlNode:
        """"""
    @property
    def NodeType(self) -> XmlNodeType:
        """"""
    @property
    def OuterXml(self) -> str:
        """"""
    @property
    def OwnerDocument(self) -> XmlDocument:
        """"""
    @property
    def ParentNode(self) -> XmlNode:
        """"""
    @property
    def Prefix(self) -> str:
        """"""
    @Prefix.setter
    def Prefix(self, value: str) -> None: ...
    @property
    def PreserveWhitespace(self) -> bool:
        """"""
    @PreserveWhitespace.setter
    def PreserveWhitespace(self, value: bool) -> None: ...
    @property
    def PreviousSibling(self) -> XmlNode:
        """"""
    @property
    def PreviousText(self) -> XmlNode:
        """"""
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo:
        """"""
    @property
    def Schemas(self) -> XmlSchemaSet:
        """"""
    @Schemas.setter
    def Schemas(self, value: XmlSchemaSet) -> None: ...
    @property
    def Value(self) -> str:
        """"""
    @Value.setter
    def Value(self, value: str) -> None: ...
    @property
    def XmlResolver(self) -> XmlResolver:
        """"""
    @XmlResolver.setter
    def XmlResolver(self, value: XmlResolver) -> None: ...
    def AppendChild(self, newChild: XmlNode) -> XmlNode:
        """"""
    def Clone(self) -> XmlNode:
        """"""
    def CloneNode(self, deep: bool) -> XmlNode:
        """"""
    @overload
    def CreateAttribute(self, name: str) -> XmlAttribute:
        """"""
    @overload
    def CreateAttribute(self, qualifiedName: str, namespaceURI: str) -> XmlAttribute:
        """"""
    @overload
    def CreateAttribute(self, prefix: str, localName: str, namespaceUri: str) -> XmlAttribute:
        """"""
    def CreateCDataSection(self, data: str) -> XmlCDataSection:
        """"""
    def CreateComment(self, data: str) -> XmlComment:
        """"""
    def CreateDocumentFragment(self) -> XmlDocumentFragment:
        """"""
    def CreateDocumentType(
        self, name: str, publicId: str, systemId: str, internalSubset: str
    ) -> XmlDocumentType:
        """"""
    @overload
    def CreateElement(self, name: str) -> XmlElement:
        """"""
    @overload
    def CreateElement(self, qualifiedName: str, namespaceURI: str) -> XmlElement:
        """"""
    @overload
    def CreateElement(self, prefix: str, localName: str, namespaceUri: str) -> XmlElement:
        """"""
    def CreateEntityReference(self, name: str) -> XmlEntityReference:
        """"""
    def CreateNavigator(self) -> XPathNavigator:
        """"""
    @overload
    def CreateNode(self, type: XmlNodeType, name: str, namespaceURI: str) -> XmlNode:
        """"""
    @overload
    def CreateNode(self, type: XmlNodeType, prefix: str, name: str, namespaceURI: str) -> XmlNode:
        """"""
    @overload
    def CreateNode(self, nodeTypeString: str, name: str, namespaceURI: str) -> XmlNode:
        """"""
    def CreateProcessingInstruction(self, target: str, data: str) -> XmlProcessingInstruction:
        """"""
    def CreateSignificantWhitespace(self, data: str) -> XmlSignificantWhitespace:
        """"""
    def CreateTextNode(self, text: str) -> XmlText:
        """"""
    def CreateWhitespace(self, data: str) -> XmlWhitespace:
        """"""
    def CreateXmlDeclaration(self, version: str, encoding: str, standalone: str) -> XmlDeclaration:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetElementById(self, elementId: str) -> XmlElement:
        """"""
    @overload
    def GetElementsByTagName(self, name: str) -> XmlNodeList:
        """"""
    @overload
    def GetElementsByTagName(self, localName: str, namespaceURI: str) -> XmlNodeList:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetNamespaceOfPrefix(self, prefix: str) -> str:
        """"""
    def GetPrefixOfNamespace(self, namespaceURI: str) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def ImportNode(self, node: XmlNode, deep: bool) -> XmlNode:
        """"""
    def InsertAfter(self, newChild: XmlNode, refChild: XmlNode) -> XmlNode:
        """"""
    def InsertBefore(self, newChild: XmlNode, refChild: XmlNode) -> XmlNode:
        """"""
    @overload
    def Load(self, inStream: Stream) -> None:
        """"""
    @overload
    def Load(self, txtReader: TextReader) -> None:
        """"""
    @overload
    def Load(self, reader: XmlReader) -> None:
        """"""
    @overload
    def Load(self, filename: str) -> None:
        """"""
    def LoadSingleElement(self, filename: str, sourceReader: XmlTextReader) -> None:
        """"""
    def LoadXml(self, xml: str) -> None:
        """"""
    def Normalize(self) -> None:
        """"""
    def PrependChild(self, newChild: XmlNode) -> XmlNode:
        """"""
    def ReadNode(self, reader: XmlReader) -> XmlNode:
        """"""
    def RemoveAll(self) -> None:
        """"""
    def RemoveChild(self, oldChild: XmlNode) -> XmlNode:
        """"""
    def ReplaceChild(self, newChild: XmlNode, oldChild: XmlNode) -> XmlNode:
        """"""
    @overload
    def Save(self, outStream: Stream) -> None:
        """"""
    @overload
    def Save(self, writer: TextWriter) -> None:
        """"""
    @overload
    def Save(self, w: XmlWriter) -> None:
        """"""
    @overload
    def Save(self, filename: str) -> None:
        """"""
    @overload
    def SelectNodes(self, xpath: str) -> XmlNodeList:
        """"""
    @overload
    def SelectNodes(self, xpath: str, nsmgr: XmlNamespaceManager) -> XmlNodeList:
        """"""
    @overload
    def SelectSingleNode(self, xpath: str) -> XmlNode:
        """"""
    @overload
    def SelectSingleNode(self, xpath: str, nsmgr: XmlNamespaceManager) -> XmlNode:
        """"""
    def Supports(self, feature: str, version: str) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def Validate(self, validationEventHandler: ValidationEventHandler) -> None:
        """"""
    @overload
    def Validate(
        self, validationEventHandler: ValidationEventHandler, nodeToValidate: XmlNode
    ) -> None:
        """"""
    def WriteContentTo(self, xw: XmlWriter) -> None:
        """"""
    def WriteTo(self, w: XmlWriter) -> None:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __getitem__(self, name: str) -> XmlElement:
        """"""
    @overload
    def __getitem__(self, localname: str, ns: str) -> XmlElement:
        """"""
    NodeChanged: EventType[XmlNodeChangedEventHandler] = ...
    """"""
    NodeChanging: EventType[XmlNodeChangedEventHandler] = ...
    """"""
    NodeInserted: EventType[XmlNodeChangedEventHandler] = ...
    """"""
    NodeInserting: EventType[XmlNodeChangedEventHandler] = ...
    """"""
    NodeRemoved: EventType[XmlNodeChangedEventHandler] = ...
    """"""
    NodeRemoving: EventType[XmlNodeChangedEventHandler] = ...
    """"""

class ConfigXmlElement(XmlElement, IEnumerable, IConfigErrorInfo, IXPathNavigable, ICloneable):
    """"""
    def __init__(
        self,
        filename: str,
        line: int,
        prefix: str,
        localName: str,
        namespaceUri: str,
        doc: XmlDocument,
    ) -> None:
        """"""
    @property
    def Attributes(self) -> XmlAttributeCollection:
        """"""
    @property
    def BaseURI(self) -> str:
        """"""
    @property
    def ChildNodes(self) -> XmlNodeList:
        """"""
    @property
    def Filename(self) -> str:
        """"""
    @property
    def FirstChild(self) -> XmlNode:
        """"""
    @property
    def HasAttributes(self) -> bool:
        """"""
    @property
    def HasChildNodes(self) -> bool:
        """"""
    @property
    def InnerText(self) -> str:
        """"""
    @InnerText.setter
    def InnerText(self, value: str) -> None: ...
    @property
    def InnerXml(self) -> str:
        """"""
    @InnerXml.setter
    def InnerXml(self, value: str) -> None: ...
    @property
    def IsEmpty(self) -> bool:
        """"""
    @IsEmpty.setter
    def IsEmpty(self, value: bool) -> None: ...
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def Item(self) -> XmlElement:
        """"""
    @property
    def LastChild(self) -> XmlNode:
        """"""
    @property
    def LineNumber(self) -> int:
        """"""
    @property
    def LocalName(self) -> str:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def NamespaceURI(self) -> str:
        """"""
    @property
    def NextSibling(self) -> XmlNode:
        """"""
    @property
    def NodeType(self) -> XmlNodeType:
        """"""
    @property
    def OuterXml(self) -> str:
        """"""
    @property
    def OwnerDocument(self) -> XmlDocument:
        """"""
    @property
    def ParentNode(self) -> XmlNode:
        """"""
    @property
    def Prefix(self) -> str:
        """"""
    @Prefix.setter
    def Prefix(self, value: str) -> None: ...
    @property
    def PreviousSibling(self) -> XmlNode:
        """"""
    @property
    def PreviousText(self) -> XmlNode:
        """"""
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo:
        """"""
    @property
    def Value(self) -> str:
        """"""
    @Value.setter
    def Value(self, value: str) -> None: ...
    def AppendChild(self, newChild: XmlNode) -> XmlNode:
        """"""
    def Clone(self) -> XmlNode:
        """"""
    def CloneNode(self, deep: bool) -> XmlNode:
        """"""
    def CreateNavigator(self) -> XPathNavigator:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetAttribute(self, name: str) -> str:
        """"""
    @overload
    def GetAttribute(self, localName: str, namespaceURI: str) -> str:
        """"""
    @overload
    def GetAttributeNode(self, name: str) -> XmlAttribute:
        """"""
    @overload
    def GetAttributeNode(self, localName: str, namespaceURI: str) -> XmlAttribute:
        """"""
    @overload
    def GetElementsByTagName(self, name: str) -> XmlNodeList:
        """"""
    @overload
    def GetElementsByTagName(self, localName: str, namespaceURI: str) -> XmlNodeList:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetNamespaceOfPrefix(self, prefix: str) -> str:
        """"""
    def GetPrefixOfNamespace(self, namespaceURI: str) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def HasAttribute(self, name: str) -> bool:
        """"""
    @overload
    def HasAttribute(self, localName: str, namespaceURI: str) -> bool:
        """"""
    def InsertAfter(self, newChild: XmlNode, refChild: XmlNode) -> XmlNode:
        """"""
    def InsertBefore(self, newChild: XmlNode, refChild: XmlNode) -> XmlNode:
        """"""
    def Normalize(self) -> None:
        """"""
    def PrependChild(self, newChild: XmlNode) -> XmlNode:
        """"""
    def RemoveAll(self) -> None:
        """"""
    def RemoveAllAttributes(self) -> None:
        """"""
    @overload
    def RemoveAttribute(self, name: str) -> None:
        """"""
    @overload
    def RemoveAttribute(self, localName: str, namespaceURI: str) -> None:
        """"""
    def RemoveAttributeAt(self, i: int) -> XmlNode:
        """"""
    @overload
    def RemoveAttributeNode(self, oldAttr: XmlAttribute) -> XmlAttribute:
        """"""
    @overload
    def RemoveAttributeNode(self, localName: str, namespaceURI: str) -> XmlAttribute:
        """"""
    def RemoveChild(self, oldChild: XmlNode) -> XmlNode:
        """"""
    def ReplaceChild(self, newChild: XmlNode, oldChild: XmlNode) -> XmlNode:
        """"""
    @overload
    def SelectNodes(self, xpath: str) -> XmlNodeList:
        """"""
    @overload
    def SelectNodes(self, xpath: str, nsmgr: XmlNamespaceManager) -> XmlNodeList:
        """"""
    @overload
    def SelectSingleNode(self, xpath: str) -> XmlNode:
        """"""
    @overload
    def SelectSingleNode(self, xpath: str, nsmgr: XmlNamespaceManager) -> XmlNode:
        """"""
    @overload
    def SetAttribute(self, name: str, value: str) -> None:
        """"""
    @overload
    def SetAttribute(self, localName: str, namespaceURI: str, value: str) -> str:
        """"""
    @overload
    def SetAttributeNode(self, newAttr: XmlAttribute) -> XmlAttribute:
        """"""
    @overload
    def SetAttributeNode(self, localName: str, namespaceURI: str) -> XmlAttribute:
        """"""
    def Supports(self, feature: str, version: str) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteContentTo(self, w: XmlWriter) -> None:
        """"""
    def WriteTo(self, w: XmlWriter) -> None:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __getitem__(self, name: str) -> XmlElement:
        """"""
    @overload
    def __getitem__(self, localname: str, ns: str) -> XmlElement:
        """"""

class ConfigXmlSignificantWhitespace(
    XmlSignificantWhitespace, IEnumerable, IConfigErrorInfo, IXPathNavigable, ICloneable
):
    """"""
    def __init__(self, filename: str, line: int, strData: str, doc: XmlDocument) -> None:
        """"""
    @property
    def Attributes(self) -> XmlAttributeCollection:
        """"""
    @property
    def BaseURI(self) -> str:
        """"""
    @property
    def ChildNodes(self) -> XmlNodeList:
        """"""
    @property
    def Data(self) -> str:
        """"""
    @Data.setter
    def Data(self, value: str) -> None: ...
    @property
    def Filename(self) -> str:
        """"""
    @property
    def FirstChild(self) -> XmlNode:
        """"""
    @property
    def HasChildNodes(self) -> bool:
        """"""
    @property
    def InnerText(self) -> str:
        """"""
    @InnerText.setter
    def InnerText(self, value: str) -> None: ...
    @property
    def InnerXml(self) -> str:
        """"""
    @InnerXml.setter
    def InnerXml(self, value: str) -> None: ...
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def Item(self) -> XmlElement:
        """"""
    @property
    def LastChild(self) -> XmlNode:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def LineNumber(self) -> int:
        """"""
    @property
    def LocalName(self) -> str:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def NamespaceURI(self) -> str:
        """"""
    @property
    def NextSibling(self) -> XmlNode:
        """"""
    @property
    def NodeType(self) -> XmlNodeType:
        """"""
    @property
    def OuterXml(self) -> str:
        """"""
    @property
    def OwnerDocument(self) -> XmlDocument:
        """"""
    @property
    def ParentNode(self) -> XmlNode:
        """"""
    @property
    def Prefix(self) -> str:
        """"""
    @Prefix.setter
    def Prefix(self, value: str) -> None: ...
    @property
    def PreviousSibling(self) -> XmlNode:
        """"""
    @property
    def PreviousText(self) -> XmlNode:
        """"""
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo:
        """"""
    @property
    def Value(self) -> str:
        """"""
    @Value.setter
    def Value(self, value: str) -> None: ...
    def AppendChild(self, newChild: XmlNode) -> XmlNode:
        """"""
    def AppendData(self, strData: str) -> None:
        """"""
    def Clone(self) -> XmlNode:
        """"""
    def CloneNode(self, deep: bool) -> XmlNode:
        """"""
    def CreateNavigator(self) -> XPathNavigator:
        """"""
    def DeleteData(self, offset: int, count: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetNamespaceOfPrefix(self, prefix: str) -> str:
        """"""
    def GetPrefixOfNamespace(self, namespaceURI: str) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def InsertAfter(self, newChild: XmlNode, refChild: XmlNode) -> XmlNode:
        """"""
    def InsertBefore(self, newChild: XmlNode, refChild: XmlNode) -> XmlNode:
        """"""
    def InsertData(self, offset: int, strData: str) -> None:
        """"""
    def Normalize(self) -> None:
        """"""
    def PrependChild(self, newChild: XmlNode) -> XmlNode:
        """"""
    def RemoveAll(self) -> None:
        """"""
    def RemoveChild(self, oldChild: XmlNode) -> XmlNode:
        """"""
    def ReplaceChild(self, newChild: XmlNode, oldChild: XmlNode) -> XmlNode:
        """"""
    def ReplaceData(self, offset: int, count: int, strData: str) -> None:
        """"""
    @overload
    def SelectNodes(self, xpath: str) -> XmlNodeList:
        """"""
    @overload
    def SelectNodes(self, xpath: str, nsmgr: XmlNamespaceManager) -> XmlNodeList:
        """"""
    @overload
    def SelectSingleNode(self, xpath: str) -> XmlNode:
        """"""
    @overload
    def SelectSingleNode(self, xpath: str, nsmgr: XmlNamespaceManager) -> XmlNode:
        """"""
    def Substring(self, offset: int, count: int) -> str:
        """"""
    def Supports(self, feature: str, version: str) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteContentTo(self, w: XmlWriter) -> None:
        """"""
    def WriteTo(self, w: XmlWriter) -> None:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __getitem__(self, name: str) -> XmlElement:
        """"""
    @overload
    def __getitem__(self, localname: str, ns: str) -> XmlElement:
        """"""

class ConfigXmlText(XmlText, IEnumerable, IConfigErrorInfo, IXPathNavigable, ICloneable):
    """"""
    def __init__(self, filename: str, line: int, strData: str, doc: XmlDocument) -> None:
        """"""
    @property
    def Attributes(self) -> XmlAttributeCollection:
        """"""
    @property
    def BaseURI(self) -> str:
        """"""
    @property
    def ChildNodes(self) -> XmlNodeList:
        """"""
    @property
    def Data(self) -> str:
        """"""
    @Data.setter
    def Data(self, value: str) -> None: ...
    @property
    def Filename(self) -> str:
        """"""
    @property
    def FirstChild(self) -> XmlNode:
        """"""
    @property
    def HasChildNodes(self) -> bool:
        """"""
    @property
    def InnerText(self) -> str:
        """"""
    @InnerText.setter
    def InnerText(self, value: str) -> None: ...
    @property
    def InnerXml(self) -> str:
        """"""
    @InnerXml.setter
    def InnerXml(self, value: str) -> None: ...
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def Item(self) -> XmlElement:
        """"""
    @property
    def LastChild(self) -> XmlNode:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def LineNumber(self) -> int:
        """"""
    @property
    def LocalName(self) -> str:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def NamespaceURI(self) -> str:
        """"""
    @property
    def NextSibling(self) -> XmlNode:
        """"""
    @property
    def NodeType(self) -> XmlNodeType:
        """"""
    @property
    def OuterXml(self) -> str:
        """"""
    @property
    def OwnerDocument(self) -> XmlDocument:
        """"""
    @property
    def ParentNode(self) -> XmlNode:
        """"""
    @property
    def Prefix(self) -> str:
        """"""
    @Prefix.setter
    def Prefix(self, value: str) -> None: ...
    @property
    def PreviousSibling(self) -> XmlNode:
        """"""
    @property
    def PreviousText(self) -> XmlNode:
        """"""
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo:
        """"""
    @property
    def Value(self) -> str:
        """"""
    @Value.setter
    def Value(self, value: str) -> None: ...
    def AppendChild(self, newChild: XmlNode) -> XmlNode:
        """"""
    def AppendData(self, strData: str) -> None:
        """"""
    def Clone(self) -> XmlNode:
        """"""
    def CloneNode(self, deep: bool) -> XmlNode:
        """"""
    def CreateNavigator(self) -> XPathNavigator:
        """"""
    def DeleteData(self, offset: int, count: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetNamespaceOfPrefix(self, prefix: str) -> str:
        """"""
    def GetPrefixOfNamespace(self, namespaceURI: str) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def InsertAfter(self, newChild: XmlNode, refChild: XmlNode) -> XmlNode:
        """"""
    def InsertBefore(self, newChild: XmlNode, refChild: XmlNode) -> XmlNode:
        """"""
    def InsertData(self, offset: int, strData: str) -> None:
        """"""
    def Normalize(self) -> None:
        """"""
    def PrependChild(self, newChild: XmlNode) -> XmlNode:
        """"""
    def RemoveAll(self) -> None:
        """"""
    def RemoveChild(self, oldChild: XmlNode) -> XmlNode:
        """"""
    def ReplaceChild(self, newChild: XmlNode, oldChild: XmlNode) -> XmlNode:
        """"""
    def ReplaceData(self, offset: int, count: int, strData: str) -> None:
        """"""
    @overload
    def SelectNodes(self, xpath: str) -> XmlNodeList:
        """"""
    @overload
    def SelectNodes(self, xpath: str, nsmgr: XmlNamespaceManager) -> XmlNodeList:
        """"""
    @overload
    def SelectSingleNode(self, xpath: str) -> XmlNode:
        """"""
    @overload
    def SelectSingleNode(self, xpath: str, nsmgr: XmlNamespaceManager) -> XmlNode:
        """"""
    def SplitText(self, offset: int) -> XmlText:
        """"""
    def Substring(self, offset: int, count: int) -> str:
        """"""
    def Supports(self, feature: str, version: str) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteContentTo(self, w: XmlWriter) -> None:
        """"""
    def WriteTo(self, w: XmlWriter) -> None:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __getitem__(self, name: str) -> XmlElement:
        """"""
    @overload
    def __getitem__(self, localname: str, ns: str) -> XmlElement:
        """"""

class ConfigXmlWhitespace(
    XmlWhitespace, IEnumerable, IConfigErrorInfo, IXPathNavigable, ICloneable
):
    """"""
    def __init__(self, filename: str, line: int, comment: str, doc: XmlDocument) -> None:
        """"""
    @property
    def Attributes(self) -> XmlAttributeCollection:
        """"""
    @property
    def BaseURI(self) -> str:
        """"""
    @property
    def ChildNodes(self) -> XmlNodeList:
        """"""
    @property
    def Data(self) -> str:
        """"""
    @Data.setter
    def Data(self, value: str) -> None: ...
    @property
    def Filename(self) -> str:
        """"""
    @property
    def FirstChild(self) -> XmlNode:
        """"""
    @property
    def HasChildNodes(self) -> bool:
        """"""
    @property
    def InnerText(self) -> str:
        """"""
    @InnerText.setter
    def InnerText(self, value: str) -> None: ...
    @property
    def InnerXml(self) -> str:
        """"""
    @InnerXml.setter
    def InnerXml(self, value: str) -> None: ...
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def Item(self) -> XmlElement:
        """"""
    @property
    def LastChild(self) -> XmlNode:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def LineNumber(self) -> int:
        """"""
    @property
    def LocalName(self) -> str:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def NamespaceURI(self) -> str:
        """"""
    @property
    def NextSibling(self) -> XmlNode:
        """"""
    @property
    def NodeType(self) -> XmlNodeType:
        """"""
    @property
    def OuterXml(self) -> str:
        """"""
    @property
    def OwnerDocument(self) -> XmlDocument:
        """"""
    @property
    def ParentNode(self) -> XmlNode:
        """"""
    @property
    def Prefix(self) -> str:
        """"""
    @Prefix.setter
    def Prefix(self, value: str) -> None: ...
    @property
    def PreviousSibling(self) -> XmlNode:
        """"""
    @property
    def PreviousText(self) -> XmlNode:
        """"""
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo:
        """"""
    @property
    def Value(self) -> str:
        """"""
    @Value.setter
    def Value(self, value: str) -> None: ...
    def AppendChild(self, newChild: XmlNode) -> XmlNode:
        """"""
    def AppendData(self, strData: str) -> None:
        """"""
    def Clone(self) -> XmlNode:
        """"""
    def CloneNode(self, deep: bool) -> XmlNode:
        """"""
    def CreateNavigator(self) -> XPathNavigator:
        """"""
    def DeleteData(self, offset: int, count: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetNamespaceOfPrefix(self, prefix: str) -> str:
        """"""
    def GetPrefixOfNamespace(self, namespaceURI: str) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def InsertAfter(self, newChild: XmlNode, refChild: XmlNode) -> XmlNode:
        """"""
    def InsertBefore(self, newChild: XmlNode, refChild: XmlNode) -> XmlNode:
        """"""
    def InsertData(self, offset: int, strData: str) -> None:
        """"""
    def Normalize(self) -> None:
        """"""
    def PrependChild(self, newChild: XmlNode) -> XmlNode:
        """"""
    def RemoveAll(self) -> None:
        """"""
    def RemoveChild(self, oldChild: XmlNode) -> XmlNode:
        """"""
    def ReplaceChild(self, newChild: XmlNode, oldChild: XmlNode) -> XmlNode:
        """"""
    def ReplaceData(self, offset: int, count: int, strData: str) -> None:
        """"""
    @overload
    def SelectNodes(self, xpath: str) -> XmlNodeList:
        """"""
    @overload
    def SelectNodes(self, xpath: str, nsmgr: XmlNamespaceManager) -> XmlNodeList:
        """"""
    @overload
    def SelectSingleNode(self, xpath: str) -> XmlNode:
        """"""
    @overload
    def SelectSingleNode(self, xpath: str, nsmgr: XmlNamespaceManager) -> XmlNode:
        """"""
    def Substring(self, offset: int, count: int) -> str:
        """"""
    def Supports(self, feature: str, version: str) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def WriteContentTo(self, w: XmlWriter) -> None:
        """"""
    def WriteTo(self, w: XmlWriter) -> None:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __getitem__(self, name: str) -> XmlElement:
        """"""
    @overload
    def __getitem__(self, localname: str, ns: str) -> XmlElement:
        """"""

class ConfigurationException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, inner: Exception) -> None:
        """"""
    @overload
    def __init__(self, message: str, node: XmlNode) -> None:
        """"""
    @overload
    def __init__(self, message: str, inner: Exception, node: XmlNode) -> None:
        """"""
    @overload
    def __init__(self, message: str, filename: str, line: int) -> None:
        """"""
    @overload
    def __init__(self, message: str, inner: Exception, filename: str, line: int) -> None:
        """"""
    @property
    def BareMessage(self) -> str:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def Filename(self) -> str:
        """"""
    @property
    def HResult(self) -> int:
        """"""
    @property
    def HelpLink(self) -> str:
        """"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """"""
    @property
    def Line(self) -> int:
        """"""
    @property
    def Message(self) -> str:
        """"""
    @property
    def Source(self) -> str:
        """"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """"""
    @property
    def TargetSite(self) -> MethodBase:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseException(self) -> Exception:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def GetXmlNodeFilename(cls, node: XmlNode) -> str:
        """"""
    @classmethod
    def GetXmlNodeLineNumber(cls, node: XmlNode) -> int:
        """"""
    def ToString(self) -> str:
        """"""

class ConfigurationManagerInternalFactory(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ConfigurationSettings(Object):
    """"""
    @classmethod
    @property
    def AppSettings(cls) -> NameValueCollection:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetConfig(cls, sectionName: str) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DefaultSettingValueAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, value: str) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Value(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class DictionarySectionHandler(Object, IConfigurationSectionHandler):
    """"""
    def __init__(self) -> None:
        """"""
    def Create(self, parent: object, context: object, section: XmlNode) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class HandlerBase(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IApplicationSettingsProvider:
    """"""
    def GetPreviousVersion(
        self, context: SettingsContext, property: SettingsProperty
    ) -> SettingsPropertyValue:
        """"""
    def Reset(self, context: SettingsContext) -> None:
        """"""
    def Upgrade(self, context: SettingsContext, properties: SettingsPropertyCollection) -> None:
        """"""

class IConfigurationSectionHandler:
    """"""
    def Create(self, parent: object, configContext: object, section: XmlNode) -> object:
        """"""

class IConfigurationSystem:
    """"""
    def GetConfig(self, configKey: str) -> object:
        """"""
    def Init(self) -> None:
        """"""

class IPersistComponentSettings:
    """"""
    @property
    def SaveSettings(self) -> bool:
        """"""
    @SaveSettings.setter
    def SaveSettings(self, value: bool) -> None: ...
    @property
    def SettingsKey(self) -> str:
        """"""
    @SettingsKey.setter
    def SettingsKey(self, value: str) -> None: ...
    def LoadComponentSettings(self) -> None:
        """"""
    def ResetComponentSettings(self) -> None:
        """"""
    def SaveComponentSettings(self) -> None:
        """"""

class ISettingsProviderService:
    """"""
    def GetSettingsProvider(self, property: SettingsProperty) -> SettingsProvider:
        """"""

class IdnElement(ConfigurationElement):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def Enabled(self) -> UriIdnScope:
        """"""
    @Enabled.setter
    def Enabled(self, value: UriIdnScope) -> None: ...
    @property
    def LockAllAttributesExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAllElementsExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAttributes(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockElements(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockItem(self) -> bool:
        """"""
    @LockItem.setter
    def LockItem(self, value: bool) -> None: ...
    def Equals(self, compareTo: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class IgnoreSectionHandler(Object, IConfigurationSectionHandler):
    """"""
    def __init__(self) -> None:
        """"""
    def Create(self, parent: object, configContext: object, section: XmlNode) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IriParsingElement(ConfigurationElement):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def Enabled(self) -> bool:
        """"""
    @Enabled.setter
    def Enabled(self, value: bool) -> None: ...
    @property
    def LockAllAttributesExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAllElementsExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAttributes(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockElements(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockItem(self) -> bool:
        """"""
    @LockItem.setter
    def LockItem(self, value: bool) -> None: ...
    def Equals(self, compareTo: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class LocalFileSettingsProvider(SettingsProvider, IApplicationSettingsProvider):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def ApplicationName(self) -> str:
        """"""
    @ApplicationName.setter
    def ApplicationName(self, value: str) -> None: ...
    @property
    def Description(self) -> str:
        """"""
    @property
    def Name(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetPreviousVersion(
        self, context: SettingsContext, property: SettingsProperty
    ) -> SettingsPropertyValue:
        """"""
    def GetPropertyValues(
        self, context: SettingsContext, properties: SettingsPropertyCollection
    ) -> SettingsPropertyValueCollection:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self, name: str, values: NameValueCollection) -> None:
        """"""
    def Reset(self, context: SettingsContext) -> None:
        """"""
    def SetPropertyValues(
        self, context: SettingsContext, values: SettingsPropertyValueCollection
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Upgrade(self, context: SettingsContext, properties: SettingsPropertyCollection) -> None:
        """"""

class NameValueFileSectionHandler(Object, IConfigurationSectionHandler):
    """"""
    def __init__(self) -> None:
        """"""
    def Create(self, parent: object, configContext: object, section: XmlNode) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class NameValueSectionHandler(Object, IConfigurationSectionHandler):
    """"""
    def __init__(self) -> None:
        """"""
    def Create(self, parent: object, context: object, section: XmlNode) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class NoSettingsVersionUpgradeAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class PrivilegedConfigurationManager(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ReadOnlyNameValueCollection(
    NameValueCollection, ICollection, IEnumerable, IDeserializationCallback, ISerializable
):
    """"""
    @property
    def AllKeys(self) -> Array[str]:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> str:
        """"""
    @property
    def Keys(self) -> NameObjectCollectionBase.KeysCollection:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, c: NameValueCollection) -> None:
        """"""
    @overload
    def Add(self, name: str, value: str) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def CopyTo(self, dest: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Get(self, index: int) -> str:
        """"""
    @overload
    def Get(self, name: str) -> str:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetKey(self, index: int) -> str:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def GetValues(self, index: int) -> Array[str]:
        """"""
    @overload
    def GetValues(self, name: str) -> Array[str]:
        """"""
    def HasKeys(self) -> bool:
        """"""
    def OnDeserialization(self, sender: object) -> None:
        """"""
    def Remove(self, name: str) -> None:
        """"""
    def Set(self, name: str, value: str) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, name: str) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    @overload
    def __getitem__(self, index: int) -> str:
        """"""
    @overload
    def __getitem__(self, name: str) -> str:
        """"""
    def __setitem__(self, name: str, value: str) -> None:
        """"""
    class KeysCollection(Object, ICollection, IEnumerable):
        """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> str:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def Get(self, index: int) -> str:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> str:
            """"""

class SchemeSettingElement(ConfigurationElement):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def GenericUriParserOptions(self) -> GenericUriParserOptions:
        """"""
    @property
    def LockAllAttributesExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAllElementsExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAttributes(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockElements(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockItem(self) -> bool:
        """"""
    @LockItem.setter
    def LockItem(self, value: bool) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    def Equals(self, compareTo: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class SchemeSettingElementCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CollectionType(self) -> ConfigurationElementCollectionType:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def EmitClear(self) -> bool:
        """"""
    @EmitClear.setter
    def EmitClear(self, value: bool) -> None: ...
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> SchemeSettingElement:
        """"""
    @property
    def LockAllAttributesExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAllElementsExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAttributes(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockElements(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockItem(self) -> bool:
        """"""
    @LockItem.setter
    def LockItem(self, value: bool) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[ConfigurationElement], index: int) -> None:
        """"""
    def Equals(self, compareTo: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IndexOf(self, element: SchemeSettingElement) -> int:
        """"""
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""
    @overload
    def __getitem__(self, index: int) -> SchemeSettingElement:
        """"""
    @overload
    def __getitem__(self, name: str) -> SchemeSettingElement:
        """"""

class SchemeSettingInternal(Object):
    """"""
    def __init__(self, name: str, options: GenericUriParserOptions) -> None:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Options(self) -> GenericUriParserOptions:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SettingAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class SettingChangingEventArgs(CancelEventArgs):
    """"""
    def __init__(
        self, settingName: str, settingClass: str, settingKey: str, newValue: object, cancel: bool
    ) -> None:
        """"""
    @property
    def Cancel(self) -> bool:
        """"""
    @Cancel.setter
    def Cancel(self, value: bool) -> None: ...
    @property
    def NewValue(self) -> object:
        """"""
    @property
    def SettingClass(self) -> str:
        """"""
    @property
    def SettingKey(self) -> str:
        """"""
    @property
    def SettingName(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

SettingChangingEventHandler: Callable[[object, SettingChangingEventArgs], None] = ...
""""""

class SettingElement(ConfigurationElement):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, name: str, serializeAs: SettingsSerializeAs) -> None:
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def LockAllAttributesExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAllElementsExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAttributes(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockElements(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockItem(self) -> bool:
        """"""
    @LockItem.setter
    def LockItem(self, value: bool) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def SerializeAs(self) -> SettingsSerializeAs:
        """"""
    @SerializeAs.setter
    def SerializeAs(self, value: SettingsSerializeAs) -> None: ...
    @property
    def Value(self) -> SettingValueElement:
        """"""
    @Value.setter
    def Value(self, value: SettingValueElement) -> None: ...
    def Equals(self, settings: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class SettingElementCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CollectionType(self) -> ConfigurationElementCollectionType:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def EmitClear(self) -> bool:
        """"""
    @EmitClear.setter
    def EmitClear(self, value: bool) -> None: ...
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def LockAllAttributesExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAllElementsExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAttributes(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockElements(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockItem(self) -> bool:
        """"""
    @LockItem.setter
    def LockItem(self, value: bool) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    def Add(self, element: SettingElement) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[ConfigurationElement], index: int) -> None:
        """"""
    def Equals(self, compareTo: object) -> bool:
        """"""
    def Get(self, elementKey: str) -> SettingElement:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsReadOnly(self) -> bool:
        """"""
    def Remove(self, element: SettingElement) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, element: SettingElement) -> None:
        """"""
    def __len__(self) -> int:
        """"""

class SettingValueElement(ConfigurationElement):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def LockAllAttributesExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAllElementsExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAttributes(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockElements(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockItem(self) -> bool:
        """"""
    @LockItem.setter
    def LockItem(self, value: bool) -> None: ...
    @property
    def ValueXml(self) -> XmlNode:
        """"""
    @ValueXml.setter
    def ValueXml(self, value: XmlNode) -> None: ...
    def Equals(self, settingValue: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class SettingsAttributeDictionary(
    Hashtable,
    ICollection,
    IDictionary,
    IEnumerable,
    IDeserializationCallback,
    ISerializable,
    ICloneable,
):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, attributes: SettingsAttributeDictionary) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Keys(self) -> ICollection:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @property
    def Values(self) -> ICollection:
        """"""
    def Add(self, key: object, value: object) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Clone(self) -> object:
        """"""
    def Contains(self, key: object) -> bool:
        """"""
    def ContainsKey(self, key: object) -> bool:
        """"""
    def ContainsValue(self, value: object) -> bool:
        """"""
    def CopyTo(self, array: Array, arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IDictionaryEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def OnDeserialization(self, sender: object) -> None:
        """"""
    def Remove(self, key: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, key: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, key: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, key: object) -> object:
        """"""
    def __setitem__(self, key: object, value: object) -> None:
        """"""

class SettingsBase(ABC, Object):
    """"""
    @property
    def Context(self) -> SettingsContext:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Properties(self) -> SettingsPropertyCollection:
        """"""
    @property
    def PropertyValues(self) -> SettingsPropertyValueCollection:
        """"""
    @property
    def Providers(self) -> SettingsProviderCollection:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(
        self,
        context: SettingsContext,
        properties: SettingsPropertyCollection,
        providers: SettingsProviderCollection,
    ) -> None:
        """"""
    def Save(self) -> None:
        """"""
    @classmethod
    def Synchronized(cls, settingsBase: SettingsBase) -> SettingsBase:
        """"""
    def ToString(self) -> str:
        """"""
    def __getitem__(self, propertyName: str) -> object:
        """"""
    def __setitem__(self, propertyName: str, value: object) -> None:
        """"""

class SettingsContext(
    Hashtable,
    ICollection,
    IDictionary,
    IEnumerable,
    IDeserializationCallback,
    ISerializable,
    ICloneable,
):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Keys(self) -> ICollection:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @property
    def Values(self) -> ICollection:
        """"""
    def Add(self, key: object, value: object) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Clone(self) -> object:
        """"""
    def Contains(self, key: object) -> bool:
        """"""
    def ContainsKey(self, key: object) -> bool:
        """"""
    def ContainsValue(self, value: object) -> bool:
        """"""
    def CopyTo(self, array: Array, arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IDictionaryEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def OnDeserialization(self, sender: object) -> None:
        """"""
    def Remove(self, key: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, key: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, key: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, key: object) -> object:
        """"""
    def __setitem__(self, key: object, value: object) -> None:
        """"""

class SettingsDescriptionAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, description: str) -> None:
        """"""
    @property
    def Description(self) -> str:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class SettingsGroupDescriptionAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, description: str) -> None:
        """"""
    @property
    def Description(self) -> str:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class SettingsGroupNameAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, groupName: str) -> None:
        """"""
    @property
    def GroupName(self) -> str:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class SettingsLoadedEventArgs(EventArgs):
    """"""
    def __init__(self, provider: SettingsProvider) -> None:
        """"""
    @property
    def Provider(self) -> SettingsProvider:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

SettingsLoadedEventHandler: Callable[[object, SettingsLoadedEventArgs], None] = ...
""""""

class SettingsManageability(Enum):
    """"""

    Roaming: SettingsManageability = ...
    """"""

class SettingsManageabilityAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, manageability: SettingsManageability) -> None:
        """"""
    @property
    def Manageability(self) -> SettingsManageability:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class SettingsProperty(Object):
    """"""
    @overload
    def __init__(self, name: str) -> None:
        """"""
    @overload
    def __init__(
        self,
        name: str,
        propertyType: Type,
        provider: SettingsProvider,
        isReadOnly: bool,
        defaultValue: object,
        serializeAs: SettingsSerializeAs,
        attributes: SettingsAttributeDictionary,
        throwOnErrorDeserializing: bool,
        throwOnErrorSerializing: bool,
    ) -> None:
        """"""
    @overload
    def __init__(self, propertyToCopy: SettingsProperty) -> None:
        """"""
    @property
    def Attributes(self) -> SettingsAttributeDictionary:
        """"""
    @property
    def DefaultValue(self) -> object:
        """"""
    @DefaultValue.setter
    def DefaultValue(self, value: object) -> None: ...
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @IsReadOnly.setter
    def IsReadOnly(self, value: bool) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def PropertyType(self) -> Type:
        """"""
    @PropertyType.setter
    def PropertyType(self, value: Type) -> None: ...
    @property
    def Provider(self) -> SettingsProvider:
        """"""
    @Provider.setter
    def Provider(self, value: SettingsProvider) -> None: ...
    @property
    def SerializeAs(self) -> SettingsSerializeAs:
        """"""
    @SerializeAs.setter
    def SerializeAs(self, value: SettingsSerializeAs) -> None: ...
    @property
    def ThrowOnErrorDeserializing(self) -> bool:
        """"""
    @ThrowOnErrorDeserializing.setter
    def ThrowOnErrorDeserializing(self, value: bool) -> None: ...
    @property
    def ThrowOnErrorSerializing(self) -> bool:
        """"""
    @ThrowOnErrorSerializing.setter
    def ThrowOnErrorSerializing(self, value: bool) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SettingsPropertyCollection(Object, ICollection, IEnumerable, ICloneable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> SettingsProperty:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    def Add(self, property: SettingsProperty) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Clone(self) -> object:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove(self, name: str) -> None:
        """"""
    def SetReadOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, name: str) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, name: str) -> SettingsProperty:
        """"""

class SettingsPropertyIsReadOnlyException(Exception, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
        """"""
    @overload
    def __init__(self) -> None:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def HResult(self) -> int:
        """"""
    @property
    def HelpLink(self) -> str:
        """"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """"""
    @property
    def Message(self) -> str:
        """"""
    @property
    def Source(self) -> str:
        """"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """"""
    @property
    def TargetSite(self) -> MethodBase:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseException(self) -> Exception:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SettingsPropertyNotFoundException(Exception, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
        """"""
    @overload
    def __init__(self) -> None:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def HResult(self) -> int:
        """"""
    @property
    def HelpLink(self) -> str:
        """"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """"""
    @property
    def Message(self) -> str:
        """"""
    @property
    def Source(self) -> str:
        """"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """"""
    @property
    def TargetSite(self) -> MethodBase:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseException(self) -> Exception:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SettingsPropertyValue(Object):
    """"""
    def __init__(self, property: SettingsProperty) -> None:
        """"""
    @property
    def Deserialized(self) -> bool:
        """"""
    @Deserialized.setter
    def Deserialized(self, value: bool) -> None: ...
    @property
    def IsDirty(self) -> bool:
        """"""
    @IsDirty.setter
    def IsDirty(self, value: bool) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @property
    def Property(self) -> SettingsProperty:
        """"""
    @property
    def PropertyValue(self) -> object:
        """"""
    @PropertyValue.setter
    def PropertyValue(self, value: object) -> None: ...
    @property
    def SerializedValue(self) -> object:
        """"""
    @SerializedValue.setter
    def SerializedValue(self, value: object) -> None: ...
    @property
    def UsingDefaultValue(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SettingsPropertyValueCollection(Object, ICollection, IEnumerable, ICloneable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> SettingsPropertyValue:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    def Add(self, property: SettingsPropertyValue) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Clone(self) -> object:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove(self, name: str) -> None:
        """"""
    def SetReadOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, name: str) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, name: str) -> SettingsPropertyValue:
        """"""

class SettingsPropertyWrongTypeException(Exception, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
        """"""
    @overload
    def __init__(self) -> None:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def HResult(self) -> int:
        """"""
    @property
    def HelpLink(self) -> str:
        """"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """"""
    @property
    def Message(self) -> str:
        """"""
    @property
    def Source(self) -> str:
        """"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """"""
    @property
    def TargetSite(self) -> MethodBase:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseException(self) -> Exception:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SettingsProvider(ABC, ProviderBase):
    """"""
    @property
    def ApplicationName(self) -> str:
        """"""
    @ApplicationName.setter
    def ApplicationName(self, value: str) -> None: ...
    @property
    def Description(self) -> str:
        """"""
    @property
    def Name(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetPropertyValues(
        self, context: SettingsContext, collection: SettingsPropertyCollection
    ) -> SettingsPropertyValueCollection:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self, name: str, config: NameValueCollection) -> None:
        """"""
    def SetPropertyValues(
        self, context: SettingsContext, collection: SettingsPropertyValueCollection
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SettingsProviderAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, providerTypeName: str) -> None:
        """"""
    @overload
    def __init__(self, providerType: Type) -> None:
        """"""
    @property
    def ProviderTypeName(self) -> str:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class SettingsProviderCollection(ProviderCollection, ICollection, IEnumerable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> ProviderBase:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    def Add(self, provider: ProviderBase) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[ProviderBase], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove(self, name: str) -> None:
        """"""
    def SetReadOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, name: str) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, name: str) -> ProviderBase:
        """"""

SettingsSavingEventHandler: Callable[[object, CancelEventArgs], None] = ...
""""""

class SettingsSerializeAs(Enum):
    """"""

    String: SettingsSerializeAs = ...
    """"""
    Xml: SettingsSerializeAs = ...
    """"""
    Binary: SettingsSerializeAs = ...
    """"""
    ProviderSpecific: SettingsSerializeAs = ...
    """"""

class SettingsSerializeAsAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, serializeAs: SettingsSerializeAs) -> None:
        """"""
    @property
    def SerializeAs(self) -> SettingsSerializeAs:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class SingleTagSectionHandler(Object, IConfigurationSectionHandler):
    """"""
    def __init__(self) -> None:
        """"""
    def Create(self, parent: object, context: object, section: XmlNode) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SpecialSetting(Enum):
    """"""

    ConnectionString: SpecialSetting = ...
    """"""
    WebServiceUrl: SpecialSetting = ...
    """"""

class SpecialSettingAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, specialSetting: SpecialSetting) -> None:
        """"""
    @property
    def SpecialSetting(self) -> SpecialSetting:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class StoredSetting(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TypeUtil(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class UriSection(ConfigurationSection):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def Idn(self) -> IdnElement:
        """"""
    @property
    def IriParsing(self) -> IriParsingElement:
        """"""
    @property
    def LockAllAttributesExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAllElementsExcept(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockAttributes(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockElements(self) -> ConfigurationLockCollection:
        """"""
    @property
    def LockItem(self) -> bool:
        """"""
    @LockItem.setter
    def LockItem(self, value: bool) -> None: ...
    @property
    def SchemeSettings(self) -> SchemeSettingElementCollection:
        """"""
    @property
    def SectionInformation(self) -> SectionInformation:
        """"""
    def Equals(self, compareTo: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class UriSectionData(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def IdnScope(self) -> UriIdnScope | None:
        """"""
    @IdnScope.setter
    def IdnScope(self, value: UriIdnScope | None) -> None: ...
    @property
    def IriParsing(self) -> bool | None:
        """"""
    @IriParsing.setter
    def IriParsing(self, value: bool | None) -> None: ...
    @property
    def SchemeSettings(self) -> Dictionary[str, SchemeSettingInternal]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class UriSectionInternal(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class UriSectionReader(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def Read(cls, configFilePath: str) -> UriSectionData:
        """"""
    @classmethod
    @overload
    def Read(cls, configFilePath: str, parentData: UriSectionData) -> UriSectionData:
        """"""
    def ToString(self) -> str:
        """"""

class UserScopedSettingAttribute(SettingAttribute, _Attribute):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class UserSettingsGroup(ConfigurationSectionGroup):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def IsDeclarationRequired(self) -> bool:
        """"""
    @property
    def IsDeclared(self) -> bool:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def SectionGroupName(self) -> str:
        """"""
    @property
    def SectionGroups(self) -> ConfigurationSectionGroupCollection:
        """"""
    @property
    def Sections(self) -> ConfigurationSectionCollection:
        """"""
    @property
    def Type(self) -> str:
        """"""
    @Type.setter
    def Type(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def ForceDeclaration(self) -> None:
        """"""
    @overload
    def ForceDeclaration(self, force: bool) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
