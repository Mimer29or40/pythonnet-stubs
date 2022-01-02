__all__ = [
    'IPv6MulticastOption',
    'LingerOption',
    'MulticastOption',
    'NetworkStream',
    'SafeSocketHandle',
    'SendPacketsElement',
    'Socket',
    'SocketAsyncEventArgs',
    'SocketException',
    'SocketTaskExtensions',
    'TcpClient',
    'TcpListener',
    'UdpClient',
    'UnixDomainSocketEndPoint',
    'IPPacketInformation',
    'SocketInformation',
    'SocketReceiveFromResult',
    'SocketReceiveMessageFromResult',
    'UdpReceiveResult',
    'AddressFamily',
    'IOControlCode',
    'IPProtectionLevel',
    'ProtocolFamily',
    'ProtocolType',
    'SelectMode',
    'SocketAsyncOperation',
    'SocketError',
    'SocketFlags',
    'SocketInformationOptions',
    'SocketOptionLevel',
    'SocketOptionName',
    'SocketShutdown',
    'SocketType',
    'TransmitFileOptions',
]


# TODO

# ---------- CLASSES ---------- #

class IPv6MulticastOption:
    """Contains option values for joining an IPv6 multicast group."""


class LingerOption:
    """Specifies whether a Socket will remain connected after a call to the Close() or Close() methods and the length of time it will remain connected, if data remains to be sent."""


class MulticastOption:
    """Contains IPAddress values used to join and drop multicast groups."""


class NetworkStream:
    """Provides the underlying stream of data for network access."""


class SafeSocketHandle:
    """Represents a wrapper class for a socket handle."""


class SendPacketsElement:
    """Represents an element in a SendPacketsElement array."""


class Socket:
    """Implements the Berkeley sockets interface."""


class SocketAsyncEventArgs:
    """Represents an asynchronous socket operation."""


class SocketException:
    """The exception that is thrown when a socket error occurs."""


class SocketTaskExtensions:
    """This class contains extension methods to the Socket class."""


class TcpClient:
    """Provides client connections for TCP network services."""


class TcpListener:
    """Listens for connections from TCP network clients."""


class UdpClient:
    """Provides User Datagram Protocol (UDP) network services."""


class UnixDomainSocketEndPoint:
    """Represents a Unix Domain Socket endpoint as a path."""


# ---------- STRUCTS ---------- #

class IPPacketInformation:
    """Presents the packet information from a call to ReceiveMessageFrom(Byte[], Int32, Int32, SocketFlags, EndPoint, IPPacketInformation) or EndReceiveMessageFrom(IAsyncResult, SocketFlags, EndPoint, IPPacketInformation)."""


class SocketInformation:
    """Encapsulates the information that is necessary to duplicate a Socket."""


class SocketReceiveFromResult:
    """The result of a ReceiveFromAsync(Socket, ArraySegment<Byte>, SocketFlags, EndPoint) operation."""


class SocketReceiveMessageFromResult:
    """The result of a ReceiveMessageFromAsync(Socket, ArraySegment<Byte>, SocketFlags, EndPoint) operation."""


class UdpReceiveResult:
    """Presents UDP receive result information from a call to the ReceiveAsync() method."""


# ---------- ENUMS ---------- #

class AddressFamily:
    """Specifies the addressing scheme that an instance of the Socket class can use."""


class IOControlCode:
    """Specifies the IO control codes supported by the IOControl(Int32, Byte[], Byte[]) method."""


class IPProtectionLevel:
    """A value that enables restriction of an IPv6 socket to a specified scope, such as addresses with the same link local or site local prefix."""


class ProtocolFamily:
    """Specifies the type of protocol that an instance of the Socket class can use."""


class ProtocolType:
    """Specifies the protocols that the Socket class supports."""


class SelectMode:
    """Defines the polling modes for the Poll(Int32, SelectMode) method."""


class SocketAsyncOperation:
    """The type of asynchronous socket operation most recently performed with this context object."""


class SocketError:
    """Defines error codes for the Socket class."""


class SocketFlags:
    """Specifies socket send and receive behaviors."""


class SocketInformationOptions:
    """Describes states for a Socket."""


class SocketOptionLevel:
    """Defines socket option levels for the SetSocketOption(SocketOptionLevel, SocketOptionName, Int32) and GetSocketOption(SocketOptionLevel, SocketOptionName) methods."""


class SocketOptionName:
    """Defines configuration option names."""


class SocketShutdown:
    """Defines constants that are used by the Shutdown(SocketShutdown) method."""


class SocketType:
    """Specifies the type of socket that an instance of the Socket class represents."""


class TransmitFileOptions:
    """The TransmitFileOptions enumeration defines values used in file transfer requests."""
