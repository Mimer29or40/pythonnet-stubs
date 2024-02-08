from __future__ import annotations

from abc import ABC
from typing import Callable
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import Iterator
from typing import Tuple
from typing import TypeVar
from typing import overload

from Microsoft.Win32.SafeHandles import SafeHandleZeroOrMinusOneIsInvalid
from System import Action
from System import Array
from System import AsyncCallback
from System import Enum
from System import EventArgs
from System import EventHandler
from System import Exception
from System import Guid
from System import IAsyncResult
from System import IDisposable
from System import IntPtr
from System import InvalidOperationException
from System import Object
from System import Type
from System import ValueType
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections.Generic import ICollection
from System.Collections.Generic import IEnumerable
from System.ComponentModel import AsyncCompletedEventArgs
from System.ComponentModel import Component
from System.ComponentModel import IComponent
from System.ComponentModel import IContainer
from System.ComponentModel import ISite
from System.ComponentModel import Win32Exception
from System.Net import IPAddress
from System.Net import IPEndPoint
from System.Reflection import MethodBase
from System.Runtime.InteropServices import _Attribute
from System.Runtime.InteropServices import _Exception
from System.Runtime.Remoting import ObjRef
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Security import CodeAccessPermission
from System.Security import IPermission
from System.Security import ISecurityEncodable
from System.Security import IStackWalk
from System.Security import SecurityElement
from System.Security.Permissions import CodeAccessSecurityAttribute
from System.Security.Permissions import IUnrestrictedPermission
from System.Security.Permissions import PermissionState
from System.Security.Permissions import SecurityAction
from System.Threading.Tasks import Task

T = TypeVar("T")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

class AdapterAddressFlags(Enum):
    """"""

    DnsEligible: AdapterAddressFlags = ...
    """"""
    Transient: AdapterAddressFlags = ...
    """"""

class AdapterFlags(Enum):
    """"""

    DnsEnabled: AdapterFlags = ...
    """"""
    RegisterAdapterSuffix: AdapterFlags = ...
    """"""
    DhcpEnabled: AdapterFlags = ...
    """"""
    ReceiveOnly: AdapterFlags = ...
    """"""
    NoMulticast: AdapterFlags = ...
    """"""
    Ipv6OtherStatefulConfig: AdapterFlags = ...
    """"""
    NetBiosOverTcp: AdapterFlags = ...
    """"""
    IPv4Enabled: AdapterFlags = ...
    """"""
    IPv6Enabled: AdapterFlags = ...
    """"""
    IPv6ManagedAddressConfigurationSupported: AdapterFlags = ...
    """"""

class DuplicateAddressDetectionState(Enum):
    """"""

    Invalid: DuplicateAddressDetectionState = ...
    """"""
    Tentative: DuplicateAddressDetectionState = ...
    """"""
    Duplicate: DuplicateAddressDetectionState = ...
    """"""
    Deprecated: DuplicateAddressDetectionState = ...
    """"""
    Preferred: DuplicateAddressDetectionState = ...
    """"""

class FIXED_INFO(ValueType):
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

class FixedInfo(ValueType):
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

class GatewayIPAddressInformation(ABC, Object):
    """"""

    @property
    def Address(self) -> IPAddress:
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

class GatewayIPAddressInformationCollection(
    Object,
    ICollection[GatewayIPAddressInformation],
    IEnumerable[GatewayIPAddressInformation],
    IEnumerable,
):
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> GatewayIPAddressInformation:
        """

        :return:
        """
    def Add(self, item: GatewayIPAddressInformation) -> None:
        """

        :param item:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, item: GatewayIPAddressInformation) -> bool:
        """

        :param item:
        :return:
        """
    def CopyTo(self, array: Array[GatewayIPAddressInformation], arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    def Remove(self, item: GatewayIPAddressInformation) -> bool:
        """

        :param item:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: GatewayIPAddressInformation) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> GatewayIPAddressInformation:
        """

        :param index:
        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[GatewayIPAddressInformation]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

class GetAdaptersAddressesFlags(Enum):
    """"""

    SkipUnicast: GetAdaptersAddressesFlags = ...
    """"""
    SkipAnycast: GetAdaptersAddressesFlags = ...
    """"""
    SkipMulticast: GetAdaptersAddressesFlags = ...
    """"""
    SkipDnsServer: GetAdaptersAddressesFlags = ...
    """"""
    IncludePrefix: GetAdaptersAddressesFlags = ...
    """"""
    SkipFriendlyName: GetAdaptersAddressesFlags = ...
    """"""
    IncludeWins: GetAdaptersAddressesFlags = ...
    """"""
    IncludeGateways: GetAdaptersAddressesFlags = ...
    """"""
    IncludeAllInterfaces: GetAdaptersAddressesFlags = ...
    """"""
    IncludeAllCompartments: GetAdaptersAddressesFlags = ...
    """"""
    IncludeTunnelBindingOrder: GetAdaptersAddressesFlags = ...
    """"""

class IPAddressCollection(Object, ICollection[IPAddress], IEnumerable[IPAddress], IEnumerable):
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> IPAddress:
        """

        :return:
        """
    def Add(self, item: IPAddress) -> None:
        """

        :param item:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, item: IPAddress) -> bool:
        """

        :param item:
        :return:
        """
    def CopyTo(self, array: Array[IPAddress], arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    def Remove(self, item: IPAddress) -> bool:
        """

        :param item:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: IPAddress) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> IPAddress:
        """

        :param index:
        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[IPAddress]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

class IPAddressInformation(ABC, Object):
    """"""

    @property
    def Address(self) -> IPAddress:
        """

        :return:
        """
    @property
    def IsDnsEligible(self) -> bool:
        """

        :return:
        """
    @property
    def IsTransient(self) -> bool:
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

class IPAddressInformationCollection(
    Object, ICollection[IPAddressInformation], IEnumerable[IPAddressInformation], IEnumerable
):
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> IPAddressInformation:
        """

        :return:
        """
    def Add(self, item: IPAddressInformation) -> None:
        """

        :param item:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, item: IPAddressInformation) -> bool:
        """

        :param item:
        :return:
        """
    def CopyTo(self, array: Array[IPAddressInformation], arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    def Remove(self, item: IPAddressInformation) -> bool:
        """

        :param item:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: IPAddressInformation) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> IPAddressInformation:
        """

        :param index:
        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[IPAddressInformation]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

class IPGlobalProperties(ABC, Object):
    """"""

    @property
    def DhcpScopeName(self) -> str:
        """

        :return:
        """
    @property
    def DomainName(self) -> str:
        """

        :return:
        """
    @property
    def HostName(self) -> str:
        """

        :return:
        """
    @property
    def IsWinsProxy(self) -> bool:
        """

        :return:
        """
    @property
    def NodeType(self) -> NetBiosNodeType:
        """

        :return:
        """
    def BeginGetUnicastAddresses(self, callback: AsyncCallback, state: object) -> IAsyncResult:
        """

        :param callback:
        :param state:
        :return:
        """
    def EndGetUnicastAddresses(
        self, asyncResult: IAsyncResult
    ) -> UnicastIPAddressInformationCollection:
        """

        :param asyncResult:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetActiveTcpConnections(self) -> Array[TcpConnectionInformation]:
        """

        :return:
        """
    def GetActiveTcpListeners(self) -> Array[IPEndPoint]:
        """

        :return:
        """
    def GetActiveUdpListeners(self) -> Array[IPEndPoint]:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @classmethod
    def GetIPGlobalProperties(cls) -> IPGlobalProperties:
        """

        :return:
        """
    def GetIPv4GlobalStatistics(self) -> IPGlobalStatistics:
        """

        :return:
        """
    def GetIPv6GlobalStatistics(self) -> IPGlobalStatistics:
        """

        :return:
        """
    def GetIcmpV4Statistics(self) -> IcmpV4Statistics:
        """

        :return:
        """
    def GetIcmpV6Statistics(self) -> IcmpV6Statistics:
        """

        :return:
        """
    def GetTcpIPv4Statistics(self) -> TcpStatistics:
        """

        :return:
        """
    def GetTcpIPv6Statistics(self) -> TcpStatistics:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetUdpIPv4Statistics(self) -> UdpStatistics:
        """

        :return:
        """
    def GetUdpIPv6Statistics(self) -> UdpStatistics:
        """

        :return:
        """
    def GetUnicastAddresses(self) -> UnicastIPAddressInformationCollection:
        """

        :return:
        """
    def GetUnicastAddressesAsync(self) -> Task[UnicastIPAddressInformationCollection]:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class IPGlobalStatistics(ABC, Object):
    """"""

    @property
    def DefaultTtl(self) -> int:
        """

        :return:
        """
    @property
    def ForwardingEnabled(self) -> bool:
        """

        :return:
        """
    @property
    def NumberOfIPAddresses(self) -> int:
        """

        :return:
        """
    @property
    def NumberOfInterfaces(self) -> int:
        """

        :return:
        """
    @property
    def NumberOfRoutes(self) -> int:
        """

        :return:
        """
    @property
    def OutputPacketRequests(self) -> int:
        """

        :return:
        """
    @property
    def OutputPacketRoutingDiscards(self) -> int:
        """

        :return:
        """
    @property
    def OutputPacketsDiscarded(self) -> int:
        """

        :return:
        """
    @property
    def OutputPacketsWithNoRoute(self) -> int:
        """

        :return:
        """
    @property
    def PacketFragmentFailures(self) -> int:
        """

        :return:
        """
    @property
    def PacketReassembliesRequired(self) -> int:
        """

        :return:
        """
    @property
    def PacketReassemblyFailures(self) -> int:
        """

        :return:
        """
    @property
    def PacketReassemblyTimeout(self) -> int:
        """

        :return:
        """
    @property
    def PacketsFragmented(self) -> int:
        """

        :return:
        """
    @property
    def PacketsReassembled(self) -> int:
        """

        :return:
        """
    @property
    def ReceivedPackets(self) -> int:
        """

        :return:
        """
    @property
    def ReceivedPacketsDelivered(self) -> int:
        """

        :return:
        """
    @property
    def ReceivedPacketsDiscarded(self) -> int:
        """

        :return:
        """
    @property
    def ReceivedPacketsForwarded(self) -> int:
        """

        :return:
        """
    @property
    def ReceivedPacketsWithAddressErrors(self) -> int:
        """

        :return:
        """
    @property
    def ReceivedPacketsWithHeadersErrors(self) -> int:
        """

        :return:
        """
    @property
    def ReceivedPacketsWithUnknownProtocol(self) -> int:
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

class IPInterfaceProperties(ABC, Object):
    """"""

    @property
    def AnycastAddresses(self) -> IPAddressInformationCollection:
        """

        :return:
        """
    @property
    def DhcpServerAddresses(self) -> IPAddressCollection:
        """

        :return:
        """
    @property
    def DnsAddresses(self) -> IPAddressCollection:
        """

        :return:
        """
    @property
    def DnsSuffix(self) -> str:
        """

        :return:
        """
    @property
    def GatewayAddresses(self) -> GatewayIPAddressInformationCollection:
        """

        :return:
        """
    @property
    def IsDnsEnabled(self) -> bool:
        """

        :return:
        """
    @property
    def IsDynamicDnsEnabled(self) -> bool:
        """

        :return:
        """
    @property
    def MulticastAddresses(self) -> MulticastIPAddressInformationCollection:
        """

        :return:
        """
    @property
    def UnicastAddresses(self) -> UnicastIPAddressInformationCollection:
        """

        :return:
        """
    @property
    def WinsServersAddresses(self) -> IPAddressCollection:
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
    def GetIPv4Properties(self) -> IPv4InterfaceProperties:
        """

        :return:
        """
    def GetIPv6Properties(self) -> IPv6InterfaceProperties:
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

class IPInterfaceStatistics(ABC, Object):
    """"""

    @property
    def BytesReceived(self) -> int:
        """

        :return:
        """
    @property
    def BytesSent(self) -> int:
        """

        :return:
        """
    @property
    def IncomingPacketsDiscarded(self) -> int:
        """

        :return:
        """
    @property
    def IncomingPacketsWithErrors(self) -> int:
        """

        :return:
        """
    @property
    def IncomingUnknownProtocolPackets(self) -> int:
        """

        :return:
        """
    @property
    def NonUnicastPacketsReceived(self) -> int:
        """

        :return:
        """
    @property
    def NonUnicastPacketsSent(self) -> int:
        """

        :return:
        """
    @property
    def OutgoingPacketsDiscarded(self) -> int:
        """

        :return:
        """
    @property
    def OutgoingPacketsWithErrors(self) -> int:
        """

        :return:
        """
    @property
    def OutputQueueLength(self) -> int:
        """

        :return:
        """
    @property
    def UnicastPacketsReceived(self) -> int:
        """

        :return:
        """
    @property
    def UnicastPacketsSent(self) -> int:
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

class IPOptions(ValueType):
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

class IPStatus(Enum):
    """"""

    Success: IPStatus = ...
    """"""
    DestinationNetworkUnreachable: IPStatus = ...
    """"""
    DestinationHostUnreachable: IPStatus = ...
    """"""
    DestinationProhibited: IPStatus = ...
    """"""
    DestinationProtocolUnreachable: IPStatus = ...
    """"""
    DestinationPortUnreachable: IPStatus = ...
    """"""
    NoResources: IPStatus = ...
    """"""
    BadOption: IPStatus = ...
    """"""
    HardwareError: IPStatus = ...
    """"""
    PacketTooBig: IPStatus = ...
    """"""
    TimedOut: IPStatus = ...
    """"""
    BadRoute: IPStatus = ...
    """"""
    TtlExpired: IPStatus = ...
    """"""
    TtlReassemblyTimeExceeded: IPStatus = ...
    """"""
    ParameterProblem: IPStatus = ...
    """"""
    SourceQuench: IPStatus = ...
    """"""
    BadDestination: IPStatus = ...
    """"""
    DestinationUnreachable: IPStatus = ...
    """"""
    TimeExceeded: IPStatus = ...
    """"""
    BadHeader: IPStatus = ...
    """"""
    UnrecognizedNextHeader: IPStatus = ...
    """"""
    IcmpError: IPStatus = ...
    """"""
    DestinationScopeMismatch: IPStatus = ...
    """"""
    Unknown: IPStatus = ...
    """"""

class IPv4InterfaceProperties(ABC, Object):
    """"""

    @property
    def Index(self) -> int:
        """

        :return:
        """
    @property
    def IsAutomaticPrivateAddressingActive(self) -> bool:
        """

        :return:
        """
    @property
    def IsAutomaticPrivateAddressingEnabled(self) -> bool:
        """

        :return:
        """
    @property
    def IsDhcpEnabled(self) -> bool:
        """

        :return:
        """
    @property
    def IsForwardingEnabled(self) -> bool:
        """

        :return:
        """
    @property
    def Mtu(self) -> int:
        """

        :return:
        """
    @property
    def UsesWins(self) -> bool:
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

class IPv4InterfaceStatistics(ABC, Object):
    """"""

    @property
    def BytesReceived(self) -> int:
        """

        :return:
        """
    @property
    def BytesSent(self) -> int:
        """

        :return:
        """
    @property
    def IncomingPacketsDiscarded(self) -> int:
        """

        :return:
        """
    @property
    def IncomingPacketsWithErrors(self) -> int:
        """

        :return:
        """
    @property
    def IncomingUnknownProtocolPackets(self) -> int:
        """

        :return:
        """
    @property
    def NonUnicastPacketsReceived(self) -> int:
        """

        :return:
        """
    @property
    def NonUnicastPacketsSent(self) -> int:
        """

        :return:
        """
    @property
    def OutgoingPacketsDiscarded(self) -> int:
        """

        :return:
        """
    @property
    def OutgoingPacketsWithErrors(self) -> int:
        """

        :return:
        """
    @property
    def OutputQueueLength(self) -> int:
        """

        :return:
        """
    @property
    def UnicastPacketsReceived(self) -> int:
        """

        :return:
        """
    @property
    def UnicastPacketsSent(self) -> int:
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

class IPv6InterfaceProperties(ABC, Object):
    """"""

    @property
    def Index(self) -> int:
        """

        :return:
        """
    @property
    def Mtu(self) -> int:
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
    def GetScopeId(self, scopeLevel: ScopeLevel) -> int:
        """

        :param scopeLevel:
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

class Icmp6EchoReply(ValueType):
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

class IcmpEchoReply(ValueType):
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

class IcmpV4Code(Enum):
    """"""

    ICMP4_UNREACH_NET: IcmpV4Code = ...
    """"""
    ICMP4_UNREACH_HOST: IcmpV4Code = ...
    """"""
    ICMP4_UNREACH_PROTOCOL: IcmpV4Code = ...
    """"""
    ICMP4_UNREACH_PORT: IcmpV4Code = ...
    """"""
    ICMP4_UNREACH_FRAG_NEEDED: IcmpV4Code = ...
    """"""
    ICMP4_UNREACH_SOURCEROUTE_FAILED: IcmpV4Code = ...
    """"""
    ICMP4_UNREACH_NET_UNKNOWN: IcmpV4Code = ...
    """"""
    ICMP4_UNREACH_HOST_UNKNOWN: IcmpV4Code = ...
    """"""
    ICMP4_UNREACH_ISOLATED: IcmpV4Code = ...
    """"""
    ICMP4_UNREACH_NET_ADMIN: IcmpV4Code = ...
    """"""
    ICMP4_UNREACH_HOST_ADMIN: IcmpV4Code = ...
    """"""
    ICMP4_UNREACH_NET_TOS: IcmpV4Code = ...
    """"""
    ICMP4_UNREACH_HOST_TOS: IcmpV4Code = ...
    """"""
    ICMP4_UNREACH_ADMIN: IcmpV4Code = ...
    """"""

class IcmpV4Statistics(ABC, Object):
    """"""

    @property
    def AddressMaskRepliesReceived(self) -> int:
        """

        :return:
        """
    @property
    def AddressMaskRepliesSent(self) -> int:
        """

        :return:
        """
    @property
    def AddressMaskRequestsReceived(self) -> int:
        """

        :return:
        """
    @property
    def AddressMaskRequestsSent(self) -> int:
        """

        :return:
        """
    @property
    def DestinationUnreachableMessagesReceived(self) -> int:
        """

        :return:
        """
    @property
    def DestinationUnreachableMessagesSent(self) -> int:
        """

        :return:
        """
    @property
    def EchoRepliesReceived(self) -> int:
        """

        :return:
        """
    @property
    def EchoRepliesSent(self) -> int:
        """

        :return:
        """
    @property
    def EchoRequestsReceived(self) -> int:
        """

        :return:
        """
    @property
    def EchoRequestsSent(self) -> int:
        """

        :return:
        """
    @property
    def ErrorsReceived(self) -> int:
        """

        :return:
        """
    @property
    def ErrorsSent(self) -> int:
        """

        :return:
        """
    @property
    def MessagesReceived(self) -> int:
        """

        :return:
        """
    @property
    def MessagesSent(self) -> int:
        """

        :return:
        """
    @property
    def ParameterProblemsReceived(self) -> int:
        """

        :return:
        """
    @property
    def ParameterProblemsSent(self) -> int:
        """

        :return:
        """
    @property
    def RedirectsReceived(self) -> int:
        """

        :return:
        """
    @property
    def RedirectsSent(self) -> int:
        """

        :return:
        """
    @property
    def SourceQuenchesReceived(self) -> int:
        """

        :return:
        """
    @property
    def SourceQuenchesSent(self) -> int:
        """

        :return:
        """
    @property
    def TimeExceededMessagesReceived(self) -> int:
        """

        :return:
        """
    @property
    def TimeExceededMessagesSent(self) -> int:
        """

        :return:
        """
    @property
    def TimestampRepliesReceived(self) -> int:
        """

        :return:
        """
    @property
    def TimestampRepliesSent(self) -> int:
        """

        :return:
        """
    @property
    def TimestampRequestsReceived(self) -> int:
        """

        :return:
        """
    @property
    def TimestampRequestsSent(self) -> int:
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

class IcmpV4Type(Enum):
    """"""

    ICMP4_ECHO_REPLY: IcmpV4Type = ...
    """"""
    ICMP4_DST_UNREACH: IcmpV4Type = ...
    """"""
    ICMP4_SOURCE_QUENCH: IcmpV4Type = ...
    """"""
    ICMP4_REDIRECT: IcmpV4Type = ...
    """"""
    ICMP4_ECHO_REQUEST: IcmpV4Type = ...
    """"""
    ICMP4_ROUTER_ADVERT: IcmpV4Type = ...
    """"""
    ICMP4_ROUTER_SOLICIT: IcmpV4Type = ...
    """"""
    ICMP4_TIME_EXCEEDED: IcmpV4Type = ...
    """"""
    ICMP4_PARAM_PROB: IcmpV4Type = ...
    """"""
    ICMP4_TIMESTAMP_REQUEST: IcmpV4Type = ...
    """"""
    ICMP4_TIMESTAMP_REPLY: IcmpV4Type = ...
    """"""
    ICMP4_MASK_REQUEST: IcmpV4Type = ...
    """"""
    ICMP4_MASK_REPLY: IcmpV4Type = ...
    """"""

class IcmpV6StatType(Enum):
    """"""

    DestinationUnreachable: IcmpV6StatType = ...
    """"""
    PacketTooBig: IcmpV6StatType = ...
    """"""
    TimeExceeded: IcmpV6StatType = ...
    """"""
    ParameterProblem: IcmpV6StatType = ...
    """"""
    EchoRequest: IcmpV6StatType = ...
    """"""
    EchoReply: IcmpV6StatType = ...
    """"""
    MembershipQuery: IcmpV6StatType = ...
    """"""
    MembershipReport: IcmpV6StatType = ...
    """"""
    MembershipReduction: IcmpV6StatType = ...
    """"""
    RouterSolicit: IcmpV6StatType = ...
    """"""
    RouterAdvertisement: IcmpV6StatType = ...
    """"""
    NeighborSolict: IcmpV6StatType = ...
    """"""
    NeighborAdvertisement: IcmpV6StatType = ...
    """"""
    Redirect: IcmpV6StatType = ...
    """"""

class IcmpV6Statistics(ABC, Object):
    """"""

    @property
    def DestinationUnreachableMessagesReceived(self) -> int:
        """

        :return:
        """
    @property
    def DestinationUnreachableMessagesSent(self) -> int:
        """

        :return:
        """
    @property
    def EchoRepliesReceived(self) -> int:
        """

        :return:
        """
    @property
    def EchoRepliesSent(self) -> int:
        """

        :return:
        """
    @property
    def EchoRequestsReceived(self) -> int:
        """

        :return:
        """
    @property
    def EchoRequestsSent(self) -> int:
        """

        :return:
        """
    @property
    def ErrorsReceived(self) -> int:
        """

        :return:
        """
    @property
    def ErrorsSent(self) -> int:
        """

        :return:
        """
    @property
    def MembershipQueriesReceived(self) -> int:
        """

        :return:
        """
    @property
    def MembershipQueriesSent(self) -> int:
        """

        :return:
        """
    @property
    def MembershipReductionsReceived(self) -> int:
        """

        :return:
        """
    @property
    def MembershipReductionsSent(self) -> int:
        """

        :return:
        """
    @property
    def MembershipReportsReceived(self) -> int:
        """

        :return:
        """
    @property
    def MembershipReportsSent(self) -> int:
        """

        :return:
        """
    @property
    def MessagesReceived(self) -> int:
        """

        :return:
        """
    @property
    def MessagesSent(self) -> int:
        """

        :return:
        """
    @property
    def NeighborAdvertisementsReceived(self) -> int:
        """

        :return:
        """
    @property
    def NeighborAdvertisementsSent(self) -> int:
        """

        :return:
        """
    @property
    def NeighborSolicitsReceived(self) -> int:
        """

        :return:
        """
    @property
    def NeighborSolicitsSent(self) -> int:
        """

        :return:
        """
    @property
    def PacketTooBigMessagesReceived(self) -> int:
        """

        :return:
        """
    @property
    def PacketTooBigMessagesSent(self) -> int:
        """

        :return:
        """
    @property
    def ParameterProblemsReceived(self) -> int:
        """

        :return:
        """
    @property
    def ParameterProblemsSent(self) -> int:
        """

        :return:
        """
    @property
    def RedirectsReceived(self) -> int:
        """

        :return:
        """
    @property
    def RedirectsSent(self) -> int:
        """

        :return:
        """
    @property
    def RouterAdvertisementsReceived(self) -> int:
        """

        :return:
        """
    @property
    def RouterAdvertisementsSent(self) -> int:
        """

        :return:
        """
    @property
    def RouterSolicitsReceived(self) -> int:
        """

        :return:
        """
    @property
    def RouterSolicitsSent(self) -> int:
        """

        :return:
        """
    @property
    def TimeExceededMessagesReceived(self) -> int:
        """

        :return:
        """
    @property
    def TimeExceededMessagesSent(self) -> int:
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

class InterfaceConnectionType(Enum):
    """"""

    Dedicated: InterfaceConnectionType = ...
    """"""
    Passive: InterfaceConnectionType = ...
    """"""
    Demand: InterfaceConnectionType = ...
    """"""
    Maximum: InterfaceConnectionType = ...
    """"""

class InterfaceTunnelType(Enum):
    """"""

    _None: InterfaceTunnelType = ...
    """"""
    Other: InterfaceTunnelType = ...
    """"""
    Direct: InterfaceTunnelType = ...
    """"""
    SixToFour: InterfaceTunnelType = ...
    """"""
    Isatap: InterfaceTunnelType = ...
    """"""
    Teredo: InterfaceTunnelType = ...
    """"""
    IpHttps: InterfaceTunnelType = ...
    """"""

class IpAdapterAddress(ValueType):
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

class IpAdapterAddresses(ValueType):
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

class IpAdapterUnicastAddress(ValueType):
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

class IpAddrString(ValueType):
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

class IpHelperErrors(Object):
    """"""

    def __init__(self):
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

class IpPerAdapterInfo(ValueType):
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

class IpSocketAddress(ValueType):
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

class Ipv6Address(ValueType):
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

class MibIcmpInfo(ValueType):
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

class MibIcmpInfoEx(ValueType):
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

class MibIcmpStats(ValueType):
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

class MibIcmpStatsEx(ValueType):
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

class MibIfRow2(ValueType):
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

class MibIpStats(ValueType):
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

class MibTcp6RowOwnerPid(ValueType):
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

class MibTcp6TableOwnerPid(ValueType):
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

class MibTcpRow(ValueType):
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

class MibTcpStats(ValueType):
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

class MibTcpTable(ValueType):
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

class MibUdp6RowOwnerPid(ValueType):
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

class MibUdp6TableOwnerPid(ValueType):
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

class MibUdpRow(ValueType):
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

class MibUdpStats(ValueType):
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

class MibUdpTable(ValueType):
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

class MulticastIPAddressInformation(ABC, IPAddressInformation):
    """"""

    @property
    def Address(self) -> IPAddress:
        """

        :return:
        """
    @property
    def AddressPreferredLifetime(self) -> int:
        """

        :return:
        """
    @property
    def AddressValidLifetime(self) -> int:
        """

        :return:
        """
    @property
    def DhcpLeaseLifetime(self) -> int:
        """

        :return:
        """
    @property
    def DuplicateAddressDetectionState(self) -> DuplicateAddressDetectionState:
        """

        :return:
        """
    @property
    def IsDnsEligible(self) -> bool:
        """

        :return:
        """
    @property
    def IsTransient(self) -> bool:
        """

        :return:
        """
    @property
    def PrefixOrigin(self) -> PrefixOrigin:
        """

        :return:
        """
    @property
    def SuffixOrigin(self) -> SuffixOrigin:
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

class MulticastIPAddressInformationCollection(
    Object,
    ICollection[MulticastIPAddressInformation],
    IEnumerable[MulticastIPAddressInformation],
    IEnumerable,
):
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> MulticastIPAddressInformation:
        """

        :return:
        """
    def Add(self, item: MulticastIPAddressInformation) -> None:
        """

        :param item:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, item: MulticastIPAddressInformation) -> bool:
        """

        :param item:
        :return:
        """
    def CopyTo(self, array: Array[MulticastIPAddressInformation], arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    def Remove(self, item: MulticastIPAddressInformation) -> bool:
        """

        :param item:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: MulticastIPAddressInformation) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> MulticastIPAddressInformation:
        """

        :param index:
        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[MulticastIPAddressInformation]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

class NetBiosNodeType(Enum):
    """"""

    Unknown: NetBiosNodeType = ...
    """"""
    Broadcast: NetBiosNodeType = ...
    """"""
    Peer2Peer: NetBiosNodeType = ...
    """"""
    Mixed: NetBiosNodeType = ...
    """"""
    Hybrid: NetBiosNodeType = ...
    """"""

NetworkAddressChangedEventHandler: Callable[[object, EventArgs], None] = ...
"""

:param sender: 
:param e: 
"""
NetworkAvailabilityChangedEventHandler: Callable[[object, NetworkAvailabilityEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class NetworkAvailabilityEventArgs(EventArgs):
    """"""

    @property
    def IsAvailable(self) -> bool:
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

class NetworkChange(Object):
    """"""

    def __init__(self):
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
    def RegisterNetworkChange(cls, nc: NetworkChange) -> None:
        """

        :param nc:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    NetworkAddressChanged: EventType[NetworkAddressChangedEventHandler] = ...
    """"""
    NetworkAvailabilityChanged: EventType[NetworkAvailabilityChangedEventHandler] = ...
    """"""

class NetworkInformationAccess(Enum):
    """"""

    _None: NetworkInformationAccess = ...
    """"""
    Read: NetworkInformationAccess = ...
    """"""
    Ping: NetworkInformationAccess = ...
    """"""

class NetworkInformationException(Win32Exception, _Exception, ISerializable):
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

class NetworkInformationPermission(
    CodeAccessPermission, IUnrestrictedPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""

    @overload
    def __init__(self, access: NetworkInformationAccess):
        """

        :param access:
        """
    @overload
    def __init__(self, state: PermissionState):
        """

        :param state:
        """
    @property
    def Access(self) -> NetworkInformationAccess:
        """

        :return:
        """
    def AddPermission(self, access: NetworkInformationAccess) -> None:
        """

        :param access:
        """
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """

        :return:
        """
    @overload
    def Demand(self) -> None:
        """"""
    @overload
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FromXml(self, e: SecurityElement) -> None:
        """

        :param e:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Intersect(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """
    def IsSubsetOf(self, target: IPermission) -> bool:
        """

        :param target:
        :return:
        """
    def IsUnrestricted(self) -> bool:
        """

        :return:
        """
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXml(self) -> SecurityElement:
        """

        :return:
        """
    def Union(self, target: IPermission) -> IPermission:
        """

        :param target:
        :return:
        """

class NetworkInformationPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""

    def __init__(self, action: SecurityAction):
        """

        :param action:
        """
    @property
    def Access(self) -> str:
        """

        :return:
        """
    @Access.setter
    def Access(self, value: str) -> None: ...
    @property
    def Action(self) -> SecurityAction:
        """

        :return:
        """
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Unrestricted(self) -> bool:
        """

        :return:
        """
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    def CreatePermission(self) -> IPermission:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class NetworkInterface(ABC, Object):
    """"""

    @property
    def Description(self) -> str:
        """

        :return:
        """
    @classmethod
    @property
    def IPv6LoopbackInterfaceIndex(cls) -> int:
        """

        :return:
        """
    @property
    def Id(self) -> str:
        """

        :return:
        """
    @property
    def IsReceiveOnly(self) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def LoopbackInterfaceIndex(cls) -> int:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def NetworkInterfaceType(self) -> NetworkInterfaceType:
        """

        :return:
        """
    @property
    def OperationalStatus(self) -> OperationalStatus:
        """

        :return:
        """
    @property
    def Speed(self) -> int:
        """

        :return:
        """
    @property
    def SupportsMulticast(self) -> bool:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def GetAllNetworkInterfaces(cls) -> Array[NetworkInterface]:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIPProperties(self) -> IPInterfaceProperties:
        """

        :return:
        """
    def GetIPStatistics(self) -> IPInterfaceStatistics:
        """

        :return:
        """
    def GetIPv4Statistics(self) -> IPv4InterfaceStatistics:
        """

        :return:
        """
    @classmethod
    def GetIsNetworkAvailable(cls) -> bool:
        """

        :return:
        """
    def GetPhysicalAddress(self) -> PhysicalAddress:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Supports(self, networkInterfaceComponent: NetworkInterfaceComponent) -> bool:
        """

        :param networkInterfaceComponent:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class NetworkInterfaceComponent(Enum):
    """"""

    IPv4: NetworkInterfaceComponent = ...
    """"""
    IPv6: NetworkInterfaceComponent = ...
    """"""

class NetworkInterfaceType(Enum):
    """"""

    Unknown: NetworkInterfaceType = ...
    """"""
    Ethernet: NetworkInterfaceType = ...
    """"""
    TokenRing: NetworkInterfaceType = ...
    """"""
    Fddi: NetworkInterfaceType = ...
    """"""
    BasicIsdn: NetworkInterfaceType = ...
    """"""
    PrimaryIsdn: NetworkInterfaceType = ...
    """"""
    Ppp: NetworkInterfaceType = ...
    """"""
    Loopback: NetworkInterfaceType = ...
    """"""
    Ethernet3Megabit: NetworkInterfaceType = ...
    """"""
    Slip: NetworkInterfaceType = ...
    """"""
    Atm: NetworkInterfaceType = ...
    """"""
    GenericModem: NetworkInterfaceType = ...
    """"""
    FastEthernetT: NetworkInterfaceType = ...
    """"""
    Isdn: NetworkInterfaceType = ...
    """"""
    FastEthernetFx: NetworkInterfaceType = ...
    """"""
    Wireless80211: NetworkInterfaceType = ...
    """"""
    AsymmetricDsl: NetworkInterfaceType = ...
    """"""
    RateAdaptDsl: NetworkInterfaceType = ...
    """"""
    SymmetricDsl: NetworkInterfaceType = ...
    """"""
    VeryHighSpeedDsl: NetworkInterfaceType = ...
    """"""
    IPOverAtm: NetworkInterfaceType = ...
    """"""
    GigabitEthernet: NetworkInterfaceType = ...
    """"""
    Tunnel: NetworkInterfaceType = ...
    """"""
    MultiRateSymmetricDsl: NetworkInterfaceType = ...
    """"""
    HighPerformanceSerialBus: NetworkInterfaceType = ...
    """"""
    Wman: NetworkInterfaceType = ...
    """"""
    Wwanpp: NetworkInterfaceType = ...
    """"""
    Wwanpp2: NetworkInterfaceType = ...
    """"""

class OldOperationalStatus(Enum):
    """"""

    NonOperational: OldOperationalStatus = ...
    """"""
    Unreachable: OldOperationalStatus = ...
    """"""
    Disconnected: OldOperationalStatus = ...
    """"""
    Connecting: OldOperationalStatus = ...
    """"""
    Connected: OldOperationalStatus = ...
    """"""
    Operational: OldOperationalStatus = ...
    """"""

class OperationalStatus(Enum):
    """"""

    Up: OperationalStatus = ...
    """"""
    Down: OperationalStatus = ...
    """"""
    Testing: OperationalStatus = ...
    """"""
    Unknown: OperationalStatus = ...
    """"""
    Dormant: OperationalStatus = ...
    """"""
    NotPresent: OperationalStatus = ...
    """"""
    LowerLayerDown: OperationalStatus = ...
    """"""

class PhysicalAddress(Object):
    """"""

    _None: Final[ClassVar[PhysicalAddress]] = ...
    """
    
    :return: 
    """
    def __init__(self, address: Array[int]):
        """

        :param address:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetAddressBytes(self) -> Array[int]:
        """

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
    def Parse(cls, address: str) -> PhysicalAddress:
        """

        :param address:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class Ping(Component, IComponent, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def Container(self) -> IContainer:
        """

        :return:
        """
    @property
    def Site(self) -> ISite:
        """

        :return:
        """
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
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
    @overload
    def Send(self, address: IPAddress) -> PingReply:
        """

        :param address:
        :return:
        """
    @overload
    def Send(self, hostNameOrAddress: str) -> PingReply:
        """

        :param hostNameOrAddress:
        :return:
        """
    @overload
    def Send(self, address: IPAddress, timeout: int) -> PingReply:
        """

        :param address:
        :param timeout:
        :return:
        """
    @overload
    def Send(self, hostNameOrAddress: str, timeout: int) -> PingReply:
        """

        :param hostNameOrAddress:
        :param timeout:
        :return:
        """
    @overload
    def Send(self, address: IPAddress, timeout: int, buffer: Array[int]) -> PingReply:
        """

        :param address:
        :param timeout:
        :param buffer:
        :return:
        """
    @overload
    def Send(self, hostNameOrAddress: str, timeout: int, buffer: Array[int]) -> PingReply:
        """

        :param hostNameOrAddress:
        :param timeout:
        :param buffer:
        :return:
        """
    @overload
    def Send(
        self, address: IPAddress, timeout: int, buffer: Array[int], options: PingOptions
    ) -> PingReply:
        """

        :param address:
        :param timeout:
        :param buffer:
        :param options:
        :return:
        """
    @overload
    def Send(
        self, hostNameOrAddress: str, timeout: int, buffer: Array[int], options: PingOptions
    ) -> PingReply:
        """

        :param hostNameOrAddress:
        :param timeout:
        :param buffer:
        :param options:
        :return:
        """
    @overload
    def SendAsync(self, address: IPAddress, userToken: object) -> None:
        """

        :param address:
        :param userToken:
        """
    @overload
    def SendAsync(self, hostNameOrAddress: str, userToken: object) -> None:
        """

        :param hostNameOrAddress:
        :param userToken:
        """
    @overload
    def SendAsync(self, address: IPAddress, timeout: int, userToken: object) -> None:
        """

        :param address:
        :param timeout:
        :param userToken:
        """
    @overload
    def SendAsync(self, hostNameOrAddress: str, timeout: int, userToken: object) -> None:
        """

        :param hostNameOrAddress:
        :param timeout:
        :param userToken:
        """
    @overload
    def SendAsync(
        self, address: IPAddress, timeout: int, buffer: Array[int], userToken: object
    ) -> None:
        """

        :param address:
        :param timeout:
        :param buffer:
        :param userToken:
        """
    @overload
    def SendAsync(
        self, hostNameOrAddress: str, timeout: int, buffer: Array[int], userToken: object
    ) -> None:
        """

        :param hostNameOrAddress:
        :param timeout:
        :param buffer:
        :param userToken:
        """
    @overload
    def SendAsync(
        self,
        address: IPAddress,
        timeout: int,
        buffer: Array[int],
        options: PingOptions,
        userToken: object,
    ) -> None:
        """

        :param address:
        :param timeout:
        :param buffer:
        :param options:
        :param userToken:
        """
    @overload
    def SendAsync(
        self,
        hostNameOrAddress: str,
        timeout: int,
        buffer: Array[int],
        options: PingOptions,
        userToken: object,
    ) -> None:
        """

        :param hostNameOrAddress:
        :param timeout:
        :param buffer:
        :param options:
        :param userToken:
        """
    def SendAsyncCancel(self) -> None:
        """"""
    @overload
    def SendPingAsync(self, address: IPAddress) -> Task[PingReply]:
        """

        :param address:
        :return:
        """
    @overload
    def SendPingAsync(self, hostNameOrAddress: str) -> Task[PingReply]:
        """

        :param hostNameOrAddress:
        :return:
        """
    @overload
    def SendPingAsync(self, address: IPAddress, timeout: int) -> Task[PingReply]:
        """

        :param address:
        :param timeout:
        :return:
        """
    @overload
    def SendPingAsync(self, hostNameOrAddress: str, timeout: int) -> Task[PingReply]:
        """

        :param hostNameOrAddress:
        :param timeout:
        :return:
        """
    @overload
    def SendPingAsync(
        self, address: IPAddress, timeout: int, buffer: Array[int]
    ) -> Task[PingReply]:
        """

        :param address:
        :param timeout:
        :param buffer:
        :return:
        """
    @overload
    def SendPingAsync(
        self, hostNameOrAddress: str, timeout: int, buffer: Array[int]
    ) -> Task[PingReply]:
        """

        :param hostNameOrAddress:
        :param timeout:
        :param buffer:
        :return:
        """
    @overload
    def SendPingAsync(
        self, address: IPAddress, timeout: int, buffer: Array[int], options: PingOptions
    ) -> Task[PingReply]:
        """

        :param address:
        :param timeout:
        :param buffer:
        :param options:
        :return:
        """
    @overload
    def SendPingAsync(
        self, hostNameOrAddress: str, timeout: int, buffer: Array[int], options: PingOptions
    ) -> Task[PingReply]:
        """

        :param hostNameOrAddress:
        :param timeout:
        :param buffer:
        :param options:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    Disposed: EventType[EventHandler] = ...
    """"""
    PingCompleted: EventType[PingCompletedEventHandler] = ...
    """"""

class PingCompletedEventArgs(AsyncCompletedEventArgs):
    """"""

    @property
    def Cancelled(self) -> bool:
        """

        :return:
        """
    @property
    def Error(self) -> Exception:
        """

        :return:
        """
    @property
    def Reply(self) -> PingReply:
        """

        :return:
        """
    @property
    def UserState(self) -> object:
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

PingCompletedEventHandler: Callable[[object, PingCompletedEventArgs], None] = ...
"""

:param sender: 
:param e: 
"""

class PingException(InvalidOperationException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self, message: str):
        """

        :param message:
        """
    @overload
    def __init__(self, message: str, innerException: Exception):
        """

        :param message:
        :param innerException:
        """
    @property
    def Data(self) -> IDictionary:
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

class PingOptions(Object):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, ttl: int, dontFragment: bool):
        """

        :param ttl:
        :param dontFragment:
        """
    @property
    def DontFragment(self) -> bool:
        """

        :return:
        """
    @DontFragment.setter
    def DontFragment(self, value: bool) -> None: ...
    @property
    def Ttl(self) -> int:
        """

        :return:
        """
    @Ttl.setter
    def Ttl(self, value: int) -> None: ...
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

class PingReply(Object):
    """"""

    @property
    def Address(self) -> IPAddress:
        """

        :return:
        """
    @property
    def Buffer(self) -> Array[int]:
        """

        :return:
        """
    @property
    def Options(self) -> PingOptions:
        """

        :return:
        """
    @property
    def RoundtripTime(self) -> int:
        """

        :return:
        """
    @property
    def Status(self) -> IPStatus:
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

class PrefixOrigin(Enum):
    """"""

    Other: PrefixOrigin = ...
    """"""
    Manual: PrefixOrigin = ...
    """"""
    WellKnown: PrefixOrigin = ...
    """"""
    Dhcp: PrefixOrigin = ...
    """"""
    RouterAdvertisement: PrefixOrigin = ...
    """"""

class SafeCancelMibChangeNotify(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
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
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class SafeFreeMibTable(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def IsClosed(self) -> bool:
        """

        :return:
        """
    @property
    def IsInvalid(self) -> bool:
        """

        :return:
        """
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: bool) -> None:
        """

        :param success:
        """
    def DangerousGetHandle(self) -> IntPtr:
        """

        :return:
        """
    def DangerousRelease(self) -> None:
        """"""
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
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class ScopeLevel(Enum):
    """"""

    _None: ScopeLevel = ...
    """"""
    Interface: ScopeLevel = ...
    """"""
    Link: ScopeLevel = ...
    """"""
    Subnet: ScopeLevel = ...
    """"""
    Admin: ScopeLevel = ...
    """"""
    Site: ScopeLevel = ...
    """"""
    Organization: ScopeLevel = ...
    """"""
    Global: ScopeLevel = ...
    """"""

StableUnicastIpAddressTableDelegate: Callable[[IntPtr, IntPtr], None] = ...
"""

:param context: 
:param table: 
"""

class StartIPOptions(Enum):
    """"""

    _None: StartIPOptions = ...
    """"""
    StartIPv4: StartIPOptions = ...
    """"""
    StartIPv6: StartIPOptions = ...
    """"""
    Both: StartIPOptions = ...
    """"""

class SuffixOrigin(Enum):
    """"""

    Other: SuffixOrigin = ...
    """"""
    Manual: SuffixOrigin = ...
    """"""
    WellKnown: SuffixOrigin = ...
    """"""
    OriginDhcp: SuffixOrigin = ...
    """"""
    LinkLayerAddress: SuffixOrigin = ...
    """"""
    Random: SuffixOrigin = ...
    """"""

class SystemGatewayIPAddressInformation(GatewayIPAddressInformation):
    """"""

    @property
    def Address(self) -> IPAddress:
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

class SystemIPAddressInformation(IPAddressInformation):
    """"""

    @property
    def Address(self) -> IPAddress:
        """

        :return:
        """
    @property
    def IsDnsEligible(self) -> bool:
        """

        :return:
        """
    @property
    def IsTransient(self) -> bool:
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

class SystemIPGlobalProperties(IPGlobalProperties):
    """"""

    @property
    def DhcpScopeName(self) -> str:
        """

        :return:
        """
    @property
    def DomainName(self) -> str:
        """

        :return:
        """
    @property
    def HostName(self) -> str:
        """

        :return:
        """
    @property
    def IsWinsProxy(self) -> bool:
        """

        :return:
        """
    @property
    def NodeType(self) -> NetBiosNodeType:
        """

        :return:
        """
    def BeginGetUnicastAddresses(self, callback: AsyncCallback, state: object) -> IAsyncResult:
        """

        :param callback:
        :param state:
        :return:
        """
    def EndGetUnicastAddresses(
        self, asyncResult: IAsyncResult
    ) -> UnicastIPAddressInformationCollection:
        """

        :param asyncResult:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetActiveTcpConnections(self) -> Array[TcpConnectionInformation]:
        """

        :return:
        """
    def GetActiveTcpListeners(self) -> Array[IPEndPoint]:
        """

        :return:
        """
    def GetActiveUdpListeners(self) -> Array[IPEndPoint]:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIPv4GlobalStatistics(self) -> IPGlobalStatistics:
        """

        :return:
        """
    def GetIPv6GlobalStatistics(self) -> IPGlobalStatistics:
        """

        :return:
        """
    def GetIcmpV4Statistics(self) -> IcmpV4Statistics:
        """

        :return:
        """
    def GetIcmpV6Statistics(self) -> IcmpV6Statistics:
        """

        :return:
        """
    def GetTcpIPv4Statistics(self) -> TcpStatistics:
        """

        :return:
        """
    def GetTcpIPv6Statistics(self) -> TcpStatistics:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetUdpIPv4Statistics(self) -> UdpStatistics:
        """

        :return:
        """
    def GetUdpIPv6Statistics(self) -> UdpStatistics:
        """

        :return:
        """
    def GetUnicastAddresses(self) -> UnicastIPAddressInformationCollection:
        """

        :return:
        """
    def GetUnicastAddressesAsync(self) -> Task[UnicastIPAddressInformationCollection]:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SystemIPGlobalStatistics(IPGlobalStatistics):
    """"""

    @property
    def DefaultTtl(self) -> int:
        """

        :return:
        """
    @property
    def ForwardingEnabled(self) -> bool:
        """

        :return:
        """
    @property
    def NumberOfIPAddresses(self) -> int:
        """

        :return:
        """
    @property
    def NumberOfInterfaces(self) -> int:
        """

        :return:
        """
    @property
    def NumberOfRoutes(self) -> int:
        """

        :return:
        """
    @property
    def OutputPacketRequests(self) -> int:
        """

        :return:
        """
    @property
    def OutputPacketRoutingDiscards(self) -> int:
        """

        :return:
        """
    @property
    def OutputPacketsDiscarded(self) -> int:
        """

        :return:
        """
    @property
    def OutputPacketsWithNoRoute(self) -> int:
        """

        :return:
        """
    @property
    def PacketFragmentFailures(self) -> int:
        """

        :return:
        """
    @property
    def PacketReassembliesRequired(self) -> int:
        """

        :return:
        """
    @property
    def PacketReassemblyFailures(self) -> int:
        """

        :return:
        """
    @property
    def PacketReassemblyTimeout(self) -> int:
        """

        :return:
        """
    @property
    def PacketsFragmented(self) -> int:
        """

        :return:
        """
    @property
    def PacketsReassembled(self) -> int:
        """

        :return:
        """
    @property
    def ReceivedPackets(self) -> int:
        """

        :return:
        """
    @property
    def ReceivedPacketsDelivered(self) -> int:
        """

        :return:
        """
    @property
    def ReceivedPacketsDiscarded(self) -> int:
        """

        :return:
        """
    @property
    def ReceivedPacketsForwarded(self) -> int:
        """

        :return:
        """
    @property
    def ReceivedPacketsWithAddressErrors(self) -> int:
        """

        :return:
        """
    @property
    def ReceivedPacketsWithHeadersErrors(self) -> int:
        """

        :return:
        """
    @property
    def ReceivedPacketsWithUnknownProtocol(self) -> int:
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

class SystemIPInterfaceProperties(IPInterfaceProperties):
    """"""

    @property
    def AnycastAddresses(self) -> IPAddressInformationCollection:
        """

        :return:
        """
    @property
    def DhcpServerAddresses(self) -> IPAddressCollection:
        """

        :return:
        """
    @property
    def DnsAddresses(self) -> IPAddressCollection:
        """

        :return:
        """
    @property
    def DnsSuffix(self) -> str:
        """

        :return:
        """
    @property
    def GatewayAddresses(self) -> GatewayIPAddressInformationCollection:
        """

        :return:
        """
    @property
    def IsDnsEnabled(self) -> bool:
        """

        :return:
        """
    @property
    def IsDynamicDnsEnabled(self) -> bool:
        """

        :return:
        """
    @property
    def MulticastAddresses(self) -> MulticastIPAddressInformationCollection:
        """

        :return:
        """
    @property
    def UnicastAddresses(self) -> UnicastIPAddressInformationCollection:
        """

        :return:
        """
    @property
    def WinsServersAddresses(self) -> IPAddressCollection:
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
    def GetIPv4Properties(self) -> IPv4InterfaceProperties:
        """

        :return:
        """
    def GetIPv6Properties(self) -> IPv6InterfaceProperties:
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

class SystemIPInterfaceStatistics(IPInterfaceStatistics):
    """"""

    @property
    def BytesReceived(self) -> int:
        """

        :return:
        """
    @property
    def BytesSent(self) -> int:
        """

        :return:
        """
    @property
    def IncomingPacketsDiscarded(self) -> int:
        """

        :return:
        """
    @property
    def IncomingPacketsWithErrors(self) -> int:
        """

        :return:
        """
    @property
    def IncomingUnknownProtocolPackets(self) -> int:
        """

        :return:
        """
    @property
    def NonUnicastPacketsReceived(self) -> int:
        """

        :return:
        """
    @property
    def NonUnicastPacketsSent(self) -> int:
        """

        :return:
        """
    @property
    def OutgoingPacketsDiscarded(self) -> int:
        """

        :return:
        """
    @property
    def OutgoingPacketsWithErrors(self) -> int:
        """

        :return:
        """
    @property
    def OutputQueueLength(self) -> int:
        """

        :return:
        """
    @property
    def UnicastPacketsReceived(self) -> int:
        """

        :return:
        """
    @property
    def UnicastPacketsSent(self) -> int:
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

class SystemIPv4InterfaceProperties(IPv4InterfaceProperties):
    """"""

    @property
    def Index(self) -> int:
        """

        :return:
        """
    @property
    def IsAutomaticPrivateAddressingActive(self) -> bool:
        """

        :return:
        """
    @property
    def IsAutomaticPrivateAddressingEnabled(self) -> bool:
        """

        :return:
        """
    @property
    def IsDhcpEnabled(self) -> bool:
        """

        :return:
        """
    @property
    def IsForwardingEnabled(self) -> bool:
        """

        :return:
        """
    @property
    def Mtu(self) -> int:
        """

        :return:
        """
    @property
    def UsesWins(self) -> bool:
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

class SystemIPv4InterfaceStatistics(IPv4InterfaceStatistics):
    """"""

    @property
    def BytesReceived(self) -> int:
        """

        :return:
        """
    @property
    def BytesSent(self) -> int:
        """

        :return:
        """
    @property
    def IncomingPacketsDiscarded(self) -> int:
        """

        :return:
        """
    @property
    def IncomingPacketsWithErrors(self) -> int:
        """

        :return:
        """
    @property
    def IncomingUnknownProtocolPackets(self) -> int:
        """

        :return:
        """
    @property
    def NonUnicastPacketsReceived(self) -> int:
        """

        :return:
        """
    @property
    def NonUnicastPacketsSent(self) -> int:
        """

        :return:
        """
    @property
    def OutgoingPacketsDiscarded(self) -> int:
        """

        :return:
        """
    @property
    def OutgoingPacketsWithErrors(self) -> int:
        """

        :return:
        """
    @property
    def OutputQueueLength(self) -> int:
        """

        :return:
        """
    @property
    def UnicastPacketsReceived(self) -> int:
        """

        :return:
        """
    @property
    def UnicastPacketsSent(self) -> int:
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

class SystemIPv6InterfaceProperties(IPv6InterfaceProperties):
    """"""

    @property
    def Index(self) -> int:
        """

        :return:
        """
    @property
    def Mtu(self) -> int:
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
    def GetScopeId(self, scopeLevel: ScopeLevel) -> int:
        """

        :param scopeLevel:
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

class SystemIcmpV4Statistics(IcmpV4Statistics):
    """"""

    @property
    def AddressMaskRepliesReceived(self) -> int:
        """

        :return:
        """
    @property
    def AddressMaskRepliesSent(self) -> int:
        """

        :return:
        """
    @property
    def AddressMaskRequestsReceived(self) -> int:
        """

        :return:
        """
    @property
    def AddressMaskRequestsSent(self) -> int:
        """

        :return:
        """
    @property
    def DestinationUnreachableMessagesReceived(self) -> int:
        """

        :return:
        """
    @property
    def DestinationUnreachableMessagesSent(self) -> int:
        """

        :return:
        """
    @property
    def EchoRepliesReceived(self) -> int:
        """

        :return:
        """
    @property
    def EchoRepliesSent(self) -> int:
        """

        :return:
        """
    @property
    def EchoRequestsReceived(self) -> int:
        """

        :return:
        """
    @property
    def EchoRequestsSent(self) -> int:
        """

        :return:
        """
    @property
    def ErrorsReceived(self) -> int:
        """

        :return:
        """
    @property
    def ErrorsSent(self) -> int:
        """

        :return:
        """
    @property
    def MessagesReceived(self) -> int:
        """

        :return:
        """
    @property
    def MessagesSent(self) -> int:
        """

        :return:
        """
    @property
    def ParameterProblemsReceived(self) -> int:
        """

        :return:
        """
    @property
    def ParameterProblemsSent(self) -> int:
        """

        :return:
        """
    @property
    def RedirectsReceived(self) -> int:
        """

        :return:
        """
    @property
    def RedirectsSent(self) -> int:
        """

        :return:
        """
    @property
    def SourceQuenchesReceived(self) -> int:
        """

        :return:
        """
    @property
    def SourceQuenchesSent(self) -> int:
        """

        :return:
        """
    @property
    def TimeExceededMessagesReceived(self) -> int:
        """

        :return:
        """
    @property
    def TimeExceededMessagesSent(self) -> int:
        """

        :return:
        """
    @property
    def TimestampRepliesReceived(self) -> int:
        """

        :return:
        """
    @property
    def TimestampRepliesSent(self) -> int:
        """

        :return:
        """
    @property
    def TimestampRequestsReceived(self) -> int:
        """

        :return:
        """
    @property
    def TimestampRequestsSent(self) -> int:
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

class SystemIcmpV6Statistics(IcmpV6Statistics):
    """"""

    @property
    def DestinationUnreachableMessagesReceived(self) -> int:
        """

        :return:
        """
    @property
    def DestinationUnreachableMessagesSent(self) -> int:
        """

        :return:
        """
    @property
    def EchoRepliesReceived(self) -> int:
        """

        :return:
        """
    @property
    def EchoRepliesSent(self) -> int:
        """

        :return:
        """
    @property
    def EchoRequestsReceived(self) -> int:
        """

        :return:
        """
    @property
    def EchoRequestsSent(self) -> int:
        """

        :return:
        """
    @property
    def ErrorsReceived(self) -> int:
        """

        :return:
        """
    @property
    def ErrorsSent(self) -> int:
        """

        :return:
        """
    @property
    def MembershipQueriesReceived(self) -> int:
        """

        :return:
        """
    @property
    def MembershipQueriesSent(self) -> int:
        """

        :return:
        """
    @property
    def MembershipReductionsReceived(self) -> int:
        """

        :return:
        """
    @property
    def MembershipReductionsSent(self) -> int:
        """

        :return:
        """
    @property
    def MembershipReportsReceived(self) -> int:
        """

        :return:
        """
    @property
    def MembershipReportsSent(self) -> int:
        """

        :return:
        """
    @property
    def MessagesReceived(self) -> int:
        """

        :return:
        """
    @property
    def MessagesSent(self) -> int:
        """

        :return:
        """
    @property
    def NeighborAdvertisementsReceived(self) -> int:
        """

        :return:
        """
    @property
    def NeighborAdvertisementsSent(self) -> int:
        """

        :return:
        """
    @property
    def NeighborSolicitsReceived(self) -> int:
        """

        :return:
        """
    @property
    def NeighborSolicitsSent(self) -> int:
        """

        :return:
        """
    @property
    def PacketTooBigMessagesReceived(self) -> int:
        """

        :return:
        """
    @property
    def PacketTooBigMessagesSent(self) -> int:
        """

        :return:
        """
    @property
    def ParameterProblemsReceived(self) -> int:
        """

        :return:
        """
    @property
    def ParameterProblemsSent(self) -> int:
        """

        :return:
        """
    @property
    def RedirectsReceived(self) -> int:
        """

        :return:
        """
    @property
    def RedirectsSent(self) -> int:
        """

        :return:
        """
    @property
    def RouterAdvertisementsReceived(self) -> int:
        """

        :return:
        """
    @property
    def RouterAdvertisementsSent(self) -> int:
        """

        :return:
        """
    @property
    def RouterSolicitsReceived(self) -> int:
        """

        :return:
        """
    @property
    def RouterSolicitsSent(self) -> int:
        """

        :return:
        """
    @property
    def TimeExceededMessagesReceived(self) -> int:
        """

        :return:
        """
    @property
    def TimeExceededMessagesSent(self) -> int:
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

class SystemMulticastIPAddressInformation(MulticastIPAddressInformation):
    """"""

    def __init__(self, addressInfo: SystemIPAddressInformation):
        """

        :param addressInfo:
        """
    @property
    def Address(self) -> IPAddress:
        """

        :return:
        """
    @property
    def AddressPreferredLifetime(self) -> int:
        """

        :return:
        """
    @property
    def AddressValidLifetime(self) -> int:
        """

        :return:
        """
    @property
    def DhcpLeaseLifetime(self) -> int:
        """

        :return:
        """
    @property
    def DuplicateAddressDetectionState(self) -> DuplicateAddressDetectionState:
        """

        :return:
        """
    @property
    def IsDnsEligible(self) -> bool:
        """

        :return:
        """
    @property
    def IsTransient(self) -> bool:
        """

        :return:
        """
    @property
    def PrefixOrigin(self) -> PrefixOrigin:
        """

        :return:
        """
    @property
    def SuffixOrigin(self) -> SuffixOrigin:
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

class SystemNetworkInterface(NetworkInterface):
    """"""

    @property
    def Description(self) -> str:
        """

        :return:
        """
    @classmethod
    @property
    def IPv6LoopbackInterfaceIndex(cls) -> int:
        """

        :return:
        """
    @property
    def Id(self) -> str:
        """

        :return:
        """
    @property
    def IsReceiveOnly(self) -> bool:
        """

        :return:
        """
    @classmethod
    @property
    def LoopbackInterfaceIndex(cls) -> int:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def NetworkInterfaceType(self) -> NetworkInterfaceType:
        """

        :return:
        """
    @property
    def OperationalStatus(self) -> OperationalStatus:
        """

        :return:
        """
    @property
    def Speed(self) -> int:
        """

        :return:
        """
    @property
    def SupportsMulticast(self) -> bool:
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
    def GetIPProperties(self) -> IPInterfaceProperties:
        """

        :return:
        """
    def GetIPStatistics(self) -> IPInterfaceStatistics:
        """

        :return:
        """
    def GetIPv4Statistics(self) -> IPv4InterfaceStatistics:
        """

        :return:
        """
    def GetPhysicalAddress(self) -> PhysicalAddress:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Supports(self, networkInterfaceComponent: NetworkInterfaceComponent) -> bool:
        """

        :param networkInterfaceComponent:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class SystemTcpConnectionInformation(TcpConnectionInformation):
    """"""

    @property
    def LocalEndPoint(self) -> IPEndPoint:
        """

        :return:
        """
    @property
    def RemoteEndPoint(self) -> IPEndPoint:
        """

        :return:
        """
    @property
    def State(self) -> TcpState:
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

class SystemTcpStatistics(TcpStatistics):
    """"""

    @property
    def ConnectionsAccepted(self) -> int:
        """

        :return:
        """
    @property
    def ConnectionsInitiated(self) -> int:
        """

        :return:
        """
    @property
    def CumulativeConnections(self) -> int:
        """

        :return:
        """
    @property
    def CurrentConnections(self) -> int:
        """

        :return:
        """
    @property
    def ErrorsReceived(self) -> int:
        """

        :return:
        """
    @property
    def FailedConnectionAttempts(self) -> int:
        """

        :return:
        """
    @property
    def MaximumConnections(self) -> int:
        """

        :return:
        """
    @property
    def MaximumTransmissionTimeout(self) -> int:
        """

        :return:
        """
    @property
    def MinimumTransmissionTimeout(self) -> int:
        """

        :return:
        """
    @property
    def ResetConnections(self) -> int:
        """

        :return:
        """
    @property
    def ResetsSent(self) -> int:
        """

        :return:
        """
    @property
    def SegmentsReceived(self) -> int:
        """

        :return:
        """
    @property
    def SegmentsResent(self) -> int:
        """

        :return:
        """
    @property
    def SegmentsSent(self) -> int:
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

class SystemUdpStatistics(UdpStatistics):
    """"""

    @property
    def DatagramsReceived(self) -> int:
        """

        :return:
        """
    @property
    def DatagramsSent(self) -> int:
        """

        :return:
        """
    @property
    def IncomingDatagramsDiscarded(self) -> int:
        """

        :return:
        """
    @property
    def IncomingDatagramsWithErrors(self) -> int:
        """

        :return:
        """
    @property
    def UdpListeners(self) -> int:
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

class SystemUnicastIPAddressInformation(UnicastIPAddressInformation):
    """"""

    @property
    def Address(self) -> IPAddress:
        """

        :return:
        """
    @property
    def AddressPreferredLifetime(self) -> int:
        """

        :return:
        """
    @property
    def AddressValidLifetime(self) -> int:
        """

        :return:
        """
    @property
    def DhcpLeaseLifetime(self) -> int:
        """

        :return:
        """
    @property
    def DuplicateAddressDetectionState(self) -> DuplicateAddressDetectionState:
        """

        :return:
        """
    @property
    def IPv4Mask(self) -> IPAddress:
        """

        :return:
        """
    @property
    def IsDnsEligible(self) -> bool:
        """

        :return:
        """
    @property
    def IsTransient(self) -> bool:
        """

        :return:
        """
    @property
    def PrefixLength(self) -> int:
        """

        :return:
        """
    @property
    def PrefixOrigin(self) -> PrefixOrigin:
        """

        :return:
        """
    @property
    def SuffixOrigin(self) -> SuffixOrigin:
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

class TcpConnectionInformation(ABC, Object):
    """"""

    @property
    def LocalEndPoint(self) -> IPEndPoint:
        """

        :return:
        """
    @property
    def RemoteEndPoint(self) -> IPEndPoint:
        """

        :return:
        """
    @property
    def State(self) -> TcpState:
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

class TcpState(Enum):
    """"""

    Unknown: TcpState = ...
    """"""
    Closed: TcpState = ...
    """"""
    Listen: TcpState = ...
    """"""
    SynSent: TcpState = ...
    """"""
    SynReceived: TcpState = ...
    """"""
    Established: TcpState = ...
    """"""
    FinWait1: TcpState = ...
    """"""
    FinWait2: TcpState = ...
    """"""
    CloseWait: TcpState = ...
    """"""
    Closing: TcpState = ...
    """"""
    LastAck: TcpState = ...
    """"""
    TimeWait: TcpState = ...
    """"""
    DeleteTcb: TcpState = ...
    """"""

class TcpStatistics(ABC, Object):
    """"""

    @property
    def ConnectionsAccepted(self) -> int:
        """

        :return:
        """
    @property
    def ConnectionsInitiated(self) -> int:
        """

        :return:
        """
    @property
    def CumulativeConnections(self) -> int:
        """

        :return:
        """
    @property
    def CurrentConnections(self) -> int:
        """

        :return:
        """
    @property
    def ErrorsReceived(self) -> int:
        """

        :return:
        """
    @property
    def FailedConnectionAttempts(self) -> int:
        """

        :return:
        """
    @property
    def MaximumConnections(self) -> int:
        """

        :return:
        """
    @property
    def MaximumTransmissionTimeout(self) -> int:
        """

        :return:
        """
    @property
    def MinimumTransmissionTimeout(self) -> int:
        """

        :return:
        """
    @property
    def ResetConnections(self) -> int:
        """

        :return:
        """
    @property
    def ResetsSent(self) -> int:
        """

        :return:
        """
    @property
    def SegmentsReceived(self) -> int:
        """

        :return:
        """
    @property
    def SegmentsResent(self) -> int:
        """

        :return:
        """
    @property
    def SegmentsSent(self) -> int:
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

class TcpTableClass(Enum):
    """"""

    TcpTableBasicListener: TcpTableClass = ...
    """"""
    TcpTableBasicConnections: TcpTableClass = ...
    """"""
    TcpTableBasicAll: TcpTableClass = ...
    """"""
    TcpTableOwnerPidListener: TcpTableClass = ...
    """"""
    TcpTableOwnerPidConnections: TcpTableClass = ...
    """"""
    TcpTableOwnerPidAll: TcpTableClass = ...
    """"""
    TcpTableOwnerModuleListener: TcpTableClass = ...
    """"""
    TcpTableOwnerModuleConnections: TcpTableClass = ...
    """"""
    TcpTableOwnerModuleAll: TcpTableClass = ...
    """"""

class TeredoHelper(Object):
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
    @classmethod
    def UnsafeNotifyStableUnicastIpAddressTable(
        cls, callback: Action[object], state: object
    ) -> bool:
        """

        :param callback:
        :param state:
        :return:
        """

class UdpStatistics(ABC, Object):
    """"""

    @property
    def DatagramsReceived(self) -> int:
        """

        :return:
        """
    @property
    def DatagramsSent(self) -> int:
        """

        :return:
        """
    @property
    def IncomingDatagramsDiscarded(self) -> int:
        """

        :return:
        """
    @property
    def IncomingDatagramsWithErrors(self) -> int:
        """

        :return:
        """
    @property
    def UdpListeners(self) -> int:
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

class UdpTableClass(Enum):
    """"""

    UdpTableBasic: UdpTableClass = ...
    """"""
    UdpTableOwnerPid: UdpTableClass = ...
    """"""
    UdpTableOwnerModule: UdpTableClass = ...
    """"""

class UnicastIPAddressInformation(ABC, IPAddressInformation):
    """"""

    @property
    def Address(self) -> IPAddress:
        """

        :return:
        """
    @property
    def AddressPreferredLifetime(self) -> int:
        """

        :return:
        """
    @property
    def AddressValidLifetime(self) -> int:
        """

        :return:
        """
    @property
    def DhcpLeaseLifetime(self) -> int:
        """

        :return:
        """
    @property
    def DuplicateAddressDetectionState(self) -> DuplicateAddressDetectionState:
        """

        :return:
        """
    @property
    def IPv4Mask(self) -> IPAddress:
        """

        :return:
        """
    @property
    def IsDnsEligible(self) -> bool:
        """

        :return:
        """
    @property
    def IsTransient(self) -> bool:
        """

        :return:
        """
    @property
    def PrefixLength(self) -> int:
        """

        :return:
        """
    @property
    def PrefixOrigin(self) -> PrefixOrigin:
        """

        :return:
        """
    @property
    def SuffixOrigin(self) -> SuffixOrigin:
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

class UnicastIPAddressInformationCollection(
    Object,
    ICollection[UnicastIPAddressInformation],
    IEnumerable[UnicastIPAddressInformation],
    IEnumerable,
):
    """"""

    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> UnicastIPAddressInformation:
        """

        :return:
        """
    def Add(self, item: UnicastIPAddressInformation) -> None:
        """

        :param item:
        """
    def Clear(self) -> None:
        """"""
    def Contains(self, item: UnicastIPAddressInformation) -> bool:
        """

        :param item:
        :return:
        """
    def CopyTo(self, array: Array[UnicastIPAddressInformation], arrayIndex: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

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
    def Remove(self, item: UnicastIPAddressInformation) -> bool:
        """

        :param item:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: UnicastIPAddressInformation) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> UnicastIPAddressInformation:
        """

        :param index:
        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[UnicastIPAddressInformation]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

class UnsafeNetInfoNativeMethods(ABC, Object):
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
