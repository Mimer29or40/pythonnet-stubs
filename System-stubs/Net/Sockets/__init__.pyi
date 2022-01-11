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
    Unknown = -1
    Unspecified = 0
    Unix = 1
    InterNetwork = 2
    ImpLink = 3
    Pup = 4
    Chaos = 5
    Ipx = 6
    NS = 6
    Iso = 7
    Osi = 7
    Ecma = 8
    DataKit = 9
    Ccitt = 10
    Sna = 11
    DecNet = 12
    DataLink = 13
    Lat = 14
    HyperChannel = 15
    AppleTalk = 16
    NetBios = 17
    VoiceView = 18
    FireFox = 19
    Banyan = 21
    Atm = 22
    InterNetworkV6 = 23
    Cluster = 24
    Ieee12844 = 25
    Irda = 26
    NetworkDesigners = 28
    Max = 29


class AsyncEventBits(Enum):
    FdNone = 0
    FdRead = 1
    FdWrite = 2
    FdOob = 4
    FdAccept = 8
    FdConnect = 16
    FdClose = 32
    FdQos = 64
    FdGroupQos = 128
    FdRoutingInterfaceChange = 256
    FdAddressListChange = 512
    FdAllEvents = 1023


class AsyncEventBitsPos(Enum):
    FdReadBit = 0
    FdWriteBit = 1
    FdOobBit = 2
    FdAcceptBit = 3
    FdConnectBit = 4
    FdCloseBit = 5
    FdQosBit = 6
    FdGroupQosBit = 7
    FdRoutingInterfaceChangeBit = 8
    FdAddressListChangeBit = 9
    FdMaxEvents = 10


class IOControlCode(Enum):
    EnableCircularQueuing = 671088642
    Flush = 671088644
    AddressListChange = 671088663
    DataToRead = 1074030207
    OobDataRead = 1074033415
    GetBroadcastAddress = 1207959557
    AddressListQuery = 1207959574
    QueryTargetPnpHandle = 1207959576
    AsyncIO = 2147772029
    NonBlockingIO = 2147772030
    AssociateHandle = 2281701377
    MultipointLoopback = 2281701385
    MulticastScope = 2281701386
    SetQos = 2281701387
    SetGroupQos = 2281701388
    RoutingInterfaceChange = 2281701397
    NamespaceChange = 2281701401
    ReceiveAll = 2550136833
    ReceiveAllMulticast = 2550136834
    ReceiveAllIgmpMulticast = 2550136835
    KeepAliveValues = 2550136836
    AbsorbRouterAlert = 2550136837
    UnicastInterface = 2550136838
    LimitBroadcasts = 2550136839
    BindToInterface = 2550136840
    MulticastInterface = 2550136841
    AddMulticastGroupOnInterface = 2550136842
    DeleteMulticastGroupFromInterface = 2550136843
    GetExtensionFunctionPointer = 3355443206
    GetQos = 3355443207
    GetGroupQos = 3355443208
    TranslateHandle = 3355443213
    RoutingInterfaceQuery = 3355443220
    AddressListSort = 3355443225


class IPProtectionLevel(Enum):
    Unspecified = -1
    Unrestricted = 10
    EdgeRestricted = 20
    Restricted = 30


class ProtocolFamily(Enum):
    Unknown = -1
    Unspecified = 0
    Unix = 1
    InterNetwork = 2
    ImpLink = 3
    Pup = 4
    Chaos = 5
    Ipx = 6
    NS = 6
    Iso = 7
    Osi = 7
    Ecma = 8
    DataKit = 9
    Ccitt = 10
    Sna = 11
    DecNet = 12
    DataLink = 13
    Lat = 14
    HyperChannel = 15
    AppleTalk = 16
    NetBios = 17
    VoiceView = 18
    FireFox = 19
    Banyan = 21
    Atm = 22
    InterNetworkV6 = 23
    Cluster = 24
    Ieee12844 = 25
    Irda = 26
    NetworkDesigners = 28
    Max = 29


class ProtocolType(Enum):
    Unknown = -1
    IPv6HopByHopOptions = 0
    IP = 0
    Unspecified = 0
    Icmp = 1
    Igmp = 2
    Ggp = 3
    IPv4 = 4
    Tcp = 6
    Pup = 12
    Udp = 17
    Idp = 22
    IPv6 = 41
    IPv6RoutingHeader = 43
    IPv6FragmentHeader = 44
    IPSecEncapsulatingSecurityPayload = 50
    IPSecAuthenticationHeader = 51
    IcmpV6 = 58
    IPv6NoNextHeader = 59
    IPv6DestinationOptions = 60
    ND = 77
    Raw = 255
    Ipx = 1000
    Spx = 1256
    SpxII = 1257


class SelectMode(Enum):
    SelectRead = 0
    SelectWrite = 1
    SelectError = 2


class SocketAsyncOperation(Enum):
    #None = 0
    Accept = 1
    Connect = 2
    Disconnect = 3
    Receive = 4
    ReceiveFrom = 5
    ReceiveMessageFrom = 6
    Send = 7
    SendPackets = 8
    SendTo = 9


class SocketClientAccessPolicyProtocol(Enum):
    Tcp = 0
    Http = 1


class SocketError(Enum):
    SocketError = -1
    Success = 0
    OperationAborted = 995
    IOPending = 997
    Interrupted = 10004
    AccessDenied = 10013
    Fault = 10014
    InvalidArgument = 10022
    TooManyOpenSockets = 10024
    WouldBlock = 10035
    InProgress = 10036
    AlreadyInProgress = 10037
    NotSocket = 10038
    DestinationAddressRequired = 10039
    MessageSize = 10040
    ProtocolType = 10041
    ProtocolOption = 10042
    ProtocolNotSupported = 10043
    SocketNotSupported = 10044
    OperationNotSupported = 10045
    ProtocolFamilyNotSupported = 10046
    AddressFamilyNotSupported = 10047
    AddressAlreadyInUse = 10048
    AddressNotAvailable = 10049
    NetworkDown = 10050
    NetworkUnreachable = 10051
    NetworkReset = 10052
    ConnectionAborted = 10053
    ConnectionReset = 10054
    NoBufferSpaceAvailable = 10055
    IsConnected = 10056
    NotConnected = 10057
    Shutdown = 10058
    TimedOut = 10060
    ConnectionRefused = 10061
    HostDown = 10064
    HostUnreachable = 10065
    ProcessLimit = 10067
    SystemNotReady = 10091
    VersionNotSupported = 10092
    NotInitialized = 10093
    Disconnecting = 10101
    TypeNotFound = 10109
    HostNotFound = 11001
    TryAgain = 11002
    NoRecovery = 11003
    NoData = 11004


class SocketFlags(Enum):
    #None = 0
    OutOfBand = 1
    Peek = 2
    DontRoute = 4
    MaxIOVectorLength = 16
    Truncated = 256
    ControlDataTruncated = 512
    Broadcast = 1024
    Multicast = 2048
    Partial = 32768


class SocketInformationOptions(Enum):
    NonBlocking = 1
    Connected = 2
    Listening = 4
    UseOnlyOverlappedIO = 8


class SocketOptionLevel(Enum):
    IP = 0
    Tcp = 6
    Udp = 17
    IPv6 = 41
    Socket = 65535


class SocketOptionName(Enum):
    DontLinger = -129
    ExclusiveAddressUse = -5
    IPOptions = 1
    Debug = 1
    NoChecksum = 1
    NoDelay = 1
    HeaderIncluded = 2
    AcceptConnection = 2
    BsdUrgent = 2
    Expedited = 2
    TypeOfService = 3
    ReuseAddress = 4
    IpTimeToLive = 4
    KeepAlive = 8
    MulticastInterface = 9
    MulticastTimeToLive = 10
    MulticastLoopback = 11
    AddMembership = 12
    DropMembership = 13
    DontFragment = 14
    AddSourceMembership = 15
    DropSourceMembership = 16
    DontRoute = 16
    BlockSource = 17
    UnblockSource = 18
    PacketInformation = 19
    ChecksumCoverage = 20
    HopLimit = 21
    IPProtectionLevel = 23
    IPv6Only = 27
    Broadcast = 32
    UseLoopback = 64
    Linger = 128
    OutOfBandInline = 256
    SendBuffer = 4097
    ReceiveBuffer = 4098
    SendLowWater = 4099
    ReceiveLowWater = 4100
    SendTimeout = 4101
    ReceiveTimeout = 4102
    Error = 4103
    Type = 4104
    ReuseUnicastPort = 12295
    UpdateAcceptContext = 28683
    UpdateConnectContext = 28688
    MaxConnections = 2147483647


class SocketShutdown(Enum):
    Receive = 0
    Send = 1
    Both = 2


class SocketType(Enum):
    Unknown = -1
    Stream = 1
    Dgram = 2
    Raw = 3
    Rdm = 4
    Seqpacket = 5


class TransmitFileOptions(Enum):
    UseDefaultWorkerThread = 0
    Disconnect = 1
    ReuseSocket = 2
    WriteBehind = 4
    UseSystemThread = 16
    UseKernelApc = 32


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
