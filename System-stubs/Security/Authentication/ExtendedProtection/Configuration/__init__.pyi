from __future__ import annotations

from abc import ABC
from typing import Union, overload

from System import Int32, Object, String, Void
from System.Collections import ICollection, IEnumerable
from System.Configuration import ConfigurationElement, ConfigurationElementCollection
from System.Security.Authentication.ExtendedProtection import ExtendedProtectionPolicy, PolicyEnforcement, ProtectionScenario

# ---------- Types ---------- #

IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class ExtendedProtectionConfigurationStrings(ABC, ObjectType):
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


class ExtendedProtectionConfigurationStrings(ABC, ObjectType):
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


class ExtendedProtectionPolicyElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CustomServiceNames(self) -> ServiceNameElementCollection: ...
    
    @property
    def PolicyEnforcement(self) -> PolicyEnforcement: ...
    
    @PolicyEnforcement.setter
    def PolicyEnforcement(self, value: PolicyEnforcement) -> None: ...
    
    @property
    def ProtectionScenario(self) -> ProtectionScenario: ...
    
    @ProtectionScenario.setter
    def ProtectionScenario(self, value: ProtectionScenario) -> None: ...
    
    # ---------- Methods ---------- #
    
    def BuildPolicy(self) -> ExtendedProtectionPolicy: ...
    
    def get_CustomServiceNames(self) -> ServiceNameElementCollection: ...
    
    def get_PolicyEnforcement(self) -> PolicyEnforcement: ...
    
    def get_ProtectionScenario(self) -> ProtectionScenario: ...
    
    def set_PolicyEnforcement(self, value: PolicyEnforcement) -> VoidType: ...
    
    def set_ProtectionScenario(self, value: ProtectionScenario) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ExtendedProtectionPolicyElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CustomServiceNames(self) -> ServiceNameElementCollection: ...
    
    @property
    def PolicyEnforcement(self) -> PolicyEnforcement: ...
    
    @PolicyEnforcement.setter
    def PolicyEnforcement(self, value: PolicyEnforcement) -> None: ...
    
    @property
    def ProtectionScenario(self) -> ProtectionScenario: ...
    
    @ProtectionScenario.setter
    def ProtectionScenario(self, value: ProtectionScenario) -> None: ...
    
    # ---------- Methods ---------- #
    
    def BuildPolicy(self) -> ExtendedProtectionPolicy: ...
    
    def get_CustomServiceNames(self) -> ServiceNameElementCollection: ...
    
    def get_PolicyEnforcement(self) -> PolicyEnforcement: ...
    
    def get_ProtectionScenario(self) -> ProtectionScenario: ...
    
    def set_PolicyEnforcement(self, value: PolicyEnforcement) -> VoidType: ...
    
    def set_ProtectionScenario(self, value: ProtectionScenario) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ServiceNameElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> StringType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ServiceNameElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> StringType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ServiceNameElementCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    def __getitem__(self, key: IntType) -> ServiceNameElement: ...
    
    def __setitem__(self, key: IntType, value: ServiceNameElement) -> None: ...
    
    def __getitem__(self, key: StringType) -> ServiceNameElement: ...
    
    def __setitem__(self, key: StringType, value: ServiceNameElement) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, element: ServiceNameElement) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def IndexOf(self, element: ServiceNameElement) -> IntType: ...
    
    @overload
    def Remove(self, element: ServiceNameElement) -> VoidType: ...
    
    @overload
    def Remove(self, name: StringType) -> VoidType: ...
    
    def RemoveAt(self, index: IntType) -> VoidType: ...
    
    @overload
    def get_Item(self, index: IntType) -> ServiceNameElement: ...
    
    @overload
    def get_Item(self, name: StringType) -> ServiceNameElement: ...
    
    @overload
    def set_Item(self, index: IntType, value: ServiceNameElement) -> VoidType: ...
    
    @overload
    def set_Item(self, name: StringType, value: ServiceNameElement) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ServiceNameElementCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    def __getitem__(self, key: IntType) -> ServiceNameElement: ...
    
    def __setitem__(self, key: IntType, value: ServiceNameElement) -> None: ...
    
    def __getitem__(self, key: StringType) -> ServiceNameElement: ...
    
    def __setitem__(self, key: StringType, value: ServiceNameElement) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, element: ServiceNameElement) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def IndexOf(self, element: ServiceNameElement) -> IntType: ...
    
    @overload
    def Remove(self, element: ServiceNameElement) -> VoidType: ...
    
    @overload
    def Remove(self, name: StringType) -> VoidType: ...
    
    def RemoveAt(self, index: IntType) -> VoidType: ...
    
    @overload
    def get_Item(self, index: IntType) -> ServiceNameElement: ...
    
    @overload
    def get_Item(self, name: StringType) -> ServiceNameElement: ...
    
    @overload
    def set_Item(self, index: IntType, value: ServiceNameElement) -> VoidType: ...
    
    @overload
    def set_Item(self, name: StringType, value: ServiceNameElement) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# No Interfaces

# No Enums

# No Delegates

__all__ = [
    ExtendedProtectionConfigurationStrings,
    ExtendedProtectionPolicyElement,
    ServiceNameElement,
    ServiceNameElementCollection,
]
