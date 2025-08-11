"""Automatically generated stubs for C# namespace: System.IO.Compression."""

from abc import ABC
from typing import ClassVar
from typing import Final
from typing import overload

from Microsoft.Win32.SafeHandles import SafeHandleMinusOneIsInvalid
from System import Array
from System import AsyncCallback
from System import Boolean
from System import Enum
from System import Exception
from System import IAsyncResult
from System import IDisposable
from System import Int32
from System import IntPtr
from System import Object
from System import Type
from System.Collections import IDictionary
from System.Collections.Specialized import StringDictionary
from System.Diagnostics import Switch
from System.IO import IOException
from System.IO import SeekOrigin
from System.IO import Stream
from System.Reflection import MethodBase
from System.Runtime.InteropServices import _Exception
from System.Runtime.Remoting import ObjRef
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Threading import CancellationToken
from System.Threading import WaitHandle
from System.Threading.Tasks import Task

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class BlockType(Enum):
    """"""

    Uncompressed: BlockType = ...
    """"""
    Static: BlockType = ...
    """"""
    Dynamic: BlockType = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CompressionLevel(Enum):
    """"""

    Optimal: CompressionLevel = ...
    """"""
    Fastest: CompressionLevel = ...
    """"""
    NoCompression: CompressionLevel = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CompressionMode(Enum):
    """"""

    Decompress: CompressionMode = ...
    """"""
    Compress: CompressionMode = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CompressionTracingSwitch(Switch):
    """"""
    @property
    def Attributes(self) -> StringDictionary:
        """"""
    @property
    def Description(self) -> str:
        """"""
    @property
    def DisplayName(self) -> str:
        """"""
    @classmethod
    @property
    def Informational(cls) -> bool:
        """"""
    @classmethod
    @property
    def Verbose(cls) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CompressionTracingSwitchLevel(Enum):
    """"""

    Off: CompressionTracingSwitchLevel = ...
    """"""
    Informational: CompressionTracingSwitchLevel = ...
    """"""
    Verbose: CompressionTracingSwitchLevel = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CopyEncoder(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBlock(self, input: DeflateInput, output: OutputBuffer, isFinal: bool) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Crc32Helper(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def UpdateCrc32(cls, crc32: int, buffer: Array[int], offset: int, length: int) -> int:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DeflateInput(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DeflateStream(Stream, IDisposable):
    """"""
    @overload
    def __init__(self, stream: Stream, mode: CompressionMode) -> None:
        """"""
    @overload
    def __init__(self, stream: Stream, mode: CompressionMode, leaveOpen: bool) -> None:
        """"""
    @overload
    def __init__(self, stream: Stream, compressionLevel: CompressionLevel) -> None:
        """"""
    @overload
    def __init__(self, stream: Stream, compressionLevel: CompressionLevel, leaveOpen: bool) -> None:
        """"""
    @property
    def BaseStream(self) -> Stream:
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
        self,
        array: Array[int],
        offset: int,
        count: int,
        asyncCallback: AsyncCallback,
        asyncState: object,
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self,
        array: Array[int],
        offset: int,
        count: int,
        asyncCallback: AsyncCallback,
        asyncState: object,
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
    def Read(self, array: Array[int], offset: int, count: int) -> int:
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
    def Write(self, array: Array[int], offset: int, count: int) -> None:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DeflateStreamAsyncResult(Object, IAsyncResult):
    """"""

    buffer: Final[Array[int]]
    """"""
    count: Final[int]
    """"""
    isWrite: Final[bool]
    """"""
    offset: Final[int]
    """"""
    def __init__(
        self,
        asyncObject: object,
        asyncState: object,
        asyncCallback: AsyncCallback,
        buffer: Array[int],
        offset: int,
        count: int,
    ) -> None:
        """"""
    @property
    def AsyncState(self) -> object:
        """"""
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """"""
    @property
    def CompletedSynchronously(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DeflaterManaged(Object, IDeflater, IDisposable):
    """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Finish(self, outputBuffer: Array[int], bytesRead: Int32) -> tuple[bool, Int32]:
        """"""
    def GetDeflateOutput(self, outputBuffer: Array[int]) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def NeedsInput(self) -> bool:
        """"""
    def SetInput(self, inputBuffer: Array[int], startIndex: int, count: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DeflaterZLib(Object, IDeflater, IDisposable):
    """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Finish(self, outputBuffer: Array[int], bytesRead: Int32) -> tuple[bool, Int32]:
        """"""
    def GetDeflateOutput(self, outputBuffer: Array[int]) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def NeedsInput(self) -> bool:
        """"""
    def SetInput(self, inputBuffer: Array[int], startIndex: int, count: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class FastEncoder(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class FastEncoderStatics(ABC, Object):
    """"""
    @classmethod
    def BitReverse(cls, code: int, length: int) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class FastEncoderWindow(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def BytesAvailable(self) -> int:
        """"""
    @property
    def FreeWindowSpace(self) -> int:
        """"""
    @property
    def UnprocessedInput(self) -> DeflateInput:
        """"""
    def CopyBytes(self, inputBuffer: Array[int], startIndex: int, count: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FlushWindow(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MoveWindows(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class GZipConstants(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class GZipDecoder(Object, IFileFormatReader):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ReadFooter(self, input: InputBuffer) -> bool:
        """"""
    def ReadHeader(self, input: InputBuffer) -> bool:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def UpdateWithBytesRead(self, buffer: Array[int], offset: int, copied: int) -> None:
        """"""
    def Validate(self) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class GZipFormatter(Object, IFileFormatWriter):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetFooter(self) -> Array[int]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetHeader(self) -> Array[int]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def UpdateWithBytesRead(self, buffer: Array[int], offset: int, bytesToCopy: int) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class GZipStream(Stream, IDisposable):
    """"""
    @overload
    def __init__(self, stream: Stream, mode: CompressionMode) -> None:
        """"""
    @overload
    def __init__(self, stream: Stream, mode: CompressionMode, leaveOpen: bool) -> None:
        """"""
    @overload
    def __init__(self, stream: Stream, compressionLevel: CompressionLevel) -> None:
        """"""
    @overload
    def __init__(self, stream: Stream, compressionLevel: CompressionLevel, leaveOpen: bool) -> None:
        """"""
    @property
    def BaseStream(self) -> Stream:
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
        self,
        array: Array[int],
        offset: int,
        count: int,
        asyncCallback: AsyncCallback,
        asyncState: object,
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self,
        array: Array[int],
        offset: int,
        count: int,
        asyncCallback: AsyncCallback,
        asyncState: object,
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
    def Read(self, array: Array[int], offset: int, count: int) -> int:
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
    def Write(self, array: Array[int], offset: int, count: int) -> None:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class HuffmanTree(Object):
    """"""
    def __init__(self, codeLengths: Array[int]) -> None:
        """"""
    @classmethod
    @property
    def StaticDistanceTree(cls) -> HuffmanTree:
        """"""
    @classmethod
    @property
    def StaticLiteralLengthTree(cls) -> HuffmanTree:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetNextSymbol(self, input: InputBuffer) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IDeflater(ABC, IDisposable):
    """"""
    def Dispose(self) -> None:
        """"""
    def Finish(self, outputBuffer: Array[int], bytesRead: Int32) -> tuple[bool, Int32]:
        """"""
    def GetDeflateOutput(self, outputBuffer: Array[int]) -> int:
        """"""
    def NeedsInput(self) -> bool:
        """"""
    def SetInput(self, inputBuffer: Array[int], startIndex: int, count: int) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IFileFormatReader(ABC):
    """"""
    def ReadFooter(self, input: InputBuffer) -> bool:
        """"""
    def ReadHeader(self, input: InputBuffer) -> bool:
        """"""
    def UpdateWithBytesRead(self, buffer: Array[int], offset: int, bytesToCopy: int) -> None:
        """"""
    def Validate(self) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IFileFormatWriter(ABC):
    """"""
    def GetFooter(self) -> Array[int]:
        """"""
    def GetHeader(self) -> Array[int]:
        """"""
    def UpdateWithBytesRead(self, buffer: Array[int], offset: int, bytesToCopy: int) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IInflater(ABC, IDisposable):
    """"""
    @property
    def AvailableOutput(self) -> int:
        """"""
    def Dispose(self) -> None:
        """"""
    def Finished(self) -> bool:
        """"""
    def Inflate(self, bytes: Array[int], offset: int, length: int) -> int:
        """"""
    def NeedsInput(self) -> bool:
        """"""
    def SetInput(self, inputBytes: Array[int], offset: int, length: int) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Inflater(Object, IInflater, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AvailableOutput(self) -> int:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Finished(self) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Inflate(self, bytes: Array[int], offset: int, length: int) -> int:
        """"""
    def NeedsInput(self) -> bool:
        """"""
    def SetInput(self, inputBytes: Array[int], offset: int, length: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class InflaterState(Enum):
    """"""

    ReadingHeader: InflaterState = ...
    """"""
    ReadingBFinal: InflaterState = ...
    """"""
    ReadingBType: InflaterState = ...
    """"""
    ReadingNumLitCodes: InflaterState = ...
    """"""
    ReadingNumDistCodes: InflaterState = ...
    """"""
    ReadingNumCodeLengthCodes: InflaterState = ...
    """"""
    ReadingCodeLengthCodes: InflaterState = ...
    """"""
    ReadingTreeCodesBefore: InflaterState = ...
    """"""
    ReadingTreeCodesAfter: InflaterState = ...
    """"""
    DecodeTop: InflaterState = ...
    """"""
    HaveInitialLength: InflaterState = ...
    """"""
    HaveFullLength: InflaterState = ...
    """"""
    HaveDistCode: InflaterState = ...
    """"""
    UncompressedAligning: InflaterState = ...
    """"""
    UncompressedByte1: InflaterState = ...
    """"""
    UncompressedByte2: InflaterState = ...
    """"""
    UncompressedByte3: InflaterState = ...
    """"""
    UncompressedByte4: InflaterState = ...
    """"""
    DecodingUncompressed: InflaterState = ...
    """"""
    StartReadingFooter: InflaterState = ...
    """"""
    ReadingFooter: InflaterState = ...
    """"""
    VerifyingFooter: InflaterState = ...
    """"""
    Done: InflaterState = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class InflaterZlib(Object, IInflater, IDisposable):
    """"""
    @property
    def AvailableOutput(self) -> int:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Finished(self) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Inflate(self, bytes: Array[int], offset: int, length: int) -> int:
        """"""
    def NeedsInput(self) -> bool:
        """"""
    def SetInput(self, inputBuffer: Array[int], startIndex: int, count: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class InputBuffer(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AvailableBits(self) -> int:
        """"""
    @property
    def AvailableBytes(self) -> int:
        """"""
    def CopyTo(self, output: Array[int], offset: int, length: int) -> int:
        """"""
    def EnsureBitsAvailable(self, count: int) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBits(self, count: int) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def NeedsInput(self) -> bool:
        """"""
    def SetInput(self, buffer: Array[int], offset: int, length: int) -> None:
        """"""
    def SkipBits(self, n: int) -> None:
        """"""
    def SkipToByteBoundary(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TryLoad16Bits(self) -> int:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Match(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class OutputBuffer(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class OutputWindow(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AvailableBytes(self) -> int:
        """"""
    @property
    def FreeBytes(self) -> int:
        """"""
    def CopyFrom(self, input: InputBuffer, length: int) -> int:
        """"""
    def CopyTo(self, output: Array[int], offset: int, length: int) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def Write(self, b: int) -> None:
        """"""
    def WriteLengthDistance(self, length: int, distance: int) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ZLibException(IOException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(
        self, message: str, zlibErrorContext: str, zlibErrorCode: int, zlibErrorMessage: str
    ) -> None:
        """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, inner: Exception) -> None:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def HResult(self) -> int:
        """"""
    @property
    def HelpLink(self) -> str:
        """"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """"""
    @property
    def Message(self) -> str:
        """"""
    @property
    def Source(self) -> str:
        """"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """"""
    @property
    def TargetSite(self) -> MethodBase:
        """"""
    @property
    def ZLibContext(self) -> str:
        """"""
    @property
    def ZLibErrorCode(self) -> int:
        """"""
    @property
    def ZLibErrorMessage(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseException(self) -> Exception:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ZLibNative(ABC, Object):
    """"""

    Deflate_DefaultMemLevel: ClassVar[int]
    """"""
    Deflate_DefaultWindowBits: ClassVar[int]
    """"""
    ZLibNativeDllName: ClassVar[str]
    """"""
    ZLibVersion: ClassVar[str]
    """"""
    @classmethod
    @overload
    def CreateZLibStreamForDeflate(
        cls, zLibStreamHandle: ZLibStreamHandle
    ) -> tuple[ZLibNative.ErrorCode, ZLibStreamHandle]:
        """"""
    @classmethod
    @overload
    def CreateZLibStreamForDeflate(
        cls,
        zLibStreamHandle: ZLibStreamHandle,
        level: ZLibNative.CompressionLevel,
        windowBits: int,
        memLevel: int,
        strategy: ZLibNative.CompressionStrategy,
    ) -> tuple[ZLibNative.ErrorCode, ZLibStreamHandle]:
        """"""
    @classmethod
    @overload
    def CreateZLibStreamForInflate(
        cls, zLibStreamHandle: ZLibStreamHandle
    ) -> tuple[ZLibNative.ErrorCode, ZLibStreamHandle]:
        """"""
    @classmethod
    @overload
    def CreateZLibStreamForInflate(
        cls, zLibStreamHandle: ZLibStreamHandle, windowBits: int
    ) -> tuple[ZLibNative.ErrorCode, ZLibStreamHandle]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def ZLibCompileFlags(cls) -> int:
        """"""
    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class CompressionLevel(Enum):
        """"""

        NoCompression: ZLibNative.CompressionLevel = ...
        """"""
        BestSpeed: ZLibNative.CompressionLevel = ...
        """"""
        BestCompression: ZLibNative.CompressionLevel = ...
        """"""
        DefaultCompression: ZLibNative.CompressionLevel = ...
        """"""

    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class CompressionMethod(Enum):
        """"""

        Deflated: ZLibNative.CompressionMethod = ...
        """"""

    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class CompressionStrategy(Enum):
        """"""

        DefaultStrategy: ZLibNative.CompressionStrategy = ...
        """"""
        Filtered: ZLibNative.CompressionStrategy = ...
        """"""
        HuffmanOnly: ZLibNative.CompressionStrategy = ...
        """"""
        Rle: ZLibNative.CompressionStrategy = ...
        """"""
        Fixed: ZLibNative.CompressionStrategy = ...
        """"""

    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class ErrorCode(Enum):
        """"""

        Ok: ZLibNative.ErrorCode = ...
        """"""
        StreamEnd: ZLibNative.ErrorCode = ...
        """"""
        NeedDictionary: ZLibNative.ErrorCode = ...
        """"""
        VersionError: ZLibNative.ErrorCode = ...
        """"""
        BufError: ZLibNative.ErrorCode = ...
        """"""
        MemError: ZLibNative.ErrorCode = ...
        """"""
        DataError: ZLibNative.ErrorCode = ...
        """"""
        StreamError: ZLibNative.ErrorCode = ...
        """"""
        ErrorNo: ZLibNative.ErrorCode = ...
        """"""

    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class FlushCode(Enum):
        """"""

        NoFlush: ZLibNative.FlushCode = ...
        """"""
        PartialFlush: ZLibNative.FlushCode = ...
        """"""
        SyncFlush: ZLibNative.FlushCode = ...
        """"""
        FullFlush: ZLibNative.FlushCode = ...
        """"""
        Finish: ZLibNative.FlushCode = ...
        """"""
        Block: ZLibNative.FlushCode = ...
        """"""

    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class ZLibStreamHandle(SafeHandleMinusOneIsInvalid, IDisposable):
        """"""
        def __init__(self) -> None:
            """"""
        @property
        def Adler(self) -> int:
            """"""
        @property
        def AvailIn(self) -> int:
            """"""
        @AvailIn.setter
        def AvailIn(self, value: int) -> None: ...
        @property
        def AvailOut(self) -> int:
            """"""
        @AvailOut.setter
        def AvailOut(self, value: int) -> None: ...
        @property
        def DataType(self) -> int:
            """"""
        @property
        def InitializationState(self) -> ZLibNative.ZLibStreamHandle.State:
            """"""
        @property
        def IsClosed(self) -> bool:
            """"""
        @property
        def IsInvalid(self) -> bool:
            """"""
        @property
        def NextIn(self) -> IntPtr:
            """"""
        @NextIn.setter
        def NextIn(self, value: IntPtr) -> None: ...
        @property
        def NextOut(self) -> IntPtr:
            """"""
        @NextOut.setter
        def NextOut(self, value: IntPtr) -> None: ...
        @property
        def TotalIn(self) -> int:
            """"""
        @property
        def TotalOut(self) -> int:
            """"""
        def Close(self) -> None:
            """"""
        def DangerousAddRef(self, success: Boolean) -> None:
            """"""
        def DangerousGetHandle(self) -> IntPtr:
            """"""
        def DangerousRelease(self) -> None:
            """"""
        def Deflate(self, flush: ZLibNative.FlushCode) -> ZLibNative.ErrorCode:
            """"""
        def DeflateEnd(self) -> ZLibNative.ErrorCode:
            """"""
        def DeflateInit2_(
            self,
            level: ZLibNative.CompressionLevel,
            windowBits: int,
            memLevel: int,
            strategy: ZLibNative.CompressionStrategy,
        ) -> ZLibNative.ErrorCode:
            """"""
        def Dispose(self) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetErrorMessage(self) -> str:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def Inflate(self, flush: ZLibNative.FlushCode) -> ZLibNative.ErrorCode:
            """"""
        def InflateEnd(self) -> ZLibNative.ErrorCode:
            """"""
        def InflateInit2_(self, windowBits: int) -> ZLibNative.ErrorCode:
            """"""
        def SetHandleAsInvalid(self) -> None:
            """"""
        def ToString(self) -> str:
            """"""
        # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
        class State(Enum):
            """"""

            NotInitialized: ZLibNative.ZLibStreamHandle.State = ...
            """"""
            InitializedForDeflate: ZLibNative.ZLibStreamHandle.State = ...
            """"""
            InitializedForInflate: ZLibNative.ZLibStreamHandle.State = ...
            """"""
            Disposed: ZLibNative.ZLibStreamHandle.State = ...
            """"""
