from __future__ import annotations

from typing import List, Union, overload

from System import Array, Byte, Enum, ICloneable, Int32, Object, ValueType, Void

# ---------- Types ---------- #

ArrayType = Union[List, Array]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
ObjectType = Object
VoidType = Union[None, Void]


# No Classes

# ---------- Structs ---------- #

class AssemblyHash(ValueType, ICloneable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Empty() -> AssemblyHash: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, value: ArrayType[ByteType]): ...
    
    @overload
    def __init__(self, algorithm: AssemblyHashAlgorithm, value: ArrayType[ByteType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Algorithm(self) -> AssemblyHashAlgorithm: ...
    
    @Algorithm.setter
    def Algorithm(self, value: AssemblyHashAlgorithm) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Clone(self) -> ObjectType: ...
    
    def GetValue(self) -> ArrayType[ByteType]: ...
    
    def SetValue(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    def get_Algorithm(self) -> AssemblyHashAlgorithm: ...
    
    def set_Algorithm(self, value: AssemblyHashAlgorithm) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Interfaces

# ---------- Enums ---------- #

class AssemblyHashAlgorithm(Enum):
    #None = 0
    MD5 = 32771
    SHA1 = 32772
    SHA256 = 32780
    SHA384 = 32781
    SHA512 = 32782


class AssemblyVersionCompatibility(Enum):
    SameMachine = 1
    SameProcess = 2
    SameDomain = 3


# No Delegates

__all__ = [
    AssemblyHash,
    AssemblyHashAlgorithm,
    AssemblyVersionCompatibility,
]
