from __future__ import annotations

from abc import ABC
from typing import Callable, Generic, List, Union, overload

from Microsoft.Win32.SafeHandles import SafeHandleZeroOrMinusOneIsInvalid
from System import Action, Array, AsyncCallback, Boolean, Byte, Enum, EventArgs, Exception, IAsyncResult, ICloneable, IDisposable, Int32, Int64, IntPtr, InvalidOperationException, MulticastDelegate, Object, String, ValueType, Void
from System.Collections import IEnumerable
from System.Collections.Generic import ICollection, IEnumerable, IEnumerator
from System.ComponentModel import AsyncCompletedEventArgs, Component, IComponent, Win32Exception
from System.Net import IPAddress, IPEndPoint
from System.Runtime.InteropServices import _Attribute, _Exception
from System.Runtime.Serialization import ISerializable
from System.Security import CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, SecurityElement
from System.Security.Permissions import CodeAccessSecurityAttribute, IUnrestrictedPermission, PermissionState, SecurityAction
from System.Threading.Tasks import Task

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]


class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    
    def __isub__(self, other: T): ...


# ---------- Classes ---------- #

class GatewayIPAddressInformation(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Address(self) -> IPAddress: ...
    
    # ---------- Methods ---------- #
    
    def get_Address(self) -> IPAddress: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GatewayIPAddressInformationCollection(ObjectType, ICollection[GatewayIPAddressInformation], IEnumerable[GatewayIPAddressInformation], IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def Item(self) -> GatewayIPAddressInformation: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, address: GatewayIPAddressInformation) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Contains(self, address: GatewayIPAddressInformation) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[GatewayIPAddressInformation], offset: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator[GatewayIPAddressInformation]: ...
    
    def Remove(self, address: GatewayIPAddressInformation) -> BooleanType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_Item(self, index: IntType) -> GatewayIPAddressInformation: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IPAddressCollection(ObjectType, ICollection[IPAddress], IEnumerable[IPAddress], IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def Item(self) -> IPAddress: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, address: IPAddress) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Contains(self, address: IPAddress) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[IPAddress], offset: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator[IPAddress]: ...
    
    def Remove(self, address: IPAddress) -> BooleanType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_Item(self, index: IntType) -> IPAddress: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IPAddressInformation(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Address(self) -> IPAddress: ...
    
    @property
    def IsDnsEligible(self) -> BooleanType: ...
    
    @property
    def IsTransient(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_Address(self) -> IPAddress: ...
    
    def get_IsDnsEligible(self) -> BooleanType: ...
    
    def get_IsTransient(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IPAddressInformationCollection(ObjectType, ICollection[IPAddressInformation], IEnumerable[IPAddressInformation], IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def Item(self) -> IPAddressInformation: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, address: IPAddressInformation) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Contains(self, address: IPAddressInformation) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[IPAddressInformation], offset: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator[IPAddressInformation]: ...
    
    def Remove(self, address: IPAddressInformation) -> BooleanType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_Item(self, index: IntType) -> IPAddressInformation: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IPGlobalProperties(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def DhcpScopeName(self) -> StringType: ...
    
    @property
    def DomainName(self) -> StringType: ...
    
    @property
    def HostName(self) -> StringType: ...
    
    @property
    def IsWinsProxy(self) -> BooleanType: ...
    
    @property
    def NodeType(self) -> NetBiosNodeType: ...
    
    # ---------- Methods ---------- #
    
    def BeginGetUnicastAddresses(self, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def EndGetUnicastAddresses(self, asyncResult: IAsyncResult) -> UnicastIPAddressInformationCollection: ...
    
    def GetActiveTcpConnections(self) -> ArrayType[TcpConnectionInformation]: ...
    
    def GetActiveTcpListeners(self) -> ArrayType[IPEndPoint]: ...
    
    def GetActiveUdpListeners(self) -> ArrayType[IPEndPoint]: ...
    
    @staticmethod
    def GetIPGlobalProperties() -> IPGlobalProperties: ...
    
    def GetIPv4GlobalStatistics(self) -> IPGlobalStatistics: ...
    
    def GetIPv6GlobalStatistics(self) -> IPGlobalStatistics: ...
    
    def GetIcmpV4Statistics(self) -> IcmpV4Statistics: ...
    
    def GetIcmpV6Statistics(self) -> IcmpV6Statistics: ...
    
    def GetTcpIPv4Statistics(self) -> TcpStatistics: ...
    
    def GetTcpIPv6Statistics(self) -> TcpStatistics: ...
    
    def GetUdpIPv4Statistics(self) -> UdpStatistics: ...
    
    def GetUdpIPv6Statistics(self) -> UdpStatistics: ...
    
    def GetUnicastAddresses(self) -> UnicastIPAddressInformationCollection: ...
    
    def GetUnicastAddressesAsync(self) -> Task[UnicastIPAddressInformationCollection]: ...
    
    def get_DhcpScopeName(self) -> StringType: ...
    
    def get_DomainName(self) -> StringType: ...
    
    def get_HostName(self) -> StringType: ...
    
    def get_IsWinsProxy(self) -> BooleanType: ...
    
    def get_NodeType(self) -> NetBiosNodeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IPGlobalStatistics(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def DefaultTtl(self) -> IntType: ...
    
    @property
    def ForwardingEnabled(self) -> BooleanType: ...
    
    @property
    def NumberOfIPAddresses(self) -> IntType: ...
    
    @property
    def NumberOfInterfaces(self) -> IntType: ...
    
    @property
    def NumberOfRoutes(self) -> IntType: ...
    
    @property
    def OutputPacketRequests(self) -> LongType: ...
    
    @property
    def OutputPacketRoutingDiscards(self) -> LongType: ...
    
    @property
    def OutputPacketsDiscarded(self) -> LongType: ...
    
    @property
    def OutputPacketsWithNoRoute(self) -> LongType: ...
    
    @property
    def PacketFragmentFailures(self) -> LongType: ...
    
    @property
    def PacketReassembliesRequired(self) -> LongType: ...
    
    @property
    def PacketReassemblyFailures(self) -> LongType: ...
    
    @property
    def PacketReassemblyTimeout(self) -> LongType: ...
    
    @property
    def PacketsFragmented(self) -> LongType: ...
    
    @property
    def PacketsReassembled(self) -> LongType: ...
    
    @property
    def ReceivedPackets(self) -> LongType: ...
    
    @property
    def ReceivedPacketsDelivered(self) -> LongType: ...
    
    @property
    def ReceivedPacketsDiscarded(self) -> LongType: ...
    
    @property
    def ReceivedPacketsForwarded(self) -> LongType: ...
    
    @property
    def ReceivedPacketsWithAddressErrors(self) -> LongType: ...
    
    @property
    def ReceivedPacketsWithHeadersErrors(self) -> LongType: ...
    
    @property
    def ReceivedPacketsWithUnknownProtocol(self) -> LongType: ...
    
    # ---------- Methods ---------- #
    
    def get_DefaultTtl(self) -> IntType: ...
    
    def get_ForwardingEnabled(self) -> BooleanType: ...
    
    def get_NumberOfIPAddresses(self) -> IntType: ...
    
    def get_NumberOfInterfaces(self) -> IntType: ...
    
    def get_NumberOfRoutes(self) -> IntType: ...
    
    def get_OutputPacketRequests(self) -> LongType: ...
    
    def get_OutputPacketRoutingDiscards(self) -> LongType: ...
    
    def get_OutputPacketsDiscarded(self) -> LongType: ...
    
    def get_OutputPacketsWithNoRoute(self) -> LongType: ...
    
    def get_PacketFragmentFailures(self) -> LongType: ...
    
    def get_PacketReassembliesRequired(self) -> LongType: ...
    
    def get_PacketReassemblyFailures(self) -> LongType: ...
    
    def get_PacketReassemblyTimeout(self) -> LongType: ...
    
    def get_PacketsFragmented(self) -> LongType: ...
    
    def get_PacketsReassembled(self) -> LongType: ...
    
    def get_ReceivedPackets(self) -> LongType: ...
    
    def get_ReceivedPacketsDelivered(self) -> LongType: ...
    
    def get_ReceivedPacketsDiscarded(self) -> LongType: ...
    
    def get_ReceivedPacketsForwarded(self) -> LongType: ...
    
    def get_ReceivedPacketsWithAddressErrors(self) -> LongType: ...
    
    def get_ReceivedPacketsWithHeadersErrors(self) -> LongType: ...
    
    def get_ReceivedPacketsWithUnknownProtocol(self) -> LongType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IPInterfaceProperties(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AnycastAddresses(self) -> IPAddressInformationCollection: ...
    
    @property
    def DhcpServerAddresses(self) -> IPAddressCollection: ...
    
    @property
    def DnsAddresses(self) -> IPAddressCollection: ...
    
    @property
    def DnsSuffix(self) -> StringType: ...
    
    @property
    def GatewayAddresses(self) -> GatewayIPAddressInformationCollection: ...
    
    @property
    def IsDnsEnabled(self) -> BooleanType: ...
    
    @property
    def IsDynamicDnsEnabled(self) -> BooleanType: ...
    
    @property
    def MulticastAddresses(self) -> MulticastIPAddressInformationCollection: ...
    
    @property
    def UnicastAddresses(self) -> UnicastIPAddressInformationCollection: ...
    
    @property
    def WinsServersAddresses(self) -> IPAddressCollection: ...
    
    # ---------- Methods ---------- #
    
    def GetIPv4Properties(self) -> IPv4InterfaceProperties: ...
    
    def GetIPv6Properties(self) -> IPv6InterfaceProperties: ...
    
    def get_AnycastAddresses(self) -> IPAddressInformationCollection: ...
    
    def get_DhcpServerAddresses(self) -> IPAddressCollection: ...
    
    def get_DnsAddresses(self) -> IPAddressCollection: ...
    
    def get_DnsSuffix(self) -> StringType: ...
    
    def get_GatewayAddresses(self) -> GatewayIPAddressInformationCollection: ...
    
    def get_IsDnsEnabled(self) -> BooleanType: ...
    
    def get_IsDynamicDnsEnabled(self) -> BooleanType: ...
    
    def get_MulticastAddresses(self) -> MulticastIPAddressInformationCollection: ...
    
    def get_UnicastAddresses(self) -> UnicastIPAddressInformationCollection: ...
    
    def get_WinsServersAddresses(self) -> IPAddressCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IPInterfaceStatistics(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def BytesReceived(self) -> LongType: ...
    
    @property
    def BytesSent(self) -> LongType: ...
    
    @property
    def IncomingPacketsDiscarded(self) -> LongType: ...
    
    @property
    def IncomingPacketsWithErrors(self) -> LongType: ...
    
    @property
    def IncomingUnknownProtocolPackets(self) -> LongType: ...
    
    @property
    def NonUnicastPacketsReceived(self) -> LongType: ...
    
    @property
    def NonUnicastPacketsSent(self) -> LongType: ...
    
    @property
    def OutgoingPacketsDiscarded(self) -> LongType: ...
    
    @property
    def OutgoingPacketsWithErrors(self) -> LongType: ...
    
    @property
    def OutputQueueLength(self) -> LongType: ...
    
    @property
    def UnicastPacketsReceived(self) -> LongType: ...
    
    @property
    def UnicastPacketsSent(self) -> LongType: ...
    
    # ---------- Methods ---------- #
    
    def get_BytesReceived(self) -> LongType: ...
    
    def get_BytesSent(self) -> LongType: ...
    
    def get_IncomingPacketsDiscarded(self) -> LongType: ...
    
    def get_IncomingPacketsWithErrors(self) -> LongType: ...
    
    def get_IncomingUnknownProtocolPackets(self) -> LongType: ...
    
    def get_NonUnicastPacketsReceived(self) -> LongType: ...
    
    def get_NonUnicastPacketsSent(self) -> LongType: ...
    
    def get_OutgoingPacketsDiscarded(self) -> LongType: ...
    
    def get_OutgoingPacketsWithErrors(self) -> LongType: ...
    
    def get_OutputQueueLength(self) -> LongType: ...
    
    def get_UnicastPacketsReceived(self) -> LongType: ...
    
    def get_UnicastPacketsSent(self) -> LongType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IPv4InterfaceProperties(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Index(self) -> IntType: ...
    
    @property
    def IsAutomaticPrivateAddressingActive(self) -> BooleanType: ...
    
    @property
    def IsAutomaticPrivateAddressingEnabled(self) -> BooleanType: ...
    
    @property
    def IsDhcpEnabled(self) -> BooleanType: ...
    
    @property
    def IsForwardingEnabled(self) -> BooleanType: ...
    
    @property
    def Mtu(self) -> IntType: ...
    
    @property
    def UsesWins(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_Index(self) -> IntType: ...
    
    def get_IsAutomaticPrivateAddressingActive(self) -> BooleanType: ...
    
    def get_IsAutomaticPrivateAddressingEnabled(self) -> BooleanType: ...
    
    def get_IsDhcpEnabled(self) -> BooleanType: ...
    
    def get_IsForwardingEnabled(self) -> BooleanType: ...
    
    def get_Mtu(self) -> IntType: ...
    
    def get_UsesWins(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IPv4InterfaceStatistics(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def BytesReceived(self) -> LongType: ...
    
    @property
    def BytesSent(self) -> LongType: ...
    
    @property
    def IncomingPacketsDiscarded(self) -> LongType: ...
    
    @property
    def IncomingPacketsWithErrors(self) -> LongType: ...
    
    @property
    def IncomingUnknownProtocolPackets(self) -> LongType: ...
    
    @property
    def NonUnicastPacketsReceived(self) -> LongType: ...
    
    @property
    def NonUnicastPacketsSent(self) -> LongType: ...
    
    @property
    def OutgoingPacketsDiscarded(self) -> LongType: ...
    
    @property
    def OutgoingPacketsWithErrors(self) -> LongType: ...
    
    @property
    def OutputQueueLength(self) -> LongType: ...
    
    @property
    def UnicastPacketsReceived(self) -> LongType: ...
    
    @property
    def UnicastPacketsSent(self) -> LongType: ...
    
    # ---------- Methods ---------- #
    
    def get_BytesReceived(self) -> LongType: ...
    
    def get_BytesSent(self) -> LongType: ...
    
    def get_IncomingPacketsDiscarded(self) -> LongType: ...
    
    def get_IncomingPacketsWithErrors(self) -> LongType: ...
    
    def get_IncomingUnknownProtocolPackets(self) -> LongType: ...
    
    def get_NonUnicastPacketsReceived(self) -> LongType: ...
    
    def get_NonUnicastPacketsSent(self) -> LongType: ...
    
    def get_OutgoingPacketsDiscarded(self) -> LongType: ...
    
    def get_OutgoingPacketsWithErrors(self) -> LongType: ...
    
    def get_OutputQueueLength(self) -> LongType: ...
    
    def get_UnicastPacketsReceived(self) -> LongType: ...
    
    def get_UnicastPacketsSent(self) -> LongType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IPv6InterfaceProperties(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Index(self) -> IntType: ...
    
    @property
    def Mtu(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def GetScopeId(self, scopeLevel: ScopeLevel) -> LongType: ...
    
    def get_Index(self) -> IntType: ...
    
    def get_Mtu(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IcmpV4Statistics(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AddressMaskRepliesReceived(self) -> LongType: ...
    
    @property
    def AddressMaskRepliesSent(self) -> LongType: ...
    
    @property
    def AddressMaskRequestsReceived(self) -> LongType: ...
    
    @property
    def AddressMaskRequestsSent(self) -> LongType: ...
    
    @property
    def DestinationUnreachableMessagesReceived(self) -> LongType: ...
    
    @property
    def DestinationUnreachableMessagesSent(self) -> LongType: ...
    
    @property
    def EchoRepliesReceived(self) -> LongType: ...
    
    @property
    def EchoRepliesSent(self) -> LongType: ...
    
    @property
    def EchoRequestsReceived(self) -> LongType: ...
    
    @property
    def EchoRequestsSent(self) -> LongType: ...
    
    @property
    def ErrorsReceived(self) -> LongType: ...
    
    @property
    def ErrorsSent(self) -> LongType: ...
    
    @property
    def MessagesReceived(self) -> LongType: ...
    
    @property
    def MessagesSent(self) -> LongType: ...
    
    @property
    def ParameterProblemsReceived(self) -> LongType: ...
    
    @property
    def ParameterProblemsSent(self) -> LongType: ...
    
    @property
    def RedirectsReceived(self) -> LongType: ...
    
    @property
    def RedirectsSent(self) -> LongType: ...
    
    @property
    def SourceQuenchesReceived(self) -> LongType: ...
    
    @property
    def SourceQuenchesSent(self) -> LongType: ...
    
    @property
    def TimeExceededMessagesReceived(self) -> LongType: ...
    
    @property
    def TimeExceededMessagesSent(self) -> LongType: ...
    
    @property
    def TimestampRepliesReceived(self) -> LongType: ...
    
    @property
    def TimestampRepliesSent(self) -> LongType: ...
    
    @property
    def TimestampRequestsReceived(self) -> LongType: ...
    
    @property
    def TimestampRequestsSent(self) -> LongType: ...
    
    # ---------- Methods ---------- #
    
    def get_AddressMaskRepliesReceived(self) -> LongType: ...
    
    def get_AddressMaskRepliesSent(self) -> LongType: ...
    
    def get_AddressMaskRequestsReceived(self) -> LongType: ...
    
    def get_AddressMaskRequestsSent(self) -> LongType: ...
    
    def get_DestinationUnreachableMessagesReceived(self) -> LongType: ...
    
    def get_DestinationUnreachableMessagesSent(self) -> LongType: ...
    
    def get_EchoRepliesReceived(self) -> LongType: ...
    
    def get_EchoRepliesSent(self) -> LongType: ...
    
    def get_EchoRequestsReceived(self) -> LongType: ...
    
    def get_EchoRequestsSent(self) -> LongType: ...
    
    def get_ErrorsReceived(self) -> LongType: ...
    
    def get_ErrorsSent(self) -> LongType: ...
    
    def get_MessagesReceived(self) -> LongType: ...
    
    def get_MessagesSent(self) -> LongType: ...
    
    def get_ParameterProblemsReceived(self) -> LongType: ...
    
    def get_ParameterProblemsSent(self) -> LongType: ...
    
    def get_RedirectsReceived(self) -> LongType: ...
    
    def get_RedirectsSent(self) -> LongType: ...
    
    def get_SourceQuenchesReceived(self) -> LongType: ...
    
    def get_SourceQuenchesSent(self) -> LongType: ...
    
    def get_TimeExceededMessagesReceived(self) -> LongType: ...
    
    def get_TimeExceededMessagesSent(self) -> LongType: ...
    
    def get_TimestampRepliesReceived(self) -> LongType: ...
    
    def get_TimestampRepliesSent(self) -> LongType: ...
    
    def get_TimestampRequestsReceived(self) -> LongType: ...
    
    def get_TimestampRequestsSent(self) -> LongType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IcmpV6Statistics(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def DestinationUnreachableMessagesReceived(self) -> LongType: ...
    
    @property
    def DestinationUnreachableMessagesSent(self) -> LongType: ...
    
    @property
    def EchoRepliesReceived(self) -> LongType: ...
    
    @property
    def EchoRepliesSent(self) -> LongType: ...
    
    @property
    def EchoRequestsReceived(self) -> LongType: ...
    
    @property
    def EchoRequestsSent(self) -> LongType: ...
    
    @property
    def ErrorsReceived(self) -> LongType: ...
    
    @property
    def ErrorsSent(self) -> LongType: ...
    
    @property
    def MembershipQueriesReceived(self) -> LongType: ...
    
    @property
    def MembershipQueriesSent(self) -> LongType: ...
    
    @property
    def MembershipReductionsReceived(self) -> LongType: ...
    
    @property
    def MembershipReductionsSent(self) -> LongType: ...
    
    @property
    def MembershipReportsReceived(self) -> LongType: ...
    
    @property
    def MembershipReportsSent(self) -> LongType: ...
    
    @property
    def MessagesReceived(self) -> LongType: ...
    
    @property
    def MessagesSent(self) -> LongType: ...
    
    @property
    def NeighborAdvertisementsReceived(self) -> LongType: ...
    
    @property
    def NeighborAdvertisementsSent(self) -> LongType: ...
    
    @property
    def NeighborSolicitsReceived(self) -> LongType: ...
    
    @property
    def NeighborSolicitsSent(self) -> LongType: ...
    
    @property
    def PacketTooBigMessagesReceived(self) -> LongType: ...
    
    @property
    def PacketTooBigMessagesSent(self) -> LongType: ...
    
    @property
    def ParameterProblemsReceived(self) -> LongType: ...
    
    @property
    def ParameterProblemsSent(self) -> LongType: ...
    
    @property
    def RedirectsReceived(self) -> LongType: ...
    
    @property
    def RedirectsSent(self) -> LongType: ...
    
    @property
    def RouterAdvertisementsReceived(self) -> LongType: ...
    
    @property
    def RouterAdvertisementsSent(self) -> LongType: ...
    
    @property
    def RouterSolicitsReceived(self) -> LongType: ...
    
    @property
    def RouterSolicitsSent(self) -> LongType: ...
    
    @property
    def TimeExceededMessagesReceived(self) -> LongType: ...
    
    @property
    def TimeExceededMessagesSent(self) -> LongType: ...
    
    # ---------- Methods ---------- #
    
    def get_DestinationUnreachableMessagesReceived(self) -> LongType: ...
    
    def get_DestinationUnreachableMessagesSent(self) -> LongType: ...
    
    def get_EchoRepliesReceived(self) -> LongType: ...
    
    def get_EchoRepliesSent(self) -> LongType: ...
    
    def get_EchoRequestsReceived(self) -> LongType: ...
    
    def get_EchoRequestsSent(self) -> LongType: ...
    
    def get_ErrorsReceived(self) -> LongType: ...
    
    def get_ErrorsSent(self) -> LongType: ...
    
    def get_MembershipQueriesReceived(self) -> LongType: ...
    
    def get_MembershipQueriesSent(self) -> LongType: ...
    
    def get_MembershipReductionsReceived(self) -> LongType: ...
    
    def get_MembershipReductionsSent(self) -> LongType: ...
    
    def get_MembershipReportsReceived(self) -> LongType: ...
    
    def get_MembershipReportsSent(self) -> LongType: ...
    
    def get_MessagesReceived(self) -> LongType: ...
    
    def get_MessagesSent(self) -> LongType: ...
    
    def get_NeighborAdvertisementsReceived(self) -> LongType: ...
    
    def get_NeighborAdvertisementsSent(self) -> LongType: ...
    
    def get_NeighborSolicitsReceived(self) -> LongType: ...
    
    def get_NeighborSolicitsSent(self) -> LongType: ...
    
    def get_PacketTooBigMessagesReceived(self) -> LongType: ...
    
    def get_PacketTooBigMessagesSent(self) -> LongType: ...
    
    def get_ParameterProblemsReceived(self) -> LongType: ...
    
    def get_ParameterProblemsSent(self) -> LongType: ...
    
    def get_RedirectsReceived(self) -> LongType: ...
    
    def get_RedirectsSent(self) -> LongType: ...
    
    def get_RouterAdvertisementsReceived(self) -> LongType: ...
    
    def get_RouterAdvertisementsSent(self) -> LongType: ...
    
    def get_RouterSolicitsReceived(self) -> LongType: ...
    
    def get_RouterSolicitsSent(self) -> LongType: ...
    
    def get_TimeExceededMessagesReceived(self) -> LongType: ...
    
    def get_TimeExceededMessagesSent(self) -> LongType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class IpHelperErrors(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MulticastIPAddressInformation(ABC, IPAddressInformation):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AddressPreferredLifetime(self) -> LongType: ...
    
    @property
    def AddressValidLifetime(self) -> LongType: ...
    
    @property
    def DhcpLeaseLifetime(self) -> LongType: ...
    
    @property
    def DuplicateAddressDetectionState(self) -> DuplicateAddressDetectionState: ...
    
    @property
    def PrefixOrigin(self) -> PrefixOrigin: ...
    
    @property
    def SuffixOrigin(self) -> SuffixOrigin: ...
    
    # ---------- Methods ---------- #
    
    def get_AddressPreferredLifetime(self) -> LongType: ...
    
    def get_AddressValidLifetime(self) -> LongType: ...
    
    def get_DhcpLeaseLifetime(self) -> LongType: ...
    
    def get_DuplicateAddressDetectionState(self) -> DuplicateAddressDetectionState: ...
    
    def get_PrefixOrigin(self) -> PrefixOrigin: ...
    
    def get_SuffixOrigin(self) -> SuffixOrigin: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MulticastIPAddressInformationCollection(ObjectType, ICollection[MulticastIPAddressInformation], IEnumerable[MulticastIPAddressInformation], IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def Item(self) -> MulticastIPAddressInformation: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, address: MulticastIPAddressInformation) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Contains(self, address: MulticastIPAddressInformation) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[MulticastIPAddressInformation], offset: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator[MulticastIPAddressInformation]: ...
    
    def Remove(self, address: MulticastIPAddressInformation) -> BooleanType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_Item(self, index: IntType) -> MulticastIPAddressInformation: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NetworkAddressChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: EventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: EventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NetworkAvailabilityChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: NetworkAvailabilityEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: NetworkAvailabilityEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NetworkAvailabilityEventArgs(EventArgs):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsAvailable(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_IsAvailable(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NetworkChange(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def RegisterNetworkChange(nc: NetworkChange) -> VoidType: ...
    
    @staticmethod
    def add_NetworkAddressChanged(value: NetworkAddressChangedEventHandler) -> VoidType: ...
    
    @staticmethod
    def add_NetworkAvailabilityChanged(value: NetworkAvailabilityChangedEventHandler) -> VoidType: ...
    
    @staticmethod
    def remove_NetworkAddressChanged(value: NetworkAddressChangedEventHandler) -> VoidType: ...
    
    @staticmethod
    def remove_NetworkAvailabilityChanged(value: NetworkAvailabilityChangedEventHandler) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    NetworkAddressChanged: EventType[NetworkAddressChangedEventHandler] = ...
    
    NetworkAvailabilityChanged: EventType[NetworkAvailabilityChangedEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NetworkInformationException(Win32Exception, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, errorCode: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ErrorCode(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_ErrorCode(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NetworkInformationPermission(CodeAccessPermission, IPermission, ISecurityEncodable, IStackWalk, IUnrestrictedPermission):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, state: PermissionState): ...
    
    @overload
    def __init__(self, access: NetworkInformationAccess): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Access(self) -> NetworkInformationAccess: ...
    
    # ---------- Methods ---------- #
    
    def AddPermission(self, access: NetworkInformationAccess) -> VoidType: ...
    
    def Copy(self) -> IPermission: ...
    
    def FromXml(self, securityElement: SecurityElement) -> VoidType: ...
    
    def Intersect(self, target: IPermission) -> IPermission: ...
    
    def IsSubsetOf(self, target: IPermission) -> BooleanType: ...
    
    def IsUnrestricted(self) -> BooleanType: ...
    
    def ToXml(self) -> SecurityElement: ...
    
    def Union(self, target: IPermission) -> IPermission: ...
    
    def get_Access(self) -> NetworkInformationAccess: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NetworkInformationPermissionAttribute(CodeAccessSecurityAttribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, action: SecurityAction): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Access(self) -> StringType: ...
    
    @Access.setter
    def Access(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CreatePermission(self) -> IPermission: ...
    
    def get_Access(self) -> StringType: ...
    
    def set_Access(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NetworkInterface(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Description(self) -> StringType: ...
    
    @staticmethod
    @property
    def IPv6LoopbackInterfaceIndex() -> IntType: ...
    
    @property
    def Id(self) -> StringType: ...
    
    @property
    def IsReceiveOnly(self) -> BooleanType: ...
    
    @staticmethod
    @property
    def LoopbackInterfaceIndex() -> IntType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NetworkInterfaceType(self) -> NetworkInterfaceType: ...
    
    @property
    def OperationalStatus(self) -> OperationalStatus: ...
    
    @property
    def Speed(self) -> LongType: ...
    
    @property
    def SupportsMulticast(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetAllNetworkInterfaces() -> ArrayType[NetworkInterface]: ...
    
    def GetIPProperties(self) -> IPInterfaceProperties: ...
    
    def GetIPStatistics(self) -> IPInterfaceStatistics: ...
    
    def GetIPv4Statistics(self) -> IPv4InterfaceStatistics: ...
    
    @staticmethod
    def GetIsNetworkAvailable() -> BooleanType: ...
    
    def GetPhysicalAddress(self) -> PhysicalAddress: ...
    
    def Supports(self, networkInterfaceComponent: NetworkInterfaceComponent) -> BooleanType: ...
    
    def get_Description(self) -> StringType: ...
    
    @staticmethod
    def get_IPv6LoopbackInterfaceIndex() -> IntType: ...
    
    def get_Id(self) -> StringType: ...
    
    def get_IsReceiveOnly(self) -> BooleanType: ...
    
    @staticmethod
    def get_LoopbackInterfaceIndex() -> IntType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NetworkInterfaceType(self) -> NetworkInterfaceType: ...
    
    def get_OperationalStatus(self) -> OperationalStatus: ...
    
    def get_Speed(self) -> LongType: ...
    
    def get_SupportsMulticast(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PhysicalAddress(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def _None() -> PhysicalAddress: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, address: ArrayType[ByteType]): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, comparand: ObjectType) -> BooleanType: ...
    
    def GetAddressBytes(self) -> ArrayType[ByteType]: ...
    
    def GetHashCode(self) -> IntType: ...
    
    @staticmethod
    def Parse(address: StringType) -> PhysicalAddress: ...
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Ping(Component, IComponent, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Send(self, hostNameOrAddress: StringType) -> PingReply: ...
    
    @overload
    def Send(self, hostNameOrAddress: StringType, timeout: IntType) -> PingReply: ...
    
    @overload
    def Send(self, address: IPAddress) -> PingReply: ...
    
    @overload
    def Send(self, address: IPAddress, timeout: IntType) -> PingReply: ...
    
    @overload
    def Send(self, hostNameOrAddress: StringType, timeout: IntType, buffer: ArrayType[ByteType]) -> PingReply: ...
    
    @overload
    def Send(self, address: IPAddress, timeout: IntType, buffer: ArrayType[ByteType]) -> PingReply: ...
    
    @overload
    def Send(self, hostNameOrAddress: StringType, timeout: IntType, buffer: ArrayType[ByteType], options: PingOptions) -> PingReply: ...
    
    @overload
    def Send(self, address: IPAddress, timeout: IntType, buffer: ArrayType[ByteType], options: PingOptions) -> PingReply: ...
    
    @overload
    def SendAsync(self, hostNameOrAddress: StringType, userToken: ObjectType) -> VoidType: ...
    
    @overload
    def SendAsync(self, hostNameOrAddress: StringType, timeout: IntType, userToken: ObjectType) -> VoidType: ...
    
    @overload
    def SendAsync(self, address: IPAddress, userToken: ObjectType) -> VoidType: ...
    
    @overload
    def SendAsync(self, address: IPAddress, timeout: IntType, userToken: ObjectType) -> VoidType: ...
    
    @overload
    def SendAsync(self, hostNameOrAddress: StringType, timeout: IntType, buffer: ArrayType[ByteType], userToken: ObjectType) -> VoidType: ...
    
    @overload
    def SendAsync(self, address: IPAddress, timeout: IntType, buffer: ArrayType[ByteType], userToken: ObjectType) -> VoidType: ...
    
    @overload
    def SendAsync(self, hostNameOrAddress: StringType, timeout: IntType, buffer: ArrayType[ByteType], options: PingOptions, userToken: ObjectType) -> VoidType: ...
    
    @overload
    def SendAsync(self, address: IPAddress, timeout: IntType, buffer: ArrayType[ByteType], options: PingOptions, userToken: ObjectType) -> VoidType: ...
    
    def SendAsyncCancel(self) -> VoidType: ...
    
    @overload
    def SendPingAsync(self, address: IPAddress) -> Task[PingReply]: ...
    
    @overload
    def SendPingAsync(self, hostNameOrAddress: StringType) -> Task[PingReply]: ...
    
    @overload
    def SendPingAsync(self, address: IPAddress, timeout: IntType) -> Task[PingReply]: ...
    
    @overload
    def SendPingAsync(self, hostNameOrAddress: StringType, timeout: IntType) -> Task[PingReply]: ...
    
    @overload
    def SendPingAsync(self, address: IPAddress, timeout: IntType, buffer: ArrayType[ByteType]) -> Task[PingReply]: ...
    
    @overload
    def SendPingAsync(self, hostNameOrAddress: StringType, timeout: IntType, buffer: ArrayType[ByteType]) -> Task[PingReply]: ...
    
    @overload
    def SendPingAsync(self, address: IPAddress, timeout: IntType, buffer: ArrayType[ByteType], options: PingOptions) -> Task[PingReply]: ...
    
    @overload
    def SendPingAsync(self, hostNameOrAddress: StringType, timeout: IntType, buffer: ArrayType[ByteType], options: PingOptions) -> Task[PingReply]: ...
    
    def add_PingCompleted(self, value: PingCompletedEventHandler) -> VoidType: ...
    
    def remove_PingCompleted(self, value: PingCompletedEventHandler) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    PingCompleted: EventType[PingCompletedEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PingCompletedEventArgs(AsyncCompletedEventArgs):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Reply(self) -> PingReply: ...
    
    # ---------- Methods ---------- #
    
    def get_Reply(self) -> PingReply: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PingCompletedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: PingCompletedEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: PingCompletedEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PingException(InvalidOperationException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, innerException: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PingOptions(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, ttl: IntType, dontFragment: BooleanType): ...
    
    @overload
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DontFragment(self) -> BooleanType: ...
    
    @DontFragment.setter
    def DontFragment(self, value: BooleanType) -> None: ...
    
    @property
    def Ttl(self) -> IntType: ...
    
    @Ttl.setter
    def Ttl(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_DontFragment(self) -> BooleanType: ...
    
    def get_Ttl(self) -> IntType: ...
    
    def set_DontFragment(self, value: BooleanType) -> VoidType: ...
    
    def set_Ttl(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PingReply(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Address(self) -> IPAddress: ...
    
    @property
    def Buffer(self) -> ArrayType[ByteType]: ...
    
    @property
    def Options(self) -> PingOptions: ...
    
    @property
    def RoundtripTime(self) -> LongType: ...
    
    @property
    def Status(self) -> IPStatus: ...
    
    # ---------- Methods ---------- #
    
    def get_Address(self) -> IPAddress: ...
    
    def get_Buffer(self) -> ArrayType[ByteType]: ...
    
    def get_Options(self) -> PingOptions: ...
    
    def get_RoundtripTime(self) -> LongType: ...
    
    def get_Status(self) -> IPStatus: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeCancelMibChangeNotify(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SafeFreeMibTable(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StableUnicastIpAddressTableDelegate(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, context: NIntType, table: NIntType, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, context: NIntType, table: NIntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SystemGatewayIPAddressInformation(GatewayIPAddressInformation):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Address(self) -> IPAddress: ...
    
    # ---------- Methods ---------- #
    
    def get_Address(self) -> IPAddress: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SystemIPAddressInformation(IPAddressInformation):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Address(self) -> IPAddress: ...
    
    @property
    def IsDnsEligible(self) -> BooleanType: ...
    
    @property
    def IsTransient(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_Address(self) -> IPAddress: ...
    
    def get_IsDnsEligible(self) -> BooleanType: ...
    
    def get_IsTransient(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SystemIPGlobalProperties(IPGlobalProperties):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def DhcpScopeName(self) -> StringType: ...
    
    @property
    def DomainName(self) -> StringType: ...
    
    @property
    def HostName(self) -> StringType: ...
    
    @property
    def IsWinsProxy(self) -> BooleanType: ...
    
    @property
    def NodeType(self) -> NetBiosNodeType: ...
    
    # ---------- Methods ---------- #
    
    def BeginGetUnicastAddresses(self, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def EndGetUnicastAddresses(self, asyncResult: IAsyncResult) -> UnicastIPAddressInformationCollection: ...
    
    def GetActiveTcpConnections(self) -> ArrayType[TcpConnectionInformation]: ...
    
    def GetActiveTcpListeners(self) -> ArrayType[IPEndPoint]: ...
    
    def GetActiveUdpListeners(self) -> ArrayType[IPEndPoint]: ...
    
    def GetIPv4GlobalStatistics(self) -> IPGlobalStatistics: ...
    
    def GetIPv6GlobalStatistics(self) -> IPGlobalStatistics: ...
    
    def GetIcmpV4Statistics(self) -> IcmpV4Statistics: ...
    
    def GetIcmpV6Statistics(self) -> IcmpV6Statistics: ...
    
    def GetTcpIPv4Statistics(self) -> TcpStatistics: ...
    
    def GetTcpIPv6Statistics(self) -> TcpStatistics: ...
    
    def GetUdpIPv4Statistics(self) -> UdpStatistics: ...
    
    def GetUdpIPv6Statistics(self) -> UdpStatistics: ...
    
    def GetUnicastAddresses(self) -> UnicastIPAddressInformationCollection: ...
    
    def get_DhcpScopeName(self) -> StringType: ...
    
    def get_DomainName(self) -> StringType: ...
    
    def get_HostName(self) -> StringType: ...
    
    def get_IsWinsProxy(self) -> BooleanType: ...
    
    def get_NodeType(self) -> NetBiosNodeType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SystemIPGlobalStatistics(IPGlobalStatistics):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def DefaultTtl(self) -> IntType: ...
    
    @property
    def ForwardingEnabled(self) -> BooleanType: ...
    
    @property
    def NumberOfIPAddresses(self) -> IntType: ...
    
    @property
    def NumberOfInterfaces(self) -> IntType: ...
    
    @property
    def NumberOfRoutes(self) -> IntType: ...
    
    @property
    def OutputPacketRequests(self) -> LongType: ...
    
    @property
    def OutputPacketRoutingDiscards(self) -> LongType: ...
    
    @property
    def OutputPacketsDiscarded(self) -> LongType: ...
    
    @property
    def OutputPacketsWithNoRoute(self) -> LongType: ...
    
    @property
    def PacketFragmentFailures(self) -> LongType: ...
    
    @property
    def PacketReassembliesRequired(self) -> LongType: ...
    
    @property
    def PacketReassemblyFailures(self) -> LongType: ...
    
    @property
    def PacketReassemblyTimeout(self) -> LongType: ...
    
    @property
    def PacketsFragmented(self) -> LongType: ...
    
    @property
    def PacketsReassembled(self) -> LongType: ...
    
    @property
    def ReceivedPackets(self) -> LongType: ...
    
    @property
    def ReceivedPacketsDelivered(self) -> LongType: ...
    
    @property
    def ReceivedPacketsDiscarded(self) -> LongType: ...
    
    @property
    def ReceivedPacketsForwarded(self) -> LongType: ...
    
    @property
    def ReceivedPacketsWithAddressErrors(self) -> LongType: ...
    
    @property
    def ReceivedPacketsWithHeadersErrors(self) -> LongType: ...
    
    @property
    def ReceivedPacketsWithUnknownProtocol(self) -> LongType: ...
    
    # ---------- Methods ---------- #
    
    def get_DefaultTtl(self) -> IntType: ...
    
    def get_ForwardingEnabled(self) -> BooleanType: ...
    
    def get_NumberOfIPAddresses(self) -> IntType: ...
    
    def get_NumberOfInterfaces(self) -> IntType: ...
    
    def get_NumberOfRoutes(self) -> IntType: ...
    
    def get_OutputPacketRequests(self) -> LongType: ...
    
    def get_OutputPacketRoutingDiscards(self) -> LongType: ...
    
    def get_OutputPacketsDiscarded(self) -> LongType: ...
    
    def get_OutputPacketsWithNoRoute(self) -> LongType: ...
    
    def get_PacketFragmentFailures(self) -> LongType: ...
    
    def get_PacketReassembliesRequired(self) -> LongType: ...
    
    def get_PacketReassemblyFailures(self) -> LongType: ...
    
    def get_PacketReassemblyTimeout(self) -> LongType: ...
    
    def get_PacketsFragmented(self) -> LongType: ...
    
    def get_PacketsReassembled(self) -> LongType: ...
    
    def get_ReceivedPackets(self) -> LongType: ...
    
    def get_ReceivedPacketsDelivered(self) -> LongType: ...
    
    def get_ReceivedPacketsDiscarded(self) -> LongType: ...
    
    def get_ReceivedPacketsForwarded(self) -> LongType: ...
    
    def get_ReceivedPacketsWithAddressErrors(self) -> LongType: ...
    
    def get_ReceivedPacketsWithHeadersErrors(self) -> LongType: ...
    
    def get_ReceivedPacketsWithUnknownProtocol(self) -> LongType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SystemIPInterfaceProperties(IPInterfaceProperties):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AnycastAddresses(self) -> IPAddressInformationCollection: ...
    
    @property
    def DhcpServerAddresses(self) -> IPAddressCollection: ...
    
    @property
    def DnsAddresses(self) -> IPAddressCollection: ...
    
    @property
    def DnsSuffix(self) -> StringType: ...
    
    @property
    def GatewayAddresses(self) -> GatewayIPAddressInformationCollection: ...
    
    @property
    def IsDnsEnabled(self) -> BooleanType: ...
    
    @property
    def IsDynamicDnsEnabled(self) -> BooleanType: ...
    
    @property
    def MulticastAddresses(self) -> MulticastIPAddressInformationCollection: ...
    
    @property
    def UnicastAddresses(self) -> UnicastIPAddressInformationCollection: ...
    
    @property
    def WinsServersAddresses(self) -> IPAddressCollection: ...
    
    # ---------- Methods ---------- #
    
    def GetIPv4Properties(self) -> IPv4InterfaceProperties: ...
    
    def GetIPv6Properties(self) -> IPv6InterfaceProperties: ...
    
    def get_AnycastAddresses(self) -> IPAddressInformationCollection: ...
    
    def get_DhcpServerAddresses(self) -> IPAddressCollection: ...
    
    def get_DnsAddresses(self) -> IPAddressCollection: ...
    
    def get_DnsSuffix(self) -> StringType: ...
    
    def get_GatewayAddresses(self) -> GatewayIPAddressInformationCollection: ...
    
    def get_IsDnsEnabled(self) -> BooleanType: ...
    
    def get_IsDynamicDnsEnabled(self) -> BooleanType: ...
    
    def get_MulticastAddresses(self) -> MulticastIPAddressInformationCollection: ...
    
    def get_UnicastAddresses(self) -> UnicastIPAddressInformationCollection: ...
    
    def get_WinsServersAddresses(self) -> IPAddressCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SystemIPInterfaceStatistics(IPInterfaceStatistics):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def BytesReceived(self) -> LongType: ...
    
    @property
    def BytesSent(self) -> LongType: ...
    
    @property
    def IncomingPacketsDiscarded(self) -> LongType: ...
    
    @property
    def IncomingPacketsWithErrors(self) -> LongType: ...
    
    @property
    def IncomingUnknownProtocolPackets(self) -> LongType: ...
    
    @property
    def NonUnicastPacketsReceived(self) -> LongType: ...
    
    @property
    def NonUnicastPacketsSent(self) -> LongType: ...
    
    @property
    def OutgoingPacketsDiscarded(self) -> LongType: ...
    
    @property
    def OutgoingPacketsWithErrors(self) -> LongType: ...
    
    @property
    def OutputQueueLength(self) -> LongType: ...
    
    @property
    def UnicastPacketsReceived(self) -> LongType: ...
    
    @property
    def UnicastPacketsSent(self) -> LongType: ...
    
    # ---------- Methods ---------- #
    
    def get_BytesReceived(self) -> LongType: ...
    
    def get_BytesSent(self) -> LongType: ...
    
    def get_IncomingPacketsDiscarded(self) -> LongType: ...
    
    def get_IncomingPacketsWithErrors(self) -> LongType: ...
    
    def get_IncomingUnknownProtocolPackets(self) -> LongType: ...
    
    def get_NonUnicastPacketsReceived(self) -> LongType: ...
    
    def get_NonUnicastPacketsSent(self) -> LongType: ...
    
    def get_OutgoingPacketsDiscarded(self) -> LongType: ...
    
    def get_OutgoingPacketsWithErrors(self) -> LongType: ...
    
    def get_OutputQueueLength(self) -> LongType: ...
    
    def get_UnicastPacketsReceived(self) -> LongType: ...
    
    def get_UnicastPacketsSent(self) -> LongType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SystemIPv4InterfaceProperties(IPv4InterfaceProperties):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Index(self) -> IntType: ...
    
    @property
    def IsAutomaticPrivateAddressingActive(self) -> BooleanType: ...
    
    @property
    def IsAutomaticPrivateAddressingEnabled(self) -> BooleanType: ...
    
    @property
    def IsDhcpEnabled(self) -> BooleanType: ...
    
    @property
    def IsForwardingEnabled(self) -> BooleanType: ...
    
    @property
    def Mtu(self) -> IntType: ...
    
    @property
    def UsesWins(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def get_Index(self) -> IntType: ...
    
    def get_IsAutomaticPrivateAddressingActive(self) -> BooleanType: ...
    
    def get_IsAutomaticPrivateAddressingEnabled(self) -> BooleanType: ...
    
    def get_IsDhcpEnabled(self) -> BooleanType: ...
    
    def get_IsForwardingEnabled(self) -> BooleanType: ...
    
    def get_Mtu(self) -> IntType: ...
    
    def get_UsesWins(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SystemIPv4InterfaceStatistics(IPv4InterfaceStatistics):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def BytesReceived(self) -> LongType: ...
    
    @property
    def BytesSent(self) -> LongType: ...
    
    @property
    def IncomingPacketsDiscarded(self) -> LongType: ...
    
    @property
    def IncomingPacketsWithErrors(self) -> LongType: ...
    
    @property
    def IncomingUnknownProtocolPackets(self) -> LongType: ...
    
    @property
    def NonUnicastPacketsReceived(self) -> LongType: ...
    
    @property
    def NonUnicastPacketsSent(self) -> LongType: ...
    
    @property
    def OutgoingPacketsDiscarded(self) -> LongType: ...
    
    @property
    def OutgoingPacketsWithErrors(self) -> LongType: ...
    
    @property
    def OutputQueueLength(self) -> LongType: ...
    
    @property
    def UnicastPacketsReceived(self) -> LongType: ...
    
    @property
    def UnicastPacketsSent(self) -> LongType: ...
    
    # ---------- Methods ---------- #
    
    def get_BytesReceived(self) -> LongType: ...
    
    def get_BytesSent(self) -> LongType: ...
    
    def get_IncomingPacketsDiscarded(self) -> LongType: ...
    
    def get_IncomingPacketsWithErrors(self) -> LongType: ...
    
    def get_IncomingUnknownProtocolPackets(self) -> LongType: ...
    
    def get_NonUnicastPacketsReceived(self) -> LongType: ...
    
    def get_NonUnicastPacketsSent(self) -> LongType: ...
    
    def get_OutgoingPacketsDiscarded(self) -> LongType: ...
    
    def get_OutgoingPacketsWithErrors(self) -> LongType: ...
    
    def get_OutputQueueLength(self) -> LongType: ...
    
    def get_UnicastPacketsReceived(self) -> LongType: ...
    
    def get_UnicastPacketsSent(self) -> LongType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SystemIPv6InterfaceProperties(IPv6InterfaceProperties):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Index(self) -> IntType: ...
    
    @property
    def Mtu(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def GetScopeId(self, scopeLevel: ScopeLevel) -> LongType: ...
    
    def get_Index(self) -> IntType: ...
    
    def get_Mtu(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SystemIcmpV4Statistics(IcmpV4Statistics):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AddressMaskRepliesReceived(self) -> LongType: ...
    
    @property
    def AddressMaskRepliesSent(self) -> LongType: ...
    
    @property
    def AddressMaskRequestsReceived(self) -> LongType: ...
    
    @property
    def AddressMaskRequestsSent(self) -> LongType: ...
    
    @property
    def DestinationUnreachableMessagesReceived(self) -> LongType: ...
    
    @property
    def DestinationUnreachableMessagesSent(self) -> LongType: ...
    
    @property
    def EchoRepliesReceived(self) -> LongType: ...
    
    @property
    def EchoRepliesSent(self) -> LongType: ...
    
    @property
    def EchoRequestsReceived(self) -> LongType: ...
    
    @property
    def EchoRequestsSent(self) -> LongType: ...
    
    @property
    def ErrorsReceived(self) -> LongType: ...
    
    @property
    def ErrorsSent(self) -> LongType: ...
    
    @property
    def MessagesReceived(self) -> LongType: ...
    
    @property
    def MessagesSent(self) -> LongType: ...
    
    @property
    def ParameterProblemsReceived(self) -> LongType: ...
    
    @property
    def ParameterProblemsSent(self) -> LongType: ...
    
    @property
    def RedirectsReceived(self) -> LongType: ...
    
    @property
    def RedirectsSent(self) -> LongType: ...
    
    @property
    def SourceQuenchesReceived(self) -> LongType: ...
    
    @property
    def SourceQuenchesSent(self) -> LongType: ...
    
    @property
    def TimeExceededMessagesReceived(self) -> LongType: ...
    
    @property
    def TimeExceededMessagesSent(self) -> LongType: ...
    
    @property
    def TimestampRepliesReceived(self) -> LongType: ...
    
    @property
    def TimestampRepliesSent(self) -> LongType: ...
    
    @property
    def TimestampRequestsReceived(self) -> LongType: ...
    
    @property
    def TimestampRequestsSent(self) -> LongType: ...
    
    # ---------- Methods ---------- #
    
    def get_AddressMaskRepliesReceived(self) -> LongType: ...
    
    def get_AddressMaskRepliesSent(self) -> LongType: ...
    
    def get_AddressMaskRequestsReceived(self) -> LongType: ...
    
    def get_AddressMaskRequestsSent(self) -> LongType: ...
    
    def get_DestinationUnreachableMessagesReceived(self) -> LongType: ...
    
    def get_DestinationUnreachableMessagesSent(self) -> LongType: ...
    
    def get_EchoRepliesReceived(self) -> LongType: ...
    
    def get_EchoRepliesSent(self) -> LongType: ...
    
    def get_EchoRequestsReceived(self) -> LongType: ...
    
    def get_EchoRequestsSent(self) -> LongType: ...
    
    def get_ErrorsReceived(self) -> LongType: ...
    
    def get_ErrorsSent(self) -> LongType: ...
    
    def get_MessagesReceived(self) -> LongType: ...
    
    def get_MessagesSent(self) -> LongType: ...
    
    def get_ParameterProblemsReceived(self) -> LongType: ...
    
    def get_ParameterProblemsSent(self) -> LongType: ...
    
    def get_RedirectsReceived(self) -> LongType: ...
    
    def get_RedirectsSent(self) -> LongType: ...
    
    def get_SourceQuenchesReceived(self) -> LongType: ...
    
    def get_SourceQuenchesSent(self) -> LongType: ...
    
    def get_TimeExceededMessagesReceived(self) -> LongType: ...
    
    def get_TimeExceededMessagesSent(self) -> LongType: ...
    
    def get_TimestampRepliesReceived(self) -> LongType: ...
    
    def get_TimestampRepliesSent(self) -> LongType: ...
    
    def get_TimestampRequestsReceived(self) -> LongType: ...
    
    def get_TimestampRequestsSent(self) -> LongType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SystemIcmpV6Statistics(IcmpV6Statistics):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def DestinationUnreachableMessagesReceived(self) -> LongType: ...
    
    @property
    def DestinationUnreachableMessagesSent(self) -> LongType: ...
    
    @property
    def EchoRepliesReceived(self) -> LongType: ...
    
    @property
    def EchoRepliesSent(self) -> LongType: ...
    
    @property
    def EchoRequestsReceived(self) -> LongType: ...
    
    @property
    def EchoRequestsSent(self) -> LongType: ...
    
    @property
    def ErrorsReceived(self) -> LongType: ...
    
    @property
    def ErrorsSent(self) -> LongType: ...
    
    @property
    def MembershipQueriesReceived(self) -> LongType: ...
    
    @property
    def MembershipQueriesSent(self) -> LongType: ...
    
    @property
    def MembershipReductionsReceived(self) -> LongType: ...
    
    @property
    def MembershipReductionsSent(self) -> LongType: ...
    
    @property
    def MembershipReportsReceived(self) -> LongType: ...
    
    @property
    def MembershipReportsSent(self) -> LongType: ...
    
    @property
    def MessagesReceived(self) -> LongType: ...
    
    @property
    def MessagesSent(self) -> LongType: ...
    
    @property
    def NeighborAdvertisementsReceived(self) -> LongType: ...
    
    @property
    def NeighborAdvertisementsSent(self) -> LongType: ...
    
    @property
    def NeighborSolicitsReceived(self) -> LongType: ...
    
    @property
    def NeighborSolicitsSent(self) -> LongType: ...
    
    @property
    def PacketTooBigMessagesReceived(self) -> LongType: ...
    
    @property
    def PacketTooBigMessagesSent(self) -> LongType: ...
    
    @property
    def ParameterProblemsReceived(self) -> LongType: ...
    
    @property
    def ParameterProblemsSent(self) -> LongType: ...
    
    @property
    def RedirectsReceived(self) -> LongType: ...
    
    @property
    def RedirectsSent(self) -> LongType: ...
    
    @property
    def RouterAdvertisementsReceived(self) -> LongType: ...
    
    @property
    def RouterAdvertisementsSent(self) -> LongType: ...
    
    @property
    def RouterSolicitsReceived(self) -> LongType: ...
    
    @property
    def RouterSolicitsSent(self) -> LongType: ...
    
    @property
    def TimeExceededMessagesReceived(self) -> LongType: ...
    
    @property
    def TimeExceededMessagesSent(self) -> LongType: ...
    
    # ---------- Methods ---------- #
    
    def get_DestinationUnreachableMessagesReceived(self) -> LongType: ...
    
    def get_DestinationUnreachableMessagesSent(self) -> LongType: ...
    
    def get_EchoRepliesReceived(self) -> LongType: ...
    
    def get_EchoRepliesSent(self) -> LongType: ...
    
    def get_EchoRequestsReceived(self) -> LongType: ...
    
    def get_EchoRequestsSent(self) -> LongType: ...
    
    def get_ErrorsReceived(self) -> LongType: ...
    
    def get_ErrorsSent(self) -> LongType: ...
    
    def get_MembershipQueriesReceived(self) -> LongType: ...
    
    def get_MembershipQueriesSent(self) -> LongType: ...
    
    def get_MembershipReductionsReceived(self) -> LongType: ...
    
    def get_MembershipReductionsSent(self) -> LongType: ...
    
    def get_MembershipReportsReceived(self) -> LongType: ...
    
    def get_MembershipReportsSent(self) -> LongType: ...
    
    def get_MessagesReceived(self) -> LongType: ...
    
    def get_MessagesSent(self) -> LongType: ...
    
    def get_NeighborAdvertisementsReceived(self) -> LongType: ...
    
    def get_NeighborAdvertisementsSent(self) -> LongType: ...
    
    def get_NeighborSolicitsReceived(self) -> LongType: ...
    
    def get_NeighborSolicitsSent(self) -> LongType: ...
    
    def get_PacketTooBigMessagesReceived(self) -> LongType: ...
    
    def get_PacketTooBigMessagesSent(self) -> LongType: ...
    
    def get_ParameterProblemsReceived(self) -> LongType: ...
    
    def get_ParameterProblemsSent(self) -> LongType: ...
    
    def get_RedirectsReceived(self) -> LongType: ...
    
    def get_RedirectsSent(self) -> LongType: ...
    
    def get_RouterAdvertisementsReceived(self) -> LongType: ...
    
    def get_RouterAdvertisementsSent(self) -> LongType: ...
    
    def get_RouterSolicitsReceived(self) -> LongType: ...
    
    def get_RouterSolicitsSent(self) -> LongType: ...
    
    def get_TimeExceededMessagesReceived(self) -> LongType: ...
    
    def get_TimeExceededMessagesSent(self) -> LongType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SystemMulticastIPAddressInformation(MulticastIPAddressInformation):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, addressInfo: SystemIPAddressInformation): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Address(self) -> IPAddress: ...
    
    @property
    def AddressPreferredLifetime(self) -> LongType: ...
    
    @property
    def AddressValidLifetime(self) -> LongType: ...
    
    @property
    def DhcpLeaseLifetime(self) -> LongType: ...
    
    @property
    def DuplicateAddressDetectionState(self) -> DuplicateAddressDetectionState: ...
    
    @property
    def IsDnsEligible(self) -> BooleanType: ...
    
    @property
    def IsTransient(self) -> BooleanType: ...
    
    @property
    def PrefixOrigin(self) -> PrefixOrigin: ...
    
    @property
    def SuffixOrigin(self) -> SuffixOrigin: ...
    
    # ---------- Methods ---------- #
    
    def get_Address(self) -> IPAddress: ...
    
    def get_AddressPreferredLifetime(self) -> LongType: ...
    
    def get_AddressValidLifetime(self) -> LongType: ...
    
    def get_DhcpLeaseLifetime(self) -> LongType: ...
    
    def get_DuplicateAddressDetectionState(self) -> DuplicateAddressDetectionState: ...
    
    def get_IsDnsEligible(self) -> BooleanType: ...
    
    def get_IsTransient(self) -> BooleanType: ...
    
    def get_PrefixOrigin(self) -> PrefixOrigin: ...
    
    def get_SuffixOrigin(self) -> SuffixOrigin: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SystemNetworkInterface(NetworkInterface):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Description(self) -> StringType: ...
    
    @property
    def Id(self) -> StringType: ...
    
    @property
    def IsReceiveOnly(self) -> BooleanType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NetworkInterfaceType(self) -> NetworkInterfaceType: ...
    
    @property
    def OperationalStatus(self) -> OperationalStatus: ...
    
    @property
    def Speed(self) -> LongType: ...
    
    @property
    def SupportsMulticast(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def GetIPProperties(self) -> IPInterfaceProperties: ...
    
    def GetIPStatistics(self) -> IPInterfaceStatistics: ...
    
    def GetIPv4Statistics(self) -> IPv4InterfaceStatistics: ...
    
    def GetPhysicalAddress(self) -> PhysicalAddress: ...
    
    def Supports(self, networkInterfaceComponent: NetworkInterfaceComponent) -> BooleanType: ...
    
    def get_Description(self) -> StringType: ...
    
    def get_Id(self) -> StringType: ...
    
    def get_IsReceiveOnly(self) -> BooleanType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NetworkInterfaceType(self) -> NetworkInterfaceType: ...
    
    def get_OperationalStatus(self) -> OperationalStatus: ...
    
    def get_Speed(self) -> LongType: ...
    
    def get_SupportsMulticast(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SystemTcpConnectionInformation(TcpConnectionInformation):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def LocalEndPoint(self) -> IPEndPoint: ...
    
    @property
    def RemoteEndPoint(self) -> IPEndPoint: ...
    
    @property
    def State(self) -> TcpState: ...
    
    # ---------- Methods ---------- #
    
    def get_LocalEndPoint(self) -> IPEndPoint: ...
    
    def get_RemoteEndPoint(self) -> IPEndPoint: ...
    
    def get_State(self) -> TcpState: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SystemTcpStatistics(TcpStatistics):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ConnectionsAccepted(self) -> LongType: ...
    
    @property
    def ConnectionsInitiated(self) -> LongType: ...
    
    @property
    def CumulativeConnections(self) -> LongType: ...
    
    @property
    def CurrentConnections(self) -> LongType: ...
    
    @property
    def ErrorsReceived(self) -> LongType: ...
    
    @property
    def FailedConnectionAttempts(self) -> LongType: ...
    
    @property
    def MaximumConnections(self) -> LongType: ...
    
    @property
    def MaximumTransmissionTimeout(self) -> LongType: ...
    
    @property
    def MinimumTransmissionTimeout(self) -> LongType: ...
    
    @property
    def ResetConnections(self) -> LongType: ...
    
    @property
    def ResetsSent(self) -> LongType: ...
    
    @property
    def SegmentsReceived(self) -> LongType: ...
    
    @property
    def SegmentsResent(self) -> LongType: ...
    
    @property
    def SegmentsSent(self) -> LongType: ...
    
    # ---------- Methods ---------- #
    
    def get_ConnectionsAccepted(self) -> LongType: ...
    
    def get_ConnectionsInitiated(self) -> LongType: ...
    
    def get_CumulativeConnections(self) -> LongType: ...
    
    def get_CurrentConnections(self) -> LongType: ...
    
    def get_ErrorsReceived(self) -> LongType: ...
    
    def get_FailedConnectionAttempts(self) -> LongType: ...
    
    def get_MaximumConnections(self) -> LongType: ...
    
    def get_MaximumTransmissionTimeout(self) -> LongType: ...
    
    def get_MinimumTransmissionTimeout(self) -> LongType: ...
    
    def get_ResetConnections(self) -> LongType: ...
    
    def get_ResetsSent(self) -> LongType: ...
    
    def get_SegmentsReceived(self) -> LongType: ...
    
    def get_SegmentsResent(self) -> LongType: ...
    
    def get_SegmentsSent(self) -> LongType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SystemUdpStatistics(UdpStatistics):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def DatagramsReceived(self) -> LongType: ...
    
    @property
    def DatagramsSent(self) -> LongType: ...
    
    @property
    def IncomingDatagramsDiscarded(self) -> LongType: ...
    
    @property
    def IncomingDatagramsWithErrors(self) -> LongType: ...
    
    @property
    def UdpListeners(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_DatagramsReceived(self) -> LongType: ...
    
    def get_DatagramsSent(self) -> LongType: ...
    
    def get_IncomingDatagramsDiscarded(self) -> LongType: ...
    
    def get_IncomingDatagramsWithErrors(self) -> LongType: ...
    
    def get_UdpListeners(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SystemUnicastIPAddressInformation(UnicastIPAddressInformation):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Address(self) -> IPAddress: ...
    
    @property
    def AddressPreferredLifetime(self) -> LongType: ...
    
    @property
    def AddressValidLifetime(self) -> LongType: ...
    
    @property
    def DhcpLeaseLifetime(self) -> LongType: ...
    
    @property
    def DuplicateAddressDetectionState(self) -> DuplicateAddressDetectionState: ...
    
    @property
    def IPv4Mask(self) -> IPAddress: ...
    
    @property
    def IsDnsEligible(self) -> BooleanType: ...
    
    @property
    def IsTransient(self) -> BooleanType: ...
    
    @property
    def PrefixLength(self) -> IntType: ...
    
    @property
    def PrefixOrigin(self) -> PrefixOrigin: ...
    
    @property
    def SuffixOrigin(self) -> SuffixOrigin: ...
    
    # ---------- Methods ---------- #
    
    def get_Address(self) -> IPAddress: ...
    
    def get_AddressPreferredLifetime(self) -> LongType: ...
    
    def get_AddressValidLifetime(self) -> LongType: ...
    
    def get_DhcpLeaseLifetime(self) -> LongType: ...
    
    def get_DuplicateAddressDetectionState(self) -> DuplicateAddressDetectionState: ...
    
    def get_IPv4Mask(self) -> IPAddress: ...
    
    def get_IsDnsEligible(self) -> BooleanType: ...
    
    def get_IsTransient(self) -> BooleanType: ...
    
    def get_PrefixLength(self) -> IntType: ...
    
    def get_PrefixOrigin(self) -> PrefixOrigin: ...
    
    def get_SuffixOrigin(self) -> SuffixOrigin: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TcpConnectionInformation(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def LocalEndPoint(self) -> IPEndPoint: ...
    
    @property
    def RemoteEndPoint(self) -> IPEndPoint: ...
    
    @property
    def State(self) -> TcpState: ...
    
    # ---------- Methods ---------- #
    
    def get_LocalEndPoint(self) -> IPEndPoint: ...
    
    def get_RemoteEndPoint(self) -> IPEndPoint: ...
    
    def get_State(self) -> TcpState: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TcpStatistics(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ConnectionsAccepted(self) -> LongType: ...
    
    @property
    def ConnectionsInitiated(self) -> LongType: ...
    
    @property
    def CumulativeConnections(self) -> LongType: ...
    
    @property
    def CurrentConnections(self) -> LongType: ...
    
    @property
    def ErrorsReceived(self) -> LongType: ...
    
    @property
    def FailedConnectionAttempts(self) -> LongType: ...
    
    @property
    def MaximumConnections(self) -> LongType: ...
    
    @property
    def MaximumTransmissionTimeout(self) -> LongType: ...
    
    @property
    def MinimumTransmissionTimeout(self) -> LongType: ...
    
    @property
    def ResetConnections(self) -> LongType: ...
    
    @property
    def ResetsSent(self) -> LongType: ...
    
    @property
    def SegmentsReceived(self) -> LongType: ...
    
    @property
    def SegmentsResent(self) -> LongType: ...
    
    @property
    def SegmentsSent(self) -> LongType: ...
    
    # ---------- Methods ---------- #
    
    def get_ConnectionsAccepted(self) -> LongType: ...
    
    def get_ConnectionsInitiated(self) -> LongType: ...
    
    def get_CumulativeConnections(self) -> LongType: ...
    
    def get_CurrentConnections(self) -> LongType: ...
    
    def get_ErrorsReceived(self) -> LongType: ...
    
    def get_FailedConnectionAttempts(self) -> LongType: ...
    
    def get_MaximumConnections(self) -> LongType: ...
    
    def get_MaximumTransmissionTimeout(self) -> LongType: ...
    
    def get_MinimumTransmissionTimeout(self) -> LongType: ...
    
    def get_ResetConnections(self) -> LongType: ...
    
    def get_ResetsSent(self) -> LongType: ...
    
    def get_SegmentsReceived(self) -> LongType: ...
    
    def get_SegmentsResent(self) -> LongType: ...
    
    def get_SegmentsSent(self) -> LongType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TeredoHelper(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def UnsafeNotifyStableUnicastIpAddressTable(callback: Action[ObjectType], state: ObjectType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UdpStatistics(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def DatagramsReceived(self) -> LongType: ...
    
    @property
    def DatagramsSent(self) -> LongType: ...
    
    @property
    def IncomingDatagramsDiscarded(self) -> LongType: ...
    
    @property
    def IncomingDatagramsWithErrors(self) -> LongType: ...
    
    @property
    def UdpListeners(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_DatagramsReceived(self) -> LongType: ...
    
    def get_DatagramsSent(self) -> LongType: ...
    
    def get_IncomingDatagramsDiscarded(self) -> LongType: ...
    
    def get_IncomingDatagramsWithErrors(self) -> LongType: ...
    
    def get_UdpListeners(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UnicastIPAddressInformation(ABC, IPAddressInformation):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AddressPreferredLifetime(self) -> LongType: ...
    
    @property
    def AddressValidLifetime(self) -> LongType: ...
    
    @property
    def DhcpLeaseLifetime(self) -> LongType: ...
    
    @property
    def DuplicateAddressDetectionState(self) -> DuplicateAddressDetectionState: ...
    
    @property
    def IPv4Mask(self) -> IPAddress: ...
    
    @property
    def PrefixLength(self) -> IntType: ...
    
    @property
    def PrefixOrigin(self) -> PrefixOrigin: ...
    
    @property
    def SuffixOrigin(self) -> SuffixOrigin: ...
    
    # ---------- Methods ---------- #
    
    def get_AddressPreferredLifetime(self) -> LongType: ...
    
    def get_AddressValidLifetime(self) -> LongType: ...
    
    def get_DhcpLeaseLifetime(self) -> LongType: ...
    
    def get_DuplicateAddressDetectionState(self) -> DuplicateAddressDetectionState: ...
    
    def get_IPv4Mask(self) -> IPAddress: ...
    
    def get_PrefixLength(self) -> IntType: ...
    
    def get_PrefixOrigin(self) -> PrefixOrigin: ...
    
    def get_SuffixOrigin(self) -> SuffixOrigin: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UnicastIPAddressInformationCollection(ObjectType, ICollection[UnicastIPAddressInformation], IEnumerable[UnicastIPAddressInformation], IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsReadOnly(self) -> BooleanType: ...
    
    @property
    def Item(self) -> UnicastIPAddressInformation: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, address: UnicastIPAddressInformation) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def Contains(self, address: UnicastIPAddressInformation) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[UnicastIPAddressInformation], offset: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator[UnicastIPAddressInformation]: ...
    
    def Remove(self, address: UnicastIPAddressInformation) -> BooleanType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsReadOnly(self) -> BooleanType: ...
    
    def get_Item(self, index: IntType) -> UnicastIPAddressInformation: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UnsafeNetInfoNativeMethods(ABC, ObjectType):
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


# ---------- Structs ---------- #

class FIXED_INFO(ValueType):
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


class FixedInfo(ValueType):
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


class IPOptions(ValueType):
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


class Icmp6EchoReply(ValueType):
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


class IcmpEchoReply(ValueType):
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


class IpAdapterAddress(ValueType):
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


class IpAdapterAddresses(ValueType):
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


class IpAdapterUnicastAddress(ValueType):
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


class IpAddrString(ValueType):
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


class IpPerAdapterInfo(ValueType):
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


class IpSocketAddress(ValueType):
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


class Ipv6Address(ValueType):
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


class MibIcmpInfo(ValueType):
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


class MibIcmpInfoEx(ValueType):
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


class MibIcmpStats(ValueType):
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


class MibIcmpStatsEx(ValueType):
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


class MibIfRow2(ValueType):
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


class MibIpStats(ValueType):
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


class MibTcp6RowOwnerPid(ValueType):
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


class MibTcp6TableOwnerPid(ValueType):
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


class MibTcpRow(ValueType):
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


class MibTcpStats(ValueType):
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


class MibTcpTable(ValueType):
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


class MibUdp6RowOwnerPid(ValueType):
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


class MibUdp6TableOwnerPid(ValueType):
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


class MibUdpRow(ValueType):
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


class MibUdpStats(ValueType):
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


class MibUdpTable(ValueType):
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


# No Interfaces

# ---------- Enums ---------- #

class AdapterAddressFlags(Enum):
    DnsEligible: IntType = 1
    Transient: IntType = 2


class AdapterFlags(Enum):
    DnsEnabled: IntType = 1
    RegisterAdapterSuffix: IntType = 2
    DhcpEnabled: IntType = 4
    ReceiveOnly: IntType = 8
    NoMulticast: IntType = 16
    Ipv6OtherStatefulConfig: IntType = 32
    NetBiosOverTcp: IntType = 64
    IPv4Enabled: IntType = 128
    IPv6Enabled: IntType = 256
    IPv6ManagedAddressConfigurationSupported: IntType = 512


class DuplicateAddressDetectionState(Enum):
    Invalid: IntType = 0
    Tentative: IntType = 1
    Duplicate: IntType = 2
    Deprecated: IntType = 3
    Preferred: IntType = 4


class GetAdaptersAddressesFlags(Enum):
    SkipUnicast: IntType = 1
    SkipAnycast: IntType = 2
    SkipMulticast: IntType = 4
    SkipDnsServer: IntType = 8
    IncludePrefix: IntType = 16
    SkipFriendlyName: IntType = 32
    IncludeWins: IntType = 64
    IncludeGateways: IntType = 128
    IncludeAllInterfaces: IntType = 256
    IncludeAllCompartments: IntType = 512
    IncludeTunnelBindingOrder: IntType = 1024


class IPStatus(Enum):
    Unknown: IntType = -1
    Success: IntType = 0
    DestinationNetworkUnreachable: IntType = 11002
    DestinationHostUnreachable: IntType = 11003
    DestinationProhibited: IntType = 11004
    DestinationProtocolUnreachable: IntType = 11004
    DestinationPortUnreachable: IntType = 11005
    NoResources: IntType = 11006
    BadOption: IntType = 11007
    HardwareError: IntType = 11008
    PacketTooBig: IntType = 11009
    TimedOut: IntType = 11010
    BadRoute: IntType = 11012
    TtlExpired: IntType = 11013
    TtlReassemblyTimeExceeded: IntType = 11014
    ParameterProblem: IntType = 11015
    SourceQuench: IntType = 11016
    BadDestination: IntType = 11018
    DestinationUnreachable: IntType = 11040
    TimeExceeded: IntType = 11041
    BadHeader: IntType = 11042
    UnrecognizedNextHeader: IntType = 11043
    IcmpError: IntType = 11044
    DestinationScopeMismatch: IntType = 11045


class IcmpV4Code(Enum):
    ICMP4_UNREACH_NET: IntType = 0
    ICMP4_UNREACH_HOST: IntType = 1
    ICMP4_UNREACH_PROTOCOL: IntType = 2
    ICMP4_UNREACH_PORT: IntType = 3
    ICMP4_UNREACH_FRAG_NEEDED: IntType = 4
    ICMP4_UNREACH_SOURCEROUTE_FAILED: IntType = 5
    ICMP4_UNREACH_NET_UNKNOWN: IntType = 6
    ICMP4_UNREACH_HOST_UNKNOWN: IntType = 7
    ICMP4_UNREACH_ISOLATED: IntType = 8
    ICMP4_UNREACH_NET_ADMIN: IntType = 9
    ICMP4_UNREACH_HOST_ADMIN: IntType = 10
    ICMP4_UNREACH_NET_TOS: IntType = 11
    ICMP4_UNREACH_HOST_TOS: IntType = 12
    ICMP4_UNREACH_ADMIN: IntType = 13


class IcmpV4Type(Enum):
    ICMP4_ECHO_REPLY: IntType = 0
    ICMP4_DST_UNREACH: IntType = 3
    ICMP4_SOURCE_QUENCH: IntType = 4
    ICMP4_REDIRECT: IntType = 5
    ICMP4_ECHO_REQUEST: IntType = 8
    ICMP4_ROUTER_ADVERT: IntType = 9
    ICMP4_ROUTER_SOLICIT: IntType = 10
    ICMP4_TIME_EXCEEDED: IntType = 11
    ICMP4_PARAM_PROB: IntType = 12
    ICMP4_TIMESTAMP_REQUEST: IntType = 13
    ICMP4_TIMESTAMP_REPLY: IntType = 14
    ICMP4_MASK_REQUEST: IntType = 17
    ICMP4_MASK_REPLY: IntType = 18


class IcmpV6StatType(Enum):
    DestinationUnreachable: IntType = 1
    PacketTooBig: IntType = 2
    TimeExceeded: IntType = 3
    ParameterProblem: IntType = 4
    EchoRequest: IntType = 128
    EchoReply: IntType = 129
    MembershipQuery: IntType = 130
    MembershipReport: IntType = 131
    MembershipReduction: IntType = 132
    RouterSolicit: IntType = 133
    RouterAdvertisement: IntType = 134
    NeighborSolict: IntType = 135
    NeighborAdvertisement: IntType = 136
    Redirect: IntType = 137


class InterfaceConnectionType(Enum):
    Dedicated: IntType = 1
    Passive: IntType = 2
    Demand: IntType = 3
    Maximum: IntType = 4


class InterfaceTunnelType(Enum):
    #None: IntType = 0
    Other: IntType = 1
    Direct: IntType = 2
    SixToFour: IntType = 11
    Isatap: IntType = 13
    Teredo: IntType = 14
    IpHttps: IntType = 15


class NetBiosNodeType(Enum):
    Unknown: IntType = 0
    Broadcast: IntType = 1
    Peer2Peer: IntType = 2
    Mixed: IntType = 4
    Hybrid: IntType = 8


class NetworkInformationAccess(Enum):
    #None: IntType = 0
    Read: IntType = 1
    Ping: IntType = 4


class NetworkInterfaceComponent(Enum):
    IPv4: IntType = 0
    IPv6: IntType = 1


class NetworkInterfaceType(Enum):
    Unknown: IntType = 1
    Ethernet: IntType = 6
    TokenRing: IntType = 9
    Fddi: IntType = 15
    BasicIsdn: IntType = 20
    PrimaryIsdn: IntType = 21
    Ppp: IntType = 23
    Loopback: IntType = 24
    Ethernet3Megabit: IntType = 26
    Slip: IntType = 28
    Atm: IntType = 37
    GenericModem: IntType = 48
    FastEthernetT: IntType = 62
    Isdn: IntType = 63
    FastEthernetFx: IntType = 69
    Wireless80211: IntType = 71
    AsymmetricDsl: IntType = 94
    RateAdaptDsl: IntType = 95
    SymmetricDsl: IntType = 96
    VeryHighSpeedDsl: IntType = 97
    IPOverAtm: IntType = 114
    GigabitEthernet: IntType = 117
    Tunnel: IntType = 131
    MultiRateSymmetricDsl: IntType = 143
    HighPerformanceSerialBus: IntType = 144
    Wman: IntType = 237
    Wwanpp: IntType = 243
    Wwanpp2: IntType = 244


class OldOperationalStatus(Enum):
    NonOperational: IntType = 0
    Unreachable: IntType = 1
    Disconnected: IntType = 2
    Connecting: IntType = 3
    Connected: IntType = 4
    Operational: IntType = 5


class OperationalStatus(Enum):
    Up: IntType = 1
    Down: IntType = 2
    Testing: IntType = 3
    Unknown: IntType = 4
    Dormant: IntType = 5
    NotPresent: IntType = 6
    LowerLayerDown: IntType = 7


class PrefixOrigin(Enum):
    Other: IntType = 0
    Manual: IntType = 1
    WellKnown: IntType = 2
    Dhcp: IntType = 3
    RouterAdvertisement: IntType = 4


class ScopeLevel(Enum):
    #None: IntType = 0
    Interface: IntType = 1
    Link: IntType = 2
    Subnet: IntType = 3
    Admin: IntType = 4
    Site: IntType = 5
    Organization: IntType = 8
    Global: IntType = 14


class StartIPOptions(Enum):
    #None: IntType = 0
    StartIPv4: IntType = 1
    StartIPv6: IntType = 2
    Both: IntType = 3


class SuffixOrigin(Enum):
    Other: IntType = 0
    Manual: IntType = 1
    WellKnown: IntType = 2
    OriginDhcp: IntType = 3
    LinkLayerAddress: IntType = 4
    Random: IntType = 5


class TcpState(Enum):
    Unknown: IntType = 0
    Closed: IntType = 1
    Listen: IntType = 2
    SynSent: IntType = 3
    SynReceived: IntType = 4
    Established: IntType = 5
    FinWait1: IntType = 6
    FinWait2: IntType = 7
    CloseWait: IntType = 8
    Closing: IntType = 9
    LastAck: IntType = 10
    TimeWait: IntType = 11
    DeleteTcb: IntType = 12


class TcpTableClass(Enum):
    TcpTableBasicListener: IntType = 0
    TcpTableBasicConnections: IntType = 1
    TcpTableBasicAll: IntType = 2
    TcpTableOwnerPidListener: IntType = 3
    TcpTableOwnerPidConnections: IntType = 4
    TcpTableOwnerPidAll: IntType = 5
    TcpTableOwnerModuleListener: IntType = 6
    TcpTableOwnerModuleConnections: IntType = 7
    TcpTableOwnerModuleAll: IntType = 8


class UdpTableClass(Enum):
    UdpTableBasic: IntType = 0
    UdpTableOwnerPid: IntType = 1
    UdpTableOwnerModule: IntType = 2


# ---------- Delegates ---------- #

NetworkAddressChangedEventHandler = Callable[[ObjectType, EventArgs], VoidType]

NetworkAvailabilityChangedEventHandler = Callable[[ObjectType, NetworkAvailabilityEventArgs], VoidType]

PingCompletedEventHandler = Callable[[ObjectType, PingCompletedEventArgs], VoidType]

StableUnicastIpAddressTableDelegate = Callable[[NIntType, NIntType], VoidType]

__all__ = [
    GatewayIPAddressInformation,
    GatewayIPAddressInformationCollection,
    IPAddressCollection,
    IPAddressInformation,
    IPAddressInformationCollection,
    IPGlobalProperties,
    IPGlobalStatistics,
    IPInterfaceProperties,
    IPInterfaceStatistics,
    IPv4InterfaceProperties,
    IPv4InterfaceStatistics,
    IPv6InterfaceProperties,
    IcmpV4Statistics,
    IcmpV6Statistics,
    IpHelperErrors,
    MulticastIPAddressInformation,
    MulticastIPAddressInformationCollection,
    NetworkAddressChangedEventHandler,
    NetworkAvailabilityChangedEventHandler,
    NetworkAvailabilityEventArgs,
    NetworkChange,
    NetworkInformationException,
    NetworkInformationPermission,
    NetworkInformationPermissionAttribute,
    NetworkInterface,
    PhysicalAddress,
    Ping,
    PingCompletedEventArgs,
    PingCompletedEventHandler,
    PingException,
    PingOptions,
    PingReply,
    SafeCancelMibChangeNotify,
    SafeFreeMibTable,
    StableUnicastIpAddressTableDelegate,
    SystemGatewayIPAddressInformation,
    SystemIPAddressInformation,
    SystemIPGlobalProperties,
    SystemIPGlobalStatistics,
    SystemIPInterfaceProperties,
    SystemIPInterfaceStatistics,
    SystemIPv4InterfaceProperties,
    SystemIPv4InterfaceStatistics,
    SystemIPv6InterfaceProperties,
    SystemIcmpV4Statistics,
    SystemIcmpV6Statistics,
    SystemMulticastIPAddressInformation,
    SystemNetworkInterface,
    SystemTcpConnectionInformation,
    SystemTcpStatistics,
    SystemUdpStatistics,
    SystemUnicastIPAddressInformation,
    TcpConnectionInformation,
    TcpStatistics,
    TeredoHelper,
    UdpStatistics,
    UnicastIPAddressInformation,
    UnicastIPAddressInformationCollection,
    UnsafeNetInfoNativeMethods,
    FIXED_INFO,
    FixedInfo,
    IPOptions,
    Icmp6EchoReply,
    IcmpEchoReply,
    IpAdapterAddress,
    IpAdapterAddresses,
    IpAdapterUnicastAddress,
    IpAddrString,
    IpPerAdapterInfo,
    IpSocketAddress,
    Ipv6Address,
    MibIcmpInfo,
    MibIcmpInfoEx,
    MibIcmpStats,
    MibIcmpStatsEx,
    MibIfRow2,
    MibIpStats,
    MibTcp6RowOwnerPid,
    MibTcp6TableOwnerPid,
    MibTcpRow,
    MibTcpStats,
    MibTcpTable,
    MibUdp6RowOwnerPid,
    MibUdp6TableOwnerPid,
    MibUdpRow,
    MibUdpStats,
    MibUdpTable,
    AdapterAddressFlags,
    AdapterFlags,
    DuplicateAddressDetectionState,
    GetAdaptersAddressesFlags,
    IPStatus,
    IcmpV4Code,
    IcmpV4Type,
    IcmpV6StatType,
    InterfaceConnectionType,
    InterfaceTunnelType,
    NetBiosNodeType,
    NetworkInformationAccess,
    NetworkInterfaceComponent,
    NetworkInterfaceType,
    OldOperationalStatus,
    OperationalStatus,
    PrefixOrigin,
    ScopeLevel,
    StartIPOptions,
    SuffixOrigin,
    TcpState,
    TcpTableClass,
    UdpTableClass,
    NetworkAddressChangedEventHandler,
    NetworkAvailabilityChangedEventHandler,
    PingCompletedEventHandler,
    StableUnicastIpAddressTableDelegate,
]
