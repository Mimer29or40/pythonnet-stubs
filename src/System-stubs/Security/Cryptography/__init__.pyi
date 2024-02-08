from __future__ import annotations

from abc import ABC
from typing import Final
from typing import Iterator
from typing import Optional
from typing import Tuple
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
from System.Collections import ICollection
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections import IList
from System.Collections.Generic import ICollection
from System.Collections.Generic import IEnumerable
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
from System.Security.Cryptography.BCryptNative import KeyBlobMagicNumber
from System.Security.Cryptography.CapiNative import AlgorithmId
from System.Security.Cryptography.CapiNative import ProviderType
from System.Security.Cryptography.ECCurve import ECCurveType
from System.Security.Cryptography.X509Certificates import AuthenticodeSignatureInformation
from System.Security.Cryptography.X509Certificates import X509RevocationFlag
from System.Security.Cryptography.X509Certificates import X509RevocationMode
from System.Threading import CancellationToken
from System.Threading.Tasks import Task

class Aes(ABC, SymmetricAlgorithm, IDisposable):
    """"""

    @property
    def BlockSize(self) -> int:
        """

        :return:
        """
    @BlockSize.setter
    def BlockSize(self, value: int) -> None: ...
    @property
    def FeedbackSize(self) -> int:
        """

        :return:
        """
    @FeedbackSize.setter
    def FeedbackSize(self, value: int) -> None: ...
    @property
    def IV(self) -> Array[int]:
        """

        :return:
        """
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def Key(self) -> Array[int]:
        """

        :return:
        """
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def KeySize(self) -> int:
        """

        :return:
        """
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalBlockSizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def Mode(self) -> CipherMode:
        """

        :return:
        """
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    @property
    def Padding(self) -> PaddingMode:
        """

        :return:
        """
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    def Clear(self) -> None:
        """"""
    @classmethod
    @overload
    def Create(cls) -> Aes:
        """

        :return:
        """
    @classmethod
    @overload
    def Create(cls, algorithmName: str) -> Aes:
        """

        :param algorithmName:
        :return:
        """
    @overload
    def CreateDecryptor(self) -> ICryptoTransform:
        """

        :return:
        """
    @overload
    def CreateDecryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """

        :param rgbKey:
        :param rgbIV:
        :return:
        """
    @overload
    def CreateEncryptor(self) -> ICryptoTransform:
        """

        :return:
        """
    @overload
    def CreateEncryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """

        :param rgbKey:
        :param rgbIV:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GenerateIV(self) -> None:
        """"""
    def GenerateKey(self) -> None:
        """"""
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
    def ValidKeySize(self, bitLength: int) -> bool:
        """

        :param bitLength:
        :return:
        """

class AesCng(Aes, ICngSymmetricAlgorithm, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, keyName: str):
        """

        :param keyName:
        """
    @overload
    def __init__(self, keyName: str, provider: CngProvider):
        """

        :param keyName:
        :param provider:
        """
    @overload
    def __init__(self, keyName: str, provider: CngProvider, openOptions: CngKeyOpenOptions):
        """

        :param keyName:
        :param provider:
        :param openOptions:
        """
    @property
    def BaseKey(self) -> Array[int]:
        """

        :return:
        """
    @BaseKey.setter
    def BaseKey(self, value: Array[int]) -> None: ...
    @property
    def BaseKeySize(self) -> int:
        """

        :return:
        """
    @BaseKeySize.setter
    def BaseKeySize(self, value: int) -> None: ...
    @property
    def BlockSize(self) -> int:
        """

        :return:
        """
    @property
    def BlockSize(self) -> int:
        """

        :return:
        """
    @BlockSize.setter
    def BlockSize(self, value: int) -> None: ...
    @property
    def FeedbackSize(self) -> int:
        """

        :return:
        """
    @FeedbackSize.setter
    def FeedbackSize(self, value: int) -> None: ...
    @property
    def IV(self) -> Array[int]:
        """

        :return:
        """
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def IV(self) -> Array[int]:
        """

        :return:
        """
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def Key(self) -> Array[int]:
        """

        :return:
        """
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def KeySize(self) -> int:
        """

        :return:
        """
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalBlockSizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def Mode(self) -> CipherMode:
        """

        :return:
        """
    @property
    def Mode(self) -> CipherMode:
        """

        :return:
        """
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    @property
    def Padding(self) -> PaddingMode:
        """

        :return:
        """
    @property
    def Padding(self) -> PaddingMode:
        """

        :return:
        """
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    def Clear(self) -> None:
        """"""
    @overload
    def CreateDecryptor(self) -> ICryptoTransform:
        """

        :return:
        """
    @overload
    def CreateDecryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """

        :param rgbKey:
        :param rgbIV:
        :return:
        """
    @overload
    def CreateEncryptor(self) -> ICryptoTransform:
        """

        :return:
        """
    @overload
    def CreateEncryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """

        :param rgbKey:
        :param rgbIV:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GenerateIV(self) -> None:
        """"""
    def GenerateKey(self) -> None:
        """"""
    def GetEphemeralModeHandle(self) -> SafeBCryptAlgorithmHandle:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetNCryptAlgorithmIdentifier(self) -> str:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def IsWeakKey(self, key: Array[int]) -> bool:
        """

        :param key:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def ValidKeySize(self, bitLength: int) -> bool:
        """

        :param bitLength:
        :return:
        """

class AesCryptoServiceProvider(Aes, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def BlockSize(self) -> int:
        """

        :return:
        """
    @BlockSize.setter
    def BlockSize(self, value: int) -> None: ...
    @property
    def FeedbackSize(self) -> int:
        """

        :return:
        """
    @FeedbackSize.setter
    def FeedbackSize(self, value: int) -> None: ...
    @property
    def IV(self) -> Array[int]:
        """

        :return:
        """
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def Key(self) -> Array[int]:
        """

        :return:
        """
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def KeySize(self) -> int:
        """

        :return:
        """
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalBlockSizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def Mode(self) -> CipherMode:
        """

        :return:
        """
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    @property
    def Padding(self) -> PaddingMode:
        """

        :return:
        """
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    def Clear(self) -> None:
        """"""
    @overload
    def CreateDecryptor(self) -> ICryptoTransform:
        """

        :return:
        """
    @overload
    def CreateDecryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """

        :param rgbKey:
        :param rgbIV:
        :return:
        """
    @overload
    def CreateEncryptor(self) -> ICryptoTransform:
        """

        :return:
        """
    @overload
    def CreateEncryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """

        :param rgbKey:
        :param rgbIV:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GenerateIV(self) -> None:
        """"""
    def GenerateKey(self) -> None:
        """"""
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
    def ValidKeySize(self, bitLength: int) -> bool:
        """

        :param bitLength:
        :return:
        """

class AesManaged(Aes, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def BlockSize(self) -> int:
        """

        :return:
        """
    @BlockSize.setter
    def BlockSize(self, value: int) -> None: ...
    @property
    def FeedbackSize(self) -> int:
        """

        :return:
        """
    @FeedbackSize.setter
    def FeedbackSize(self, value: int) -> None: ...
    @property
    def IV(self) -> Array[int]:
        """

        :return:
        """
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def Key(self) -> Array[int]:
        """

        :return:
        """
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def KeySize(self) -> int:
        """

        :return:
        """
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalBlockSizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def Mode(self) -> CipherMode:
        """

        :return:
        """
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    @property
    def Padding(self) -> PaddingMode:
        """

        :return:
        """
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    def Clear(self) -> None:
        """"""
    @overload
    def CreateDecryptor(self) -> ICryptoTransform:
        """

        :return:
        """
    @overload
    def CreateDecryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """

        :param rgbKey:
        :param rgbIV:
        :return:
        """
    @overload
    def CreateEncryptor(self) -> ICryptoTransform:
        """

        :return:
        """
    @overload
    def CreateEncryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """

        :param rgbKey:
        :param rgbIV:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GenerateIV(self) -> None:
        """"""
    def GenerateKey(self) -> None:
        """"""
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
    def ValidKeySize(self, bitLength: int) -> bool:
        """

        :param bitLength:
        :return:
        """

class AsnEncodedData(Object):
    """"""

    @overload
    def __init__(self, asnEncodedData: AsnEncodedData):
        """

        :param asnEncodedData:
        """
    @overload
    def __init__(self, rawData: Array[int]):
        """

        :param rawData:
        """
    @overload
    def __init__(self, oid: Oid, rawData: Array[int]):
        """

        :param oid:
        :param rawData:
        """
    @overload
    def __init__(self, oid: str, rawData: Array[int]):
        """

        :param oid:
        :param rawData:
        """
    @property
    def Oid(self) -> Oid:
        """

        :return:
        """
    @Oid.setter
    def Oid(self, value: Oid) -> None: ...
    @property
    def RawData(self) -> Array[int]:
        """

        :return:
        """
    @RawData.setter
    def RawData(self, value: Array[int]) -> None: ...
    def CopyFrom(self, asnEncodedData: AsnEncodedData) -> None:
        """

        :param asnEncodedData:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Format(self, multiLine: bool) -> str:
        """

        :param multiLine:
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

class AsnEncodedDataCollection(Object, ICollection, IEnumerable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, asnEncodedData: AsnEncodedData):
        """

        :param asnEncodedData:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> AsnEncodedData:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    def Add(self, asnEncodedData: AsnEncodedData) -> int:
        """

        :param asnEncodedData:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[AsnEncodedData], index: int) -> None:
        """

        :param array:
        :param index:
        """
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
    def Remove(self, asnEncodedData: AsnEncodedData) -> None:
        """

        :param asnEncodedData:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> AsnEncodedData:
        """

        :param index:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

class AsnEncodedDataEnumerator(Object, IEnumerator):
    """"""

    @property
    def Current(self) -> object:
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
    def MoveNext(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class AsymmetricAlgorithm(ABC, Object, IDisposable):
    """"""

    @property
    def KeyExchangeAlgorithm(self) -> str:
        """

        :return:
        """
    @property
    def KeySize(self) -> int:
        """

        :return:
        """
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def SignatureAlgorithm(self) -> str:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @classmethod
    @overload
    def Create(cls) -> AsymmetricAlgorithm:
        """

        :return:
        """
    @classmethod
    @overload
    def Create(cls, algName: str) -> AsymmetricAlgorithm:
        """

        :param algName:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FromXmlString(self, xmlString: str) -> None:
        """

        :param xmlString:
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
    def ToXmlString(self, includePrivateParameters: bool) -> str:
        """

        :param includePrivateParameters:
        :return:
        """

class AsymmetricKeyExchangeDeformatter(ABC, Object):
    """"""

    @property
    def Parameters(self) -> str:
        """

        :return:
        """
    @Parameters.setter
    def Parameters(self, value: str) -> None: ...
    def DecryptKeyExchange(self, rgb: Array[int]) -> Array[int]:
        """

        :param rgb:
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
    def SetKey(self, key: AsymmetricAlgorithm) -> None:
        """

        :param key:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class AsymmetricKeyExchangeFormatter(ABC, Object):
    """"""

    @property
    def Parameters(self) -> str:
        """

        :return:
        """
    @overload
    def CreateKeyExchange(self, data: Array[int]) -> Array[int]:
        """

        :param data:
        :return:
        """
    @overload
    def CreateKeyExchange(self, data: Array[int], symAlgType: Type) -> Array[int]:
        """

        :param data:
        :param symAlgType:
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
    def SetKey(self, key: AsymmetricAlgorithm) -> None:
        """

        :param key:
        """
    def ToString(self) -> str:
        """

        :return:
        """

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

class AsymmetricSignatureDeformatter(ABC, Object):
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
    def SetHashAlgorithm(self, strName: str) -> None:
        """

        :param strName:
        """
    def SetKey(self, key: AsymmetricAlgorithm) -> None:
        """

        :param key:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def VerifySignature(self, hash: HashAlgorithm, rgbSignature: Array[int]) -> bool:
        """

        :param hash:
        :param rgbSignature:
        :return:
        """
    @overload
    def VerifySignature(self, rgbHash: Array[int], rgbSignature: Array[int]) -> bool:
        """

        :param rgbHash:
        :param rgbSignature:
        :return:
        """

class AsymmetricSignatureFormatter(ABC, Object):
    """"""

    @overload
    def CreateSignature(self, hash: HashAlgorithm) -> Array[int]:
        """

        :param hash:
        :return:
        """
    @overload
    def CreateSignature(self, rgbHash: Array[int]) -> Array[int]:
        """

        :param rgbHash:
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
    def SetHashAlgorithm(self, strName: str) -> None:
        """

        :param strName:
        """
    def SetKey(self, key: AsymmetricAlgorithm) -> None:
        """

        :param key:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class BCRYPT_DSA_KEY_BLOB_V2(ValueType):
    """"""

    Count0: Final[int] = ...
    """
    
    :return: 
    """
    Count1: Final[int] = ...
    """
    
    :return: 
    """
    Count2: Final[int] = ...
    """
    
    :return: 
    """
    Count3: Final[int] = ...
    """
    
    :return: 
    """
    cbGroupSize: Final[int] = ...
    """
    
    :return: 
    """
    cbKey: Final[int] = ...
    """
    
    :return: 
    """
    cbSeedLength: Final[int] = ...
    """
    
    :return: 
    """
    dwMagic: Final[BCryptNative.KeyBlobMagicNumber] = ...
    """
    
    :return: 
    """
    hashAlgorithm: Final[HASHALGORITHM_ENUM] = ...
    """
    
    :return: 
    """
    standardVersion: Final[DSAFIPSVERSION_ENUM] = ...
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

class BCryptAlgorithmHandleCache(Object):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetCachedAlgorithmHandle(
        self, algorithm: str, implementation: str
    ) -> SafeBCryptAlgorithmHandle:
        """

        :param algorithm:
        :param implementation:
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

class BCryptHashAlgorithm(Object, IDisposable):
    """"""

    def __init__(self, algorithm: CngAlgorithm, implementation: str):
        """

        :param algorithm:
        :param implementation:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def HashCore(self, array: Array[int], ibStart: int, cbSize: int) -> None:
        """

        :param array:
        :param ibStart:
        :param cbSize:
        """
    def HashFinal(self) -> Array[int]:
        """

        :return:
        """
    def HashStream(self, stream: Stream) -> None:
        """

        :param stream:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

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
        """

        :param hKey:
        :param input:
        :param inputOffset:
        :param inputCount:
        :param iv:
        :param output:
        :param outputOffset:
        :param outputCount:
        :return:
        """
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
        """

        :param hKey:
        :param input:
        :param inputOffset:
        :param inputCount:
        :param iv:
        :param output:
        :param outputOffset:
        :param outputCount:
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
    @classmethod
    def SetCipherMode(cls, hAlg: SafeBCryptAlgorithmHandle, cipherMode: str) -> None:
        """

        :param hAlg:
        :param cipherMode:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class BigInt(Object):
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
    def __eq__(self, other: BigInt) -> bool:
        """

        :param other:
        :return:
        """
    def __gt__(self, other: BigInt) -> bool:
        """

        :param other:
        :return:
        """
    def __lt__(self, other: BigInt) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: BigInt) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, value1: BigInt, value2: BigInt) -> bool:
        """

        :param value1:
        :param value2:
        :return:
        """
    @classmethod
    def op_GreaterThan(cls, value1: BigInt, value2: BigInt) -> bool:
        """

        :param value1:
        :param value2:
        :return:
        """
    @classmethod
    def op_Inequality(cls, value1: BigInt, value2: BigInt) -> bool:
        """

        :param value1:
        :param value2:
        :return:
        """
    @classmethod
    def op_LessThan(cls, value1: BigInt, value2: BigInt) -> bool:
        """

        :param value1:
        :param value2:
        :return:
        """

class CAPI(CAPIMethods):
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

class CAPIBase(ABC, Object):
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

class CAPIMethods(ABC, CAPIUnsafe):
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

class CAPINative(ABC, CAPIBase):
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

class CAPISafe(ABC, CAPINative):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def FreeLibrary(cls, hModule: IntPtr) -> bool:
        """

        :param hModule:
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

class CAPIUnsafe(ABC, CAPISafe):
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

class CapiHashAlgorithm(Object, IDisposable):
    """"""

    def __init__(
        self,
        provider: str,
        providerType: CapiNative.ProviderType,
        algorithm: CapiNative.AlgorithmId,
    ):
        """

        :param provider:
        :param providerType:
        :param algorithm:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def HashCore(self, array: Array[int], ibStart: int, cbSize: int) -> None:
        """

        :param array:
        :param ibStart:
        :param cbSize:
        """
    def HashFinal(self) -> Array[int]:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class CapiNative(ABC, Object):
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
    ):
        """

        :param blockSize:
        :param feedbackSize:
        :param provider:
        :param key:
        :param iv:
        :param cipherMode:
        :param paddingMode:
        :param encryptionMode:
        """
    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def OutputBlockSize(self) -> int:
        """

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
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

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

class CngAlgorithm(Object, IEquatable[CngAlgorithm]):
    """"""

    def __init__(self, algorithm: str):
        """

        :param algorithm:
        """
    @property
    def Algorithm(self) -> str:
        """

        :return:
        """
    @classmethod
    @property
    def ECDiffieHellman(cls) -> CngAlgorithm:
        """

        :return:
        """
    @classmethod
    @property
    def ECDiffieHellmanP256(cls) -> CngAlgorithm:
        """

        :return:
        """
    @classmethod
    @property
    def ECDiffieHellmanP384(cls) -> CngAlgorithm:
        """

        :return:
        """
    @classmethod
    @property
    def ECDiffieHellmanP521(cls) -> CngAlgorithm:
        """

        :return:
        """
    @classmethod
    @property
    def ECDsa(cls) -> CngAlgorithm:
        """

        :return:
        """
    @classmethod
    @property
    def ECDsaP256(cls) -> CngAlgorithm:
        """

        :return:
        """
    @classmethod
    @property
    def ECDsaP384(cls) -> CngAlgorithm:
        """

        :return:
        """
    @classmethod
    @property
    def ECDsaP521(cls) -> CngAlgorithm:
        """

        :return:
        """
    @classmethod
    @property
    def MD5(cls) -> CngAlgorithm:
        """

        :return:
        """
    @classmethod
    @property
    def Rsa(cls) -> CngAlgorithm:
        """

        :return:
        """
    @classmethod
    @property
    def Sha1(cls) -> CngAlgorithm:
        """

        :return:
        """
    @classmethod
    @property
    def Sha256(cls) -> CngAlgorithm:
        """

        :return:
        """
    @classmethod
    @property
    def Sha384(cls) -> CngAlgorithm:
        """

        :return:
        """
    @classmethod
    @property
    def Sha512(cls) -> CngAlgorithm:
        """

        :return:
        """
    @overload
    def Equals(self, other: CngAlgorithm) -> bool:
        """

        :param other:
        :return:
        """
    @overload
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
    def __eq__(self, other: CngAlgorithm) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: CngAlgorithm) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: CngAlgorithm, right: CngAlgorithm) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: CngAlgorithm, right: CngAlgorithm) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

class CngAlgorithmGroup(Object, IEquatable[CngAlgorithmGroup]):
    """"""

    def __init__(self, algorithmGroup: str):
        """

        :param algorithmGroup:
        """
    @property
    def AlgorithmGroup(self) -> str:
        """

        :return:
        """
    @classmethod
    @property
    def DiffieHellman(cls) -> CngAlgorithmGroup:
        """

        :return:
        """
    @classmethod
    @property
    def Dsa(cls) -> CngAlgorithmGroup:
        """

        :return:
        """
    @classmethod
    @property
    def ECDiffieHellman(cls) -> CngAlgorithmGroup:
        """

        :return:
        """
    @classmethod
    @property
    def ECDsa(cls) -> CngAlgorithmGroup:
        """

        :return:
        """
    @classmethod
    @property
    def Rsa(cls) -> CngAlgorithmGroup:
        """

        :return:
        """
    @overload
    def Equals(self, other: CngAlgorithmGroup) -> bool:
        """

        :param other:
        :return:
        """
    @overload
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
    def __eq__(self, other: CngAlgorithmGroup) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: CngAlgorithmGroup) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: CngAlgorithmGroup, right: CngAlgorithmGroup) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: CngAlgorithmGroup, right: CngAlgorithmGroup) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

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

class CngKey(Object, IDisposable):
    """"""

    @property
    def Algorithm(self) -> CngAlgorithm:
        """

        :return:
        """
    @property
    def AlgorithmGroup(self) -> CngAlgorithmGroup:
        """

        :return:
        """
    @property
    def ExportPolicy(self) -> CngExportPolicies:
        """

        :return:
        """
    @property
    def Handle(self) -> SafeNCryptKeyHandle:
        """

        :return:
        """
    @property
    def IsEphemeral(self) -> bool:
        """

        :return:
        """
    @property
    def IsMachineKey(self) -> bool:
        """

        :return:
        """
    @property
    def KeyName(self) -> str:
        """

        :return:
        """
    @property
    def KeySize(self) -> int:
        """

        :return:
        """
    @property
    def KeyUsage(self) -> CngKeyUsages:
        """

        :return:
        """
    @property
    def ParentWindowHandle(self) -> IntPtr:
        """

        :return:
        """
    @ParentWindowHandle.setter
    def ParentWindowHandle(self, value: IntPtr) -> None: ...
    @property
    def Provider(self) -> CngProvider:
        """

        :return:
        """
    @property
    def ProviderHandle(self) -> SafeNCryptProviderHandle:
        """

        :return:
        """
    @property
    def UIPolicy(self) -> CngUIPolicy:
        """

        :return:
        """
    @property
    def UniqueName(self) -> str:
        """

        :return:
        """
    @classmethod
    @overload
    def Create(cls, algorithm: CngAlgorithm) -> CngKey:
        """

        :param algorithm:
        :return:
        """
    @classmethod
    @overload
    def Create(cls, algorithm: CngAlgorithm, keyName: str) -> CngKey:
        """

        :param algorithm:
        :param keyName:
        :return:
        """
    @classmethod
    @overload
    def Create(
        cls, algorithm: CngAlgorithm, keyName: str, creationParameters: CngKeyCreationParameters
    ) -> CngKey:
        """

        :param algorithm:
        :param keyName:
        :param creationParameters:
        :return:
        """
    def Delete(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    @overload
    def Exists(cls, keyName: str) -> bool:
        """

        :param keyName:
        :return:
        """
    @classmethod
    @overload
    def Exists(cls, keyName: str, provider: CngProvider) -> bool:
        """

        :param keyName:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def Exists(cls, keyName: str, provider: CngProvider, options: CngKeyOpenOptions) -> bool:
        """

        :param keyName:
        :param provider:
        :param options:
        :return:
        """
    def Export(self, format: CngKeyBlobFormat) -> Array[int]:
        """

        :param format:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetProperty(self, name: str, options: CngPropertyOptions) -> CngProperty:
        """

        :param name:
        :param options:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def HasProperty(self, name: str, options: CngPropertyOptions) -> bool:
        """

        :param name:
        :param options:
        :return:
        """
    @classmethod
    @overload
    def Import(cls, keyBlob: Array[int], format: CngKeyBlobFormat) -> CngKey:
        """

        :param keyBlob:
        :param format:
        :return:
        """
    @classmethod
    @overload
    def Import(cls, keyBlob: Array[int], format: CngKeyBlobFormat, provider: CngProvider) -> CngKey:
        """

        :param keyBlob:
        :param format:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def Open(cls, keyName: str) -> CngKey:
        """

        :param keyName:
        :return:
        """
    @classmethod
    @overload
    def Open(
        cls, keyHandle: SafeNCryptKeyHandle, keyHandleOpenOptions: CngKeyHandleOpenOptions
    ) -> CngKey:
        """

        :param keyHandle:
        :param keyHandleOpenOptions:
        :return:
        """
    @classmethod
    @overload
    def Open(cls, keyName: str, provider: CngProvider) -> CngKey:
        """

        :param keyName:
        :param provider:
        :return:
        """
    @classmethod
    @overload
    def Open(cls, keyName: str, provider: CngProvider, openOptions: CngKeyOpenOptions) -> CngKey:
        """

        :param keyName:
        :param provider:
        :param openOptions:
        :return:
        """
    def SetProperty(self, property: CngProperty) -> None:
        """

        :param property:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CngKeyBlobFormat(Object, IEquatable[CngKeyBlobFormat]):
    """"""

    def __init__(self, format: str):
        """

        :param format:
        """
    @classmethod
    @property
    def EccFullPrivateBlob(cls) -> CngKeyBlobFormat:
        """

        :return:
        """
    @classmethod
    @property
    def EccFullPublicBlob(cls) -> CngKeyBlobFormat:
        """

        :return:
        """
    @classmethod
    @property
    def EccPrivateBlob(cls) -> CngKeyBlobFormat:
        """

        :return:
        """
    @classmethod
    @property
    def EccPublicBlob(cls) -> CngKeyBlobFormat:
        """

        :return:
        """
    @property
    def Format(self) -> str:
        """

        :return:
        """
    @classmethod
    @property
    def GenericPrivateBlob(cls) -> CngKeyBlobFormat:
        """

        :return:
        """
    @classmethod
    @property
    def GenericPublicBlob(cls) -> CngKeyBlobFormat:
        """

        :return:
        """
    @classmethod
    @property
    def OpaqueTransportBlob(cls) -> CngKeyBlobFormat:
        """

        :return:
        """
    @classmethod
    @property
    def Pkcs8PrivateBlob(cls) -> CngKeyBlobFormat:
        """

        :return:
        """
    @overload
    def Equals(self, other: CngKeyBlobFormat) -> bool:
        """

        :param other:
        :return:
        """
    @overload
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
    def __eq__(self, other: CngKeyBlobFormat) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: CngKeyBlobFormat) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: CngKeyBlobFormat, right: CngKeyBlobFormat) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: CngKeyBlobFormat, right: CngKeyBlobFormat) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

class CngKeyCreationOptions(Enum):
    """"""

    _None: CngKeyCreationOptions = ...
    """"""
    MachineKey: CngKeyCreationOptions = ...
    """"""
    OverwriteExistingKey: CngKeyCreationOptions = ...
    """"""

class CngKeyCreationParameters(Object):
    """"""

    def __init__(self):
        """"""
    @property
    def ExportPolicy(self) -> Optional[CngExportPolicies]:
        """

        :return:
        """
    @ExportPolicy.setter
    def ExportPolicy(self, value: Optional[CngExportPolicies]) -> None: ...
    @property
    def KeyCreationOptions(self) -> CngKeyCreationOptions:
        """

        :return:
        """
    @KeyCreationOptions.setter
    def KeyCreationOptions(self, value: CngKeyCreationOptions) -> None: ...
    @property
    def KeyUsage(self) -> Optional[CngKeyUsages]:
        """

        :return:
        """
    @KeyUsage.setter
    def KeyUsage(self, value: Optional[CngKeyUsages]) -> None: ...
    @property
    def Parameters(self) -> CngPropertyCollection:
        """

        :return:
        """
    @property
    def ParentWindowHandle(self) -> IntPtr:
        """

        :return:
        """
    @ParentWindowHandle.setter
    def ParentWindowHandle(self, value: IntPtr) -> None: ...
    @property
    def Provider(self) -> CngProvider:
        """

        :return:
        """
    @Provider.setter
    def Provider(self, value: CngProvider) -> None: ...
    @property
    def UIPolicy(self) -> CngUIPolicy:
        """

        :return:
        """
    @UIPolicy.setter
    def UIPolicy(self, value: CngUIPolicy) -> None: ...
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

class CngKeyHandleOpenOptions(Enum):
    """"""

    _None: CngKeyHandleOpenOptions = ...
    """"""
    EphemeralKey: CngKeyHandleOpenOptions = ...
    """"""

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

class CngKeyTypes(Enum):
    """"""

    _None: CngKeyTypes = ...
    """"""
    MachineKey: CngKeyTypes = ...
    """"""

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

class CngProperty(ValueType, IEquatable[CngProperty]):
    """"""

    def __init__(self, name: str, value: Array[int], options: CngPropertyOptions):
        """

        :param name:
        :param value:
        :param options:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Options(self) -> CngPropertyOptions:
        """

        :return:
        """
    @overload
    def Equals(self, other: CngProperty) -> bool:
        """

        :param other:
        :return:
        """
    @overload
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
    def GetValue(self) -> Array[int]:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __eq__(self, other: CngProperty) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: CngProperty) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: CngProperty, right: CngProperty) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: CngProperty, right: CngProperty) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

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

    def __init__(self):
        """"""
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Item(self) -> CngProperty:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: CngProperty) -> None: ...
    @property
    def Item(self) -> CngProperty:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, item: CngProperty) -> None:
        """

        :param item:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, item: CngProperty) -> bool:
        """

        :param item:
        :return:
        """
    @overload
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[CngProperty], arrayIndex: int) -> None:
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
    @overload
    def IndexOf(self, item: CngProperty) -> int:
        """

        :param item:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, item: CngProperty) -> None:
        """

        :param index:
        :param item:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, item: CngProperty) -> bool:
        """

        :param item:
        :return:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    @overload
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    @overload
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def __contains__(self, value: CngProperty) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> CngProperty:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> CngProperty:
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
    def __iter__(self) -> Iterator[CngProperty]:
        """

        :return:
        """
    @overload
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __setitem__(self, index: int, value: CngProperty) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """

class CngPropertyOptions(Enum):
    """"""

    _None: CngPropertyOptions = ...
    """"""
    CustomProperty: CngPropertyOptions = ...
    """"""
    Persist: CngPropertyOptions = ...
    """"""

class CngProvider(Object, IEquatable[CngProvider]):
    """"""

    def __init__(self, provider: str):
        """

        :param provider:
        """
    @classmethod
    @property
    def MicrosoftSmartCardKeyStorageProvider(cls) -> CngProvider:
        """

        :return:
        """
    @classmethod
    @property
    def MicrosoftSoftwareKeyStorageProvider(cls) -> CngProvider:
        """

        :return:
        """
    @property
    def Provider(self) -> str:
        """

        :return:
        """
    @overload
    def Equals(self, other: CngProvider) -> bool:
        """

        :param other:
        :return:
        """
    @overload
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
    def __eq__(self, other: CngProvider) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: CngProvider) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: CngProvider, right: CngProvider) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: CngProvider, right: CngProvider) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

class CngUIPolicy(Object):
    """"""

    @overload
    def __init__(self, protectionLevel: CngUIProtectionLevels):
        """

        :param protectionLevel:
        """
    @overload
    def __init__(self, protectionLevel: CngUIProtectionLevels, friendlyName: str):
        """

        :param protectionLevel:
        :param friendlyName:
        """
    @overload
    def __init__(self, protectionLevel: CngUIProtectionLevels, friendlyName: str, description: str):
        """

        :param protectionLevel:
        :param friendlyName:
        :param description:
        """
    @overload
    def __init__(
        self,
        protectionLevel: CngUIProtectionLevels,
        friendlyName: str,
        description: str,
        useContext: str,
    ):
        """

        :param protectionLevel:
        :param friendlyName:
        :param description:
        :param useContext:
        """
    @overload
    def __init__(
        self,
        protectionLevel: CngUIProtectionLevels,
        friendlyName: str,
        description: str,
        useContext: str,
        creationTitle: str,
    ):
        """

        :param protectionLevel:
        :param friendlyName:
        :param description:
        :param useContext:
        :param creationTitle:
        """
    @property
    def CreationTitle(self) -> str:
        """

        :return:
        """
    @property
    def Description(self) -> str:
        """

        :return:
        """
    @property
    def FriendlyName(self) -> str:
        """

        :return:
        """
    @property
    def ProtectionLevel(self) -> CngUIProtectionLevels:
        """

        :return:
        """
    @property
    def UseContext(self) -> str:
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

class CngUIProtectionLevels(Enum):
    """"""

    _None: CngUIProtectionLevels = ...
    """"""
    ProtectKey: CngUIProtectionLevels = ...
    """"""
    ForceHighProtection: CngUIProtectionLevels = ...
    """"""

class Constants(ABC, Object):
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

class CryptoAPITransform(Object, ICryptoTransform, IDisposable):
    """"""

    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def KeyHandle(self) -> IntPtr:
        """

        :return:
        """
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
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
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class CryptoAPITransformMode(Enum):
    """"""

    Encrypt: CryptoAPITransformMode = ...
    """"""
    Decrypt: CryptoAPITransformMode = ...
    """"""

class CryptoConfig(Object):
    """"""

    def __init__(self):
        """"""
    @classmethod
    @property
    def AllowOnlyFipsAlgorithms(cls) -> bool:
        """

        :return:
        """
    @classmethod
    def AddAlgorithm(cls, algorithm: Type, names: Array[str]) -> None:
        """

        :param algorithm:
        :param names:
        """
    @classmethod
    def AddOID(cls, oid: str, names: Array[str]) -> None:
        """

        :param oid:
        :param names:
        """
    @classmethod
    @overload
    def CreateFromName(cls, name: str) -> object:
        """

        :param name:
        :return:
        """
    @classmethod
    @overload
    def CreateFromName(cls, name: str, args: Array[object]) -> object:
        """

        :param name:
        :param args:
        :return:
        """
    @classmethod
    def EncodeOID(cls, str: str) -> Array[int]:
        """

        :param str:
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
    @classmethod
    def MapNameToOID(cls, name: str) -> str:
        """

        :param name:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CryptoStream(Stream, IDisposable):
    """"""

    @overload
    def __init__(self, stream: Stream, transform: ICryptoTransform, mode: CryptoStreamMode):
        """

        :param stream:
        :param transform:
        :param mode:
        """
    @overload
    def __init__(
        self, stream: Stream, transform: ICryptoTransform, mode: CryptoStreamMode, leaveOpen: bool
    ):
        """

        :param stream:
        :param transform:
        :param mode:
        :param leaveOpen:
        """
    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def HasFlushedFinalBlock(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def Clear(self) -> None:
        """"""
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
        :return:
        """
    def FlushFinalBlock(self) -> None:
        """"""
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
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """

class CryptoStreamMode(Enum):
    """"""

    Read: CryptoStreamMode = ...
    """"""
    Write: CryptoStreamMode = ...
    """"""

class CryptographicException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, hr: int):
        """

        :param hr:
        """
    @overload
    def __init__(self, message: str):
        """

        :param message:
        """
    @overload
    def __init__(self, message: str, inner: Exception):
        """

        :param message:
        :param inner:
        """
    @overload
    def __init__(self, format: str, insert: str):
        """

        :param format:
        :param insert:
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

class CryptographicUnexpectedOperationException(CryptographicException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """

        :param message:
        """
    @overload
    def __init__(self, message: str, inner: Exception):
        """

        :param message:
        :param inner:
        """
    @overload
    def __init__(self, format: str, insert: str):
        """

        :param format:
        :param insert:
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

class CspAlgorithmType(Enum):
    """"""

    Rsa: CspAlgorithmType = ...
    """"""
    Dss: CspAlgorithmType = ...
    """"""

class CspKeyContainerInfo(Object):
    """"""

    def __init__(self, parameters: CspParameters):
        """

        :param parameters:
        """
    @property
    def Accessible(self) -> bool:
        """

        :return:
        """
    @property
    def CryptoKeySecurity(self) -> CryptoKeySecurity:
        """

        :return:
        """
    @property
    def Exportable(self) -> bool:
        """

        :return:
        """
    @property
    def HardwareDevice(self) -> bool:
        """

        :return:
        """
    @property
    def KeyContainerName(self) -> str:
        """

        :return:
        """
    @property
    def KeyNumber(self) -> KeyNumber:
        """

        :return:
        """
    @property
    def MachineKeyStore(self) -> bool:
        """

        :return:
        """
    @property
    def Protected(self) -> bool:
        """

        :return:
        """
    @property
    def ProviderName(self) -> str:
        """

        :return:
        """
    @property
    def ProviderType(self) -> int:
        """

        :return:
        """
    @property
    def RandomlyGenerated(self) -> bool:
        """

        :return:
        """
    @property
    def Removable(self) -> bool:
        """

        :return:
        """
    @property
    def UniqueKeyContainerName(self) -> str:
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

class CspParameters(Object):
    """"""

    KeyContainerName: Final[str] = ...
    """
    
    :return: 
    """
    KeyNumber: Final[int] = ...
    """
    
    :return: 
    """
    ProviderName: Final[str] = ...
    """
    
    :return: 
    """
    ProviderType: Final[int] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, dwTypeIn: int):
        """

        :param dwTypeIn:
        """
    @overload
    def __init__(self, dwTypeIn: int, strProviderNameIn: str):
        """

        :param dwTypeIn:
        :param strProviderNameIn:
        """
    @overload
    def __init__(self, dwTypeIn: int, strProviderNameIn: str, strContainerNameIn: str):
        """

        :param dwTypeIn:
        :param strProviderNameIn:
        :param strContainerNameIn:
        """
    @overload
    def __init__(
        self,
        providerType: int,
        providerName: str,
        keyContainerName: str,
        cryptoKeySecurity: CryptoKeySecurity,
        keyPassword: SecureString,
    ):
        """

        :param providerType:
        :param providerName:
        :param keyContainerName:
        :param cryptoKeySecurity:
        :param keyPassword:
        """
    @overload
    def __init__(
        self,
        providerType: int,
        providerName: str,
        keyContainerName: str,
        cryptoKeySecurity: CryptoKeySecurity,
        parentWindowHandle: IntPtr,
    ):
        """

        :param providerType:
        :param providerName:
        :param keyContainerName:
        :param cryptoKeySecurity:
        :param parentWindowHandle:
        """
    @property
    def CryptoKeySecurity(self) -> CryptoKeySecurity:
        """

        :return:
        """
    @CryptoKeySecurity.setter
    def CryptoKeySecurity(self, value: CryptoKeySecurity) -> None: ...
    @property
    def Flags(self) -> CspProviderFlags:
        """

        :return:
        """
    @Flags.setter
    def Flags(self, value: CspProviderFlags) -> None: ...
    @property
    def KeyPassword(self) -> SecureString:
        """

        :return:
        """
    @KeyPassword.setter
    def KeyPassword(self, value: SecureString) -> None: ...
    @property
    def ParentWindowHandle(self) -> IntPtr:
        """

        :return:
        """
    @ParentWindowHandle.setter
    def ParentWindowHandle(self, value: IntPtr) -> None: ...
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

class DES(ABC, SymmetricAlgorithm, IDisposable):
    """"""

    @property
    def BlockSize(self) -> int:
        """

        :return:
        """
    @BlockSize.setter
    def BlockSize(self, value: int) -> None: ...
    @property
    def FeedbackSize(self) -> int:
        """

        :return:
        """
    @FeedbackSize.setter
    def FeedbackSize(self, value: int) -> None: ...
    @property
    def IV(self) -> Array[int]:
        """

        :return:
        """
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def Key(self) -> Array[int]:
        """

        :return:
        """
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def KeySize(self) -> int:
        """

        :return:
        """
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalBlockSizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def Mode(self) -> CipherMode:
        """

        :return:
        """
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    @property
    def Padding(self) -> PaddingMode:
        """

        :return:
        """
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    def Clear(self) -> None:
        """"""
    @classmethod
    @overload
    def Create(cls) -> DES:
        """

        :return:
        """
    @classmethod
    @overload
    def Create(cls, algName: str) -> DES:
        """

        :param algName:
        :return:
        """
    @overload
    def CreateDecryptor(self) -> ICryptoTransform:
        """

        :return:
        """
    @overload
    def CreateDecryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """

        :param rgbKey:
        :param rgbIV:
        :return:
        """
    @overload
    def CreateEncryptor(self) -> ICryptoTransform:
        """

        :return:
        """
    @overload
    def CreateEncryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """

        :param rgbKey:
        :param rgbIV:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GenerateIV(self) -> None:
        """"""
    def GenerateKey(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def IsSemiWeakKey(cls, rgbKey: Array[int]) -> bool:
        """

        :param rgbKey:
        :return:
        """
    @classmethod
    def IsWeakKey(cls, rgbKey: Array[int]) -> bool:
        """

        :param rgbKey:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def ValidKeySize(self, bitLength: int) -> bool:
        """

        :param bitLength:
        :return:
        """

class DESCryptoServiceProvider(DES, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def BlockSize(self) -> int:
        """

        :return:
        """
    @BlockSize.setter
    def BlockSize(self, value: int) -> None: ...
    @property
    def FeedbackSize(self) -> int:
        """

        :return:
        """
    @FeedbackSize.setter
    def FeedbackSize(self, value: int) -> None: ...
    @property
    def IV(self) -> Array[int]:
        """

        :return:
        """
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def Key(self) -> Array[int]:
        """

        :return:
        """
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def KeySize(self) -> int:
        """

        :return:
        """
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalBlockSizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def Mode(self) -> CipherMode:
        """

        :return:
        """
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    @property
    def Padding(self) -> PaddingMode:
        """

        :return:
        """
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    def Clear(self) -> None:
        """"""
    @overload
    def CreateDecryptor(self) -> ICryptoTransform:
        """

        :return:
        """
    @overload
    def CreateDecryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """

        :param rgbKey:
        :param rgbIV:
        :return:
        """
    @overload
    def CreateEncryptor(self) -> ICryptoTransform:
        """

        :return:
        """
    @overload
    def CreateEncryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """

        :param rgbKey:
        :param rgbIV:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GenerateIV(self) -> None:
        """"""
    def GenerateKey(self) -> None:
        """"""
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
    def ValidKeySize(self, bitLength: int) -> bool:
        """

        :param bitLength:
        :return:
        """

class DSA(ABC, AsymmetricAlgorithm, IDisposable):
    """"""

    @property
    def KeyExchangeAlgorithm(self) -> str:
        """

        :return:
        """
    @property
    def KeySize(self) -> int:
        """

        :return:
        """
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def SignatureAlgorithm(self) -> str:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @classmethod
    @overload
    def Create(cls) -> DSA:
        """

        :return:
        """
    @classmethod
    @overload
    def Create(cls, parameters: DSAParameters) -> DSA:
        """

        :param parameters:
        :return:
        """
    @classmethod
    @overload
    def Create(cls, keySizeInBits: int) -> DSA:
        """

        :param keySizeInBits:
        :return:
        """
    @classmethod
    @overload
    def Create(cls, algName: str) -> DSA:
        """

        :param algName:
        :return:
        """
    def CreateSignature(self, rgbHash: Array[int]) -> Array[int]:
        """

        :param rgbHash:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ExportParameters(self, includePrivateParameters: bool) -> DSAParameters:
        """

        :param includePrivateParameters:
        :return:
        """
    def FromXmlString(self, xmlString: str) -> None:
        """

        :param xmlString:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ImportParameters(self, parameters: DSAParameters) -> None:
        """

        :param parameters:
        """
    @overload
    def SignData(self, data: Stream, hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """

        :param data:
        :param hashAlgorithm:
        :return:
        """
    @overload
    def SignData(self, data: Array[int], hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """

        :param data:
        :param hashAlgorithm:
        :return:
        """
    @overload
    def SignData(
        self, data: Array[int], offset: int, count: int, hashAlgorithm: HashAlgorithmName
    ) -> Array[int]:
        """

        :param data:
        :param offset:
        :param count:
        :param hashAlgorithm:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXmlString(self, includePrivateParameters: bool) -> str:
        """

        :param includePrivateParameters:
        :return:
        """
    @overload
    def VerifyData(
        self, data: Stream, signature: Array[int], hashAlgorithm: HashAlgorithmName
    ) -> bool:
        """

        :param data:
        :param signature:
        :param hashAlgorithm:
        :return:
        """
    @overload
    def VerifyData(
        self, data: Array[int], signature: Array[int], hashAlgorithm: HashAlgorithmName
    ) -> bool:
        """

        :param data:
        :param signature:
        :param hashAlgorithm:
        :return:
        """
    @overload
    def VerifyData(
        self,
        data: Array[int],
        offset: int,
        count: int,
        signature: Array[int],
        hashAlgorithm: HashAlgorithmName,
    ) -> bool:
        """

        :param data:
        :param offset:
        :param count:
        :param signature:
        :param hashAlgorithm:
        :return:
        """
    def VerifySignature(self, rgbHash: Array[int], rgbSignature: Array[int]) -> bool:
        """

        :param rgbHash:
        :param rgbSignature:
        :return:
        """

class DSACng(DSA, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, key: CngKey):
        """

        :param key:
        """
    @overload
    def __init__(self, keySize: int):
        """

        :param keySize:
        """
    @property
    def Key(self) -> CngKey:
        """

        :return:
        """
    @property
    def KeyExchangeAlgorithm(self) -> str:
        """

        :return:
        """
    @property
    def KeySize(self) -> int:
        """

        :return:
        """
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def SignatureAlgorithm(self) -> str:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    def CreateSignature(self, rgbHash: Array[int]) -> Array[int]:
        """

        :param rgbHash:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ExportParameters(self, includePrivateParameters: bool) -> DSAParameters:
        """

        :param includePrivateParameters:
        :return:
        """
    def FromXmlString(self, xmlString: str) -> None:
        """

        :param xmlString:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ImportParameters(self, parameters: DSAParameters) -> None:
        """

        :param parameters:
        """
    @overload
    def SignData(self, data: Stream, hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """

        :param data:
        :param hashAlgorithm:
        :return:
        """
    @overload
    def SignData(self, data: Array[int], hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """

        :param data:
        :param hashAlgorithm:
        :return:
        """
    @overload
    def SignData(
        self, data: Array[int], offset: int, count: int, hashAlgorithm: HashAlgorithmName
    ) -> Array[int]:
        """

        :param data:
        :param offset:
        :param count:
        :param hashAlgorithm:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXmlString(self, includePrivateParameters: bool) -> str:
        """

        :param includePrivateParameters:
        :return:
        """
    @overload
    def VerifyData(
        self, data: Stream, signature: Array[int], hashAlgorithm: HashAlgorithmName
    ) -> bool:
        """

        :param data:
        :param signature:
        :param hashAlgorithm:
        :return:
        """
    @overload
    def VerifyData(
        self, data: Array[int], signature: Array[int], hashAlgorithm: HashAlgorithmName
    ) -> bool:
        """

        :param data:
        :param signature:
        :param hashAlgorithm:
        :return:
        """
    @overload
    def VerifyData(
        self,
        data: Array[int],
        offset: int,
        count: int,
        signature: Array[int],
        hashAlgorithm: HashAlgorithmName,
    ) -> bool:
        """

        :param data:
        :param offset:
        :param count:
        :param signature:
        :param hashAlgorithm:
        :return:
        """
    def VerifySignature(self, rgbHash: Array[int], rgbSignature: Array[int]) -> bool:
        """

        :param rgbHash:
        :param rgbSignature:
        :return:
        """

class DSACryptoServiceProvider(DSA, ICspAsymmetricAlgorithm, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, parameters: CspParameters):
        """

        :param parameters:
        """
    @overload
    def __init__(self, dwKeySize: int):
        """

        :param dwKeySize:
        """
    @overload
    def __init__(self, dwKeySize: int, parameters: CspParameters):
        """

        :param dwKeySize:
        :param parameters:
        """
    @property
    def CspKeyContainerInfo(self) -> CspKeyContainerInfo:
        """

        :return:
        """
    @property
    def KeyExchangeAlgorithm(self) -> str:
        """

        :return:
        """
    @property
    def KeySize(self) -> int:
        """

        :return:
        """
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def PersistKeyInCsp(self) -> bool:
        """

        :return:
        """
    @PersistKeyInCsp.setter
    def PersistKeyInCsp(self, value: bool) -> None: ...
    @property
    def PublicOnly(self) -> bool:
        """

        :return:
        """
    @property
    def SignatureAlgorithm(self) -> str:
        """

        :return:
        """
    @classmethod
    @property
    def UseMachineKeyStore(cls) -> bool:
        """

        :return:
        """
    @classmethod
    @UseMachineKeyStore.setter
    def UseMachineKeyStore(cls, value: bool) -> None: ...
    def Clear(self) -> None:
        """"""
    def CreateSignature(self, rgbHash: Array[int]) -> Array[int]:
        """

        :param rgbHash:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ExportCspBlob(self, includePrivateParameters: bool) -> Array[int]:
        """

        :param includePrivateParameters:
        :return:
        """
    def ExportParameters(self, includePrivateParameters: bool) -> DSAParameters:
        """

        :param includePrivateParameters:
        :return:
        """
    def FromXmlString(self, xmlString: str) -> None:
        """

        :param xmlString:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ImportCspBlob(self, rawData: Array[int]) -> None:
        """

        :param rawData:
        """
    def ImportParameters(self, parameters: DSAParameters) -> None:
        """

        :param parameters:
        """
    @overload
    def SignData(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def SignData(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def SignData(self, data: Stream, hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """

        :param data:
        :param hashAlgorithm:
        :return:
        """
    @overload
    def SignData(self, data: Array[int], hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """

        :param data:
        :param hashAlgorithm:
        :return:
        """
    @overload
    def SignData(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def SignData(
        self, data: Array[int], offset: int, count: int, hashAlgorithm: HashAlgorithmName
    ) -> Array[int]:
        """

        :param data:
        :param offset:
        :param count:
        :param hashAlgorithm:
        :return:
        """
    def SignHash(self, rgbHash: Array[int], str: str) -> Array[int]:
        """

        :param rgbHash:
        :param str:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXmlString(self, includePrivateParameters: bool) -> str:
        """

        :param includePrivateParameters:
        :return:
        """
    @overload
    def VerifyData(self, rgbData: Array[int], rgbSignature: Array[int]) -> bool:
        """

        :param rgbData:
        :param rgbSignature:
        :return:
        """
    @overload
    def VerifyData(
        self, data: Stream, signature: Array[int], hashAlgorithm: HashAlgorithmName
    ) -> bool:
        """

        :param data:
        :param signature:
        :param hashAlgorithm:
        :return:
        """
    @overload
    def VerifyData(
        self, data: Array[int], signature: Array[int], hashAlgorithm: HashAlgorithmName
    ) -> bool:
        """

        :param data:
        :param signature:
        :param hashAlgorithm:
        :return:
        """
    @overload
    def VerifyData(
        self,
        data: Array[int],
        offset: int,
        count: int,
        signature: Array[int],
        hashAlgorithm: HashAlgorithmName,
    ) -> bool:
        """

        :param data:
        :param offset:
        :param count:
        :param signature:
        :param hashAlgorithm:
        :return:
        """
    def VerifyHash(self, rgbHash: Array[int], str: str, rgbSignature: Array[int]) -> bool:
        """

        :param rgbHash:
        :param str:
        :param rgbSignature:
        :return:
        """
    def VerifySignature(self, rgbHash: Array[int], rgbSignature: Array[int]) -> bool:
        """

        :param rgbHash:
        :param rgbSignature:
        :return:
        """

class DSACspObject(Object):
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

class DSAFIPSVERSION_ENUM(Enum):
    """"""

    DSA_FIPS186_2: DSAFIPSVERSION_ENUM = ...
    """"""
    DSA_FIPS186_3: DSAFIPSVERSION_ENUM = ...
    """"""

class DSAParameters(ValueType):
    """"""

    Counter: Final[int] = ...
    """
    
    :return: 
    """
    G: Final[Array[int]] = ...
    """
    
    :return: 
    """
    J: Final[Array[int]] = ...
    """
    
    :return: 
    """
    P: Final[Array[int]] = ...
    """
    
    :return: 
    """
    Q: Final[Array[int]] = ...
    """
    
    :return: 
    """
    Seed: Final[Array[int]] = ...
    """
    
    :return: 
    """
    X: Final[Array[int]] = ...
    """
    
    :return: 
    """
    Y: Final[Array[int]] = ...
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

class DSASignatureDeformatter(AsymmetricSignatureDeformatter):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, key: AsymmetricAlgorithm):
        """

        :param key:
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
    def SetHashAlgorithm(self, strName: str) -> None:
        """

        :param strName:
        """
    def SetKey(self, key: AsymmetricAlgorithm) -> None:
        """

        :param key:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def VerifySignature(self, hash: HashAlgorithm, rgbSignature: Array[int]) -> bool:
        """

        :param hash:
        :param rgbSignature:
        :return:
        """
    @overload
    def VerifySignature(self, rgbHash: Array[int], rgbSignature: Array[int]) -> bool:
        """

        :param rgbHash:
        :param rgbSignature:
        :return:
        """

class DSASignatureDescription(SignatureDescription):
    """"""

    def __init__(self):
        """"""
    @property
    def DeformatterAlgorithm(self) -> str:
        """

        :return:
        """
    @DeformatterAlgorithm.setter
    def DeformatterAlgorithm(self, value: str) -> None: ...
    @property
    def DigestAlgorithm(self) -> str:
        """

        :return:
        """
    @DigestAlgorithm.setter
    def DigestAlgorithm(self, value: str) -> None: ...
    @property
    def FormatterAlgorithm(self) -> str:
        """

        :return:
        """
    @FormatterAlgorithm.setter
    def FormatterAlgorithm(self, value: str) -> None: ...
    @property
    def KeyAlgorithm(self) -> str:
        """

        :return:
        """
    @KeyAlgorithm.setter
    def KeyAlgorithm(self, value: str) -> None: ...
    def CreateDeformatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureDeformatter:
        """

        :param key:
        :return:
        """
    def CreateDigest(self) -> HashAlgorithm:
        """

        :return:
        """
    def CreateFormatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureFormatter:
        """

        :param key:
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

class DSASignatureFormatter(AsymmetricSignatureFormatter):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, key: AsymmetricAlgorithm):
        """

        :param key:
        """
    @overload
    def CreateSignature(self, hash: HashAlgorithm) -> Array[int]:
        """

        :param hash:
        :return:
        """
    @overload
    def CreateSignature(self, rgbHash: Array[int]) -> Array[int]:
        """

        :param rgbHash:
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
    def SetHashAlgorithm(self, strName: str) -> None:
        """

        :param strName:
        """
    def SetKey(self, key: AsymmetricAlgorithm) -> None:
        """

        :param key:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class DeriveBytes(ABC, Object, IDisposable):
    """"""

    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetBytes(self, cb: int) -> Array[int]:
        """

        :param cb:
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
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class ECCng(ABC, Object):
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

class ECCurve(ValueType):
    """"""

    A: Final[Array[int]] = ...
    """
    
    :return: 
    """
    B: Final[Array[int]] = ...
    """
    
    :return: 
    """
    Cofactor: Final[Array[int]] = ...
    """
    
    :return: 
    """
    CurveType: Final[ECCurve.ECCurveType] = ...
    """
    
    :return: 
    """
    G: Final[ECPoint] = ...
    """
    
    :return: 
    """
    Hash: Final[Optional[HashAlgorithmName]] = ...
    """
    
    :return: 
    """
    Order: Final[Array[int]] = ...
    """
    
    :return: 
    """
    Polynomial: Final[Array[int]] = ...
    """
    
    :return: 
    """
    Prime: Final[Array[int]] = ...
    """
    
    :return: 
    """
    Seed: Final[Array[int]] = ...
    """
    
    :return: 
    """
    @property
    def IsCharacteristic2(self) -> bool:
        """

        :return:
        """
    @property
    def IsExplicit(self) -> bool:
        """

        :return:
        """
    @property
    def IsNamed(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrime(self) -> bool:
        """

        :return:
        """
    @property
    def Oid(self) -> Oid:
        """

        :return:
        """
    @classmethod
    def CreateFromFriendlyName(cls, oidFriendlyName: str) -> ECCurve:
        """

        :param oidFriendlyName:
        :return:
        """
    @classmethod
    def CreateFromOid(cls, curveOid: Oid) -> ECCurve:
        """

        :param curveOid:
        :return:
        """
    @classmethod
    def CreateFromValue(cls, oidValue: str) -> ECCurve:
        """

        :param oidValue:
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
    def Validate(self) -> None:
        """"""

    class ECCurveType(Enum):
        """"""

        Implicit: ECCurveType = ...
        """"""
        PrimeShortWeierstrass: ECCurveType = ...
        """"""
        PrimeTwistedEdwards: ECCurveType = ...
        """"""
        PrimeMontgomery: ECCurveType = ...
        """"""
        Characteristic2: ECCurveType = ...
        """"""
        Named: ECCurveType = ...
        """"""

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

class ECDiffieHellman(ABC, AsymmetricAlgorithm, IDisposable):
    """"""

    @property
    def KeyExchangeAlgorithm(self) -> str:
        """

        :return:
        """
    @property
    def KeySize(self) -> int:
        """

        :return:
        """
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def PublicKey(self) -> ECDiffieHellmanPublicKey:
        """

        :return:
        """
    @property
    def SignatureAlgorithm(self) -> str:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @classmethod
    @overload
    def Create(cls) -> ECDiffieHellman:
        """

        :return:
        """
    @classmethod
    @overload
    def Create(cls, curve: ECCurve) -> ECDiffieHellman:
        """

        :param curve:
        :return:
        """
    @classmethod
    @overload
    def Create(cls, parameters: ECParameters) -> ECDiffieHellman:
        """

        :param parameters:
        :return:
        """
    @classmethod
    @overload
    def Create(cls, algorithm: str) -> ECDiffieHellman:
        """

        :param algorithm:
        :return:
        """
    @overload
    def DeriveKeyFromHash(
        self, otherPartyPublicKey: ECDiffieHellmanPublicKey, hashAlgorithm: HashAlgorithmName
    ) -> Array[int]:
        """

        :param otherPartyPublicKey:
        :param hashAlgorithm:
        :return:
        """
    @overload
    def DeriveKeyFromHash(
        self,
        otherPartyPublicKey: ECDiffieHellmanPublicKey,
        hashAlgorithm: HashAlgorithmName,
        secretPrepend: Array[int],
        secretAppend: Array[int],
    ) -> Array[int]:
        """

        :param otherPartyPublicKey:
        :param hashAlgorithm:
        :param secretPrepend:
        :param secretAppend:
        :return:
        """
    @overload
    def DeriveKeyFromHmac(
        self,
        otherPartyPublicKey: ECDiffieHellmanPublicKey,
        hashAlgorithm: HashAlgorithmName,
        hmacKey: Array[int],
    ) -> Array[int]:
        """

        :param otherPartyPublicKey:
        :param hashAlgorithm:
        :param hmacKey:
        :return:
        """
    @overload
    def DeriveKeyFromHmac(
        self,
        otherPartyPublicKey: ECDiffieHellmanPublicKey,
        hashAlgorithm: HashAlgorithmName,
        hmacKey: Array[int],
        secretPrepend: Array[int],
        secretAppend: Array[int],
    ) -> Array[int]:
        """

        :param otherPartyPublicKey:
        :param hashAlgorithm:
        :param hmacKey:
        :param secretPrepend:
        :param secretAppend:
        :return:
        """
    def DeriveKeyMaterial(self, otherPartyPublicKey: ECDiffieHellmanPublicKey) -> Array[int]:
        """

        :param otherPartyPublicKey:
        :return:
        """
    def DeriveKeyTls(
        self,
        otherPartyPublicKey: ECDiffieHellmanPublicKey,
        prfLabel: Array[int],
        prfSeed: Array[int],
    ) -> Array[int]:
        """

        :param otherPartyPublicKey:
        :param prfLabel:
        :param prfSeed:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ExportExplicitParameters(self, includePrivateParameters: bool) -> ECParameters:
        """

        :param includePrivateParameters:
        :return:
        """
    def ExportParameters(self, includePrivateParameters: bool) -> ECParameters:
        """

        :param includePrivateParameters:
        :return:
        """
    def FromXmlString(self, xmlString: str) -> None:
        """

        :param xmlString:
        """
    def GenerateKey(self, curve: ECCurve) -> None:
        """

        :param curve:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ImportParameters(self, parameters: ECParameters) -> None:
        """

        :param parameters:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXmlString(self, includePrivateParameters: bool) -> str:
        """

        :param includePrivateParameters:
        :return:
        """

class ECDiffieHellmanCng(ECDiffieHellman, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, key: CngKey):
        """

        :param key:
        """
    @overload
    def __init__(self, curve: ECCurve):
        """

        :param curve:
        """
    @overload
    def __init__(self, keySize: int):
        """

        :param keySize:
        """
    @property
    def HashAlgorithm(self) -> CngAlgorithm:
        """

        :return:
        """
    @HashAlgorithm.setter
    def HashAlgorithm(self, value: CngAlgorithm) -> None: ...
    @property
    def HmacKey(self) -> Array[int]:
        """

        :return:
        """
    @HmacKey.setter
    def HmacKey(self, value: Array[int]) -> None: ...
    @property
    def Key(self) -> CngKey:
        """

        :return:
        """
    @property
    def KeyDerivationFunction(self) -> ECDiffieHellmanKeyDerivationFunction:
        """

        :return:
        """
    @KeyDerivationFunction.setter
    def KeyDerivationFunction(self, value: ECDiffieHellmanKeyDerivationFunction) -> None: ...
    @property
    def KeyExchangeAlgorithm(self) -> str:
        """

        :return:
        """
    @property
    def KeySize(self) -> int:
        """

        :return:
        """
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def Label(self) -> Array[int]:
        """

        :return:
        """
    @Label.setter
    def Label(self, value: Array[int]) -> None: ...
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def PublicKey(self) -> ECDiffieHellmanPublicKey:
        """

        :return:
        """
    @property
    def SecretAppend(self) -> Array[int]:
        """

        :return:
        """
    @SecretAppend.setter
    def SecretAppend(self, value: Array[int]) -> None: ...
    @property
    def SecretPrepend(self) -> Array[int]:
        """

        :return:
        """
    @SecretPrepend.setter
    def SecretPrepend(self, value: Array[int]) -> None: ...
    @property
    def Seed(self) -> Array[int]:
        """

        :return:
        """
    @Seed.setter
    def Seed(self, value: Array[int]) -> None: ...
    @property
    def SignatureAlgorithm(self) -> str:
        """

        :return:
        """
    @property
    def UseSecretAgreementAsHmacKey(self) -> bool:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def DeriveKeyFromHash(
        self, otherPartyPublicKey: ECDiffieHellmanPublicKey, hashAlgorithm: HashAlgorithmName
    ) -> Array[int]:
        """

        :param otherPartyPublicKey:
        :param hashAlgorithm:
        :return:
        """
    @overload
    def DeriveKeyFromHash(
        self,
        otherPartyPublicKey: ECDiffieHellmanPublicKey,
        hashAlgorithm: HashAlgorithmName,
        secretPrepend: Array[int],
        secretAppend: Array[int],
    ) -> Array[int]:
        """

        :param otherPartyPublicKey:
        :param hashAlgorithm:
        :param secretPrepend:
        :param secretAppend:
        :return:
        """
    @overload
    def DeriveKeyFromHmac(
        self,
        otherPartyPublicKey: ECDiffieHellmanPublicKey,
        hashAlgorithm: HashAlgorithmName,
        hmacKey: Array[int],
    ) -> Array[int]:
        """

        :param otherPartyPublicKey:
        :param hashAlgorithm:
        :param hmacKey:
        :return:
        """
    @overload
    def DeriveKeyFromHmac(
        self,
        otherPartyPublicKey: ECDiffieHellmanPublicKey,
        hashAlgorithm: HashAlgorithmName,
        hmacKey: Array[int],
        secretPrepend: Array[int],
        secretAppend: Array[int],
    ) -> Array[int]:
        """

        :param otherPartyPublicKey:
        :param hashAlgorithm:
        :param hmacKey:
        :param secretPrepend:
        :param secretAppend:
        :return:
        """
    @overload
    def DeriveKeyMaterial(self, otherPartyPublicKey: CngKey) -> Array[int]:
        """

        :param otherPartyPublicKey:
        :return:
        """
    @overload
    def DeriveKeyMaterial(self, otherPartyPublicKey: ECDiffieHellmanPublicKey) -> Array[int]:
        """

        :param otherPartyPublicKey:
        :return:
        """
    def DeriveKeyTls(
        self,
        otherPartyPublicKey: ECDiffieHellmanPublicKey,
        prfLabel: Array[int],
        prfSeed: Array[int],
    ) -> Array[int]:
        """

        :param otherPartyPublicKey:
        :param prfLabel:
        :param prfSeed:
        :return:
        """
    @overload
    def DeriveSecretAgreementHandle(self, otherPartyPublicKey: CngKey) -> SafeNCryptSecretHandle:
        """

        :param otherPartyPublicKey:
        :return:
        """
    @overload
    def DeriveSecretAgreementHandle(
        self, otherPartyPublicKey: ECDiffieHellmanPublicKey
    ) -> SafeNCryptSecretHandle:
        """

        :param otherPartyPublicKey:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ExportExplicitParameters(self, includePrivateParameters: bool) -> ECParameters:
        """

        :param includePrivateParameters:
        :return:
        """
    def ExportParameters(self, includePrivateParameters: bool) -> ECParameters:
        """

        :param includePrivateParameters:
        :return:
        """
    @overload
    def FromXmlString(self, xmlString: str) -> None:
        """

        :param xmlString:
        """
    @overload
    def FromXmlString(self, xml: str, format: ECKeyXmlFormat) -> None:
        """

        :param xml:
        :param format:
        """
    def GenerateKey(self, curve: ECCurve) -> None:
        """

        :param curve:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ImportParameters(self, parameters: ECParameters) -> None:
        """

        :param parameters:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToXmlString(self, format: ECKeyXmlFormat) -> str:
        """

        :param format:
        :return:
        """
    @overload
    def ToXmlString(self, includePrivateParameters: bool) -> str:
        """

        :param includePrivateParameters:
        :return:
        """

class ECDiffieHellmanCngPublicKey(ECDiffieHellmanPublicKey, IDisposable):
    """"""

    @property
    def BlobFormat(self) -> CngKeyBlobFormat:
        """

        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ExportExplicitParameters(self) -> ECParameters:
        """

        :return:
        """
    def ExportParameters(self) -> ECParameters:
        """

        :return:
        """
    @classmethod
    def FromByteArray(
        cls, publicKeyBlob: Array[int], format: CngKeyBlobFormat
    ) -> ECDiffieHellmanPublicKey:
        """

        :param publicKeyBlob:
        :param format:
        :return:
        """
    @classmethod
    def FromXmlString(cls, xml: str) -> ECDiffieHellmanCngPublicKey:
        """

        :param xml:
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
    def Import(self) -> CngKey:
        """

        :return:
        """
    def ToByteArray(self) -> Array[int]:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXmlString(self) -> str:
        """

        :return:
        """

class ECDiffieHellmanKeyDerivationFunction(Enum):
    """"""

    Hash: ECDiffieHellmanKeyDerivationFunction = ...
    """"""
    Hmac: ECDiffieHellmanKeyDerivationFunction = ...
    """"""
    Tls: ECDiffieHellmanKeyDerivationFunction = ...
    """"""

class ECDiffieHellmanPublicKey(ABC, Object, IDisposable):
    """"""

    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ExportExplicitParameters(self) -> ECParameters:
        """

        :return:
        """
    def ExportParameters(self) -> ECParameters:
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
    def ToByteArray(self) -> Array[int]:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXmlString(self) -> str:
        """

        :return:
        """

class ECDsa(ABC, AsymmetricAlgorithm, IDisposable):
    """"""

    @property
    def KeyExchangeAlgorithm(self) -> str:
        """

        :return:
        """
    @property
    def KeySize(self) -> int:
        """

        :return:
        """
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def SignatureAlgorithm(self) -> str:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @classmethod
    @overload
    def Create(cls) -> ECDsa:
        """

        :return:
        """
    @classmethod
    @overload
    def Create(cls, curve: ECCurve) -> ECDsa:
        """

        :param curve:
        :return:
        """
    @classmethod
    @overload
    def Create(cls, parameters: ECParameters) -> ECDsa:
        """

        :param parameters:
        :return:
        """
    @classmethod
    @overload
    def Create(cls, algorithm: str) -> ECDsa:
        """

        :param algorithm:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ExportExplicitParameters(self, includePrivateParameters: bool) -> ECParameters:
        """

        :param includePrivateParameters:
        :return:
        """
    def ExportParameters(self, includePrivateParameters: bool) -> ECParameters:
        """

        :param includePrivateParameters:
        :return:
        """
    def FromXmlString(self, xmlString: str) -> None:
        """

        :param xmlString:
        """
    def GenerateKey(self, curve: ECCurve) -> None:
        """

        :param curve:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ImportParameters(self, parameters: ECParameters) -> None:
        """

        :param parameters:
        """
    @overload
    def SignData(self, data: Stream, hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """

        :param data:
        :param hashAlgorithm:
        :return:
        """
    @overload
    def SignData(self, data: Array[int], hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """

        :param data:
        :param hashAlgorithm:
        :return:
        """
    @overload
    def SignData(
        self, data: Array[int], offset: int, count: int, hashAlgorithm: HashAlgorithmName
    ) -> Array[int]:
        """

        :param data:
        :param offset:
        :param count:
        :param hashAlgorithm:
        :return:
        """
    def SignHash(self, hash: Array[int]) -> Array[int]:
        """

        :param hash:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXmlString(self, includePrivateParameters: bool) -> str:
        """

        :param includePrivateParameters:
        :return:
        """
    @overload
    def VerifyData(
        self, data: Stream, signature: Array[int], hashAlgorithm: HashAlgorithmName
    ) -> bool:
        """

        :param data:
        :param signature:
        :param hashAlgorithm:
        :return:
        """
    @overload
    def VerifyData(
        self, data: Array[int], signature: Array[int], hashAlgorithm: HashAlgorithmName
    ) -> bool:
        """

        :param data:
        :param signature:
        :param hashAlgorithm:
        :return:
        """
    @overload
    def VerifyData(
        self,
        data: Array[int],
        offset: int,
        count: int,
        signature: Array[int],
        hashAlgorithm: HashAlgorithmName,
    ) -> bool:
        """

        :param data:
        :param offset:
        :param count:
        :param signature:
        :param hashAlgorithm:
        :return:
        """
    def VerifyHash(self, hash: Array[int], signature: Array[int]) -> bool:
        """

        :param hash:
        :param signature:
        :return:
        """

class ECDsaCng(ECDsa, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, key: CngKey):
        """

        :param key:
        """
    @overload
    def __init__(self, curve: ECCurve):
        """

        :param curve:
        """
    @overload
    def __init__(self, keySize: int):
        """

        :param keySize:
        """
    @property
    def HashAlgorithm(self) -> CngAlgorithm:
        """

        :return:
        """
    @HashAlgorithm.setter
    def HashAlgorithm(self, value: CngAlgorithm) -> None: ...
    @property
    def Key(self) -> CngKey:
        """

        :return:
        """
    @property
    def KeyExchangeAlgorithm(self) -> str:
        """

        :return:
        """
    @property
    def KeySize(self) -> int:
        """

        :return:
        """
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def SignatureAlgorithm(self) -> str:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ExportExplicitParameters(self, includePrivateParameters: bool) -> ECParameters:
        """

        :param includePrivateParameters:
        :return:
        """
    def ExportParameters(self, includePrivateParameters: bool) -> ECParameters:
        """

        :param includePrivateParameters:
        :return:
        """
    @overload
    def FromXmlString(self, xmlString: str) -> None:
        """

        :param xmlString:
        """
    @overload
    def FromXmlString(self, xml: str, format: ECKeyXmlFormat) -> None:
        """

        :param xml:
        :param format:
        """
    def GenerateKey(self, curve: ECCurve) -> None:
        """

        :param curve:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ImportParameters(self, parameters: ECParameters) -> None:
        """

        :param parameters:
        """
    @overload
    def SignData(self, data: Stream) -> Array[int]:
        """

        :param data:
        :return:
        """
    @overload
    def SignData(self, data: Array[int]) -> Array[int]:
        """

        :param data:
        :return:
        """
    @overload
    def SignData(self, data: Stream, hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """

        :param data:
        :param hashAlgorithm:
        :return:
        """
    @overload
    def SignData(self, data: Array[int], hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """

        :param data:
        :param hashAlgorithm:
        :return:
        """
    @overload
    def SignData(self, data: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param data:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def SignData(
        self, data: Array[int], offset: int, count: int, hashAlgorithm: HashAlgorithmName
    ) -> Array[int]:
        """

        :param data:
        :param offset:
        :param count:
        :param hashAlgorithm:
        :return:
        """
    def SignHash(self, hash: Array[int]) -> Array[int]:
        """

        :param hash:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToXmlString(self, format: ECKeyXmlFormat) -> str:
        """

        :param format:
        :return:
        """
    @overload
    def ToXmlString(self, includePrivateParameters: bool) -> str:
        """

        :param includePrivateParameters:
        :return:
        """
    @overload
    def VerifyData(self, data: Stream, signature: Array[int]) -> bool:
        """

        :param data:
        :param signature:
        :return:
        """
    @overload
    def VerifyData(self, data: Array[int], signature: Array[int]) -> bool:
        """

        :param data:
        :param signature:
        :return:
        """
    @overload
    def VerifyData(
        self, data: Stream, signature: Array[int], hashAlgorithm: HashAlgorithmName
    ) -> bool:
        """

        :param data:
        :param signature:
        :param hashAlgorithm:
        :return:
        """
    @overload
    def VerifyData(
        self, data: Array[int], signature: Array[int], hashAlgorithm: HashAlgorithmName
    ) -> bool:
        """

        :param data:
        :param signature:
        :param hashAlgorithm:
        :return:
        """
    @overload
    def VerifyData(self, data: Array[int], offset: int, count: int, signature: Array[int]) -> bool:
        """

        :param data:
        :param offset:
        :param count:
        :param signature:
        :return:
        """
    @overload
    def VerifyData(
        self,
        data: Array[int],
        offset: int,
        count: int,
        signature: Array[int],
        hashAlgorithm: HashAlgorithmName,
    ) -> bool:
        """

        :param data:
        :param offset:
        :param count:
        :param signature:
        :param hashAlgorithm:
        :return:
        """
    def VerifyHash(self, hash: Array[int], signature: Array[int]) -> bool:
        """

        :param hash:
        :param signature:
        :return:
        """

class ECKeyXmlFormat(Enum):
    """"""

    Rfc4050: ECKeyXmlFormat = ...
    """"""

class ECParameters(ValueType):
    """"""

    Curve: Final[ECCurve] = ...
    """
    
    :return: 
    """
    D: Final[Array[int]] = ...
    """
    
    :return: 
    """
    Q: Final[ECPoint] = ...
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
    def Validate(self) -> None:
        """"""

class ECPoint(ValueType):
    """"""

    X: Final[Array[int]] = ...
    """
    
    :return: 
    """
    Y: Final[Array[int]] = ...
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

class EncryptionMode(Enum):
    """"""

    Encrypt: EncryptionMode = ...
    """"""
    Decrypt: EncryptionMode = ...
    """"""

class FromBase64Transform(Object, ICryptoTransform, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, whitespaces: FromBase64TransformMode):
        """

        :param whitespaces:
        """
    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
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
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class FromBase64TransformMode(Enum):
    """"""

    IgnoreWhiteSpaces: FromBase64TransformMode = ...
    """"""
    DoNotIgnoreWhiteSpaces: FromBase64TransformMode = ...
    """"""

class HASHALGORITHM_ENUM(Enum):
    """"""

    DSA_HASH_ALGORITHM_SHA1: HASHALGORITHM_ENUM = ...
    """"""
    DSA_HASH_ALGORITHM_SHA256: HASHALGORITHM_ENUM = ...
    """"""
    DSA_HASH_ALGORITHM_SHA512: HASHALGORITHM_ENUM = ...
    """"""

class HMAC(ABC, KeyedHashAlgorithm, ICryptoTransform, IDisposable):
    """"""

    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def Hash(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HashName(self) -> str:
        """

        :return:
        """
    @HashName.setter
    def HashName(self, value: str) -> None: ...
    @property
    def HashSize(self) -> int:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def Key(self) -> Array[int]:
        """

        :return:
        """
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @classmethod
    @overload
    def Create(cls) -> HMAC:
        """

        :return:
        """
    @classmethod
    @overload
    def Create(cls, algorithmName: str) -> HMAC:
        """

        :param algorithmName:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class HMACMD5(HMAC, ICryptoTransform, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, key: Array[int]):
        """

        :param key:
        """
    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def Hash(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HashName(self) -> str:
        """

        :return:
        """
    @HashName.setter
    def HashName(self, value: str) -> None: ...
    @property
    def HashSize(self) -> int:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def Key(self) -> Array[int]:
        """

        :return:
        """
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class HMACRIPEMD160(HMAC, ICryptoTransform, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, key: Array[int]):
        """

        :param key:
        """
    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def Hash(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HashName(self) -> str:
        """

        :return:
        """
    @HashName.setter
    def HashName(self, value: str) -> None: ...
    @property
    def HashSize(self) -> int:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def Key(self) -> Array[int]:
        """

        :return:
        """
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class HMACSHA1(HMAC, ICryptoTransform, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, key: Array[int]):
        """

        :param key:
        """
    @overload
    def __init__(self, key: Array[int], useManagedSha1: bool):
        """

        :param key:
        :param useManagedSha1:
        """
    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def Hash(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HashName(self) -> str:
        """

        :return:
        """
    @HashName.setter
    def HashName(self, value: str) -> None: ...
    @property
    def HashSize(self) -> int:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def Key(self) -> Array[int]:
        """

        :return:
        """
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class HMACSHA256(HMAC, ICryptoTransform, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, key: Array[int]):
        """

        :param key:
        """
    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def Hash(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HashName(self) -> str:
        """

        :return:
        """
    @HashName.setter
    def HashName(self, value: str) -> None: ...
    @property
    def HashSize(self) -> int:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def Key(self) -> Array[int]:
        """

        :return:
        """
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class HMACSHA384(HMAC, ICryptoTransform, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, key: Array[int]):
        """

        :param key:
        """
    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def Hash(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HashName(self) -> str:
        """

        :return:
        """
    @HashName.setter
    def HashName(self, value: str) -> None: ...
    @property
    def HashSize(self) -> int:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def Key(self) -> Array[int]:
        """

        :return:
        """
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def ProduceLegacyHmacValues(self) -> bool:
        """

        :return:
        """
    @ProduceLegacyHmacValues.setter
    def ProduceLegacyHmacValues(self, value: bool) -> None: ...
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class HMACSHA512(HMAC, ICryptoTransform, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, key: Array[int]):
        """

        :param key:
        """
    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def Hash(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HashName(self) -> str:
        """

        :return:
        """
    @HashName.setter
    def HashName(self, value: str) -> None: ...
    @property
    def HashSize(self) -> int:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def Key(self) -> Array[int]:
        """

        :return:
        """
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def ProduceLegacyHmacValues(self) -> bool:
        """

        :return:
        """
    @ProduceLegacyHmacValues.setter
    def ProduceLegacyHmacValues(self, value: bool) -> None: ...
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class HashAlgorithm(ABC, Object, ICryptoTransform, IDisposable):
    """"""

    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def Hash(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HashSize(self) -> int:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @classmethod
    @overload
    def Create(cls) -> HashAlgorithm:
        """

        :return:
        """
    @classmethod
    @overload
    def Create(cls, hashName: str) -> HashAlgorithm:
        """

        :param hashName:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class HashAlgorithmName(ValueType, IEquatable[HashAlgorithmName]):
    """"""

    def __init__(self, name: str):
        """

        :param name:
        """
    @classmethod
    @property
    def MD5(cls) -> HashAlgorithmName:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @classmethod
    @property
    def SHA1(cls) -> HashAlgorithmName:
        """

        :return:
        """
    @classmethod
    @property
    def SHA256(cls) -> HashAlgorithmName:
        """

        :return:
        """
    @classmethod
    @property
    def SHA384(cls) -> HashAlgorithmName:
        """

        :return:
        """
    @classmethod
    @property
    def SHA512(cls) -> HashAlgorithmName:
        """

        :return:
        """
    @overload
    def Equals(self, other: HashAlgorithmName) -> bool:
        """

        :param other:
        :return:
        """
    @overload
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
    def __eq__(self, other: HashAlgorithmName) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: HashAlgorithmName) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: HashAlgorithmName, right: HashAlgorithmName) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: HashAlgorithmName, right: HashAlgorithmName) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

class ICryptoTransform(IDisposable):
    """"""

    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
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
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class ICspAsymmetricAlgorithm:
    """"""

    @property
    def CspKeyContainerInfo(self) -> CspKeyContainerInfo:
        """

        :return:
        """
    def ExportCspBlob(self, includePrivateParameters: bool) -> Array[int]:
        """

        :param includePrivateParameters:
        :return:
        """
    def ImportCspBlob(self, rawData: Array[int]) -> None:
        """

        :param rawData:
        """

class IncrementalHash(Object, IDisposable):
    """"""

    @property
    def AlgorithmName(self) -> HashAlgorithmName:
        """

        :return:
        """
    @overload
    def AppendData(self, data: Array[int]) -> None:
        """

        :param data:
        """
    @overload
    def AppendData(self, data: Array[int], offset: int, count: int) -> None:
        """

        :param data:
        :param offset:
        :param count:
        """
    @classmethod
    def CreateHMAC(cls, hashAlgorithm: HashAlgorithmName, key: Array[int]) -> IncrementalHash:
        """

        :param hashAlgorithm:
        :param key:
        :return:
        """
    @classmethod
    def CreateHash(cls, hashAlgorithm: HashAlgorithmName) -> IncrementalHash:
        """

        :param hashAlgorithm:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashAndReset(self) -> Array[int]:
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
    def ToString(self) -> str:
        """

        :return:
        """

class KeyNumber(Enum):
    """"""

    Exchange: KeyNumber = ...
    """"""
    Signature: KeyNumber = ...
    """"""

class KeySizes(Object):
    """"""

    def __init__(self, minSize: int, maxSize: int, skipSize: int):
        """

        :param minSize:
        :param maxSize:
        :param skipSize:
        """
    @property
    def MaxSize(self) -> int:
        """

        :return:
        """
    @property
    def MinSize(self) -> int:
        """

        :return:
        """
    @property
    def SkipSize(self) -> int:
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

class KeyedHashAlgorithm(ABC, HashAlgorithm, ICryptoTransform, IDisposable):
    """"""

    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def Hash(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HashSize(self) -> int:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def Key(self) -> Array[int]:
        """

        :return:
        """
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @classmethod
    @overload
    def Create(cls) -> KeyedHashAlgorithm:
        """

        :return:
        """
    @classmethod
    @overload
    def Create(cls, algName: str) -> KeyedHashAlgorithm:
        """

        :param algName:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class MACTripleDES(KeyedHashAlgorithm, ICryptoTransform, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, rgbKey: Array[int]):
        """

        :param rgbKey:
        """
    @overload
    def __init__(self, strTripleDES: str, rgbKey: Array[int]):
        """

        :param strTripleDES:
        :param rgbKey:
        """
    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def Hash(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HashSize(self) -> int:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def Key(self) -> Array[int]:
        """

        :return:
        """
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def Padding(self) -> PaddingMode:
        """

        :return:
        """
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class MD5(ABC, HashAlgorithm, ICryptoTransform, IDisposable):
    """"""

    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def Hash(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HashSize(self) -> int:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @classmethod
    @overload
    def Create(cls) -> MD5:
        """

        :return:
        """
    @classmethod
    @overload
    def Create(cls, algName: str) -> MD5:
        """

        :param algName:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class MD5Cng(MD5, ICryptoTransform, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def Hash(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HashSize(self) -> int:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class MD5CryptoServiceProvider(MD5, ICryptoTransform, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def Hash(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HashSize(self) -> int:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class ManifestSignatureInformation(Object):
    """"""

    @property
    def AuthenticodeSignature(self) -> AuthenticodeSignatureInformation:
        """

        :return:
        """
    @property
    def Manifest(self) -> ManifestKinds:
        """

        :return:
        """
    @property
    def StrongNameSignature(self) -> StrongNameSignatureInformation:
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
    @classmethod
    @overload
    def VerifySignature(
        cls, application: ActivationContext
    ) -> ManifestSignatureInformationCollection:
        """

        :param application:
        :return:
        """
    @classmethod
    @overload
    def VerifySignature(
        cls, application: ActivationContext, manifests: ManifestKinds
    ) -> ManifestSignatureInformationCollection:
        """

        :param application:
        :param manifests:
        :return:
        """
    @classmethod
    @overload
    def VerifySignature(
        cls,
        application: ActivationContext,
        manifests: ManifestKinds,
        revocationFlag: X509RevocationFlag,
        revocationMode: X509RevocationMode,
    ) -> ManifestSignatureInformationCollection:
        """

        :param application:
        :param manifests:
        :param revocationFlag:
        :param revocationMode:
        :return:
        """

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
        """

        :return:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Item(self) -> ManifestSignatureInformation:
        """

        :return:
        """
    @property
    def Item(self) -> ManifestSignatureInformation:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: ManifestSignatureInformation) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, item: ManifestSignatureInformation) -> None:
        """

        :param item:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, item: ManifestSignatureInformation) -> bool:
        """

        :param item:
        :return:
        """
    @overload
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[ManifestSignatureInformation], arrayIndex: int) -> None:
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
    @overload
    def IndexOf(self, item: ManifestSignatureInformation) -> int:
        """

        :param item:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, item: ManifestSignatureInformation) -> None:
        """

        :param index:
        :param item:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, item: ManifestSignatureInformation) -> bool:
        """

        :param item:
        :return:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    @overload
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    @overload
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def __contains__(self, value: ManifestSignatureInformation) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> ManifestSignatureInformation:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> ManifestSignatureInformation:
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
    def __iter__(self) -> Iterator[ManifestSignatureInformation]:
        """

        :return:
        """
    @overload
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __setitem__(self, index: int, value: ManifestSignatureInformation) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """

class MaskGenerationMethod(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GenerateMask(self, rgbSeed: Array[int], cbReturn: int) -> Array[int]:
        """

        :param rgbSeed:
        :param cbReturn:
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

class NCryptNative(ABC, Object):
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

class Oid(Object):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, oid: Oid):
        """

        :param oid:
        """
    @overload
    def __init__(self, oid: str):
        """

        :param oid:
        """
    @overload
    def __init__(self, value: str, friendlyName: str):
        """

        :param value:
        :param friendlyName:
        """
    @property
    def FriendlyName(self) -> str:
        """

        :return:
        """
    @FriendlyName.setter
    def FriendlyName(self, value: str) -> None: ...
    @property
    def Value(self) -> str:
        """

        :return:
        """
    @Value.setter
    def Value(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def FromFriendlyName(cls, friendlyName: str, group: OidGroup) -> Oid:
        """

        :param friendlyName:
        :param group:
        :return:
        """
    @classmethod
    def FromOidValue(cls, oidValue: str, group: OidGroup) -> Oid:
        """

        :param oidValue:
        :param group:
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

class OidCollection(Object, ICollection, IEnumerable):
    """"""

    def __init__(self):
        """"""
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> Oid:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    def Add(self, oid: Oid) -> int:
        """

        :param oid:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[Oid], index: int) -> None:
        """

        :param array:
        :param index:
        """
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
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def __getitem__(self, index: int) -> Oid:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, oid: str) -> Oid:
        """

        :param oid:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """

class OidEnumerator(Object, IEnumerator):
    """"""

    @property
    def Current(self) -> object:
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
    def MoveNext(self) -> bool:
        """

        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

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

class PKCS1MaskGenerationMethod(MaskGenerationMethod):
    """"""

    def __init__(self):
        """"""
    @property
    def HashName(self) -> str:
        """

        :return:
        """
    @HashName.setter
    def HashName(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GenerateMask(self, rgbSeed: Array[int], cbReturn: int) -> Array[int]:
        """

        :param rgbSeed:
        :param cbReturn:
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

class PasswordDeriveBytes(DeriveBytes, IDisposable):
    """"""

    @overload
    def __init__(self, password: Array[int], salt: Array[int]):
        """

        :param password:
        :param salt:
        """
    @overload
    def __init__(self, strPassword: str, rgbSalt: Array[int]):
        """

        :param strPassword:
        :param rgbSalt:
        """
    @overload
    def __init__(self, password: Array[int], salt: Array[int], cspParams: CspParameters):
        """

        :param password:
        :param salt:
        :param cspParams:
        """
    @overload
    def __init__(self, strPassword: str, rgbSalt: Array[int], cspParams: CspParameters):
        """

        :param strPassword:
        :param rgbSalt:
        :param cspParams:
        """
    @overload
    def __init__(self, password: Array[int], salt: Array[int], hashName: str, iterations: int):
        """

        :param password:
        :param salt:
        :param hashName:
        :param iterations:
        """
    @overload
    def __init__(self, strPassword: str, rgbSalt: Array[int], strHashName: str, iterations: int):
        """

        :param strPassword:
        :param rgbSalt:
        :param strHashName:
        :param iterations:
        """
    @overload
    def __init__(
        self,
        password: Array[int],
        salt: Array[int],
        hashName: str,
        iterations: int,
        cspParams: CspParameters,
    ):
        """

        :param password:
        :param salt:
        :param hashName:
        :param iterations:
        :param cspParams:
        """
    @overload
    def __init__(
        self,
        strPassword: str,
        rgbSalt: Array[int],
        strHashName: str,
        iterations: int,
        cspParams: CspParameters,
    ):
        """

        :param strPassword:
        :param rgbSalt:
        :param strHashName:
        :param iterations:
        :param cspParams:
        """
    @property
    def HashName(self) -> str:
        """

        :return:
        """
    @HashName.setter
    def HashName(self, value: str) -> None: ...
    @property
    def IterationCount(self) -> int:
        """

        :return:
        """
    @IterationCount.setter
    def IterationCount(self, value: int) -> None: ...
    @property
    def Salt(self) -> Array[int]:
        """

        :return:
        """
    @Salt.setter
    def Salt(self, value: Array[int]) -> None: ...
    def CryptDeriveKey(
        self, algname: str, alghashname: str, keySize: int, rgbIV: Array[int]
    ) -> Array[int]:
        """

        :param algname:
        :param alghashname:
        :param keySize:
        :param rgbIV:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetBytes(self, cb: int) -> Array[int]:
        """

        :param cb:
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
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class RC2(ABC, SymmetricAlgorithm, IDisposable):
    """"""

    @property
    def BlockSize(self) -> int:
        """

        :return:
        """
    @BlockSize.setter
    def BlockSize(self, value: int) -> None: ...
    @property
    def EffectiveKeySize(self) -> int:
        """

        :return:
        """
    @EffectiveKeySize.setter
    def EffectiveKeySize(self, value: int) -> None: ...
    @property
    def FeedbackSize(self) -> int:
        """

        :return:
        """
    @FeedbackSize.setter
    def FeedbackSize(self, value: int) -> None: ...
    @property
    def IV(self) -> Array[int]:
        """

        :return:
        """
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def Key(self) -> Array[int]:
        """

        :return:
        """
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def KeySize(self) -> int:
        """

        :return:
        """
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalBlockSizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def Mode(self) -> CipherMode:
        """

        :return:
        """
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    @property
    def Padding(self) -> PaddingMode:
        """

        :return:
        """
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    def Clear(self) -> None:
        """"""
    @classmethod
    @overload
    def Create(cls) -> RC2:
        """

        :return:
        """
    @classmethod
    @overload
    def Create(cls, AlgName: str) -> RC2:
        """

        :param AlgName:
        :return:
        """
    @overload
    def CreateDecryptor(self) -> ICryptoTransform:
        """

        :return:
        """
    @overload
    def CreateDecryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """

        :param rgbKey:
        :param rgbIV:
        :return:
        """
    @overload
    def CreateEncryptor(self) -> ICryptoTransform:
        """

        :return:
        """
    @overload
    def CreateEncryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """

        :param rgbKey:
        :param rgbIV:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GenerateIV(self) -> None:
        """"""
    def GenerateKey(self) -> None:
        """"""
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
    def ValidKeySize(self, bitLength: int) -> bool:
        """

        :param bitLength:
        :return:
        """

class RC2CryptoServiceProvider(RC2, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def BlockSize(self) -> int:
        """

        :return:
        """
    @BlockSize.setter
    def BlockSize(self, value: int) -> None: ...
    @property
    def EffectiveKeySize(self) -> int:
        """

        :return:
        """
    @EffectiveKeySize.setter
    def EffectiveKeySize(self, value: int) -> None: ...
    @property
    def FeedbackSize(self) -> int:
        """

        :return:
        """
    @FeedbackSize.setter
    def FeedbackSize(self, value: int) -> None: ...
    @property
    def IV(self) -> Array[int]:
        """

        :return:
        """
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def Key(self) -> Array[int]:
        """

        :return:
        """
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def KeySize(self) -> int:
        """

        :return:
        """
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalBlockSizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def Mode(self) -> CipherMode:
        """

        :return:
        """
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    @property
    def Padding(self) -> PaddingMode:
        """

        :return:
        """
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    @property
    def UseSalt(self) -> bool:
        """

        :return:
        """
    @UseSalt.setter
    def UseSalt(self, value: bool) -> None: ...
    def Clear(self) -> None:
        """"""
    @overload
    def CreateDecryptor(self) -> ICryptoTransform:
        """

        :return:
        """
    @overload
    def CreateDecryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """

        :param rgbKey:
        :param rgbIV:
        :return:
        """
    @overload
    def CreateEncryptor(self) -> ICryptoTransform:
        """

        :return:
        """
    @overload
    def CreateEncryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """

        :param rgbKey:
        :param rgbIV:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GenerateIV(self) -> None:
        """"""
    def GenerateKey(self) -> None:
        """"""
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
    def ValidKeySize(self, bitLength: int) -> bool:
        """

        :param bitLength:
        :return:
        """

class RIPEMD160(ABC, HashAlgorithm, ICryptoTransform, IDisposable):
    """"""

    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def Hash(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HashSize(self) -> int:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @classmethod
    @overload
    def Create(cls) -> RIPEMD160:
        """

        :return:
        """
    @classmethod
    @overload
    def Create(cls, hashName: str) -> RIPEMD160:
        """

        :param hashName:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class RIPEMD160Managed(RIPEMD160, ICryptoTransform, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def Hash(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HashSize(self) -> int:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class RNGCryptoServiceProvider(RandomNumberGenerator, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, cspParams: CspParameters):
        """

        :param cspParams:
        """
    @overload
    def __init__(self, rgb: Array[int]):
        """

        :param rgb:
        """
    @overload
    def __init__(self, str: str):
        """

        :param str:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetBytes(self, data: Array[int]) -> None:
        """

        :param data:
        """
    @overload
    def GetBytes(self, data: Array[int], offset: int, count: int) -> None:
        """

        :param data:
        :param offset:
        :param count:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetNonZeroBytes(self, data: Array[int]) -> None:
        """

        :param data:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class RSA(ABC, AsymmetricAlgorithm, IDisposable):
    """"""

    @property
    def KeyExchangeAlgorithm(self) -> str:
        """

        :return:
        """
    @property
    def KeySize(self) -> int:
        """

        :return:
        """
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def SignatureAlgorithm(self) -> str:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @classmethod
    @overload
    def Create(cls) -> RSA:
        """

        :return:
        """
    @classmethod
    @overload
    def Create(cls, parameters: RSAParameters) -> RSA:
        """

        :param parameters:
        :return:
        """
    @classmethod
    @overload
    def Create(cls, keySizeInBits: int) -> RSA:
        """

        :param keySizeInBits:
        :return:
        """
    @classmethod
    @overload
    def Create(cls, algName: str) -> RSA:
        """

        :param algName:
        :return:
        """
    def Decrypt(self, data: Array[int], padding: RSAEncryptionPadding) -> Array[int]:
        """

        :param data:
        :param padding:
        :return:
        """
    def DecryptValue(self, rgb: Array[int]) -> Array[int]:
        """

        :param rgb:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Encrypt(self, data: Array[int], padding: RSAEncryptionPadding) -> Array[int]:
        """

        :param data:
        :param padding:
        :return:
        """
    def EncryptValue(self, rgb: Array[int]) -> Array[int]:
        """

        :param rgb:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ExportParameters(self, includePrivateParameters: bool) -> RSAParameters:
        """

        :param includePrivateParameters:
        :return:
        """
    def FromXmlString(self, xmlString: str) -> None:
        """

        :param xmlString:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ImportParameters(self, parameters: RSAParameters) -> None:
        """

        :param parameters:
        """
    @overload
    def SignData(
        self, data: Stream, hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding
    ) -> Array[int]:
        """

        :param data:
        :param hashAlgorithm:
        :param padding:
        :return:
        """
    @overload
    def SignData(
        self, data: Array[int], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding
    ) -> Array[int]:
        """

        :param data:
        :param hashAlgorithm:
        :param padding:
        :return:
        """
    @overload
    def SignData(
        self,
        data: Array[int],
        offset: int,
        count: int,
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> Array[int]:
        """

        :param data:
        :param offset:
        :param count:
        :param hashAlgorithm:
        :param padding:
        :return:
        """
    def SignHash(
        self, hash: Array[int], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding
    ) -> Array[int]:
        """

        :param hash:
        :param hashAlgorithm:
        :param padding:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXmlString(self, includePrivateParameters: bool) -> str:
        """

        :param includePrivateParameters:
        :return:
        """
    @overload
    def VerifyData(
        self,
        data: Stream,
        signature: Array[int],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> bool:
        """

        :param data:
        :param signature:
        :param hashAlgorithm:
        :param padding:
        :return:
        """
    @overload
    def VerifyData(
        self,
        data: Array[int],
        signature: Array[int],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> bool:
        """

        :param data:
        :param signature:
        :param hashAlgorithm:
        :param padding:
        :return:
        """
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
        """

        :param data:
        :param offset:
        :param count:
        :param signature:
        :param hashAlgorithm:
        :param padding:
        :return:
        """
    def VerifyHash(
        self,
        hash: Array[int],
        signature: Array[int],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> bool:
        """

        :param hash:
        :param signature:
        :param hashAlgorithm:
        :param padding:
        :return:
        """

class RSACng(RSA, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, key: CngKey):
        """

        :param key:
        """
    @overload
    def __init__(self, keySize: int):
        """

        :param keySize:
        """
    @property
    def Key(self) -> CngKey:
        """

        :return:
        """
    @property
    def KeyExchangeAlgorithm(self) -> str:
        """

        :return:
        """
    @property
    def KeySize(self) -> int:
        """

        :return:
        """
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def SignatureAlgorithm(self) -> str:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    def Decrypt(self, data: Array[int], padding: RSAEncryptionPadding) -> Array[int]:
        """

        :param data:
        :param padding:
        :return:
        """
    def DecryptValue(self, rgb: Array[int]) -> Array[int]:
        """

        :param rgb:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Encrypt(self, data: Array[int], padding: RSAEncryptionPadding) -> Array[int]:
        """

        :param data:
        :param padding:
        :return:
        """
    def EncryptValue(self, rgb: Array[int]) -> Array[int]:
        """

        :param rgb:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ExportParameters(self, includePrivateParameters: bool) -> RSAParameters:
        """

        :param includePrivateParameters:
        :return:
        """
    def FromXmlString(self, xmlString: str) -> None:
        """

        :param xmlString:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ImportParameters(self, parameters: RSAParameters) -> None:
        """

        :param parameters:
        """
    @overload
    def SignData(
        self, data: Stream, hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding
    ) -> Array[int]:
        """

        :param data:
        :param hashAlgorithm:
        :param padding:
        :return:
        """
    @overload
    def SignData(
        self, data: Array[int], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding
    ) -> Array[int]:
        """

        :param data:
        :param hashAlgorithm:
        :param padding:
        :return:
        """
    @overload
    def SignData(
        self,
        data: Array[int],
        offset: int,
        count: int,
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> Array[int]:
        """

        :param data:
        :param offset:
        :param count:
        :param hashAlgorithm:
        :param padding:
        :return:
        """
    def SignHash(
        self, hash: Array[int], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding
    ) -> Array[int]:
        """

        :param hash:
        :param hashAlgorithm:
        :param padding:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXmlString(self, includePrivateParameters: bool) -> str:
        """

        :param includePrivateParameters:
        :return:
        """
    @overload
    def VerifyData(
        self,
        data: Stream,
        signature: Array[int],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> bool:
        """

        :param data:
        :param signature:
        :param hashAlgorithm:
        :param padding:
        :return:
        """
    @overload
    def VerifyData(
        self,
        data: Array[int],
        signature: Array[int],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> bool:
        """

        :param data:
        :param signature:
        :param hashAlgorithm:
        :param padding:
        :return:
        """
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
        """

        :param data:
        :param offset:
        :param count:
        :param signature:
        :param hashAlgorithm:
        :param padding:
        :return:
        """
    def VerifyHash(
        self,
        hash: Array[int],
        signature: Array[int],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> bool:
        """

        :param hash:
        :param signature:
        :param hashAlgorithm:
        :param padding:
        :return:
        """

class RSACryptoServiceProvider(RSA, ICspAsymmetricAlgorithm, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, parameters: CspParameters):
        """

        :param parameters:
        """
    @overload
    def __init__(self, dwKeySize: int):
        """

        :param dwKeySize:
        """
    @overload
    def __init__(self, dwKeySize: int, parameters: CspParameters):
        """

        :param dwKeySize:
        :param parameters:
        """
    @property
    def CspKeyContainerInfo(self) -> CspKeyContainerInfo:
        """

        :return:
        """
    @property
    def KeyExchangeAlgorithm(self) -> str:
        """

        :return:
        """
    @property
    def KeySize(self) -> int:
        """

        :return:
        """
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def PersistKeyInCsp(self) -> bool:
        """

        :return:
        """
    @PersistKeyInCsp.setter
    def PersistKeyInCsp(self, value: bool) -> None: ...
    @property
    def PublicOnly(self) -> bool:
        """

        :return:
        """
    @property
    def SignatureAlgorithm(self) -> str:
        """

        :return:
        """
    @classmethod
    @property
    def UseMachineKeyStore(cls) -> bool:
        """

        :return:
        """
    @classmethod
    @UseMachineKeyStore.setter
    def UseMachineKeyStore(cls, value: bool) -> None: ...
    def Clear(self) -> None:
        """"""
    @overload
    def Decrypt(self, data: Array[int], padding: RSAEncryptionPadding) -> Array[int]:
        """

        :param data:
        :param padding:
        :return:
        """
    @overload
    def Decrypt(self, rgb: Array[int], fOAEP: bool) -> Array[int]:
        """

        :param rgb:
        :param fOAEP:
        :return:
        """
    def DecryptValue(self, rgb: Array[int]) -> Array[int]:
        """

        :param rgb:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    @overload
    def Encrypt(self, data: Array[int], padding: RSAEncryptionPadding) -> Array[int]:
        """

        :param data:
        :param padding:
        :return:
        """
    @overload
    def Encrypt(self, rgb: Array[int], fOAEP: bool) -> Array[int]:
        """

        :param rgb:
        :param fOAEP:
        :return:
        """
    def EncryptValue(self, rgb: Array[int]) -> Array[int]:
        """

        :param rgb:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ExportCspBlob(self, includePrivateParameters: bool) -> Array[int]:
        """

        :param includePrivateParameters:
        :return:
        """
    def ExportParameters(self, includePrivateParameters: bool) -> RSAParameters:
        """

        :param includePrivateParameters:
        :return:
        """
    def FromXmlString(self, xmlString: str) -> None:
        """

        :param xmlString:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ImportCspBlob(self, rawData: Array[int]) -> None:
        """

        :param rawData:
        """
    def ImportParameters(self, parameters: RSAParameters) -> None:
        """

        :param parameters:
        """
    @overload
    def SignData(self, inputStream: Stream, halg: object) -> Array[int]:
        """

        :param inputStream:
        :param halg:
        :return:
        """
    @overload
    def SignData(self, buffer: Array[int], halg: object) -> Array[int]:
        """

        :param buffer:
        :param halg:
        :return:
        """
    @overload
    def SignData(
        self, data: Stream, hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding
    ) -> Array[int]:
        """

        :param data:
        :param hashAlgorithm:
        :param padding:
        :return:
        """
    @overload
    def SignData(
        self, data: Array[int], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding
    ) -> Array[int]:
        """

        :param data:
        :param hashAlgorithm:
        :param padding:
        :return:
        """
    @overload
    def SignData(self, buffer: Array[int], offset: int, count: int, halg: object) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param halg:
        :return:
        """
    @overload
    def SignData(
        self,
        data: Array[int],
        offset: int,
        count: int,
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> Array[int]:
        """

        :param data:
        :param offset:
        :param count:
        :param hashAlgorithm:
        :param padding:
        :return:
        """
    @overload
    def SignHash(self, rgbHash: Array[int], str: str) -> Array[int]:
        """

        :param rgbHash:
        :param str:
        :return:
        """
    @overload
    def SignHash(
        self, hash: Array[int], hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding
    ) -> Array[int]:
        """

        :param hash:
        :param hashAlgorithm:
        :param padding:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def ToXmlString(self, includePrivateParameters: bool) -> str:
        """

        :param includePrivateParameters:
        :return:
        """
    @overload
    def VerifyData(self, buffer: Array[int], halg: object, signature: Array[int]) -> bool:
        """

        :param buffer:
        :param halg:
        :param signature:
        :return:
        """
    @overload
    def VerifyData(
        self,
        data: Stream,
        signature: Array[int],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> bool:
        """

        :param data:
        :param signature:
        :param hashAlgorithm:
        :param padding:
        :return:
        """
    @overload
    def VerifyData(
        self,
        data: Array[int],
        signature: Array[int],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> bool:
        """

        :param data:
        :param signature:
        :param hashAlgorithm:
        :param padding:
        :return:
        """
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
        """

        :param data:
        :param offset:
        :param count:
        :param signature:
        :param hashAlgorithm:
        :param padding:
        :return:
        """
    @overload
    def VerifyHash(self, rgbHash: Array[int], str: str, rgbSignature: Array[int]) -> bool:
        """

        :param rgbHash:
        :param str:
        :param rgbSignature:
        :return:
        """
    @overload
    def VerifyHash(
        self,
        hash: Array[int],
        signature: Array[int],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> bool:
        """

        :param hash:
        :param signature:
        :param hashAlgorithm:
        :param padding:
        :return:
        """

class RSACspObject(Object):
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

class RSAEncryptionPadding(Object, IEquatable[RSAEncryptionPadding]):
    """"""

    @property
    def Mode(self) -> RSAEncryptionPaddingMode:
        """

        :return:
        """
    @property
    def OaepHashAlgorithm(self) -> HashAlgorithmName:
        """

        :return:
        """
    @classmethod
    @property
    def OaepSHA1(cls) -> RSAEncryptionPadding:
        """

        :return:
        """
    @classmethod
    @property
    def OaepSHA256(cls) -> RSAEncryptionPadding:
        """

        :return:
        """
    @classmethod
    @property
    def OaepSHA384(cls) -> RSAEncryptionPadding:
        """

        :return:
        """
    @classmethod
    @property
    def OaepSHA512(cls) -> RSAEncryptionPadding:
        """

        :return:
        """
    @classmethod
    @property
    def Pkcs1(cls) -> RSAEncryptionPadding:
        """

        :return:
        """
    @classmethod
    def CreateOaep(cls, hashAlgorithm: HashAlgorithmName) -> RSAEncryptionPadding:
        """

        :param hashAlgorithm:
        :return:
        """
    @overload
    def Equals(self, other: RSAEncryptionPadding) -> bool:
        """

        :param other:
        :return:
        """
    @overload
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
    def __eq__(self, other: RSAEncryptionPadding) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: RSAEncryptionPadding) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: RSAEncryptionPadding, right: RSAEncryptionPadding) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: RSAEncryptionPadding, right: RSAEncryptionPadding) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

class RSAEncryptionPaddingMode(Enum):
    """"""

    Pkcs1: RSAEncryptionPaddingMode = ...
    """"""
    Oaep: RSAEncryptionPaddingMode = ...
    """"""

class RSAOAEPKeyExchangeDeformatter(AsymmetricKeyExchangeDeformatter):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, key: AsymmetricAlgorithm):
        """

        :param key:
        """
    @property
    def Parameters(self) -> str:
        """

        :return:
        """
    @Parameters.setter
    def Parameters(self, value: str) -> None: ...
    def DecryptKeyExchange(self, rgb: Array[int]) -> Array[int]:
        """

        :param rgb:
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
    def SetKey(self, key: AsymmetricAlgorithm) -> None:
        """

        :param key:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class RSAOAEPKeyExchangeFormatter(AsymmetricKeyExchangeFormatter):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, key: AsymmetricAlgorithm):
        """

        :param key:
        """
    @property
    def Parameter(self) -> Array[int]:
        """

        :return:
        """
    @Parameter.setter
    def Parameter(self, value: Array[int]) -> None: ...
    @property
    def Parameters(self) -> str:
        """

        :return:
        """
    @property
    def Rng(self) -> RandomNumberGenerator:
        """

        :return:
        """
    @Rng.setter
    def Rng(self, value: RandomNumberGenerator) -> None: ...
    @overload
    def CreateKeyExchange(self, data: Array[int]) -> Array[int]:
        """

        :param data:
        :return:
        """
    @overload
    def CreateKeyExchange(self, data: Array[int], symAlgType: Type) -> Array[int]:
        """

        :param data:
        :param symAlgType:
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
    def SetKey(self, key: AsymmetricAlgorithm) -> None:
        """

        :param key:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class RSAPKCS1KeyExchangeDeformatter(AsymmetricKeyExchangeDeformatter):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, key: AsymmetricAlgorithm):
        """

        :param key:
        """
    @property
    def Parameters(self) -> str:
        """

        :return:
        """
    @Parameters.setter
    def Parameters(self, value: str) -> None: ...
    @property
    def RNG(self) -> RandomNumberGenerator:
        """

        :return:
        """
    @RNG.setter
    def RNG(self, value: RandomNumberGenerator) -> None: ...
    def DecryptKeyExchange(self, rgb: Array[int]) -> Array[int]:
        """

        :param rgb:
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
    def SetKey(self, key: AsymmetricAlgorithm) -> None:
        """

        :param key:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class RSAPKCS1KeyExchangeFormatter(AsymmetricKeyExchangeFormatter):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, key: AsymmetricAlgorithm):
        """

        :param key:
        """
    @property
    def Parameters(self) -> str:
        """

        :return:
        """
    @property
    def Rng(self) -> RandomNumberGenerator:
        """

        :return:
        """
    @Rng.setter
    def Rng(self, value: RandomNumberGenerator) -> None: ...
    @overload
    def CreateKeyExchange(self, data: Array[int]) -> Array[int]:
        """

        :param data:
        :return:
        """
    @overload
    def CreateKeyExchange(self, data: Array[int], symAlgType: Type) -> Array[int]:
        """

        :param data:
        :param symAlgType:
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
    def SetKey(self, key: AsymmetricAlgorithm) -> None:
        """

        :param key:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class RSAPKCS1SHA1SignatureDescription(RSAPKCS1SignatureDescription):
    """"""

    def __init__(self):
        """"""
    @property
    def DeformatterAlgorithm(self) -> str:
        """

        :return:
        """
    @DeformatterAlgorithm.setter
    def DeformatterAlgorithm(self, value: str) -> None: ...
    @property
    def DigestAlgorithm(self) -> str:
        """

        :return:
        """
    @DigestAlgorithm.setter
    def DigestAlgorithm(self, value: str) -> None: ...
    @property
    def FormatterAlgorithm(self) -> str:
        """

        :return:
        """
    @FormatterAlgorithm.setter
    def FormatterAlgorithm(self, value: str) -> None: ...
    @property
    def KeyAlgorithm(self) -> str:
        """

        :return:
        """
    @KeyAlgorithm.setter
    def KeyAlgorithm(self, value: str) -> None: ...
    def CreateDeformatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureDeformatter:
        """

        :param key:
        :return:
        """
    def CreateDigest(self) -> HashAlgorithm:
        """

        :return:
        """
    def CreateFormatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureFormatter:
        """

        :param key:
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

class RSAPKCS1SHA256SignatureDescription(RSAPKCS1SignatureDescription):
    """"""

    def __init__(self):
        """"""
    @property
    def DeformatterAlgorithm(self) -> str:
        """

        :return:
        """
    @DeformatterAlgorithm.setter
    def DeformatterAlgorithm(self, value: str) -> None: ...
    @property
    def DigestAlgorithm(self) -> str:
        """

        :return:
        """
    @DigestAlgorithm.setter
    def DigestAlgorithm(self, value: str) -> None: ...
    @property
    def FormatterAlgorithm(self) -> str:
        """

        :return:
        """
    @FormatterAlgorithm.setter
    def FormatterAlgorithm(self, value: str) -> None: ...
    @property
    def KeyAlgorithm(self) -> str:
        """

        :return:
        """
    @KeyAlgorithm.setter
    def KeyAlgorithm(self, value: str) -> None: ...
    def CreateDeformatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureDeformatter:
        """

        :param key:
        :return:
        """
    def CreateDigest(self) -> HashAlgorithm:
        """

        :return:
        """
    def CreateFormatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureFormatter:
        """

        :param key:
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

class RSAPKCS1SHA384SignatureDescription(RSAPKCS1SignatureDescription):
    """"""

    def __init__(self):
        """"""
    @property
    def DeformatterAlgorithm(self) -> str:
        """

        :return:
        """
    @DeformatterAlgorithm.setter
    def DeformatterAlgorithm(self, value: str) -> None: ...
    @property
    def DigestAlgorithm(self) -> str:
        """

        :return:
        """
    @DigestAlgorithm.setter
    def DigestAlgorithm(self, value: str) -> None: ...
    @property
    def FormatterAlgorithm(self) -> str:
        """

        :return:
        """
    @FormatterAlgorithm.setter
    def FormatterAlgorithm(self, value: str) -> None: ...
    @property
    def KeyAlgorithm(self) -> str:
        """

        :return:
        """
    @KeyAlgorithm.setter
    def KeyAlgorithm(self, value: str) -> None: ...
    def CreateDeformatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureDeformatter:
        """

        :param key:
        :return:
        """
    def CreateDigest(self) -> HashAlgorithm:
        """

        :return:
        """
    def CreateFormatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureFormatter:
        """

        :param key:
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

class RSAPKCS1SHA512SignatureDescription(RSAPKCS1SignatureDescription):
    """"""

    def __init__(self):
        """"""
    @property
    def DeformatterAlgorithm(self) -> str:
        """

        :return:
        """
    @DeformatterAlgorithm.setter
    def DeformatterAlgorithm(self, value: str) -> None: ...
    @property
    def DigestAlgorithm(self) -> str:
        """

        :return:
        """
    @DigestAlgorithm.setter
    def DigestAlgorithm(self, value: str) -> None: ...
    @property
    def FormatterAlgorithm(self) -> str:
        """

        :return:
        """
    @FormatterAlgorithm.setter
    def FormatterAlgorithm(self, value: str) -> None: ...
    @property
    def KeyAlgorithm(self) -> str:
        """

        :return:
        """
    @KeyAlgorithm.setter
    def KeyAlgorithm(self, value: str) -> None: ...
    def CreateDeformatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureDeformatter:
        """

        :param key:
        :return:
        """
    def CreateDigest(self) -> HashAlgorithm:
        """

        :return:
        """
    def CreateFormatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureFormatter:
        """

        :param key:
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

class RSAPKCS1SignatureDeformatter(AsymmetricSignatureDeformatter):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, key: AsymmetricAlgorithm):
        """

        :param key:
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
    def SetHashAlgorithm(self, strName: str) -> None:
        """

        :param strName:
        """
    def SetKey(self, key: AsymmetricAlgorithm) -> None:
        """

        :param key:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def VerifySignature(self, hash: HashAlgorithm, rgbSignature: Array[int]) -> bool:
        """

        :param hash:
        :param rgbSignature:
        :return:
        """
    @overload
    def VerifySignature(self, rgbHash: Array[int], rgbSignature: Array[int]) -> bool:
        """

        :param rgbHash:
        :param rgbSignature:
        :return:
        """

class RSAPKCS1SignatureDescription(ABC, SignatureDescription):
    """"""

    @property
    def DeformatterAlgorithm(self) -> str:
        """

        :return:
        """
    @DeformatterAlgorithm.setter
    def DeformatterAlgorithm(self, value: str) -> None: ...
    @property
    def DigestAlgorithm(self) -> str:
        """

        :return:
        """
    @DigestAlgorithm.setter
    def DigestAlgorithm(self, value: str) -> None: ...
    @property
    def FormatterAlgorithm(self) -> str:
        """

        :return:
        """
    @FormatterAlgorithm.setter
    def FormatterAlgorithm(self, value: str) -> None: ...
    @property
    def KeyAlgorithm(self) -> str:
        """

        :return:
        """
    @KeyAlgorithm.setter
    def KeyAlgorithm(self, value: str) -> None: ...
    def CreateDeformatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureDeformatter:
        """

        :param key:
        :return:
        """
    def CreateDigest(self) -> HashAlgorithm:
        """

        :return:
        """
    def CreateFormatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureFormatter:
        """

        :param key:
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

class RSAPKCS1SignatureFormatter(AsymmetricSignatureFormatter):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, key: AsymmetricAlgorithm):
        """

        :param key:
        """
    @overload
    def CreateSignature(self, hash: HashAlgorithm) -> Array[int]:
        """

        :param hash:
        :return:
        """
    @overload
    def CreateSignature(self, rgbHash: Array[int]) -> Array[int]:
        """

        :param rgbHash:
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
    def SetHashAlgorithm(self, strName: str) -> None:
        """

        :param strName:
        """
    def SetKey(self, key: AsymmetricAlgorithm) -> None:
        """

        :param key:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class RSAParameters(ValueType):
    """"""

    D: Final[Array[int]] = ...
    """
    
    :return: 
    """
    DP: Final[Array[int]] = ...
    """
    
    :return: 
    """
    DQ: Final[Array[int]] = ...
    """
    
    :return: 
    """
    Exponent: Final[Array[int]] = ...
    """
    
    :return: 
    """
    InverseQ: Final[Array[int]] = ...
    """
    
    :return: 
    """
    Modulus: Final[Array[int]] = ...
    """
    
    :return: 
    """
    P: Final[Array[int]] = ...
    """
    
    :return: 
    """
    Q: Final[Array[int]] = ...
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

class RSASignaturePadding(Object, IEquatable[RSASignaturePadding]):
    """"""

    @property
    def Mode(self) -> RSASignaturePaddingMode:
        """

        :return:
        """
    @classmethod
    @property
    def Pkcs1(cls) -> RSASignaturePadding:
        """

        :return:
        """
    @classmethod
    @property
    def Pss(cls) -> RSASignaturePadding:
        """

        :return:
        """
    @overload
    def Equals(self, other: RSASignaturePadding) -> bool:
        """

        :param other:
        :return:
        """
    @overload
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
    def __eq__(self, other: RSASignaturePadding) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: RSASignaturePadding) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: RSASignaturePadding, right: RSASignaturePadding) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: RSASignaturePadding, right: RSASignaturePadding) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

class RSASignaturePaddingMode(Enum):
    """"""

    Pkcs1: RSASignaturePaddingMode = ...
    """"""
    Pss: RSASignaturePaddingMode = ...
    """"""

class RandomNumberGenerator(ABC, Object, IDisposable):
    """"""

    @classmethod
    @overload
    def Create(cls) -> RandomNumberGenerator:
        """

        :return:
        """
    @classmethod
    @overload
    def Create(cls, rngName: str) -> RandomNumberGenerator:
        """

        :param rngName:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetBytes(self, data: Array[int]) -> None:
        """

        :param data:
        """
    @overload
    def GetBytes(self, data: Array[int], offset: int, count: int) -> None:
        """

        :param data:
        :param offset:
        :param count:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetNonZeroBytes(self, data: Array[int]) -> None:
        """

        :param data:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class Rfc2898DeriveBytes(DeriveBytes, IDisposable):
    """"""

    @overload
    def __init__(self, password: str, salt: Array[int]):
        """

        :param password:
        :param salt:
        """
    @overload
    def __init__(self, password: str, saltSize: int):
        """

        :param password:
        :param saltSize:
        """
    @overload
    def __init__(self, password: Array[int], salt: Array[int], iterations: int):
        """

        :param password:
        :param salt:
        :param iterations:
        """
    @overload
    def __init__(self, password: str, salt: Array[int], iterations: int):
        """

        :param password:
        :param salt:
        :param iterations:
        """
    @overload
    def __init__(self, password: str, saltSize: int, iterations: int):
        """

        :param password:
        :param saltSize:
        :param iterations:
        """
    @overload
    def __init__(
        self,
        password: Array[int],
        salt: Array[int],
        iterations: int,
        hashAlgorithm: HashAlgorithmName,
    ):
        """

        :param password:
        :param salt:
        :param iterations:
        :param hashAlgorithm:
        """
    @overload
    def __init__(
        self, password: str, salt: Array[int], iterations: int, hashAlgorithm: HashAlgorithmName
    ):
        """

        :param password:
        :param salt:
        :param iterations:
        :param hashAlgorithm:
        """
    @overload
    def __init__(
        self, password: str, saltSize: int, iterations: int, hashAlgorithm: HashAlgorithmName
    ):
        """

        :param password:
        :param saltSize:
        :param iterations:
        :param hashAlgorithm:
        """
    @property
    def IterationCount(self) -> int:
        """

        :return:
        """
    @IterationCount.setter
    def IterationCount(self, value: int) -> None: ...
    @property
    def Salt(self) -> Array[int]:
        """

        :return:
        """
    @Salt.setter
    def Salt(self, value: Array[int]) -> None: ...
    def CryptDeriveKey(
        self, algname: str, alghashname: str, keySize: int, rgbIV: Array[int]
    ) -> Array[int]:
        """

        :param algname:
        :param alghashname:
        :param keySize:
        :param rgbIV:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetBytes(self, cb: int) -> Array[int]:
        """

        :param cb:
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
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class Rfc4050KeyFormatter(ABC, Object):
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

class Rijndael(ABC, SymmetricAlgorithm, IDisposable):
    """"""

    @property
    def BlockSize(self) -> int:
        """

        :return:
        """
    @BlockSize.setter
    def BlockSize(self, value: int) -> None: ...
    @property
    def FeedbackSize(self) -> int:
        """

        :return:
        """
    @FeedbackSize.setter
    def FeedbackSize(self, value: int) -> None: ...
    @property
    def IV(self) -> Array[int]:
        """

        :return:
        """
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def Key(self) -> Array[int]:
        """

        :return:
        """
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def KeySize(self) -> int:
        """

        :return:
        """
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalBlockSizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def Mode(self) -> CipherMode:
        """

        :return:
        """
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    @property
    def Padding(self) -> PaddingMode:
        """

        :return:
        """
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    def Clear(self) -> None:
        """"""
    @classmethod
    @overload
    def Create(cls) -> Rijndael:
        """

        :return:
        """
    @classmethod
    @overload
    def Create(cls, algName: str) -> Rijndael:
        """

        :param algName:
        :return:
        """
    @overload
    def CreateDecryptor(self) -> ICryptoTransform:
        """

        :return:
        """
    @overload
    def CreateDecryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """

        :param rgbKey:
        :param rgbIV:
        :return:
        """
    @overload
    def CreateEncryptor(self) -> ICryptoTransform:
        """

        :return:
        """
    @overload
    def CreateEncryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """

        :param rgbKey:
        :param rgbIV:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GenerateIV(self) -> None:
        """"""
    def GenerateKey(self) -> None:
        """"""
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
    def ValidKeySize(self, bitLength: int) -> bool:
        """

        :param bitLength:
        :return:
        """

class RijndaelManaged(Rijndael, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def BlockSize(self) -> int:
        """

        :return:
        """
    @BlockSize.setter
    def BlockSize(self, value: int) -> None: ...
    @property
    def FeedbackSize(self) -> int:
        """

        :return:
        """
    @FeedbackSize.setter
    def FeedbackSize(self, value: int) -> None: ...
    @property
    def IV(self) -> Array[int]:
        """

        :return:
        """
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def Key(self) -> Array[int]:
        """

        :return:
        """
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def KeySize(self) -> int:
        """

        :return:
        """
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalBlockSizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def Mode(self) -> CipherMode:
        """

        :return:
        """
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    @property
    def Padding(self) -> PaddingMode:
        """

        :return:
        """
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    def Clear(self) -> None:
        """"""
    @overload
    def CreateDecryptor(self) -> ICryptoTransform:
        """

        :return:
        """
    @overload
    def CreateDecryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """

        :param rgbKey:
        :param rgbIV:
        :return:
        """
    @overload
    def CreateEncryptor(self) -> ICryptoTransform:
        """

        :return:
        """
    @overload
    def CreateEncryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """

        :param rgbKey:
        :param rgbIV:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GenerateIV(self) -> None:
        """"""
    def GenerateKey(self) -> None:
        """"""
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
    def ValidKeySize(self, bitLength: int) -> bool:
        """

        :param bitLength:
        :return:
        """

class RijndaelManagedTransform(Object, ICryptoTransform, IDisposable):
    """"""

    @property
    def BlockSizeValue(self) -> int:
        """

        :return:
        """
    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
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
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class RijndaelManagedTransformMode(Enum):
    """"""

    Encrypt: RijndaelManagedTransformMode = ...
    """"""
    Decrypt: RijndaelManagedTransformMode = ...
    """"""

class SHA1(ABC, HashAlgorithm, ICryptoTransform, IDisposable):
    """"""

    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def Hash(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HashSize(self) -> int:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @classmethod
    @overload
    def Create(cls) -> SHA1:
        """

        :return:
        """
    @classmethod
    @overload
    def Create(cls, hashName: str) -> SHA1:
        """

        :param hashName:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class SHA1Cng(SHA1, ICryptoTransform, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def Hash(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HashSize(self) -> int:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class SHA1CryptoServiceProvider(SHA1, ICryptoTransform, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def Hash(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HashSize(self) -> int:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class SHA1Managed(SHA1, ICryptoTransform, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def Hash(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HashSize(self) -> int:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class SHA256(ABC, HashAlgorithm, ICryptoTransform, IDisposable):
    """"""

    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def Hash(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HashSize(self) -> int:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @classmethod
    @overload
    def Create(cls) -> SHA256:
        """

        :return:
        """
    @classmethod
    @overload
    def Create(cls, hashName: str) -> SHA256:
        """

        :param hashName:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class SHA256Cng(SHA256, ICryptoTransform, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def Hash(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HashSize(self) -> int:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class SHA256CryptoServiceProvider(SHA256, ICryptoTransform, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def Hash(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HashSize(self) -> int:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class SHA256Managed(SHA256, ICryptoTransform, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def Hash(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HashSize(self) -> int:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class SHA384(ABC, HashAlgorithm, ICryptoTransform, IDisposable):
    """"""

    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def Hash(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HashSize(self) -> int:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @classmethod
    @overload
    def Create(cls) -> SHA384:
        """

        :return:
        """
    @classmethod
    @overload
    def Create(cls, hashName: str) -> SHA384:
        """

        :param hashName:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class SHA384Cng(SHA384, ICryptoTransform, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def Hash(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HashSize(self) -> int:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class SHA384CryptoServiceProvider(SHA384, ICryptoTransform, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def Hash(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HashSize(self) -> int:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class SHA384Managed(SHA384, ICryptoTransform, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def Hash(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HashSize(self) -> int:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class SHA512(ABC, HashAlgorithm, ICryptoTransform, IDisposable):
    """"""

    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def Hash(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HashSize(self) -> int:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @classmethod
    @overload
    def Create(cls) -> SHA512:
        """

        :return:
        """
    @classmethod
    @overload
    def Create(cls, hashName: str) -> SHA512:
        """

        :param hashName:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class SHA512Cng(SHA512, ICryptoTransform, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def Hash(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HashSize(self) -> int:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class SHA512CryptoServiceProvider(SHA512, ICryptoTransform, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def Hash(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HashSize(self) -> int:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class SHA512Managed(SHA512, ICryptoTransform, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def Hash(self) -> Array[int]:
        """

        :return:
        """
    @property
    def HashSize(self) -> int:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def ComputeHash(self, inputStream: Stream) -> Array[int]:
        """

        :param inputStream:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int]) -> Array[int]:
        """

        :param buffer:
        :return:
        """
    @overload
    def ComputeHash(self, buffer: Array[int], offset: int, count: int) -> Array[int]:
        """

        :param buffer:
        :param offset:
        :param count:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class SafeCertContextHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

class SafeCertStoreHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

class SafeCryptMsgHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

class SafeCryptProvHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

class SafeCspHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

class SafeCspHashHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

class SafeCspKeyHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

class SafeHashHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

class SafeKeyHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

class SafeLibraryHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

class SafeLocalAllocHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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
    def SetHandleAsInvalid(self) -> None:
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
    def ToString(self) -> str:
        """

        :return:
        """

class SafeProvHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

class SignatureDescription(Object):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, el: SecurityElement):
        """

        :param el:
        """
    @property
    def DeformatterAlgorithm(self) -> str:
        """

        :return:
        """
    @DeformatterAlgorithm.setter
    def DeformatterAlgorithm(self, value: str) -> None: ...
    @property
    def DigestAlgorithm(self) -> str:
        """

        :return:
        """
    @DigestAlgorithm.setter
    def DigestAlgorithm(self, value: str) -> None: ...
    @property
    def FormatterAlgorithm(self) -> str:
        """

        :return:
        """
    @FormatterAlgorithm.setter
    def FormatterAlgorithm(self, value: str) -> None: ...
    @property
    def KeyAlgorithm(self) -> str:
        """

        :return:
        """
    @KeyAlgorithm.setter
    def KeyAlgorithm(self, value: str) -> None: ...
    def CreateDeformatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureDeformatter:
        """

        :param key:
        :return:
        """
    def CreateDigest(self) -> HashAlgorithm:
        """

        :return:
        """
    def CreateFormatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureFormatter:
        """

        :param key:
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

class StrongNameSignatureInformation(Object):
    """"""

    @property
    def HResult(self) -> int:
        """

        :return:
        """
    @property
    def HashAlgorithm(self) -> str:
        """

        :return:
        """
    @property
    def IsValid(self) -> bool:
        """

        :return:
        """
    @property
    def PublicKey(self) -> AsymmetricAlgorithm:
        """

        :return:
        """
    @property
    def VerificationResult(self) -> SignatureVerificationResult:
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

class SymmetricAlgorithm(ABC, Object, IDisposable):
    """"""

    @property
    def BlockSize(self) -> int:
        """

        :return:
        """
    @BlockSize.setter
    def BlockSize(self, value: int) -> None: ...
    @property
    def FeedbackSize(self) -> int:
        """

        :return:
        """
    @FeedbackSize.setter
    def FeedbackSize(self, value: int) -> None: ...
    @property
    def IV(self) -> Array[int]:
        """

        :return:
        """
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def Key(self) -> Array[int]:
        """

        :return:
        """
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def KeySize(self) -> int:
        """

        :return:
        """
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalBlockSizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def Mode(self) -> CipherMode:
        """

        :return:
        """
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    @property
    def Padding(self) -> PaddingMode:
        """

        :return:
        """
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    def Clear(self) -> None:
        """"""
    @classmethod
    @overload
    def Create(cls) -> SymmetricAlgorithm:
        """

        :return:
        """
    @classmethod
    @overload
    def Create(cls, algName: str) -> SymmetricAlgorithm:
        """

        :param algName:
        :return:
        """
    @overload
    def CreateDecryptor(self) -> ICryptoTransform:
        """

        :return:
        """
    @overload
    def CreateDecryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """

        :param rgbKey:
        :param rgbIV:
        :return:
        """
    @overload
    def CreateEncryptor(self) -> ICryptoTransform:
        """

        :return:
        """
    @overload
    def CreateEncryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """

        :param rgbKey:
        :param rgbIV:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GenerateIV(self) -> None:
        """"""
    def GenerateKey(self) -> None:
        """"""
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
    def ValidKeySize(self, bitLength: int) -> bool:
        """

        :param bitLength:
        :return:
        """

class TailStream(Stream, IDisposable):
    """"""

    def __init__(self, bufferSize: int):
        """

        :param bufferSize:
        """
    @property
    def Buffer(self) -> Array[int]:
        """

        :return:
        """
    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanSeek(self) -> bool:
        """

        :return:
        """
    @property
    def CanTimeout(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def ReadTimeout(self) -> int:
        """

        :return:
        """
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @property
    def WriteTimeout(self) -> int:
        """

        :return:
        """
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def BeginRead(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def BeginWrite(
        self, buffer: Array[int], offset: int, count: int, callback: AsyncCallback, state: object
    ) -> IAsyncResult:
        """

        :param buffer:
        :param offset:
        :param count:
        :param callback:
        :param state:
        :return:
        """
    def Clear(self) -> None:
        """"""
    def Close(self) -> None:
        """"""
    @overload
    def CopyTo(self, destination: Stream) -> None:
        """

        :param destination:
        """
    @overload
    def CopyTo(self, destination: Stream, bufferSize: int) -> None:
        """

        :param destination:
        :param bufferSize:
        """
    @overload
    def CopyToAsync(self, destination: Stream) -> Task:
        """

        :param destination:
        :return:
        """
    @overload
    def CopyToAsync(self, destination: Stream, bufferSize: int) -> Task:
        """

        :param destination:
        :param bufferSize:
        :return:
        """
    @overload
    def CopyToAsync(
        self, destination: Stream, bufferSize: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param destination:
        :param bufferSize:
        :param cancellationToken:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def EndRead(self, asyncResult: IAsyncResult) -> int:
        """

        :param asyncResult:
        :return:
        """
    def EndWrite(self, asyncResult: IAsyncResult) -> None:
        """

        :param asyncResult:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    @overload
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task:
        """

        :param cancellationToken:
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
    def Read(self, buffer: Array[int], offset: int, count: int) -> Tuple[int, Array[int]]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(self, buffer: Array[int], offset: int, count: int) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def ReadAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task[int]:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    def Seek(self, offset: int, origin: SeekOrigin) -> int:
        """

        :param offset:
        :param origin:
        :return:
        """
    def SetLength(self, value: int) -> None:
        """

        :param value:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def Write(self, buffer: Array[int], offset: int, count: int) -> None:
        """

        :param buffer:
        :param offset:
        :param count:
        """
    @overload
    def WriteAsync(self, buffer: Array[int], offset: int, count: int) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :return:
        """
    @overload
    def WriteAsync(
        self, buffer: Array[int], offset: int, count: int, cancellationToken: CancellationToken
    ) -> Task:
        """

        :param buffer:
        :param offset:
        :param count:
        :param cancellationToken:
        :return:
        """
    def WriteByte(self, value: int) -> None:
        """

        :param value:
        """

class ToBase64Transform(Object, ICryptoTransform, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def CanReuseTransform(self) -> bool:
        """

        :return:
        """
    @property
    def CanTransformMultipleBlocks(self) -> bool:
        """

        :return:
        """
    @property
    def InputBlockSize(self) -> int:
        """

        :return:
        """
    @property
    def OutputBlockSize(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
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
    def ToString(self) -> str:
        """

        :return:
        """
    def TransformBlock(
        self,
        inputBuffer: Array[int],
        inputOffset: int,
        inputCount: int,
        outputBuffer: Array[int],
        outputOffset: int,
    ) -> int:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :param outputBuffer:
        :param outputOffset:
        :return:
        """
    def TransformFinalBlock(
        self, inputBuffer: Array[int], inputOffset: int, inputCount: int
    ) -> Array[int]:
        """

        :param inputBuffer:
        :param inputOffset:
        :param inputCount:
        :return:
        """

class TripleDES(ABC, SymmetricAlgorithm, IDisposable):
    """"""

    @property
    def BlockSize(self) -> int:
        """

        :return:
        """
    @BlockSize.setter
    def BlockSize(self, value: int) -> None: ...
    @property
    def FeedbackSize(self) -> int:
        """

        :return:
        """
    @FeedbackSize.setter
    def FeedbackSize(self, value: int) -> None: ...
    @property
    def IV(self) -> Array[int]:
        """

        :return:
        """
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def Key(self) -> Array[int]:
        """

        :return:
        """
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def KeySize(self) -> int:
        """

        :return:
        """
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalBlockSizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def Mode(self) -> CipherMode:
        """

        :return:
        """
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    @property
    def Padding(self) -> PaddingMode:
        """

        :return:
        """
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    def Clear(self) -> None:
        """"""
    @classmethod
    @overload
    def Create(cls) -> TripleDES:
        """

        :return:
        """
    @classmethod
    @overload
    def Create(cls, str: str) -> TripleDES:
        """

        :param str:
        :return:
        """
    @overload
    def CreateDecryptor(self) -> ICryptoTransform:
        """

        :return:
        """
    @overload
    def CreateDecryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """

        :param rgbKey:
        :param rgbIV:
        :return:
        """
    @overload
    def CreateEncryptor(self) -> ICryptoTransform:
        """

        :return:
        """
    @overload
    def CreateEncryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """

        :param rgbKey:
        :param rgbIV:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GenerateIV(self) -> None:
        """"""
    def GenerateKey(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def IsWeakKey(cls, rgbKey: Array[int]) -> bool:
        """

        :param rgbKey:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def ValidKeySize(self, bitLength: int) -> bool:
        """

        :param bitLength:
        :return:
        """

class TripleDESCng(TripleDES, ICngSymmetricAlgorithm, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, keyName: str):
        """

        :param keyName:
        """
    @overload
    def __init__(self, keyName: str, provider: CngProvider):
        """

        :param keyName:
        :param provider:
        """
    @overload
    def __init__(self, keyName: str, provider: CngProvider, openOptions: CngKeyOpenOptions):
        """

        :param keyName:
        :param provider:
        :param openOptions:
        """
    @property
    def BaseKey(self) -> Array[int]:
        """

        :return:
        """
    @BaseKey.setter
    def BaseKey(self, value: Array[int]) -> None: ...
    @property
    def BaseKeySize(self) -> int:
        """

        :return:
        """
    @BaseKeySize.setter
    def BaseKeySize(self, value: int) -> None: ...
    @property
    def BlockSize(self) -> int:
        """

        :return:
        """
    @property
    def BlockSize(self) -> int:
        """

        :return:
        """
    @BlockSize.setter
    def BlockSize(self, value: int) -> None: ...
    @property
    def FeedbackSize(self) -> int:
        """

        :return:
        """
    @FeedbackSize.setter
    def FeedbackSize(self, value: int) -> None: ...
    @property
    def IV(self) -> Array[int]:
        """

        :return:
        """
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def IV(self) -> Array[int]:
        """

        :return:
        """
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def Key(self) -> Array[int]:
        """

        :return:
        """
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def KeySize(self) -> int:
        """

        :return:
        """
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalBlockSizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def Mode(self) -> CipherMode:
        """

        :return:
        """
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    @property
    def Mode(self) -> CipherMode:
        """

        :return:
        """
    @property
    def Padding(self) -> PaddingMode:
        """

        :return:
        """
    @property
    def Padding(self) -> PaddingMode:
        """

        :return:
        """
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    def Clear(self) -> None:
        """"""
    @overload
    def CreateDecryptor(self) -> ICryptoTransform:
        """

        :return:
        """
    @overload
    def CreateDecryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """

        :param rgbKey:
        :param rgbIV:
        :return:
        """
    @overload
    def CreateEncryptor(self) -> ICryptoTransform:
        """

        :return:
        """
    @overload
    def CreateEncryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """

        :param rgbKey:
        :param rgbIV:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GenerateIV(self) -> None:
        """"""
    def GenerateKey(self) -> None:
        """"""
    def GetEphemeralModeHandle(self) -> SafeBCryptAlgorithmHandle:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetNCryptAlgorithmIdentifier(self) -> str:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def IsWeakKey(self, key: Array[int]) -> bool:
        """

        :param key:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def ValidKeySize(self, bitLength: int) -> bool:
        """

        :param bitLength:
        :return:
        """

class TripleDESCryptoServiceProvider(TripleDES, IDisposable):
    """"""

    def __init__(self):
        """"""
    @property
    def BlockSize(self) -> int:
        """

        :return:
        """
    @BlockSize.setter
    def BlockSize(self, value: int) -> None: ...
    @property
    def FeedbackSize(self) -> int:
        """

        :return:
        """
    @FeedbackSize.setter
    def FeedbackSize(self, value: int) -> None: ...
    @property
    def IV(self) -> Array[int]:
        """

        :return:
        """
    @IV.setter
    def IV(self, value: Array[int]) -> None: ...
    @property
    def Key(self) -> Array[int]:
        """

        :return:
        """
    @Key.setter
    def Key(self, value: Array[int]) -> None: ...
    @property
    def KeySize(self) -> int:
        """

        :return:
        """
    @KeySize.setter
    def KeySize(self, value: int) -> None: ...
    @property
    def LegalBlockSizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def LegalKeySizes(self) -> Array[KeySizes]:
        """

        :return:
        """
    @property
    def Mode(self) -> CipherMode:
        """

        :return:
        """
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    @property
    def Padding(self) -> PaddingMode:
        """

        :return:
        """
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    def Clear(self) -> None:
        """"""
    @overload
    def CreateDecryptor(self) -> ICryptoTransform:
        """

        :return:
        """
    @overload
    def CreateDecryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """

        :param rgbKey:
        :param rgbIV:
        :return:
        """
    @overload
    def CreateEncryptor(self) -> ICryptoTransform:
        """

        :return:
        """
    @overload
    def CreateEncryptor(self, rgbKey: Array[int], rgbIV: Array[int]) -> ICryptoTransform:
        """

        :param rgbKey:
        :param rgbIV:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GenerateIV(self) -> None:
        """"""
    def GenerateKey(self) -> None:
        """"""
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
    def ValidKeySize(self, bitLength: int) -> bool:
        """

        :param bitLength:
        :return:
        """

class Utils(ABC, Object):
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

class X509Utils(Object):
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
