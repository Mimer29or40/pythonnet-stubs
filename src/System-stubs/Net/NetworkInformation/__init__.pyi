"""Automatically generated stubs for C# namespace: System.Net.NetworkInformation."""

from abc import ABC
from collections.abc import Callable
from collections.abc import Iterator
from typing import ClassVar
from typing import Self
from typing import overload

from Microsoft.Win32.SafeHandles import SafeHandleZeroOrMinusOneIsInvalid
from System import Action
from System import Array
from System import AsyncCallback
from System import Boolean
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
from System import UInt32
from System import ValueType
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System.Collections.Generic import ICollection
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IEnumerator
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

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

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
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class FixedInfo(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class GatewayIPAddressInformation(ABC, Object):
    """"""
    @property
    def Address(self) -> IPAddress:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class GatewayIPAddressInformationCollection(
    Object,
    ICollection[GatewayIPAddressInformation],
    IEnumerable[GatewayIPAddressInformation],
    IEnumerable,
):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def Item(self) -> GatewayIPAddressInformation:
        """"""
    def Add(self, address: GatewayIPAddressInformation) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains(self, address: GatewayIPAddressInformation) -> bool:
        """"""
    def CopyTo(self, array: Array[GatewayIPAddressInformation], offset: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[GatewayIPAddressInformation]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove(self, address: GatewayIPAddressInformation) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, address: GatewayIPAddressInformation) -> bool:
        """"""
    def __iter__(self) -> Iterator[GatewayIPAddressInformation]:
        """"""
    def __delitem__(self, address: GatewayIPAddressInformation) -> bool:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> GatewayIPAddressInformation:
        """"""

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
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def Item(self) -> IPAddress:
        """"""
    def Add(self, address: IPAddress) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains(self, address: IPAddress) -> bool:
        """"""
    def CopyTo(self, array: Array[IPAddress], offset: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[IPAddress]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove(self, address: IPAddress) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, address: IPAddress) -> bool:
        """"""
    def __iter__(self) -> Iterator[IPAddress]:
        """"""
    def __delitem__(self, address: IPAddress) -> bool:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> IPAddress:
        """"""

class IPAddressInformation(ABC, Object):
    """"""
    @property
    def Address(self) -> IPAddress:
        """"""
    @property
    def IsDnsEligible(self) -> bool:
        """"""
    @property
    def IsTransient(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IPAddressInformationCollection(
    Object, ICollection[IPAddressInformation], IEnumerable[IPAddressInformation], IEnumerable
):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def Item(self) -> IPAddressInformation:
        """"""
    def Add(self, address: IPAddressInformation) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains(self, address: IPAddressInformation) -> bool:
        """"""
    def CopyTo(self, array: Array[IPAddressInformation], offset: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[IPAddressInformation]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove(self, address: IPAddressInformation) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, address: IPAddressInformation) -> bool:
        """"""
    def __iter__(self) -> Iterator[IPAddressInformation]:
        """"""
    def __delitem__(self, address: IPAddressInformation) -> bool:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> IPAddressInformation:
        """"""

class IPGlobalProperties(ABC, Object):
    """"""
    @property
    def DhcpScopeName(self) -> str:
        """"""
    @property
    def DomainName(self) -> str:
        """"""
    @property
    def HostName(self) -> str:
        """"""
    @property
    def IsWinsProxy(self) -> bool:
        """"""
    @property
    def NodeType(self) -> NetBiosNodeType:
        """"""
    def BeginGetUnicastAddresses(self, callback: AsyncCallback, state: object) -> IAsyncResult:
        """"""
    def EndGetUnicastAddresses(
        self, asyncResult: IAsyncResult
    ) -> UnicastIPAddressInformationCollection:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetActiveTcpConnections(self) -> Array[TcpConnectionInformation]:
        """"""
    def GetActiveTcpListeners(self) -> Array[IPEndPoint]:
        """"""
    def GetActiveUdpListeners(self) -> Array[IPEndPoint]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetIPGlobalProperties(cls) -> IPGlobalProperties:
        """"""
    def GetIPv4GlobalStatistics(self) -> IPGlobalStatistics:
        """"""
    def GetIPv6GlobalStatistics(self) -> IPGlobalStatistics:
        """"""
    def GetIcmpV4Statistics(self) -> IcmpV4Statistics:
        """"""
    def GetIcmpV6Statistics(self) -> IcmpV6Statistics:
        """"""
    def GetTcpIPv4Statistics(self) -> TcpStatistics:
        """"""
    def GetTcpIPv6Statistics(self) -> TcpStatistics:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetUdpIPv4Statistics(self) -> UdpStatistics:
        """"""
    def GetUdpIPv6Statistics(self) -> UdpStatistics:
        """"""
    def GetUnicastAddresses(self) -> UnicastIPAddressInformationCollection:
        """"""
    def GetUnicastAddressesAsync(self) -> Task[UnicastIPAddressInformationCollection]:
        """"""
    def ToString(self) -> str:
        """"""

class IPGlobalStatistics(ABC, Object):
    """"""
    @property
    def DefaultTtl(self) -> int:
        """"""
    @property
    def ForwardingEnabled(self) -> bool:
        """"""
    @property
    def NumberOfIPAddresses(self) -> int:
        """"""
    @property
    def NumberOfInterfaces(self) -> int:
        """"""
    @property
    def NumberOfRoutes(self) -> int:
        """"""
    @property
    def OutputPacketRequests(self) -> int:
        """"""
    @property
    def OutputPacketRoutingDiscards(self) -> int:
        """"""
    @property
    def OutputPacketsDiscarded(self) -> int:
        """"""
    @property
    def OutputPacketsWithNoRoute(self) -> int:
        """"""
    @property
    def PacketFragmentFailures(self) -> int:
        """"""
    @property
    def PacketReassembliesRequired(self) -> int:
        """"""
    @property
    def PacketReassemblyFailures(self) -> int:
        """"""
    @property
    def PacketReassemblyTimeout(self) -> int:
        """"""
    @property
    def PacketsFragmented(self) -> int:
        """"""
    @property
    def PacketsReassembled(self) -> int:
        """"""
    @property
    def ReceivedPackets(self) -> int:
        """"""
    @property
    def ReceivedPacketsDelivered(self) -> int:
        """"""
    @property
    def ReceivedPacketsDiscarded(self) -> int:
        """"""
    @property
    def ReceivedPacketsForwarded(self) -> int:
        """"""
    @property
    def ReceivedPacketsWithAddressErrors(self) -> int:
        """"""
    @property
    def ReceivedPacketsWithHeadersErrors(self) -> int:
        """"""
    @property
    def ReceivedPacketsWithUnknownProtocol(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IPInterfaceProperties(ABC, Object):
    """"""
    @property
    def AnycastAddresses(self) -> IPAddressInformationCollection:
        """"""
    @property
    def DhcpServerAddresses(self) -> IPAddressCollection:
        """"""
    @property
    def DnsAddresses(self) -> IPAddressCollection:
        """"""
    @property
    def DnsSuffix(self) -> str:
        """"""
    @property
    def GatewayAddresses(self) -> GatewayIPAddressInformationCollection:
        """"""
    @property
    def IsDnsEnabled(self) -> bool:
        """"""
    @property
    def IsDynamicDnsEnabled(self) -> bool:
        """"""
    @property
    def MulticastAddresses(self) -> MulticastIPAddressInformationCollection:
        """"""
    @property
    def UnicastAddresses(self) -> UnicastIPAddressInformationCollection:
        """"""
    @property
    def WinsServersAddresses(self) -> IPAddressCollection:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIPv4Properties(self) -> IPv4InterfaceProperties:
        """"""
    def GetIPv6Properties(self) -> IPv6InterfaceProperties:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IPInterfaceStatistics(ABC, Object):
    """"""
    @property
    def BytesReceived(self) -> int:
        """"""
    @property
    def BytesSent(self) -> int:
        """"""
    @property
    def IncomingPacketsDiscarded(self) -> int:
        """"""
    @property
    def IncomingPacketsWithErrors(self) -> int:
        """"""
    @property
    def IncomingUnknownProtocolPackets(self) -> int:
        """"""
    @property
    def NonUnicastPacketsReceived(self) -> int:
        """"""
    @property
    def NonUnicastPacketsSent(self) -> int:
        """"""
    @property
    def OutgoingPacketsDiscarded(self) -> int:
        """"""
    @property
    def OutgoingPacketsWithErrors(self) -> int:
        """"""
    @property
    def OutputQueueLength(self) -> int:
        """"""
    @property
    def UnicastPacketsReceived(self) -> int:
        """"""
    @property
    def UnicastPacketsSent(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IPOptions(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

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
        """"""
    @property
    def IsAutomaticPrivateAddressingActive(self) -> bool:
        """"""
    @property
    def IsAutomaticPrivateAddressingEnabled(self) -> bool:
        """"""
    @property
    def IsDhcpEnabled(self) -> bool:
        """"""
    @property
    def IsForwardingEnabled(self) -> bool:
        """"""
    @property
    def Mtu(self) -> int:
        """"""
    @property
    def UsesWins(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IPv4InterfaceStatistics(ABC, Object):
    """"""
    @property
    def BytesReceived(self) -> int:
        """"""
    @property
    def BytesSent(self) -> int:
        """"""
    @property
    def IncomingPacketsDiscarded(self) -> int:
        """"""
    @property
    def IncomingPacketsWithErrors(self) -> int:
        """"""
    @property
    def IncomingUnknownProtocolPackets(self) -> int:
        """"""
    @property
    def NonUnicastPacketsReceived(self) -> int:
        """"""
    @property
    def NonUnicastPacketsSent(self) -> int:
        """"""
    @property
    def OutgoingPacketsDiscarded(self) -> int:
        """"""
    @property
    def OutgoingPacketsWithErrors(self) -> int:
        """"""
    @property
    def OutputQueueLength(self) -> int:
        """"""
    @property
    def UnicastPacketsReceived(self) -> int:
        """"""
    @property
    def UnicastPacketsSent(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IPv6InterfaceProperties(ABC, Object):
    """"""
    @property
    def Index(self) -> int:
        """"""
    @property
    def Mtu(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetScopeId(self, scopeLevel: ScopeLevel) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Icmp6EchoReply(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IcmpEchoReply(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

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
        """"""
    @property
    def AddressMaskRepliesSent(self) -> int:
        """"""
    @property
    def AddressMaskRequestsReceived(self) -> int:
        """"""
    @property
    def AddressMaskRequestsSent(self) -> int:
        """"""
    @property
    def DestinationUnreachableMessagesReceived(self) -> int:
        """"""
    @property
    def DestinationUnreachableMessagesSent(self) -> int:
        """"""
    @property
    def EchoRepliesReceived(self) -> int:
        """"""
    @property
    def EchoRepliesSent(self) -> int:
        """"""
    @property
    def EchoRequestsReceived(self) -> int:
        """"""
    @property
    def EchoRequestsSent(self) -> int:
        """"""
    @property
    def ErrorsReceived(self) -> int:
        """"""
    @property
    def ErrorsSent(self) -> int:
        """"""
    @property
    def MessagesReceived(self) -> int:
        """"""
    @property
    def MessagesSent(self) -> int:
        """"""
    @property
    def ParameterProblemsReceived(self) -> int:
        """"""
    @property
    def ParameterProblemsSent(self) -> int:
        """"""
    @property
    def RedirectsReceived(self) -> int:
        """"""
    @property
    def RedirectsSent(self) -> int:
        """"""
    @property
    def SourceQuenchesReceived(self) -> int:
        """"""
    @property
    def SourceQuenchesSent(self) -> int:
        """"""
    @property
    def TimeExceededMessagesReceived(self) -> int:
        """"""
    @property
    def TimeExceededMessagesSent(self) -> int:
        """"""
    @property
    def TimestampRepliesReceived(self) -> int:
        """"""
    @property
    def TimestampRepliesSent(self) -> int:
        """"""
    @property
    def TimestampRequestsReceived(self) -> int:
        """"""
    @property
    def TimestampRequestsSent(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

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
        """"""
    @property
    def DestinationUnreachableMessagesSent(self) -> int:
        """"""
    @property
    def EchoRepliesReceived(self) -> int:
        """"""
    @property
    def EchoRepliesSent(self) -> int:
        """"""
    @property
    def EchoRequestsReceived(self) -> int:
        """"""
    @property
    def EchoRequestsSent(self) -> int:
        """"""
    @property
    def ErrorsReceived(self) -> int:
        """"""
    @property
    def ErrorsSent(self) -> int:
        """"""
    @property
    def MembershipQueriesReceived(self) -> int:
        """"""
    @property
    def MembershipQueriesSent(self) -> int:
        """"""
    @property
    def MembershipReductionsReceived(self) -> int:
        """"""
    @property
    def MembershipReductionsSent(self) -> int:
        """"""
    @property
    def MembershipReportsReceived(self) -> int:
        """"""
    @property
    def MembershipReportsSent(self) -> int:
        """"""
    @property
    def MessagesReceived(self) -> int:
        """"""
    @property
    def MessagesSent(self) -> int:
        """"""
    @property
    def NeighborAdvertisementsReceived(self) -> int:
        """"""
    @property
    def NeighborAdvertisementsSent(self) -> int:
        """"""
    @property
    def NeighborSolicitsReceived(self) -> int:
        """"""
    @property
    def NeighborSolicitsSent(self) -> int:
        """"""
    @property
    def PacketTooBigMessagesReceived(self) -> int:
        """"""
    @property
    def PacketTooBigMessagesSent(self) -> int:
        """"""
    @property
    def ParameterProblemsReceived(self) -> int:
        """"""
    @property
    def ParameterProblemsSent(self) -> int:
        """"""
    @property
    def RedirectsReceived(self) -> int:
        """"""
    @property
    def RedirectsSent(self) -> int:
        """"""
    @property
    def RouterAdvertisementsReceived(self) -> int:
        """"""
    @property
    def RouterAdvertisementsSent(self) -> int:
        """"""
    @property
    def RouterSolicitsReceived(self) -> int:
        """"""
    @property
    def RouterSolicitsSent(self) -> int:
        """"""
    @property
    def TimeExceededMessagesReceived(self) -> int:
        """"""
    @property
    def TimeExceededMessagesSent(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

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
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IpAdapterAddresses(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IpAdapterUnicastAddress(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IpAddrString(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IpHelperErrors(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IpPerAdapterInfo(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IpSocketAddress(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Ipv6Address(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MibIcmpInfo(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MibIcmpInfoEx(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MibIcmpStats(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MibIcmpStatsEx(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MibIfRow2(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MibIpStats(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MibTcp6RowOwnerPid(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MibTcp6TableOwnerPid(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MibTcpRow(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MibTcpStats(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MibTcpTable(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MibUdp6RowOwnerPid(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MibUdp6TableOwnerPid(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MibUdpRow(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MibUdpStats(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MibUdpTable(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MulticastIPAddressInformation(ABC, IPAddressInformation):
    """"""
    @property
    def Address(self) -> IPAddress:
        """"""
    @property
    def AddressPreferredLifetime(self) -> int:
        """"""
    @property
    def AddressValidLifetime(self) -> int:
        """"""
    @property
    def DhcpLeaseLifetime(self) -> int:
        """"""
    @property
    def DuplicateAddressDetectionState(self) -> DuplicateAddressDetectionState:
        """"""
    @property
    def IsDnsEligible(self) -> bool:
        """"""
    @property
    def IsTransient(self) -> bool:
        """"""
    @property
    def PrefixOrigin(self) -> PrefixOrigin:
        """"""
    @property
    def SuffixOrigin(self) -> SuffixOrigin:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MulticastIPAddressInformationCollection(
    Object,
    ICollection[MulticastIPAddressInformation],
    IEnumerable[MulticastIPAddressInformation],
    IEnumerable,
):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def Item(self) -> MulticastIPAddressInformation:
        """"""
    def Add(self, address: MulticastIPAddressInformation) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains(self, address: MulticastIPAddressInformation) -> bool:
        """"""
    def CopyTo(self, array: Array[MulticastIPAddressInformation], offset: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[MulticastIPAddressInformation]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove(self, address: MulticastIPAddressInformation) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, address: MulticastIPAddressInformation) -> bool:
        """"""
    def __iter__(self) -> Iterator[MulticastIPAddressInformation]:
        """"""
    def __delitem__(self, address: MulticastIPAddressInformation) -> bool:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> MulticastIPAddressInformation:
        """"""

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
""""""
NetworkAvailabilityChangedEventHandler: Callable[[object, NetworkAvailabilityEventArgs], None] = ...
""""""

class NetworkAvailabilityEventArgs(EventArgs):
    """"""
    @property
    def IsAvailable(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class NetworkChange(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def RegisterNetworkChange(cls, nc: NetworkChange) -> None:
        """"""
    def ToString(self) -> str:
        """"""
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

class NetworkInformationPermission(
    CodeAccessPermission, IUnrestrictedPermission, IPermission, ISecurityEncodable, IStackWalk
):
    """"""
    @overload
    def __init__(self, state: PermissionState) -> None:
        """"""
    @overload
    def __init__(self, access: NetworkInformationAccess) -> None:
        """"""
    @property
    def Access(self) -> NetworkInformationAccess:
        """"""
    def AddPermission(self, access: NetworkInformationAccess) -> None:
        """"""
    def Assert(self) -> None:
        """"""
    def Copy(self) -> IPermission:
        """"""
    def Demand(self) -> None:
        """"""
    def Deny(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FromXml(self, securityElement: SecurityElement) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Intersect(self, target: IPermission) -> IPermission:
        """"""
    def IsSubsetOf(self, target: IPermission) -> bool:
        """"""
    def IsUnrestricted(self) -> bool:
        """"""
    def PermitOnly(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXml(self) -> SecurityElement:
        """"""
    def Union(self, target: IPermission) -> IPermission:
        """"""

class NetworkInformationPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    """"""
    def __init__(self, action: SecurityAction) -> None:
        """"""
    @property
    def Access(self) -> str:
        """"""
    @Access.setter
    def Access(self, value: str) -> None: ...
    @property
    def Action(self) -> SecurityAction:
        """"""
    @Action.setter
    def Action(self, value: SecurityAction) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Unrestricted(self) -> bool:
        """"""
    @Unrestricted.setter
    def Unrestricted(self, value: bool) -> None: ...
    def CreatePermission(self) -> IPermission:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
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
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class NetworkInterface(ABC, Object):
    """"""
    @property
    def Description(self) -> str:
        """"""
    @classmethod
    @property
    def IPv6LoopbackInterfaceIndex(cls) -> int:
        """"""
    @property
    def Id(self) -> str:
        """"""
    @property
    def IsReceiveOnly(self) -> bool:
        """"""
    @classmethod
    @property
    def LoopbackInterfaceIndex(cls) -> int:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def NetworkInterfaceType(self) -> NetworkInterfaceType:
        """"""
    @property
    def OperationalStatus(self) -> OperationalStatus:
        """"""
    @property
    def Speed(self) -> int:
        """"""
    @property
    def SupportsMulticast(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetAllNetworkInterfaces(cls) -> Array[NetworkInterface]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIPProperties(self) -> IPInterfaceProperties:
        """"""
    def GetIPStatistics(self) -> IPInterfaceStatistics:
        """"""
    def GetIPv4Statistics(self) -> IPv4InterfaceStatistics:
        """"""
    @classmethod
    def GetIsNetworkAvailable(cls) -> bool:
        """"""
    def GetPhysicalAddress(self) -> PhysicalAddress:
        """"""
    def GetType(self) -> Type:
        """"""
    def Supports(self, networkInterfaceComponent: NetworkInterfaceComponent) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

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

    _None: ClassVar[PhysicalAddress]
    """"""
    def __init__(self, address: Array[int]) -> None:
        """"""
    def Equals(self, comparand: object) -> bool:
        """"""
    def GetAddressBytes(self) -> Array[int]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Parse(cls, address: str) -> PhysicalAddress:
        """"""
    def ToString(self) -> str:
        """"""

class Ping(Component, IComponent, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Container(self) -> IContainer:
        """"""
    @property
    def Site(self) -> ISite:
        """"""
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    @overload
    def Send(self, address: IPAddress) -> PingReply:
        """"""
    @overload
    def Send(self, address: IPAddress, timeout: int) -> PingReply:
        """"""
    @overload
    def Send(self, address: IPAddress, timeout: int, buffer: Array[int]) -> PingReply:
        """"""
    @overload
    def Send(
        self, address: IPAddress, timeout: int, buffer: Array[int], options: PingOptions
    ) -> PingReply:
        """"""
    @overload
    def Send(self, hostNameOrAddress: str) -> PingReply:
        """"""
    @overload
    def Send(self, hostNameOrAddress: str, timeout: int) -> PingReply:
        """"""
    @overload
    def Send(self, hostNameOrAddress: str, timeout: int, buffer: Array[int]) -> PingReply:
        """"""
    @overload
    def Send(
        self, hostNameOrAddress: str, timeout: int, buffer: Array[int], options: PingOptions
    ) -> PingReply:
        """"""
    @overload
    def SendAsync(
        self,
        address: IPAddress,
        timeout: int,
        buffer: Array[int],
        options: PingOptions,
        userToken: object,
    ) -> None:
        """"""
    @overload
    def SendAsync(
        self, address: IPAddress, timeout: int, buffer: Array[int], userToken: object
    ) -> None:
        """"""
    @overload
    def SendAsync(self, address: IPAddress, timeout: int, userToken: object) -> None:
        """"""
    @overload
    def SendAsync(self, address: IPAddress, userToken: object) -> None:
        """"""
    @overload
    def SendAsync(
        self,
        hostNameOrAddress: str,
        timeout: int,
        buffer: Array[int],
        options: PingOptions,
        userToken: object,
    ) -> None:
        """"""
    @overload
    def SendAsync(
        self, hostNameOrAddress: str, timeout: int, buffer: Array[int], userToken: object
    ) -> None:
        """"""
    @overload
    def SendAsync(self, hostNameOrAddress: str, timeout: int, userToken: object) -> None:
        """"""
    @overload
    def SendAsync(self, hostNameOrAddress: str, userToken: object) -> None:
        """"""
    def SendAsyncCancel(self) -> None:
        """"""
    @overload
    def SendPingAsync(self, address: IPAddress) -> Task[PingReply]:
        """"""
    @overload
    def SendPingAsync(self, address: IPAddress, timeout: int) -> Task[PingReply]:
        """"""
    @overload
    def SendPingAsync(
        self, address: IPAddress, timeout: int, buffer: Array[int]
    ) -> Task[PingReply]:
        """"""
    @overload
    def SendPingAsync(
        self, address: IPAddress, timeout: int, buffer: Array[int], options: PingOptions
    ) -> Task[PingReply]:
        """"""
    @overload
    def SendPingAsync(self, hostNameOrAddress: str) -> Task[PingReply]:
        """"""
    @overload
    def SendPingAsync(self, hostNameOrAddress: str, timeout: int) -> Task[PingReply]:
        """"""
    @overload
    def SendPingAsync(
        self, hostNameOrAddress: str, timeout: int, buffer: Array[int]
    ) -> Task[PingReply]:
        """"""
    @overload
    def SendPingAsync(
        self, hostNameOrAddress: str, timeout: int, buffer: Array[int], options: PingOptions
    ) -> Task[PingReply]:
        """"""
    def ToString(self) -> str:
        """"""
    Disposed: EventType[EventHandler] = ...
    """"""
    PingCompleted: EventType[PingCompletedEventHandler] = ...
    """"""

class PingCompletedEventArgs(AsyncCompletedEventArgs):
    """"""
    @property
    def Cancelled(self) -> bool:
        """"""
    @property
    def Error(self) -> Exception:
        """"""
    @property
    def Reply(self) -> PingReply:
        """"""
    @property
    def UserState(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

PingCompletedEventHandler: Callable[[object, PingCompletedEventArgs], None] = ...
""""""

class PingException(InvalidOperationException, _Exception, ISerializable):
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

class PingOptions(Object):
    """"""
    @overload
    def __init__(self, ttl: int, dontFragment: bool) -> None:
        """"""
    @overload
    def __init__(self) -> None:
        """"""
    @property
    def DontFragment(self) -> bool:
        """"""
    @DontFragment.setter
    def DontFragment(self, value: bool) -> None: ...
    @property
    def Ttl(self) -> int:
        """"""
    @Ttl.setter
    def Ttl(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class PingReply(Object):
    """"""
    @property
    def Address(self) -> IPAddress:
        """"""
    @property
    def Buffer(self) -> Array[int]:
        """"""
    @property
    def Options(self) -> PingOptions:
        """"""
    @property
    def RoundtripTime(self) -> int:
        """"""
    @property
    def Status(self) -> IPStatus:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

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
    def __init__(self) -> None:
        """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SafeFreeMibTable(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

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
""""""

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
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SystemIPAddressInformation(IPAddressInformation):
    """"""
    @property
    def Address(self) -> IPAddress:
        """"""
    @property
    def IsDnsEligible(self) -> bool:
        """"""
    @property
    def IsTransient(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SystemIPGlobalProperties(IPGlobalProperties):
    """"""
    @property
    def DhcpScopeName(self) -> str:
        """"""
    @property
    def DomainName(self) -> str:
        """"""
    @property
    def HostName(self) -> str:
        """"""
    @property
    def IsWinsProxy(self) -> bool:
        """"""
    @property
    def NodeType(self) -> NetBiosNodeType:
        """"""
    def BeginGetUnicastAddresses(self, callback: AsyncCallback, state: object) -> IAsyncResult:
        """"""
    def EndGetUnicastAddresses(
        self, asyncResult: IAsyncResult
    ) -> UnicastIPAddressInformationCollection:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetActiveTcpConnections(self) -> Array[TcpConnectionInformation]:
        """"""
    def GetActiveTcpListeners(self) -> Array[IPEndPoint]:
        """"""
    def GetActiveUdpListeners(self) -> Array[IPEndPoint]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIPv4GlobalStatistics(self) -> IPGlobalStatistics:
        """"""
    def GetIPv6GlobalStatistics(self) -> IPGlobalStatistics:
        """"""
    def GetIcmpV4Statistics(self) -> IcmpV4Statistics:
        """"""
    def GetIcmpV6Statistics(self) -> IcmpV6Statistics:
        """"""
    def GetTcpIPv4Statistics(self) -> TcpStatistics:
        """"""
    def GetTcpIPv6Statistics(self) -> TcpStatistics:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetUdpIPv4Statistics(self) -> UdpStatistics:
        """"""
    def GetUdpIPv6Statistics(self) -> UdpStatistics:
        """"""
    def GetUnicastAddresses(self) -> UnicastIPAddressInformationCollection:
        """"""
    def GetUnicastAddressesAsync(self) -> Task[UnicastIPAddressInformationCollection]:
        """"""
    def ToString(self) -> str:
        """"""

class SystemIPGlobalStatistics(IPGlobalStatistics):
    """"""
    @property
    def DefaultTtl(self) -> int:
        """"""
    @property
    def ForwardingEnabled(self) -> bool:
        """"""
    @property
    def NumberOfIPAddresses(self) -> int:
        """"""
    @property
    def NumberOfInterfaces(self) -> int:
        """"""
    @property
    def NumberOfRoutes(self) -> int:
        """"""
    @property
    def OutputPacketRequests(self) -> int:
        """"""
    @property
    def OutputPacketRoutingDiscards(self) -> int:
        """"""
    @property
    def OutputPacketsDiscarded(self) -> int:
        """"""
    @property
    def OutputPacketsWithNoRoute(self) -> int:
        """"""
    @property
    def PacketFragmentFailures(self) -> int:
        """"""
    @property
    def PacketReassembliesRequired(self) -> int:
        """"""
    @property
    def PacketReassemblyFailures(self) -> int:
        """"""
    @property
    def PacketReassemblyTimeout(self) -> int:
        """"""
    @property
    def PacketsFragmented(self) -> int:
        """"""
    @property
    def PacketsReassembled(self) -> int:
        """"""
    @property
    def ReceivedPackets(self) -> int:
        """"""
    @property
    def ReceivedPacketsDelivered(self) -> int:
        """"""
    @property
    def ReceivedPacketsDiscarded(self) -> int:
        """"""
    @property
    def ReceivedPacketsForwarded(self) -> int:
        """"""
    @property
    def ReceivedPacketsWithAddressErrors(self) -> int:
        """"""
    @property
    def ReceivedPacketsWithHeadersErrors(self) -> int:
        """"""
    @property
    def ReceivedPacketsWithUnknownProtocol(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SystemIPInterfaceProperties(IPInterfaceProperties):
    """"""
    @property
    def AnycastAddresses(self) -> IPAddressInformationCollection:
        """"""
    @property
    def DhcpServerAddresses(self) -> IPAddressCollection:
        """"""
    @property
    def DnsAddresses(self) -> IPAddressCollection:
        """"""
    @property
    def DnsSuffix(self) -> str:
        """"""
    @property
    def GatewayAddresses(self) -> GatewayIPAddressInformationCollection:
        """"""
    @property
    def IsDnsEnabled(self) -> bool:
        """"""
    @property
    def IsDynamicDnsEnabled(self) -> bool:
        """"""
    @property
    def MulticastAddresses(self) -> MulticastIPAddressInformationCollection:
        """"""
    @property
    def UnicastAddresses(self) -> UnicastIPAddressInformationCollection:
        """"""
    @property
    def WinsServersAddresses(self) -> IPAddressCollection:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIPv4Properties(self) -> IPv4InterfaceProperties:
        """"""
    def GetIPv6Properties(self) -> IPv6InterfaceProperties:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SystemIPInterfaceStatistics(IPInterfaceStatistics):
    """"""
    @property
    def BytesReceived(self) -> int:
        """"""
    @property
    def BytesSent(self) -> int:
        """"""
    @property
    def IncomingPacketsDiscarded(self) -> int:
        """"""
    @property
    def IncomingPacketsWithErrors(self) -> int:
        """"""
    @property
    def IncomingUnknownProtocolPackets(self) -> int:
        """"""
    @property
    def NonUnicastPacketsReceived(self) -> int:
        """"""
    @property
    def NonUnicastPacketsSent(self) -> int:
        """"""
    @property
    def OutgoingPacketsDiscarded(self) -> int:
        """"""
    @property
    def OutgoingPacketsWithErrors(self) -> int:
        """"""
    @property
    def OutputQueueLength(self) -> int:
        """"""
    @property
    def UnicastPacketsReceived(self) -> int:
        """"""
    @property
    def UnicastPacketsSent(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SystemIPv4InterfaceProperties(IPv4InterfaceProperties):
    """"""
    @property
    def Index(self) -> int:
        """"""
    @property
    def IsAutomaticPrivateAddressingActive(self) -> bool:
        """"""
    @property
    def IsAutomaticPrivateAddressingEnabled(self) -> bool:
        """"""
    @property
    def IsDhcpEnabled(self) -> bool:
        """"""
    @property
    def IsForwardingEnabled(self) -> bool:
        """"""
    @property
    def Mtu(self) -> int:
        """"""
    @property
    def UsesWins(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SystemIPv4InterfaceStatistics(IPv4InterfaceStatistics):
    """"""
    @property
    def BytesReceived(self) -> int:
        """"""
    @property
    def BytesSent(self) -> int:
        """"""
    @property
    def IncomingPacketsDiscarded(self) -> int:
        """"""
    @property
    def IncomingPacketsWithErrors(self) -> int:
        """"""
    @property
    def IncomingUnknownProtocolPackets(self) -> int:
        """"""
    @property
    def NonUnicastPacketsReceived(self) -> int:
        """"""
    @property
    def NonUnicastPacketsSent(self) -> int:
        """"""
    @property
    def OutgoingPacketsDiscarded(self) -> int:
        """"""
    @property
    def OutgoingPacketsWithErrors(self) -> int:
        """"""
    @property
    def OutputQueueLength(self) -> int:
        """"""
    @property
    def UnicastPacketsReceived(self) -> int:
        """"""
    @property
    def UnicastPacketsSent(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SystemIPv6InterfaceProperties(IPv6InterfaceProperties):
    """"""
    @property
    def Index(self) -> int:
        """"""
    @property
    def Mtu(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetScopeId(self, scopeLevel: ScopeLevel) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SystemIcmpV4Statistics(IcmpV4Statistics):
    """"""
    @property
    def AddressMaskRepliesReceived(self) -> int:
        """"""
    @property
    def AddressMaskRepliesSent(self) -> int:
        """"""
    @property
    def AddressMaskRequestsReceived(self) -> int:
        """"""
    @property
    def AddressMaskRequestsSent(self) -> int:
        """"""
    @property
    def DestinationUnreachableMessagesReceived(self) -> int:
        """"""
    @property
    def DestinationUnreachableMessagesSent(self) -> int:
        """"""
    @property
    def EchoRepliesReceived(self) -> int:
        """"""
    @property
    def EchoRepliesSent(self) -> int:
        """"""
    @property
    def EchoRequestsReceived(self) -> int:
        """"""
    @property
    def EchoRequestsSent(self) -> int:
        """"""
    @property
    def ErrorsReceived(self) -> int:
        """"""
    @property
    def ErrorsSent(self) -> int:
        """"""
    @property
    def MessagesReceived(self) -> int:
        """"""
    @property
    def MessagesSent(self) -> int:
        """"""
    @property
    def ParameterProblemsReceived(self) -> int:
        """"""
    @property
    def ParameterProblemsSent(self) -> int:
        """"""
    @property
    def RedirectsReceived(self) -> int:
        """"""
    @property
    def RedirectsSent(self) -> int:
        """"""
    @property
    def SourceQuenchesReceived(self) -> int:
        """"""
    @property
    def SourceQuenchesSent(self) -> int:
        """"""
    @property
    def TimeExceededMessagesReceived(self) -> int:
        """"""
    @property
    def TimeExceededMessagesSent(self) -> int:
        """"""
    @property
    def TimestampRepliesReceived(self) -> int:
        """"""
    @property
    def TimestampRepliesSent(self) -> int:
        """"""
    @property
    def TimestampRequestsReceived(self) -> int:
        """"""
    @property
    def TimestampRequestsSent(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SystemIcmpV6Statistics(IcmpV6Statistics):
    """"""
    @property
    def DestinationUnreachableMessagesReceived(self) -> int:
        """"""
    @property
    def DestinationUnreachableMessagesSent(self) -> int:
        """"""
    @property
    def EchoRepliesReceived(self) -> int:
        """"""
    @property
    def EchoRepliesSent(self) -> int:
        """"""
    @property
    def EchoRequestsReceived(self) -> int:
        """"""
    @property
    def EchoRequestsSent(self) -> int:
        """"""
    @property
    def ErrorsReceived(self) -> int:
        """"""
    @property
    def ErrorsSent(self) -> int:
        """"""
    @property
    def MembershipQueriesReceived(self) -> int:
        """"""
    @property
    def MembershipQueriesSent(self) -> int:
        """"""
    @property
    def MembershipReductionsReceived(self) -> int:
        """"""
    @property
    def MembershipReductionsSent(self) -> int:
        """"""
    @property
    def MembershipReportsReceived(self) -> int:
        """"""
    @property
    def MembershipReportsSent(self) -> int:
        """"""
    @property
    def MessagesReceived(self) -> int:
        """"""
    @property
    def MessagesSent(self) -> int:
        """"""
    @property
    def NeighborAdvertisementsReceived(self) -> int:
        """"""
    @property
    def NeighborAdvertisementsSent(self) -> int:
        """"""
    @property
    def NeighborSolicitsReceived(self) -> int:
        """"""
    @property
    def NeighborSolicitsSent(self) -> int:
        """"""
    @property
    def PacketTooBigMessagesReceived(self) -> int:
        """"""
    @property
    def PacketTooBigMessagesSent(self) -> int:
        """"""
    @property
    def ParameterProblemsReceived(self) -> int:
        """"""
    @property
    def ParameterProblemsSent(self) -> int:
        """"""
    @property
    def RedirectsReceived(self) -> int:
        """"""
    @property
    def RedirectsSent(self) -> int:
        """"""
    @property
    def RouterAdvertisementsReceived(self) -> int:
        """"""
    @property
    def RouterAdvertisementsSent(self) -> int:
        """"""
    @property
    def RouterSolicitsReceived(self) -> int:
        """"""
    @property
    def RouterSolicitsSent(self) -> int:
        """"""
    @property
    def TimeExceededMessagesReceived(self) -> int:
        """"""
    @property
    def TimeExceededMessagesSent(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SystemMulticastIPAddressInformation(MulticastIPAddressInformation):
    """"""
    def __init__(self, addressInfo: SystemIPAddressInformation) -> None:
        """"""
    @property
    def Address(self) -> IPAddress:
        """"""
    @property
    def AddressPreferredLifetime(self) -> int:
        """"""
    @property
    def AddressValidLifetime(self) -> int:
        """"""
    @property
    def DhcpLeaseLifetime(self) -> int:
        """"""
    @property
    def DuplicateAddressDetectionState(self) -> DuplicateAddressDetectionState:
        """"""
    @property
    def IsDnsEligible(self) -> bool:
        """"""
    @property
    def IsTransient(self) -> bool:
        """"""
    @property
    def PrefixOrigin(self) -> PrefixOrigin:
        """"""
    @property
    def SuffixOrigin(self) -> SuffixOrigin:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SystemNetworkInterface(NetworkInterface):
    """"""
    @property
    def Description(self) -> str:
        """"""
    @property
    def Id(self) -> str:
        """"""
    @property
    def IsReceiveOnly(self) -> bool:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def NetworkInterfaceType(self) -> NetworkInterfaceType:
        """"""
    @property
    def OperationalStatus(self) -> OperationalStatus:
        """"""
    @property
    def Speed(self) -> int:
        """"""
    @property
    def SupportsMulticast(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIPProperties(self) -> IPInterfaceProperties:
        """"""
    def GetIPStatistics(self) -> IPInterfaceStatistics:
        """"""
    def GetIPv4Statistics(self) -> IPv4InterfaceStatistics:
        """"""
    def GetPhysicalAddress(self) -> PhysicalAddress:
        """"""
    def GetType(self) -> Type:
        """"""
    def Supports(self, networkInterfaceComponent: NetworkInterfaceComponent) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class SystemTcpConnectionInformation(TcpConnectionInformation):
    """"""
    @property
    def LocalEndPoint(self) -> IPEndPoint:
        """"""
    @property
    def RemoteEndPoint(self) -> IPEndPoint:
        """"""
    @property
    def State(self) -> TcpState:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SystemTcpStatistics(TcpStatistics):
    """"""
    @property
    def ConnectionsAccepted(self) -> int:
        """"""
    @property
    def ConnectionsInitiated(self) -> int:
        """"""
    @property
    def CumulativeConnections(self) -> int:
        """"""
    @property
    def CurrentConnections(self) -> int:
        """"""
    @property
    def ErrorsReceived(self) -> int:
        """"""
    @property
    def FailedConnectionAttempts(self) -> int:
        """"""
    @property
    def MaximumConnections(self) -> int:
        """"""
    @property
    def MaximumTransmissionTimeout(self) -> int:
        """"""
    @property
    def MinimumTransmissionTimeout(self) -> int:
        """"""
    @property
    def ResetConnections(self) -> int:
        """"""
    @property
    def ResetsSent(self) -> int:
        """"""
    @property
    def SegmentsReceived(self) -> int:
        """"""
    @property
    def SegmentsResent(self) -> int:
        """"""
    @property
    def SegmentsSent(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SystemUdpStatistics(UdpStatistics):
    """"""
    @property
    def DatagramsReceived(self) -> int:
        """"""
    @property
    def DatagramsSent(self) -> int:
        """"""
    @property
    def IncomingDatagramsDiscarded(self) -> int:
        """"""
    @property
    def IncomingDatagramsWithErrors(self) -> int:
        """"""
    @property
    def UdpListeners(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SystemUnicastIPAddressInformation(UnicastIPAddressInformation):
    """"""
    @property
    def Address(self) -> IPAddress:
        """"""
    @property
    def AddressPreferredLifetime(self) -> int:
        """"""
    @property
    def AddressValidLifetime(self) -> int:
        """"""
    @property
    def DhcpLeaseLifetime(self) -> int:
        """"""
    @property
    def DuplicateAddressDetectionState(self) -> DuplicateAddressDetectionState:
        """"""
    @property
    def IPv4Mask(self) -> IPAddress:
        """"""
    @property
    def IsDnsEligible(self) -> bool:
        """"""
    @property
    def IsTransient(self) -> bool:
        """"""
    @property
    def PrefixLength(self) -> int:
        """"""
    @property
    def PrefixOrigin(self) -> PrefixOrigin:
        """"""
    @property
    def SuffixOrigin(self) -> SuffixOrigin:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TcpConnectionInformation(ABC, Object):
    """"""
    @property
    def LocalEndPoint(self) -> IPEndPoint:
        """"""
    @property
    def RemoteEndPoint(self) -> IPEndPoint:
        """"""
    @property
    def State(self) -> TcpState:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

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
        """"""
    @property
    def ConnectionsInitiated(self) -> int:
        """"""
    @property
    def CumulativeConnections(self) -> int:
        """"""
    @property
    def CurrentConnections(self) -> int:
        """"""
    @property
    def ErrorsReceived(self) -> int:
        """"""
    @property
    def FailedConnectionAttempts(self) -> int:
        """"""
    @property
    def MaximumConnections(self) -> int:
        """"""
    @property
    def MaximumTransmissionTimeout(self) -> int:
        """"""
    @property
    def MinimumTransmissionTimeout(self) -> int:
        """"""
    @property
    def ResetConnections(self) -> int:
        """"""
    @property
    def ResetsSent(self) -> int:
        """"""
    @property
    def SegmentsReceived(self) -> int:
        """"""
    @property
    def SegmentsResent(self) -> int:
        """"""
    @property
    def SegmentsSent(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

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
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def UnsafeNotifyStableUnicastIpAddressTable(
        cls, callback: Action[object], state: object
    ) -> bool:
        """"""

class UdpStatistics(ABC, Object):
    """"""
    @property
    def DatagramsReceived(self) -> int:
        """"""
    @property
    def DatagramsSent(self) -> int:
        """"""
    @property
    def IncomingDatagramsDiscarded(self) -> int:
        """"""
    @property
    def IncomingDatagramsWithErrors(self) -> int:
        """"""
    @property
    def UdpListeners(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

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
        """"""
    @property
    def AddressPreferredLifetime(self) -> int:
        """"""
    @property
    def AddressValidLifetime(self) -> int:
        """"""
    @property
    def DhcpLeaseLifetime(self) -> int:
        """"""
    @property
    def DuplicateAddressDetectionState(self) -> DuplicateAddressDetectionState:
        """"""
    @property
    def IPv4Mask(self) -> IPAddress:
        """"""
    @property
    def IsDnsEligible(self) -> bool:
        """"""
    @property
    def IsTransient(self) -> bool:
        """"""
    @property
    def PrefixLength(self) -> int:
        """"""
    @property
    def PrefixOrigin(self) -> PrefixOrigin:
        """"""
    @property
    def SuffixOrigin(self) -> SuffixOrigin:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class UnicastIPAddressInformationCollection(
    Object,
    ICollection[UnicastIPAddressInformation],
    IEnumerable[UnicastIPAddressInformation],
    IEnumerable,
):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def Item(self) -> UnicastIPAddressInformation:
        """"""
    def Add(self, address: UnicastIPAddressInformation) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains(self, address: UnicastIPAddressInformation) -> bool:
        """"""
    def CopyTo(self, array: Array[UnicastIPAddressInformation], offset: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[UnicastIPAddressInformation]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove(self, address: UnicastIPAddressInformation) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def __contains__(self, address: UnicastIPAddressInformation) -> bool:
        """"""
    def __iter__(self) -> Iterator[UnicastIPAddressInformation]:
        """"""
    def __delitem__(self, address: UnicastIPAddressInformation) -> bool:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> UnicastIPAddressInformation:
        """"""

class UnsafeNetInfoNativeMethods(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
