from __future__ import annotations

from abc import ABC
from typing import Callable
from typing import Generic
from typing import List
from typing import Optional
from typing import Protocol
from typing import Tuple
from typing import TypeVar
from typing import Union
from typing import overload

from System import Array
from System import AsyncCallback
from System import Attribute
from System import Boolean
from System import Enum
from System import EventArgs
from System import Exception
from System import Func
from System import GenericUriParserOptions
from System import IAsyncResult
from System import ICloneable
from System import IDisposable
from System import Int32
from System import Int64
from System import IntPtr
from System import MulticastDelegate
from System import Nullable
from System import Object
from System import String
from System import SystemException
from System import TimeSpan
from System import Type
from System import UriIdnScope
from System import ValueType
from System import Void
from System.Collections import Hashtable
from System.Collections import ICollection
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections import IList
from System.Collections import ReadOnlyCollectionBase
from System.Collections.Generic import Dictionary
from System.Collections.Generic import List
from System.Collections.Specialized import NameObjectCollectionBase
from System.Collections.Specialized import NameValueCollection
from System.Collections.Specialized import StringCollection
from System.ComponentModel import CancelEventArgs
from System.ComponentModel import CategoryAttribute
from System.ComponentModel import DescriptionAttribute
from System.ComponentModel import INotifyPropertyChanged
from System.ComponentModel import ITypeDescriptorContext
from System.ComponentModel import PropertyChangedEventHandler
from System.ComponentModel import TypeConverter
from System.Configuration.Internal import DelegatingConfigHost
from System.Configuration.Internal import IConfigErrorInfo
from System.Configuration.Internal import IInternalConfigClientHost
from System.Configuration.Internal import IInternalConfigHost
from System.Configuration.Internal import IInternalConfigRecord
from System.Configuration.Internal import IInternalConfigRoot
from System.Configuration.Internal import IInternalConfigSystem
from System.Configuration.Internal import IInternalConfigurationBuilderHost
from System.Configuration.Provider import ProviderBase
from System.Configuration.Provider import ProviderCollection
from System.Globalization import CultureInfo
from System.IO import Stream
from System.Resources import ResourceManager
from System.Runtime.InteropServices import _Attribute
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import IDeserializationCallback
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Runtime.Versioning import FrameworkName
from System.Security import CodeAccessPermission
from System.Security import IPermission
from System.Security import ISecurityEncodable
from System.Security import IStackWalk
from System.Security import PermissionSet
from System.Security import SecurityElement
from System.Security.Cryptography import RSAParameters
from System.Security.Cryptography import SymmetricAlgorithm
from System.Security.Cryptography.Xml import EncryptedData
from System.Security.Cryptography.Xml import EncryptedXml
from System.Security.Permissions import CodeAccessSecurityAttribute
from System.Security.Permissions import IUnrestrictedPermission
from System.Security.Permissions import PermissionState
from System.Security.Permissions import SecurityAction
from System.Xml import IXmlLineInfo
from System.Xml import IXmlNamespaceResolver
from System.Xml import XmlAttribute
from System.Xml import XmlCDataSection
from System.Xml import XmlComment
from System.Xml import XmlDocument
from System.Xml import XmlElement
from System.Xml import XmlNode
from System.Xml import XmlReader
from System.Xml import XmlSignificantWhitespace
from System.Xml import XmlText
from System.Xml import XmlTextReader
from System.Xml import XmlWhitespace
from System.Xml.XPath import IXPathNavigable

# ---------- Types ---------- #

T = TypeVar("T")

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
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

class AppSettingsSection(ConfigurationSection):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def File(self) -> StringType: ...
    @File.setter
    def File(self, value: StringType) -> None: ...
    @property
    def Settings(self) -> KeyValueConfigurationCollection: ...

    # ---------- Methods ---------- #

    def get_File(self) -> StringType: ...
    def get_Settings(self) -> KeyValueConfigurationCollection: ...
    def set_File(self, value: StringType) -> VoidType: ...

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
    def __getitem__(self, key: StringType) -> ObjectType: ...
    def __setitem__(self, key: StringType, value: ObjectType) -> None: ...
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

class BaseConfigurationRecord(ABC, ObjectType, IInternalConfigRecord):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def ConfigPath(self) -> StringType: ...
    @property
    def HasInitErrors(self) -> BooleanType: ...
    @property
    def StreamName(self) -> StringType: ...

    # ---------- Methods ---------- #

    def GetLkgSection(self, configKey: StringType) -> ObjectType: ...
    def GetSection(self, configKey: StringType) -> ObjectType: ...
    def RefreshSection(self, configKey: StringType) -> VoidType: ...
    def Remove(self) -> VoidType: ...
    def ThrowIfInitErrors(self) -> VoidType: ...
    def get_ConfigPath(self) -> StringType: ...
    def get_HasInitErrors(self) -> BooleanType: ...
    def get_StreamName(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CallbackValidator(ConfigurationValidatorBase):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, type: TypeType, callback: ValidatorCallback): ...

    # No Properties

    # ---------- Methods ---------- #

    def CanValidate(self, type: TypeType) -> BooleanType: ...
    def Validate(self, value: ObjectType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CallbackValidatorAttribute(ConfigurationValidatorAttribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def CallbackMethodName(self) -> StringType: ...
    @CallbackMethodName.setter
    def CallbackMethodName(self, value: StringType) -> None: ...
    @property
    def Type(self) -> TypeType: ...
    @Type.setter
    def Type(self, value: TypeType) -> None: ...
    @property
    def ValidatorInstance(self) -> ConfigurationValidatorBase: ...

    # ---------- Methods ---------- #

    def get_CallbackMethodName(self) -> StringType: ...
    def get_Type(self) -> TypeType: ...
    def get_ValidatorInstance(self) -> ConfigurationValidatorBase: ...
    def set_CallbackMethodName(self, value: StringType) -> VoidType: ...
    def set_Type(self, value: TypeType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ClientConfigPaths(ObjectType):
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

class ClientConfigurationHost(
    DelegatingConfigHost,
    IInternalConfigHost,
    IInternalConfigurationBuilderHost,
    IInternalConfigClientHost,
):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def SupportsLocation(self) -> BooleanType: ...
    @property
    def SupportsPath(self) -> BooleanType: ...
    @property
    def SupportsRefresh(self) -> BooleanType: ...

    # ---------- Methods ---------- #

    def CreateConfigurationContext(
        self, configPath: StringType, locationSubPath: StringType
    ) -> ObjectType: ...
    def CreateDeprecatedConfigContext(self, configPath: StringType) -> ObjectType: ...
    def DeleteStream(self, streamName: StringType) -> VoidType: ...
    def GetRestrictedPermissions(
        self,
        configRecord: IInternalConfigRecord,
        permissionSet: PermissionSet,
        isHostReady: BooleanType,
    ) -> Tuple[VoidType, PermissionSet, BooleanType]: ...
    def GetStreamName(self, configPath: StringType) -> StringType: ...
    def GetStreamNameForConfigSource(
        self, streamName: StringType, configSource: StringType
    ) -> StringType: ...
    def GetStreamVersion(self, streamName: StringType) -> ObjectType: ...
    def Impersonate(self) -> IDisposable: ...
    def Init(
        self, configRoot: IInternalConfigRoot, hostInitParams: ArrayType[ObjectType]
    ) -> VoidType: ...
    def InitForConfiguration(
        self,
        locationSubPath: StringType,
        configPath: StringType,
        locationConfigPath: StringType,
        configRoot: IInternalConfigRoot,
        hostInitConfigurationParams: ArrayType[ObjectType],
    ) -> Tuple[VoidType, StringType, StringType, StringType]: ...
    def IsConfigRecordRequired(self, configPath: StringType) -> BooleanType: ...
    def IsDefinitionAllowed(
        self,
        configPath: StringType,
        allowDefinition: ConfigurationAllowDefinition,
        allowExeDefinition: ConfigurationAllowExeDefinition,
    ) -> BooleanType: ...
    def IsInitDelayed(self, configRecord: IInternalConfigRecord) -> BooleanType: ...
    def IsTrustedConfigPath(self, configPath: StringType) -> BooleanType: ...
    @overload
    def OpenStreamForRead(self, streamName: StringType) -> Stream: ...
    @overload
    def OpenStreamForWrite(
        self, streamName: StringType, templateStreamName: StringType, writeContext: ObjectType
    ) -> Tuple[Stream, ObjectType]: ...
    def PrefetchAll(self, configPath: StringType, streamName: StringType) -> BooleanType: ...
    def PrefetchSection(
        self, sectionGroupName: StringType, sectionName: StringType
    ) -> BooleanType: ...
    def RequireCompleteInit(self, record: IInternalConfigRecord) -> VoidType: ...
    def VerifyDefinitionAllowed(
        self,
        configPath: StringType,
        allowDefinition: ConfigurationAllowDefinition,
        allowExeDefinition: ConfigurationAllowExeDefinition,
        errorInfo: IConfigErrorInfo,
    ) -> VoidType: ...
    def get_SupportsLocation(self) -> BooleanType: ...
    def get_SupportsPath(self) -> BooleanType: ...
    def get_SupportsRefresh(self) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ClientConfigurationSystem(ObjectType, IInternalConfigSystem):
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

class CommaDelimitedStringCollection(StringCollection, IList, ICollection, IEnumerable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def IsModified(self) -> BooleanType: ...
    @property
    def IsReadOnly(self) -> BooleanType: ...
    def __getitem__(self, key: IntType) -> StringType: ...
    def __setitem__(self, key: IntType, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    @overload
    def Add(self, value: StringType) -> VoidType: ...
    @overload
    def AddRange(self, range: ArrayType[StringType]) -> VoidType: ...
    @overload
    def Clear(self) -> VoidType: ...
    def Clone(self) -> CommaDelimitedStringCollection: ...
    @overload
    def Insert(self, index: IntType, value: StringType) -> VoidType: ...
    @overload
    def Remove(self, value: StringType) -> VoidType: ...
    def SetReadOnly(self) -> VoidType: ...
    def ToString(self) -> StringType: ...
    def get_IsModified(self) -> BooleanType: ...
    @overload
    def get_IsReadOnly(self) -> BooleanType: ...
    @overload
    def get_Item(self, index: IntType) -> StringType: ...
    @overload
    def set_Item(self, index: IntType, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CommaDelimitedStringCollectionConverter(ConfigurationConverterBase):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def ConvertFrom(
        self, ctx: ITypeDescriptorContext, ci: CultureInfo, data: ObjectType
    ) -> ObjectType: ...
    @overload
    def ConvertTo(
        self, ctx: ITypeDescriptorContext, ci: CultureInfo, value: ObjectType, type: TypeType
    ) -> ObjectType: ...

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

class ConfigDefinitionUpdates(ObjectType):
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

class ConfigPathUtility(ABC, ObjectType):
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

    def __init__(
        self,
        filename: StringType,
        line: IntType,
        prefix: StringType,
        localName: StringType,
        namespaceUri: StringType,
        doc: XmlDocument,
    ): ...

    # No Properties

    # ---------- Methods ---------- #

    def CloneNode(self, deep: BooleanType) -> XmlNode: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConfigXmlCDataSection(
    XmlCDataSection, ICloneable, IEnumerable, IXPathNavigable, IConfigErrorInfo
):
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

    def __init__(
        self, filename: StringType, line: IntType, comment: StringType, doc: XmlDocument
    ): ...

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
    def CreateAttribute(
        self, prefix: StringType, localName: StringType, namespaceUri: StringType
    ) -> XmlAttribute: ...
    def CreateCDataSection(self, data: StringType) -> XmlCDataSection: ...
    def CreateComment(self, data: StringType) -> XmlComment: ...
    @overload
    def CreateElement(
        self, prefix: StringType, localName: StringType, namespaceUri: StringType
    ) -> XmlElement: ...
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

    def __init__(
        self,
        filename: StringType,
        line: IntType,
        prefix: StringType,
        localName: StringType,
        namespaceUri: StringType,
        doc: XmlDocument,
    ): ...

    # No Properties

    # ---------- Methods ---------- #

    def CloneNode(self, deep: BooleanType) -> XmlNode: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConfigXmlReader(
    XmlTextReader, IDisposable, IXmlLineInfo, IXmlNamespaceResolver, IConfigErrorInfo
):
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

class ConfigXmlSignificantWhitespace(
    XmlSignificantWhitespace, ICloneable, IEnumerable, IXPathNavigable, IConfigErrorInfo
):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(
        self, filename: StringType, line: IntType, strData: StringType, doc: XmlDocument
    ): ...

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

    def __init__(
        self, filename: StringType, line: IntType, strData: StringType, doc: XmlDocument
    ): ...

    # No Properties

    # ---------- Methods ---------- #

    def CloneNode(self, deep: BooleanType) -> XmlNode: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConfigXmlWhitespace(
    XmlWhitespace, ICloneable, IEnumerable, IXPathNavigable, IConfigErrorInfo
):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(
        self, filename: StringType, line: IntType, comment: StringType, doc: XmlDocument
    ): ...

    # No Properties

    # ---------- Methods ---------- #

    def CloneNode(self, deep: BooleanType) -> XmlNode: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Configuration(ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def AppSettings(self) -> AppSettingsSection: ...
    @property
    def AssemblyStringTransformer(self) -> Func[StringType, StringType]: ...
    @AssemblyStringTransformer.setter
    def AssemblyStringTransformer(self, value: Func[StringType, StringType]) -> None: ...
    @property
    def ConnectionStrings(self) -> ConnectionStringsSection: ...
    @property
    def EvaluationContext(self) -> ContextInformation: ...
    @property
    def FilePath(self) -> StringType: ...
    @property
    def HasFile(self) -> BooleanType: ...
    @property
    def Locations(self) -> ConfigurationLocationCollection: ...
    @property
    def NamespaceDeclared(self) -> BooleanType: ...
    @NamespaceDeclared.setter
    def NamespaceDeclared(self, value: BooleanType) -> None: ...
    @property
    def RootSectionGroup(self) -> ConfigurationSectionGroup: ...
    @property
    def SectionGroups(self) -> ConfigurationSectionGroupCollection: ...
    @property
    def Sections(self) -> ConfigurationSectionCollection: ...
    @property
    def TargetFramework(self) -> FrameworkName: ...
    @TargetFramework.setter
    def TargetFramework(self, value: FrameworkName) -> None: ...
    @property
    def TypeStringTransformer(self) -> Func[StringType, StringType]: ...
    @TypeStringTransformer.setter
    def TypeStringTransformer(self, value: Func[StringType, StringType]) -> None: ...

    # ---------- Methods ---------- #

    def GetSection(self, sectionName: StringType) -> ConfigurationSection: ...
    def GetSectionGroup(self, sectionGroupName: StringType) -> ConfigurationSectionGroup: ...
    @overload
    def Save(self) -> VoidType: ...
    @overload
    def Save(self, saveMode: ConfigurationSaveMode) -> VoidType: ...
    @overload
    def Save(self, saveMode: ConfigurationSaveMode, forceSaveAll: BooleanType) -> VoidType: ...
    @overload
    def SaveAs(self, filename: StringType) -> VoidType: ...
    @overload
    def SaveAs(self, filename: StringType, saveMode: ConfigurationSaveMode) -> VoidType: ...
    @overload
    def SaveAs(
        self, filename: StringType, saveMode: ConfigurationSaveMode, forceSaveAll: BooleanType
    ) -> VoidType: ...
    def get_AppSettings(self) -> AppSettingsSection: ...
    def get_AssemblyStringTransformer(self) -> Func[StringType, StringType]: ...
    def get_ConnectionStrings(self) -> ConnectionStringsSection: ...
    def get_EvaluationContext(self) -> ContextInformation: ...
    def get_FilePath(self) -> StringType: ...
    def get_HasFile(self) -> BooleanType: ...
    def get_Locations(self) -> ConfigurationLocationCollection: ...
    def get_NamespaceDeclared(self) -> BooleanType: ...
    def get_RootSectionGroup(self) -> ConfigurationSectionGroup: ...
    def get_SectionGroups(self) -> ConfigurationSectionGroupCollection: ...
    def get_Sections(self) -> ConfigurationSectionCollection: ...
    def get_TargetFramework(self) -> FrameworkName: ...
    def get_TypeStringTransformer(self) -> Func[StringType, StringType]: ...
    def set_AssemblyStringTransformer(self, value: Func[StringType, StringType]) -> VoidType: ...
    def set_NamespaceDeclared(self, value: BooleanType) -> VoidType: ...
    def set_TargetFramework(self, value: FrameworkName) -> VoidType: ...
    def set_TypeStringTransformer(self, value: Func[StringType, StringType]) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConfigurationBuilder(ABC, ProviderBase):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def ProcessConfigurationSection(
        self, configSection: ConfigurationSection
    ) -> ConfigurationSection: ...
    def ProcessRawXml(self, rawXml: XmlNode) -> XmlNode: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConfigurationBuilderChain(ConfigurationBuilder):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def Builders(self) -> List[ConfigurationBuilder]: ...

    # ---------- Methods ---------- #

    def Initialize(self, name: StringType, config: NameValueCollection) -> VoidType: ...
    def ProcessConfigurationSection(
        self, configSection: ConfigurationSection
    ) -> ConfigurationSection: ...
    def ProcessRawXml(self, rawXml: XmlNode) -> XmlNode: ...
    def get_Builders(self) -> List[ConfigurationBuilder]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConfigurationBuilderCollection(ProviderCollection, IEnumerable, ICollection):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    def __getitem__(self, key: StringType) -> ConfigurationBuilder: ...

    # ---------- Methods ---------- #

    def Add(self, builder: ProviderBase) -> VoidType: ...
    @overload
    def get_Item(self, name: StringType) -> ConfigurationBuilder: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConfigurationBuilderSettings(ConfigurationElement):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def Builders(self) -> ProviderSettingsCollection: ...

    # ---------- Methods ---------- #

    def get_Builders(self) -> ProviderSettingsCollection: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConfigurationBuildersSection(ConfigurationSection):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def Builders(self) -> ProviderSettingsCollection: ...

    # ---------- Methods ---------- #

    def GetBuilderFromName(self, builderName: StringType) -> ConfigurationBuilder: ...
    def get_Builders(self) -> ProviderSettingsCollection: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConfigurationCollectionAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, itemType: TypeType): ...

    # ---------- Properties ---------- #

    @property
    def AddItemName(self) -> StringType: ...
    @AddItemName.setter
    def AddItemName(self, value: StringType) -> None: ...
    @property
    def ClearItemsName(self) -> StringType: ...
    @ClearItemsName.setter
    def ClearItemsName(self, value: StringType) -> None: ...
    @property
    def CollectionType(self) -> ConfigurationElementCollectionType: ...
    @CollectionType.setter
    def CollectionType(self, value: ConfigurationElementCollectionType) -> None: ...
    @property
    def ItemType(self) -> TypeType: ...
    @property
    def RemoveItemName(self) -> StringType: ...
    @RemoveItemName.setter
    def RemoveItemName(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    def get_AddItemName(self) -> StringType: ...
    def get_ClearItemsName(self) -> StringType: ...
    def get_CollectionType(self) -> ConfigurationElementCollectionType: ...
    def get_ItemType(self) -> TypeType: ...
    def get_RemoveItemName(self) -> StringType: ...
    def set_AddItemName(self, value: StringType) -> VoidType: ...
    def set_ClearItemsName(self, value: StringType) -> VoidType: ...
    def set_CollectionType(self, value: ConfigurationElementCollectionType) -> VoidType: ...
    def set_RemoveItemName(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConfigurationConverterBase(ABC, TypeConverter):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def CanConvertFrom(self, ctx: ITypeDescriptorContext, type: TypeType) -> BooleanType: ...
    @overload
    def CanConvertTo(self, ctx: ITypeDescriptorContext, type: TypeType) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConfigurationElement(ABC, ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def CurrentConfiguration(self) -> Configuration: ...
    @property
    def ElementInformation(self) -> ElementInformation: ...
    @property
    def LockAllAttributesExcept(self) -> ConfigurationLockCollection: ...
    @property
    def LockAllElementsExcept(self) -> ConfigurationLockCollection: ...
    @property
    def LockAttributes(self) -> ConfigurationLockCollection: ...
    @property
    def LockElements(self) -> ConfigurationLockCollection: ...
    @property
    def LockItem(self) -> BooleanType: ...
    @LockItem.setter
    def LockItem(self, value: BooleanType) -> None: ...

    # ---------- Methods ---------- #

    def Equals(self, compareTo: ObjectType) -> BooleanType: ...
    def GetHashCode(self) -> IntType: ...
    def IsReadOnly(self) -> BooleanType: ...
    def get_CurrentConfiguration(self) -> Configuration: ...
    def get_ElementInformation(self) -> ElementInformation: ...
    def get_LockAllAttributesExcept(self) -> ConfigurationLockCollection: ...
    def get_LockAllElementsExcept(self) -> ConfigurationLockCollection: ...
    def get_LockAttributes(self) -> ConfigurationLockCollection: ...
    def get_LockElements(self) -> ConfigurationLockCollection: ...
    def get_LockItem(self) -> BooleanType: ...
    def set_LockItem(self, value: BooleanType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConfigurationElementCollection(ABC, ConfigurationElement, ICollection, IEnumerable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def CollectionType(self) -> ConfigurationElementCollectionType: ...
    @property
    def Count(self) -> IntType: ...
    @property
    def EmitClear(self) -> BooleanType: ...
    @EmitClear.setter
    def EmitClear(self, value: BooleanType) -> None: ...
    @property
    def IsSynchronized(self) -> BooleanType: ...
    @property
    def SyncRoot(self) -> ObjectType: ...

    # ---------- Methods ---------- #

    def CopyTo(self, array: ArrayType[ConfigurationElement], index: IntType) -> VoidType: ...
    def Equals(self, compareTo: ObjectType) -> BooleanType: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def GetHashCode(self) -> IntType: ...
    def IsReadOnly(self) -> BooleanType: ...
    def get_CollectionType(self) -> ConfigurationElementCollectionType: ...
    def get_Count(self) -> IntType: ...
    def get_EmitClear(self) -> BooleanType: ...
    def get_IsSynchronized(self) -> BooleanType: ...
    def get_SyncRoot(self) -> ObjectType: ...
    def set_EmitClear(self, value: BooleanType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConfigurationElementProperty(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, validator: ConfigurationValidatorBase): ...

    # ---------- Properties ---------- #

    @property
    def Validator(self) -> ConfigurationValidatorBase: ...

    # ---------- Methods ---------- #

    def get_Validator(self) -> ConfigurationValidatorBase: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConfigurationErrorsException(ConfigurationException, ISerializable, _Exception):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(
        self, message: StringType, inner: Exception, filename: StringType, line: IntType
    ): ...
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: StringType): ...
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    @overload
    def __init__(self, message: StringType, filename: StringType, line: IntType): ...
    @overload
    def __init__(self, message: StringType, node: XmlNode): ...
    @overload
    def __init__(self, message: StringType, inner: Exception, node: XmlNode): ...
    @overload
    def __init__(self, message: StringType, reader: XmlReader): ...
    @overload
    def __init__(self, message: StringType, inner: Exception, reader: XmlReader): ...

    # ---------- Properties ---------- #

    @property
    def BareMessage(self) -> StringType: ...
    @property
    def Errors(self) -> ICollection: ...
    @property
    def Filename(self) -> StringType: ...
    @property
    def Line(self) -> IntType: ...
    @property
    def Message(self) -> StringType: ...

    # ---------- Methods ---------- #

    @staticmethod
    @overload
    def GetFilename(node: XmlNode) -> StringType: ...
    @staticmethod
    @overload
    def GetFilename(reader: XmlReader) -> StringType: ...
    @staticmethod
    @overload
    def GetLineNumber(node: XmlNode) -> IntType: ...
    @staticmethod
    @overload
    def GetLineNumber(reader: XmlReader) -> IntType: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    def get_BareMessage(self) -> StringType: ...
    def get_Errors(self) -> ICollection: ...
    def get_Filename(self) -> StringType: ...
    def get_Line(self) -> IntType: ...
    def get_Message(self) -> StringType: ...

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
    def __init__(
        self, message: StringType, inner: Exception, filename: StringType, line: IntType
    ): ...

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

class ConfigurationFileMap(ObjectType, ICloneable):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, machineConfigFilename: StringType): ...

    # ---------- Properties ---------- #

    @property
    def MachineConfigFilename(self) -> StringType: ...
    @MachineConfigFilename.setter
    def MachineConfigFilename(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    def Clone(self) -> ObjectType: ...
    def get_MachineConfigFilename(self) -> StringType: ...
    def set_MachineConfigFilename(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConfigurationLocation(ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Path(self) -> StringType: ...

    # ---------- Methods ---------- #

    def OpenConfiguration(self) -> Configuration: ...
    def get_Path(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConfigurationLocationCollection(ReadOnlyCollectionBase, ICollection, IEnumerable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    def __getitem__(self, key: IntType) -> ConfigurationLocation: ...

    # ---------- Methods ---------- #

    def get_Item(self, index: IntType) -> ConfigurationLocation: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConfigurationLockCollection(ObjectType, IEnumerable, ICollection):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def AttributeList(self) -> StringType: ...
    @property
    def Count(self) -> IntType: ...
    @property
    def HasParentElements(self) -> BooleanType: ...
    @property
    def IsModified(self) -> BooleanType: ...
    @property
    def IsSynchronized(self) -> BooleanType: ...
    @property
    def SyncRoot(self) -> ObjectType: ...

    # ---------- Methods ---------- #

    def Add(self, name: StringType) -> VoidType: ...
    def Clear(self) -> VoidType: ...
    def Contains(self, name: StringType) -> BooleanType: ...
    def CopyTo(self, array: ArrayType[StringType], index: IntType) -> VoidType: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def IsReadOnly(self, name: StringType) -> BooleanType: ...
    def Remove(self, name: StringType) -> VoidType: ...
    def SetFromList(self, attributeList: StringType) -> VoidType: ...
    def get_AttributeList(self) -> StringType: ...
    def get_Count(self) -> IntType: ...
    def get_HasParentElements(self) -> BooleanType: ...
    def get_IsModified(self) -> BooleanType: ...
    def get_IsSynchronized(self) -> BooleanType: ...
    def get_SyncRoot(self) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConfigurationManager(ABC, ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @staticmethod
    @property
    def AppSettings() -> NameValueCollection: ...
    @staticmethod
    @property
    def ConnectionStrings() -> ConnectionStringSettingsCollection: ...

    # ---------- Methods ---------- #

    @staticmethod
    def GetSection(sectionName: StringType) -> ObjectType: ...
    @staticmethod
    @overload
    def OpenExeConfiguration(userLevel: ConfigurationUserLevel) -> Configuration: ...
    @staticmethod
    @overload
    def OpenExeConfiguration(exePath: StringType) -> Configuration: ...
    @staticmethod
    def OpenMachineConfiguration() -> Configuration: ...
    @staticmethod
    @overload
    def OpenMappedExeConfiguration(
        fileMap: ExeConfigurationFileMap, userLevel: ConfigurationUserLevel
    ) -> Configuration: ...
    @staticmethod
    @overload
    def OpenMappedExeConfiguration(
        fileMap: ExeConfigurationFileMap, userLevel: ConfigurationUserLevel, preLoad: BooleanType
    ) -> Configuration: ...
    @staticmethod
    def OpenMappedMachineConfiguration(fileMap: ConfigurationFileMap) -> Configuration: ...
    @staticmethod
    def RefreshSection(sectionName: StringType) -> VoidType: ...
    @staticmethod
    def get_AppSettings() -> NameValueCollection: ...
    @staticmethod
    def get_ConnectionStrings() -> ConnectionStringSettingsCollection: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConfigurationManagerHelperFactory(ABC, ObjectType):
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

class ConfigurationPermission(
    CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission
):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, state: PermissionState): ...

    # No Properties

    # ---------- Methods ---------- #

    def Copy(self) -> IPermission: ...
    def FromXml(self, securityElement: SecurityElement) -> VoidType: ...
    def Intersect(self, target: IPermission) -> IPermission: ...
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    def IsUnrestricted(self) -> BooleanType: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, target: IPermission) -> IPermission: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConfigurationPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, action: SecurityAction): ...

    # No Properties

    # ---------- Methods ---------- #

    def CreatePermission(self) -> IPermission: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConfigurationProperty(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, name: StringType, type: TypeType): ...
    @overload
    def __init__(self, name: StringType, type: TypeType, defaultValue: ObjectType): ...
    @overload
    def __init__(
        self,
        name: StringType,
        type: TypeType,
        defaultValue: ObjectType,
        options: ConfigurationPropertyOptions,
    ): ...
    @overload
    def __init__(
        self,
        name: StringType,
        type: TypeType,
        defaultValue: ObjectType,
        typeConverter: TypeConverter,
        validator: ConfigurationValidatorBase,
        options: ConfigurationPropertyOptions,
    ): ...
    @overload
    def __init__(
        self,
        name: StringType,
        type: TypeType,
        defaultValue: ObjectType,
        typeConverter: TypeConverter,
        validator: ConfigurationValidatorBase,
        options: ConfigurationPropertyOptions,
        description: StringType,
    ): ...

    # ---------- Properties ---------- #

    @property
    def Converter(self) -> TypeConverter: ...
    @property
    def DefaultValue(self) -> ObjectType: ...
    @property
    def Description(self) -> StringType: ...
    @property
    def IsAssemblyStringTransformationRequired(self) -> BooleanType: ...
    @property
    def IsDefaultCollection(self) -> BooleanType: ...
    @property
    def IsKey(self) -> BooleanType: ...
    @property
    def IsRequired(self) -> BooleanType: ...
    @property
    def IsTypeStringTransformationRequired(self) -> BooleanType: ...
    @property
    def IsVersionCheckRequired(self) -> BooleanType: ...
    @property
    def Name(self) -> StringType: ...
    @property
    def Type(self) -> TypeType: ...
    @property
    def Validator(self) -> ConfigurationValidatorBase: ...

    # ---------- Methods ---------- #

    def get_Converter(self) -> TypeConverter: ...
    def get_DefaultValue(self) -> ObjectType: ...
    def get_Description(self) -> StringType: ...
    def get_IsAssemblyStringTransformationRequired(self) -> BooleanType: ...
    def get_IsDefaultCollection(self) -> BooleanType: ...
    def get_IsKey(self) -> BooleanType: ...
    def get_IsRequired(self) -> BooleanType: ...
    def get_IsTypeStringTransformationRequired(self) -> BooleanType: ...
    def get_IsVersionCheckRequired(self) -> BooleanType: ...
    def get_Name(self) -> StringType: ...
    def get_Type(self) -> TypeType: ...
    def get_Validator(self) -> ConfigurationValidatorBase: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConfigurationPropertyAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, name: StringType): ...

    # ---------- Properties ---------- #

    @property
    def DefaultValue(self) -> ObjectType: ...
    @DefaultValue.setter
    def DefaultValue(self, value: ObjectType) -> None: ...
    @property
    def IsDefaultCollection(self) -> BooleanType: ...
    @IsDefaultCollection.setter
    def IsDefaultCollection(self, value: BooleanType) -> None: ...
    @property
    def IsKey(self) -> BooleanType: ...
    @IsKey.setter
    def IsKey(self, value: BooleanType) -> None: ...
    @property
    def IsRequired(self) -> BooleanType: ...
    @IsRequired.setter
    def IsRequired(self, value: BooleanType) -> None: ...
    @property
    def Name(self) -> StringType: ...
    @property
    def Options(self) -> ConfigurationPropertyOptions: ...
    @Options.setter
    def Options(self, value: ConfigurationPropertyOptions) -> None: ...

    # ---------- Methods ---------- #

    def get_DefaultValue(self) -> ObjectType: ...
    def get_IsDefaultCollection(self) -> BooleanType: ...
    def get_IsKey(self) -> BooleanType: ...
    def get_IsRequired(self) -> BooleanType: ...
    def get_Name(self) -> StringType: ...
    def get_Options(self) -> ConfigurationPropertyOptions: ...
    def set_DefaultValue(self, value: ObjectType) -> VoidType: ...
    def set_IsDefaultCollection(self, value: BooleanType) -> VoidType: ...
    def set_IsKey(self, value: BooleanType) -> VoidType: ...
    def set_IsRequired(self, value: BooleanType) -> VoidType: ...
    def set_Options(self, value: ConfigurationPropertyOptions) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConfigurationPropertyCollection(ObjectType, ICollection, IEnumerable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def Count(self) -> IntType: ...
    @property
    def IsSynchronized(self) -> BooleanType: ...
    def __getitem__(self, key: StringType) -> ConfigurationProperty: ...
    @property
    def SyncRoot(self) -> ObjectType: ...

    # ---------- Methods ---------- #

    def Add(self, property: ConfigurationProperty) -> VoidType: ...
    def Clear(self) -> VoidType: ...
    def Contains(self, name: StringType) -> BooleanType: ...
    def CopyTo(self, array: ArrayType[ConfigurationProperty], index: IntType) -> VoidType: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def Remove(self, name: StringType) -> BooleanType: ...
    def get_Count(self) -> IntType: ...
    def get_IsSynchronized(self) -> BooleanType: ...
    def get_Item(self, name: StringType) -> ConfigurationProperty: ...
    def get_SyncRoot(self) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConfigurationSchemaErrors(ObjectType):
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

class ConfigurationSection(ABC, ConfigurationElement):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def SectionInformation(self) -> SectionInformation: ...

    # ---------- Methods ---------- #

    def get_SectionInformation(self) -> SectionInformation: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConfigurationSectionCollection(
    NameObjectCollectionBase, ICollection, IEnumerable, ISerializable, IDeserializationCallback
):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Count(self) -> IntType: ...
    def __getitem__(self, key: StringType) -> ConfigurationSection: ...
    def __getitem__(self, key: IntType) -> ConfigurationSection: ...
    @property
    def Keys(self) -> KeysCollection: ...

    # ---------- Methods ---------- #

    def Add(self, name: StringType, section: ConfigurationSection) -> VoidType: ...
    def Clear(self) -> VoidType: ...
    def CopyTo(self, array: ArrayType[ConfigurationSection], index: IntType) -> VoidType: ...
    @overload
    def Get(self, index: IntType) -> ConfigurationSection: ...
    @overload
    def Get(self, name: StringType) -> ConfigurationSection: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def GetKey(self, index: IntType) -> StringType: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    def Remove(self, name: StringType) -> VoidType: ...
    def RemoveAt(self, index: IntType) -> VoidType: ...
    def get_Count(self) -> IntType: ...
    @overload
    def get_Item(self, name: StringType) -> ConfigurationSection: ...
    @overload
    def get_Item(self, index: IntType) -> ConfigurationSection: ...
    def get_Keys(self) -> KeysCollection: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConfigurationSectionGroup(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def IsDeclarationRequired(self) -> BooleanType: ...
    @property
    def IsDeclared(self) -> BooleanType: ...
    @property
    def Name(self) -> StringType: ...
    @property
    def SectionGroupName(self) -> StringType: ...
    @property
    def SectionGroups(self) -> ConfigurationSectionGroupCollection: ...
    @property
    def Sections(self) -> ConfigurationSectionCollection: ...
    @property
    def Type(self) -> StringType: ...
    @Type.setter
    def Type(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    @overload
    def ForceDeclaration(self) -> VoidType: ...
    @overload
    def ForceDeclaration(self, force: BooleanType) -> VoidType: ...
    def get_IsDeclarationRequired(self) -> BooleanType: ...
    def get_IsDeclared(self) -> BooleanType: ...
    def get_Name(self) -> StringType: ...
    def get_SectionGroupName(self) -> StringType: ...
    def get_SectionGroups(self) -> ConfigurationSectionGroupCollection: ...
    def get_Sections(self) -> ConfigurationSectionCollection: ...
    def get_Type(self) -> StringType: ...
    def set_Type(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConfigurationSectionGroupCollection(
    NameObjectCollectionBase, ICollection, IEnumerable, ISerializable, IDeserializationCallback
):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Count(self) -> IntType: ...
    def __getitem__(self, key: StringType) -> ConfigurationSectionGroup: ...
    def __getitem__(self, key: IntType) -> ConfigurationSectionGroup: ...
    @property
    def Keys(self) -> KeysCollection: ...

    # ---------- Methods ---------- #

    def Add(self, name: StringType, sectionGroup: ConfigurationSectionGroup) -> VoidType: ...
    def Clear(self) -> VoidType: ...
    def CopyTo(self, array: ArrayType[ConfigurationSectionGroup], index: IntType) -> VoidType: ...
    @overload
    def Get(self, index: IntType) -> ConfigurationSectionGroup: ...
    @overload
    def Get(self, name: StringType) -> ConfigurationSectionGroup: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def GetKey(self, index: IntType) -> StringType: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    def Remove(self, name: StringType) -> VoidType: ...
    def RemoveAt(self, index: IntType) -> VoidType: ...
    def get_Count(self) -> IntType: ...
    @overload
    def get_Item(self, name: StringType) -> ConfigurationSectionGroup: ...
    @overload
    def get_Item(self, index: IntType) -> ConfigurationSectionGroup: ...
    def get_Keys(self) -> KeysCollection: ...

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

class ConfigurationStringConstants(ABC, ObjectType):
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

class ConfigurationValidatorAttribute(Attribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, validator: TypeType): ...

    # ---------- Properties ---------- #

    @property
    def ValidatorInstance(self) -> ConfigurationValidatorBase: ...
    @property
    def ValidatorType(self) -> TypeType: ...

    # ---------- Methods ---------- #

    def get_ValidatorInstance(self) -> ConfigurationValidatorBase: ...
    def get_ValidatorType(self) -> TypeType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConfigurationValidatorBase(ABC, ObjectType):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def CanValidate(self, type: TypeType) -> BooleanType: ...
    def Validate(self, value: ObjectType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConfigurationValue(ObjectType):
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

class ConfigurationValues(
    NameObjectCollectionBase, ICollection, IEnumerable, ISerializable, IDeserializationCallback
):
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

class ConnectionStringSettings(ConfigurationElement):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, name: StringType, connectionString: StringType): ...
    @overload
    def __init__(
        self, name: StringType, connectionString: StringType, providerName: StringType
    ): ...

    # ---------- Properties ---------- #

    @property
    def ConnectionString(self) -> StringType: ...
    @ConnectionString.setter
    def ConnectionString(self, value: StringType) -> None: ...
    @property
    def Name(self) -> StringType: ...
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    @property
    def ProviderName(self) -> StringType: ...
    @ProviderName.setter
    def ProviderName(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    def ToString(self) -> StringType: ...
    def get_ConnectionString(self) -> StringType: ...
    def get_Name(self) -> StringType: ...
    def get_ProviderName(self) -> StringType: ...
    def set_ConnectionString(self, value: StringType) -> VoidType: ...
    def set_Name(self, value: StringType) -> VoidType: ...
    def set_ProviderName(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConnectionStringSettingsCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    def __getitem__(self, key: IntType) -> ConnectionStringSettings: ...
    def __setitem__(self, key: IntType, value: ConnectionStringSettings) -> None: ...
    def __getitem__(self, key: StringType) -> ConnectionStringSettings: ...

    # ---------- Methods ---------- #

    def Add(self, settings: ConnectionStringSettings) -> VoidType: ...
    def Clear(self) -> VoidType: ...
    def IndexOf(self, settings: ConnectionStringSettings) -> IntType: ...
    @overload
    def Remove(self, settings: ConnectionStringSettings) -> VoidType: ...
    @overload
    def Remove(self, name: StringType) -> VoidType: ...
    def RemoveAt(self, index: IntType) -> VoidType: ...
    @overload
    def get_Item(self, index: IntType) -> ConnectionStringSettings: ...
    @overload
    def get_Item(self, name: StringType) -> ConnectionStringSettings: ...
    def set_Item(self, index: IntType, value: ConnectionStringSettings) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ConnectionStringsSection(ConfigurationSection):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def ConnectionStrings(self) -> ConnectionStringSettingsCollection: ...

    # ---------- Methods ---------- #

    def get_ConnectionStrings(self) -> ConnectionStringSettingsCollection: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ContextInformation(ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def HostingContext(self) -> ObjectType: ...
    @property
    def IsMachineLevel(self) -> BooleanType: ...

    # ---------- Methods ---------- #

    def GetSection(self, sectionName: StringType) -> ObjectType: ...
    def get_HostingContext(self) -> ObjectType: ...
    def get_IsMachineLevel(self) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Debug(ABC, ObjectType):
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

class DeclarationUpdate(Update):
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

class DefaultSection(ConfigurationSection):
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

class DefaultValidator(ConfigurationValidatorBase):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def CanValidate(self, type: TypeType) -> BooleanType: ...
    def Validate(self, value: ObjectType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class DefinitionUpdate(Update):
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

class DpapiProtectedConfigurationProvider(ProtectedConfigurationProvider):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def UseMachineProtection(self) -> BooleanType: ...

    # ---------- Methods ---------- #

    def Decrypt(self, encryptedNode: XmlNode) -> XmlNode: ...
    def Encrypt(self, node: XmlNode) -> XmlNode: ...
    def Initialize(
        self, name: StringType, configurationValues: NameValueCollection
    ) -> VoidType: ...
    def get_UseMachineProtection(self) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ElementInformation(ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Errors(self) -> ICollection: ...
    @property
    def IsCollection(self) -> BooleanType: ...
    @property
    def IsLocked(self) -> BooleanType: ...
    @property
    def IsPresent(self) -> BooleanType: ...
    @property
    def LineNumber(self) -> IntType: ...
    @property
    def Properties(self) -> PropertyInformationCollection: ...
    @property
    def Source(self) -> StringType: ...
    @property
    def Type(self) -> TypeType: ...
    @property
    def Validator(self) -> ConfigurationValidatorBase: ...

    # ---------- Methods ---------- #

    def get_Errors(self) -> ICollection: ...
    def get_IsCollection(self) -> BooleanType: ...
    def get_IsLocked(self) -> BooleanType: ...
    def get_IsPresent(self) -> BooleanType: ...
    def get_LineNumber(self) -> IntType: ...
    def get_Properties(self) -> PropertyInformationCollection: ...
    def get_Source(self) -> StringType: ...
    def get_Type(self) -> TypeType: ...
    def get_Validator(self) -> ConfigurationValidatorBase: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EmptyImpersonationContext(ObjectType, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def Dispose(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ErrorInfoXmlDocument(XmlDocument, ICloneable, IEnumerable, IXPathNavigable, IConfigErrorInfo):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def CreateAttribute(
        self, prefix: StringType, localName: StringType, namespaceUri: StringType
    ) -> XmlAttribute: ...
    def CreateCDataSection(self, data: StringType) -> XmlCDataSection: ...
    def CreateComment(self, data: StringType) -> XmlComment: ...
    @overload
    def CreateElement(
        self, prefix: StringType, localName: StringType, namespaceUri: StringType
    ) -> XmlElement: ...
    def CreateSignificantWhitespace(self, data: StringType) -> XmlSignificantWhitespace: ...
    def CreateTextNode(self, text: StringType) -> XmlText: ...
    def CreateWhitespace(self, data: StringType) -> XmlWhitespace: ...
    @overload
    def Load(self, filename: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ErrorsHelper(ABC, ObjectType):
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

class ExceptionUtil(ABC, ObjectType):
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

class ExeConfigurationFileMap(ConfigurationFileMap, ICloneable):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, machineConfigFileName: StringType): ...

    # ---------- Properties ---------- #

    @property
    def ExeConfigFilename(self) -> StringType: ...
    @ExeConfigFilename.setter
    def ExeConfigFilename(self, value: StringType) -> None: ...
    @property
    def LocalUserConfigFilename(self) -> StringType: ...
    @LocalUserConfigFilename.setter
    def LocalUserConfigFilename(self, value: StringType) -> None: ...
    @property
    def RoamingUserConfigFilename(self) -> StringType: ...
    @RoamingUserConfigFilename.setter
    def RoamingUserConfigFilename(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    def Clone(self) -> ObjectType: ...
    def get_ExeConfigFilename(self) -> StringType: ...
    def get_LocalUserConfigFilename(self) -> StringType: ...
    def get_RoamingUserConfigFilename(self) -> StringType: ...
    def set_ExeConfigFilename(self, value: StringType) -> VoidType: ...
    def set_LocalUserConfigFilename(self, value: StringType) -> VoidType: ...
    def set_RoamingUserConfigFilename(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ExeContext(ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def ExePath(self) -> StringType: ...
    @property
    def UserLevel(self) -> ConfigurationUserLevel: ...

    # ---------- Methods ---------- #

    def get_ExePath(self) -> StringType: ...
    def get_UserLevel(self) -> ConfigurationUserLevel: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class FactoryId(ObjectType):
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

class FactoryRecord(ObjectType, IConfigErrorInfo):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Filename(self) -> StringType: ...
    @Filename.setter
    def Filename(self, value: StringType) -> None: ...
    @property
    def LineNumber(self) -> IntType: ...
    @LineNumber.setter
    def LineNumber(self, value: IntType) -> None: ...

    # ---------- Methods ---------- #

    def get_Filename(self) -> StringType: ...
    def get_LineNumber(self) -> IntType: ...
    def set_Filename(self, value: StringType) -> VoidType: ...
    def set_LineNumber(self, value: IntType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class FileUtil(ABC, ObjectType):
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

class FipsAwareEncryptedXml(EncryptedXml):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, doc: XmlDocument): ...

    # No Properties

    # ---------- Methods ---------- #

    def GetDecryptionKey(
        self, encryptedData: EncryptedData, symmetricAlgorithmUri: StringType
    ) -> SymmetricAlgorithm: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class GenericEnumConverter(ConfigurationConverterBase):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, typeEnum: TypeType): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def ConvertFrom(
        self, ctx: ITypeDescriptorContext, ci: CultureInfo, data: ObjectType
    ) -> ObjectType: ...
    @overload
    def ConvertTo(
        self, ctx: ITypeDescriptorContext, ci: CultureInfo, value: ObjectType, type: TypeType
    ) -> ObjectType: ...

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

class IgnoreSection(ConfigurationSection):
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

class IgnoreSectionHandler(ObjectType, IConfigurationSectionHandler):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def Create(
        self, parent: ObjectType, configContext: ObjectType, section: XmlNode
    ) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class InfiniteIntConverter(ConfigurationConverterBase):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def ConvertFrom(
        self, ctx: ITypeDescriptorContext, ci: CultureInfo, data: ObjectType
    ) -> ObjectType: ...
    @overload
    def ConvertTo(
        self, ctx: ITypeDescriptorContext, ci: CultureInfo, value: ObjectType, type: TypeType
    ) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class InfiniteTimeSpanConverter(ConfigurationConverterBase):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def ConvertFrom(
        self, ctx: ITypeDescriptorContext, ci: CultureInfo, data: ObjectType
    ) -> ObjectType: ...
    @overload
    def ConvertTo(
        self, ctx: ITypeDescriptorContext, ci: CultureInfo, value: ObjectType, type: TypeType
    ) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class IntegerValidator(ConfigurationValidatorBase):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, minValue: IntType, maxValue: IntType): ...
    @overload
    def __init__(self, minValue: IntType, maxValue: IntType, rangeIsExclusive: BooleanType): ...
    @overload
    def __init__(
        self,
        minValue: IntType,
        maxValue: IntType,
        rangeIsExclusive: BooleanType,
        resolution: IntType,
    ): ...

    # No Properties

    # ---------- Methods ---------- #

    def CanValidate(self, type: TypeType) -> BooleanType: ...
    def Validate(self, value: ObjectType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class IntegerValidatorAttribute(ConfigurationValidatorAttribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def ExcludeRange(self) -> BooleanType: ...
    @ExcludeRange.setter
    def ExcludeRange(self, value: BooleanType) -> None: ...
    @property
    def MaxValue(self) -> IntType: ...
    @MaxValue.setter
    def MaxValue(self, value: IntType) -> None: ...
    @property
    def MinValue(self) -> IntType: ...
    @MinValue.setter
    def MinValue(self, value: IntType) -> None: ...
    @property
    def ValidatorInstance(self) -> ConfigurationValidatorBase: ...

    # ---------- Methods ---------- #

    def get_ExcludeRange(self) -> BooleanType: ...
    def get_MaxValue(self) -> IntType: ...
    def get_MinValue(self) -> IntType: ...
    def get_ValidatorInstance(self) -> ConfigurationValidatorBase: ...
    def set_ExcludeRange(self, value: BooleanType) -> VoidType: ...
    def set_MaxValue(self, value: IntType) -> VoidType: ...
    def set_MinValue(self, value: IntType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class InvalidPropValue(ObjectType):
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

class KeyValueConfigurationCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def AllKeys(self) -> ArrayType[StringType]: ...
    def __getitem__(self, key: StringType) -> KeyValueConfigurationElement: ...

    # ---------- Methods ---------- #

    @overload
    def Add(self, key: StringType, value: StringType) -> VoidType: ...
    @overload
    def Add(self, keyValue: KeyValueConfigurationElement) -> VoidType: ...
    def Clear(self) -> VoidType: ...
    def Remove(self, key: StringType) -> VoidType: ...
    def get_AllKeys(self) -> ArrayType[StringType]: ...
    def get_Item(self, key: StringType) -> KeyValueConfigurationElement: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class KeyValueConfigurationElement(ConfigurationElement):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, key: StringType, value: StringType): ...

    # ---------- Properties ---------- #

    @property
    def Key(self) -> StringType: ...
    @property
    def Value(self) -> StringType: ...
    @Value.setter
    def Value(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    def get_Key(self) -> StringType: ...
    def get_Value(self) -> StringType: ...
    def set_Value(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class KeyValueInternalCollection(
    NameValueCollection, ICollection, IEnumerable, ISerializable, IDeserializationCallback
):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, root: AppSettingsSection): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def Add(self, key: StringType, value: StringType) -> VoidType: ...
    def Clear(self) -> VoidType: ...
    def Remove(self, key: StringType) -> VoidType: ...

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

    def GetPreviousVersion(
        self, context: SettingsContext, property: SettingsProperty
    ) -> SettingsPropertyValue: ...
    def GetPropertyValues(
        self, context: SettingsContext, properties: SettingsPropertyCollection
    ) -> SettingsPropertyValueCollection: ...
    def Initialize(self, name: StringType, values: NameValueCollection) -> VoidType: ...
    def Reset(self, context: SettingsContext) -> VoidType: ...
    def SetPropertyValues(
        self, context: SettingsContext, values: SettingsPropertyValueCollection
    ) -> VoidType: ...
    def Upgrade(
        self, context: SettingsContext, properties: SettingsPropertyCollection
    ) -> VoidType: ...
    def get_ApplicationName(self) -> StringType: ...
    def set_ApplicationName(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class LocationSectionRecord(ObjectType):
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

class LocationUpdates(ObjectType):
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

class LongValidator(ConfigurationValidatorBase):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, minValue: LongType, maxValue: LongType): ...
    @overload
    def __init__(self, minValue: LongType, maxValue: LongType, rangeIsExclusive: BooleanType): ...
    @overload
    def __init__(
        self,
        minValue: LongType,
        maxValue: LongType,
        rangeIsExclusive: BooleanType,
        resolution: LongType,
    ): ...

    # No Properties

    # ---------- Methods ---------- #

    def CanValidate(self, type: TypeType) -> BooleanType: ...
    def Validate(self, value: ObjectType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class LongValidatorAttribute(ConfigurationValidatorAttribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def ExcludeRange(self) -> BooleanType: ...
    @ExcludeRange.setter
    def ExcludeRange(self, value: BooleanType) -> None: ...
    @property
    def MaxValue(self) -> LongType: ...
    @MaxValue.setter
    def MaxValue(self, value: LongType) -> None: ...
    @property
    def MinValue(self) -> LongType: ...
    @MinValue.setter
    def MinValue(self, value: LongType) -> None: ...
    @property
    def ValidatorInstance(self) -> ConfigurationValidatorBase: ...

    # ---------- Methods ---------- #

    def get_ExcludeRange(self) -> BooleanType: ...
    def get_MaxValue(self) -> LongType: ...
    def get_MinValue(self) -> LongType: ...
    def get_ValidatorInstance(self) -> ConfigurationValidatorBase: ...
    def set_ExcludeRange(self, value: BooleanType) -> VoidType: ...
    def set_MaxValue(self, value: LongType) -> VoidType: ...
    def set_MinValue(self, value: LongType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class MgmtConfigurationRecord(BaseConfigurationRecord, IInternalConfigRecord):
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

class NameValueConfigurationCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def AllKeys(self) -> ArrayType[StringType]: ...
    def __getitem__(self, key: StringType) -> NameValueConfigurationElement: ...
    def __setitem__(self, key: StringType, value: NameValueConfigurationElement) -> None: ...

    # ---------- Methods ---------- #

    def Add(self, nameValue: NameValueConfigurationElement) -> VoidType: ...
    def Clear(self) -> VoidType: ...
    @overload
    def Remove(self, nameValue: NameValueConfigurationElement) -> VoidType: ...
    @overload
    def Remove(self, name: StringType) -> VoidType: ...
    def get_AllKeys(self) -> ArrayType[StringType]: ...
    def get_Item(self, name: StringType) -> NameValueConfigurationElement: ...
    def set_Item(self, name: StringType, value: NameValueConfigurationElement) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class NameValueConfigurationElement(ConfigurationElement):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, name: StringType, value: StringType): ...

    # ---------- Properties ---------- #

    @property
    def Name(self) -> StringType: ...
    @property
    def Value(self) -> StringType: ...
    @Value.setter
    def Value(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    def get_Name(self) -> StringType: ...
    def get_Value(self) -> StringType: ...
    def set_Value(self, value: StringType) -> VoidType: ...

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

    def Create(
        self, parent: ObjectType, configContext: ObjectType, section: XmlNode
    ) -> ObjectType: ...

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

class PositiveTimeSpanValidator(ConfigurationValidatorBase):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def CanValidate(self, type: TypeType) -> BooleanType: ...
    def Validate(self, value: ObjectType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class PositiveTimeSpanValidatorAttribute(ConfigurationValidatorAttribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def ValidatorInstance(self) -> ConfigurationValidatorBase: ...

    # ---------- Methods ---------- #

    def get_ValidatorInstance(self) -> ConfigurationValidatorBase: ...

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

class PropertyInformation(ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Converter(self) -> TypeConverter: ...
    @property
    def DefaultValue(self) -> ObjectType: ...
    @property
    def Description(self) -> StringType: ...
    @property
    def IsKey(self) -> BooleanType: ...
    @property
    def IsLocked(self) -> BooleanType: ...
    @property
    def IsModified(self) -> BooleanType: ...
    @property
    def IsRequired(self) -> BooleanType: ...
    @property
    def LineNumber(self) -> IntType: ...
    @property
    def Name(self) -> StringType: ...
    @property
    def Source(self) -> StringType: ...
    @property
    def Type(self) -> TypeType: ...
    @property
    def Validator(self) -> ConfigurationValidatorBase: ...
    @property
    def Value(self) -> ObjectType: ...
    @Value.setter
    def Value(self, value: ObjectType) -> None: ...
    @property
    def ValueOrigin(self) -> PropertyValueOrigin: ...

    # ---------- Methods ---------- #

    def get_Converter(self) -> TypeConverter: ...
    def get_DefaultValue(self) -> ObjectType: ...
    def get_Description(self) -> StringType: ...
    def get_IsKey(self) -> BooleanType: ...
    def get_IsLocked(self) -> BooleanType: ...
    def get_IsModified(self) -> BooleanType: ...
    def get_IsRequired(self) -> BooleanType: ...
    def get_LineNumber(self) -> IntType: ...
    def get_Name(self) -> StringType: ...
    def get_Source(self) -> StringType: ...
    def get_Type(self) -> TypeType: ...
    def get_Validator(self) -> ConfigurationValidatorBase: ...
    def get_Value(self) -> ObjectType: ...
    def get_ValueOrigin(self) -> PropertyValueOrigin: ...
    def set_Value(self, value: ObjectType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class PropertyInformationCollection(
    NameObjectCollectionBase, ICollection, IEnumerable, ISerializable, IDeserializationCallback
):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    def __getitem__(self, key: StringType) -> PropertyInformation: ...

    # ---------- Methods ---------- #

    def CopyTo(self, array: ArrayType[PropertyInformation], index: IntType) -> VoidType: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    def get_Item(self, propertyName: StringType) -> PropertyInformation: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class PropertySourceInfo(ObjectType):
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

class ProtectedConfiguration(ABC, ObjectType):
    # ---------- Fields ---------- #

    @staticmethod
    @property
    def DataProtectionProviderName() -> StringType: ...
    @staticmethod
    @property
    def ProtectedDataSectionName() -> StringType: ...
    @staticmethod
    @property
    def RsaProviderName() -> StringType: ...

    # No Constructors

    # ---------- Properties ---------- #

    @staticmethod
    @property
    def DefaultProvider() -> StringType: ...
    @staticmethod
    @property
    def Providers() -> ProtectedConfigurationProviderCollection: ...

    # ---------- Methods ---------- #

    @staticmethod
    def get_DefaultProvider() -> StringType: ...
    @staticmethod
    def get_Providers() -> ProtectedConfigurationProviderCollection: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ProtectedConfigurationProvider(ABC, ProviderBase):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def Decrypt(self, encryptedNode: XmlNode) -> XmlNode: ...
    def Encrypt(self, node: XmlNode) -> XmlNode: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ProtectedConfigurationProviderCollection(ProviderCollection, IEnumerable, ICollection):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    def __getitem__(self, key: StringType) -> ProtectedConfigurationProvider: ...

    # ---------- Methods ---------- #

    def Add(self, provider: ProviderBase) -> VoidType: ...
    @overload
    def get_Item(self, name: StringType) -> ProtectedConfigurationProvider: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ProtectedConfigurationSection(ConfigurationSection):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def DefaultProvider(self) -> StringType: ...
    @DefaultProvider.setter
    def DefaultProvider(self, value: StringType) -> None: ...
    @property
    def Providers(self) -> ProviderSettingsCollection: ...

    # ---------- Methods ---------- #

    def get_DefaultProvider(self) -> StringType: ...
    def get_Providers(self) -> ProviderSettingsCollection: ...
    def set_DefaultProvider(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ProtectedProviderSettings(ConfigurationElement):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def Providers(self) -> ProviderSettingsCollection: ...

    # ---------- Methods ---------- #

    def get_Providers(self) -> ProviderSettingsCollection: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ProviderSettings(ConfigurationElement):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, name: StringType, type: StringType): ...

    # ---------- Properties ---------- #

    @property
    def Name(self) -> StringType: ...
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    @property
    def Parameters(self) -> NameValueCollection: ...
    @property
    def Type(self) -> StringType: ...
    @Type.setter
    def Type(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    def get_Name(self) -> StringType: ...
    def get_Parameters(self) -> NameValueCollection: ...
    def get_Type(self) -> StringType: ...
    def set_Name(self, value: StringType) -> VoidType: ...
    def set_Type(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ProviderSettingsCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    def __getitem__(self, key: StringType) -> ProviderSettings: ...
    def __getitem__(self, key: IntType) -> ProviderSettings: ...
    def __setitem__(self, key: IntType, value: ProviderSettings) -> None: ...

    # ---------- Methods ---------- #

    def Add(self, provider: ProviderSettings) -> VoidType: ...
    def Clear(self) -> VoidType: ...
    def Remove(self, name: StringType) -> VoidType: ...
    @overload
    def get_Item(self, key: StringType) -> ProviderSettings: ...
    @overload
    def get_Item(self, index: IntType) -> ProviderSettings: ...
    def set_Item(self, index: IntType, value: ProviderSettings) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ReadOnlyNameValueCollection(
    NameValueCollection, ICollection, IEnumerable, ISerializable, IDeserializationCallback
):
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

class RegexStringValidator(ConfigurationValidatorBase):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, regex: StringType): ...

    # No Properties

    # ---------- Methods ---------- #

    def CanValidate(self, type: TypeType) -> BooleanType: ...
    def Validate(self, value: ObjectType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RegexStringValidatorAttribute(ConfigurationValidatorAttribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, regex: StringType): ...

    # ---------- Properties ---------- #

    @property
    def Regex(self) -> StringType: ...
    @property
    def ValidatorInstance(self) -> ConfigurationValidatorBase: ...

    # ---------- Methods ---------- #

    def get_Regex(self) -> StringType: ...
    def get_ValidatorInstance(self) -> ConfigurationValidatorBase: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RsaProtectedConfigurationProvider(ProtectedConfigurationProvider):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def CspProviderName(self) -> StringType: ...
    @property
    def KeyContainerName(self) -> StringType: ...
    @property
    def RsaPublicKey(self) -> RSAParameters: ...
    @property
    def UseFIPS(self) -> BooleanType: ...
    @property
    def UseMachineContainer(self) -> BooleanType: ...
    @property
    def UseOAEP(self) -> BooleanType: ...

    # ---------- Methods ---------- #

    def AddKey(self, keySize: IntType, exportable: BooleanType) -> VoidType: ...
    def Decrypt(self, encryptedNode: XmlNode) -> XmlNode: ...
    def DeleteKey(self) -> VoidType: ...
    def Encrypt(self, node: XmlNode) -> XmlNode: ...
    def ExportKey(
        self, xmlFileName: StringType, includePrivateParameters: BooleanType
    ) -> VoidType: ...
    def ImportKey(self, xmlFileName: StringType, exportable: BooleanType) -> VoidType: ...
    def Initialize(
        self, name: StringType, configurationValues: NameValueCollection
    ) -> VoidType: ...
    def get_CspProviderName(self) -> StringType: ...
    def get_KeyContainerName(self) -> StringType: ...
    def get_RsaPublicKey(self) -> RSAParameters: ...
    def get_UseFIPS(self) -> BooleanType: ...
    def get_UseMachineContainer(self) -> BooleanType: ...
    def get_UseOAEP(self) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RuntimeConfigurationRecord(BaseConfigurationRecord, IInternalConfigRecord):
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

class SR(ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @staticmethod
    @property
    def Resources() -> ResourceManager: ...

    # ---------- Methods ---------- #

    @staticmethod
    def GetObject(name: StringType) -> ObjectType: ...
    @staticmethod
    @overload
    def GetString(name: StringType) -> StringType: ...
    @staticmethod
    @overload
    def GetString(
        name: StringType, usedFallback: BooleanType
    ) -> Tuple[StringType, BooleanType]: ...
    @staticmethod
    @overload
    def GetString(name: StringType, args: ArrayType[ObjectType]) -> StringType: ...
    @staticmethod
    def get_Resources() -> ResourceManager: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SRCategoryAttribute(CategoryAttribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, category: StringType): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SRDescriptionAttribute(DescriptionAttribute, _Attribute):
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
    def __getitem__(self, key: IntType) -> SchemeSettingElement: ...
    def __getitem__(self, key: StringType) -> SchemeSettingElement: ...

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

class SectionInformation(ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def AllowDefinition(self) -> ConfigurationAllowDefinition: ...
    @AllowDefinition.setter
    def AllowDefinition(self, value: ConfigurationAllowDefinition) -> None: ...
    @property
    def AllowExeDefinition(self) -> ConfigurationAllowExeDefinition: ...
    @AllowExeDefinition.setter
    def AllowExeDefinition(self, value: ConfigurationAllowExeDefinition) -> None: ...
    @property
    def AllowLocation(self) -> BooleanType: ...
    @AllowLocation.setter
    def AllowLocation(self, value: BooleanType) -> None: ...
    @property
    def AllowOverride(self) -> BooleanType: ...
    @AllowOverride.setter
    def AllowOverride(self, value: BooleanType) -> None: ...
    @property
    def ConfigSource(self) -> StringType: ...
    @ConfigSource.setter
    def ConfigSource(self, value: StringType) -> None: ...
    @property
    def ConfigurationBuilder(self) -> ConfigurationBuilder: ...
    @property
    def ForceSave(self) -> BooleanType: ...
    @ForceSave.setter
    def ForceSave(self, value: BooleanType) -> None: ...
    @property
    def InheritInChildApplications(self) -> BooleanType: ...
    @InheritInChildApplications.setter
    def InheritInChildApplications(self, value: BooleanType) -> None: ...
    @property
    def IsDeclarationRequired(self) -> BooleanType: ...
    @property
    def IsDeclared(self) -> BooleanType: ...
    @property
    def IsLocked(self) -> BooleanType: ...
    @property
    def IsProtected(self) -> BooleanType: ...
    @property
    def Name(self) -> StringType: ...
    @property
    def OverrideMode(self) -> OverrideMode: ...
    @OverrideMode.setter
    def OverrideMode(self, value: OverrideMode) -> None: ...
    @property
    def OverrideModeDefault(self) -> OverrideMode: ...
    @OverrideModeDefault.setter
    def OverrideModeDefault(self, value: OverrideMode) -> None: ...
    @property
    def OverrideModeEffective(self) -> OverrideMode: ...
    @property
    def ProtectionProvider(self) -> ProtectedConfigurationProvider: ...
    @property
    def RequirePermission(self) -> BooleanType: ...
    @RequirePermission.setter
    def RequirePermission(self, value: BooleanType) -> None: ...
    @property
    def RestartOnExternalChanges(self) -> BooleanType: ...
    @RestartOnExternalChanges.setter
    def RestartOnExternalChanges(self, value: BooleanType) -> None: ...
    @property
    def SectionName(self) -> StringType: ...
    @property
    def Type(self) -> StringType: ...
    @Type.setter
    def Type(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    @overload
    def ForceDeclaration(self) -> VoidType: ...
    @overload
    def ForceDeclaration(self, force: BooleanType) -> VoidType: ...
    def GetParentSection(self) -> ConfigurationSection: ...
    def GetRawXml(self) -> StringType: ...
    def ProtectSection(self, protectionProvider: StringType) -> VoidType: ...
    def RevertToParent(self) -> VoidType: ...
    def SetRawXml(self, rawXml: StringType) -> VoidType: ...
    def UnprotectSection(self) -> VoidType: ...
    def get_AllowDefinition(self) -> ConfigurationAllowDefinition: ...
    def get_AllowExeDefinition(self) -> ConfigurationAllowExeDefinition: ...
    def get_AllowLocation(self) -> BooleanType: ...
    def get_AllowOverride(self) -> BooleanType: ...
    def get_ConfigSource(self) -> StringType: ...
    def get_ConfigurationBuilder(self) -> ConfigurationBuilder: ...
    def get_ForceSave(self) -> BooleanType: ...
    def get_InheritInChildApplications(self) -> BooleanType: ...
    def get_IsDeclarationRequired(self) -> BooleanType: ...
    def get_IsDeclared(self) -> BooleanType: ...
    def get_IsLocked(self) -> BooleanType: ...
    def get_IsProtected(self) -> BooleanType: ...
    def get_Name(self) -> StringType: ...
    def get_OverrideMode(self) -> OverrideMode: ...
    def get_OverrideModeDefault(self) -> OverrideMode: ...
    def get_OverrideModeEffective(self) -> OverrideMode: ...
    def get_ProtectionProvider(self) -> ProtectedConfigurationProvider: ...
    def get_RequirePermission(self) -> BooleanType: ...
    def get_RestartOnExternalChanges(self) -> BooleanType: ...
    def get_SectionName(self) -> StringType: ...
    def get_Type(self) -> StringType: ...
    def set_AllowDefinition(self, value: ConfigurationAllowDefinition) -> VoidType: ...
    def set_AllowExeDefinition(self, value: ConfigurationAllowExeDefinition) -> VoidType: ...
    def set_AllowLocation(self, value: BooleanType) -> VoidType: ...
    def set_AllowOverride(self, value: BooleanType) -> VoidType: ...
    def set_ConfigSource(self, value: StringType) -> VoidType: ...
    def set_ForceSave(self, value: BooleanType) -> VoidType: ...
    def set_InheritInChildApplications(self, value: BooleanType) -> VoidType: ...
    def set_OverrideMode(self, value: OverrideMode) -> VoidType: ...
    def set_OverrideModeDefault(self, value: OverrideMode) -> VoidType: ...
    def set_RequirePermission(self, value: BooleanType) -> VoidType: ...
    def set_RestartOnExternalChanges(self, value: BooleanType) -> VoidType: ...
    def set_Type(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SectionInput(ObjectType):
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

class SectionRecord(ObjectType):
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

class SectionUpdates(ObjectType):
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

class SectionXmlInfo(ObjectType, IConfigErrorInfo):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Filename(self) -> StringType: ...
    @property
    def LineNumber(self) -> IntType: ...
    @LineNumber.setter
    def LineNumber(self, value: IntType) -> None: ...

    # ---------- Methods ---------- #

    def get_Filename(self) -> StringType: ...
    def get_LineNumber(self) -> IntType: ...
    def set_LineNumber(self, value: IntType) -> VoidType: ...

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

    def __init__(
        self,
        settingName: StringType,
        settingClass: StringType,
        settingKey: StringType,
        newValue: ObjectType,
        cancel: BooleanType,
    ): ...

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

    def BeginInvoke(
        self,
        sender: ObjectType,
        e: SettingChangingEventArgs,
        callback: AsyncCallback,
        object: ObjectType,
    ) -> IAsyncResult: ...
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

class SettingsAttributeDictionary(
    Hashtable,
    IDictionary,
    ICollection,
    IEnumerable,
    ISerializable,
    IDeserializationCallback,
    ICloneable,
):
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
    def __getitem__(self, key: StringType) -> ObjectType: ...
    def __setitem__(self, key: StringType, value: ObjectType) -> None: ...
    @property
    def Properties(self) -> SettingsPropertyCollection: ...
    @property
    def PropertyValues(self) -> SettingsPropertyValueCollection: ...
    @property
    def Providers(self) -> SettingsProviderCollection: ...

    # ---------- Methods ---------- #

    def Initialize(
        self,
        context: SettingsContext,
        properties: SettingsPropertyCollection,
        providers: SettingsProviderCollection,
    ) -> VoidType: ...
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

class SettingsContext(
    Hashtable,
    IDictionary,
    ICollection,
    IEnumerable,
    ISerializable,
    IDeserializationCallback,
    ICloneable,
):
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

    def BeginInvoke(
        self,
        sender: ObjectType,
        e: SettingsLoadedEventArgs,
        callback: AsyncCallback,
        object: ObjectType,
    ) -> IAsyncResult: ...
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
    def __init__(
        self,
        name: StringType,
        propertyType: TypeType,
        provider: SettingsProvider,
        isReadOnly: BooleanType,
        defaultValue: ObjectType,
        serializeAs: SettingsSerializeAs,
        attributes: SettingsAttributeDictionary,
        throwOnErrorDeserializing: BooleanType,
        throwOnErrorSerializing: BooleanType,
    ): ...
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
    def __getitem__(self, key: StringType) -> SettingsProperty: ...
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
    def __getitem__(self, key: StringType) -> SettingsPropertyValue: ...
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

    def GetPropertyValues(
        self, context: SettingsContext, collection: SettingsPropertyCollection
    ) -> SettingsPropertyValueCollection: ...
    def SetPropertyValues(
        self, context: SettingsContext, collection: SettingsPropertyValueCollection
    ) -> VoidType: ...
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

    def __getitem__(self, key: StringType) -> SettingsProvider: ...

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

    def BeginInvoke(
        self, sender: ObjectType, e: CancelEventArgs, callback: AsyncCallback, object: ObjectType
    ) -> IAsyncResult: ...
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

class StreamInfo(ObjectType):
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

class StreamUpdate(ObjectType):
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

class StringUtil(ABC, ObjectType):
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

class StringValidator(ConfigurationValidatorBase):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, minLength: IntType): ...
    @overload
    def __init__(self, minLength: IntType, maxLength: IntType): ...
    @overload
    def __init__(self, minLength: IntType, maxLength: IntType, invalidCharacters: StringType): ...

    # No Properties

    # ---------- Methods ---------- #

    def CanValidate(self, type: TypeType) -> BooleanType: ...
    def Validate(self, value: ObjectType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class StringValidatorAttribute(ConfigurationValidatorAttribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def InvalidCharacters(self) -> StringType: ...
    @InvalidCharacters.setter
    def InvalidCharacters(self, value: StringType) -> None: ...
    @property
    def MaxLength(self) -> IntType: ...
    @MaxLength.setter
    def MaxLength(self, value: IntType) -> None: ...
    @property
    def MinLength(self) -> IntType: ...
    @MinLength.setter
    def MinLength(self, value: IntType) -> None: ...
    @property
    def ValidatorInstance(self) -> ConfigurationValidatorBase: ...

    # ---------- Methods ---------- #

    def get_InvalidCharacters(self) -> StringType: ...
    def get_MaxLength(self) -> IntType: ...
    def get_MinLength(self) -> IntType: ...
    def get_ValidatorInstance(self) -> ConfigurationValidatorBase: ...
    def set_InvalidCharacters(self, value: StringType) -> VoidType: ...
    def set_MaxLength(self, value: IntType) -> VoidType: ...
    def set_MinLength(self, value: IntType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SubclassTypeValidator(ConfigurationValidatorBase):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, baseClass: TypeType): ...

    # No Properties

    # ---------- Methods ---------- #

    def CanValidate(self, type: TypeType) -> BooleanType: ...
    def Validate(self, value: ObjectType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SubclassTypeValidatorAttribute(ConfigurationValidatorAttribute, _Attribute):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, baseClass: TypeType): ...

    # ---------- Properties ---------- #

    @property
    def BaseClass(self) -> TypeType: ...
    @property
    def ValidatorInstance(self) -> ConfigurationValidatorBase: ...

    # ---------- Methods ---------- #

    def get_BaseClass(self) -> TypeType: ...
    def get_ValidatorInstance(self) -> ConfigurationValidatorBase: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class TimeSpanMinutesConverter(ConfigurationConverterBase):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def ConvertFrom(
        self, ctx: ITypeDescriptorContext, ci: CultureInfo, data: ObjectType
    ) -> ObjectType: ...
    @overload
    def ConvertTo(
        self, ctx: ITypeDescriptorContext, ci: CultureInfo, value: ObjectType, type: TypeType
    ) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class TimeSpanMinutesOrInfiniteConverter(TimeSpanMinutesConverter):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def ConvertFrom(
        self, ctx: ITypeDescriptorContext, ci: CultureInfo, data: ObjectType
    ) -> ObjectType: ...
    @overload
    def ConvertTo(
        self, ctx: ITypeDescriptorContext, ci: CultureInfo, value: ObjectType, type: TypeType
    ) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class TimeSpanSecondsConverter(ConfigurationConverterBase):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def ConvertFrom(
        self, ctx: ITypeDescriptorContext, ci: CultureInfo, data: ObjectType
    ) -> ObjectType: ...
    @overload
    def ConvertTo(
        self, ctx: ITypeDescriptorContext, ci: CultureInfo, value: ObjectType, type: TypeType
    ) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class TimeSpanSecondsOrInfiniteConverter(TimeSpanSecondsConverter):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def ConvertFrom(
        self, ctx: ITypeDescriptorContext, ci: CultureInfo, data: ObjectType
    ) -> ObjectType: ...
    @overload
    def ConvertTo(
        self, ctx: ITypeDescriptorContext, ci: CultureInfo, value: ObjectType, type: TypeType
    ) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class TimeSpanValidator(ConfigurationValidatorBase):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, minValue: TimeSpan, maxValue: TimeSpan): ...
    @overload
    def __init__(self, minValue: TimeSpan, maxValue: TimeSpan, rangeIsExclusive: BooleanType): ...
    @overload
    def __init__(
        self,
        minValue: TimeSpan,
        maxValue: TimeSpan,
        rangeIsExclusive: BooleanType,
        resolutionInSeconds: LongType,
    ): ...

    # No Properties

    # ---------- Methods ---------- #

    def CanValidate(self, type: TypeType) -> BooleanType: ...
    def Validate(self, value: ObjectType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class TimeSpanValidatorAttribute(ConfigurationValidatorAttribute, _Attribute):
    # ---------- Fields ---------- #

    @staticmethod
    @property
    def TimeSpanMaxValue() -> StringType: ...
    @staticmethod
    @property
    def TimeSpanMinValue() -> StringType: ...

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def ExcludeRange(self) -> BooleanType: ...
    @ExcludeRange.setter
    def ExcludeRange(self, value: BooleanType) -> None: ...
    @property
    def MaxValue(self) -> TimeSpan: ...
    @property
    def MaxValueString(self) -> StringType: ...
    @MaxValueString.setter
    def MaxValueString(self, value: StringType) -> None: ...
    @property
    def MinValue(self) -> TimeSpan: ...
    @property
    def MinValueString(self) -> StringType: ...
    @MinValueString.setter
    def MinValueString(self, value: StringType) -> None: ...
    @property
    def ValidatorInstance(self) -> ConfigurationValidatorBase: ...

    # ---------- Methods ---------- #

    def get_ExcludeRange(self) -> BooleanType: ...
    def get_MaxValue(self) -> TimeSpan: ...
    def get_MaxValueString(self) -> StringType: ...
    def get_MinValue(self) -> TimeSpan: ...
    def get_MinValueString(self) -> StringType: ...
    def get_ValidatorInstance(self) -> ConfigurationValidatorBase: ...
    def set_ExcludeRange(self, value: BooleanType) -> VoidType: ...
    def set_MaxValueString(self, value: StringType) -> VoidType: ...
    def set_MinValueString(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class TypeNameConverter(ConfigurationConverterBase):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def ConvertFrom(
        self, ctx: ITypeDescriptorContext, ci: CultureInfo, data: ObjectType
    ) -> ObjectType: ...
    @overload
    def ConvertTo(
        self, ctx: ITypeDescriptorContext, ci: CultureInfo, value: ObjectType, type: TypeType
    ) -> ObjectType: ...

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

class Update(ABC, ObjectType):
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

class UpdateConfigHost(
    DelegatingConfigHost, IInternalConfigHost, IInternalConfigurationBuilderHost
):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def DeleteStream(self, streamName: StringType) -> VoidType: ...
    def GetStreamVersion(self, streamName: StringType) -> ObjectType: ...
    def IsConfigRecordRequired(self, configPath: StringType) -> BooleanType: ...
    def IsFile(self, streamName: StringType) -> BooleanType: ...
    @overload
    def OpenStreamForRead(self, streamName: StringType) -> Stream: ...
    @overload
    def OpenStreamForWrite(
        self, streamName: StringType, templateStreamName: StringType, writeContext: ObjectType
    ) -> Tuple[Stream, ObjectType]: ...
    @overload
    def WriteCompleted(
        self, streamName: StringType, success: BooleanType, writeContext: ObjectType
    ) -> VoidType: ...

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

class UrlPath(ABC, ObjectType):
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

class ValidatorCallback(MulticastDelegate, ICloneable, ISerializable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, object: ObjectType, method: NIntType): ...

    # No Properties

    # ---------- Methods ---------- #

    def BeginInvoke(
        self, value: ObjectType, callback: AsyncCallback, object: ObjectType
    ) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    def Invoke(self, value: ObjectType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ValidatorUtils(ABC, ObjectType):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    def HelperParamValidation(value: ObjectType, allowedType: TypeType) -> VoidType: ...
    @staticmethod
    @overload
    def ValidateScalar(
        value: TimeSpan,
        min: TimeSpan,
        max: TimeSpan,
        resolutionInSeconds: LongType,
        exclusiveRange: BooleanType,
    ) -> VoidType: ...
    @staticmethod
    @overload
    def ValidateScalar(
        value: T, min: T, max: T, resolution: T, exclusiveRange: BooleanType
    ) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class WhiteSpaceTrimStringConverter(ConfigurationConverterBase):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def ConvertFrom(
        self, ctx: ITypeDescriptorContext, ci: CultureInfo, data: ObjectType
    ) -> ObjectType: ...
    @overload
    def ConvertTo(
        self, ctx: ITypeDescriptorContext, ci: CultureInfo, value: ObjectType, type: TypeType
    ) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class XmlUtil(ObjectType, IDisposable, IConfigErrorInfo):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Filename(self) -> StringType: ...
    @property
    def LineNumber(self) -> IntType: ...

    # ---------- Methods ---------- #

    def Dispose(self) -> VoidType: ...
    def get_Filename(self) -> StringType: ...
    def get_LineNumber(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class XmlUtilWriter(ObjectType):
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

# ---------- Structs ---------- #

class CRYPTPROTECT_PROMPTSTRUCT(ValueType, IDisposable):
    # ---------- Fields ---------- #

    @property
    def cbSize(self) -> IntType: ...
    @cbSize.setter
    def cbSize(self, value: IntType) -> None: ...
    @property
    def dwPromptFlags(self) -> IntType: ...
    @dwPromptFlags.setter
    def dwPromptFlags(self, value: IntType) -> None: ...
    @property
    def hwndApp(self) -> NIntType: ...
    @hwndApp.setter
    def hwndApp(self, value: NIntType) -> None: ...
    @property
    def szPrompt(self) -> StringType: ...
    @szPrompt.setter
    def szPrompt(self, value: StringType) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class DATA_BLOB(ValueType, IDisposable):
    # ---------- Fields ---------- #

    @property
    def cbData(self) -> IntType: ...
    @cbData.setter
    def cbData(self, value: IntType) -> None: ...
    @property
    def pbData(self) -> NIntType: ...
    @pbData.setter
    def pbData(self, value: NIntType) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class OverrideModeSetting(ValueType):
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

class SafeBitVector32(ValueType):
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

class SimpleBitVector32(ValueType):
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

    def GetPreviousVersion(
        self, context: SettingsContext, property: SettingsProperty
    ) -> SettingsPropertyValue: ...
    def Reset(self, context: SettingsContext) -> VoidType: ...
    def Upgrade(
        self, context: SettingsContext, properties: SettingsPropertyCollection
    ) -> VoidType: ...

    # No Events

class IConfigurationSectionHandler(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def Create(
        self, parent: ObjectType, configContext: ObjectType, section: XmlNode
    ) -> ObjectType: ...

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

class ConfigurationAllowDefinition(Enum):
    MachineOnly = 0
    MachineToWebRoot = 100
    MachineToApplication = 200
    Everywhere = 300

class ConfigurationAllowExeDefinition(Enum):
    MachineOnly = 0
    MachineToApplication = 100
    MachineToRoamingUser = 200
    MachineToLocalUser = 300

class ConfigurationElementCollectionType(Enum):
    BasicMap = 0
    AddRemoveClearMap = 1
    BasicMapAlternate = 2
    AddRemoveClearMapAlternate = 3

class ConfigurationLockCollectionType(Enum):
    LockedAttributes = 1
    LockedExceptionList = 2
    LockedElements = 3
    LockedElementsExceptionList = 4

class ConfigurationPropertyOptions(Enum):
    # None = 0
    IsDefaultCollection = 1
    IsRequired = 2
    IsKey = 4
    IsTypeStringTransformationRequired = 8
    IsAssemblyStringTransformationRequired = 16
    IsVersionCheckRequired = 32

class ConfigurationSaveMode(Enum):
    Modified = 0
    Minimal = 1
    Full = 2

class ConfigurationUserLevel(Enum):
    # None = 0
    PerUserRoaming = 10
    PerUserRoamingAndLocal = 20

class ConfigurationValueFlags(Enum):
    Default = 0
    Inherited = 1
    Modified = 2
    Locked = 4
    XMLParentInherited = 8

class ExceptionAction(Enum):
    NonSpecific = 0
    Local = 1
    Global = 2

class NamespaceChange(Enum):
    # None = 0
    Add = 1
    Remove = 2

class OverrideMode(Enum):
    Inherit = 0
    Allow = 1
    Deny = 2

class PropertyValueOrigin(Enum):
    Default = 0
    Inherited = 1
    SetHere = 2

class SettingsManageability(Enum):
    Roaming = 0

class SettingsSerializeAs(Enum):
    String = 0
    Xml = 1
    Binary = 2
    ProviderSpecific = 3

class SpecialSetting(Enum):
    ConnectionString = 0
    WebServiceUrl = 1

# ---------- Delegates ---------- #

SettingChangingEventHandler = Callable[[ObjectType, SettingChangingEventArgs], VoidType]

SettingsLoadedEventHandler = Callable[[ObjectType, SettingsLoadedEventArgs], VoidType]

SettingsSavingEventHandler = Callable[[ObjectType, CancelEventArgs], VoidType]

ValidatorCallback = Callable[[ObjectType], VoidType]

__all__ = [
    AppSettingsReader,
    AppSettingsSection,
    ApplicationScopedSettingAttribute,
    ApplicationSettingsBase,
    ApplicationSettingsGroup,
    BaseConfigurationRecord,
    CallbackValidator,
    CallbackValidatorAttribute,
    ClientConfigPaths,
    ClientConfigurationHost,
    ClientConfigurationSystem,
    ClientSettingsSection,
    ClientSettingsStore,
    CommaDelimitedStringCollection,
    CommaDelimitedStringCollectionConverter,
    CommonConfigurationStrings,
    ConfigDefinitionUpdates,
    ConfigPathUtility,
    ConfigXmlAttribute,
    ConfigXmlCDataSection,
    ConfigXmlComment,
    ConfigXmlDocument,
    ConfigXmlElement,
    ConfigXmlReader,
    ConfigXmlSignificantWhitespace,
    ConfigXmlText,
    ConfigXmlWhitespace,
    Configuration,
    ConfigurationBuilder,
    ConfigurationBuilderChain,
    ConfigurationBuilderCollection,
    ConfigurationBuilderSettings,
    ConfigurationBuildersSection,
    ConfigurationCollectionAttribute,
    ConfigurationConverterBase,
    ConfigurationElement,
    ConfigurationElementCollection,
    ConfigurationElementProperty,
    ConfigurationErrorsException,
    ConfigurationException,
    ConfigurationFileMap,
    ConfigurationLocation,
    ConfigurationLocationCollection,
    ConfigurationLockCollection,
    ConfigurationManager,
    ConfigurationManagerHelperFactory,
    ConfigurationManagerInternalFactory,
    ConfigurationPermission,
    ConfigurationPermissionAttribute,
    ConfigurationProperty,
    ConfigurationPropertyAttribute,
    ConfigurationPropertyCollection,
    ConfigurationSchemaErrors,
    ConfigurationSection,
    ConfigurationSectionCollection,
    ConfigurationSectionGroup,
    ConfigurationSectionGroupCollection,
    ConfigurationSettings,
    ConfigurationStringConstants,
    ConfigurationValidatorAttribute,
    ConfigurationValidatorBase,
    ConfigurationValue,
    ConfigurationValues,
    ConnectionStringSettings,
    ConnectionStringSettingsCollection,
    ConnectionStringsSection,
    ContextInformation,
    Debug,
    DeclarationUpdate,
    DefaultSection,
    DefaultSettingValueAttribute,
    DefaultValidator,
    DefinitionUpdate,
    DictionarySectionHandler,
    DpapiProtectedConfigurationProvider,
    ElementInformation,
    EmptyImpersonationContext,
    ErrorInfoXmlDocument,
    ErrorsHelper,
    ExceptionUtil,
    ExeConfigurationFileMap,
    ExeContext,
    FactoryId,
    FactoryRecord,
    FileUtil,
    FipsAwareEncryptedXml,
    GenericEnumConverter,
    HandlerBase,
    IdnElement,
    IgnoreSection,
    IgnoreSectionHandler,
    InfiniteIntConverter,
    InfiniteTimeSpanConverter,
    IntegerValidator,
    IntegerValidatorAttribute,
    InvalidPropValue,
    IriParsingElement,
    KeyValueConfigurationCollection,
    KeyValueConfigurationElement,
    KeyValueInternalCollection,
    LocalFileSettingsProvider,
    LocationSectionRecord,
    LocationUpdates,
    LongValidator,
    LongValidatorAttribute,
    MgmtConfigurationRecord,
    NameValueConfigurationCollection,
    NameValueConfigurationElement,
    NameValueFileSectionHandler,
    NameValueSectionHandler,
    NoSettingsVersionUpgradeAttribute,
    PositiveTimeSpanValidator,
    PositiveTimeSpanValidatorAttribute,
    PrivilegedConfigurationManager,
    PropertyInformation,
    PropertyInformationCollection,
    PropertySourceInfo,
    ProtectedConfiguration,
    ProtectedConfigurationProvider,
    ProtectedConfigurationProviderCollection,
    ProtectedConfigurationSection,
    ProtectedProviderSettings,
    ProviderSettings,
    ProviderSettingsCollection,
    ReadOnlyNameValueCollection,
    RegexStringValidator,
    RegexStringValidatorAttribute,
    RsaProtectedConfigurationProvider,
    RuntimeConfigurationRecord,
    SR,
    SRCategoryAttribute,
    SRDescriptionAttribute,
    SchemeSettingElement,
    SchemeSettingElementCollection,
    SchemeSettingInternal,
    SectionInformation,
    SectionInput,
    SectionRecord,
    SectionUpdates,
    SectionXmlInfo,
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
    StreamInfo,
    StreamUpdate,
    StringUtil,
    StringValidator,
    StringValidatorAttribute,
    SubclassTypeValidator,
    SubclassTypeValidatorAttribute,
    TimeSpanMinutesConverter,
    TimeSpanMinutesOrInfiniteConverter,
    TimeSpanSecondsConverter,
    TimeSpanSecondsOrInfiniteConverter,
    TimeSpanValidator,
    TimeSpanValidatorAttribute,
    TypeNameConverter,
    TypeUtil,
    Update,
    UpdateConfigHost,
    UriSection,
    UriSectionData,
    UriSectionInternal,
    UriSectionReader,
    UrlPath,
    UserScopedSettingAttribute,
    UserSettingsGroup,
    ValidatorCallback,
    ValidatorUtils,
    WhiteSpaceTrimStringConverter,
    XmlUtil,
    XmlUtilWriter,
    CRYPTPROTECT_PROMPTSTRUCT,
    DATA_BLOB,
    OverrideModeSetting,
    SafeBitVector32,
    SimpleBitVector32,
    StoredSetting,
    IApplicationSettingsProvider,
    IConfigurationSectionHandler,
    IConfigurationSystem,
    IPersistComponentSettings,
    ISettingsProviderService,
    ConfigurationAllowDefinition,
    ConfigurationAllowExeDefinition,
    ConfigurationElementCollectionType,
    ConfigurationLockCollectionType,
    ConfigurationPropertyOptions,
    ConfigurationSaveMode,
    ConfigurationUserLevel,
    ConfigurationValueFlags,
    ExceptionAction,
    NamespaceChange,
    OverrideMode,
    PropertyValueOrigin,
    SettingsManageability,
    SettingsSerializeAs,
    SpecialSetting,
    SettingChangingEventHandler,
    SettingsLoadedEventHandler,
    SettingsSavingEventHandler,
    ValidatorCallback,
]
