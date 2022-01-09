from __future__ import annotations

from typing import List, Union, overload

from Microsoft.Win32.SafeHandles import SafeX509ChainHandle
from System import Array, Boolean, Byte, DateTime, Enum, IDisposable, Int32, IntPtr, Object, String, TimeSpan, ValueType, Void
from System.Collections import CollectionBase, ICollection, IEnumerable, IEnumerator, IList
from System.Runtime.Serialization import IDeserializationCallback, ISerializable
from System.Security import SecureString
from System.Security.Cryptography import AsnEncodedData, AsymmetricAlgorithm, Oid, OidCollection
from System.Security.Cryptography.X509Certificates import X509Certificate, X509ContentType, X509KeyStorageFlags

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

class PublicKey(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, oid: Oid, parameters: AsnEncodedData, keyValue: AsnEncodedData): ...
    
    # ---------- Properties ---------- #
    
    @property
    def EncodedKeyValue(self) -> AsnEncodedData: ...
    
    @property
    def EncodedParameters(self) -> AsnEncodedData: ...
    
    @property
    def Key(self) -> AsymmetricAlgorithm: ...
    
    @property
    def Oid(self) -> Oid: ...
    
    # ---------- Methods ---------- #
    
    def get_EncodedKeyValue(self) -> AsnEncodedData: ...
    
    def get_EncodedParameters(self) -> AsnEncodedData: ...
    
    def get_Key(self) -> AsymmetricAlgorithm: ...
    
    def get_Oid(self) -> Oid: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class X500DistinguishedName(AsnEncodedData):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, encodedDistinguishedName: ArrayType[ByteType]): ...
    
    @overload
    def __init__(self, encodedDistinguishedName: AsnEncodedData): ...
    
    @overload
    def __init__(self, distinguishedName: X500DistinguishedName): ...
    
    @overload
    def __init__(self, distinguishedName: StringType): ...
    
    @overload
    def __init__(self, distinguishedName: StringType, flag: X500DistinguishedNameFlags): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def Decode(self, flag: X500DistinguishedNameFlags) -> StringType: ...
    
    def Format(self, multiLine: BooleanType) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class X509BasicConstraintsExtension(X509Extension):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, certificateAuthority: BooleanType, hasPathLengthConstraint: BooleanType, pathLengthConstraint: IntType, critical: BooleanType): ...
    
    @overload
    def __init__(self, encodedBasicConstraints: AsnEncodedData, critical: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CertificateAuthority(self) -> BooleanType: ...
    
    @property
    def HasPathLengthConstraint(self) -> BooleanType: ...
    
    @property
    def PathLengthConstraint(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def CopyFrom(self, asnEncodedData: AsnEncodedData) -> VoidType: ...
    
    def get_CertificateAuthority(self) -> BooleanType: ...
    
    def get_HasPathLengthConstraint(self) -> BooleanType: ...
    
    def get_PathLengthConstraint(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class X509Certificate2(X509Certificate, IDisposable, IDeserializationCallback, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, rawData: ArrayType[ByteType]): ...
    
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
    def __init__(self, certificate: X509Certificate): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Archived(self) -> BooleanType: ...
    
    @Archived.setter
    def Archived(self, value: BooleanType) -> None: ...
    
    @property
    def Extensions(self) -> X509ExtensionCollection: ...
    
    @property
    def FriendlyName(self) -> StringType: ...
    
    @FriendlyName.setter
    def FriendlyName(self, value: StringType) -> None: ...
    
    @property
    def HasPrivateKey(self) -> BooleanType: ...
    
    @property
    def IssuerName(self) -> X500DistinguishedName: ...
    
    @property
    def NotAfter(self) -> DateTime: ...
    
    @property
    def NotBefore(self) -> DateTime: ...
    
    @property
    def PrivateKey(self) -> AsymmetricAlgorithm: ...
    
    @PrivateKey.setter
    def PrivateKey(self, value: AsymmetricAlgorithm) -> None: ...
    
    @property
    def PublicKey(self) -> PublicKey: ...
    
    @property
    def RawData(self) -> ArrayType[ByteType]: ...
    
    @property
    def SerialNumber(self) -> StringType: ...
    
    @property
    def SignatureAlgorithm(self) -> Oid: ...
    
    @property
    def SubjectName(self) -> X500DistinguishedName: ...
    
    @property
    def Thumbprint(self) -> StringType: ...
    
    @property
    def Version(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def GetCertContentType(rawData: ArrayType[ByteType]) -> X509ContentType: ...
    
    @staticmethod
    @overload
    def GetCertContentType(fileName: StringType) -> X509ContentType: ...
    
    def GetNameInfo(self, nameType: X509NameType, forIssuer: BooleanType) -> StringType: ...
    
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
    def ToString(self, verbose: BooleanType) -> StringType: ...
    
    def Verify(self) -> BooleanType: ...
    
    def get_Archived(self) -> BooleanType: ...
    
    def get_Extensions(self) -> X509ExtensionCollection: ...
    
    def get_FriendlyName(self) -> StringType: ...
    
    def get_HasPrivateKey(self) -> BooleanType: ...
    
    def get_IssuerName(self) -> X500DistinguishedName: ...
    
    def get_NotAfter(self) -> DateTime: ...
    
    def get_NotBefore(self) -> DateTime: ...
    
    def get_PrivateKey(self) -> AsymmetricAlgorithm: ...
    
    def get_PublicKey(self) -> PublicKey: ...
    
    def get_RawData(self) -> ArrayType[ByteType]: ...
    
    def get_SerialNumber(self) -> StringType: ...
    
    def get_SignatureAlgorithm(self) -> Oid: ...
    
    def get_SubjectName(self) -> X500DistinguishedName: ...
    
    def get_Thumbprint(self) -> StringType: ...
    
    def get_Version(self) -> IntType: ...
    
    def set_Archived(self, value: BooleanType) -> VoidType: ...
    
    def set_FriendlyName(self, value: StringType) -> VoidType: ...
    
    def set_PrivateKey(self, value: AsymmetricAlgorithm) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class X509Certificate2Collection(X509CertificateCollection, IList, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, certificate: X509Certificate2): ...
    
    @overload
    def __init__(self, certificates: X509Certificate2Collection): ...
    
    @overload
    def __init__(self, certificates: ArrayType[X509Certificate2]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> X509Certificate2: ...
    
    @Item.setter
    def Item(self, value: X509Certificate2) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Add(self, certificate: X509Certificate2) -> IntType: ...
    
    @overload
    def AddRange(self, certificates: ArrayType[X509Certificate2]) -> VoidType: ...
    
    @overload
    def AddRange(self, certificates: X509Certificate2Collection) -> VoidType: ...
    
    @overload
    def Contains(self, certificate: X509Certificate2) -> BooleanType: ...
    
    @overload
    def Export(self, contentType: X509ContentType) -> ArrayType[ByteType]: ...
    
    @overload
    def Export(self, contentType: X509ContentType, password: StringType) -> ArrayType[ByteType]: ...
    
    def Find(self, findType: X509FindType, findValue: ObjectType, validOnly: BooleanType) -> X509Certificate2Collection: ...
    
    @overload
    def GetEnumerator(self) -> X509Certificate2Enumerator: ...
    
    @overload
    def Import(self, rawData: ArrayType[ByteType]) -> VoidType: ...
    
    @overload
    def Import(self, fileName: StringType) -> VoidType: ...
    
    @overload
    def Import(self, rawData: ArrayType[ByteType], password: StringType, keyStorageFlags: X509KeyStorageFlags) -> VoidType: ...
    
    @overload
    def Import(self, fileName: StringType, password: StringType, keyStorageFlags: X509KeyStorageFlags) -> VoidType: ...
    
    @overload
    def Insert(self, index: IntType, certificate: X509Certificate2) -> VoidType: ...
    
    @overload
    def Remove(self, certificate: X509Certificate2) -> VoidType: ...
    
    @overload
    def RemoveRange(self, certificates: ArrayType[X509Certificate2]) -> VoidType: ...
    
    @overload
    def RemoveRange(self, certificates: X509Certificate2Collection) -> VoidType: ...
    
    @overload
    def get_Item(self, index: IntType) -> X509Certificate2: ...
    
    @overload
    def set_Item(self, index: IntType, value: X509Certificate2) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class X509Certificate2Enumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> X509Certificate2: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> X509Certificate2: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class X509CertificateCollection(CollectionBase, IList, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: X509CertificateCollection): ...
    
    @overload
    def __init__(self, value: ArrayType[X509Certificate]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> X509Certificate: ...
    
    @Item.setter
    def Item(self, value: X509Certificate) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, value: X509Certificate) -> IntType: ...
    
    @overload
    def AddRange(self, value: ArrayType[X509Certificate]) -> VoidType: ...
    
    @overload
    def AddRange(self, value: X509CertificateCollection) -> VoidType: ...
    
    def Contains(self, value: X509Certificate) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[X509Certificate], index: IntType) -> VoidType: ...
    
    @overload
    def GetEnumerator(self) -> X509CertificateEnumerator: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def IndexOf(self, value: X509Certificate) -> IntType: ...
    
    def Insert(self, index: IntType, value: X509Certificate) -> VoidType: ...
    
    def Remove(self, value: X509Certificate) -> VoidType: ...
    
    def get_Item(self, index: IntType) -> X509Certificate: ...
    
    def set_Item(self, index: IntType, value: X509Certificate) -> VoidType: ...
    
    # No Events
    
    
    # ---------- Sub Classes ---------- #
    
    class X509CertificateEnumerator(ObjectType, IEnumerator):
        # No Fields
        
        # ---------- Constructors ---------- #
        
        def __init__(self, mappings: X509CertificateCollection): ...
        
        # ---------- Properties ---------- #
        
        @property
        def Current(self) -> X509Certificate: ...
        
        # ---------- Methods ---------- #
        
        def MoveNext(self) -> BooleanType: ...
        
        def Reset(self) -> VoidType: ...
        
        def get_Current(self) -> X509Certificate: ...
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class X509Chain(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, useMachineContext: BooleanType): ...
    
    @overload
    def __init__(self, chainContext: NIntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ChainContext(self) -> NIntType: ...
    
    @property
    def ChainElements(self) -> X509ChainElementCollection: ...
    
    @property
    def ChainPolicy(self) -> X509ChainPolicy: ...
    
    @ChainPolicy.setter
    def ChainPolicy(self, value: X509ChainPolicy) -> None: ...
    
    @property
    def ChainStatus(self) -> ArrayType[X509ChainStatus]: ...
    
    @property
    def SafeHandle(self) -> SafeX509ChainHandle: ...
    
    # ---------- Methods ---------- #
    
    def Build(self, certificate: X509Certificate2) -> BooleanType: ...
    
    @staticmethod
    def Create() -> X509Chain: ...
    
    def Dispose(self) -> VoidType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_ChainContext(self) -> NIntType: ...
    
    def get_ChainElements(self) -> X509ChainElementCollection: ...
    
    def get_ChainPolicy(self) -> X509ChainPolicy: ...
    
    def get_ChainStatus(self) -> ArrayType[X509ChainStatus]: ...
    
    def get_SafeHandle(self) -> SafeX509ChainHandle: ...
    
    def set_ChainPolicy(self, value: X509ChainPolicy) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class X509ChainElement(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Certificate(self) -> X509Certificate2: ...
    
    @property
    def ChainElementStatus(self) -> ArrayType[X509ChainStatus]: ...
    
    @property
    def Information(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Certificate(self) -> X509Certificate2: ...
    
    def get_ChainElementStatus(self) -> ArrayType[X509ChainStatus]: ...
    
    def get_Information(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class X509ChainElementCollection(ObjectType, ICollection, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    @property
    def Item(self) -> X509ChainElement: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def CopyTo(self, array: ArrayType[X509ChainElement], index: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> X509ChainElementEnumerator: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_Item(self, index: IntType) -> X509ChainElement: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class X509ChainElementEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> X509ChainElement: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> X509ChainElement: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class X509ChainPolicy(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ApplicationPolicy(self) -> OidCollection: ...
    
    @property
    def CertificatePolicy(self) -> OidCollection: ...
    
    @property
    def ExtraStore(self) -> X509Certificate2Collection: ...
    
    @property
    def RevocationFlag(self) -> X509RevocationFlag: ...
    
    @RevocationFlag.setter
    def RevocationFlag(self, value: X509RevocationFlag) -> None: ...
    
    @property
    def RevocationMode(self) -> X509RevocationMode: ...
    
    @RevocationMode.setter
    def RevocationMode(self, value: X509RevocationMode) -> None: ...
    
    @property
    def UrlRetrievalTimeout(self) -> TimeSpan: ...
    
    @UrlRetrievalTimeout.setter
    def UrlRetrievalTimeout(self, value: TimeSpan) -> None: ...
    
    @property
    def VerificationFlags(self) -> X509VerificationFlags: ...
    
    @VerificationFlags.setter
    def VerificationFlags(self, value: X509VerificationFlags) -> None: ...
    
    @property
    def VerificationTime(self) -> DateTime: ...
    
    @VerificationTime.setter
    def VerificationTime(self, value: DateTime) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Reset(self) -> VoidType: ...
    
    def get_ApplicationPolicy(self) -> OidCollection: ...
    
    def get_CertificatePolicy(self) -> OidCollection: ...
    
    def get_ExtraStore(self) -> X509Certificate2Collection: ...
    
    def get_RevocationFlag(self) -> X509RevocationFlag: ...
    
    def get_RevocationMode(self) -> X509RevocationMode: ...
    
    def get_UrlRetrievalTimeout(self) -> TimeSpan: ...
    
    def get_VerificationFlags(self) -> X509VerificationFlags: ...
    
    def get_VerificationTime(self) -> DateTime: ...
    
    def set_RevocationFlag(self, value: X509RevocationFlag) -> VoidType: ...
    
    def set_RevocationMode(self, value: X509RevocationMode) -> VoidType: ...
    
    def set_UrlRetrievalTimeout(self, value: TimeSpan) -> VoidType: ...
    
    def set_VerificationFlags(self, value: X509VerificationFlags) -> VoidType: ...
    
    def set_VerificationTime(self, value: DateTime) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class X509EnhancedKeyUsageExtension(X509Extension):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, enhancedKeyUsages: OidCollection, critical: BooleanType): ...
    
    @overload
    def __init__(self, encodedEnhancedKeyUsages: AsnEncodedData, critical: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def EnhancedKeyUsages(self) -> OidCollection: ...
    
    # ---------- Methods ---------- #
    
    def CopyFrom(self, asnEncodedData: AsnEncodedData) -> VoidType: ...
    
    def get_EnhancedKeyUsages(self) -> OidCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class X509Extension(AsnEncodedData):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, oid: StringType, rawData: ArrayType[ByteType], critical: BooleanType): ...
    
    @overload
    def __init__(self, encodedExtension: AsnEncodedData, critical: BooleanType): ...
    
    @overload
    def __init__(self, oid: Oid, rawData: ArrayType[ByteType], critical: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Critical(self) -> BooleanType: ...
    
    @Critical.setter
    def Critical(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def CopyFrom(self, asnEncodedData: AsnEncodedData) -> VoidType: ...
    
    def get_Critical(self) -> BooleanType: ...
    
    def set_Critical(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class X509ExtensionCollection(ObjectType, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    @property
    def Item(self) -> X509Extension: ...
    
    @property
    def Item(self) -> X509Extension: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, extension: X509Extension) -> IntType: ...
    
    def CopyTo(self, array: ArrayType[X509Extension], index: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> X509ExtensionEnumerator: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    @overload
    def get_Item(self, index: IntType) -> X509Extension: ...
    
    @overload
    def get_Item(self, oid: StringType) -> X509Extension: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class X509ExtensionEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> X509Extension: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> X509Extension: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class X509KeyUsageExtension(X509Extension):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, keyUsages: X509KeyUsageFlags, critical: BooleanType): ...
    
    @overload
    def __init__(self, encodedKeyUsage: AsnEncodedData, critical: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def KeyUsages(self) -> X509KeyUsageFlags: ...
    
    # ---------- Methods ---------- #
    
    def CopyFrom(self, asnEncodedData: AsnEncodedData) -> VoidType: ...
    
    def get_KeyUsages(self) -> X509KeyUsageFlags: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class X509Store(ObjectType, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, storeName: StringType): ...
    
    @overload
    def __init__(self, storeName: StoreName): ...
    
    @overload
    def __init__(self, storeLocation: StoreLocation): ...
    
    @overload
    def __init__(self, storeName: StoreName, storeLocation: StoreLocation): ...
    
    @overload
    def __init__(self, storeName: StringType, storeLocation: StoreLocation): ...
    
    @overload
    def __init__(self, storeHandle: NIntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Certificates(self) -> X509Certificate2Collection: ...
    
    @property
    def Location(self) -> StoreLocation: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def StoreHandle(self) -> NIntType: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, certificate: X509Certificate2) -> VoidType: ...
    
    def AddRange(self, certificates: X509Certificate2Collection) -> VoidType: ...
    
    def Close(self) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    def Open(self, flags: OpenFlags) -> VoidType: ...
    
    def Remove(self, certificate: X509Certificate2) -> VoidType: ...
    
    def RemoveRange(self, certificates: X509Certificate2Collection) -> VoidType: ...
    
    def get_Certificates(self) -> X509Certificate2Collection: ...
    
    def get_Location(self) -> StoreLocation: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_StoreHandle(self) -> NIntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class X509SubjectKeyIdentifierExtension(X509Extension):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, subjectKeyIdentifier: StringType, critical: BooleanType): ...
    
    @overload
    def __init__(self, subjectKeyIdentifier: ArrayType[ByteType], critical: BooleanType): ...
    
    @overload
    def __init__(self, encodedSubjectKeyIdentifier: AsnEncodedData, critical: BooleanType): ...
    
    @overload
    def __init__(self, key: PublicKey, critical: BooleanType): ...
    
    @overload
    def __init__(self, key: PublicKey, algorithm: X509SubjectKeyIdentifierHashAlgorithm, critical: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def SubjectKeyIdentifier(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def CopyFrom(self, asnEncodedData: AsnEncodedData) -> VoidType: ...
    
    def get_SubjectKeyIdentifier(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class X509Utils(ObjectType):
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

class X509ChainStatus(ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Status(self) -> X509ChainStatusFlags: ...
    
    @Status.setter
    def Status(self, value: X509ChainStatusFlags) -> None: ...
    
    @property
    def StatusInformation(self) -> StringType: ...
    
    @StatusInformation.setter
    def StatusInformation(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Status(self) -> X509ChainStatusFlags: ...
    
    def get_StatusInformation(self) -> StringType: ...
    
    def set_Status(self, value: X509ChainStatusFlags) -> VoidType: ...
    
    def set_StatusInformation(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Interfaces

# ---------- Enums ---------- #

class OpenFlags(Enum):
    ReadOnly: IntType = 0
    ReadWrite: IntType = 1
    MaxAllowed: IntType = 2
    OpenExistingOnly: IntType = 4
    IncludeArchived: IntType = 8


class StoreLocation(Enum):
    CurrentUser: IntType = 1
    LocalMachine: IntType = 2


class StoreName(Enum):
    AddressBook: IntType = 1
    AuthRoot: IntType = 2
    CertificateAuthority: IntType = 3
    Disallowed: IntType = 4
    My: IntType = 5
    Root: IntType = 6
    TrustedPeople: IntType = 7
    TrustedPublisher: IntType = 8


class X500DistinguishedNameFlags(Enum):
    #None: IntType = 0
    Reversed: IntType = 1
    UseSemicolons: IntType = 16
    DoNotUsePlusSign: IntType = 32
    DoNotUseQuotes: IntType = 64
    UseCommas: IntType = 128
    UseNewLines: IntType = 256
    UseUTF8Encoding: IntType = 4096
    UseT61Encoding: IntType = 8192
    ForceUTF8Encoding: IntType = 16384


class X509ChainStatusFlags(Enum):
    NoError: IntType = 0
    NotTimeValid: IntType = 1
    NotTimeNested: IntType = 2
    Revoked: IntType = 4
    NotSignatureValid: IntType = 8
    NotValidForUsage: IntType = 16
    UntrustedRoot: IntType = 32
    RevocationStatusUnknown: IntType = 64
    Cyclic: IntType = 128
    InvalidExtension: IntType = 256
    InvalidPolicyConstraints: IntType = 512
    InvalidBasicConstraints: IntType = 1024
    InvalidNameConstraints: IntType = 2048
    HasNotSupportedNameConstraint: IntType = 4096
    HasNotDefinedNameConstraint: IntType = 8192
    HasNotPermittedNameConstraint: IntType = 16384
    HasExcludedNameConstraint: IntType = 32768
    PartialChain: IntType = 65536
    CtlNotTimeValid: IntType = 131072
    CtlNotSignatureValid: IntType = 262144
    CtlNotValidForUsage: IntType = 524288
    HasWeakSignature: IntType = 1048576
    OfflineRevocation: IntType = 16777216
    NoIssuanceChainPolicy: IntType = 33554432
    ExplicitDistrust: IntType = 67108864
    HasNotSupportedCriticalExtension: IntType = 134217728


class X509FindType(Enum):
    FindByThumbprint: IntType = 0
    FindBySubjectName: IntType = 1
    FindBySubjectDistinguishedName: IntType = 2
    FindByIssuerName: IntType = 3
    FindByIssuerDistinguishedName: IntType = 4
    FindBySerialNumber: IntType = 5
    FindByTimeValid: IntType = 6
    FindByTimeNotYetValid: IntType = 7
    FindByTimeExpired: IntType = 8
    FindByTemplateName: IntType = 9
    FindByApplicationPolicy: IntType = 10
    FindByCertificatePolicy: IntType = 11
    FindByExtension: IntType = 12
    FindByKeyUsage: IntType = 13
    FindBySubjectKeyIdentifier: IntType = 14


class X509IncludeOption(Enum):
    #None: IntType = 0
    ExcludeRoot: IntType = 1
    EndCertOnly: IntType = 2
    WholeChain: IntType = 3


class X509KeyUsageFlags(Enum):
    #None: IntType = 0
    EncipherOnly: IntType = 1
    CrlSign: IntType = 2
    KeyCertSign: IntType = 4
    KeyAgreement: IntType = 8
    DataEncipherment: IntType = 16
    KeyEncipherment: IntType = 32
    NonRepudiation: IntType = 64
    DigitalSignature: IntType = 128
    DecipherOnly: IntType = 32768


class X509NameType(Enum):
    SimpleName: IntType = 0
    EmailName: IntType = 1
    UpnName: IntType = 2
    DnsName: IntType = 3
    DnsFromAlternativeName: IntType = 4
    UrlName: IntType = 5


class X509RevocationFlag(Enum):
    EndCertificateOnly: IntType = 0
    EntireChain: IntType = 1
    ExcludeRoot: IntType = 2


class X509RevocationMode(Enum):
    NoCheck: IntType = 0
    Online: IntType = 1
    Offline: IntType = 2


class X509SubjectKeyIdentifierHashAlgorithm(Enum):
    Sha1: IntType = 0
    ShortSha1: IntType = 1
    CapiSha1: IntType = 2


class X509VerificationFlags(Enum):
    NoFlag: IntType = 0
    IgnoreNotTimeValid: IntType = 1
    IgnoreCtlNotTimeValid: IntType = 2
    IgnoreNotTimeNested: IntType = 4
    IgnoreInvalidBasicConstraints: IntType = 8
    AllowUnknownCertificateAuthority: IntType = 16
    IgnoreWrongUsage: IntType = 32
    IgnoreInvalidName: IntType = 64
    IgnoreInvalidPolicy: IntType = 128
    IgnoreEndRevocationUnknown: IntType = 256
    IgnoreCtlSignerRevocationUnknown: IntType = 512
    IgnoreCertificateAuthorityRevocationUnknown: IntType = 1024
    IgnoreRootRevocationUnknown: IntType = 2048
    AllFlags: IntType = 4095


# No Delegates

__all__ = [
    PublicKey,
    X500DistinguishedName,
    X509BasicConstraintsExtension,
    X509Certificate2,
    X509Certificate2Collection,
    X509Certificate2Enumerator,
    X509CertificateCollection,
    X509Chain,
    X509ChainElement,
    X509ChainElementCollection,
    X509ChainElementEnumerator,
    X509ChainPolicy,
    X509EnhancedKeyUsageExtension,
    X509Extension,
    X509ExtensionCollection,
    X509ExtensionEnumerator,
    X509KeyUsageExtension,
    X509Store,
    X509SubjectKeyIdentifierExtension,
    X509Utils,
    X509ChainStatus,
    OpenFlags,
    StoreLocation,
    StoreName,
    X500DistinguishedNameFlags,
    X509ChainStatusFlags,
    X509FindType,
    X509IncludeOption,
    X509KeyUsageFlags,
    X509NameType,
    X509RevocationFlag,
    X509RevocationMode,
    X509SubjectKeyIdentifierHashAlgorithm,
    X509VerificationFlags,
]
