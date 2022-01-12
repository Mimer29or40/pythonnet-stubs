from __future__ import annotations

from typing import Callable, Generic, List, Protocol, Tuple, TypeVar, Union, overload

from System import Array, AsyncCallback, Boolean, EventArgs, IAsyncResult, ICloneable, IDisposable, Int32, IntPtr, MulticastDelegate, Object, String, Type, Void
from System.Configuration import BaseConfigurationRecord, Configuration, ConfigurationAllowDefinition, ConfigurationAllowExeDefinition, ConfigurationBuilder, ConfigurationSection, ProtectedConfigurationProvider, ProtectedConfigurationSection
from System.IO import Stream
from System.Runtime.Serialization import ISerializable
from System.Security import PermissionSet
from System.Xml import XmlNode

# ---------- Types ---------- #

T = TypeVar('T')

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]


class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    
    def __isub__(self, other: T): ...



# ---------- Classes ---------- #

class ConfigSystem(ObjectType, IConfigSystem):
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


class ConfigurationManagerHelper(ObjectType, IConfigurationManagerHelper):
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


class ConfigurationManagerInternal(ObjectType, IConfigurationManagerInternal):
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


class DelegatingConfigHost(ObjectType, IInternalConfigHost, IInternalConfigurationBuilderHost):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsRemote(self) -> BooleanType: ...
    
    @property
    def SupportsChangeNotifications(self) -> BooleanType: ...
    
    @property
    def SupportsLocation(self) -> BooleanType: ...
    
    @property
    def SupportsPath(self) -> BooleanType: ...
    
    @property
    def SupportsRefresh(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def CreateConfigurationContext(self, configPath: StringType, locationSubPath: StringType) -> ObjectType: ...
    
    def CreateDeprecatedConfigContext(self, configPath: StringType) -> ObjectType: ...
    
    def DecryptSection(self, encryptedXml: StringType, protectionProvider: ProtectedConfigurationProvider, protectedConfigSection: ProtectedConfigurationSection) -> StringType: ...
    
    def DeleteStream(self, streamName: StringType) -> VoidType: ...
    
    def EncryptSection(self, clearTextXml: StringType, protectionProvider: ProtectedConfigurationProvider, protectedConfigSection: ProtectedConfigurationSection) -> StringType: ...
    
    def GetConfigPathFromLocationSubPath(self, configPath: StringType, locationSubPath: StringType) -> StringType: ...
    
    def GetConfigType(self, typeName: StringType, throwOnError: BooleanType) -> TypeType: ...
    
    def GetConfigTypeName(self, t: TypeType) -> StringType: ...
    
    def GetRestrictedPermissions(self, configRecord: IInternalConfigRecord, permissionSet: PermissionSet, isHostReady: BooleanType) -> Tuple[VoidType, PermissionSet, BooleanType]: ...
    
    def GetStreamName(self, configPath: StringType) -> StringType: ...
    
    def GetStreamNameForConfigSource(self, streamName: StringType, configSource: StringType) -> StringType: ...
    
    def GetStreamVersion(self, streamName: StringType) -> ObjectType: ...
    
    def Impersonate(self) -> IDisposable: ...
    
    def Init(self, configRoot: IInternalConfigRoot, hostInitParams: ArrayType[ObjectType]) -> VoidType: ...
    
    def InitForConfiguration(self, locationSubPath: StringType, configPath: StringType, locationConfigPath: StringType, configRoot: IInternalConfigRoot, hostInitConfigurationParams: ArrayType[ObjectType]) -> Tuple[VoidType, StringType, StringType, StringType]: ...
    
    def IsAboveApplication(self, configPath: StringType) -> BooleanType: ...
    
    def IsConfigRecordRequired(self, configPath: StringType) -> BooleanType: ...
    
    def IsDefinitionAllowed(self, configPath: StringType, allowDefinition: ConfigurationAllowDefinition, allowExeDefinition: ConfigurationAllowExeDefinition) -> BooleanType: ...
    
    def IsFile(self, streamName: StringType) -> BooleanType: ...
    
    def IsFullTrustSectionWithoutAptcaAllowed(self, configRecord: IInternalConfigRecord) -> BooleanType: ...
    
    def IsInitDelayed(self, configRecord: IInternalConfigRecord) -> BooleanType: ...
    
    def IsLocationApplicable(self, configPath: StringType) -> BooleanType: ...
    
    def IsSecondaryRoot(self, configPath: StringType) -> BooleanType: ...
    
    def IsTrustedConfigPath(self, configPath: StringType) -> BooleanType: ...
    
    @overload
    def OpenStreamForRead(self, streamName: StringType) -> Stream: ...
    
    @overload
    def OpenStreamForRead(self, streamName: StringType, assertPermissions: BooleanType) -> Stream: ...
    
    @overload
    def OpenStreamForWrite(self, streamName: StringType, templateStreamName: StringType, writeContext: ObjectType) -> Tuple[Stream, ObjectType]: ...
    
    @overload
    def OpenStreamForWrite(self, streamName: StringType, templateStreamName: StringType, writeContext: ObjectType, assertPermissions: BooleanType) -> Tuple[Stream, ObjectType]: ...
    
    def PrefetchAll(self, configPath: StringType, streamName: StringType) -> BooleanType: ...
    
    def PrefetchSection(self, sectionGroupName: StringType, sectionName: StringType) -> BooleanType: ...
    
    def ProcessConfigurationSection(self, configSection: ConfigurationSection, builder: ConfigurationBuilder) -> ConfigurationSection: ...
    
    def ProcessRawXml(self, rawXml: XmlNode, builder: ConfigurationBuilder) -> XmlNode: ...
    
    def RequireCompleteInit(self, configRecord: IInternalConfigRecord) -> VoidType: ...
    
    def StartMonitoringStreamForChanges(self, streamName: StringType, callback: StreamChangeCallback) -> ObjectType: ...
    
    def StopMonitoringStreamForChanges(self, streamName: StringType, callback: StreamChangeCallback) -> VoidType: ...
    
    def VerifyDefinitionAllowed(self, configPath: StringType, allowDefinition: ConfigurationAllowDefinition, allowExeDefinition: ConfigurationAllowExeDefinition, errorInfo: IConfigErrorInfo) -> VoidType: ...
    
    @overload
    def WriteCompleted(self, streamName: StringType, success: BooleanType, writeContext: ObjectType) -> VoidType: ...
    
    @overload
    def WriteCompleted(self, streamName: StringType, success: BooleanType, writeContext: ObjectType, assertPermissions: BooleanType) -> VoidType: ...
    
    def get_IsRemote(self) -> BooleanType: ...
    
    def get_SupportsChangeNotifications(self) -> BooleanType: ...
    
    def get_SupportsLocation(self) -> BooleanType: ...
    
    def get_SupportsPath(self) -> BooleanType: ...
    
    def get_SupportsRefresh(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileVersion(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InternalConfigConfigurationFactory(ObjectType, IInternalConfigConfigurationFactory):
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


class InternalConfigEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, configPath: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ConfigPath(self) -> StringType: ...
    
    @ConfigPath.setter
    def ConfigPath(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_ConfigPath(self) -> StringType: ...
    
    def set_ConfigPath(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InternalConfigEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: InternalConfigEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: InternalConfigEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InternalConfigHost(ObjectType, IInternalConfigHost, IInternalConfigurationBuilderHost):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def IsSecondaryRoot(self, configPath: StringType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InternalConfigRoot(ObjectType, IInternalConfigRoot):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ClearResult(self, configRecord: BaseConfigurationRecord, configKey: StringType, forceEvaluation: BooleanType) -> VoidType: ...
    
    def GetConfigRecord(self, configPath: StringType) -> IInternalConfigRecord: ...
    
    def GetSection(self, section: StringType, configPath: StringType) -> ObjectType: ...
    
    def GetUniqueConfigPath(self, configPath: StringType) -> StringType: ...
    
    def GetUniqueConfigRecord(self, configPath: StringType) -> IInternalConfigRecord: ...
    
    def RemoveConfig(self, configPath: StringType) -> VoidType: ...
    
    def RemoveConfigRecord(self, configRecord: BaseConfigurationRecord) -> VoidType: ...
    
    def add_ConfigChanged(self, value: InternalConfigEventHandler) -> VoidType: ...
    
    def add_ConfigRemoved(self, value: InternalConfigEventHandler) -> VoidType: ...
    
    def remove_ConfigChanged(self, value: InternalConfigEventHandler) -> VoidType: ...
    
    def remove_ConfigRemoved(self, value: InternalConfigEventHandler) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    ConfigChanged: EventType[InternalConfigEventHandler] = ...
    
    ConfigRemoved: EventType[InternalConfigEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InternalConfigSettingsFactory(ObjectType, IInternalConfigSettingsFactory):
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


class StreamChangeCallback(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, streamName: StringType, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, streamName: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WriteFileContext(ObjectType):
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


# No Structs

# ---------- Interfaces ---------- #

class IConfigErrorInfo(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Filename(self) -> StringType: ...
    
    @property
    def LineNumber(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_Filename(self) -> StringType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    # No Events


class IConfigSystem(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Host(self) -> IInternalConfigHost: ...
    
    @property
    def Root(self) -> IInternalConfigRoot: ...
    
    # ---------- Methods ---------- #
    
    def Init(self, typeConfigHost: TypeType, hostInitParams: ArrayType[ObjectType]) -> VoidType: ...
    
    def get_Host(self) -> IInternalConfigHost: ...
    
    def get_Root(self) -> IInternalConfigRoot: ...
    
    # No Events


class IConfigurationManagerHelper(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def EnsureNetConfigLoaded(self) -> VoidType: ...
    
    # No Events


class IConfigurationManagerInternal(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def ApplicationConfigUri(self) -> StringType: ...
    
    @property
    def ExeLocalConfigDirectory(self) -> StringType: ...
    
    @property
    def ExeLocalConfigPath(self) -> StringType: ...
    
    @property
    def ExeProductName(self) -> StringType: ...
    
    @property
    def ExeProductVersion(self) -> StringType: ...
    
    @property
    def ExeRoamingConfigDirectory(self) -> StringType: ...
    
    @property
    def ExeRoamingConfigPath(self) -> StringType: ...
    
    @property
    def MachineConfigPath(self) -> StringType: ...
    
    @property
    def SetConfigurationSystemInProgress(self) -> BooleanType: ...
    
    @property
    def SupportsUserConfig(self) -> BooleanType: ...
    
    @property
    def UserConfigFilename(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_ApplicationConfigUri(self) -> StringType: ...
    
    def get_ExeLocalConfigDirectory(self) -> StringType: ...
    
    def get_ExeLocalConfigPath(self) -> StringType: ...
    
    def get_ExeProductName(self) -> StringType: ...
    
    def get_ExeProductVersion(self) -> StringType: ...
    
    def get_ExeRoamingConfigDirectory(self) -> StringType: ...
    
    def get_ExeRoamingConfigPath(self) -> StringType: ...
    
    def get_MachineConfigPath(self) -> StringType: ...
    
    def get_SetConfigurationSystemInProgress(self) -> BooleanType: ...
    
    def get_SupportsUserConfig(self) -> BooleanType: ...
    
    def get_UserConfigFilename(self) -> StringType: ...
    
    # No Events


class IInternalConfigClientHost(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetExeConfigPath(self) -> StringType: ...
    
    def GetLocalUserConfigPath(self) -> StringType: ...
    
    def GetRoamingUserConfigPath(self) -> StringType: ...
    
    def IsExeConfig(self, configPath: StringType) -> BooleanType: ...
    
    def IsLocalUserConfig(self, configPath: StringType) -> BooleanType: ...
    
    def IsRoamingUserConfig(self, configPath: StringType) -> BooleanType: ...
    
    # No Events


class IInternalConfigConfigurationFactory(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Create(self, typeConfigHost: TypeType, hostInitConfigurationParams: ArrayType[ObjectType]) -> Configuration: ...
    
    def NormalizeLocationSubPath(self, subPath: StringType, errorInfo: IConfigErrorInfo) -> StringType: ...
    
    # No Events


class IInternalConfigHost(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def IsRemote(self) -> BooleanType: ...
    
    @property
    def SupportsChangeNotifications(self) -> BooleanType: ...
    
    @property
    def SupportsLocation(self) -> BooleanType: ...
    
    @property
    def SupportsPath(self) -> BooleanType: ...
    
    @property
    def SupportsRefresh(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def CreateConfigurationContext(self, configPath: StringType, locationSubPath: StringType) -> ObjectType: ...
    
    def CreateDeprecatedConfigContext(self, configPath: StringType) -> ObjectType: ...
    
    def DecryptSection(self, encryptedXml: StringType, protectionProvider: ProtectedConfigurationProvider, protectedConfigSection: ProtectedConfigurationSection) -> StringType: ...
    
    def DeleteStream(self, streamName: StringType) -> VoidType: ...
    
    def EncryptSection(self, clearTextXml: StringType, protectionProvider: ProtectedConfigurationProvider, protectedConfigSection: ProtectedConfigurationSection) -> StringType: ...
    
    def GetConfigPathFromLocationSubPath(self, configPath: StringType, locationSubPath: StringType) -> StringType: ...
    
    def GetConfigType(self, typeName: StringType, throwOnError: BooleanType) -> TypeType: ...
    
    def GetConfigTypeName(self, t: TypeType) -> StringType: ...
    
    def GetRestrictedPermissions(self, configRecord: IInternalConfigRecord, permissionSet: PermissionSet, isHostReady: BooleanType) -> Tuple[VoidType, PermissionSet, BooleanType]: ...
    
    def GetStreamName(self, configPath: StringType) -> StringType: ...
    
    def GetStreamNameForConfigSource(self, streamName: StringType, configSource: StringType) -> StringType: ...
    
    def GetStreamVersion(self, streamName: StringType) -> ObjectType: ...
    
    def Impersonate(self) -> IDisposable: ...
    
    def Init(self, configRoot: IInternalConfigRoot, hostInitParams: ArrayType[ObjectType]) -> VoidType: ...
    
    def InitForConfiguration(self, locationSubPath: StringType, configPath: StringType, locationConfigPath: StringType, configRoot: IInternalConfigRoot, hostInitConfigurationParams: ArrayType[ObjectType]) -> Tuple[VoidType, StringType, StringType, StringType]: ...
    
    def IsAboveApplication(self, configPath: StringType) -> BooleanType: ...
    
    def IsConfigRecordRequired(self, configPath: StringType) -> BooleanType: ...
    
    def IsDefinitionAllowed(self, configPath: StringType, allowDefinition: ConfigurationAllowDefinition, allowExeDefinition: ConfigurationAllowExeDefinition) -> BooleanType: ...
    
    def IsFile(self, streamName: StringType) -> BooleanType: ...
    
    def IsFullTrustSectionWithoutAptcaAllowed(self, configRecord: IInternalConfigRecord) -> BooleanType: ...
    
    def IsInitDelayed(self, configRecord: IInternalConfigRecord) -> BooleanType: ...
    
    def IsLocationApplicable(self, configPath: StringType) -> BooleanType: ...
    
    def IsSecondaryRoot(self, configPath: StringType) -> BooleanType: ...
    
    def IsTrustedConfigPath(self, configPath: StringType) -> BooleanType: ...
    
    @overload
    def OpenStreamForRead(self, streamName: StringType) -> Stream: ...
    
    @overload
    def OpenStreamForRead(self, streamName: StringType, assertPermissions: BooleanType) -> Stream: ...
    
    @overload
    def OpenStreamForWrite(self, streamName: StringType, templateStreamName: StringType, writeContext: ObjectType) -> Tuple[Stream, ObjectType]: ...
    
    @overload
    def OpenStreamForWrite(self, streamName: StringType, templateStreamName: StringType, writeContext: ObjectType, assertPermissions: BooleanType) -> Tuple[Stream, ObjectType]: ...
    
    def PrefetchAll(self, configPath: StringType, streamName: StringType) -> BooleanType: ...
    
    def PrefetchSection(self, sectionGroupName: StringType, sectionName: StringType) -> BooleanType: ...
    
    def RequireCompleteInit(self, configRecord: IInternalConfigRecord) -> VoidType: ...
    
    def StartMonitoringStreamForChanges(self, streamName: StringType, callback: StreamChangeCallback) -> ObjectType: ...
    
    def StopMonitoringStreamForChanges(self, streamName: StringType, callback: StreamChangeCallback) -> VoidType: ...
    
    def VerifyDefinitionAllowed(self, configPath: StringType, allowDefinition: ConfigurationAllowDefinition, allowExeDefinition: ConfigurationAllowExeDefinition, errorInfo: IConfigErrorInfo) -> VoidType: ...
    
    @overload
    def WriteCompleted(self, streamName: StringType, success: BooleanType, writeContext: ObjectType) -> VoidType: ...
    
    @overload
    def WriteCompleted(self, streamName: StringType, success: BooleanType, writeContext: ObjectType, assertPermissions: BooleanType) -> VoidType: ...
    
    def get_IsRemote(self) -> BooleanType: ...
    
    def get_SupportsChangeNotifications(self) -> BooleanType: ...
    
    def get_SupportsLocation(self) -> BooleanType: ...
    
    def get_SupportsPath(self) -> BooleanType: ...
    
    def get_SupportsRefresh(self) -> BooleanType: ...
    
    # No Events


class IInternalConfigRecord(Protocol):
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


class IInternalConfigRoot(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def IsDesignTime(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def GetConfigRecord(self, configPath: StringType) -> IInternalConfigRecord: ...
    
    def GetSection(self, section: StringType, configPath: StringType) -> ObjectType: ...
    
    def GetUniqueConfigPath(self, configPath: StringType) -> StringType: ...
    
    def GetUniqueConfigRecord(self, configPath: StringType) -> IInternalConfigRecord: ...
    
    def Init(self, host: IInternalConfigHost, isDesignTime: BooleanType) -> VoidType: ...
    
    def RemoveConfig(self, configPath: StringType) -> VoidType: ...
    
    def add_ConfigChanged(self, value: InternalConfigEventHandler) -> VoidType: ...
    
    def add_ConfigRemoved(self, value: InternalConfigEventHandler) -> VoidType: ...
    
    def get_IsDesignTime(self) -> BooleanType: ...
    
    def remove_ConfigChanged(self, value: InternalConfigEventHandler) -> VoidType: ...
    
    def remove_ConfigRemoved(self, value: InternalConfigEventHandler) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    ConfigChanged: EventType[InternalConfigEventHandler] = ...
    
    ConfigRemoved: EventType[InternalConfigEventHandler] = ...


class IInternalConfigSettingsFactory(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CompleteInit(self) -> VoidType: ...
    
    def SetConfigurationSystem(self, internalConfigSystem: IInternalConfigSystem, initComplete: BooleanType) -> VoidType: ...
    
    # No Events


class IInternalConfigSystem(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def SupportsUserConfig(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def GetSection(self, configKey: StringType) -> ObjectType: ...
    
    def RefreshConfig(self, sectionName: StringType) -> VoidType: ...
    
    def get_SupportsUserConfig(self) -> BooleanType: ...
    
    # No Events


class IInternalConfigurationBuilderHost(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ProcessConfigurationSection(self, configSection: ConfigurationSection, builder: ConfigurationBuilder) -> ConfigurationSection: ...
    
    def ProcessRawXml(self, rawXml: XmlNode, builder: ConfigurationBuilder) -> XmlNode: ...
    
    # No Events


# No Enums

# ---------- Delegates ---------- #

InternalConfigEventHandler = Callable[[ObjectType, InternalConfigEventArgs], VoidType]

StreamChangeCallback = Callable[[StringType], VoidType]

__all__ = [
    ConfigSystem,
    ConfigurationManagerHelper,
    ConfigurationManagerInternal,
    DelegatingConfigHost,
    FileVersion,
    InternalConfigConfigurationFactory,
    InternalConfigEventArgs,
    InternalConfigEventHandler,
    InternalConfigHost,
    InternalConfigRoot,
    InternalConfigSettingsFactory,
    StreamChangeCallback,
    WriteFileContext,
    IConfigErrorInfo,
    IConfigSystem,
    IConfigurationManagerHelper,
    IConfigurationManagerInternal,
    IInternalConfigClientHost,
    IInternalConfigConfigurationFactory,
    IInternalConfigHost,
    IInternalConfigRecord,
    IInternalConfigRoot,
    IInternalConfigSettingsFactory,
    IInternalConfigSystem,
    IInternalConfigurationBuilderHost,
    InternalConfigEventHandler,
    StreamChangeCallback,
]
