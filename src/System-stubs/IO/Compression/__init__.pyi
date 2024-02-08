from __future__ import annotations

from abc import ABC
from typing import ClassVar
from typing import Final
from typing import Tuple
from typing import overload

from Microsoft.Win32.SafeHandles import SafeHandleMinusOneIsInvalid
from System import Array
from System import AsyncCallback
from System import Enum
from System import Exception
from System import IAsyncResult
from System import IDisposable
from System import IntPtr
from System import Object
from System import Type
from System.Collections import IDictionary
from System.Collections.Specialized import StringDictionary
from System.Diagnostics import Switch
from System.IO import IOException
from System.IO import SeekOrigin
from System.IO import Stream
from System.IO.Compression.ZLibNative import CompressionLevel
from System.IO.Compression.ZLibNative import CompressionStrategy
from System.IO.Compression.ZLibNative import ErrorCode
from System.IO.Compression.ZLibNative import FlushCode
from System.IO.Compression.ZLibNative.ZLibStreamHandle import State
from System.Reflection import MethodBase
from System.Runtime.InteropServices import _Exception
from System.Runtime.Remoting import ObjRef
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Threading import CancellationToken
from System.Threading import WaitHandle
from System.Threading.Tasks import Task

class BlockType(Enum):
    """"""

    Uncompressed: BlockType = ...
    """"""
    Static: BlockType = ...
    """"""
    Dynamic: BlockType = ...
    """"""

class CompressionLevel(Enum):
    """"""

    Optimal: CompressionLevel = ...
    """"""
    Fastest: CompressionLevel = ...
    """"""
    NoCompression: CompressionLevel = ...
    """"""

class CompressionMode(Enum):
    """"""

    Decompress: CompressionMode = ...
    """"""
    Compress: CompressionMode = ...
    """"""

class CompressionTracingSwitch(Switch):
    """"""

    @property
    def Attributes(self) -> StringDictionary:
        """

        :return:
        """
    @property
    def Description(self) -> str:
        """

        :return:
        """
    @property
    def DisplayName(self) -> str:
        """

        :return:
        """
    @classmethod
    @property
    def Informational(cls) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def Verbose(cls) -> bool:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CompressionTracingSwitchLevel(Enum):
    """"""

    Off: CompressionTracingSwitchLevel = ...
    """"""
    Informational: CompressionTracingSwitchLevel = ...
    """"""
    Verbose: CompressionTracingSwitchLevel = ...
    """"""

class CopyEncoder(Object):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetBlock(self, input: DeflateInput, output: OutputBuffer, isFinal: bool) -> None:
        """

        :param input:
        :param output:
        :param isFinal:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class Crc32Helper(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    def UpdateCrc32(cls, crc32: int, buffer: Array[int], offset: int, length: int) -> int:
        """

        :param crc32:
        :param buffer:
        :param offset:
        :param length:
        :return:
        """

class DeflateInput(Object):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DeflateStream(Stream, IDisposable):
    """"""

    @overload
    def __init__(self, stream: Stream, compressionLevel: CompressionLevel):
        """

        :param stream:
        :param compressionLevel:
        """
    @overload
    def __init__(self, stream: Stream, mode: CompressionMode):
        """

        :param stream:
        :param mode:
        """
    @overload
    def __init__(self, stream: Stream, compressionLevel: CompressionLevel, leaveOpen: bool):
        """

        :param stream:
        :param compressionLevel:
        :param leaveOpen:
        """
    @overload
    def __init__(self, stream: Stream, mode: CompressionMode, leaveOpen: bool):
        """

        :param stream:
        :param mode:
        :param leaveOpen:
        """
    @property
    def BaseStream(self) -> Stream:
        """

        :return:
        """
    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """

class DeflateStreamAsyncResult(Object, IAsyncResult):
    """"""

    buffer: Final[Array[int]] = ...
    """
    
    :return: 
    """
    count: Final[int] = ...
    """
    
    :return: 
    """
    isWrite: Final[bool] = ...
    """
    
    :return: 
    """
    offset: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(
        self,
        asyncObject: object,
        asyncState: object,
        asyncCallback: AsyncCallback,
        buffer: Array[int],
        offset: int,
        count: int,
    ):
        """

        :param asyncObject:
        :param asyncState:
        :param asyncCallback:
        :param buffer:
        :param offset:
        :param count:
        """
    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DeflaterManaged(Object, IDeflater, IDisposable):
    """"""

    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Finish(self, outputBuffer: Array[int], bytesRead: int) -> Tuple[bool, int]:
        """

        :param outputBuffer:
        :param bytesRead:
        :return:
        """
    def GetDeflateOutput(self, outputBuffer: Array[int]) -> int:
        """

        :param outputBuffer:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def NeedsInput(self) -> bool:
        """

        :return:
        """
    def SetInput(self, inputBuffer: Array[int], startIndex: int, count: int) -> None:
        """

        :param inputBuffer:
        :param startIndex:
        :param count:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DeflaterZLib(Object, IDeflater, IDisposable):
    """"""

    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Finish(self, outputBuffer: Array[int], bytesRead: int) -> Tuple[bool, int]:
        """

        :param outputBuffer:
        :param bytesRead:
        :return:
        """
    def GetDeflateOutput(self, outputBuffer: Array[int]) -> int:
        """

        :param outputBuffer:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def NeedsInput(self) -> bool:
        """

        :return:
        """
    def SetInput(self, inputBuffer: Array[int], startIndex: int, count: int) -> None:
        """

        :param inputBuffer:
        :param startIndex:
        :param count:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class FastEncoder(Object):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class FastEncoderStatics(ABC, Object):
    """"""

    @classmethod
    def BitReverse(cls, code: int, length: int) -> int:
        """

        :param code:
        :param length:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class FastEncoderWindow(Object):
    """"""

    def __init__(self):
        """"""
    @property
    def BytesAvailable(self) -> int:
        """

        :return:
        """
    @property
    def FreeWindowSpace(self) -> int:
        """

        :return:
        """
    @property
    def UnprocessedInput(self) -> DeflateInput:
        """

        :return:
        """
    def CopyBytes(self, inputBuffer: Array[int], startIndex: int, count: int) -> None:
        """

        :param inputBuffer:
        :param startIndex:
        :param count:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FlushWindow(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def MoveWindows(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class GZipConstants(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class GZipDecoder(Object, IFileFormatReader):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ReadFooter(self, input: InputBuffer) -> bool:
        """

        :param input:
        :return:
        """
    def ReadHeader(self, input: InputBuffer) -> bool:
        """

        :param input:
        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def UpdateWithBytesRead(self, buffer: Array[int], offset: int, bytesToCopy: int) -> None:
        """

        :param buffer:
        :param offset:
        :param bytesToCopy:
        """
    def Validate(self) -> None:
        """"""

class GZipFormatter(Object, IFileFormatWriter):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetFooter(self) -> Array[int]:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetHeader(self) -> Array[int]:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def UpdateWithBytesRead(self, buffer: Array[int], offset: int, bytesToCopy: int) -> None:
        """

        :param buffer:
        :param offset:
        :param bytesToCopy:
        """

class GZipStream(Stream, IDisposable):
    """"""

    @overload
    def __init__(self, stream: Stream, compressionLevel: CompressionLevel):
        """

        :param stream:
        :param compressionLevel:
        """
    @overload
    def __init__(self, stream: Stream, mode: CompressionMode):
        """

        :param stream:
        :param mode:
        """
    @overload
    def __init__(self, stream: Stream, compressionLevel: CompressionLevel, leaveOpen: bool):
        """

        :param stream:
        :param compressionLevel:
        :param leaveOpen:
        """
    @overload
    def __init__(self, stream: Stream, mode: CompressionMode, leaveOpen: bool):
        """

        :param stream:
        :param mode:
        :param leaveOpen:
        """
    @property
    def BaseStream(self) -> Stream:
        """

        :return:
        """
    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """

class HuffmanTree(Object):
    """"""

    def __init__(self, codeLengths: Array[int]):
        """

        :param codeLengths:
        """
    @classmethod
    @property
    def StaticDistanceTree(cls) -> HuffmanTree:
        """

        :return:
        """
    @classmethod
    @property
    def StaticLiteralLengthTree(cls) -> HuffmanTree:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetNextSymbol(self, input: InputBuffer) -> int:
        """

        :param input:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class IDeflater(IDisposable):
    """"""

    def Dispose(self) -> None:
        """"""
    def Finish(self, outputBuffer: Array[int], bytesRead: int) -> Tuple[bool, int]:
        """

        :param outputBuffer:
        :param bytesRead:
        :return:
        """
    def GetDeflateOutput(self, outputBuffer: Array[int]) -> int:
        """

        :param outputBuffer:
        :return:
        """
    def NeedsInput(self) -> bool:
        """

        :return:
        """
    def SetInput(self, inputBuffer: Array[int], startIndex: int, count: int) -> None:
        """

        :param inputBuffer:
        :param startIndex:
        :param count:
        """

class IFileFormatReader:
    """"""

    def ReadFooter(self, input: InputBuffer) -> bool:
        """

        :param input:
        :return:
        """
    def ReadHeader(self, input: InputBuffer) -> bool:
        """

        :param input:
        :return:
        """
    def UpdateWithBytesRead(self, buffer: Array[int], offset: int, bytesToCopy: int) -> None:
        """

        :param buffer:
        :param offset:
        :param bytesToCopy:
        """
    def Validate(self) -> None:
        """"""

class IFileFormatWriter:
    """"""

    def GetFooter(self) -> Array[int]:
        """

        :return:
        """
    def GetHeader(self) -> Array[int]:
        """

        :return:
        """
    def UpdateWithBytesRead(self, buffer: Array[int], offset: int, bytesToCopy: int) -> None:
        """

        :param buffer:
        :param offset:
        :param bytesToCopy:
        """

class IInflater(IDisposable):
    """"""

    @property
    def AvailableOutput(self) -> int:
        """

        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Finished(self) -> bool:
        """

        :return:
        """
    def Inflate(self, bytes: Array[int], offset: int, length: int) -> int:
        """

        :param bytes:
        :param offset:
        :param length:
        :return:
        """
    def NeedsInput(self) -> bool:
        """

        :return:
        """
    def SetInput(self, inputBytes: Array[int], offset: int, length: int) -> None:
        """

        :param inputBytes:
        :param offset:
        :param length:
        """

class Inflater(Object, IInflater, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def AvailableOutput(self) -> int:
        """

        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Finished(self) -> bool:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Inflate(self, bytes: Array[int], offset: int, length: int) -> int:
        """

        :param bytes:
        :param offset:
        :param length:
        :return:
        """
    def NeedsInput(self) -> bool:
        """

        :return:
        """
    def SetInput(self, inputBytes: Array[int], offset: int, length: int) -> None:
        """

        :param inputBytes:
        :param offset:
        :param length:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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

class InflaterZlib(Object, IInflater, IDisposable):
    """"""

    @property
    def AvailableOutput(self) -> int:
        """

        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Finished(self) -> bool:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Inflate(self, bytes: Array[int], offset: int, length: int) -> int:
        """

        :param bytes:
        :param offset:
        :param length:
        :return:
        """
    def NeedsInput(self) -> bool:
        """

        :return:
        """
    def SetInput(self, inputBytes: Array[int], offset: int, length: int) -> None:
        """

        :param inputBytes:
        :param offset:
        :param length:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class InputBuffer(Object):
    """"""

    def __init__(self):
        """"""
    @property
    def AvailableBits(self) -> int:
        """

        :return:
        """
    @property
    def AvailableBytes(self) -> int:
        """

        :return:
        """
    def CopyTo(self, output: Array[int], offset: int, length: int) -> int:
        """

        :param output:
        :param offset:
        :param length:
        :return:
        """
    def EnsureBitsAvailable(self, count: int) -> bool:
        """

        :param count:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetBits(self, count: int) -> int:
        """

        :param count:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def NeedsInput(self) -> bool:
        """

        :return:
        """
    def SetInput(self, buffer: Array[int], offset: int, length: int) -> None:
        """

        :param buffer:
        :param offset:
        :param length:
        """
    def SkipBits(self, n: int) -> None:
        """

        :param n:
        """
    def SkipToByteBoundary(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TryLoad16Bits(self) -> int:
        """

        :return:
        """

class Match(Object):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class OutputBuffer(Object):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class OutputWindow(Object):
    """"""

    def __init__(self):
        """"""
    @property
    def AvailableBytes(self) -> int:
        """

        :return:
        """
    @property
    def FreeBytes(self) -> int:
        """

        :return:
        """
    def CopyFrom(self, input: InputBuffer, length: int) -> int:
        """

        :param input:
        :param length:
        :return:
        """
    def CopyTo(self, output: Array[int], offset: int, length: int) -> int:
        """

        :param output:
        :param offset:
        :param length:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, b: int) -> None:
        """

        :param b:
        """
    def WriteLengthDistance(self, length: int, distance: int) -> None:
        """

        :param length:
        :param distance:
        """

class ZLibException(IOException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """

        :param message:
        """
    @overload
    def __init__(self, message: str, inner: Exception):
        """

        :param message:
        :param inner:
        """
    @overload
    def __init__(
        self, message: str, zlibErrorContext: str, zlibErrorCode: int, zlibErrorMessage: str
    ):
        """

        :param message:
        :param zlibErrorContext:
        :param zlibErrorCode:
        :param zlibErrorMessage:
        """
    @property
    def Data(self) -> IDictionary:
        """

        :return:
        """
    @property
    def HResult(self) -> int:
        """

        :return:
        """
    @property
    def HelpLink(self) -> str:
        """

        :return:
        """
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """

        :return:
        """
    @property
    def Message(self) -> str:
        """

        :return:
        """
    @property
    def Source(self) -> str:
        """

        :return:
        """
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """

        :return:
        """
    @property
    def TargetSite(self) -> MethodBase:
        """

        :return:
        """
    @property
    def ZLibContext(self) -> str:
        """

        :return:
        """
    @property
    def ZLibErrorCode(self) -> int:
        """

        :return:
        """
    @property
    def ZLibErrorMessage(self) -> str:
        """

        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class ZLibNative(ABC, Object):
    """"""

    Deflate_DefaultMemLevel: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    Deflate_DefaultWindowBits: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    ZLibNativeDllName: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    ZLibVersion: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    @classmethod
    @overload
    def CreateZLibStreamForDeflate(
        cls, zLibStreamHandle: ZLibStreamHandle
    ) -> Tuple[ZLibNative.ErrorCode, ZLibStreamHandle]:
        """

        :param zLibStreamHandle:
        :return:
        """
    @classmethod
    @overload
    def CreateZLibStreamForDeflate(
        cls,
        zLibStreamHandle: ZLibStreamHandle,
        level: ZLibNative.CompressionLevel,
        windowBits: int,
        memLevel: int,
        strategy: ZLibNative.CompressionStrategy,
    ) -> Tuple[ZLibNative.ErrorCode, ZLibStreamHandle]:
        """

        :param zLibStreamHandle:
        :param level:
        :param windowBits:
        :param memLevel:
        :param strategy:
        :return:
        """
    @classmethod
    @overload
    def CreateZLibStreamForInflate(
        cls, zLibStreamHandle: ZLibStreamHandle
    ) -> Tuple[ZLibNative.ErrorCode, ZLibStreamHandle]:
        """

        :param zLibStreamHandle:
        :return:
        """
    @classmethod
    @overload
    def CreateZLibStreamForInflate(
        cls, zLibStreamHandle: ZLibStreamHandle, windowBits: int
    ) -> Tuple[ZLibNative.ErrorCode, ZLibStreamHandle]:
        """

        :param zLibStreamHandle:
        :param windowBits:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    def ZLibCompileFlags(cls) -> int:
        """

        :return:
        """

    class CompressionLevel(Enum):
        """"""

        NoCompression: CompressionLevel = ...
        """"""
        BestSpeed: CompressionLevel = ...
        """"""
        BestCompression: CompressionLevel = ...
        """"""
        DefaultCompression: CompressionLevel = ...
        """"""

    class CompressionMethod(Enum):
        """"""

        Deflated: CompressionMethod = ...
        """"""

    class CompressionStrategy(Enum):
        """"""

        DefaultStrategy: CompressionStrategy = ...
        """"""
        Filtered: CompressionStrategy = ...
        """"""
        HuffmanOnly: CompressionStrategy = ...
        """"""
        Rle: CompressionStrategy = ...
        """"""
        Fixed: CompressionStrategy = ...
        """"""

    class ErrorCode(Enum):
        """"""

        Ok: ErrorCode = ...
        """"""
        StreamEnd: ErrorCode = ...
        """"""
        NeedDictionary: ErrorCode = ...
        """"""
        VersionError: ErrorCode = ...
        """"""
        BufError: ErrorCode = ...
        """"""
        MemError: ErrorCode = ...
        """"""
        DataError: ErrorCode = ...
        """"""
        StreamError: ErrorCode = ...
        """"""
        ErrorNo: ErrorCode = ...
        """"""

    class FlushCode(Enum):
        """"""

        NoFlush: FlushCode = ...
        """"""
        PartialFlush: FlushCode = ...
        """"""
        SyncFlush: FlushCode = ...
        """"""
        FullFlush: FlushCode = ...
        """"""
        Finish: FlushCode = ...
        """"""
        Block: FlushCode = ...
        """"""

    class ZLibStreamHandle(SafeHandleMinusOneIsInvalid, IDisposable):
        """"""

        def __init__(self):
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
            """

            :return:
            """
        @property
        def IsInvalid(self) -> bool:
            """

            :return:
            """
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
        def DangerousAddRef(self, success: bool) -> None:
            """

            :param success:
            """
        def DangerousGetHandle(self) -> IntPtr:
            """

            :return:
            """
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
            """

            :param obj:
            :return:
            """
        def GetErrorMessage(self) -> str:
            """"""
        def GetHashCode(self) -> int:
            """

            :return:
            """
        def GetType(self) -> Type:
            """

            :return:
            """
        def Inflate(self, flush: ZLibNative.FlushCode) -> ZLibNative.ErrorCode:
            """"""
        def InflateEnd(self) -> ZLibNative.ErrorCode:
            """"""
        def InflateInit2_(self, windowBits: int) -> ZLibNative.ErrorCode:
            """"""
        def SetHandleAsInvalid(self) -> None:
            """"""
        def ToString(self) -> str:
            """

            :return:
            """

        class State(Enum):
            """"""

            NotInitialized: State = ...
            """"""
            InitializedForDeflate: State = ...
            """"""
            InitializedForInflate: State = ...
            """"""
            Disposed: State = ...
            """"""
