from __future__ import annotations

from abc import ABC
from typing import List
from typing import Union
from typing import overload

from Microsoft.Win32.SafeHandles import SafeHandleZeroOrMinusOneIsInvalid
from System import Array
from System import Boolean
from System import Byte
from System import Enum
from System import IDisposable
from System import Int32
from System import Object
from System import String
from System import Type
from System.Collections import ICollection
from System.Collections import IEnumerable
from System.Collections import ReadOnlyCollectionBase
from System.ComponentModel import ITypeDescriptorContext
from System.ComponentModel import TypeConverter
from System.Globalization import CultureInfo
from System.Runtime.Serialization import ISerializable

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]

# ---------- Classes ---------- #

class ChannelBinding(ABC, SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Size(self) -> IntType: ...

    # ---------- Methods ---------- #

    def get_Size(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ExtendedProtectionPolicy(ObjectType, ISerializable):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(
        self,
        policyEnforcement: PolicyEnforcement,
        protectionScenario: ProtectionScenario,
        customServiceNames: ServiceNameCollection,
    ): ...
    @overload
    def __init__(
        self,
        policyEnforcement: PolicyEnforcement,
        protectionScenario: ProtectionScenario,
        customServiceNames: ICollection,
    ): ...
    @overload
    def __init__(
        self, policyEnforcement: PolicyEnforcement, customChannelBinding: ChannelBinding
    ): ...
    @overload
    def __init__(self, policyEnforcement: PolicyEnforcement): ...

    # ---------- Properties ---------- #

    @property
    def CustomChannelBinding(self) -> ChannelBinding: ...
    @property
    def CustomServiceNames(self) -> ServiceNameCollection: ...
    @staticmethod
    @property
    def OSSupportsExtendedProtection() -> BooleanType: ...
    @property
    def PolicyEnforcement(self) -> PolicyEnforcement: ...
    @property
    def ProtectionScenario(self) -> ProtectionScenario: ...

    # ---------- Methods ---------- #

    def ToString(self) -> StringType: ...
    def get_CustomChannelBinding(self) -> ChannelBinding: ...
    def get_CustomServiceNames(self) -> ServiceNameCollection: ...
    @staticmethod
    def get_OSSupportsExtendedProtection() -> BooleanType: ...
    def get_PolicyEnforcement(self) -> PolicyEnforcement: ...
    def get_ProtectionScenario(self) -> ProtectionScenario: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ExtendedProtectionPolicyTypeConverter(TypeConverter):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def CanConvertTo(
        self, context: ITypeDescriptorContext, destinationType: TypeType
    ) -> BooleanType: ...
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: ObjectType,
        destinationType: TypeType,
    ) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ServiceNameCollection(ReadOnlyCollectionBase, ICollection, IEnumerable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, items: ICollection): ...

    # No Properties

    # ---------- Methods ---------- #

    def Contains(self, searchServiceName: StringType) -> BooleanType: ...
    @overload
    def Merge(self, serviceName: StringType) -> ServiceNameCollection: ...
    @overload
    def Merge(self, serviceNames: IEnumerable) -> ServiceNameCollection: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class TokenBinding(ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def BindingType(self) -> TokenBindingType: ...

    # ---------- Methods ---------- #

    def GetRawTokenBindingId(self) -> ArrayType[ByteType]: ...
    def get_BindingType(self) -> TokenBindingType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

# No Structs

# No Interfaces

# ---------- Enums ---------- #

class ChannelBindingKind(Enum):
    Unknown = 0
    Unique = 25
    Endpoint = 26

class PolicyEnforcement(Enum):
    Never = 0
    WhenSupported = 1
    Always = 2

class ProtectionScenario(Enum):
    TransportSelected = 0
    TrustedProxy = 1

class TokenBindingType(Enum):
    Provided = 0
    Referred = 1

# No Delegates

__all__ = [
    ChannelBinding,
    ExtendedProtectionPolicy,
    ExtendedProtectionPolicyTypeConverter,
    ServiceNameCollection,
    TokenBinding,
    ChannelBindingKind,
    PolicyEnforcement,
    ProtectionScenario,
    TokenBindingType,
]
