from __future__ import annotations

from abc import ABC
from typing import Iterator
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
from System.Net.Configuration.ProxyElement import AutoDetectValues
from System.Net.Configuration.ProxyElement import BypassOnLocalValues
from System.Net.Configuration.ProxyElement import UseSystemDefaultValues
from System.Net.Mail import SmtpDeliveryFormat
from System.Net.Mail import SmtpDeliveryMethod
from System.Net.Security import EncryptionPolicy
from System.Net.Sockets import IPProtectionLevel

class AuthenticationModuleElement(ConfigurationElement):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, typeName: str):
        """

        :param typeName:
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
    def Type(self) -> str:
        """

        :return:
        """
    @Type.setter
    def Type(self, value: str) -> None: ...
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

class AuthenticationModuleElementCollection(
    ConfigurationElementCollection, ICollection, IEnumerable
):
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
    def Item(self) -> AuthenticationModuleElement:
        """

        :return:
        """
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
        """

        :return:
        """
    def Add(self, element: AuthenticationModuleElement) -> None:
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
    def IndexOf(self, element: AuthenticationModuleElement) -> int:
        """

        :param element:
        :return:
        """
    def IsReadOnly(self) -> bool:
        """"""
    @overload
    def Remove(self, element: AuthenticationModuleElement) -> None:
        """

        :param element:
        """
    @overload
    def Remove(self, name: str) -> None:
        """

        :param name:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
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
    def __getitem__(self, index: int) -> AuthenticationModuleElement:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, name: str) -> AuthenticationModuleElement:
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
    @overload
    def __setitem__(self, index: int, value: AuthenticationModuleElement) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, name: str, value: AuthenticationModuleElement) -> None:
        """

        :param name:
        :param value:
        """

class AuthenticationModulesSection(ConfigurationSection):
    """"""

    def __init__(self):
        """"""
    @property
    def AuthenticationModules(self) -> AuthenticationModuleElementCollection:
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

class AuthenticationModulesSectionInternal(Object):
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

class BypassElement(ConfigurationElement):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, address: str):
        """

        :param address:
        """
    @property
    def Address(self) -> str:
        """

        :return:
        """
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

class BypassElementCollection(ConfigurationElementCollection, ICollection, IEnumerable):
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
    def Item(self) -> BypassElement:
        """

        :return:
        """
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
        """

        :return:
        """
    def Add(self, element: BypassElement) -> None:
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
    def IndexOf(self, element: BypassElement) -> int:
        """

        :param element:
        :return:
        """
    def IsReadOnly(self) -> bool:
        """"""
    @overload
    def Remove(self, element: BypassElement) -> None:
        """

        :param element:
        """
    @overload
    def Remove(self, name: str) -> None:
        """

        :param name:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
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
    def __getitem__(self, index: int) -> BypassElement:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, name: str) -> BypassElement:
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
    @overload
    def __setitem__(self, index: int, value: BypassElement) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, name: str, value: BypassElement) -> None:
        """

        :param name:
        :param value:
        """

class ConfigurationStrings(ABC, Object):
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

class ConnectionManagementElement(ConfigurationElement):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, address: str, maxConnection: int):
        """

        :param address:
        :param maxConnection:
        """
    @property
    def Address(self) -> str:
        """

        :return:
        """
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
        """

        :return:
        """
    @MaxConnection.setter
    def MaxConnection(self, value: int) -> None: ...
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

class ConnectionManagementElementCollection(
    ConfigurationElementCollection, ICollection, IEnumerable
):
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
    def Item(self) -> ConnectionManagementElement:
        """

        :return:
        """
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
        """

        :return:
        """
    def Add(self, element: ConnectionManagementElement) -> None:
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
    def IndexOf(self, element: ConnectionManagementElement) -> int:
        """

        :param element:
        :return:
        """
    def IsReadOnly(self) -> bool:
        """"""
    @overload
    def Remove(self, element: ConnectionManagementElement) -> None:
        """

        :param element:
        """
    @overload
    def Remove(self, name: str) -> None:
        """

        :param name:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
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
    def __getitem__(self, index: int) -> ConnectionManagementElement:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, name: str) -> ConnectionManagementElement:
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
    @overload
    def __setitem__(self, index: int, value: ConnectionManagementElement) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, name: str, value: ConnectionManagementElement) -> None:
        """

        :param name:
        :param value:
        """

class ConnectionManagementSection(ConfigurationSection):
    """"""

    def __init__(self):
        """"""
    @property
    def ConnectionManagement(self) -> ConnectionManagementElementCollection:
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

class ConnectionManagementSectionInternal(Object):
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

class DefaultProxySection(ConfigurationSection):
    """"""

    def __init__(self):
        """"""
    @property
    def BypassList(self) -> BypassElementCollection:
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
    @property
    def Module(self) -> ModuleElement:
        """

        :return:
        """
    @property
    def Proxy(self) -> ProxyElement:
        """

        :return:
        """
    @property
    def SectionInformation(self) -> SectionInformation:
        """"""
    @property
    def UseDefaultCredentials(self) -> bool:
        """

        :return:
        """
    @UseDefaultCredentials.setter
    def UseDefaultCredentials(self, value: bool) -> None: ...
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

class DefaultProxySectionInternal(Object):
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

class FtpCachePolicyElement(ConfigurationElement):
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
    def PolicyLevel(self) -> RequestCacheLevel:
        """

        :return:
        """
    @PolicyLevel.setter
    def PolicyLevel(self, value: RequestCacheLevel) -> None: ...
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

class HttpCachePolicyElement(ConfigurationElement):
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
    def MaximumAge(self) -> TimeSpan:
        """

        :return:
        """
    @MaximumAge.setter
    def MaximumAge(self, value: TimeSpan) -> None: ...
    @property
    def MaximumStale(self) -> TimeSpan:
        """

        :return:
        """
    @MaximumStale.setter
    def MaximumStale(self, value: TimeSpan) -> None: ...
    @property
    def MinimumFresh(self) -> TimeSpan:
        """

        :return:
        """
    @MinimumFresh.setter
    def MinimumFresh(self, value: TimeSpan) -> None: ...
    @property
    def PolicyLevel(self) -> HttpRequestCacheLevel:
        """

        :return:
        """
    @PolicyLevel.setter
    def PolicyLevel(self, value: HttpRequestCacheLevel) -> None: ...
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

class HttpListenerElement(ConfigurationElement):
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
    def Timeouts(self) -> HttpListenerTimeoutsElement:
        """

        :return:
        """
    @property
    def UnescapeRequestUrl(self) -> bool:
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

class HttpListenerTimeoutsElement(ConfigurationElement):
    """"""

    def __init__(self):
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def DrainEntityBody(self) -> TimeSpan:
        """

        :return:
        """
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def EntityBody(self) -> TimeSpan:
        """

        :return:
        """
    @property
    def HeaderWait(self) -> TimeSpan:
        """

        :return:
        """
    @property
    def IdleConnection(self) -> TimeSpan:
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
    def MinSendBytesPerSecond(self) -> int:
        """

        :return:
        """
    @property
    def RequestQueue(self) -> TimeSpan:
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

class HttpWebRequestElement(ConfigurationElement):
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
    def MaximumErrorResponseLength(self) -> int:
        """

        :return:
        """
    @MaximumErrorResponseLength.setter
    def MaximumErrorResponseLength(self, value: int) -> None: ...
    @property
    def MaximumResponseHeadersLength(self) -> int:
        """

        :return:
        """
    @MaximumResponseHeadersLength.setter
    def MaximumResponseHeadersLength(self, value: int) -> None: ...
    @property
    def MaximumUnauthorizedUploadLength(self) -> int:
        """

        :return:
        """
    @MaximumUnauthorizedUploadLength.setter
    def MaximumUnauthorizedUploadLength(self, value: int) -> None: ...
    @property
    def UseUnsafeHeaderParsing(self) -> bool:
        """

        :return:
        """
    @UseUnsafeHeaderParsing.setter
    def UseUnsafeHeaderParsing(self, value: bool) -> None: ...
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

class Ipv6Element(ConfigurationElement):
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

class MailSettingsSectionGroup(ConfigurationSectionGroup):
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
    def Smtp(self) -> SmtpSection:
        """

        :return:
        """
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

class MailSettingsSectionGroupInternal(Object):
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

class ModuleElement(ConfigurationElement):
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
    def Type(self) -> str:
        """

        :return:
        """
    @Type.setter
    def Type(self, value: str) -> None: ...
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

class NetSectionGroup(ConfigurationSectionGroup):
    """"""

    def __init__(self):
        """"""
    @property
    def AuthenticationModules(self) -> AuthenticationModulesSection:
        """

        :return:
        """
    @property
    def ConnectionManagement(self) -> ConnectionManagementSection:
        """

        :return:
        """
    @property
    def DefaultProxy(self) -> DefaultProxySection:
        """

        :return:
        """
    @property
    def IsDeclarationRequired(self) -> bool:
        """"""
    @property
    def IsDeclared(self) -> bool:
        """"""
    @property
    def MailSettings(self) -> MailSettingsSectionGroup:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """"""
    @property
    def RequestCaching(self) -> RequestCachingSection:
        """

        :return:
        """
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
        """

        :return:
        """
    @property
    def Type(self) -> str:
        """"""
    @Type.setter
    def Type(self, value: str) -> None: ...
    @property
    def WebRequestModules(self) -> WebRequestModulesSection:
        """

        :return:
        """
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
    @classmethod
    def GetSectionGroup(cls, config: Configuration) -> NetSectionGroup:
        """

        :param config:
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

class PerformanceCountersElement(ConfigurationElement):
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

class ProxyElement(ConfigurationElement):
    """"""

    def __init__(self):
        """"""
    @property
    def AutoDetect(self) -> ProxyElement.AutoDetectValues:
        """

        :return:
        """
    @AutoDetect.setter
    def AutoDetect(self, value: ProxyElement.AutoDetectValues) -> None: ...
    @property
    def BypassOnLocal(self) -> ProxyElement.BypassOnLocalValues:
        """

        :return:
        """
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
        """

        :return:
        """
    @ProxyAddress.setter
    def ProxyAddress(self, value: Uri) -> None: ...
    @property
    def ScriptLocation(self) -> Uri:
        """

        :return:
        """
    @ScriptLocation.setter
    def ScriptLocation(self, value: Uri) -> None: ...
    @property
    def UseSystemDefault(self) -> ProxyElement.UseSystemDefaultValues:
        """

        :return:
        """
    @UseSystemDefault.setter
    def UseSystemDefault(self, value: ProxyElement.UseSystemDefaultValues) -> None: ...
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

    class AutoDetectValues(Enum):
        """"""

        _False: AutoDetectValues = ...
        """"""
        _True: AutoDetectValues = ...
        """"""
        Unspecified: AutoDetectValues = ...
        """"""

    class BypassOnLocalValues(Enum):
        """"""

        _False: BypassOnLocalValues = ...
        """"""
        _True: BypassOnLocalValues = ...
        """"""
        Unspecified: BypassOnLocalValues = ...
        """"""

    class UseSystemDefaultValues(Enum):
        """"""

        _False: UseSystemDefaultValues = ...
        """"""
        _True: UseSystemDefaultValues = ...
        """"""
        Unspecified: UseSystemDefaultValues = ...
        """"""

class RequestCachingSection(ConfigurationSection):
    """"""

    def __init__(self):
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def DefaultFtpCachePolicy(self) -> FtpCachePolicyElement:
        """

        :return:
        """
    @property
    def DefaultHttpCachePolicy(self) -> HttpCachePolicyElement:
        """

        :return:
        """
    @property
    def DefaultPolicyLevel(self) -> RequestCacheLevel:
        """

        :return:
        """
    @DefaultPolicyLevel.setter
    def DefaultPolicyLevel(self, value: RequestCacheLevel) -> None: ...
    @property
    def DisableAllCaching(self) -> bool:
        """

        :return:
        """
    @DisableAllCaching.setter
    def DisableAllCaching(self, value: bool) -> None: ...
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def IsPrivateCache(self) -> bool:
        """

        :return:
        """
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
        """

        :return:
        """
    @UnspecifiedMaximumAge.setter
    def UnspecifiedMaximumAge(self, value: TimeSpan) -> None: ...
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

class RequestCachingSectionInternal(Object):
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

class ServicePointManagerElement(ConfigurationElement):
    """"""

    def __init__(self):
        """"""
    @property
    def CheckCertificateName(self) -> bool:
        """

        :return:
        """
    @CheckCertificateName.setter
    def CheckCertificateName(self, value: bool) -> None: ...
    @property
    def CheckCertificateRevocationList(self) -> bool:
        """

        :return:
        """
    @CheckCertificateRevocationList.setter
    def CheckCertificateRevocationList(self, value: bool) -> None: ...
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def DnsRefreshTimeout(self) -> int:
        """

        :return:
        """
    @DnsRefreshTimeout.setter
    def DnsRefreshTimeout(self, value: int) -> None: ...
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def EnableDnsRoundRobin(self) -> bool:
        """

        :return:
        """
    @EnableDnsRoundRobin.setter
    def EnableDnsRoundRobin(self, value: bool) -> None: ...
    @property
    def EncryptionPolicy(self) -> EncryptionPolicy:
        """

        :return:
        """
    @EncryptionPolicy.setter
    def EncryptionPolicy(self, value: EncryptionPolicy) -> None: ...
    @property
    def Expect100Continue(self) -> bool:
        """

        :return:
        """
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
        """

        :return:
        """
    @UseNagleAlgorithm.setter
    def UseNagleAlgorithm(self, value: bool) -> None: ...
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

class SettingsSection(ConfigurationSection):
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
    def HttpListener(self) -> HttpListenerElement:
        """

        :return:
        """
    @property
    def HttpWebRequest(self) -> HttpWebRequestElement:
        """

        :return:
        """
    @property
    def Ipv6(self) -> Ipv6Element:
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
    def PerformanceCounters(self) -> PerformanceCountersElement:
        """

        :return:
        """
    @property
    def SectionInformation(self) -> SectionInformation:
        """"""
    @property
    def ServicePointManager(self) -> ServicePointManagerElement:
        """

        :return:
        """
    @property
    def Socket(self) -> SocketElement:
        """

        :return:
        """
    @property
    def WebProxyScript(self) -> WebProxyScriptElement:
        """

        :return:
        """
    @property
    def WebUtility(self) -> WebUtilityElement:
        """

        :return:
        """
    @property
    def WindowsAuthentication(self) -> WindowsAuthenticationElement:
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

class SettingsSectionInternal(Object):
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

class SmtpNetworkElement(ConfigurationElement):
    """"""

    def __init__(self):
        """"""
    @property
    def ClientDomain(self) -> str:
        """

        :return:
        """
    @ClientDomain.setter
    def ClientDomain(self, value: str) -> None: ...
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def DefaultCredentials(self) -> bool:
        """

        :return:
        """
    @DefaultCredentials.setter
    def DefaultCredentials(self, value: bool) -> None: ...
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def EnableSsl(self) -> bool:
        """

        :return:
        """
    @EnableSsl.setter
    def EnableSsl(self, value: bool) -> None: ...
    @property
    def Host(self) -> str:
        """

        :return:
        """
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
        """

        :return:
        """
    @Password.setter
    def Password(self, value: str) -> None: ...
    @property
    def Port(self) -> int:
        """

        :return:
        """
    @Port.setter
    def Port(self, value: int) -> None: ...
    @property
    def TargetName(self) -> str:
        """

        :return:
        """
    @TargetName.setter
    def TargetName(self, value: str) -> None: ...
    @property
    def UserName(self) -> str:
        """

        :return:
        """
    @UserName.setter
    def UserName(self, value: str) -> None: ...
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

class SmtpNetworkElementInternal(Object):
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

class SmtpSection(ConfigurationSection):
    """"""

    def __init__(self):
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def DeliveryFormat(self) -> SmtpDeliveryFormat:
        """

        :return:
        """
    @DeliveryFormat.setter
    def DeliveryFormat(self, value: SmtpDeliveryFormat) -> None: ...
    @property
    def DeliveryMethod(self) -> SmtpDeliveryMethod:
        """

        :return:
        """
    @DeliveryMethod.setter
    def DeliveryMethod(self, value: SmtpDeliveryMethod) -> None: ...
    @property
    def ElementInformation(self) -> ElementInformation:
        """"""
    @property
    def From(self) -> str:
        """

        :return:
        """
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
        """

        :return:
        """
    @property
    def SectionInformation(self) -> SectionInformation:
        """"""
    @property
    def SpecifiedPickupDirectory(self) -> SmtpSpecifiedPickupDirectoryElement:
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

class SmtpSectionInternal(Object):
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

class SmtpSpecifiedPickupDirectoryElement(ConfigurationElement):
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
    def PickupDirectoryLocation(self) -> str:
        """

        :return:
        """
    @PickupDirectoryLocation.setter
    def PickupDirectoryLocation(self, value: str) -> None: ...
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

class SmtpSpecifiedPickupDirectoryElementInternal(Object):
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

class SocketElement(ConfigurationElement):
    """"""

    def __init__(self):
        """"""
    @property
    def AlwaysUseCompletionPortsForAccept(self) -> bool:
        """

        :return:
        """
    @AlwaysUseCompletionPortsForAccept.setter
    def AlwaysUseCompletionPortsForAccept(self, value: bool) -> None: ...
    @property
    def AlwaysUseCompletionPortsForConnect(self) -> bool:
        """

        :return:
        """
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
        """

        :return:
        """
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

    def __init__(self):
        """"""
    @property
    def AutoConfigUrlRetryInterval(self) -> int:
        """

        :return:
        """
    @AutoConfigUrlRetryInterval.setter
    def AutoConfigUrlRetryInterval(self, value: int) -> None: ...
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def DownloadTimeout(self) -> TimeSpan:
        """

        :return:
        """
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

class WebRequestModuleElement(ConfigurationElement):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, prefix: str, type: str):
        """

        :param prefix:
        :param type:
        """
    @overload
    def __init__(self, prefix: str, type: Type):
        """

        :param prefix:
        :param type:
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
    def Prefix(self) -> str:
        """

        :return:
        """
    @Prefix.setter
    def Prefix(self, value: str) -> None: ...
    @property
    def Type(self) -> Type:
        """

        :return:
        """
    @Type.setter
    def Type(self, value: Type) -> None: ...
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

class WebRequestModuleElementCollection(ConfigurationElementCollection, ICollection, IEnumerable):
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
    def Item(self) -> WebRequestModuleElement:
        """

        :return:
        """
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
        """

        :return:
        """
    def Add(self, element: WebRequestModuleElement) -> None:
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
    def IndexOf(self, element: WebRequestModuleElement) -> int:
        """

        :param element:
        :return:
        """
    def IsReadOnly(self) -> bool:
        """"""
    @overload
    def Remove(self, element: WebRequestModuleElement) -> None:
        """

        :param element:
        """
    @overload
    def Remove(self, name: str) -> None:
        """

        :param name:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
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
    def __getitem__(self, index: int) -> WebRequestModuleElement:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, name: str) -> WebRequestModuleElement:
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
    @overload
    def __setitem__(self, index: int, value: WebRequestModuleElement) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, name: str, value: WebRequestModuleElement) -> None:
        """

        :param name:
        :param value:
        """

class WebRequestModulesSection(ConfigurationSection):
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
    def WebRequestModules(self) -> WebRequestModuleElementCollection:
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

class WebRequestModulesSectionInternal(Object):
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

class WebUtilityElement(ConfigurationElement):
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
    def UnicodeDecodingConformance(self) -> UnicodeDecodingConformance:
        """

        :return:
        """
    @UnicodeDecodingConformance.setter
    def UnicodeDecodingConformance(self, value: UnicodeDecodingConformance) -> None: ...
    @property
    def UnicodeEncodingConformance(self) -> UnicodeEncodingConformance:
        """

        :return:
        """
    @UnicodeEncodingConformance.setter
    def UnicodeEncodingConformance(self, value: UnicodeEncodingConformance) -> None: ...
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

class WindowsAuthenticationElement(ConfigurationElement):
    """"""

    def __init__(self):
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def DefaultCredentialsHandleCacheSize(self) -> int:
        """

        :return:
        """
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
