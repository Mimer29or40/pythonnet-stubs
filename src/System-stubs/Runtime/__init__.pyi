"""Automatically generated stubs for C# namespace: System.Runtime."""

from abc import ABC

from System import Attribute
from System import Enum
from System import Guid
from System import IDisposable
from System import IntPtr
from System import Object
from System import Type
from System import UInt32
from System.Runtime.ConstrainedExecution import CriticalFinalizerObject
from System.Runtime.InteropServices import _Attribute

class AssemblyTargetedPatchBandAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, targetedPatchBand: str) -> None:
        """"""
    @property
    def TargetedPatchBand(self) -> str:
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

class GCLargeObjectHeapCompactionMode(Enum):
    """"""

    Default: GCLargeObjectHeapCompactionMode = ...
    """"""
    CompactOnce: GCLargeObjectHeapCompactionMode = ...
    """"""

class GCLatencyMode(Enum):
    """"""

    Batch: GCLatencyMode = ...
    """"""
    Interactive: GCLatencyMode = ...
    """"""
    LowLatency: GCLatencyMode = ...
    """"""
    SustainedLowLatency: GCLatencyMode = ...
    """"""
    NoGCRegion: GCLatencyMode = ...
    """"""

class GCSettings(ABC, Object):
    """"""
    @classmethod
    @property
    def IsServerGC(cls) -> bool:
        """"""
    @classmethod
    @property
    def LargeObjectHeapCompactionMode(cls) -> GCLargeObjectHeapCompactionMode:
        """"""
    @classmethod
    @LargeObjectHeapCompactionMode.setter
    def LargeObjectHeapCompactionMode(cls, value: GCLargeObjectHeapCompactionMode) -> None: ...
    @classmethod
    @property
    def LatencyMode(cls) -> GCLatencyMode:
        """"""
    @classmethod
    @LatencyMode.setter
    def LatencyMode(cls, value: GCLatencyMode) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MemoryFailPoint(CriticalFinalizerObject, IDisposable):
    """"""
    def __init__(self, sizeInMegabytes: int) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ProfileOptimization(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def SetProfileRoot(cls, directoryPath: str) -> None:
        """"""
    @classmethod
    def StartProfile(cls, profile: str) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class TargetedPatchingOptOutAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, reason: str) -> None:
        """"""
    @property
    def Reason(self) -> str:
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
