from __future__ import annotations

from abc import ABC
from typing import List, Union

from System import Array, Boolean, Byte, Enum, IDisposable, Int32, Int64, Object, Void
from System.IO import SeekOrigin, Stream

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
ObjectType = Object
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class BufferedStream2(ABC, Stream, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Flush(self) -> VoidType: ...
    
    def Write(self, array: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LogStream(BufferedStream2, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CanRead(self) -> BooleanType: ...
    
    @property
    def CanSeek(self) -> BooleanType: ...
    
    @property
    def CanWrite(self) -> BooleanType: ...
    
    @property
    def Length(self) -> LongType: ...
    
    @property
    def Position(self) -> LongType: ...
    
    @Position.setter
    def Position(self, value: LongType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Read(self, array: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanSeek(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_Length(self) -> LongType: ...
    
    def get_Position(self) -> LongType: ...
    
    def set_Position(self, value: LongType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class __Error(ABC, ObjectType):
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

# ---------- Enums ---------- #

class HandleInheritability(Enum):
    #None: IntType = 0
    Inheritable: IntType = 1


class LogRetentionOption(Enum):
    UnlimitedSequentialFiles: IntType = 0
    LimitedCircularFiles: IntType = 1
    SingleFileUnboundedSize: IntType = 2
    LimitedSequentialFiles: IntType = 3
    SingleFileBoundedSize: IntType = 4


# No Delegates

__all__ = [
    BufferedStream2,
    LogStream,
    __Error,
    HandleInheritability,
    LogRetentionOption,
]
