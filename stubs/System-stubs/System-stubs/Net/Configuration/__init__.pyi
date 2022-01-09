from __future__ import annotations

from abc import ABC
from typing import Union, overload

from System import Boolean, Enum, Int32, Int64, Object, String, TimeSpan, Type, Uri, Void
from System.Collections import ICollection, IEnumerable
from System.Configuration import Configuration, ConfigurationElement, ConfigurationElementCollection, ConfigurationSection, ConfigurationSectionGroup
from System.Net.Cache import HttpRequestCacheLevel, RequestCacheLevel
from System.Net.Mail import SmtpDeliveryFormat, SmtpDeliveryMethod
from System.Net.Security import EncryptionPolicy
from System.Net.Sockets import IPProtectionLevel

# ---------- Types ---------- #

BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class AuthenticationModuleElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, typeName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Type(self) -> StringType: ...
    
    @Type.setter
    def Type(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Type(self) -> StringType: ...
    
    def set_Type(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AuthenticationModuleElementCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> AuthenticationModuleElement: ...
    
    @Item.setter
    def Item(self, value: AuthenticationModuleElement) -> None: ...
    
    @property
    def Item(self) -> AuthenticationModuleElement: ...
    
    @Item.setter
    def Item(self, value: AuthenticationModuleElement) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, element: AuthenticationModuleElement) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def IndexOf(self, element: AuthenticationModuleElement) -> IntType: ...
    
    @overload
    def Remove(self, element: AuthenticationModuleElement) -> VoidType: ...
    
    @overload
    def Remove(self, name: StringType) -> VoidType: ...
    
    def RemoveAt(self, index: IntType) -> VoidType: ...
    
    @overload
    def get_Item(self, index: IntType) -> AuthenticationModuleElement: ...
    
    @overload
    def get_Item(self, name: StringType) -> AuthenticationModuleElement: ...
    
    @overload
    def set_Item(self, index: IntType, value: AuthenticationModuleElement) -> VoidType: ...
    
    @overload
    def set_Item(self, name: StringType, value: AuthenticationModuleElement) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AuthenticationModulesSection(ConfigurationSection):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AuthenticationModules(self) -> AuthenticationModuleElementCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_AuthenticationModules(self) -> AuthenticationModuleElementCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AuthenticationModulesSectionInternal(ObjectType):
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


class BypassElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, address: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Address(self) -> StringType: ...
    
    @Address.setter
    def Address(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Address(self) -> StringType: ...
    
    def set_Address(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BypassElementCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> BypassElement: ...
    
    @Item.setter
    def Item(self, value: BypassElement) -> None: ...
    
    @property
    def Item(self) -> BypassElement: ...
    
    @Item.setter
    def Item(self, value: BypassElement) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, element: BypassElement) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def IndexOf(self, element: BypassElement) -> IntType: ...
    
    @overload
    def Remove(self, element: BypassElement) -> VoidType: ...
    
    @overload
    def Remove(self, name: StringType) -> VoidType: ...
    
    def RemoveAt(self, index: IntType) -> VoidType: ...
    
    @overload
    def get_Item(self, index: IntType) -> BypassElement: ...
    
    @overload
    def get_Item(self, name: StringType) -> BypassElement: ...
    
    @overload
    def set_Item(self, index: IntType, value: BypassElement) -> VoidType: ...
    
    @overload
    def set_Item(self, name: StringType, value: BypassElement) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConfigurationStrings(ABC, ObjectType):
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


class ConnectionManagementElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, address: StringType, maxConnection: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Address(self) -> StringType: ...
    
    @Address.setter
    def Address(self, value: StringType) -> None: ...
    
    @property
    def MaxConnection(self) -> IntType: ...
    
    @MaxConnection.setter
    def MaxConnection(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Address(self) -> StringType: ...
    
    def get_MaxConnection(self) -> IntType: ...
    
    def set_Address(self, value: StringType) -> VoidType: ...
    
    def set_MaxConnection(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConnectionManagementElementCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> ConnectionManagementElement: ...
    
    @Item.setter
    def Item(self, value: ConnectionManagementElement) -> None: ...
    
    @property
    def Item(self) -> ConnectionManagementElement: ...
    
    @Item.setter
    def Item(self, value: ConnectionManagementElement) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, element: ConnectionManagementElement) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def IndexOf(self, element: ConnectionManagementElement) -> IntType: ...
    
    @overload
    def Remove(self, element: ConnectionManagementElement) -> VoidType: ...
    
    @overload
    def Remove(self, name: StringType) -> VoidType: ...
    
    def RemoveAt(self, index: IntType) -> VoidType: ...
    
    @overload
    def get_Item(self, index: IntType) -> ConnectionManagementElement: ...
    
    @overload
    def get_Item(self, name: StringType) -> ConnectionManagementElement: ...
    
    @overload
    def set_Item(self, index: IntType, value: ConnectionManagementElement) -> VoidType: ...
    
    @overload
    def set_Item(self, name: StringType, value: ConnectionManagementElement) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConnectionManagementSection(ConfigurationSection):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ConnectionManagement(self) -> ConnectionManagementElementCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_ConnectionManagement(self) -> ConnectionManagementElementCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConnectionManagementSectionInternal(ObjectType):
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


class DefaultProxySection(ConfigurationSection):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BypassList(self) -> BypassElementCollection: ...
    
    @property
    def Enabled(self) -> BooleanType: ...
    
    @Enabled.setter
    def Enabled(self, value: BooleanType) -> None: ...
    
    @property
    def Module(self) -> ModuleElement: ...
    
    @property
    def Proxy(self) -> ProxyElement: ...
    
    @property
    def UseDefaultCredentials(self) -> BooleanType: ...
    
    @UseDefaultCredentials.setter
    def UseDefaultCredentials(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_BypassList(self) -> BypassElementCollection: ...
    
    def get_Enabled(self) -> BooleanType: ...
    
    def get_Module(self) -> ModuleElement: ...
    
    def get_Proxy(self) -> ProxyElement: ...
    
    def get_UseDefaultCredentials(self) -> BooleanType: ...
    
    def set_Enabled(self, value: BooleanType) -> VoidType: ...
    
    def set_UseDefaultCredentials(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DefaultProxySectionInternal(ObjectType):
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


class FtpCachePolicyElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def PolicyLevel(self) -> RequestCacheLevel: ...
    
    @PolicyLevel.setter
    def PolicyLevel(self, value: RequestCacheLevel) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_PolicyLevel(self) -> RequestCacheLevel: ...
    
    def set_PolicyLevel(self, value: RequestCacheLevel) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HttpCachePolicyElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def MaximumAge(self) -> TimeSpan: ...
    
    @MaximumAge.setter
    def MaximumAge(self, value: TimeSpan) -> None: ...
    
    @property
    def MaximumStale(self) -> TimeSpan: ...
    
    @MaximumStale.setter
    def MaximumStale(self, value: TimeSpan) -> None: ...
    
    @property
    def MinimumFresh(self) -> TimeSpan: ...
    
    @MinimumFresh.setter
    def MinimumFresh(self, value: TimeSpan) -> None: ...
    
    @property
    def PolicyLevel(self) -> HttpRequestCacheLevel: ...
    
    @PolicyLevel.setter
    def PolicyLevel(self, value: HttpRequestCacheLevel) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_MaximumAge(self) -> TimeSpan: ...
    
    def get_MaximumStale(self) -> TimeSpan: ...
    
    def get_MinimumFresh(self) -> TimeSpan: ...
    
    def get_PolicyLevel(self) -> HttpRequestCacheLevel: ...
    
    def set_MaximumAge(self, value: TimeSpan) -> VoidType: ...
    
    def set_MaximumStale(self, value: TimeSpan) -> VoidType: ...
    
    def set_MinimumFresh(self, value: TimeSpan) -> VoidType: ...
    
    def set_PolicyLevel(self, value: HttpRequestCacheLevel) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HttpListenerElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Timeouts(self) -> HttpListenerTimeoutsElement: ...
    
    @property
    def UnescapeRequestUrl(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_Timeouts(self) -> HttpListenerTimeoutsElement: ...
    
    def get_UnescapeRequestUrl(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HttpListenerTimeoutsElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DrainEntityBody(self) -> TimeSpan: ...
    
    @property
    def EntityBody(self) -> TimeSpan: ...
    
    @property
    def HeaderWait(self) -> TimeSpan: ...
    
    @property
    def IdleConnection(self) -> TimeSpan: ...
    
    @property
    def MinSendBytesPerSecond(self) -> LongType: ...
    
    @property
    def RequestQueue(self) -> TimeSpan: ...
    
    # ---------- Methods ---------- #
    
    def get_DrainEntityBody(self) -> TimeSpan: ...
    
    def get_EntityBody(self) -> TimeSpan: ...
    
    def get_HeaderWait(self) -> TimeSpan: ...
    
    def get_IdleConnection(self) -> TimeSpan: ...
    
    def get_MinSendBytesPerSecond(self) -> LongType: ...
    
    def get_RequestQueue(self) -> TimeSpan: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HttpWebRequestElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def MaximumErrorResponseLength(self) -> IntType: ...
    
    @MaximumErrorResponseLength.setter
    def MaximumErrorResponseLength(self, value: IntType) -> None: ...
    
    @property
    def MaximumResponseHeadersLength(self) -> IntType: ...
    
    @MaximumResponseHeadersLength.setter
    def MaximumResponseHeadersLength(self, value: IntType) -> None: ...
    
    @property
    def MaximumUnauthorizedUploadLength(self) -> IntType: ...
    
    @MaximumUnauthorizedUploadLength.setter
    def MaximumUnauthorizedUploadLength(self, value: IntType) -> None: ...
    
    @property
    def UseUnsafeHeaderParsing(self) -> BooleanType: ...
    
    @UseUnsafeHeaderParsing.setter
    def UseUnsafeHeaderParsing(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_MaximumErrorResponseLength(self) -> IntType: ...
    
    def get_MaximumResponseHeadersLength(self) -> IntType: ...
    
    def get_MaximumUnauthorizedUploadLength(self) -> IntType: ...
    
    def get_UseUnsafeHeaderParsing(self) -> BooleanType: ...
    
    def set_MaximumErrorResponseLength(self, value: IntType) -> VoidType: ...
    
    def set_MaximumResponseHeadersLength(self, value: IntType) -> VoidType: ...
    
    def set_MaximumUnauthorizedUploadLength(self, value: IntType) -> VoidType: ...
    
    def set_UseUnsafeHeaderParsing(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Ipv6Element(ConfigurationElement):
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


class MailSettingsSectionGroup(ConfigurationSectionGroup):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Smtp(self) -> SmtpSection: ...
    
    # ---------- Methods ---------- #
    
    def get_Smtp(self) -> SmtpSection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MailSettingsSectionGroupInternal(ObjectType):
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


class ModuleElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Type(self) -> StringType: ...
    
    @Type.setter
    def Type(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Type(self) -> StringType: ...
    
    def set_Type(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NetSectionGroup(ConfigurationSectionGroup):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AuthenticationModules(self) -> AuthenticationModulesSection: ...
    
    @property
    def ConnectionManagement(self) -> ConnectionManagementSection: ...
    
    @property
    def DefaultProxy(self) -> DefaultProxySection: ...
    
    @property
    def MailSettings(self) -> MailSettingsSectionGroup: ...
    
    @property
    def RequestCaching(self) -> RequestCachingSection: ...
    
    @property
    def Settings(self) -> SettingsSection: ...
    
    @property
    def WebRequestModules(self) -> WebRequestModulesSection: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetSectionGroup(config: Configuration) -> NetSectionGroup: ...
    
    def get_AuthenticationModules(self) -> AuthenticationModulesSection: ...
    
    def get_ConnectionManagement(self) -> ConnectionManagementSection: ...
    
    def get_DefaultProxy(self) -> DefaultProxySection: ...
    
    def get_MailSettings(self) -> MailSettingsSectionGroup: ...
    
    def get_RequestCaching(self) -> RequestCachingSection: ...
    
    def get_Settings(self) -> SettingsSection: ...
    
    def get_WebRequestModules(self) -> WebRequestModulesSection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PerformanceCountersElement(ConfigurationElement):
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


class ProxyElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AutoDetect(self) -> AutoDetectValues: ...
    
    @AutoDetect.setter
    def AutoDetect(self, value: AutoDetectValues) -> None: ...
    
    @property
    def BypassOnLocal(self) -> BypassOnLocalValues: ...
    
    @BypassOnLocal.setter
    def BypassOnLocal(self, value: BypassOnLocalValues) -> None: ...
    
    @property
    def ProxyAddress(self) -> Uri: ...
    
    @ProxyAddress.setter
    def ProxyAddress(self, value: Uri) -> None: ...
    
    @property
    def ScriptLocation(self) -> Uri: ...
    
    @ScriptLocation.setter
    def ScriptLocation(self, value: Uri) -> None: ...
    
    @property
    def UseSystemDefault(self) -> UseSystemDefaultValues: ...
    
    @UseSystemDefault.setter
    def UseSystemDefault(self, value: UseSystemDefaultValues) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_AutoDetect(self) -> AutoDetectValues: ...
    
    def get_BypassOnLocal(self) -> BypassOnLocalValues: ...
    
    def get_ProxyAddress(self) -> Uri: ...
    
    def get_ScriptLocation(self) -> Uri: ...
    
    def get_UseSystemDefault(self) -> UseSystemDefaultValues: ...
    
    def set_AutoDetect(self, value: AutoDetectValues) -> VoidType: ...
    
    def set_BypassOnLocal(self, value: BypassOnLocalValues) -> VoidType: ...
    
    def set_ProxyAddress(self, value: Uri) -> VoidType: ...
    
    def set_ScriptLocation(self, value: Uri) -> VoidType: ...
    
    def set_UseSystemDefault(self, value: UseSystemDefaultValues) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class BypassOnLocalValues(Enum):
        Unspecified: IntType = -1
        False: IntType = 0
        True: IntType = 1
    
    
    class UseSystemDefaultValues(Enum):
        Unspecified: IntType = -1
        False: IntType = 0
        True: IntType = 1
    
    
    class AutoDetectValues(Enum):
        Unspecified: IntType = -1
        False: IntType = 0
        True: IntType = 1
    


class RequestCachingSection(ConfigurationSection):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DefaultFtpCachePolicy(self) -> FtpCachePolicyElement: ...
    
    @property
    def DefaultHttpCachePolicy(self) -> HttpCachePolicyElement: ...
    
    @property
    def DefaultPolicyLevel(self) -> RequestCacheLevel: ...
    
    @DefaultPolicyLevel.setter
    def DefaultPolicyLevel(self, value: RequestCacheLevel) -> None: ...
    
    @property
    def DisableAllCaching(self) -> BooleanType: ...
    
    @DisableAllCaching.setter
    def DisableAllCaching(self, value: BooleanType) -> None: ...
    
    @property
    def IsPrivateCache(self) -> BooleanType: ...
    
    @IsPrivateCache.setter
    def IsPrivateCache(self, value: BooleanType) -> None: ...
    
    @property
    def UnspecifiedMaximumAge(self) -> TimeSpan: ...
    
    @UnspecifiedMaximumAge.setter
    def UnspecifiedMaximumAge(self, value: TimeSpan) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_DefaultFtpCachePolicy(self) -> FtpCachePolicyElement: ...
    
    def get_DefaultHttpCachePolicy(self) -> HttpCachePolicyElement: ...
    
    def get_DefaultPolicyLevel(self) -> RequestCacheLevel: ...
    
    def get_DisableAllCaching(self) -> BooleanType: ...
    
    def get_IsPrivateCache(self) -> BooleanType: ...
    
    def get_UnspecifiedMaximumAge(self) -> TimeSpan: ...
    
    def set_DefaultPolicyLevel(self, value: RequestCacheLevel) -> VoidType: ...
    
    def set_DisableAllCaching(self, value: BooleanType) -> VoidType: ...
    
    def set_IsPrivateCache(self, value: BooleanType) -> VoidType: ...
    
    def set_UnspecifiedMaximumAge(self, value: TimeSpan) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RequestCachingSectionInternal(ObjectType):
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


class ServicePointManagerElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CheckCertificateName(self) -> BooleanType: ...
    
    @CheckCertificateName.setter
    def CheckCertificateName(self, value: BooleanType) -> None: ...
    
    @property
    def CheckCertificateRevocationList(self) -> BooleanType: ...
    
    @CheckCertificateRevocationList.setter
    def CheckCertificateRevocationList(self, value: BooleanType) -> None: ...
    
    @property
    def DnsRefreshTimeout(self) -> IntType: ...
    
    @DnsRefreshTimeout.setter
    def DnsRefreshTimeout(self, value: IntType) -> None: ...
    
    @property
    def EnableDnsRoundRobin(self) -> BooleanType: ...
    
    @EnableDnsRoundRobin.setter
    def EnableDnsRoundRobin(self, value: BooleanType) -> None: ...
    
    @property
    def EncryptionPolicy(self) -> EncryptionPolicy: ...
    
    @EncryptionPolicy.setter
    def EncryptionPolicy(self, value: EncryptionPolicy) -> None: ...
    
    @property
    def Expect100Continue(self) -> BooleanType: ...
    
    @Expect100Continue.setter
    def Expect100Continue(self, value: BooleanType) -> None: ...
    
    @property
    def UseNagleAlgorithm(self) -> BooleanType: ...
    
    @UseNagleAlgorithm.setter
    def UseNagleAlgorithm(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_CheckCertificateName(self) -> BooleanType: ...
    
    def get_CheckCertificateRevocationList(self) -> BooleanType: ...
    
    def get_DnsRefreshTimeout(self) -> IntType: ...
    
    def get_EnableDnsRoundRobin(self) -> BooleanType: ...
    
    def get_EncryptionPolicy(self) -> EncryptionPolicy: ...
    
    def get_Expect100Continue(self) -> BooleanType: ...
    
    def get_UseNagleAlgorithm(self) -> BooleanType: ...
    
    def set_CheckCertificateName(self, value: BooleanType) -> VoidType: ...
    
    def set_CheckCertificateRevocationList(self, value: BooleanType) -> VoidType: ...
    
    def set_DnsRefreshTimeout(self, value: IntType) -> VoidType: ...
    
    def set_EnableDnsRoundRobin(self, value: BooleanType) -> VoidType: ...
    
    def set_EncryptionPolicy(self, value: EncryptionPolicy) -> VoidType: ...
    
    def set_Expect100Continue(self, value: BooleanType) -> VoidType: ...
    
    def set_UseNagleAlgorithm(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SettingsSection(ConfigurationSection):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def HttpListener(self) -> HttpListenerElement: ...
    
    @property
    def HttpWebRequest(self) -> HttpWebRequestElement: ...
    
    @property
    def Ipv6(self) -> Ipv6Element: ...
    
    @property
    def PerformanceCounters(self) -> PerformanceCountersElement: ...
    
    @property
    def ServicePointManager(self) -> ServicePointManagerElement: ...
    
    @property
    def Socket(self) -> SocketElement: ...
    
    @property
    def WebProxyScript(self) -> WebProxyScriptElement: ...
    
    @property
    def WebUtility(self) -> WebUtilityElement: ...
    
    @property
    def WindowsAuthentication(self) -> WindowsAuthenticationElement: ...
    
    # ---------- Methods ---------- #
    
    def get_HttpListener(self) -> HttpListenerElement: ...
    
    def get_HttpWebRequest(self) -> HttpWebRequestElement: ...
    
    def get_Ipv6(self) -> Ipv6Element: ...
    
    def get_PerformanceCounters(self) -> PerformanceCountersElement: ...
    
    def get_ServicePointManager(self) -> ServicePointManagerElement: ...
    
    def get_Socket(self) -> SocketElement: ...
    
    def get_WebProxyScript(self) -> WebProxyScriptElement: ...
    
    def get_WebUtility(self) -> WebUtilityElement: ...
    
    def get_WindowsAuthentication(self) -> WindowsAuthenticationElement: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SettingsSectionInternal(ObjectType):
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


class SmtpNetworkElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ClientDomain(self) -> StringType: ...
    
    @ClientDomain.setter
    def ClientDomain(self, value: StringType) -> None: ...
    
    @property
    def DefaultCredentials(self) -> BooleanType: ...
    
    @DefaultCredentials.setter
    def DefaultCredentials(self, value: BooleanType) -> None: ...
    
    @property
    def EnableSsl(self) -> BooleanType: ...
    
    @EnableSsl.setter
    def EnableSsl(self, value: BooleanType) -> None: ...
    
    @property
    def Host(self) -> StringType: ...
    
    @Host.setter
    def Host(self, value: StringType) -> None: ...
    
    @property
    def Password(self) -> StringType: ...
    
    @Password.setter
    def Password(self, value: StringType) -> None: ...
    
    @property
    def Port(self) -> IntType: ...
    
    @Port.setter
    def Port(self, value: IntType) -> None: ...
    
    @property
    def TargetName(self) -> StringType: ...
    
    @TargetName.setter
    def TargetName(self, value: StringType) -> None: ...
    
    @property
    def UserName(self) -> StringType: ...
    
    @UserName.setter
    def UserName(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_ClientDomain(self) -> StringType: ...
    
    def get_DefaultCredentials(self) -> BooleanType: ...
    
    def get_EnableSsl(self) -> BooleanType: ...
    
    def get_Host(self) -> StringType: ...
    
    def get_Password(self) -> StringType: ...
    
    def get_Port(self) -> IntType: ...
    
    def get_TargetName(self) -> StringType: ...
    
    def get_UserName(self) -> StringType: ...
    
    def set_ClientDomain(self, value: StringType) -> VoidType: ...
    
    def set_DefaultCredentials(self, value: BooleanType) -> VoidType: ...
    
    def set_EnableSsl(self, value: BooleanType) -> VoidType: ...
    
    def set_Host(self, value: StringType) -> VoidType: ...
    
    def set_Password(self, value: StringType) -> VoidType: ...
    
    def set_Port(self, value: IntType) -> VoidType: ...
    
    def set_TargetName(self, value: StringType) -> VoidType: ...
    
    def set_UserName(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SmtpNetworkElementInternal(ObjectType):
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


class SmtpSection(ConfigurationSection):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DeliveryFormat(self) -> SmtpDeliveryFormat: ...
    
    @DeliveryFormat.setter
    def DeliveryFormat(self, value: SmtpDeliveryFormat) -> None: ...
    
    @property
    def DeliveryMethod(self) -> SmtpDeliveryMethod: ...
    
    @DeliveryMethod.setter
    def DeliveryMethod(self, value: SmtpDeliveryMethod) -> None: ...
    
    @property
    def From(self) -> StringType: ...
    
    @From.setter
    def From(self, value: StringType) -> None: ...
    
    @property
    def Network(self) -> SmtpNetworkElement: ...
    
    @property
    def SpecifiedPickupDirectory(self) -> SmtpSpecifiedPickupDirectoryElement: ...
    
    # ---------- Methods ---------- #
    
    def get_DeliveryFormat(self) -> SmtpDeliveryFormat: ...
    
    def get_DeliveryMethod(self) -> SmtpDeliveryMethod: ...
    
    def get_From(self) -> StringType: ...
    
    def get_Network(self) -> SmtpNetworkElement: ...
    
    def get_SpecifiedPickupDirectory(self) -> SmtpSpecifiedPickupDirectoryElement: ...
    
    def set_DeliveryFormat(self, value: SmtpDeliveryFormat) -> VoidType: ...
    
    def set_DeliveryMethod(self, value: SmtpDeliveryMethod) -> VoidType: ...
    
    def set_From(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SmtpSectionInternal(ObjectType):
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


class SmtpSpecifiedPickupDirectoryElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def PickupDirectoryLocation(self) -> StringType: ...
    
    @PickupDirectoryLocation.setter
    def PickupDirectoryLocation(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_PickupDirectoryLocation(self) -> StringType: ...
    
    def set_PickupDirectoryLocation(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SmtpSpecifiedPickupDirectoryElementInternal(ObjectType):
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


class SocketElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AlwaysUseCompletionPortsForAccept(self) -> BooleanType: ...
    
    @AlwaysUseCompletionPortsForAccept.setter
    def AlwaysUseCompletionPortsForAccept(self, value: BooleanType) -> None: ...
    
    @property
    def AlwaysUseCompletionPortsForConnect(self) -> BooleanType: ...
    
    @AlwaysUseCompletionPortsForConnect.setter
    def AlwaysUseCompletionPortsForConnect(self, value: BooleanType) -> None: ...
    
    @property
    def IPProtectionLevel(self) -> IPProtectionLevel: ...
    
    @IPProtectionLevel.setter
    def IPProtectionLevel(self, value: IPProtectionLevel) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_AlwaysUseCompletionPortsForAccept(self) -> BooleanType: ...
    
    def get_AlwaysUseCompletionPortsForConnect(self) -> BooleanType: ...
    
    def get_IPProtectionLevel(self) -> IPProtectionLevel: ...
    
    def set_AlwaysUseCompletionPortsForAccept(self, value: BooleanType) -> VoidType: ...
    
    def set_AlwaysUseCompletionPortsForConnect(self, value: BooleanType) -> VoidType: ...
    
    def set_IPProtectionLevel(self, value: IPProtectionLevel) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebProxyScriptElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AutoConfigUrlRetryInterval(self) -> IntType: ...
    
    @AutoConfigUrlRetryInterval.setter
    def AutoConfigUrlRetryInterval(self, value: IntType) -> None: ...
    
    @property
    def DownloadTimeout(self) -> TimeSpan: ...
    
    @DownloadTimeout.setter
    def DownloadTimeout(self, value: TimeSpan) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_AutoConfigUrlRetryInterval(self) -> IntType: ...
    
    def get_DownloadTimeout(self) -> TimeSpan: ...
    
    def set_AutoConfigUrlRetryInterval(self, value: IntType) -> VoidType: ...
    
    def set_DownloadTimeout(self, value: TimeSpan) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebRequestModuleElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, prefix: StringType, type: StringType): ...
    
    @overload
    def __init__(self, prefix: StringType, type: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Prefix(self) -> StringType: ...
    
    @Prefix.setter
    def Prefix(self, value: StringType) -> None: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    @Type.setter
    def Type(self, value: TypeType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Prefix(self) -> StringType: ...
    
    def get_Type(self) -> TypeType: ...
    
    def set_Prefix(self, value: StringType) -> VoidType: ...
    
    def set_Type(self, value: TypeType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebRequestModuleElementCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> WebRequestModuleElement: ...
    
    @Item.setter
    def Item(self, value: WebRequestModuleElement) -> None: ...
    
    @property
    def Item(self) -> WebRequestModuleElement: ...
    
    @Item.setter
    def Item(self, value: WebRequestModuleElement) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, element: WebRequestModuleElement) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def IndexOf(self, element: WebRequestModuleElement) -> IntType: ...
    
    @overload
    def Remove(self, element: WebRequestModuleElement) -> VoidType: ...
    
    @overload
    def Remove(self, name: StringType) -> VoidType: ...
    
    def RemoveAt(self, index: IntType) -> VoidType: ...
    
    @overload
    def get_Item(self, index: IntType) -> WebRequestModuleElement: ...
    
    @overload
    def get_Item(self, name: StringType) -> WebRequestModuleElement: ...
    
    @overload
    def set_Item(self, index: IntType, value: WebRequestModuleElement) -> VoidType: ...
    
    @overload
    def set_Item(self, name: StringType, value: WebRequestModuleElement) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebRequestModulesSection(ConfigurationSection):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def WebRequestModules(self) -> WebRequestModuleElementCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_WebRequestModules(self) -> WebRequestModuleElementCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebRequestModulesSectionInternal(ObjectType):
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


class WebUtilityElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def UnicodeDecodingConformance(self) -> UnicodeDecodingConformance: ...
    
    @UnicodeDecodingConformance.setter
    def UnicodeDecodingConformance(self, value: UnicodeDecodingConformance) -> None: ...
    
    @property
    def UnicodeEncodingConformance(self) -> UnicodeEncodingConformance: ...
    
    @UnicodeEncodingConformance.setter
    def UnicodeEncodingConformance(self, value: UnicodeEncodingConformance) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_UnicodeDecodingConformance(self) -> UnicodeDecodingConformance: ...
    
    def get_UnicodeEncodingConformance(self) -> UnicodeEncodingConformance: ...
    
    def set_UnicodeDecodingConformance(self, value: UnicodeDecodingConformance) -> VoidType: ...
    
    def set_UnicodeEncodingConformance(self, value: UnicodeEncodingConformance) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WindowsAuthenticationElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DefaultCredentialsHandleCacheSize(self) -> IntType: ...
    
    @DefaultCredentialsHandleCacheSize.setter
    def DefaultCredentialsHandleCacheSize(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_DefaultCredentialsHandleCacheSize(self) -> IntType: ...
    
    def set_DefaultCredentialsHandleCacheSize(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# No Interfaces

# ---------- Enums ---------- #

class UnicodeDecodingConformance(Enum):
    Auto: IntType = 0
    Strict: IntType = 1
    Compat: IntType = 2
    Loose: IntType = 3


class UnicodeEncodingConformance(Enum):
    Auto: IntType = 0
    Strict: IntType = 1
    Compat: IntType = 2


# No Delegates

__all__ = [
    AuthenticationModuleElement,
    AuthenticationModuleElementCollection,
    AuthenticationModulesSection,
    AuthenticationModulesSectionInternal,
    BypassElement,
    BypassElementCollection,
    ConfigurationStrings,
    ConnectionManagementElement,
    ConnectionManagementElementCollection,
    ConnectionManagementSection,
    ConnectionManagementSectionInternal,
    DefaultProxySection,
    DefaultProxySectionInternal,
    FtpCachePolicyElement,
    HttpCachePolicyElement,
    HttpListenerElement,
    HttpListenerTimeoutsElement,
    HttpWebRequestElement,
    Ipv6Element,
    MailSettingsSectionGroup,
    MailSettingsSectionGroupInternal,
    ModuleElement,
    NetSectionGroup,
    PerformanceCountersElement,
    ProxyElement,
    RequestCachingSection,
    RequestCachingSectionInternal,
    ServicePointManagerElement,
    SettingsSection,
    SettingsSectionInternal,
    SmtpNetworkElement,
    SmtpNetworkElementInternal,
    SmtpSection,
    SmtpSectionInternal,
    SmtpSpecifiedPickupDirectoryElement,
    SmtpSpecifiedPickupDirectoryElementInternal,
    SocketElement,
    WebProxyScriptElement,
    WebRequestModuleElement,
    WebRequestModuleElementCollection,
    WebRequestModulesSection,
    WebRequestModulesSectionInternal,
    WebUtilityElement,
    WindowsAuthenticationElement,
    UnicodeDecodingConformance,
    UnicodeEncodingConformance,
]
