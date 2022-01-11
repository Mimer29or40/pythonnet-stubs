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
    #None: IntType = 0
    Null: IntType = 24576
    Des: IntType = 26113
    Rc2: IntType = 26114
    TripleDes: IntType = 26115
    Aes128: IntType = 26126
    Aes192: IntType = 26127
    Aes256: IntType = 26128
    Aes: IntType = 26129
    Rc4: IntType = 26625


class CipherAlgorithmType(Enum):
    #None: IntType = 0
    Null: IntType = 24576
    Des: IntType = 26113
    Rc2: IntType = 26114
    TripleDes: IntType = 26115
    Aes128: IntType = 26126
    Aes192: IntType = 26127
    Aes256: IntType = 26128
    Aes: IntType = 26129
    Rc4: IntType = 26625


class ExchangeAlgorithmType(Enum):
    #None: IntType = 0
    RsaSign: IntType = 9216
    RsaKeyX: IntType = 41984
    DiffieHellman: IntType = 43522


class ExchangeAlgorithmType(Enum):
    #None: IntType = 0
    RsaSign: IntType = 9216
    RsaKeyX: IntType = 41984
    DiffieHellman: IntType = 43522


class HashAlgorithmType(Enum):
    #None: IntType = 0
    Md5: IntType = 32771
    Sha1: IntType = 32772
    Sha256: IntType = 32780
    Sha384: IntType = 32781
    Sha512: IntType = 32782


class HashAlgorithmType(Enum):
    #None: IntType = 0
    Md5: IntType = 32771
    Sha1: IntType = 32772
    Sha256: IntType = 32780
    Sha384: IntType = 32781
    Sha512: IntType = 32782


class SslProtocols(Enum):
    #None: IntType = 0
    Ssl2: IntType = 12
    Ssl3: IntType = 48
    Tls: IntType = 192
    Default: IntType = 240
    Tls11: IntType = 768
    Tls12: IntType = 3072
    Tls13: IntType = 12288


class SslProtocols(Enum):
    #None: IntType = 0
    Ssl2: IntType = 12
    Ssl3: IntType = 48
    Tls: IntType = 192
    Default: IntType = 240
    Tls11: IntType = 768
    Tls12: IntType = 3072
    Tls13: IntType = 12288


# No Delegates

__all__ = [
    AuthenticationException,
    InvalidCredentialException,
    CipherAlgorithmType,
    ExchangeAlgorithmType,
    HashAlgorithmType,
    SslProtocols,
]
