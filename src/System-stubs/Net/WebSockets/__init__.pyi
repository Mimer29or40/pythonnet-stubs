from __future__ import annotations

from abc import ABC
from typing import Optional
from typing import Tuple
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
from System.Net.WebSockets.WebSocketBase import IWebSocketStream
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

    def __init__(self):
        """"""
    @property
    def CloseStatus(self) -> Optional[WebSocketCloseStatus]:
        """

        :return:
        """
    @property
    def CloseStatusDescription(self) -> str:
        """

        :return:
        """
    @classmethod
    @property
    def DefaultKeepAliveInterval(cls) -> TimeSpan:
        """

        :return:
        """
    @property
    def Options(self) -> ClientWebSocketOptions:
        """

        :return:
        """
    @property
    def State(self) -> WebSocketState:
        """

        :return:
        """
    @property
    def SubProtocol(self) -> str:
        """

        :return:
        """
    def Abort(self) -> None:
        """"""
    def CloseAsync(
        self,
        closeStatus: WebSocketCloseStatus,
        statusDescription: str,
        cancellationToken: CancellationToken,
    ) -> Task:
        """

        :param closeStatus:
        :param statusDescription:
        :param cancellationToken:
        :return:
        """
    def CloseOutputAsync(
        self,
        closeStatus: WebSocketCloseStatus,
        statusDescription: str,
        cancellationToken: CancellationToken,
    ) -> Task:
        """

        :param closeStatus:
        :param statusDescription:
        :param cancellationToken:
        :return:
        """
    def ConnectAsync(self, uri: Uri, cancellationToken: CancellationToken) -> Task:
        """

        :param uri:
        :param cancellationToken:
        :return:
        """
    def Dispose(self) -> None:
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
    def ReceiveAsync(
        self, buffer: ArraySegment[int], cancellationToken: CancellationToken
    ) -> Task[WebSocketReceiveResult]:
        """

        :param buffer:
        :param cancellationToken:
        :return:
        """
    def SendAsync(
        self,
        buffer: ArraySegment[int],
        messageType: WebSocketMessageType,
        endOfMessage: bool,
        cancellationToken: CancellationToken,
    ) -> Task:
        """

        :param buffer:
        :param messageType:
        :param endOfMessage:
        :param cancellationToken:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ClientWebSocketOptions(Object):
    """"""

    @property
    def ClientCertificates(self) -> X509CertificateCollection:
        """

        :return:
        """
    @ClientCertificates.setter
    def ClientCertificates(self, value: X509CertificateCollection) -> None: ...
    @property
    def Cookies(self) -> CookieContainer:
        """

        :return:
        """
    @Cookies.setter
    def Cookies(self, value: CookieContainer) -> None: ...
    @property
    def Credentials(self) -> ICredentials:
        """

        :return:
        """
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    @property
    def KeepAliveInterval(self) -> TimeSpan:
        """

        :return:
        """
    @KeepAliveInterval.setter
    def KeepAliveInterval(self, value: TimeSpan) -> None: ...
    @property
    def Proxy(self) -> IWebProxy:
        """

        :return:
        """
    @Proxy.setter
    def Proxy(self, value: IWebProxy) -> None: ...
    @property
    def UseDefaultCredentials(self) -> bool:
        """

        :return:
        """
    @UseDefaultCredentials.setter
    def UseDefaultCredentials(self, value: bool) -> None: ...
    def AddSubProtocol(self, subProtocol: str) -> None:
        """

        :param subProtocol:
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
    @overload
    def SetBuffer(self, receiveBufferSize: int, sendBufferSize: int) -> None:
        """

        :param receiveBufferSize:
        :param sendBufferSize:
        """
    @overload
    def SetBuffer(
        self, receiveBufferSize: int, sendBufferSize: int, buffer: ArraySegment[int]
    ) -> None:
        """

        :param receiveBufferSize:
        :param sendBufferSize:
        :param buffer:
        """
    def SetRequestHeader(self, headerName: str, headerValue: str) -> None:
        """

        :param headerName:
        :param headerValue:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class HttpListenerWebSocketContext(WebSocketContext):
    """"""

    @property
    def CookieCollection(self) -> CookieCollection:
        """

        :return:
        """
    @property
    def Headers(self) -> NameValueCollection:
        """

        :return:
        """
    @property
    def IsAuthenticated(self) -> bool:
        """

        :return:
        """
    @property
    def IsLocal(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecureConnection(self) -> bool:
        """

        :return:
        """
    @property
    def Origin(self) -> str:
        """

        :return:
        """
    @property
    def RequestUri(self) -> Uri:
        """

        :return:
        """
    @property
    def SecWebSocketKey(self) -> str:
        """

        :return:
        """
    @property
    def SecWebSocketProtocols(self) -> IEnumerable[str]:
        """

        :return:
        """
    @property
    def SecWebSocketVersion(self) -> str:
        """

        :return:
        """
    @property
    def User(self) -> IPrincipal:
        """

        :return:
        """
    @property
    def WebSocket(self) -> WebSocket:
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
    ):
        """

        :param innerStream:
        :param subProtocol:
        :param receiveBufferSize:
        :param sendBufferSize:
        :param keepAliveInterval:
        :param useZeroMaskingKey:
        :param internalBuffer:
        """
    @property
    def CloseStatus(self) -> Optional[WebSocketCloseStatus]:
        """

        :return:
        """
    @property
    def CloseStatusDescription(self) -> str:
        """

        :return:
        """
    @classmethod
    @property
    def DefaultKeepAliveInterval(cls) -> TimeSpan:
        """

        :return:
        """
    @property
    def State(self) -> WebSocketState:
        """

        :return:
        """
    @property
    def SubProtocol(self) -> str:
        """

        :return:
        """
    def Abort(self) -> None:
        """"""
    def CloseAsync(
        self,
        closeStatus: WebSocketCloseStatus,
        statusDescription: str,
        cancellationToken: CancellationToken,
    ) -> Task:
        """

        :param closeStatus:
        :param statusDescription:
        :param cancellationToken:
        :return:
        """
    def CloseOutputAsync(
        self,
        closeStatus: WebSocketCloseStatus,
        statusDescription: str,
        cancellationToken: CancellationToken,
    ) -> Task:
        """

        :param closeStatus:
        :param statusDescription:
        :param cancellationToken:
        :return:
        """
    def Dispose(self) -> None:
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
    def ReceiveAsync(
        self, buffer: ArraySegment[int], cancellationToken: CancellationToken
    ) -> Task[WebSocketReceiveResult]:
        """

        :param buffer:
        :param cancellationToken:
        :return:
        """
    def SendAsync(
        self,
        buffer: ArraySegment[int],
        messageType: WebSocketMessageType,
        endOfMessage: bool,
        cancellationToken: CancellationToken,
    ) -> Task:
        """

        :param buffer:
        :param messageType:
        :param endOfMessage:
        :param cancellationToken:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ServerWebSocket(WebSocketBase, IDisposable):
    """"""

    def __init__(
        self,
        innerStream: Stream,
        subProtocol: str,
        receiveBufferSize: int,
        keepAliveInterval: TimeSpan,
        internalBuffer: ArraySegment[int],
    ):
        """

        :param innerStream:
        :param subProtocol:
        :param receiveBufferSize:
        :param keepAliveInterval:
        :param internalBuffer:
        """
    @property
    def CloseStatus(self) -> Optional[WebSocketCloseStatus]:
        """

        :return:
        """
    @property
    def CloseStatusDescription(self) -> str:
        """

        :return:
        """
    @classmethod
    @property
    def DefaultKeepAliveInterval(cls) -> TimeSpan:
        """

        :return:
        """
    @property
    def State(self) -> WebSocketState:
        """

        :return:
        """
    @property
    def SubProtocol(self) -> str:
        """

        :return:
        """
    def Abort(self) -> None:
        """"""
    def CloseAsync(
        self,
        closeStatus: WebSocketCloseStatus,
        statusDescription: str,
        cancellationToken: CancellationToken,
    ) -> Task:
        """

        :param closeStatus:
        :param statusDescription:
        :param cancellationToken:
        :return:
        """
    def CloseOutputAsync(
        self,
        closeStatus: WebSocketCloseStatus,
        statusDescription: str,
        cancellationToken: CancellationToken,
    ) -> Task:
        """

        :param closeStatus:
        :param statusDescription:
        :param cancellationToken:
        :return:
        """
    def Dispose(self) -> None:
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
    def ReceiveAsync(
        self, buffer: ArraySegment[int], cancellationToken: CancellationToken
    ) -> Task[WebSocketReceiveResult]:
        """

        :param buffer:
        :param cancellationToken:
        :return:
        """
    def SendAsync(
        self,
        buffer: ArraySegment[int],
        messageType: WebSocketMessageType,
        endOfMessage: bool,
        cancellationToken: CancellationToken,
    ) -> Task:
        """

        :param buffer:
        :param messageType:
        :param endOfMessage:
        :param cancellationToken:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class WebSocket(ABC, Object, IDisposable):
    """"""

    @property
    def CloseStatus(self) -> Optional[WebSocketCloseStatus]:
        """

        :return:
        """
    @property
    def CloseStatusDescription(self) -> str:
        """

        :return:
        """
    @classmethod
    @property
    def DefaultKeepAliveInterval(cls) -> TimeSpan:
        """

        :return:
        """
    @property
    def State(self) -> WebSocketState:
        """

        :return:
        """
    @property
    def SubProtocol(self) -> str:
        """

        :return:
        """
    def Abort(self) -> None:
        """"""
    def CloseAsync(
        self,
        closeStatus: WebSocketCloseStatus,
        statusDescription: str,
        cancellationToken: CancellationToken,
    ) -> Task:
        """

        :param closeStatus:
        :param statusDescription:
        :param cancellationToken:
        :return:
        """
    def CloseOutputAsync(
        self,
        closeStatus: WebSocketCloseStatus,
        statusDescription: str,
        cancellationToken: CancellationToken,
    ) -> Task:
        """

        :param closeStatus:
        :param statusDescription:
        :param cancellationToken:
        :return:
        """
    @classmethod
    def CreateClientBuffer(cls, receiveBufferSize: int, sendBufferSize: int) -> ArraySegment[int]:
        """

        :param receiveBufferSize:
        :param sendBufferSize:
        :return:
        """
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
        """

        :param innerStream:
        :param subProtocol:
        :param receiveBufferSize:
        :param sendBufferSize:
        :param keepAliveInterval:
        :param useZeroMaskingKey:
        :param internalBuffer:
        :return:
        """
    @classmethod
    def CreateServerBuffer(cls, receiveBufferSize: int) -> ArraySegment[int]:
        """

        :param receiveBufferSize:
        :return:
        """
    def Dispose(self) -> None:
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
    @classmethod
    def IsApplicationTargeting45(cls) -> bool:
        """

        :return:
        """
    def ReceiveAsync(
        self, buffer: ArraySegment[int], cancellationToken: CancellationToken
    ) -> Task[WebSocketReceiveResult]:
        """

        :param buffer:
        :param cancellationToken:
        :return:
        """
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
        """

        :param buffer:
        :param messageType:
        :param endOfMessage:
        :param cancellationToken:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class WebSocketBase(ABC, WebSocket, IDisposable):
    """"""

    @property
    def CloseStatus(self) -> Optional[WebSocketCloseStatus]:
        """

        :return:
        """
    @property
    def CloseStatusDescription(self) -> str:
        """

        :return:
        """
    @classmethod
    @property
    def DefaultKeepAliveInterval(cls) -> TimeSpan:
        """

        :return:
        """
    @property
    def State(self) -> WebSocketState:
        """

        :return:
        """
    @property
    def SubProtocol(self) -> str:
        """

        :return:
        """
    def Abort(self) -> None:
        """"""
    def CloseAsync(
        self,
        closeStatus: WebSocketCloseStatus,
        statusDescription: str,
        cancellationToken: CancellationToken,
    ) -> Task:
        """

        :param closeStatus:
        :param statusDescription:
        :param cancellationToken:
        :return:
        """
    def CloseOutputAsync(
        self,
        closeStatus: WebSocketCloseStatus,
        statusDescription: str,
        cancellationToken: CancellationToken,
    ) -> Task:
        """

        :param closeStatus:
        :param statusDescription:
        :param cancellationToken:
        :return:
        """
    def Dispose(self) -> None:
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
    def ReceiveAsync(
        self, buffer: ArraySegment[int], cancellationToken: CancellationToken
    ) -> Task[WebSocketReceiveResult]:
        """

        :param buffer:
        :param cancellationToken:
        :return:
        """
    def SendAsync(
        self,
        buffer: ArraySegment[int],
        messageType: WebSocketMessageType,
        endOfMessage: bool,
        cancellationToken: CancellationToken,
    ) -> Task:
        """

        :param buffer:
        :param messageType:
        :param endOfMessage:
        :param cancellationToken:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class WebSocketBuffer(Object, IDisposable):
    """"""

    @property
    def ReceiveBufferSize(self) -> int:
        """

        :return:
        """
    @property
    def SendBufferSize(self) -> int:
        """

        :return:
        """
    @overload
    def Dispose(self) -> None:
        """"""
    @overload
    def Dispose(self, webSocketState: WebSocketState) -> None:
        """

        :param webSocketState:
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

    def __init__(self, connectStream: ConnectStream, connectionGroupName: str):
        """

        :param connectStream:
        :param connectionGroupName:
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
    def SupportsMultipleWrite(self) -> bool:
        """"""
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def Abort(self) -> None:
        """"""
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
    def CloseNetworkConnectionAsync(self, cancellationToken: CancellationToken) -> Task:
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
    def MultipleWriteAsync(
        self, buffers: IList[ArraySegment[int]], cancellationToken: CancellationToken
    ) -> Task:
        """"""
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
    def SwitchToOpaqueMode(self, webSocket: WebSocketBase) -> None:
        """"""
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

class WebSocketContext(ABC, Object):
    """"""

    @property
    def CookieCollection(self) -> CookieCollection:
        """

        :return:
        """
    @property
    def Headers(self) -> NameValueCollection:
        """

        :return:
        """
    @property
    def IsAuthenticated(self) -> bool:
        """

        :return:
        """
    @property
    def IsLocal(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecureConnection(self) -> bool:
        """

        :return:
        """
    @property
    def Origin(self) -> str:
        """

        :return:
        """
    @property
    def RequestUri(self) -> Uri:
        """

        :return:
        """
    @property
    def SecWebSocketKey(self) -> str:
        """

        :return:
        """
    @property
    def SecWebSocketProtocols(self) -> IEnumerable[str]:
        """

        :return:
        """
    @property
    def SecWebSocketVersion(self) -> str:
        """

        :return:
        """
    @property
    def User(self) -> IPrincipal:
        """

        :return:
        """
    @property
    def WebSocket(self) -> WebSocket:
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
    def __init__(self):
        """"""
    @overload
    def __init__(self, error: WebSocketError):
        """

        :param error:
        """
    @overload
    def __init__(self, nativeError: int):
        """

        :param nativeError:
        """
    @overload
    def __init__(self, message: str):
        """

        :param message:
        """
    @overload
    def __init__(self, error: WebSocketError, innerException: Exception):
        """

        :param error:
        :param innerException:
        """
    @overload
    def __init__(self, error: WebSocketError, nativeError: int):
        """

        :param error:
        :param nativeError:
        """
    @overload
    def __init__(self, error: WebSocketError, message: str):
        """

        :param error:
        :param message:
        """
    @overload
    def __init__(self, nativeError: int, innerException: Exception):
        """

        :param nativeError:
        :param innerException:
        """
    @overload
    def __init__(self, nativeError: int, message: str):
        """

        :param nativeError:
        :param message:
        """
    @overload
    def __init__(self, message: str, innerException: Exception):
        """

        :param message:
        :param innerException:
        """
    @overload
    def __init__(self, error: WebSocketError, nativeError: int, innerException: Exception):
        """

        :param error:
        :param nativeError:
        :param innerException:
        """
    @overload
    def __init__(self, error: WebSocketError, nativeError: int, message: str):
        """

        :param error:
        :param nativeError:
        :param message:
        """
    @overload
    def __init__(self, error: WebSocketError, message: str, innerException: Exception):
        """

        :param error:
        :param message:
        :param innerException:
        """
    @overload
    def __init__(
        self, error: WebSocketError, nativeError: int, message: str, innerException: Exception
    ):
        """

        :param error:
        :param nativeError:
        :param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
        """

        :return:
        """
    @property
    def ErrorCode(self) -> int:
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
    def NativeErrorCode(self) -> int:
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
    def WebSocketErrorCode(self) -> WebSocketError:
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

class WebSocketHelpers(ABC, Object):
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

class WebSocketHttpListenerDuplexStream(Stream, WebSocketBase.IWebSocketStream, IDisposable):
    """"""

    def __init__(
        self,
        inputStream: HttpRequestStream,
        outputStream: HttpResponseStream,
        context: HttpListenerContext,
    ):
        """

        :param inputStream:
        :param outputStream:
        :param context:
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
    def SupportsMultipleWrite(self) -> bool:
        """"""
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def Abort(self) -> None:
        """"""
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
    def CloseNetworkConnectionAsync(self, cancellationToken: CancellationToken) -> Task:
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
    def MultipleWriteAsync(
        self, buffers: IList[ArraySegment[int]], cancellationToken: CancellationToken
    ) -> Task:
        """"""
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
    def SwitchToOpaqueMode(self, webSocket: WebSocketBase) -> None:
        """"""
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
    @classmethod
    def Succeeded(cls, hr: int) -> bool:
        """

        :param hr:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class WebSocketReceiveResult(Object):
    """"""

    @overload
    def __init__(self, count: int, messageType: WebSocketMessageType, endOfMessage: bool):
        """

        :param count:
        :param messageType:
        :param endOfMessage:
        """
    @overload
    def __init__(
        self,
        count: int,
        messageType: WebSocketMessageType,
        endOfMessage: bool,
        closeStatus: Optional[WebSocketCloseStatus],
        closeStatusDescription: str,
    ):
        """

        :param count:
        :param messageType:
        :param endOfMessage:
        :param closeStatus:
        :param closeStatusDescription:
        """
    @property
    def CloseStatus(self) -> Optional[WebSocketCloseStatus]:
        """

        :return:
        """
    @property
    def CloseStatusDescription(self) -> str:
        """

        :return:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def EndOfMessage(self) -> bool:
        """

        :return:
        """
    @property
    def MessageType(self) -> WebSocketMessageType:
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
