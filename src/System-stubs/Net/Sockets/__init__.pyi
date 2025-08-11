"""Automatically generated stubs for C# namespace: System.Net.Sockets."""

from abc import ABC
from collections.abc import Callable
from typing import ClassVar
from typing import Final
from typing import Self
from typing import overload

from System import Array
from System import ArraySegment
from System import AsyncCallback
from System import Byte
from System import Enum
from System import EventArgs
from System import EventHandler
from System import Exception
from System import IAsyncResult
from System import IDisposable
from System import IEquatable
from System import Int32
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

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AcceptAsyncResult(ContextAwareResult, IAsyncResult):
    """"""
    @property
    def AsyncState(self) -> object:
        """"""
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """"""
    @property
    def CompletedSynchronously(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type AcceptExDelegate = Callable[
    [SafeCloseSocket, SafeCloseSocket, IntPtr, int, int, int, Int32, SafeHandle], bool
]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AcceptOverlappedAsyncResult(BaseOverlappedAsyncResult, IAsyncResult):
    """"""
    @property
    def AsyncState(self) -> object:
        """"""
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """"""
    @property
    def CompletedSynchronously(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class BaseOverlappedAsyncResult(ContextAwareResult, IAsyncResult):
    """"""
    @property
    def AsyncState(self) -> object:
        """"""
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """"""
    @property
    def CompletedSynchronously(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ConnectAsyncResult(ContextAwareResult, IAsyncResult):
    """"""
    @property
    def AsyncState(self) -> object:
        """"""
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """"""
    @property
    def CompletedSynchronously(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type ConnectExDelegate = Callable[
    [SafeCloseSocket, IntPtr, int, IntPtr, int, Int32, SafeHandle], bool
]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ConnectOverlappedAsyncResult(BaseOverlappedAsyncResult, IAsyncResult):
    """"""
    @property
    def AsyncState(self) -> object:
        """"""
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """"""
    @property
    def CompletedSynchronously(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type DisconnectExDelegate = Callable[[SafeCloseSocket, SafeHandle, int, int], bool]
""""""
type DisconnectExDelegate_Blocking = Callable[[IntPtr, IntPtr, int, int], bool]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DisconnectOverlappedAsyncResult(BaseOverlappedAsyncResult, IAsyncResult):
    """"""
    @property
    def AsyncState(self) -> object:
        """"""
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """"""
    @property
    def CompletedSynchronously(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DynamicWinsockMethods(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetDelegate[T](self, socketHandle: SafeCloseSocket) -> T:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetMethods(
        cls, addressFamily: AddressFamily, socketType: SocketType, protocolType: ProtocolType
    ) -> DynamicWinsockMethods:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type GetAcceptExSockaddrsDelegate = Callable[
    [IntPtr, int, int, int, IntPtr, Int32, IntPtr, Int32], None
]
""""""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IPPacketInformation(ValueType):
    """"""
    @property
    def Address(self) -> IPAddress:
        """"""
    @property
    def Interface(self) -> int:
        """"""
    def Equals(self, comparand: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(
        cls, packetInformation1: IPPacketInformation, packetInformation2: IPPacketInformation
    ) -> bool:
        """"""
    @classmethod
    def op_Inequality(
        cls, packetInformation1: IPPacketInformation, packetInformation2: IPPacketInformation
    ) -> bool:
        """"""
    def __eq__(self, other: IPPacketInformation) -> bool:
        """"""
    def __ne__(self, other: IPPacketInformation) -> bool:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IPv6MulticastOption(Object):
    """"""
    @overload
    def __init__(self, group: IPAddress, ifindex: int) -> None:
        """"""
    @overload
    def __init__(self, group: IPAddress) -> None:
        """"""
    @property
    def Group(self) -> IPAddress:
        """"""
    @Group.setter
    def Group(self, value: IPAddress) -> None: ...
    @property
    def InterfaceIndex(self) -> int:
        """"""
    @InterfaceIndex.setter
    def InterfaceIndex(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IoctlSocketConstants(ABC, Object):
    """"""

    FIOASYNC: ClassVar[int]
    """"""
    FIONBIO: ClassVar[int]
    """"""
    FIONREAD: ClassVar[int]
    """"""
    SIOGETEXTENSIONFUNCTIONPOINTER: ClassVar[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class LingerOption(Object):
    """"""
    def __init__(self, enable: bool, seconds: int) -> None:
        """"""
    @property
    def Enabled(self) -> bool:
        """"""
    @Enabled.setter
    def Enabled(self, value: bool) -> None: ...
    @property
    def LingerTime(self) -> int:
        """"""
    @LingerTime.setter
    def LingerTime(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MulticastOption(Object):
    """"""
    @overload
    def __init__(self, group: IPAddress, mcint: IPAddress) -> None:
        """"""
    @overload
    def __init__(self, group: IPAddress, interfaceIndex: int) -> None:
        """"""
    @overload
    def __init__(self, group: IPAddress) -> None:
        """"""
    @property
    def Group(self) -> IPAddress:
        """"""
    @Group.setter
    def Group(self, value: IPAddress) -> None: ...
    @property
    def InterfaceIndex(self) -> int:
        """"""
    @InterfaceIndex.setter
    def InterfaceIndex(self, value: int) -> None: ...
    @property
    def LocalAddress(self) -> IPAddress:
        """"""
    @LocalAddress.setter
    def LocalAddress(self, value: IPAddress) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MultipleConnectAsync(ABC, Object):
    """"""
    def Cancel(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def StartConnectAsync(self, args: SocketAsyncEventArgs, endPoint: DnsEndPoint) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MultipleSocketMultipleConnectAsync(MultipleConnectAsync):
    """"""
    def __init__(self, socketType: SocketType, protocolType: ProtocolType) -> None:
        """"""
    def Cancel(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def StartConnectAsync(self, args: SocketAsyncEventArgs, endPoint: DnsEndPoint) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class NetworkEvents(ValueType):
    """"""

    ErrorCodes: Final[Array[int]]
    """"""
    Events: Final[AsyncEventBits]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class NetworkStream(Stream, IDisposable):
    """"""
    @overload
    def __init__(self, socket: Socket) -> None:
        """"""
    @overload
    def __init__(self, socket: Socket, ownsSocket: bool) -> None:
        """"""
    @overload
    def __init__(self, socket: Socket, access: FileAccess) -> None:
        """"""
    @overload
    def __init__(self, socket: Socket, access: FileAccess, ownsSocket: bool) -> None:
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
    def DataAvailable(self) -> bool:
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
        self, buffer: Array[int], offset: int, size: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self, buffer: Array[int], offset: int, size: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    @overload
    def Close(self) -> None:
        """"""
    @overload
    def Close(self, timeout: int) -> None:
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
    def Read(self, buffer: Array[int], offset: int, size: int) -> tuple[int, Array[int]]:
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
    def Write(self, buffer: Array[int], offset: int, size: int) -> None:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class OverlappedAsyncResult(BaseOverlappedAsyncResult, IAsyncResult):
    """"""
    @property
    def AsyncState(self) -> object:
        """"""
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """"""
    @property
    def CompletedSynchronously(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class OverlappedCache(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ReceiveFromOverlappedAsyncResult(OverlappedAsyncResult, IAsyncResult):
    """"""
    @property
    def AsyncState(self) -> object:
        """"""
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """"""
    @property
    def CompletedSynchronously(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ReceiveMessageOverlappedAsyncResult(BaseOverlappedAsyncResult, IAsyncResult):
    """"""
    @property
    def AsyncState(self) -> object:
        """"""
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """"""
    @property
    def CompletedSynchronously(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class SelectMode(Enum):
    """"""

    SelectRead: SelectMode = ...
    """"""
    SelectWrite: SelectMode = ...
    """"""
    SelectError: SelectMode = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SendPacketsElement(Object):
    """"""
    @overload
    def __init__(self, filepath: str) -> None:
        """"""
    @overload
    def __init__(self, filepath: str, offset: int, count: int) -> None:
        """"""
    @overload
    def __init__(self, filepath: str, offset: int, count: int, endOfPacket: bool) -> None:
        """"""
    @overload
    def __init__(self, buffer: Array[int]) -> None:
        """"""
    @overload
    def __init__(self, buffer: Array[int], offset: int, count: int) -> None:
        """"""
    @overload
    def __init__(self, buffer: Array[int], offset: int, count: int, endOfPacket: bool) -> None:
        """"""
    @property
    def Buffer(self) -> Array[int]:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def EndOfPacket(self) -> bool:
        """"""
    @property
    def FilePath(self) -> str:
        """"""
    @property
    def Offset(self) -> int:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SingleSocketMultipleConnectAsync(MultipleConnectAsync):
    """"""
    def __init__(self, socket: Socket, userSocket: bool) -> None:
        """"""
    def Cancel(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def StartConnectAsync(self, args: SocketAsyncEventArgs, endPoint: DnsEndPoint) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Socket(Object, IDisposable):
    """"""
    @overload
    def __init__(self, socketType: SocketType, protocolType: ProtocolType) -> None:
        """"""
    @overload
    def __init__(
        self, addressFamily: AddressFamily, socketType: SocketType, protocolType: ProtocolType
    ) -> None:
        """"""
    @overload
    def __init__(self, socketInformation: SocketInformation) -> None:
        """"""
    @property
    def AddressFamily(self) -> AddressFamily:
        """"""
    @property
    def Available(self) -> int:
        """"""
    @property
    def Blocking(self) -> bool:
        """"""
    @Blocking.setter
    def Blocking(self, value: bool) -> None: ...
    @property
    def Connected(self) -> bool:
        """"""
    @property
    def DontFragment(self) -> bool:
        """"""
    @DontFragment.setter
    def DontFragment(self, value: bool) -> None: ...
    @property
    def DualMode(self) -> bool:
        """"""
    @DualMode.setter
    def DualMode(self, value: bool) -> None: ...
    @property
    def EnableBroadcast(self) -> bool:
        """"""
    @EnableBroadcast.setter
    def EnableBroadcast(self, value: bool) -> None: ...
    @property
    def ExclusiveAddressUse(self) -> bool:
        """"""
    @ExclusiveAddressUse.setter
    def ExclusiveAddressUse(self, value: bool) -> None: ...
    @property
    def Handle(self) -> IntPtr:
        """"""
    @property
    def IsBound(self) -> bool:
        """"""
    @property
    def LingerState(self) -> LingerOption:
        """"""
    @LingerState.setter
    def LingerState(self, value: LingerOption) -> None: ...
    @property
    def LocalEndPoint(self) -> EndPoint:
        """"""
    @property
    def MulticastLoopback(self) -> bool:
        """"""
    @MulticastLoopback.setter
    def MulticastLoopback(self, value: bool) -> None: ...
    @property
    def NoDelay(self) -> bool:
        """"""
    @NoDelay.setter
    def NoDelay(self, value: bool) -> None: ...
    @classmethod
    @property
    def OSSupportsIPv4(cls) -> bool:
        """"""
    @classmethod
    @property
    def OSSupportsIPv6(cls) -> bool:
        """"""
    @property
    def ProtocolType(self) -> ProtocolType:
        """"""
    @property
    def ReceiveBufferSize(self) -> int:
        """"""
    @ReceiveBufferSize.setter
    def ReceiveBufferSize(self, value: int) -> None: ...
    @property
    def ReceiveTimeout(self) -> int:
        """"""
    @ReceiveTimeout.setter
    def ReceiveTimeout(self, value: int) -> None: ...
    @property
    def RemoteEndPoint(self) -> EndPoint:
        """"""
    @property
    def SendBufferSize(self) -> int:
        """"""
    @SendBufferSize.setter
    def SendBufferSize(self, value: int) -> None: ...
    @property
    def SendTimeout(self) -> int:
        """"""
    @SendTimeout.setter
    def SendTimeout(self, value: int) -> None: ...
    @property
    def SocketType(self) -> SocketType:
        """"""
    @classmethod
    @property
    def SupportsIPv4(cls) -> bool:
        """"""
    @classmethod
    @property
    def SupportsIPv6(cls) -> bool:
        """"""
    @property
    def Ttl(self) -> int:
        """"""
    @Ttl.setter
    def Ttl(self, value: int) -> None: ...
    @property
    def UseOnlyOverlappedIO(self) -> bool:
        """"""
    @UseOnlyOverlappedIO.setter
    def UseOnlyOverlappedIO(self, value: bool) -> None: ...
    def Accept(self) -> Socket:
        """"""
    def AcceptAsync(self, e: SocketAsyncEventArgs) -> bool:
        """"""
    @overload
    def BeginAccept(
        self, acceptSocket: Socket, receiveSize: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    @overload
    def BeginAccept(self, callback: AsyncCallback, state: object) -> IAsyncResult:
        """"""
    @overload
    def BeginAccept(self, receiveSize: int, callback: AsyncCallback, state: object) -> IAsyncResult:
        """"""
    @overload
    def BeginConnect(
        self, remoteEP: EndPoint, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    @overload
    def BeginConnect(
        self, address: IPAddress, port: int, requestCallback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    @overload
    def BeginConnect(
        self, addresses: Array[IPAddress], port: int, requestCallback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    @overload
    def BeginConnect(
        self, host: str, port: int, requestCallback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginDisconnect(
        self, reuseSocket: bool, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    @overload
    def BeginReceive(
        self,
        buffers: IList[ArraySegment[int]],
        socketFlags: SocketFlags,
        errorCode: SocketError,
        callback: AsyncCallback,
        state: object,
    ) -> tuple[IAsyncResult, SocketError]:
        """"""
    @overload
    def BeginReceive(
        self,
        buffers: IList[ArraySegment[int]],
        socketFlags: SocketFlags,
        callback: AsyncCallback,
        state: object,
    ) -> IAsyncResult:
        """"""
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
    ) -> tuple[IAsyncResult, SocketError]:
        """"""
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
        """"""
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
        """"""
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
        """"""
    @overload
    def BeginSend(
        self,
        buffers: IList[ArraySegment[int]],
        socketFlags: SocketFlags,
        errorCode: SocketError,
        callback: AsyncCallback,
        state: object,
    ) -> tuple[IAsyncResult, SocketError]:
        """"""
    @overload
    def BeginSend(
        self,
        buffers: IList[ArraySegment[int]],
        socketFlags: SocketFlags,
        callback: AsyncCallback,
        state: object,
    ) -> IAsyncResult:
        """"""
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
    ) -> tuple[IAsyncResult, SocketError]:
        """"""
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
        """"""
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
        """"""
    @overload
    def BeginSendFile(self, fileName: str, callback: AsyncCallback, state: object) -> IAsyncResult:
        """"""
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
        """"""
    def Bind(self, localEP: EndPoint) -> None:
        """"""
    @classmethod
    def CancelConnectAsync(cls, e: SocketAsyncEventArgs) -> None:
        """"""
    @overload
    def Close(self) -> None:
        """"""
    @overload
    def Close(self, timeout: int) -> None:
        """"""
    @overload
    def Connect(self, remoteEP: EndPoint) -> None:
        """"""
    @overload
    def Connect(self, address: IPAddress, port: int) -> None:
        """"""
    @overload
    def Connect(self, addresses: Array[IPAddress], port: int) -> None:
        """"""
    @overload
    def Connect(self, host: str, port: int) -> None:
        """"""
    @overload
    def ConnectAsync(self, e: SocketAsyncEventArgs) -> bool:
        """"""
    @classmethod
    @overload
    def ConnectAsync(
        cls, socketType: SocketType, protocolType: ProtocolType, e: SocketAsyncEventArgs
    ) -> bool:
        """"""
    def Disconnect(self, reuseSocket: bool) -> None:
        """"""
    def DisconnectAsync(self, e: SocketAsyncEventArgs) -> bool:
        """"""
    def Dispose(self) -> None:
        """"""
    def DuplicateAndClose(self, targetProcessId: int) -> SocketInformation:
        """"""
    @overload
    def EndAccept(
        self, buffer: Byte, bytesTransferred: Int32, asyncResult: IAsyncResult
    ) -> tuple[Socket, Byte, Int32]:
        """"""
    @overload
    def EndAccept(self, buffer: Byte, asyncResult: IAsyncResult) -> tuple[Socket, Byte]:
        """"""
    @overload
    def EndAccept(self, asyncResult: IAsyncResult) -> Socket:
        """"""
    def EndConnect(self, asyncResult: IAsyncResult) -> None:
        """"""
    def EndDisconnect(self, asyncResult: IAsyncResult) -> None:
        """"""
    @overload
    def EndReceive(self, asyncResult: IAsyncResult) -> int:
        """"""
    @overload
    def EndReceive(
        self, asyncResult: IAsyncResult, errorCode: SocketError
    ) -> tuple[int, SocketError]:
        """"""
    def EndReceiveFrom(self, asyncResult: IAsyncResult, endPoint: EndPoint) -> int:
        """"""
    def EndReceiveMessageFrom(
        self,
        asyncResult: IAsyncResult,
        socketFlags: SocketFlags,
        endPoint: EndPoint,
        ipPacketInformation: IPPacketInformation,
    ) -> tuple[int, IPPacketInformation]:
        """"""
    @overload
    def EndSend(self, asyncResult: IAsyncResult) -> int:
        """"""
    @overload
    def EndSend(self, asyncResult: IAsyncResult, errorCode: SocketError) -> tuple[int, SocketError]:
        """"""
    def EndSendFile(self, asyncResult: IAsyncResult) -> None:
        """"""
    def EndSendTo(self, asyncResult: IAsyncResult) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetSocketOption(
        self, optionLevel: SocketOptionLevel, optionName: SocketOptionName
    ) -> object:
        """"""
    @overload
    def GetSocketOption(
        self, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: Array[int]
    ) -> None:
        """"""
    @overload
    def GetSocketOption(
        self, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionLength: int
    ) -> Array[int]:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IOControl(
        self, ioControlCode: IOControlCode, optionInValue: Array[int], optionOutValue: Array[int]
    ) -> int:
        """"""
    @overload
    def IOControl(
        self, ioControlCode: int, optionInValue: Array[int], optionOutValue: Array[int]
    ) -> int:
        """"""
    def Listen(self, backlog: int) -> None:
        """"""
    def Poll(self, microSeconds: int, mode: SelectMode) -> bool:
        """"""
    @overload
    def Receive(self, buffers: IList[ArraySegment[int]]) -> int:
        """"""
    @overload
    def Receive(self, buffers: IList[ArraySegment[int]], socketFlags: SocketFlags) -> int:
        """"""
    @overload
    def Receive(
        self, buffers: IList[ArraySegment[int]], socketFlags: SocketFlags, errorCode: SocketError
    ) -> tuple[int, SocketError]:
        """"""
    @overload
    def Receive(self, buffer: Array[int]) -> int:
        """"""
    @overload
    def Receive(self, buffer: Array[int], socketFlags: SocketFlags) -> int:
        """"""
    @overload
    def Receive(self, buffer: Array[int], size: int, socketFlags: SocketFlags) -> int:
        """"""
    @overload
    def Receive(self, buffer: Array[int], offset: int, size: int, socketFlags: SocketFlags) -> int:
        """"""
    @overload
    def Receive(
        self,
        buffer: Array[int],
        offset: int,
        size: int,
        socketFlags: SocketFlags,
        errorCode: SocketError,
    ) -> tuple[int, SocketError]:
        """"""
    def ReceiveAsync(self, e: SocketAsyncEventArgs) -> bool:
        """"""
    @overload
    def ReceiveFrom(self, buffer: Array[int], socketFlags: SocketFlags, remoteEP: EndPoint) -> int:
        """"""
    @overload
    def ReceiveFrom(self, buffer: Array[int], remoteEP: EndPoint) -> int:
        """"""
    @overload
    def ReceiveFrom(
        self, buffer: Array[int], size: int, socketFlags: SocketFlags, remoteEP: EndPoint
    ) -> int:
        """"""
    @overload
    def ReceiveFrom(
        self,
        buffer: Array[int],
        offset: int,
        size: int,
        socketFlags: SocketFlags,
        remoteEP: EndPoint,
    ) -> int:
        """"""
    def ReceiveFromAsync(self, e: SocketAsyncEventArgs) -> bool:
        """"""
    def ReceiveMessageFrom(
        self,
        buffer: Array[int],
        offset: int,
        size: int,
        socketFlags: SocketFlags,
        remoteEP: EndPoint,
        ipPacketInformation: IPPacketInformation,
    ) -> tuple[int, IPPacketInformation]:
        """"""
    def ReceiveMessageFromAsync(self, e: SocketAsyncEventArgs) -> bool:
        """"""
    @classmethod
    def Select(
        cls, checkRead: IList, checkWrite: IList, checkError: IList, microSeconds: int
    ) -> None:
        """"""
    @overload
    def Send(self, buffers: IList[ArraySegment[int]]) -> int:
        """"""
    @overload
    def Send(self, buffers: IList[ArraySegment[int]], socketFlags: SocketFlags) -> int:
        """"""
    @overload
    def Send(
        self, buffers: IList[ArraySegment[int]], socketFlags: SocketFlags, errorCode: SocketError
    ) -> tuple[int, SocketError]:
        """"""
    @overload
    def Send(self, buffer: Array[int]) -> int:
        """"""
    @overload
    def Send(self, buffer: Array[int], socketFlags: SocketFlags) -> int:
        """"""
    @overload
    def Send(self, buffer: Array[int], size: int, socketFlags: SocketFlags) -> int:
        """"""
    @overload
    def Send(self, buffer: Array[int], offset: int, size: int, socketFlags: SocketFlags) -> int:
        """"""
    @overload
    def Send(
        self,
        buffer: Array[int],
        offset: int,
        size: int,
        socketFlags: SocketFlags,
        errorCode: SocketError,
    ) -> tuple[int, SocketError]:
        """"""
    def SendAsync(self, e: SocketAsyncEventArgs) -> bool:
        """"""
    @overload
    def SendFile(self, fileName: str) -> None:
        """"""
    @overload
    def SendFile(
        self,
        fileName: str,
        preBuffer: Array[int],
        postBuffer: Array[int],
        flags: TransmitFileOptions,
    ) -> None:
        """"""
    def SendPacketsAsync(self, e: SocketAsyncEventArgs) -> bool:
        """"""
    @overload
    def SendTo(self, buffer: Array[int], socketFlags: SocketFlags, remoteEP: EndPoint) -> int:
        """"""
    @overload
    def SendTo(self, buffer: Array[int], remoteEP: EndPoint) -> int:
        """"""
    @overload
    def SendTo(
        self, buffer: Array[int], size: int, socketFlags: SocketFlags, remoteEP: EndPoint
    ) -> int:
        """"""
    @overload
    def SendTo(
        self,
        buffer: Array[int],
        offset: int,
        size: int,
        socketFlags: SocketFlags,
        remoteEP: EndPoint,
    ) -> int:
        """"""
    def SendToAsync(self, e: SocketAsyncEventArgs) -> bool:
        """"""
    def SetIPProtectionLevel(self, level: IPProtectionLevel) -> None:
        """"""
    @overload
    def SetSocketOption(
        self, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: Array[int]
    ) -> None:
        """"""
    @overload
    def SetSocketOption(
        self, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: bool
    ) -> None:
        """"""
    @overload
    def SetSocketOption(
        self, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: int
    ) -> None:
        """"""
    @overload
    def SetSocketOption(
        self, optionLevel: SocketOptionLevel, optionName: SocketOptionName, optionValue: object
    ) -> None:
        """"""
    def Shutdown(self, how: SocketShutdown) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SocketAsyncEventArgs(EventArgs, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def AcceptSocket(self) -> Socket:
        """"""
    @AcceptSocket.setter
    def AcceptSocket(self, value: Socket) -> None: ...
    @property
    def Buffer(self) -> Array[int]:
        """"""
    @property
    def BufferList(self) -> IList[ArraySegment[int]]:
        """"""
    @BufferList.setter
    def BufferList(self, value: IList[ArraySegment[int]]) -> None: ...
    @property
    def BytesTransferred(self) -> int:
        """"""
    @property
    def ConnectByNameError(self) -> Exception:
        """"""
    @property
    def ConnectSocket(self) -> Socket:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def DisconnectReuseSocket(self) -> bool:
        """"""
    @DisconnectReuseSocket.setter
    def DisconnectReuseSocket(self, value: bool) -> None: ...
    @property
    def LastOperation(self) -> SocketAsyncOperation:
        """"""
    @property
    def Offset(self) -> int:
        """"""
    @property
    def ReceiveMessageFromPacketInfo(self) -> IPPacketInformation:
        """"""
    @property
    def RemoteEndPoint(self) -> EndPoint:
        """"""
    @RemoteEndPoint.setter
    def RemoteEndPoint(self, value: EndPoint) -> None: ...
    @property
    def SendPacketsElements(self) -> Array[SendPacketsElement]:
        """"""
    @SendPacketsElements.setter
    def SendPacketsElements(self, value: Array[SendPacketsElement]) -> None: ...
    @property
    def SendPacketsFlags(self) -> TransmitFileOptions:
        """"""
    @SendPacketsFlags.setter
    def SendPacketsFlags(self, value: TransmitFileOptions) -> None: ...
    @property
    def SendPacketsSendSize(self) -> int:
        """"""
    @SendPacketsSendSize.setter
    def SendPacketsSendSize(self, value: int) -> None: ...
    @property
    def SocketClientAccessPolicyProtocol(self) -> SocketClientAccessPolicyProtocol:
        """"""
    @SocketClientAccessPolicyProtocol.setter
    def SocketClientAccessPolicyProtocol(self, value: SocketClientAccessPolicyProtocol) -> None: ...
    @property
    def SocketError(self) -> SocketError:
        """"""
    @SocketError.setter
    def SocketError(self, value: SocketError) -> None: ...
    @property
    def SocketFlags(self) -> SocketFlags:
        """"""
    @SocketFlags.setter
    def SocketFlags(self, value: SocketFlags) -> None: ...
    @property
    def UserToken(self) -> object:
        """"""
    @UserToken.setter
    def UserToken(self, value: object) -> None: ...
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def SetBuffer(self, buffer: Array[int], offset: int, count: int) -> None:
        """"""
    @overload
    def SetBuffer(self, offset: int, count: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __len__(self) -> int:
        """"""
    Completed: EventType[EventHandler[SocketAsyncEventArgs]] = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class SocketClientAccessPolicyProtocol(Enum):
    """"""

    Tcp: SocketClientAccessPolicyProtocol = ...
    """"""
    Http: SocketClientAccessPolicyProtocol = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SocketException(Win32Exception, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, errorCode: int) -> None:
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
    def SocketErrorCode(self) -> SocketError:
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SocketInformation(ValueType):
    """"""
    @property
    def Options(self) -> SocketInformationOptions:
        """"""
    @Options.setter
    def Options(self, value: SocketInformationOptions) -> None: ...
    @property
    def ProtocolInformation(self) -> Array[int]:
        """"""
    @ProtocolInformation.setter
    def ProtocolInformation(self, value: Array[int]) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SocketReceiveFromResult(ValueType):
    """"""

    ReceivedBytes: Final[int]
    """"""
    RemoteEndPoint: Final[EndPoint]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SocketReceiveMessageFromResult(ValueType):
    """"""

    PacketInformation: Final[IPPacketInformation]
    """"""
    ReceivedBytes: Final[int]
    """"""
    RemoteEndPoint: Final[EndPoint]
    """"""
    SocketFlags: Final[SocketFlags]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class SocketShutdown(Enum):
    """"""

    Receive: SocketShutdown = ...
    """"""
    Send: SocketShutdown = ...
    """"""
    Both: SocketShutdown = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SocketTaskExtensions(ABC, Object):
    """"""
    @classmethod
    @overload
    def AcceptAsync(cls, socket: Socket) -> Task[Socket]:
        """"""
    @classmethod
    @overload
    def AcceptAsync(cls, socket: Socket, acceptSocket: Socket) -> Task[Socket]:
        """"""
    @classmethod
    @overload
    def ConnectAsync(cls, socket: Socket, remoteEP: EndPoint) -> Task:
        """"""
    @classmethod
    @overload
    def ConnectAsync(cls, socket: Socket, address: IPAddress, port: int) -> Task:
        """"""
    @classmethod
    @overload
    def ConnectAsync(cls, socket: Socket, addresses: Array[IPAddress], port: int) -> Task:
        """"""
    @classmethod
    @overload
    def ConnectAsync(cls, socket: Socket, host: str, port: int) -> Task:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def ReceiveAsync(
        cls, socket: Socket, buffers: IList[ArraySegment[int]], socketFlags: SocketFlags
    ) -> Task[int]:
        """"""
    @classmethod
    @overload
    def ReceiveAsync(
        cls, socket: Socket, buffer: ArraySegment[int], socketFlags: SocketFlags
    ) -> Task[int]:
        """"""
    @classmethod
    def ReceiveFromAsync(
        cls,
        socket: Socket,
        buffer: ArraySegment[int],
        socketFlags: SocketFlags,
        remoteEndPoint: EndPoint,
    ) -> Task[SocketReceiveFromResult]:
        """"""
    @classmethod
    def ReceiveMessageFromAsync(
        cls,
        socket: Socket,
        buffer: ArraySegment[int],
        socketFlags: SocketFlags,
        remoteEndPoint: EndPoint,
    ) -> Task[SocketReceiveMessageFromResult]:
        """"""
    @classmethod
    @overload
    def SendAsync(
        cls, socket: Socket, buffers: IList[ArraySegment[int]], socketFlags: SocketFlags
    ) -> Task[int]:
        """"""
    @classmethod
    @overload
    def SendAsync(
        cls, socket: Socket, buffer: ArraySegment[int], socketFlags: SocketFlags
    ) -> Task[int]:
        """"""
    @classmethod
    def SendToAsync(
        cls, socket: Socket, buffer: ArraySegment[int], socketFlags: SocketFlags, remoteEP: EndPoint
    ) -> Task[int]:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TcpClient(Object, IDisposable):
    """"""
    @overload
    def __init__(self, localEP: IPEndPoint) -> None:
        """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, family: AddressFamily) -> None:
        """"""
    @overload
    def __init__(self, hostname: str, port: int) -> None:
        """"""
    @property
    def Available(self) -> int:
        """"""
    @property
    def Client(self) -> Socket:
        """"""
    @Client.setter
    def Client(self, value: Socket) -> None: ...
    @property
    def Connected(self) -> bool:
        """"""
    @property
    def ExclusiveAddressUse(self) -> bool:
        """"""
    @ExclusiveAddressUse.setter
    def ExclusiveAddressUse(self, value: bool) -> None: ...
    @property
    def LingerState(self) -> LingerOption:
        """"""
    @LingerState.setter
    def LingerState(self, value: LingerOption) -> None: ...
    @property
    def NoDelay(self) -> bool:
        """"""
    @NoDelay.setter
    def NoDelay(self, value: bool) -> None: ...
    @property
    def ReceiveBufferSize(self) -> int:
        """"""
    @ReceiveBufferSize.setter
    def ReceiveBufferSize(self, value: int) -> None: ...
    @property
    def ReceiveTimeout(self) -> int:
        """"""
    @ReceiveTimeout.setter
    def ReceiveTimeout(self, value: int) -> None: ...
    @property
    def SendBufferSize(self) -> int:
        """"""
    @SendBufferSize.setter
    def SendBufferSize(self, value: int) -> None: ...
    @property
    def SendTimeout(self) -> int:
        """"""
    @SendTimeout.setter
    def SendTimeout(self, value: int) -> None: ...
    @overload
    def BeginConnect(
        self, address: IPAddress, port: int, requestCallback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    @overload
    def BeginConnect(
        self, addresses: Array[IPAddress], port: int, requestCallback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    @overload
    def BeginConnect(
        self, host: str, port: int, requestCallback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def Close(self) -> None:
        """"""
    @overload
    def Connect(self, address: IPAddress, port: int) -> None:
        """"""
    @overload
    def Connect(self, remoteEP: IPEndPoint) -> None:
        """"""
    @overload
    def Connect(self, ipAddresses: Array[IPAddress], port: int) -> None:
        """"""
    @overload
    def Connect(self, hostname: str, port: int) -> None:
        """"""
    @overload
    def ConnectAsync(self, address: IPAddress, port: int) -> Task:
        """"""
    @overload
    def ConnectAsync(self, addresses: Array[IPAddress], port: int) -> Task:
        """"""
    @overload
    def ConnectAsync(self, host: str, port: int) -> Task:
        """"""
    def Dispose(self) -> None:
        """"""
    def EndConnect(self, asyncResult: IAsyncResult) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetStream(self) -> NetworkStream:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TcpListener(Object):
    """"""
    @overload
    def __init__(self, localEP: IPEndPoint) -> None:
        """"""
    @overload
    def __init__(self, localaddr: IPAddress, port: int) -> None:
        """"""
    @overload
    def __init__(self, port: int) -> None:
        """"""
    @property
    def ExclusiveAddressUse(self) -> bool:
        """"""
    @ExclusiveAddressUse.setter
    def ExclusiveAddressUse(self, value: bool) -> None: ...
    @property
    def LocalEndpoint(self) -> EndPoint:
        """"""
    @property
    def Server(self) -> Socket:
        """"""
    def AcceptSocket(self) -> Socket:
        """"""
    def AcceptSocketAsync(self) -> Task[Socket]:
        """"""
    def AcceptTcpClient(self) -> TcpClient:
        """"""
    def AcceptTcpClientAsync(self) -> Task[TcpClient]:
        """"""
    def AllowNatTraversal(self, allowed: bool) -> None:
        """"""
    def BeginAcceptSocket(self, callback: AsyncCallback, state: object) -> IAsyncResult:
        """"""
    def BeginAcceptTcpClient(self, callback: AsyncCallback, state: object) -> IAsyncResult:
        """"""
    @classmethod
    def Create(cls, port: int) -> TcpListener:
        """"""
    def EndAcceptSocket(self, asyncResult: IAsyncResult) -> Socket:
        """"""
    def EndAcceptTcpClient(self, asyncResult: IAsyncResult) -> TcpClient:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Pending(self) -> bool:
        """"""
    @overload
    def Start(self) -> None:
        """"""
    @overload
    def Start(self, backlog: int) -> None:
        """"""
    def Stop(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TimeValue(ValueType):
    """"""

    Microseconds: Final[int]
    """"""
    Seconds: Final[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TransmitFileOverlappedAsyncResult(BaseOverlappedAsyncResult, IAsyncResult):
    """"""
    @property
    def AsyncState(self) -> object:
        """"""
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """"""
    @property
    def CompletedSynchronously(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type TransmitPacketsDelegate = Callable[
    [SafeCloseSocket, IntPtr, int, int, SafeNativeOverlapped, TransmitFileOptions], bool
]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class UdpClient(Object, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, family: AddressFamily) -> None:
        """"""
    @overload
    def __init__(self, port: int) -> None:
        """"""
    @overload
    def __init__(self, port: int, family: AddressFamily) -> None:
        """"""
    @overload
    def __init__(self, localEP: IPEndPoint) -> None:
        """"""
    @overload
    def __init__(self, hostname: str, port: int) -> None:
        """"""
    @property
    def Available(self) -> int:
        """"""
    @property
    def Client(self) -> Socket:
        """"""
    @Client.setter
    def Client(self, value: Socket) -> None: ...
    @property
    def DontFragment(self) -> bool:
        """"""
    @DontFragment.setter
    def DontFragment(self, value: bool) -> None: ...
    @property
    def EnableBroadcast(self) -> bool:
        """"""
    @EnableBroadcast.setter
    def EnableBroadcast(self, value: bool) -> None: ...
    @property
    def ExclusiveAddressUse(self) -> bool:
        """"""
    @ExclusiveAddressUse.setter
    def ExclusiveAddressUse(self, value: bool) -> None: ...
    @property
    def MulticastLoopback(self) -> bool:
        """"""
    @MulticastLoopback.setter
    def MulticastLoopback(self, value: bool) -> None: ...
    @property
    def Ttl(self) -> int:
        """"""
    @Ttl.setter
    def Ttl(self, value: int) -> None: ...
    def AllowNatTraversal(self, allowed: bool) -> None:
        """"""
    def BeginReceive(self, requestCallback: AsyncCallback, state: object) -> IAsyncResult:
        """"""
    @overload
    def BeginSend(
        self,
        datagram: Array[int],
        bytes: int,
        endPoint: IPEndPoint,
        requestCallback: AsyncCallback,
        state: object,
    ) -> IAsyncResult:
        """"""
    @overload
    def BeginSend(
        self, datagram: Array[int], bytes: int, requestCallback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
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
        """"""
    def Close(self) -> None:
        """"""
    @overload
    def Connect(self, addr: IPAddress, port: int) -> None:
        """"""
    @overload
    def Connect(self, endPoint: IPEndPoint) -> None:
        """"""
    @overload
    def Connect(self, hostname: str, port: int) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    @overload
    def DropMulticastGroup(self, multicastAddr: IPAddress) -> None:
        """"""
    @overload
    def DropMulticastGroup(self, multicastAddr: IPAddress, ifindex: int) -> None:
        """"""
    def EndReceive(self, asyncResult: IAsyncResult, remoteEP: IPEndPoint) -> Array[int]:
        """"""
    def EndSend(self, asyncResult: IAsyncResult) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def JoinMulticastGroup(self, multicastAddr: IPAddress) -> None:
        """"""
    @overload
    def JoinMulticastGroup(self, multicastAddr: IPAddress, localAddress: IPAddress) -> None:
        """"""
    @overload
    def JoinMulticastGroup(self, multicastAddr: IPAddress, timeToLive: int) -> None:
        """"""
    @overload
    def JoinMulticastGroup(self, ifindex: int, multicastAddr: IPAddress) -> None:
        """"""
    def Receive(self, remoteEP: IPEndPoint) -> Array[int]:
        """"""
    def ReceiveAsync(self) -> Task[UdpReceiveResult]:
        """"""
    @overload
    def Send(self, dgram: Array[int], bytes: int) -> int:
        """"""
    @overload
    def Send(self, dgram: Array[int], bytes: int, endPoint: IPEndPoint) -> int:
        """"""
    @overload
    def Send(self, dgram: Array[int], bytes: int, hostname: str, port: int) -> int:
        """"""
    @overload
    def SendAsync(self, datagram: Array[int], bytes: int) -> Task[int]:
        """"""
    @overload
    def SendAsync(self, datagram: Array[int], bytes: int, endPoint: IPEndPoint) -> Task[int]:
        """"""
    @overload
    def SendAsync(self, datagram: Array[int], bytes: int, hostname: str, port: int) -> Task[int]:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class UdpReceiveResult(ValueType, IEquatable[UdpReceiveResult]):
    """"""
    def __init__(self, buffer: Array[int], remoteEndPoint: IPEndPoint) -> None:
        """"""
    @property
    def Buffer(self) -> Array[int]:
        """"""
    @property
    def RemoteEndPoint(self) -> IPEndPoint:
        """"""
    @overload
    def Equals(self, other: UdpReceiveResult) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, left: UdpReceiveResult, right: UdpReceiveResult) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: UdpReceiveResult, right: UdpReceiveResult) -> bool:
        """"""
    def __eq__(self, other: UdpReceiveResult) -> bool:
        """"""
    def __ne__(self, other: UdpReceiveResult) -> bool:
        """"""

type WSARecvMsgDelegate = Callable[
    [SafeCloseSocket, IntPtr, Int32, SafeHandle, IntPtr], SocketError
]
""""""
type WSARecvMsgDelegate_Blocking = Callable[[IntPtr, IntPtr, Int32, IntPtr, IntPtr], SocketError]
""""""
