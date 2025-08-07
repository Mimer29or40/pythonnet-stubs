"""Automatically generated stubs for C# namespace: System.Security.Authentication.ExtendedProtection."""

from abc import ABC
from collections.abc import Iterator
from typing import overload

from Microsoft.Win32.SafeHandles import SafeHandleZeroOrMinusOneIsInvalid
from System import Array
from System import Attribute
from System import Boolean
from System import Enum
from System import IDisposable
from System import IntPtr
from System import Object
from System import Type
from System.Collections import ICollection
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections import ReadOnlyCollectionBase
from System.ComponentModel import ITypeDescriptorContext
from System.ComponentModel import PropertyDescriptorCollection
from System.ComponentModel import TypeConverter
from System.Globalization import CultureInfo
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext

class ChannelBinding(ABC, SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    @property
    def Size(self) -> int:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class ChannelBindingKind(Enum):
    """"""

    Unknown: ChannelBindingKind = ...
    """"""
    Unique: ChannelBindingKind = ...
    """"""
    Endpoint: ChannelBindingKind = ...
    """"""

class ExtendedProtectionPolicy(Object, ISerializable):
    """"""
    @overload
    def __init__(
        self,
        policyEnforcement: PolicyEnforcement,
        protectionScenario: ProtectionScenario,
        customServiceNames: ServiceNameCollection,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        policyEnforcement: PolicyEnforcement,
        protectionScenario: ProtectionScenario,
        customServiceNames: ICollection,
    ) -> None:
        """"""
    @overload
    def __init__(
        self, policyEnforcement: PolicyEnforcement, customChannelBinding: ChannelBinding
    ) -> None:
        """"""
    @overload
    def __init__(self, policyEnforcement: PolicyEnforcement) -> None:
        """"""
    @property
    def CustomChannelBinding(self) -> ChannelBinding:
        """"""
    @property
    def CustomServiceNames(self) -> ServiceNameCollection:
        """"""
    @classmethod
    @property
    def OSSupportsExtendedProtection(cls) -> bool:
        """"""
    @property
    def PolicyEnforcement(self) -> PolicyEnforcement:
        """"""
    @property
    def ProtectionScenario(self) -> ProtectionScenario:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ExtendedProtectionPolicyTypeConverter(TypeConverter):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

class PolicyEnforcement(Enum):
    """"""

    Never: PolicyEnforcement = ...
    """"""
    WhenSupported: PolicyEnforcement = ...
    """"""
    Always: PolicyEnforcement = ...
    """"""

class ProtectionScenario(Enum):
    """"""

    TransportSelected: ProtectionScenario = ...
    """"""
    TrustedProxy: ProtectionScenario = ...
    """"""

class ServiceNameCollection(ReadOnlyCollectionBase, ICollection, IEnumerable):
    """"""
    def __init__(self, items: ICollection) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    def Contains(self, searchServiceName: str) -> bool:
        """"""
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def Merge(self, serviceNames: IEnumerable) -> ServiceNameCollection:
        """"""
    @overload
    def Merge(self, serviceName: str) -> ServiceNameCollection:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, searchServiceName: str) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""

class TokenBinding(Object):
    """"""
    @property
    def BindingType(self) -> TokenBindingType:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetRawTokenBindingId(self) -> Array[int]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TokenBindingType(Enum):
    """"""

    Provided: TokenBindingType = ...
    """"""
    Referred: TokenBindingType = ...
    """"""
