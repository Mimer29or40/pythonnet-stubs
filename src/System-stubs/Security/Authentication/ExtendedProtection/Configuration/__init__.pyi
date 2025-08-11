"""Automatically generated stubs for C# namespace: System.Security.Authentication.ExtendedProtection.Configuration."""

from abc import ABC
from collections.abc import Iterator
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ExtendedProtectionConfigurationStrings(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ExtendedProtectionPolicyElement(ConfigurationElement):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CurrentConfiguration(self) -> Configuration:
        """"""
    @property
    def CustomServiceNames(self) -> ServiceNameElementCollection:
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
    def PolicyEnforcement(self) -> PolicyEnforcement:
        """"""
    @PolicyEnforcement.setter
    def PolicyEnforcement(self, value: PolicyEnforcement) -> None: ...
    @property
    def ProtectionScenario(self) -> ProtectionScenario:
        """"""
    @ProtectionScenario.setter
    def ProtectionScenario(self, value: ProtectionScenario) -> None: ...
    def BuildPolicy(self) -> ExtendedProtectionPolicy:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ServiceNameElement(ConfigurationElement):
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
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ServiceNameElementCollection(ConfigurationElementCollection, ICollection, IEnumerable):
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
    def Item(self) -> ServiceNameElement:
        """"""
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
        """"""
    def Add(self, element: ServiceNameElement) -> None:
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
    def IndexOf(self, element: ServiceNameElement) -> int:
        """"""
    def IsReadOnly(self) -> bool:
        """"""
    @overload
    def Remove(self, element: ServiceNameElement) -> None:
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
    def __delitem__(self, element: ServiceNameElement) -> None:
        """"""
    @overload
    def __delitem__(self, name: str) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    @overload
    def __getitem__(self, index: int) -> ServiceNameElement:
        """"""
    @overload
    def __getitem__(self, name: str) -> ServiceNameElement:
        """"""
    @overload
    def __setitem__(self, index: int, value: ServiceNameElement) -> None:
        """"""
    @overload
    def __setitem__(self, name: str, value: ServiceNameElement) -> None:
        """"""
