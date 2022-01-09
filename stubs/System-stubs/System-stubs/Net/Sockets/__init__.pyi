from __future__ import annotations

from abc import ABC
from typing import Callable, Generic, List, Tuple, TypeVar, Union, overload

from System import Array, ArraySegment, AsyncCallback, Boolean, Byte, Enum, EventArgs, EventHandler, Exception, IAsyncResult, ICloneable, IDisposable, IEquatable, Int16, Int32, Int64, IntPtr, MulticastDelegate, Object, String, ValueType, Void
from System.Collections import IList
from System.Collections.Generic import IList
from System.ComponentModel import Win32Exception
from System.IO import FileAccess, SeekOrigin, Stream
from System.Net import ContextAwareResult, DnsEndPoint, EndPoint, IPAddress, IPEndPoint, SafeCloseSocket, SafeNativeOverlapped
from System.Runtime.InteropServices import SafeHandle, _Exception
from System.Runtime.Serialization import ISerializable
from System.Threading import CancellationToken
from System.Threading.Tasks import Task

# ---------- Types ---------- #

T = TypeVar('T')

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
ObjectType = Object
ShortType = Union[int, Int16]
StringType = Union[str, String]
VoidType = Union[None, Void]


class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    
    def __isub__(self, other: T): ...


# ---------- Classes ---------- #

class AcceptAsyncResult(ContextAwareResult, IAsyncResult):
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


class AcceptExDelegate(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, listenSocketHandle: SafeCloseSocket, acceptSocketHandle: SafeCloseSocket, buffer: NIntType, len: IntType, localAddressLength: IntType, remoteAddressLength: IntType, bytesReceived: IntType, overlapped: SafeHandle, callback: AsyncCallback, object: ObjectType) -> Tuple[IAsyncResult, IntType]: ...
    
    def EndInvoke(self, bytesReceived: IntType, result: IAsyncResult) -> Tuple[BooleanType, IntType]: ...
    
    def Invoke(self, listenSocketHandle: SafeCloseSocket, acceptSocketHandle: SafeCloseSocket, buffer: NIntType, len: IntType, localAddressLength: IntType, remoteAddressLength: IntType, bytesReceived: IntType, overlapped: SafeHandle) -> Tuple[BooleanType, IntType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AcceptOverlappedAsyncResult(BaseOverlappedAsyncResult, IAsyncResult):
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


class BaseOverlappedAsyncResult(ContextAwareResult, IAsyncResult):
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


class ConnectAsyncResult(ContextAwareResult, IAsyncResult):
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


class ConnectExDelegate(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, socketHandle: SafeCloseSocket, socketAddress: NIntType, socketAddressSize: IntType, buffer: NIntType, dataLength: IntType, bytesSent: IntType, overlapped: SafeHandle, callback: AsyncCallback, object: ObjectType) -> Tuple[IAsyncResult, IntType]: ...
    
    def EndInvoke(self, bytesSent: IntType, result: IAsyncResult) -> Tuple[BooleanType, IntType]: ...
    
    def Invoke(self, socketHandle: SafeCloseSocket, socketAddress: NIntType, socketAddressSize: IntType, buffer: NIntType, dataLength: IntType, bytesSent: IntType, overlapped: SafeHandle) -> Tuple[BooleanType, IntType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ConnectOverlappedAsyncResult(BaseOverlappedAsyncResult, IAsyncResult):
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


class DisconnectExDelegate(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, socketHandle: SafeCloseSocket, overlapped: SafeHandle, flags: IntType, reserved: IntType, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> BooleanType: ...
    
    def Invoke(self, socketHandle: SafeCloseSocket, overlapped: SafeHandle, flags: IntType, reserved: IntType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DisconnectExDelegate_Blocking(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, socketHandle: NIntType, overlapped: NIntType, flags: IntType, reserved: IntType, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> BooleanType: ...
    
    def Invoke(self, socketHandle: NIntType, overlapped: NIntType, flags: IntType, reserved: IntType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DisconnectOverlappedAsyncResult(BaseOverlappedAsyncResult, IAsyncResult):
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


class DynamicWinsockMethods(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetDelegate(self, socketHandle: SafeCloseSocket) -> T: ...
    
    @staticmethod
    def GetMethods(addressFamily: AddressFamily, socketType: SocketType, protocolType: ProtocolType) -> DynamicWinsockMethods: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GetAcceptExSockaddrsDelegate(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, buffer: NIntType, receiveDataLength: IntType, localAddressLength: IntType, remoteAddressLength: IntType, localSocketAddress: NIntType, localSocketAddressLength: IntType, remoteSocketAddress: NIntType, remoteSocketAddressLength: IntType, callback: AsyncCallback, object: ObjectType) -> Tuple[IAsyncResult, NIntType, IntType, NIntType, IntType]: ...
    
    def EndInvoke(self, localSocketAddress: NIntType, localSocketAddressLength: IntType, remoteSocketAddress: NIntType, remoteSocketAddressLength: IntType, result: IAsyncResult) -> Tuple[VoidType, NIntType, IntType, NIntType, IntType]: ...
    
    def Invoke(self, buffer: NIntType, receiveDataLength: IntType, localAddressLength: IntType, remoteAddressLength: IntType, localSocketAddress: NIntType, localSocketAddressLength: IntType, remoteSocketAddress: NIntType, remoteSocketAddressLength: IntType) -> Tuple[VoidType, NIntType, IntType, NIntType, IntType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IPv6MulticastOption(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, group: IPAddress, ifindex: LongType): ...
    
    @overload
    def __init__(self, group: IPAddress): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Group(self) -> IPAddress: ...
    
    @Group.setter
    def Group(self, value: IPAddress) -> None: ...
    
    @property
    def InterfaceIndex(self) -> LongType: ...
    
    @InterfaceIndex.setter
    def InterfaceIndex(self, value: LongType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Group(self) -> IPAddress: ...
    
    def get_InterfaceIndex(self) -> LongType: ...
    
    def set_Group(self, value: IPAddress) -> VoidType: ...
    
    def set_InterfaceIndex(self, value: LongType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IoctlSocketConstants(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def FIOASYNC() -> IntType: ...
    
    @staticmethod
    @property
    def FIONBIO() -> IntType: ...
    
    @staticmethod
    @property
    def FIONREAD() -> IntType: ...
    
    @staticmethod
    @property
    def SIOGETEXTENSIONFUNCTIONPOINTER() -> IntType: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class LingerOption(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, enable: BooleanType, seconds: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Enabled(self) -> BooleanType: ...
    
    @Enabled.setter
    def Enabled(self, value: BooleanType) -> None: ...
    
    @property
    def LingerTime(self) -> IntType: ...
    
    @LingerTime.setter
    def LingerTime(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Enabled(self) -> BooleanType: ...
    
    def get_LingerTime(self) -> IntType: ...
    
    def set_Enabled(self, value: BooleanType) -> VoidType: ...
    
    def set_LingerTime(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MulticastOption(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, group: IPAddress, mcint: IPAddress): ...
    
    @overload
    def __init__(self, group: IPAddress, interfaceIndex: IntType): ...
    
    @overload
    def __init__(self, group: IPAddress): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Group(self) -> IPAddress: ...
    
    @Group.setter
    def Group(self, value: IPAddress) -> None: ...
    
    @property
    def InterfaceIndex(self) -> IntType: ...
    
    @InterfaceIndex.setter
    def InterfaceIndex(self, value: IntType) -> None: ...
    
    @property
    def LocalAddress(self) -> IPAddress: ...
    
    @LocalAddress.setter
    def LocalAddress(self, value: IPAddress) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Group(self) -> IPAddress: ...
    
    def get_InterfaceIndex(self) -> IntType: ...
    
    def get_LocalAddress(self) -> IPAddress: ...
    
    def set_Group(self, value: IPAddress) -> VoidType: ...
    
    def set_InterfaceIndex(self, value: IntType) -> VoidType: ...
    
    def set_LocalAddress(self, value: IPAddress) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MultipleConnectAsync(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Cancel(self) -> VoidType: ...
    
    def StartConnectAsync(self, args: SocketAsyncEventArgs, endPoint: DnsEndPoint) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MultipleSocketMultipleConnectAsync(MultipleConnectAsync):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, socketType: SocketType, protocolType: ProtocolType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NetworkStream(Stream, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, socket: Socket): ...
    
    @overload
    def __init__(self, socket: Socket, ownsSocket: BooleanType): ...
    
    @overload
    def __init__(self, socket: Socket, access: FileAccess): ...
    
    @overload
    def __init__(self, socket: Socket, access: FileAccess, ownsSocket: BooleanType): ...
    
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
    def DataAvailable(self) -> BooleanType: ...
    
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
    
    def BeginRead(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def BeginWrite(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    @overload
    def Close(self, timeout: IntType) -> VoidType: ...
    
    def EndRead(self, asyncResult: IAsyncResult) -> IntType: ...
    
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task: ...
    
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType) -> Tuple[IntType, ArrayType[ByteType]]: ...
    
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    
    def SetLength(self, value: LongType) -> VoidType: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType) -> VoidType: ...
    
    def get_CanRead(self) -> BooleanType: ...
    
    def get_CanSeek(self) -> BooleanType: ...
    
    def get_CanTimeout(self) -> BooleanType: ...
    
    def get_CanWrite(self) -> BooleanType: ...
    
    def get_DataAvailable(self) -> BooleanType: ...
    
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


class OverlappedAsyncResult(BaseOverlappedAsyncResult, IAsyncResult):
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


class OverlappedCache(ObjectType):
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


class ReceiveMessageOverlappedAsyncResult(BaseOverlappedAsyncResult, IAsyncResult):
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


class SendPacketsElement(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, filepath: StringType): ...
    
    @overload
    def __init__(self, filepath: StringType, offset: IntType, count: IntType): ...
    
    @overload
    def __init__(self, filepath: StringType, offset: IntType, count: IntType, endOfPacket: BooleanType): ...
    
    @overload
    def __init__(self, buffer: ArrayType[ByteType]): ...
    
    @overload
    def __init__(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType): ...
    
    @overload
    def __init__(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, endOfPacket: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Buffer(self) -> ArrayType[ByteType]: ...
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def EndOfPacket(self) -> BooleanType: ...
    
    @property
    def FilePath(self) -> StringType: ...
    
    @property
    def Offset(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_Buffer(self) -> ArrayType[ByteType]: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_EndOfPacket(self) -> BooleanType: ...
    
    def get_FilePath(self) -> StringType: ...
    
    def get_Offset(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SingleSocketMultipleConnectAsync(MultipleConnectAsync):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, socket: Socket, userSocket: BooleanType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Socket(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, socketType: SocketType, protocolType: ProtocolType): ...
    
    @overload
    def __init__(self, addressFamily: AddressFamily, socketType: SocketType, protocolType: ProtocolType): ...
    
    @overload
    def __init__(self, socketInformation: SocketInformation): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AddressFamily(self) -> AddressFamily: ...
    
    @property
    def Available(self) -> IntType: ...
    
    @property
    def Blocking(self) -> BooleanType: ...
    
    @Blocking.setter
    def Blocking(self, value: BooleanType) -> None: ...
    
    @property
    def Connected(self) -> BooleanType: ...
    
    @property
    def DontFragment(self) -> BooleanType: ...
    
    @DontFragment.setter
    def DontFragment(self, value: BooleanType) -> None: ...
    
    @property
    def DualMode(self) -> BooleanType: ...
    
    @DualMode.setter
    def DualMode(self, value: BooleanType) -> None: ...
    
    @property
    def EnableBroadcast(self) -> BooleanType: ...
    
    @EnableBroadcast.setter
    def EnableBroadcast(self, value: BooleanType) -> None: ...
    
    @property
    def ExclusiveAddressUse(self) -> BooleanType: ...
    
    @ExclusiveAddressUse.setter
    def ExclusiveAddressUse(self, value: BooleanType) -> None: ...
    
    @property
    def Handle(self) -> NIntType: ...
    
    @property
    def IsBound(self) -> BooleanType: ...
    
    @property
    def LingerState(self) -> LingerOption: ...
    
    @LingerState.setter
    def LingerState(self, value: LingerOption) -> None: ...
    
    @property
    def LocalEndPoint(self) -> EndPoint: ...
    
    @property
    def MulticastLoopback(self) -> BooleanType: ...
    
    @MulticastLoopback.setter
    def MulticastLoopback(self, value: BooleanType) -> None: ...
    
    @property
    def NoDelay(self) -> BooleanType: ...
    
    @NoDelay.setter
    def NoDelay(self, value: BooleanType) -> None: ...
    
    @staticmethod
    @property
    def OSSupportsIPv4() -> BooleanType: ...
    
    @staticmethod
    @property
    def OSSupportsIPv6() -> BooleanType: ...
    
    @property
    def ProtocolType(self) -> ProtocolType: ...
    
    @property
    def ReceiveBufferSize(self) -> IntType: ...
    
    @ReceiveBufferSize.setter
    def ReceiveBufferSize(self, value: IntType) -> None: ...
    
    @property
    def ReceiveTimeout(self) -> IntType: ...
    
    @ReceiveTimeout.setter
    def ReceiveTimeout(self, value: IntType) -> None: ...
    
    @property
    def RemoteEndPoint(self) -> EndPoint: ...
    
    @property
    def SendBufferSize(self) -> IntType: ...
    
    @SendBufferSize.setter
    def SendBufferSize(self, value: IntType) -> None: ...
    
    @property
    def SendTimeout(self) -> IntType: ...
    
    @SendTimeout.setter
    def SendTimeout(self, value: IntType) -> None: ...
    
    @property
    def SocketType(self) -> SocketType: ...
    
    @staticmethod
    @property
    def SupportsIPv4() -> BooleanType: ...
    
    @staticmethod
    @property
    def SupportsIPv6() -> BooleanType: ...
    
    @property
    def Ttl(self) -> ShortType: ...
    
    @Ttl.setter
    def Ttl(self, value: ShortType) -> None: ...
    
    @property
    def UseOnlyOverlappedIO(self) -> BooleanType: ...
    
    @UseOnlyOverlappedIO.setter
    def UseOnlyOverlappedIO(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Accept(self) -> Socket: ...
    
    def AcceptAsync(self, e: SocketAsyncEventArgs) -> BooleanType: ...
    
    @overload
    def BeginAccept(self, receiveSize: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    @overload
    def BeginAccept(self, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    @overload
    def BeginAccept(self, acceptSocket: Socket, receiveSize: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    @overload
    def BeginConnect(self, remoteEP: EndPoint, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    @overload
    def BeginConnect(self, host: StringType, port: IntType, requestCallback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    @overload
    def BeginConnect(self, address: IPAddress, port: IntType, requestCallback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    @overload
    def BeginConnect(self, addresses: ArrayType[IPAddress], port: IntType, requestCallback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def BeginDisconnect(self, reuseSocket: BooleanType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    @overload
    def BeginReceive(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, socketFlags: SocketFlags, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    @overload
    def BeginReceive(self, buffers: IList[ArraySegment[ByteType]], socketFlags: SocketFlags, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    @overload
    def BeginReceive(self, buffers: IList[ArraySegment[ByteType]], socketFlags: SocketFlags, errorCode: SocketError, callback: AsyncCallback, state: ObjectType) -> Tuple[IAsyncResult, SocketError]: ...
    
    @overload
    def BeginReceive(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, socketFlags: SocketFlags, errorCode: SocketError, callback: AsyncCallback, state: ObjectType) -> Tuple[IAsyncResult, SocketError]: ...
    
    def BeginReceiveFrom(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, socketFlags: SocketFlags, remoteEP: EndPoint, callback: AsyncCallback, state: ObjectType) -> Tuple[IAsyncResult, EndPoint]: ...
    
    def BeginReceiveMessageFrom(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, socketFlags: SocketFlags, remoteEP: EndPoint, callback: AsyncCallback, state: ObjectType) -> Tuple[IAsyncResult, EndPoint]: ...
    
    @overload
    def BeginSend(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, socketFlags: SocketFlags, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    @overload
    def BeginSend(self, buffers: IList[ArraySegment[ByteType]], socketFlags: SocketFlags, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    @overload
    def BeginSend(self, buffers: IList[ArraySegment[ByteType]], socketFlags: SocketFlags, errorCode: SocketError, callback: AsyncCallback, state: ObjectType) -> Tuple[IAsyncResult, SocketError]: ...
    
    @overload
    def BeginSend(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, socketFlags: SocketFlags, errorCode: SocketError, callback: AsyncCallback, state: ObjectType) -> Tuple[IAsyncResult, SocketError]: ...
    
    @overload
    def BeginSendFile(self, fileName: StringType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    @overload
    def BeginSendFile(self, fileName: StringType, preBuffer: ArrayType[ByteType], postBuffer: ArrayType[ByteType], flags: TransmitFileOptions, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def BeginSendTo(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, socketFlags: SocketFlags, remoteEP: EndPoint, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def Bind(self, localEP: EndPoint) -> VoidType: ...
    
    @staticmethod
    def CancelConnectAsync(e: SocketAsyncEventArgs) -> VoidType: ...
    
    @overload
    def Close(self, timeout: IntType) -> VoidType: ...
    
    @overload
    def Close(self) -> VoidType: ...
    
    @overload
    def Connect(self, remoteEP: EndPoint) -> VoidType: ...
    
    @overload
    def Connect(self, address: IPAddress, port: IntType) -> VoidType: ...
    
    @overload
    def Connect(self, host: StringType, port: IntType) -> VoidType: ...
    
    @overload
    def Connect(self, addresses: ArrayType[IPAddress], port: IntType) -> VoidType: ...
    
    @overload
    def ConnectAsync(self, e: SocketAsyncEventArgs) -> BooleanType: ...
    
    @staticmethod
    @overload
    def ConnectAsync(socketType: SocketType, protocolType: ProtocolType, e: SocketAsyncEventArgs) -> BooleanType: ...
    
    def Disconnect(self, reuseSocket: BooleanType) -> VoidType: ...
    
    def DisconnectAsync(self, e: SocketAsyncEventArgs) -> BooleanType: ...
    
    def Dispose(self) -> VoidType: ...
    
    def DuplicateAndClose(self, targetProcessId: IntType) -> SocketInformation: ...
    
    @overload
    def EndAccept(self, asyncResult: IAsyncResult) -> Socket: ...
    
    @overload
    def EndAccept(self, buffer: ByteType, asyncResult: IAsyncResult) -> Tuple[Socket, ByteType]: ...
    
    @overload
    def EndAccept(self, buffer: ByteType, bytesTransferred: IntType, asyncResult: IAsyncResult) -> Tuple[Socket, ByteType, IntType]: ...
    
    def EndConnect(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    def EndDisconnect(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    @overload
    def EndReceive(self, asyncResult: IAsyncResult) -> IntType: ...
    
    @overload
    def EndReceive(self, asyncResult: IAsyncResult, errorCode: SocketError) -> Tuple[IntType, SocketError]: ...
    
    def EndReceiveFrom(self, asyncResult: IAsyncResult, endPoint: EndPoint) -> Tuple[IntType, EndPoint]: ...
    
    def EndReceiveMessageFrom(self, asyncResult: IAsyncResult, socketFlags: SocketFlags, endPoint: EndPoint, ipPacketInformation: IPPacketInformation) -> Tuple[IntType, SocketFlags, EndPoint, IPPacketInformation]: ...
    
    @overload
    def EndSend(self, asyncResult: IAsyncResult) -> IntType: ...
    
    @overload
    def EndSend(self, asyncResult: IAsyncResult, errorCode: SocketError) -> Tuple[IntType, SocketError]: ...
    
    def EndSendFile(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    def EndSendTo(self, asyncResult: IAsyncResult) -> IntType: ...
    
    @overload
    def GetSocketOption(self, optionLevel: SocketOptionLevel, optionName: SocketOptionName) -> ObjectType: ...
    
    @overload
    def GetSocketOption(self, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: ArrayType[ByteType]) -> VoidType: ...
    
    @overload
    def GetSocketOption(self, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionLength: IntType) -> ArrayType[ByteType]: ...
    
    @overload
    def IOControl(self, ioControlCode: IOControlCode, optionInValue: ArrayType[ByteType], optionOutValue: ArrayType[ByteType]) -> IntType: ...
    
    @overload
    def IOControl(self, ioControlCode: IntType, optionInValue: ArrayType[ByteType], optionOutValue: ArrayType[ByteType]) -> IntType: ...
    
    def Listen(self, backlog: IntType) -> VoidType: ...
    
    def Poll(self, microSeconds: IntType, mode: SelectMode) -> BooleanType: ...
    
    @overload
    def Receive(self, buffer: ArrayType[ByteType], size: IntType, socketFlags: SocketFlags) -> IntType: ...
    
    @overload
    def Receive(self, buffer: ArrayType[ByteType], socketFlags: SocketFlags) -> IntType: ...
    
    @overload
    def Receive(self, buffer: ArrayType[ByteType]) -> IntType: ...
    
    @overload
    def Receive(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, socketFlags: SocketFlags) -> IntType: ...
    
    @overload
    def Receive(self, buffers: IList[ArraySegment[ByteType]]) -> IntType: ...
    
    @overload
    def Receive(self, buffers: IList[ArraySegment[ByteType]], socketFlags: SocketFlags) -> IntType: ...
    
    @overload
    def Receive(self, buffers: IList[ArraySegment[ByteType]], socketFlags: SocketFlags, errorCode: SocketError) -> Tuple[IntType, SocketError]: ...
    
    @overload
    def Receive(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, socketFlags: SocketFlags, errorCode: SocketError) -> Tuple[IntType, SocketError]: ...
    
    def ReceiveAsync(self, e: SocketAsyncEventArgs) -> BooleanType: ...
    
    @overload
    def ReceiveFrom(self, buffer: ArrayType[ByteType], size: IntType, socketFlags: SocketFlags, remoteEP: EndPoint) -> Tuple[IntType, EndPoint]: ...
    
    @overload
    def ReceiveFrom(self, buffer: ArrayType[ByteType], socketFlags: SocketFlags, remoteEP: EndPoint) -> Tuple[IntType, EndPoint]: ...
    
    @overload
    def ReceiveFrom(self, buffer: ArrayType[ByteType], remoteEP: EndPoint) -> Tuple[IntType, EndPoint]: ...
    
    @overload
    def ReceiveFrom(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, socketFlags: SocketFlags, remoteEP: EndPoint) -> Tuple[IntType, EndPoint]: ...
    
    def ReceiveFromAsync(self, e: SocketAsyncEventArgs) -> BooleanType: ...
    
    def ReceiveMessageFrom(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, socketFlags: SocketFlags, remoteEP: EndPoint, ipPacketInformation: IPPacketInformation) -> Tuple[IntType, SocketFlags, EndPoint, IPPacketInformation]: ...
    
    def ReceiveMessageFromAsync(self, e: SocketAsyncEventArgs) -> BooleanType: ...
    
    @staticmethod
    def Select(checkRead: IList, checkWrite: IList, checkError: IList, microSeconds: IntType) -> VoidType: ...
    
    @overload
    def Send(self, buffer: ArrayType[ByteType], size: IntType, socketFlags: SocketFlags) -> IntType: ...
    
    @overload
    def Send(self, buffer: ArrayType[ByteType], socketFlags: SocketFlags) -> IntType: ...
    
    @overload
    def Send(self, buffer: ArrayType[ByteType]) -> IntType: ...
    
    @overload
    def Send(self, buffers: IList[ArraySegment[ByteType]]) -> IntType: ...
    
    @overload
    def Send(self, buffers: IList[ArraySegment[ByteType]], socketFlags: SocketFlags) -> IntType: ...
    
    @overload
    def Send(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, socketFlags: SocketFlags) -> IntType: ...
    
    @overload
    def Send(self, buffers: IList[ArraySegment[ByteType]], socketFlags: SocketFlags, errorCode: SocketError) -> Tuple[IntType, SocketError]: ...
    
    @overload
    def Send(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, socketFlags: SocketFlags, errorCode: SocketError) -> Tuple[IntType, SocketError]: ...
    
    def SendAsync(self, e: SocketAsyncEventArgs) -> BooleanType: ...
    
    @overload
    def SendFile(self, fileName: StringType) -> VoidType: ...
    
    @overload
    def SendFile(self, fileName: StringType, preBuffer: ArrayType[ByteType], postBuffer: ArrayType[ByteType], flags: TransmitFileOptions) -> VoidType: ...
    
    def SendPacketsAsync(self, e: SocketAsyncEventArgs) -> BooleanType: ...
    
    @overload
    def SendTo(self, buffer: ArrayType[ByteType], size: IntType, socketFlags: SocketFlags, remoteEP: EndPoint) -> IntType: ...
    
    @overload
    def SendTo(self, buffer: ArrayType[ByteType], socketFlags: SocketFlags, remoteEP: EndPoint) -> IntType: ...
    
    @overload
    def SendTo(self, buffer: ArrayType[ByteType], remoteEP: EndPoint) -> IntType: ...
    
    @overload
    def SendTo(self, buffer: ArrayType[ByteType], offset: IntType, size: IntType, socketFlags: SocketFlags, remoteEP: EndPoint) -> IntType: ...
    
    def SendToAsync(self, e: SocketAsyncEventArgs) -> BooleanType: ...
    
    def SetIPProtectionLevel(self, level: IPProtectionLevel) -> VoidType: ...
    
    @overload
    def SetSocketOption(self, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: IntType) -> VoidType: ...
    
    @overload
    def SetSocketOption(self, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: BooleanType) -> VoidType: ...
    
    @overload
    def SetSocketOption(self, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: ArrayType[ByteType]) -> VoidType: ...
    
    @overload
    def SetSocketOption(self, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: ObjectType) -> VoidType: ...
    
    def Shutdown(self, how: SocketShutdown) -> VoidType: ...
    
    def get_AddressFamily(self) -> AddressFamily: ...
    
    def get_Available(self) -> IntType: ...
    
    def get_Blocking(self) -> BooleanType: ...
    
    def get_Connected(self) -> BooleanType: ...
    
    def get_DontFragment(self) -> BooleanType: ...
    
    def get_DualMode(self) -> BooleanType: ...
    
    def get_EnableBroadcast(self) -> BooleanType: ...
    
    def get_ExclusiveAddressUse(self) -> BooleanType: ...
    
    def get_Handle(self) -> NIntType: ...
    
    def get_IsBound(self) -> BooleanType: ...
    
    def get_LingerState(self) -> LingerOption: ...
    
    def get_LocalEndPoint(self) -> EndPoint: ...
    
    def get_MulticastLoopback(self) -> BooleanType: ...
    
    def get_NoDelay(self) -> BooleanType: ...
    
    @staticmethod
    def get_OSSupportsIPv4() -> BooleanType: ...
    
    @staticmethod
    def get_OSSupportsIPv6() -> BooleanType: ...
    
    def get_ProtocolType(self) -> ProtocolType: ...
    
    def get_ReceiveBufferSize(self) -> IntType: ...
    
    def get_ReceiveTimeout(self) -> IntType: ...
    
    def get_RemoteEndPoint(self) -> EndPoint: ...
    
    def get_SendBufferSize(self) -> IntType: ...
    
    def get_SendTimeout(self) -> IntType: ...
    
    def get_SocketType(self) -> SocketType: ...
    
    @staticmethod
    def get_SupportsIPv4() -> BooleanType: ...
    
    @staticmethod
    def get_SupportsIPv6() -> BooleanType: ...
    
    def get_Ttl(self) -> ShortType: ...
    
    def get_UseOnlyOverlappedIO(self) -> BooleanType: ...
    
    def set_Blocking(self, value: BooleanType) -> VoidType: ...
    
    def set_DontFragment(self, value: BooleanType) -> VoidType: ...
    
    def set_DualMode(self, value: BooleanType) -> VoidType: ...
    
    def set_EnableBroadcast(self, value: BooleanType) -> VoidType: ...
    
    def set_ExclusiveAddressUse(self, value: BooleanType) -> VoidType: ...
    
    def set_LingerState(self, value: LingerOption) -> VoidType: ...
    
    def set_MulticastLoopback(self, value: BooleanType) -> VoidType: ...
    
    def set_NoDelay(self, value: BooleanType) -> VoidType: ...
    
    def set_ReceiveBufferSize(self, value: IntType) -> VoidType: ...
    
    def set_ReceiveTimeout(self, value: IntType) -> VoidType: ...
    
    def set_SendBufferSize(self, value: IntType) -> VoidType: ...
    
    def set_SendTimeout(self, value: IntType) -> VoidType: ...
    
    def set_Ttl(self, value: ShortType) -> VoidType: ...
    
    def set_UseOnlyOverlappedIO(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SocketAsyncEventArgs(EventArgs, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AcceptSocket(self) -> Socket: ...
    
    @AcceptSocket.setter
    def AcceptSocket(self, value: Socket) -> None: ...
    
    @property
    def Buffer(self) -> ArrayType[ByteType]: ...
    
    @property
    def BufferList(self) -> IList[ArraySegment[ByteType]]: ...
    
    @BufferList.setter
    def BufferList(self, value: IList[ArraySegment[ByteType]]) -> None: ...
    
    @property
    def BytesTransferred(self) -> IntType: ...
    
    @property
    def ConnectByNameError(self) -> Exception: ...
    
    @property
    def ConnectSocket(self) -> Socket: ...
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def DisconnectReuseSocket(self) -> BooleanType: ...
    
    @DisconnectReuseSocket.setter
    def DisconnectReuseSocket(self, value: BooleanType) -> None: ...
    
    @property
    def LastOperation(self) -> SocketAsyncOperation: ...
    
    @property
    def Offset(self) -> IntType: ...
    
    @property
    def ReceiveMessageFromPacketInfo(self) -> IPPacketInformation: ...
    
    @property
    def RemoteEndPoint(self) -> EndPoint: ...
    
    @RemoteEndPoint.setter
    def RemoteEndPoint(self, value: EndPoint) -> None: ...
    
    @property
    def SendPacketsElements(self) -> ArrayType[SendPacketsElement]: ...
    
    @SendPacketsElements.setter
    def SendPacketsElements(self, value: ArrayType[SendPacketsElement]) -> None: ...
    
    @property
    def SendPacketsFlags(self) -> TransmitFileOptions: ...
    
    @SendPacketsFlags.setter
    def SendPacketsFlags(self, value: TransmitFileOptions) -> None: ...
    
    @property
    def SendPacketsSendSize(self) -> IntType: ...
    
    @SendPacketsSendSize.setter
    def SendPacketsSendSize(self, value: IntType) -> None: ...
    
    @property
    def SocketClientAccessPolicyProtocol(self) -> SocketClientAccessPolicyProtocol: ...
    
    @SocketClientAccessPolicyProtocol.setter
    def SocketClientAccessPolicyProtocol(self, value: SocketClientAccessPolicyProtocol) -> None: ...
    
    @property
    def SocketError(self) -> SocketError: ...
    
    @SocketError.setter
    def SocketError(self, value: SocketError) -> None: ...
    
    @property
    def SocketFlags(self) -> SocketFlags: ...
    
    @SocketFlags.setter
    def SocketFlags(self, value: SocketFlags) -> None: ...
    
    @property
    def UserToken(self) -> ObjectType: ...
    
    @UserToken.setter
    def UserToken(self, value: ObjectType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    @overload
    def SetBuffer(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def SetBuffer(self, offset: IntType, count: IntType) -> VoidType: ...
    
    def add_Completed(self, value: EventHandler[SocketAsyncEventArgs]) -> VoidType: ...
    
    def get_AcceptSocket(self) -> Socket: ...
    
    def get_Buffer(self) -> ArrayType[ByteType]: ...
    
    def get_BufferList(self) -> IList[ArraySegment[ByteType]]: ...
    
    def get_BytesTransferred(self) -> IntType: ...
    
    def get_ConnectByNameError(self) -> Exception: ...
    
    def get_ConnectSocket(self) -> Socket: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_DisconnectReuseSocket(self) -> BooleanType: ...
    
    def get_LastOperation(self) -> SocketAsyncOperation: ...
    
    def get_Offset(self) -> IntType: ...
    
    def get_ReceiveMessageFromPacketInfo(self) -> IPPacketInformation: ...
    
    def get_RemoteEndPoint(self) -> EndPoint: ...
    
    def get_SendPacketsElements(self) -> ArrayType[SendPacketsElement]: ...
    
    def get_SendPacketsFlags(self) -> TransmitFileOptions: ...
    
    def get_SendPacketsSendSize(self) -> IntType: ...
    
    def get_SocketClientAccessPolicyProtocol(self) -> SocketClientAccessPolicyProtocol: ...
    
    def get_SocketError(self) -> SocketError: ...
    
    def get_SocketFlags(self) -> SocketFlags: ...
    
    def get_UserToken(self) -> ObjectType: ...
    
    def remove_Completed(self, value: EventHandler[SocketAsyncEventArgs]) -> VoidType: ...
    
    def set_AcceptSocket(self, value: Socket) -> VoidType: ...
    
    def set_BufferList(self, value: IList[ArraySegment[ByteType]]) -> VoidType: ...
    
    def set_DisconnectReuseSocket(self, value: BooleanType) -> VoidType: ...
    
    def set_RemoteEndPoint(self, value: EndPoint) -> VoidType: ...
    
    def set_SendPacketsElements(self, value: ArrayType[SendPacketsElement]) -> VoidType: ...
    
    def set_SendPacketsFlags(self, value: TransmitFileOptions) -> VoidType: ...
    
    def set_SendPacketsSendSize(self, value: IntType) -> VoidType: ...
    
    def set_SocketClientAccessPolicyProtocol(self, value: SocketClientAccessPolicyProtocol) -> VoidType: ...
    
    def set_SocketError(self, value: SocketError) -> VoidType: ...
    
    def set_SocketFlags(self, value: SocketFlags) -> VoidType: ...
    
    def set_UserToken(self, value: ObjectType) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    Completed: EventType[EventHandler[SocketAsyncEventArgs]] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SocketException(Win32Exception, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, errorCode: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ErrorCode(self) -> IntType: ...
    
    @property
    def Message(self) -> StringType: ...
    
    @property
    def SocketErrorCode(self) -> SocketError: ...
    
    # ---------- Methods ---------- #
    
    def get_ErrorCode(self) -> IntType: ...
    
    def get_Message(self) -> StringType: ...
    
    def get_SocketErrorCode(self) -> SocketError: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SocketTaskExtensions(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def AcceptAsync(socket: Socket) -> Task[Socket]: ...
    
    @staticmethod
    @overload
    def AcceptAsync(socket: Socket, acceptSocket: Socket) -> Task[Socket]: ...
    
    @staticmethod
    @overload
    def ConnectAsync(socket: Socket, remoteEP: EndPoint) -> Task: ...
    
    @staticmethod
    @overload
    def ConnectAsync(socket: Socket, address: IPAddress, port: IntType) -> Task: ...
    
    @staticmethod
    @overload
    def ConnectAsync(socket: Socket, addresses: ArrayType[IPAddress], port: IntType) -> Task: ...
    
    @staticmethod
    @overload
    def ConnectAsync(socket: Socket, host: StringType, port: IntType) -> Task: ...
    
    @staticmethod
    @overload
    def ReceiveAsync(socket: Socket, buffers: IList[ArraySegment[ByteType]], socketFlags: SocketFlags) -> Task[IntType]: ...
    
    @staticmethod
    @overload
    def ReceiveAsync(socket: Socket, buffer: ArraySegment[ByteType], socketFlags: SocketFlags) -> Task[IntType]: ...
    
    @staticmethod
    def ReceiveFromAsync(socket: Socket, buffer: ArraySegment[ByteType], socketFlags: SocketFlags, remoteEndPoint: EndPoint) -> Task[SocketReceiveFromResult]: ...
    
    @staticmethod
    def ReceiveMessageFromAsync(socket: Socket, buffer: ArraySegment[ByteType], socketFlags: SocketFlags, remoteEndPoint: EndPoint) -> Task[SocketReceiveMessageFromResult]: ...
    
    @staticmethod
    @overload
    def SendAsync(socket: Socket, buffers: IList[ArraySegment[ByteType]], socketFlags: SocketFlags) -> Task[IntType]: ...
    
    @staticmethod
    @overload
    def SendAsync(socket: Socket, buffer: ArraySegment[ByteType], socketFlags: SocketFlags) -> Task[IntType]: ...
    
    @staticmethod
    def SendToAsync(socket: Socket, buffer: ArraySegment[ByteType], socketFlags: SocketFlags, remoteEP: EndPoint) -> Task[IntType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TcpClient(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, localEP: IPEndPoint): ...
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, family: AddressFamily): ...
    
    @overload
    def __init__(self, hostname: StringType, port: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Available(self) -> IntType: ...
    
    @property
    def Client(self) -> Socket: ...
    
    @Client.setter
    def Client(self, value: Socket) -> None: ...
    
    @property
    def Connected(self) -> BooleanType: ...
    
    @property
    def ExclusiveAddressUse(self) -> BooleanType: ...
    
    @ExclusiveAddressUse.setter
    def ExclusiveAddressUse(self, value: BooleanType) -> None: ...
    
    @property
    def LingerState(self) -> LingerOption: ...
    
    @LingerState.setter
    def LingerState(self, value: LingerOption) -> None: ...
    
    @property
    def NoDelay(self) -> BooleanType: ...
    
    @NoDelay.setter
    def NoDelay(self, value: BooleanType) -> None: ...
    
    @property
    def ReceiveBufferSize(self) -> IntType: ...
    
    @ReceiveBufferSize.setter
    def ReceiveBufferSize(self, value: IntType) -> None: ...
    
    @property
    def ReceiveTimeout(self) -> IntType: ...
    
    @ReceiveTimeout.setter
    def ReceiveTimeout(self, value: IntType) -> None: ...
    
    @property
    def SendBufferSize(self) -> IntType: ...
    
    @SendBufferSize.setter
    def SendBufferSize(self, value: IntType) -> None: ...
    
    @property
    def SendTimeout(self) -> IntType: ...
    
    @SendTimeout.setter
    def SendTimeout(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def BeginConnect(self, host: StringType, port: IntType, requestCallback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    @overload
    def BeginConnect(self, address: IPAddress, port: IntType, requestCallback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    @overload
    def BeginConnect(self, addresses: ArrayType[IPAddress], port: IntType, requestCallback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def Close(self) -> VoidType: ...
    
    @overload
    def Connect(self, hostname: StringType, port: IntType) -> VoidType: ...
    
    @overload
    def Connect(self, address: IPAddress, port: IntType) -> VoidType: ...
    
    @overload
    def Connect(self, remoteEP: IPEndPoint) -> VoidType: ...
    
    @overload
    def Connect(self, ipAddresses: ArrayType[IPAddress], port: IntType) -> VoidType: ...
    
    @overload
    def ConnectAsync(self, address: IPAddress, port: IntType) -> Task: ...
    
    @overload
    def ConnectAsync(self, host: StringType, port: IntType) -> Task: ...
    
    @overload
    def ConnectAsync(self, addresses: ArrayType[IPAddress], port: IntType) -> Task: ...
    
    def Dispose(self) -> VoidType: ...
    
    def EndConnect(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    def GetStream(self) -> NetworkStream: ...
    
    def get_Available(self) -> IntType: ...
    
    def get_Client(self) -> Socket: ...
    
    def get_Connected(self) -> BooleanType: ...
    
    def get_ExclusiveAddressUse(self) -> BooleanType: ...
    
    def get_LingerState(self) -> LingerOption: ...
    
    def get_NoDelay(self) -> BooleanType: ...
    
    def get_ReceiveBufferSize(self) -> IntType: ...
    
    def get_ReceiveTimeout(self) -> IntType: ...
    
    def get_SendBufferSize(self) -> IntType: ...
    
    def get_SendTimeout(self) -> IntType: ...
    
    def set_Client(self, value: Socket) -> VoidType: ...
    
    def set_ExclusiveAddressUse(self, value: BooleanType) -> VoidType: ...
    
    def set_LingerState(self, value: LingerOption) -> VoidType: ...
    
    def set_NoDelay(self, value: BooleanType) -> VoidType: ...
    
    def set_ReceiveBufferSize(self, value: IntType) -> VoidType: ...
    
    def set_ReceiveTimeout(self, value: IntType) -> VoidType: ...
    
    def set_SendBufferSize(self, value: IntType) -> VoidType: ...
    
    def set_SendTimeout(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TcpListener(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, localEP: IPEndPoint): ...
    
    @overload
    def __init__(self, localaddr: IPAddress, port: IntType): ...
    
    @overload
    def __init__(self, port: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ExclusiveAddressUse(self) -> BooleanType: ...
    
    @ExclusiveAddressUse.setter
    def ExclusiveAddressUse(self, value: BooleanType) -> None: ...
    
    @property
    def LocalEndpoint(self) -> EndPoint: ...
    
    @property
    def Server(self) -> Socket: ...
    
    # ---------- Methods ---------- #
    
    def AcceptSocket(self) -> Socket: ...
    
    def AcceptSocketAsync(self) -> Task[Socket]: ...
    
    def AcceptTcpClient(self) -> TcpClient: ...
    
    def AcceptTcpClientAsync(self) -> Task[TcpClient]: ...
    
    def AllowNatTraversal(self, allowed: BooleanType) -> VoidType: ...
    
    def BeginAcceptSocket(self, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def BeginAcceptTcpClient(self, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    @staticmethod
    def Create(port: IntType) -> TcpListener: ...
    
    def EndAcceptSocket(self, asyncResult: IAsyncResult) -> Socket: ...
    
    def EndAcceptTcpClient(self, asyncResult: IAsyncResult) -> TcpClient: ...
    
    def Pending(self) -> BooleanType: ...
    
    @overload
    def Start(self) -> VoidType: ...
    
    @overload
    def Start(self, backlog: IntType) -> VoidType: ...
    
    def Stop(self) -> VoidType: ...
    
    def get_ExclusiveAddressUse(self) -> BooleanType: ...
    
    def get_LocalEndpoint(self) -> EndPoint: ...
    
    def get_Server(self) -> Socket: ...
    
    def set_ExclusiveAddressUse(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TransmitFileOverlappedAsyncResult(BaseOverlappedAsyncResult, IAsyncResult):
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


class TransmitPacketsDelegate(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, socketHandle: SafeCloseSocket, packetArray: NIntType, elementCount: IntType, sendSize: IntType, overlapped: SafeNativeOverlapped, flags: TransmitFileOptions, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> BooleanType: ...
    
    def Invoke(self, socketHandle: SafeCloseSocket, packetArray: NIntType, elementCount: IntType, sendSize: IntType, overlapped: SafeNativeOverlapped, flags: TransmitFileOptions) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UdpClient(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, family: AddressFamily): ...
    
    @overload
    def __init__(self, port: IntType): ...
    
    @overload
    def __init__(self, port: IntType, family: AddressFamily): ...
    
    @overload
    def __init__(self, localEP: IPEndPoint): ...
    
    @overload
    def __init__(self, hostname: StringType, port: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Available(self) -> IntType: ...
    
    @property
    def Client(self) -> Socket: ...
    
    @Client.setter
    def Client(self, value: Socket) -> None: ...
    
    @property
    def DontFragment(self) -> BooleanType: ...
    
    @DontFragment.setter
    def DontFragment(self, value: BooleanType) -> None: ...
    
    @property
    def EnableBroadcast(self) -> BooleanType: ...
    
    @EnableBroadcast.setter
    def EnableBroadcast(self, value: BooleanType) -> None: ...
    
    @property
    def ExclusiveAddressUse(self) -> BooleanType: ...
    
    @ExclusiveAddressUse.setter
    def ExclusiveAddressUse(self, value: BooleanType) -> None: ...
    
    @property
    def MulticastLoopback(self) -> BooleanType: ...
    
    @MulticastLoopback.setter
    def MulticastLoopback(self, value: BooleanType) -> None: ...
    
    @property
    def Ttl(self) -> ShortType: ...
    
    @Ttl.setter
    def Ttl(self, value: ShortType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def AllowNatTraversal(self, allowed: BooleanType) -> VoidType: ...
    
    def BeginReceive(self, requestCallback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    @overload
    def BeginSend(self, datagram: ArrayType[ByteType], bytes: IntType, endPoint: IPEndPoint, requestCallback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    @overload
    def BeginSend(self, datagram: ArrayType[ByteType], bytes: IntType, hostname: StringType, port: IntType, requestCallback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    @overload
    def BeginSend(self, datagram: ArrayType[ByteType], bytes: IntType, requestCallback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def Close(self) -> VoidType: ...
    
    @overload
    def Connect(self, hostname: StringType, port: IntType) -> VoidType: ...
    
    @overload
    def Connect(self, addr: IPAddress, port: IntType) -> VoidType: ...
    
    @overload
    def Connect(self, endPoint: IPEndPoint) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    @overload
    def DropMulticastGroup(self, multicastAddr: IPAddress, ifindex: IntType) -> VoidType: ...
    
    @overload
    def DropMulticastGroup(self, multicastAddr: IPAddress) -> VoidType: ...
    
    def EndReceive(self, asyncResult: IAsyncResult, remoteEP: IPEndPoint) -> Tuple[ArrayType[ByteType], IPEndPoint]: ...
    
    def EndSend(self, asyncResult: IAsyncResult) -> IntType: ...
    
    @overload
    def JoinMulticastGroup(self, multicastAddr: IPAddress, localAddress: IPAddress) -> VoidType: ...
    
    @overload
    def JoinMulticastGroup(self, ifindex: IntType, multicastAddr: IPAddress) -> VoidType: ...
    
    @overload
    def JoinMulticastGroup(self, multicastAddr: IPAddress, timeToLive: IntType) -> VoidType: ...
    
    @overload
    def JoinMulticastGroup(self, multicastAddr: IPAddress) -> VoidType: ...
    
    def Receive(self, remoteEP: IPEndPoint) -> Tuple[ArrayType[ByteType], IPEndPoint]: ...
    
    def ReceiveAsync(self) -> Task[UdpReceiveResult]: ...
    
    @overload
    def Send(self, dgram: ArrayType[ByteType], bytes: IntType, endPoint: IPEndPoint) -> IntType: ...
    
    @overload
    def Send(self, dgram: ArrayType[ByteType], bytes: IntType, hostname: StringType, port: IntType) -> IntType: ...
    
    @overload
    def Send(self, dgram: ArrayType[ByteType], bytes: IntType) -> IntType: ...
    
    @overload
    def SendAsync(self, datagram: ArrayType[ByteType], bytes: IntType) -> Task[IntType]: ...
    
    @overload
    def SendAsync(self, datagram: ArrayType[ByteType], bytes: IntType, endPoint: IPEndPoint) -> Task[IntType]: ...
    
    @overload
    def SendAsync(self, datagram: ArrayType[ByteType], bytes: IntType, hostname: StringType, port: IntType) -> Task[IntType]: ...
    
    def get_Available(self) -> IntType: ...
    
    def get_Client(self) -> Socket: ...
    
    def get_DontFragment(self) -> BooleanType: ...
    
    def get_EnableBroadcast(self) -> BooleanType: ...
    
    def get_ExclusiveAddressUse(self) -> BooleanType: ...
    
    def get_MulticastLoopback(self) -> BooleanType: ...
    
    def get_Ttl(self) -> ShortType: ...
    
    def set_Client(self, value: Socket) -> VoidType: ...
    
    def set_DontFragment(self, value: BooleanType) -> VoidType: ...
    
    def set_EnableBroadcast(self, value: BooleanType) -> VoidType: ...
    
    def set_ExclusiveAddressUse(self, value: BooleanType) -> VoidType: ...
    
    def set_MulticastLoopback(self, value: BooleanType) -> VoidType: ...
    
    def set_Ttl(self, value: ShortType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WSARecvMsgDelegate(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, socketHandle: SafeCloseSocket, msg: NIntType, bytesTransferred: IntType, overlapped: SafeHandle, completionRoutine: NIntType, callback: AsyncCallback, object: ObjectType) -> Tuple[IAsyncResult, IntType]: ...
    
    def EndInvoke(self, bytesTransferred: IntType, result: IAsyncResult) -> Tuple[SocketError, IntType]: ...
    
    def Invoke(self, socketHandle: SafeCloseSocket, msg: NIntType, bytesTransferred: IntType, overlapped: SafeHandle, completionRoutine: NIntType) -> Tuple[SocketError, IntType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WSARecvMsgDelegate_Blocking(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, socketHandle: NIntType, msg: NIntType, bytesTransferred: IntType, overlapped: NIntType, completionRoutine: NIntType, callback: AsyncCallback, object: ObjectType) -> Tuple[IAsyncResult, IntType]: ...
    
    def EndInvoke(self, bytesTransferred: IntType, result: IAsyncResult) -> Tuple[SocketError, IntType]: ...
    
    def Invoke(self, socketHandle: NIntType, msg: NIntType, bytesTransferred: IntType, overlapped: NIntType, completionRoutine: NIntType) -> Tuple[SocketError, IntType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Structs ---------- #

class IPPacketInformation(ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Address(self) -> IPAddress: ...
    
    @property
    def Interface(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, comparand: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Address(self) -> IPAddress: ...
    
    def get_Interface(self) -> IntType: ...
    
    @staticmethod
    def op_Equality(packetInformation1: IPPacketInformation, packetInformation2: IPPacketInformation) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(packetInformation1: IPPacketInformation, packetInformation2: IPPacketInformation) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NetworkEvents(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def ErrorCodes(self) -> ArrayType[IntType]: ...
    
    @ErrorCodes.setter
    def ErrorCodes(self, value: ArrayType[IntType]) -> None: ...
    
    @property
    def Events(self) -> AsyncEventBits: ...
    
    @Events.setter
    def Events(self, value: AsyncEventBits) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SocketInformation(ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Options(self) -> SocketInformationOptions: ...
    
    @Options.setter
    def Options(self, value: SocketInformationOptions) -> None: ...
    
    @property
    def ProtocolInformation(self) -> ArrayType[ByteType]: ...
    
    @ProtocolInformation.setter
    def ProtocolInformation(self, value: ArrayType[ByteType]) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Options(self) -> SocketInformationOptions: ...
    
    def get_ProtocolInformation(self) -> ArrayType[ByteType]: ...
    
    def set_Options(self, value: SocketInformationOptions) -> VoidType: ...
    
    def set_ProtocolInformation(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SocketReceiveFromResult(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def ReceivedBytes(self) -> IntType: ...
    
    @ReceivedBytes.setter
    def ReceivedBytes(self, value: IntType) -> None: ...
    
    @property
    def RemoteEndPoint(self) -> EndPoint: ...
    
    @RemoteEndPoint.setter
    def RemoteEndPoint(self, value: EndPoint) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SocketReceiveMessageFromResult(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def PacketInformation(self) -> IPPacketInformation: ...
    
    @PacketInformation.setter
    def PacketInformation(self, value: IPPacketInformation) -> None: ...
    
    @property
    def ReceivedBytes(self) -> IntType: ...
    
    @ReceivedBytes.setter
    def ReceivedBytes(self, value: IntType) -> None: ...
    
    @property
    def RemoteEndPoint(self) -> EndPoint: ...
    
    @RemoteEndPoint.setter
    def RemoteEndPoint(self, value: EndPoint) -> None: ...
    
    @property
    def SocketFlags(self) -> SocketFlags: ...
    
    @SocketFlags.setter
    def SocketFlags(self, value: SocketFlags) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TimeValue(ValueType):
    # ---------- Fields ---------- #
    
    @property
    def Microseconds(self) -> IntType: ...
    
    @Microseconds.setter
    def Microseconds(self, value: IntType) -> None: ...
    
    @property
    def Seconds(self) -> IntType: ...
    
    @Seconds.setter
    def Seconds(self, value: IntType) -> None: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UdpReceiveResult(ValueType, IEquatable[UdpReceiveResult]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, buffer: ArrayType[ByteType], remoteEndPoint: IPEndPoint): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Buffer(self) -> ArrayType[ByteType]: ...
    
    @property
    def RemoteEndPoint(self) -> IPEndPoint: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: UdpReceiveResult) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Buffer(self) -> ArrayType[ByteType]: ...
    
    def get_RemoteEndPoint(self) -> IPEndPoint: ...
    
    @staticmethod
    def op_Equality(left: UdpReceiveResult, right: UdpReceiveResult) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: UdpReceiveResult, right: UdpReceiveResult) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Interfaces

# ---------- Enums ---------- #

class AddressFamily(Enum):
    Unknown: IntType = -1
    Unspecified: IntType = 0
    Unix: IntType = 1
    InterNetwork: IntType = 2
    ImpLink: IntType = 3
    Pup: IntType = 4
    Chaos: IntType = 5
    Ipx: IntType = 6
    NS: IntType = 6
    Iso: IntType = 7
    Osi: IntType = 7
    Ecma: IntType = 8
    DataKit: IntType = 9
    Ccitt: IntType = 10
    Sna: IntType = 11
    DecNet: IntType = 12
    DataLink: IntType = 13
    Lat: IntType = 14
    HyperChannel: IntType = 15
    AppleTalk: IntType = 16
    NetBios: IntType = 17
    VoiceView: IntType = 18
    FireFox: IntType = 19
    Banyan: IntType = 21
    Atm: IntType = 22
    InterNetworkV6: IntType = 23
    Cluster: IntType = 24
    Ieee12844: IntType = 25
    Irda: IntType = 26
    NetworkDesigners: IntType = 28
    Max: IntType = 29


class AsyncEventBits(Enum):
    FdNone: IntType = 0
    FdRead: IntType = 1
    FdWrite: IntType = 2
    FdOob: IntType = 4
    FdAccept: IntType = 8
    FdConnect: IntType = 16
    FdClose: IntType = 32
    FdQos: IntType = 64
    FdGroupQos: IntType = 128
    FdRoutingInterfaceChange: IntType = 256
    FdAddressListChange: IntType = 512
    FdAllEvents: IntType = 1023


class AsyncEventBitsPos(Enum):
    FdReadBit: IntType = 0
    FdWriteBit: IntType = 1
    FdOobBit: IntType = 2
    FdAcceptBit: IntType = 3
    FdConnectBit: IntType = 4
    FdCloseBit: IntType = 5
    FdQosBit: IntType = 6
    FdGroupQosBit: IntType = 7
    FdRoutingInterfaceChangeBit: IntType = 8
    FdAddressListChangeBit: IntType = 9
    FdMaxEvents: IntType = 10


class IOControlCode(Enum):
    EnableCircularQueuing: LongType = 671088642
    Flush: LongType = 671088644
    AddressListChange: LongType = 671088663
    DataToRead: LongType = 1074030207
    OobDataRead: LongType = 1074033415
    GetBroadcastAddress: LongType = 1207959557
    AddressListQuery: LongType = 1207959574
    QueryTargetPnpHandle: LongType = 1207959576
    AsyncIO: LongType = 2147772029
    NonBlockingIO: LongType = 2147772030
    AssociateHandle: LongType = 2281701377
    MultipointLoopback: LongType = 2281701385
    MulticastScope: LongType = 2281701386
    SetQos: LongType = 2281701387
    SetGroupQos: LongType = 2281701388
    RoutingInterfaceChange: LongType = 2281701397
    NamespaceChange: LongType = 2281701401
    ReceiveAll: LongType = 2550136833
    ReceiveAllMulticast: LongType = 2550136834
    ReceiveAllIgmpMulticast: LongType = 2550136835
    KeepAliveValues: LongType = 2550136836
    AbsorbRouterAlert: LongType = 2550136837
    UnicastInterface: LongType = 2550136838
    LimitBroadcasts: LongType = 2550136839
    BindToInterface: LongType = 2550136840
    MulticastInterface: LongType = 2550136841
    AddMulticastGroupOnInterface: LongType = 2550136842
    DeleteMulticastGroupFromInterface: LongType = 2550136843
    GetExtensionFunctionPointer: LongType = 3355443206
    GetQos: LongType = 3355443207
    GetGroupQos: LongType = 3355443208
    TranslateHandle: LongType = 3355443213
    RoutingInterfaceQuery: LongType = 3355443220
    AddressListSort: LongType = 3355443225


class IPProtectionLevel(Enum):
    Unspecified: IntType = -1
    Unrestricted: IntType = 10
    EdgeRestricted: IntType = 20
    Restricted: IntType = 30


class ProtocolFamily(Enum):
    Unknown: IntType = -1
    Unspecified: IntType = 0
    Unix: IntType = 1
    InterNetwork: IntType = 2
    ImpLink: IntType = 3
    Pup: IntType = 4
    Chaos: IntType = 5
    Ipx: IntType = 6
    NS: IntType = 6
    Iso: IntType = 7
    Osi: IntType = 7
    Ecma: IntType = 8
    DataKit: IntType = 9
    Ccitt: IntType = 10
    Sna: IntType = 11
    DecNet: IntType = 12
    DataLink: IntType = 13
    Lat: IntType = 14
    HyperChannel: IntType = 15
    AppleTalk: IntType = 16
    NetBios: IntType = 17
    VoiceView: IntType = 18
    FireFox: IntType = 19
    Banyan: IntType = 21
    Atm: IntType = 22
    InterNetworkV6: IntType = 23
    Cluster: IntType = 24
    Ieee12844: IntType = 25
    Irda: IntType = 26
    NetworkDesigners: IntType = 28
    Max: IntType = 29


class ProtocolType(Enum):
    Unknown: IntType = -1
    IPv6HopByHopOptions: IntType = 0
    IP: IntType = 0
    Unspecified: IntType = 0
    Icmp: IntType = 1
    Igmp: IntType = 2
    Ggp: IntType = 3
    IPv4: IntType = 4
    Tcp: IntType = 6
    Pup: IntType = 12
    Udp: IntType = 17
    Idp: IntType = 22
    IPv6: IntType = 41
    IPv6RoutingHeader: IntType = 43
    IPv6FragmentHeader: IntType = 44
    IPSecEncapsulatingSecurityPayload: IntType = 50
    IPSecAuthenticationHeader: IntType = 51
    IcmpV6: IntType = 58
    IPv6NoNextHeader: IntType = 59
    IPv6DestinationOptions: IntType = 60
    ND: IntType = 77
    Raw: IntType = 255
    Ipx: IntType = 1000
    Spx: IntType = 1256
    SpxII: IntType = 1257


class SelectMode(Enum):
    SelectRead: IntType = 0
    SelectWrite: IntType = 1
    SelectError: IntType = 2


class SocketAsyncOperation(Enum):
    #None: IntType = 0
    Accept: IntType = 1
    Connect: IntType = 2
    Disconnect: IntType = 3
    Receive: IntType = 4
    ReceiveFrom: IntType = 5
    ReceiveMessageFrom: IntType = 6
    Send: IntType = 7
    SendPackets: IntType = 8
    SendTo: IntType = 9


class SocketClientAccessPolicyProtocol(Enum):
    Tcp: IntType = 0
    Http: IntType = 1


class SocketError(Enum):
    SocketError: IntType = -1
    Success: IntType = 0
    OperationAborted: IntType = 995
    IOPending: IntType = 997
    Interrupted: IntType = 10004
    AccessDenied: IntType = 10013
    Fault: IntType = 10014
    InvalidArgument: IntType = 10022
    TooManyOpenSockets: IntType = 10024
    WouldBlock: IntType = 10035
    InProgress: IntType = 10036
    AlreadyInProgress: IntType = 10037
    NotSocket: IntType = 10038
    DestinationAddressRequired: IntType = 10039
    MessageSize: IntType = 10040
    ProtocolType: IntType = 10041
    ProtocolOption: IntType = 10042
    ProtocolNotSupported: IntType = 10043
    SocketNotSupported: IntType = 10044
    OperationNotSupported: IntType = 10045
    ProtocolFamilyNotSupported: IntType = 10046
    AddressFamilyNotSupported: IntType = 10047
    AddressAlreadyInUse: IntType = 10048
    AddressNotAvailable: IntType = 10049
    NetworkDown: IntType = 10050
    NetworkUnreachable: IntType = 10051
    NetworkReset: IntType = 10052
    ConnectionAborted: IntType = 10053
    ConnectionReset: IntType = 10054
    NoBufferSpaceAvailable: IntType = 10055
    IsConnected: IntType = 10056
    NotConnected: IntType = 10057
    Shutdown: IntType = 10058
    TimedOut: IntType = 10060
    ConnectionRefused: IntType = 10061
    HostDown: IntType = 10064
    HostUnreachable: IntType = 10065
    ProcessLimit: IntType = 10067
    SystemNotReady: IntType = 10091
    VersionNotSupported: IntType = 10092
    NotInitialized: IntType = 10093
    Disconnecting: IntType = 10101
    TypeNotFound: IntType = 10109
    HostNotFound: IntType = 11001
    TryAgain: IntType = 11002
    NoRecovery: IntType = 11003
    NoData: IntType = 11004


class SocketFlags(Enum):
    #None: IntType = 0
    OutOfBand: IntType = 1
    Peek: IntType = 2
    DontRoute: IntType = 4
    MaxIOVectorLength: IntType = 16
    Truncated: IntType = 256
    ControlDataTruncated: IntType = 512
    Broadcast: IntType = 1024
    Multicast: IntType = 2048
    Partial: IntType = 32768


class SocketInformationOptions(Enum):
    NonBlocking: IntType = 1
    Connected: IntType = 2
    Listening: IntType = 4
    UseOnlyOverlappedIO: IntType = 8


class SocketOptionLevel(Enum):
    IP: IntType = 0
    Tcp: IntType = 6
    Udp: IntType = 17
    IPv6: IntType = 41
    Socket: IntType = 65535


class SocketOptionName(Enum):
    DontLinger: IntType = -129
    ExclusiveAddressUse: IntType = -5
    IPOptions: IntType = 1
    Debug: IntType = 1
    NoChecksum: IntType = 1
    NoDelay: IntType = 1
    HeaderIncluded: IntType = 2
    AcceptConnection: IntType = 2
    BsdUrgent: IntType = 2
    Expedited: IntType = 2
    TypeOfService: IntType = 3
    ReuseAddress: IntType = 4
    IpTimeToLive: IntType = 4
    KeepAlive: IntType = 8
    MulticastInterface: IntType = 9
    MulticastTimeToLive: IntType = 10
    MulticastLoopback: IntType = 11
    AddMembership: IntType = 12
    DropMembership: IntType = 13
    DontFragment: IntType = 14
    AddSourceMembership: IntType = 15
    DropSourceMembership: IntType = 16
    DontRoute: IntType = 16
    BlockSource: IntType = 17
    UnblockSource: IntType = 18
    PacketInformation: IntType = 19
    ChecksumCoverage: IntType = 20
    HopLimit: IntType = 21
    IPProtectionLevel: IntType = 23
    IPv6Only: IntType = 27
    Broadcast: IntType = 32
    UseLoopback: IntType = 64
    Linger: IntType = 128
    OutOfBandInline: IntType = 256
    SendBuffer: IntType = 4097
    ReceiveBuffer: IntType = 4098
    SendLowWater: IntType = 4099
    ReceiveLowWater: IntType = 4100
    SendTimeout: IntType = 4101
    ReceiveTimeout: IntType = 4102
    Error: IntType = 4103
    Type: IntType = 4104
    ReuseUnicastPort: IntType = 12295
    UpdateAcceptContext: IntType = 28683
    UpdateConnectContext: IntType = 28688
    MaxConnections: IntType = 2147483647


class SocketShutdown(Enum):
    Receive: IntType = 0
    Send: IntType = 1
    Both: IntType = 2


class SocketType(Enum):
    Unknown: IntType = -1
    Stream: IntType = 1
    Dgram: IntType = 2
    Raw: IntType = 3
    Rdm: IntType = 4
    Seqpacket: IntType = 5


class TransmitFileOptions(Enum):
    UseDefaultWorkerThread: IntType = 0
    Disconnect: IntType = 1
    ReuseSocket: IntType = 2
    WriteBehind: IntType = 4
    UseSystemThread: IntType = 16
    UseKernelApc: IntType = 32


# ---------- Delegates ---------- #

AcceptExDelegate = Callable[[SafeCloseSocket, SafeCloseSocket, NIntType, IntType, IntType, IntType, IntType, SafeHandle], BooleanType]

ConnectExDelegate = Callable[[SafeCloseSocket, NIntType, IntType, NIntType, IntType, IntType, SafeHandle], BooleanType]

DisconnectExDelegate = Callable[[SafeCloseSocket, SafeHandle, IntType, IntType], BooleanType]

DisconnectExDelegate_Blocking = Callable[[NIntType, NIntType, IntType, IntType], BooleanType]

GetAcceptExSockaddrsDelegate = Callable[[NIntType, IntType, IntType, IntType, NIntType, IntType, NIntType, IntType], VoidType]

TransmitPacketsDelegate = Callable[[SafeCloseSocket, NIntType, IntType, IntType, SafeNativeOverlapped, TransmitFileOptions], BooleanType]

WSARecvMsgDelegate = Callable[[SafeCloseSocket, NIntType, IntType, SafeHandle, NIntType], SocketError]

WSARecvMsgDelegate_Blocking = Callable[[NIntType, NIntType, IntType, NIntType, NIntType], SocketError]

__all__ = [
    AcceptAsyncResult,
    AcceptExDelegate,
    AcceptOverlappedAsyncResult,
    BaseOverlappedAsyncResult,
    ConnectAsyncResult,
    ConnectExDelegate,
    ConnectOverlappedAsyncResult,
    DisconnectExDelegate,
    DisconnectExDelegate_Blocking,
    DisconnectOverlappedAsyncResult,
    DynamicWinsockMethods,
    GetAcceptExSockaddrsDelegate,
    IPv6MulticastOption,
    IoctlSocketConstants,
    LingerOption,
    MulticastOption,
    MultipleConnectAsync,
    MultipleSocketMultipleConnectAsync,
    NetworkStream,
    OverlappedAsyncResult,
    OverlappedCache,
    ReceiveMessageOverlappedAsyncResult,
    SendPacketsElement,
    SingleSocketMultipleConnectAsync,
    Socket,
    SocketAsyncEventArgs,
    SocketException,
    SocketTaskExtensions,
    TcpClient,
    TcpListener,
    TransmitFileOverlappedAsyncResult,
    TransmitPacketsDelegate,
    UdpClient,
    WSARecvMsgDelegate,
    WSARecvMsgDelegate_Blocking,
    IPPacketInformation,
    NetworkEvents,
    SocketInformation,
    SocketReceiveFromResult,
    SocketReceiveMessageFromResult,
    TimeValue,
    UdpReceiveResult,
    AddressFamily,
    AsyncEventBits,
    AsyncEventBitsPos,
    IOControlCode,
    IPProtectionLevel,
    ProtocolFamily,
    ProtocolType,
    SelectMode,
    SocketAsyncOperation,
    SocketClientAccessPolicyProtocol,
    SocketError,
    SocketFlags,
    SocketInformationOptions,
    SocketOptionLevel,
    SocketOptionName,
    SocketShutdown,
    SocketType,
    TransmitFileOptions,
    AcceptExDelegate,
    ConnectExDelegate,
    DisconnectExDelegate,
    DisconnectExDelegate_Blocking,
    GetAcceptExSockaddrsDelegate,
    TransmitPacketsDelegate,
    WSARecvMsgDelegate,
    WSARecvMsgDelegate_Blocking,
]
