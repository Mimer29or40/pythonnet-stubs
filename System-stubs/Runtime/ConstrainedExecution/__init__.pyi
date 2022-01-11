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
    #None: IntType = 0
    MayFail: IntType = 1
    Success: IntType = 2


class Cer(Enum):
    #None: IntType = 0
    MayFail: IntType = 1
    Success: IntType = 2


class Cer(Enum):
    #None: IntType = 0
    MayFail: IntType = 1
    Success: IntType = 2


class Consistency(Enum):
    MayCorruptProcess: IntType = 0
    MayCorruptAppDomain: IntType = 1
    MayCorruptInstance: IntType = 2
    WillNotCorruptState: IntType = 3


class Consistency(Enum):
    MayCorruptProcess: IntType = 0
    MayCorruptAppDomain: IntType = 1
    MayCorruptInstance: IntType = 2
    WillNotCorruptState: IntType = 3


class Consistency(Enum):
    MayCorruptProcess: IntType = 0
    MayCorruptAppDomain: IntType = 1
    MayCorruptInstance: IntType = 2
    WillNotCorruptState: IntType = 3


# No Delegates

__all__ = [
    CriticalFinalizerObject,
    PrePrepareMethodAttribute,
    ReliabilityContractAttribute,
    Cer,
    Consistency,
]
