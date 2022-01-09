from __future__ import annotations

from abc import ABC
from typing import List, Tuple, Union, overload

from Microsoft.Win32.SafeHandles import SafeAxlBufferHandle, SafeHandleZeroOrMinusOneIsInvalid
from System import Array, Boolean, Byte, DateTime, DateTimeOffset, Enum, IDisposable, Int32, IntPtr, Object, String, Uri, ValueType, Void
from System.Collections.ObjectModel import Collection
from System.Net import IPAddress
from System.Runtime.InteropServices.ComTypes import FILETIME
from System.Security.Cryptography import AsnEncodedData, CapiNative, DSA, ECDsa, HashAlgorithmName, RSA, RSASignaturePadding, SignatureVerificationResult
from System.Security.Cryptography.X509Certificates import PublicKey, X500DistinguishedName, X509Certificate2, X509Chain, X509Extension

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


# ---------- Structs ---------- #

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


# No Interfaces

# ---------- Enums ---------- #

class TrustStatus(Enum):
    Untrusted: IntType = 0
    UnknownIdentity: IntType = 1
    KnownIdentity: IntType = 2
    Trusted: IntType = 3


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
    RSACertificateExtensions,
    RSAPkcs1X509SignatureGenerator,
    RSAPssX509SignatureGenerator,
    SafeCertContextHandle,
    SubjectAlternativeNameBuilder,
    TbsCertificate,
    TimestampInformation,
    X501Attribute,
    X509Native,
    X509SignatureGenerator,
    PinAndClear,
    TrustStatus,
]
