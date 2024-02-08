from __future__ import annotations

from abc import ABC
from typing import Tuple

from System import Attribute
from System import Enum
from System import Guid
from System import IDisposable
from System import IntPtr
from System import Object
from System import Type
from System.Runtime.ConstrainedExecution import CriticalFinalizerObject
from System.Runtime.InteropServices import _Attribute

class AssemblyTargetedPatchBandAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, targetedPatchBand: str):
        """

        :param targetedPatchBand:
        """
    @property
    def TargetedPatchBand(self) -> str:
        """

        :return:
        """
    @property
    def TypeId(self) -> object:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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
        """

        :return:
        """
    @classmethod
    @property
    def LargeObjectHeapCompactionMode(cls) -> GCLargeObjectHeapCompactionMode:
        """

        :return:
        """
    @classmethod
    @LargeObjectHeapCompactionMode.setter
    def LargeObjectHeapCompactionMode(cls, value: GCLargeObjectHeapCompactionMode) -> None: ...
    @classmethod
    @property
    def LatencyMode(cls) -> GCLatencyMode:
        """

        :return:
        """
    @classmethod
    @LatencyMode.setter
    def LatencyMode(cls, value: GCLatencyMode) -> None: ...
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
    def ToString(self) -> str:
        """

        :return:
        """

class MemoryFailPoint(CriticalFinalizerObject, IDisposable):
    """"""

    def __init__(self, sizeInMegabytes: int):
        """

        :param sizeInMegabytes:
        """
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
    def ToString(self) -> str:
        """

        :return:
        """

class ProfileOptimization(ABC, Object):
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
    @classmethod
    def SetProfileRoot(cls, directoryPath: str) -> None:
        """

        :param directoryPath:
        """
    @classmethod
    def StartProfile(cls, profile: str) -> None:
        """

        :param profile:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class TargetedPatchingOptOutAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, reason: str):
        """

        :param reason:
        """
    @property
    def Reason(self) -> str:
        """

        :return:
        """
    @property
    def TypeId(self) -> object:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
