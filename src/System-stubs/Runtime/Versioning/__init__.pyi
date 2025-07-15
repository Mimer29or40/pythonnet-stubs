from abc import ABC
from typing import overload

from System import Attribute
from System import Enum
from System import Guid
from System import IEquatable
from System import IntPtr
from System import Object
from System import Type
from System import Version
from System.Runtime.InteropServices import _Attribute

class BinaryCompatibility(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class CompatibilitySwitch(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    def GetValue(cls, compatibilitySwitchName: str) -> str:
        """:param compatibilitySwitchName:
        :return:
        """
    @classmethod
    def IsEnabled(cls, compatibilitySwitchName: str) -> bool:
        """:param compatibilitySwitchName:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class ComponentGuaranteesAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, guarantees: ComponentGuaranteesOptions):
        """:param guarantees:"""
    @property
    def Guarantees(self) -> ComponentGuaranteesOptions:
        """:return:"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
        """:param pcTInfo:"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """:return:"""
    def Match(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class ComponentGuaranteesOptions(Enum):
    """"""

    _None: ComponentGuaranteesOptions = ...
    """"""
    Exchange: ComponentGuaranteesOptions = ...
    """"""
    Stable: ComponentGuaranteesOptions = ...
    """"""
    SideBySide: ComponentGuaranteesOptions = ...
    """"""

class FrameworkName(Object, IEquatable[FrameworkName]):
    """"""

    @overload
    def __init__(self, frameworkName: str):
        """:param frameworkName:"""
    @overload
    def __init__(self, identifier: str, version: Version):
        """:param identifier:
        :param version:
        """
    @overload
    def __init__(self, identifier: str, version: Version, profile: str):
        """:param identifier:
        :param version:
        :param profile:
        """
    @property
    def FullName(self) -> str:
        """:return:"""
    @property
    def Identifier(self) -> str:
        """:return:"""
    @property
    def Profile(self) -> str:
        """:return:"""
    @property
    def Version(self) -> Version:
        """:return:"""
    @overload
    def Equals(self, other: FrameworkName) -> bool:
        """:param other:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""
    def __eq__(self, other: FrameworkName) -> bool:
        """:param other:
        :return:
        """
    def __ne__(self, other: FrameworkName) -> bool:
        """:param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: FrameworkName, right: FrameworkName) -> bool:
        """:param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: FrameworkName, right: FrameworkName) -> bool:
        """:param left:
        :param right:
        :return:
        """

class MultitargetingHelpers(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    def ToString(self) -> str:
        """:return:"""

class NonVersionableAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
        """:param pcTInfo:"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """:return:"""
    def Match(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class ResourceConsumptionAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self, resourceScope: ResourceScope):
        """:param resourceScope:"""
    @overload
    def __init__(self, resourceScope: ResourceScope, consumptionScope: ResourceScope):
        """:param resourceScope:
        :param consumptionScope:
        """
    @property
    def ConsumptionScope(self) -> ResourceScope:
        """:return:"""
    @property
    def ResourceScope(self) -> ResourceScope:
        """:return:"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
        """:param pcTInfo:"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """:return:"""
    def Match(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class ResourceExposureAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, exposureLevel: ResourceScope):
        """:param exposureLevel:"""
    @property
    def ResourceExposureLevel(self) -> ResourceScope:
        """:return:"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
        """:param pcTInfo:"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """:return:"""
    def Match(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class ResourceScope(Enum):
    """"""

    _None: ResourceScope = ...
    """"""
    Machine: ResourceScope = ...
    """"""
    Process: ResourceScope = ...
    """"""
    AppDomain: ResourceScope = ...
    """"""
    Library: ResourceScope = ...
    """"""
    Private: ResourceScope = ...
    """"""
    Assembly: ResourceScope = ...
    """"""

class SxSRequirements(Enum):
    """"""

    _None: SxSRequirements = ...
    """"""
    AppDomainID: SxSRequirements = ...
    """"""
    ProcessID: SxSRequirements = ...
    """"""
    CLRInstanceID: SxSRequirements = ...
    """"""
    AssemblyName: SxSRequirements = ...
    """"""
    TypeName: SxSRequirements = ...
    """"""

class TargetFrameworkAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, frameworkName: str):
        """:param frameworkName:"""
    @property
    def FrameworkDisplayName(self) -> str:
        """:return:"""
    @FrameworkDisplayName.setter
    def FrameworkDisplayName(self, value: str) -> None: ...
    @property
    def FrameworkName(self) -> str:
        """:return:"""
    @property
    def TypeId(self) -> object:
        """:return:"""
    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """:param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """:return:"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """:param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> tuple[None, int]:
        """:param pcTInfo:"""
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """:param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """:return:"""
    def Match(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""

class TargetFrameworkId(Enum):
    """"""

    NotYetChecked: TargetFrameworkId = ...
    """"""
    Unrecognized: TargetFrameworkId = ...
    """"""
    Unspecified: TargetFrameworkId = ...
    """"""
    NetFramework: TargetFrameworkId = ...
    """"""
    Portable: TargetFrameworkId = ...
    """"""
    NetCore: TargetFrameworkId = ...
    """"""
    Silverlight: TargetFrameworkId = ...
    """"""
    Phone: TargetFrameworkId = ...
    """"""

class VersioningHelper(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """:param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """:return:"""
    def GetType(self) -> Type:
        """:return:"""
    @classmethod
    @overload
    def MakeVersionSafeName(cls, name: str, _from: ResourceScope, to: ResourceScope) -> str:
        """:param name:
        :param _from:
        :param to:
        :return:
        """
    @classmethod
    @overload
    def MakeVersionSafeName(
        cls, name: str, _from: ResourceScope, to: ResourceScope, type: Type
    ) -> str:
        """:param name:
        :param _from:
        :param to:
        :param type:
        :return:
        """
    def ToString(self) -> str:
        """:return:"""
