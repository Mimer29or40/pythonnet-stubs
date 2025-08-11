"""Automatically generated stubs for C# namespace: System.Security.Authentication."""

from typing import overload

from System import Enum
from System import Exception
from System import SystemException
from System import Type
from System.Collections import IDictionary
from System.Reflection import MethodBase
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AuthenticationException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CipherAlgorithmType(Enum):
    """"""

    _None: CipherAlgorithmType = ...
    """"""
    Null: CipherAlgorithmType = ...
    """"""
    Des: CipherAlgorithmType = ...
    """"""
    Rc2: CipherAlgorithmType = ...
    """"""
    TripleDes: CipherAlgorithmType = ...
    """"""
    Aes128: CipherAlgorithmType = ...
    """"""
    Aes192: CipherAlgorithmType = ...
    """"""
    Aes256: CipherAlgorithmType = ...
    """"""
    Aes: CipherAlgorithmType = ...
    """"""
    Rc4: CipherAlgorithmType = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class ExchangeAlgorithmType(Enum):
    """"""

    _None: ExchangeAlgorithmType = ...
    """"""
    RsaSign: ExchangeAlgorithmType = ...
    """"""
    RsaKeyX: ExchangeAlgorithmType = ...
    """"""
    DiffieHellman: ExchangeAlgorithmType = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class HashAlgorithmType(Enum):
    """"""

    _None: HashAlgorithmType = ...
    """"""
    Md5: HashAlgorithmType = ...
    """"""
    Sha1: HashAlgorithmType = ...
    """"""
    Sha256: HashAlgorithmType = ...
    """"""
    Sha384: HashAlgorithmType = ...
    """"""
    Sha512: HashAlgorithmType = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class InvalidCredentialException(AuthenticationException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class SslProtocols(Enum):
    """"""

    _None: SslProtocols = ...
    """"""
    Ssl2: SslProtocols = ...
    """"""
    Ssl3: SslProtocols = ...
    """"""
    Tls: SslProtocols = ...
    """"""
    Default: SslProtocols = ...
    """"""
    Tls11: SslProtocols = ...
    """"""
    Tls12: SslProtocols = ...
    """"""
    Tls13: SslProtocols = ...
    """"""
