from __future__ import annotations

from abc import ABC
from typing import Iterator
from typing import overload

from System import Array
from System import Object
from System import Type
from System.Collections import ICollection
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Configuration import Configuration
from System.Configuration import ConfigurationElement
from System.Configuration import ConfigurationElementCollection
from System.Configuration import ConfigurationElementCollectionType
from System.Configuration import ConfigurationLockCollection
from System.Configuration import ElementInformation
from System.Security.Authentication.ExtendedProtection import ExtendedProtectionPolicy
from System.Security.Authentication.ExtendedProtection import PolicyEnforcement
from System.Security.Authentication.ExtendedProtection import ProtectionScenario

class ExtendedProtectionConfigurationStrings(ABC, Object):
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

class ExtendedProtectionPolicyElement(ConfigurationElement):
    """"""

    def __init__(self):
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def CustomServiceNames(self) -> ServiceNameElementCollection:
        """

        :return:
        """
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
    def PolicyEnforcement(self) -> PolicyEnforcement:
        """

        :return:
        """
    @PolicyEnforcement.setter
    def PolicyEnforcement(self, value: PolicyEnforcement) -> None: ...
    @property
    def ProtectionScenario(self) -> ProtectionScenario:
        """

        :return:
        """
    @ProtectionScenario.setter
    def ProtectionScenario(self, value: ProtectionScenario) -> None: ...
    def BuildPolicy(self) -> ExtendedProtectionPolicy:
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

class ServiceNameElement(ConfigurationElement):
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
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
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

class ServiceNameElementCollection(ConfigurationElementCollection, ICollection, IEnumerable):
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
    def Item(self) -> ServiceNameElement:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: ServiceNameElement) -> None: ...
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
    def Add(self, element: ServiceNameElement) -> None:
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
    def IndexOf(self, element: ServiceNameElement) -> int:
        """

        :param element:
        :return:
        """
    def IsReadOnly(self) -> bool:
        """"""
    @overload
    def Remove(self, element: ServiceNameElement) -> None:
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
    def __getitem__(self, index: int) -> ServiceNameElement:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, name: str) -> ServiceNameElement:
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
    def __setitem__(self, index: int, value: ServiceNameElement) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, name: str, value: ServiceNameElement) -> None:
        """

        :param name:
        :param value:
        """
