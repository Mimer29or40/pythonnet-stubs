"""Automatically generated stubs for C# namespace: System.Runtime.Versioning."""

from abc import ABC
from typing import overload

from System import Attribute
from System import Enum
from System import Guid
from System import IEquatable
from System import IntPtr
from System import Object
from System import Type
from System import UInt32
from System import Version
from System.Runtime.InteropServices import _Attribute

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class BinaryCompatibility(ABC, Object):
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
class CompatibilitySwitch(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def GetValue(cls, compatibilitySwitchName: str) -> str:
        """"""
    @classmethod
    def IsEnabled(cls, compatibilitySwitchName: str) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ComponentGuaranteesAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, guarantees: ComponentGuaranteesOptions) -> None:
        """"""
    @property
    def Guarantees(self) -> ComponentGuaranteesOptions:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
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
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class FrameworkName(Object, IEquatable[FrameworkName]):
    """"""
    @overload
    def __init__(self, identifier: str, version: Version) -> None:
        """"""
    @overload
    def __init__(self, identifier: str, version: Version, profile: str) -> None:
        """"""
    @overload
    def __init__(self, frameworkName: str) -> None:
        """"""
    @property
    def FullName(self) -> str:
        """"""
    @property
    def Identifier(self) -> str:
        """"""
    @property
    def Profile(self) -> str:
        """"""
    @property
    def Version(self) -> Version:
        """"""
    @overload
    def Equals(self, other: FrameworkName) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, left: FrameworkName, right: FrameworkName) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: FrameworkName, right: FrameworkName) -> bool:
        """"""
    def __eq__(self, other: FrameworkName) -> bool:
        """"""
    def __ne__(self, other: FrameworkName) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MultitargetingHelpers(ABC, Object):
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
class NonVersionableAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
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
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ResourceConsumptionAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, resourceScope: ResourceScope) -> None:
        """"""
    @overload
    def __init__(self, resourceScope: ResourceScope, consumptionScope: ResourceScope) -> None:
        """"""
    @property
    def ConsumptionScope(self) -> ResourceScope:
        """"""
    @property
    def ResourceScope(self) -> ResourceScope:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
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
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ResourceExposureAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, exposureLevel: ResourceScope) -> None:
        """"""
    @property
    def ResourceExposureLevel(self) -> ResourceScope:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
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
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TargetFrameworkAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, frameworkName: str) -> None:
        """"""
    @property
    def FrameworkDisplayName(self) -> str:
        """"""
    @FrameworkDisplayName.setter
    def FrameworkDisplayName(self, value: str) -> None: ...
    @property
    def FrameworkName(self) -> str:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
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
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class VersioningHelper(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def MakeVersionSafeName(cls, name: str, _from: ResourceScope, to: ResourceScope) -> str:
        """"""
    @classmethod
    @overload
    def MakeVersionSafeName(
        cls, name: str, _from: ResourceScope, to: ResourceScope, type: Type
    ) -> str:
        """"""
    def ToString(self) -> str:
        """"""
