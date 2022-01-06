__all__ = [
    'ClientWebSocket',
    'ClientWebSocketOptions',
    'HttpListenerWebSocketContext',
    'WebSocket',
    'WebSocketContext',
    'WebSocketCreationOptions',
    'WebSocketDeflateOptions',
    'WebSocketException',
    'WebSocketReceiveResult',
    'ValueWebSocketReceiveResult',
    'WebSocketCloseStatus',
    'WebSocketError',
    'WebSocketMessageFlags',
    'WebSocketMessageType',
    'WebSocketState',
]


# TODO

# ---------- CLASSES ---------- #

class ClientWebSocket:
    """Provides a client for connecting to WebSocket services."""


class ClientWebSocketOptions:
    """Options to use with a ClientWebSocket object."""


class HttpListenerWebSocketContext:
    """Provides access to information received by the HttpListener class when accepting WebSocket connections."""


class WebSocket:
    """The WebSocket class allows applications to send and receive data after the WebSocket upgrade has completed."""


class WebSocketContext:
    """Used for accessing the information in the WebSocket handshake."""


class WebSocketCreationOptions:
    """Options that control how a WebSocket is created."""


class WebSocketDeflateOptions:
    """Options to enable per-message deflate compression for WebSocket."""


class WebSocketException:
    """Represents an exception that occurred when performing an operation on a WebSocket connection."""


class WebSocketReceiveResult:
    """An instance of this class represents the result of performing a single ReceiveAsync operation on a WebSocket."""


# ---------- STRUCTS ---------- #

class ValueWebSocketReceiveResult:
    """Represents the result of performing a single ReceiveAsync(Memory<Byte>, CancellationToken) operation on a WebSocket."""


# ---------- ENUMS ---------- #

class WebSocketCloseStatus:
    """Represents well known WebSocket close codes as defined in section 11.7 of the WebSocket protocol spec."""


class WebSocketError:
    """Contains the list of possible WebSocket errors."""


class WebSocketMessageFlags:
    """Flags for controlling how the WebSocket should send a message."""


class WebSocketMessageType:
    """Indicates the message type."""


class WebSocketState:
    """Defines the different states a WebSockets instance can be in."""
