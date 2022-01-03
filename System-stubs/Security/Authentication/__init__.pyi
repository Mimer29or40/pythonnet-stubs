__all__ = [
    'AuthenticationException',
    'InvalidCredentialException',
    'CipherAlgorithmType',
    'ExchangeAlgorithmType',
    'HashAlgorithmType',
    'SslProtocols',
]


# TODO

# ---------- CLASSES ---------- #

class AuthenticationException:
    """The exception that is thrown when authentication fails for an authentication stream."""


class InvalidCredentialException:
    """The exception that is thrown when authentication fails for an authentication stream and cannot be retried."""


# ---------- ENUMS ---------- #

class CipherAlgorithmType:
    """Defines the possible cipher algorithms for the SslStream class."""


class ExchangeAlgorithmType:
    """Specifies the algorithm used to create keys shared by the client and server."""


class HashAlgorithmType:
    """Specifies the algorithm used for generating message authentication codes (MACs)."""


class SslProtocols:
    """Defines the possible versions of SslProtocols."""
