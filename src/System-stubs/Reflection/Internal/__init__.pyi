"""Automatically generated stubs for C# namespace: System.Reflection.Internal."""

from abc import ABC
from typing import Final
from typing import overload

from System import Array
from System import AsyncCallback
from System import IAsyncResult
from System import IDisposable
from System import Object
from System import Type
from System import ValueType
from System.Collections.Immutable import ImmutableArray
from System.IO import SeekOrigin
from System.IO import Stream
from System.Reflection.Metadata import BlobReader
from System.Runtime.ConstrainedExecution import CriticalFinalizerObject
from System.Runtime.Remoting import ObjRef
from System.Text import StringBuilder
from System.Threading import CancellationToken
from System.Threading.Tasks import Task

class AbstractMemoryBlock(ABC, Object, IDisposable):
    """"""
    @property
    def Pointer(self) -> int:
        """"""
    @property
    def Size(self) -> int:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetReader(self) -> BlobReader:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ByteArrayMemoryBlock(AbstractMemoryBlock, IDisposable):
    """"""
    @property
    def Pointer(self) -> int:
        """"""
    @property
    def Size(self) -> int:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetReader(self) -> BlobReader:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ByteArrayMemoryProvider(MemoryBlockProvider, IDisposable):
    """"""
    def __init__(self, array: ImmutableArray[int]) -> None:
        """"""
    @property
    def Array(self) -> ImmutableArray[int]:
        """"""
    @property
    def Size(self) -> int:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetMemoryBlock(self) -> AbstractMemoryBlock:
        """"""
    @overload
    def GetMemoryBlock(self, start: int, size: int) -> AbstractMemoryBlock:
        """"""
    def GetStream(self, constraints: StreamConstraints) -> tuple[Stream, StreamConstraints]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CriticalDisposableObject(ABC, CriticalFinalizerObject, IDisposable):
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

class ExternalMemoryBlock(AbstractMemoryBlock, IDisposable):
    """"""
    def __init__(self, memoryOwner: object, buffer: int, size: int) -> None:
        """"""
    @property
    def Pointer(self) -> int:
        """"""
    @property
    def Size(self) -> int:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetReader(self) -> BlobReader:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ExternalMemoryBlockProvider(MemoryBlockProvider, IDisposable):
    """"""
    def __init__(self, memory: int, size: int) -> None:
        """"""
    @property
    def Pointer(self) -> int:
        """"""
    @property
    def Size(self) -> int:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetMemoryBlock(self) -> AbstractMemoryBlock:
        """"""
    @overload
    def GetMemoryBlock(self, start: int, size: int) -> AbstractMemoryBlock:
        """"""
    def GetStream(self, constraints: StreamConstraints) -> tuple[Stream, StreamConstraints]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Hash(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ImmutableMemoryStream(Stream, IDisposable):
    """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanSeek(self) -> bool:
        """"""
    @property
    def CanTimeout(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """"""
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """"""
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """"""
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def GetBuffer(self) -> ImmutableArray[int]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Read(self, buffer: Array[int], offset: int, count: int) -> int:
        """"""
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """"""
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """"""
    def ReadByte(self) -> int:
        """"""
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def WriteByte(self, value: int) -> None:
        """"""

class LightUpHelper(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MemoryBlock(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MemoryBlockProvider(ABC, Object, IDisposable):
    """"""
    @property
    def Size(self) -> int:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetMemoryBlock(self) -> AbstractMemoryBlock:
        """"""
    @overload
    def GetMemoryBlock(self, start: int, size: int) -> AbstractMemoryBlock:
        """"""
    def GetStream(self, constraints: StreamConstraints) -> tuple[Stream, StreamConstraints]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MemoryMapLightUp(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MemoryMappedFileBlock(AbstractMemoryBlock, IDisposable):
    """"""
    @property
    def Pointer(self) -> int:
        """"""
    @property
    def Size(self) -> int:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetReader(self) -> BlobReader:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class NativeHeapMemoryBlock(AbstractMemoryBlock, IDisposable):
    """"""
    @property
    def Pointer(self) -> int:
        """"""
    @property
    def Size(self) -> int:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetReader(self) -> BlobReader:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ObjectPool[T](Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class PinnedObject(CriticalDisposableObject, IDisposable):
    """"""
    def __init__(self, obj: object) -> None:
        """"""
    @property
    def Pointer(self) -> int:
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

class PooledStringBuilder(Object):
    """"""

    Builder: Final[StringBuilder]
    """"""
    @property
    def Length(self) -> int:
        """"""
    @classmethod
    def CreatePool(cls) -> ObjectPool[PooledStringBuilder]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Free(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetInstance(cls) -> PooledStringBuilder:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def ToStringAndFree(self) -> str:
        """"""

class ReadOnlyUnmanagedMemoryStream(Stream, IDisposable):
    """"""
    def __init__(self, data: int, length: int) -> None:
        """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanSeek(self) -> bool:
        """"""
    @property
    def CanTimeout(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """"""
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """"""
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """"""
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """"""
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """"""
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Read(self, buffer: Array[int], offset: int, count: int) -> int:
        """"""
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """"""
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """"""
    def ReadByte(self) -> int:
        """"""
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """"""
    def SetLength(self, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """"""
    def WriteByte(self, value: int) -> None:
        """"""

class StreamConstraints(ValueType):
    """"""

    GuardOpt: Final[object]
    """"""
    ImageSize: Final[int]
    """"""
    ImageStart: Final[int]
    """"""
    def __init__(self, guardOpt: object, startPosition: int, imageSize: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class StreamExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class StreamMemoryBlockProvider(MemoryBlockProvider, IDisposable):
    """"""
    def __init__(
        self, stream: Stream, imageStart: int, imageSize: int, isFileStream: bool, leaveOpen: bool
    ) -> None:
        """"""
    @property
    def Size(self) -> int:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetMemoryBlock(self) -> AbstractMemoryBlock:
        """"""
    @overload
    def GetMemoryBlock(self, start: int, size: int) -> AbstractMemoryBlock:
        """"""
    def GetStream(self, constraints: StreamConstraints) -> tuple[Stream, StreamConstraints]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
