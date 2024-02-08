from __future__ import annotations

from abc import ABC
from typing import Callable
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import Tuple
from typing import TypeVar
from typing import overload

from System import Array
from System import ArraySegment
from System import AsyncCallback
from System import Enum
from System import EventArgs
from System import EventHandler
from System import Exception
from System import IAsyncResult
from System import IDisposable
from System import IEquatable
from System import IntPtr
from System import Object
from System import Type
from System import ValueType
from System.Collections import IDictionary
from System.Collections import IList
from System.Collections.Generic import IList
from System.ComponentModel import Win32Exception
from System.IO import FileAccess
from System.IO import SeekOrigin
from System.IO import Stream
from System.Net import ContextAwareResult
from System.Net import DnsEndPoint
from System.Net import EndPoint
from System.Net import IPAddress
from System.Net import IPEndPoint
from System.Net import SafeCloseSocket
from System.Net import SafeNativeOverlapped
from System.Reflection import MethodBase
from System.Runtime.InteropServices import SafeHandle
from System.Runtime.InteropServices import _Exception
from System.Runtime.Remoting import ObjRef
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Threading import CancellationToken
from System.Threading import WaitHandle
from System.Threading.Tasks import Task

T = TypeVar("T")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

class AcceptAsyncResult(ContextAwareResult, IAsyncResult):
    """"""

    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
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

AcceptExDelegate: Callable[
    [SafeCloseSocket, SafeCloseSocket, IntPtr, int, int, int, int, SafeHandle], bool
] = ...
"""

:param listenSocketHandle: 
:param acceptSocketHandle: 
:param buffer: 
:param len: 
:param localAddressLength: 
:param remoteAddressLength: 
:param bytesReceived: 
:param overlapped: 
:return: 
"""

class AcceptOverlappedAsyncResult(BaseOverlappedAsyncResult, IAsyncResult):
    """"""

    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
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

class AddressFamily(Enum):
    """"""

    Unspecified: AddressFamily = ...
    """"""
    Unix: AddressFamily = ...
    """"""
    InterNetwork: AddressFamily = ...
    """"""
    ImpLink: AddressFamily = ...
    """"""
    Pup: AddressFamily = ...
    """"""
    Chaos: AddressFamily = ...
    """"""
    Ipx: AddressFamily = ...
    """"""
    NS: AddressFamily = ...
    """"""
    Iso: AddressFamily = ...
    """"""
    Osi: AddressFamily = ...
    """"""
    Ecma: AddressFamily = ...
    """"""
    DataKit: AddressFamily = ...
    """"""
    Ccitt: AddressFamily = ...
    """"""
    Sna: AddressFamily = ...
    """"""
    DecNet: AddressFamily = ...
    """"""
    DataLink: AddressFamily = ...
    """"""
    Lat: AddressFamily = ...
    """"""
    HyperChannel: AddressFamily = ...
    """"""
    AppleTalk: AddressFamily = ...
    """"""
    NetBios: AddressFamily = ...
    """"""
    VoiceView: AddressFamily = ...
    """"""
    FireFox: AddressFamily = ...
    """"""
    Banyan: AddressFamily = ...
    """"""
    Atm: AddressFamily = ...
    """"""
    InterNetworkV6: AddressFamily = ...
    """"""
    Cluster: AddressFamily = ...
    """"""
    Ieee12844: AddressFamily = ...
    """"""
    Irda: AddressFamily = ...
    """"""
    NetworkDesigners: AddressFamily = ...
    """"""
    Max: AddressFamily = ...
    """"""
    Unknown: AddressFamily = ...
    """"""

class AsyncEventBits(Enum):
    """"""

    FdNone: AsyncEventBits = ...
    """"""
    FdRead: AsyncEventBits = ...
    """"""
    FdWrite: AsyncEventBits = ...
    """"""
    FdOob: AsyncEventBits = ...
    """"""
    FdAccept: AsyncEventBits = ...
    """"""
    FdConnect: AsyncEventBits = ...
    """"""
    FdClose: AsyncEventBits = ...
    """"""
    FdQos: AsyncEventBits = ...
    """"""
    FdGroupQos: AsyncEventBits = ...
    """"""
    FdRoutingInterfaceChange: AsyncEventBits = ...
    """"""
    FdAddressListChange: AsyncEventBits = ...
    """"""
    FdAllEvents: AsyncEventBits = ...
    """"""

class AsyncEventBitsPos(Enum):
    """"""

    FdReadBit: AsyncEventBitsPos = ...
    """"""
    FdWriteBit: AsyncEventBitsPos = ...
    """"""
    FdOobBit: AsyncEventBitsPos = ...
    """"""
    FdAcceptBit: AsyncEventBitsPos = ...
    """"""
    FdConnectBit: AsyncEventBitsPos = ...
    """"""
    FdCloseBit: AsyncEventBitsPos = ...
    """"""
    FdQosBit: AsyncEventBitsPos = ...
    """"""
    FdGroupQosBit: AsyncEventBitsPos = ...
    """"""
    FdRoutingInterfaceChangeBit: AsyncEventBitsPos = ...
    """"""
    FdAddressListChangeBit: AsyncEventBitsPos = ...
    """"""
    FdMaxEvents: AsyncEventBitsPos = ...
    """"""

class BaseOverlappedAsyncResult(ContextAwareResult, IAsyncResult):
    """"""

    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
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

class ConnectAsyncResult(ContextAwareResult, IAsyncResult):
    """"""

    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
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

ConnectExDelegate: Callable[
    [SafeCloseSocket, IntPtr, int, IntPtr, int, int, SafeHandle], bool
] = ...
"""

:param socketHandle: 
:param socketAddress: 
:param socketAddressSize: 
:param buffer: 
:param dataLength: 
:param bytesSent: 
:param overlapped: 
:return: 
"""

class ConnectOverlappedAsyncResult(BaseOverlappedAsyncResult, IAsyncResult):
    """"""

    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
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

DisconnectExDelegate: Callable[[SafeCloseSocket, SafeHandle, int, int], bool] = ...
"""

:param socketHandle: 
:param overlapped: 
:param flags: 
:param reserved: 
:return: 
"""
DisconnectExDelegate_Blocking: Callable[[IntPtr, IntPtr, int, int], bool] = ...
"""

:param socketHandle: 
:param overlapped: 
:param flags: 
:param reserved: 
:return: 
"""

class DisconnectOverlappedAsyncResult(BaseOverlappedAsyncResult, IAsyncResult):
    """"""

    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
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

class DynamicWinsockMethods(Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetDelegate(self, socketHandle: SafeCloseSocket) -> T:
        """

        :param socketHandle:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @classmethod
    def GetMethods(
        cls, addressFamily: AddressFamily, socketType: SocketType, protocolType: ProtocolType
    ) -> DynamicWinsockMethods:
        """

        :param addressFamily:
        :param socketType:
        :param protocolType:
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

GetAcceptExSockaddrsDelegate: Callable[
    [IntPtr, int, int, int, IntPtr, int, IntPtr, int], None
] = ...
"""

:param buffer: 
:param receiveDataLength: 
:param localAddressLength: 
:param remoteAddressLength: 
:param localSocketAddress: 
:param localSocketAddressLength: 
:param remoteSocketAddress: 
:param remoteSocketAddressLength: 
"""

class IOControlCode(Enum):
    """"""

    EnableCircularQueuing: IOControlCode = ...
    """"""
    Flush: IOControlCode = ...
    """"""
    AddressListChange: IOControlCode = ...
    """"""
    DataToRead: IOControlCode = ...
    """"""
    OobDataRead: IOControlCode = ...
    """"""
    GetBroadcastAddress: IOControlCode = ...
    """"""
    AddressListQuery: IOControlCode = ...
    """"""
    QueryTargetPnpHandle: IOControlCode = ...
    """"""
    AsyncIO: IOControlCode = ...
    """"""
    NonBlockingIO: IOControlCode = ...
    """"""
    AssociateHandle: IOControlCode = ...
    """"""
    MultipointLoopback: IOControlCode = ...
    """"""
    MulticastScope: IOControlCode = ...
    """"""
    SetQos: IOControlCode = ...
    """"""
    SetGroupQos: IOControlCode = ...
    """"""
    RoutingInterfaceChange: IOControlCode = ...
    """"""
    NamespaceChange: IOControlCode = ...
    """"""
    ReceiveAll: IOControlCode = ...
    """"""
    ReceiveAllMulticast: IOControlCode = ...
    """"""
    ReceiveAllIgmpMulticast: IOControlCode = ...
    """"""
    KeepAliveValues: IOControlCode = ...
    """"""
    AbsorbRouterAlert: IOControlCode = ...
    """"""
    UnicastInterface: IOControlCode = ...
    """"""
    LimitBroadcasts: IOControlCode = ...
    """"""
    BindToInterface: IOControlCode = ...
    """"""
    MulticastInterface: IOControlCode = ...
    """"""
    AddMulticastGroupOnInterface: IOControlCode = ...
    """"""
    DeleteMulticastGroupFromInterface: IOControlCode = ...
    """"""
    GetExtensionFunctionPointer: IOControlCode = ...
    """"""
    GetQos: IOControlCode = ...
    """"""
    GetGroupQos: IOControlCode = ...
    """"""
    TranslateHandle: IOControlCode = ...
    """"""
    RoutingInterfaceQuery: IOControlCode = ...
    """"""
    AddressListSort: IOControlCode = ...
    """"""

class IPPacketInformation(ValueType):
    """"""

    @property
    def Address(self) -> IPAddress:
        """

        :return:
        """
    @property
    def Interface(self) -> int:
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
    def __eq__(self, other: IPPacketInformation) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: IPPacketInformation) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(
        cls, packetInformation1: IPPacketInformation, packetInformation2: IPPacketInformation
    ) -> bool:
        """

        :param packetInformation1:
        :param packetInformation2:
        :return:
        """
    @classmethod
    def op_Inequality(
        cls, packetInformation1: IPPacketInformation, packetInformation2: IPPacketInformation
    ) -> bool:
        """

        :param packetInformation1:
        :param packetInformation2:
        :return:
        """

class IPProtectionLevel(Enum):
    """"""

    Unrestricted: IPProtectionLevel = ...
    """"""
    EdgeRestricted: IPProtectionLevel = ...
    """"""
    Restricted: IPProtectionLevel = ...
    """"""
    Unspecified: IPProtectionLevel = ...
    """"""

class IPv6MulticastOption(Object):
    """"""

    @overload
    def __init__(self, group: IPAddress):
        """

        :param group:
        """
    @overload
    def __init__(self, group: IPAddress, ifindex: int):
        """

        :param group:
        :param ifindex:
        """
    @property
    def Group(self) -> IPAddress:
        """

        :return:
        """
    @Group.setter
    def Group(self, value: IPAddress) -> None: ...
    @property
    def InterfaceIndex(self) -> int:
        """

        :return:
        """
    @InterfaceIndex.setter
    def InterfaceIndex(self, value: int) -> None: ...
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

class IoctlSocketConstants(ABC, Object):
    """"""

    FIOASYNC: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FIONBIO: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    FIONREAD: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    SIOGETEXTENSIONFUNCTIONPOINTER: Final[ClassVar[int]] = ...
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

class LingerOption(Object):
    """"""

    def __init__(self, enable: bool, seconds: int):
        """

        :param enable:
        :param seconds:
        """
    @property
    def Enabled(self) -> bool:
        """

        :return:
        """
    @Enabled.setter
    def Enabled(self, value: bool) -> None: ...
    @property
    def LingerTime(self) -> int:
        """

        :return:
        """
    @LingerTime.setter
    def LingerTime(self, value: int) -> None: ...
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

class MulticastOption(Object):
    """"""

    @overload
    def __init__(self, group: IPAddress):
        """

        :param group:
        """
    @overload
    def __init__(self, group: IPAddress, mcint: IPAddress):
        """

        :param group:
        :param mcint:
        """
    @overload
    def __init__(self, group: IPAddress, interfaceIndex: int):
        """

        :param group:
        :param interfaceIndex:
        """
    @property
    def Group(self) -> IPAddress:
        """

        :return:
        """
    @Group.setter
    def Group(self, value: IPAddress) -> None: ...
    @property
    def InterfaceIndex(self) -> int:
        """

        :return:
        """
    @InterfaceIndex.setter
    def InterfaceIndex(self, value: int) -> None: ...
    @property
    def LocalAddress(self) -> IPAddress:
        """

        :return:
        """
    @LocalAddress.setter
    def LocalAddress(self, value: IPAddress) -> None: ...
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

class MultipleConnectAsync(ABC, Object):
    """"""

    def Cancel(self) -> None:
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
    def StartConnectAsync(self, args: SocketAsyncEventArgs, endPoint: DnsEndPoint) -> bool:
        """

        :param args:
        :param endPoint:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class MultipleSocketMultipleConnectAsync(MultipleConnectAsync):
    """"""

    def __init__(self, socketType: SocketType, protocolType: ProtocolType):
        """

        :param socketType:
        :param protocolType:
        """
    def Cancel(self) -> None:
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
    def StartConnectAsync(self, args: SocketAsyncEventArgs, endPoint: DnsEndPoint) -> bool:
        """

        :param args:
        :param endPoint:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class NetworkEvents(ValueType):
    """"""

    ErrorCodes: Final[Array[int]] = ...
    """
    
    :return: 
    """
    Events: Final[AsyncEventBits] = ...
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

class NetworkStream(Stream, IDisposable):
    """"""

    @overload
    def __init__(self, socket: Socket):
        """

        :param socket:
        """
    @overload
    def __init__(self, socket: Socket, access: FileAccess):
        """

        :param socket:
        :param access:
        """
    @overload
    def __init__(self, socket: Socket, ownsSocket: bool):
        """

        :param socket:
        :param ownsSocket:
        """
    @overload
    def __init__(self, socket: Socket, access: FileAccess, ownsSocket: bool):
        """

        :param socket:
        :param access:
        :param ownsSocket:
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
    def DataAvailable(self) -> bool:
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
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
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
    @overload
    def Close(self) -> None:
        """"""
    @overload
    def Close(self, timeout: int) -> None:
        """

        :param timeout:
        """
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

class OverlappedAsyncResult(BaseOverlappedAsyncResult, IAsyncResult):
    """"""

    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
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

class OverlappedCache(Object):
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

class ProtocolFamily(Enum):
    """"""

    Unspecified: ProtocolFamily = ...
    """"""
    Unix: ProtocolFamily = ...
    """"""
    InterNetwork: ProtocolFamily = ...
    """"""
    ImpLink: ProtocolFamily = ...
    """"""
    Pup: ProtocolFamily = ...
    """"""
    Chaos: ProtocolFamily = ...
    """"""
    Ipx: ProtocolFamily = ...
    """"""
    NS: ProtocolFamily = ...
    """"""
    Iso: ProtocolFamily = ...
    """"""
    Osi: ProtocolFamily = ...
    """"""
    Ecma: ProtocolFamily = ...
    """"""
    DataKit: ProtocolFamily = ...
    """"""
    Ccitt: ProtocolFamily = ...
    """"""
    Sna: ProtocolFamily = ...
    """"""
    DecNet: ProtocolFamily = ...
    """"""
    DataLink: ProtocolFamily = ...
    """"""
    Lat: ProtocolFamily = ...
    """"""
    HyperChannel: ProtocolFamily = ...
    """"""
    AppleTalk: ProtocolFamily = ...
    """"""
    NetBios: ProtocolFamily = ...
    """"""
    VoiceView: ProtocolFamily = ...
    """"""
    FireFox: ProtocolFamily = ...
    """"""
    Banyan: ProtocolFamily = ...
    """"""
    Atm: ProtocolFamily = ...
    """"""
    InterNetworkV6: ProtocolFamily = ...
    """"""
    Cluster: ProtocolFamily = ...
    """"""
    Ieee12844: ProtocolFamily = ...
    """"""
    Irda: ProtocolFamily = ...
    """"""
    NetworkDesigners: ProtocolFamily = ...
    """"""
    Max: ProtocolFamily = ...
    """"""
    Unknown: ProtocolFamily = ...
    """"""

class ProtocolType(Enum):
    """"""

    IPv6HopByHopOptions: ProtocolType = ...
    """"""
    IP: ProtocolType = ...
    """"""
    Unspecified: ProtocolType = ...
    """"""
    Icmp: ProtocolType = ...
    """"""
    Igmp: ProtocolType = ...
    """"""
    Ggp: ProtocolType = ...
    """"""
    IPv4: ProtocolType = ...
    """"""
    Tcp: ProtocolType = ...
    """"""
    Pup: ProtocolType = ...
    """"""
    Udp: ProtocolType = ...
    """"""
    Idp: ProtocolType = ...
    """"""
    IPv6: ProtocolType = ...
    """"""
    IPv6RoutingHeader: ProtocolType = ...
    """"""
    IPv6FragmentHeader: ProtocolType = ...
    """"""
    IPSecEncapsulatingSecurityPayload: ProtocolType = ...
    """"""
    IPSecAuthenticationHeader: ProtocolType = ...
    """"""
    IcmpV6: ProtocolType = ...
    """"""
    IPv6NoNextHeader: ProtocolType = ...
    """"""
    IPv6DestinationOptions: ProtocolType = ...
    """"""
    ND: ProtocolType = ...
    """"""
    Raw: ProtocolType = ...
    """"""
    Ipx: ProtocolType = ...
    """"""
    Spx: ProtocolType = ...
    """"""
    SpxII: ProtocolType = ...
    """"""
    Unknown: ProtocolType = ...
    """"""

class ReceiveFromOverlappedAsyncResult(OverlappedAsyncResult, IAsyncResult):
    """"""

    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
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

class ReceiveMessageOverlappedAsyncResult(BaseOverlappedAsyncResult, IAsyncResult):
    """"""

    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
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

class SelectMode(Enum):
    """"""

    SelectRead: SelectMode = ...
    """"""
    SelectWrite: SelectMode = ...
    """"""
    SelectError: SelectMode = ...
    """"""

class SendPacketsElement(Object):
    """"""

    @overload
    def __init__(self, buffer: Array[int]):
        """

        :param buffer:
        """
    @overload
    def __init__(self, filepath: str):
        """

        :param filepath:
        """
    @overload
    def __init__(self, buffer: Array[int], offset: int, count: int):
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def __init__(self, filepath: str, offset: int, count: int):
        """

        :param filepath:
        :param offset:
        :param count:
        """
    @overload
    def __init__(self, buffer: Array[int], offset: int, count: int, endOfPacket: bool):
        """

        :param buffer:
        :param offset:
        :param count:
        :param endOfPacket:
        """
    @overload
    def __init__(self, filepath: str, offset: int, count: int, endOfPacket: bool):
        """

        :param filepath:
        :param offset:
        :param count:
        :param endOfPacket:
        """
    @property
    def Buffer(self) -> Array[int]:
        """

        :return:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def EndOfPacket(self) -> bool:
        """

        :return:
        """
    @property
    def FilePath(self) -> str:
        """

        :return:
        """
    @property
    def Offset(self) -> int:
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

class SingleSocketMultipleConnectAsync(MultipleConnectAsync):
    """"""

    def __init__(self, socket: Socket, userSocket: bool):
        """

        :param socket:
        :param userSocket:
        """
    def Cancel(self) -> None:
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
    def StartConnectAsync(self, args: SocketAsyncEventArgs, endPoint: DnsEndPoint) -> bool:
        """

        :param args:
        :param endPoint:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class Socket(Object, IDisposable):
    """"""

    @overload
    def __init__(self, socketInformation: SocketInformation):
        """

        :param socketInformation:
        """
    @overload
    def __init__(self, socketType: SocketType, protocolType: ProtocolType):
        """

        :param socketType:
        :param protocolType:
        """
    @overload
    def __init__(
        self, addressFamily: AddressFamily, socketType: SocketType, protocolType: ProtocolType
    ):
        """

        :param addressFamily:
        :param socketType:
        :param protocolType:
        """
    @property
    def AddressFamily(self) -> AddressFamily:
        """

        :return:
        """
    @property
    def Available(self) -> int:
        """

        :return:
        """
    @property
    def Blocking(self) -> bool:
        """

        :return:
        """
    @Blocking.setter
    def Blocking(self, value: bool) -> None: ...
    @property
    def Connected(self) -> bool:
        """

        :return:
        """
    @property
    def DontFragment(self) -> bool:
        """

        :return:
        """
    @DontFragment.setter
    def DontFragment(self, value: bool) -> None: ...
    @property
    def DualMode(self) -> bool:
        """

        :return:
        """
    @DualMode.setter
    def DualMode(self, value: bool) -> None: ...
    @property
    def EnableBroadcast(self) -> bool:
        """

        :return:
        """
    @EnableBroadcast.setter
    def EnableBroadcast(self, value: bool) -> None: ...
    @property
    def ExclusiveAddressUse(self) -> bool:
        """

        :return:
        """
    @ExclusiveAddressUse.setter
    def ExclusiveAddressUse(self, value: bool) -> None: ...
    @property
    def Handle(self) -> IntPtr:
        """

        :return:
        """
    @property
    def IsBound(self) -> bool:
        """

        :return:
        """
    @property
    def LingerState(self) -> LingerOption:
        """

        :return:
        """
    @LingerState.setter
    def LingerState(self, value: LingerOption) -> None: ...
    @property
    def LocalEndPoint(self) -> EndPoint:
        """

        :return:
        """
    @property
    def MulticastLoopback(self) -> bool:
        """

        :return:
        """
    @MulticastLoopback.setter
    def MulticastLoopback(self, value: bool) -> None: ...
    @property
    def NoDelay(self) -> bool:
        """

        :return:
        """
    @NoDelay.setter
    def NoDelay(self, value: bool) -> None: ...
    @classmethod
    @property
    def OSSupportsIPv4(cls) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def OSSupportsIPv6(cls) -> bool:
        """

        :return:
        """
    @property
    def ProtocolType(self) -> ProtocolType:
        """

        :return:
        """
    @property
    def ReceiveBufferSize(self) -> int:
        """

        :return:
        """
    @ReceiveBufferSize.setter
    def ReceiveBufferSize(self, value: int) -> None: ...
    @property
    def ReceiveTimeout(self) -> int:
        """

        :return:
        """
    @ReceiveTimeout.setter
    def ReceiveTimeout(self, value: int) -> None: ...
    @property
    def RemoteEndPoint(self) -> EndPoint:
        """

        :return:
        """
    @property
    def SendBufferSize(self) -> int:
        """

        :return:
        """
    @SendBufferSize.setter
    def SendBufferSize(self, value: int) -> None: ...
    @property
    def SendTimeout(self) -> int:
        """

        :return:
        """
    @SendTimeout.setter
    def SendTimeout(self, value: int) -> None: ...
    @property
    def SocketType(self) -> SocketType:
        """

        :return:
        """
    @classmethod
    @property
    def SupportsIPv4(cls) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def SupportsIPv6(cls) -> bool:
        """

        :return:
        """
    @property
    def Ttl(self) -> int:
        """

        :return:
        """
    @Ttl.setter
    def Ttl(self, value: int) -> None: ...
    @property
    def UseOnlyOverlappedIO(self) -> bool:
        """

        :return:
        """
    @UseOnlyOverlappedIO.setter
    def UseOnlyOverlappedIO(self, value: bool) -> None: ...
    def Accept(self) -> Socket:
        """

        :return:
        """
    def AcceptAsync(self, e: SocketAsyncEventArgs) -> bool:
        """

        :param e:
        :return:
        """
    @overload
    def BeginAccept(self, callback: AsyncCallback, state: object) -> IAsyncResult:
        """

        :param callback:
        :param state:
        :return:
        """
    @overload
    def BeginAccept(self, receiveSize: int, callback: AsyncCallback, state: object) -> IAsyncResult:
        """

        :param receiveSize:
        :param callback:
        :param state:
        :return:
        """
    @overload
    def BeginAccept(
        self, acceptSocket: Socket, receiveSize: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param acceptSocket:
        :param receiveSize:
        :param callback:
        :param state:
        :return:
        """
    @overload
    def BeginConnect(
        self, remoteEP: EndPoint, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param remoteEP:
        :param callback:
        :param state:
        :return:
        """
    @overload
    def BeginConnect(
        self, address: IPAddress, port: int, requestCallback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param address:
        :param port:
        :param requestCallback:
        :param state:
        :return:
        """
    @overload
    def BeginConnect(
        self, addresses: Array[IPAddress], port: int, requestCallback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param addresses:
        :param port:
        :param requestCallback:
        :param state:
        :return:
        """
    @overload
    def BeginConnect(
        self, host: str, port: int, requestCallback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param host:
        :param port:
        :param requestCallback:
        :param state:
        :return:
        """
    def BeginDisconnect(
        self, reuseSocket: bool, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param reuseSocket:
        :param callback:
        :param state:
        :return:
        """
    @overload
    def BeginReceive(
        self,
        buffers: IList[ArraySegment[int]],
        socketFlags: SocketFlags,
        callback: AsyncCallback,
        state: object,
    ) -> IAsyncResult:
        """

        :param buffers:
        :param socketFlags:
        :param callback:
        :param state:
        :return:
        """
    @overload
    def BeginReceive(
        self,
        buffers: IList[ArraySegment[int]],
        socketFlags: SocketFlags,
        errorCode: SocketError,
        callback: AsyncCallback,
        state: object,
    ) -> Tuple[IAsyncResult, SocketError]:
        """

        :param buffers:
        :param socketFlags:
        :param errorCode:
        :param callback:
        :param state:
        :return:
        """
    @overload
    def BeginReceive(
        self,
        buffer: Array[int],
        offset: int,
        size: int,
        socketFlags: SocketFlags,
        callback: AsyncCallback,
        state: object,
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param size:
        :param socketFlags:
        :param callback:
        :param state:
        :return:
        """
    @overload
    def BeginReceive(
        self,
        buffer: Array[int],
        offset: int,
        size: int,
        socketFlags: SocketFlags,
        errorCode: SocketError,
        callback: AsyncCallback,
        state: object,
    ) -> Tuple[IAsyncResult, SocketError]:
        """

        :param buffer:
        :param offset:
        :param size:
        :param socketFlags:
        :param errorCode:
        :param callback:
        :param state:
        :return:
        """
    def BeginReceiveFrom(
        self,
        buffer: Array[int],
        offset: int,
        size: int,
        socketFlags: SocketFlags,
        remoteEP: EndPoint,
        callback: AsyncCallback,
        state: object,
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param size:
        :param socketFlags:
        :param remoteEP:
        :param callback:
        :param state:
        :return:
        """
    def BeginReceiveMessageFrom(
        self,
        buffer: Array[int],
        offset: int,
        size: int,
        socketFlags: SocketFlags,
        remoteEP: EndPoint,
        callback: AsyncCallback,
        state: object,
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param size:
        :param socketFlags:
        :param remoteEP:
        :param callback:
        :param state:
        :return:
        """
    @overload
    def BeginSend(
        self,
        buffers: IList[ArraySegment[int]],
        socketFlags: SocketFlags,
        callback: AsyncCallback,
        state: object,
    ) -> IAsyncResult:
        """

        :param buffers:
        :param socketFlags:
        :param callback:
        :param state:
        :return:
        """
    @overload
    def BeginSend(
        self,
        buffers: IList[ArraySegment[int]],
        socketFlags: SocketFlags,
        errorCode: SocketError,
        callback: AsyncCallback,
        state: object,
    ) -> Tuple[IAsyncResult, SocketError]:
        """

        :param buffers:
        :param socketFlags:
        :param errorCode:
        :param callback:
        :param state:
        :return:
        """
    @overload
    def BeginSend(
        self,
        buffer: Array[int],
        offset: int,
        size: int,
        socketFlags: SocketFlags,
        callback: AsyncCallback,
        state: object,
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param size:
        :param socketFlags:
        :param callback:
        :param state:
        :return:
        """
    @overload
    def BeginSend(
        self,
        buffer: Array[int],
        offset: int,
        size: int,
        socketFlags: SocketFlags,
        errorCode: SocketError,
        callback: AsyncCallback,
        state: object,
    ) -> Tuple[IAsyncResult, SocketError]:
        """

        :param buffer:
        :param offset:
        :param size:
        :param socketFlags:
        :param errorCode:
        :param callback:
        :param state:
        :return:
        """
    @overload
    def BeginSendFile(self, fileName: str, callback: AsyncCallback, state: object) -> IAsyncResult:
        """

        :param fileName:
        :param callback:
        :param state:
        :return:
        """
    @overload
    def BeginSendFile(
        self,
        fileName: str,
        preBuffer: Array[int],
        postBuffer: Array[int],
        flags: TransmitFileOptions,
        callback: AsyncCallback,
        state: object,
    ) -> IAsyncResult:
        """

        :param fileName:
        :param preBuffer:
        :param postBuffer:
        :param flags:
        :param callback:
        :param state:
        :return:
        """
    def BeginSendTo(
        self,
        buffer: Array[int],
        offset: int,
        size: int,
        socketFlags: SocketFlags,
        remoteEP: EndPoint,
        callback: AsyncCallback,
        state: object,
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param size:
        :param socketFlags:
        :param remoteEP:
        :param callback:
        :param state:
        :return:
        """
    def Bind(self, localEP: EndPoint) -> None:
        """

        :param localEP:
        """
    @classmethod
    def CancelConnectAsync(cls, e: SocketAsyncEventArgs) -> None:
        """

        :param e:
        """
    @overload
    def Close(self) -> None:
        """"""
    @overload
    def Close(self, timeout: int) -> None:
        """

        :param timeout:
        """
    @overload
    def Connect(self, remoteEP: EndPoint) -> None:
        """

        :param remoteEP:
        """
    @overload
    def Connect(self, address: IPAddress, port: int) -> None:
        """

        :param address:
        :param port:
        """
    @overload
    def Connect(self, addresses: Array[IPAddress], port: int) -> None:
        """

        :param addresses:
        :param port:
        """
    @overload
    def Connect(self, host: str, port: int) -> None:
        """

        :param host:
        :param port:
        """
    @overload
    def ConnectAsync(self, e: SocketAsyncEventArgs) -> bool:
        """

        :param e:
        :return:
        """
    @classmethod
    @overload
    def ConnectAsync(
        cls, socketType: SocketType, protocolType: ProtocolType, e: SocketAsyncEventArgs
    ) -> bool:
        """

        :param socketType:
        :param protocolType:
        :param e:
        :return:
        """
    def Disconnect(self, reuseSocket: bool) -> None:
        """

        :param reuseSocket:
        """
    def DisconnectAsync(self, e: SocketAsyncEventArgs) -> bool:
        """

        :param e:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def DuplicateAndClose(self, targetProcessId: int) -> SocketInformation:
        """

        :param targetProcessId:
        :return:
        """
    @overload
    def EndAccept(self, asyncResult: IAsyncResult) -> Socket:
        """

        :param asyncResult:
        :return:
        """
    @overload
    def EndAccept(self, buffer: int, asyncResult: IAsyncResult) -> Tuple[Socket, int]:
        """

        :param buffer:
        :param asyncResult:
        :return:
        """
    @overload
    def EndAccept(
        self, buffer: int, bytesTransferred: int, asyncResult: IAsyncResult
    ) -> Tuple[Socket, int, int]:
        """

        :param buffer:
        :param bytesTransferred:
        :param asyncResult:
        :return:
        """
    def EndConnect(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def EndDisconnect(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    @overload
    def EndReceive(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    @overload
    def EndReceive(
        self, asyncResult: IAsyncResult, errorCode: SocketError
    ) -> Tuple[int, SocketError]:
        """

        :param asyncResult:
        :param errorCode:
        :return:
        """
    def EndReceiveFrom(self, asyncResult: IAsyncResult, endPoint: EndPoint) -> int:
        """

        :param asyncResult:
        :param endPoint:
        :return:
        """
    def EndReceiveMessageFrom(
        self,
        asyncResult: IAsyncResult,
        socketFlags: SocketFlags,
        endPoint: EndPoint,
        ipPacketInformation: IPPacketInformation,
    ) -> Tuple[int, IPPacketInformation]:
        """

        :param asyncResult:
        :param socketFlags:
        :param endPoint:
        :param ipPacketInformation:
        :return:
        """
    @overload
    def EndSend(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    @overload
    def EndSend(self, asyncResult: IAsyncResult, errorCode: SocketError) -> Tuple[int, SocketError]:
        """

        :param asyncResult:
        :param errorCode:
        :return:
        """
    def EndSendFile(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def EndSendTo(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
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
    @overload
    def GetSocketOption(
        self, optionLevel: SocketOptionLevel, optionName: SocketOptionName
    ) -> object:
        """

        :param optionLevel:
        :param optionName:
        :return:
        """
    @overload
    def GetSocketOption(
        self, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: Array[int]
    ) -> None:
        """

        :param optionLevel:
        :param optionName:
        :param optionValue:
        """
    @overload
    def GetSocketOption(
        self, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionLength: int
    ) -> Array[int]:
        """

        :param optionLevel:
        :param optionName:
        :param optionLength:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IOControl(
        self, ioControlCode: IOControlCode, optionInValue: Array[int], optionOutValue: Array[int]
    ) -> int:
        """

        :param ioControlCode:
        :param optionInValue:
        :param optionOutValue:
        :return:
        """
    @overload
    def IOControl(
        self, ioControlCode: int, optionInValue: Array[int], optionOutValue: Array[int]
    ) -> int:
        """

        :param ioControlCode:
        :param optionInValue:
        :param optionOutValue:
        :return:
        """
    def Listen(self, backlog: int) -> None:
        """

        :param backlog:
        """
    def Poll(self, microSeconds: int, mode: SelectMode) -> bool:
        """

        :param microSeconds:
        :param mode:
        :return:
        """
    @overload
    def Receive(self, buffers: IList[ArraySegment[int]]) -> int:
        """

        :param buffers:
        :return:
        """
    @overload
    def Receive(self, buffer: Array[int]) -> int:
        """

        :param buffer:
        :return:
        """
    @overload
    def Receive(self, buffers: IList[ArraySegment[int]], socketFlags: SocketFlags) -> int:
        """

        :param buffers:
        :param socketFlags:
        :return:
        """
    @overload
    def Receive(self, buffer: Array[int], socketFlags: SocketFlags) -> int:
        """

        :param buffer:
        :param socketFlags:
        :return:
        """
    @overload
    def Receive(
        self, buffers: IList[ArraySegment[int]], socketFlags: SocketFlags, errorCode: SocketError
    ) -> Tuple[int, SocketError]:
        """

        :param buffers:
        :param socketFlags:
        :param errorCode:
        :return:
        """
    @overload
    def Receive(self, buffer: Array[int], size: int, socketFlags: SocketFlags) -> int:
        """

        :param buffer:
        :param size:
        :param socketFlags:
        :return:
        """
    @overload
    def Receive(self, buffer: Array[int], offset: int, size: int, socketFlags: SocketFlags) -> int:
        """

        :param buffer:
        :param offset:
        :param size:
        :param socketFlags:
        :return:
        """
    @overload
    def Receive(
        self,
        buffer: Array[int],
        offset: int,
        size: int,
        socketFlags: SocketFlags,
        errorCode: SocketError,
    ) -> Tuple[int, SocketError]:
        """

        :param buffer:
        :param offset:
        :param size:
        :param socketFlags:
        :param errorCode:
        :return:
        """
    def ReceiveAsync(self, e: SocketAsyncEventArgs) -> bool:
        """

        :param e:
        :return:
        """
    @overload
    def ReceiveFrom(self, buffer: Array[int], remoteEP: EndPoint) -> int:
        """

        :param buffer:
        :param remoteEP:
        :return:
        """
    @overload
    def ReceiveFrom(self, buffer: Array[int], socketFlags: SocketFlags, remoteEP: EndPoint) -> int:
        """

        :param buffer:
        :param socketFlags:
        :param remoteEP:
        :return:
        """
    @overload
    def ReceiveFrom(
        self, buffer: Array[int], size: int, socketFlags: SocketFlags, remoteEP: EndPoint
    ) -> int:
        """

        :param buffer:
        :param size:
        :param socketFlags:
        :param remoteEP:
        :return:
        """
    @overload
    def ReceiveFrom(
        self,
        buffer: Array[int],
        offset: int,
        size: int,
        socketFlags: SocketFlags,
        remoteEP: EndPoint,
    ) -> int:
        """

        :param buffer:
        :param offset:
        :param size:
        :param socketFlags:
        :param remoteEP:
        :return:
        """
    def ReceiveFromAsync(self, e: SocketAsyncEventArgs) -> bool:
        """

        :param e:
        :return:
        """
    def ReceiveMessageFrom(
        self,
        buffer: Array[int],
        offset: int,
        size: int,
        socketFlags: SocketFlags,
        remoteEP: EndPoint,
        ipPacketInformation: IPPacketInformation,
    ) -> Tuple[int, IPPacketInformation]:
        """

        :param buffer:
        :param offset:
        :param size:
        :param socketFlags:
        :param remoteEP:
        :param ipPacketInformation:
        :return:
        """
    def ReceiveMessageFromAsync(self, e: SocketAsyncEventArgs) -> bool:
        """

        :param e:
        :return:
        """
    @classmethod
    def Select(
        cls, checkRead: IList, checkWrite: IList, checkError: IList, microSeconds: int
    ) -> None:
        """

        :param checkRead:
        :param checkWrite:
        :param checkError:
        :param microSeconds:
        """
    @overload
    def Send(self, buffers: IList[ArraySegment[int]]) -> int:
        """

        :param buffers:
        :return:
        """
    @overload
    def Send(self, buffer: Array[int]) -> int:
        """

        :param buffer:
        :return:
        """
    @overload
    def Send(self, buffers: IList[ArraySegment[int]], socketFlags: SocketFlags) -> int:
        """

        :param buffers:
        :param socketFlags:
        :return:
        """
    @overload
    def Send(self, buffer: Array[int], socketFlags: SocketFlags) -> int:
        """

        :param buffer:
        :param socketFlags:
        :return:
        """
    @overload
    def Send(
        self, buffers: IList[ArraySegment[int]], socketFlags: SocketFlags, errorCode: SocketError
    ) -> Tuple[int, SocketError]:
        """

        :param buffers:
        :param socketFlags:
        :param errorCode:
        :return:
        """
    @overload
    def Send(self, buffer: Array[int], size: int, socketFlags: SocketFlags) -> int:
        """

        :param buffer:
        :param size:
        :param socketFlags:
        :return:
        """
    @overload
    def Send(self, buffer: Array[int], offset: int, size: int, socketFlags: SocketFlags) -> int:
        """

        :param buffer:
        :param offset:
        :param size:
        :param socketFlags:
        :return:
        """
    @overload
    def Send(
        self,
        buffer: Array[int],
        offset: int,
        size: int,
        socketFlags: SocketFlags,
        errorCode: SocketError,
    ) -> Tuple[int, SocketError]:
        """

        :param buffer:
        :param offset:
        :param size:
        :param socketFlags:
        :param errorCode:
        :return:
        """
    def SendAsync(self, e: SocketAsyncEventArgs) -> bool:
        """

        :param e:
        :return:
        """
    @overload
    def SendFile(self, fileName: str) -> None:
        """

        :param fileName:
        """
    @overload
    def SendFile(
        self,
        fileName: str,
        preBuffer: Array[int],
        postBuffer: Array[int],
        flags: TransmitFileOptions,
    ) -> None:
        """

        :param fileName:
        :param preBuffer:
        :param postBuffer:
        :param flags:
        """
    def SendPacketsAsync(self, e: SocketAsyncEventArgs) -> bool:
        """

        :param e:
        :return:
        """
    @overload
    def SendTo(self, buffer: Array[int], remoteEP: EndPoint) -> int:
        """

        :param buffer:
        :param remoteEP:
        :return:
        """
    @overload
    def SendTo(self, buffer: Array[int], socketFlags: SocketFlags, remoteEP: EndPoint) -> int:
        """

        :param buffer:
        :param socketFlags:
        :param remoteEP:
        :return:
        """
    @overload
    def SendTo(
        self, buffer: Array[int], size: int, socketFlags: SocketFlags, remoteEP: EndPoint
    ) -> int:
        """

        :param buffer:
        :param size:
        :param socketFlags:
        :param remoteEP:
        :return:
        """
    @overload
    def SendTo(
        self,
        buffer: Array[int],
        offset: int,
        size: int,
        socketFlags: SocketFlags,
        remoteEP: EndPoint,
    ) -> int:
        """

        :param buffer:
        :param offset:
        :param size:
        :param socketFlags:
        :param remoteEP:
        :return:
        """
    def SendToAsync(self, e: SocketAsyncEventArgs) -> bool:
        """

        :param e:
        :return:
        """
    def SetIPProtectionLevel(self, level: IPProtectionLevel) -> None:
        """

        :param level:
        """
    @overload
    def SetSocketOption(
        self, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: Array[int]
    ) -> None:
        """

        :param optionLevel:
        :param optionName:
        :param optionValue:
        """
    @overload
    def SetSocketOption(
        self, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: bool
    ) -> None:
        """

        :param optionLevel:
        :param optionName:
        :param optionValue:
        """
    @overload
    def SetSocketOption(
        self, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: int
    ) -> None:
        """

        :param optionLevel:
        :param optionName:
        :param optionValue:
        """
    @overload
    def SetSocketOption(
        self, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: object
    ) -> None:
        """

        :param optionLevel:
        :param optionName:
        :param optionValue:
        """
    def Shutdown(self, how: SocketShutdown) -> None:
        """

        :param how:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SocketAsyncEventArgs(EventArgs, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def AcceptSocket(self) -> Socket:
        """

        :return:
        """
    @AcceptSocket.setter
    def AcceptSocket(self, value: Socket) -> None: ...
    @property
    def Buffer(self) -> Array[int]:
        """

        :return:
        """
    @property
    def BufferList(self) -> IList[ArraySegment[int]]:
        """

        :return:
        """
    @BufferList.setter
    def BufferList(self, value: IList[ArraySegment[int]]) -> None: ...
    @property
    def BytesTransferred(self) -> int:
        """

        :return:
        """
    @property
    def ConnectByNameError(self) -> Exception:
        """

        :return:
        """
    @property
    def ConnectSocket(self) -> Socket:
        """

        :return:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def DisconnectReuseSocket(self) -> bool:
        """

        :return:
        """
    @DisconnectReuseSocket.setter
    def DisconnectReuseSocket(self, value: bool) -> None: ...
    @property
    def LastOperation(self) -> SocketAsyncOperation:
        """

        :return:
        """
    @property
    def Offset(self) -> int:
        """

        :return:
        """
    @property
    def ReceiveMessageFromPacketInfo(self) -> IPPacketInformation:
        """

        :return:
        """
    @property
    def RemoteEndPoint(self) -> EndPoint:
        """

        :return:
        """
    @RemoteEndPoint.setter
    def RemoteEndPoint(self, value: EndPoint) -> None: ...
    @property
    def SendPacketsElements(self) -> Array[SendPacketsElement]:
        """

        :return:
        """
    @SendPacketsElements.setter
    def SendPacketsElements(self, value: Array[SendPacketsElement]) -> None: ...
    @property
    def SendPacketsFlags(self) -> TransmitFileOptions:
        """

        :return:
        """
    @SendPacketsFlags.setter
    def SendPacketsFlags(self, value: TransmitFileOptions) -> None: ...
    @property
    def SendPacketsSendSize(self) -> int:
        """

        :return:
        """
    @SendPacketsSendSize.setter
    def SendPacketsSendSize(self, value: int) -> None: ...
    @property
    def SocketClientAccessPolicyProtocol(self) -> SocketClientAccessPolicyProtocol:
        """

        :return:
        """
    @SocketClientAccessPolicyProtocol.setter
    def SocketClientAccessPolicyProtocol(self, value: SocketClientAccessPolicyProtocol) -> None: ...
    @property
    def SocketError(self) -> SocketError:
        """

        :return:
        """
    @SocketError.setter
    def SocketError(self, value: SocketError) -> None: ...
    @property
    def SocketFlags(self) -> SocketFlags:
        """

        :return:
        """
    @SocketFlags.setter
    def SocketFlags(self, value: SocketFlags) -> None: ...
    @property
    def UserToken(self) -> object:
        """

        :return:
        """
    @UserToken.setter
    def UserToken(self, value: object) -> None: ...
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
    @overload
    def SetBuffer(self, offset: int, count: int) -> None:
        """

        :param offset:
        :param count:
        """
    @overload
    def SetBuffer(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    Completed: EventType[EventHandler[SocketAsyncEventArgs]] = ...
    """"""

class SocketAsyncOperation(Enum):
    """"""

    _None: SocketAsyncOperation = ...
    """"""
    Accept: SocketAsyncOperation = ...
    """"""
    Connect: SocketAsyncOperation = ...
    """"""
    Disconnect: SocketAsyncOperation = ...
    """"""
    Receive: SocketAsyncOperation = ...
    """"""
    ReceiveFrom: SocketAsyncOperation = ...
    """"""
    ReceiveMessageFrom: SocketAsyncOperation = ...
    """"""
    Send: SocketAsyncOperation = ...
    """"""
    SendPackets: SocketAsyncOperation = ...
    """"""
    SendTo: SocketAsyncOperation = ...
    """"""

class SocketClientAccessPolicyProtocol(Enum):
    """"""

    Tcp: SocketClientAccessPolicyProtocol = ...
    """"""
    Http: SocketClientAccessPolicyProtocol = ...
    """"""

class SocketError(Enum):
    """"""

    Success: SocketError = ...
    """"""
    OperationAborted: SocketError = ...
    """"""
    IOPending: SocketError = ...
    """"""
    Interrupted: SocketError = ...
    """"""
    AccessDenied: SocketError = ...
    """"""
    Fault: SocketError = ...
    """"""
    InvalidArgument: SocketError = ...
    """"""
    TooManyOpenSockets: SocketError = ...
    """"""
    WouldBlock: SocketError = ...
    """"""
    InProgress: SocketError = ...
    """"""
    AlreadyInProgress: SocketError = ...
    """"""
    NotSocket: SocketError = ...
    """"""
    DestinationAddressRequired: SocketError = ...
    """"""
    MessageSize: SocketError = ...
    """"""
    ProtocolType: SocketError = ...
    """"""
    ProtocolOption: SocketError = ...
    """"""
    ProtocolNotSupported: SocketError = ...
    """"""
    SocketNotSupported: SocketError = ...
    """"""
    OperationNotSupported: SocketError = ...
    """"""
    ProtocolFamilyNotSupported: SocketError = ...
    """"""
    AddressFamilyNotSupported: SocketError = ...
    """"""
    AddressAlreadyInUse: SocketError = ...
    """"""
    AddressNotAvailable: SocketError = ...
    """"""
    NetworkDown: SocketError = ...
    """"""
    NetworkUnreachable: SocketError = ...
    """"""
    NetworkReset: SocketError = ...
    """"""
    ConnectionAborted: SocketError = ...
    """"""
    ConnectionReset: SocketError = ...
    """"""
    NoBufferSpaceAvailable: SocketError = ...
    """"""
    IsConnected: SocketError = ...
    """"""
    NotConnected: SocketError = ...
    """"""
    Shutdown: SocketError = ...
    """"""
    TimedOut: SocketError = ...
    """"""
    ConnectionRefused: SocketError = ...
    """"""
    HostDown: SocketError = ...
    """"""
    HostUnreachable: SocketError = ...
    """"""
    ProcessLimit: SocketError = ...
    """"""
    SystemNotReady: SocketError = ...
    """"""
    VersionNotSupported: SocketError = ...
    """"""
    NotInitialized: SocketError = ...
    """"""
    Disconnecting: SocketError = ...
    """"""
    TypeNotFound: SocketError = ...
    """"""
    HostNotFound: SocketError = ...
    """"""
    TryAgain: SocketError = ...
    """"""
    NoRecovery: SocketError = ...
    """"""
    NoData: SocketError = ...
    """"""
    SocketError: SocketError = ...
    """"""

class SocketException(Win32Exception, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, errorCode: int):
        """

        :param errorCode:
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
    def SocketErrorCode(self) -> SocketError:
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

class SocketFlags(Enum):
    """"""

    _None: SocketFlags = ...
    """"""
    OutOfBand: SocketFlags = ...
    """"""
    Peek: SocketFlags = ...
    """"""
    DontRoute: SocketFlags = ...
    """"""
    MaxIOVectorLength: SocketFlags = ...
    """"""
    Truncated: SocketFlags = ...
    """"""
    ControlDataTruncated: SocketFlags = ...
    """"""
    Broadcast: SocketFlags = ...
    """"""
    Multicast: SocketFlags = ...
    """"""
    Partial: SocketFlags = ...
    """"""

class SocketInformation(ValueType):
    """"""

    @property
    def Options(self) -> SocketInformationOptions:
        """

        :return:
        """
    @Options.setter
    def Options(self, value: SocketInformationOptions) -> None: ...
    @property
    def ProtocolInformation(self) -> Array[int]:
        """

        :return:
        """
    @ProtocolInformation.setter
    def ProtocolInformation(self, value: Array[int]) -> None: ...
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

class SocketInformationOptions(Enum):
    """"""

    NonBlocking: SocketInformationOptions = ...
    """"""
    Connected: SocketInformationOptions = ...
    """"""
    Listening: SocketInformationOptions = ...
    """"""
    UseOnlyOverlappedIO: SocketInformationOptions = ...
    """"""

class SocketOptionLevel(Enum):
    """"""

    IP: SocketOptionLevel = ...
    """"""
    Tcp: SocketOptionLevel = ...
    """"""
    Udp: SocketOptionLevel = ...
    """"""
    IPv6: SocketOptionLevel = ...
    """"""
    Socket: SocketOptionLevel = ...
    """"""

class SocketOptionName(Enum):
    """"""

    IPOptions: SocketOptionName = ...
    """"""
    Debug: SocketOptionName = ...
    """"""
    NoChecksum: SocketOptionName = ...
    """"""
    NoDelay: SocketOptionName = ...
    """"""
    HeaderIncluded: SocketOptionName = ...
    """"""
    AcceptConnection: SocketOptionName = ...
    """"""
    BsdUrgent: SocketOptionName = ...
    """"""
    Expedited: SocketOptionName = ...
    """"""
    TypeOfService: SocketOptionName = ...
    """"""
    ReuseAddress: SocketOptionName = ...
    """"""
    IpTimeToLive: SocketOptionName = ...
    """"""
    KeepAlive: SocketOptionName = ...
    """"""
    MulticastInterface: SocketOptionName = ...
    """"""
    MulticastTimeToLive: SocketOptionName = ...
    """"""
    MulticastLoopback: SocketOptionName = ...
    """"""
    AddMembership: SocketOptionName = ...
    """"""
    DropMembership: SocketOptionName = ...
    """"""
    DontFragment: SocketOptionName = ...
    """"""
    AddSourceMembership: SocketOptionName = ...
    """"""
    DropSourceMembership: SocketOptionName = ...
    """"""
    DontRoute: SocketOptionName = ...
    """"""
    BlockSource: SocketOptionName = ...
    """"""
    UnblockSource: SocketOptionName = ...
    """"""
    PacketInformation: SocketOptionName = ...
    """"""
    ChecksumCoverage: SocketOptionName = ...
    """"""
    HopLimit: SocketOptionName = ...
    """"""
    IPProtectionLevel: SocketOptionName = ...
    """"""
    IPv6Only: SocketOptionName = ...
    """"""
    Broadcast: SocketOptionName = ...
    """"""
    UseLoopback: SocketOptionName = ...
    """"""
    Linger: SocketOptionName = ...
    """"""
    OutOfBandInline: SocketOptionName = ...
    """"""
    SendBuffer: SocketOptionName = ...
    """"""
    ReceiveBuffer: SocketOptionName = ...
    """"""
    SendLowWater: SocketOptionName = ...
    """"""
    ReceiveLowWater: SocketOptionName = ...
    """"""
    SendTimeout: SocketOptionName = ...
    """"""
    ReceiveTimeout: SocketOptionName = ...
    """"""
    Error: SocketOptionName = ...
    """"""
    Type: SocketOptionName = ...
    """"""
    ReuseUnicastPort: SocketOptionName = ...
    """"""
    UpdateAcceptContext: SocketOptionName = ...
    """"""
    UpdateConnectContext: SocketOptionName = ...
    """"""
    MaxConnections: SocketOptionName = ...
    """"""
    DontLinger: SocketOptionName = ...
    """"""
    ExclusiveAddressUse: SocketOptionName = ...
    """"""

class SocketReceiveFromResult(ValueType):
    """"""

    ReceivedBytes: Final[int] = ...
    """
    
    :return: 
    """
    RemoteEndPoint: Final[EndPoint] = ...
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

class SocketReceiveMessageFromResult(ValueType):
    """"""

    PacketInformation: Final[IPPacketInformation] = ...
    """
    
    :return: 
    """
    ReceivedBytes: Final[int] = ...
    """
    
    :return: 
    """
    RemoteEndPoint: Final[EndPoint] = ...
    """
    
    :return: 
    """
    SocketFlags: Final[SocketFlags] = ...
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

class SocketShutdown(Enum):
    """"""

    Receive: SocketShutdown = ...
    """"""
    Send: SocketShutdown = ...
    """"""
    Both: SocketShutdown = ...
    """"""

class SocketTaskExtensions(ABC, Object):
    """"""

    @classmethod
    @overload
    def AcceptAsync(cls, socket: Socket) -> Task[Socket]:
        """

        :param socket:
        :return:
        """
    @classmethod
    @overload
    def AcceptAsync(cls, socket: Socket, acceptSocket: Socket) -> Task[Socket]:
        """

        :param socket:
        :param acceptSocket:
        :return:
        """
    @classmethod
    @overload
    def ConnectAsync(cls, socket: Socket, remoteEP: EndPoint) -> Task:
        """

        :param socket:
        :param remoteEP:
        :return:
        """
    @classmethod
    @overload
    def ConnectAsync(cls, socket: Socket, address: IPAddress, port: int) -> Task:
        """

        :param socket:
        :param address:
        :param port:
        :return:
        """
    @classmethod
    @overload
    def ConnectAsync(cls, socket: Socket, addresses: Array[IPAddress], port: int) -> Task:
        """

        :param socket:
        :param addresses:
        :param port:
        :return:
        """
    @classmethod
    @overload
    def ConnectAsync(cls, socket: Socket, host: str, port: int) -> Task:
        """

        :param socket:
        :param host:
        :param port:
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
    @classmethod
    @overload
    def ReceiveAsync(
        cls, socket: Socket, buffers: IList[ArraySegment[int]], socketFlags: SocketFlags
    ) -> Task[int]:
        """

        :param socket:
        :param buffers:
        :param socketFlags:
        :return:
        """
    @classmethod
    @overload
    def ReceiveAsync(
        cls, socket: Socket, buffer: ArraySegment[int], socketFlags: SocketFlags
    ) -> Task[int]:
        """

        :param socket:
        :param buffer:
        :param socketFlags:
        :return:
        """
    @classmethod
    def ReceiveFromAsync(
        cls,
        socket: Socket,
        buffer: ArraySegment[int],
        socketFlags: SocketFlags,
        remoteEndPoint: EndPoint,
    ) -> Task[SocketReceiveFromResult]:
        """

        :param socket:
        :param buffer:
        :param socketFlags:
        :param remoteEndPoint:
        :return:
        """
    @classmethod
    def ReceiveMessageFromAsync(
        cls,
        socket: Socket,
        buffer: ArraySegment[int],
        socketFlags: SocketFlags,
        remoteEndPoint: EndPoint,
    ) -> Task[SocketReceiveMessageFromResult]:
        """

        :param socket:
        :param buffer:
        :param socketFlags:
        :param remoteEndPoint:
        :return:
        """
    @classmethod
    @overload
    def SendAsync(
        cls, socket: Socket, buffers: IList[ArraySegment[int]], socketFlags: SocketFlags
    ) -> Task[int]:
        """

        :param socket:
        :param buffers:
        :param socketFlags:
        :return:
        """
    @classmethod
    @overload
    def SendAsync(
        cls, socket: Socket, buffer: ArraySegment[int], socketFlags: SocketFlags
    ) -> Task[int]:
        """

        :param socket:
        :param buffer:
        :param socketFlags:
        :return:
        """
    @classmethod
    def SendToAsync(
        cls, socket: Socket, buffer: ArraySegment[int], socketFlags: SocketFlags, remoteEP: EndPoint
    ) -> Task[int]:
        """

        :param socket:
        :param buffer:
        :param socketFlags:
        :param remoteEP:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SocketType(Enum):
    """"""

    Stream: SocketType = ...
    """"""
    Dgram: SocketType = ...
    """"""
    Raw: SocketType = ...
    """"""
    Rdm: SocketType = ...
    """"""
    Seqpacket: SocketType = ...
    """"""
    Unknown: SocketType = ...
    """"""

class TcpClient(Object, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, family: AddressFamily):
        """

        :param family:
        """
    @overload
    def __init__(self, localEP: IPEndPoint):
        """

        :param localEP:
        """
    @overload
    def __init__(self, hostname: str, port: int):
        """

        :param hostname:
        :param port:
        """
    @property
    def Available(self) -> int:
        """

        :return:
        """
    @property
    def Client(self) -> Socket:
        """

        :return:
        """
    @Client.setter
    def Client(self, value: Socket) -> None: ...
    @property
    def Connected(self) -> bool:
        """

        :return:
        """
    @property
    def ExclusiveAddressUse(self) -> bool:
        """

        :return:
        """
    @ExclusiveAddressUse.setter
    def ExclusiveAddressUse(self, value: bool) -> None: ...
    @property
    def LingerState(self) -> LingerOption:
        """

        :return:
        """
    @LingerState.setter
    def LingerState(self, value: LingerOption) -> None: ...
    @property
    def NoDelay(self) -> bool:
        """

        :return:
        """
    @NoDelay.setter
    def NoDelay(self, value: bool) -> None: ...
    @property
    def ReceiveBufferSize(self) -> int:
        """

        :return:
        """
    @ReceiveBufferSize.setter
    def ReceiveBufferSize(self, value: int) -> None: ...
    @property
    def ReceiveTimeout(self) -> int:
        """

        :return:
        """
    @ReceiveTimeout.setter
    def ReceiveTimeout(self, value: int) -> None: ...
    @property
    def SendBufferSize(self) -> int:
        """

        :return:
        """
    @SendBufferSize.setter
    def SendBufferSize(self, value: int) -> None: ...
    @property
    def SendTimeout(self) -> int:
        """

        :return:
        """
    @SendTimeout.setter
    def SendTimeout(self, value: int) -> None: ...
    @overload
    def BeginConnect(
        self, address: IPAddress, port: int, requestCallback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param address:
        :param port:
        :param requestCallback:
        :param state:
        :return:
        """
    @overload
    def BeginConnect(
        self, addresses: Array[IPAddress], port: int, requestCallback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param addresses:
        :param port:
        :param requestCallback:
        :param state:
        :return:
        """
    @overload
    def BeginConnect(
        self, host: str, port: int, requestCallback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param host:
        :param port:
        :param requestCallback:
        :param state:
        :return:
        """
    def Close(self) -> None:
        """"""
    @overload
    def Connect(self, remoteEP: IPEndPoint) -> None:
        """

        :param remoteEP:
        """
    @overload
    def Connect(self, address: IPAddress, port: int) -> None:
        """

        :param address:
        :param port:
        """
    @overload
    def Connect(self, ipAddresses: Array[IPAddress], port: int) -> None:
        """

        :param ipAddresses:
        :param port:
        """
    @overload
    def Connect(self, hostname: str, port: int) -> None:
        """

        :param hostname:
        :param port:
        """
    @overload
    def ConnectAsync(self, address: IPAddress, port: int) -> Task:
        """

        :param address:
        :param port:
        :return:
        """
    @overload
    def ConnectAsync(self, addresses: Array[IPAddress], port: int) -> Task:
        """

        :param addresses:
        :param port:
        :return:
        """
    @overload
    def ConnectAsync(self, host: str, port: int) -> Task:
        """

        :param host:
        :param port:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndConnect(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
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
    def GetStream(self) -> NetworkStream:
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

class TcpListener(Object):
    """"""

    @overload
    def __init__(self, localEP: IPEndPoint):
        """

        :param localEP:
        """
    @overload
    def __init__(self, port: int):
        """

        :param port:
        """
    @overload
    def __init__(self, localaddr: IPAddress, port: int):
        """

        :param localaddr:
        :param port:
        """
    @property
    def ExclusiveAddressUse(self) -> bool:
        """

        :return:
        """
    @ExclusiveAddressUse.setter
    def ExclusiveAddressUse(self, value: bool) -> None: ...
    @property
    def LocalEndpoint(self) -> EndPoint:
        """

        :return:
        """
    @property
    def Server(self) -> Socket:
        """

        :return:
        """
    def AcceptSocket(self) -> Socket:
        """

        :return:
        """
    def AcceptSocketAsync(self) -> Task[Socket]:
        """

        :return:
        """
    def AcceptTcpClient(self) -> TcpClient:
        """

        :return:
        """
    def AcceptTcpClientAsync(self) -> Task[TcpClient]:
        """

        :return:
        """
    def AllowNatTraversal(self, allowed: bool) -> None:
        """

        :param allowed:
        """
    def BeginAcceptSocket(self, callback: AsyncCallback, state: object) -> IAsyncResult:
        """

        :param callback:
        :param state:
        :return:
        """
    def BeginAcceptTcpClient(self, callback: AsyncCallback, state: object) -> IAsyncResult:
        """

        :param callback:
        :param state:
        :return:
        """
    @classmethod
    def Create(cls, port: int) -> TcpListener:
        """

        :param port:
        :return:
        """
    def EndAcceptSocket(self, asyncResult: IAsyncResult) -> Socket:
        """

        :param asyncResult:
        :return:
        """
    def EndAcceptTcpClient(self, asyncResult: IAsyncResult) -> TcpClient:
        """

        :param asyncResult:
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
    def Pending(self) -> bool:
        """

        :return:
        """
    @overload
    def Start(self) -> None:
        """"""
    @overload
    def Start(self, backlog: int) -> None:
        """

        :param backlog:
        """
    def Stop(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class TimeValue(ValueType):
    """"""

    Microseconds: Final[int] = ...
    """
    
    :return: 
    """
    Seconds: Final[int] = ...
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

class TransmitFileOptions(Enum):
    """"""

    UseDefaultWorkerThread: TransmitFileOptions = ...
    """"""
    Disconnect: TransmitFileOptions = ...
    """"""
    ReuseSocket: TransmitFileOptions = ...
    """"""
    WriteBehind: TransmitFileOptions = ...
    """"""
    UseSystemThread: TransmitFileOptions = ...
    """"""
    UseKernelApc: TransmitFileOptions = ...
    """"""

class TransmitFileOverlappedAsyncResult(BaseOverlappedAsyncResult, IAsyncResult):
    """"""

    @property
    def AsyncState(self) -> object:
        """

        :return:
        """
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """

        :return:
        """
    @property
    def CompletedSynchronously(self) -> bool:
        """

        :return:
        """
    @property
    def IsCompleted(self) -> bool:
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

TransmitPacketsDelegate: Callable[
    [SafeCloseSocket, IntPtr, int, int, SafeNativeOverlapped, TransmitFileOptions], bool
] = ...
"""

:param socketHandle: 
:param packetArray: 
:param elementCount: 
:param sendSize: 
:param overlapped: 
:param flags: 
:return: 
"""

class UdpClient(Object, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, family: AddressFamily):
        """

        :param family:
        """
    @overload
    def __init__(self, localEP: IPEndPoint):
        """

        :param localEP:
        """
    @overload
    def __init__(self, port: int):
        """

        :param port:
        """
    @overload
    def __init__(self, port: int, family: AddressFamily):
        """

        :param port:
        :param family:
        """
    @overload
    def __init__(self, hostname: str, port: int):
        """

        :param hostname:
        :param port:
        """
    @property
    def Available(self) -> int:
        """

        :return:
        """
    @property
    def Client(self) -> Socket:
        """

        :return:
        """
    @Client.setter
    def Client(self, value: Socket) -> None: ...
    @property
    def DontFragment(self) -> bool:
        """

        :return:
        """
    @DontFragment.setter
    def DontFragment(self, value: bool) -> None: ...
    @property
    def EnableBroadcast(self) -> bool:
        """

        :return:
        """
    @EnableBroadcast.setter
    def EnableBroadcast(self, value: bool) -> None: ...
    @property
    def ExclusiveAddressUse(self) -> bool:
        """

        :return:
        """
    @ExclusiveAddressUse.setter
    def ExclusiveAddressUse(self, value: bool) -> None: ...
    @property
    def MulticastLoopback(self) -> bool:
        """

        :return:
        """
    @MulticastLoopback.setter
    def MulticastLoopback(self, value: bool) -> None: ...
    @property
    def Ttl(self) -> int:
        """

        :return:
        """
    @Ttl.setter
    def Ttl(self, value: int) -> None: ...
    def AllowNatTraversal(self, allowed: bool) -> None:
        """

        :param allowed:
        """
    def BeginReceive(self, requestCallback: AsyncCallback, state: object) -> IAsyncResult:
        """

        :param requestCallback:
        :param state:
        :return:
        """
    @overload
    def BeginSend(
        self, datagram: Array[int], bytes: int, requestCallback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param datagram:
        :param bytes:
        :param requestCallback:
        :param state:
        :return:
        """
    @overload
    def BeginSend(
        self,
        datagram: Array[int],
        bytes: int,
        endPoint: IPEndPoint,
        requestCallback: AsyncCallback,
        state: object,
    ) -> IAsyncResult:
        """

        :param datagram:
        :param bytes:
        :param endPoint:
        :param requestCallback:
        :param state:
        :return:
        """
    @overload
    def BeginSend(
        self,
        datagram: Array[int],
        bytes: int,
        hostname: str,
        port: int,
        requestCallback: AsyncCallback,
        state: object,
    ) -> IAsyncResult:
        """

        :param datagram:
        :param bytes:
        :param hostname:
        :param port:
        :param requestCallback:
        :param state:
        :return:
        """
    def Close(self) -> None:
        """"""
    @overload
    def Connect(self, endPoint: IPEndPoint) -> None:
        """

        :param endPoint:
        """
    @overload
    def Connect(self, addr: IPAddress, port: int) -> None:
        """

        :param addr:
        :param port:
        """
    @overload
    def Connect(self, hostname: str, port: int) -> None:
        """

        :param hostname:
        :param port:
        """
    def Dispose(self) -> None:
        """"""
    @overload
    def DropMulticastGroup(self, multicastAddr: IPAddress) -> None:
        """

        :param multicastAddr:
        """
    @overload
    def DropMulticastGroup(self, multicastAddr: IPAddress, ifindex: int) -> None:
        """

        :param multicastAddr:
        :param ifindex:
        """
    def EndReceive(self, asyncResult: IAsyncResult, remoteEP: IPEndPoint) -> Array[int]:
        """

        :param asyncResult:
        :param remoteEP:
        :return:
        """
    def EndSend(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
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
    @overload
    def JoinMulticastGroup(self, multicastAddr: IPAddress) -> None:
        """

        :param multicastAddr:
        """
    @overload
    def JoinMulticastGroup(self, multicastAddr: IPAddress, localAddress: IPAddress) -> None:
        """

        :param multicastAddr:
        :param localAddress:
        """
    @overload
    def JoinMulticastGroup(self, multicastAddr: IPAddress, timeToLive: int) -> None:
        """

        :param multicastAddr:
        :param timeToLive:
        """
    @overload
    def JoinMulticastGroup(self, ifindex: int, multicastAddr: IPAddress) -> None:
        """

        :param ifindex:
        :param multicastAddr:
        """
    def Receive(self, remoteEP: IPEndPoint) -> Array[int]:
        """

        :param remoteEP:
        :return:
        """
    def ReceiveAsync(self) -> Task[UdpReceiveResult]:
        """

        :return:
        """
    @overload
    def Send(self, dgram: Array[int], bytes: int) -> int:
        """

        :param dgram:
        :param bytes:
        :return:
        """
    @overload
    def Send(self, dgram: Array[int], bytes: int, endPoint: IPEndPoint) -> int:
        """

        :param dgram:
        :param bytes:
        :param endPoint:
        :return:
        """
    @overload
    def Send(self, dgram: Array[int], bytes: int, hostname: str, port: int) -> int:
        """

        :param dgram:
        :param bytes:
        :param hostname:
        :param port:
        :return:
        """
    @overload
    def SendAsync(self, datagram: Array[int], bytes: int) -> Task[int]:
        """

        :param datagram:
        :param bytes:
        :return:
        """
    @overload
    def SendAsync(self, datagram: Array[int], bytes: int, endPoint: IPEndPoint) -> Task[int]:
        """

        :param datagram:
        :param bytes:
        :param endPoint:
        :return:
        """
    @overload
    def SendAsync(self, datagram: Array[int], bytes: int, hostname: str, port: int) -> Task[int]:
        """

        :param datagram:
        :param bytes:
        :param hostname:
        :param port:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class UdpReceiveResult(ValueType, IEquatable[UdpReceiveResult]):
    """"""

    def __init__(self, buffer: Array[int], remoteEndPoint: IPEndPoint):
        """

        :param buffer:
        :param remoteEndPoint:
        """
    @property
    def Buffer(self) -> Array[int]:
        """

        :return:
        """
    @property
    def RemoteEndPoint(self) -> IPEndPoint:
        """

        :return:
        """
    @overload
    def Equals(self, other: UdpReceiveResult) -> bool:
        """

        :param other:
        :return:
        """
    @overload
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
    def __eq__(self, other: UdpReceiveResult) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: UdpReceiveResult) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: UdpReceiveResult, right: UdpReceiveResult) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: UdpReceiveResult, right: UdpReceiveResult) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

WSARecvMsgDelegate: Callable[[SafeCloseSocket, IntPtr, int, SafeHandle, IntPtr], SocketError] = ...
"""

:param socketHandle: 
:param msg: 
:param bytesTransferred: 
:param overlapped: 
:param completionRoutine: 
:return: 
"""
WSARecvMsgDelegate_Blocking: Callable[[IntPtr, IntPtr, int, IntPtr, IntPtr], SocketError] = ...
"""

:param socketHandle: 
:param msg: 
:param bytesTransferred: 
:param overlapped: 
:param completionRoutine: 
:return: 
"""
