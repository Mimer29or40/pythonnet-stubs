from __future__ import annotations

from abc import ABC
from typing import List, Protocol, Tuple, Union, overload

from Microsoft.Win32.SafeHandles import SafeHandleMinusOneIsInvalid
from System import Array, AsyncCallback, Boolean, Byte, Enum, Exception, IAsyncResult, IDisposable, Int32, Int64, IntPtr, Object, String, UInt32, Void
from System.Diagnostics import Switch
from System.IO import IOException, SeekOrigin, Stream
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import ISerializable
from System.Threading import WaitHandle

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
UIntType = Union[int, UInt32]
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class CompressionTracingSwitch(Switch):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Informational() -> BooleanType: ...
    
    @staticmethod
    @property
    def Verbose() -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def get_Informational() -> BooleanType: ...
    
    @staticmethod
    def get_Verbose() -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CopyEncoder(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetBlock(self, input: DeflateInput, output: OutputBuffer, isFinal: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Crc32Helper(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def UpdateCrc32(crc32: UIntType, buffer: ArrayType[ByteType], offset: IntType, length: IntType) -> UIntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DeflateInput(ObjectType):
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


class DeflateStream(Stream, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, stream: Stream, mode: CompressionMode): ...
    
    @overload
    def __init__(self, stream: Stream, mode: CompressionMode, leaveOpen: BooleanType): ...
    
    @overload
    def __init__(self, stream: Stream, compressionLevel: CompressionLevel): ...
    
    @overload
    def __init__(self, stream: Stream, compressionLevel: CompressionLevel, leaveOpen: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BaseStream(self) -> Stream: ...
    
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
    
    def BeginRead(self, array: ArrayType[ByteType], offset: IntType, count: IntType, asyncCallback: AsyncCallback, asyncState: ObjectType) -> IAsyncResult: ...
    
    def BeginWrite(self, array: ArrayType[ByteType], offset: IntType, count: IntType, asyncCallback: AsyncCallback, asyncState: ObjectType) -> IAsyncResult: ...
    
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def Read(self, array: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def Write(self, array: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
    def get_BaseStream(self) -> Stream: ...
    
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


class DeflateStreamAsyncResult(ObjectType, IAsyncResult):
    # ---------- Fields ---------- #
    
    @property
    def buffer(self) -> ArrayType[ByteType]: ...
    
    @buffer.setter
    def buffer(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def count(self) -> IntType: ...
    
    @count.setter
    def count(self, value: IntType) -> None: ...
    
    @property
    def isWrite(self) -> BooleanType: ...
    
    @isWrite.setter
    def isWrite(self, value: BooleanType) -> None: ...
    
    @property
    def offset(self) -> IntType: ...
    
    @offset.setter
    def offset(self, value: IntType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, asyncObject: ObjectType, asyncState: ObjectType, asyncCallback: AsyncCallback, buffer: ArrayType[ByteType], offset: IntType, count: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AsyncState(self) -> ObjectType: ...
    
    @property
    def AsyncWaitHandle(self) -> WaitHandle: ...
    
    @property
    def CompletedSynchronously(self) -> BooleanType: ...
    
    @property
    def IsCompleted(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_AsyncState(self) -> ObjectType: ...
    
    def get_AsyncWaitHandle(self) -> WaitHandle: ...
    
    def get_CompletedSynchronously(self) -> BooleanType: ...
    
    def get_IsCompleted(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DeflaterManaged(ObjectType, IDeflater, IDisposable):
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


class DeflaterZLib(ObjectType, IDeflater, IDisposable):
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


class FastEncoder(ObjectType):
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


class FastEncoderStatics(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def BitReverse(code: UIntType, length: IntType) -> UIntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FastEncoderWindow(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BytesAvailable(self) -> IntType: ...
    
    @property
    def FreeWindowSpace(self) -> IntType: ...
    
    @property
    def UnprocessedInput(self) -> DeflateInput: ...
    
    # ---------- Methods ---------- #
    
    def CopyBytes(self, inputBuffer: ArrayType[ByteType], startIndex: IntType, count: IntType) -> VoidType: ...
    
    def FlushWindow(self) -> VoidType: ...
    
    def MoveWindows(self) -> VoidType: ...
    
    def get_BytesAvailable(self) -> IntType: ...
    
    def get_FreeWindowSpace(self) -> IntType: ...
    
    def get_UnprocessedInput(self) -> DeflateInput: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GZipConstants(ABC, ObjectType):
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


class GZipDecoder(ObjectType, IFileFormatReader):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ReadFooter(self, input: InputBuffer) -> BooleanType: ...
    
    def ReadHeader(self, input: InputBuffer) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def UpdateWithBytesRead(self, buffer: ArrayType[ByteType], offset: IntType, copied: IntType) -> VoidType: ...
    
    def Validate(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GZipFormatter(ObjectType, IFileFormatWriter):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetFooter(self) -> ArrayType[ByteType]: ...
    
    def GetHeader(self) -> ArrayType[ByteType]: ...
    
    def UpdateWithBytesRead(self, buffer: ArrayType[ByteType], offset: IntType, bytesToCopy: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GZipStream(Stream, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, stream: Stream, mode: CompressionMode): ...
    
    @overload
    def __init__(self, stream: Stream, mode: CompressionMode, leaveOpen: BooleanType): ...
    
    @overload
    def __init__(self, stream: Stream, compressionLevel: CompressionLevel): ...
    
    @overload
    def __init__(self, stream: Stream, compressionLevel: CompressionLevel, leaveOpen: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BaseStream(self) -> Stream: ...
    
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
    
    def BeginRead(self, array: ArrayType[ByteType], offset: IntType, count: IntType, asyncCallback: AsyncCallback, asyncState: ObjectType) -> IAsyncResult: ...
    
    def BeginWrite(self, array: ArrayType[ByteType], offset: IntType, count: IntType, asyncCallback: AsyncCallback, asyncState: ObjectType) -> IAsyncResult: ...
    
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def Read(self, array: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def Write(self, array: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
    def get_BaseStream(self) -> Stream: ...
    
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


class HuffmanTree(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, codeLengths: ArrayType[ByteType]): ...
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def StaticDistanceTree() -> HuffmanTree: ...
    
    @staticmethod
    @property
    def StaticLiteralLengthTree() -> HuffmanTree: ...
    
    # ---------- Methods ---------- #
    
    def GetNextSymbol(self, input: InputBuffer) -> IntType: ...
    
    @staticmethod
    def get_StaticDistanceTree() -> HuffmanTree: ...
    
    @staticmethod
    def get_StaticLiteralLengthTree() -> HuffmanTree: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Inflater(ObjectType, IInflater, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AvailableOutput(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def Finished(self) -> BooleanType: ...
    
    def Inflate(self, bytes: ArrayType[ByteType], offset: IntType, length: IntType) -> IntType: ...
    
    def NeedsInput(self) -> BooleanType: ...
    
    def SetInput(self, inputBytes: ArrayType[ByteType], offset: IntType, length: IntType) -> VoidType: ...
    
    def get_AvailableOutput(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InflaterZlib(ObjectType, IInflater, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AvailableOutput(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Finished(self) -> BooleanType: ...
    
    def Inflate(self, bytes: ArrayType[ByteType], offset: IntType, length: IntType) -> IntType: ...
    
    def NeedsInput(self) -> BooleanType: ...
    
    def SetInput(self, inputBuffer: ArrayType[ByteType], startIndex: IntType, count: IntType) -> VoidType: ...
    
    def get_AvailableOutput(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InputBuffer(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AvailableBits(self) -> IntType: ...
    
    @property
    def AvailableBytes(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def CopyTo(self, output: ArrayType[ByteType], offset: IntType, length: IntType) -> IntType: ...
    
    def EnsureBitsAvailable(self, count: IntType) -> BooleanType: ...
    
    def GetBits(self, count: IntType) -> IntType: ...
    
    def NeedsInput(self) -> BooleanType: ...
    
    def SetInput(self, buffer: ArrayType[ByteType], offset: IntType, length: IntType) -> VoidType: ...
    
    def SkipBits(self, n: IntType) -> VoidType: ...
    
    def SkipToByteBoundary(self) -> VoidType: ...
    
    def TryLoad16Bits(self) -> UIntType: ...
    
    def get_AvailableBits(self) -> IntType: ...
    
    def get_AvailableBytes(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Match(ObjectType):
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


class OutputBuffer(ObjectType):
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


class OutputWindow(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AvailableBytes(self) -> IntType: ...
    
    @property
    def FreeBytes(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def CopyFrom(self, input: InputBuffer, length: IntType) -> IntType: ...
    
    def CopyTo(self, output: ArrayType[ByteType], offset: IntType, length: IntType) -> IntType: ...
    
    def Write(self, b: ByteType) -> VoidType: ...
    
    def WriteLengthDistance(self, length: IntType, distance: IntType) -> VoidType: ...
    
    def get_AvailableBytes(self) -> IntType: ...
    
    def get_FreeBytes(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ZLibException(IOException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, message: StringType, zlibErrorContext: StringType, zlibErrorCode: IntType, zlibErrorMessage: StringType): ...
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ZLibContext(self) -> StringType: ...
    
    @property
    def ZLibErrorCode(self) -> IntType: ...
    
    @property
    def ZLibErrorMessage(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_ZLibContext(self) -> StringType: ...
    
    def get_ZLibErrorCode(self) -> IntType: ...
    
    def get_ZLibErrorMessage(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ZLibNative(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Deflate_DefaultMemLevel() -> IntType: ...
    
    @staticmethod
    @property
    def Deflate_DefaultWindowBits() -> IntType: ...
    
    @staticmethod
    @property
    def ZLibNativeDllName() -> StringType: ...
    
    @staticmethod
    @property
    def ZLibVersion() -> StringType: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def CreateZLibStreamForDeflate(zLibStreamHandle: ZLibStreamHandle) -> Tuple[ErrorCode, ZLibStreamHandle]: ...
    
    @staticmethod
    @overload
    def CreateZLibStreamForDeflate(zLibStreamHandle: ZLibStreamHandle, level: CompressionLevel, windowBits: IntType, memLevel: IntType, strategy: CompressionStrategy) -> Tuple[ErrorCode, ZLibStreamHandle]: ...
    
    @staticmethod
    @overload
    def CreateZLibStreamForInflate(zLibStreamHandle: ZLibStreamHandle) -> Tuple[ErrorCode, ZLibStreamHandle]: ...
    
    @staticmethod
    @overload
    def CreateZLibStreamForInflate(zLibStreamHandle: ZLibStreamHandle, windowBits: IntType) -> Tuple[ErrorCode, ZLibStreamHandle]: ...
    
    @staticmethod
    def ZLibCompileFlags() -> IntType: ...
    
    # No Events
    
    
    # ---------- Sub Classes ---------- #
    
    class ZLibStreamHandle(SafeHandleMinusOneIsInvalid, IDisposable):
        # No Fields
        
        # ---------- Constructors ---------- #
        
        def __init__(self): ...
        
        # ---------- Properties ---------- #
        
        @property
        def Adler(self) -> UIntType: ...
        
        @property
        def AvailIn(self) -> UIntType: ...
        
        @AvailIn.setter
        def AvailIn(self, value: UIntType) -> None: ...
        
        @property
        def AvailOut(self) -> UIntType: ...
        
        @AvailOut.setter
        def AvailOut(self, value: UIntType) -> None: ...
        
        @property
        def DataType(self) -> IntType: ...
        
        @property
        def InitializationState(self) -> State: ...
        
        @property
        def NextIn(self) -> NIntType: ...
        
        @NextIn.setter
        def NextIn(self, value: NIntType) -> None: ...
        
        @property
        def NextOut(self) -> NIntType: ...
        
        @NextOut.setter
        def NextOut(self, value: NIntType) -> None: ...
        
        @property
        def TotalIn(self) -> UIntType: ...
        
        @property
        def TotalOut(self) -> UIntType: ...
        
        # ---------- Methods ---------- #
        
        def Deflate(self, flush: FlushCode) -> ErrorCode: ...
        
        def DeflateEnd(self) -> ErrorCode: ...
        
        def DeflateInit2_(self, level: CompressionLevel, windowBits: IntType, memLevel: IntType, strategy: CompressionStrategy) -> ErrorCode: ...
        
        def GetErrorMessage(self) -> StringType: ...
        
        def Inflate(self, flush: FlushCode) -> ErrorCode: ...
        
        def InflateEnd(self) -> ErrorCode: ...
        
        def InflateInit2_(self, windowBits: IntType) -> ErrorCode: ...
        
        def get_Adler(self) -> UIntType: ...
        
        def get_AvailIn(self) -> UIntType: ...
        
        def get_AvailOut(self) -> UIntType: ...
        
        def get_DataType(self) -> IntType: ...
        
        def get_InitializationState(self) -> State: ...
        
        def get_NextIn(self) -> NIntType: ...
        
        def get_NextOut(self) -> NIntType: ...
        
        def get_TotalIn(self) -> UIntType: ...
        
        def get_TotalOut(self) -> UIntType: ...
        
        def set_AvailIn(self, value: UIntType) -> VoidType: ...
        
        def set_AvailOut(self, value: UIntType) -> VoidType: ...
        
        def set_NextIn(self, value: NIntType) -> VoidType: ...
        
        def set_NextOut(self, value: NIntType) -> VoidType: ...
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # ---------- Sub Enums ---------- #
        
        class State(Enum):
            NotInitialized: IntType = 0
            InitializedForDeflate: IntType = 1
            InitializedForInflate: IntType = 2
            Disposed: IntType = 3
        
    
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class FlushCode(Enum):
        NoFlush: IntType = 0
        PartialFlush: IntType = 1
        SyncFlush: IntType = 2
        FullFlush: IntType = 3
        Finish: IntType = 4
        Block: IntType = 5
    
    
    class ErrorCode(Enum):
        VersionError: IntType = -6
        BufError: IntType = -5
        MemError: IntType = -4
        DataError: IntType = -3
        StreamError: IntType = -2
        ErrorNo: IntType = -1
        Ok: IntType = 0
        StreamEnd: IntType = 1
        NeedDictionary: IntType = 2
    
    
    class CompressionLevel(Enum):
        DefaultCompression: IntType = -1
        NoCompression: IntType = 0
        BestSpeed: IntType = 1
        BestCompression: IntType = 9
    
    
    class CompressionStrategy(Enum):
        DefaultStrategy: IntType = 0
        Filtered: IntType = 1
        HuffmanOnly: IntType = 2
        Rle: IntType = 3
        Fixed: IntType = 4
    
    
    class CompressionMethod(Enum):
        Deflated: IntType = 8
    


# No Structs

# ---------- Interfaces ---------- #

class IDeflater(Protocol, IDisposable):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Finish(self, outputBuffer: ArrayType[ByteType], bytesRead: IntType) -> Tuple[BooleanType, IntType]: ...
    
    def GetDeflateOutput(self, outputBuffer: ArrayType[ByteType]) -> IntType: ...
    
    def NeedsInput(self) -> BooleanType: ...
    
    def SetInput(self, inputBuffer: ArrayType[ByteType], startIndex: IntType, count: IntType) -> VoidType: ...
    
    # No Events


class IFileFormatReader(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ReadFooter(self, input: InputBuffer) -> BooleanType: ...
    
    def ReadHeader(self, input: InputBuffer) -> BooleanType: ...
    
    def UpdateWithBytesRead(self, buffer: ArrayType[ByteType], offset: IntType, bytesToCopy: IntType) -> VoidType: ...
    
    def Validate(self) -> VoidType: ...
    
    # No Events


class IFileFormatWriter(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetFooter(self) -> ArrayType[ByteType]: ...
    
    def GetHeader(self) -> ArrayType[ByteType]: ...
    
    def UpdateWithBytesRead(self, buffer: ArrayType[ByteType], offset: IntType, bytesToCopy: IntType) -> VoidType: ...
    
    # No Events


class IInflater(Protocol, IDisposable):
    # ---------- Properties ---------- #
    
    @property
    def AvailableOutput(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Finished(self) -> BooleanType: ...
    
    def Inflate(self, bytes: ArrayType[ByteType], offset: IntType, length: IntType) -> IntType: ...
    
    def NeedsInput(self) -> BooleanType: ...
    
    def SetInput(self, inputBytes: ArrayType[ByteType], offset: IntType, length: IntType) -> VoidType: ...
    
    def get_AvailableOutput(self) -> IntType: ...
    
    # No Events


# ---------- Enums ---------- #

class BlockType(Enum):
    Uncompressed: IntType = 0
    Static: IntType = 1
    Dynamic: IntType = 2


class CompressionLevel(Enum):
    Optimal: IntType = 0
    Fastest: IntType = 1
    NoCompression: IntType = 2


class CompressionMode(Enum):
    Decompress: IntType = 0
    Compress: IntType = 1


class CompressionTracingSwitchLevel(Enum):
    Off: IntType = 0
    Informational: IntType = 1
    Verbose: IntType = 2


class InflaterState(Enum):
    ReadingHeader: IntType = 0
    ReadingBFinal: IntType = 2
    ReadingBType: IntType = 3
    ReadingNumLitCodes: IntType = 4
    ReadingNumDistCodes: IntType = 5
    ReadingNumCodeLengthCodes: IntType = 6
    ReadingCodeLengthCodes: IntType = 7
    ReadingTreeCodesBefore: IntType = 8
    ReadingTreeCodesAfter: IntType = 9
    DecodeTop: IntType = 10
    HaveInitialLength: IntType = 11
    HaveFullLength: IntType = 12
    HaveDistCode: IntType = 13
    UncompressedAligning: IntType = 15
    UncompressedByte1: IntType = 16
    UncompressedByte2: IntType = 17
    UncompressedByte3: IntType = 18
    UncompressedByte4: IntType = 19
    DecodingUncompressed: IntType = 20
    StartReadingFooter: IntType = 21
    ReadingFooter: IntType = 22
    VerifyingFooter: IntType = 23
    Done: IntType = 24


# No Delegates

__all__ = [
    CompressionTracingSwitch,
    CopyEncoder,
    Crc32Helper,
    DeflateInput,
    DeflateStream,
    DeflateStreamAsyncResult,
    DeflaterManaged,
    DeflaterZLib,
    FastEncoder,
    FastEncoderStatics,
    FastEncoderWindow,
    GZipConstants,
    GZipDecoder,
    GZipFormatter,
    GZipStream,
    HuffmanTree,
    Inflater,
    InflaterZlib,
    InputBuffer,
    Match,
    OutputBuffer,
    OutputWindow,
    ZLibException,
    ZLibNative,
    IDeflater,
    IFileFormatReader,
    IFileFormatWriter,
    IInflater,
    BlockType,
    CompressionLevel,
    CompressionMode,
    CompressionTracingSwitchLevel,
    InflaterState,
]
