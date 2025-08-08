"""Automatically generated stubs for C# namespace: System.Net.Configuration."""

from abc import ABC
from collections.abc import Iterator
from typing import overload

from System import Array
from System import Enum
from System import Object
from System import TimeSpan
from System import Type
from System import Uri
from System.Collections import ICollection
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Configuration import Configuration
from System.Configuration import ConfigurationElement
from System.Configuration import ConfigurationElementCollection
from System.Configuration import ConfigurationElementCollectionType
from System.Configuration import ConfigurationLockCollection
from System.Configuration import ConfigurationSection
from System.Configuration import ConfigurationSectionCollection
from System.Configuration import ConfigurationSectionGroup
from System.Configuration import ConfigurationSectionGroupCollection
from System.Configuration import ElementInformation
from System.Configuration import SectionInformation
from System.Net.Cache import HttpRequestCacheLevel
from System.Net.Cache import RequestCacheLevel
from System.Net.Mail import SmtpDeliveryFormat
from System.Net.Mail import SmtpDeliveryMethod
from System.Net.Security import EncryptionPolicy
from System.Net.Sockets import IPProtectionLevel

class AuthenticationModuleElement(ConfigurationElement):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, typeName: str) -> None:
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
    def Type(self) -> str:
        """"""
    @Type.setter
    def Type(self, value: str) -> None: ...
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

class AuthenticationModuleElementCollection(
    ConfigurationElementCollection, ICollection, IEnumerable
):
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
    def Item(self) -> AuthenticationModuleElement:
        """"""
    @Item.setter
    def Item(self, value: AuthenticationModuleElement) -> None: ...
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
    def Add(self, element: AuthenticationModuleElement) -> None:
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
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IndexOf(self, element: AuthenticationModuleElement) -> int:
        """"""
    def IsReadOnly(self) -> bool:
        """"""
    @overload
    def Remove(self, element: AuthenticationModuleElement) -> None:
        """"""
    @overload
    def Remove(self, name: str) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, element: AuthenticationModuleElement) -> None:
        """"""
    @overload
    def __delitem__(self, name: str) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    @overload
    def __getitem__(self, index: int) -> AuthenticationModuleElement:
        """"""
    @overload
    def __getitem__(self, name: str) -> AuthenticationModuleElement:
        """"""
    @overload
    def __setitem__(self, index: int, value: AuthenticationModuleElement) -> None:
        """"""
    @overload
    def __setitem__(self, name: str, value: AuthenticationModuleElement) -> None:
        """"""

class AuthenticationModulesSection(ConfigurationSection):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AuthenticationModules(self) -> AuthenticationModuleElementCollection:
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

class AuthenticationModulesSectionInternal(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class BypassElement(ConfigurationElement):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, address: str) -> None:
        """"""
    @property
    def Address(self) -> str:
        """"""
    @Address.setter
    def Address(self, value: str) -> None: ...
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

class BypassElementCollection(ConfigurationElementCollection, ICollection, IEnumerable):
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
    def Item(self) -> BypassElement:
        """"""
    @Item.setter
    def Item(self, value: BypassElement) -> None: ...
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
    def Add(self, element: BypassElement) -> None:
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
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IndexOf(self, element: BypassElement) -> int:
        """"""
    def IsReadOnly(self) -> bool:
        """"""
    @overload
    def Remove(self, element: BypassElement) -> None:
        """"""
    @overload
    def Remove(self, name: str) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, element: BypassElement) -> None:
        """"""
    @overload
    def __delitem__(self, name: str) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    @overload
    def __getitem__(self, index: int) -> BypassElement:
        """"""
    @overload
    def __getitem__(self, name: str) -> BypassElement:
        """"""
    @overload
    def __setitem__(self, index: int, value: BypassElement) -> None:
        """"""
    @overload
    def __setitem__(self, name: str, value: BypassElement) -> None:
        """"""

class ConfigurationStrings(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ConnectionManagementElement(ConfigurationElement):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, address: str, maxConnection: int) -> None:
        """"""
    @property
    def Address(self) -> str:
        """"""
    @Address.setter
    def Address(self, value: str) -> None: ...
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
    def MaxConnection(self) -> int:
        """"""
    @MaxConnection.setter
    def MaxConnection(self, value: int) -> None: ...
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

class ConnectionManagementElementCollection(
    ConfigurationElementCollection, ICollection, IEnumerable
):
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
    def Item(self) -> ConnectionManagementElement:
        """"""
    @Item.setter
    def Item(self, value: ConnectionManagementElement) -> None: ...
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
    def Add(self, element: ConnectionManagementElement) -> None:
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
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IndexOf(self, element: ConnectionManagementElement) -> int:
        """"""
    def IsReadOnly(self) -> bool:
        """"""
    @overload
    def Remove(self, element: ConnectionManagementElement) -> None:
        """"""
    @overload
    def Remove(self, name: str) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, element: ConnectionManagementElement) -> None:
        """"""
    @overload
    def __delitem__(self, name: str) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    @overload
    def __getitem__(self, index: int) -> ConnectionManagementElement:
        """"""
    @overload
    def __getitem__(self, name: str) -> ConnectionManagementElement:
        """"""
    @overload
    def __setitem__(self, index: int, value: ConnectionManagementElement) -> None:
        """"""
    @overload
    def __setitem__(self, name: str, value: ConnectionManagementElement) -> None:
        """"""

class ConnectionManagementSection(ConfigurationSection):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def ConnectionManagement(self) -> ConnectionManagementElementCollection:
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

class ConnectionManagementSectionInternal(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DefaultProxySection(ConfigurationSection):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def BypassList(self) -> BypassElementCollection:
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
    @property
    def Module(self) -> ModuleElement:
        """"""
    @property
    def Proxy(self) -> ProxyElement:
        """"""
    @property
    def SectionInformation(self) -> SectionInformation:
        """"""
    @property
    def UseDefaultCredentials(self) -> bool:
        """"""
    @UseDefaultCredentials.setter
    def UseDefaultCredentials(self, value: bool) -> None: ...
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

class DefaultProxySectionInternal(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class FtpCachePolicyElement(ConfigurationElement):
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
    def PolicyLevel(self) -> RequestCacheLevel:
        """"""
    @PolicyLevel.setter
    def PolicyLevel(self, value: RequestCacheLevel) -> None: ...
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

class HttpCachePolicyElement(ConfigurationElement):
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
    def MaximumAge(self) -> TimeSpan:
        """"""
    @MaximumAge.setter
    def MaximumAge(self, value: TimeSpan) -> None: ...
    @property
    def MaximumStale(self) -> TimeSpan:
        """"""
    @MaximumStale.setter
    def MaximumStale(self, value: TimeSpan) -> None: ...
    @property
    def MinimumFresh(self) -> TimeSpan:
        """"""
    @MinimumFresh.setter
    def MinimumFresh(self, value: TimeSpan) -> None: ...
    @property
    def PolicyLevel(self) -> HttpRequestCacheLevel:
        """"""
    @PolicyLevel.setter
    def PolicyLevel(self, value: HttpRequestCacheLevel) -> None: ...
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

class HttpListenerElement(ConfigurationElement):
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
    def Timeouts(self) -> HttpListenerTimeoutsElement:
        """"""
    @property
    def UnescapeRequestUrl(self) -> bool:
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

class HttpListenerTimeoutsElement(ConfigurationElement):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def DrainEntityBody(self) -> TimeSpan:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def EntityBody(self) -> TimeSpan:
        """"""
    @property
    def HeaderWait(self) -> TimeSpan:
        """"""
    @property
    def IdleConnection(self) -> TimeSpan:
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
    def MinSendBytesPerSecond(self) -> int:
        """"""
    @property
    def RequestQueue(self) -> TimeSpan:
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

class HttpWebRequestElement(ConfigurationElement):
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
    def MaximumErrorResponseLength(self) -> int:
        """"""
    @MaximumErrorResponseLength.setter
    def MaximumErrorResponseLength(self, value: int) -> None: ...
    @property
    def MaximumResponseHeadersLength(self) -> int:
        """"""
    @MaximumResponseHeadersLength.setter
    def MaximumResponseHeadersLength(self, value: int) -> None: ...
    @property
    def MaximumUnauthorizedUploadLength(self) -> int:
        """"""
    @MaximumUnauthorizedUploadLength.setter
    def MaximumUnauthorizedUploadLength(self, value: int) -> None: ...
    @property
    def UseUnsafeHeaderParsing(self) -> bool:
        """"""
    @UseUnsafeHeaderParsing.setter
    def UseUnsafeHeaderParsing(self, value: bool) -> None: ...
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

class Ipv6Element(ConfigurationElement):
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

class MailSettingsSectionGroup(ConfigurationSectionGroup):
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
    def Smtp(self) -> SmtpSection:
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

class MailSettingsSectionGroupInternal(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ModuleElement(ConfigurationElement):
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
    def Type(self) -> str:
        """"""
    @Type.setter
    def Type(self, value: str) -> None: ...
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

class NetSectionGroup(ConfigurationSectionGroup):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AuthenticationModules(self) -> AuthenticationModulesSection:
        """"""
    @property
    def ConnectionManagement(self) -> ConnectionManagementSection:
        """"""
    @property
    def DefaultProxy(self) -> DefaultProxySection:
        """"""
    @property
    def IsDeclarationRequired(self) -> bool:
        """"""
    @property
    def IsDeclared(self) -> bool:
        """"""
    @property
    def MailSettings(self) -> MailSettingsSectionGroup:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def RequestCaching(self) -> RequestCachingSection:
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
    def Settings(self) -> SettingsSection:
        """"""
    @property
    def Type(self) -> str:
        """"""
    @Type.setter
    def Type(self, value: str) -> None: ...
    @property
    def WebRequestModules(self) -> WebRequestModulesSection:
        """"""
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
    @classmethod
    def GetSectionGroup(cls, config: Configuration) -> NetSectionGroup:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class PerformanceCountersElement(ConfigurationElement):
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

class ProxyElement(ConfigurationElement):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AutoDetect(self) -> ProxyElement.AutoDetectValues:
        """"""
    @AutoDetect.setter
    def AutoDetect(self, value: ProxyElement.AutoDetectValues) -> None: ...
    @property
    def BypassOnLocal(self) -> ProxyElement.BypassOnLocalValues:
        """"""
    @BypassOnLocal.setter
    def BypassOnLocal(self, value: ProxyElement.BypassOnLocalValues) -> None: ...
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
    def ProxyAddress(self) -> Uri:
        """"""
    @ProxyAddress.setter
    def ProxyAddress(self, value: Uri) -> None: ...
    @property
    def ScriptLocation(self) -> Uri:
        """"""
    @ScriptLocation.setter
    def ScriptLocation(self, value: Uri) -> None: ...
    @property
    def UseSystemDefault(self) -> ProxyElement.UseSystemDefaultValues:
        """"""
    @UseSystemDefault.setter
    def UseSystemDefault(self, value: ProxyElement.UseSystemDefaultValues) -> None: ...
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
    class AutoDetectValues(Enum):
        """"""

        _False: ProxyElement.AutoDetectValues = ...
        """"""
        _True: ProxyElement.AutoDetectValues = ...
        """"""
        Unspecified: ProxyElement.AutoDetectValues = ...
        """"""

    class BypassOnLocalValues(Enum):
        """"""

        _False: ProxyElement.BypassOnLocalValues = ...
        """"""
        _True: ProxyElement.BypassOnLocalValues = ...
        """"""
        Unspecified: ProxyElement.BypassOnLocalValues = ...
        """"""

    class UseSystemDefaultValues(Enum):
        """"""

        _False: ProxyElement.UseSystemDefaultValues = ...
        """"""
        _True: ProxyElement.UseSystemDefaultValues = ...
        """"""
        Unspecified: ProxyElement.UseSystemDefaultValues = ...
        """"""

class RequestCachingSection(ConfigurationSection):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def DefaultFtpCachePolicy(self) -> FtpCachePolicyElement:
        """"""
    @property
    def DefaultHttpCachePolicy(self) -> HttpCachePolicyElement:
        """"""
    @property
    def DefaultPolicyLevel(self) -> RequestCacheLevel:
        """"""
    @DefaultPolicyLevel.setter
    def DefaultPolicyLevel(self, value: RequestCacheLevel) -> None: ...
    @property
    def DisableAllCaching(self) -> bool:
        """"""
    @DisableAllCaching.setter
    def DisableAllCaching(self, value: bool) -> None: ...
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def IsPrivateCache(self) -> bool:
        """"""
    @IsPrivateCache.setter
    def IsPrivateCache(self, value: bool) -> None: ...
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
    def UnspecifiedMaximumAge(self) -> TimeSpan:
        """"""
    @UnspecifiedMaximumAge.setter
    def UnspecifiedMaximumAge(self, value: TimeSpan) -> None: ...
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

class RequestCachingSectionInternal(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ServicePointManagerElement(ConfigurationElement):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CheckCertificateName(self) -> bool:
        """"""
    @CheckCertificateName.setter
    def CheckCertificateName(self, value: bool) -> None: ...
    @property
    def CheckCertificateRevocationList(self) -> bool:
        """"""
    @CheckCertificateRevocationList.setter
    def CheckCertificateRevocationList(self, value: bool) -> None: ...
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def DnsRefreshTimeout(self) -> int:
        """"""
    @DnsRefreshTimeout.setter
    def DnsRefreshTimeout(self, value: int) -> None: ...
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def EnableDnsRoundRobin(self) -> bool:
        """"""
    @EnableDnsRoundRobin.setter
    def EnableDnsRoundRobin(self, value: bool) -> None: ...
    @property
    def EncryptionPolicy(self) -> EncryptionPolicy:
        """"""
    @EncryptionPolicy.setter
    def EncryptionPolicy(self, value: EncryptionPolicy) -> None: ...
    @property
    def Expect100Continue(self) -> bool:
        """"""
    @Expect100Continue.setter
    def Expect100Continue(self, value: bool) -> None: ...
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
    def UseNagleAlgorithm(self) -> bool:
        """"""
    @UseNagleAlgorithm.setter
    def UseNagleAlgorithm(self, value: bool) -> None: ...
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

class SettingsSection(ConfigurationSection):
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
    def HttpListener(self) -> HttpListenerElement:
        """"""
    @property
    def HttpWebRequest(self) -> HttpWebRequestElement:
        """"""
    @property
    def Ipv6(self) -> Ipv6Element:
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
    def PerformanceCounters(self) -> PerformanceCountersElement:
        """"""
    @property
    def SectionInformation(self) -> SectionInformation:
        """"""
    @property
    def ServicePointManager(self) -> ServicePointManagerElement:
        """"""
    @property
    def Socket(self) -> SocketElement:
        """"""
    @property
    def WebProxyScript(self) -> WebProxyScriptElement:
        """"""
    @property
    def WebUtility(self) -> WebUtilityElement:
        """"""
    @property
    def WindowsAuthentication(self) -> WindowsAuthenticationElement:
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

class SettingsSectionInternal(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SmtpNetworkElement(ConfigurationElement):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def ClientDomain(self) -> str:
        """"""
    @ClientDomain.setter
    def ClientDomain(self, value: str) -> None: ...
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def DefaultCredentials(self) -> bool:
        """"""
    @DefaultCredentials.setter
    def DefaultCredentials(self, value: bool) -> None: ...
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def EnableSsl(self) -> bool:
        """"""
    @EnableSsl.setter
    def EnableSsl(self, value: bool) -> None: ...
    @property
    def Host(self) -> str:
        """"""
    @Host.setter
    def Host(self, value: str) -> None: ...
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
    def Password(self) -> str:
        """"""
    @Password.setter
    def Password(self, value: str) -> None: ...
    @property
    def Port(self) -> int:
        """"""
    @Port.setter
    def Port(self, value: int) -> None: ...
    @property
    def TargetName(self) -> str:
        """"""
    @TargetName.setter
    def TargetName(self, value: str) -> None: ...
    @property
    def UserName(self) -> str:
        """"""
    @UserName.setter
    def UserName(self, value: str) -> None: ...
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

class SmtpNetworkElementInternal(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SmtpSection(ConfigurationSection):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def DeliveryFormat(self) -> SmtpDeliveryFormat:
        """"""
    @DeliveryFormat.setter
    def DeliveryFormat(self, value: SmtpDeliveryFormat) -> None: ...
    @property
    def DeliveryMethod(self) -> SmtpDeliveryMethod:
        """"""
    @DeliveryMethod.setter
    def DeliveryMethod(self, value: SmtpDeliveryMethod) -> None: ...
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def From(self) -> str:
        """"""
    @From.setter
    def From(self, value: str) -> None: ...
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
    def Network(self) -> SmtpNetworkElement:
        """"""
    @property
    def SectionInformation(self) -> SectionInformation:
        """"""
    @property
    def SpecifiedPickupDirectory(self) -> SmtpSpecifiedPickupDirectoryElement:
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

class SmtpSectionInternal(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SmtpSpecifiedPickupDirectoryElement(ConfigurationElement):
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
    def PickupDirectoryLocation(self) -> str:
        """"""
    @PickupDirectoryLocation.setter
    def PickupDirectoryLocation(self, value: str) -> None: ...
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

class SmtpSpecifiedPickupDirectoryElementInternal(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SocketElement(ConfigurationElement):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AlwaysUseCompletionPortsForAccept(self) -> bool:
        """"""
    @AlwaysUseCompletionPortsForAccept.setter
    def AlwaysUseCompletionPortsForAccept(self, value: bool) -> None: ...
    @property
    def AlwaysUseCompletionPortsForConnect(self) -> bool:
        """"""
    @AlwaysUseCompletionPortsForConnect.setter
    def AlwaysUseCompletionPortsForConnect(self, value: bool) -> None: ...
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def IPProtectionLevel(self) -> IPProtectionLevel:
        """"""
    @IPProtectionLevel.setter
    def IPProtectionLevel(self, value: IPProtectionLevel) -> None: ...
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

class UnicodeDecodingConformance(Enum):
    """"""

    Auto: UnicodeDecodingConformance = ...
    """"""
    Strict: UnicodeDecodingConformance = ...
    """"""
    Compat: UnicodeDecodingConformance = ...
    """"""
    Loose: UnicodeDecodingConformance = ...
    """"""

class UnicodeEncodingConformance(Enum):
    """"""

    Auto: UnicodeEncodingConformance = ...
    """"""
    Strict: UnicodeEncodingConformance = ...
    """"""
    Compat: UnicodeEncodingConformance = ...
    """"""

class WebProxyScriptElement(ConfigurationElement):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AutoConfigUrlRetryInterval(self) -> int:
        """"""
    @AutoConfigUrlRetryInterval.setter
    def AutoConfigUrlRetryInterval(self, value: int) -> None: ...
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def DownloadTimeout(self) -> TimeSpan:
        """"""
    @DownloadTimeout.setter
    def DownloadTimeout(self, value: TimeSpan) -> None: ...
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

class WebRequestModuleElement(ConfigurationElement):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, prefix: str, type: str) -> None:
        """"""
    @overload
    def __init__(self, prefix: str, type: Type) -> None:
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
    def Prefix(self) -> str:
        """"""
    @Prefix.setter
    def Prefix(self, value: str) -> None: ...
    @property
    def Type(self) -> Type:
        """"""
    @Type.setter
    def Type(self, value: Type) -> None: ...
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

class WebRequestModuleElementCollection(ConfigurationElementCollection, ICollection, IEnumerable):
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
    def Item(self) -> WebRequestModuleElement:
        """"""
    @Item.setter
    def Item(self, value: WebRequestModuleElement) -> None: ...
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
    def Add(self, element: WebRequestModuleElement) -> None:
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
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IndexOf(self, element: WebRequestModuleElement) -> int:
        """"""
    def IsReadOnly(self) -> bool:
        """"""
    @overload
    def Remove(self, element: WebRequestModuleElement) -> None:
        """"""
    @overload
    def Remove(self, name: str) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, element: WebRequestModuleElement) -> None:
        """"""
    @overload
    def __delitem__(self, name: str) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    @overload
    def __getitem__(self, index: int) -> WebRequestModuleElement:
        """"""
    @overload
    def __getitem__(self, name: str) -> WebRequestModuleElement:
        """"""
    @overload
    def __setitem__(self, index: int, value: WebRequestModuleElement) -> None:
        """"""
    @overload
    def __setitem__(self, name: str, value: WebRequestModuleElement) -> None:
        """"""

class WebRequestModulesSection(ConfigurationSection):
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
    def WebRequestModules(self) -> WebRequestModuleElementCollection:
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

class WebRequestModulesSectionInternal(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class WebUtilityElement(ConfigurationElement):
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
    def UnicodeDecodingConformance(self) -> UnicodeDecodingConformance:
        """"""
    @UnicodeDecodingConformance.setter
    def UnicodeDecodingConformance(self, value: UnicodeDecodingConformance) -> None: ...
    @property
    def UnicodeEncodingConformance(self) -> UnicodeEncodingConformance:
        """"""
    @UnicodeEncodingConformance.setter
    def UnicodeEncodingConformance(self, value: UnicodeEncodingConformance) -> None: ...
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

class WindowsAuthenticationElement(ConfigurationElement):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def DefaultCredentialsHandleCacheSize(self) -> int:
        """"""
    @DefaultCredentialsHandleCacheSize.setter
    def DefaultCredentialsHandleCacheSize(self, value: int) -> None: ...
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
