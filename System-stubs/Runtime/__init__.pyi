from __future__ import annotations

from abc import ABC
from typing import Union

from System import Attribute, Boolean, Enum, IDisposable, Int32, Object, String, Void
from System.Runtime.ConstrainedExecution import CriticalFinalizerObject
from System.Runtime.InteropServices import _Attribute

# ---------- Types ---------- #

BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class AssemblyTargetedPatchBandAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, targetedPatchBand: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TargetedPatchBand(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_TargetedPatchBand(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GCSettings(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def IsServerGC() -> BooleanType: ...
    
    @staticmethod
    @property
    def LargeObjectHeapCompactionMode() -> GCLargeObjectHeapCompactionMode: ...
    
    @staticmethod
    @LargeObjectHeapCompactionMode.setter
    def LargeObjectHeapCompactionMode(value: GCLargeObjectHeapCompactionMode) -> None: ...
    
    @staticmethod
    @property
    def LatencyMode() -> GCLatencyMode: ...
    
    @staticmethod
    @LatencyMode.setter
    def LatencyMode(value: GCLatencyMode) -> None: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def get_IsServerGC() -> BooleanType: ...
    
    @staticmethod
    def get_LargeObjectHeapCompactionMode() -> GCLargeObjectHeapCompactionMode: ...
    
    @staticmethod
    def get_LatencyMode() -> GCLatencyMode: ...
    
    @staticmethod
    def set_LargeObjectHeapCompactionMode(value: GCLargeObjectHeapCompactionMode) -> VoidType: ...
    
    @staticmethod
    def set_LatencyMode(value: GCLatencyMode) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MemoryFailPoint(CriticalFinalizerObject, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, sizeInMegabytes: IntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ProfileOptimization(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def SetProfileRoot(directoryPath: StringType) -> VoidType: ...
    
    @staticmethod
    def StartProfile(profile: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TargetedPatchingOptOutAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, reason: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Reason(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Reason(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# No Interfaces

# ---------- Enums ---------- #

class GCLargeObjectHeapCompactionMode(Enum):
    Default: IntType = 1
    CompactOnce: IntType = 2


class GCLatencyMode(Enum):
    Batch: IntType = 0
    Interactive: IntType = 1
    LowLatency: IntType = 2
    SustainedLowLatency: IntType = 3
    NoGCRegion: IntType = 4


# No Delegates

__all__ = [
    AssemblyTargetedPatchBandAttribute,
    GCSettings,
    MemoryFailPoint,
    ProfileOptimization,
    TargetedPatchingOptOutAttribute,
    GCLargeObjectHeapCompactionMode,
    GCLatencyMode,
]
