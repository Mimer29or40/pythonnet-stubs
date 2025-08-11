"""Automatically generated stubs for C# namespace: System.Security.Cryptography."""

from abc import ABC
from collections.abc import Iterator
from typing import Final
from typing import overload

from Internal.Cryptography import ICngSymmetricAlgorithm
from Microsoft.Win32.SafeHandles import SafeBCryptAlgorithmHandle
from Microsoft.Win32.SafeHandles import SafeBCryptKeyHandle
from Microsoft.Win32.SafeHandles import SafeCapiKeyHandle
from Microsoft.Win32.SafeHandles import SafeCspHandle
from Microsoft.Win32.SafeHandles import SafeHandleZeroOrMinusOneIsInvalid
from Microsoft.Win32.SafeHandles import SafeNCryptKeyHandle
from Microsoft.Win32.SafeHandles import SafeNCryptProviderHandle
from Microsoft.Win32.SafeHandles import SafeNCryptSecretHandle
from System import ActivationContext
from System import Array
from System import AsyncCallback
from System import Boolean
from System import Enum
from System import Exception
from System import IAsyncResult
from System import IDisposable
from System import IEquatable
from System import IntPtr
from System import Object
from System import SystemException
from System import Type
from System import ValueType
from System.Collections import IDictionary
from System.Collections import IEnumerator
from System.Collections.Generic import ICollection
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IEnumerator
from System.Collections.Generic import IList
from System.Collections.Generic import IReadOnlyCollection
from System.Collections.Generic import IReadOnlyList
from System.Collections.ObjectModel import Collection
from System.Collections.ObjectModel import ReadOnlyCollection
from System.IO import SeekOrigin
from System.IO import Stream
from System.Reflection import MethodBase
from System.Runtime.InteropServices import _Exception
from System.Runtime.Remoting import ObjRef
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Security import ManifestKinds
from System.Security import SecureString
from System.Security import SecurityElement
from System.Security.AccessControl import CryptoKeySecurity
from System.Threading import CancellationToken
from System.Threading.Tasks import Task

from .X509Certificates import AuthenticodeSignatureInformation
from .X509Certificates import X509RevocationFlag
from .X509Certificates import X509RevocationMode

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Aes(ABC, SymmetricAlgorithm, IDisposable):
    """"""
    @property
    def BlockSize(self) -> int:
        """"""
    @BlockSize.setter
    def BlockSize(self, value: int) -> None: ...
    @property
    def FeedbackSize(self) -> int:
        """"""
    @FeedbackSize.setter
    def FeedbackSize(self, value: int) -> None: ...
    @property
    def IV(self) -> Array[int]:
        """"""
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def Key(self) -> Array[int]:
        """"""
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def KeySize(self) -> int:
        """"""
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalBlockSizes(self) -> Array[KeySizes]:
        """"""
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """"""
    @property
    def Mode(self) -> CipherMode:
        """"""
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    @property
    def Padding(self) -> PaddingMode:
        """"""
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    def Clear(self) -> None:
        """"""
    @classmethod
    @overload
    def Create(cls) -> Aes:
        """"""
    @classmethod
    @overload
    def Create(cls, algorithmName: str) -> Aes:
        """"""
    @overload
    def CreateDecryptor(self) -> ICryptoTransform:
        """"""
    @overload
    def CreateDecryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """"""
    @overload
    def CreateEncryptor(self) -> ICryptoTransform:
        """"""
    @overload
    def CreateEncryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GenerateIV(self) -> None:
        """"""
    def GenerateKey(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def ValidKeySize(self, bitLength: int) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AesCng(Aes, ICngSymmetricAlgorithm, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, keyName: str) -> None:
        """"""
    @overload
    def __init__(self, keyName: str, provider: CngProvider) -> None:
        """"""
    @overload
    def __init__(self, keyName: str, provider: CngProvider, openOptions: CngKeyOpenOptions) -> None:
        """"""
    @property
    def BaseKey(self) -> Array[int]:
        """"""
    @BaseKey.setter
    def BaseKey(self, value: Array[int]) -> None: ...
    @property
    def BaseKeySize(self) -> int:
        """"""
    @BaseKeySize.setter
    def BaseKeySize(self, value: int) -> None: ...
    @property
    def BlockSize(self) -> int:
        """"""
    @BlockSize.setter
    def BlockSize(self, value: int) -> None: ...
    @property
    def FeedbackSize(self) -> int:
        """"""
    @FeedbackSize.setter
    def FeedbackSize(self, value: int) -> None: ...
    @property
    def IV(self) -> Array[int]:
        """"""
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def Key(self) -> Array[int]:
        """"""
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def KeySize(self) -> int:
        """"""
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalBlockSizes(self) -> Array[KeySizes]:
        """"""
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """"""
    @property
    def Mode(self) -> CipherMode:
        """"""
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    @property
    def Padding(self) -> PaddingMode:
        """"""
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    def Clear(self) -> None:
        """"""
    @overload
    def CreateDecryptor(self) -> ICryptoTransform:
        """"""
    @overload
    def CreateDecryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """"""
    @overload
    def CreateEncryptor(self) -> ICryptoTransform:
        """"""
    @overload
    def CreateEncryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GenerateIV(self) -> None:
        """"""
    def GenerateKey(self) -> None:
        """"""
    def GetEphemeralModeHandle(self) -> SafeBCryptAlgorithmHandle:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetNCryptAlgorithmIdentifier(self) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsWeakKey(self, key: Array[int]) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def ValidKeySize(self, bitLength: int) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AesCryptoServiceProvider(Aes, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def BlockSize(self) -> int:
        """"""
    @BlockSize.setter
    def BlockSize(self, value: int) -> None: ...
    @property
    def FeedbackSize(self) -> int:
        """"""
    @FeedbackSize.setter
    def FeedbackSize(self, value: int) -> None: ...
    @property
    def IV(self) -> Array[int]:
        """"""
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def Key(self) -> Array[int]:
        """"""
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def KeySize(self) -> int:
        """"""
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalBlockSizes(self) -> Array[KeySizes]:
        """"""
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """"""
    @property
    def Mode(self) -> CipherMode:
        """"""
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    @property
    def Padding(self) -> PaddingMode:
        """"""
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    def Clear(self) -> None:
        """"""
    @overload
    def CreateDecryptor(self) -> ICryptoTransform:
        """"""
    @overload
    def CreateDecryptor(self, key: Array[int], iv: Array[int]) -> ICryptoTransform:
        """"""
    @overload
    def CreateEncryptor(self) -> ICryptoTransform:
        """"""
    @overload
    def CreateEncryptor(self, key: Array[int], iv: Array[int]) -> ICryptoTransform:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GenerateIV(self) -> None:
        """"""
    def GenerateKey(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def ValidKeySize(self, bitLength: int) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AesManaged(Aes, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def BlockSize(self) -> int:
        """"""
    @BlockSize.setter
    def BlockSize(self, value: int) -> None: ...
    @property
    def FeedbackSize(self) -> int:
        """"""
    @FeedbackSize.setter
    def FeedbackSize(self, value: int) -> None: ...
    @property
    def IV(self) -> Array[int]:
        """"""
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def Key(self) -> Array[int]:
        """"""
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def KeySize(self) -> int:
        """"""
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalBlockSizes(self) -> Array[KeySizes]:
        """"""
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """"""
    @property
    def Mode(self) -> CipherMode:
        """"""
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    @property
    def Padding(self) -> PaddingMode:
        """"""
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    def Clear(self) -> None:
        """"""
    @overload
    def CreateDecryptor(self) -> ICryptoTransform:
        """"""
    @overload
    def CreateDecryptor(self, key: Array[int], iv: Array[int]) -> ICryptoTransform:
        """"""
    @overload
    def CreateEncryptor(self) -> ICryptoTransform:
        """"""
    @overload
    def CreateEncryptor(self, key: Array[int], iv: Array[int]) -> ICryptoTransform:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GenerateIV(self) -> None:
        """"""
    def GenerateKey(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def ValidKeySize(self, bitLength: int) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AsnEncodedData(Object):
    """"""
    @overload
    def __init__(self, rawData: Array[int]) -> None:
        """"""
    @overload
    def __init__(self, oid: str, rawData: Array[int]) -> None:
        """"""
    @overload
    def __init__(self, oid: Oid, rawData: Array[int]) -> None:
        """"""
    @overload
    def __init__(self, asnEncodedData: AsnEncodedData) -> None:
        """"""
    @property
    def Oid(self) -> Oid:
        """"""
    @Oid.setter
    def Oid(self, value: Oid) -> None: ...
    @property
    def RawData(self) -> Array[int]:
        """"""
    @RawData.setter
    def RawData(self, value: Array[int]) -> None: ...
    def CopyFrom(self, asnEncodedData: AsnEncodedData) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Format(self, multiLine: bool) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AsnEncodedDataCollection(Object, ICollection, IEnumerable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, asnEncodedData: AsnEncodedData) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> AsnEncodedData:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    def Add(self, asnEncodedData: AsnEncodedData) -> int:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[AsnEncodedData], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> AsnEncodedDataEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Remove(self, asnEncodedData: AsnEncodedData) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, asnEncodedData: AsnEncodedData) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> AsnEncodedData:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AsnEncodedDataEnumerator(Object, IEnumerator):
    """"""
    @property
    def Current(self) -> AsnEncodedData:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MoveNext(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AsymmetricAlgorithm(ABC, Object, IDisposable):
    """"""
    @property
    def KeyExchangeAlgorithm(self) -> str:
        """"""
    @property
    def KeySize(self) -> int:
        """"""
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """"""
    @property
    def SignatureAlgorithm(self) -> str:
        """"""
    def Clear(self) -> None:
        """"""
    @classmethod
    @overload
    def Create(cls) -> AsymmetricAlgorithm:
        """"""
    @classmethod
    @overload
    def Create(cls, algName: str) -> AsymmetricAlgorithm:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FromXmlString(self, xmlString: str) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXmlString(self, includePrivateParameters: bool) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AsymmetricKeyExchangeDeformatter(ABC, Object):
    """"""
    @property
    def Parameters(self) -> str:
        """"""
    @Parameters.setter
    def Parameters(self, value: str) -> None: ...
    def DecryptKeyExchange(self, rgb: Array[int]) -> Array[int]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetKey(self, key: AsymmetricAlgorithm) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AsymmetricKeyExchangeFormatter(ABC, Object):
    """"""
    @property
    def Parameters(self) -> str:
        """"""
    @overload
    def CreateKeyExchange(self, data: Array[int]) -> Array[int]:
        """"""
    @overload
    def CreateKeyExchange(self, data: Array[int], symAlgType: Type) -> Array[int]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetKey(self, key: AsymmetricAlgorithm) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class AsymmetricPaddingMode(Enum):
    """"""

    _None: AsymmetricPaddingMode = ...
    """"""
    Pkcs1: AsymmetricPaddingMode = ...
    """"""
    Oaep: AsymmetricPaddingMode = ...
    """"""
    Pss: AsymmetricPaddingMode = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AsymmetricSignatureDeformatter(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHashAlgorithm(self, strName: str) -> None:
        """"""
    def SetKey(self, key: AsymmetricAlgorithm) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def VerifySignature(self, hash: HashAlgorithm, rgbSignature: Array[int]) -> bool:
        """"""
    @overload
    def VerifySignature(self, rgbHash: Array[int], rgbSignature: Array[int]) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AsymmetricSignatureFormatter(ABC, Object):
    """"""
    @overload
    def CreateSignature(self, hash: HashAlgorithm) -> Array[int]:
        """"""
    @overload
    def CreateSignature(self, rgbHash: Array[int]) -> Array[int]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHashAlgorithm(self, strName: str) -> None:
        """"""
    def SetKey(self, key: AsymmetricAlgorithm) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class BCRYPT_DSA_KEY_BLOB_V2(ValueType):
    """"""

    Count0: Final[int]
    """"""
    Count1: Final[int]
    """"""
    Count2: Final[int]
    """"""
    Count3: Final[int]
    """"""
    cbGroupSize: Final[int]
    """"""
    cbKey: Final[int]
    """"""
    cbSeedLength: Final[int]
    """"""
    dwMagic: Final[BCryptNative.KeyBlobMagicNumber]
    """"""
    hashAlgorithm: Final[HASHALGORITHM_ENUM]
    """"""
    standardVersion: Final[DSAFIPSVERSION_ENUM]
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
class BCryptAlgorithmHandleCache(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetCachedAlgorithmHandle(
        self, algorithm: str, implementation: str
    ) -> SafeBCryptAlgorithmHandle:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class BCryptHashAlgorithm(Object, IDisposable):
    """"""
    def __init__(self, algorithm: CngAlgorithm, implementation: str) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def HashCore(self, array: Array[int], ibStart: int, cbSize: int) -> None:
        """"""
    def HashFinal(self) -> Array[int]:
        """"""
    def HashStream(self, stream: Stream) -> None:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class BCryptNative(ABC, Object):
    """"""
    @classmethod
    def BCryptDecrypt(
        cls,
        hKey: SafeBCryptKeyHandle,
        input: Array[int],
        inputOffset: int,
        inputCount: int,
        iv: Array[int],
        output: Array[int],
        outputOffset: int,
        outputCount: int,
    ) -> int:
        """"""
    @classmethod
    def BCryptEncrypt(
        cls,
        hKey: SafeBCryptKeyHandle,
        input: Array[int],
        inputOffset: int,
        inputCount: int,
        iv: Array[int],
        output: Array[int],
        outputOffset: int,
        outputCount: int,
    ) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def SetCipherMode(cls, hAlg: SafeBCryptAlgorithmHandle, cipherMode: str) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class BigInt(Object):
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
    def op_Equality(cls, value1: BigInt, value2: BigInt) -> bool:
        """"""
    @classmethod
    def op_GreaterThan(cls, value1: BigInt, value2: BigInt) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, value1: BigInt, value2: BigInt) -> bool:
        """"""
    @classmethod
    def op_LessThan(cls, value1: BigInt, value2: BigInt) -> bool:
        """"""
    def __eq__(self, other: BigInt) -> bool:
        """"""
    def __gt__(self, other: BigInt) -> bool:
        """"""
    def __ne__(self, other: BigInt) -> bool:
        """"""
    def __lt__(self, other: BigInt) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CAPI(CAPIMethods):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CAPIBase(ABC, Object):
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
class CAPIMethods(ABC, CAPIUnsafe):
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
class CAPINative(ABC, CAPIBase):
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
class CAPISafe(ABC, CAPINative):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def FreeLibrary(cls, hModule: IntPtr) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CAPIUnsafe(ABC, CAPISafe):
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
class CapiHashAlgorithm(Object, IDisposable):
    """"""
    def __init__(
        self,
        provider: str,
        providerType: CapiNative.ProviderType,
        algorithm: CapiNative.AlgorithmId,
    ) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def HashCore(self, array: Array[int], ibStart: int, cbSize: int) -> None:
        """"""
    def HashFinal(self) -> Array[int]:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CapiNative(ABC, Object):
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
class CapiSymmetricAlgorithm(Object, ICryptoTransform, IDisposable):
    """"""
    def __init__(
        self,
        blockSize: int,
        feedbackSize: int,
        provider: SafeCspHandle,
        key: SafeCapiKeyHandle,
        iv: Array[int],
        cipherMode: CipherMode,
        paddingMode: PaddingMode,
        encryptionMode: EncryptionMode,
    ) -> None:
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CipherMode(Enum):
    """"""

    CBC: CipherMode = ...
    """"""
    ECB: CipherMode = ...
    """"""
    OFB: CipherMode = ...
    """"""
    CFB: CipherMode = ...
    """"""
    CTS: CipherMode = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CngAlgorithm(Object, IEquatable[CngAlgorithm]):
    """"""
    def __init__(self, algorithm: str) -> None:
        """"""
    @property
    def Algorithm(self) -> str:
        """"""
    @classmethod
    @property
    def ECDiffieHellman(cls) -> CngAlgorithm:
        """"""
    @classmethod
    @property
    def ECDiffieHellmanP256(cls) -> CngAlgorithm:
        """"""
    @classmethod
    @property
    def ECDiffieHellmanP384(cls) -> CngAlgorithm:
        """"""
    @classmethod
    @property
    def ECDiffieHellmanP521(cls) -> CngAlgorithm:
        """"""
    @classmethod
    @property
    def ECDsa(cls) -> CngAlgorithm:
        """"""
    @classmethod
    @property
    def ECDsaP256(cls) -> CngAlgorithm:
        """"""
    @classmethod
    @property
    def ECDsaP384(cls) -> CngAlgorithm:
        """"""
    @classmethod
    @property
    def ECDsaP521(cls) -> CngAlgorithm:
        """"""
    @classmethod
    @property
    def MD5(cls) -> CngAlgorithm:
        """"""
    @classmethod
    @property
    def Rsa(cls) -> CngAlgorithm:
        """"""
    @classmethod
    @property
    def Sha1(cls) -> CngAlgorithm:
        """"""
    @classmethod
    @property
    def Sha256(cls) -> CngAlgorithm:
        """"""
    @classmethod
    @property
    def Sha384(cls) -> CngAlgorithm:
        """"""
    @classmethod
    @property
    def Sha512(cls) -> CngAlgorithm:
        """"""
    @overload
    def Equals(self, other: CngAlgorithm) -> bool:
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
    def op_Equality(cls, left: CngAlgorithm, right: CngAlgorithm) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: CngAlgorithm, right: CngAlgorithm) -> bool:
        """"""
    def __eq__(self, other: CngAlgorithm) -> bool:
        """"""
    def __ne__(self, other: CngAlgorithm) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CngAlgorithmGroup(Object, IEquatable[CngAlgorithmGroup]):
    """"""
    def __init__(self, algorithmGroup: str) -> None:
        """"""
    @property
    def AlgorithmGroup(self) -> str:
        """"""
    @classmethod
    @property
    def DiffieHellman(cls) -> CngAlgorithmGroup:
        """"""
    @classmethod
    @property
    def Dsa(cls) -> CngAlgorithmGroup:
        """"""
    @classmethod
    @property
    def ECDiffieHellman(cls) -> CngAlgorithmGroup:
        """"""
    @classmethod
    @property
    def ECDsa(cls) -> CngAlgorithmGroup:
        """"""
    @classmethod
    @property
    def Rsa(cls) -> CngAlgorithmGroup:
        """"""
    @overload
    def Equals(self, other: CngAlgorithmGroup) -> bool:
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
    def op_Equality(cls, left: CngAlgorithmGroup, right: CngAlgorithmGroup) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: CngAlgorithmGroup, right: CngAlgorithmGroup) -> bool:
        """"""
    def __eq__(self, other: CngAlgorithmGroup) -> bool:
        """"""
    def __ne__(self, other: CngAlgorithmGroup) -> bool:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CngExportPolicies(Enum):
    """"""

    _None: CngExportPolicies = ...
    """"""
    AllowExport: CngExportPolicies = ...
    """"""
    AllowPlaintextExport: CngExportPolicies = ...
    """"""
    AllowArchiving: CngExportPolicies = ...
    """"""
    AllowPlaintextArchiving: CngExportPolicies = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CngHashAlgorithmFactory[THashAlgorithm](Object):
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
class CngKey(Object, IDisposable):
    """"""
    @property
    def Algorithm(self) -> CngAlgorithm:
        """"""
    @property
    def AlgorithmGroup(self) -> CngAlgorithmGroup:
        """"""
    @property
    def ExportPolicy(self) -> CngExportPolicies:
        """"""
    @property
    def Handle(self) -> SafeNCryptKeyHandle:
        """"""
    @property
    def IsEphemeral(self) -> bool:
        """"""
    @property
    def IsMachineKey(self) -> bool:
        """"""
    @property
    def KeyName(self) -> str:
        """"""
    @property
    def KeySize(self) -> int:
        """"""
    @property
    def KeyUsage(self) -> CngKeyUsages:
        """"""
    @property
    def ParentWindowHandle(self) -> IntPtr:
        """"""
    @ParentWindowHandle.setter
    def ParentWindowHandle(self, value: IntPtr) -> None: ...
    @property
    def Provider(self) -> CngProvider:
        """"""
    @property
    def ProviderHandle(self) -> SafeNCryptProviderHandle:
        """"""
    @property
    def UIPolicy(self) -> CngUIPolicy:
        """"""
    @property
    def UniqueName(self) -> str:
        """"""
    @classmethod
    @overload
    def Create(cls, algorithm: CngAlgorithm) -> CngKey:
        """"""
    @classmethod
    @overload
    def Create(cls, algorithm: CngAlgorithm, keyName: str) -> CngKey:
        """"""
    @classmethod
    @overload
    def Create(
        cls, algorithm: CngAlgorithm, keyName: str, creationParameters: CngKeyCreationParameters
    ) -> CngKey:
        """"""
    def Delete(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    @overload
    def Exists(cls, keyName: str) -> bool:
        """"""
    @classmethod
    @overload
    def Exists(cls, keyName: str, provider: CngProvider) -> bool:
        """"""
    @classmethod
    @overload
    def Exists(cls, keyName: str, provider: CngProvider, options: CngKeyOpenOptions) -> bool:
        """"""
    def Export(self, format: CngKeyBlobFormat) -> Array[int]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetProperty(self, name: str, options: CngPropertyOptions) -> CngProperty:
        """"""
    def GetType(self) -> Type:
        """"""
    def HasProperty(self, name: str, options: CngPropertyOptions) -> bool:
        """"""
    @classmethod
    @overload
    def Import(cls, keyBlob: Array[int], format: CngKeyBlobFormat) -> CngKey:
        """"""
    @classmethod
    @overload
    def Import(cls, keyBlob: Array[int], format: CngKeyBlobFormat, provider: CngProvider) -> CngKey:
        """"""
    @classmethod
    @overload
    def Open(
        cls, keyHandle: SafeNCryptKeyHandle, keyHandleOpenOptions: CngKeyHandleOpenOptions
    ) -> CngKey:
        """"""
    @classmethod
    @overload
    def Open(cls, keyName: str) -> CngKey:
        """"""
    @classmethod
    @overload
    def Open(cls, keyName: str, provider: CngProvider) -> CngKey:
        """"""
    @classmethod
    @overload
    def Open(cls, keyName: str, provider: CngProvider, openOptions: CngKeyOpenOptions) -> CngKey:
        """"""
    def SetProperty(self, property: CngProperty) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CngKeyBlobFormat(Object, IEquatable[CngKeyBlobFormat]):
    """"""
    def __init__(self, format: str) -> None:
        """"""
    @classmethod
    @property
    def EccFullPrivateBlob(cls) -> CngKeyBlobFormat:
        """"""
    @classmethod
    @property
    def EccFullPublicBlob(cls) -> CngKeyBlobFormat:
        """"""
    @classmethod
    @property
    def EccPrivateBlob(cls) -> CngKeyBlobFormat:
        """"""
    @classmethod
    @property
    def EccPublicBlob(cls) -> CngKeyBlobFormat:
        """"""
    @property
    def Format(self) -> str:
        """"""
    @classmethod
    @property
    def GenericPrivateBlob(cls) -> CngKeyBlobFormat:
        """"""
    @classmethod
    @property
    def GenericPublicBlob(cls) -> CngKeyBlobFormat:
        """"""
    @classmethod
    @property
    def OpaqueTransportBlob(cls) -> CngKeyBlobFormat:
        """"""
    @classmethod
    @property
    def Pkcs8PrivateBlob(cls) -> CngKeyBlobFormat:
        """"""
    @overload
    def Equals(self, other: CngKeyBlobFormat) -> bool:
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
    def op_Equality(cls, left: CngKeyBlobFormat, right: CngKeyBlobFormat) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: CngKeyBlobFormat, right: CngKeyBlobFormat) -> bool:
        """"""
    def __eq__(self, other: CngKeyBlobFormat) -> bool:
        """"""
    def __ne__(self, other: CngKeyBlobFormat) -> bool:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CngKeyCreationOptions(Enum):
    """"""

    _None: CngKeyCreationOptions = ...
    """"""
    MachineKey: CngKeyCreationOptions = ...
    """"""
    OverwriteExistingKey: CngKeyCreationOptions = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CngKeyCreationParameters(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def ExportPolicy(self) -> CngExportPolicies | None:
        """"""
    @ExportPolicy.setter
    def ExportPolicy(self, value: CngExportPolicies | None) -> None: ...
    @property
    def KeyCreationOptions(self) -> CngKeyCreationOptions:
        """"""
    @KeyCreationOptions.setter
    def KeyCreationOptions(self, value: CngKeyCreationOptions) -> None: ...
    @property
    def KeyUsage(self) -> CngKeyUsages | None:
        """"""
    @KeyUsage.setter
    def KeyUsage(self, value: CngKeyUsages | None) -> None: ...
    @property
    def Parameters(self) -> CngPropertyCollection:
        """"""
    @property
    def ParentWindowHandle(self) -> IntPtr:
        """"""
    @ParentWindowHandle.setter
    def ParentWindowHandle(self, value: IntPtr) -> None: ...
    @property
    def Provider(self) -> CngProvider:
        """"""
    @Provider.setter
    def Provider(self, value: CngProvider) -> None: ...
    @property
    def UIPolicy(self) -> CngUIPolicy:
        """"""
    @UIPolicy.setter
    def UIPolicy(self, value: CngUIPolicy) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CngKeyHandleOpenOptions(Enum):
    """"""

    _None: CngKeyHandleOpenOptions = ...
    """"""
    EphemeralKey: CngKeyHandleOpenOptions = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CngKeyOpenOptions(Enum):
    """"""

    _None: CngKeyOpenOptions = ...
    """"""
    UserKey: CngKeyOpenOptions = ...
    """"""
    MachineKey: CngKeyOpenOptions = ...
    """"""
    Silent: CngKeyOpenOptions = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CngKeyTypes(Enum):
    """"""

    _None: CngKeyTypes = ...
    """"""
    MachineKey: CngKeyTypes = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CngKeyUsages(Enum):
    """"""

    _None: CngKeyUsages = ...
    """"""
    Decryption: CngKeyUsages = ...
    """"""
    Signing: CngKeyUsages = ...
    """"""
    KeyAgreement: CngKeyUsages = ...
    """"""
    AllUsages: CngKeyUsages = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CngProperty(ValueType, IEquatable[CngProperty]):
    """"""
    def __init__(self, name: str, value: Array[int], options: CngPropertyOptions) -> None:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Options(self) -> CngPropertyOptions:
        """"""
    @overload
    def Equals(self, other: CngProperty) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetValue(self) -> Array[int]:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, left: CngProperty, right: CngProperty) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: CngProperty, right: CngProperty) -> bool:
        """"""
    def __eq__(self, other: CngProperty) -> bool:
        """"""
    def __ne__(self, other: CngProperty) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CngPropertyCollection(
    Collection[CngProperty],
    ICollection[CngProperty],
    IEnumerable[CngProperty],
    IList[CngProperty],
    IReadOnlyCollection[CngProperty],
    IReadOnlyList[CngProperty],
    ICollection,
    IEnumerable,
    IList,
):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> CngProperty:
        """"""
    @Item.setter
    def Item(self, value: CngProperty) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, item: CngProperty) -> None:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, item: CngProperty) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[CngProperty], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[CngProperty]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, item: CngProperty) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, item: CngProperty) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, item: CngProperty) -> bool:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, item: CngProperty) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator[CngProperty]:
        """"""
    @overload
    def __delitem__(self, item: CngProperty) -> bool:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> CngProperty:
        """"""
    @overload
    def __setitem__(self, index: int, value: CngProperty) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CngPropertyOptions(Enum):
    """"""

    _None: CngPropertyOptions = ...
    """"""
    CustomProperty: CngPropertyOptions = ...
    """"""
    Persist: CngPropertyOptions = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CngProvider(Object, IEquatable[CngProvider]):
    """"""
    def __init__(self, provider: str) -> None:
        """"""
    @classmethod
    @property
    def MicrosoftSmartCardKeyStorageProvider(cls) -> CngProvider:
        """"""
    @classmethod
    @property
    def MicrosoftSoftwareKeyStorageProvider(cls) -> CngProvider:
        """"""
    @property
    def Provider(self) -> str:
        """"""
    @overload
    def Equals(self, other: CngProvider) -> bool:
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
    def op_Equality(cls, left: CngProvider, right: CngProvider) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: CngProvider, right: CngProvider) -> bool:
        """"""
    def __eq__(self, other: CngProvider) -> bool:
        """"""
    def __ne__(self, other: CngProvider) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CngUIPolicy(Object):
    """"""
    @overload
    def __init__(self, protectionLevel: CngUIProtectionLevels) -> None:
        """"""
    @overload
    def __init__(self, protectionLevel: CngUIProtectionLevels, friendlyName: str) -> None:
        """"""
    @overload
    def __init__(
        self, protectionLevel: CngUIProtectionLevels, friendlyName: str, description: str
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        protectionLevel: CngUIProtectionLevels,
        friendlyName: str,
        description: str,
        useContext: str,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        protectionLevel: CngUIProtectionLevels,
        friendlyName: str,
        description: str,
        useContext: str,
        creationTitle: str,
    ) -> None:
        """"""
    @property
    def CreationTitle(self) -> str:
        """"""
    @property
    def Description(self) -> str:
        """"""
    @property
    def FriendlyName(self) -> str:
        """"""
    @property
    def ProtectionLevel(self) -> CngUIProtectionLevels:
        """"""
    @property
    def UseContext(self) -> str:
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
class CngUIProtectionLevels(Enum):
    """"""

    _None: CngUIProtectionLevels = ...
    """"""
    ProtectKey: CngUIProtectionLevels = ...
    """"""
    ForceHighProtection: CngUIProtectionLevels = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Constants(ABC, Object):
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
class CryptoAPITransform(Object, ICryptoTransform, IDisposable):
    """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def KeyHandle(self) -> IntPtr:
        """"""
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CryptoAPITransformMode(Enum):
    """"""

    Encrypt: CryptoAPITransformMode = ...
    """"""
    Decrypt: CryptoAPITransformMode = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CryptoConfig(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @classmethod
    @property
    def AllowOnlyFipsAlgorithms(cls) -> bool:
        """"""
    @classmethod
    def AddAlgorithm(cls, algorithm: Type, names: Array[str]) -> None:
        """"""
    @classmethod
    def AddOID(cls, oid: str, names: Array[str]) -> None:
        """"""
    @classmethod
    @overload
    def CreateFromName(cls, name: str) -> object:
        """"""
    @classmethod
    @overload
    def CreateFromName(cls, name: str, args: Array[object]) -> object:
        """"""
    @classmethod
    def EncodeOID(cls, str: str) -> Array[int]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def MapNameToOID(cls, name: str) -> str:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CryptoStream(Stream, IDisposable):
    """"""
    @overload
    def __init__(self, stream: Stream, transform: ICryptoTransform, mode: CryptoStreamMode) -> None:
        """"""
    @overload
    def __init__(
        self, stream: Stream, transform: ICryptoTransform, mode: CryptoStreamMode, leaveOpen: bool
    ) -> None:
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
    def HasFlushedFinalBlock(self) -> bool:
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
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def Clear(self) -> None:
        """"""
    def Close(self) -> None:
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
    def FlushFinalBlock(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def Read(self, buffer: Array[int], offset: int, count: int) -> tuple[int, Array[int]]:
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
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CryptoStreamMode(Enum):
    """"""

    Read: CryptoStreamMode = ...
    """"""
    Write: CryptoStreamMode = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CryptographicException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, format: str, insert: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, inner: Exception) -> None:
        """"""
    @overload
    def __init__(self, hr: int) -> None:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CryptographicUnexpectedOperationException(CryptographicException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, format: str, insert: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, inner: Exception) -> None:
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
class CspAlgorithmType(Enum):
    """"""

    Rsa: CspAlgorithmType = ...
    """"""
    Dss: CspAlgorithmType = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CspKeyContainerInfo(Object):
    """"""
    def __init__(self, parameters: CspParameters) -> None:
        """"""
    @property
    def Accessible(self) -> bool:
        """"""
    @property
    def CryptoKeySecurity(self) -> CryptoKeySecurity:
        """"""
    @property
    def Exportable(self) -> bool:
        """"""
    @property
    def HardwareDevice(self) -> bool:
        """"""
    @property
    def KeyContainerName(self) -> str:
        """"""
    @property
    def KeyNumber(self) -> KeyNumber:
        """"""
    @property
    def MachineKeyStore(self) -> bool:
        """"""
    @property
    def Protected(self) -> bool:
        """"""
    @property
    def ProviderName(self) -> str:
        """"""
    @property
    def ProviderType(self) -> int:
        """"""
    @property
    def RandomlyGenerated(self) -> bool:
        """"""
    @property
    def Removable(self) -> bool:
        """"""
    @property
    def UniqueKeyContainerName(self) -> str:
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
class CspParameters(Object):
    """"""

    KeyContainerName: Final[str]
    """"""
    KeyNumber: Final[int]
    """"""
    ProviderName: Final[str]
    """"""
    ProviderType: Final[int]
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, dwTypeIn: int) -> None:
        """"""
    @overload
    def __init__(self, dwTypeIn: int, strProviderNameIn: str) -> None:
        """"""
    @overload
    def __init__(self, dwTypeIn: int, strProviderNameIn: str, strContainerNameIn: str) -> None:
        """"""
    @overload
    def __init__(
        self,
        providerType: int,
        providerName: str,
        keyContainerName: str,
        cryptoKeySecurity: CryptoKeySecurity,
        keyPassword: SecureString,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        providerType: int,
        providerName: str,
        keyContainerName: str,
        cryptoKeySecurity: CryptoKeySecurity,
        parentWindowHandle: IntPtr,
    ) -> None:
        """"""
    @property
    def CryptoKeySecurity(self) -> CryptoKeySecurity:
        """"""
    @CryptoKeySecurity.setter
    def CryptoKeySecurity(self, value: CryptoKeySecurity) -> None: ...
    @property
    def Flags(self) -> CspProviderFlags:
        """"""
    @Flags.setter
    def Flags(self, value: CspProviderFlags) -> None: ...
    @property
    def KeyPassword(self) -> SecureString:
        """"""
    @KeyPassword.setter
    def KeyPassword(self, value: SecureString) -> None: ...
    @property
    def ParentWindowHandle(self) -> IntPtr:
        """"""
    @ParentWindowHandle.setter
    def ParentWindowHandle(self, value: IntPtr) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class CspProviderFlags(Enum):
    """"""

    NoFlags: CspProviderFlags = ...
    """"""
    UseMachineKeyStore: CspProviderFlags = ...
    """"""
    UseDefaultKeyContainer: CspProviderFlags = ...
    """"""
    UseNonExportableKey: CspProviderFlags = ...
    """"""
    UseExistingKey: CspProviderFlags = ...
    """"""
    UseArchivableKey: CspProviderFlags = ...
    """"""
    UseUserProtectedKey: CspProviderFlags = ...
    """"""
    NoPrompt: CspProviderFlags = ...
    """"""
    CreateEphemeralKey: CspProviderFlags = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DES(ABC, SymmetricAlgorithm, IDisposable):
    """"""
    @property
    def BlockSize(self) -> int:
        """"""
    @BlockSize.setter
    def BlockSize(self, value: int) -> None: ...
    @property
    def FeedbackSize(self) -> int:
        """"""
    @FeedbackSize.setter
    def FeedbackSize(self, value: int) -> None: ...
    @property
    def IV(self) -> Array[int]:
        """"""
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def Key(self) -> Array[int]:
        """"""
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def KeySize(self) -> int:
        """"""
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalBlockSizes(self) -> Array[KeySizes]:
        """"""
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """"""
    @property
    def Mode(self) -> CipherMode:
        """"""
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    @property
    def Padding(self) -> PaddingMode:
        """"""
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    def Clear(self) -> None:
        """"""
    @classmethod
    @overload
    def Create(cls) -> DES:
        """"""
    @classmethod
    @overload
    def Create(cls, algName: str) -> DES:
        """"""
    @overload
    def CreateDecryptor(self) -> ICryptoTransform:
        """"""
    @overload
    def CreateDecryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """"""
    @overload
    def CreateEncryptor(self) -> ICryptoTransform:
        """"""
    @overload
    def CreateEncryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GenerateIV(self) -> None:
        """"""
    def GenerateKey(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsSemiWeakKey(cls, rgbKey: Array[int]) -> bool:
        """"""
    @classmethod
    def IsWeakKey(cls, rgbKey: Array[int]) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def ValidKeySize(self, bitLength: int) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DESCryptoServiceProvider(DES, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def BlockSize(self) -> int:
        """"""
    @BlockSize.setter
    def BlockSize(self, value: int) -> None: ...
    @property
    def FeedbackSize(self) -> int:
        """"""
    @FeedbackSize.setter
    def FeedbackSize(self, value: int) -> None: ...
    @property
    def IV(self) -> Array[int]:
        """"""
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def Key(self) -> Array[int]:
        """"""
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def KeySize(self) -> int:
        """"""
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalBlockSizes(self) -> Array[KeySizes]:
        """"""
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """"""
    @property
    def Mode(self) -> CipherMode:
        """"""
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    @property
    def Padding(self) -> PaddingMode:
        """"""
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    def Clear(self) -> None:
        """"""
    @overload
    def CreateDecryptor(self) -> ICryptoTransform:
        """"""
    @overload
    def CreateDecryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """"""
    @overload
    def CreateEncryptor(self) -> ICryptoTransform:
        """"""
    @overload
    def CreateEncryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GenerateIV(self) -> None:
        """"""
    def GenerateKey(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def ValidKeySize(self, bitLength: int) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DSA(ABC, AsymmetricAlgorithm, IDisposable):
    """"""
    @property
    def KeyExchangeAlgorithm(self) -> str:
        """"""
    @property
    def KeySize(self) -> int:
        """"""
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """"""
    @property
    def SignatureAlgorithm(self) -> str:
        """"""
    def Clear(self) -> None:
        """"""
    @classmethod
    @overload
    def Create(cls) -> DSA:
        """"""
    @classmethod
    @overload
    def Create(cls, parameters: DSAParameters) -> DSA:
        """"""
    @classmethod
    @overload
    def Create(cls, keySizeInBits: int) -> DSA:
        """"""
    @classmethod
    @overload
    def Create(cls, algName: str) -> DSA:
        """"""
    def CreateSignature(self, rgbHash: Array[int]) -> Array[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def ExportParameters(self, includePrivateParameters: bool) -> DSAParameters:
        """"""
    def FromXmlString(self, xmlString: str) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ImportParameters(self, parameters: DSAParameters) -> None:
        """"""
    @overload
    def SignData(self, data: Stream, hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """"""
    @overload
    def SignData(self, data: Array[int], hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """"""
    @overload
    def SignData(
        self, data: Array[int], offset: int, count: int, hashAlgorithm: HashAlgorithmName
    ) -> Array[int]:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXmlString(self, includePrivateParameters: bool) -> str:
        """"""
    @overload
    def VerifyData(
        self, data: Stream, signature: Array[int], hashAlgorithm: HashAlgorithmName
    ) -> bool:
        """"""
    @overload
    def VerifyData(
        self, data: Array[int], signature: Array[int], hashAlgorithm: HashAlgorithmName
    ) -> bool:
        """"""
    @overload
    def VerifyData(
        self,
        data: Array[int],
        offset: int,
        count: int,
        signature: Array[int],
        hashAlgorithm: HashAlgorithmName,
    ) -> bool:
        """"""
    def VerifySignature(self, rgbHash: Array[int], rgbSignature: Array[int]) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DSACng(DSA, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, keySize: int) -> None:
        """"""
    @overload
    def __init__(self, key: CngKey) -> None:
        """"""
    @property
    def Key(self) -> CngKey:
        """"""
    @property
    def KeyExchangeAlgorithm(self) -> str:
        """"""
    @property
    def KeySize(self) -> int:
        """"""
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """"""
    @property
    def SignatureAlgorithm(self) -> str:
        """"""
    def Clear(self) -> None:
        """"""
    def CreateSignature(self, rgbHash: Array[int]) -> Array[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def ExportParameters(self, includePrivateParameters: bool) -> DSAParameters:
        """"""
    def FromXmlString(self, xmlString: str) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ImportParameters(self, parameters: DSAParameters) -> None:
        """"""
    @overload
    def SignData(self, data: Stream, hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """"""
    @overload
    def SignData(self, data: Array[int], hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """"""
    @overload
    def SignData(
        self, data: Array[int], offset: int, count: int, hashAlgorithm: HashAlgorithmName
    ) -> Array[int]:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXmlString(self, includePrivateParameters: bool) -> str:
        """"""
    @overload
    def VerifyData(
        self, data: Stream, signature: Array[int], hashAlgorithm: HashAlgorithmName
    ) -> bool:
        """"""
    @overload
    def VerifyData(
        self, data: Array[int], signature: Array[int], hashAlgorithm: HashAlgorithmName
    ) -> bool:
        """"""
    @overload
    def VerifyData(
        self,
        data: Array[int],
        offset: int,
        count: int,
        signature: Array[int],
        hashAlgorithm: HashAlgorithmName,
    ) -> bool:
        """"""
    def VerifySignature(self, rgbHash: Array[int], rgbSignature: Array[int]) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DSACryptoServiceProvider(DSA, ICspAsymmetricAlgorithm, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, dwKeySize: int) -> None:
        """"""
    @overload
    def __init__(self, parameters: CspParameters) -> None:
        """"""
    @overload
    def __init__(self, dwKeySize: int, parameters: CspParameters) -> None:
        """"""
    @property
    def CspKeyContainerInfo(self) -> CspKeyContainerInfo:
        """"""
    @property
    def KeyExchangeAlgorithm(self) -> str:
        """"""
    @property
    def KeySize(self) -> int:
        """"""
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """"""
    @property
    def PersistKeyInCsp(self) -> bool:
        """"""
    @PersistKeyInCsp.setter
    def PersistKeyInCsp(self, value: bool) -> None: ...
    @property
    def PublicOnly(self) -> bool:
        """"""
    @property
    def SignatureAlgorithm(self) -> str:
        """"""
    @classmethod
    @property
    def UseMachineKeyStore(cls) -> bool:
        """"""
    @classmethod
    @UseMachineKeyStore.setter
    def UseMachineKeyStore(cls, value: bool) -> None: ...
    def Clear(self) -> None:
        """"""
    def CreateSignature(self, rgbHash: Array[int]) -> Array[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def ExportCspBlob(self, includePrivateParameters: bool) -> Array[int]:
        """"""
    def ExportParameters(self, includePrivateParameters: bool) -> DSAParameters:
        """"""
    def FromXmlString(self, xmlString: str) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ImportCspBlob(self, keyBlob: Array[int]) -> None:
        """"""
    def ImportParameters(self, parameters: DSAParameters) -> None:
        """"""
    @overload
    def SignData(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def SignData(self, data: Stream, hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """"""
    @overload
    def SignData(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def SignData(self, data: Array[int], hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """"""
    @overload
    def SignData(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    @overload
    def SignData(
        self, data: Array[int], offset: int, count: int, hashAlgorithm: HashAlgorithmName
    ) -> Array[int]:
        """"""
    def SignHash(self, rgbHash: Array[int], str: str) -> Array[int]:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXmlString(self, includePrivateParameters: bool) -> str:
        """"""
    @overload
    def VerifyData(
        self, data: Stream, signature: Array[int], hashAlgorithm: HashAlgorithmName
    ) -> bool:
        """"""
    @overload
    def VerifyData(self, rgbData: Array[int], rgbSignature: Array[int]) -> bool:
        """"""
    @overload
    def VerifyData(
        self, data: Array[int], signature: Array[int], hashAlgorithm: HashAlgorithmName
    ) -> bool:
        """"""
    @overload
    def VerifyData(
        self,
        data: Array[int],
        offset: int,
        count: int,
        signature: Array[int],
        hashAlgorithm: HashAlgorithmName,
    ) -> bool:
        """"""
    def VerifyHash(self, rgbHash: Array[int], str: str, rgbSignature: Array[int]) -> bool:
        """"""
    def VerifySignature(self, rgbHash: Array[int], rgbSignature: Array[int]) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DSACspObject(Object):
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class DSAFIPSVERSION_ENUM(Enum):
    """"""

    DSA_FIPS186_2: DSAFIPSVERSION_ENUM = ...
    """"""
    DSA_FIPS186_3: DSAFIPSVERSION_ENUM = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DSAParameters(ValueType):
    """"""

    Counter: Final[int]
    """"""
    G: Final[Array[int]]
    """"""
    J: Final[Array[int]]
    """"""
    P: Final[Array[int]]
    """"""
    Q: Final[Array[int]]
    """"""
    Seed: Final[Array[int]]
    """"""
    X: Final[Array[int]]
    """"""
    Y: Final[Array[int]]
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
class DSASignatureDeformatter(AsymmetricSignatureDeformatter):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, key: AsymmetricAlgorithm) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHashAlgorithm(self, strName: str) -> None:
        """"""
    def SetKey(self, key: AsymmetricAlgorithm) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def VerifySignature(self, hash: HashAlgorithm, rgbSignature: Array[int]) -> bool:
        """"""
    @overload
    def VerifySignature(self, rgbHash: Array[int], rgbSignature: Array[int]) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DSASignatureDescription(SignatureDescription):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def DeformatterAlgorithm(self) -> str:
        """"""
    @DeformatterAlgorithm.setter
    def DeformatterAlgorithm(self, value: str) -> None: ...
    @property
    def DigestAlgorithm(self) -> str:
        """"""
    @DigestAlgorithm.setter
    def DigestAlgorithm(self, value: str) -> None: ...
    @property
    def FormatterAlgorithm(self) -> str:
        """"""
    @FormatterAlgorithm.setter
    def FormatterAlgorithm(self, value: str) -> None: ...
    @property
    def KeyAlgorithm(self) -> str:
        """"""
    @KeyAlgorithm.setter
    def KeyAlgorithm(self, value: str) -> None: ...
    def CreateDeformatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureDeformatter:
        """"""
    def CreateDigest(self) -> HashAlgorithm:
        """"""
    def CreateFormatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureFormatter:
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
class DSASignatureFormatter(AsymmetricSignatureFormatter):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, key: AsymmetricAlgorithm) -> None:
        """"""
    @overload
    def CreateSignature(self, hash: HashAlgorithm) -> Array[int]:
        """"""
    @overload
    def CreateSignature(self, rgbHash: Array[int]) -> Array[int]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHashAlgorithm(self, strName: str) -> None:
        """"""
    def SetKey(self, key: AsymmetricAlgorithm) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DeriveBytes(ABC, Object, IDisposable):
    """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBytes(self, cb: int) -> Array[int]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ECCng(ABC, Object):
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
class ECCurve(ValueType):
    """"""

    A: Final[Array[int]]
    """"""
    B: Final[Array[int]]
    """"""
    Cofactor: Final[Array[int]]
    """"""
    CurveType: Final[ECCurve.ECCurveType]
    """"""
    G: Final[ECPoint]
    """"""
    Hash: Final[HashAlgorithmName | None]
    """"""
    Order: Final[Array[int]]
    """"""
    Polynomial: Final[Array[int]]
    """"""
    Prime: Final[Array[int]]
    """"""
    Seed: Final[Array[int]]
    """"""
    @property
    def IsCharacteristic2(self) -> bool:
        """"""
    @property
    def IsExplicit(self) -> bool:
        """"""
    @property
    def IsNamed(self) -> bool:
        """"""
    @property
    def IsPrime(self) -> bool:
        """"""
    @property
    def Oid(self) -> Oid:
        """"""
    @classmethod
    def CreateFromFriendlyName(cls, oidFriendlyName: str) -> ECCurve:
        """"""
    @classmethod
    def CreateFromOid(cls, curveOid: Oid) -> ECCurve:
        """"""
    @classmethod
    def CreateFromValue(cls, oidValue: str) -> ECCurve:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def Validate(self) -> None:
        """"""
    # noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
    class ECCurveType(Enum):
        """"""

        Implicit: ECCurve.ECCurveType = ...
        """"""
        PrimeShortWeierstrass: ECCurve.ECCurveType = ...
        """"""
        PrimeTwistedEdwards: ECCurve.ECCurveType = ...
        """"""
        PrimeMontgomery: ECCurve.ECCurveType = ...
        """"""
        Characteristic2: ECCurve.ECCurveType = ...
        """"""
        Named: ECCurve.ECCurveType = ...
        """"""

    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class NamedCurves(ABC, Object):
        """"""
        @classmethod
        @property
        def brainpoolP160r1(cls) -> ECCurve:
            """"""
        @classmethod
        @property
        def brainpoolP160t1(cls) -> ECCurve:
            """"""
        @classmethod
        @property
        def brainpoolP192r1(cls) -> ECCurve:
            """"""
        @classmethod
        @property
        def brainpoolP192t1(cls) -> ECCurve:
            """"""
        @classmethod
        @property
        def brainpoolP224r1(cls) -> ECCurve:
            """"""
        @classmethod
        @property
        def brainpoolP224t1(cls) -> ECCurve:
            """"""
        @classmethod
        @property
        def brainpoolP256r1(cls) -> ECCurve:
            """"""
        @classmethod
        @property
        def brainpoolP256t1(cls) -> ECCurve:
            """"""
        @classmethod
        @property
        def brainpoolP320r1(cls) -> ECCurve:
            """"""
        @classmethod
        @property
        def brainpoolP320t1(cls) -> ECCurve:
            """"""
        @classmethod
        @property
        def brainpoolP384r1(cls) -> ECCurve:
            """"""
        @classmethod
        @property
        def brainpoolP384t1(cls) -> ECCurve:
            """"""
        @classmethod
        @property
        def brainpoolP512r1(cls) -> ECCurve:
            """"""
        @classmethod
        @property
        def brainpoolP512t1(cls) -> ECCurve:
            """"""
        @classmethod
        @property
        def nistP256(cls) -> ECCurve:
            """"""
        @classmethod
        @property
        def nistP384(cls) -> ECCurve:
            """"""
        @classmethod
        @property
        def nistP521(cls) -> ECCurve:
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
class ECDiffieHellman(ABC, AsymmetricAlgorithm, IDisposable):
    """"""
    @property
    def KeyExchangeAlgorithm(self) -> str:
        """"""
    @property
    def KeySize(self) -> int:
        """"""
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """"""
    @property
    def PublicKey(self) -> ECDiffieHellmanPublicKey:
        """"""
    @property
    def SignatureAlgorithm(self) -> str:
        """"""
    def Clear(self) -> None:
        """"""
    @classmethod
    @overload
    def Create(cls) -> ECDiffieHellman:
        """"""
    @classmethod
    @overload
    def Create(cls, curve: ECCurve) -> ECDiffieHellman:
        """"""
    @classmethod
    @overload
    def Create(cls, parameters: ECParameters) -> ECDiffieHellman:
        """"""
    @classmethod
    @overload
    def Create(cls, algorithm: str) -> ECDiffieHellman:
        """"""
    @overload
    def DeriveKeyFromHash(
        self, otherPartyPublicKey: ECDiffieHellmanPublicKey, hashAlgorithm: HashAlgorithmName
    ) -> Array[int]:
        """"""
    @overload
    def DeriveKeyFromHash(
        self,
        otherPartyPublicKey: ECDiffieHellmanPublicKey,
        hashAlgorithm: HashAlgorithmName,
        secretPrepend: Array[int],
        secretAppend: Array[int],
    ) -> Array[int]:
        """"""
    @overload
    def DeriveKeyFromHmac(
        self,
        otherPartyPublicKey: ECDiffieHellmanPublicKey,
        hashAlgorithm: HashAlgorithmName,
        hmacKey: Array[int],
    ) -> Array[int]:
        """"""
    @overload
    def DeriveKeyFromHmac(
        self,
        otherPartyPublicKey: ECDiffieHellmanPublicKey,
        hashAlgorithm: HashAlgorithmName,
        hmacKey: Array[int],
        secretPrepend: Array[int],
        secretAppend: Array[int],
    ) -> Array[int]:
        """"""
    def DeriveKeyMaterial(self, otherPartyPublicKey: ECDiffieHellmanPublicKey) -> Array[int]:
        """"""
    def DeriveKeyTls(
        self,
        otherPartyPublicKey: ECDiffieHellmanPublicKey,
        prfLabel: Array[int],
        prfSeed: Array[int],
    ) -> Array[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def ExportExplicitParameters(self, includePrivateParameters: bool) -> ECParameters:
        """"""
    def ExportParameters(self, includePrivateParameters: bool) -> ECParameters:
        """"""
    def FromXmlString(self, xmlString: str) -> None:
        """"""
    def GenerateKey(self, curve: ECCurve) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ImportParameters(self, parameters: ECParameters) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXmlString(self, includePrivateParameters: bool) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ECDiffieHellmanCng(ECDiffieHellman, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, keySize: int) -> None:
        """"""
    @overload
    def __init__(self, curve: ECCurve) -> None:
        """"""
    @overload
    def __init__(self, key: CngKey) -> None:
        """"""
    @property
    def HashAlgorithm(self) -> CngAlgorithm:
        """"""
    @HashAlgorithm.setter
    def HashAlgorithm(self, value: CngAlgorithm) -> None: ...
    @property
    def HmacKey(self) -> Array[int]:
        """"""
    @HmacKey.setter
    def HmacKey(self, value: Array[int]) -> None: ...
    @property
    def Key(self) -> CngKey:
        """"""
    @property
    def KeyDerivationFunction(self) -> ECDiffieHellmanKeyDerivationFunction:
        """"""
    @KeyDerivationFunction.setter
    def KeyDerivationFunction(self, value: ECDiffieHellmanKeyDerivationFunction) -> None: ...
    @property
    def KeyExchangeAlgorithm(self) -> str:
        """"""
    @property
    def KeySize(self) -> int:
        """"""
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def Label(self) -> Array[int]:
        """"""
    @Label.setter
    def Label(self, value: Array[int]) -> None: ...
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """"""
    @property
    def PublicKey(self) -> ECDiffieHellmanPublicKey:
        """"""
    @property
    def SecretAppend(self) -> Array[int]:
        """"""
    @SecretAppend.setter
    def SecretAppend(self, value: Array[int]) -> None: ...
    @property
    def SecretPrepend(self) -> Array[int]:
        """"""
    @SecretPrepend.setter
    def SecretPrepend(self, value: Array[int]) -> None: ...
    @property
    def Seed(self) -> Array[int]:
        """"""
    @Seed.setter
    def Seed(self, value: Array[int]) -> None: ...
    @property
    def SignatureAlgorithm(self) -> str:
        """"""
    @property
    def UseSecretAgreementAsHmacKey(self) -> bool:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def DeriveKeyFromHash(
        self, otherPartyPublicKey: ECDiffieHellmanPublicKey, hashAlgorithm: HashAlgorithmName
    ) -> Array[int]:
        """"""
    @overload
    def DeriveKeyFromHash(
        self,
        otherPartyPublicKey: ECDiffieHellmanPublicKey,
        hashAlgorithm: HashAlgorithmName,
        secretPrepend: Array[int],
        secretAppend: Array[int],
    ) -> Array[int]:
        """"""
    @overload
    def DeriveKeyFromHmac(
        self,
        otherPartyPublicKey: ECDiffieHellmanPublicKey,
        hashAlgorithm: HashAlgorithmName,
        hmacKey: Array[int],
    ) -> Array[int]:
        """"""
    @overload
    def DeriveKeyFromHmac(
        self,
        otherPartyPublicKey: ECDiffieHellmanPublicKey,
        hashAlgorithm: HashAlgorithmName,
        hmacKey: Array[int],
        secretPrepend: Array[int],
        secretAppend: Array[int],
    ) -> Array[int]:
        """"""
    @overload
    def DeriveKeyMaterial(self, otherPartyPublicKey: CngKey) -> Array[int]:
        """"""
    @overload
    def DeriveKeyMaterial(self, otherPartyPublicKey: ECDiffieHellmanPublicKey) -> Array[int]:
        """"""
    def DeriveKeyTls(
        self,
        otherPartyPublicKey: ECDiffieHellmanPublicKey,
        prfLabel: Array[int],
        prfSeed: Array[int],
    ) -> Array[int]:
        """"""
    @overload
    def DeriveSecretAgreementHandle(self, otherPartyPublicKey: CngKey) -> SafeNCryptSecretHandle:
        """"""
    @overload
    def DeriveSecretAgreementHandle(
        self, otherPartyPublicKey: ECDiffieHellmanPublicKey
    ) -> SafeNCryptSecretHandle:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def ExportExplicitParameters(self, includePrivateParameters: bool) -> ECParameters:
        """"""
    def ExportParameters(self, includePrivateParameters: bool) -> ECParameters:
        """"""
    @overload
    def FromXmlString(self, xmlString: str) -> None:
        """"""
    @overload
    def FromXmlString(self, xml: str, format: ECKeyXmlFormat) -> None:
        """"""
    def GenerateKey(self, curve: ECCurve) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ImportParameters(self, parameters: ECParameters) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def ToXmlString(self, format: ECKeyXmlFormat) -> str:
        """"""
    @overload
    def ToXmlString(self, includePrivateParameters: bool) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ECDiffieHellmanCngPublicKey(ECDiffieHellmanPublicKey, IDisposable):
    """"""
    @property
    def BlobFormat(self) -> CngKeyBlobFormat:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def ExportExplicitParameters(self) -> ECParameters:
        """"""
    def ExportParameters(self) -> ECParameters:
        """"""
    @classmethod
    def FromByteArray(
        cls, publicKeyBlob: Array[int], format: CngKeyBlobFormat
    ) -> ECDiffieHellmanPublicKey:
        """"""
    @classmethod
    def FromXmlString(cls, xml: str) -> ECDiffieHellmanCngPublicKey:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Import(self) -> CngKey:
        """"""
    def ToByteArray(self) -> Array[int]:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXmlString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class ECDiffieHellmanKeyDerivationFunction(Enum):
    """"""

    Hash: ECDiffieHellmanKeyDerivationFunction = ...
    """"""
    Hmac: ECDiffieHellmanKeyDerivationFunction = ...
    """"""
    Tls: ECDiffieHellmanKeyDerivationFunction = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ECDiffieHellmanPublicKey(ABC, Object, IDisposable):
    """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def ExportExplicitParameters(self) -> ECParameters:
        """"""
    def ExportParameters(self) -> ECParameters:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToByteArray(self) -> Array[int]:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXmlString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ECDsa(ABC, AsymmetricAlgorithm, IDisposable):
    """"""
    @property
    def KeyExchangeAlgorithm(self) -> str:
        """"""
    @property
    def KeySize(self) -> int:
        """"""
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """"""
    @property
    def SignatureAlgorithm(self) -> str:
        """"""
    def Clear(self) -> None:
        """"""
    @classmethod
    @overload
    def Create(cls) -> ECDsa:
        """"""
    @classmethod
    @overload
    def Create(cls, curve: ECCurve) -> ECDsa:
        """"""
    @classmethod
    @overload
    def Create(cls, parameters: ECParameters) -> ECDsa:
        """"""
    @classmethod
    @overload
    def Create(cls, algorithm: str) -> ECDsa:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def ExportExplicitParameters(self, includePrivateParameters: bool) -> ECParameters:
        """"""
    def ExportParameters(self, includePrivateParameters: bool) -> ECParameters:
        """"""
    def FromXmlString(self, xmlString: str) -> None:
        """"""
    def GenerateKey(self, curve: ECCurve) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ImportParameters(self, parameters: ECParameters) -> None:
        """"""
    @overload
    def SignData(self, data: Stream, hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """"""
    @overload
    def SignData(self, data: Array[int], hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """"""
    @overload
    def SignData(
        self, data: Array[int], offset: int, count: int, hashAlgorithm: HashAlgorithmName
    ) -> Array[int]:
        """"""
    def SignHash(self, hash: Array[int]) -> Array[int]:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXmlString(self, includePrivateParameters: bool) -> str:
        """"""
    @overload
    def VerifyData(
        self, data: Stream, signature: Array[int], hashAlgorithm: HashAlgorithmName
    ) -> bool:
        """"""
    @overload
    def VerifyData(
        self, data: Array[int], signature: Array[int], hashAlgorithm: HashAlgorithmName
    ) -> bool:
        """"""
    @overload
    def VerifyData(
        self,
        data: Array[int],
        offset: int,
        count: int,
        signature: Array[int],
        hashAlgorithm: HashAlgorithmName,
    ) -> bool:
        """"""
    def VerifyHash(self, hash: Array[int], signature: Array[int]) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ECDsaCng(ECDsa, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, keySize: int) -> None:
        """"""
    @overload
    def __init__(self, curve: ECCurve) -> None:
        """"""
    @overload
    def __init__(self, key: CngKey) -> None:
        """"""
    @property
    def HashAlgorithm(self) -> CngAlgorithm:
        """"""
    @HashAlgorithm.setter
    def HashAlgorithm(self, value: CngAlgorithm) -> None: ...
    @property
    def Key(self) -> CngKey:
        """"""
    @property
    def KeyExchangeAlgorithm(self) -> str:
        """"""
    @property
    def KeySize(self) -> int:
        """"""
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """"""
    @property
    def SignatureAlgorithm(self) -> str:
        """"""
    def Clear(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def ExportExplicitParameters(self, includePrivateParameters: bool) -> ECParameters:
        """"""
    def ExportParameters(self, includePrivateParameters: bool) -> ECParameters:
        """"""
    @overload
    def FromXmlString(self, xmlString: str) -> None:
        """"""
    @overload
    def FromXmlString(self, xml: str, format: ECKeyXmlFormat) -> None:
        """"""
    def GenerateKey(self, curve: ECCurve) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ImportParameters(self, parameters: ECParameters) -> None:
        """"""
    @overload
    def SignData(self, data: Stream) -> Array[int]:
        """"""
    @overload
    def SignData(self, data: Stream, hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """"""
    @overload
    def SignData(self, data: Array[int]) -> Array[int]:
        """"""
    @overload
    def SignData(self, data: Array[int], hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """"""
    @overload
    def SignData(self, data: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    @overload
    def SignData(
        self, data: Array[int], offset: int, count: int, hashAlgorithm: HashAlgorithmName
    ) -> Array[int]:
        """"""
    def SignHash(self, hash: Array[int]) -> Array[int]:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def ToXmlString(self, format: ECKeyXmlFormat) -> str:
        """"""
    @overload
    def ToXmlString(self, includePrivateParameters: bool) -> str:
        """"""
    @overload
    def VerifyData(self, data: Stream, signature: Array[int]) -> bool:
        """"""
    @overload
    def VerifyData(
        self, data: Stream, signature: Array[int], hashAlgorithm: HashAlgorithmName
    ) -> bool:
        """"""
    @overload
    def VerifyData(self, data: Array[int], signature: Array[int]) -> bool:
        """"""
    @overload
    def VerifyData(
        self, data: Array[int], signature: Array[int], hashAlgorithm: HashAlgorithmName
    ) -> bool:
        """"""
    @overload
    def VerifyData(self, data: Array[int], offset: int, count: int, signature: Array[int]) -> bool:
        """"""
    @overload
    def VerifyData(
        self,
        data: Array[int],
        offset: int,
        count: int,
        signature: Array[int],
        hashAlgorithm: HashAlgorithmName,
    ) -> bool:
        """"""
    def VerifyHash(self, hash: Array[int], signature: Array[int]) -> bool:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class ECKeyXmlFormat(Enum):
    """"""

    Rfc4050: ECKeyXmlFormat = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ECParameters(ValueType):
    """"""

    Curve: Final[ECCurve]
    """"""
    D: Final[Array[int]]
    """"""
    Q: Final[ECPoint]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def Validate(self) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ECPoint(ValueType):
    """"""

    X: Final[Array[int]]
    """"""
    Y: Final[Array[int]]
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
class EncryptionMode(Enum):
    """"""

    Encrypt: EncryptionMode = ...
    """"""
    Decrypt: EncryptionMode = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class FromBase64Transform(Object, ICryptoTransform, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, whitespaces: FromBase64TransformMode) -> None:
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class FromBase64TransformMode(Enum):
    """"""

    IgnoreWhiteSpaces: FromBase64TransformMode = ...
    """"""
    DoNotIgnoreWhiteSpaces: FromBase64TransformMode = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class HASHALGORITHM_ENUM(Enum):
    """"""

    DSA_HASH_ALGORITHM_SHA1: HASHALGORITHM_ENUM = ...
    """"""
    DSA_HASH_ALGORITHM_SHA256: HASHALGORITHM_ENUM = ...
    """"""
    DSA_HASH_ALGORITHM_SHA512: HASHALGORITHM_ENUM = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class HMAC(ABC, KeyedHashAlgorithm, ICryptoTransform, IDisposable):
    """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def Hash(self) -> Array[int]:
        """"""
    @property
    def HashName(self) -> str:
        """"""
    @HashName.setter
    def HashName(self, value: str) -> None: ...
    @property
    def HashSize(self) -> int:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def Key(self) -> Array[int]:
        """"""
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    @classmethod
    @overload
    def Create(cls) -> HMAC:
        """"""
    @classmethod
    @overload
    def Create(cls, algorithmName: str) -> HMAC:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class HMACMD5(HMAC, ICryptoTransform, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, key: Array[int]) -> None:
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def Hash(self) -> Array[int]:
        """"""
    @property
    def HashName(self) -> str:
        """"""
    @HashName.setter
    def HashName(self, value: str) -> None: ...
    @property
    def HashSize(self) -> int:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def Key(self) -> Array[int]:
        """"""
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class HMACRIPEMD160(HMAC, ICryptoTransform, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, key: Array[int]) -> None:
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def Hash(self) -> Array[int]:
        """"""
    @property
    def HashName(self) -> str:
        """"""
    @HashName.setter
    def HashName(self, value: str) -> None: ...
    @property
    def HashSize(self) -> int:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def Key(self) -> Array[int]:
        """"""
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class HMACSHA1(HMAC, ICryptoTransform, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, key: Array[int]) -> None:
        """"""
    @overload
    def __init__(self, key: Array[int], useManagedSha1: bool) -> None:
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def Hash(self) -> Array[int]:
        """"""
    @property
    def HashName(self) -> str:
        """"""
    @HashName.setter
    def HashName(self, value: str) -> None: ...
    @property
    def HashSize(self) -> int:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def Key(self) -> Array[int]:
        """"""
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class HMACSHA256(HMAC, ICryptoTransform, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, key: Array[int]) -> None:
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def Hash(self) -> Array[int]:
        """"""
    @property
    def HashName(self) -> str:
        """"""
    @HashName.setter
    def HashName(self, value: str) -> None: ...
    @property
    def HashSize(self) -> int:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def Key(self) -> Array[int]:
        """"""
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class HMACSHA384(HMAC, ICryptoTransform, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, key: Array[int]) -> None:
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def Hash(self) -> Array[int]:
        """"""
    @property
    def HashName(self) -> str:
        """"""
    @HashName.setter
    def HashName(self, value: str) -> None: ...
    @property
    def HashSize(self) -> int:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def Key(self) -> Array[int]:
        """"""
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def OutputBlockSize(self) -> int:
        """"""
    @property
    def ProduceLegacyHmacValues(self) -> bool:
        """"""
    @ProduceLegacyHmacValues.setter
    def ProduceLegacyHmacValues(self, value: bool) -> None: ...
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class HMACSHA512(HMAC, ICryptoTransform, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, key: Array[int]) -> None:
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def Hash(self) -> Array[int]:
        """"""
    @property
    def HashName(self) -> str:
        """"""
    @HashName.setter
    def HashName(self, value: str) -> None: ...
    @property
    def HashSize(self) -> int:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def Key(self) -> Array[int]:
        """"""
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def OutputBlockSize(self) -> int:
        """"""
    @property
    def ProduceLegacyHmacValues(self) -> bool:
        """"""
    @ProduceLegacyHmacValues.setter
    def ProduceLegacyHmacValues(self, value: bool) -> None: ...
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class HashAlgorithm(ABC, Object, ICryptoTransform, IDisposable):
    """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def Hash(self) -> Array[int]:
        """"""
    @property
    def HashSize(self) -> int:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    @classmethod
    @overload
    def Create(cls) -> HashAlgorithm:
        """"""
    @classmethod
    @overload
    def Create(cls, hashName: str) -> HashAlgorithm:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class HashAlgorithmName(ValueType, IEquatable[HashAlgorithmName]):
    """"""
    def __init__(self, name: str) -> None:
        """"""
    @classmethod
    @property
    def MD5(cls) -> HashAlgorithmName:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @classmethod
    @property
    def SHA1(cls) -> HashAlgorithmName:
        """"""
    @classmethod
    @property
    def SHA256(cls) -> HashAlgorithmName:
        """"""
    @classmethod
    @property
    def SHA384(cls) -> HashAlgorithmName:
        """"""
    @classmethod
    @property
    def SHA512(cls) -> HashAlgorithmName:
        """"""
    @overload
    def Equals(self, other: HashAlgorithmName) -> bool:
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
    def op_Equality(cls, left: HashAlgorithmName, right: HashAlgorithmName) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: HashAlgorithmName, right: HashAlgorithmName) -> bool:
        """"""
    def __eq__(self, other: HashAlgorithmName) -> bool:
        """"""
    def __ne__(self, other: HashAlgorithmName) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ICryptoTransform(ABC, IDisposable):
    """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Dispose(self) -> None:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ICspAsymmetricAlgorithm(ABC):
    """"""
    @property
    def CspKeyContainerInfo(self) -> CspKeyContainerInfo:
        """"""
    def ExportCspBlob(self, includePrivateParameters: bool) -> Array[int]:
        """"""
    def ImportCspBlob(self, rawData: Array[int]) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IncrementalHash(Object, IDisposable):
    """"""
    @property
    def AlgorithmName(self) -> HashAlgorithmName:
        """"""
    @overload
    def AppendData(self, data: Array[int]) -> None:
        """"""
    @overload
    def AppendData(self, data: Array[int], offset: int, count: int) -> None:
        """"""
    @classmethod
    def CreateHMAC(cls, hashAlgorithm: HashAlgorithmName, key: Array[int]) -> IncrementalHash:
        """"""
    @classmethod
    def CreateHash(cls, hashAlgorithm: HashAlgorithmName) -> IncrementalHash:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashAndReset(self) -> Array[int]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class KeyNumber(Enum):
    """"""

    Exchange: KeyNumber = ...
    """"""
    Signature: KeyNumber = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class KeySizes(Object):
    """"""
    def __init__(self, minSize: int, maxSize: int, skipSize: int) -> None:
        """"""
    @property
    def MaxSize(self) -> int:
        """"""
    @property
    def MinSize(self) -> int:
        """"""
    @property
    def SkipSize(self) -> int:
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
class KeyedHashAlgorithm(ABC, HashAlgorithm, ICryptoTransform, IDisposable):
    """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def Hash(self) -> Array[int]:
        """"""
    @property
    def HashSize(self) -> int:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def Key(self) -> Array[int]:
        """"""
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    @classmethod
    @overload
    def Create(cls) -> KeyedHashAlgorithm:
        """"""
    @classmethod
    @overload
    def Create(cls, algName: str) -> KeyedHashAlgorithm:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MACTripleDES(KeyedHashAlgorithm, ICryptoTransform, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, rgbKey: Array[int]) -> None:
        """"""
    @overload
    def __init__(self, strTripleDES: str, rgbKey: Array[int]) -> None:
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def Hash(self) -> Array[int]:
        """"""
    @property
    def HashSize(self) -> int:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def Key(self) -> Array[int]:
        """"""
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def OutputBlockSize(self) -> int:
        """"""
    @property
    def Padding(self) -> PaddingMode:
        """"""
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MD5(ABC, HashAlgorithm, ICryptoTransform, IDisposable):
    """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def Hash(self) -> Array[int]:
        """"""
    @property
    def HashSize(self) -> int:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    @classmethod
    @overload
    def Create(cls) -> MD5:
        """"""
    @classmethod
    @overload
    def Create(cls, algName: str) -> MD5:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MD5Cng(MD5, ICryptoTransform, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def Hash(self) -> Array[int]:
        """"""
    @property
    def HashSize(self) -> int:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MD5CryptoServiceProvider(MD5, ICryptoTransform, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def Hash(self) -> Array[int]:
        """"""
    @property
    def HashSize(self) -> int:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ManifestSignatureInformation(Object):
    """"""
    @property
    def AuthenticodeSignature(self) -> AuthenticodeSignatureInformation:
        """"""
    @property
    def Manifest(self) -> ManifestKinds:
        """"""
    @property
    def StrongNameSignature(self) -> StrongNameSignatureInformation:
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
    @overload
    def VerifySignature(
        cls, application: ActivationContext
    ) -> ManifestSignatureInformationCollection:
        """"""
    @classmethod
    @overload
    def VerifySignature(
        cls, application: ActivationContext, manifests: ManifestKinds
    ) -> ManifestSignatureInformationCollection:
        """"""
    @classmethod
    @overload
    def VerifySignature(
        cls,
        application: ActivationContext,
        manifests: ManifestKinds,
        revocationFlag: X509RevocationFlag,
        revocationMode: X509RevocationMode,
    ) -> ManifestSignatureInformationCollection:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ManifestSignatureInformationCollection(
    ReadOnlyCollection[ManifestSignatureInformation],
    ICollection[ManifestSignatureInformation],
    IEnumerable[ManifestSignatureInformation],
    IList[ManifestSignatureInformation],
    IReadOnlyCollection[ManifestSignatureInformation],
    IReadOnlyList[ManifestSignatureInformation],
    ICollection,
    IEnumerable,
    IList,
):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> ManifestSignatureInformation:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, item: ManifestSignatureInformation) -> None:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: ManifestSignatureInformation) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[ManifestSignatureInformation], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[ManifestSignatureInformation]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, value: ManifestSignatureInformation) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, item: ManifestSignatureInformation) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, item: ManifestSignatureInformation) -> bool:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, value: ManifestSignatureInformation) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator[ManifestSignatureInformation]:
        """"""
    @overload
    def __delitem__(self, item: ManifestSignatureInformation) -> bool:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> ManifestSignatureInformation:
        """"""
    @overload
    def __setitem__(self, index: int, value: ManifestSignatureInformation) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MaskGenerationMethod(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GenerateMask(self, rgbSeed: Array[int], cbReturn: int) -> Array[int]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class NCryptNative(ABC, Object):
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
class NativeHmac(Object, IDisposable):
    """"""
    def Dispose(self) -> None:
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
class Oid(Object):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, oid: str) -> None:
        """"""
    @overload
    def __init__(self, value: str, friendlyName: str) -> None:
        """"""
    @overload
    def __init__(self, oid: Oid) -> None:
        """"""
    @property
    def FriendlyName(self) -> str:
        """"""
    @FriendlyName.setter
    def FriendlyName(self, value: str) -> None: ...
    @property
    def Value(self) -> str:
        """"""
    @Value.setter
    def Value(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def FromFriendlyName(cls, friendlyName: str, group: OidGroup) -> Oid:
        """"""
    @classmethod
    def FromOidValue(cls, oidValue: str, group: OidGroup) -> Oid:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class OidCollection(Object, ICollection, IEnumerable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> Oid:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    def Add(self, oid: Oid) -> int:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[Oid], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> OidEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""
    @overload
    def __getitem__(self, index: int) -> Oid:
        """"""
    @overload
    def __getitem__(self, oid: str) -> Oid:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class OidEnumerator(Object, IEnumerator):
    """"""
    @property
    def Current(self) -> Oid:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MoveNext(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class OidGroup(Enum):
    """"""

    All: OidGroup = ...
    """"""
    HashAlgorithm: OidGroup = ...
    """"""
    EncryptionAlgorithm: OidGroup = ...
    """"""
    PublicKeyAlgorithm: OidGroup = ...
    """"""
    SignatureAlgorithm: OidGroup = ...
    """"""
    Attribute: OidGroup = ...
    """"""
    ExtensionOrAttribute: OidGroup = ...
    """"""
    EnhancedKeyUsage: OidGroup = ...
    """"""
    Policy: OidGroup = ...
    """"""
    Template: OidGroup = ...
    """"""
    KeyDerivationFunction: OidGroup = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PKCS1MaskGenerationMethod(MaskGenerationMethod):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def HashName(self) -> str:
        """"""
    @HashName.setter
    def HashName(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GenerateMask(self, rgbSeed: Array[int], cbReturn: int) -> Array[int]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class PaddingMode(Enum):
    """"""

    _None: PaddingMode = ...
    """"""
    PKCS7: PaddingMode = ...
    """"""
    Zeros: PaddingMode = ...
    """"""
    ANSIX923: PaddingMode = ...
    """"""
    ISO10126: PaddingMode = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PasswordDeriveBytes(DeriveBytes, IDisposable):
    """"""
    @overload
    def __init__(self, strPassword: str, rgbSalt: Array[int]) -> None:
        """"""
    @overload
    def __init__(self, password: Array[int], salt: Array[int]) -> None:
        """"""
    @overload
    def __init__(
        self, strPassword: str, rgbSalt: Array[int], strHashName: str, iterations: int
    ) -> None:
        """"""
    @overload
    def __init__(
        self, password: Array[int], salt: Array[int], hashName: str, iterations: int
    ) -> None:
        """"""
    @overload
    def __init__(self, strPassword: str, rgbSalt: Array[int], cspParams: CspParameters) -> None:
        """"""
    @overload
    def __init__(self, password: Array[int], salt: Array[int], cspParams: CspParameters) -> None:
        """"""
    @overload
    def __init__(
        self,
        strPassword: str,
        rgbSalt: Array[int],
        strHashName: str,
        iterations: int,
        cspParams: CspParameters,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        password: Array[int],
        salt: Array[int],
        hashName: str,
        iterations: int,
        cspParams: CspParameters,
    ) -> None:
        """"""
    @property
    def HashName(self) -> str:
        """"""
    @HashName.setter
    def HashName(self, value: str) -> None: ...
    @property
    def IterationCount(self) -> int:
        """"""
    @IterationCount.setter
    def IterationCount(self, value: int) -> None: ...
    @property
    def Salt(self) -> Array[int]:
        """"""
    @Salt.setter
    def Salt(self, value: Array[int]) -> None: ...
    def CryptDeriveKey(
        self, algname: str, alghashname: str, keySize: int, rgbIV: Array[int]
    ) -> Array[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBytes(self, cb: int) -> Array[int]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RC2(ABC, SymmetricAlgorithm, IDisposable):
    """"""
    @property
    def BlockSize(self) -> int:
        """"""
    @BlockSize.setter
    def BlockSize(self, value: int) -> None: ...
    @property
    def EffectiveKeySize(self) -> int:
        """"""
    @EffectiveKeySize.setter
    def EffectiveKeySize(self, value: int) -> None: ...
    @property
    def FeedbackSize(self) -> int:
        """"""
    @FeedbackSize.setter
    def FeedbackSize(self, value: int) -> None: ...
    @property
    def IV(self) -> Array[int]:
        """"""
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def Key(self) -> Array[int]:
        """"""
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def KeySize(self) -> int:
        """"""
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalBlockSizes(self) -> Array[KeySizes]:
        """"""
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """"""
    @property
    def Mode(self) -> CipherMode:
        """"""
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    @property
    def Padding(self) -> PaddingMode:
        """"""
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    def Clear(self) -> None:
        """"""
    @classmethod
    @overload
    def Create(cls) -> RC2:
        """"""
    @classmethod
    @overload
    def Create(cls, AlgName: str) -> RC2:
        """"""
    @overload
    def CreateDecryptor(self) -> ICryptoTransform:
        """"""
    @overload
    def CreateDecryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """"""
    @overload
    def CreateEncryptor(self) -> ICryptoTransform:
        """"""
    @overload
    def CreateEncryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GenerateIV(self) -> None:
        """"""
    def GenerateKey(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def ValidKeySize(self, bitLength: int) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RC2CryptoServiceProvider(RC2, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def BlockSize(self) -> int:
        """"""
    @BlockSize.setter
    def BlockSize(self, value: int) -> None: ...
    @property
    def EffectiveKeySize(self) -> int:
        """"""
    @EffectiveKeySize.setter
    def EffectiveKeySize(self, value: int) -> None: ...
    @property
    def FeedbackSize(self) -> int:
        """"""
    @FeedbackSize.setter
    def FeedbackSize(self, value: int) -> None: ...
    @property
    def IV(self) -> Array[int]:
        """"""
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def Key(self) -> Array[int]:
        """"""
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def KeySize(self) -> int:
        """"""
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalBlockSizes(self) -> Array[KeySizes]:
        """"""
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """"""
    @property
    def Mode(self) -> CipherMode:
        """"""
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    @property
    def Padding(self) -> PaddingMode:
        """"""
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    @property
    def UseSalt(self) -> bool:
        """"""
    @UseSalt.setter
    def UseSalt(self, value: bool) -> None: ...
    def Clear(self) -> None:
        """"""
    @overload
    def CreateDecryptor(self) -> ICryptoTransform:
        """"""
    @overload
    def CreateDecryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """"""
    @overload
    def CreateEncryptor(self) -> ICryptoTransform:
        """"""
    @overload
    def CreateEncryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GenerateIV(self) -> None:
        """"""
    def GenerateKey(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def ValidKeySize(self, bitLength: int) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RIPEMD160(ABC, HashAlgorithm, ICryptoTransform, IDisposable):
    """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def Hash(self) -> Array[int]:
        """"""
    @property
    def HashSize(self) -> int:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    @classmethod
    @overload
    def Create(cls) -> RIPEMD160:
        """"""
    @classmethod
    @overload
    def Create(cls, hashName: str) -> RIPEMD160:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RIPEMD160Managed(RIPEMD160, ICryptoTransform, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def Hash(self) -> Array[int]:
        """"""
    @property
    def HashSize(self) -> int:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RNGCryptoServiceProvider(RandomNumberGenerator, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, str: str) -> None:
        """"""
    @overload
    def __init__(self, rgb: Array[int]) -> None:
        """"""
    @overload
    def __init__(self, cspParams: CspParameters) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetBytes(self, data: Array[int]) -> None:
        """"""
    @overload
    def GetBytes(self, data: Array[int], offset: int, count: int) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetNonZeroBytes(self, data: Array[int]) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RSA(ABC, AsymmetricAlgorithm, IDisposable):
    """"""
    @property
    def KeyExchangeAlgorithm(self) -> str:
        """"""
    @property
    def KeySize(self) -> int:
        """"""
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """"""
    @property
    def SignatureAlgorithm(self) -> str:
        """"""
    def Clear(self) -> None:
        """"""
    @classmethod
    @overload
    def Create(cls) -> RSA:
        """"""
    @classmethod
    @overload
    def Create(cls, parameters: RSAParameters) -> RSA:
        """"""
    @classmethod
    @overload
    def Create(cls, keySizeInBits: int) -> RSA:
        """"""
    @classmethod
    @overload
    def Create(cls, algName: str) -> RSA:
        """"""
    def Decrypt(self, data: Array[int], padding: RSAEncryptionPadding) -> Array[int]:
        """"""
    def DecryptValue(self, rgb: Array[int]) -> Array[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Encrypt(self, data: Array[int], padding: RSAEncryptionPadding) -> Array[int]:
        """"""
    def EncryptValue(self, rgb: Array[int]) -> Array[int]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def ExportParameters(self, includePrivateParameters: bool) -> RSAParameters:
        """"""
    def FromXmlString(self, xmlString: str) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ImportParameters(self, parameters: RSAParameters) -> None:
        """"""
    @overload
    def SignData(
        self, data: Stream, hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding
    ) -> Array[int]:
        """"""
    @overload
    def SignData(
        self, data: Array[int], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding
    ) -> Array[int]:
        """"""
    @overload
    def SignData(
        self,
        data: Array[int],
        offset: int,
        count: int,
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> Array[int]:
        """"""
    def SignHash(
        self, hash: Array[int], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding
    ) -> Array[int]:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXmlString(self, includePrivateParameters: bool) -> str:
        """"""
    @overload
    def VerifyData(
        self,
        data: Stream,
        signature: Array[int],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> bool:
        """"""
    @overload
    def VerifyData(
        self,
        data: Array[int],
        signature: Array[int],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> bool:
        """"""
    @overload
    def VerifyData(
        self,
        data: Array[int],
        offset: int,
        count: int,
        signature: Array[int],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> bool:
        """"""
    def VerifyHash(
        self,
        hash: Array[int],
        signature: Array[int],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RSACng(RSA, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, keySize: int) -> None:
        """"""
    @overload
    def __init__(self, key: CngKey) -> None:
        """"""
    @property
    def Key(self) -> CngKey:
        """"""
    @property
    def KeyExchangeAlgorithm(self) -> str:
        """"""
    @property
    def KeySize(self) -> int:
        """"""
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """"""
    @property
    def SignatureAlgorithm(self) -> str:
        """"""
    def Clear(self) -> None:
        """"""
    def Decrypt(self, data: Array[int], padding: RSAEncryptionPadding) -> Array[int]:
        """"""
    def DecryptValue(self, rgb: Array[int]) -> Array[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Encrypt(self, data: Array[int], padding: RSAEncryptionPadding) -> Array[int]:
        """"""
    def EncryptValue(self, rgb: Array[int]) -> Array[int]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def ExportParameters(self, includePrivateParameters: bool) -> RSAParameters:
        """"""
    def FromXmlString(self, xmlString: str) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ImportParameters(self, parameters: RSAParameters) -> None:
        """"""
    @overload
    def SignData(
        self, data: Stream, hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding
    ) -> Array[int]:
        """"""
    @overload
    def SignData(
        self, data: Array[int], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding
    ) -> Array[int]:
        """"""
    @overload
    def SignData(
        self,
        data: Array[int],
        offset: int,
        count: int,
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> Array[int]:
        """"""
    def SignHash(
        self, hash: Array[int], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding
    ) -> Array[int]:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXmlString(self, includePrivateParameters: bool) -> str:
        """"""
    @overload
    def VerifyData(
        self,
        data: Stream,
        signature: Array[int],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> bool:
        """"""
    @overload
    def VerifyData(
        self,
        data: Array[int],
        signature: Array[int],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> bool:
        """"""
    @overload
    def VerifyData(
        self,
        data: Array[int],
        offset: int,
        count: int,
        signature: Array[int],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> bool:
        """"""
    def VerifyHash(
        self,
        hash: Array[int],
        signature: Array[int],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RSACryptoServiceProvider(RSA, ICspAsymmetricAlgorithm, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, dwKeySize: int) -> None:
        """"""
    @overload
    def __init__(self, parameters: CspParameters) -> None:
        """"""
    @overload
    def __init__(self, dwKeySize: int, parameters: CspParameters) -> None:
        """"""
    @property
    def CspKeyContainerInfo(self) -> CspKeyContainerInfo:
        """"""
    @property
    def KeyExchangeAlgorithm(self) -> str:
        """"""
    @property
    def KeySize(self) -> int:
        """"""
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """"""
    @property
    def PersistKeyInCsp(self) -> bool:
        """"""
    @PersistKeyInCsp.setter
    def PersistKeyInCsp(self, value: bool) -> None: ...
    @property
    def PublicOnly(self) -> bool:
        """"""
    @property
    def SignatureAlgorithm(self) -> str:
        """"""
    @classmethod
    @property
    def UseMachineKeyStore(cls) -> bool:
        """"""
    @classmethod
    @UseMachineKeyStore.setter
    def UseMachineKeyStore(cls, value: bool) -> None: ...
    def Clear(self) -> None:
        """"""
    @overload
    def Decrypt(self, data: Array[int], padding: RSAEncryptionPadding) -> Array[int]:
        """"""
    @overload
    def Decrypt(self, rgb: Array[int], fOAEP: bool) -> Array[int]:
        """"""
    def DecryptValue(self, rgb: Array[int]) -> Array[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    @overload
    def Encrypt(self, data: Array[int], padding: RSAEncryptionPadding) -> Array[int]:
        """"""
    @overload
    def Encrypt(self, rgb: Array[int], fOAEP: bool) -> Array[int]:
        """"""
    def EncryptValue(self, rgb: Array[int]) -> Array[int]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def ExportCspBlob(self, includePrivateParameters: bool) -> Array[int]:
        """"""
    def ExportParameters(self, includePrivateParameters: bool) -> RSAParameters:
        """"""
    def FromXmlString(self, xmlString: str) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ImportCspBlob(self, keyBlob: Array[int]) -> None:
        """"""
    def ImportParameters(self, parameters: RSAParameters) -> None:
        """"""
    @overload
    def SignData(
        self, data: Stream, hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding
    ) -> Array[int]:
        """"""
    @overload
    def SignData(self, inputStream: Stream, halg: object) -> Array[int]:
        """"""
    @overload
    def SignData(
        self, data: Array[int], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding
    ) -> Array[int]:
        """"""
    @overload
    def SignData(
        self,
        data: Array[int],
        offset: int,
        count: int,
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> Array[int]:
        """"""
    @overload
    def SignData(self, buffer: Array[int], offset: int, count: int, halg: object) -> Array[int]:
        """"""
    @overload
    def SignData(self, buffer: Array[int], halg: object) -> Array[int]:
        """"""
    @overload
    def SignHash(
        self, hash: Array[int], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding
    ) -> Array[int]:
        """"""
    @overload
    def SignHash(self, rgbHash: Array[int], str: str) -> Array[int]:
        """"""
    def ToString(self) -> str:
        """"""
    def ToXmlString(self, includePrivateParameters: bool) -> str:
        """"""
    @overload
    def VerifyData(
        self,
        data: Stream,
        signature: Array[int],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> bool:
        """"""
    @overload
    def VerifyData(
        self,
        data: Array[int],
        signature: Array[int],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> bool:
        """"""
    @overload
    def VerifyData(
        self,
        data: Array[int],
        offset: int,
        count: int,
        signature: Array[int],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> bool:
        """"""
    @overload
    def VerifyData(self, buffer: Array[int], halg: object, signature: Array[int]) -> bool:
        """"""
    @overload
    def VerifyHash(
        self,
        hash: Array[int],
        signature: Array[int],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> bool:
        """"""
    @overload
    def VerifyHash(self, rgbHash: Array[int], str: str, rgbSignature: Array[int]) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RSACspObject(Object):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RSAEncryptionPadding(Object, IEquatable[RSAEncryptionPadding]):
    """"""
    @property
    def Mode(self) -> RSAEncryptionPaddingMode:
        """"""
    @property
    def OaepHashAlgorithm(self) -> HashAlgorithmName:
        """"""
    @classmethod
    @property
    def OaepSHA1(cls) -> RSAEncryptionPadding:
        """"""
    @classmethod
    @property
    def OaepSHA256(cls) -> RSAEncryptionPadding:
        """"""
    @classmethod
    @property
    def OaepSHA384(cls) -> RSAEncryptionPadding:
        """"""
    @classmethod
    @property
    def OaepSHA512(cls) -> RSAEncryptionPadding:
        """"""
    @classmethod
    @property
    def Pkcs1(cls) -> RSAEncryptionPadding:
        """"""
    @classmethod
    def CreateOaep(cls, hashAlgorithm: HashAlgorithmName) -> RSAEncryptionPadding:
        """"""
    @overload
    def Equals(self, other: RSAEncryptionPadding) -> bool:
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
    def op_Equality(cls, left: RSAEncryptionPadding, right: RSAEncryptionPadding) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: RSAEncryptionPadding, right: RSAEncryptionPadding) -> bool:
        """"""
    def __eq__(self, other: RSAEncryptionPadding) -> bool:
        """"""
    def __ne__(self, other: RSAEncryptionPadding) -> bool:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class RSAEncryptionPaddingMode(Enum):
    """"""

    Pkcs1: RSAEncryptionPaddingMode = ...
    """"""
    Oaep: RSAEncryptionPaddingMode = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RSAOAEPKeyExchangeDeformatter(AsymmetricKeyExchangeDeformatter):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, key: AsymmetricAlgorithm) -> None:
        """"""
    @property
    def Parameters(self) -> str:
        """"""
    @Parameters.setter
    def Parameters(self, value: str) -> None: ...
    def DecryptKeyExchange(self, rgbData: Array[int]) -> Array[int]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetKey(self, key: AsymmetricAlgorithm) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RSAOAEPKeyExchangeFormatter(AsymmetricKeyExchangeFormatter):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, key: AsymmetricAlgorithm) -> None:
        """"""
    @property
    def Parameter(self) -> Array[int]:
        """"""
    @Parameter.setter
    def Parameter(self, value: Array[int]) -> None: ...
    @property
    def Parameters(self) -> str:
        """"""
    @property
    def Rng(self) -> RandomNumberGenerator:
        """"""
    @Rng.setter
    def Rng(self, value: RandomNumberGenerator) -> None: ...
    @overload
    def CreateKeyExchange(self, rgbData: Array[int]) -> Array[int]:
        """"""
    @overload
    def CreateKeyExchange(self, rgbData: Array[int], symAlgType: Type) -> Array[int]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetKey(self, key: AsymmetricAlgorithm) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RSAPKCS1KeyExchangeDeformatter(AsymmetricKeyExchangeDeformatter):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, key: AsymmetricAlgorithm) -> None:
        """"""
    @property
    def Parameters(self) -> str:
        """"""
    @Parameters.setter
    def Parameters(self, value: str) -> None: ...
    @property
    def RNG(self) -> RandomNumberGenerator:
        """"""
    @RNG.setter
    def RNG(self, value: RandomNumberGenerator) -> None: ...
    def DecryptKeyExchange(self, rgbIn: Array[int]) -> Array[int]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetKey(self, key: AsymmetricAlgorithm) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RSAPKCS1KeyExchangeFormatter(AsymmetricKeyExchangeFormatter):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, key: AsymmetricAlgorithm) -> None:
        """"""
    @property
    def Parameters(self) -> str:
        """"""
    @property
    def Rng(self) -> RandomNumberGenerator:
        """"""
    @Rng.setter
    def Rng(self, value: RandomNumberGenerator) -> None: ...
    @overload
    def CreateKeyExchange(self, rgbData: Array[int]) -> Array[int]:
        """"""
    @overload
    def CreateKeyExchange(self, rgbData: Array[int], symAlgType: Type) -> Array[int]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetKey(self, key: AsymmetricAlgorithm) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RSAPKCS1SHA1SignatureDescription(RSAPKCS1SignatureDescription):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def DeformatterAlgorithm(self) -> str:
        """"""
    @DeformatterAlgorithm.setter
    def DeformatterAlgorithm(self, value: str) -> None: ...
    @property
    def DigestAlgorithm(self) -> str:
        """"""
    @DigestAlgorithm.setter
    def DigestAlgorithm(self, value: str) -> None: ...
    @property
    def FormatterAlgorithm(self) -> str:
        """"""
    @FormatterAlgorithm.setter
    def FormatterAlgorithm(self, value: str) -> None: ...
    @property
    def KeyAlgorithm(self) -> str:
        """"""
    @KeyAlgorithm.setter
    def KeyAlgorithm(self, value: str) -> None: ...
    def CreateDeformatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureDeformatter:
        """"""
    def CreateDigest(self) -> HashAlgorithm:
        """"""
    def CreateFormatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureFormatter:
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
class RSAPKCS1SHA256SignatureDescription(RSAPKCS1SignatureDescription):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def DeformatterAlgorithm(self) -> str:
        """"""
    @DeformatterAlgorithm.setter
    def DeformatterAlgorithm(self, value: str) -> None: ...
    @property
    def DigestAlgorithm(self) -> str:
        """"""
    @DigestAlgorithm.setter
    def DigestAlgorithm(self, value: str) -> None: ...
    @property
    def FormatterAlgorithm(self) -> str:
        """"""
    @FormatterAlgorithm.setter
    def FormatterAlgorithm(self, value: str) -> None: ...
    @property
    def KeyAlgorithm(self) -> str:
        """"""
    @KeyAlgorithm.setter
    def KeyAlgorithm(self, value: str) -> None: ...
    def CreateDeformatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureDeformatter:
        """"""
    def CreateDigest(self) -> HashAlgorithm:
        """"""
    def CreateFormatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureFormatter:
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
class RSAPKCS1SHA384SignatureDescription(RSAPKCS1SignatureDescription):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def DeformatterAlgorithm(self) -> str:
        """"""
    @DeformatterAlgorithm.setter
    def DeformatterAlgorithm(self, value: str) -> None: ...
    @property
    def DigestAlgorithm(self) -> str:
        """"""
    @DigestAlgorithm.setter
    def DigestAlgorithm(self, value: str) -> None: ...
    @property
    def FormatterAlgorithm(self) -> str:
        """"""
    @FormatterAlgorithm.setter
    def FormatterAlgorithm(self, value: str) -> None: ...
    @property
    def KeyAlgorithm(self) -> str:
        """"""
    @KeyAlgorithm.setter
    def KeyAlgorithm(self, value: str) -> None: ...
    def CreateDeformatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureDeformatter:
        """"""
    def CreateDigest(self) -> HashAlgorithm:
        """"""
    def CreateFormatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureFormatter:
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
class RSAPKCS1SHA512SignatureDescription(RSAPKCS1SignatureDescription):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def DeformatterAlgorithm(self) -> str:
        """"""
    @DeformatterAlgorithm.setter
    def DeformatterAlgorithm(self, value: str) -> None: ...
    @property
    def DigestAlgorithm(self) -> str:
        """"""
    @DigestAlgorithm.setter
    def DigestAlgorithm(self, value: str) -> None: ...
    @property
    def FormatterAlgorithm(self) -> str:
        """"""
    @FormatterAlgorithm.setter
    def FormatterAlgorithm(self, value: str) -> None: ...
    @property
    def KeyAlgorithm(self) -> str:
        """"""
    @KeyAlgorithm.setter
    def KeyAlgorithm(self, value: str) -> None: ...
    def CreateDeformatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureDeformatter:
        """"""
    def CreateDigest(self) -> HashAlgorithm:
        """"""
    def CreateFormatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureFormatter:
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
class RSAPKCS1SignatureDeformatter(AsymmetricSignatureDeformatter):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, key: AsymmetricAlgorithm) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHashAlgorithm(self, strName: str) -> None:
        """"""
    def SetKey(self, key: AsymmetricAlgorithm) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def VerifySignature(self, hash: HashAlgorithm, rgbSignature: Array[int]) -> bool:
        """"""
    @overload
    def VerifySignature(self, rgbHash: Array[int], rgbSignature: Array[int]) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RSAPKCS1SignatureDescription(ABC, SignatureDescription):
    """"""
    @property
    def DeformatterAlgorithm(self) -> str:
        """"""
    @DeformatterAlgorithm.setter
    def DeformatterAlgorithm(self, value: str) -> None: ...
    @property
    def DigestAlgorithm(self) -> str:
        """"""
    @DigestAlgorithm.setter
    def DigestAlgorithm(self, value: str) -> None: ...
    @property
    def FormatterAlgorithm(self) -> str:
        """"""
    @FormatterAlgorithm.setter
    def FormatterAlgorithm(self, value: str) -> None: ...
    @property
    def KeyAlgorithm(self) -> str:
        """"""
    @KeyAlgorithm.setter
    def KeyAlgorithm(self, value: str) -> None: ...
    def CreateDeformatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureDeformatter:
        """"""
    def CreateDigest(self) -> HashAlgorithm:
        """"""
    def CreateFormatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureFormatter:
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
class RSAPKCS1SignatureFormatter(AsymmetricSignatureFormatter):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, key: AsymmetricAlgorithm) -> None:
        """"""
    @overload
    def CreateSignature(self, hash: HashAlgorithm) -> Array[int]:
        """"""
    @overload
    def CreateSignature(self, rgbHash: Array[int]) -> Array[int]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHashAlgorithm(self, strName: str) -> None:
        """"""
    def SetKey(self, key: AsymmetricAlgorithm) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RSAParameters(ValueType):
    """"""

    D: Final[Array[int]]
    """"""
    DP: Final[Array[int]]
    """"""
    DQ: Final[Array[int]]
    """"""
    Exponent: Final[Array[int]]
    """"""
    InverseQ: Final[Array[int]]
    """"""
    Modulus: Final[Array[int]]
    """"""
    P: Final[Array[int]]
    """"""
    Q: Final[Array[int]]
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
class RSASignaturePadding(Object, IEquatable[RSASignaturePadding]):
    """"""
    @property
    def Mode(self) -> RSASignaturePaddingMode:
        """"""
    @classmethod
    @property
    def Pkcs1(cls) -> RSASignaturePadding:
        """"""
    @classmethod
    @property
    def Pss(cls) -> RSASignaturePadding:
        """"""
    @overload
    def Equals(self, other: RSASignaturePadding) -> bool:
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
    def op_Equality(cls, left: RSASignaturePadding, right: RSASignaturePadding) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: RSASignaturePadding, right: RSASignaturePadding) -> bool:
        """"""
    def __eq__(self, other: RSASignaturePadding) -> bool:
        """"""
    def __ne__(self, other: RSASignaturePadding) -> bool:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class RSASignaturePaddingMode(Enum):
    """"""

    Pkcs1: RSASignaturePaddingMode = ...
    """"""
    Pss: RSASignaturePaddingMode = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RandomNumberGenerator(ABC, Object, IDisposable):
    """"""
    @classmethod
    @overload
    def Create(cls) -> RandomNumberGenerator:
        """"""
    @classmethod
    @overload
    def Create(cls, rngName: str) -> RandomNumberGenerator:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetBytes(self, data: Array[int]) -> None:
        """"""
    @overload
    def GetBytes(self, data: Array[int], offset: int, count: int) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetNonZeroBytes(self, data: Array[int]) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Rfc2898DeriveBytes(DeriveBytes, IDisposable):
    """"""
    @overload
    def __init__(self, password: str, saltSize: int) -> None:
        """"""
    @overload
    def __init__(self, password: str, saltSize: int, iterations: int) -> None:
        """"""
    @overload
    def __init__(
        self, password: str, saltSize: int, iterations: int, hashAlgorithm: HashAlgorithmName
    ) -> None:
        """"""
    @overload
    def __init__(self, password: str, salt: Array[int]) -> None:
        """"""
    @overload
    def __init__(self, password: str, salt: Array[int], iterations: int) -> None:
        """"""
    @overload
    def __init__(
        self, password: str, salt: Array[int], iterations: int, hashAlgorithm: HashAlgorithmName
    ) -> None:
        """"""
    @overload
    def __init__(self, password: Array[int], salt: Array[int], iterations: int) -> None:
        """"""
    @overload
    def __init__(
        self,
        password: Array[int],
        salt: Array[int],
        iterations: int,
        hashAlgorithm: HashAlgorithmName,
    ) -> None:
        """"""
    @property
    def IterationCount(self) -> int:
        """"""
    @IterationCount.setter
    def IterationCount(self, value: int) -> None: ...
    @property
    def Salt(self) -> Array[int]:
        """"""
    @Salt.setter
    def Salt(self, value: Array[int]) -> None: ...
    def CryptDeriveKey(
        self, algname: str, alghashname: str, keySize: int, rgbIV: Array[int]
    ) -> Array[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBytes(self, cb: int) -> Array[int]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Rfc4050KeyFormatter(ABC, Object):
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
class Rijndael(ABC, SymmetricAlgorithm, IDisposable):
    """"""
    @property
    def BlockSize(self) -> int:
        """"""
    @BlockSize.setter
    def BlockSize(self, value: int) -> None: ...
    @property
    def FeedbackSize(self) -> int:
        """"""
    @FeedbackSize.setter
    def FeedbackSize(self, value: int) -> None: ...
    @property
    def IV(self) -> Array[int]:
        """"""
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def Key(self) -> Array[int]:
        """"""
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def KeySize(self) -> int:
        """"""
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalBlockSizes(self) -> Array[KeySizes]:
        """"""
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """"""
    @property
    def Mode(self) -> CipherMode:
        """"""
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    @property
    def Padding(self) -> PaddingMode:
        """"""
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    def Clear(self) -> None:
        """"""
    @classmethod
    @overload
    def Create(cls) -> Rijndael:
        """"""
    @classmethod
    @overload
    def Create(cls, algName: str) -> Rijndael:
        """"""
    @overload
    def CreateDecryptor(self) -> ICryptoTransform:
        """"""
    @overload
    def CreateDecryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """"""
    @overload
    def CreateEncryptor(self) -> ICryptoTransform:
        """"""
    @overload
    def CreateEncryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GenerateIV(self) -> None:
        """"""
    def GenerateKey(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def ValidKeySize(self, bitLength: int) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RijndaelManaged(Rijndael, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def BlockSize(self) -> int:
        """"""
    @BlockSize.setter
    def BlockSize(self, value: int) -> None: ...
    @property
    def FeedbackSize(self) -> int:
        """"""
    @FeedbackSize.setter
    def FeedbackSize(self, value: int) -> None: ...
    @property
    def IV(self) -> Array[int]:
        """"""
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def Key(self) -> Array[int]:
        """"""
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def KeySize(self) -> int:
        """"""
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalBlockSizes(self) -> Array[KeySizes]:
        """"""
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """"""
    @property
    def Mode(self) -> CipherMode:
        """"""
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    @property
    def Padding(self) -> PaddingMode:
        """"""
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    def Clear(self) -> None:
        """"""
    @overload
    def CreateDecryptor(self) -> ICryptoTransform:
        """"""
    @overload
    def CreateDecryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """"""
    @overload
    def CreateEncryptor(self) -> ICryptoTransform:
        """"""
    @overload
    def CreateEncryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GenerateIV(self) -> None:
        """"""
    def GenerateKey(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def ValidKeySize(self, bitLength: int) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RijndaelManagedTransform(Object, ICryptoTransform, IDisposable):
    """"""
    @property
    def BlockSizeValue(self) -> int:
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class RijndaelManagedTransformMode(Enum):
    """"""

    Encrypt: RijndaelManagedTransformMode = ...
    """"""
    Decrypt: RijndaelManagedTransformMode = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SHA1(ABC, HashAlgorithm, ICryptoTransform, IDisposable):
    """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def Hash(self) -> Array[int]:
        """"""
    @property
    def HashSize(self) -> int:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    @classmethod
    @overload
    def Create(cls) -> SHA1:
        """"""
    @classmethod
    @overload
    def Create(cls, hashName: str) -> SHA1:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SHA1Cng(SHA1, ICryptoTransform, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def Hash(self) -> Array[int]:
        """"""
    @property
    def HashSize(self) -> int:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SHA1CryptoServiceProvider(SHA1, ICryptoTransform, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def Hash(self) -> Array[int]:
        """"""
    @property
    def HashSize(self) -> int:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SHA1Managed(SHA1, ICryptoTransform, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def Hash(self) -> Array[int]:
        """"""
    @property
    def HashSize(self) -> int:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SHA256(ABC, HashAlgorithm, ICryptoTransform, IDisposable):
    """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def Hash(self) -> Array[int]:
        """"""
    @property
    def HashSize(self) -> int:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    @classmethod
    @overload
    def Create(cls) -> SHA256:
        """"""
    @classmethod
    @overload
    def Create(cls, hashName: str) -> SHA256:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SHA256Cng(SHA256, ICryptoTransform, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def Hash(self) -> Array[int]:
        """"""
    @property
    def HashSize(self) -> int:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SHA256CngFactory(ABC, Object):
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
class SHA256CryptoServiceProvider(SHA256, ICryptoTransform, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def Hash(self) -> Array[int]:
        """"""
    @property
    def HashSize(self) -> int:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SHA256Managed(SHA256, ICryptoTransform, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def Hash(self) -> Array[int]:
        """"""
    @property
    def HashSize(self) -> int:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SHA384(ABC, HashAlgorithm, ICryptoTransform, IDisposable):
    """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def Hash(self) -> Array[int]:
        """"""
    @property
    def HashSize(self) -> int:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    @classmethod
    @overload
    def Create(cls) -> SHA384:
        """"""
    @classmethod
    @overload
    def Create(cls, hashName: str) -> SHA384:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SHA384Cng(SHA384, ICryptoTransform, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def Hash(self) -> Array[int]:
        """"""
    @property
    def HashSize(self) -> int:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SHA384CngFactory(ABC, Object):
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
class SHA384CryptoServiceProvider(SHA384, ICryptoTransform, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def Hash(self) -> Array[int]:
        """"""
    @property
    def HashSize(self) -> int:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SHA384Managed(SHA384, ICryptoTransform, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def Hash(self) -> Array[int]:
        """"""
    @property
    def HashSize(self) -> int:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SHA512(ABC, HashAlgorithm, ICryptoTransform, IDisposable):
    """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def Hash(self) -> Array[int]:
        """"""
    @property
    def HashSize(self) -> int:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    @classmethod
    @overload
    def Create(cls) -> SHA512:
        """"""
    @classmethod
    @overload
    def Create(cls, hashName: str) -> SHA512:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SHA512Cng(SHA512, ICryptoTransform, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def Hash(self) -> Array[int]:
        """"""
    @property
    def HashSize(self) -> int:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SHA512CngFactory(ABC, Object):
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
class SHA512CryptoServiceProvider(SHA512, ICryptoTransform, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def Hash(self) -> Array[int]:
        """"""
    @property
    def HashSize(self) -> int:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SHA512Managed(SHA512, ICryptoTransform, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def Hash(self) -> Array[int]:
        """"""
    @property
    def HashSize(self) -> int:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """"""
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SafeCertContextHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SafeCertStoreHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SafeCryptMsgHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SafeCryptProvHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SafeCspHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SafeCspHashHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SafeCspKeyHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SafeHashHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SafeKeyHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SafeLibraryHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SafeLocalAllocHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SafeProvHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SignatureDescription(Object):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, el: SecurityElement) -> None:
        """"""
    @property
    def DeformatterAlgorithm(self) -> str:
        """"""
    @DeformatterAlgorithm.setter
    def DeformatterAlgorithm(self, value: str) -> None: ...
    @property
    def DigestAlgorithm(self) -> str:
        """"""
    @DigestAlgorithm.setter
    def DigestAlgorithm(self, value: str) -> None: ...
    @property
    def FormatterAlgorithm(self) -> str:
        """"""
    @FormatterAlgorithm.setter
    def FormatterAlgorithm(self, value: str) -> None: ...
    @property
    def KeyAlgorithm(self) -> str:
        """"""
    @KeyAlgorithm.setter
    def KeyAlgorithm(self, value: str) -> None: ...
    def CreateDeformatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureDeformatter:
        """"""
    def CreateDigest(self) -> HashAlgorithm:
        """"""
    def CreateFormatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureFormatter:
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
class SignatureVerificationResult(Enum):
    """"""

    Valid: SignatureVerificationResult = ...
    """"""
    AssemblyIdentityMismatch: SignatureVerificationResult = ...
    """"""
    ContainingSignatureInvalid: SignatureVerificationResult = ...
    """"""
    PublicKeyTokenMismatch: SignatureVerificationResult = ...
    """"""
    PublisherMismatch: SignatureVerificationResult = ...
    """"""
    SystemError: SignatureVerificationResult = ...
    """"""
    InvalidSignerCertificate: SignatureVerificationResult = ...
    """"""
    InvalidCountersignature: SignatureVerificationResult = ...
    """"""
    InvalidCertificateSignature: SignatureVerificationResult = ...
    """"""
    InvalidTimestamp: SignatureVerificationResult = ...
    """"""
    BadDigest: SignatureVerificationResult = ...
    """"""
    BasicConstraintsNotObserved: SignatureVerificationResult = ...
    """"""
    UnknownTrustProvider: SignatureVerificationResult = ...
    """"""
    UnknownVerificationAction: SignatureVerificationResult = ...
    """"""
    BadSignatureFormat: SignatureVerificationResult = ...
    """"""
    CertificateNotExplicitlyTrusted: SignatureVerificationResult = ...
    """"""
    MissingSignature: SignatureVerificationResult = ...
    """"""
    CertificateExpired: SignatureVerificationResult = ...
    """"""
    InvalidTimePeriodNesting: SignatureVerificationResult = ...
    """"""
    InvalidCertificateRole: SignatureVerificationResult = ...
    """"""
    PathLengthConstraintViolated: SignatureVerificationResult = ...
    """"""
    UnknownCriticalExtension: SignatureVerificationResult = ...
    """"""
    CertificateUsageNotAllowed: SignatureVerificationResult = ...
    """"""
    IssuerChainingError: SignatureVerificationResult = ...
    """"""
    CertificateMalformed: SignatureVerificationResult = ...
    """"""
    UntrustedRootCertificate: SignatureVerificationResult = ...
    """"""
    CouldNotBuildChain: SignatureVerificationResult = ...
    """"""
    GenericTrustFailure: SignatureVerificationResult = ...
    """"""
    CertificateRevoked: SignatureVerificationResult = ...
    """"""
    UntrustedTestRootCertificate: SignatureVerificationResult = ...
    """"""
    RevocationCheckFailure: SignatureVerificationResult = ...
    """"""
    InvalidCertificateUsage: SignatureVerificationResult = ...
    """"""
    CertificateExplicitlyDistrusted: SignatureVerificationResult = ...
    """"""
    UntrustedCertificationAuthority: SignatureVerificationResult = ...
    """"""
    InvalidCertificatePolicy: SignatureVerificationResult = ...
    """"""
    InvalidCertificateName: SignatureVerificationResult = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StrongNameSignatureInformation(Object):
    """"""
    @property
    def HResult(self) -> int:
        """"""
    @property
    def HashAlgorithm(self) -> str:
        """"""
    @property
    def IsValid(self) -> bool:
        """"""
    @property
    def PublicKey(self) -> AsymmetricAlgorithm:
        """"""
    @property
    def VerificationResult(self) -> SignatureVerificationResult:
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
class SymmetricAlgorithm(ABC, Object, IDisposable):
    """"""
    @property
    def BlockSize(self) -> int:
        """"""
    @BlockSize.setter
    def BlockSize(self, value: int) -> None: ...
    @property
    def FeedbackSize(self) -> int:
        """"""
    @FeedbackSize.setter
    def FeedbackSize(self, value: int) -> None: ...
    @property
    def IV(self) -> Array[int]:
        """"""
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def Key(self) -> Array[int]:
        """"""
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def KeySize(self) -> int:
        """"""
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalBlockSizes(self) -> Array[KeySizes]:
        """"""
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """"""
    @property
    def Mode(self) -> CipherMode:
        """"""
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    @property
    def Padding(self) -> PaddingMode:
        """"""
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    def Clear(self) -> None:
        """"""
    @classmethod
    @overload
    def Create(cls) -> SymmetricAlgorithm:
        """"""
    @classmethod
    @overload
    def Create(cls, algName: str) -> SymmetricAlgorithm:
        """"""
    @overload
    def CreateDecryptor(self) -> ICryptoTransform:
        """"""
    @overload
    def CreateDecryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """"""
    @overload
    def CreateEncryptor(self) -> ICryptoTransform:
        """"""
    @overload
    def CreateEncryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GenerateIV(self) -> None:
        """"""
    def GenerateKey(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def ValidKeySize(self, bitLength: int) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TailStream(Stream, IDisposable):
    """"""
    def __init__(self, bufferSize: int) -> None:
        """"""
    @property
    def Buffer(self) -> Array[int]:
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
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """"""
    def Clear(self) -> None:
        """"""
    def Close(self) -> None:
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
    def Read(self, buffer: Array[int], offset: int, count: int) -> int:
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
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
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
class ToBase64Transform(Object, ICryptoTransform, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """"""
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """"""
    @property
    def InputBlockSize(self) -> int:
        """"""
    @property
    def OutputBlockSize(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """"""
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TripleDES(ABC, SymmetricAlgorithm, IDisposable):
    """"""
    @property
    def BlockSize(self) -> int:
        """"""
    @BlockSize.setter
    def BlockSize(self, value: int) -> None: ...
    @property
    def FeedbackSize(self) -> int:
        """"""
    @FeedbackSize.setter
    def FeedbackSize(self, value: int) -> None: ...
    @property
    def IV(self) -> Array[int]:
        """"""
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def Key(self) -> Array[int]:
        """"""
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def KeySize(self) -> int:
        """"""
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalBlockSizes(self) -> Array[KeySizes]:
        """"""
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """"""
    @property
    def Mode(self) -> CipherMode:
        """"""
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    @property
    def Padding(self) -> PaddingMode:
        """"""
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    def Clear(self) -> None:
        """"""
    @classmethod
    @overload
    def Create(cls) -> TripleDES:
        """"""
    @classmethod
    @overload
    def Create(cls, str: str) -> TripleDES:
        """"""
    @overload
    def CreateDecryptor(self) -> ICryptoTransform:
        """"""
    @overload
    def CreateDecryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """"""
    @overload
    def CreateEncryptor(self) -> ICryptoTransform:
        """"""
    @overload
    def CreateEncryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GenerateIV(self) -> None:
        """"""
    def GenerateKey(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsWeakKey(cls, rgbKey: Array[int]) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def ValidKeySize(self, bitLength: int) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TripleDESCng(TripleDES, ICngSymmetricAlgorithm, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, keyName: str) -> None:
        """"""
    @overload
    def __init__(self, keyName: str, provider: CngProvider) -> None:
        """"""
    @overload
    def __init__(self, keyName: str, provider: CngProvider, openOptions: CngKeyOpenOptions) -> None:
        """"""
    @property
    def BaseKey(self) -> Array[int]:
        """"""
    @BaseKey.setter
    def BaseKey(self, value: Array[int]) -> None: ...
    @property
    def BaseKeySize(self) -> int:
        """"""
    @BaseKeySize.setter
    def BaseKeySize(self, value: int) -> None: ...
    @property
    def BlockSize(self) -> int:
        """"""
    @BlockSize.setter
    def BlockSize(self, value: int) -> None: ...
    @property
    def FeedbackSize(self) -> int:
        """"""
    @FeedbackSize.setter
    def FeedbackSize(self, value: int) -> None: ...
    @property
    def IV(self) -> Array[int]:
        """"""
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def Key(self) -> Array[int]:
        """"""
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def KeySize(self) -> int:
        """"""
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalBlockSizes(self) -> Array[KeySizes]:
        """"""
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """"""
    @property
    def Mode(self) -> CipherMode:
        """"""
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    @property
    def Padding(self) -> PaddingMode:
        """"""
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    def Clear(self) -> None:
        """"""
    @overload
    def CreateDecryptor(self) -> ICryptoTransform:
        """"""
    @overload
    def CreateDecryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """"""
    @overload
    def CreateEncryptor(self) -> ICryptoTransform:
        """"""
    @overload
    def CreateEncryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GenerateIV(self) -> None:
        """"""
    def GenerateKey(self) -> None:
        """"""
    def GetEphemeralModeHandle(self) -> SafeBCryptAlgorithmHandle:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetNCryptAlgorithmIdentifier(self) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def IsWeakKey(self, key: Array[int]) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def ValidKeySize(self, bitLength: int) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TripleDESCryptoServiceProvider(TripleDES, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def BlockSize(self) -> int:
        """"""
    @BlockSize.setter
    def BlockSize(self, value: int) -> None: ...
    @property
    def FeedbackSize(self) -> int:
        """"""
    @FeedbackSize.setter
    def FeedbackSize(self, value: int) -> None: ...
    @property
    def IV(self) -> Array[int]:
        """"""
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def Key(self) -> Array[int]:
        """"""
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def KeySize(self) -> int:
        """"""
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalBlockSizes(self) -> Array[KeySizes]:
        """"""
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """"""
    @property
    def Mode(self) -> CipherMode:
        """"""
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    @property
    def Padding(self) -> PaddingMode:
        """"""
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    def Clear(self) -> None:
        """"""
    @overload
    def CreateDecryptor(self) -> ICryptoTransform:
        """"""
    @overload
    def CreateDecryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """"""
    @overload
    def CreateEncryptor(self) -> ICryptoTransform:
        """"""
    @overload
    def CreateEncryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GenerateIV(self) -> None:
        """"""
    def GenerateKey(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def ValidKeySize(self, bitLength: int) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Utils(ABC, Object):
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
class X509Utils(Object):
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
