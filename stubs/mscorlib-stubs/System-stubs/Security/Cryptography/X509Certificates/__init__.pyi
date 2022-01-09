from __future__ import annotations

from abc import ABC
from typing import List, Union, overload

from Microsoft.Win32.SafeHandles import SafeHandleZeroOrMinusOneIsInvalid
from System import Array, Boolean, Byte, Enum, IDisposable, Int32, IntPtr, Object, String, ValueType, Void
from System.Runtime.Serialization import IDeserializationCallback, ISerializable, SerializationInfo, StreamingContext
from System.Security import SecureString
from System.Security.Cryptography import HashAlgorithmName

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

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


class X509Certificate(ObjectType, IDisposable, IDeserializationCallback, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, data: ArrayType[ByteType]): ...
    
    @overload
    def __init__(self, rawData: ArrayType[ByteType], password: StringType): ...
    
    @overload
    def __init__(self, rawData: ArrayType[ByteType], password: SecureString): ...
    
    @overload
    def __init__(self, rawData: ArrayType[ByteType], password: StringType, keyStorageFlags: X509KeyStorageFlags): ...
    
    @overload
    def __init__(self, rawData: ArrayType[ByteType], password: SecureString, keyStorageFlags: X509KeyStorageFlags): ...
    
    @overload
    def __init__(self, fileName: StringType): ...
    
    @overload
    def __init__(self, fileName: StringType, password: StringType): ...
    
    @overload
    def __init__(self, fileName: StringType, password: SecureString): ...
    
    @overload
    def __init__(self, fileName: StringType, password: StringType, keyStorageFlags: X509KeyStorageFlags): ...
    
    @overload
    def __init__(self, fileName: StringType, password: SecureString, keyStorageFlags: X509KeyStorageFlags): ...
    
    @overload
    def __init__(self, handle: NIntType): ...
    
    @overload
    def __init__(self, cert: X509Certificate): ...
    
    @overload
    def __init__(self, info: SerializationInfo, context: StreamingContext): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Handle(self) -> NIntType: ...
    
    @property
    def Issuer(self) -> StringType: ...
    
    @property
    def Subject(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CreateFromCertFile(filename: StringType) -> X509Certificate: ...
    
    @staticmethod
    def CreateFromSignedFile(filename: StringType) -> X509Certificate: ...
    
    def Dispose(self) -> VoidType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: X509Certificate) -> BooleanType: ...
    
    @overload
    def Export(self, contentType: X509ContentType) -> ArrayType[ByteType]: ...
    
    @overload
    def Export(self, contentType: X509ContentType, password: StringType) -> ArrayType[ByteType]: ...
    
    @overload
    def Export(self, contentType: X509ContentType, password: SecureString) -> ArrayType[ByteType]: ...
    
    @overload
    def GetCertHash(self) -> ArrayType[ByteType]: ...
    
    @overload
    def GetCertHash(self, hashAlgorithm: HashAlgorithmName) -> ArrayType[ByteType]: ...
    
    @overload
    def GetCertHashString(self) -> StringType: ...
    
    @overload
    def GetCertHashString(self, hashAlgorithm: HashAlgorithmName) -> StringType: ...
    
    def GetEffectiveDateString(self) -> StringType: ...
    
    def GetExpirationDateString(self) -> StringType: ...
    
    def GetFormat(self) -> StringType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetIssuerName(self) -> StringType: ...
    
    def GetKeyAlgorithm(self) -> StringType: ...
    
    def GetKeyAlgorithmParameters(self) -> ArrayType[ByteType]: ...
    
    def GetKeyAlgorithmParametersString(self) -> StringType: ...
    
    def GetName(self) -> StringType: ...
    
    def GetPublicKey(self) -> ArrayType[ByteType]: ...
    
    def GetPublicKeyString(self) -> StringType: ...
    
    def GetRawCertData(self) -> ArrayType[ByteType]: ...
    
    def GetRawCertDataString(self) -> StringType: ...
    
    def GetSerialNumber(self) -> ArrayType[ByteType]: ...
    
    def GetSerialNumberString(self) -> StringType: ...
    
    @overload
    def Import(self, rawData: ArrayType[ByteType]) -> VoidType: ...
    
    @overload
    def Import(self, rawData: ArrayType[ByteType], password: StringType, keyStorageFlags: X509KeyStorageFlags) -> VoidType: ...
    
    @overload
    def Import(self, rawData: ArrayType[ByteType], password: SecureString, keyStorageFlags: X509KeyStorageFlags) -> VoidType: ...
    
    @overload
    def Import(self, fileName: StringType) -> VoidType: ...
    
    @overload
    def Import(self, fileName: StringType, password: StringType, keyStorageFlags: X509KeyStorageFlags) -> VoidType: ...
    
    @overload
    def Import(self, fileName: StringType, password: SecureString, keyStorageFlags: X509KeyStorageFlags) -> VoidType: ...
    
    def Reset(self) -> VoidType: ...
    
    @overload
    def ToString(self) -> StringType: ...
    
    @overload
    def ToString(self, fVerbose: BooleanType) -> StringType: ...
    
    def get_Handle(self) -> NIntType: ...
    
    def get_Issuer(self) -> StringType: ...
    
    def get_Subject(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class X509Constants(ABC, ObjectType):
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


class X509Utils(ABC, ObjectType):
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

class CRYPT_OID_INFO(ValueType):
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

class OidGroup(Enum):
    DisableSearchDS: IntType = -2147483648
    AllGroups: IntType = 0
    HashAlgorithm: IntType = 1
    EncryptionAlgorithm: IntType = 2
    PublicKeyAlgorithm: IntType = 3
    SignatureAlgorithm: IntType = 4
    Attribute: IntType = 5
    ExtensionOrAttribute: IntType = 6
    EnhancedKeyUsage: IntType = 7
    Policy: IntType = 8
    Template: IntType = 9
    KeyDerivationFunction: IntType = 10


class OidKeyType(Enum):
    Oid: IntType = 1
    Name: IntType = 2
    AlgorithmID: IntType = 3
    SignatureID: IntType = 4
    CngAlgorithmID: IntType = 5
    CngSignatureID: IntType = 6


class X509ContentType(Enum):
    Unknown: IntType = 0
    Cert: IntType = 1
    SerializedCert: IntType = 2
    Pfx: IntType = 3
    Pkcs12: IntType = 3
    SerializedStore: IntType = 4
    Pkcs7: IntType = 5
    Authenticode: IntType = 6


class X509KeyStorageFlags(Enum):
    DefaultKeySet: IntType = 0
    UserKeySet: IntType = 1
    MachineKeySet: IntType = 2
    Exportable: IntType = 4
    UserProtected: IntType = 8
    PersistKeySet: IntType = 16
    EphemeralKeySet: IntType = 32


# No Delegates

__all__ = [
    SafeCertContextHandle,
    SafeCertStoreHandle,
    X509Certificate,
    X509Constants,
    X509Utils,
    CRYPT_OID_INFO,
    OidGroup,
    OidKeyType,
    X509ContentType,
    X509KeyStorageFlags,
]
