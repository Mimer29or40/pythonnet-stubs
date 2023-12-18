from __future__ import annotations

from abc import ABC
from typing import List
from typing import Optional
from typing import Protocol
from typing import Tuple
from typing import Union
from typing import overload

from Internal.Cryptography import ICngSymmetricAlgorithm
from Microsoft.Win32.SafeHandles import SafeBCryptAlgorithmHandle
from Microsoft.Win32.SafeHandles import SafeBCryptKeyHandle
from Microsoft.Win32.SafeHandles import SafeCapiKeyHandle
from Microsoft.Win32.SafeHandles import SafeHandleZeroOrMinusOneIsInvalid
from Microsoft.Win32.SafeHandles import SafeNCryptKeyHandle
from Microsoft.Win32.SafeHandles import SafeNCryptProviderHandle
from Microsoft.Win32.SafeHandles import SafeNCryptSecretHandle
from System import ActivationContext
from System import Array
from System import Boolean
from System import Byte
from System import Enum
from System import Exception
from System import IDisposable
from System import IEquatable
from System import Int32
from System import Int64
from System import IntPtr
from System import Nullable
from System import Object
from System import String
from System import SystemException
from System import Type
from System import ValueType
from System import Void
from System.Collections import ICollection
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
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import ISerializable
from System.Security import ManifestKinds
from System.Security import SecureString
from System.Security import SecurityElement
from System.Security.AccessControl import CryptoKeySecurity
from System.Security.Cryptography.X509Certificates import AuthenticodeSignatureInformation
from System.Security.Cryptography.X509Certificates import X509RevocationFlag
from System.Security.Cryptography.X509Certificates import X509RevocationMode
from System.Threading import CancellationToken
from System.Threading.Tasks import Task

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
NullableType = Union[Optional, Nullable]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class Aes(ABC, SymmetricAlgorithm, IDisposable):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    @overload
    def Create(algorithmName: StringType) -> Aes: ...
    @staticmethod
    @overload
    def Create() -> Aes: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class AesCng(Aes, IDisposable, ICngSymmetricAlgorithm):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, keyName: StringType): ...
    @overload
    def __init__(self, keyName: StringType, provider: CngProvider): ...
    @overload
    def __init__(
        self, keyName: StringType, provider: CngProvider, openOptions: CngKeyOpenOptions
    ): ...

    # ---------- Properties ---------- #

    @property
    def Key(self) -> ArrayType[ByteType]: ...
    @Key.setter
    def Key(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def KeySize(self) -> IntType: ...
    @KeySize.setter
    def KeySize(self, value: IntType) -> None: ...

    # ---------- Methods ---------- #

    @overload
    def CreateDecryptor(self) -> ICryptoTransform: ...
    @overload
    def CreateDecryptor(
        self, rgbKey: ArrayType[ByteType], rgbIV: ArrayType[ByteType]
    ) -> ICryptoTransform: ...
    @overload
    def CreateEncryptor(self) -> ICryptoTransform: ...
    @overload
    def CreateEncryptor(
        self, rgbKey: ArrayType[ByteType], rgbIV: ArrayType[ByteType]
    ) -> ICryptoTransform: ...
    def GenerateIV(self) -> VoidType: ...
    def GenerateKey(self) -> VoidType: ...
    def get_Key(self) -> ArrayType[ByteType]: ...
    def get_KeySize(self) -> IntType: ...
    def set_Key(self, value: ArrayType[ByteType]) -> VoidType: ...
    def set_KeySize(self, value: IntType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class AesCryptoServiceProvider(Aes, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def Key(self) -> ArrayType[ByteType]: ...
    @Key.setter
    def Key(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def KeySize(self) -> IntType: ...
    @KeySize.setter
    def KeySize(self, value: IntType) -> None: ...

    # ---------- Methods ---------- #

    @overload
    def CreateDecryptor(self) -> ICryptoTransform: ...
    @overload
    def CreateDecryptor(
        self, key: ArrayType[ByteType], iv: ArrayType[ByteType]
    ) -> ICryptoTransform: ...
    @overload
    def CreateEncryptor(self) -> ICryptoTransform: ...
    @overload
    def CreateEncryptor(
        self, key: ArrayType[ByteType], iv: ArrayType[ByteType]
    ) -> ICryptoTransform: ...
    def GenerateIV(self) -> VoidType: ...
    def GenerateKey(self) -> VoidType: ...
    def get_Key(self) -> ArrayType[ByteType]: ...
    def get_KeySize(self) -> IntType: ...
    def set_Key(self, value: ArrayType[ByteType]) -> VoidType: ...
    def set_KeySize(self, value: IntType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class AesManaged(Aes, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def FeedbackSize(self) -> IntType: ...
    @FeedbackSize.setter
    def FeedbackSize(self, value: IntType) -> None: ...
    @property
    def IV(self) -> ArrayType[ByteType]: ...
    @IV.setter
    def IV(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def Key(self) -> ArrayType[ByteType]: ...
    @Key.setter
    def Key(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def KeySize(self) -> IntType: ...
    @KeySize.setter
    def KeySize(self, value: IntType) -> None: ...
    @property
    def Mode(self) -> CipherMode: ...
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    @property
    def Padding(self) -> PaddingMode: ...
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...

    # ---------- Methods ---------- #

    @overload
    def CreateDecryptor(self) -> ICryptoTransform: ...
    @overload
    def CreateDecryptor(
        self, key: ArrayType[ByteType], iv: ArrayType[ByteType]
    ) -> ICryptoTransform: ...
    @overload
    def CreateEncryptor(self) -> ICryptoTransform: ...
    @overload
    def CreateEncryptor(
        self, key: ArrayType[ByteType], iv: ArrayType[ByteType]
    ) -> ICryptoTransform: ...
    def GenerateIV(self) -> VoidType: ...
    def GenerateKey(self) -> VoidType: ...
    def get_FeedbackSize(self) -> IntType: ...
    def get_IV(self) -> ArrayType[ByteType]: ...
    def get_Key(self) -> ArrayType[ByteType]: ...
    def get_KeySize(self) -> IntType: ...
    def get_Mode(self) -> CipherMode: ...
    def get_Padding(self) -> PaddingMode: ...
    def set_FeedbackSize(self, value: IntType) -> VoidType: ...
    def set_IV(self, value: ArrayType[ByteType]) -> VoidType: ...
    def set_Key(self, value: ArrayType[ByteType]) -> VoidType: ...
    def set_KeySize(self, value: IntType) -> VoidType: ...
    def set_Mode(self, value: CipherMode) -> VoidType: ...
    def set_Padding(self, value: PaddingMode) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class AsnEncodedData(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, rawData: ArrayType[ByteType]): ...
    @overload
    def __init__(self, oid: StringType, rawData: ArrayType[ByteType]): ...
    @overload
    def __init__(self, oid: Oid, rawData: ArrayType[ByteType]): ...
    @overload
    def __init__(self, asnEncodedData: AsnEncodedData): ...

    # ---------- Properties ---------- #

    @property
    def Oid(self) -> Oid: ...
    @Oid.setter
    def Oid(self, value: Oid) -> None: ...
    @property
    def RawData(self) -> ArrayType[ByteType]: ...
    @RawData.setter
    def RawData(self, value: ArrayType[ByteType]) -> None: ...

    # ---------- Methods ---------- #

    def CopyFrom(self, asnEncodedData: AsnEncodedData) -> VoidType: ...
    def Format(self, multiLine: BooleanType) -> StringType: ...
    def get_Oid(self) -> Oid: ...
    def get_RawData(self) -> ArrayType[ByteType]: ...
    def set_Oid(self, value: Oid) -> VoidType: ...
    def set_RawData(self, value: ArrayType[ByteType]) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class AsnEncodedDataCollection(ObjectType, ICollection, IEnumerable):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, asnEncodedData: AsnEncodedData): ...

    # ---------- Properties ---------- #

    @property
    def Count(self) -> IntType: ...
    @property
    def IsSynchronized(self) -> BooleanType: ...
    def __getitem__(self, key: IntType) -> AsnEncodedData: ...
    @property
    def SyncRoot(self) -> ObjectType: ...

    # ---------- Methods ---------- #

    def Add(self, asnEncodedData: AsnEncodedData) -> IntType: ...
    def CopyTo(self, array: ArrayType[AsnEncodedData], index: IntType) -> VoidType: ...
    def GetEnumerator(self) -> AsnEncodedDataEnumerator: ...
    def Remove(self, asnEncodedData: AsnEncodedData) -> VoidType: ...
    def get_Count(self) -> IntType: ...
    def get_IsSynchronized(self) -> BooleanType: ...
    def get_Item(self, index: IntType) -> AsnEncodedData: ...
    def get_SyncRoot(self) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class AsnEncodedDataEnumerator(ObjectType, IEnumerator):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Current(self) -> AsnEncodedData: ...

    # ---------- Methods ---------- #

    def MoveNext(self) -> BooleanType: ...
    def Reset(self) -> VoidType: ...
    def get_Current(self) -> AsnEncodedData: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class AsymmetricAlgorithm(ABC, ObjectType, IDisposable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def KeyExchangeAlgorithm(self) -> StringType: ...
    @property
    def KeySize(self) -> IntType: ...
    @KeySize.setter
    def KeySize(self, value: IntType) -> None: ...
    @property
    def LegalKeySizes(self) -> ArrayType[KeySizes]: ...
    @property
    def SignatureAlgorithm(self) -> StringType: ...

    # ---------- Methods ---------- #

    def Clear(self) -> VoidType: ...
    @staticmethod
    @overload
    def Create(algName: StringType) -> AsymmetricAlgorithm: ...
    @staticmethod
    @overload
    def Create() -> AsymmetricAlgorithm: ...
    def Dispose(self) -> VoidType: ...
    def FromXmlString(self, xmlString: StringType) -> VoidType: ...
    def ToXmlString(self, includePrivateParameters: BooleanType) -> StringType: ...
    def get_KeyExchangeAlgorithm(self) -> StringType: ...
    def get_KeySize(self) -> IntType: ...
    def get_LegalKeySizes(self) -> ArrayType[KeySizes]: ...
    def get_SignatureAlgorithm(self) -> StringType: ...
    def set_KeySize(self, value: IntType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class AsymmetricKeyExchangeDeformatter(ABC, ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Parameters(self) -> StringType: ...
    @Parameters.setter
    def Parameters(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    def DecryptKeyExchange(self, rgb: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    def SetKey(self, key: AsymmetricAlgorithm) -> VoidType: ...
    def get_Parameters(self) -> StringType: ...
    def set_Parameters(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class AsymmetricKeyExchangeFormatter(ABC, ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Parameters(self) -> StringType: ...

    # ---------- Methods ---------- #

    @overload
    def CreateKeyExchange(self, data: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    @overload
    def CreateKeyExchange(
        self, data: ArrayType[ByteType], symAlgType: TypeType
    ) -> ArrayType[ByteType]: ...
    def SetKey(self, key: AsymmetricAlgorithm) -> VoidType: ...
    def get_Parameters(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class AsymmetricSignatureDeformatter(ABC, ObjectType):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def SetHashAlgorithm(self, strName: StringType) -> VoidType: ...
    def SetKey(self, key: AsymmetricAlgorithm) -> VoidType: ...
    @overload
    def VerifySignature(
        self, hash: HashAlgorithm, rgbSignature: ArrayType[ByteType]
    ) -> BooleanType: ...
    @overload
    def VerifySignature(
        self, rgbHash: ArrayType[ByteType], rgbSignature: ArrayType[ByteType]
    ) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class AsymmetricSignatureFormatter(ABC, ObjectType):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def CreateSignature(self, hash: HashAlgorithm) -> ArrayType[ByteType]: ...
    @overload
    def CreateSignature(self, rgbHash: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    def SetHashAlgorithm(self, strName: StringType) -> VoidType: ...
    def SetKey(self, key: AsymmetricAlgorithm) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class BCryptAlgorithmHandleCache(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def GetCachedAlgorithmHandle(
        self, algorithm: StringType, implementation: StringType
    ) -> SafeBCryptAlgorithmHandle: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class BCryptHashAlgorithm(ObjectType, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, algorithm: CngAlgorithm, implementation: StringType): ...

    # No Properties

    # ---------- Methods ---------- #

    def Dispose(self) -> VoidType: ...
    def HashCore(
        self, array: ArrayType[ByteType], ibStart: IntType, cbSize: IntType
    ) -> VoidType: ...
    def HashFinal(self) -> ArrayType[ByteType]: ...
    def HashStream(self, stream: Stream) -> VoidType: ...
    def Initialize(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class BCryptNative(ABC, ObjectType):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    def BCryptDecrypt(
        hKey: SafeBCryptKeyHandle,
        input: ArrayType[ByteType],
        inputOffset: IntType,
        inputCount: IntType,
        iv: ArrayType[ByteType],
        output: ArrayType[ByteType],
        outputOffset: IntType,
        outputCount: IntType,
    ) -> IntType: ...
    @staticmethod
    def BCryptEncrypt(
        hKey: SafeBCryptKeyHandle,
        input: ArrayType[ByteType],
        inputOffset: IntType,
        inputCount: IntType,
        iv: ArrayType[ByteType],
        output: ArrayType[ByteType],
        outputOffset: IntType,
        outputCount: IntType,
    ) -> IntType: ...
    @staticmethod
    def SetCipherMode(hAlg: SafeBCryptAlgorithmHandle, cipherMode: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class BigInt(ObjectType):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def Equals(self, obj: ObjectType) -> BooleanType: ...
    def GetHashCode(self) -> IntType: ...
    @staticmethod
    def op_Equality(value1: BigInt, value2: BigInt) -> BooleanType: ...
    @staticmethod
    def op_GreaterThan(value1: BigInt, value2: BigInt) -> BooleanType: ...
    @staticmethod
    def op_Inequality(value1: BigInt, value2: BigInt) -> BooleanType: ...
    @staticmethod
    def op_LessThan(value1: BigInt, value2: BigInt) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CAPI(CAPIMethods):
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

class CAPI(ABC, ObjectType):
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

class CAPIBase(ABC, ObjectType):
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

class CAPIMethods(ABC, CAPIUnsafe):
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

class CAPINative(ABC, CAPIBase):
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

class CAPISafe(ABC, CAPINative):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    def FreeLibrary(hModule: NIntType) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CAPIUnsafe(ABC, CAPISafe):
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

class CapiHashAlgorithm(ObjectType, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(
        self, provider: StringType, providerType: ProviderType, algorithm: AlgorithmId
    ): ...

    # No Properties

    # ---------- Methods ---------- #

    def Dispose(self) -> VoidType: ...
    def HashCore(
        self, array: ArrayType[ByteType], ibStart: IntType, cbSize: IntType
    ) -> VoidType: ...
    def HashFinal(self) -> ArrayType[ByteType]: ...
    def Initialize(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CapiNative(ABC, ObjectType):
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

class CapiSymmetricAlgorithm(ObjectType, ICryptoTransform, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(
        self,
        blockSize: IntType,
        feedbackSize: IntType,
        provider: SafeCspHandle,
        key: SafeCapiKeyHandle,
        iv: ArrayType[ByteType],
        cipherMode: CipherMode,
        paddingMode: PaddingMode,
        encryptionMode: EncryptionMode,
    ): ...

    # ---------- Properties ---------- #

    @property
    def CanReuseTransform(self) -> BooleanType: ...
    @property
    def CanTransformMultipleBlocks(self) -> BooleanType: ...
    @property
    def InputBlockSize(self) -> IntType: ...
    @property
    def OutputBlockSize(self) -> IntType: ...

    # ---------- Methods ---------- #

    def Dispose(self) -> VoidType: ...
    def TransformBlock(
        self,
        inputBuffer: ArrayType[ByteType],
        inputOffset: IntType,
        inputCount: IntType,
        outputBuffer: ArrayType[ByteType],
        outputOffset: IntType,
    ) -> IntType: ...
    def TransformFinalBlock(
        self, inputBuffer: ArrayType[ByteType], inputOffset: IntType, inputCount: IntType
    ) -> ArrayType[ByteType]: ...
    def get_CanReuseTransform(self) -> BooleanType: ...
    def get_CanTransformMultipleBlocks(self) -> BooleanType: ...
    def get_InputBlockSize(self) -> IntType: ...
    def get_OutputBlockSize(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CngAlgorithm(ObjectType, IEquatable[CngAlgorithm]):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, algorithm: StringType): ...

    # ---------- Properties ---------- #

    @property
    def Algorithm(self) -> StringType: ...
    @staticmethod
    @property
    def ECDiffieHellman() -> CngAlgorithm: ...
    @staticmethod
    @property
    def ECDiffieHellmanP256() -> CngAlgorithm: ...
    @staticmethod
    @property
    def ECDiffieHellmanP384() -> CngAlgorithm: ...
    @staticmethod
    @property
    def ECDiffieHellmanP521() -> CngAlgorithm: ...
    @staticmethod
    @property
    def ECDsa() -> CngAlgorithm: ...
    @staticmethod
    @property
    def ECDsaP256() -> CngAlgorithm: ...
    @staticmethod
    @property
    def ECDsaP384() -> CngAlgorithm: ...
    @staticmethod
    @property
    def ECDsaP521() -> CngAlgorithm: ...
    @staticmethod
    @property
    def MD5() -> CngAlgorithm: ...
    @staticmethod
    @property
    def Rsa() -> CngAlgorithm: ...
    @staticmethod
    @property
    def Sha1() -> CngAlgorithm: ...
    @staticmethod
    @property
    def Sha256() -> CngAlgorithm: ...
    @staticmethod
    @property
    def Sha384() -> CngAlgorithm: ...
    @staticmethod
    @property
    def Sha512() -> CngAlgorithm: ...

    # ---------- Methods ---------- #

    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    @overload
    def Equals(self, other: CngAlgorithm) -> BooleanType: ...
    def GetHashCode(self) -> IntType: ...
    def ToString(self) -> StringType: ...
    def get_Algorithm(self) -> StringType: ...
    @staticmethod
    def get_ECDiffieHellman() -> CngAlgorithm: ...
    @staticmethod
    def get_ECDiffieHellmanP256() -> CngAlgorithm: ...
    @staticmethod
    def get_ECDiffieHellmanP384() -> CngAlgorithm: ...
    @staticmethod
    def get_ECDiffieHellmanP521() -> CngAlgorithm: ...
    @staticmethod
    def get_ECDsa() -> CngAlgorithm: ...
    @staticmethod
    def get_ECDsaP256() -> CngAlgorithm: ...
    @staticmethod
    def get_ECDsaP384() -> CngAlgorithm: ...
    @staticmethod
    def get_ECDsaP521() -> CngAlgorithm: ...
    @staticmethod
    def get_MD5() -> CngAlgorithm: ...
    @staticmethod
    def get_Rsa() -> CngAlgorithm: ...
    @staticmethod
    def get_Sha1() -> CngAlgorithm: ...
    @staticmethod
    def get_Sha256() -> CngAlgorithm: ...
    @staticmethod
    def get_Sha384() -> CngAlgorithm: ...
    @staticmethod
    def get_Sha512() -> CngAlgorithm: ...
    @staticmethod
    def op_Equality(left: CngAlgorithm, right: CngAlgorithm) -> BooleanType: ...
    @staticmethod
    def op_Inequality(left: CngAlgorithm, right: CngAlgorithm) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CngAlgorithmGroup(ObjectType, IEquatable[CngAlgorithmGroup]):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, algorithmGroup: StringType): ...

    # ---------- Properties ---------- #

    @property
    def AlgorithmGroup(self) -> StringType: ...
    @staticmethod
    @property
    def DiffieHellman() -> CngAlgorithmGroup: ...
    @staticmethod
    @property
    def Dsa() -> CngAlgorithmGroup: ...
    @staticmethod
    @property
    def ECDiffieHellman() -> CngAlgorithmGroup: ...
    @staticmethod
    @property
    def ECDsa() -> CngAlgorithmGroup: ...
    @staticmethod
    @property
    def Rsa() -> CngAlgorithmGroup: ...

    # ---------- Methods ---------- #

    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    @overload
    def Equals(self, other: CngAlgorithmGroup) -> BooleanType: ...
    def GetHashCode(self) -> IntType: ...
    def ToString(self) -> StringType: ...
    def get_AlgorithmGroup(self) -> StringType: ...
    @staticmethod
    def get_DiffieHellman() -> CngAlgorithmGroup: ...
    @staticmethod
    def get_Dsa() -> CngAlgorithmGroup: ...
    @staticmethod
    def get_ECDiffieHellman() -> CngAlgorithmGroup: ...
    @staticmethod
    def get_ECDsa() -> CngAlgorithmGroup: ...
    @staticmethod
    def get_Rsa() -> CngAlgorithmGroup: ...
    @staticmethod
    def op_Equality(left: CngAlgorithmGroup, right: CngAlgorithmGroup) -> BooleanType: ...
    @staticmethod
    def op_Inequality(left: CngAlgorithmGroup, right: CngAlgorithmGroup) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CngKey(ObjectType, IDisposable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Algorithm(self) -> CngAlgorithm: ...
    @property
    def AlgorithmGroup(self) -> CngAlgorithmGroup: ...
    @property
    def ExportPolicy(self) -> CngExportPolicies: ...
    @property
    def Handle(self) -> SafeNCryptKeyHandle: ...
    @property
    def IsEphemeral(self) -> BooleanType: ...
    @property
    def IsMachineKey(self) -> BooleanType: ...
    @property
    def KeyName(self) -> StringType: ...
    @property
    def KeySize(self) -> IntType: ...
    @property
    def KeyUsage(self) -> CngKeyUsages: ...
    @property
    def ParentWindowHandle(self) -> NIntType: ...
    @ParentWindowHandle.setter
    def ParentWindowHandle(self, value: NIntType) -> None: ...
    @property
    def Provider(self) -> CngProvider: ...
    @property
    def ProviderHandle(self) -> SafeNCryptProviderHandle: ...
    @property
    def UIPolicy(self) -> CngUIPolicy: ...
    @property
    def UniqueName(self) -> StringType: ...

    # ---------- Methods ---------- #

    @staticmethod
    @overload
    def Create(algorithm: CngAlgorithm) -> CngKey: ...
    @staticmethod
    @overload
    def Create(algorithm: CngAlgorithm, keyName: StringType) -> CngKey: ...
    @staticmethod
    @overload
    def Create(
        algorithm: CngAlgorithm, keyName: StringType, creationParameters: CngKeyCreationParameters
    ) -> CngKey: ...
    def Delete(self) -> VoidType: ...
    def Dispose(self) -> VoidType: ...
    @staticmethod
    @overload
    def Exists(keyName: StringType) -> BooleanType: ...
    @staticmethod
    @overload
    def Exists(keyName: StringType, provider: CngProvider) -> BooleanType: ...
    @staticmethod
    @overload
    def Exists(
        keyName: StringType, provider: CngProvider, options: CngKeyOpenOptions
    ) -> BooleanType: ...
    def Export(self, format: CngKeyBlobFormat) -> ArrayType[ByteType]: ...
    def GetProperty(self, name: StringType, options: CngPropertyOptions) -> CngProperty: ...
    def HasProperty(self, name: StringType, options: CngPropertyOptions) -> BooleanType: ...
    @staticmethod
    @overload
    def Import(keyBlob: ArrayType[ByteType], format: CngKeyBlobFormat) -> CngKey: ...
    @staticmethod
    @overload
    def Import(
        keyBlob: ArrayType[ByteType], format: CngKeyBlobFormat, provider: CngProvider
    ) -> CngKey: ...
    @staticmethod
    @overload
    def Open(keyName: StringType) -> CngKey: ...
    @staticmethod
    @overload
    def Open(keyName: StringType, provider: CngProvider) -> CngKey: ...
    @staticmethod
    @overload
    def Open(
        keyName: StringType, provider: CngProvider, openOptions: CngKeyOpenOptions
    ) -> CngKey: ...
    @staticmethod
    @overload
    def Open(
        keyHandle: SafeNCryptKeyHandle, keyHandleOpenOptions: CngKeyHandleOpenOptions
    ) -> CngKey: ...
    def SetProperty(self, property: CngProperty) -> VoidType: ...
    def get_Algorithm(self) -> CngAlgorithm: ...
    def get_AlgorithmGroup(self) -> CngAlgorithmGroup: ...
    def get_ExportPolicy(self) -> CngExportPolicies: ...
    def get_Handle(self) -> SafeNCryptKeyHandle: ...
    def get_IsEphemeral(self) -> BooleanType: ...
    def get_IsMachineKey(self) -> BooleanType: ...
    def get_KeyName(self) -> StringType: ...
    def get_KeySize(self) -> IntType: ...
    def get_KeyUsage(self) -> CngKeyUsages: ...
    def get_ParentWindowHandle(self) -> NIntType: ...
    def get_Provider(self) -> CngProvider: ...
    def get_ProviderHandle(self) -> SafeNCryptProviderHandle: ...
    def get_UIPolicy(self) -> CngUIPolicy: ...
    def get_UniqueName(self) -> StringType: ...
    def set_ParentWindowHandle(self, value: NIntType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CngKeyBlobFormat(ObjectType, IEquatable[CngKeyBlobFormat]):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, format: StringType): ...

    # ---------- Properties ---------- #

    @staticmethod
    @property
    def EccFullPrivateBlob() -> CngKeyBlobFormat: ...
    @staticmethod
    @property
    def EccFullPublicBlob() -> CngKeyBlobFormat: ...
    @staticmethod
    @property
    def EccPrivateBlob() -> CngKeyBlobFormat: ...
    @staticmethod
    @property
    def EccPublicBlob() -> CngKeyBlobFormat: ...
    @property
    def Format(self) -> StringType: ...
    @staticmethod
    @property
    def GenericPrivateBlob() -> CngKeyBlobFormat: ...
    @staticmethod
    @property
    def GenericPublicBlob() -> CngKeyBlobFormat: ...
    @staticmethod
    @property
    def OpaqueTransportBlob() -> CngKeyBlobFormat: ...
    @staticmethod
    @property
    def Pkcs8PrivateBlob() -> CngKeyBlobFormat: ...

    # ---------- Methods ---------- #

    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    @overload
    def Equals(self, other: CngKeyBlobFormat) -> BooleanType: ...
    def GetHashCode(self) -> IntType: ...
    def ToString(self) -> StringType: ...
    @staticmethod
    def get_EccFullPrivateBlob() -> CngKeyBlobFormat: ...
    @staticmethod
    def get_EccFullPublicBlob() -> CngKeyBlobFormat: ...
    @staticmethod
    def get_EccPrivateBlob() -> CngKeyBlobFormat: ...
    @staticmethod
    def get_EccPublicBlob() -> CngKeyBlobFormat: ...
    def get_Format(self) -> StringType: ...
    @staticmethod
    def get_GenericPrivateBlob() -> CngKeyBlobFormat: ...
    @staticmethod
    def get_GenericPublicBlob() -> CngKeyBlobFormat: ...
    @staticmethod
    def get_OpaqueTransportBlob() -> CngKeyBlobFormat: ...
    @staticmethod
    def get_Pkcs8PrivateBlob() -> CngKeyBlobFormat: ...
    @staticmethod
    def op_Equality(left: CngKeyBlobFormat, right: CngKeyBlobFormat) -> BooleanType: ...
    @staticmethod
    def op_Inequality(left: CngKeyBlobFormat, right: CngKeyBlobFormat) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CngKeyCreationParameters(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def ExportPolicy(self) -> NullableType[Nullable[CngExportPolicies]]: ...
    @ExportPolicy.setter
    def ExportPolicy(self, value: NullableType[Nullable[CngExportPolicies]]) -> None: ...
    @property
    def KeyCreationOptions(self) -> CngKeyCreationOptions: ...
    @KeyCreationOptions.setter
    def KeyCreationOptions(self, value: CngKeyCreationOptions) -> None: ...
    @property
    def KeyUsage(self) -> NullableType[Nullable[CngKeyUsages]]: ...
    @KeyUsage.setter
    def KeyUsage(self, value: NullableType[Nullable[CngKeyUsages]]) -> None: ...
    @property
    def Parameters(self) -> CngPropertyCollection: ...
    @property
    def ParentWindowHandle(self) -> NIntType: ...
    @ParentWindowHandle.setter
    def ParentWindowHandle(self, value: NIntType) -> None: ...
    @property
    def Provider(self) -> CngProvider: ...
    @Provider.setter
    def Provider(self, value: CngProvider) -> None: ...
    @property
    def UIPolicy(self) -> CngUIPolicy: ...
    @UIPolicy.setter
    def UIPolicy(self, value: CngUIPolicy) -> None: ...

    # ---------- Methods ---------- #

    def get_ExportPolicy(self) -> NullableType[Nullable[CngExportPolicies]]: ...
    def get_KeyCreationOptions(self) -> CngKeyCreationOptions: ...
    def get_KeyUsage(self) -> NullableType[Nullable[CngKeyUsages]]: ...
    def get_Parameters(self) -> CngPropertyCollection: ...
    def get_ParentWindowHandle(self) -> NIntType: ...
    def get_Provider(self) -> CngProvider: ...
    def get_UIPolicy(self) -> CngUIPolicy: ...
    def set_ExportPolicy(self, value: NullableType[Nullable[CngExportPolicies]]) -> VoidType: ...
    def set_KeyCreationOptions(self, value: CngKeyCreationOptions) -> VoidType: ...
    def set_KeyUsage(self, value: NullableType[Nullable[CngKeyUsages]]) -> VoidType: ...
    def set_ParentWindowHandle(self, value: NIntType) -> VoidType: ...
    def set_Provider(self, value: CngProvider) -> VoidType: ...
    def set_UIPolicy(self, value: CngUIPolicy) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CngLightup(ABC, ObjectType):
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

class CngPropertyCollection(
    Collection[CngProperty],
    IList[CngProperty],
    ICollection[CngProperty],
    IEnumerable[CngProperty],
    IEnumerable,
    IList,
    ICollection,
    IReadOnlyList[CngProperty],
    IReadOnlyCollection[CngProperty],
):
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

class CngProvider(ObjectType, IEquatable[CngProvider]):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, provider: StringType): ...

    # ---------- Properties ---------- #

    @staticmethod
    @property
    def MicrosoftSmartCardKeyStorageProvider() -> CngProvider: ...
    @staticmethod
    @property
    def MicrosoftSoftwareKeyStorageProvider() -> CngProvider: ...
    @property
    def Provider(self) -> StringType: ...

    # ---------- Methods ---------- #

    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    @overload
    def Equals(self, other: CngProvider) -> BooleanType: ...
    def GetHashCode(self) -> IntType: ...
    def ToString(self) -> StringType: ...
    @staticmethod
    def get_MicrosoftSmartCardKeyStorageProvider() -> CngProvider: ...
    @staticmethod
    def get_MicrosoftSoftwareKeyStorageProvider() -> CngProvider: ...
    def get_Provider(self) -> StringType: ...
    @staticmethod
    def op_Equality(left: CngProvider, right: CngProvider) -> BooleanType: ...
    @staticmethod
    def op_Inequality(left: CngProvider, right: CngProvider) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CngUIPolicy(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, protectionLevel: CngUIProtectionLevels): ...
    @overload
    def __init__(self, protectionLevel: CngUIProtectionLevels, friendlyName: StringType): ...
    @overload
    def __init__(
        self,
        protectionLevel: CngUIProtectionLevels,
        friendlyName: StringType,
        description: StringType,
    ): ...
    @overload
    def __init__(
        self,
        protectionLevel: CngUIProtectionLevels,
        friendlyName: StringType,
        description: StringType,
        useContext: StringType,
    ): ...
    @overload
    def __init__(
        self,
        protectionLevel: CngUIProtectionLevels,
        friendlyName: StringType,
        description: StringType,
        useContext: StringType,
        creationTitle: StringType,
    ): ...

    # ---------- Properties ---------- #

    @property
    def CreationTitle(self) -> StringType: ...
    @property
    def Description(self) -> StringType: ...
    @property
    def FriendlyName(self) -> StringType: ...
    @property
    def ProtectionLevel(self) -> CngUIProtectionLevels: ...
    @property
    def UseContext(self) -> StringType: ...

    # ---------- Methods ---------- #

    def get_CreationTitle(self) -> StringType: ...
    def get_Description(self) -> StringType: ...
    def get_FriendlyName(self) -> StringType: ...
    def get_ProtectionLevel(self) -> CngUIProtectionLevels: ...
    def get_UseContext(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Constants(ABC, ObjectType):
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

class CryptoAPITransform(ObjectType, ICryptoTransform, IDisposable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def CanReuseTransform(self) -> BooleanType: ...
    @property
    def CanTransformMultipleBlocks(self) -> BooleanType: ...
    @property
    def InputBlockSize(self) -> IntType: ...
    @property
    def KeyHandle(self) -> NIntType: ...
    @property
    def OutputBlockSize(self) -> IntType: ...

    # ---------- Methods ---------- #

    def Clear(self) -> VoidType: ...
    def Dispose(self) -> VoidType: ...
    def Reset(self) -> VoidType: ...
    def TransformBlock(
        self,
        inputBuffer: ArrayType[ByteType],
        inputOffset: IntType,
        inputCount: IntType,
        outputBuffer: ArrayType[ByteType],
        outputOffset: IntType,
    ) -> IntType: ...
    def TransformFinalBlock(
        self, inputBuffer: ArrayType[ByteType], inputOffset: IntType, inputCount: IntType
    ) -> ArrayType[ByteType]: ...
    def get_CanReuseTransform(self) -> BooleanType: ...
    def get_CanTransformMultipleBlocks(self) -> BooleanType: ...
    def get_InputBlockSize(self) -> IntType: ...
    def get_KeyHandle(self) -> NIntType: ...
    def get_OutputBlockSize(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CryptoConfig(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @staticmethod
    @property
    def AllowOnlyFipsAlgorithms() -> BooleanType: ...

    # ---------- Methods ---------- #

    @staticmethod
    def AddAlgorithm(algorithm: TypeType, names: ArrayType[StringType]) -> VoidType: ...
    @staticmethod
    def AddOID(oid: StringType, names: ArrayType[StringType]) -> VoidType: ...
    @staticmethod
    @overload
    def CreateFromName(name: StringType, args: ArrayType[ObjectType]) -> ObjectType: ...
    @staticmethod
    @overload
    def CreateFromName(name: StringType) -> ObjectType: ...
    @staticmethod
    def EncodeOID(str: StringType) -> ArrayType[ByteType]: ...
    @staticmethod
    def MapNameToOID(name: StringType) -> StringType: ...
    @staticmethod
    def get_AllowOnlyFipsAlgorithms() -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CryptoStream(Stream, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, stream: Stream, transform: ICryptoTransform, mode: CryptoStreamMode): ...
    @overload
    def __init__(
        self,
        stream: Stream,
        transform: ICryptoTransform,
        mode: CryptoStreamMode,
        leaveOpen: BooleanType,
    ): ...

    # ---------- Properties ---------- #

    @property
    def CanRead(self) -> BooleanType: ...
    @property
    def CanSeek(self) -> BooleanType: ...
    @property
    def CanWrite(self) -> BooleanType: ...
    @property
    def HasFlushedFinalBlock(self) -> BooleanType: ...
    @property
    def Length(self) -> LongType: ...
    @property
    def Position(self) -> LongType: ...
    @Position.setter
    def Position(self, value: LongType) -> None: ...

    # ---------- Methods ---------- #

    def Clear(self) -> VoidType: ...
    def Flush(self) -> VoidType: ...
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task: ...
    def FlushFinalBlock(self) -> VoidType: ...
    def Read(
        self, buffer: ArrayType[ByteType], offset: IntType, count: IntType
    ) -> Tuple[IntType, ArrayType[ByteType]]: ...
    @overload
    def ReadAsync(
        self,
        buffer: ArrayType[ByteType],
        offset: IntType,
        count: IntType,
        cancellationToken: CancellationToken,
    ) -> Task[IntType]: ...
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    def SetLength(self, value: LongType) -> VoidType: ...
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    @overload
    def WriteAsync(
        self,
        buffer: ArrayType[ByteType],
        offset: IntType,
        count: IntType,
        cancellationToken: CancellationToken,
    ) -> Task: ...
    def get_CanRead(self) -> BooleanType: ...
    def get_CanSeek(self) -> BooleanType: ...
    def get_CanWrite(self) -> BooleanType: ...
    def get_HasFlushedFinalBlock(self) -> BooleanType: ...
    def get_Length(self) -> LongType: ...
    def get_Position(self) -> LongType: ...
    def set_Position(self, value: LongType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CryptographicAttributeObject(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, oid: Oid): ...
    @overload
    def __init__(self, oid: Oid, values: AsnEncodedDataCollection): ...

    # ---------- Properties ---------- #

    @property
    def Oid(self) -> Oid: ...
    @property
    def Values(self) -> AsnEncodedDataCollection: ...

    # ---------- Methods ---------- #

    def get_Oid(self) -> Oid: ...
    def get_Values(self) -> AsnEncodedDataCollection: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CryptographicAttributeObjectCollection(ObjectType, ICollection, IEnumerable):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, attribute: CryptographicAttributeObject): ...

    # ---------- Properties ---------- #

    @property
    def Count(self) -> IntType: ...
    @property
    def IsSynchronized(self) -> BooleanType: ...
    def __getitem__(self, key: IntType) -> CryptographicAttributeObject: ...
    @property
    def SyncRoot(self) -> ObjectType: ...

    # ---------- Methods ---------- #

    @overload
    def Add(self, asnEncodedData: AsnEncodedData) -> IntType: ...
    @overload
    def Add(self, attribute: CryptographicAttributeObject) -> IntType: ...
    def CopyTo(
        self, array: ArrayType[CryptographicAttributeObject], index: IntType
    ) -> VoidType: ...
    def GetEnumerator(self) -> CryptographicAttributeObjectEnumerator: ...
    def Remove(self, attribute: CryptographicAttributeObject) -> VoidType: ...
    def get_Count(self) -> IntType: ...
    def get_IsSynchronized(self) -> BooleanType: ...
    def get_Item(self, index: IntType) -> CryptographicAttributeObject: ...
    def get_SyncRoot(self) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CryptographicAttributeObjectEnumerator(ObjectType, IEnumerator):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Current(self) -> CryptographicAttributeObject: ...

    # ---------- Methods ---------- #

    def MoveNext(self) -> BooleanType: ...
    def Reset(self) -> VoidType: ...
    def get_Current(self) -> CryptographicAttributeObject: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CryptographicException(SystemException, ISerializable, _Exception):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: StringType): ...
    @overload
    def __init__(self, format: StringType, insert: StringType): ...
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    @overload
    def __init__(self, hr: IntType): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CryptographicUnexpectedOperationException(CryptographicException, ISerializable, _Exception):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: StringType): ...
    @overload
    def __init__(self, format: StringType, insert: StringType): ...
    @overload
    def __init__(self, message: StringType, inner: Exception): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CspKeyContainerInfo(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, parameters: CspParameters): ...

    # ---------- Properties ---------- #

    @property
    def Accessible(self) -> BooleanType: ...
    @property
    def CryptoKeySecurity(self) -> CryptoKeySecurity: ...
    @property
    def Exportable(self) -> BooleanType: ...
    @property
    def HardwareDevice(self) -> BooleanType: ...
    @property
    def KeyContainerName(self) -> StringType: ...
    @property
    def KeyNumber(self) -> KeyNumber: ...
    @property
    def MachineKeyStore(self) -> BooleanType: ...
    @property
    def Protected(self) -> BooleanType: ...
    @property
    def ProviderName(self) -> StringType: ...
    @property
    def ProviderType(self) -> IntType: ...
    @property
    def RandomlyGenerated(self) -> BooleanType: ...
    @property
    def Removable(self) -> BooleanType: ...
    @property
    def UniqueKeyContainerName(self) -> StringType: ...

    # ---------- Methods ---------- #

    def get_Accessible(self) -> BooleanType: ...
    def get_CryptoKeySecurity(self) -> CryptoKeySecurity: ...
    def get_Exportable(self) -> BooleanType: ...
    def get_HardwareDevice(self) -> BooleanType: ...
    def get_KeyContainerName(self) -> StringType: ...
    def get_KeyNumber(self) -> KeyNumber: ...
    def get_MachineKeyStore(self) -> BooleanType: ...
    def get_Protected(self) -> BooleanType: ...
    def get_ProviderName(self) -> StringType: ...
    def get_ProviderType(self) -> IntType: ...
    def get_RandomlyGenerated(self) -> BooleanType: ...
    def get_Removable(self) -> BooleanType: ...
    def get_UniqueKeyContainerName(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CspParameters(ObjectType):
    # ---------- Fields ---------- #

    @property
    def KeyContainerName(self) -> StringType: ...
    @KeyContainerName.setter
    def KeyContainerName(self, value: StringType) -> None: ...
    @property
    def KeyNumber(self) -> IntType: ...
    @KeyNumber.setter
    def KeyNumber(self, value: IntType) -> None: ...
    @property
    def ProviderName(self) -> StringType: ...
    @ProviderName.setter
    def ProviderName(self, value: StringType) -> None: ...
    @property
    def ProviderType(self) -> IntType: ...
    @ProviderType.setter
    def ProviderType(self, value: IntType) -> None: ...

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, dwTypeIn: IntType): ...
    @overload
    def __init__(self, dwTypeIn: IntType, strProviderNameIn: StringType): ...
    @overload
    def __init__(
        self, dwTypeIn: IntType, strProviderNameIn: StringType, strContainerNameIn: StringType
    ): ...
    @overload
    def __init__(
        self,
        providerType: IntType,
        providerName: StringType,
        keyContainerName: StringType,
        cryptoKeySecurity: CryptoKeySecurity,
        keyPassword: SecureString,
    ): ...
    @overload
    def __init__(
        self,
        providerType: IntType,
        providerName: StringType,
        keyContainerName: StringType,
        cryptoKeySecurity: CryptoKeySecurity,
        parentWindowHandle: NIntType,
    ): ...

    # ---------- Properties ---------- #

    @property
    def CryptoKeySecurity(self) -> CryptoKeySecurity: ...
    @CryptoKeySecurity.setter
    def CryptoKeySecurity(self, value: CryptoKeySecurity) -> None: ...
    @property
    def Flags(self) -> CspProviderFlags: ...
    @Flags.setter
    def Flags(self, value: CspProviderFlags) -> None: ...
    @property
    def KeyPassword(self) -> SecureString: ...
    @KeyPassword.setter
    def KeyPassword(self, value: SecureString) -> None: ...
    @property
    def ParentWindowHandle(self) -> NIntType: ...
    @ParentWindowHandle.setter
    def ParentWindowHandle(self, value: NIntType) -> None: ...

    # ---------- Methods ---------- #

    def get_CryptoKeySecurity(self) -> CryptoKeySecurity: ...
    def get_Flags(self) -> CspProviderFlags: ...
    def get_KeyPassword(self) -> SecureString: ...
    def get_ParentWindowHandle(self) -> NIntType: ...
    def set_CryptoKeySecurity(self, value: CryptoKeySecurity) -> VoidType: ...
    def set_Flags(self, value: CspProviderFlags) -> VoidType: ...
    def set_KeyPassword(self, value: SecureString) -> VoidType: ...
    def set_ParentWindowHandle(self, value: NIntType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class DES(ABC, SymmetricAlgorithm, IDisposable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Key(self) -> ArrayType[ByteType]: ...
    @Key.setter
    def Key(self, value: ArrayType[ByteType]) -> None: ...

    # ---------- Methods ---------- #

    @staticmethod
    @overload
    def Create(algName: StringType) -> DES: ...
    @staticmethod
    @overload
    def Create() -> DES: ...
    @staticmethod
    def IsSemiWeakKey(rgbKey: ArrayType[ByteType]) -> BooleanType: ...
    @staticmethod
    def IsWeakKey(rgbKey: ArrayType[ByteType]) -> BooleanType: ...
    def get_Key(self) -> ArrayType[ByteType]: ...
    def set_Key(self, value: ArrayType[ByteType]) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class DESCryptoServiceProvider(DES, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def CreateDecryptor(
        self, rgbKey: ArrayType[ByteType], rgbIV: ArrayType[ByteType]
    ) -> ICryptoTransform: ...
    @overload
    def CreateEncryptor(
        self, rgbKey: ArrayType[ByteType], rgbIV: ArrayType[ByteType]
    ) -> ICryptoTransform: ...
    def GenerateIV(self) -> VoidType: ...
    def GenerateKey(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class DSA(ABC, AsymmetricAlgorithm, IDisposable):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    @overload
    def Create(algName: StringType) -> DSA: ...
    @staticmethod
    @overload
    def Create() -> DSA: ...
    @staticmethod
    @overload
    def Create(keySizeInBits: IntType) -> DSA: ...
    @staticmethod
    @overload
    def Create(parameters: DSAParameters) -> DSA: ...
    def CreateSignature(self, rgbHash: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    def ExportParameters(self, includePrivateParameters: BooleanType) -> DSAParameters: ...
    def FromXmlString(self, xmlString: StringType) -> VoidType: ...
    def ImportParameters(self, parameters: DSAParameters) -> VoidType: ...
    @overload
    def SignData(
        self, data: ArrayType[ByteType], hashAlgorithm: HashAlgorithmName
    ) -> ArrayType[ByteType]: ...
    @overload
    def SignData(
        self,
        data: ArrayType[ByteType],
        offset: IntType,
        count: IntType,
        hashAlgorithm: HashAlgorithmName,
    ) -> ArrayType[ByteType]: ...
    @overload
    def SignData(self, data: Stream, hashAlgorithm: HashAlgorithmName) -> ArrayType[ByteType]: ...
    def ToXmlString(self, includePrivateParameters: BooleanType) -> StringType: ...
    @overload
    def VerifyData(
        self,
        data: ArrayType[ByteType],
        signature: ArrayType[ByteType],
        hashAlgorithm: HashAlgorithmName,
    ) -> BooleanType: ...
    @overload
    def VerifyData(
        self,
        data: ArrayType[ByteType],
        offset: IntType,
        count: IntType,
        signature: ArrayType[ByteType],
        hashAlgorithm: HashAlgorithmName,
    ) -> BooleanType: ...
    @overload
    def VerifyData(
        self, data: Stream, signature: ArrayType[ByteType], hashAlgorithm: HashAlgorithmName
    ) -> BooleanType: ...
    def VerifySignature(
        self, rgbHash: ArrayType[ByteType], rgbSignature: ArrayType[ByteType]
    ) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class DSACng(DSA, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, keySize: IntType): ...
    @overload
    def __init__(self, key: CngKey): ...

    # ---------- Properties ---------- #

    @property
    def Key(self) -> CngKey: ...
    @property
    def KeyExchangeAlgorithm(self) -> StringType: ...
    @property
    def LegalKeySizes(self) -> ArrayType[KeySizes]: ...
    @property
    def SignatureAlgorithm(self) -> StringType: ...

    # ---------- Methods ---------- #

    def CreateSignature(self, rgbHash: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    def ExportParameters(self, includePrivateParameters: BooleanType) -> DSAParameters: ...
    def ImportParameters(self, parameters: DSAParameters) -> VoidType: ...
    def VerifySignature(
        self, rgbHash: ArrayType[ByteType], rgbSignature: ArrayType[ByteType]
    ) -> BooleanType: ...
    def get_Key(self) -> CngKey: ...
    def get_KeyExchangeAlgorithm(self) -> StringType: ...
    def get_LegalKeySizes(self) -> ArrayType[KeySizes]: ...
    def get_SignatureAlgorithm(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class DSACryptoServiceProvider(DSA, IDisposable, ICspAsymmetricAlgorithm):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, dwKeySize: IntType): ...
    @overload
    def __init__(self, parameters: CspParameters): ...
    @overload
    def __init__(self, dwKeySize: IntType, parameters: CspParameters): ...

    # ---------- Properties ---------- #

    @property
    def CspKeyContainerInfo(self) -> CspKeyContainerInfo: ...
    @property
    def KeyExchangeAlgorithm(self) -> StringType: ...
    @property
    def KeySize(self) -> IntType: ...
    @property
    def PersistKeyInCsp(self) -> BooleanType: ...
    @PersistKeyInCsp.setter
    def PersistKeyInCsp(self, value: BooleanType) -> None: ...
    @property
    def PublicOnly(self) -> BooleanType: ...
    @property
    def SignatureAlgorithm(self) -> StringType: ...
    @staticmethod
    @property
    def UseMachineKeyStore() -> BooleanType: ...
    @staticmethod
    @UseMachineKeyStore.setter
    def UseMachineKeyStore(value: BooleanType) -> None: ...

    # ---------- Methods ---------- #

    def CreateSignature(self, rgbHash: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    def ExportCspBlob(self, includePrivateParameters: BooleanType) -> ArrayType[ByteType]: ...
    def ExportParameters(self, includePrivateParameters: BooleanType) -> DSAParameters: ...
    def ImportCspBlob(self, keyBlob: ArrayType[ByteType]) -> VoidType: ...
    def ImportParameters(self, parameters: DSAParameters) -> VoidType: ...
    @overload
    def SignData(self, inputStream: Stream) -> ArrayType[ByteType]: ...
    @overload
    def SignData(self, buffer: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    @overload
    def SignData(
        self, buffer: ArrayType[ByteType], offset: IntType, count: IntType
    ) -> ArrayType[ByteType]: ...
    def SignHash(self, rgbHash: ArrayType[ByteType], str: StringType) -> ArrayType[ByteType]: ...
    @overload
    def VerifyData(
        self, rgbData: ArrayType[ByteType], rgbSignature: ArrayType[ByteType]
    ) -> BooleanType: ...
    def VerifyHash(
        self, rgbHash: ArrayType[ByteType], str: StringType, rgbSignature: ArrayType[ByteType]
    ) -> BooleanType: ...
    def VerifySignature(
        self, rgbHash: ArrayType[ByteType], rgbSignature: ArrayType[ByteType]
    ) -> BooleanType: ...
    def get_CspKeyContainerInfo(self) -> CspKeyContainerInfo: ...
    def get_KeyExchangeAlgorithm(self) -> StringType: ...
    def get_KeySize(self) -> IntType: ...
    def get_PersistKeyInCsp(self) -> BooleanType: ...
    def get_PublicOnly(self) -> BooleanType: ...
    def get_SignatureAlgorithm(self) -> StringType: ...
    @staticmethod
    def get_UseMachineKeyStore() -> BooleanType: ...
    def set_PersistKeyInCsp(self, value: BooleanType) -> VoidType: ...
    @staticmethod
    def set_UseMachineKeyStore(value: BooleanType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class DSACspObject(ObjectType):
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

class DSASignatureDeformatter(AsymmetricSignatureDeformatter):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, key: AsymmetricAlgorithm): ...

    # No Properties

    # ---------- Methods ---------- #

    def SetHashAlgorithm(self, strName: StringType) -> VoidType: ...
    def SetKey(self, key: AsymmetricAlgorithm) -> VoidType: ...
    @overload
    def VerifySignature(
        self, rgbHash: ArrayType[ByteType], rgbSignature: ArrayType[ByteType]
    ) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class DSASignatureDescription(SignatureDescription):
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

class DSASignatureFormatter(AsymmetricSignatureFormatter):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, key: AsymmetricAlgorithm): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def CreateSignature(self, rgbHash: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    def SetHashAlgorithm(self, strName: StringType) -> VoidType: ...
    def SetKey(self, key: AsymmetricAlgorithm) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class DataProtector(ABC, ObjectType):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    def Create(
        providerClass: StringType,
        applicationName: StringType,
        primaryPurpose: StringType,
        specificPurposes: ArrayType[StringType],
    ) -> DataProtector: ...
    def IsReprotectRequired(self, encryptedData: ArrayType[ByteType]) -> BooleanType: ...
    def Protect(self, userData: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    def Unprotect(self, encryptedData: ArrayType[ByteType]) -> ArrayType[ByteType]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class DeriveBytes(ABC, ObjectType, IDisposable):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def Dispose(self) -> VoidType: ...
    def GetBytes(self, cb: IntType) -> ArrayType[ByteType]: ...
    def Reset(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class DpapiDataProtector(DataProtector):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(
        self,
        appName: StringType,
        primaryPurpose: StringType,
        specificPurpose: ArrayType[StringType],
    ): ...

    # ---------- Properties ---------- #

    @property
    def Scope(self) -> DataProtectionScope: ...
    @Scope.setter
    def Scope(self, value: DataProtectionScope) -> None: ...

    # ---------- Methods ---------- #

    def IsReprotectRequired(self, encryptedData: ArrayType[ByteType]) -> BooleanType: ...
    def get_Scope(self) -> DataProtectionScope: ...
    def set_Scope(self, value: DataProtectionScope) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ECCng(ABC, ObjectType):
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

class ECDiffieHellman(ABC, AsymmetricAlgorithm, IDisposable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def KeyExchangeAlgorithm(self) -> StringType: ...
    @property
    def PublicKey(self) -> ECDiffieHellmanPublicKey: ...
    @property
    def SignatureAlgorithm(self) -> StringType: ...

    # ---------- Methods ---------- #

    @staticmethod
    @overload
    def Create() -> ECDiffieHellman: ...
    @staticmethod
    @overload
    def Create(algorithm: StringType) -> ECDiffieHellman: ...
    @staticmethod
    @overload
    def Create(curve: ECCurve) -> ECDiffieHellman: ...
    @staticmethod
    @overload
    def Create(parameters: ECParameters) -> ECDiffieHellman: ...
    @overload
    def DeriveKeyFromHash(
        self, otherPartyPublicKey: ECDiffieHellmanPublicKey, hashAlgorithm: HashAlgorithmName
    ) -> ArrayType[ByteType]: ...
    @overload
    def DeriveKeyFromHash(
        self,
        otherPartyPublicKey: ECDiffieHellmanPublicKey,
        hashAlgorithm: HashAlgorithmName,
        secretPrepend: ArrayType[ByteType],
        secretAppend: ArrayType[ByteType],
    ) -> ArrayType[ByteType]: ...
    @overload
    def DeriveKeyFromHmac(
        self,
        otherPartyPublicKey: ECDiffieHellmanPublicKey,
        hashAlgorithm: HashAlgorithmName,
        hmacKey: ArrayType[ByteType],
    ) -> ArrayType[ByteType]: ...
    @overload
    def DeriveKeyFromHmac(
        self,
        otherPartyPublicKey: ECDiffieHellmanPublicKey,
        hashAlgorithm: HashAlgorithmName,
        hmacKey: ArrayType[ByteType],
        secretPrepend: ArrayType[ByteType],
        secretAppend: ArrayType[ByteType],
    ) -> ArrayType[ByteType]: ...
    def DeriveKeyMaterial(
        self, otherPartyPublicKey: ECDiffieHellmanPublicKey
    ) -> ArrayType[ByteType]: ...
    def DeriveKeyTls(
        self,
        otherPartyPublicKey: ECDiffieHellmanPublicKey,
        prfLabel: ArrayType[ByteType],
        prfSeed: ArrayType[ByteType],
    ) -> ArrayType[ByteType]: ...
    def ExportExplicitParameters(self, includePrivateParameters: BooleanType) -> ECParameters: ...
    def ExportParameters(self, includePrivateParameters: BooleanType) -> ECParameters: ...
    def GenerateKey(self, curve: ECCurve) -> VoidType: ...
    def ImportParameters(self, parameters: ECParameters) -> VoidType: ...
    def get_KeyExchangeAlgorithm(self) -> StringType: ...
    def get_PublicKey(self) -> ECDiffieHellmanPublicKey: ...
    def get_SignatureAlgorithm(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ECDiffieHellmanCng(ECDiffieHellman, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, keySize: IntType): ...
    @overload
    def __init__(self, curve: ECCurve): ...
    @overload
    def __init__(self, key: CngKey): ...

    # ---------- Properties ---------- #

    @property
    def HashAlgorithm(self) -> CngAlgorithm: ...
    @HashAlgorithm.setter
    def HashAlgorithm(self, value: CngAlgorithm) -> None: ...
    @property
    def HmacKey(self) -> ArrayType[ByteType]: ...
    @HmacKey.setter
    def HmacKey(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def Key(self) -> CngKey: ...
    @property
    def KeyDerivationFunction(self) -> ECDiffieHellmanKeyDerivationFunction: ...
    @KeyDerivationFunction.setter
    def KeyDerivationFunction(self, value: ECDiffieHellmanKeyDerivationFunction) -> None: ...
    @property
    def Label(self) -> ArrayType[ByteType]: ...
    @Label.setter
    def Label(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def PublicKey(self) -> ECDiffieHellmanPublicKey: ...
    @property
    def SecretAppend(self) -> ArrayType[ByteType]: ...
    @SecretAppend.setter
    def SecretAppend(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def SecretPrepend(self) -> ArrayType[ByteType]: ...
    @SecretPrepend.setter
    def SecretPrepend(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def Seed(self) -> ArrayType[ByteType]: ...
    @Seed.setter
    def Seed(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def UseSecretAgreementAsHmacKey(self) -> BooleanType: ...

    # ---------- Methods ---------- #

    @overload
    def DeriveKeyFromHash(
        self,
        otherPartyPublicKey: ECDiffieHellmanPublicKey,
        hashAlgorithm: HashAlgorithmName,
        secretPrepend: ArrayType[ByteType],
        secretAppend: ArrayType[ByteType],
    ) -> ArrayType[ByteType]: ...
    @overload
    def DeriveKeyFromHmac(
        self,
        otherPartyPublicKey: ECDiffieHellmanPublicKey,
        hashAlgorithm: HashAlgorithmName,
        hmacKey: ArrayType[ByteType],
        secretPrepend: ArrayType[ByteType],
        secretAppend: ArrayType[ByteType],
    ) -> ArrayType[ByteType]: ...
    @overload
    def DeriveKeyMaterial(
        self, otherPartyPublicKey: ECDiffieHellmanPublicKey
    ) -> ArrayType[ByteType]: ...
    @overload
    def DeriveKeyMaterial(self, otherPartyPublicKey: CngKey) -> ArrayType[ByteType]: ...
    def DeriveKeyTls(
        self,
        otherPartyPublicKey: ECDiffieHellmanPublicKey,
        prfLabel: ArrayType[ByteType],
        prfSeed: ArrayType[ByteType],
    ) -> ArrayType[ByteType]: ...
    @overload
    def DeriveSecretAgreementHandle(
        self, otherPartyPublicKey: ECDiffieHellmanPublicKey
    ) -> SafeNCryptSecretHandle: ...
    @overload
    def DeriveSecretAgreementHandle(
        self, otherPartyPublicKey: CngKey
    ) -> SafeNCryptSecretHandle: ...
    def ExportExplicitParameters(self, includePrivateParameters: BooleanType) -> ECParameters: ...
    def ExportParameters(self, includePrivateParameters: BooleanType) -> ECParameters: ...
    @overload
    def FromXmlString(self, xmlString: StringType) -> VoidType: ...
    @overload
    def FromXmlString(self, xml: StringType, format: ECKeyXmlFormat) -> VoidType: ...
    def GenerateKey(self, curve: ECCurve) -> VoidType: ...
    def ImportParameters(self, parameters: ECParameters) -> VoidType: ...
    @overload
    def ToXmlString(self, includePrivateParameters: BooleanType) -> StringType: ...
    @overload
    def ToXmlString(self, format: ECKeyXmlFormat) -> StringType: ...
    def get_HashAlgorithm(self) -> CngAlgorithm: ...
    def get_HmacKey(self) -> ArrayType[ByteType]: ...
    def get_Key(self) -> CngKey: ...
    def get_KeyDerivationFunction(self) -> ECDiffieHellmanKeyDerivationFunction: ...
    def get_Label(self) -> ArrayType[ByteType]: ...
    def get_PublicKey(self) -> ECDiffieHellmanPublicKey: ...
    def get_SecretAppend(self) -> ArrayType[ByteType]: ...
    def get_SecretPrepend(self) -> ArrayType[ByteType]: ...
    def get_Seed(self) -> ArrayType[ByteType]: ...
    def get_UseSecretAgreementAsHmacKey(self) -> BooleanType: ...
    def set_HashAlgorithm(self, value: CngAlgorithm) -> VoidType: ...
    def set_HmacKey(self, value: ArrayType[ByteType]) -> VoidType: ...
    def set_KeyDerivationFunction(
        self, value: ECDiffieHellmanKeyDerivationFunction
    ) -> VoidType: ...
    def set_Label(self, value: ArrayType[ByteType]) -> VoidType: ...
    def set_SecretAppend(self, value: ArrayType[ByteType]) -> VoidType: ...
    def set_SecretPrepend(self, value: ArrayType[ByteType]) -> VoidType: ...
    def set_Seed(self, value: ArrayType[ByteType]) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ECDiffieHellmanCngPublicKey(ECDiffieHellmanPublicKey, IDisposable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def BlobFormat(self) -> CngKeyBlobFormat: ...

    # ---------- Methods ---------- #

    def ExportExplicitParameters(self) -> ECParameters: ...
    def ExportParameters(self) -> ECParameters: ...
    @staticmethod
    def FromByteArray(
        publicKeyBlob: ArrayType[ByteType], format: CngKeyBlobFormat
    ) -> ECDiffieHellmanPublicKey: ...
    @staticmethod
    def FromXmlString(xml: StringType) -> ECDiffieHellmanCngPublicKey: ...
    def Import(self) -> CngKey: ...
    def ToXmlString(self) -> StringType: ...
    def get_BlobFormat(self) -> CngKeyBlobFormat: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ECDiffieHellmanPublicKey(ABC, ObjectType, IDisposable):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def Dispose(self) -> VoidType: ...
    def ExportExplicitParameters(self) -> ECParameters: ...
    def ExportParameters(self) -> ECParameters: ...
    def ToByteArray(self) -> ArrayType[ByteType]: ...
    def ToXmlString(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ECDsa(ABC, AsymmetricAlgorithm, IDisposable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def KeyExchangeAlgorithm(self) -> StringType: ...
    @property
    def SignatureAlgorithm(self) -> StringType: ...

    # ---------- Methods ---------- #

    @staticmethod
    @overload
    def Create() -> ECDsa: ...
    @staticmethod
    @overload
    def Create(algorithm: StringType) -> ECDsa: ...
    @staticmethod
    @overload
    def Create(curve: ECCurve) -> ECDsa: ...
    @staticmethod
    @overload
    def Create(parameters: ECParameters) -> ECDsa: ...
    def ExportExplicitParameters(self, includePrivateParameters: BooleanType) -> ECParameters: ...
    def ExportParameters(self, includePrivateParameters: BooleanType) -> ECParameters: ...
    def GenerateKey(self, curve: ECCurve) -> VoidType: ...
    def ImportParameters(self, parameters: ECParameters) -> VoidType: ...
    @overload
    def SignData(
        self, data: ArrayType[ByteType], hashAlgorithm: HashAlgorithmName
    ) -> ArrayType[ByteType]: ...
    @overload
    def SignData(
        self,
        data: ArrayType[ByteType],
        offset: IntType,
        count: IntType,
        hashAlgorithm: HashAlgorithmName,
    ) -> ArrayType[ByteType]: ...
    @overload
    def SignData(self, data: Stream, hashAlgorithm: HashAlgorithmName) -> ArrayType[ByteType]: ...
    def SignHash(self, hash: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    @overload
    def VerifyData(
        self,
        data: ArrayType[ByteType],
        signature: ArrayType[ByteType],
        hashAlgorithm: HashAlgorithmName,
    ) -> BooleanType: ...
    @overload
    def VerifyData(
        self,
        data: ArrayType[ByteType],
        offset: IntType,
        count: IntType,
        signature: ArrayType[ByteType],
        hashAlgorithm: HashAlgorithmName,
    ) -> BooleanType: ...
    @overload
    def VerifyData(
        self, data: Stream, signature: ArrayType[ByteType], hashAlgorithm: HashAlgorithmName
    ) -> BooleanType: ...
    def VerifyHash(
        self, hash: ArrayType[ByteType], signature: ArrayType[ByteType]
    ) -> BooleanType: ...
    def get_KeyExchangeAlgorithm(self) -> StringType: ...
    def get_SignatureAlgorithm(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ECDsaCng(ECDsa, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, keySize: IntType): ...
    @overload
    def __init__(self, curve: ECCurve): ...
    @overload
    def __init__(self, key: CngKey): ...

    # ---------- Properties ---------- #

    @property
    def HashAlgorithm(self) -> CngAlgorithm: ...
    @HashAlgorithm.setter
    def HashAlgorithm(self, value: CngAlgorithm) -> None: ...
    @property
    def Key(self) -> CngKey: ...

    # ---------- Methods ---------- #

    def ExportExplicitParameters(self, includePrivateParameters: BooleanType) -> ECParameters: ...
    def ExportParameters(self, includePrivateParameters: BooleanType) -> ECParameters: ...
    @overload
    def FromXmlString(self, xmlString: StringType) -> VoidType: ...
    @overload
    def FromXmlString(self, xml: StringType, format: ECKeyXmlFormat) -> VoidType: ...
    def GenerateKey(self, curve: ECCurve) -> VoidType: ...
    def ImportParameters(self, parameters: ECParameters) -> VoidType: ...
    @overload
    def SignData(self, data: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    @overload
    def SignData(
        self, data: ArrayType[ByteType], offset: IntType, count: IntType
    ) -> ArrayType[ByteType]: ...
    @overload
    def SignData(self, data: Stream) -> ArrayType[ByteType]: ...
    def SignHash(self, hash: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    @overload
    def ToXmlString(self, includePrivateParameters: BooleanType) -> StringType: ...
    @overload
    def ToXmlString(self, format: ECKeyXmlFormat) -> StringType: ...
    @overload
    def VerifyData(
        self, data: ArrayType[ByteType], signature: ArrayType[ByteType]
    ) -> BooleanType: ...
    @overload
    def VerifyData(
        self,
        data: ArrayType[ByteType],
        offset: IntType,
        count: IntType,
        signature: ArrayType[ByteType],
    ) -> BooleanType: ...
    @overload
    def VerifyData(self, data: Stream, signature: ArrayType[ByteType]) -> BooleanType: ...
    def VerifyHash(
        self, hash: ArrayType[ByteType], signature: ArrayType[ByteType]
    ) -> BooleanType: ...
    def get_HashAlgorithm(self) -> CngAlgorithm: ...
    def get_Key(self) -> CngKey: ...
    def set_HashAlgorithm(self, value: CngAlgorithm) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class FromBase64Transform(ObjectType, ICryptoTransform, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, whitespaces: FromBase64TransformMode): ...

    # ---------- Properties ---------- #

    @property
    def CanReuseTransform(self) -> BooleanType: ...
    @property
    def CanTransformMultipleBlocks(self) -> BooleanType: ...
    @property
    def InputBlockSize(self) -> IntType: ...
    @property
    def OutputBlockSize(self) -> IntType: ...

    # ---------- Methods ---------- #

    def Clear(self) -> VoidType: ...
    def Dispose(self) -> VoidType: ...
    def TransformBlock(
        self,
        inputBuffer: ArrayType[ByteType],
        inputOffset: IntType,
        inputCount: IntType,
        outputBuffer: ArrayType[ByteType],
        outputOffset: IntType,
    ) -> IntType: ...
    def TransformFinalBlock(
        self, inputBuffer: ArrayType[ByteType], inputOffset: IntType, inputCount: IntType
    ) -> ArrayType[ByteType]: ...
    def get_CanReuseTransform(self) -> BooleanType: ...
    def get_CanTransformMultipleBlocks(self) -> BooleanType: ...
    def get_InputBlockSize(self) -> IntType: ...
    def get_OutputBlockSize(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class HMAC(ABC, KeyedHashAlgorithm, IDisposable, ICryptoTransform):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def HashName(self) -> StringType: ...
    @HashName.setter
    def HashName(self, value: StringType) -> None: ...
    @property
    def Key(self) -> ArrayType[ByteType]: ...
    @Key.setter
    def Key(self, value: ArrayType[ByteType]) -> None: ...

    # ---------- Methods ---------- #

    @staticmethod
    @overload
    def Create(algorithmName: StringType) -> HMAC: ...
    @staticmethod
    @overload
    def Create() -> HMAC: ...
    def Initialize(self) -> VoidType: ...
    def get_HashName(self) -> StringType: ...
    def get_Key(self) -> ArrayType[ByteType]: ...
    def set_HashName(self, value: StringType) -> VoidType: ...
    def set_Key(self, value: ArrayType[ByteType]) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class HMACMD5(HMAC, IDisposable, ICryptoTransform):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, key: ArrayType[ByteType]): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class HMACRIPEMD160(HMAC, IDisposable, ICryptoTransform):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, key: ArrayType[ByteType]): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class HMACSHA1(HMAC, IDisposable, ICryptoTransform):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, key: ArrayType[ByteType]): ...
    @overload
    def __init__(self, key: ArrayType[ByteType], useManagedSha1: BooleanType): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class HMACSHA256(HMAC, IDisposable, ICryptoTransform):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, key: ArrayType[ByteType]): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class HMACSHA384(HMAC, IDisposable, ICryptoTransform):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, key: ArrayType[ByteType]): ...

    # ---------- Properties ---------- #

    @property
    def ProduceLegacyHmacValues(self) -> BooleanType: ...
    @ProduceLegacyHmacValues.setter
    def ProduceLegacyHmacValues(self, value: BooleanType) -> None: ...

    # ---------- Methods ---------- #

    def get_ProduceLegacyHmacValues(self) -> BooleanType: ...
    def set_ProduceLegacyHmacValues(self, value: BooleanType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class HMACSHA512(HMAC, IDisposable, ICryptoTransform):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, key: ArrayType[ByteType]): ...

    # ---------- Properties ---------- #

    @property
    def ProduceLegacyHmacValues(self) -> BooleanType: ...
    @ProduceLegacyHmacValues.setter
    def ProduceLegacyHmacValues(self, value: BooleanType) -> None: ...

    # ---------- Methods ---------- #

    def get_ProduceLegacyHmacValues(self) -> BooleanType: ...
    def set_ProduceLegacyHmacValues(self, value: BooleanType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class HashAlgorithm(ABC, ObjectType, IDisposable, ICryptoTransform):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def CanReuseTransform(self) -> BooleanType: ...
    @property
    def CanTransformMultipleBlocks(self) -> BooleanType: ...
    @property
    def Hash(self) -> ArrayType[ByteType]: ...
    @property
    def HashSize(self) -> IntType: ...
    @property
    def InputBlockSize(self) -> IntType: ...
    @property
    def OutputBlockSize(self) -> IntType: ...

    # ---------- Methods ---------- #

    def Clear(self) -> VoidType: ...
    @overload
    def ComputeHash(self, inputStream: Stream) -> ArrayType[ByteType]: ...
    @overload
    def ComputeHash(self, buffer: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    @overload
    def ComputeHash(
        self, buffer: ArrayType[ByteType], offset: IntType, count: IntType
    ) -> ArrayType[ByteType]: ...
    @staticmethod
    @overload
    def Create(hashName: StringType) -> HashAlgorithm: ...
    @staticmethod
    @overload
    def Create() -> HashAlgorithm: ...
    def Dispose(self) -> VoidType: ...
    def Initialize(self) -> VoidType: ...
    def TransformBlock(
        self,
        inputBuffer: ArrayType[ByteType],
        inputOffset: IntType,
        inputCount: IntType,
        outputBuffer: ArrayType[ByteType],
        outputOffset: IntType,
    ) -> IntType: ...
    def TransformFinalBlock(
        self, inputBuffer: ArrayType[ByteType], inputOffset: IntType, inputCount: IntType
    ) -> ArrayType[ByteType]: ...
    def get_CanReuseTransform(self) -> BooleanType: ...
    def get_CanTransformMultipleBlocks(self) -> BooleanType: ...
    def get_Hash(self) -> ArrayType[ByteType]: ...
    def get_HashSize(self) -> IntType: ...
    def get_InputBlockSize(self) -> IntType: ...
    def get_OutputBlockSize(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class IncrementalHash(ObjectType, IDisposable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def AlgorithmName(self) -> HashAlgorithmName: ...

    # ---------- Methods ---------- #

    @overload
    def AppendData(self, data: ArrayType[ByteType]) -> VoidType: ...
    @overload
    def AppendData(
        self, data: ArrayType[ByteType], offset: IntType, count: IntType
    ) -> VoidType: ...
    @staticmethod
    def CreateHMAC(
        hashAlgorithm: HashAlgorithmName, key: ArrayType[ByteType]
    ) -> IncrementalHash: ...
    @staticmethod
    def CreateHash(hashAlgorithm: HashAlgorithmName) -> IncrementalHash: ...
    def Dispose(self) -> VoidType: ...
    def GetHashAndReset(self) -> ArrayType[ByteType]: ...
    def get_AlgorithmName(self) -> HashAlgorithmName: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class KeySizes(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, minSize: IntType, maxSize: IntType, skipSize: IntType): ...

    # ---------- Properties ---------- #

    @property
    def MaxSize(self) -> IntType: ...
    @property
    def MinSize(self) -> IntType: ...
    @property
    def SkipSize(self) -> IntType: ...

    # ---------- Methods ---------- #

    def get_MaxSize(self) -> IntType: ...
    def get_MinSize(self) -> IntType: ...
    def get_SkipSize(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class KeyedHashAlgorithm(ABC, HashAlgorithm, IDisposable, ICryptoTransform):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Key(self) -> ArrayType[ByteType]: ...
    @Key.setter
    def Key(self, value: ArrayType[ByteType]) -> None: ...

    # ---------- Methods ---------- #

    @staticmethod
    @overload
    def Create(algName: StringType) -> KeyedHashAlgorithm: ...
    @staticmethod
    @overload
    def Create() -> KeyedHashAlgorithm: ...
    def get_Key(self) -> ArrayType[ByteType]: ...
    def set_Key(self, value: ArrayType[ByteType]) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class MACTripleDES(KeyedHashAlgorithm, IDisposable, ICryptoTransform):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, rgbKey: ArrayType[ByteType]): ...
    @overload
    def __init__(self, strTripleDES: StringType, rgbKey: ArrayType[ByteType]): ...

    # ---------- Properties ---------- #

    @property
    def Padding(self) -> PaddingMode: ...
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...

    # ---------- Methods ---------- #

    def Initialize(self) -> VoidType: ...
    def get_Padding(self) -> PaddingMode: ...
    def set_Padding(self, value: PaddingMode) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class MD5(ABC, HashAlgorithm, IDisposable, ICryptoTransform):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    @overload
    def Create(algName: StringType) -> MD5: ...
    @staticmethod
    @overload
    def Create() -> MD5: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class MD5Cng(MD5, IDisposable, ICryptoTransform):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def Initialize(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class MD5CryptoServiceProvider(MD5, IDisposable, ICryptoTransform):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def Initialize(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ManifestSignatureInformation(ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def AuthenticodeSignature(self) -> AuthenticodeSignatureInformation: ...
    @property
    def Manifest(self) -> ManifestKinds: ...
    @property
    def StrongNameSignature(self) -> StrongNameSignatureInformation: ...

    # ---------- Methods ---------- #

    @staticmethod
    @overload
    def VerifySignature(
        application: ActivationContext,
    ) -> ManifestSignatureInformationCollection: ...
    @staticmethod
    @overload
    def VerifySignature(
        application: ActivationContext, manifests: ManifestKinds
    ) -> ManifestSignatureInformationCollection: ...
    @staticmethod
    @overload
    def VerifySignature(
        application: ActivationContext,
        manifests: ManifestKinds,
        revocationFlag: X509RevocationFlag,
        revocationMode: X509RevocationMode,
    ) -> ManifestSignatureInformationCollection: ...
    def get_AuthenticodeSignature(self) -> AuthenticodeSignatureInformation: ...
    def get_Manifest(self) -> ManifestKinds: ...
    def get_StrongNameSignature(self) -> StrongNameSignatureInformation: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ManifestSignatureInformationCollection(
    ReadOnlyCollection[ManifestSignatureInformation],
    IList[ManifestSignatureInformation],
    ICollection[ManifestSignatureInformation],
    IEnumerable[ManifestSignatureInformation],
    IEnumerable,
    IList,
    ICollection,
    IReadOnlyList[ManifestSignatureInformation],
    IReadOnlyCollection[ManifestSignatureInformation],
):
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

class MaskGenerationMethod(ABC, ObjectType):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def GenerateMask(
        self, rgbSeed: ArrayType[ByteType], cbReturn: IntType
    ) -> ArrayType[ByteType]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class NCryptNative(ABC, ObjectType):
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

class Oid(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, oid: StringType): ...
    @overload
    def __init__(self, value: StringType, friendlyName: StringType): ...
    @overload
    def __init__(self, oid: Oid): ...

    # ---------- Properties ---------- #

    @property
    def FriendlyName(self) -> StringType: ...
    @FriendlyName.setter
    def FriendlyName(self, value: StringType) -> None: ...
    @property
    def Value(self) -> StringType: ...
    @Value.setter
    def Value(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    @staticmethod
    def FromFriendlyName(friendlyName: StringType, group: OidGroup) -> Oid: ...
    @staticmethod
    def FromOidValue(oidValue: StringType, group: OidGroup) -> Oid: ...
    def get_FriendlyName(self) -> StringType: ...
    def get_Value(self) -> StringType: ...
    def set_FriendlyName(self, value: StringType) -> VoidType: ...
    def set_Value(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class OidCollection(ObjectType, ICollection, IEnumerable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def Count(self) -> IntType: ...
    @property
    def IsSynchronized(self) -> BooleanType: ...
    def __getitem__(self, key: IntType) -> Oid: ...
    def __getitem__(self, key: StringType) -> Oid: ...
    @property
    def SyncRoot(self) -> ObjectType: ...

    # ---------- Methods ---------- #

    def Add(self, oid: Oid) -> IntType: ...
    def CopyTo(self, array: ArrayType[Oid], index: IntType) -> VoidType: ...
    def GetEnumerator(self) -> OidEnumerator: ...
    def get_Count(self) -> IntType: ...
    def get_IsSynchronized(self) -> BooleanType: ...
    @overload
    def get_Item(self, index: IntType) -> Oid: ...
    @overload
    def get_Item(self, oid: StringType) -> Oid: ...
    def get_SyncRoot(self) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class OidEnumerator(ObjectType, IEnumerator):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Current(self) -> Oid: ...

    # ---------- Methods ---------- #

    def MoveNext(self) -> BooleanType: ...
    def Reset(self) -> VoidType: ...
    def get_Current(self) -> Oid: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class PKCS1MaskGenerationMethod(MaskGenerationMethod):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def HashName(self) -> StringType: ...
    @HashName.setter
    def HashName(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    def GenerateMask(
        self, rgbSeed: ArrayType[ByteType], cbReturn: IntType
    ) -> ArrayType[ByteType]: ...
    def get_HashName(self) -> StringType: ...
    def set_HashName(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class PasswordDeriveBytes(DeriveBytes, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, strPassword: StringType, rgbSalt: ArrayType[ByteType]): ...
    @overload
    def __init__(self, password: ArrayType[ByteType], salt: ArrayType[ByteType]): ...
    @overload
    def __init__(
        self,
        strPassword: StringType,
        rgbSalt: ArrayType[ByteType],
        strHashName: StringType,
        iterations: IntType,
    ): ...
    @overload
    def __init__(
        self,
        password: ArrayType[ByteType],
        salt: ArrayType[ByteType],
        hashName: StringType,
        iterations: IntType,
    ): ...
    @overload
    def __init__(
        self, strPassword: StringType, rgbSalt: ArrayType[ByteType], cspParams: CspParameters
    ): ...
    @overload
    def __init__(
        self, password: ArrayType[ByteType], salt: ArrayType[ByteType], cspParams: CspParameters
    ): ...
    @overload
    def __init__(
        self,
        strPassword: StringType,
        rgbSalt: ArrayType[ByteType],
        strHashName: StringType,
        iterations: IntType,
        cspParams: CspParameters,
    ): ...
    @overload
    def __init__(
        self,
        password: ArrayType[ByteType],
        salt: ArrayType[ByteType],
        hashName: StringType,
        iterations: IntType,
        cspParams: CspParameters,
    ): ...

    # ---------- Properties ---------- #

    @property
    def HashName(self) -> StringType: ...
    @HashName.setter
    def HashName(self, value: StringType) -> None: ...
    @property
    def IterationCount(self) -> IntType: ...
    @IterationCount.setter
    def IterationCount(self, value: IntType) -> None: ...
    @property
    def Salt(self) -> ArrayType[ByteType]: ...
    @Salt.setter
    def Salt(self, value: ArrayType[ByteType]) -> None: ...

    # ---------- Methods ---------- #

    def CryptDeriveKey(
        self,
        algname: StringType,
        alghashname: StringType,
        keySize: IntType,
        rgbIV: ArrayType[ByteType],
    ) -> ArrayType[ByteType]: ...
    def GetBytes(self, cb: IntType) -> ArrayType[ByteType]: ...
    def Reset(self) -> VoidType: ...
    def get_HashName(self) -> StringType: ...
    def get_IterationCount(self) -> IntType: ...
    def get_Salt(self) -> ArrayType[ByteType]: ...
    def set_HashName(self, value: StringType) -> VoidType: ...
    def set_IterationCount(self, value: IntType) -> VoidType: ...
    def set_Salt(self, value: ArrayType[ByteType]) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ProtectedData(ABC, ObjectType):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    def Protect(
        userData: ArrayType[ByteType],
        optionalEntropy: ArrayType[ByteType],
        scope: DataProtectionScope,
    ) -> ArrayType[ByteType]: ...
    @staticmethod
    def Unprotect(
        encryptedData: ArrayType[ByteType],
        optionalEntropy: ArrayType[ByteType],
        scope: DataProtectionScope,
    ) -> ArrayType[ByteType]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ProtectedMemory(ABC, ObjectType):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    def Protect(userData: ArrayType[ByteType], scope: MemoryProtectionScope) -> VoidType: ...
    @staticmethod
    def Unprotect(encryptedData: ArrayType[ByteType], scope: MemoryProtectionScope) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RC2(ABC, SymmetricAlgorithm, IDisposable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def EffectiveKeySize(self) -> IntType: ...
    @EffectiveKeySize.setter
    def EffectiveKeySize(self, value: IntType) -> None: ...
    @property
    def KeySize(self) -> IntType: ...
    @KeySize.setter
    def KeySize(self, value: IntType) -> None: ...

    # ---------- Methods ---------- #

    @staticmethod
    @overload
    def Create(AlgName: StringType) -> RC2: ...
    @staticmethod
    @overload
    def Create() -> RC2: ...
    def get_EffectiveKeySize(self) -> IntType: ...
    def get_KeySize(self) -> IntType: ...
    def set_EffectiveKeySize(self, value: IntType) -> VoidType: ...
    def set_KeySize(self, value: IntType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RC2CryptoServiceProvider(RC2, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def EffectiveKeySize(self) -> IntType: ...
    @EffectiveKeySize.setter
    def EffectiveKeySize(self, value: IntType) -> None: ...
    @property
    def UseSalt(self) -> BooleanType: ...
    @UseSalt.setter
    def UseSalt(self, value: BooleanType) -> None: ...

    # ---------- Methods ---------- #

    @overload
    def CreateDecryptor(
        self, rgbKey: ArrayType[ByteType], rgbIV: ArrayType[ByteType]
    ) -> ICryptoTransform: ...
    @overload
    def CreateEncryptor(
        self, rgbKey: ArrayType[ByteType], rgbIV: ArrayType[ByteType]
    ) -> ICryptoTransform: ...
    def GenerateIV(self) -> VoidType: ...
    def GenerateKey(self) -> VoidType: ...
    def get_EffectiveKeySize(self) -> IntType: ...
    def get_UseSalt(self) -> BooleanType: ...
    def set_EffectiveKeySize(self, value: IntType) -> VoidType: ...
    def set_UseSalt(self, value: BooleanType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RIPEMD160(ABC, HashAlgorithm, IDisposable, ICryptoTransform):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    @overload
    def Create(hashName: StringType) -> RIPEMD160: ...
    @staticmethod
    @overload
    def Create() -> RIPEMD160: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RIPEMD160Managed(RIPEMD160, IDisposable, ICryptoTransform):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def Initialize(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RNGCryptoServiceProvider(RandomNumberGenerator, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, str: StringType): ...
    @overload
    def __init__(self, rgb: ArrayType[ByteType]): ...
    @overload
    def __init__(self, cspParams: CspParameters): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def GetBytes(self, data: ArrayType[ByteType]) -> VoidType: ...
    def GetNonZeroBytes(self, data: ArrayType[ByteType]) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RSA(ABC, AsymmetricAlgorithm, IDisposable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def KeyExchangeAlgorithm(self) -> StringType: ...
    @property
    def SignatureAlgorithm(self) -> StringType: ...

    # ---------- Methods ---------- #

    @staticmethod
    @overload
    def Create(algName: StringType) -> RSA: ...
    @staticmethod
    @overload
    def Create() -> RSA: ...
    @staticmethod
    @overload
    def Create(keySizeInBits: IntType) -> RSA: ...
    @staticmethod
    @overload
    def Create(parameters: RSAParameters) -> RSA: ...
    def Decrypt(
        self, data: ArrayType[ByteType], padding: RSAEncryptionPadding
    ) -> ArrayType[ByteType]: ...
    def DecryptValue(self, rgb: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    def Encrypt(
        self, data: ArrayType[ByteType], padding: RSAEncryptionPadding
    ) -> ArrayType[ByteType]: ...
    def EncryptValue(self, rgb: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    def ExportParameters(self, includePrivateParameters: BooleanType) -> RSAParameters: ...
    def FromXmlString(self, xmlString: StringType) -> VoidType: ...
    def ImportParameters(self, parameters: RSAParameters) -> VoidType: ...
    @overload
    def SignData(
        self,
        data: ArrayType[ByteType],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> ArrayType[ByteType]: ...
    @overload
    def SignData(
        self,
        data: ArrayType[ByteType],
        offset: IntType,
        count: IntType,
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> ArrayType[ByteType]: ...
    @overload
    def SignData(
        self, data: Stream, hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding
    ) -> ArrayType[ByteType]: ...
    def SignHash(
        self,
        hash: ArrayType[ByteType],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> ArrayType[ByteType]: ...
    def ToXmlString(self, includePrivateParameters: BooleanType) -> StringType: ...
    @overload
    def VerifyData(
        self,
        data: ArrayType[ByteType],
        signature: ArrayType[ByteType],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> BooleanType: ...
    @overload
    def VerifyData(
        self,
        data: ArrayType[ByteType],
        offset: IntType,
        count: IntType,
        signature: ArrayType[ByteType],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> BooleanType: ...
    @overload
    def VerifyData(
        self,
        data: Stream,
        signature: ArrayType[ByteType],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> BooleanType: ...
    def VerifyHash(
        self,
        hash: ArrayType[ByteType],
        signature: ArrayType[ByteType],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> BooleanType: ...
    def get_KeyExchangeAlgorithm(self) -> StringType: ...
    def get_SignatureAlgorithm(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RSACng(RSA, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, keySize: IntType): ...
    @overload
    def __init__(self, key: CngKey): ...

    # ---------- Properties ---------- #

    @property
    def Key(self) -> CngKey: ...
    @property
    def KeyExchangeAlgorithm(self) -> StringType: ...
    @property
    def SignatureAlgorithm(self) -> StringType: ...

    # ---------- Methods ---------- #

    def Decrypt(
        self, data: ArrayType[ByteType], padding: RSAEncryptionPadding
    ) -> ArrayType[ByteType]: ...
    def DecryptValue(self, rgb: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    def Encrypt(
        self, data: ArrayType[ByteType], padding: RSAEncryptionPadding
    ) -> ArrayType[ByteType]: ...
    def EncryptValue(self, rgb: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    def ExportParameters(self, includePrivateParameters: BooleanType) -> RSAParameters: ...
    def ImportParameters(self, parameters: RSAParameters) -> VoidType: ...
    def SignHash(
        self,
        hash: ArrayType[ByteType],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> ArrayType[ByteType]: ...
    def VerifyHash(
        self,
        hash: ArrayType[ByteType],
        signature: ArrayType[ByteType],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> BooleanType: ...
    def get_Key(self) -> CngKey: ...
    def get_KeyExchangeAlgorithm(self) -> StringType: ...
    def get_SignatureAlgorithm(self) -> StringType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RSACryptoServiceProvider(RSA, IDisposable, ICspAsymmetricAlgorithm):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, dwKeySize: IntType): ...
    @overload
    def __init__(self, parameters: CspParameters): ...
    @overload
    def __init__(self, dwKeySize: IntType, parameters: CspParameters): ...

    # ---------- Properties ---------- #

    @property
    def CspKeyContainerInfo(self) -> CspKeyContainerInfo: ...
    @property
    def KeyExchangeAlgorithm(self) -> StringType: ...
    @property
    def KeySize(self) -> IntType: ...
    @property
    def PersistKeyInCsp(self) -> BooleanType: ...
    @PersistKeyInCsp.setter
    def PersistKeyInCsp(self, value: BooleanType) -> None: ...
    @property
    def PublicOnly(self) -> BooleanType: ...
    @property
    def SignatureAlgorithm(self) -> StringType: ...
    @staticmethod
    @property
    def UseMachineKeyStore() -> BooleanType: ...
    @staticmethod
    @UseMachineKeyStore.setter
    def UseMachineKeyStore(value: BooleanType) -> None: ...

    # ---------- Methods ---------- #

    @overload
    def Decrypt(self, rgb: ArrayType[ByteType], fOAEP: BooleanType) -> ArrayType[ByteType]: ...
    @overload
    def Decrypt(
        self, data: ArrayType[ByteType], padding: RSAEncryptionPadding
    ) -> ArrayType[ByteType]: ...
    def DecryptValue(self, rgb: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    @overload
    def Encrypt(self, rgb: ArrayType[ByteType], fOAEP: BooleanType) -> ArrayType[ByteType]: ...
    @overload
    def Encrypt(
        self, data: ArrayType[ByteType], padding: RSAEncryptionPadding
    ) -> ArrayType[ByteType]: ...
    def EncryptValue(self, rgb: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    def ExportCspBlob(self, includePrivateParameters: BooleanType) -> ArrayType[ByteType]: ...
    def ExportParameters(self, includePrivateParameters: BooleanType) -> RSAParameters: ...
    def ImportCspBlob(self, keyBlob: ArrayType[ByteType]) -> VoidType: ...
    def ImportParameters(self, parameters: RSAParameters) -> VoidType: ...
    @overload
    def SignData(self, inputStream: Stream, halg: ObjectType) -> ArrayType[ByteType]: ...
    @overload
    def SignData(self, buffer: ArrayType[ByteType], halg: ObjectType) -> ArrayType[ByteType]: ...
    @overload
    def SignData(
        self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, halg: ObjectType
    ) -> ArrayType[ByteType]: ...
    @overload
    def SignHash(self, rgbHash: ArrayType[ByteType], str: StringType) -> ArrayType[ByteType]: ...
    @overload
    def SignHash(
        self,
        hash: ArrayType[ByteType],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> ArrayType[ByteType]: ...
    @overload
    def VerifyData(
        self, buffer: ArrayType[ByteType], halg: ObjectType, signature: ArrayType[ByteType]
    ) -> BooleanType: ...
    @overload
    def VerifyHash(
        self, rgbHash: ArrayType[ByteType], str: StringType, rgbSignature: ArrayType[ByteType]
    ) -> BooleanType: ...
    @overload
    def VerifyHash(
        self,
        hash: ArrayType[ByteType],
        signature: ArrayType[ByteType],
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> BooleanType: ...
    def get_CspKeyContainerInfo(self) -> CspKeyContainerInfo: ...
    def get_KeyExchangeAlgorithm(self) -> StringType: ...
    def get_KeySize(self) -> IntType: ...
    def get_PersistKeyInCsp(self) -> BooleanType: ...
    def get_PublicOnly(self) -> BooleanType: ...
    def get_SignatureAlgorithm(self) -> StringType: ...
    @staticmethod
    def get_UseMachineKeyStore() -> BooleanType: ...
    def set_PersistKeyInCsp(self, value: BooleanType) -> VoidType: ...
    @staticmethod
    def set_UseMachineKeyStore(value: BooleanType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RSACspObject(ObjectType):
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

class RSAEncryptionPadding(ObjectType, IEquatable[RSAEncryptionPadding]):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Mode(self) -> RSAEncryptionPaddingMode: ...
    @property
    def OaepHashAlgorithm(self) -> HashAlgorithmName: ...
    @staticmethod
    @property
    def OaepSHA1() -> RSAEncryptionPadding: ...
    @staticmethod
    @property
    def OaepSHA256() -> RSAEncryptionPadding: ...
    @staticmethod
    @property
    def OaepSHA384() -> RSAEncryptionPadding: ...
    @staticmethod
    @property
    def OaepSHA512() -> RSAEncryptionPadding: ...
    @staticmethod
    @property
    def Pkcs1() -> RSAEncryptionPadding: ...

    # ---------- Methods ---------- #

    @staticmethod
    def CreateOaep(hashAlgorithm: HashAlgorithmName) -> RSAEncryptionPadding: ...
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    @overload
    def Equals(self, other: RSAEncryptionPadding) -> BooleanType: ...
    def GetHashCode(self) -> IntType: ...
    def ToString(self) -> StringType: ...
    def get_Mode(self) -> RSAEncryptionPaddingMode: ...
    def get_OaepHashAlgorithm(self) -> HashAlgorithmName: ...
    @staticmethod
    def get_OaepSHA1() -> RSAEncryptionPadding: ...
    @staticmethod
    def get_OaepSHA256() -> RSAEncryptionPadding: ...
    @staticmethod
    def get_OaepSHA384() -> RSAEncryptionPadding: ...
    @staticmethod
    def get_OaepSHA512() -> RSAEncryptionPadding: ...
    @staticmethod
    def get_Pkcs1() -> RSAEncryptionPadding: ...
    @staticmethod
    def op_Equality(left: RSAEncryptionPadding, right: RSAEncryptionPadding) -> BooleanType: ...
    @staticmethod
    def op_Inequality(left: RSAEncryptionPadding, right: RSAEncryptionPadding) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RSAOAEPKeyExchangeDeformatter(AsymmetricKeyExchangeDeformatter):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, key: AsymmetricAlgorithm): ...

    # ---------- Properties ---------- #

    @property
    def Parameters(self) -> StringType: ...
    @Parameters.setter
    def Parameters(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    def DecryptKeyExchange(self, rgbData: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    def SetKey(self, key: AsymmetricAlgorithm) -> VoidType: ...
    def get_Parameters(self) -> StringType: ...
    def set_Parameters(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RSAOAEPKeyExchangeFormatter(AsymmetricKeyExchangeFormatter):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, key: AsymmetricAlgorithm): ...

    # ---------- Properties ---------- #

    @property
    def Parameter(self) -> ArrayType[ByteType]: ...
    @Parameter.setter
    def Parameter(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def Parameters(self) -> StringType: ...
    @property
    def Rng(self) -> RandomNumberGenerator: ...
    @Rng.setter
    def Rng(self, value: RandomNumberGenerator) -> None: ...

    # ---------- Methods ---------- #

    @overload
    def CreateKeyExchange(
        self, rgbData: ArrayType[ByteType], symAlgType: TypeType
    ) -> ArrayType[ByteType]: ...
    @overload
    def CreateKeyExchange(self, rgbData: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    def SetKey(self, key: AsymmetricAlgorithm) -> VoidType: ...
    def get_Parameter(self) -> ArrayType[ByteType]: ...
    def get_Parameters(self) -> StringType: ...
    def get_Rng(self) -> RandomNumberGenerator: ...
    def set_Parameter(self, value: ArrayType[ByteType]) -> VoidType: ...
    def set_Rng(self, value: RandomNumberGenerator) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RSAPKCS1KeyExchangeDeformatter(AsymmetricKeyExchangeDeformatter):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, key: AsymmetricAlgorithm): ...

    # ---------- Properties ---------- #

    @property
    def Parameters(self) -> StringType: ...
    @Parameters.setter
    def Parameters(self, value: StringType) -> None: ...
    @property
    def RNG(self) -> RandomNumberGenerator: ...
    @RNG.setter
    def RNG(self, value: RandomNumberGenerator) -> None: ...

    # ---------- Methods ---------- #

    def DecryptKeyExchange(self, rgbIn: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    def SetKey(self, key: AsymmetricAlgorithm) -> VoidType: ...
    def get_Parameters(self) -> StringType: ...
    def get_RNG(self) -> RandomNumberGenerator: ...
    def set_Parameters(self, value: StringType) -> VoidType: ...
    def set_RNG(self, value: RandomNumberGenerator) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RSAPKCS1KeyExchangeFormatter(AsymmetricKeyExchangeFormatter):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, key: AsymmetricAlgorithm): ...

    # ---------- Properties ---------- #

    @property
    def Parameters(self) -> StringType: ...
    @property
    def Rng(self) -> RandomNumberGenerator: ...
    @Rng.setter
    def Rng(self, value: RandomNumberGenerator) -> None: ...

    # ---------- Methods ---------- #

    @overload
    def CreateKeyExchange(
        self, rgbData: ArrayType[ByteType], symAlgType: TypeType
    ) -> ArrayType[ByteType]: ...
    @overload
    def CreateKeyExchange(self, rgbData: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    def SetKey(self, key: AsymmetricAlgorithm) -> VoidType: ...
    def get_Parameters(self) -> StringType: ...
    def get_Rng(self) -> RandomNumberGenerator: ...
    def set_Rng(self, value: RandomNumberGenerator) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RSAPKCS1SHA1SignatureDescription(RSAPKCS1SignatureDescription):
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

class RSAPKCS1SHA256SignatureDescription(RSAPKCS1SignatureDescription):
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

class RSAPKCS1SHA384SignatureDescription(RSAPKCS1SignatureDescription):
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

class RSAPKCS1SHA512SignatureDescription(RSAPKCS1SignatureDescription):
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

class RSAPKCS1SignatureDeformatter(AsymmetricSignatureDeformatter):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, key: AsymmetricAlgorithm): ...

    # No Properties

    # ---------- Methods ---------- #

    def SetHashAlgorithm(self, strName: StringType) -> VoidType: ...
    def SetKey(self, key: AsymmetricAlgorithm) -> VoidType: ...
    @overload
    def VerifySignature(
        self, rgbHash: ArrayType[ByteType], rgbSignature: ArrayType[ByteType]
    ) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RSAPKCS1SignatureDescription(ABC, SignatureDescription):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def CreateDeformatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureDeformatter: ...
    def CreateFormatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureFormatter: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RSAPKCS1SignatureFormatter(AsymmetricSignatureFormatter):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, key: AsymmetricAlgorithm): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def CreateSignature(self, rgbHash: ArrayType[ByteType]) -> ArrayType[ByteType]: ...
    def SetHashAlgorithm(self, strName: StringType) -> VoidType: ...
    def SetKey(self, key: AsymmetricAlgorithm) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RSASignaturePadding(ObjectType, IEquatable[RSASignaturePadding]):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Mode(self) -> RSASignaturePaddingMode: ...
    @staticmethod
    @property
    def Pkcs1() -> RSASignaturePadding: ...
    @staticmethod
    @property
    def Pss() -> RSASignaturePadding: ...

    # ---------- Methods ---------- #

    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    @overload
    def Equals(self, other: RSASignaturePadding) -> BooleanType: ...
    def GetHashCode(self) -> IntType: ...
    def ToString(self) -> StringType: ...
    def get_Mode(self) -> RSASignaturePaddingMode: ...
    @staticmethod
    def get_Pkcs1() -> RSASignaturePadding: ...
    @staticmethod
    def get_Pss() -> RSASignaturePadding: ...
    @staticmethod
    def op_Equality(left: RSASignaturePadding, right: RSASignaturePadding) -> BooleanType: ...
    @staticmethod
    def op_Inequality(left: RSASignaturePadding, right: RSASignaturePadding) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RandomNumberGenerator(ABC, ObjectType, IDisposable):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    @overload
    def Create() -> RandomNumberGenerator: ...
    @staticmethod
    @overload
    def Create(rngName: StringType) -> RandomNumberGenerator: ...
    def Dispose(self) -> VoidType: ...
    @overload
    def GetBytes(self, data: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    @overload
    def GetBytes(self, data: ArrayType[ByteType]) -> VoidType: ...
    def GetNonZeroBytes(self, data: ArrayType[ByteType]) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Rfc2898DeriveBytes(DeriveBytes, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self, password: StringType, saltSize: IntType): ...
    @overload
    def __init__(self, password: StringType, saltSize: IntType, iterations: IntType): ...
    @overload
    def __init__(
        self,
        password: StringType,
        saltSize: IntType,
        iterations: IntType,
        hashAlgorithm: HashAlgorithmName,
    ): ...
    @overload
    def __init__(self, password: StringType, salt: ArrayType[ByteType]): ...
    @overload
    def __init__(self, password: StringType, salt: ArrayType[ByteType], iterations: IntType): ...
    @overload
    def __init__(
        self,
        password: StringType,
        salt: ArrayType[ByteType],
        iterations: IntType,
        hashAlgorithm: HashAlgorithmName,
    ): ...
    @overload
    def __init__(
        self, password: ArrayType[ByteType], salt: ArrayType[ByteType], iterations: IntType
    ): ...
    @overload
    def __init__(
        self,
        password: ArrayType[ByteType],
        salt: ArrayType[ByteType],
        iterations: IntType,
        hashAlgorithm: HashAlgorithmName,
    ): ...

    # ---------- Properties ---------- #

    @property
    def IterationCount(self) -> IntType: ...
    @IterationCount.setter
    def IterationCount(self, value: IntType) -> None: ...
    @property
    def Salt(self) -> ArrayType[ByteType]: ...
    @Salt.setter
    def Salt(self, value: ArrayType[ByteType]) -> None: ...

    # ---------- Methods ---------- #

    def CryptDeriveKey(
        self,
        algname: StringType,
        alghashname: StringType,
        keySize: IntType,
        rgbIV: ArrayType[ByteType],
    ) -> ArrayType[ByteType]: ...
    def GetBytes(self, cb: IntType) -> ArrayType[ByteType]: ...
    def Reset(self) -> VoidType: ...
    def get_IterationCount(self) -> IntType: ...
    def get_Salt(self) -> ArrayType[ByteType]: ...
    def set_IterationCount(self, value: IntType) -> VoidType: ...
    def set_Salt(self, value: ArrayType[ByteType]) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Rfc4050KeyFormatter(ABC, ObjectType):
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

class Rijndael(ABC, SymmetricAlgorithm, IDisposable):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    @overload
    def Create(algName: StringType) -> Rijndael: ...
    @staticmethod
    @overload
    def Create() -> Rijndael: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RijndaelManaged(Rijndael, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def CreateDecryptor(
        self, rgbKey: ArrayType[ByteType], rgbIV: ArrayType[ByteType]
    ) -> ICryptoTransform: ...
    @overload
    def CreateEncryptor(
        self, rgbKey: ArrayType[ByteType], rgbIV: ArrayType[ByteType]
    ) -> ICryptoTransform: ...
    def GenerateIV(self) -> VoidType: ...
    def GenerateKey(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RijndaelManagedTransform(ObjectType, ICryptoTransform, IDisposable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def BlockSizeValue(self) -> IntType: ...
    @property
    def CanReuseTransform(self) -> BooleanType: ...
    @property
    def CanTransformMultipleBlocks(self) -> BooleanType: ...
    @property
    def InputBlockSize(self) -> IntType: ...
    @property
    def OutputBlockSize(self) -> IntType: ...

    # ---------- Methods ---------- #

    def Clear(self) -> VoidType: ...
    def Dispose(self) -> VoidType: ...
    def Reset(self) -> VoidType: ...
    def TransformBlock(
        self,
        inputBuffer: ArrayType[ByteType],
        inputOffset: IntType,
        inputCount: IntType,
        outputBuffer: ArrayType[ByteType],
        outputOffset: IntType,
    ) -> IntType: ...
    def TransformFinalBlock(
        self, inputBuffer: ArrayType[ByteType], inputOffset: IntType, inputCount: IntType
    ) -> ArrayType[ByteType]: ...
    def get_BlockSizeValue(self) -> IntType: ...
    def get_CanReuseTransform(self) -> BooleanType: ...
    def get_CanTransformMultipleBlocks(self) -> BooleanType: ...
    def get_InputBlockSize(self) -> IntType: ...
    def get_OutputBlockSize(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SHA1(ABC, HashAlgorithm, IDisposable, ICryptoTransform):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    @overload
    def Create(hashName: StringType) -> SHA1: ...
    @staticmethod
    @overload
    def Create() -> SHA1: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SHA1Cng(SHA1, IDisposable, ICryptoTransform):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def Initialize(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SHA1CryptoServiceProvider(SHA1, IDisposable, ICryptoTransform):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def Initialize(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SHA1Managed(SHA1, IDisposable, ICryptoTransform):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def Initialize(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SHA256(ABC, HashAlgorithm, IDisposable, ICryptoTransform):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    @overload
    def Create(hashName: StringType) -> SHA256: ...
    @staticmethod
    @overload
    def Create() -> SHA256: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SHA256Cng(SHA256, IDisposable, ICryptoTransform):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def Initialize(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SHA256CryptoServiceProvider(SHA256, IDisposable, ICryptoTransform):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def Initialize(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SHA256Managed(SHA256, IDisposable, ICryptoTransform):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def Initialize(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SHA384(ABC, HashAlgorithm, IDisposable, ICryptoTransform):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    @overload
    def Create(hashName: StringType) -> SHA384: ...
    @staticmethod
    @overload
    def Create() -> SHA384: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SHA384Cng(SHA384, IDisposable, ICryptoTransform):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def Initialize(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SHA384CryptoServiceProvider(SHA384, IDisposable, ICryptoTransform):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def Initialize(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SHA384Managed(SHA384, IDisposable, ICryptoTransform):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def Initialize(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SHA512(ABC, HashAlgorithm, IDisposable, ICryptoTransform):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    @overload
    def Create(hashName: StringType) -> SHA512: ...
    @staticmethod
    @overload
    def Create() -> SHA512: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SHA512Cng(SHA512, IDisposable, ICryptoTransform):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def Initialize(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SHA512CryptoServiceProvider(SHA512, IDisposable, ICryptoTransform):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def Initialize(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SHA512Managed(SHA512, IDisposable, ICryptoTransform):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def Initialize(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SafeCertChainHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

class SafeCertContextHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

class SafeCertStoreHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

class SafeCryptMsgHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

class SafeCryptProvHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

class SafeCspHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

class SafeCspHashHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

class SafeCspKeyHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

class SafeHashHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

class SafeKeyHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

class SafeLibraryHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

class SafeLocalAllocHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

class SafeProvHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
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

class SignatureDescription(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, el: SecurityElement): ...

    # ---------- Properties ---------- #

    @property
    def DeformatterAlgorithm(self) -> StringType: ...
    @DeformatterAlgorithm.setter
    def DeformatterAlgorithm(self, value: StringType) -> None: ...
    @property
    def DigestAlgorithm(self) -> StringType: ...
    @DigestAlgorithm.setter
    def DigestAlgorithm(self, value: StringType) -> None: ...
    @property
    def FormatterAlgorithm(self) -> StringType: ...
    @FormatterAlgorithm.setter
    def FormatterAlgorithm(self, value: StringType) -> None: ...
    @property
    def KeyAlgorithm(self) -> StringType: ...
    @KeyAlgorithm.setter
    def KeyAlgorithm(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    def CreateDeformatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureDeformatter: ...
    def CreateDigest(self) -> HashAlgorithm: ...
    def CreateFormatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureFormatter: ...
    def get_DeformatterAlgorithm(self) -> StringType: ...
    def get_DigestAlgorithm(self) -> StringType: ...
    def get_FormatterAlgorithm(self) -> StringType: ...
    def get_KeyAlgorithm(self) -> StringType: ...
    def set_DeformatterAlgorithm(self, value: StringType) -> VoidType: ...
    def set_DigestAlgorithm(self, value: StringType) -> VoidType: ...
    def set_FormatterAlgorithm(self, value: StringType) -> VoidType: ...
    def set_KeyAlgorithm(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class StrongNameSignatureInformation(ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def HResult(self) -> IntType: ...
    @property
    def HashAlgorithm(self) -> StringType: ...
    @property
    def IsValid(self) -> BooleanType: ...
    @property
    def PublicKey(self) -> AsymmetricAlgorithm: ...
    @property
    def VerificationResult(self) -> SignatureVerificationResult: ...

    # ---------- Methods ---------- #

    def get_HResult(self) -> IntType: ...
    def get_HashAlgorithm(self) -> StringType: ...
    def get_IsValid(self) -> BooleanType: ...
    def get_PublicKey(self) -> AsymmetricAlgorithm: ...
    def get_VerificationResult(self) -> SignatureVerificationResult: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SymmetricAlgorithm(ABC, ObjectType, IDisposable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def BlockSize(self) -> IntType: ...
    @BlockSize.setter
    def BlockSize(self, value: IntType) -> None: ...
    @property
    def FeedbackSize(self) -> IntType: ...
    @FeedbackSize.setter
    def FeedbackSize(self, value: IntType) -> None: ...
    @property
    def IV(self) -> ArrayType[ByteType]: ...
    @IV.setter
    def IV(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def Key(self) -> ArrayType[ByteType]: ...
    @Key.setter
    def Key(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def KeySize(self) -> IntType: ...
    @KeySize.setter
    def KeySize(self, value: IntType) -> None: ...
    @property
    def LegalBlockSizes(self) -> ArrayType[KeySizes]: ...
    @property
    def LegalKeySizes(self) -> ArrayType[KeySizes]: ...
    @property
    def Mode(self) -> CipherMode: ...
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    @property
    def Padding(self) -> PaddingMode: ...
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...

    # ---------- Methods ---------- #

    def Clear(self) -> VoidType: ...
    @staticmethod
    @overload
    def Create(algName: StringType) -> SymmetricAlgorithm: ...
    @staticmethod
    @overload
    def Create() -> SymmetricAlgorithm: ...
    @overload
    def CreateDecryptor(self) -> ICryptoTransform: ...
    @overload
    def CreateDecryptor(
        self, rgbKey: ArrayType[ByteType], rgbIV: ArrayType[ByteType]
    ) -> ICryptoTransform: ...
    @overload
    def CreateEncryptor(self) -> ICryptoTransform: ...
    @overload
    def CreateEncryptor(
        self, rgbKey: ArrayType[ByteType], rgbIV: ArrayType[ByteType]
    ) -> ICryptoTransform: ...
    def Dispose(self) -> VoidType: ...
    def GenerateIV(self) -> VoidType: ...
    def GenerateKey(self) -> VoidType: ...
    def ValidKeySize(self, bitLength: IntType) -> BooleanType: ...
    def get_BlockSize(self) -> IntType: ...
    def get_FeedbackSize(self) -> IntType: ...
    def get_IV(self) -> ArrayType[ByteType]: ...
    def get_Key(self) -> ArrayType[ByteType]: ...
    def get_KeySize(self) -> IntType: ...
    def get_LegalBlockSizes(self) -> ArrayType[KeySizes]: ...
    def get_LegalKeySizes(self) -> ArrayType[KeySizes]: ...
    def get_Mode(self) -> CipherMode: ...
    def get_Padding(self) -> PaddingMode: ...
    def set_BlockSize(self, value: IntType) -> VoidType: ...
    def set_FeedbackSize(self, value: IntType) -> VoidType: ...
    def set_IV(self, value: ArrayType[ByteType]) -> VoidType: ...
    def set_Key(self, value: ArrayType[ByteType]) -> VoidType: ...
    def set_KeySize(self, value: IntType) -> VoidType: ...
    def set_Mode(self, value: CipherMode) -> VoidType: ...
    def set_Padding(self, value: PaddingMode) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class TailStream(Stream, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, bufferSize: IntType): ...

    # ---------- Properties ---------- #

    @property
    def Buffer(self) -> ArrayType[ByteType]: ...
    @property
    def CanRead(self) -> BooleanType: ...
    @property
    def CanSeek(self) -> BooleanType: ...
    @property
    def CanWrite(self) -> BooleanType: ...
    @property
    def Length(self) -> LongType: ...
    @property
    def Position(self) -> LongType: ...
    @Position.setter
    def Position(self, value: LongType) -> None: ...

    # ---------- Methods ---------- #

    def Clear(self) -> VoidType: ...
    def Flush(self) -> VoidType: ...
    def Read(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    def Seek(self, offset: LongType, origin: SeekOrigin) -> LongType: ...
    def SetLength(self, value: LongType) -> VoidType: ...
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    def get_Buffer(self) -> ArrayType[ByteType]: ...
    def get_CanRead(self) -> BooleanType: ...
    def get_CanSeek(self) -> BooleanType: ...
    def get_CanWrite(self) -> BooleanType: ...
    def get_Length(self) -> LongType: ...
    def get_Position(self) -> LongType: ...
    def set_Position(self, value: LongType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ToBase64Transform(ObjectType, ICryptoTransform, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def CanReuseTransform(self) -> BooleanType: ...
    @property
    def CanTransformMultipleBlocks(self) -> BooleanType: ...
    @property
    def InputBlockSize(self) -> IntType: ...
    @property
    def OutputBlockSize(self) -> IntType: ...

    # ---------- Methods ---------- #

    def Clear(self) -> VoidType: ...
    def Dispose(self) -> VoidType: ...
    def TransformBlock(
        self,
        inputBuffer: ArrayType[ByteType],
        inputOffset: IntType,
        inputCount: IntType,
        outputBuffer: ArrayType[ByteType],
        outputOffset: IntType,
    ) -> IntType: ...
    def TransformFinalBlock(
        self, inputBuffer: ArrayType[ByteType], inputOffset: IntType, inputCount: IntType
    ) -> ArrayType[ByteType]: ...
    def get_CanReuseTransform(self) -> BooleanType: ...
    def get_CanTransformMultipleBlocks(self) -> BooleanType: ...
    def get_InputBlockSize(self) -> IntType: ...
    def get_OutputBlockSize(self) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class TripleDES(ABC, SymmetricAlgorithm, IDisposable):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Key(self) -> ArrayType[ByteType]: ...
    @Key.setter
    def Key(self, value: ArrayType[ByteType]) -> None: ...

    # ---------- Methods ---------- #

    @staticmethod
    @overload
    def Create(str: StringType) -> TripleDES: ...
    @staticmethod
    @overload
    def Create() -> TripleDES: ...
    @staticmethod
    def IsWeakKey(rgbKey: ArrayType[ByteType]) -> BooleanType: ...
    def get_Key(self) -> ArrayType[ByteType]: ...
    def set_Key(self, value: ArrayType[ByteType]) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class TripleDESCng(TripleDES, IDisposable, ICngSymmetricAlgorithm):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, keyName: StringType): ...
    @overload
    def __init__(self, keyName: StringType, provider: CngProvider): ...
    @overload
    def __init__(
        self, keyName: StringType, provider: CngProvider, openOptions: CngKeyOpenOptions
    ): ...

    # ---------- Properties ---------- #

    @property
    def Key(self) -> ArrayType[ByteType]: ...
    @Key.setter
    def Key(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def KeySize(self) -> IntType: ...
    @KeySize.setter
    def KeySize(self, value: IntType) -> None: ...

    # ---------- Methods ---------- #

    @overload
    def CreateDecryptor(self) -> ICryptoTransform: ...
    @overload
    def CreateDecryptor(
        self, rgbKey: ArrayType[ByteType], rgbIV: ArrayType[ByteType]
    ) -> ICryptoTransform: ...
    @overload
    def CreateEncryptor(self) -> ICryptoTransform: ...
    @overload
    def CreateEncryptor(
        self, rgbKey: ArrayType[ByteType], rgbIV: ArrayType[ByteType]
    ) -> ICryptoTransform: ...
    def GenerateIV(self) -> VoidType: ...
    def GenerateKey(self) -> VoidType: ...
    def get_Key(self) -> ArrayType[ByteType]: ...
    def get_KeySize(self) -> IntType: ...
    def set_Key(self, value: ArrayType[ByteType]) -> VoidType: ...
    def set_KeySize(self, value: IntType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class TripleDESCryptoServiceProvider(TripleDES, IDisposable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    @overload
    def CreateDecryptor(
        self, rgbKey: ArrayType[ByteType], rgbIV: ArrayType[ByteType]
    ) -> ICryptoTransform: ...
    @overload
    def CreateEncryptor(
        self, rgbKey: ArrayType[ByteType], rgbIV: ArrayType[ByteType]
    ) -> ICryptoTransform: ...
    def GenerateIV(self) -> VoidType: ...
    def GenerateKey(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Utils(ABC, ObjectType):
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

class X509Utils(ObjectType):
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

# ---------- Structs ---------- #

class BCRYPT_DSA_KEY_BLOB_V2(ValueType):
    # ---------- Fields ---------- #

    @property
    def Count0(self) -> ByteType: ...
    @Count0.setter
    def Count0(self, value: ByteType) -> None: ...
    @property
    def Count1(self) -> ByteType: ...
    @Count1.setter
    def Count1(self, value: ByteType) -> None: ...
    @property
    def Count2(self) -> ByteType: ...
    @Count2.setter
    def Count2(self, value: ByteType) -> None: ...
    @property
    def Count3(self) -> ByteType: ...
    @Count3.setter
    def Count3(self, value: ByteType) -> None: ...
    @property
    def cbGroupSize(self) -> IntType: ...
    @cbGroupSize.setter
    def cbGroupSize(self, value: IntType) -> None: ...
    @property
    def cbKey(self) -> IntType: ...
    @cbKey.setter
    def cbKey(self, value: IntType) -> None: ...
    @property
    def cbSeedLength(self) -> IntType: ...
    @cbSeedLength.setter
    def cbSeedLength(self, value: IntType) -> None: ...
    @property
    def dwMagic(self) -> KeyBlobMagicNumber: ...
    @dwMagic.setter
    def dwMagic(self, value: KeyBlobMagicNumber) -> None: ...
    @property
    def hashAlgorithm(self) -> HASHALGORITHM_ENUM: ...
    @hashAlgorithm.setter
    def hashAlgorithm(self, value: HASHALGORITHM_ENUM) -> None: ...
    @property
    def standardVersion(self) -> DSAFIPSVERSION_ENUM: ...
    @standardVersion.setter
    def standardVersion(self, value: DSAFIPSVERSION_ENUM) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CngProperty(ValueType, IEquatable[CngProperty]):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(
        self, name: StringType, value: ArrayType[ByteType], options: CngPropertyOptions
    ): ...

    # ---------- Properties ---------- #

    @property
    def Name(self) -> StringType: ...
    @property
    def Options(self) -> CngPropertyOptions: ...

    # ---------- Methods ---------- #

    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    @overload
    def Equals(self, other: CngProperty) -> BooleanType: ...
    def GetHashCode(self) -> IntType: ...
    def GetValue(self) -> ArrayType[ByteType]: ...
    def get_Name(self) -> StringType: ...
    def get_Options(self) -> CngPropertyOptions: ...
    @staticmethod
    def op_Equality(left: CngProperty, right: CngProperty) -> BooleanType: ...
    @staticmethod
    def op_Inequality(left: CngProperty, right: CngProperty) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class DSAParameters(ValueType):
    # ---------- Fields ---------- #

    @property
    def Counter(self) -> IntType: ...
    @Counter.setter
    def Counter(self, value: IntType) -> None: ...
    @property
    def G(self) -> ArrayType[ByteType]: ...
    @G.setter
    def G(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def J(self) -> ArrayType[ByteType]: ...
    @J.setter
    def J(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def P(self) -> ArrayType[ByteType]: ...
    @P.setter
    def P(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def Q(self) -> ArrayType[ByteType]: ...
    @Q.setter
    def Q(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def Seed(self) -> ArrayType[ByteType]: ...
    @Seed.setter
    def Seed(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def X(self) -> ArrayType[ByteType]: ...
    @X.setter
    def X(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def Y(self) -> ArrayType[ByteType]: ...
    @Y.setter
    def Y(self, value: ArrayType[ByteType]) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ECCurve(ValueType):
    # ---------- Fields ---------- #

    @property
    def A(self) -> ArrayType[ByteType]: ...
    @A.setter
    def A(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def B(self) -> ArrayType[ByteType]: ...
    @B.setter
    def B(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def Cofactor(self) -> ArrayType[ByteType]: ...
    @Cofactor.setter
    def Cofactor(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def CurveType(self) -> ECCurveType: ...
    @CurveType.setter
    def CurveType(self, value: ECCurveType) -> None: ...
    @property
    def G(self) -> ECPoint: ...
    @G.setter
    def G(self, value: ECPoint) -> None: ...
    @property
    def Hash(self) -> NullableType[Nullable[HashAlgorithmName]]: ...
    @Hash.setter
    def Hash(self, value: NullableType[Nullable[HashAlgorithmName]]) -> None: ...
    @property
    def Order(self) -> ArrayType[ByteType]: ...
    @Order.setter
    def Order(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def Polynomial(self) -> ArrayType[ByteType]: ...
    @Polynomial.setter
    def Polynomial(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def Prime(self) -> ArrayType[ByteType]: ...
    @Prime.setter
    def Prime(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def Seed(self) -> ArrayType[ByteType]: ...
    @Seed.setter
    def Seed(self, value: ArrayType[ByteType]) -> None: ...

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def IsCharacteristic2(self) -> BooleanType: ...
    @property
    def IsExplicit(self) -> BooleanType: ...
    @property
    def IsNamed(self) -> BooleanType: ...
    @property
    def IsPrime(self) -> BooleanType: ...
    @property
    def Oid(self) -> Oid: ...

    # ---------- Methods ---------- #

    @staticmethod
    def CreateFromFriendlyName(oidFriendlyName: StringType) -> ECCurve: ...
    @staticmethod
    def CreateFromOid(curveOid: Oid) -> ECCurve: ...
    @staticmethod
    def CreateFromValue(oidValue: StringType) -> ECCurve: ...
    def Validate(self) -> VoidType: ...
    def get_IsCharacteristic2(self) -> BooleanType: ...
    def get_IsExplicit(self) -> BooleanType: ...
    def get_IsNamed(self) -> BooleanType: ...
    def get_IsPrime(self) -> BooleanType: ...
    def get_Oid(self) -> Oid: ...

    # No Events

    # ---------- Sub Classes ---------- #

    class NamedCurves(ABC, ObjectType):
        # No Fields

        # No Constructors

        # ---------- Properties ---------- #

        @staticmethod
        @property
        def brainpoolP160r1() -> ECCurve: ...
        @staticmethod
        @property
        def brainpoolP160t1() -> ECCurve: ...
        @staticmethod
        @property
        def brainpoolP192r1() -> ECCurve: ...
        @staticmethod
        @property
        def brainpoolP192t1() -> ECCurve: ...
        @staticmethod
        @property
        def brainpoolP224r1() -> ECCurve: ...
        @staticmethod
        @property
        def brainpoolP224t1() -> ECCurve: ...
        @staticmethod
        @property
        def brainpoolP256r1() -> ECCurve: ...
        @staticmethod
        @property
        def brainpoolP256t1() -> ECCurve: ...
        @staticmethod
        @property
        def brainpoolP320r1() -> ECCurve: ...
        @staticmethod
        @property
        def brainpoolP320t1() -> ECCurve: ...
        @staticmethod
        @property
        def brainpoolP384r1() -> ECCurve: ...
        @staticmethod
        @property
        def brainpoolP384t1() -> ECCurve: ...
        @staticmethod
        @property
        def brainpoolP512r1() -> ECCurve: ...
        @staticmethod
        @property
        def brainpoolP512t1() -> ECCurve: ...
        @staticmethod
        @property
        def nistP256() -> ECCurve: ...
        @staticmethod
        @property
        def nistP384() -> ECCurve: ...
        @staticmethod
        @property
        def nistP521() -> ECCurve: ...

        # ---------- Methods ---------- #

        @staticmethod
        def get_brainpoolP160r1() -> ECCurve: ...
        @staticmethod
        def get_brainpoolP160t1() -> ECCurve: ...
        @staticmethod
        def get_brainpoolP192r1() -> ECCurve: ...
        @staticmethod
        def get_brainpoolP192t1() -> ECCurve: ...
        @staticmethod
        def get_brainpoolP224r1() -> ECCurve: ...
        @staticmethod
        def get_brainpoolP224t1() -> ECCurve: ...
        @staticmethod
        def get_brainpoolP256r1() -> ECCurve: ...
        @staticmethod
        def get_brainpoolP256t1() -> ECCurve: ...
        @staticmethod
        def get_brainpoolP320r1() -> ECCurve: ...
        @staticmethod
        def get_brainpoolP320t1() -> ECCurve: ...
        @staticmethod
        def get_brainpoolP384r1() -> ECCurve: ...
        @staticmethod
        def get_brainpoolP384t1() -> ECCurve: ...
        @staticmethod
        def get_brainpoolP512r1() -> ECCurve: ...
        @staticmethod
        def get_brainpoolP512t1() -> ECCurve: ...
        @staticmethod
        def get_nistP256() -> ECCurve: ...
        @staticmethod
        def get_nistP384() -> ECCurve: ...
        @staticmethod
        def get_nistP521() -> ECCurve: ...

        # No Events

        # No Sub Classes

        # No Sub Structs

        # No Sub Interfaces

        # No Sub Enums
    # No Sub Structs

    # No Sub Interfaces

    # ---------- Sub Enums ---------- #

    class ECCurveType(Enum):
        Implicit = 0
        PrimeShortWeierstrass = 1
        PrimeTwistedEdwards = 2
        PrimeMontgomery = 3
        Characteristic2 = 4
        Named = 5

class ECParameters(ValueType):
    # ---------- Fields ---------- #

    @property
    def Curve(self) -> ECCurve: ...
    @Curve.setter
    def Curve(self, value: ECCurve) -> None: ...
    @property
    def D(self) -> ArrayType[ByteType]: ...
    @D.setter
    def D(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def Q(self) -> ECPoint: ...
    @Q.setter
    def Q(self, value: ECPoint) -> None: ...

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def Validate(self) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ECPoint(ValueType):
    # ---------- Fields ---------- #

    @property
    def X(self) -> ArrayType[ByteType]: ...
    @X.setter
    def X(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def Y(self) -> ArrayType[ByteType]: ...
    @Y.setter
    def Y(self, value: ArrayType[ByteType]) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class HashAlgorithmName(ValueType, IEquatable[HashAlgorithmName]):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, name: StringType): ...

    # ---------- Properties ---------- #

    @staticmethod
    @property
    def MD5() -> HashAlgorithmName: ...
    @property
    def Name(self) -> StringType: ...
    @staticmethod
    @property
    def SHA1() -> HashAlgorithmName: ...
    @staticmethod
    @property
    def SHA256() -> HashAlgorithmName: ...
    @staticmethod
    @property
    def SHA384() -> HashAlgorithmName: ...
    @staticmethod
    @property
    def SHA512() -> HashAlgorithmName: ...

    # ---------- Methods ---------- #

    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    @overload
    def Equals(self, other: HashAlgorithmName) -> BooleanType: ...
    def GetHashCode(self) -> IntType: ...
    def ToString(self) -> StringType: ...
    @staticmethod
    def get_MD5() -> HashAlgorithmName: ...
    def get_Name(self) -> StringType: ...
    @staticmethod
    def get_SHA1() -> HashAlgorithmName: ...
    @staticmethod
    def get_SHA256() -> HashAlgorithmName: ...
    @staticmethod
    def get_SHA384() -> HashAlgorithmName: ...
    @staticmethod
    def get_SHA512() -> HashAlgorithmName: ...
    @staticmethod
    def op_Equality(left: HashAlgorithmName, right: HashAlgorithmName) -> BooleanType: ...
    @staticmethod
    def op_Inequality(left: HashAlgorithmName, right: HashAlgorithmName) -> BooleanType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RSAParameters(ValueType):
    # ---------- Fields ---------- #

    @property
    def D(self) -> ArrayType[ByteType]: ...
    @D.setter
    def D(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def DP(self) -> ArrayType[ByteType]: ...
    @DP.setter
    def DP(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def DQ(self) -> ArrayType[ByteType]: ...
    @DQ.setter
    def DQ(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def Exponent(self) -> ArrayType[ByteType]: ...
    @Exponent.setter
    def Exponent(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def InverseQ(self) -> ArrayType[ByteType]: ...
    @InverseQ.setter
    def InverseQ(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def Modulus(self) -> ArrayType[ByteType]: ...
    @Modulus.setter
    def Modulus(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def P(self) -> ArrayType[ByteType]: ...
    @P.setter
    def P(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def Q(self) -> ArrayType[ByteType]: ...
    @Q.setter
    def Q(self, value: ArrayType[ByteType]) -> None: ...

    # No Constructors

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

# ---------- Interfaces ---------- #

class ICryptoTransform(Protocol, IDisposable):
    # ---------- Properties ---------- #

    @property
    def CanReuseTransform(self) -> BooleanType: ...
    @property
    def CanTransformMultipleBlocks(self) -> BooleanType: ...
    @property
    def InputBlockSize(self) -> IntType: ...
    @property
    def OutputBlockSize(self) -> IntType: ...

    # ---------- Methods ---------- #

    def TransformBlock(
        self,
        inputBuffer: ArrayType[ByteType],
        inputOffset: IntType,
        inputCount: IntType,
        outputBuffer: ArrayType[ByteType],
        outputOffset: IntType,
    ) -> IntType: ...
    def TransformFinalBlock(
        self, inputBuffer: ArrayType[ByteType], inputOffset: IntType, inputCount: IntType
    ) -> ArrayType[ByteType]: ...
    def get_CanReuseTransform(self) -> BooleanType: ...
    def get_CanTransformMultipleBlocks(self) -> BooleanType: ...
    def get_InputBlockSize(self) -> IntType: ...
    def get_OutputBlockSize(self) -> IntType: ...

    # No Events

class ICspAsymmetricAlgorithm(Protocol):
    # ---------- Properties ---------- #

    @property
    def CspKeyContainerInfo(self) -> CspKeyContainerInfo: ...

    # ---------- Methods ---------- #

    def ExportCspBlob(self, includePrivateParameters: BooleanType) -> ArrayType[ByteType]: ...
    def ImportCspBlob(self, rawData: ArrayType[ByteType]) -> VoidType: ...
    def get_CspKeyContainerInfo(self) -> CspKeyContainerInfo: ...

    # No Events

# ---------- Enums ---------- #

class AsymmetricPaddingMode(Enum):
    # None = 1
    Pkcs1 = 2
    Oaep = 4
    Pss = 8

class CipherMode(Enum):
    CBC = 1
    ECB = 2
    OFB = 3
    CFB = 4
    CTS = 5

class CngExportPolicies(Enum):
    # None = 0
    AllowExport = 1
    AllowPlaintextExport = 2
    AllowArchiving = 4
    AllowPlaintextArchiving = 8

class CngKeyCreationOptions(Enum):
    # None = 0
    MachineKey = 32
    OverwriteExistingKey = 128

class CngKeyHandleOpenOptions(Enum):
    # None = 0
    EphemeralKey = 1

class CngKeyOpenOptions(Enum):
    # None = 0
    UserKey = 0
    MachineKey = 32
    Silent = 64

class CngKeyTypes(Enum):
    # None = 0
    MachineKey = 32

class CngKeyUsages(Enum):
    # None = 0
    Decryption = 1
    Signing = 2
    KeyAgreement = 4
    AllUsages = 16777215

class CngPropertyOptions(Enum):
    Persist = -2147483648
    # None = 0
    CustomProperty = 1073741824

class CngUIProtectionLevels(Enum):
    # None = 0
    ProtectKey = 1
    ForceHighProtection = 2

class CryptoAPITransformMode(Enum):
    Encrypt = 0
    Decrypt = 1

class CryptoStreamMode(Enum):
    Read = 0
    Write = 1

class CspAlgorithmType(Enum):
    Rsa = 0
    Dss = 1

class CspProviderFlags(Enum):
    NoFlags = 0
    UseMachineKeyStore = 1
    UseDefaultKeyContainer = 2
    UseNonExportableKey = 4
    UseExistingKey = 8
    UseArchivableKey = 16
    UseUserProtectedKey = 32
    NoPrompt = 64
    CreateEphemeralKey = 128

class DSAFIPSVERSION_ENUM(Enum):
    DSA_FIPS186_2 = 0
    DSA_FIPS186_3 = 1

class DataProtectionScope(Enum):
    CurrentUser = 0
    LocalMachine = 1

class ECDiffieHellmanKeyDerivationFunction(Enum):
    Hash = 0
    Hmac = 1
    Tls = 2

class ECKeyXmlFormat(Enum):
    Rfc4050 = 0

class EncryptionMode(Enum):
    Encrypt = 0
    Decrypt = 1

class FromBase64TransformMode(Enum):
    IgnoreWhiteSpaces = 0
    DoNotIgnoreWhiteSpaces = 1

class HASHALGORITHM_ENUM(Enum):
    DSA_HASH_ALGORITHM_SHA1 = 0
    DSA_HASH_ALGORITHM_SHA256 = 1
    DSA_HASH_ALGORITHM_SHA512 = 2

class KeyNumber(Enum):
    Exchange = 1
    Signature = 2

class MemoryProtectionScope(Enum):
    SameProcess = 0
    CrossProcess = 1
    SameLogon = 2

class OidGroup(Enum):
    All = 0
    HashAlgorithm = 1
    EncryptionAlgorithm = 2
    PublicKeyAlgorithm = 3
    SignatureAlgorithm = 4
    Attribute = 5
    ExtensionOrAttribute = 6
    EnhancedKeyUsage = 7
    Policy = 8
    Template = 9
    KeyDerivationFunction = 10

class PaddingMode(Enum):
    # None = 1
    PKCS7 = 2
    Zeros = 3
    ANSIX923 = 4
    ISO10126 = 5

class RSAEncryptionPaddingMode(Enum):
    Pkcs1 = 0
    Oaep = 1

class RSASignaturePaddingMode(Enum):
    Pkcs1 = 0
    Pss = 1

class RijndaelManagedTransformMode(Enum):
    Encrypt = 0
    Decrypt = 1

class SignatureVerificationResult(Enum):
    SystemError = -2146869247
    InvalidSignerCertificate = -2146869246
    InvalidCountersignature = -2146869245
    InvalidCertificateSignature = -2146869244
    InvalidTimestamp = -2146869243
    BadDigest = -2146869232
    BasicConstraintsNotObserved = -2146869223
    UnknownTrustProvider = -2146762751
    UnknownVerificationAction = -2146762750
    BadSignatureFormat = -2146762749
    CertificateNotExplicitlyTrusted = -2146762748
    MissingSignature = -2146762496
    CertificateExpired = -2146762495
    InvalidTimePeriodNesting = -2146762494
    InvalidCertificateRole = -2146762493
    PathLengthConstraintViolated = -2146762492
    UnknownCriticalExtension = -2146762491
    CertificateUsageNotAllowed = -2146762490
    IssuerChainingError = -2146762489
    CertificateMalformed = -2146762488
    UntrustedRootCertificate = -2146762487
    CouldNotBuildChain = -2146762486
    GenericTrustFailure = -2146762485
    CertificateRevoked = -2146762484
    UntrustedTestRootCertificate = -2146762483
    RevocationCheckFailure = -2146762482
    InvalidCertificateUsage = -2146762480
    CertificateExplicitlyDistrusted = -2146762479
    UntrustedCertificationAuthority = -2146762478
    InvalidCertificatePolicy = -2146762477
    InvalidCertificateName = -2146762476
    Valid = 0
    AssemblyIdentityMismatch = 1
    ContainingSignatureInvalid = 2
    PublicKeyTokenMismatch = 3
    PublisherMismatch = 4

# No Delegates

__all__ = [
    Aes,
    AesCng,
    AesCryptoServiceProvider,
    AesManaged,
    AsnEncodedData,
    AsnEncodedDataCollection,
    AsnEncodedDataEnumerator,
    AsymmetricAlgorithm,
    AsymmetricKeyExchangeDeformatter,
    AsymmetricKeyExchangeFormatter,
    AsymmetricSignatureDeformatter,
    AsymmetricSignatureFormatter,
    BCryptAlgorithmHandleCache,
    BCryptHashAlgorithm,
    BCryptNative,
    BigInt,
    CAPI,
    CAPIBase,
    CAPIMethods,
    CAPINative,
    CAPISafe,
    CAPIUnsafe,
    CapiHashAlgorithm,
    CapiNative,
    CapiSymmetricAlgorithm,
    CngAlgorithm,
    CngAlgorithmGroup,
    CngKey,
    CngKeyBlobFormat,
    CngKeyCreationParameters,
    CngLightup,
    CngPropertyCollection,
    CngProvider,
    CngUIPolicy,
    Constants,
    CryptoAPITransform,
    CryptoConfig,
    CryptoStream,
    CryptographicAttributeObject,
    CryptographicAttributeObjectCollection,
    CryptographicAttributeObjectEnumerator,
    CryptographicException,
    CryptographicUnexpectedOperationException,
    CspKeyContainerInfo,
    CspParameters,
    DES,
    DESCryptoServiceProvider,
    DSA,
    DSACng,
    DSACryptoServiceProvider,
    DSACspObject,
    DSASignatureDeformatter,
    DSASignatureDescription,
    DSASignatureFormatter,
    DataProtector,
    DeriveBytes,
    DpapiDataProtector,
    ECCng,
    ECDiffieHellman,
    ECDiffieHellmanCng,
    ECDiffieHellmanCngPublicKey,
    ECDiffieHellmanPublicKey,
    ECDsa,
    ECDsaCng,
    FromBase64Transform,
    HMAC,
    HMACMD5,
    HMACRIPEMD160,
    HMACSHA1,
    HMACSHA256,
    HMACSHA384,
    HMACSHA512,
    HashAlgorithm,
    IncrementalHash,
    KeySizes,
    KeyedHashAlgorithm,
    MACTripleDES,
    MD5,
    MD5Cng,
    MD5CryptoServiceProvider,
    ManifestSignatureInformation,
    ManifestSignatureInformationCollection,
    MaskGenerationMethod,
    NCryptNative,
    Oid,
    OidCollection,
    OidEnumerator,
    PKCS1MaskGenerationMethod,
    PasswordDeriveBytes,
    ProtectedData,
    ProtectedMemory,
    RC2,
    RC2CryptoServiceProvider,
    RIPEMD160,
    RIPEMD160Managed,
    RNGCryptoServiceProvider,
    RSA,
    RSACng,
    RSACryptoServiceProvider,
    RSACspObject,
    RSAEncryptionPadding,
    RSAOAEPKeyExchangeDeformatter,
    RSAOAEPKeyExchangeFormatter,
    RSAPKCS1KeyExchangeDeformatter,
    RSAPKCS1KeyExchangeFormatter,
    RSAPKCS1SHA1SignatureDescription,
    RSAPKCS1SHA256SignatureDescription,
    RSAPKCS1SHA384SignatureDescription,
    RSAPKCS1SHA512SignatureDescription,
    RSAPKCS1SignatureDeformatter,
    RSAPKCS1SignatureDescription,
    RSAPKCS1SignatureFormatter,
    RSASignaturePadding,
    RandomNumberGenerator,
    Rfc2898DeriveBytes,
    Rfc4050KeyFormatter,
    Rijndael,
    RijndaelManaged,
    RijndaelManagedTransform,
    SHA1,
    SHA1Cng,
    SHA1CryptoServiceProvider,
    SHA1Managed,
    SHA256,
    SHA256Cng,
    SHA256CryptoServiceProvider,
    SHA256Managed,
    SHA384,
    SHA384Cng,
    SHA384CryptoServiceProvider,
    SHA384Managed,
    SHA512,
    SHA512Cng,
    SHA512CryptoServiceProvider,
    SHA512Managed,
    SafeCertChainHandle,
    SafeCertContextHandle,
    SafeCertStoreHandle,
    SafeCryptMsgHandle,
    SafeCryptProvHandle,
    SafeCspHandle,
    SafeCspHashHandle,
    SafeCspKeyHandle,
    SafeHashHandle,
    SafeKeyHandle,
    SafeLibraryHandle,
    SafeLocalAllocHandle,
    SafeProvHandle,
    SignatureDescription,
    StrongNameSignatureInformation,
    SymmetricAlgorithm,
    TailStream,
    ToBase64Transform,
    TripleDES,
    TripleDESCng,
    TripleDESCryptoServiceProvider,
    Utils,
    X509Utils,
    BCRYPT_DSA_KEY_BLOB_V2,
    CngProperty,
    DSAParameters,
    ECCurve,
    ECParameters,
    ECPoint,
    HashAlgorithmName,
    RSAParameters,
    ICryptoTransform,
    ICspAsymmetricAlgorithm,
    AsymmetricPaddingMode,
    CipherMode,
    CngExportPolicies,
    CngKeyCreationOptions,
    CngKeyHandleOpenOptions,
    CngKeyOpenOptions,
    CngKeyTypes,
    CngKeyUsages,
    CngPropertyOptions,
    CngUIProtectionLevels,
    CryptoAPITransformMode,
    CryptoStreamMode,
    CspAlgorithmType,
    CspProviderFlags,
    DSAFIPSVERSION_ENUM,
    DataProtectionScope,
    ECDiffieHellmanKeyDerivationFunction,
    ECKeyXmlFormat,
    EncryptionMode,
    FromBase64TransformMode,
    HASHALGORITHM_ENUM,
    KeyNumber,
    MemoryProtectionScope,
    OidGroup,
    PaddingMode,
    RSAEncryptionPaddingMode,
    RSASignaturePaddingMode,
    RijndaelManagedTransformMode,
    SignatureVerificationResult,
]
