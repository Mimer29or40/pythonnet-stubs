__all__ = [
    'GatewayIPAddressInformation',
    'GatewayIPAddressInformationCollection',
    'IcmpV4Statistics',
    'IcmpV6Statistics',
    'IPAddressCollection',
    'IPAddressInformation',
    'IPAddressInformationCollection',
    'IPGlobalProperties',
    'IPGlobalStatistics',
    'IPInterfaceProperties',
    'IPInterfaceStatistics',
    'IPv4InterfaceProperties',
    'IPv4InterfaceStatistics',
    'IPv6InterfaceProperties',
    'MulticastIPAddressInformation',
    'MulticastIPAddressInformationCollection',
    'NetworkAvailabilityEventArgs',
    'NetworkChange',
    'NetworkInformationException',
    'NetworkInterface',
    'PhysicalAddress',
    'Ping',
    'PingCompletedEventArgs',
    'PingException',
    'PingOptions',
    'PingReply',
    'TcpConnectionInformation',
    'TcpStatistics',
    'UdpStatistics',
    'UnicastIPAddressInformation',
    'UnicastIPAddressInformationCollection',
    'DuplicateAddressDetectionState',
    'IPStatus',
    'NetBiosNodeType',
    'NetworkInterfaceComponent',
    'NetworkInterfaceType',
    'OperationalStatus',
    'PrefixOrigin',
    'ScopeLevel',
    'SuffixOrigin',
    'TcpState',
    'NetworkAddressChangedEventHandler',
    'NetworkAvailabilityChangedEventHandler',
    'PingCompletedEventHandler',
]


# TODO

# ---------- CLASSES ---------- #

class GatewayIPAddressInformation:
    """Represents the IP address of the network gateway. This class cannot be instantiated."""


class GatewayIPAddressInformationCollection:
    """Stores a set of GatewayIPAddressInformation types."""


class IcmpV4Statistics:
    """Provides Internet Control Message Protocol for IPv4 (ICMPv4) statistical data for the local computer."""


class IcmpV6Statistics:
    """Provides Internet Control Message Protocol for Internet Protocol version 6 (ICMPv6) statistical data for the local computer."""


class IPAddressCollection:
    """Stores a set of IPAddress types."""


class IPAddressInformation:
    """Provides information about a network interface address."""


class IPAddressInformationCollection:
    """Stores a set of IPAddressInformation types."""


class IPGlobalProperties:
    """Provides information about the network connectivity of the local computer."""


class IPGlobalStatistics:
    """Provides Internet Protocol (IP) statistical data."""


class IPInterfaceProperties:
    """Provides information about network interfaces that support Internet Protocol version 4 (IPv4) or Internet Protocol version 6 (IPv6)."""


class IPInterfaceStatistics:
    """Provides Internet Protocol (IP) statistical data for an network interface on the local computer."""


class IPv4InterfaceProperties:
    """Provides information about network interfaces that support Internet Protocol version 4 (IPv4)."""


class IPv4InterfaceStatistics:
    """Provides statistical data for a network interface on the local computer."""


class IPv6InterfaceProperties:
    """Provides information about network interfaces that support Internet Protocol version 6 (IPv6)."""


class MulticastIPAddressInformation:
    """Provides information about a network interface's multicast address."""


class MulticastIPAddressInformationCollection:
    """Stores a set of MulticastIPAddressInformation types."""


class NetworkAvailabilityEventArgs:
    """Provides data for the NetworkAvailabilityChanged event."""


class NetworkChange:
    """Allows applications to receive notification when the Internet Protocol (IP) address of a network interface, also called a network card or adapter, changes."""


class NetworkInformationException:
    """The exception that is thrown when an error occurs while retrieving network information."""


class NetworkInterface:
    """Provides configuration and statistical information for a network interface."""


class PhysicalAddress:
    """Provides the Media Access Control (MAC) address for a network interface (adapter)."""


class Ping:
    """Allows an application to determine whether a remote computer is accessible over the network."""


class PingCompletedEventArgs:
    """Provides data for the PingCompleted event."""


class PingException:
    """The exception that is thrown when a Send or SendAsync method calls a method that throws an exception."""


class PingOptions:
    """Used to control how Ping data packets are transmitted."""


class PingReply:
    """Provides information about the status and data resulting from a Send or SendAsync operation."""


class TcpConnectionInformation:
    """Provides information about the Transmission Control Protocol (TCP) connections on the local computer."""


class TcpStatistics:
    """Provides Transmission Control Protocol (TCP) statistical data."""


class UdpStatistics:
    """Provides User Datagram Protocol (UDP) statistical data."""


class UnicastIPAddressInformation:
    """Provides information about a network interface's unicast address."""


class UnicastIPAddressInformationCollection:
    """Stores a set of UnicastIPAddressInformation types."""


# ---------- ENUMS ---------- #

class DuplicateAddressDetectionState:
    """Specifies the current state of an IP address."""


class IPStatus:
    """Reports the status of sending an Internet Control Message Protocol (ICMP) echo message to a computer."""


class NetBiosNodeType:
    """Specifies the Network Basic Input/Output System (NetBIOS) node type."""


class NetworkInterfaceComponent:
    """Specifies the Internet Protocol versions that are supported by a network interface."""


class NetworkInterfaceType:
    """Specifies types of network interfaces."""


class OperationalStatus:
    """Specifies the operational state of a network interface."""


class PrefixOrigin:
    """Specifies how an IP address network prefix was located."""


class ScopeLevel:
    """The scope level for an IPv6 address."""


class SuffixOrigin:
    """Specifies how an IP address host suffix was located."""


class TcpState:
    """Specifies the states of a Transmission Control Protocol (TCP) connection."""


# ---------- DELEGATES ---------- #

class NetworkAddressChangedEventHandler:
    """References one or more methods to be called when the address of a network interface changes."""


class NetworkAvailabilityChangedEventHandler:
    """References one or more methods to be called when the availability of the network changes."""


class PingCompletedEventHandler:
    """Represents the method that will handle the PingCompleted event of a Ping object."""
