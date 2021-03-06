from __future__ import annotations

from abc import ABC
from typing import Union

from System import Attribute, Enum, Int32, Object
from System.Runtime.InteropServices import _Attribute

# ---------- Types ---------- #

IntType = Union[int, Int32]
ObjectType = Object


# ---------- Classes ---------- #

class CriticalFinalizerObject(ABC, ObjectType):
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


class PrePrepareMethodAttribute(Attribute, _Attribute):
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


class ReliabilityContractAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, consistencyGuarantee: Consistency, cer: Cer): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Cer(self) -> Cer: ...
    
    @property
    def ConsistencyGuarantee(self) -> Consistency: ...
    
    # ---------- Methods ---------- #
    
    def get_Cer(self) -> Cer: ...
    
    def get_ConsistencyGuarantee(self) -> Consistency: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# No Interfaces

# ---------- Enums ---------- #

class Cer(Enum):
    #None = 0
    MayFail = 1
    Success = 2


class Consistency(Enum):
    MayCorruptProcess = 0
    MayCorruptAppDomain = 1
    MayCorruptInstance = 2
    WillNotCorruptState = 3


# No Delegates

__all__ = [
    CriticalFinalizerObject,
    PrePrepareMethodAttribute,
    ReliabilityContractAttribute,
    Cer,
    Consistency,
]
