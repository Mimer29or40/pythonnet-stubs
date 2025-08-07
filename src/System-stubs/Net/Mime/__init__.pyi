"""Automatically generated stubs for C# namespace: System.Net.Mime."""

from abc import ABC
from collections.abc import Iterator
from typing import ClassVar
from typing import overload

from System import Array
from System import AsyncCallback
from System import DateTime
from System import Enum
from System import IAsyncResult
from System import IDisposable
from System import Object
from System import Type
from System.Collections import ICollection
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections.Specialized import NameValueCollection
from System.Collections.Specialized import StringDictionary
from System.IO import SeekOrigin
from System.IO import Stream
from System.Net import DelegatedStream
from System.Net import LazyAsyncResult
from System.Runtime.Remoting import ObjRef
from System.Runtime.Serialization import IDeserializationCallback
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Threading import CancellationToken
from System.Threading import WaitHandle
from System.Threading.Tasks import Task

class Base64WriteStateInfo(WriteStateInfoBase):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class BaseWriter(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ContentDisposition(Object):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, disposition: str) -> None:
        """"""
    @property
    def CreationDate(self) -> DateTime:
        """"""
    @CreationDate.setter
    def CreationDate(self, value: DateTime) -> None: ...
    @property
    def DispositionType(self) -> str:
        """"""
    @DispositionType.setter
    def DispositionType(self, value: str) -> None: ...
    @property
    def FileName(self) -> str:
        """"""
    @FileName.setter
    def FileName(self, value: str) -> None: ...
    @property
    def Inline(self) -> bool:
        """"""
    @Inline.setter
    def Inline(self, value: bool) -> None: ...
    @property
    def ModificationDate(self) -> DateTime:
        """"""
    @ModificationDate.setter
    def ModificationDate(self, value: DateTime) -> None: ...
    @property
    def Parameters(self) -> StringDictionary:
        """"""
    @property
    def ReadDate(self) -> DateTime:
        """"""
    @ReadDate.setter
    def ReadDate(self, value: DateTime) -> None: ...
    @property
    def Size(self) -> int:
        """"""
    @Size.setter
    def Size(self, value: int) -> None: ...
    def Equals(self, rparam: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ContentTransferEncoding(Enum):
    """"""

    SevenBit: ContentTransferEncoding = ...
    """"""
    EightBit: ContentTransferEncoding = ...
    """"""
    Binary: ContentTransferEncoding = ...
    """"""
    Base64: ContentTransferEncoding = ...
    """"""
    QuotedPrintable: ContentTransferEncoding = ...
    """"""
    QEncoded: ContentTransferEncoding = ...
    """"""
    Other: ContentTransferEncoding = ...
    """"""
    Unspecified: ContentTransferEncoding = ...
    """"""

class ContentType(Object):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, contentType: str) -> None:
        """"""
    @property
    def Boundary(self) -> str:
        """"""
    @Boundary.setter
    def Boundary(self, value: str) -> None: ...
    @property
    def CharSet(self) -> str:
        """"""
    @CharSet.setter
    def CharSet(self, value: str) -> None: ...
    @property
    def MediaType(self) -> str:
        """"""
    @MediaType.setter
    def MediaType(self, value: str) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def Parameters(self) -> StringDictionary:
        """"""
    def Equals(self, rparam: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DispositionTypeNames(ABC, Object):
    """"""

    Attachment: ClassVar[str]
    """"""
    Inline: ClassVar[str]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class EightBitStream(DelegatedStream, IEncodableStream, IDisposable):
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
    def DecodeBytes(self, buffer: Array[int], offset: int, count: int) -> int:
        """"""
    def Dispose(self) -> None:
        """"""
    def EncodeBytes(self, buffer: Array[int], offset: int, count: int) -> int:
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
    def GetEncodedString(self) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetStream(self) -> Stream:
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

class EncodedStreamFactory(Object):
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

class HeaderCollection(
    NameValueCollection, ICollection, IEnumerable, IDeserializationCallback, ISerializable
):
    """"""
    @property
    def AllKeys(self) -> Array[str]:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> str:
        """"""
    @property
    def Keys(self) -> NameObjectCollectionBase.KeysCollection:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, c: NameValueCollection) -> None:
        """"""
    @overload
    def Add(self, name: str, value: str) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def CopyTo(self, dest: Array, index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Get(self, index: int) -> str:
        """"""
    @overload
    def Get(self, name: str) -> str:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetKey(self, index: int) -> str:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def GetValues(self, index: int) -> Array[str]:
        """"""
    @overload
    def GetValues(self, name: str) -> Array[str]:
        """"""
    def HasKeys(self) -> bool:
        """"""
    def OnDeserialization(self, sender: object) -> None:
        """"""
    def Remove(self, name: str) -> None:
        """"""
    def Set(self, name: str, value: str) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, name: str) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    @overload
    def __getitem__(self, index: int) -> str:
        """"""
    @overload
    def __getitem__(self, name: str) -> str:
        """"""
    def __setitem__(self, name: str, value: str) -> None:
        """"""
    class KeysCollection(Object, ICollection, IEnumerable):
        """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> str:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def Get(self, index: int) -> str:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> str:
            """"""

class IEncodableStream:
    """"""
    def DecodeBytes(self, buffer: Array[int], offset: int, count: int) -> int:
        """"""
    def EncodeBytes(self, buffer: Array[int], offset: int, count: int) -> int:
        """"""
    def GetEncodedString(self) -> str:
        """"""
    def GetStream(self) -> Stream:
        """"""

class MailBnfHelper(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MediaTypeNames(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    class Application(ABC, Object):
        """"""

        Octet: ClassVar[str]
        """"""
        Pdf: ClassVar[str]
        """"""
        Rtf: ClassVar[str]
        """"""
        Soap: ClassVar[str]
        """"""
        Zip: ClassVar[str]
        """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""

    class Image(ABC, Object):
        """"""

        Gif: ClassVar[str]
        """"""
        Jpeg: ClassVar[str]
        """"""
        Tiff: ClassVar[str]
        """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""

    class Text(ABC, Object):
        """"""

        Html: ClassVar[str]
        """"""
        Plain: ClassVar[str]
        """"""
        RichText: ClassVar[str]
        """"""
        Xml: ClassVar[str]
        """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""

class MimeBasePart(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MimeMultiPart(MimeBasePart):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MimeMultiPartType(Enum):
    """"""

    Mixed: MimeMultiPartType = ...
    """"""
    Alternative: MimeMultiPartType = ...
    """"""
    Parallel: MimeMultiPartType = ...
    """"""
    Related: MimeMultiPartType = ...
    """"""
    Unknown: MimeMultiPartType = ...
    """"""

class MimePart(MimeBasePart, IDisposable):
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

class MimeWriter(BaseWriter):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MultiAsyncResult(LazyAsyncResult, IAsyncResult):
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

class QEncodedStream(DelegatedStream, IEncodableStream, IDisposable):
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
    def DecodeBytes(self, buffer: Array[int], offset: int, count: int) -> int:
        """"""
    def Dispose(self) -> None:
        """"""
    def EncodeBytes(self, buffer: Array[int], offset: int, count: int) -> int:
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
    def GetEncodedString(self) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetStream(self) -> Stream:
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

class QuotedPrintableStream(DelegatedStream, IEncodableStream, IDisposable):
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
    def DecodeBytes(self, buffer: Array[int], offset: int, count: int) -> int:
        """"""
    def Dispose(self) -> None:
        """"""
    def EncodeBytes(self, buffer: Array[int], offset: int, count: int) -> int:
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
    def GetEncodedString(self) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetStream(self) -> Stream:
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

class SmtpDateTime(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TransferEncoding(Enum):
    """"""

    QuotedPrintable: TransferEncoding = ...
    """"""
    Base64: TransferEncoding = ...
    """"""
    SevenBit: TransferEncoding = ...
    """"""
    EightBit: TransferEncoding = ...
    """"""
    Unknown: TransferEncoding = ...
    """"""

class WriteStateInfoBase(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
