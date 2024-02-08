from __future__ import annotations

from abc import ABC
from typing import Callable
from typing import Generic
from typing import Iterator
from typing import Optional
from typing import Tuple
from typing import TypeVar
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
from System import UriIdnScope
from System import ValueType
from System.Collections import Hashtable
from System.Collections import ICollection
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections.Generic import Dictionary
from System.Collections.Specialized import NameValueCollection
from System.Collections.Specialized.NameObjectCollectionBase import KeysCollection
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

T = TypeVar("T")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

class AppSettingsReader(Object):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetValue(self, key: str, type: Type) -> object:
        """

        :param key:
        :param type:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ApplicationScopedSettingAttribute(SettingAttribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ApplicationSettingsBase(ABC, SettingsBase, INotifyPropertyChanged):
    """"""

    @property
    def Context(self) -> SettingsContext:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Properties(self) -> SettingsPropertyCollection:
        """

        :return:
        """
    @property
    def PropertyValues(self) -> SettingsPropertyValueCollection:
        """

        :return:
        """
    @property
    def Providers(self) -> SettingsProviderCollection:
        """

        :return:
        """
    @property
    def SettingsKey(self) -> str:
        """

        :return:
        """
    @SettingsKey.setter
    def SettingsKey(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetPreviousVersion(self, propertyName: str) -> object:
        """

        :param propertyName:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(
        self,
        context: SettingsContext,
        properties: SettingsPropertyCollection,
        providers: SettingsProviderCollection,
    ) -> None:
        """

        :param context:
        :param properties:
        :param providers:
        """
    def Reload(self) -> None:
        """"""
    def Reset(self) -> None:
        """"""
    def Save(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def Upgrade(self) -> None:
        """"""
    def __getitem__(self, propertyName: str) -> object:
        """

        :param propertyName:
        :return:
        """
    def __setitem__(self, propertyName: str, value: object) -> None:
        """

        :param propertyName:
        :param value:
        """
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

    def __init__(self):
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
        """

        :param obj:
        :return:
        """
    @overload
    def ForceDeclaration(self) -> None:
        """"""
    @overload
    def ForceDeclaration(self, force: bool) -> None:
        """"""
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ClientSettingsSection(ConfigurationSection):
    """"""

    def __init__(self):
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
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class ClientSettingsStore(Object):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CommonConfigurationStrings(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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
    ):
        """

        :param filename:
        :param line:
        :param prefix:
        :param localName:
        :param namespaceUri:
        :param doc:
        """
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
    def Clone(self) -> object:
        """

        :return:
        """
    def CloneNode(self, deep: bool) -> XmlNode:
        """"""
    def CreateNavigator(self) -> XPathNavigator:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetNamespaceOfPrefix(self, prefix: str) -> str:
        """"""
    def GetPrefixOfNamespace(self, namespaceURI: str) -> str:
        """"""
    def GetType(self) -> Type:
        """

        :return:
        """
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
        """

        :return:
        """
    def WriteContentTo(self, w: XmlWriter) -> None:
        """"""
    def WriteTo(self, w: XmlWriter) -> None:
        """"""
    @overload
    def __getitem__(self, name: str) -> XmlElement:
        """"""
    @overload
    def __getitem__(self, localname: str, ns: str) -> XmlElement:
        """"""
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """

class ConfigXmlCDataSection(
    XmlCDataSection, IEnumerable, IConfigErrorInfo, IXPathNavigable, ICloneable
):
    """"""

    def __init__(self, filename: str, line: int, data: str, doc: XmlDocument):
        """

        :param filename:
        :param line:
        :param data:
        :param doc:
        """
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
    def Clone(self) -> object:
        """

        :return:
        """
    def CloneNode(self, deep: bool) -> XmlNode:
        """"""
    def CreateNavigator(self) -> XPathNavigator:
        """"""
    def DeleteData(self, offset: int, count: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetNamespaceOfPrefix(self, prefix: str) -> str:
        """"""
    def GetPrefixOfNamespace(self, namespaceURI: str) -> str:
        """"""
    def GetType(self) -> Type:
        """

        :return:
        """
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
        """

        :return:
        """
    def WriteContentTo(self, w: XmlWriter) -> None:
        """"""
    def WriteTo(self, w: XmlWriter) -> None:
        """"""
    @overload
    def __getitem__(self, name: str) -> XmlElement:
        """"""
    @overload
    def __getitem__(self, localname: str, ns: str) -> XmlElement:
        """"""
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """

class ConfigXmlComment(XmlComment, IEnumerable, IConfigErrorInfo, IXPathNavigable, ICloneable):
    """"""

    def __init__(self, filename: str, line: int, comment: str, doc: XmlDocument):
        """

        :param filename:
        :param line:
        :param comment:
        :param doc:
        """
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
    def Clone(self) -> object:
        """

        :return:
        """
    def CloneNode(self, deep: bool) -> XmlNode:
        """"""
    def CreateNavigator(self) -> XPathNavigator:
        """"""
    def DeleteData(self, offset: int, count: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetNamespaceOfPrefix(self, prefix: str) -> str:
        """"""
    def GetPrefixOfNamespace(self, namespaceURI: str) -> str:
        """"""
    def GetType(self) -> Type:
        """

        :return:
        """
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
        """

        :return:
        """
    def WriteContentTo(self, w: XmlWriter) -> None:
        """"""
    def WriteTo(self, w: XmlWriter) -> None:
        """"""
    @overload
    def __getitem__(self, name: str) -> XmlElement:
        """"""
    @overload
    def __getitem__(self, localname: str, ns: str) -> XmlElement:
        """"""
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """

class ConfigXmlDocument(XmlDocument, IEnumerable, IConfigErrorInfo, IXPathNavigable, ICloneable):
    """"""

    def __init__(self):
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
    def Clone(self) -> object:
        """

        :return:
        """
    def CloneNode(self, deep: bool) -> XmlNode:
        """"""
    @overload
    def CreateAttribute(self, name: str) -> XmlAttribute:
        """"""
    @overload
    def CreateAttribute(self, qualifiedName: str, namespaceURI: str) -> XmlAttribute:
        """"""
    @overload
    def CreateAttribute(self, prefix: str, localName: str, namespaceURI: str) -> XmlAttribute:
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
    def CreateElement(self, prefix: str, localName: str, namespaceURI: str) -> XmlElement:
        """"""
    def CreateEntityReference(self, name: str) -> XmlEntityReference:
        """"""
    def CreateNavigator(self) -> XPathNavigator:
        """"""
    @overload
    def CreateNode(self, type: XmlNodeType, name: str, namespaceURI: str) -> XmlNode:
        """"""
    @overload
    def CreateNode(self, nodeTypeString: str, name: str, namespaceURI: str) -> XmlNode:
        """"""
    @overload
    def CreateNode(self, type: XmlNodeType, prefix: str, name: str, namespaceURI: str) -> XmlNode:
        """"""
    def CreateProcessingInstruction(self, target: str, data: str) -> XmlProcessingInstruction:
        """"""
    def CreateSignificantWhitespace(self, text: str) -> XmlSignificantWhitespace:
        """"""
    def CreateTextNode(self, text: str) -> XmlText:
        """"""
    def CreateWhitespace(self, text: str) -> XmlWhitespace:
        """"""
    def CreateXmlDeclaration(self, version: str, encoding: str, standalone: str) -> XmlDeclaration:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetElementById(self, elementId: str) -> XmlElement:
        """"""
    @overload
    def GetElementsByTagName(self, name: str) -> XmlNodeList:
        """"""
    @overload
    def GetElementsByTagName(self, localName: str, namespaceURI: str) -> XmlNodeList:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetNamespaceOfPrefix(self, prefix: str) -> str:
        """"""
    def GetPrefixOfNamespace(self, namespaceURI: str) -> str:
        """"""
    def GetType(self) -> Type:
        """

        :return:
        """
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
        """

        :param filename:
        :param sourceReader:
        """
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
        """

        :return:
        """
    @overload
    def Validate(self, validationEventHandler: ValidationEventHandler) -> None:
        """"""
    @overload
    def Validate(
        self, validationEventHandler: ValidationEventHandler, nodeToValidate: XmlNode
    ) -> None:
        """"""
    def WriteContentTo(self, w: XmlWriter) -> None:
        """"""
    def WriteTo(self, w: XmlWriter) -> None:
        """"""
    @overload
    def __getitem__(self, name: str) -> XmlElement:
        """"""
    @overload
    def __getitem__(self, localname: str, ns: str) -> XmlElement:
        """"""
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
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
    ):
        """

        :param filename:
        :param line:
        :param prefix:
        :param localName:
        :param namespaceUri:
        :param doc:
        """
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
    def Clone(self) -> object:
        """

        :return:
        """
    def CloneNode(self, deep: bool) -> XmlNode:
        """"""
    def CreateNavigator(self) -> XPathNavigator:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
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
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetNamespaceOfPrefix(self, prefix: str) -> str:
        """"""
    def GetPrefixOfNamespace(self, namespaceURI: str) -> str:
        """"""
    def GetType(self) -> Type:
        """

        :return:
        """
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
        """

        :return:
        """
    def WriteContentTo(self, w: XmlWriter) -> None:
        """"""
    def WriteTo(self, w: XmlWriter) -> None:
        """"""
    @overload
    def __getitem__(self, name: str) -> XmlElement:
        """"""
    @overload
    def __getitem__(self, localname: str, ns: str) -> XmlElement:
        """"""
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """

class ConfigXmlSignificantWhitespace(
    XmlSignificantWhitespace, IEnumerable, IConfigErrorInfo, IXPathNavigable, ICloneable
):
    """"""

    def __init__(self, filename: str, line: int, strData: str, doc: XmlDocument):
        """

        :param filename:
        :param line:
        :param strData:
        :param doc:
        """
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
    def Clone(self) -> object:
        """

        :return:
        """
    def CloneNode(self, deep: bool) -> XmlNode:
        """"""
    def CreateNavigator(self) -> XPathNavigator:
        """"""
    def DeleteData(self, offset: int, count: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetNamespaceOfPrefix(self, prefix: str) -> str:
        """"""
    def GetPrefixOfNamespace(self, namespaceURI: str) -> str:
        """"""
    def GetType(self) -> Type:
        """

        :return:
        """
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
        """

        :return:
        """
    def WriteContentTo(self, w: XmlWriter) -> None:
        """"""
    def WriteTo(self, w: XmlWriter) -> None:
        """"""
    @overload
    def __getitem__(self, name: str) -> XmlElement:
        """"""
    @overload
    def __getitem__(self, localname: str, ns: str) -> XmlElement:
        """"""
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """

class ConfigXmlText(XmlText, IEnumerable, IConfigErrorInfo, IXPathNavigable, ICloneable):
    """"""

    def __init__(self, filename: str, line: int, strData: str, doc: XmlDocument):
        """

        :param filename:
        :param line:
        :param strData:
        :param doc:
        """
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
    def Clone(self) -> object:
        """

        :return:
        """
    def CloneNode(self, deep: bool) -> XmlNode:
        """"""
    def CreateNavigator(self) -> XPathNavigator:
        """"""
    def DeleteData(self, offset: int, count: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetNamespaceOfPrefix(self, prefix: str) -> str:
        """"""
    def GetPrefixOfNamespace(self, namespaceURI: str) -> str:
        """"""
    def GetType(self) -> Type:
        """

        :return:
        """
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
        """

        :return:
        """
    def WriteContentTo(self, w: XmlWriter) -> None:
        """"""
    def WriteTo(self, w: XmlWriter) -> None:
        """"""
    @overload
    def __getitem__(self, name: str) -> XmlElement:
        """"""
    @overload
    def __getitem__(self, localname: str, ns: str) -> XmlElement:
        """"""
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """

class ConfigXmlWhitespace(
    XmlWhitespace, IEnumerable, IConfigErrorInfo, IXPathNavigable, ICloneable
):
    """"""

    def __init__(self, filename: str, line: int, comment: str, doc: XmlDocument):
        """

        :param filename:
        :param line:
        :param comment:
        :param doc:
        """
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
    def Clone(self) -> object:
        """

        :return:
        """
    def CloneNode(self, deep: bool) -> XmlNode:
        """"""
    def CreateNavigator(self) -> XPathNavigator:
        """"""
    def DeleteData(self, offset: int, count: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetNamespaceOfPrefix(self, prefix: str) -> str:
        """"""
    def GetPrefixOfNamespace(self, namespaceURI: str) -> str:
        """"""
    def GetType(self) -> Type:
        """

        :return:
        """
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
        """

        :return:
        """
    def WriteContentTo(self, w: XmlWriter) -> None:
        """"""
    def WriteTo(self, w: XmlWriter) -> None:
        """"""
    @overload
    def __getitem__(self, name: str) -> XmlElement:
        """"""
    @overload
    def __getitem__(self, localname: str, ns: str) -> XmlElement:
        """"""
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """

class ConfigurationException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """

        :param message:
        """
    @overload
    def __init__(self, message: str, node: XmlNode):
        """

        :param message:
        :param node:
        """
    @overload
    def __init__(self, message: str, inner: Exception):
        """

        :param message:
        :param inner:
        """
    @overload
    def __init__(self, message: str, inner: Exception, node: XmlNode):
        """

        :param message:
        :param inner:
        :param node:
        """
    @overload
    def __init__(self, message: str, filename: str, line: int):
        """

        :param message:
        :param filename:
        :param line:
        """
    @overload
    def __init__(self, message: str, inner: Exception, filename: str, line: int):
        """

        :param message:
        :param inner:
        :param filename:
        :param line:
        """
    @property
    def BareMessage(self) -> str:
        """

        :return:
        """
    @property
    def Data(self) -> IDictionary:
        """

        :return:
        """
    @property
    def Filename(self) -> str:
        """

        :return:
        """
    @property
    def HResult(self) -> int:
        """

        :return:
        """
    @property
    def HelpLink(self) -> str:
        """

        :return:
        """
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """

        :return:
        """
    @property
    def Line(self) -> int:
        """

        :return:
        """
    @property
    def Message(self) -> str:
        """

        :return:
        """
    @property
    def Source(self) -> str:
        """

        :return:
        """
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """

        :return:
        """
    @property
    def TargetSite(self) -> MethodBase:
        """

        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def GetXmlNodeFilename(cls, node: XmlNode) -> str:
        """

        :param node:
        :return:
        """
    @classmethod
    def GetXmlNodeLineNumber(cls, node: XmlNode) -> int:
        """

        :param node:
        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class ConfigurationManagerInternalFactory(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ConfigurationSettings(Object):
    """"""

    @classmethod
    @property
    def AppSettings(cls) -> NameValueCollection:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def GetConfig(cls, sectionName: str) -> object:
        """

        :param sectionName:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DefaultSettingValueAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, value: str):
        """

        :param value:
        """
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Value(self) -> str:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DictionarySectionHandler(Object, IConfigurationSectionHandler):
    """"""

    def __init__(self):
        """"""
    def Create(self, parent: object, configContext: object, section: XmlNode) -> object:
        """

        :param parent:
        :param configContext:
        :param section:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class HandlerBase(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class IApplicationSettingsProvider:
    """"""

    def GetPreviousVersion(
        self, context: SettingsContext, property: SettingsProperty
    ) -> SettingsPropertyValue:
        """

        :param context:
        :param property:
        :return:
        """
    def Reset(self, context: SettingsContext) -> None:
        """

        :param context:
        """
    def Upgrade(self, context: SettingsContext, properties: SettingsPropertyCollection) -> None:
        """

        :param context:
        :param properties:
        """

class IConfigurationSectionHandler:
    """"""

    def Create(self, parent: object, configContext: object, section: XmlNode) -> object:
        """

        :param parent:
        :param configContext:
        :param section:
        :return:
        """

class IConfigurationSystem:
    """"""

    def GetConfig(self, configKey: str) -> object:
        """

        :param configKey:
        :return:
        """
    def Init(self) -> None:
        """"""

class IPersistComponentSettings:
    """"""

    @property
    def SaveSettings(self) -> bool:
        """

        :return:
        """
    @SaveSettings.setter
    def SaveSettings(self, value: bool) -> None: ...
    @property
    def SettingsKey(self) -> str:
        """

        :return:
        """
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
        """

        :param property:
        :return:
        """

class IdnElement(ConfigurationElement):
    """"""

    def __init__(self):
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def Enabled(self) -> UriIdnScope:
        """

        :return:
        """
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
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class IgnoreSectionHandler(Object, IConfigurationSectionHandler):
    """"""

    def __init__(self):
        """"""
    def Create(self, parent: object, configContext: object, section: XmlNode) -> object:
        """

        :param parent:
        :param configContext:
        :param section:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class IriParsingElement(ConfigurationElement):
    """"""

    def __init__(self):
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def Enabled(self) -> bool:
        """

        :return:
        """
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
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class LocalFileSettingsProvider(SettingsProvider, IApplicationSettingsProvider):
    """"""

    def __init__(self):
        """"""
    @property
    def ApplicationName(self) -> str:
        """

        :return:
        """
    @ApplicationName.setter
    def ApplicationName(self, value: str) -> None: ...
    @property
    def Description(self) -> str:
        """"""
    @property
    def Name(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetPreviousVersion(
        self, context: SettingsContext, property: SettingsProperty
    ) -> SettingsPropertyValue:
        """

        :param context:
        :param property:
        :return:
        """
    def GetPropertyValues(
        self, context: SettingsContext, collection: SettingsPropertyCollection
    ) -> SettingsPropertyValueCollection:
        """

        :param context:
        :param collection:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self, name: str, config: NameValueCollection) -> None:
        """"""
    def Reset(self, context: SettingsContext) -> None:
        """

        :param context:
        """
    def SetPropertyValues(
        self, context: SettingsContext, collection: SettingsPropertyValueCollection
    ) -> None:
        """

        :param context:
        :param collection:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Upgrade(self, context: SettingsContext, properties: SettingsPropertyCollection) -> None:
        """

        :param context:
        :param properties:
        """

class NameValueFileSectionHandler(Object, IConfigurationSectionHandler):
    """"""

    def __init__(self):
        """"""
    def Create(self, parent: object, configContext: object, section: XmlNode) -> object:
        """

        :param parent:
        :param configContext:
        :param section:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class NameValueSectionHandler(Object, IConfigurationSectionHandler):
    """"""

    def __init__(self):
        """"""
    def Create(self, parent: object, configContext: object, section: XmlNode) -> object:
        """

        :param parent:
        :param configContext:
        :param section:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class NoSettingsVersionUpgradeAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class PrivilegedConfigurationManager(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ReadOnlyNameValueCollection(
    NameValueCollection, ICollection, IEnumerable, IDeserializationCallback, ISerializable
):
    """"""

    @property
    def AllKeys(self) -> Array[str]:
        """

        :return:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> str:
        """

        :return:
        """
    @property
    def Keys(self) -> NameObjectCollectionBase.KeysCollection:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, c: NameValueCollection) -> None:
        """

        :param c:
        """
    @overload
    def Add(self, name: str, value: str) -> None:
        """

        :param name:
        :param value:
        """
    def Clear(self) -> None:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Get(self, index: int) -> str:
        """

        :param index:
        :return:
        """
    @overload
    def Get(self, name: str) -> str:
        """

        :param name:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetKey(self, index: int) -> str:
        """

        :param index:
        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetValues(self, index: int) -> Array[str]:
        """

        :param index:
        :return:
        """
    @overload
    def GetValues(self, name: str) -> Array[str]:
        """

        :param name:
        :return:
        """
    def HasKeys(self) -> bool:
        """

        :return:
        """
    def OnDeserialization(self, sender: object) -> None:
        """

        :param sender:
        """
    def Remove(self, name: str) -> None:
        """

        :param name:
        """
    def Set(self, name: str, value: str) -> None:
        """

        :param name:
        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> str:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, name: str) -> str:
        """

        :param name:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    def __setitem__(self, name: str, value: str) -> None:
        """

        :param name:
        :param value:
        """

class SchemeSettingElement(ConfigurationElement):
    """"""

    def __init__(self):
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def GenericUriParserOptions(self) -> GenericUriParserOptions:
        """

        :return:
        """
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
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SchemeSettingElementCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    """"""

    def __init__(self):
        """"""
    @property
    def CollectionType(self) -> ConfigurationElementCollectionType:
        """"""
    @property
    def Count(self) -> int:
        """

        :return:
        """
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
        """

        :return:
        """
    @property
    def Item(self) -> SchemeSettingElement:
        """

        :return:
        """
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
        """

        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[ConfigurationElement], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def IndexOf(self, element: SchemeSettingElement) -> int:
        """

        :param element:
        :return:
        """
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> SchemeSettingElement:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, name: str) -> SchemeSettingElement:
        """

        :param name:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

class SchemeSettingInternal(Object):
    """"""

    def __init__(self, name: str, options: GenericUriParserOptions):
        """

        :param name:
        :param options:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Options(self) -> GenericUriParserOptions:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SettingAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SettingChangingEventArgs(CancelEventArgs):
    """"""

    def __init__(
        self, settingName: str, settingClass: str, settingKey: str, newValue: object, cancel: bool
    ):
        """

        :param settingName:
        :param settingClass:
        :param settingKey:
        :param newValue:
        :param cancel:
        """
    @property
    def Cancel(self) -> bool:
        """

        :return:
        """
    @Cancel.setter
    def Cancel(self, value: bool) -> None: ...
    @property
    def NewValue(self) -> object:
        """

        :return:
        """
    @property
    def SettingClass(self) -> str:
        """

        :return:
        """
    @property
    def SettingKey(self) -> str:
        """

        :return:
        """
    @property
    def SettingName(self) -> str:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

SettingChangingEventHandler: Callable[[object, SettingChangingEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class SettingElement(ConfigurationElement):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, name: str, serializeAs: SettingsSerializeAs):
        """

        :param name:
        :param serializeAs:
        """
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
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def SerializeAs(self) -> SettingsSerializeAs:
        """

        :return:
        """
    @SerializeAs.setter
    def SerializeAs(self, value: SettingsSerializeAs) -> None: ...
    @property
    def Value(self) -> SettingValueElement:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: SettingValueElement) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SettingElementCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    """"""

    def __init__(self):
        """"""
    @property
    def CollectionType(self) -> ConfigurationElementCollectionType:
        """"""
    @property
    def Count(self) -> int:
        """

        :return:
        """
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
        """

        :return:
        """
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
        """

        :return:
        """
    def Add(self, element: SettingElement) -> None:
        """

        :param element:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[ConfigurationElement], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Get(self, elementKey: str) -> SettingElement:
        """

        :param elementKey:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def IsReadOnly(self) -> bool:
        """"""
    def Remove(self, element: SettingElement) -> None:
        """

        :param element:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

class SettingValueElement(ConfigurationElement):
    """"""

    def __init__(self):
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
        """

        :return:
        """
    @ValueXml.setter
    def ValueXml(self, value: XmlNode) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

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
    def __init__(self):
        """"""
    @overload
    def __init__(self, attributes: SettingsAttributeDictionary):
        """

        :param attributes:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Keys(self) -> ICollection:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @property
    def Values(self) -> ICollection:
        """

        :return:
        """
    def Add(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """
    def Clear(self) -> None:
        """"""
    def Clone(self) -> object:
        """

        :return:
        """
    def Contains(self, key: object) -> bool:
        """

        :param key:
        :return:
        """
    def ContainsKey(self, key: object) -> bool:
        """

        :param key:
        :return:
        """
    def ContainsValue(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def OnDeserialization(self, sender: object) -> None:
        """

        :param sender:
        """
    def Remove(self, key: object) -> None:
        """

        :param key:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, key: object) -> object:
        """

        :param key:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    def __setitem__(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """

class SettingsBase(ABC, Object):
    """"""

    @property
    def Context(self) -> SettingsContext:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Properties(self) -> SettingsPropertyCollection:
        """

        :return:
        """
    @property
    def PropertyValues(self) -> SettingsPropertyValueCollection:
        """

        :return:
        """
    @property
    def Providers(self) -> SettingsProviderCollection:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(
        self,
        context: SettingsContext,
        properties: SettingsPropertyCollection,
        providers: SettingsProviderCollection,
    ) -> None:
        """

        :param context:
        :param properties:
        :param providers:
        """
    def Save(self) -> None:
        """"""
    @classmethod
    def Synchronized(cls, settingsBase: SettingsBase) -> SettingsBase:
        """

        :param settingsBase:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __getitem__(self, propertyName: str) -> object:
        """

        :param propertyName:
        :return:
        """
    def __setitem__(self, propertyName: str, value: object) -> None:
        """

        :param propertyName:
        :param value:
        """

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

    def __init__(self):
        """"""
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Keys(self) -> ICollection:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @property
    def Values(self) -> ICollection:
        """

        :return:
        """
    def Add(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """
    def Clear(self) -> None:
        """"""
    def Clone(self) -> object:
        """

        :return:
        """
    def Contains(self, key: object) -> bool:
        """

        :param key:
        :return:
        """
    def ContainsKey(self, key: object) -> bool:
        """

        :param key:
        :return:
        """
    def ContainsValue(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def OnDeserialization(self, sender: object) -> None:
        """

        :param sender:
        """
    def Remove(self, key: object) -> None:
        """

        :param key:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, key: object) -> object:
        """

        :param key:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    def __setitem__(self, key: object, value: object) -> None:
        """

        :param key:
        :param value:
        """

class SettingsDescriptionAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, description: str):
        """

        :param description:
        """
    @property
    def Description(self) -> str:
        """

        :return:
        """
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SettingsGroupDescriptionAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, description: str):
        """

        :param description:
        """
    @property
    def Description(self) -> str:
        """

        :return:
        """
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SettingsGroupNameAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, groupName: str):
        """

        :param groupName:
        """
    @property
    def GroupName(self) -> str:
        """

        :return:
        """
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SettingsLoadedEventArgs(EventArgs):
    """"""

    def __init__(self, provider: SettingsProvider):
        """

        :param provider:
        """
    @property
    def Provider(self) -> SettingsProvider:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

SettingsLoadedEventHandler: Callable[[object, SettingsLoadedEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class SettingsManageability(Enum):
    """"""

    Roaming: SettingsManageability = ...
    """"""

class SettingsManageabilityAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, manageability: SettingsManageability):
        """

        :param manageability:
        """
    @property
    def Manageability(self) -> SettingsManageability:
        """

        :return:
        """
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SettingsProperty(Object):
    """"""

    @overload
    def __init__(self, propertyToCopy: SettingsProperty):
        """

        :param propertyToCopy:
        """
    @overload
    def __init__(self, name: str):
        """

        :param name:
        """
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
    ):
        """

        :param name:
        :param propertyType:
        :param provider:
        :param isReadOnly:
        :param defaultValue:
        :param serializeAs:
        :param attributes:
        :param throwOnErrorDeserializing:
        :param throwOnErrorSerializing:
        """
    @property
    def Attributes(self) -> SettingsAttributeDictionary:
        """

        :return:
        """
    @property
    def DefaultValue(self) -> object:
        """

        :return:
        """
    @DefaultValue.setter
    def DefaultValue(self, value: object) -> None: ...
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @IsReadOnly.setter
    def IsReadOnly(self, value: bool) -> None: ...
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def PropertyType(self) -> Type:
        """

        :return:
        """
    @PropertyType.setter
    def PropertyType(self, value: Type) -> None: ...
    @property
    def Provider(self) -> SettingsProvider:
        """

        :return:
        """
    @Provider.setter
    def Provider(self, value: SettingsProvider) -> None: ...
    @property
    def SerializeAs(self) -> SettingsSerializeAs:
        """

        :return:
        """
    @SerializeAs.setter
    def SerializeAs(self, value: SettingsSerializeAs) -> None: ...
    @property
    def ThrowOnErrorDeserializing(self) -> bool:
        """

        :return:
        """
    @ThrowOnErrorDeserializing.setter
    def ThrowOnErrorDeserializing(self, value: bool) -> None: ...
    @property
    def ThrowOnErrorSerializing(self) -> bool:
        """

        :return:
        """
    @ThrowOnErrorSerializing.setter
    def ThrowOnErrorSerializing(self, value: bool) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SettingsPropertyCollection(Object, ICollection, IEnumerable, ICloneable):
    """"""

    def __init__(self):
        """"""
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> SettingsProperty:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    def Add(self, property: SettingsProperty) -> None:
        """

        :param property:
        """
    def Clear(self) -> None:
        """"""
    def Clone(self) -> object:
        """

        :return:
        """
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Remove(self, name: str) -> None:
        """

        :param name:
        """
    def SetReadOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, name: str) -> SettingsProperty:
        """

        :param name:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

class SettingsPropertyIsReadOnlyException(Exception, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """

        :param message:
        """
    @overload
    def __init__(self, message: str, innerException: Exception):
        """

        :param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """

        :return:
        """
    @property
    def HResult(self) -> int:
        """

        :return:
        """
    @property
    def HelpLink(self) -> str:
        """

        :return:
        """
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """

        :return:
        """
    @property
    def Message(self) -> str:
        """

        :return:
        """
    @property
    def Source(self) -> str:
        """

        :return:
        """
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """

        :return:
        """
    @property
    def TargetSite(self) -> MethodBase:
        """

        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class SettingsPropertyNotFoundException(Exception, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """

        :param message:
        """
    @overload
    def __init__(self, message: str, innerException: Exception):
        """

        :param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """

        :return:
        """
    @property
    def HResult(self) -> int:
        """

        :return:
        """
    @property
    def HelpLink(self) -> str:
        """

        :return:
        """
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """

        :return:
        """
    @property
    def Message(self) -> str:
        """

        :return:
        """
    @property
    def Source(self) -> str:
        """

        :return:
        """
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """

        :return:
        """
    @property
    def TargetSite(self) -> MethodBase:
        """

        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class SettingsPropertyValue(Object):
    """"""

    def __init__(self, property: SettingsProperty):
        """

        :param property:
        """
    @property
    def Deserialized(self) -> bool:
        """

        :return:
        """
    @Deserialized.setter
    def Deserialized(self, value: bool) -> None: ...
    @property
    def IsDirty(self) -> bool:
        """

        :return:
        """
    @IsDirty.setter
    def IsDirty(self, value: bool) -> None: ...
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Property(self) -> SettingsProperty:
        """

        :return:
        """
    @property
    def PropertyValue(self) -> object:
        """

        :return:
        """
    @PropertyValue.setter
    def PropertyValue(self, value: object) -> None: ...
    @property
    def SerializedValue(self) -> object:
        """

        :return:
        """
    @SerializedValue.setter
    def SerializedValue(self, value: object) -> None: ...
    @property
    def UsingDefaultValue(self) -> bool:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SettingsPropertyValueCollection(Object, ICollection, IEnumerable, ICloneable):
    """"""

    def __init__(self):
        """"""
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> SettingsPropertyValue:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    def Add(self, property: SettingsPropertyValue) -> None:
        """

        :param property:
        """
    def Clear(self) -> None:
        """"""
    def Clone(self) -> object:
        """

        :return:
        """
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Remove(self, name: str) -> None:
        """

        :param name:
        """
    def SetReadOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, name: str) -> SettingsPropertyValue:
        """

        :param name:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

class SettingsPropertyWrongTypeException(Exception, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """

        :param message:
        """
    @overload
    def __init__(self, message: str, innerException: Exception):
        """

        :param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """

        :return:
        """
    @property
    def HResult(self) -> int:
        """

        :return:
        """
    @property
    def HelpLink(self) -> str:
        """

        :return:
        """
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """

        :return:
        """
    @property
    def Message(self) -> str:
        """

        :return:
        """
    @property
    def Source(self) -> str:
        """

        :return:
        """
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """

        :return:
        """
    @property
    def TargetSite(self) -> MethodBase:
        """

        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class SettingsProvider(ABC, ProviderBase):
    """"""

    @property
    def ApplicationName(self) -> str:
        """

        :return:
        """
    @ApplicationName.setter
    def ApplicationName(self, value: str) -> None: ...
    @property
    def Description(self) -> str:
        """"""
    @property
    def Name(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetPropertyValues(
        self, context: SettingsContext, collection: SettingsPropertyCollection
    ) -> SettingsPropertyValueCollection:
        """

        :param context:
        :param collection:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self, name: str, config: NameValueCollection) -> None:
        """"""
    def SetPropertyValues(
        self, context: SettingsContext, collection: SettingsPropertyValueCollection
    ) -> None:
        """

        :param context:
        :param collection:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SettingsProviderAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self, providerTypeName: str):
        """

        :param providerTypeName:
        """
    @overload
    def __init__(self, providerType: Type):
        """

        :param providerType:
        """
    @property
    def ProviderTypeName(self) -> str:
        """

        :return:
        """
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SettingsProviderCollection(ProviderCollection, ICollection, IEnumerable):
    """"""

    def __init__(self):
        """"""
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> ProviderBase:
        """"""
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    def Add(self, provider: ProviderBase) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[ProviderBase], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Remove(self, name: str) -> None:
        """"""
    def SetReadOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, name: str) -> ProviderBase:
        """"""
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

SettingsSavingEventHandler: Callable[[object, CancelEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

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

    def __init__(self, serializeAs: SettingsSerializeAs):
        """

        :param serializeAs:
        """
    @property
    def SerializeAs(self) -> SettingsSerializeAs:
        """

        :return:
        """
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SingleTagSectionHandler(Object, IConfigurationSectionHandler):
    """"""

    def __init__(self):
        """"""
    def Create(self, parent: object, configContext: object, section: XmlNode) -> object:
        """

        :param parent:
        :param configContext:
        :param section:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SpecialSetting(Enum):
    """"""

    ConnectionString: SpecialSetting = ...
    """"""
    WebServiceUrl: SpecialSetting = ...
    """"""

class SpecialSettingAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, specialSetting: SpecialSetting):
        """

        :param specialSetting:
        """
    @property
    def SpecialSetting(self) -> SpecialSetting:
        """

        :return:
        """
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class StoredSetting(ValueType):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class TypeUtil(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class UriSection(ConfigurationSection):
    """"""

    def __init__(self):
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def Idn(self) -> IdnElement:
        """

        :return:
        """
    @property
    def IriParsing(self) -> IriParsingElement:
        """

        :return:
        """
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
        """

        :return:
        """
    @property
    def SectionInformation(self) -> SectionInformation:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def IsReadOnly(self) -> bool:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class UriSectionData(Object):
    """"""

    def __init__(self):
        """"""
    @property
    def IdnScope(self) -> Optional[UriIdnScope]:
        """

        :return:
        """
    @IdnScope.setter
    def IdnScope(self, value: Optional[UriIdnScope]) -> None: ...
    @property
    def IriParsing(self) -> Optional[bool]:
        """

        :return:
        """
    @IriParsing.setter
    def IriParsing(self, value: Optional[bool]) -> None: ...
    @property
    def SchemeSettings(self) -> Dictionary[str, SchemeSettingInternal]:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class UriSectionInternal(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class UriSectionReader(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    @overload
    def Read(cls, configFilePath: str) -> UriSectionData:
        """

        :param configFilePath:
        :return:
        """
    @classmethod
    @overload
    def Read(cls, configFilePath: str, parentData: UriSectionData) -> UriSectionData:
        """

        :param configFilePath:
        :param parentData:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class UserScopedSettingAttribute(SettingAttribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class UserSettingsGroup(ConfigurationSectionGroup):
    """"""

    def __init__(self):
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
        """

        :param obj:
        :return:
        """
    @overload
    def ForceDeclaration(self) -> None:
        """"""
    @overload
    def ForceDeclaration(self, force: bool) -> None:
        """"""
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
