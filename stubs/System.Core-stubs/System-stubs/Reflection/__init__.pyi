from __future__ import annotations

from abc import ABC
from typing import List, Union

from System import Array, Byte, Int32, Object
from System.Collections.Immutable import ImmutableArray

# ---------- Types ---------- #

ArrayType = Union[List, Array]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
ObjectType = Object

# ---------- Classes ---------- #

class BlobUtilities(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def SizeOfGuid() -> IntType: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def ReadBytes(buffer: ByteType, byteCount: IntType) -> ArrayType[ByteType]: ...
    
    @staticmethod
    def ReadImmutableBytes(buffer: ByteType, byteCount: IntType) -> ImmutableArray[ByteType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Throw(ABC, ObjectType):
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


# No Structs

# No Interfaces

# No Enums

# No Delegates

__all__ = [
    BlobUtilities,
    Throw,
]
