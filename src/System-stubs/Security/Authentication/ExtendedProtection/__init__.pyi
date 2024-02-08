from __future__ import annotations

from abc import ABC
from typing import Iterator
from typing import overload

from Microsoft.Win32.SafeHandles import SafeHandleZeroOrMinusOneIsInvalid
from System import Array
from System import Attribute
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
from System.ComponentModel.TypeConverter import StandardValuesCollection
from System.Globalization import CultureInfo
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext

class ChannelBinding(ABC, SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""

    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    @property
    def Size(self) -> int:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

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
    def __init__(self, policyEnforcement: PolicyEnforcement):
        """

        :param policyEnforcement:
        """
    @overload
    def __init__(self, policyEnforcement: PolicyEnforcement, customChannelBinding: ChannelBinding):
        """

        :param policyEnforcement:
        :param customChannelBinding:
        """
    @overload
    def __init__(
        self,
        policyEnforcement: PolicyEnforcement,
        protectionScenario: ProtectionScenario,
        customServiceNames: ICollection,
    ):
        """

        :param policyEnforcement:
        :param protectionScenario:
        :param customServiceNames:
        """
    @overload
    def __init__(
        self,
        policyEnforcement: PolicyEnforcement,
        protectionScenario: ProtectionScenario,
        customServiceNames: ServiceNameCollection,
    ):
        """

        :param policyEnforcement:
        :param protectionScenario:
        :param customServiceNames:
        """
    @property
    def CustomChannelBinding(self) -> ChannelBinding:
        """

        :return:
        """
    @property
    def CustomServiceNames(self) -> ServiceNameCollection:
        """

        :return:
        """
    @classmethod
    @property
    def OSSupportsExtendedProtection(cls) -> bool:
        """

        :return:
        """
    @property
    def PolicyEnforcement(self) -> PolicyEnforcement:
        """

        :return:
        """
    @property
    def ProtectionScenario(self) -> ProtectionScenario:
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
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ExtendedProtectionPolicyTypeConverter(TypeConverter):
    """"""

    def __init__(self):
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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

    def __init__(self, items: ICollection):
        """

        :param items:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    def Contains(self, searchServiceName: str) -> bool:
        """

        :param searchServiceName:
        :return:
        """
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
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
    @overload
    def Merge(self, serviceNames: IEnumerable) -> ServiceNameCollection:
        """

        :param serviceNames:
        :return:
        """
    @overload
    def Merge(self, serviceName: str) -> ServiceNameCollection:
        """

        :param serviceName:
        :return:
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
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

class TokenBinding(Object):
    """"""

    @property
    def BindingType(self) -> TokenBindingType:
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
    def GetRawTokenBindingId(self) -> Array[int]:
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

class TokenBindingType(Enum):
    """"""

    Provided: TokenBindingType = ...
    """"""
    Referred: TokenBindingType = ...
    """"""
