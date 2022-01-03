__all__ = [
    'AuthenticatedStream',
    'CipherSuitesPolicy',
    'NegotiateStream',
    'SslCertificateTrust',
    'SslClientAuthenticationOptions',
    'SslServerAuthenticationOptions',
    'SslStream',
    'SslStreamCertificateContext',
    'SslApplicationProtocol',
    'SslClientHelloInfo',
    'AuthenticationLevel',
    'EncryptionPolicy',
    'ProtectionLevel',
    'SslPolicyErrors',
    'TlsCipherSuite',
    'LocalCertificateSelectionCallback',
    'RemoteCertificateValidationCallback',
    'ServerCertificateSelectionCallback',
    'ServerOptionsSelectionCallback',
]


# TODO

# ---------- CLASSES ---------- #

class AuthenticatedStream:
    """Provides methods for passing credentials across a stream and requesting or performing authentication for client-server applications."""


class CipherSuitesPolicy:
    """Specifies allowed cipher suites."""


class NegotiateStream:
    """Provides a stream that uses the Negotiate security protocol to authenticate the client, and optionally the server, in client-server communication."""


class SslCertificateTrust:
    """Represents a trust policy for use with SSL/TLS connections."""


class SslClientAuthenticationOptions:
    """Represents a client authentication property bag for the SslStream."""


class SslServerAuthenticationOptions:
    """This struct represents a server authentication property bag for the SslStream."""


class SslStream:
    """Provides a stream used for client-server communication that uses the Secure Socket Layer (SSL) security protocol to authenticate the server and optionally the client."""


class SslStreamCertificateContext:
    """Represents a set of certificates used for building a certificate chain."""


# ---------- STRUCTS ---------- #

class SslApplicationProtocol:
    """Represents a value of TLS Application protocol."""


class SslClientHelloInfo:
    """This struct contains information from received TLS Client Hello frame."""


# ---------- ENUMS ---------- #

class AuthenticationLevel:
    """Specifies client requirements for authentication and impersonation when using the WebRequest class and derived classes to request a resource."""


class EncryptionPolicy:
    """The EncryptionPolicy to use."""


class ProtectionLevel:
    """Indicates the security services requested for an authenticated stream."""


class SslPolicyErrors:
    """Enumerates Secure Socket Layer (SSL) policy errors."""


class TlsCipherSuite:
    """Represents cipher suite values for the TLS (formerly SSL) protocol."""


# ---------- DELEGATES ---------- #

class LocalCertificateSelectionCallback:
    """Selects the local Secure Sockets Layer (SSL) certificate used for authentication."""


class RemoteCertificateValidationCallback:
    """Verifies the remote Secure Sockets Layer (SSL) certificate used for authentication."""


class ServerCertificateSelectionCallback:
    """Selects the server Secure Sockets Layer (SSL) certificate."""


class ServerOptionsSelectionCallback:
    """Represents the asynchronous callback method that will select session properties based on the name requested by the client."""
