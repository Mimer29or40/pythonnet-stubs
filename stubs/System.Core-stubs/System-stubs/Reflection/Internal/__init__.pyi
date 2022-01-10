from __future__ import annotations

from abc import ABC
from typing import Generic, List, Tuple, TypeVar, Union, overload

from System import Array, Boolean, Byte, IDisposable, Int32, Int64, Object, String, ValueType, Void
from System.Collections.Immutable import ImmutableArray
from System.IO import SeekOrigin, Stream
from System.Reflection.Metadata import BlobReader
from System.Runtime.ConstrainedExecution import CriticalFinalizerObject
from System.Text import StringBuilder

# ---------- Types ---------- #

T = TypeVar('T')

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class AbstractMemoryBlock(ABC, ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Pointer(self) -> ByteType: ...
    
    @property
    def Size(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def GetReader(self) -> BlobReader: ...
    
    def get_Pointer(self) -> ByteType: ...
    
    def get_Size(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AbstractMemoryBlock(ABC, ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Pointer(self) -> ByteType: ...
    
    @property
    def Size(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def GetReader(self) -> BlobReader: ...
    
    def get_Pointer(self) -> ByteType: ...
    
    def get_Size(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ByteArrayMemoryBlock(AbstractMemoryBlock, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Pointer(self) -> ByteType: ...
    
    @property
    def Size(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def get_Pointer(self) -> ByteType: ...
    
    def get_Size(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ByteArrayMemoryBlock(AbstractMemoryBlock, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Pointer(self) -> ByteType: ...
    
    @property
    def Size(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def get_Pointer(self) -> ByteType: ...
    
    def get_Size(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ByteArrayMemoryProvider(MemoryBlockProvider, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, array: ImmutableArray[ByteType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Array(self) -> ImmutableArray[ByteType]: ...
    
    @property
    def Size(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def GetStream(self, constraints: StreamConstraints) -> Tuple[Stream, StreamConstraints]: ...
    
    def get_Array(self) -> ImmutableArray[ByteType]: ...
    
    def get_Size(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ByteArrayMemoryProvider(MemoryBlockProvider, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, array: ImmutableArray[ByteType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Array(self) -> ImmutableArray[ByteType]: ...
    
    @property
    def Size(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def GetStream(self, constraints: StreamConstraints) -> Tuple[Stream, StreamConstraints]: ...
    
    def get_Array(self) -> ImmutableArray[ByteType]: ...
    
    def get_Size(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CriticalDisposableObject(ABC, CriticalFinalizerObject, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CriticalDisposableObject(ABC, CriticalFinalizerObject, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ExternalMemoryBlock(AbstractMemoryBlock, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, memoryOwner: ObjectType, buffer: ByteType, size: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Pointer(self) -> ByteType: ...
    
    @property
    def Size(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def get_Pointer(self) -> ByteType: ...
    
    def get_Size(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ExternalMemoryBlock(AbstractMemoryBlock, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, memoryOwner: ObjectType, buffer: ByteType, size: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Pointer(self) -> ByteType: ...
    
    @property
    def Size(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def get_Pointer(self) -> ByteType: ...
    
    def get_Size(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ExternalMemoryBlockProvider(MemoryBlockProvider, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, memory: ByteType, size: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Pointer(self) -> ByteType: ...
    
    @property
    def Size(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def GetStream(self, constraints: StreamConstraints) -> Tuple[Stream, StreamConstraints]: ...
    
    def get_Pointer(self) -> ByteType: ...
    
    def get_Size(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ExternalMemoryBlockProvider(MemoryBlockProvider, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, memory: ByteType, size: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Pointer(self) -> ByteType: ...
    
    @property
    def Size(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def GetStream(self, constraints: StreamConstraints) -> Tuple[Stream, StreamConstraints]: ...
    
    def get_Pointer(self) -> ByteType: ...
    
    def get_Size(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Hash(ABC, ObjectType):
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


class Hash(ABC, ObjectType):
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


class ImmutableMemoryStream(Stream, IDisposable):
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
    
    def Flush(self) -> VoidType: ...
    
    def GetBuffer(self) -> ImmutableArray[ByteType]: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
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


class ImmutableMemoryStream(Stream, IDisposable):
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
    
    def Flush(self) -> VoidType: ...
    
    def GetBuffer(self) -> ImmutableArray[ByteType]: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
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


class LightUpHelper(ABC, ObjectType):
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


class LightUpHelper(ABC, ObjectType):
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


class MemoryBlockProvider(ABC, ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Size(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    @overload
    def GetMemoryBlock(self) -> AbstractMemoryBlock: ...
    
    @overload
    def GetMemoryBlock(self, start: IntType, size: IntType) -> AbstractMemoryBlock: ...
    
    def GetStream(self, constraints: StreamConstraints) -> Tuple[Stream, StreamConstraints]: ...
    
    def get_Size(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MemoryBlockProvider(ABC, ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Size(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    @overload
    def GetMemoryBlock(self) -> AbstractMemoryBlock: ...
    
    @overload
    def GetMemoryBlock(self, start: IntType, size: IntType) -> AbstractMemoryBlock: ...
    
    def GetStream(self, constraints: StreamConstraints) -> Tuple[Stream, StreamConstraints]: ...
    
    def get_Size(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MemoryMapLightUp(ABC, ObjectType):
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


class MemoryMapLightUp(ABC, ObjectType):
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


class MemoryMappedFileBlock(AbstractMemoryBlock, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Pointer(self) -> ByteType: ...
    
    @property
    def Size(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def get_Pointer(self) -> ByteType: ...
    
    def get_Size(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MemoryMappedFileBlock(AbstractMemoryBlock, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Pointer(self) -> ByteType: ...
    
    @property
    def Size(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def get_Pointer(self) -> ByteType: ...
    
    def get_Size(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NativeHeapMemoryBlock(AbstractMemoryBlock, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Pointer(self) -> ByteType: ...
    
    @property
    def Size(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def get_Pointer(self) -> ByteType: ...
    
    def get_Size(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NativeHeapMemoryBlock(AbstractMemoryBlock, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Pointer(self) -> ByteType: ...
    
    @property
    def Size(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def get_Pointer(self) -> ByteType: ...
    
    def get_Size(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ObjectPool(Generic[T], ObjectType):
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


class ObjectPool(Generic[T], ObjectType):
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


class PinnedObject(CriticalDisposableObject, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, obj: ObjectType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Pointer(self) -> ByteType: ...
    
    # ---------- Methods ---------- #
    
    def get_Pointer(self) -> ByteType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PinnedObject(CriticalDisposableObject, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, obj: ObjectType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Pointer(self) -> ByteType: ...
    
    # ---------- Methods ---------- #
    
    def get_Pointer(self) -> ByteType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PooledStringBuilder(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def Builder(self) -> StringBuilder: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Length(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CreatePool() -> ObjectPool[PooledStringBuilder]: ...
    
    def Free(self) -> VoidType: ...
    
    @staticmethod
    def GetInstance() -> PooledStringBuilder: ...
    
    def ToStringAndFree(self) -> StringType: ...
    
    def get_Length(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PooledStringBuilder(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def Builder(self) -> StringBuilder: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Length(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CreatePool() -> ObjectPool[PooledStringBuilder]: ...
    
    def Free(self) -> VoidType: ...
    
    @staticmethod
    def GetInstance() -> PooledStringBuilder: ...
    
    def ToStringAndFree(self) -> StringType: ...
    
    def get_Length(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ReadOnlyUnmanagedMemoryStream(Stream, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, data: ByteType, length: IntType): ...
    
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
    
    def Flush(self) -> VoidType: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    
    def ReadByte(self) -> IntType: ...
    
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
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


class ReadOnlyUnmanagedMemoryStream(Stream, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, data: ByteType, length: IntType): ...
    
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
    
    def Flush(self) -> VoidType: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    
    def ReadByte(self) -> IntType: ...
    
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
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


class StreamExtensions(ABC, ObjectType):
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


class StreamExtensions(ABC, ObjectType):
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


class StreamMemoryBlockProvider(MemoryBlockProvider, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, stream: Stream, imageStart: LongType, imageSize: IntType, isFileStream: BooleanType, leaveOpen: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Size(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def GetStream(self, constraints: StreamConstraints) -> Tuple[Stream, StreamConstraints]: ...
    
    def get_Size(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StreamMemoryBlockProvider(MemoryBlockProvider, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, stream: Stream, imageStart: LongType, imageSize: IntType, isFileStream: BooleanType, leaveOpen: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Size(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def GetStream(self, constraints: StreamConstraints) -> Tuple[Stream, StreamConstraints]: ...
    
    def get_Size(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Structs ---------- #

class MemoryBlock(ValueType):
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


class MemoryBlock(ValueType):
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


class StreamConstraints(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def GuardOpt(self) -> ObjectType: ...
    
    @property
    def ImageSize(self) -> IntType: ...
    
    @property
    def ImageStart(self) -> LongType: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, guardOpt: ObjectType, startPosition: LongType, imageSize: IntType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StreamConstraints(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def GuardOpt(self) -> ObjectType: ...
    
    @property
    def ImageSize(self) -> IntType: ...
    
    @property
    def ImageStart(self) -> LongType: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, guardOpt: ObjectType, startPosition: LongType, imageSize: IntType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Interfaces

# No Enums

# No Delegates

__all__ = [
    AbstractMemoryBlock,
    ByteArrayMemoryBlock,
    ByteArrayMemoryProvider,
    CriticalDisposableObject,
    ExternalMemoryBlock,
    ExternalMemoryBlockProvider,
    Hash,
    ImmutableMemoryStream,
    LightUpHelper,
    MemoryBlockProvider,
    MemoryMapLightUp,
    MemoryMappedFileBlock,
    NativeHeapMemoryBlock,
    ObjectPool,
    PinnedObject,
    PooledStringBuilder,
    ReadOnlyUnmanagedMemoryStream,
    StreamExtensions,
    StreamMemoryBlockProvider,
    MemoryBlock,
    StreamConstraints,
]
