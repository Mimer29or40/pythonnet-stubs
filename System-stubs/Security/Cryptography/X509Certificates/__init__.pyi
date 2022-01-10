from __future__ import annotations

from abc import ABC
from typing import List, Tuple, Union, overload

from Microsoft.Win32.SafeHandles import SafeAxlBufferHandle, SafeHandleZeroOrMinusOneIsInvalid, SafeX509ChainHandle
from System import Array, Boolean, Byte, DateTime, DateTimeOffset, Enum, IDisposable, Int32, IntPtr, Object, String, TimeSpan, Uri, ValueType, Void
from System.Collections import CollectionBase, ICollection, IEnumerable, IEnumerator, IList
from System.Collections.ObjectModel import Collection
from System.Net import IPAddress
from System.Runtime.InteropServices.ComTypes import FILETIME
from System.Runtime.Serialization import IDeserializationCallback, ISerializable, SerializationInfo, StreamingContext
from System.Security import SecureString
from System.Security.Cryptography import AsnEncodedData, AsymmetricAlgorithm, CapiNative, DSA, ECDsa, HashAlgorithmName, Oid, OidCollection, RSA, RSASignaturePadding, SignatureVerificationResult

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

class AuthenticodeSignatureInformation(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Description(self) -> StringType: ...
    
    @property
    def DescriptionUrl(self) -> Uri: ...
    
    @property
    def HResult(self) -> IntType: ...
    
    @property
    def HashAlgorithm(self) -> StringType: ...
    
    @property
    def SignatureChain(self) -> X509Chain: ...
    
    @property
    def SigningCertificate(self) -> X509Certificate2: ...
    
    @property
    def Timestamp(self) -> TimestampInformation: ...
    
    @property
    def TrustStatus(self) -> TrustStatus: ...
    
    @property
    def VerificationResult(self) -> SignatureVerificationResult: ...
    
    # ---------- Methods ---------- #
    
    def get_Description(self) -> StringType: ...
    
    def get_DescriptionUrl(self) -> Uri: ...
    
    def get_HResult(self) -> IntType: ...
    
    def get_HashAlgorithm(self) -> StringType: ...
    
    def get_SignatureChain(self) -> X509Chain: ...
    
    def get_SigningCertificate(self) -> X509Certificate2: ...
    
    def get_Timestamp(self) -> TimestampInformation: ...
    
    def get_TrustStatus(self) -> TrustStatus: ...
    
    def get_VerificationResult(self) -> SignatureVerificationResult: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class AuthenticodeSignatureInformation(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Description(self) -> StringType: ...
    
    @property
    def DescriptionUrl(self) -> Uri: ...
    
    @property
    def HResult(self) -> IntType: ...
    
    @property
    def HashAlgorithm(self) -> StringType: ...
    
    @property
    def SignatureChain(self) -> X509Chain: ...
    
    @property
    def SigningCertificate(self) -> X509Certificate2: ...
    
    @property
    def Timestamp(self) -> TimestampInformation: ...
    
    @property
    def TrustStatus(self) -> TrustStatus: ...
    
    @property
    def VerificationResult(self) -> SignatureVerificationResult: ...
    
    # ---------- Methods ---------- #
    
    def get_Description(self) -> StringType: ...
    
    def get_DescriptionUrl(self) -> Uri: ...
    
    def get_HResult(self) -> IntType: ...
    
    def get_HashAlgorithm(self) -> StringType: ...
    
    def get_SignatureChain(self) -> X509Chain: ...
    
    def get_SigningCertificate(self) -> X509Certificate2: ...
    
    def get_Timestamp(self) -> TimestampInformation: ...
    
    def get_TrustStatus(self) -> TrustStatus: ...
    
    def get_VerificationResult(self) -> SignatureVerificationResult: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CertificateExtensionsCommon(ABC, ObjectType):
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


class CertificateExtensionsCommon(ABC, ObjectType):
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


class CertificateRequest(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, subjectName: StringType, key: ECDsa, hashAlgorithm: HashAlgorithmName): ...
    
    @overload
    def __init__(self, subjectName: X500DistinguishedName, key: ECDsa, hashAlgorithm: HashAlgorithmName): ...
    
    @overload
    def __init__(self, subjectName: StringType, key: RSA, hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding): ...
    
    @overload
    def __init__(self, subjectName: X500DistinguishedName, key: RSA, hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding): ...
    
    @overload
    def __init__(self, subjectName: X500DistinguishedName, publicKey: PublicKey, hashAlgorithm: HashAlgorithmName): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CertificateExtensions(self) -> Collection[X509Extension]: ...
    
    @property
    def HashAlgorithm(self) -> HashAlgorithmName: ...
    
    @property
    def PublicKey(self) -> PublicKey: ...
    
    @property
    def SubjectName(self) -> X500DistinguishedName: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Create(self, issuerCertificate: X509Certificate2, notBefore: DateTimeOffset, notAfter: DateTimeOffset, serialNumber: ArrayType[ByteType]) -> X509Certificate2: ...
    
    @overload
    def Create(self, issuerName: X500DistinguishedName, generator: X509SignatureGenerator, notBefore: DateTimeOffset, notAfter: DateTimeOffset, serialNumber: ArrayType[ByteType]) -> X509Certificate2: ...
    
    def CreateSelfSigned(self, notBefore: DateTimeOffset, notAfter: DateTimeOffset) -> X509Certificate2: ...
    
    @overload
    def CreateSigningRequest(self) -> ArrayType[ByteType]: ...
    
    @overload
    def CreateSigningRequest(self, signatureGenerator: X509SignatureGenerator) -> ArrayType[ByteType]: ...
    
    def get_CertificateExtensions(self) -> Collection[X509Extension]: ...
    
    def get_HashAlgorithm(self) -> HashAlgorithmName: ...
    
    def get_PublicKey(self) -> PublicKey: ...
    
    def get_SubjectName(self) -> X500DistinguishedName: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CertificateRequest(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, subjectName: StringType, key: ECDsa, hashAlgorithm: HashAlgorithmName): ...
    
    @overload
    def __init__(self, subjectName: X500DistinguishedName, key: ECDsa, hashAlgorithm: HashAlgorithmName): ...
    
    @overload
    def __init__(self, subjectName: StringType, key: RSA, hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding): ...
    
    @overload
    def __init__(self, subjectName: X500DistinguishedName, key: RSA, hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding): ...
    
    @overload
    def __init__(self, subjectName: X500DistinguishedName, publicKey: PublicKey, hashAlgorithm: HashAlgorithmName): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CertificateExtensions(self) -> Collection[X509Extension]: ...
    
    @property
    def HashAlgorithm(self) -> HashAlgorithmName: ...
    
    @property
    def PublicKey(self) -> PublicKey: ...
    
    @property
    def SubjectName(self) -> X500DistinguishedName: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Create(self, issuerCertificate: X509Certificate2, notBefore: DateTimeOffset, notAfter: DateTimeOffset, serialNumber: ArrayType[ByteType]) -> X509Certificate2: ...
    
    @overload
    def Create(self, issuerName: X500DistinguishedName, generator: X509SignatureGenerator, notBefore: DateTimeOffset, notAfter: DateTimeOffset, serialNumber: ArrayType[ByteType]) -> X509Certificate2: ...
    
    def CreateSelfSigned(self, notBefore: DateTimeOffset, notAfter: DateTimeOffset) -> X509Certificate2: ...
    
    @overload
    def CreateSigningRequest(self) -> ArrayType[ByteType]: ...
    
    @overload
    def CreateSigningRequest(self, signatureGenerator: X509SignatureGenerator) -> ArrayType[ByteType]: ...
    
    def get_CertificateExtensions(self) -> Collection[X509Extension]: ...
    
    def get_HashAlgorithm(self) -> HashAlgorithmName: ...
    
    def get_PublicKey(self) -> PublicKey: ...
    
    def get_SubjectName(self) -> X500DistinguishedName: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DSACertificateExtensions(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CopyWithPrivateKey(certificate: X509Certificate2, privateKey: DSA) -> X509Certificate2: ...
    
    @staticmethod
    def GetDSAPrivateKey(certificate: X509Certificate2) -> DSA: ...
    
    @staticmethod
    def GetDSAPublicKey(certificate: X509Certificate2) -> DSA: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DSACertificateExtensions(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CopyWithPrivateKey(certificate: X509Certificate2, privateKey: DSA) -> X509Certificate2: ...
    
    @staticmethod
    def GetDSAPrivateKey(certificate: X509Certificate2) -> DSA: ...
    
    @staticmethod
    def GetDSAPublicKey(certificate: X509Certificate2) -> DSA: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DerEncoder(ABC, ObjectType):
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


class DerEncoder(ABC, ObjectType):
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


class DerSequenceReader(ObjectType):
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


class DerSequenceReader(ObjectType):
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


class ECDsaCertificateExtensions(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CopyWithPrivateKey(certificate: X509Certificate2, privateKey: ECDsa) -> X509Certificate2: ...
    
    @staticmethod
    def GetECDsaPrivateKey(certificate: X509Certificate2) -> ECDsa: ...
    
    @staticmethod
    def GetECDsaPublicKey(certificate: X509Certificate2) -> ECDsa: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ECDsaCertificateExtensions(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CopyWithPrivateKey(certificate: X509Certificate2, privateKey: ECDsa) -> X509Certificate2: ...
    
    @staticmethod
    def GetECDsaPrivateKey(certificate: X509Certificate2) -> ECDsa: ...
    
    @staticmethod
    def GetECDsaPublicKey(certificate: X509Certificate2) -> ECDsa: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ECDsaX509SignatureGenerator(X509SignatureGenerator):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetSignatureAlgorithmIdentifier(self, hashAlgorithm: HashAlgorithmName) -> ArrayType[ByteType]: ...
    
    def SignData(self, data: ArrayType[ByteType], hashAlgorithm: HashAlgorithmName) -> ArrayType[ByteType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ECDsaX509SignatureGenerator(X509SignatureGenerator):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetSignatureAlgorithmIdentifier(self, hashAlgorithm: HashAlgorithmName) -> ArrayType[ByteType]: ...
    
    def SignData(self, data: ArrayType[ByteType], hashAlgorithm: HashAlgorithmName) -> ArrayType[ByteType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EncodingHelpers(ABC, ObjectType):
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


class EncodingHelpers(ABC, ObjectType):
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


class GeneralNameEncoder(ObjectType):
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


class GeneralNameEncoder(ObjectType):
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


class Oids(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def AnyCertPolicy() -> StringType: ...
    
    @staticmethod
    @property
    def ApplicationCertPolicies() -> StringType: ...
    
    @staticmethod
    @property
    def AuthorityInformationAccess() -> StringType: ...
    
    @staticmethod
    @property
    def BasicConstraints() -> StringType: ...
    
    @staticmethod
    @property
    def BasicConstraints2() -> StringType: ...
    
    @staticmethod
    @property
    def CertPolicies() -> StringType: ...
    
    @staticmethod
    @property
    def CertPolicyConstraints() -> StringType: ...
    
    @staticmethod
    @property
    def CertPolicyMappings() -> StringType: ...
    
    @staticmethod
    @property
    def CertificateAuthorityIssuers() -> StringType: ...
    
    @staticmethod
    @property
    def CertificateTemplate() -> StringType: ...
    
    @staticmethod
    @property
    def CommonName() -> StringType: ...
    
    @staticmethod
    @property
    def CrlDistributionPoints() -> StringType: ...
    
    @staticmethod
    @property
    def DsaDsa() -> StringType: ...
    
    @staticmethod
    @property
    def ECDsaSha256() -> StringType: ...
    
    @staticmethod
    @property
    def ECDsaSha384() -> StringType: ...
    
    @staticmethod
    @property
    def ECDsaSha512() -> StringType: ...
    
    @staticmethod
    @property
    def Ecc() -> StringType: ...
    
    @staticmethod
    @property
    def EccCurveSecp256r1() -> StringType: ...
    
    @staticmethod
    @property
    def EccCurveSecp384r1() -> StringType: ...
    
    @staticmethod
    @property
    def EccCurveSecp521r1() -> StringType: ...
    
    @staticmethod
    @property
    def EmailAddress() -> StringType: ...
    
    @staticmethod
    @property
    def EnhancedKeyUsage() -> StringType: ...
    
    @staticmethod
    @property
    def EnrollCertTypeExtension() -> StringType: ...
    
    @staticmethod
    @property
    def InhibitAnyPolicyExtension() -> StringType: ...
    
    @staticmethod
    @property
    def IssuerAltName() -> StringType: ...
    
    @staticmethod
    @property
    def KeyUsage() -> StringType: ...
    
    @staticmethod
    @property
    def Mgf1() -> StringType: ...
    
    @staticmethod
    @property
    def Organization() -> StringType: ...
    
    @staticmethod
    @property
    def OrganizationalUnit() -> StringType: ...
    
    @staticmethod
    @property
    def Pkcs9ExtensionRequest() -> StringType: ...
    
    @staticmethod
    @property
    def RsaPkcs1Sha256() -> StringType: ...
    
    @staticmethod
    @property
    def RsaPkcs1Sha384() -> StringType: ...
    
    @staticmethod
    @property
    def RsaPkcs1Sha512() -> StringType: ...
    
    @staticmethod
    @property
    def RsaRsa() -> StringType: ...
    
    @staticmethod
    @property
    def RsaSsaPss() -> StringType: ...
    
    @staticmethod
    @property
    def Sha256() -> StringType: ...
    
    @staticmethod
    @property
    def Sha384() -> StringType: ...
    
    @staticmethod
    @property
    def Sha512() -> StringType: ...
    
    @staticmethod
    @property
    def SubjectAltName() -> StringType: ...
    
    @staticmethod
    @property
    def SubjectKeyIdentifier() -> StringType: ...
    
    @staticmethod
    @property
    def UserPrincipalName() -> StringType: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Oids(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def AnyCertPolicy() -> StringType: ...
    
    @staticmethod
    @property
    def ApplicationCertPolicies() -> StringType: ...
    
    @staticmethod
    @property
    def AuthorityInformationAccess() -> StringType: ...
    
    @staticmethod
    @property
    def BasicConstraints() -> StringType: ...
    
    @staticmethod
    @property
    def BasicConstraints2() -> StringType: ...
    
    @staticmethod
    @property
    def CertPolicies() -> StringType: ...
    
    @staticmethod
    @property
    def CertPolicyConstraints() -> StringType: ...
    
    @staticmethod
    @property
    def CertPolicyMappings() -> StringType: ...
    
    @staticmethod
    @property
    def CertificateAuthorityIssuers() -> StringType: ...
    
    @staticmethod
    @property
    def CertificateTemplate() -> StringType: ...
    
    @staticmethod
    @property
    def CommonName() -> StringType: ...
    
    @staticmethod
    @property
    def CrlDistributionPoints() -> StringType: ...
    
    @staticmethod
    @property
    def DsaDsa() -> StringType: ...
    
    @staticmethod
    @property
    def ECDsaSha256() -> StringType: ...
    
    @staticmethod
    @property
    def ECDsaSha384() -> StringType: ...
    
    @staticmethod
    @property
    def ECDsaSha512() -> StringType: ...
    
    @staticmethod
    @property
    def Ecc() -> StringType: ...
    
    @staticmethod
    @property
    def EccCurveSecp256r1() -> StringType: ...
    
    @staticmethod
    @property
    def EccCurveSecp384r1() -> StringType: ...
    
    @staticmethod
    @property
    def EccCurveSecp521r1() -> StringType: ...
    
    @staticmethod
    @property
    def EmailAddress() -> StringType: ...
    
    @staticmethod
    @property
    def EnhancedKeyUsage() -> StringType: ...
    
    @staticmethod
    @property
    def EnrollCertTypeExtension() -> StringType: ...
    
    @staticmethod
    @property
    def InhibitAnyPolicyExtension() -> StringType: ...
    
    @staticmethod
    @property
    def IssuerAltName() -> StringType: ...
    
    @staticmethod
    @property
    def KeyUsage() -> StringType: ...
    
    @staticmethod
    @property
    def Mgf1() -> StringType: ...
    
    @staticmethod
    @property
    def Organization() -> StringType: ...
    
    @staticmethod
    @property
    def OrganizationalUnit() -> StringType: ...
    
    @staticmethod
    @property
    def Pkcs9ExtensionRequest() -> StringType: ...
    
    @staticmethod
    @property
    def RsaPkcs1Sha256() -> StringType: ...
    
    @staticmethod
    @property
    def RsaPkcs1Sha384() -> StringType: ...
    
    @staticmethod
    @property
    def RsaPkcs1Sha512() -> StringType: ...
    
    @staticmethod
    @property
    def RsaRsa() -> StringType: ...
    
    @staticmethod
    @property
    def RsaSsaPss() -> StringType: ...
    
    @staticmethod
    @property
    def Sha256() -> StringType: ...
    
    @staticmethod
    @property
    def Sha384() -> StringType: ...
    
    @staticmethod
    @property
    def Sha512() -> StringType: ...
    
    @staticmethod
    @property
    def SubjectAltName() -> StringType: ...
    
    @staticmethod
    @property
    def SubjectKeyIdentifier() -> StringType: ...
    
    @staticmethod
    @property
    def UserPrincipalName() -> StringType: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Pkcs10CertificationRequestInfo(ObjectType):
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


class Pkcs10CertificationRequestInfo(ObjectType):
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


class Pkcs9ExtensionRequest(X501Attribute):
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


class Pkcs9ExtensionRequest(X501Attribute):
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


class RSACertificateExtensions(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CopyWithPrivateKey(certificate: X509Certificate2, privateKey: RSA) -> X509Certificate2: ...
    
    @staticmethod
    def GetRSAPrivateKey(certificate: X509Certificate2) -> RSA: ...
    
    @staticmethod
    def GetRSAPublicKey(certificate: X509Certificate2) -> RSA: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RSACertificateExtensions(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CopyWithPrivateKey(certificate: X509Certificate2, privateKey: RSA) -> X509Certificate2: ...
    
    @staticmethod
    def GetRSAPrivateKey(certificate: X509Certificate2) -> RSA: ...
    
    @staticmethod
    def GetRSAPublicKey(certificate: X509Certificate2) -> RSA: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RSAPkcs1X509SignatureGenerator(X509SignatureGenerator):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetSignatureAlgorithmIdentifier(self, hashAlgorithm: HashAlgorithmName) -> ArrayType[ByteType]: ...
    
    def SignData(self, data: ArrayType[ByteType], hashAlgorithm: HashAlgorithmName) -> ArrayType[ByteType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RSAPkcs1X509SignatureGenerator(X509SignatureGenerator):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetSignatureAlgorithmIdentifier(self, hashAlgorithm: HashAlgorithmName) -> ArrayType[ByteType]: ...
    
    def SignData(self, data: ArrayType[ByteType], hashAlgorithm: HashAlgorithmName) -> ArrayType[ByteType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RSAPssX509SignatureGenerator(X509SignatureGenerator):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetSignatureAlgorithmIdentifier(self, hashAlgorithm: HashAlgorithmName) -> ArrayType[ByteType]: ...
    
    def SignData(self, data: ArrayType[ByteType], hashAlgorithm: HashAlgorithmName) -> ArrayType[ByteType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RSAPssX509SignatureGenerator(X509SignatureGenerator):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetSignatureAlgorithmIdentifier(self, hashAlgorithm: HashAlgorithmName) -> ArrayType[ByteType]: ...
    
    def SignData(self, data: ArrayType[ByteType], hashAlgorithm: HashAlgorithmName) -> ArrayType[ByteType]: ...
    
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


class SubjectAlternativeNameBuilder(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AddDnsName(self, dnsName: StringType) -> VoidType: ...
    
    def AddEmailAddress(self, emailAddress: StringType) -> VoidType: ...
    
    def AddIpAddress(self, ipAddress: IPAddress) -> VoidType: ...
    
    def AddUri(self, uri: Uri) -> VoidType: ...
    
    def AddUserPrincipalName(self, upn: StringType) -> VoidType: ...
    
    def Build(self, critical: BooleanType) -> X509Extension: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SubjectAlternativeNameBuilder(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def AddDnsName(self, dnsName: StringType) -> VoidType: ...
    
    def AddEmailAddress(self, emailAddress: StringType) -> VoidType: ...
    
    def AddIpAddress(self, ipAddress: IPAddress) -> VoidType: ...
    
    def AddUri(self, uri: Uri) -> VoidType: ...
    
    def AddUserPrincipalName(self, upn: StringType) -> VoidType: ...
    
    def Build(self, critical: BooleanType) -> X509Extension: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TbsCertificate(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Extensions(self) -> Collection[X509Extension]: ...
    
    @property
    def Issuer(self) -> X500DistinguishedName: ...
    
    @Issuer.setter
    def Issuer(self, value: X500DistinguishedName) -> None: ...
    
    @property
    def NotAfter(self) -> DateTimeOffset: ...
    
    @NotAfter.setter
    def NotAfter(self, value: DateTimeOffset) -> None: ...
    
    @property
    def NotBefore(self) -> DateTimeOffset: ...
    
    @NotBefore.setter
    def NotBefore(self, value: DateTimeOffset) -> None: ...
    
    @property
    def PublicKey(self) -> PublicKey: ...
    
    @PublicKey.setter
    def PublicKey(self, value: PublicKey) -> None: ...
    
    @property
    def SerialNumber(self) -> ArrayType[ByteType]: ...
    
    @SerialNumber.setter
    def SerialNumber(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def SignatureAlgorithm(self) -> ArrayType[ByteType]: ...
    
    @SignatureAlgorithm.setter
    def SignatureAlgorithm(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def Subject(self) -> X500DistinguishedName: ...
    
    @Subject.setter
    def Subject(self, value: X500DistinguishedName) -> None: ...
    
    @property
    def Version(self) -> ByteType: ...
    
    @Version.setter
    def Version(self, value: ByteType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Extensions(self) -> Collection[X509Extension]: ...
    
    def get_Issuer(self) -> X500DistinguishedName: ...
    
    def get_NotAfter(self) -> DateTimeOffset: ...
    
    def get_NotBefore(self) -> DateTimeOffset: ...
    
    def get_PublicKey(self) -> PublicKey: ...
    
    def get_SerialNumber(self) -> ArrayType[ByteType]: ...
    
    def get_SignatureAlgorithm(self) -> ArrayType[ByteType]: ...
    
    def get_Subject(self) -> X500DistinguishedName: ...
    
    def get_Version(self) -> ByteType: ...
    
    def set_Issuer(self, value: X500DistinguishedName) -> VoidType: ...
    
    def set_NotAfter(self, value: DateTimeOffset) -> VoidType: ...
    
    def set_NotBefore(self, value: DateTimeOffset) -> VoidType: ...
    
    def set_PublicKey(self, value: PublicKey) -> VoidType: ...
    
    def set_SerialNumber(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    def set_SignatureAlgorithm(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    def set_Subject(self, value: X500DistinguishedName) -> VoidType: ...
    
    def set_Version(self, value: ByteType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TbsCertificate(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Extensions(self) -> Collection[X509Extension]: ...
    
    @property
    def Issuer(self) -> X500DistinguishedName: ...
    
    @Issuer.setter
    def Issuer(self, value: X500DistinguishedName) -> None: ...
    
    @property
    def NotAfter(self) -> DateTimeOffset: ...
    
    @NotAfter.setter
    def NotAfter(self, value: DateTimeOffset) -> None: ...
    
    @property
    def NotBefore(self) -> DateTimeOffset: ...
    
    @NotBefore.setter
    def NotBefore(self, value: DateTimeOffset) -> None: ...
    
    @property
    def PublicKey(self) -> PublicKey: ...
    
    @PublicKey.setter
    def PublicKey(self, value: PublicKey) -> None: ...
    
    @property
    def SerialNumber(self) -> ArrayType[ByteType]: ...
    
    @SerialNumber.setter
    def SerialNumber(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def SignatureAlgorithm(self) -> ArrayType[ByteType]: ...
    
    @SignatureAlgorithm.setter
    def SignatureAlgorithm(self, value: ArrayType[ByteType]) -> None: ...
    
    @property
    def Subject(self) -> X500DistinguishedName: ...
    
    @Subject.setter
    def Subject(self, value: X500DistinguishedName) -> None: ...
    
    @property
    def Version(self) -> ByteType: ...
    
    @Version.setter
    def Version(self, value: ByteType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Extensions(self) -> Collection[X509Extension]: ...
    
    def get_Issuer(self) -> X500DistinguishedName: ...
    
    def get_NotAfter(self) -> DateTimeOffset: ...
    
    def get_NotBefore(self) -> DateTimeOffset: ...
    
    def get_PublicKey(self) -> PublicKey: ...
    
    def get_SerialNumber(self) -> ArrayType[ByteType]: ...
    
    def get_SignatureAlgorithm(self) -> ArrayType[ByteType]: ...
    
    def get_Subject(self) -> X500DistinguishedName: ...
    
    def get_Version(self) -> ByteType: ...
    
    def set_Issuer(self, value: X500DistinguishedName) -> VoidType: ...
    
    def set_NotAfter(self, value: DateTimeOffset) -> VoidType: ...
    
    def set_NotBefore(self, value: DateTimeOffset) -> VoidType: ...
    
    def set_PublicKey(self, value: PublicKey) -> VoidType: ...
    
    def set_SerialNumber(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    def set_SignatureAlgorithm(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    def set_Subject(self, value: X500DistinguishedName) -> VoidType: ...
    
    def set_Version(self, value: ByteType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TimestampInformation(ObjectType):
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
    def SignatureChain(self) -> X509Chain: ...
    
    @property
    def SigningCertificate(self) -> X509Certificate2: ...
    
    @property
    def Timestamp(self) -> DateTime: ...
    
    @property
    def VerificationResult(self) -> SignatureVerificationResult: ...
    
    # ---------- Methods ---------- #
    
    def get_HResult(self) -> IntType: ...
    
    def get_HashAlgorithm(self) -> StringType: ...
    
    def get_IsValid(self) -> BooleanType: ...
    
    def get_SignatureChain(self) -> X509Chain: ...
    
    def get_SigningCertificate(self) -> X509Certificate2: ...
    
    def get_Timestamp(self) -> DateTime: ...
    
    def get_VerificationResult(self) -> SignatureVerificationResult: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TimestampInformation(ObjectType):
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
    def SignatureChain(self) -> X509Chain: ...
    
    @property
    def SigningCertificate(self) -> X509Certificate2: ...
    
    @property
    def Timestamp(self) -> DateTime: ...
    
    @property
    def VerificationResult(self) -> SignatureVerificationResult: ...
    
    # ---------- Methods ---------- #
    
    def get_HResult(self) -> IntType: ...
    
    def get_HashAlgorithm(self) -> StringType: ...
    
    def get_IsValid(self) -> BooleanType: ...
    
    def get_SignatureChain(self) -> X509Chain: ...
    
    def get_SigningCertificate(self) -> X509Certificate2: ...
    
    def get_Timestamp(self) -> DateTime: ...
    
    def get_VerificationResult(self) -> SignatureVerificationResult: ...
    
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


class X501Attribute(AsnEncodedData):
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


class X501Attribute(AsnEncodedData):
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


class X509Certificate2UI(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    @overload
    def DisplayCertificate(certificate: X509Certificate2) -> VoidType: ...
    
    @staticmethod
    @overload
    def DisplayCertificate(certificate: X509Certificate2, hwndParent: NIntType) -> VoidType: ...
    
    @staticmethod
    @overload
    def SelectFromCollection(certificates: X509Certificate2Collection, title: StringType, message: StringType, selectionFlag: X509SelectionFlag) -> X509Certificate2Collection: ...
    
    @staticmethod
    @overload
    def SelectFromCollection(certificates: X509Certificate2Collection, title: StringType, message: StringType, selectionFlag: X509SelectionFlag, hwndParent: NIntType) -> X509Certificate2Collection: ...
    
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


class X509CertificateExtensions(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetAnyPublicKey(c: X509Certificate2) -> AsymmetricAlgorithm: ...
    
    @staticmethod
    def GetDSAPrivateKey(certificate: X509Certificate2) -> DSA: ...
    
    @staticmethod
    def GetDSAPublicKey(certificate: X509Certificate2) -> DSA: ...
    
    @staticmethod
    def GetECDsaPrivateKey(certificate: X509Certificate2) -> AsymmetricAlgorithm: ...
    
    @staticmethod
    def GetECDsaPublicKey(certificate: X509Certificate2) -> AsymmetricAlgorithm: ...
    
    @staticmethod
    def GetRSAPrivateKey(certificate: X509Certificate2) -> RSA: ...
    
    @staticmethod
    def GetRSAPublicKey(certificate: X509Certificate2) -> RSA: ...
    
    # No Events
    
    # No Sub Classes
    
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


class X509Native(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    
    # ---------- Sub Classes ---------- #
    
    class UnsafeNativeMethods(ABC, ObjectType):
        # No Fields
        
        # No Constructors
        
        # No Properties
        
        # ---------- Methods ---------- #
        
        @staticmethod
        def CertFreeAuthenticodeSignerInfo(pSignerInfo: AXL_AUTHENTICODE_SIGNER_INFO) -> Tuple[IntType, AXL_AUTHENTICODE_SIGNER_INFO]: ...
        
        @staticmethod
        def CertFreeAuthenticodeTimestamperInfo(pTimestamperInfo: AXL_AUTHENTICODE_TIMESTAMPER_INFO) -> Tuple[IntType, AXL_AUTHENTICODE_TIMESTAMPER_INFO]: ...
        
        @staticmethod
        def CertVerifyAuthenticodeLicense(pLicenseBlob: CRYPTOAPI_BLOB, dwFlags: AxlVerificationFlags, pSignerInfo: AXL_AUTHENTICODE_SIGNER_INFO, pTimestamperInfo: AXL_AUTHENTICODE_TIMESTAMPER_INFO) -> Tuple[IntType, CRYPTOAPI_BLOB, AXL_AUTHENTICODE_SIGNER_INFO, AXL_AUTHENTICODE_TIMESTAMPER_INFO]: ...
        
        @staticmethod
        def _AxlGetIssuerPublicKeyHash(pCertContext: NIntType, ppwszPublicKeyHash: SafeAxlBufferHandle) -> Tuple[IntType, SafeAxlBufferHandle]: ...
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    # ---------- Sub Structs ---------- #
    
    class AXL_AUTHENTICODE_SIGNER_INFO(ValueType):
        # ---------- Fields ---------- #
        
        @property
        def algHash(self) -> AlgorithmId: ...
        
        @algHash.setter
        def algHash(self, value: AlgorithmId) -> None: ...
        
        @property
        def cbSize(self) -> IntType: ...
        
        @cbSize.setter
        def cbSize(self, value: IntType) -> None: ...
        
        @property
        def dwError(self) -> IntType: ...
        
        @dwError.setter
        def dwError(self, value: IntType) -> None: ...
        
        @property
        def pChainContext(self) -> NIntType: ...
        
        @pChainContext.setter
        def pChainContext(self, value: NIntType) -> None: ...
        
        @property
        def pwszDescription(self) -> NIntType: ...
        
        @pwszDescription.setter
        def pwszDescription(self, value: NIntType) -> None: ...
        
        @property
        def pwszDescriptionUrl(self) -> NIntType: ...
        
        @pwszDescriptionUrl.setter
        def pwszDescriptionUrl(self, value: NIntType) -> None: ...
        
        @property
        def pwszHash(self) -> NIntType: ...
        
        @pwszHash.setter
        def pwszHash(self, value: NIntType) -> None: ...
        
        # No Constructors
        
        # No Properties
        
        # No Methods
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    class AXL_AUTHENTICODE_TIMESTAMPER_INFO(ValueType):
        # ---------- Fields ---------- #
        
        @property
        def algHash(self) -> AlgorithmId: ...
        
        @algHash.setter
        def algHash(self, value: AlgorithmId) -> None: ...
        
        @property
        def cbsize(self) -> IntType: ...
        
        @cbsize.setter
        def cbsize(self, value: IntType) -> None: ...
        
        @property
        def dwError(self) -> IntType: ...
        
        @dwError.setter
        def dwError(self, value: IntType) -> None: ...
        
        @property
        def ftTimestamp(self) -> FILETIME: ...
        
        @ftTimestamp.setter
        def ftTimestamp(self, value: FILETIME) -> None: ...
        
        @property
        def pChainContext(self) -> NIntType: ...
        
        @pChainContext.setter
        def pChainContext(self, value: NIntType) -> None: ...
        
        # No Constructors
        
        # No Properties
        
        # No Methods
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class AxlVerificationFlags(Enum):
        #None: IntType = 0
        NoRevocationCheck: IntType = 1
        RevocationCheckEndCertOnly: IntType = 2
        RevocationCheckEntireChain: IntType = 4
        UrlOnlyCacheRetrieval: IntType = 8
        LifetimeSigning: IntType = 16
        TrustMicrosoftRootOnly: IntType = 32
    


class X509Native(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    
    # ---------- Sub Classes ---------- #
    
    class UnsafeNativeMethods(ABC, ObjectType):
        # No Fields
        
        # No Constructors
        
        # No Properties
        
        # ---------- Methods ---------- #
        
        @staticmethod
        def CertFreeAuthenticodeSignerInfo(pSignerInfo: AXL_AUTHENTICODE_SIGNER_INFO) -> Tuple[IntType, AXL_AUTHENTICODE_SIGNER_INFO]: ...
        
        @staticmethod
        def CertFreeAuthenticodeTimestamperInfo(pTimestamperInfo: AXL_AUTHENTICODE_TIMESTAMPER_INFO) -> Tuple[IntType, AXL_AUTHENTICODE_TIMESTAMPER_INFO]: ...
        
        @staticmethod
        def CertVerifyAuthenticodeLicense(pLicenseBlob: CRYPTOAPI_BLOB, dwFlags: AxlVerificationFlags, pSignerInfo: AXL_AUTHENTICODE_SIGNER_INFO, pTimestamperInfo: AXL_AUTHENTICODE_TIMESTAMPER_INFO) -> Tuple[IntType, CRYPTOAPI_BLOB, AXL_AUTHENTICODE_SIGNER_INFO, AXL_AUTHENTICODE_TIMESTAMPER_INFO]: ...
        
        @staticmethod
        def _AxlGetIssuerPublicKeyHash(pCertContext: NIntType, ppwszPublicKeyHash: SafeAxlBufferHandle) -> Tuple[IntType, SafeAxlBufferHandle]: ...
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    # ---------- Sub Structs ---------- #
    
    class AXL_AUTHENTICODE_SIGNER_INFO(ValueType):
        # ---------- Fields ---------- #
        
        @property
        def algHash(self) -> AlgorithmId: ...
        
        @algHash.setter
        def algHash(self, value: AlgorithmId) -> None: ...
        
        @property
        def cbSize(self) -> IntType: ...
        
        @cbSize.setter
        def cbSize(self, value: IntType) -> None: ...
        
        @property
        def dwError(self) -> IntType: ...
        
        @dwError.setter
        def dwError(self, value: IntType) -> None: ...
        
        @property
        def pChainContext(self) -> NIntType: ...
        
        @pChainContext.setter
        def pChainContext(self, value: NIntType) -> None: ...
        
        @property
        def pwszDescription(self) -> NIntType: ...
        
        @pwszDescription.setter
        def pwszDescription(self, value: NIntType) -> None: ...
        
        @property
        def pwszDescriptionUrl(self) -> NIntType: ...
        
        @pwszDescriptionUrl.setter
        def pwszDescriptionUrl(self, value: NIntType) -> None: ...
        
        @property
        def pwszHash(self) -> NIntType: ...
        
        @pwszHash.setter
        def pwszHash(self, value: NIntType) -> None: ...
        
        # No Constructors
        
        # No Properties
        
        # No Methods
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    class AXL_AUTHENTICODE_TIMESTAMPER_INFO(ValueType):
        # ---------- Fields ---------- #
        
        @property
        def algHash(self) -> AlgorithmId: ...
        
        @algHash.setter
        def algHash(self, value: AlgorithmId) -> None: ...
        
        @property
        def cbsize(self) -> IntType: ...
        
        @cbsize.setter
        def cbsize(self, value: IntType) -> None: ...
        
        @property
        def dwError(self) -> IntType: ...
        
        @dwError.setter
        def dwError(self, value: IntType) -> None: ...
        
        @property
        def ftTimestamp(self) -> FILETIME: ...
        
        @ftTimestamp.setter
        def ftTimestamp(self, value: FILETIME) -> None: ...
        
        @property
        def pChainContext(self) -> NIntType: ...
        
        @pChainContext.setter
        def pChainContext(self, value: NIntType) -> None: ...
        
        # No Constructors
        
        # No Properties
        
        # No Methods
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class AxlVerificationFlags(Enum):
        #None: IntType = 0
        NoRevocationCheck: IntType = 1
        RevocationCheckEndCertOnly: IntType = 2
        RevocationCheckEntireChain: IntType = 4
        UrlOnlyCacheRetrieval: IntType = 8
        LifetimeSigning: IntType = 16
        TrustMicrosoftRootOnly: IntType = 32
    


class X509SignatureGenerator(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def PublicKey(self) -> PublicKey: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CreateForECDsa(key: ECDsa) -> X509SignatureGenerator: ...
    
    @staticmethod
    def CreateForRSA(key: RSA, signaturePadding: RSASignaturePadding) -> X509SignatureGenerator: ...
    
    def GetSignatureAlgorithmIdentifier(self, hashAlgorithm: HashAlgorithmName) -> ArrayType[ByteType]: ...
    
    def SignData(self, data: ArrayType[ByteType], hashAlgorithm: HashAlgorithmName) -> ArrayType[ByteType]: ...
    
    def get_PublicKey(self) -> PublicKey: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class X509SignatureGenerator(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def PublicKey(self) -> PublicKey: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CreateForECDsa(key: ECDsa) -> X509SignatureGenerator: ...
    
    @staticmethod
    def CreateForRSA(key: RSA, signaturePadding: RSASignaturePadding) -> X509SignatureGenerator: ...
    
    def GetSignatureAlgorithmIdentifier(self, hashAlgorithm: HashAlgorithmName) -> ArrayType[ByteType]: ...
    
    def SignData(self, data: ArrayType[ByteType], hashAlgorithm: HashAlgorithmName) -> ArrayType[ByteType]: ...
    
    def get_PublicKey(self) -> PublicKey: ...
    
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


class PinAndClear(ValueType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PinAndClear(ValueType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


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


class OidKeyType(Enum):
    Oid: IntType = 1
    Name: IntType = 2
    AlgorithmID: IntType = 3
    SignatureID: IntType = 4
    CngAlgorithmID: IntType = 5
    CngSignatureID: IntType = 6


class OidKeyType(Enum):
    Oid: IntType = 1
    Name: IntType = 2
    AlgorithmID: IntType = 3
    SignatureID: IntType = 4
    CngAlgorithmID: IntType = 5
    CngSignatureID: IntType = 6


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


class TrustStatus(Enum):
    Untrusted: IntType = 0
    UnknownIdentity: IntType = 1
    KnownIdentity: IntType = 2
    Trusted: IntType = 3


class TrustStatus(Enum):
    Untrusted: IntType = 0
    UnknownIdentity: IntType = 1
    KnownIdentity: IntType = 2
    Trusted: IntType = 3


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


class X509ContentType(Enum):
    Unknown: IntType = 0
    Cert: IntType = 1
    SerializedCert: IntType = 2
    Pfx: IntType = 3
    Pkcs12: IntType = 3
    SerializedStore: IntType = 4
    Pkcs7: IntType = 5
    Authenticode: IntType = 6


class X509ContentType(Enum):
    Unknown: IntType = 0
    Cert: IntType = 1
    SerializedCert: IntType = 2
    Pfx: IntType = 3
    Pkcs12: IntType = 3
    SerializedStore: IntType = 4
    Pkcs7: IntType = 5
    Authenticode: IntType = 6


class X509ContentType(Enum):
    Unknown: IntType = 0
    Cert: IntType = 1
    SerializedCert: IntType = 2
    Pfx: IntType = 3
    Pkcs12: IntType = 3
    SerializedStore: IntType = 4
    Pkcs7: IntType = 5
    Authenticode: IntType = 6


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


class X509KeyStorageFlags(Enum):
    DefaultKeySet: IntType = 0
    UserKeySet: IntType = 1
    MachineKeySet: IntType = 2
    Exportable: IntType = 4
    UserProtected: IntType = 8
    PersistKeySet: IntType = 16
    EphemeralKeySet: IntType = 32


class X509KeyStorageFlags(Enum):
    DefaultKeySet: IntType = 0
    UserKeySet: IntType = 1
    MachineKeySet: IntType = 2
    Exportable: IntType = 4
    UserProtected: IntType = 8
    PersistKeySet: IntType = 16
    EphemeralKeySet: IntType = 32


class X509KeyStorageFlags(Enum):
    DefaultKeySet: IntType = 0
    UserKeySet: IntType = 1
    MachineKeySet: IntType = 2
    Exportable: IntType = 4
    UserProtected: IntType = 8
    PersistKeySet: IntType = 16
    EphemeralKeySet: IntType = 32


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


class X509SelectionFlag(Enum):
    SingleSelection: IntType = 0
    MultiSelection: IntType = 1


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
    AuthenticodeSignatureInformation,
    CertificateExtensionsCommon,
    CertificateRequest,
    DSACertificateExtensions,
    DerEncoder,
    DerSequenceReader,
    ECDsaCertificateExtensions,
    ECDsaX509SignatureGenerator,
    EncodingHelpers,
    GeneralNameEncoder,
    Oids,
    Pkcs10CertificationRequestInfo,
    Pkcs9ExtensionRequest,
    PublicKey,
    RSACertificateExtensions,
    RSAPkcs1X509SignatureGenerator,
    RSAPssX509SignatureGenerator,
    SafeCertContextHandle,
    SafeCertStoreHandle,
    SubjectAlternativeNameBuilder,
    TbsCertificate,
    TimestampInformation,
    X500DistinguishedName,
    X501Attribute,
    X509BasicConstraintsExtension,
    X509Certificate,
    X509Certificate2,
    X509Certificate2Collection,
    X509Certificate2Enumerator,
    X509Certificate2UI,
    X509CertificateCollection,
    X509CertificateExtensions,
    X509Chain,
    X509ChainElement,
    X509ChainElementCollection,
    X509ChainElementEnumerator,
    X509ChainPolicy,
    X509Constants,
    X509EnhancedKeyUsageExtension,
    X509Extension,
    X509ExtensionCollection,
    X509ExtensionEnumerator,
    X509KeyUsageExtension,
    X509Native,
    X509SignatureGenerator,
    X509Store,
    X509SubjectKeyIdentifierExtension,
    X509Utils,
    CRYPT_OID_INFO,
    PinAndClear,
    X509ChainStatus,
    OidGroup,
    OidKeyType,
    OpenFlags,
    StoreLocation,
    StoreName,
    TrustStatus,
    X500DistinguishedNameFlags,
    X509ChainStatusFlags,
    X509ContentType,
    X509FindType,
    X509IncludeOption,
    X509KeyStorageFlags,
    X509KeyUsageFlags,
    X509NameType,
    X509RevocationFlag,
    X509RevocationMode,
    X509SelectionFlag,
    X509SubjectKeyIdentifierHashAlgorithm,
    X509VerificationFlags,
]
