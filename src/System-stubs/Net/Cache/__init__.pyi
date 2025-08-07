"""Automatically generated stubs for C# namespace: System.Net.Cache."""

from abc import ABC
from typing import overload

from Microsoft.Win32 import WinInetCache
from System import Array
from System import AsyncCallback
from System import DateTime
from System import Enum
from System import IAsyncResult
from System import IDisposable
from System import Object
from System import TimeSpan
from System import Type
from System.IO import SeekOrigin
from System.IO import Stream
from System.Net import CloseExState
from System.Net import ICloseEx
from System.Net import IRequestLifetimeTracker
from System.Runtime.Remoting import ObjRef
from System.Threading import CancellationToken
from System.Threading.Tasks import Task

class BaseWrapperStream(ABC, Stream, IRequestLifetimeTracker, IDisposable):
    """"""
    def __init__(self, wrappedStream: Stream) -> None:
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
    def Read(self, buffer: Array[int], offset: int, count: int) -> tuple[int, Array[int]]:
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
    def TrackRequestLifetime(self, requestStartTimestamp: int) -> None:
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

class CacheFreshnessStatus(Enum):
    """"""

    Undefined: CacheFreshnessStatus = ...
    """"""
    Fresh: CacheFreshnessStatus = ...
    """"""
    Stale: CacheFreshnessStatus = ...
    """"""

class CacheValidationStatus(Enum):
    """"""

    DoNotUseCache: CacheValidationStatus = ...
    """"""
    Fail: CacheValidationStatus = ...
    """"""
    DoNotTakeFromCache: CacheValidationStatus = ...
    """"""
    RetryResponseFromCache: CacheValidationStatus = ...
    """"""
    RetryResponseFromServer: CacheValidationStatus = ...
    """"""
    ReturnCachedResponse: CacheValidationStatus = ...
    """"""
    CombineCachedAndServerResponse: CacheValidationStatus = ...
    """"""
    CacheResponse: CacheValidationStatus = ...
    """"""
    UpdateResponseInformation: CacheValidationStatus = ...
    """"""
    RemoveFromCache: CacheValidationStatus = ...
    """"""
    DoNotUpdateCache: CacheValidationStatus = ...
    """"""
    Continue: CacheValidationStatus = ...
    """"""

class CombinedReadStream(BaseWrapperStream, ICloseEx, IRequestLifetimeTracker, IDisposable):
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
    def CloseEx(self, closeState: CloseExState) -> None:
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
    def TrackRequestLifetime(self, requestStartTimestamp: int) -> None:
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

class ForwardingReadStream(BaseWrapperStream, ICloseEx, IRequestLifetimeTracker, IDisposable):
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
    def CloseEx(self, closeState: CloseExState) -> None:
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
    def TrackRequestLifetime(self, requestStartTimestamp: int) -> None:
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

class FtpRequestCacheValidator(HttpRequestCacheValidator):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class HttpCacheAgeControl(Enum):
    """"""

    _None: HttpCacheAgeControl = ...
    """"""
    MinFresh: HttpCacheAgeControl = ...
    """"""
    MaxAge: HttpCacheAgeControl = ...
    """"""
    MaxAgeAndMinFresh: HttpCacheAgeControl = ...
    """"""
    MaxStale: HttpCacheAgeControl = ...
    """"""
    MaxAgeAndMaxStale: HttpCacheAgeControl = ...
    """"""

class HttpMethod(Enum):
    """"""

    Head: HttpMethod = ...
    """"""
    Get: HttpMethod = ...
    """"""
    Post: HttpMethod = ...
    """"""
    Put: HttpMethod = ...
    """"""
    Delete: HttpMethod = ...
    """"""
    Options: HttpMethod = ...
    """"""
    Trace: HttpMethod = ...
    """"""
    Connect: HttpMethod = ...
    """"""
    Other: HttpMethod = ...
    """"""

class HttpRequestCacheLevel(Enum):
    """"""

    Default: HttpRequestCacheLevel = ...
    """"""
    BypassCache: HttpRequestCacheLevel = ...
    """"""
    CacheOnly: HttpRequestCacheLevel = ...
    """"""
    CacheIfAvailable: HttpRequestCacheLevel = ...
    """"""
    Revalidate: HttpRequestCacheLevel = ...
    """"""
    Reload: HttpRequestCacheLevel = ...
    """"""
    NoCacheNoStore: HttpRequestCacheLevel = ...
    """"""
    CacheOrNextCacheOnly: HttpRequestCacheLevel = ...
    """"""
    Refresh: HttpRequestCacheLevel = ...
    """"""

class HttpRequestCachePolicy(RequestCachePolicy):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, level: HttpRequestCacheLevel) -> None:
        """"""
    @overload
    def __init__(self, cacheAgeControl: HttpCacheAgeControl, ageOrFreshOrStale: TimeSpan) -> None:
        """"""
    @overload
    def __init__(
        self, cacheAgeControl: HttpCacheAgeControl, maxAge: TimeSpan, freshOrStale: TimeSpan
    ) -> None:
        """"""
    @overload
    def __init__(self, cacheSyncDate: DateTime) -> None:
        """"""
    @overload
    def __init__(
        self,
        cacheAgeControl: HttpCacheAgeControl,
        maxAge: TimeSpan,
        freshOrStale: TimeSpan,
        cacheSyncDate: DateTime,
    ) -> None:
        """"""
    @property
    def CacheSyncDate(self) -> DateTime:
        """"""
    @property
    def Level(self) -> RequestCacheLevel:
        """"""
    @property
    def MaxAge(self) -> TimeSpan:
        """"""
    @property
    def MaxStale(self) -> TimeSpan:
        """"""
    @property
    def MinFresh(self) -> TimeSpan:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class HttpRequestCacheValidator(RequestCacheValidator):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MetadataUpdateStream(BaseWrapperStream, ICloseEx, IRequestLifetimeTracker, IDisposable):
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
    def CloseEx(self, closeState: CloseExState) -> None:
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
    def TrackRequestLifetime(self, requestStartTimestamp: int) -> None:
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

class RangeStream(BaseWrapperStream, ICloseEx, IRequestLifetimeTracker, IDisposable):
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
    def CloseEx(self, closeState: CloseExState) -> None:
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
    def TrackRequestLifetime(self, requestStartTimestamp: int) -> None:
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

class RequestCache(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RequestCacheBinding(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RequestCacheEntry(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RequestCacheLevel(Enum):
    """"""

    Default: RequestCacheLevel = ...
    """"""
    BypassCache: RequestCacheLevel = ...
    """"""
    CacheOnly: RequestCacheLevel = ...
    """"""
    CacheIfAvailable: RequestCacheLevel = ...
    """"""
    Revalidate: RequestCacheLevel = ...
    """"""
    Reload: RequestCacheLevel = ...
    """"""
    NoCacheNoStore: RequestCacheLevel = ...
    """"""

class RequestCacheManager(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RequestCachePolicy(Object):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, level: RequestCacheLevel) -> None:
        """"""
    @property
    def Level(self) -> RequestCacheLevel:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RequestCacheProtocol(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RequestCacheValidator(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ResponseCacheControl(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Rfc2616(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def OnUpdateCache(cls, ctx: HttpRequestCacheValidator) -> CacheValidationStatus:
        """"""
    @classmethod
    def OnValidateCache(cls, ctx: HttpRequestCacheValidator) -> CacheValidationStatus:
        """"""
    @classmethod
    def OnValidateFreshness(cls, ctx: HttpRequestCacheValidator) -> CacheFreshnessStatus:
        """"""
    @classmethod
    def OnValidateRequest(cls, ctx: HttpRequestCacheValidator) -> CacheValidationStatus:
        """"""
    @classmethod
    def OnValidateResponse(cls, ctx: HttpRequestCacheValidator) -> CacheValidationStatus:
        """"""
    def ToString(self) -> str:
        """"""

class SingleItemRequestCache(WinInetCache):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class _WinInetCache(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
