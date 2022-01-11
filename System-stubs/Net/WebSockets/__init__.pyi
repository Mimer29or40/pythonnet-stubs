from __future__ import annotations

from abc import ABC
from typing import List, Optional, Union, overload

from System import Array, ArraySegment, AsyncCallback, Boolean, Byte, Enum, Exception, IAsyncResult, IDisposable, Int32, Int64, Nullable, Object, String, TimeSpan, Uri, Void
from System.Collections.Generic import IEnumerable, IList
from System.Collections.Specialized import NameValueCollection
from System.ComponentModel import Win32Exception
from System.IO import SeekOrigin, Stream
from System.Net import BufferedReadStream, ConnectStream, CookieCollection, CookieContainer, HttpListenerContext, HttpRequestStream, HttpResponseStream, ICredentials, IWebProxy
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import ISerializable, SerializationInfo, StreamingContext
from System.Security.Cryptography.X509Certificates import X509CertificateCollection
from System.Security.Principal import IPrincipal
from System.Threading import CancellationToken
from System.Threading.Tasks import Task

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NullableType = Union[Optional, Nullable]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class ClientWebSocket(WebSocket, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CloseStatus(self) -> NullableType[Nullable[WebSocketCloseStatus]]: ...
    
    @property
    def CloseStatusDescription(self) -> StringType: ...
    
    @property
    def Options(self) -> ClientWebSocketOptions: ...
    
    @property
    def State(self) -> WebSocketState: ...
    
    @property
    def SubProtocol(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Abort(self) -> VoidType: ...
    
    def CloseAsync(self, closeStatus: WebSocketCloseStatus, statusDescription: StringType, cancellationToken: CancellationToken) -> Task: ...
    
    def CloseOutputAsync(self, closeStatus: WebSocketCloseStatus, statusDescription: StringType, cancellationToken: CancellationToken) -> Task: ...
    
    def ConnectAsync(self, uri: Uri, cancellationToken: CancellationToken) -> Task: ...
    
    def Dispose(self) -> VoidType: ...
    
    def ReceiveAsync(self, buffer: ArraySegment[ByteType], cancellationToken: CancellationToken) -> Task[WebSocketReceiveResult]: ...
    
    def SendAsync(self, buffer: ArraySegment[ByteType], messageType: WebSocketMessageType, endOfMessage: BooleanType, cancellationToken: CancellationToken) -> Task: ...
    
    def get_CloseStatus(self) -> NullableType[Nullable[WebSocketCloseStatus]]: ...
    
    def get_CloseStatusDescription(self) -> StringType: ...
    
    def get_Options(self) -> ClientWebSocketOptions: ...
    
    def get_State(self) -> WebSocketState: ...
    
    def get_SubProtocol(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ClientWebSocket(WebSocket, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CloseStatus(self) -> NullableType[Nullable[WebSocketCloseStatus]]: ...
    
    @property
    def CloseStatusDescription(self) -> StringType: ...
    
    @property
    def Options(self) -> ClientWebSocketOptions: ...
    
    @property
    def State(self) -> WebSocketState: ...
    
    @property
    def SubProtocol(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Abort(self) -> VoidType: ...
    
    def CloseAsync(self, closeStatus: WebSocketCloseStatus, statusDescription: StringType, cancellationToken: CancellationToken) -> Task: ...
    
    def CloseOutputAsync(self, closeStatus: WebSocketCloseStatus, statusDescription: StringType, cancellationToken: CancellationToken) -> Task: ...
    
    def ConnectAsync(self, uri: Uri, cancellationToken: CancellationToken) -> Task: ...
    
    def Dispose(self) -> VoidType: ...
    
    def ReceiveAsync(self, buffer: ArraySegment[ByteType], cancellationToken: CancellationToken) -> Task[WebSocketReceiveResult]: ...
    
    def SendAsync(self, buffer: ArraySegment[ByteType], messageType: WebSocketMessageType, endOfMessage: BooleanType, cancellationToken: CancellationToken) -> Task: ...
    
    def get_CloseStatus(self) -> NullableType[Nullable[WebSocketCloseStatus]]: ...
    
    def get_CloseStatusDescription(self) -> StringType: ...
    
    def get_Options(self) -> ClientWebSocketOptions: ...
    
    def get_State(self) -> WebSocketState: ...
    
    def get_SubProtocol(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ClientWebSocketOptions(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ClientCertificates(self) -> X509CertificateCollection: ...
    
    @ClientCertificates.setter
    def ClientCertificates(self, value: X509CertificateCollection) -> None: ...
    
    @property
    def Cookies(self) -> CookieContainer: ...
    
    @Cookies.setter
    def Cookies(self, value: CookieContainer) -> None: ...
    
    @property
    def Credentials(self) -> ICredentials: ...
    
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    
    @property
    def KeepAliveInterval(self) -> TimeSpan: ...
    
    @KeepAliveInterval.setter
    def KeepAliveInterval(self, value: TimeSpan) -> None: ...
    
    @property
    def Proxy(self) -> IWebProxy: ...
    
    @Proxy.setter
    def Proxy(self, value: IWebProxy) -> None: ...
    
    @property
    def UseDefaultCredentials(self) -> BooleanType: ...
    
    @UseDefaultCredentials.setter
    def UseDefaultCredentials(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AddSubProtocol(self, subProtocol: StringType) -> VoidType: ...
    
    @overload
    def SetBuffer(self, receiveBufferSize: IntType, sendBufferSize: IntType) -> VoidType: ...
    
    @overload
    def SetBuffer(self, receiveBufferSize: IntType, sendBufferSize: IntType, buffer: ArraySegment[ByteType]) -> VoidType: ...
    
    def SetRequestHeader(self, headerName: StringType, headerValue: StringType) -> VoidType: ...
    
    def get_ClientCertificates(self) -> X509CertificateCollection: ...
    
    def get_Cookies(self) -> CookieContainer: ...
    
    def get_Credentials(self) -> ICredentials: ...
    
    def get_KeepAliveInterval(self) -> TimeSpan: ...
    
    def get_Proxy(self) -> IWebProxy: ...
    
    def get_UseDefaultCredentials(self) -> BooleanType: ...
    
    def set_ClientCertificates(self, value: X509CertificateCollection) -> VoidType: ...
    
    def set_Cookies(self, value: CookieContainer) -> VoidType: ...
    
    def set_Credentials(self, value: ICredentials) -> VoidType: ...
    
    def set_KeepAliveInterval(self, value: TimeSpan) -> VoidType: ...
    
    def set_Proxy(self, value: IWebProxy) -> VoidType: ...
    
    def set_UseDefaultCredentials(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ClientWebSocketOptions(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ClientCertificates(self) -> X509CertificateCollection: ...
    
    @ClientCertificates.setter
    def ClientCertificates(self, value: X509CertificateCollection) -> None: ...
    
    @property
    def Cookies(self) -> CookieContainer: ...
    
    @Cookies.setter
    def Cookies(self, value: CookieContainer) -> None: ...
    
    @property
    def Credentials(self) -> ICredentials: ...
    
    @Credentials.setter
    def Credentials(self, value: ICredentials) -> None: ...
    
    @property
    def KeepAliveInterval(self) -> TimeSpan: ...
    
    @KeepAliveInterval.setter
    def KeepAliveInterval(self, value: TimeSpan) -> None: ...
    
    @property
    def Proxy(self) -> IWebProxy: ...
    
    @Proxy.setter
    def Proxy(self, value: IWebProxy) -> None: ...
    
    @property
    def UseDefaultCredentials(self) -> BooleanType: ...
    
    @UseDefaultCredentials.setter
    def UseDefaultCredentials(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AddSubProtocol(self, subProtocol: StringType) -> VoidType: ...
    
    @overload
    def SetBuffer(self, receiveBufferSize: IntType, sendBufferSize: IntType) -> VoidType: ...
    
    @overload
    def SetBuffer(self, receiveBufferSize: IntType, sendBufferSize: IntType, buffer: ArraySegment[ByteType]) -> VoidType: ...
    
    def SetRequestHeader(self, headerName: StringType, headerValue: StringType) -> VoidType: ...
    
    def get_ClientCertificates(self) -> X509CertificateCollection: ...
    
    def get_Cookies(self) -> CookieContainer: ...
    
    def get_Credentials(self) -> ICredentials: ...
    
    def get_KeepAliveInterval(self) -> TimeSpan: ...
    
    def get_Proxy(self) -> IWebProxy: ...
    
    def get_UseDefaultCredentials(self) -> BooleanType: ...
    
    def set_ClientCertificates(self, value: X509CertificateCollection) -> VoidType: ...
    
    def set_Cookies(self, value: CookieContainer) -> VoidType: ...
    
    def set_Credentials(self, value: ICredentials) -> VoidType: ...
    
    def set_KeepAliveInterval(self, value: TimeSpan) -> VoidType: ...
    
    def set_Proxy(self, value: IWebProxy) -> VoidType: ...
    
    def set_UseDefaultCredentials(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HttpListenerWebSocketContext(WebSocketContext):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CookieCollection(self) -> CookieCollection: ...
    
    @property
    def Headers(self) -> NameValueCollection: ...
    
    @property
    def IsAuthenticated(self) -> BooleanType: ...
    
    @property
    def IsLocal(self) -> BooleanType: ...
    
    @property
    def IsSecureConnection(self) -> BooleanType: ...
    
    @property
    def Origin(self) -> StringType: ...
    
    @property
    def RequestUri(self) -> Uri: ...
    
    @property
    def SecWebSocketKey(self) -> StringType: ...
    
    @property
    def SecWebSocketProtocols(self) -> IEnumerable[StringType]: ...
    
    @property
    def SecWebSocketVersion(self) -> StringType: ...
    
    @property
    def User(self) -> IPrincipal: ...
    
    @property
    def WebSocket(self) -> WebSocket: ...
    
    # ---------- Methods ---------- #
    
    def get_CookieCollection(self) -> CookieCollection: ...
    
    def get_Headers(self) -> NameValueCollection: ...
    
    def get_IsAuthenticated(self) -> BooleanType: ...
    
    def get_IsLocal(self) -> BooleanType: ...
    
    def get_IsSecureConnection(self) -> BooleanType: ...
    
    def get_Origin(self) -> StringType: ...
    
    def get_RequestUri(self) -> Uri: ...
    
    def get_SecWebSocketKey(self) -> StringType: ...
    
    def get_SecWebSocketProtocols(self) -> IEnumerable[StringType]: ...
    
    def get_SecWebSocketVersion(self) -> StringType: ...
    
    def get_User(self) -> IPrincipal: ...
    
    def get_WebSocket(self) -> WebSocket: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HttpListenerWebSocketContext(WebSocketContext):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CookieCollection(self) -> CookieCollection: ...
    
    @property
    def Headers(self) -> NameValueCollection: ...
    
    @property
    def IsAuthenticated(self) -> BooleanType: ...
    
    @property
    def IsLocal(self) -> BooleanType: ...
    
    @property
    def IsSecureConnection(self) -> BooleanType: ...
    
    @property
    def Origin(self) -> StringType: ...
    
    @property
    def RequestUri(self) -> Uri: ...
    
    @property
    def SecWebSocketKey(self) -> StringType: ...
    
    @property
    def SecWebSocketProtocols(self) -> IEnumerable[StringType]: ...
    
    @property
    def SecWebSocketVersion(self) -> StringType: ...
    
    @property
    def User(self) -> IPrincipal: ...
    
    @property
    def WebSocket(self) -> WebSocket: ...
    
    # ---------- Methods ---------- #
    
    def get_CookieCollection(self) -> CookieCollection: ...
    
    def get_Headers(self) -> NameValueCollection: ...
    
    def get_IsAuthenticated(self) -> BooleanType: ...
    
    def get_IsLocal(self) -> BooleanType: ...
    
    def get_IsSecureConnection(self) -> BooleanType: ...
    
    def get_Origin(self) -> StringType: ...
    
    def get_RequestUri(self) -> Uri: ...
    
    def get_SecWebSocketKey(self) -> StringType: ...
    
    def get_SecWebSocketProtocols(self) -> IEnumerable[StringType]: ...
    
    def get_SecWebSocketVersion(self) -> StringType: ...
    
    def get_User(self) -> IPrincipal: ...
    
    def get_WebSocket(self) -> WebSocket: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InternalClientWebSocket(WebSocketBase, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, innerStream: Stream, subProtocol: StringType, receiveBufferSize: IntType, sendBufferSize: IntType, keepAliveInterval: TimeSpan, useZeroMaskingKey: BooleanType, internalBuffer: ArraySegment[ByteType]): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class InternalClientWebSocket(WebSocketBase, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, innerStream: Stream, subProtocol: StringType, receiveBufferSize: IntType, sendBufferSize: IntType, keepAliveInterval: TimeSpan, useZeroMaskingKey: BooleanType, internalBuffer: ArraySegment[ByteType]): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ServerWebSocket(WebSocketBase, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, innerStream: Stream, subProtocol: StringType, receiveBufferSize: IntType, keepAliveInterval: TimeSpan, internalBuffer: ArraySegment[ByteType]): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ServerWebSocket(WebSocketBase, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, innerStream: Stream, subProtocol: StringType, receiveBufferSize: IntType, keepAliveInterval: TimeSpan, internalBuffer: ArraySegment[ByteType]): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebSocket(ABC, ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CloseStatus(self) -> NullableType[Nullable[WebSocketCloseStatus]]: ...
    
    @property
    def CloseStatusDescription(self) -> StringType: ...
    
    @staticmethod
    @property
    def DefaultKeepAliveInterval() -> TimeSpan: ...
    
    @property
    def State(self) -> WebSocketState: ...
    
    @property
    def SubProtocol(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Abort(self) -> VoidType: ...
    
    def CloseAsync(self, closeStatus: WebSocketCloseStatus, statusDescription: StringType, cancellationToken: CancellationToken) -> Task: ...
    
    def CloseOutputAsync(self, closeStatus: WebSocketCloseStatus, statusDescription: StringType, cancellationToken: CancellationToken) -> Task: ...
    
    @staticmethod
    def CreateClientBuffer(receiveBufferSize: IntType, sendBufferSize: IntType) -> ArraySegment[ByteType]: ...
    
    @staticmethod
    def CreateClientWebSocket(innerStream: Stream, subProtocol: StringType, receiveBufferSize: IntType, sendBufferSize: IntType, keepAliveInterval: TimeSpan, useZeroMaskingKey: BooleanType, internalBuffer: ArraySegment[ByteType]) -> WebSocket: ...
    
    @staticmethod
    def CreateServerBuffer(receiveBufferSize: IntType) -> ArraySegment[ByteType]: ...
    
    def Dispose(self) -> VoidType: ...
    
    @staticmethod
    def IsApplicationTargeting45() -> BooleanType: ...
    
    def ReceiveAsync(self, buffer: ArraySegment[ByteType], cancellationToken: CancellationToken) -> Task[WebSocketReceiveResult]: ...
    
    @staticmethod
    def RegisterPrefixes() -> VoidType: ...
    
    def SendAsync(self, buffer: ArraySegment[ByteType], messageType: WebSocketMessageType, endOfMessage: BooleanType, cancellationToken: CancellationToken) -> Task: ...
    
    def get_CloseStatus(self) -> NullableType[Nullable[WebSocketCloseStatus]]: ...
    
    def get_CloseStatusDescription(self) -> StringType: ...
    
    @staticmethod
    def get_DefaultKeepAliveInterval() -> TimeSpan: ...
    
    def get_State(self) -> WebSocketState: ...
    
    def get_SubProtocol(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebSocket(ABC, ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CloseStatus(self) -> NullableType[Nullable[WebSocketCloseStatus]]: ...
    
    @property
    def CloseStatusDescription(self) -> StringType: ...
    
    @staticmethod
    @property
    def DefaultKeepAliveInterval() -> TimeSpan: ...
    
    @property
    def State(self) -> WebSocketState: ...
    
    @property
    def SubProtocol(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Abort(self) -> VoidType: ...
    
    def CloseAsync(self, closeStatus: WebSocketCloseStatus, statusDescription: StringType, cancellationToken: CancellationToken) -> Task: ...
    
    def CloseOutputAsync(self, closeStatus: WebSocketCloseStatus, statusDescription: StringType, cancellationToken: CancellationToken) -> Task: ...
    
    @staticmethod
    def CreateClientBuffer(receiveBufferSize: IntType, sendBufferSize: IntType) -> ArraySegment[ByteType]: ...
    
    @staticmethod
    def CreateClientWebSocket(innerStream: Stream, subProtocol: StringType, receiveBufferSize: IntType, sendBufferSize: IntType, keepAliveInterval: TimeSpan, useZeroMaskingKey: BooleanType, internalBuffer: ArraySegment[ByteType]) -> WebSocket: ...
    
    @staticmethod
    def CreateServerBuffer(receiveBufferSize: IntType) -> ArraySegment[ByteType]: ...
    
    def Dispose(self) -> VoidType: ...
    
    @staticmethod
    def IsApplicationTargeting45() -> BooleanType: ...
    
    def ReceiveAsync(self, buffer: ArraySegment[ByteType], cancellationToken: CancellationToken) -> Task[WebSocketReceiveResult]: ...
    
    @staticmethod
    def RegisterPrefixes() -> VoidType: ...
    
    def SendAsync(self, buffer: ArraySegment[ByteType], messageType: WebSocketMessageType, endOfMessage: BooleanType, cancellationToken: CancellationToken) -> Task: ...
    
    def get_CloseStatus(self) -> NullableType[Nullable[WebSocketCloseStatus]]: ...
    
    def get_CloseStatusDescription(self) -> StringType: ...
    
    @staticmethod
    def get_DefaultKeepAliveInterval() -> TimeSpan: ...
    
    def get_State(self) -> WebSocketState: ...
    
    def get_SubProtocol(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebSocketBase(ABC, WebSocket, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CloseStatus(self) -> NullableType[Nullable[WebSocketCloseStatus]]: ...
    
    @property
    def CloseStatusDescription(self) -> StringType: ...
    
    @property
    def State(self) -> WebSocketState: ...
    
    @property
    def SubProtocol(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Abort(self) -> VoidType: ...
    
    def CloseAsync(self, closeStatus: WebSocketCloseStatus, statusDescription: StringType, cancellationToken: CancellationToken) -> Task: ...
    
    def CloseOutputAsync(self, closeStatus: WebSocketCloseStatus, statusDescription: StringType, cancellationToken: CancellationToken) -> Task: ...
    
    def Dispose(self) -> VoidType: ...
    
    def ReceiveAsync(self, buffer: ArraySegment[ByteType], cancellationToken: CancellationToken) -> Task[WebSocketReceiveResult]: ...
    
    def SendAsync(self, buffer: ArraySegment[ByteType], messageType: WebSocketMessageType, endOfMessage: BooleanType, cancellationToken: CancellationToken) -> Task: ...
    
    def get_CloseStatus(self) -> NullableType[Nullable[WebSocketCloseStatus]]: ...
    
    def get_CloseStatusDescription(self) -> StringType: ...
    
    def get_State(self) -> WebSocketState: ...
    
    def get_SubProtocol(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebSocketBase(ABC, WebSocket, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CloseStatus(self) -> NullableType[Nullable[WebSocketCloseStatus]]: ...
    
    @property
    def CloseStatusDescription(self) -> StringType: ...
    
    @property
    def State(self) -> WebSocketState: ...
    
    @property
    def SubProtocol(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Abort(self) -> VoidType: ...
    
    def CloseAsync(self, closeStatus: WebSocketCloseStatus, statusDescription: StringType, cancellationToken: CancellationToken) -> Task: ...
    
    def CloseOutputAsync(self, closeStatus: WebSocketCloseStatus, statusDescription: StringType, cancellationToken: CancellationToken) -> Task: ...
    
    def Dispose(self) -> VoidType: ...
    
    def ReceiveAsync(self, buffer: ArraySegment[ByteType], cancellationToken: CancellationToken) -> Task[WebSocketReceiveResult]: ...
    
    def SendAsync(self, buffer: ArraySegment[ByteType], messageType: WebSocketMessageType, endOfMessage: BooleanType, cancellationToken: CancellationToken) -> Task: ...
    
    def get_CloseStatus(self) -> NullableType[Nullable[WebSocketCloseStatus]]: ...
    
    def get_CloseStatusDescription(self) -> StringType: ...
    
    def get_State(self) -> WebSocketState: ...
    
    def get_SubProtocol(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebSocketBuffer(ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ReceiveBufferSize(self) -> IntType: ...
    
    @property
    def SendBufferSize(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Dispose(self, webSocketState: WebSocketState) -> VoidType: ...
    
    @overload
    def Dispose(self) -> VoidType: ...
    
    def get_ReceiveBufferSize(self) -> IntType: ...
    
    def get_SendBufferSize(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebSocketBuffer(ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ReceiveBufferSize(self) -> IntType: ...
    
    @property
    def SendBufferSize(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Dispose(self, webSocketState: WebSocketState) -> VoidType: ...
    
    @overload
    def Dispose(self) -> VoidType: ...
    
    def get_ReceiveBufferSize(self) -> IntType: ...
    
    def get_SendBufferSize(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebSocketConnectionStream(BufferedReadStream, IDisposable, IWebSocketStream):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, connectStream: ConnectStream, connectionGroupName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CanRead(self) -> BooleanType: ...
    
    @property
    def CanSeek(self) -> BooleanType: ...
    
    @property
    def CanWrite(self) -> BooleanType: ...
    
    @property
    def SupportsMultipleWrite(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Abort(self) -> VoidType: ...
    
    def Close(self) -> VoidType: ...
    
    def CloseNetworkConnectionAsync(self, cancellationToken: CancellationToken) -> Task: ...
    
    def MultipleWriteAsync(self, sendBuffers: IList[ArraySegment[ByteType]], cancellationToken: CancellationToken) -> Task: ...
    
    @overload
    def ReadAsync(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, cancellationToken: CancellationToken) -> Task[IntType]: ...
    
    def SwitchToOpaqueMode(self, webSocket: WebSocketBase) -> VoidType: ...
    
    @overload
    def WriteAsync(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, cancellationToken: CancellationToken) -> Task: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanSeek(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_SupportsMultipleWrite(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebSocketConnectionStream(BufferedReadStream, IDisposable, IWebSocketStream):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, connectStream: ConnectStream, connectionGroupName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CanRead(self) -> BooleanType: ...
    
    @property
    def CanSeek(self) -> BooleanType: ...
    
    @property
    def CanWrite(self) -> BooleanType: ...
    
    @property
    def SupportsMultipleWrite(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Abort(self) -> VoidType: ...
    
    def Close(self) -> VoidType: ...
    
    def CloseNetworkConnectionAsync(self, cancellationToken: CancellationToken) -> Task: ...
    
    def MultipleWriteAsync(self, sendBuffers: IList[ArraySegment[ByteType]], cancellationToken: CancellationToken) -> Task: ...
    
    @overload
    def ReadAsync(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, cancellationToken: CancellationToken) -> Task[IntType]: ...
    
    def SwitchToOpaqueMode(self, webSocket: WebSocketBase) -> VoidType: ...
    
    @overload
    def WriteAsync(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, cancellationToken: CancellationToken) -> Task: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanSeek(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_SupportsMultipleWrite(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebSocketContext(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CookieCollection(self) -> CookieCollection: ...
    
    @property
    def Headers(self) -> NameValueCollection: ...
    
    @property
    def IsAuthenticated(self) -> BooleanType: ...
    
    @property
    def IsLocal(self) -> BooleanType: ...
    
    @property
    def IsSecureConnection(self) -> BooleanType: ...
    
    @property
    def Origin(self) -> StringType: ...
    
    @property
    def RequestUri(self) -> Uri: ...
    
    @property
    def SecWebSocketKey(self) -> StringType: ...
    
    @property
    def SecWebSocketProtocols(self) -> IEnumerable[StringType]: ...
    
    @property
    def SecWebSocketVersion(self) -> StringType: ...
    
    @property
    def User(self) -> IPrincipal: ...
    
    @property
    def WebSocket(self) -> WebSocket: ...
    
    # ---------- Methods ---------- #
    
    def get_CookieCollection(self) -> CookieCollection: ...
    
    def get_Headers(self) -> NameValueCollection: ...
    
    def get_IsAuthenticated(self) -> BooleanType: ...
    
    def get_IsLocal(self) -> BooleanType: ...
    
    def get_IsSecureConnection(self) -> BooleanType: ...
    
    def get_Origin(self) -> StringType: ...
    
    def get_RequestUri(self) -> Uri: ...
    
    def get_SecWebSocketKey(self) -> StringType: ...
    
    def get_SecWebSocketProtocols(self) -> IEnumerable[StringType]: ...
    
    def get_SecWebSocketVersion(self) -> StringType: ...
    
    def get_User(self) -> IPrincipal: ...
    
    def get_WebSocket(self) -> WebSocket: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebSocketContext(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CookieCollection(self) -> CookieCollection: ...
    
    @property
    def Headers(self) -> NameValueCollection: ...
    
    @property
    def IsAuthenticated(self) -> BooleanType: ...
    
    @property
    def IsLocal(self) -> BooleanType: ...
    
    @property
    def IsSecureConnection(self) -> BooleanType: ...
    
    @property
    def Origin(self) -> StringType: ...
    
    @property
    def RequestUri(self) -> Uri: ...
    
    @property
    def SecWebSocketKey(self) -> StringType: ...
    
    @property
    def SecWebSocketProtocols(self) -> IEnumerable[StringType]: ...
    
    @property
    def SecWebSocketVersion(self) -> StringType: ...
    
    @property
    def User(self) -> IPrincipal: ...
    
    @property
    def WebSocket(self) -> WebSocket: ...
    
    # ---------- Methods ---------- #
    
    def get_CookieCollection(self) -> CookieCollection: ...
    
    def get_Headers(self) -> NameValueCollection: ...
    
    def get_IsAuthenticated(self) -> BooleanType: ...
    
    def get_IsLocal(self) -> BooleanType: ...
    
    def get_IsSecureConnection(self) -> BooleanType: ...
    
    def get_Origin(self) -> StringType: ...
    
    def get_RequestUri(self) -> Uri: ...
    
    def get_SecWebSocketKey(self) -> StringType: ...
    
    def get_SecWebSocketProtocols(self) -> IEnumerable[StringType]: ...
    
    def get_SecWebSocketVersion(self) -> StringType: ...
    
    def get_User(self) -> IPrincipal: ...
    
    def get_WebSocket(self) -> WebSocket: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebSocketException(Win32Exception, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, error: WebSocketError): ...
    
    @overload
    def __init__(self, error: WebSocketError, message: StringType): ...
    
    @overload
    def __init__(self, error: WebSocketError, innerException: Exception): ...
    
    @overload
    def __init__(self, error: WebSocketError, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self, nativeError: IntType): ...
    
    @overload
    def __init__(self, nativeError: IntType, message: StringType): ...
    
    @overload
    def __init__(self, nativeError: IntType, innerException: Exception): ...
    
    @overload
    def __init__(self, error: WebSocketError, nativeError: IntType): ...
    
    @overload
    def __init__(self, error: WebSocketError, nativeError: IntType, message: StringType): ...
    
    @overload
    def __init__(self, error: WebSocketError, nativeError: IntType, innerException: Exception): ...
    
    @overload
    def __init__(self, error: WebSocketError, nativeError: IntType, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ErrorCode(self) -> IntType: ...
    
    @property
    def WebSocketErrorCode(self) -> WebSocketError: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def get_ErrorCode(self) -> IntType: ...
    
    def get_WebSocketErrorCode(self) -> WebSocketError: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebSocketException(Win32Exception, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, error: WebSocketError): ...
    
    @overload
    def __init__(self, error: WebSocketError, message: StringType): ...
    
    @overload
    def __init__(self, error: WebSocketError, innerException: Exception): ...
    
    @overload
    def __init__(self, error: WebSocketError, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self, nativeError: IntType): ...
    
    @overload
    def __init__(self, nativeError: IntType, message: StringType): ...
    
    @overload
    def __init__(self, nativeError: IntType, innerException: Exception): ...
    
    @overload
    def __init__(self, error: WebSocketError, nativeError: IntType): ...
    
    @overload
    def __init__(self, error: WebSocketError, nativeError: IntType, message: StringType): ...
    
    @overload
    def __init__(self, error: WebSocketError, nativeError: IntType, innerException: Exception): ...
    
    @overload
    def __init__(self, error: WebSocketError, nativeError: IntType, message: StringType, innerException: Exception): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ErrorCode(self) -> IntType: ...
    
    @property
    def WebSocketErrorCode(self) -> WebSocketError: ...
    
    # ---------- Methods ---------- #
    
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> VoidType: ...
    
    def get_ErrorCode(self) -> IntType: ...
    
    def get_WebSocketErrorCode(self) -> WebSocketError: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebSocketHelpers(ABC, ObjectType):
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


class WebSocketHelpers(ABC, ObjectType):
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


class WebSocketHttpListenerDuplexStream(Stream, IDisposable, IWebSocketStream):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, inputStream: HttpRequestStream, outputStream: HttpResponseStream, context: HttpListenerContext): ...
    
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
    def SupportsMultipleWrite(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Abort(self) -> VoidType: ...
    
    def BeginRead(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def BeginWrite(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def CloseNetworkConnectionAsync(self, cancellationToken: CancellationToken) -> Task: ...
    
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task: ...
    
    def MultipleWriteAsync(self, sendBuffers: IList[ArraySegment[ByteType]], cancellationToken: CancellationToken) -> Task: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    
    @overload
    def ReadAsync(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, cancellationToken: CancellationToken) -> Task[IntType]: ...
    
    def ReadByte(self) -> IntType: ...
    
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def SwitchToOpaqueMode(self, webSocket: WebSocketBase) -> VoidType: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteAsync(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, cancellationToken: CancellationToken) -> Task: ...
    
    def WriteByte(self, value: ByteType) -> VoidType: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanSeek(self) -> BooleanType: ...
    
    def get_CanTimeout(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_Length(self) -> LongType: ...
    
    def get_Position(self) -> LongType: ...
    
    def get_SupportsMultipleWrite(self) -> BooleanType: ...
    
    def set_Position(self, value: LongType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebSocketHttpListenerDuplexStream(Stream, IDisposable, IWebSocketStream):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, inputStream: HttpRequestStream, outputStream: HttpResponseStream, context: HttpListenerContext): ...
    
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
    def SupportsMultipleWrite(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def Abort(self) -> VoidType: ...
    
    def BeginRead(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def BeginWrite(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def CloseNetworkConnectionAsync(self, cancellationToken: CancellationToken) -> Task: ...
    
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task: ...
    
    def MultipleWriteAsync(self, sendBuffers: IList[ArraySegment[ByteType]], cancellationToken: CancellationToken) -> Task: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    
    @overload
    def ReadAsync(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, cancellationToken: CancellationToken) -> Task[IntType]: ...
    
    def ReadByte(self) -> IntType: ...
    
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def SwitchToOpaqueMode(self, webSocket: WebSocketBase) -> VoidType: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteAsync(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, cancellationToken: CancellationToken) -> Task: ...
    
    def WriteByte(self, value: ByteType) -> VoidType: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanSeek(self) -> BooleanType: ...
    
    def get_CanTimeout(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_Length(self) -> LongType: ...
    
    def get_Position(self) -> LongType: ...
    
    def get_SupportsMultipleWrite(self) -> BooleanType: ...
    
    def set_Position(self, value: LongType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebSocketProtocolComponent(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Succeeded(hr: IntType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebSocketProtocolComponent(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def Succeeded(hr: IntType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebSocketReceiveResult(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, count: IntType, messageType: WebSocketMessageType, endOfMessage: BooleanType): ...
    
    @overload
    def __init__(self, count: IntType, messageType: WebSocketMessageType, endOfMessage: BooleanType, closeStatus: NullableType[Nullable[WebSocketCloseStatus]], closeStatusDescription: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CloseStatus(self) -> NullableType[Nullable[WebSocketCloseStatus]]: ...
    
    @property
    def CloseStatusDescription(self) -> StringType: ...
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def EndOfMessage(self) -> BooleanType: ...
    
    @property
    def MessageType(self) -> WebSocketMessageType: ...
    
    # ---------- Methods ---------- #
    
    def get_CloseStatus(self) -> NullableType[Nullable[WebSocketCloseStatus]]: ...
    
    def get_CloseStatusDescription(self) -> StringType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_EndOfMessage(self) -> BooleanType: ...
    
    def get_MessageType(self) -> WebSocketMessageType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WebSocketReceiveResult(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, count: IntType, messageType: WebSocketMessageType, endOfMessage: BooleanType): ...
    
    @overload
    def __init__(self, count: IntType, messageType: WebSocketMessageType, endOfMessage: BooleanType, closeStatus: NullableType[Nullable[WebSocketCloseStatus]], closeStatusDescription: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CloseStatus(self) -> NullableType[Nullable[WebSocketCloseStatus]]: ...
    
    @property
    def CloseStatusDescription(self) -> StringType: ...
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def EndOfMessage(self) -> BooleanType: ...
    
    @property
    def MessageType(self) -> WebSocketMessageType: ...
    
    # ---------- Methods ---------- #
    
    def get_CloseStatus(self) -> NullableType[Nullable[WebSocketCloseStatus]]: ...
    
    def get_CloseStatusDescription(self) -> StringType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_EndOfMessage(self) -> BooleanType: ...
    
    def get_MessageType(self) -> WebSocketMessageType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# No Interfaces

# ---------- Enums ---------- #

class WebSocketCloseStatus(Enum):
    NormalClosure: IntType = 1000
    EndpointUnavailable: IntType = 1001
    ProtocolError: IntType = 1002
    InvalidMessageType: IntType = 1003
    Empty: IntType = 1005
    InvalidPayloadData: IntType = 1007
    PolicyViolation: IntType = 1008
    MessageTooBig: IntType = 1009
    MandatoryExtension: IntType = 1010
    InternalServerError: IntType = 1011


class WebSocketCloseStatus(Enum):
    NormalClosure: IntType = 1000
    EndpointUnavailable: IntType = 1001
    ProtocolError: IntType = 1002
    InvalidMessageType: IntType = 1003
    Empty: IntType = 1005
    InvalidPayloadData: IntType = 1007
    PolicyViolation: IntType = 1008
    MessageTooBig: IntType = 1009
    MandatoryExtension: IntType = 1010
    InternalServerError: IntType = 1011


class WebSocketError(Enum):
    Success: IntType = 0
    InvalidMessageType: IntType = 1
    Faulted: IntType = 2
    NativeError: IntType = 3
    NotAWebSocket: IntType = 4
    UnsupportedVersion: IntType = 5
    UnsupportedProtocol: IntType = 6
    HeaderError: IntType = 7
    ConnectionClosedPrematurely: IntType = 8
    InvalidState: IntType = 9


class WebSocketError(Enum):
    Success: IntType = 0
    InvalidMessageType: IntType = 1
    Faulted: IntType = 2
    NativeError: IntType = 3
    NotAWebSocket: IntType = 4
    UnsupportedVersion: IntType = 5
    UnsupportedProtocol: IntType = 6
    HeaderError: IntType = 7
    ConnectionClosedPrematurely: IntType = 8
    InvalidState: IntType = 9


class WebSocketMessageType(Enum):
    Text: IntType = 0
    Binary: IntType = 1
    Close: IntType = 2


class WebSocketMessageType(Enum):
    Text: IntType = 0
    Binary: IntType = 1
    Close: IntType = 2


class WebSocketState(Enum):
    #None: IntType = 0
    Connecting: IntType = 1
    Open: IntType = 2
    CloseSent: IntType = 3
    CloseReceived: IntType = 4
    Closed: IntType = 5
    Aborted: IntType = 6


class WebSocketState(Enum):
    #None: IntType = 0
    Connecting: IntType = 1
    Open: IntType = 2
    CloseSent: IntType = 3
    CloseReceived: IntType = 4
    Closed: IntType = 5
    Aborted: IntType = 6


# No Delegates

__all__ = [
    ClientWebSocket,
    ClientWebSocketOptions,
    HttpListenerWebSocketContext,
    InternalClientWebSocket,
    ServerWebSocket,
    WebSocket,
    WebSocketBase,
    WebSocketBuffer,
    WebSocketConnectionStream,
    WebSocketContext,
    WebSocketException,
    WebSocketHelpers,
    WebSocketHttpListenerDuplexStream,
    WebSocketProtocolComponent,
    WebSocketReceiveResult,
    WebSocketCloseStatus,
    WebSocketError,
    WebSocketMessageType,
    WebSocketState,
]
