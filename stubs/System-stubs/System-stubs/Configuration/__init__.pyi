from __future__ import annotations

from abc import ABC
from typing import Callable, Generic, Optional, Protocol, Union, overload

from System import Array, AsyncCallback, Attribute, Boolean, Enum, EventArgs, Exception, GenericUriParserOptions, IAsyncResult, ICloneable, Int32, IntPtr, MulticastDelegate, Nullable, Object, String, SystemException, Type, UriIdnScope, ValueType, Void
from System.Collections import Hashtable, ICollection, IDictionary, IEnumerable, IEnumerator
from System.Collections.Generic import Dictionary
from System.Collections.Specialized import NameValueCollection
from System.ComponentModel import CancelEventArgs, INotifyPropertyChanged, PropertyChangedEventHandler
from System.Configuration import ConfigurationElement, ConfigurationElementCollection, ConfigurationElementCollectionType, ConfigurationSection, ConfigurationSectionGroup
from System.Configuration.Internal import IConfigErrorInfo
from System.Configuration.Provider import ProviderBase, ProviderCollection
from System.Runtime.InteropServices import _Attribute, _Exception
from System.Runtime.Serialization import IDeserializationCallback, ISerializable, SerializationInfo, StreamingContext
from System.Xml import XmlAttribute, XmlCDataSection, XmlComment, XmlDocument, XmlElement, XmlNode, XmlSignificantWhitespace, XmlText, XmlTextReader, XmlWhitespace
from System.Xml.XPath import IXPathNavigable

# ---------- Types ---------- #

BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
NIntType = Union[int, IntPtr]
NullableType = Union[Optional, Nullable]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]


class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    
    def __isub__(self, other: T): ...


# ---------- Classes ---------- #

class AppSettingsReader(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetValue(self, key: StringType, type: TypeType) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ApplicationScopedSettingAttribute(SettingAttribute, _Attribute):
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


class ApplicationSettingsBase(ABC, SettingsBase, INotifyPropertyChanged):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Context(self) -> SettingsContext: ...
    
    @property
    def Item(self) -> ObjectType: ...
    
    @Item.setter
    def Item(self, value: ObjectType) -> None: ...
    
    @property
    def Properties(self) -> SettingsPropertyCollection: ...
    
    @property
    def PropertyValues(self) -> SettingsPropertyValueCollection: ...
    
    @property
    def Providers(self) -> SettingsProviderCollection: ...
    
    @property
    def SettingsKey(self) -> StringType: ...
    
    @SettingsKey.setter
    def SettingsKey(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def GetPreviousVersion(self, propertyName: StringType) -> ObjectType: ...
    
    def Reload(self) -> VoidType: ...
    
    def Reset(self) -> VoidType: ...
    
    def Save(self) -> VoidType: ...
    
    def Upgrade(self) -> VoidType: ...
    
    def add_PropertyChanged(self, value: PropertyChangedEventHandler) -> VoidType: ...
    
    def add_SettingChanging(self, value: SettingChangingEventHandler) -> VoidType: ...
    
    def add_SettingsLoaded(self, value: SettingsLoadedEventHandler) -> VoidType: ...
    
    def add_SettingsSaving(self, value: SettingsSavingEventHandler) -> VoidType: ...
    
    def get_Context(self) -> SettingsContext: ...
    
    def get_Item(self, propertyName: StringType) -> ObjectType: ...
    
    def get_Properties(self) -> SettingsPropertyCollection: ...
    
    def get_PropertyValues(self) -> SettingsPropertyValueCollection: ...
    
    def get_Providers(self) -> SettingsProviderCollection: ...
    
    def get_SettingsKey(self) -> StringType: ...
    
    def remove_PropertyChanged(self, value: PropertyChangedEventHandler) -> VoidType: ...
    
    def remove_SettingChanging(self, value: SettingChangingEventHandler) -> VoidType: ...
    
    def remove_SettingsLoaded(self, value: SettingsLoadedEventHandler) -> VoidType: ...
    
    def remove_SettingsSaving(self, value: SettingsSavingEventHandler) -> VoidType: ...
    
    def set_Item(self, propertyName: StringType, value: ObjectType) -> VoidType: ...
    
    def set_SettingsKey(self, value: StringType) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    PropertyChanged: EventType[PropertyChangedEventHandler] = ...
    
    SettingChanging: EventType[SettingChangingEventHandler] = ...
    
    SettingsLoaded: EventType[SettingsLoadedEventHandler] = ...
    
    SettingsSaving: EventType[SettingsSavingEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ApplicationSettingsGroup(ConfigurationSectionGroup):
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


class ClientSettingsSection(ConfigurationSection):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Settings(self) -> SettingElementCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_Settings(self) -> SettingElementCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ClientSettingsStore(ObjectType):
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


class CommonConfigurationStrings(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConfigXmlAttribute(XmlAttribute, ICloneable, IEnumerable, IXPathNavigable, IConfigErrorInfo):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, filename: StringType, line: IntType, prefix: StringType, localName: StringType, namespaceUri: StringType, doc: XmlDocument): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConfigXmlCDataSection(XmlCDataSection, ICloneable, IEnumerable, IXPathNavigable, IConfigErrorInfo):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, filename: StringType, line: IntType, data: StringType, doc: XmlDocument): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConfigXmlComment(XmlComment, ICloneable, IEnumerable, IXPathNavigable, IConfigErrorInfo):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, filename: StringType, line: IntType, comment: StringType, doc: XmlDocument): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConfigXmlDocument(XmlDocument, ICloneable, IEnumerable, IXPathNavigable, IConfigErrorInfo):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Filename(self) -> StringType: ...
    
    @property
    def LineNumber(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def CreateAttribute(self, prefix: StringType, localName: StringType, namespaceUri: StringType) -> XmlAttribute: ...
    
    def CreateCDataSection(self, data: StringType) -> XmlCDataSection: ...
    
    def CreateComment(self, data: StringType) -> XmlComment: ...
    
    @overload
    def CreateElement(self, prefix: StringType, localName: StringType, namespaceUri: StringType) -> XmlElement: ...
    
    def CreateSignificantWhitespace(self, data: StringType) -> XmlSignificantWhitespace: ...
    
    def CreateTextNode(self, text: StringType) -> XmlText: ...
    
    def CreateWhitespace(self, data: StringType) -> XmlWhitespace: ...
    
    @overload
    def Load(self, filename: StringType) -> VoidType: ...
    
    def LoadSingleElement(self, filename: StringType, sourceReader: XmlTextReader) -> VoidType: ...
    
    def get_Filename(self) -> StringType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConfigXmlElement(XmlElement, ICloneable, IEnumerable, IXPathNavigable, IConfigErrorInfo):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, filename: StringType, line: IntType, prefix: StringType, localName: StringType, namespaceUri: StringType, doc: XmlDocument): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConfigXmlSignificantWhitespace(XmlSignificantWhitespace, ICloneable, IEnumerable, IXPathNavigable, IConfigErrorInfo):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, filename: StringType, line: IntType, strData: StringType, doc: XmlDocument): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConfigXmlText(XmlText, ICloneable, IEnumerable, IXPathNavigable, IConfigErrorInfo):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, filename: StringType, line: IntType, strData: StringType, doc: XmlDocument): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConfigXmlWhitespace(XmlWhitespace, ICloneable, IEnumerable, IXPathNavigable, IConfigErrorInfo):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, filename: StringType, line: IntType, comment: StringType, doc: XmlDocument): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CloneNode(self, deep: BooleanType) -> XmlNode: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConfigurationException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    @overload
    def __init__(self, message: StringType, node: XmlNode): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception, node: XmlNode): ...
    
    @overload
    def __init__(self, message: StringType, filename: StringType, line: IntType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception, filename: StringType, line: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BareMessage(self) -> StringType: ...
    
    @property
    def Filename(self) -> StringType: ...
    
    @property
    def Line(self) -> IntType: ...
    
    @property
    def Message(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    @staticmethod
    def GetXmlNodeFilename(node: XmlNode) -> StringType: ...
    
    @staticmethod
    def GetXmlNodeLineNumber(node: XmlNode) -> IntType: ...
    
    def get_BareMessage(self) -> StringType: ...
    
    def get_Filename(self) -> StringType: ...
    
    def get_Line(self) -> IntType: ...
    
    def get_Message(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConfigurationManagerInternalFactory(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConfigurationSettings(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def AppSettings() -> NameValueCollection: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetConfig(sectionName: StringType) -> ObjectType: ...
    
    @staticmethod
    def get_AppSettings() -> NameValueCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DefaultSettingValueAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, value: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Value(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Value(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DictionarySectionHandler(ObjectType, IConfigurationSectionHandler):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Create(self, parent: ObjectType, context: ObjectType, section: XmlNode) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HandlerBase(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IdnElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Enabled(self) -> UriIdnScope: ...
    
    @Enabled.setter
    def Enabled(self, value: UriIdnScope) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Enabled(self) -> UriIdnScope: ...
    
    def set_Enabled(self, value: UriIdnScope) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IgnoreSectionHandler(ObjectType, IConfigurationSectionHandler):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Create(self, parent: ObjectType, configContext: ObjectType, section: XmlNode) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IriParsingElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Enabled(self) -> BooleanType: ...
    
    @Enabled.setter
    def Enabled(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Enabled(self) -> BooleanType: ...
    
    def set_Enabled(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LocalFileSettingsProvider(SettingsProvider, IApplicationSettingsProvider):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ApplicationName(self) -> StringType: ...
    
    @ApplicationName.setter
    def ApplicationName(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def GetPreviousVersion(self, context: SettingsContext, property: SettingsProperty) -> SettingsPropertyValue: ...
    
    def GetPropertyValues(self, context: SettingsContext, properties: SettingsPropertyCollection) -> SettingsPropertyValueCollection: ...
    
    def Initialize(self, name: StringType, values: NameValueCollection) -> VoidType: ...
    
    def Reset(self, context: SettingsContext) -> VoidType: ...
    
    def SetPropertyValues(self, context: SettingsContext, values: SettingsPropertyValueCollection) -> VoidType: ...
    
    def Upgrade(self, context: SettingsContext, properties: SettingsPropertyCollection) -> VoidType: ...
    
    def get_ApplicationName(self) -> StringType: ...
    
    def set_ApplicationName(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NameValueFileSectionHandler(ObjectType, IConfigurationSectionHandler):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Create(self, parent: ObjectType, configContext: ObjectType, section: XmlNode) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NameValueSectionHandler(ObjectType, IConfigurationSectionHandler):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Create(self, parent: ObjectType, context: ObjectType, section: XmlNode) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NoSettingsVersionUpgradeAttribute(Attribute, _Attribute):
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


class PrivilegedConfigurationManager(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReadOnlyNameValueCollection(NameValueCollection, ICollection, IEnumerable, ISerializable, IDeserializationCallback):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SchemeSettingElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def GenericUriParserOptions(self) -> GenericUriParserOptions: ...
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_GenericUriParserOptions(self) -> GenericUriParserOptions: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SchemeSettingElementCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CollectionType(self) -> ConfigurationElementCollectionType: ...
    
    @property
    def Item(self) -> SchemeSettingElement: ...
    
    @property
    def Item(self) -> SchemeSettingElement: ...
    
    # ---------- Methods ---------- #
    
    def IndexOf(self, element: SchemeSettingElement) -> IntType: ...
    
    def get_CollectionType(self) -> ConfigurationElementCollectionType: ...
    
    @overload
    def get_Item(self, index: IntType) -> SchemeSettingElement: ...
    
    @overload
    def get_Item(self, name: StringType) -> SchemeSettingElement: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SchemeSettingInternal(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, name: StringType, options: GenericUriParserOptions): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Options(self) -> GenericUriParserOptions: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> StringType: ...
    
    def get_Options(self) -> GenericUriParserOptions: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SettingAttribute(Attribute, _Attribute):
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


class SettingChangingEventArgs(CancelEventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, settingName: StringType, settingClass: StringType, settingKey: StringType, newValue: ObjectType, cancel: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def NewValue(self) -> ObjectType: ...
    
    @property
    def SettingClass(self) -> StringType: ...
    
    @property
    def SettingKey(self) -> StringType: ...
    
    @property
    def SettingName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_NewValue(self) -> ObjectType: ...
    
    def get_SettingClass(self) -> StringType: ...
    
    def get_SettingKey(self) -> StringType: ...
    
    def get_SettingName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SettingChangingEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: SettingChangingEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: SettingChangingEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SettingElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, name: StringType, serializeAs: SettingsSerializeAs): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def SerializeAs(self) -> SettingsSerializeAs: ...
    
    @SerializeAs.setter
    def SerializeAs(self, value: SettingsSerializeAs) -> None: ...
    
    @property
    def Value(self) -> SettingValueElement: ...
    
    @Value.setter
    def Value(self, value: SettingValueElement) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, settings: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_SerializeAs(self) -> SettingsSerializeAs: ...
    
    def get_Value(self) -> SettingValueElement: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_SerializeAs(self, value: SettingsSerializeAs) -> VoidType: ...
    
    def set_Value(self, value: SettingValueElement) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SettingElementCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CollectionType(self) -> ConfigurationElementCollectionType: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, element: SettingElement) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Get(self, elementKey: StringType) -> SettingElement: ...
    
    def Remove(self, element: SettingElement) -> VoidType: ...
    
    def get_CollectionType(self) -> ConfigurationElementCollectionType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SettingValueElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ValueXml(self) -> XmlNode: ...
    
    @ValueXml.setter
    def ValueXml(self, value: XmlNode) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, settingValue: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_ValueXml(self) -> XmlNode: ...
    
    def set_ValueXml(self, value: XmlNode) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SettingsAttributeDictionary(Hashtable, IDictionary, ICollection, IEnumerable, ISerializable, IDeserializationCallback, ICloneable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, attributes: SettingsAttributeDictionary): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SettingsBase(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Context(self) -> SettingsContext: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    @property
    def Item(self) -> ObjectType: ...
    
    @Item.setter
    def Item(self, value: ObjectType) -> None: ...
    
    @property
    def Properties(self) -> SettingsPropertyCollection: ...
    
    @property
    def PropertyValues(self) -> SettingsPropertyValueCollection: ...
    
    @property
    def Providers(self) -> SettingsProviderCollection: ...
    
    # ---------- Methods ---------- #
    
    def Initialize(self, context: SettingsContext, properties: SettingsPropertyCollection, providers: SettingsProviderCollection) -> VoidType: ...
    
    def Save(self) -> VoidType: ...
    
    @staticmethod
    def Synchronized(settingsBase: SettingsBase) -> SettingsBase: ...
    
    def get_Context(self) -> SettingsContext: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_Item(self, propertyName: StringType) -> ObjectType: ...
    
    def get_Properties(self) -> SettingsPropertyCollection: ...
    
    def get_PropertyValues(self) -> SettingsPropertyValueCollection: ...
    
    def get_Providers(self) -> SettingsProviderCollection: ...
    
    def set_Item(self, propertyName: StringType, value: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SettingsContext(Hashtable, IDictionary, ICollection, IEnumerable, ISerializable, IDeserializationCallback, ICloneable):
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


class SettingsDescriptionAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, description: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Description(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Description(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SettingsGroupDescriptionAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, description: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Description(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Description(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SettingsGroupNameAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, groupName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def GroupName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_GroupName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SettingsLoadedEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, provider: SettingsProvider): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Provider(self) -> SettingsProvider: ...
    
    # ---------- Methods ---------- #
    
    def get_Provider(self) -> SettingsProvider: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SettingsLoadedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: SettingsLoadedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: SettingsLoadedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SettingsManageabilityAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, manageability: SettingsManageability): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Manageability(self) -> SettingsManageability: ...
    
    # ---------- Methods ---------- #
    
    def get_Manageability(self) -> SettingsManageability: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SettingsProperty(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, name: StringType): ...
    
    @overload
    def __init__(self, name: StringType, propertyType: TypeType, provider: SettingsProvider, isReadOnly: BooleanType, defaultValue: ObjectType, serializeAs: SettingsSerializeAs, attributes: SettingsAttributeDictionary, throwOnErrorDeserializing: BooleanType, throwOnErrorSerializing: BooleanType): ...
    
    @overload
    def __init__(self, propertyToCopy: SettingsProperty): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Attributes(self) -> SettingsAttributeDictionary: ...
    
    @property
    def DefaultValue(self) -> ObjectType: ...
    
    @DefaultValue.setter
    def DefaultValue(self, value: ObjectType) -> None: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @IsReadOnly.setter
    def IsReadOnly(self, value: BooleanType) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def PropertyType(self) -> TypeType: ...
    
    @PropertyType.setter
    def PropertyType(self, value: TypeType) -> None: ...
    
    @property
    def Provider(self) -> SettingsProvider: ...
    
    @Provider.setter
    def Provider(self, value: SettingsProvider) -> None: ...
    
    @property
    def SerializeAs(self) -> SettingsSerializeAs: ...
    
    @SerializeAs.setter
    def SerializeAs(self, value: SettingsSerializeAs) -> None: ...
    
    @property
    def ThrowOnErrorDeserializing(self) -> BooleanType: ...
    
    @ThrowOnErrorDeserializing.setter
    def ThrowOnErrorDeserializing(self, value: BooleanType) -> None: ...
    
    @property
    def ThrowOnErrorSerializing(self) -> BooleanType: ...
    
    @ThrowOnErrorSerializing.setter
    def ThrowOnErrorSerializing(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Attributes(self) -> SettingsAttributeDictionary: ...
    
    def get_DefaultValue(self) -> ObjectType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_PropertyType(self) -> TypeType: ...
    
    def get_Provider(self) -> SettingsProvider: ...
    
    def get_SerializeAs(self) -> SettingsSerializeAs: ...
    
    def get_ThrowOnErrorDeserializing(self) -> BooleanType: ...
    
    def get_ThrowOnErrorSerializing(self) -> BooleanType: ...
    
    def set_DefaultValue(self, value: ObjectType) -> VoidType: ...
    
    def set_IsReadOnly(self, value: BooleanType) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_PropertyType(self, value: TypeType) -> VoidType: ...
    
    def set_Provider(self, value: SettingsProvider) -> VoidType: ...
    
    def set_SerializeAs(self, value: SettingsSerializeAs) -> VoidType: ...
    
    def set_ThrowOnErrorDeserializing(self, value: BooleanType) -> VoidType: ...
    
    def set_ThrowOnErrorSerializing(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SettingsPropertyCollection(ObjectType, IEnumerable, ICloneable, ICollection):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    @property
    def Item(self) -> SettingsProperty: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, property: SettingsProperty) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Clone(self) -> ObjectType: ...
    
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def Remove(self, name: StringType) -> VoidType: ...
    
    def SetReadOnly(self) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_Item(self, name: StringType) -> SettingsProperty: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SettingsPropertyIsReadOnlyException(Exception, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SettingsPropertyNotFoundException(Exception, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SettingsPropertyValue(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, property: SettingsProperty): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Deserialized(self) -> BooleanType: ...
    
    @Deserialized.setter
    def Deserialized(self, value: BooleanType) -> None: ...
    
    @property
    def IsDirty(self) -> BooleanType: ...
    
    @IsDirty.setter
    def IsDirty(self, value: BooleanType) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def Property(self) -> SettingsProperty: ...
    
    @property
    def PropertyValue(self) -> ObjectType: ...
    
    @PropertyValue.setter
    def PropertyValue(self, value: ObjectType) -> None: ...
    
    @property
    def SerializedValue(self) -> ObjectType: ...
    
    @SerializedValue.setter
    def SerializedValue(self, value: ObjectType) -> None: ...
    
    @property
    def UsingDefaultValue(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_Deserialized(self) -> BooleanType: ...
    
    def get_IsDirty(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Property(self) -> SettingsProperty: ...
    
    def get_PropertyValue(self) -> ObjectType: ...
    
    def get_SerializedValue(self) -> ObjectType: ...
    
    def get_UsingDefaultValue(self) -> BooleanType: ...
    
    def set_Deserialized(self, value: BooleanType) -> VoidType: ...
    
    def set_IsDirty(self, value: BooleanType) -> VoidType: ...
    
    def set_PropertyValue(self, value: ObjectType) -> VoidType: ...
    
    def set_SerializedValue(self, value: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SettingsPropertyValueCollection(ObjectType, IEnumerable, ICloneable, ICollection):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    @property
    def Item(self) -> SettingsPropertyValue: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, property: SettingsPropertyValue) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Clone(self) -> ObjectType: ...
    
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def Remove(self, name: StringType) -> VoidType: ...
    
    def SetReadOnly(self) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_Item(self, name: StringType) -> SettingsPropertyValue: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SettingsPropertyWrongTypeException(Exception, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SettingsProvider(ABC, ProviderBase):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ApplicationName(self) -> StringType: ...
    
    @ApplicationName.setter
    def ApplicationName(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def GetPropertyValues(self, context: SettingsContext, collection: SettingsPropertyCollection) -> SettingsPropertyValueCollection: ...
    
    def SetPropertyValues(self, context: SettingsContext, collection: SettingsPropertyValueCollection) -> VoidType: ...
    
    def get_ApplicationName(self) -> StringType: ...
    
    def set_ApplicationName(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SettingsProviderAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, providerTypeName: StringType): ...
    
    @overload
    def __init__(self, providerType: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ProviderTypeName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_ProviderTypeName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SettingsProviderCollection(ProviderCollection, IEnumerable, ICollection):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> SettingsProvider: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, provider: ProviderBase) -> VoidType: ...
    
    @overload
    def get_Item(self, name: StringType) -> SettingsProvider: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SettingsSavingEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: CancelEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: CancelEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SettingsSerializeAsAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, serializeAs: SettingsSerializeAs): ...
    
    # ---------- Properties ---------- #
    
    @property
    def SerializeAs(self) -> SettingsSerializeAs: ...
    
    # ---------- Methods ---------- #
    
    def get_SerializeAs(self) -> SettingsSerializeAs: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SingleTagSectionHandler(ObjectType, IConfigurationSectionHandler):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Create(self, parent: ObjectType, context: ObjectType, section: XmlNode) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SpecialSettingAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, specialSetting: SpecialSetting): ...
    
    # ---------- Properties ---------- #
    
    @property
    def SpecialSetting(self) -> SpecialSetting: ...
    
    # ---------- Methods ---------- #
    
    def get_SpecialSetting(self) -> SpecialSetting: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypeUtil(ABC, ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UriSection(ConfigurationSection):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Idn(self) -> IdnElement: ...
    
    @property
    def IriParsing(self) -> IriParsingElement: ...
    
    @property
    def SchemeSettings(self) -> SchemeSettingElementCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_Idn(self) -> IdnElement: ...
    
    def get_IriParsing(self) -> IriParsingElement: ...
    
    def get_SchemeSettings(self) -> SchemeSettingElementCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UriSectionData(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IdnScope(self) -> NullableType[Nullable[UriIdnScope]]: ...
    
    @IdnScope.setter
    def IdnScope(self, value: NullableType[Nullable[UriIdnScope]]) -> None: ...
    
    @property
    def IriParsing(self) -> NullableType[Nullable[BooleanType]]: ...
    
    @IriParsing.setter
    def IriParsing(self, value: NullableType[Nullable[BooleanType]]) -> None: ...
    
    @property
    def SchemeSettings(self) -> Dictionary[StringType, SchemeSettingInternal]: ...
    
    # ---------- Methods ---------- #
    
    def get_IdnScope(self) -> NullableType[Nullable[UriIdnScope]]: ...
    
    def get_IriParsing(self) -> NullableType[Nullable[BooleanType]]: ...
    
    def get_SchemeSettings(self) -> Dictionary[StringType, SchemeSettingInternal]: ...
    
    def set_IdnScope(self, value: NullableType[Nullable[UriIdnScope]]) -> VoidType: ...
    
    def set_IriParsing(self, value: NullableType[Nullable[BooleanType]]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UriSectionInternal(ObjectType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UriSectionReader(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def Read(configFilePath: StringType) -> UriSectionData: ...
    
    @staticmethod
    @overload
    def Read(configFilePath: StringType, parentData: UriSectionData) -> UriSectionData: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UserScopedSettingAttribute(SettingAttribute, _Attribute):
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


class UserSettingsGroup(ConfigurationSectionGroup):
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


# ---------- Structs ---------- #

class StoredSetting(ValueType):
    """"""
    
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Interfaces ---------- #

class IApplicationSettingsProvider(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetPreviousVersion(self, context: SettingsContext, property: SettingsProperty) -> SettingsPropertyValue: ...
    
    def Reset(self, context: SettingsContext) -> VoidType: ...
    
    def Upgrade(self, context: SettingsContext, properties: SettingsPropertyCollection) -> VoidType: ...
    
    # No Events


class IConfigurationSectionHandler(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Create(self, parent: ObjectType, configContext: ObjectType, section: XmlNode) -> ObjectType: ...
    
    # No Events


class IConfigurationSystem(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetConfig(self, configKey: StringType) -> ObjectType: ...
    
    def Init(self) -> VoidType: ...
    
    # No Events


class IPersistComponentSettings(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def SaveSettings(self) -> BooleanType: ...
    
    @SaveSettings.setter
    def SaveSettings(self, value: BooleanType) -> None: ...
    
    @property
    def SettingsKey(self) -> StringType: ...
    
    @SettingsKey.setter
    def SettingsKey(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def LoadComponentSettings(self) -> VoidType: ...
    
    def ResetComponentSettings(self) -> VoidType: ...
    
    def SaveComponentSettings(self) -> VoidType: ...
    
    def get_SaveSettings(self) -> BooleanType: ...
    
    def get_SettingsKey(self) -> StringType: ...
    
    def set_SaveSettings(self, value: BooleanType) -> VoidType: ...
    
    def set_SettingsKey(self, value: StringType) -> VoidType: ...
    
    # No Events


class ISettingsProviderService(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetSettingsProvider(self, property: SettingsProperty) -> SettingsProvider: ...
    
    # No Events


# ---------- Enums ---------- #

class SettingsManageability(Enum):
    Roaming: IntType = 0


class SettingsSerializeAs(Enum):
    String: IntType = 0
    Xml: IntType = 1
    Binary: IntType = 2
    ProviderSpecific: IntType = 3


class SpecialSetting(Enum):
    ConnectionString: IntType = 0
    WebServiceUrl: IntType = 1


# ---------- Delegates ---------- #

SettingChangingEventHandler = Callable[[ObjectType, SettingChangingEventArgs], VoidType]

SettingsLoadedEventHandler = Callable[[ObjectType, SettingsLoadedEventArgs], VoidType]

SettingsSavingEventHandler = Callable[[ObjectType, CancelEventArgs], VoidType]

__all__ = [
    AppSettingsReader,
    ApplicationScopedSettingAttribute,
    ApplicationSettingsBase,
    ApplicationSettingsGroup,
    ClientSettingsSection,
    ClientSettingsStore,
    CommonConfigurationStrings,
    ConfigXmlAttribute,
    ConfigXmlCDataSection,
    ConfigXmlComment,
    ConfigXmlDocument,
    ConfigXmlElement,
    ConfigXmlSignificantWhitespace,
    ConfigXmlText,
    ConfigXmlWhitespace,
    ConfigurationException,
    ConfigurationManagerInternalFactory,
    ConfigurationSettings,
    DefaultSettingValueAttribute,
    DictionarySectionHandler,
    HandlerBase,
    IdnElement,
    IgnoreSectionHandler,
    IriParsingElement,
    LocalFileSettingsProvider,
    NameValueFileSectionHandler,
    NameValueSectionHandler,
    NoSettingsVersionUpgradeAttribute,
    PrivilegedConfigurationManager,
    ReadOnlyNameValueCollection,
    SchemeSettingElement,
    SchemeSettingElementCollection,
    SchemeSettingInternal,
    SettingAttribute,
    SettingChangingEventArgs,
    SettingChangingEventHandler,
    SettingElement,
    SettingElementCollection,
    SettingValueElement,
    SettingsAttributeDictionary,
    SettingsBase,
    SettingsContext,
    SettingsDescriptionAttribute,
    SettingsGroupDescriptionAttribute,
    SettingsGroupNameAttribute,
    SettingsLoadedEventArgs,
    SettingsLoadedEventHandler,
    SettingsManageabilityAttribute,
    SettingsProperty,
    SettingsPropertyCollection,
    SettingsPropertyIsReadOnlyException,
    SettingsPropertyNotFoundException,
    SettingsPropertyValue,
    SettingsPropertyValueCollection,
    SettingsPropertyWrongTypeException,
    SettingsProvider,
    SettingsProviderAttribute,
    SettingsProviderCollection,
    SettingsSavingEventHandler,
    SettingsSerializeAsAttribute,
    SingleTagSectionHandler,
    SpecialSettingAttribute,
    TypeUtil,
    UriSection,
    UriSectionData,
    UriSectionInternal,
    UriSectionReader,
    UserScopedSettingAttribute,
    UserSettingsGroup,
    StoredSetting,
    IApplicationSettingsProvider,
    IConfigurationSectionHandler,
    IConfigurationSystem,
    IPersistComponentSettings,
    ISettingsProviderService,
    SettingsManageability,
    SettingsSerializeAs,
    SpecialSetting,
    SettingChangingEventHandler,
    SettingsLoadedEventHandler,
    SettingsSavingEventHandler,
]
