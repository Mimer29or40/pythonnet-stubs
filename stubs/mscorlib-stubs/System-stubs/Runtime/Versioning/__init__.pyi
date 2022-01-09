from __future__ import annotations

from abc import ABC
from typing import Union, overload

from System import Attribute, Boolean, Enum, Int32, Object, String, Type, Void
from System.Runtime.InteropServices import _Attribute

# ---------- Types ---------- #

BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class BinaryCompatibility(ABC, ObjectType):
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


class CompatibilitySwitch(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetValue(compatibilitySwitchName: StringType) -> StringType: ...
    
    @staticmethod
    def IsEnabled(compatibilitySwitchName: StringType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ComponentGuaranteesAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, guarantees: ComponentGuaranteesOptions): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Guarantees(self) -> ComponentGuaranteesOptions: ...
    
    # ---------- Methods ---------- #
    
    def get_Guarantees(self) -> ComponentGuaranteesOptions: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MultitargetingHelpers(ABC, ObjectType):
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


class NonVersionableAttribute(Attribute, _Attribute):
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


class ResourceConsumptionAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, resourceScope: ResourceScope): ...
    
    @overload
    def __init__(self, resourceScope: ResourceScope, consumptionScope: ResourceScope): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ConsumptionScope(self) -> ResourceScope: ...
    
    @property
    def ResourceScope(self) -> ResourceScope: ...
    
    # ---------- Methods ---------- #
    
    def get_ConsumptionScope(self) -> ResourceScope: ...
    
    def get_ResourceScope(self) -> ResourceScope: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ResourceExposureAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, exposureLevel: ResourceScope): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ResourceExposureLevel(self) -> ResourceScope: ...
    
    # ---------- Methods ---------- #
    
    def get_ResourceExposureLevel(self) -> ResourceScope: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TargetFrameworkAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, frameworkName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def FrameworkDisplayName(self) -> StringType: ...
    
    @FrameworkDisplayName.setter
    def FrameworkDisplayName(self, value: StringType) -> None: ...
    
    @property
    def FrameworkName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_FrameworkDisplayName(self) -> StringType: ...
    
    def get_FrameworkName(self) -> StringType: ...
    
    def set_FrameworkDisplayName(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class VersioningHelper(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def MakeVersionSafeName(name: StringType, from: ResourceScope, to: ResourceScope, type: TypeType) -> StringType: ...
    
    @staticmethod
    @overload
    def MakeVersionSafeName(name: StringType, from: ResourceScope, to: ResourceScope) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# No Interfaces

# ---------- Enums ---------- #

class ComponentGuaranteesOptions(Enum):
    #None: IntType = 0
    Exchange: IntType = 1
    Stable: IntType = 2
    SideBySide: IntType = 4


class ResourceScope(Enum):
    #None: IntType = 0
    Machine: IntType = 1
    Process: IntType = 2
    AppDomain: IntType = 4
    Library: IntType = 8
    Private: IntType = 16
    Assembly: IntType = 32


class SxSRequirements(Enum):
    #None: IntType = 0
    AppDomainID: IntType = 1
    ProcessID: IntType = 2
    CLRInstanceID: IntType = 4
    AssemblyName: IntType = 8
    TypeName: IntType = 16


class TargetFrameworkId(Enum):
    NotYetChecked: IntType = 0
    Unrecognized: IntType = 1
    Unspecified: IntType = 2
    NetFramework: IntType = 3
    Portable: IntType = 4
    NetCore: IntType = 5
    Silverlight: IntType = 6
    Phone: IntType = 7


# No Delegates

__all__ = [
    BinaryCompatibility,
    CompatibilitySwitch,
    ComponentGuaranteesAttribute,
    MultitargetingHelpers,
    NonVersionableAttribute,
    ResourceConsumptionAttribute,
    ResourceExposureAttribute,
    TargetFrameworkAttribute,
    VersioningHelper,
    ComponentGuaranteesOptions,
    ResourceScope,
    SxSRequirements,
    TargetFrameworkId,
]
