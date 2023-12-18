from __future__ import annotations

from abc import ABC
from typing import List
from typing import Union
from typing import overload

from Microsoft.Win32 import WinInetCache
from System import Array
from System import AsyncCallback
from System import Boolean
from System import Byte
from System import DateTime
from System import Enum
from System import IAsyncResult
from System import IDisposable
from System import Int32
from System import Int64
from System import Object
from System import String
from System import TimeSpan
from System import Void
from System.IO import SeekOrigin
from System.IO import Stream
from System.Net import ICloseEx
from System.Net import IRequestLifetimeTracker

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class BaseWrapperStream(ABC, Stream, IDisposable, IRequestLifetimeTracker):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, wrappedStream: Stream): ...

    # No Properties

    # ---------- Methods ---------- #

    def TrackRequestLifetime(self, requestStartTimestamp: LongType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CombinedReadStream(BaseWrapperStream, IDisposable, IRequestLifetimeTracker, ICloseEx):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def CanRead(self) -> BooleanType: ...
    @property
    def CanSeek(self) -> BooleanType: ...
    @property
    def CanTimeout(self) -> BooleanType: ...
    @property
    def CanWrite(self) -> BooleanType: ...
    @property
    def Length(self) -> LongType: ...
    @property
    def Position(self) -> LongType: ...
    @Position.setter
    def Position(self, value: LongType) -> None: ...
    @property
    def ReadTimeout(self) -> IntType: ...
    @ReadTimeout.setter
    def ReadTimeout(self, value: IntType) -> None: ...
    @property
    def WriteTimeout(self) -> IntType: ...
    @WriteTimeout.setter
    def WriteTimeout(self, value: IntType) -> None: ...

    # ---------- Methods ---------- #

    def BeginRead(
        self,
        buffer: ArrayType[ByteType],
        offset: IntType,
        count: IntType,
        callback: AsyncCallback,
        state: ObjectType,
    ) -> IAsyncResult: ...
    def BeginWrite(
        self,
        buffer: ArrayType[ByteType],
        offset: IntType,
        count: IntType,
        callback: AsyncCallback,
        state: ObjectType,
    ) -> IAsyncResult: ...
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    def Flush(self) -> VoidType: ...
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    def SetLength(self, value: LongType) -> VoidType: ...
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    def get_CanRead(self) -> BooleanType: ...
    def get_CanSeek(self) -> BooleanType: ...
    def get_CanTimeout(self) -> BooleanType: ...
    def get_CanWrite(self) -> BooleanType: ...
    def get_Length(self) -> LongType: ...
    def get_Position(self) -> LongType: ...
    def get_ReadTimeout(self) -> IntType: ...
    def get_WriteTimeout(self) -> IntType: ...
    def set_Position(self, value: LongType) -> VoidType: ...
    def set_ReadTimeout(self, value: IntType) -> VoidType: ...
    def set_WriteTimeout(self, value: IntType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ForwardingReadStream(BaseWrapperStream, IDisposable, IRequestLifetimeTracker, ICloseEx):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def CanRead(self) -> BooleanType: ...
    @property
    def CanSeek(self) -> BooleanType: ...
    @property
    def CanTimeout(self) -> BooleanType: ...
    @property
    def CanWrite(self) -> BooleanType: ...
    @property
    def Length(self) -> LongType: ...
    @property
    def Position(self) -> LongType: ...
    @Position.setter
    def Position(self, value: LongType) -> None: ...
    @property
    def ReadTimeout(self) -> IntType: ...
    @ReadTimeout.setter
    def ReadTimeout(self, value: IntType) -> None: ...
    @property
    def WriteTimeout(self) -> IntType: ...
    @WriteTimeout.setter
    def WriteTimeout(self, value: IntType) -> None: ...

    # ---------- Methods ---------- #

    def BeginRead(
        self,
        buffer: ArrayType[ByteType],
        offset: IntType,
        count: IntType,
        callback: AsyncCallback,
        state: ObjectType,
    ) -> IAsyncResult: ...
    def BeginWrite(
        self,
        buffer: ArrayType[ByteType],
        offset: IntType,
        count: IntType,
        callback: AsyncCallback,
        state: ObjectType,
    ) -> IAsyncResult: ...
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    def Flush(self) -> VoidType: ...
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    def SetLength(self, value: LongType) -> VoidType: ...
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    def get_CanRead(self) -> BooleanType: ...
    def get_CanSeek(self) -> BooleanType: ...
    def get_CanTimeout(self) -> BooleanType: ...
    def get_CanWrite(self) -> BooleanType: ...
    def get_Length(self) -> LongType: ...
    def get_Position(self) -> LongType: ...
    def get_ReadTimeout(self) -> IntType: ...
    def get_WriteTimeout(self) -> IntType: ...
    def set_Position(self, value: LongType) -> VoidType: ...
    def set_ReadTimeout(self, value: IntType) -> VoidType: ...
    def set_WriteTimeout(self, value: IntType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class FtpRequestCacheValidator(HttpRequestCacheValidator):
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

class HttpRequestCachePolicy(RequestCachePolicy):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, level: HttpRequestCacheLevel): ...
    @overload
    def __init__(self, cacheAgeControl: HttpCacheAgeControl, ageOrFreshOrStale: TimeSpan): ...
    @overload
    def __init__(
        self, cacheAgeControl: HttpCacheAgeControl, maxAge: TimeSpan, freshOrStale: TimeSpan
    ): ...
    @overload
    def __init__(self, cacheSyncDate: DateTime): ...
    @overload
    def __init__(
        self,
        cacheAgeControl: HttpCacheAgeControl,
        maxAge: TimeSpan,
        freshOrStale: TimeSpan,
        cacheSyncDate: DateTime,
    ): ...

    # ---------- Properties ---------- #

    @property
    def CacheSyncDate(self) -> DateTime: ...
    @property
    def Level(self) -> HttpRequestCacheLevel: ...
    @property
    def MaxAge(self) -> TimeSpan: ...
    @property
    def MaxStale(self) -> TimeSpan: ...
    @property
    def MinFresh(self) -> TimeSpan: ...

    # ---------- Methods ---------- #

    def ToString(self) -> StringType: ...
    def get_CacheSyncDate(self) -> DateTime: ...
    @overload
    def get_Level(self) -> HttpRequestCacheLevel: ...
    def get_MaxAge(self) -> TimeSpan: ...
    def get_MaxStale(self) -> TimeSpan: ...
    def get_MinFresh(self) -> TimeSpan: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class HttpRequestCacheValidator(RequestCacheValidator):
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

class MetadataUpdateStream(BaseWrapperStream, IDisposable, IRequestLifetimeTracker, ICloseEx):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def CanRead(self) -> BooleanType: ...
    @property
    def CanSeek(self) -> BooleanType: ...
    @property
    def CanTimeout(self) -> BooleanType: ...
    @property
    def CanWrite(self) -> BooleanType: ...
    @property
    def Length(self) -> LongType: ...
    @property
    def Position(self) -> LongType: ...
    @Position.setter
    def Position(self, value: LongType) -> None: ...
    @property
    def ReadTimeout(self) -> IntType: ...
    @ReadTimeout.setter
    def ReadTimeout(self, value: IntType) -> None: ...
    @property
    def WriteTimeout(self) -> IntType: ...
    @WriteTimeout.setter
    def WriteTimeout(self, value: IntType) -> None: ...

    # ---------- Methods ---------- #

    def BeginRead(
        self,
        buffer: ArrayType[ByteType],
        offset: IntType,
        count: IntType,
        callback: AsyncCallback,
        state: ObjectType,
    ) -> IAsyncResult: ...
    def BeginWrite(
        self,
        buffer: ArrayType[ByteType],
        offset: IntType,
        count: IntType,
        callback: AsyncCallback,
        state: ObjectType,
    ) -> IAsyncResult: ...
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    def Flush(self) -> VoidType: ...
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    def SetLength(self, value: LongType) -> VoidType: ...
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    def get_CanRead(self) -> BooleanType: ...
    def get_CanSeek(self) -> BooleanType: ...
    def get_CanTimeout(self) -> BooleanType: ...
    def get_CanWrite(self) -> BooleanType: ...
    def get_Length(self) -> LongType: ...
    def get_Position(self) -> LongType: ...
    def get_ReadTimeout(self) -> IntType: ...
    def get_WriteTimeout(self) -> IntType: ...
    def set_Position(self, value: LongType) -> VoidType: ...
    def set_ReadTimeout(self, value: IntType) -> VoidType: ...
    def set_WriteTimeout(self, value: IntType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RangeStream(BaseWrapperStream, IDisposable, IRequestLifetimeTracker, ICloseEx):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def CanRead(self) -> BooleanType: ...
    @property
    def CanSeek(self) -> BooleanType: ...
    @property
    def CanTimeout(self) -> BooleanType: ...
    @property
    def CanWrite(self) -> BooleanType: ...
    @property
    def Length(self) -> LongType: ...
    @property
    def Position(self) -> LongType: ...
    @Position.setter
    def Position(self, value: LongType) -> None: ...
    @property
    def ReadTimeout(self) -> IntType: ...
    @ReadTimeout.setter
    def ReadTimeout(self, value: IntType) -> None: ...
    @property
    def WriteTimeout(self) -> IntType: ...
    @WriteTimeout.setter
    def WriteTimeout(self, value: IntType) -> None: ...

    # ---------- Methods ---------- #

    def BeginRead(
        self,
        buffer: ArrayType[ByteType],
        offset: IntType,
        count: IntType,
        callback: AsyncCallback,
        state: ObjectType,
    ) -> IAsyncResult: ...
    def BeginWrite(
        self,
        buffer: ArrayType[ByteType],
        offset: IntType,
        count: IntType,
        callback: AsyncCallback,
        state: ObjectType,
    ) -> IAsyncResult: ...
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    def Flush(self) -> VoidType: ...
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    def SetLength(self, value: LongType) -> VoidType: ...
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    def get_CanRead(self) -> BooleanType: ...
    def get_CanSeek(self) -> BooleanType: ...
    def get_CanTimeout(self) -> BooleanType: ...
    def get_CanWrite(self) -> BooleanType: ...
    def get_Length(self) -> LongType: ...
    def get_Position(self) -> LongType: ...
    def get_ReadTimeout(self) -> IntType: ...
    def get_WriteTimeout(self) -> IntType: ...
    def set_Position(self, value: LongType) -> VoidType: ...
    def set_ReadTimeout(self, value: IntType) -> VoidType: ...
    def set_WriteTimeout(self, value: IntType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RequestCache(ABC, ObjectType):
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

class RequestCacheBinding(ObjectType):
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

class RequestCacheEntry(ObjectType):
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

class RequestCacheManager(ObjectType):
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

class RequestCachePolicy(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, level: RequestCacheLevel): ...

    # ---------- Properties ---------- #

    @property
    def Level(self) -> RequestCacheLevel: ...

    # ---------- Methods ---------- #

    def ToString(self) -> StringType: ...
    def get_Level(self) -> RequestCacheLevel: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RequestCacheProtocol(ObjectType):
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

class RequestCacheValidator(ABC, ObjectType):
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

class ResponseCacheControl(ObjectType):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def ToString(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Rfc2616(ObjectType):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    def OnUpdateCache(ctx: HttpRequestCacheValidator) -> CacheValidationStatus: ...
    @staticmethod
    def OnValidateCache(ctx: HttpRequestCacheValidator) -> CacheValidationStatus: ...
    @staticmethod
    def OnValidateFreshness(ctx: HttpRequestCacheValidator) -> CacheFreshnessStatus: ...
    @staticmethod
    def OnValidateRequest(ctx: HttpRequestCacheValidator) -> CacheValidationStatus: ...
    @staticmethod
    def OnValidateResponse(ctx: HttpRequestCacheValidator) -> CacheValidationStatus: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SingleItemRequestCache(WinInetCache):
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

class _WinInetCache(ABC, ObjectType):
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

class CacheFreshnessStatus(Enum):
    Undefined = 0
    Fresh = 1
    Stale = 2

class CacheValidationStatus(Enum):
    DoNotUseCache = 0
    Fail = 1
    DoNotTakeFromCache = 2
    RetryResponseFromCache = 3
    RetryResponseFromServer = 4
    ReturnCachedResponse = 5
    CombineCachedAndServerResponse = 6
    CacheResponse = 7
    UpdateResponseInformation = 8
    RemoveFromCache = 9
    DoNotUpdateCache = 10
    Continue = 11

class HttpCacheAgeControl(Enum):
    # None = 0
    MinFresh = 1
    MaxAge = 2
    MaxAgeAndMinFresh = 3
    MaxStale = 4
    MaxAgeAndMaxStale = 6

class HttpMethod(Enum):
    Other = -1
    Head = 0
    Get = 1
    Post = 2
    Put = 3
    Delete = 4
    Options = 5
    Trace = 6
    Connect = 7

class HttpRequestCacheLevel(Enum):
    Default = 0
    BypassCache = 1
    CacheOnly = 2
    CacheIfAvailable = 3
    Revalidate = 4
    Reload = 5
    NoCacheNoStore = 6
    CacheOrNextCacheOnly = 7
    Refresh = 8

class RequestCacheLevel(Enum):
    Default = 0
    BypassCache = 1
    CacheOnly = 2
    CacheIfAvailable = 3
    Revalidate = 4
    Reload = 5
    NoCacheNoStore = 6

# No Delegates

__all__ = [
    BaseWrapperStream,
    CombinedReadStream,
    ForwardingReadStream,
    FtpRequestCacheValidator,
    HttpRequestCachePolicy,
    HttpRequestCacheValidator,
    MetadataUpdateStream,
    RangeStream,
    RequestCache,
    RequestCacheBinding,
    RequestCacheEntry,
    RequestCacheManager,
    RequestCachePolicy,
    RequestCacheProtocol,
    RequestCacheValidator,
    ResponseCacheControl,
    Rfc2616,
    SingleItemRequestCache,
    _WinInetCache,
    CacheFreshnessStatus,
    CacheValidationStatus,
    HttpCacheAgeControl,
    HttpMethod,
    HttpRequestCacheLevel,
    RequestCacheLevel,
]
