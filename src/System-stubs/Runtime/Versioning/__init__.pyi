from __future__ import annotations

from abc import ABC
from typing import Union, overload

from System import Attribute, Boolean, Enum, IEquatable, Int32, Object, String, Type, Version, Void
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


class FrameworkName(ObjectType, IEquatable[FrameworkName]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, identifier: StringType, version: Version): ...
    
    @overload
    def __init__(self, identifier: StringType, version: Version, profile: StringType): ...
    
    @overload
    def __init__(self, frameworkName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def FullName(self) -> StringType: ...
    
    @property
    def Identifier(self) -> StringType: ...
    
    @property
    def Profile(self) -> StringType: ...
    
    @property
    def Version(self) -> Version: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: FrameworkName) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_FullName(self) -> StringType: ...
    
    def get_Identifier(self) -> StringType: ...
    
    def get_Profile(self) -> StringType: ...
    
    def get_Version(self) -> Version: ...
    
    @staticmethod
    def op_Equality(left: FrameworkName, right: FrameworkName) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: FrameworkName, right: FrameworkName) -> BooleanType: ...
    
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
    def MakeVersionSafeName(name: StringType, _from: ResourceScope, to: ResourceScope, type: TypeType) -> StringType: ...
    
    @staticmethod
    @overload
    def MakeVersionSafeName(name: StringType, _from: ResourceScope, to: ResourceScope) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# No Interfaces

# ---------- Enums ---------- #

class ComponentGuaranteesOptions(Enum):
    #None = 0
    Exchange = 1
    Stable = 2
    SideBySide = 4


class ResourceScope(Enum):
    #None = 0
    Machine = 1
    Process = 2
    AppDomain = 4
    Library = 8
    Private = 16
    Assembly = 32


class SxSRequirements(Enum):
    #None = 0
    AppDomainID = 1
    ProcessID = 2
    CLRInstanceID = 4
    AssemblyName = 8
    TypeName = 16


class TargetFrameworkId(Enum):
    NotYetChecked = 0
    Unrecognized = 1
    Unspecified = 2
    NetFramework = 3
    Portable = 4
    NetCore = 5
    Silverlight = 6
    Phone = 7


# No Delegates

__all__ = [
    BinaryCompatibility,
    CompatibilitySwitch,
    ComponentGuaranteesAttribute,
    FrameworkName,
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
