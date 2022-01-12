from __future__ import annotations

from typing import Union, overload

from System import Enum, Exception, Int32, String, SystemException
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import ISerializable

# ---------- Types ---------- #

IntType = Union[int, Int32]
StringType = Union[str, String]


# ---------- Classes ---------- #

class AuthenticationException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
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


class InvalidCredentialException(AuthenticationException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
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


# No Structs

# No Interfaces

# ---------- Enums ---------- #

class CipherAlgorithmType(Enum):
    #None = 0
    Null = 24576
    Des = 26113
    Rc2 = 26114
    TripleDes = 26115
    Aes128 = 26126
    Aes192 = 26127
    Aes256 = 26128
    Aes = 26129
    Rc4 = 26625


class ExchangeAlgorithmType(Enum):
    #None = 0
    RsaSign = 9216
    RsaKeyX = 41984
    DiffieHellman = 43522


class HashAlgorithmType(Enum):
    #None = 0
    Md5 = 32771
    Sha1 = 32772
    Sha256 = 32780
    Sha384 = 32781
    Sha512 = 32782


class SslProtocols(Enum):
    #None = 0
    Ssl2 = 12
    Ssl3 = 48
    Tls = 192
    Default = 240
    Tls11 = 768
    Tls12 = 3072
    Tls13 = 12288


# No Delegates

__all__ = [
    AuthenticationException,
    InvalidCredentialException,
    CipherAlgorithmType,
    ExchangeAlgorithmType,
    HashAlgorithmType,
    SslProtocols,
]
