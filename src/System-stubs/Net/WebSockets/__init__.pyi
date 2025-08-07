"""Automatically generated stubs for C# namespace: System.Net.WebSockets."""

from abc import ABC
from typing import overload

from System import Array
from System import ArraySegment
from System import AsyncCallback
from System import Enum
from System import Exception
from System import IAsyncResult
from System import IDisposable
from System import Object
from System import TimeSpan
from System import Type
from System import Uri
from System.Collections import IDictionary
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IList
from System.Collections.Specialized import NameValueCollection
from System.ComponentModel import Win32Exception
from System.IO import SeekOrigin
from System.IO import Stream
from System.Net import BufferedReadStream
from System.Net import ConnectStream
from System.Net import CookieCollection
from System.Net import CookieContainer
from System.Net import HttpListenerContext
from System.Net import HttpRequestStream
from System.Net import HttpResponseStream
from System.Net import ICredentials
from System.Net import IWebProxy
from System.Reflection import MethodBase
from System.Runtime.InteropServices import _Exception
from System.Runtime.Remoting import ObjRef
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Security.Cryptography.X509Certificates import X509CertificateCollection
from System.Security.Principal import IPrincipal
from System.Threading import CancellationToken
from System.Threading.Tasks import Task

class ClientWebSocket(WebSocket, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CloseStatus(self) -> WebSocketCloseStatus | None:
        """"""
    @property
    def CloseStatusDescription(self) -> str:
        """"""
    @property
    def Options(self) -> ClientWebSocketOptions:
        """"""
    @property
    def State(self) -> WebSocketState:
        """"""
    @property
    def SubProtocol(self) -> str:
        """"""
    def Abort(self) -> None:
        """"""
    def CloseAsync(
        self,
        closeStatus: WebSocketCloseStatus,
        statusDescription: str,
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    def CloseOutputAsync(
        self,
        closeStatus: WebSocketCloseStatus,
        statusDescription: str,
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    def ConnectAsync(self, uri: Uri, cancellationToken: CancellationToken) -> Task:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ReceiveAsync(
        self, buffer: ArraySegment[int], cancellationToken: CancellationToken
    ) -> Task[WebSocketReceiveResult]:
        """"""
    def SendAsync(
        self,
        buffer: ArraySegment[int],
        messageType: WebSocketMessageType,
        endOfMessage: bool,
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    def ToString(self) -> str:
        """"""

class ClientWebSocketOptions(Object):
    """"""
    @property
    def ClientCertificates(self) -> X509CertificateCollection:
        """"""
    @ClientCertificates.setter
    def ClientCertificates(self, value: X509CertificateCollection) -> None: ...
    @property
    def Cookies(self) -> CookieContainer:
        """"""
    @Cookies.setter
    def Cookies(self, value: CookieContainer) -> None: ...
    @property
    def Credentials(self) -> ICredentials:
        """"""
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    @property
    def KeepAliveInterval(self) -> TimeSpan:
        """"""
    @KeepAliveInterval.setter
    def KeepAliveInterval(self, value: TimeSpan) -> None: ...
    @property
    def Proxy(self) -> IWebProxy:
        """"""
    @Proxy.setter
    def Proxy(self, value: IWebProxy) -> None: ...
    @property
    def UseDefaultCredentials(self) -> bool:
        """"""
    @UseDefaultCredentials.setter
    def UseDefaultCredentials(self, value: bool) -> None: ...
    def AddSubProtocol(self, subProtocol: str) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def SetBuffer(self, receiveBufferSize: int, sendBufferSize: int) -> None:
        """"""
    @overload
    def SetBuffer(
        self, receiveBufferSize: int, sendBufferSize: int, buffer: ArraySegment[int]
    ) -> None:
        """"""
    def SetRequestHeader(self, headerName: str, headerValue: str) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class HttpListenerWebSocketContext(WebSocketContext):
    """"""
    @property
    def CookieCollection(self) -> CookieCollection:
        """"""
    @property
    def Headers(self) -> NameValueCollection:
        """"""
    @property
    def IsAuthenticated(self) -> bool:
        """"""
    @property
    def IsLocal(self) -> bool:
        """"""
    @property
    def IsSecureConnection(self) -> bool:
        """"""
    @property
    def Origin(self) -> str:
        """"""
    @property
    def RequestUri(self) -> Uri:
        """"""
    @property
    def SecWebSocketKey(self) -> str:
        """"""
    @property
    def SecWebSocketProtocols(self) -> IEnumerable[str]:
        """"""
    @property
    def SecWebSocketVersion(self) -> str:
        """"""
    @property
    def User(self) -> IPrincipal:
        """"""
    @property
    def WebSocket(self) -> WebSocket:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class InternalClientWebSocket(WebSocketBase, IDisposable):
    """"""
    def __init__(
        self,
        innerStream: Stream,
        subProtocol: str,
        receiveBufferSize: int,
        sendBufferSize: int,
        keepAliveInterval: TimeSpan,
        useZeroMaskingKey: bool,
        internalBuffer: ArraySegment[int],
    ) -> None:
        """"""
    @property
    def CloseStatus(self) -> WebSocketCloseStatus | None:
        """"""
    @property
    def CloseStatusDescription(self) -> str:
        """"""
    @property
    def State(self) -> WebSocketState:
        """"""
    @property
    def SubProtocol(self) -> str:
        """"""
    def Abort(self) -> None:
        """"""
    def CloseAsync(
        self,
        closeStatus: WebSocketCloseStatus,
        statusDescription: str,
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    def CloseOutputAsync(
        self,
        closeStatus: WebSocketCloseStatus,
        statusDescription: str,
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ReceiveAsync(
        self, buffer: ArraySegment[int], cancellationToken: CancellationToken
    ) -> Task[WebSocketReceiveResult]:
        """"""
    def SendAsync(
        self,
        buffer: ArraySegment[int],
        messageType: WebSocketMessageType,
        endOfMessage: bool,
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    def ToString(self) -> str:
        """"""

class ServerWebSocket(WebSocketBase, IDisposable):
    """"""
    def __init__(
        self,
        innerStream: Stream,
        subProtocol: str,
        receiveBufferSize: int,
        keepAliveInterval: TimeSpan,
        internalBuffer: ArraySegment[int],
    ) -> None:
        """"""
    @property
    def CloseStatus(self) -> WebSocketCloseStatus | None:
        """"""
    @property
    def CloseStatusDescription(self) -> str:
        """"""
    @property
    def State(self) -> WebSocketState:
        """"""
    @property
    def SubProtocol(self) -> str:
        """"""
    def Abort(self) -> None:
        """"""
    def CloseAsync(
        self,
        closeStatus: WebSocketCloseStatus,
        statusDescription: str,
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    def CloseOutputAsync(
        self,
        closeStatus: WebSocketCloseStatus,
        statusDescription: str,
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ReceiveAsync(
        self, buffer: ArraySegment[int], cancellationToken: CancellationToken
    ) -> Task[WebSocketReceiveResult]:
        """"""
    def SendAsync(
        self,
        buffer: ArraySegment[int],
        messageType: WebSocketMessageType,
        endOfMessage: bool,
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    def ToString(self) -> str:
        """"""

class WebSocket(ABC, Object, IDisposable):
    """"""
    @property
    def CloseStatus(self) -> WebSocketCloseStatus | None:
        """"""
    @property
    def CloseStatusDescription(self) -> str:
        """"""
    @classmethod
    @property
    def DefaultKeepAliveInterval(cls) -> TimeSpan:
        """"""
    @property
    def State(self) -> WebSocketState:
        """"""
    @property
    def SubProtocol(self) -> str:
        """"""
    def Abort(self) -> None:
        """"""
    def CloseAsync(
        self,
        closeStatus: WebSocketCloseStatus,
        statusDescription: str,
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    def CloseOutputAsync(
        self,
        closeStatus: WebSocketCloseStatus,
        statusDescription: str,
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    @classmethod
    def CreateClientBuffer(cls, receiveBufferSize: int, sendBufferSize: int) -> ArraySegment[int]:
        """"""
    @classmethod
    def CreateClientWebSocket(
        cls,
        innerStream: Stream,
        subProtocol: str,
        receiveBufferSize: int,
        sendBufferSize: int,
        keepAliveInterval: TimeSpan,
        useZeroMaskingKey: bool,
        internalBuffer: ArraySegment[int],
    ) -> WebSocket:
        """"""
    @classmethod
    def CreateServerBuffer(cls, receiveBufferSize: int) -> ArraySegment[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsApplicationTargeting45(cls) -> bool:
        """"""
    def ReceiveAsync(
        self, buffer: ArraySegment[int], cancellationToken: CancellationToken
    ) -> Task[WebSocketReceiveResult]:
        """"""
    @classmethod
    def RegisterPrefixes(cls) -> None:
        """"""
    def SendAsync(
        self,
        buffer: ArraySegment[int],
        messageType: WebSocketMessageType,
        endOfMessage: bool,
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    def ToString(self) -> str:
        """"""

class WebSocketBase(ABC, WebSocket, IDisposable):
    """"""
    @property
    def CloseStatus(self) -> WebSocketCloseStatus | None:
        """"""
    @property
    def CloseStatusDescription(self) -> str:
        """"""
    @property
    def State(self) -> WebSocketState:
        """"""
    @property
    def SubProtocol(self) -> str:
        """"""
    def Abort(self) -> None:
        """"""
    def CloseAsync(
        self,
        closeStatus: WebSocketCloseStatus,
        statusDescription: str,
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    def CloseOutputAsync(
        self,
        closeStatus: WebSocketCloseStatus,
        statusDescription: str,
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ReceiveAsync(
        self, buffer: ArraySegment[int], cancellationToken: CancellationToken
    ) -> Task[WebSocketReceiveResult]:
        """"""
    def SendAsync(
        self,
        buffer: ArraySegment[int],
        messageType: WebSocketMessageType,
        endOfMessage: bool,
        cancellationToken: CancellationToken,
    ) -> Task:
        """"""
    def ToString(self) -> str:
        """"""

class WebSocketBuffer(Object, IDisposable):
    """"""
    @property
    def ReceiveBufferSize(self) -> int:
        """"""
    @property
    def SendBufferSize(self) -> int:
        """"""
    @overload
    def Dispose(self) -> None:
        """"""
    @overload
    def Dispose(self, webSocketState: WebSocketState) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class WebSocketCloseStatus(Enum):
    """"""

    NormalClosure: WebSocketCloseStatus = ...
    """"""
    EndpointUnavailable: WebSocketCloseStatus = ...
    """"""
    ProtocolError: WebSocketCloseStatus = ...
    """"""
    InvalidMessageType: WebSocketCloseStatus = ...
    """"""
    Empty: WebSocketCloseStatus = ...
    """"""
    InvalidPayloadData: WebSocketCloseStatus = ...
    """"""
    PolicyViolation: WebSocketCloseStatus = ...
    """"""
    MessageTooBig: WebSocketCloseStatus = ...
    """"""
    MandatoryExtension: WebSocketCloseStatus = ...
    """"""
    InternalServerError: WebSocketCloseStatus = ...
    """"""

class WebSocketConnectionStream(BufferedReadStream, WebSocketBase.IWebSocketStream, IDisposable):
    """"""
    def __init__(self, connectStream: ConnectStream, connectionGroupName: str) -> None:
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
    def SupportsMultipleWrite(self) -> bool:
        """"""
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def Abort(self) -> None:
        """"""
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
    def CloseNetworkConnectionAsync(self, cancellationToken: CancellationToken) -> Task:
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
    def MultipleWriteAsync(
        self, sendBuffers: IList[ArraySegment[int]], cancellationToken: CancellationToken
    ) -> Task:
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
    def SwitchToOpaqueMode(self, webSocket: WebSocketBase) -> None:
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

class WebSocketContext(ABC, Object):
    """"""
    @property
    def CookieCollection(self) -> CookieCollection:
        """"""
    @property
    def Headers(self) -> NameValueCollection:
        """"""
    @property
    def IsAuthenticated(self) -> bool:
        """"""
    @property
    def IsLocal(self) -> bool:
        """"""
    @property
    def IsSecureConnection(self) -> bool:
        """"""
    @property
    def Origin(self) -> str:
        """"""
    @property
    def RequestUri(self) -> Uri:
        """"""
    @property
    def SecWebSocketKey(self) -> str:
        """"""
    @property
    def SecWebSocketProtocols(self) -> IEnumerable[str]:
        """"""
    @property
    def SecWebSocketVersion(self) -> str:
        """"""
    @property
    def User(self) -> IPrincipal:
        """"""
    @property
    def WebSocket(self) -> WebSocket:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class WebSocketError(Enum):
    """"""

    Success: WebSocketError = ...
    """"""
    InvalidMessageType: WebSocketError = ...
    """"""
    Faulted: WebSocketError = ...
    """"""
    NativeError: WebSocketError = ...
    """"""
    NotAWebSocket: WebSocketError = ...
    """"""
    UnsupportedVersion: WebSocketError = ...
    """"""
    UnsupportedProtocol: WebSocketError = ...
    """"""
    HeaderError: WebSocketError = ...
    """"""
    ConnectionClosedPrematurely: WebSocketError = ...
    """"""
    InvalidState: WebSocketError = ...
    """"""

class WebSocketException(Win32Exception, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, error: WebSocketError) -> None:
        """"""
    @overload
    def __init__(self, error: WebSocketError, message: str) -> None:
        """"""
    @overload
    def __init__(self, error: WebSocketError, innerException: Exception) -> None:
        """"""
    @overload
    def __init__(self, error: WebSocketError, message: str, innerException: Exception) -> None:
        """"""
    @overload
    def __init__(self, nativeError: int) -> None:
        """"""
    @overload
    def __init__(self, nativeError: int, message: str) -> None:
        """"""
    @overload
    def __init__(self, nativeError: int, innerException: Exception) -> None:
        """"""
    @overload
    def __init__(self, error: WebSocketError, nativeError: int) -> None:
        """"""
    @overload
    def __init__(self, error: WebSocketError, nativeError: int, message: str) -> None:
        """"""
    @overload
    def __init__(self, error: WebSocketError, nativeError: int, innerException: Exception) -> None:
        """"""
    @overload
    def __init__(
        self, error: WebSocketError, nativeError: int, message: str, innerException: Exception
    ) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def ErrorCode(self) -> int:
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
    def NativeErrorCode(self) -> int:
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
    def WebSocketErrorCode(self) -> WebSocketError:
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

class WebSocketHelpers(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class WebSocketHttpListenerDuplexStream(Stream, WebSocketBase.IWebSocketStream, IDisposable):
    """"""
    def __init__(
        self,
        inputStream: HttpRequestStream,
        outputStream: HttpResponseStream,
        context: HttpListenerContext,
    ) -> None:
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
    def SupportsMultipleWrite(self) -> bool:
        """"""
    @property
    def WriteTimeout(self) -> int:
        """"""
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def Abort(self) -> None:
        """"""
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
    def CloseNetworkConnectionAsync(self, cancellationToken: CancellationToken) -> Task:
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
    def MultipleWriteAsync(
        self, sendBuffers: IList[ArraySegment[int]], cancellationToken: CancellationToken
    ) -> Task:
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
    def SwitchToOpaqueMode(self, webSocket: WebSocketBase) -> None:
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

class WebSocketMessageType(Enum):
    """"""

    Text: WebSocketMessageType = ...
    """"""
    Binary: WebSocketMessageType = ...
    """"""
    Close: WebSocketMessageType = ...
    """"""

class WebSocketProtocolComponent(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Succeeded(cls, hr: int) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class WebSocketReceiveResult(Object):
    """"""
    @overload
    def __init__(self, count: int, messageType: WebSocketMessageType, endOfMessage: bool) -> None:
        """"""
    @overload
    def __init__(
        self,
        count: int,
        messageType: WebSocketMessageType,
        endOfMessage: bool,
        closeStatus: WebSocketCloseStatus | None,
        closeStatusDescription: str,
    ) -> None:
        """"""
    @property
    def CloseStatus(self) -> WebSocketCloseStatus | None:
        """"""
    @property
    def CloseStatusDescription(self) -> str:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def EndOfMessage(self) -> bool:
        """"""
    @property
    def MessageType(self) -> WebSocketMessageType:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __len__(self) -> int:
        """"""

class WebSocketState(Enum):
    """"""

    _None: WebSocketState = ...
    """"""
    Connecting: WebSocketState = ...
    """"""
    Open: WebSocketState = ...
    """"""
    CloseSent: WebSocketState = ...
    """"""
    CloseReceived: WebSocketState = ...
    """"""
    Closed: WebSocketState = ...
    """"""
    Aborted: WebSocketState = ...
    """"""
