"""Automatically generated stubs for C# namespace: System.Security.Cryptography.X509Certificates."""

from abc import ABC
from collections.abc import Iterator
from typing import ClassVar
from typing import Final
from typing import overload

from Microsoft.Win32.SafeHandles import SafeAxlBufferHandle
from Microsoft.Win32.SafeHandles import SafeHandleZeroOrMinusOneIsInvalid
from Microsoft.Win32.SafeHandles import SafeX509ChainHandle
from System import Array
from System import ArraySegment
from System import Boolean
from System import Byte
from System import Char
from System import DateTime
from System import DateTimeOffset
from System import Enum
from System import IDisposable
from System import IEquatable
from System import Int32
from System import Int64
from System import IntPtr
from System import Object
from System import TimeSpan
from System import Type
from System import UInt16
from System import UInt32
from System import UInt64
from System import Uri
from System import ValueType
from System.Collections import CollectionBase
from System.Collections import ICollection
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections import IList
from System.Collections.Generic import IComparer
from System.Collections.ObjectModel import Collection
from System.Net import IPAddress
from System.Runtime.InteropServices import SafeHandle
from System.Runtime.InteropServices.ComTypes import FILETIME
from System.Runtime.Serialization import IDeserializationCallback
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Security import SecureString
from System.Security.Cryptography import CRYPTOAPI_BLOB
from System.Security.Cryptography import DSA
from System.Security.Cryptography import RSA
from System.Security.Cryptography import AsnEncodedData
from System.Security.Cryptography import AsymmetricAlgorithm
from System.Security.Cryptography import ECDsa
from System.Security.Cryptography import HashAlgorithmName
from System.Security.Cryptography import Oid
from System.Security.Cryptography import OidCollection
from System.Security.Cryptography import RSASignaturePadding
from System.Security.Cryptography import SignatureVerificationResult
from System.Text import Encoding

class AlgorithmIdentifierAsn(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Asn1Tag(ValueType, IEquatable[Asn1Tag]):
    """"""

    ConstructedBitString: ClassVar[Asn1Tag]
    """"""
    ConstructedOctetString: ClassVar[Asn1Tag]
    """"""
    Integer: ClassVar[Asn1Tag]
    """"""
    Null: ClassVar[Asn1Tag]
    """"""
    ObjectIdentifier: ClassVar[Asn1Tag]
    """"""
    PrimitiveBitString: ClassVar[Asn1Tag]
    """"""
    PrimitiveOctetString: ClassVar[Asn1Tag]
    """"""
    Sequence: ClassVar[Asn1Tag]
    """"""
    SetOf: ClassVar[Asn1Tag]
    """"""
    @overload
    def __init__(self, universalTagNumber: UniversalTagNumber, isConstructed: bool) -> None:
        """"""
    @overload
    def __init__(self, tagClass: TagClass, tagValue: int, isConstructed: bool) -> None:
        """"""
    @overload
    def __init__(self, tagClass: TagClass, tagValue: int) -> None:
        """"""
    @property
    def IsConstructed(self) -> bool:
        """"""
    @property
    def TagClass(self) -> TagClass:
        """"""
    @property
    def TagValue(self) -> int:
        """"""
    def AsConstructed(self) -> Asn1Tag:
        """"""
    @classmethod
    def Decode(cls, source: ReadOnlySpan[int], bytesConsumed: Int32) -> tuple[Asn1Tag, Int32]:
        """"""
    @overload
    def Equals(self, other: Asn1Tag) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def HasSameClassAndValue(self, other: Asn1Tag) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def TryDecode(
        cls, source: ReadOnlySpan[int], tag: Asn1Tag, bytesConsumed: Int32
    ) -> tuple[bool, Asn1Tag, Int32]:
        """"""
    @classmethod
    def op_Equality(cls, left: Asn1Tag, right: Asn1Tag) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: Asn1Tag, right: Asn1Tag) -> bool:
        """"""
    def __eq__(self, other: Asn1Tag) -> bool:
        """"""
    def __ne__(self, other: Asn1Tag) -> bool:
        """"""

class AsnDecoder(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def ReadBitString(
        cls,
        source: ReadOnlySpan[int],
        ruleSet: AsnEncodingRules,
        unusedBitCount: Int32,
        bytesConsumed: Int32,
        expectedTag: Asn1Tag | None,
    ) -> tuple[Array[int], Int32, Int32]:
        """"""
    @classmethod
    def ReadEncodedValue(
        cls,
        source: ReadOnlySpan[int],
        ruleSet: AsnEncodingRules,
        contentOffset: Int32,
        contentLength: Int32,
        bytesConsumed: Int32,
    ) -> tuple[Asn1Tag, Int32, Int32, Int32]:
        """"""
    @classmethod
    def ReadIntegerBytes(
        cls,
        source: ReadOnlySpan[int],
        ruleSet: AsnEncodingRules,
        bytesConsumed: Int32,
        expectedTag: Asn1Tag | None,
    ) -> tuple[ReadOnlySpan[int], Int32]:
        """"""
    @classmethod
    def ReadNull(
        cls,
        source: ReadOnlySpan[int],
        ruleSet: AsnEncodingRules,
        bytesConsumed: Int32,
        expectedTag: Asn1Tag | None,
    ) -> tuple[None, Int32]:
        """"""
    @classmethod
    def ReadObjectIdentifier(
        cls,
        source: ReadOnlySpan[int],
        ruleSet: AsnEncodingRules,
        bytesConsumed: Int32,
        expectedTag: Asn1Tag | None,
    ) -> tuple[Array[int], Int32]:
        """"""
    @classmethod
    def ReadOctetString(
        cls,
        source: ReadOnlySpan[int],
        ruleSet: AsnEncodingRules,
        bytesConsumed: Int32,
        expectedTag: Asn1Tag | None,
    ) -> tuple[Array[int], Int32]:
        """"""
    @classmethod
    def ReadSequence(
        cls,
        source: ReadOnlySpan[int],
        ruleSet: AsnEncodingRules,
        contentOffset: Int32,
        contentLength: Int32,
        bytesConsumed: Int32,
        expectedTag: Asn1Tag | None,
    ) -> tuple[None, Int32, Int32, Int32]:
        """"""
    @classmethod
    def ReadSetOf(
        cls,
        source: ReadOnlySpan[int],
        ruleSet: AsnEncodingRules,
        contentOffset: Int32,
        contentLength: Int32,
        bytesConsumed: Int32,
        skipSortOrderValidation: bool,
        expectedTag: Asn1Tag | None,
    ) -> tuple[None, Int32, Int32, Int32]:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def TryReadBitString(
        cls,
        source: ReadOnlySpan[int],
        destination: Span[int],
        ruleSet: AsnEncodingRules,
        unusedBitCount: Int32,
        bytesConsumed: Int32,
        bytesWritten: Int32,
        expectedTag: Asn1Tag | None,
    ) -> tuple[bool, Int32, Int32, Int32]:
        """"""
    @classmethod
    def TryReadEncodedValue(
        cls,
        source: ReadOnlySpan[int],
        ruleSet: AsnEncodingRules,
        tag: Asn1Tag,
        contentOffset: Int32,
        contentLength: Int32,
        bytesConsumed: Int32,
    ) -> tuple[bool, Asn1Tag, Int32, Int32, Int32]:
        """"""
    @classmethod
    def TryReadInt32(
        cls,
        source: ReadOnlySpan[int],
        ruleSet: AsnEncodingRules,
        value: Int32,
        bytesConsumed: Int32,
        expectedTag: Asn1Tag | None,
    ) -> tuple[bool, Int32, Int32]:
        """"""
    @classmethod
    def TryReadInt64(
        cls,
        source: ReadOnlySpan[int],
        ruleSet: AsnEncodingRules,
        value: Int64,
        bytesConsumed: Int32,
        expectedTag: Asn1Tag | None,
    ) -> tuple[bool, Int64, Int32]:
        """"""
    @classmethod
    def TryReadOctetString(
        cls,
        source: ReadOnlySpan[int],
        destination: Span[int],
        ruleSet: AsnEncodingRules,
        bytesConsumed: Int32,
        bytesWritten: Int32,
        expectedTag: Asn1Tag | None,
    ) -> tuple[bool, Int32, Int32]:
        """"""
    @classmethod
    def TryReadPrimitiveBitString(
        cls,
        source: ReadOnlySpan[int],
        ruleSet: AsnEncodingRules,
        unusedBitCount: Int32,
        value: ReadOnlySpan[int],
        bytesConsumed: Int32,
        expectedTag: Asn1Tag | None,
    ) -> tuple[bool, Int32, ReadOnlySpan[int], Int32]:
        """"""
    @classmethod
    def TryReadPrimitiveOctetString(
        cls,
        source: ReadOnlySpan[int],
        ruleSet: AsnEncodingRules,
        value: ReadOnlySpan[int],
        bytesConsumed: Int32,
        expectedTag: Asn1Tag | None,
    ) -> tuple[bool, ReadOnlySpan[int], Int32]:
        """"""
    @classmethod
    def TryReadUInt32(
        cls,
        source: ReadOnlySpan[int],
        ruleSet: AsnEncodingRules,
        value: UInt32,
        bytesConsumed: Int32,
        expectedTag: Asn1Tag | None,
    ) -> tuple[bool, UInt32, Int32]:
        """"""
    @classmethod
    def TryReadUInt64(
        cls,
        source: ReadOnlySpan[int],
        ruleSet: AsnEncodingRules,
        value: UInt64,
        bytesConsumed: Int32,
        expectedTag: Asn1Tag | None,
    ) -> tuple[bool, UInt64, Int32]:
        """"""

class AsnEncodingRules(Enum):
    """"""

    BER: AsnEncodingRules = ...
    """"""
    CER: AsnEncodingRules = ...
    """"""
    DER: AsnEncodingRules = ...
    """"""

class AsnReader(Object):
    """"""
    @overload
    def __init__(
        self, data: ReadOnlyMemory[int], ruleSet: AsnEncodingRules, options: AsnReaderOptions
    ) -> None:
        """"""
    @overload
    def __init__(self, data: ReadOnlyMemory[int], ruleSet: AsnEncodingRules) -> None:
        """"""
    @property
    def HasData(self) -> bool:
        """"""
    @property
    def RuleSet(self) -> AsnEncodingRules:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def PeekContentBytes(self) -> ReadOnlyMemory[int]:
        """"""
    def PeekEncodedValue(self) -> ReadOnlyMemory[int]:
        """"""
    def PeekTag(self) -> Asn1Tag:
        """"""
    def ReadBitString(
        self, unusedBitCount: Int32, expectedTag: Asn1Tag | None
    ) -> tuple[Array[int], Int32]:
        """"""
    def ReadEncodedValue(self) -> ReadOnlyMemory[int]:
        """"""
    def ReadIntegerBytes(self, expectedTag: Asn1Tag | None) -> ReadOnlyMemory[int]:
        """"""
    def ReadNull(self, expectedTag: Asn1Tag | None) -> None:
        """"""
    def ReadObjectIdentifier(self, expectedTag: Asn1Tag | None) -> Array[int]:
        """"""
    def ReadOctetString(self, expectedTag: Asn1Tag | None) -> Array[int]:
        """"""
    def ReadSequence(self, expectedTag: Asn1Tag | None) -> AsnReader:
        """"""
    @overload
    def ReadSetOf(self, expectedTag: Asn1Tag | None) -> AsnReader:
        """"""
    @overload
    def ReadSetOf(self, skipSortOrderValidation: bool, expectedTag: Asn1Tag | None) -> AsnReader:
        """"""
    def ThrowIfNotEmpty(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TryReadBitString(
        self,
        destination: Span[int],
        unusedBitCount: Int32,
        bytesWritten: Int32,
        expectedTag: Asn1Tag | None,
    ) -> tuple[bool, Int32, Int32]:
        """"""
    def TryReadInt32(self, value: Int32, expectedTag: Asn1Tag | None) -> tuple[bool, Int32]:
        """"""
    def TryReadInt64(self, value: Int64, expectedTag: Asn1Tag | None) -> tuple[bool, Int64]:
        """"""
    def TryReadOctetString(
        self, destination: Span[int], bytesWritten: Int32, expectedTag: Asn1Tag | None
    ) -> tuple[bool, Int32]:
        """"""
    def TryReadPrimitiveBitString(
        self, unusedBitCount: Int32, value: ReadOnlyMemory[int], expectedTag: Asn1Tag | None
    ) -> tuple[bool, Int32, ReadOnlyMemory[int]]:
        """"""
    def TryReadPrimitiveOctetString(
        self, contents: ReadOnlyMemory[int], expectedTag: Asn1Tag | None
    ) -> tuple[bool, ReadOnlyMemory[int]]:
        """"""
    def TryReadUInt32(self, value: UInt32, expectedTag: Asn1Tag | None) -> tuple[bool, UInt32]:
        """"""
    def TryReadUInt64(self, value: UInt64, expectedTag: Asn1Tag | None) -> tuple[bool, UInt64]:
        """"""

class AsnReaderOptions(ValueType):
    """"""
    @property
    def SkipSetSortOrderVerification(self) -> bool:
        """"""
    @SkipSetSortOrderVerification.setter
    def SkipSetSortOrderVerification(self, value: bool) -> None: ...
    @property
    def UtcTimeTwoDigitYearMax(self) -> int:
        """"""
    @UtcTimeTwoDigitYearMax.setter
    def UtcTimeTwoDigitYearMax(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class AsnValueReader(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class AttributeAsn(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class AuthenticodeSignatureInformation(Object):
    """"""
    @property
    def Description(self) -> str:
        """"""
    @property
    def DescriptionUrl(self) -> Uri:
        """"""
    @property
    def HResult(self) -> int:
        """"""
    @property
    def HashAlgorithm(self) -> str:
        """"""
    @property
    def SignatureChain(self) -> X509Chain:
        """"""
    @property
    def SigningCertificate(self) -> X509Certificate2:
        """"""
    @property
    def Timestamp(self) -> TimestampInformation:
        """"""
    @property
    def TrustStatus(self) -> TrustStatus:
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

class BinaryPrimitives(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def ReadInt16BigEndian(cls, bytes: ReadOnlySpan[int]) -> int:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def TryReadUInt16BigEndian(cls, bytes: ReadOnlySpan[int], value: UInt16) -> tuple[bool, UInt16]:
        """"""

class CRYPT_OID_INFO(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CertificateExtensionsCommon(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CertificateRequest(Object):
    """"""
    @overload
    def __init__(self, subjectName: str, key: ECDsa, hashAlgorithm: HashAlgorithmName) -> None:
        """"""
    @overload
    def __init__(
        self, subjectName: X500DistinguishedName, key: ECDsa, hashAlgorithm: HashAlgorithmName
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        subjectName: str,
        key: RSA,
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        subjectName: X500DistinguishedName,
        key: RSA,
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        subjectName: X500DistinguishedName,
        publicKey: PublicKey,
        hashAlgorithm: HashAlgorithmName,
    ) -> None:
        """"""
    @property
    def CertificateExtensions(self) -> Collection[X509Extension]:
        """"""
    @property
    def HashAlgorithm(self) -> HashAlgorithmName:
        """"""
    @property
    def PublicKey(self) -> PublicKey:
        """"""
    @property
    def SubjectName(self) -> X500DistinguishedName:
        """"""
    @overload
    def Create(
        self,
        issuerName: X500DistinguishedName,
        generator: X509SignatureGenerator,
        notBefore: DateTimeOffset,
        notAfter: DateTimeOffset,
        serialNumber: Array[int],
    ) -> X509Certificate2:
        """"""
    @overload
    def Create(
        self,
        issuerCertificate: X509Certificate2,
        notBefore: DateTimeOffset,
        notAfter: DateTimeOffset,
        serialNumber: Array[int],
    ) -> X509Certificate2:
        """"""
    def CreateSelfSigned(
        self, notBefore: DateTimeOffset, notAfter: DateTimeOffset
    ) -> X509Certificate2:
        """"""
    @overload
    def CreateSigningRequest(self) -> Array[int]:
        """"""
    @overload
    def CreateSigningRequest(self, signatureGenerator: X509SignatureGenerator) -> Array[int]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ContentInfoAsn(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CryptoPool(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Rent(cls, size: int) -> Array[int]:
        """"""
    @classmethod
    @overload
    def Return(cls, segment: ArraySegment[int]) -> None:
        """"""
    @classmethod
    @overload
    def Return(cls, segment: ArraySegment[int], clearSize: int) -> None:
        """"""
    @classmethod
    @overload
    def Return(cls, array: Array[int]) -> None:
        """"""
    @classmethod
    @overload
    def Return(cls, array: Array[int], clearSize: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class CryptographicOperations(ABC, Object):
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
    def ZeroMemory(cls, buffer: Span[int]) -> None:
        """"""

class DSACertificateExtensions(ABC, Object):
    """"""
    @classmethod
    def CopyWithPrivateKey(cls, certificate: X509Certificate2, privateKey: DSA) -> X509Certificate2:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetDSAPrivateKey(cls, certificate: X509Certificate2) -> DSA:
        """"""
    @classmethod
    def GetDSAPublicKey(cls, certificate: X509Certificate2) -> DSA:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DerEncoder(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DerSequenceReader(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DigestInfoAsn(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ECDsaCertificateExtensions(ABC, Object):
    """"""
    @classmethod
    def CopyWithPrivateKey(
        cls, certificate: X509Certificate2, privateKey: ECDsa
    ) -> X509Certificate2:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetECDsaPrivateKey(cls, certificate: X509Certificate2) -> ECDsa:
        """"""
    @classmethod
    def GetECDsaPublicKey(cls, certificate: X509Certificate2) -> ECDsa:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ECDsaX509SignatureGenerator(X509SignatureGenerator):
    """"""
    @property
    def PublicKey(self) -> PublicKey:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetSignatureAlgorithmIdentifier(self, hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """"""
    def GetType(self) -> Type:
        """"""
    def SignData(self, data: Array[int], hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """"""
    def ToString(self) -> str:
        """"""

class EncodingHelpers(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class EncryptedContentInfoAsn(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class EncryptedDataAsn(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class EncryptedPrivateKeyInfoAsn(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class GeneralNameEncoder(Object):
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

class Helpers(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IncrementalHash(Object, IDisposable):
    """"""
    def AppendData(self, data: ReadOnlySpan[int]) -> None:
        """"""
    @classmethod
    def CreateHash(cls, hashAlgorithm: HashAlgorithmName) -> IncrementalHash:
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
    def TryGetHashAndReset(self, destination: Span[int], bytesWritten: Int32) -> tuple[bool, Int32]:
        """"""

class IterationCountLimitEnforcer(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class KdfWorkLimiter(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MacData(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class OidGroup(Enum):
    """"""

    AllGroups: OidGroup = ...
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
    DisableSearchDS: OidGroup = ...
    """"""

class OidKeyType(Enum):
    """"""

    Oid: OidKeyType = ...
    """"""
    Name: OidKeyType = ...
    """"""
    AlgorithmID: OidKeyType = ...
    """"""
    SignatureID: OidKeyType = ...
    """"""
    CngAlgorithmID: OidKeyType = ...
    """"""
    CngSignatureID: OidKeyType = ...
    """"""

class Oids(ABC, Object):
    """"""

    AnyCertPolicy: ClassVar[str]
    """"""
    ApplicationCertPolicies: ClassVar[str]
    """"""
    AuthorityInformationAccess: ClassVar[str]
    """"""
    BasicConstraints: ClassVar[str]
    """"""
    BasicConstraints2: ClassVar[str]
    """"""
    CertPolicies: ClassVar[str]
    """"""
    CertPolicyConstraints: ClassVar[str]
    """"""
    CertPolicyMappings: ClassVar[str]
    """"""
    CertificateAuthorityIssuers: ClassVar[str]
    """"""
    CertificateTemplate: ClassVar[str]
    """"""
    CommonName: ClassVar[str]
    """"""
    CrlDistributionPoints: ClassVar[str]
    """"""
    DsaDsa: ClassVar[str]
    """"""
    ECDsaSha256: ClassVar[str]
    """"""
    ECDsaSha384: ClassVar[str]
    """"""
    ECDsaSha512: ClassVar[str]
    """"""
    Ecc: ClassVar[str]
    """"""
    EccCurveSecp256r1: ClassVar[str]
    """"""
    EccCurveSecp384r1: ClassVar[str]
    """"""
    EccCurveSecp521r1: ClassVar[str]
    """"""
    EmailAddress: ClassVar[str]
    """"""
    EnhancedKeyUsage: ClassVar[str]
    """"""
    EnrollCertTypeExtension: ClassVar[str]
    """"""
    InhibitAnyPolicyExtension: ClassVar[str]
    """"""
    IssuerAltName: ClassVar[str]
    """"""
    KeyUsage: ClassVar[str]
    """"""
    Mgf1: ClassVar[str]
    """"""
    Organization: ClassVar[str]
    """"""
    OrganizationalUnit: ClassVar[str]
    """"""
    Pkcs9ExtensionRequest: ClassVar[str]
    """"""
    RsaPkcs1Sha256: ClassVar[str]
    """"""
    RsaPkcs1Sha384: ClassVar[str]
    """"""
    RsaPkcs1Sha512: ClassVar[str]
    """"""
    RsaRsa: ClassVar[str]
    """"""
    RsaSsaPss: ClassVar[str]
    """"""
    Sha256: ClassVar[str]
    """"""
    Sha384: ClassVar[str]
    """"""
    Sha512: ClassVar[str]
    """"""
    SubjectAltName: ClassVar[str]
    """"""
    SubjectKeyIdentifier: ClassVar[str]
    """"""
    UserPrincipalName: ClassVar[str]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class OpenAlgorithmProviderFlags(Enum):
    """"""

    NONE: OpenAlgorithmProviderFlags = ...
    """"""
    BCRYPT_ALG_HANDLE_HMAC_FLAG: OpenAlgorithmProviderFlags = ...
    """"""

class OpenFlags(Enum):
    """"""

    ReadOnly: OpenFlags = ...
    """"""
    ReadWrite: OpenFlags = ...
    """"""
    MaxAllowed: OpenFlags = ...
    """"""
    OpenExistingOnly: OpenFlags = ...
    """"""
    IncludeArchived: OpenFlags = ...
    """"""

class PBEParameter(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class PBES2Params(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class PasswordBasedEncryption(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Pbkdf2(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Pbkdf2Params(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Pbkdf2SaltChoice(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class PfxAsn(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class PinAndClear(ValueType, IDisposable):
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

class Pkcs10CertificationRequestInfo(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Pkcs12Kdf(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Pkcs9ExtensionRequest(X501Attribute):
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

class PrivateKeyEnforcer(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class PublicKey(Object):
    """"""
    def __init__(self, oid: Oid, parameters: AsnEncodedData, keyValue: AsnEncodedData) -> None:
        """"""
    @property
    def EncodedKeyValue(self) -> AsnEncodedData:
        """"""
    @property
    def EncodedParameters(self) -> AsnEncodedData:
        """"""
    @property
    def Key(self) -> AsymmetricAlgorithm:
        """"""
    @property
    def Oid(self) -> Oid:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RSACertificateExtensions(ABC, Object):
    """"""
    @classmethod
    def CopyWithPrivateKey(cls, certificate: X509Certificate2, privateKey: RSA) -> X509Certificate2:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetRSAPrivateKey(cls, certificate: X509Certificate2) -> RSA:
        """"""
    @classmethod
    def GetRSAPublicKey(cls, certificate: X509Certificate2) -> RSA:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RSAPkcs1X509SignatureGenerator(X509SignatureGenerator):
    """"""
    @property
    def PublicKey(self) -> PublicKey:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetSignatureAlgorithmIdentifier(self, hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """"""
    def GetType(self) -> Type:
        """"""
    def SignData(self, data: Array[int], hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """"""
    def ToString(self) -> str:
        """"""

class RSAPssX509SignatureGenerator(X509SignatureGenerator):
    """"""
    @property
    def PublicKey(self) -> PublicKey:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetSignatureAlgorithmIdentifier(self, hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """"""
    def GetType(self) -> Type:
        """"""
    def SignData(self, data: Array[int], hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """"""
    def ToString(self) -> str:
        """"""

class Rc2CbcParameters(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ReadOnlyMemory[T](ValueType):
    """"""
    @overload
    def __init__(self, segment: ArraySegment[T]) -> None:
        """"""
    @overload
    def __init__(self, array: Array[T], offset: int, count: int) -> None:
        """"""
    @overload
    def __init__(self, array: Array[T]) -> None:
        """"""
    @property
    def IsEmpty(self) -> bool:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Span(self) -> ReadOnlySpan[T]:
        """"""
    def CopyTo(self, destination: Span[T]) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def Slice(self, start: int) -> ReadOnlyMemory[T]:
        """"""
    @overload
    def Slice(self, start: int, length: int) -> ReadOnlyMemory[T]:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    @overload
    def op_Implicit(cls, memory: ReadOnlyMemory[T]) -> ArraySegment[T]:
        """"""
    @classmethod
    @overload
    def op_Implicit(cls, segment: ArraySegment[T]) -> ReadOnlyMemory[T]:
        """"""
    @classmethod
    @overload
    def op_Implicit(cls, array: Array[T]) -> ReadOnlyMemory[T]:
        """"""

class ReadOnlySpan[T](ValueType):
    """"""

    Empty: ClassVar[Span[T]]
    """"""
    @overload
    def __init__(self, segment: ArraySegment[T]) -> None:
        """"""
    @overload
    def __init__(self, array: Array[T], offset: int, count: int) -> None:
        """"""
    @overload
    def __init__(self, array: Array[T]) -> None:
        """"""
    @property
    def IsEmpty(self) -> bool:
        """"""
    @property
    def IsNull(self) -> bool:
        """"""
    @property
    def Item(self) -> T:
        """"""
    @property
    def Length(self) -> int:
        """"""
    def CopyTo(self, destination: Span[T]) -> None:
        """"""
    def DangerousGetArraySegment(self) -> ArraySegment[T]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def Overlaps(self, destination: ReadOnlySpan[T]) -> bool:
        """"""
    @overload
    def Overlaps(self, destination: ReadOnlySpan[T], elementOffset: Int32) -> tuple[bool, Int32]:
        """"""
    @overload
    def Slice(self, start: int) -> ReadOnlySpan[T]:
        """"""
    @overload
    def Slice(self, start: int, length: int) -> ReadOnlySpan[T]:
        """"""
    def ToArray(self) -> Array[T]:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Implicit(cls, array: Array[T]) -> ReadOnlySpan[T]:
        """"""
    def __getitem__(self, index: int) -> T:
        """"""

class SR(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SafeBCryptAlgorithmHandle(SafeHandle, IDisposable):
    """"""
    def __init__(self) -> None:
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

class SafeBagAsn(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

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

class SetOfValueComparer(Object, IComparer[ReadOnlyMemory[Byte]]):
    """"""
    def __init__(self) -> None:
        """"""
    def Compare(self, x: ReadOnlyMemory[int], y: ReadOnlyMemory[int]) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Span[T](ValueType):
    """"""

    Empty: ClassVar[Span[T]]
    """"""
    @overload
    def __init__(self, segment: ArraySegment[T]) -> None:
        """"""
    @overload
    def __init__(self, array: Array[T], offset: int, count: int) -> None:
        """"""
    @overload
    def __init__(self, array: Array[T]) -> None:
        """"""
    @property
    def IsEmpty(self) -> bool:
        """"""
    @property
    def Item(self) -> T:
        """"""
    @Item.setter
    def Item(self, value: T) -> None: ...
    @property
    def Length(self) -> int:
        """"""
    def Clear(self) -> None:
        """"""
    def CopyTo(self, destination: Span[T]) -> None:
        """"""
    def DangerousGetArrayForPinning(self) -> Array[T]:
        """"""
    def DangerousGetArraySegment(self) -> ArraySegment[T]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Fill(self, value: T) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Overlaps(self, destination: ReadOnlySpan[T], elementOffset: Int32) -> tuple[bool, Int32]:
        """"""
    @overload
    def Slice(self, start: int) -> Span[T]:
        """"""
    @overload
    def Slice(self, start: int, length: int) -> Span[T]:
        """"""
    def ToArray(self) -> Array[T]:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    @overload
    def op_Implicit(cls, span: Span[T]) -> ReadOnlySpan[T]:
        """"""
    @classmethod
    @overload
    def op_Implicit(cls, array: Array[T]) -> Span[T]:
        """"""
    def __getitem__(self, index: int) -> T:
        """"""
    def __setitem__(self, index: int, value: T) -> None:
        """"""

class StoreLocation(Enum):
    """"""

    CurrentUser: StoreLocation = ...
    """"""
    LocalMachine: StoreLocation = ...
    """"""

class StoreName(Enum):
    """"""

    AddressBook: StoreName = ...
    """"""
    AuthRoot: StoreName = ...
    """"""
    CertificateAuthority: StoreName = ...
    """"""
    Disallowed: StoreName = ...
    """"""
    My: StoreName = ...
    """"""
    Root: StoreName = ...
    """"""
    TrustedPeople: StoreName = ...
    """"""
    TrustedPublisher: StoreName = ...
    """"""

class SubjectAlternativeNameBuilder(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def AddDnsName(self, dnsName: str) -> None:
        """"""
    def AddEmailAddress(self, emailAddress: str) -> None:
        """"""
    def AddIpAddress(self, ipAddress: IPAddress) -> None:
        """"""
    def AddUri(self, uri: Uri) -> None:
        """"""
    def AddUserPrincipalName(self, upn: str) -> None:
        """"""
    def Build(self, critical: bool = ...) -> X509Extension:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TagClass(Enum):
    """"""

    Universal: TagClass = ...
    """"""
    Application: TagClass = ...
    """"""
    ContextSpecific: TagClass = ...
    """"""
    Private: TagClass = ...
    """"""

class TbsCertificate(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def Extensions(self) -> Collection[X509Extension]:
        """"""
    @property
    def Issuer(self) -> X500DistinguishedName:
        """"""
    @Issuer.setter
    def Issuer(self, value: X500DistinguishedName) -> None: ...
    @property
    def NotAfter(self) -> DateTimeOffset:
        """"""
    @NotAfter.setter
    def NotAfter(self, value: DateTimeOffset) -> None: ...
    @property
    def NotBefore(self) -> DateTimeOffset:
        """"""
    @NotBefore.setter
    def NotBefore(self, value: DateTimeOffset) -> None: ...
    @property
    def PublicKey(self) -> PublicKey:
        """"""
    @PublicKey.setter
    def PublicKey(self, value: PublicKey) -> None: ...
    @property
    def SerialNumber(self) -> Array[int]:
        """"""
    @SerialNumber.setter
    def SerialNumber(self, value: Array[int]) -> None: ...
    @property
    def SignatureAlgorithm(self) -> Array[int]:
        """"""
    @SignatureAlgorithm.setter
    def SignatureAlgorithm(self, value: Array[int]) -> None: ...
    @property
    def Subject(self) -> X500DistinguishedName:
        """"""
    @Subject.setter
    def Subject(self, value: X500DistinguishedName) -> None: ...
    @property
    def Version(self) -> int:
        """"""
    @Version.setter
    def Version(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TimestampInformation(Object):
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
    def SignatureChain(self) -> X509Chain:
        """"""
    @property
    def SigningCertificate(self) -> X509Certificate2:
        """"""
    @property
    def Timestamp(self) -> DateTime:
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

class Triple[T1, T2, T3](ValueType):
    """"""
    @property
    def Item1(self) -> T1:
        """"""
    @property
    def Item2(self) -> T2:
        """"""
    @property
    def Item3(self) -> T3:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TrustStatus(Enum):
    """"""

    Untrusted: TrustStatus = ...
    """"""
    UnknownIdentity: TrustStatus = ...
    """"""
    KnownIdentity: TrustStatus = ...
    """"""
    Trusted: TrustStatus = ...
    """"""

class UniversalTagNumber(Enum):
    """"""

    EndOfContents: UniversalTagNumber = ...
    """"""
    Boolean: UniversalTagNumber = ...
    """"""
    Integer: UniversalTagNumber = ...
    """"""
    BitString: UniversalTagNumber = ...
    """"""
    OctetString: UniversalTagNumber = ...
    """"""
    Null: UniversalTagNumber = ...
    """"""
    ObjectIdentifier: UniversalTagNumber = ...
    """"""
    ObjectDescriptor: UniversalTagNumber = ...
    """"""
    External: UniversalTagNumber = ...
    """"""
    InstanceOf: UniversalTagNumber = ...
    """"""
    Real: UniversalTagNumber = ...
    """"""
    Enumerated: UniversalTagNumber = ...
    """"""
    Embedded: UniversalTagNumber = ...
    """"""
    UTF8String: UniversalTagNumber = ...
    """"""
    RelativeObjectIdentifier: UniversalTagNumber = ...
    """"""
    Time: UniversalTagNumber = ...
    """"""
    Sequence: UniversalTagNumber = ...
    """"""
    SequenceOf: UniversalTagNumber = ...
    """"""
    Set: UniversalTagNumber = ...
    """"""
    SetOf: UniversalTagNumber = ...
    """"""
    NumericString: UniversalTagNumber = ...
    """"""
    PrintableString: UniversalTagNumber = ...
    """"""
    TeletexString: UniversalTagNumber = ...
    """"""
    T61String: UniversalTagNumber = ...
    """"""
    VideotexString: UniversalTagNumber = ...
    """"""
    IA5String: UniversalTagNumber = ...
    """"""
    UtcTime: UniversalTagNumber = ...
    """"""
    GeneralizedTime: UniversalTagNumber = ...
    """"""
    GraphicString: UniversalTagNumber = ...
    """"""
    VisibleString: UniversalTagNumber = ...
    """"""
    ISO646String: UniversalTagNumber = ...
    """"""
    GeneralString: UniversalTagNumber = ...
    """"""
    UniversalString: UniversalTagNumber = ...
    """"""
    UnrestrictedCharacterString: UniversalTagNumber = ...
    """"""
    BMPString: UniversalTagNumber = ...
    """"""
    Date: UniversalTagNumber = ...
    """"""
    TimeOfDay: UniversalTagNumber = ...
    """"""
    DateTime: UniversalTagNumber = ...
    """"""
    Duration: UniversalTagNumber = ...
    """"""
    ObjectIdentifierIRI: UniversalTagNumber = ...
    """"""
    RelativeObjectIdentifierIRI: UniversalTagNumber = ...
    """"""

class Utility(ABC, Object):
    """"""
    @classmethod
    def EncodingGetByteCount(cls, encoding: Encoding, input: ReadOnlySpan[Char]) -> int:
        """"""
    @classmethod
    @overload
    def EncodingGetBytes(
        cls, encoding: Encoding, input: ReadOnlySpan[Char], destination: Span[int]
    ) -> int:
        """"""
    @classmethod
    @overload
    def EncodingGetBytes(
        cls, encoding: Encoding, input: Array[Char], destination: Span[int]
    ) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    @overload
    def GetSpanForArray[T](cls, array: Array[T], offset: int) -> Span[T]:
        """"""
    @classmethod
    @overload
    def GetSpanForArray[T](cls, array: Array[T], offset: int, count: int) -> Span[T]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class X500DistinguishedName(AsnEncodedData):
    """"""
    @overload
    def __init__(self, encodedDistinguishedName: Array[int]) -> None:
        """"""
    @overload
    def __init__(self, encodedDistinguishedName: AsnEncodedData) -> None:
        """"""
    @overload
    def __init__(self, distinguishedName: X500DistinguishedName) -> None:
        """"""
    @overload
    def __init__(self, distinguishedName: str) -> None:
        """"""
    @overload
    def __init__(self, distinguishedName: str, flag: X500DistinguishedNameFlags) -> None:
        """"""
    @property
    def Name(self) -> str:
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
    def Decode(self, flag: X500DistinguishedNameFlags) -> str:
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

class X500DistinguishedNameFlags(Enum):
    """"""

    _None: X500DistinguishedNameFlags = ...
    """"""
    Reversed: X500DistinguishedNameFlags = ...
    """"""
    UseSemicolons: X500DistinguishedNameFlags = ...
    """"""
    DoNotUsePlusSign: X500DistinguishedNameFlags = ...
    """"""
    DoNotUseQuotes: X500DistinguishedNameFlags = ...
    """"""
    UseCommas: X500DistinguishedNameFlags = ...
    """"""
    UseNewLines: X500DistinguishedNameFlags = ...
    """"""
    UseUTF8Encoding: X500DistinguishedNameFlags = ...
    """"""
    UseT61Encoding: X500DistinguishedNameFlags = ...
    """"""
    ForceUTF8Encoding: X500DistinguishedNameFlags = ...
    """"""

class X501Attribute(AsnEncodedData):
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

class X509BasicConstraintsExtension(X509Extension):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(
        self,
        certificateAuthority: bool,
        hasPathLengthConstraint: bool,
        pathLengthConstraint: int,
        critical: bool,
    ) -> None:
        """"""
    @overload
    def __init__(self, encodedBasicConstraints: AsnEncodedData, critical: bool) -> None:
        """"""
    @property
    def CertificateAuthority(self) -> bool:
        """"""
    @property
    def Critical(self) -> bool:
        """"""
    @Critical.setter
    def Critical(self, value: bool) -> None: ...
    @property
    def HasPathLengthConstraint(self) -> bool:
        """"""
    @property
    def Oid(self) -> Oid:
        """"""
    @Oid.setter
    def Oid(self, value: Oid) -> None: ...
    @property
    def PathLengthConstraint(self) -> int:
        """"""
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

class X509Certificate(Object, IDeserializationCallback, ISerializable, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, data: Array[int]) -> None:
        """"""
    @overload
    def __init__(self, rawData: Array[int], password: str) -> None:
        """"""
    @overload
    def __init__(self, rawData: Array[int], password: SecureString) -> None:
        """"""
    @overload
    def __init__(
        self, rawData: Array[int], password: str, keyStorageFlags: X509KeyStorageFlags
    ) -> None:
        """"""
    @overload
    def __init__(
        self, rawData: Array[int], password: SecureString, keyStorageFlags: X509KeyStorageFlags
    ) -> None:
        """"""
    @overload
    def __init__(self, fileName: str) -> None:
        """"""
    @overload
    def __init__(self, fileName: str, password: str) -> None:
        """"""
    @overload
    def __init__(self, fileName: str, password: SecureString) -> None:
        """"""
    @overload
    def __init__(self, fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags) -> None:
        """"""
    @overload
    def __init__(
        self, fileName: str, password: SecureString, keyStorageFlags: X509KeyStorageFlags
    ) -> None:
        """"""
    @overload
    def __init__(self, handle: IntPtr) -> None:
        """"""
    @overload
    def __init__(self, cert: X509Certificate) -> None:
        """"""
    @overload
    def __init__(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    @property
    def Handle(self) -> IntPtr:
        """"""
    @property
    def Issuer(self) -> str:
        """"""
    @property
    def Subject(self) -> str:
        """"""
    @classmethod
    def CreateFromCertFile(cls, filename: str) -> X509Certificate:
        """"""
    @classmethod
    def CreateFromSignedFile(cls, filename: str) -> X509Certificate:
        """"""
    def Dispose(self) -> None:
        """"""
    @overload
    def Equals(self, other: X509Certificate) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Export(self, contentType: X509ContentType) -> Array[int]:
        """"""
    @overload
    def Export(self, contentType: X509ContentType, password: SecureString) -> Array[int]:
        """"""
    @overload
    def Export(self, contentType: X509ContentType, password: str) -> Array[int]:
        """"""
    @overload
    def GetCertHash(self) -> Array[int]:
        """"""
    @overload
    def GetCertHash(self, hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """"""
    @overload
    def GetCertHashString(self) -> str:
        """"""
    @overload
    def GetCertHashString(self, hashAlgorithm: HashAlgorithmName) -> str:
        """"""
    def GetEffectiveDateString(self) -> str:
        """"""
    def GetExpirationDateString(self) -> str:
        """"""
    def GetFormat(self) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIssuerName(self) -> str:
        """"""
    def GetKeyAlgorithm(self) -> str:
        """"""
    def GetKeyAlgorithmParameters(self) -> Array[int]:
        """"""
    def GetKeyAlgorithmParametersString(self) -> str:
        """"""
    def GetName(self) -> str:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetPublicKey(self) -> Array[int]:
        """"""
    def GetPublicKeyString(self) -> str:
        """"""
    def GetRawCertData(self) -> Array[int]:
        """"""
    def GetRawCertDataString(self) -> str:
        """"""
    def GetSerialNumber(self) -> Array[int]:
        """"""
    def GetSerialNumberString(self) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def Import(self, rawData: Array[int]) -> None:
        """"""
    @overload
    def Import(
        self, rawData: Array[int], password: SecureString, keyStorageFlags: X509KeyStorageFlags
    ) -> None:
        """"""
    @overload
    def Import(
        self, rawData: Array[int], password: str, keyStorageFlags: X509KeyStorageFlags
    ) -> None:
        """"""
    @overload
    def Import(self, fileName: str) -> None:
        """"""
    @overload
    def Import(
        self, fileName: str, password: SecureString, keyStorageFlags: X509KeyStorageFlags
    ) -> None:
        """"""
    @overload
    def Import(self, fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags) -> None:
        """"""
    def OnDeserialization(self, sender: object) -> None:
        """"""
    def Reset(self) -> None:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, fVerbose: bool) -> str:
        """"""

class X509Certificate2(X509Certificate, IDeserializationCallback, ISerializable, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, rawData: Array[int]) -> None:
        """"""
    @overload
    def __init__(self, rawData: Array[int], password: str) -> None:
        """"""
    @overload
    def __init__(self, rawData: Array[int], password: SecureString) -> None:
        """"""
    @overload
    def __init__(
        self, rawData: Array[int], password: str, keyStorageFlags: X509KeyStorageFlags
    ) -> None:
        """"""
    @overload
    def __init__(
        self, rawData: Array[int], password: SecureString, keyStorageFlags: X509KeyStorageFlags
    ) -> None:
        """"""
    @overload
    def __init__(self, fileName: str) -> None:
        """"""
    @overload
    def __init__(self, fileName: str, password: str) -> None:
        """"""
    @overload
    def __init__(self, fileName: str, password: SecureString) -> None:
        """"""
    @overload
    def __init__(self, fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags) -> None:
        """"""
    @overload
    def __init__(
        self, fileName: str, password: SecureString, keyStorageFlags: X509KeyStorageFlags
    ) -> None:
        """"""
    @overload
    def __init__(self, handle: IntPtr) -> None:
        """"""
    @overload
    def __init__(self, certificate: X509Certificate) -> None:
        """"""
    @property
    def Archived(self) -> bool:
        """"""
    @Archived.setter
    def Archived(self, value: bool) -> None: ...
    @property
    def Extensions(self) -> X509ExtensionCollection:
        """"""
    @property
    def FriendlyName(self) -> str:
        """"""
    @FriendlyName.setter
    def FriendlyName(self, value: str) -> None: ...
    @property
    def Handle(self) -> IntPtr:
        """"""
    @property
    def HasPrivateKey(self) -> bool:
        """"""
    @property
    def Issuer(self) -> str:
        """"""
    @property
    def IssuerName(self) -> X500DistinguishedName:
        """"""
    @property
    def NotAfter(self) -> DateTime:
        """"""
    @property
    def NotBefore(self) -> DateTime:
        """"""
    @property
    def PrivateKey(self) -> AsymmetricAlgorithm:
        """"""
    @PrivateKey.setter
    def PrivateKey(self, value: AsymmetricAlgorithm) -> None: ...
    @property
    def PublicKey(self) -> PublicKey:
        """"""
    @property
    def RawData(self) -> Array[int]:
        """"""
    @property
    def SerialNumber(self) -> str:
        """"""
    @property
    def SignatureAlgorithm(self) -> Oid:
        """"""
    @property
    def Subject(self) -> str:
        """"""
    @property
    def SubjectName(self) -> X500DistinguishedName:
        """"""
    @property
    def Thumbprint(self) -> str:
        """"""
    @property
    def Version(self) -> int:
        """"""
    def Dispose(self) -> None:
        """"""
    @overload
    def Equals(self, other: X509Certificate) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Export(self, contentType: X509ContentType) -> Array[int]:
        """"""
    @overload
    def Export(self, contentType: X509ContentType, password: SecureString) -> Array[int]:
        """"""
    @overload
    def Export(self, contentType: X509ContentType, password: str) -> Array[int]:
        """"""
    @classmethod
    @overload
    def GetCertContentType(cls, rawData: Array[int]) -> X509ContentType:
        """"""
    @classmethod
    @overload
    def GetCertContentType(cls, fileName: str) -> X509ContentType:
        """"""
    @overload
    def GetCertHash(self) -> Array[int]:
        """"""
    @overload
    def GetCertHash(self, hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """"""
    @overload
    def GetCertHashString(self) -> str:
        """"""
    @overload
    def GetCertHashString(self, hashAlgorithm: HashAlgorithmName) -> str:
        """"""
    def GetEffectiveDateString(self) -> str:
        """"""
    def GetExpirationDateString(self) -> str:
        """"""
    def GetFormat(self) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIssuerName(self) -> str:
        """"""
    def GetKeyAlgorithm(self) -> str:
        """"""
    def GetKeyAlgorithmParameters(self) -> Array[int]:
        """"""
    def GetKeyAlgorithmParametersString(self) -> str:
        """"""
    def GetName(self) -> str:
        """"""
    def GetNameInfo(self, nameType: X509NameType, forIssuer: bool) -> str:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetPublicKey(self) -> Array[int]:
        """"""
    def GetPublicKeyString(self) -> str:
        """"""
    def GetRawCertData(self) -> Array[int]:
        """"""
    def GetRawCertDataString(self) -> str:
        """"""
    def GetSerialNumber(self) -> Array[int]:
        """"""
    def GetSerialNumberString(self) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def Import(self, rawData: Array[int]) -> None:
        """"""
    @overload
    def Import(
        self, rawData: Array[int], password: SecureString, keyStorageFlags: X509KeyStorageFlags
    ) -> None:
        """"""
    @overload
    def Import(
        self, rawData: Array[int], password: str, keyStorageFlags: X509KeyStorageFlags
    ) -> None:
        """"""
    @overload
    def Import(self, fileName: str) -> None:
        """"""
    @overload
    def Import(
        self, fileName: str, password: SecureString, keyStorageFlags: X509KeyStorageFlags
    ) -> None:
        """"""
    @overload
    def Import(self, fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags) -> None:
        """"""
    def OnDeserialization(self, sender: object) -> None:
        """"""
    def Reset(self) -> None:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, verbose: bool) -> str:
        """"""
    def Verify(self) -> bool:
        """"""

class X509Certificate2Collection(X509CertificateCollection, ICollection, IEnumerable, IList):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, certificate: X509Certificate2) -> None:
        """"""
    @overload
    def __init__(self, certificates: X509Certificate2Collection) -> None:
        """"""
    @overload
    def __init__(self, certificates: Array[X509Certificate2]) -> None:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
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
    def Item(self) -> X509Certificate:
        """"""
    @Item.setter
    def Item(self, value: X509Certificate) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, value: X509Certificate) -> int:
        """"""
    @overload
    def Add(self, certificate: X509Certificate2) -> int:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    @overload
    def AddRange(self, certificates: X509Certificate2Collection) -> None:
        """"""
    @overload
    def AddRange(self, value: X509CertificateCollection) -> None:
        """"""
    @overload
    def AddRange(self, certificates: Array[X509Certificate2]) -> None:
        """"""
    @overload
    def AddRange(self, value: Array[X509Certificate]) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: X509Certificate) -> bool:
        """"""
    @overload
    def Contains(self, certificate: X509Certificate2) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[X509Certificate], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Export(self, contentType: X509ContentType) -> Array[int]:
        """"""
    @overload
    def Export(self, contentType: X509ContentType, password: str) -> Array[int]:
        """"""
    def Find(
        self, findType: X509FindType, findValue: object, validOnly: bool
    ) -> X509Certificate2Collection:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def Import(self, rawData: Array[int]) -> None:
        """"""
    @overload
    def Import(
        self, rawData: Array[int], password: str, keyStorageFlags: X509KeyStorageFlags
    ) -> None:
        """"""
    @overload
    def Import(self, fileName: str) -> None:
        """"""
    @overload
    def Import(self, fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags) -> None:
        """"""
    @overload
    def IndexOf(self, value: X509Certificate) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, value: X509Certificate) -> None:
        """"""
    @overload
    def Insert(self, index: int, certificate: X509Certificate2) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, value: X509Certificate) -> None:
        """"""
    @overload
    def Remove(self, certificate: X509Certificate2) -> None:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    @overload
    def RemoveRange(self, certificates: X509Certificate2Collection) -> None:
        """"""
    @overload
    def RemoveRange(self, certificates: Array[X509Certificate2]) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, value: X509Certificate) -> bool:
        """"""
    @overload
    def __contains__(self, certificate: X509Certificate2) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, value: X509Certificate) -> None:
        """"""
    @overload
    def __delitem__(self, certificate: X509Certificate2) -> None:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> X509Certificate:
        """"""
    @overload
    def __setitem__(self, index: int, value: X509Certificate) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: X509Certificate2) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""
    class X509CertificateEnumerator(Object, IEnumerator):
        """"""
        def __init__(self, mappings: X509CertificateCollection) -> None:
            """"""
        @property
        def Current(self) -> X509Certificate:
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

class X509Certificate2Enumerator(Object, IEnumerator):
    """"""
    @property
    def Current(self) -> X509Certificate2:
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

class X509CertificateCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: X509CertificateCollection) -> None:
        """"""
    @overload
    def __init__(self, value: Array[X509Certificate]) -> None:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
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
    def Item(self) -> X509Certificate:
        """"""
    @Item.setter
    def Item(self, value: X509Certificate) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, value: X509Certificate) -> int:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    @overload
    def AddRange(self, value: X509CertificateCollection) -> None:
        """"""
    @overload
    def AddRange(self, value: Array[X509Certificate]) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: X509Certificate) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[X509Certificate], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, value: X509Certificate) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, value: X509Certificate) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, value: X509Certificate) -> None:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, value: X509Certificate) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, value: X509Certificate) -> None:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> X509Certificate:
        """"""
    @overload
    def __setitem__(self, index: int, value: X509Certificate) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""
    class X509CertificateEnumerator(Object, IEnumerator):
        """"""
        def __init__(self, mappings: X509CertificateCollection) -> None:
            """"""
        @property
        def Current(self) -> X509Certificate:
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

class X509Chain(Object, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, useMachineContext: bool) -> None:
        """"""
    @overload
    def __init__(self, chainContext: IntPtr) -> None:
        """"""
    @property
    def ChainContext(self) -> IntPtr:
        """"""
    @property
    def ChainElements(self) -> X509ChainElementCollection:
        """"""
    @property
    def ChainPolicy(self) -> X509ChainPolicy:
        """"""
    @ChainPolicy.setter
    def ChainPolicy(self, value: X509ChainPolicy) -> None: ...
    @property
    def ChainStatus(self) -> Array[X509ChainStatus]:
        """"""
    @property
    def SafeHandle(self) -> SafeX509ChainHandle:
        """"""
    def Build(self, certificate: X509Certificate2) -> bool:
        """"""
    @classmethod
    def Create(cls) -> X509Chain:
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

class X509ChainElement(Object):
    """"""
    @property
    def Certificate(self) -> X509Certificate2:
        """"""
    @property
    def ChainElementStatus(self) -> Array[X509ChainStatus]:
        """"""
    @property
    def Information(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class X509ChainElementCollection(Object, ICollection, IEnumerable):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> X509ChainElement:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[X509ChainElement], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> X509ChainElementEnumerator:
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
    def __getitem__(self, index: int) -> X509ChainElement:
        """"""

class X509ChainElementEnumerator(Object, IEnumerator):
    """"""
    @property
    def Current(self) -> X509ChainElement:
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

class X509ChainPolicy(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def ApplicationPolicy(self) -> OidCollection:
        """"""
    @property
    def CertificatePolicy(self) -> OidCollection:
        """"""
    @property
    def ExtraStore(self) -> X509Certificate2Collection:
        """"""
    @property
    def RevocationFlag(self) -> X509RevocationFlag:
        """"""
    @RevocationFlag.setter
    def RevocationFlag(self, value: X509RevocationFlag) -> None: ...
    @property
    def RevocationMode(self) -> X509RevocationMode:
        """"""
    @RevocationMode.setter
    def RevocationMode(self, value: X509RevocationMode) -> None: ...
    @property
    def UrlRetrievalTimeout(self) -> TimeSpan:
        """"""
    @UrlRetrievalTimeout.setter
    def UrlRetrievalTimeout(self, value: TimeSpan) -> None: ...
    @property
    def VerificationFlags(self) -> X509VerificationFlags:
        """"""
    @VerificationFlags.setter
    def VerificationFlags(self, value: X509VerificationFlags) -> None: ...
    @property
    def VerificationTime(self) -> DateTime:
        """"""
    @VerificationTime.setter
    def VerificationTime(self, value: DateTime) -> None: ...
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

class X509ChainStatus(ValueType):
    """"""
    @property
    def Status(self) -> X509ChainStatusFlags:
        """"""
    @Status.setter
    def Status(self, value: X509ChainStatusFlags) -> None: ...
    @property
    def StatusInformation(self) -> str:
        """"""
    @StatusInformation.setter
    def StatusInformation(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class X509ChainStatusFlags(Enum):
    """"""

    NoError: X509ChainStatusFlags = ...
    """"""
    NotTimeValid: X509ChainStatusFlags = ...
    """"""
    NotTimeNested: X509ChainStatusFlags = ...
    """"""
    Revoked: X509ChainStatusFlags = ...
    """"""
    NotSignatureValid: X509ChainStatusFlags = ...
    """"""
    NotValidForUsage: X509ChainStatusFlags = ...
    """"""
    UntrustedRoot: X509ChainStatusFlags = ...
    """"""
    RevocationStatusUnknown: X509ChainStatusFlags = ...
    """"""
    Cyclic: X509ChainStatusFlags = ...
    """"""
    InvalidExtension: X509ChainStatusFlags = ...
    """"""
    InvalidPolicyConstraints: X509ChainStatusFlags = ...
    """"""
    InvalidBasicConstraints: X509ChainStatusFlags = ...
    """"""
    InvalidNameConstraints: X509ChainStatusFlags = ...
    """"""
    HasNotSupportedNameConstraint: X509ChainStatusFlags = ...
    """"""
    HasNotDefinedNameConstraint: X509ChainStatusFlags = ...
    """"""
    HasNotPermittedNameConstraint: X509ChainStatusFlags = ...
    """"""
    HasExcludedNameConstraint: X509ChainStatusFlags = ...
    """"""
    PartialChain: X509ChainStatusFlags = ...
    """"""
    CtlNotTimeValid: X509ChainStatusFlags = ...
    """"""
    CtlNotSignatureValid: X509ChainStatusFlags = ...
    """"""
    CtlNotValidForUsage: X509ChainStatusFlags = ...
    """"""
    HasWeakSignature: X509ChainStatusFlags = ...
    """"""
    OfflineRevocation: X509ChainStatusFlags = ...
    """"""
    NoIssuanceChainPolicy: X509ChainStatusFlags = ...
    """"""
    ExplicitDistrust: X509ChainStatusFlags = ...
    """"""
    HasNotSupportedCriticalExtension: X509ChainStatusFlags = ...
    """"""

class X509Constants(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class X509ContentType(Enum):
    """"""

    Unknown: X509ContentType = ...
    """"""
    Cert: X509ContentType = ...
    """"""
    SerializedCert: X509ContentType = ...
    """"""
    Pfx: X509ContentType = ...
    """"""
    Pkcs12: X509ContentType = ...
    """"""
    SerializedStore: X509ContentType = ...
    """"""
    Pkcs7: X509ContentType = ...
    """"""
    Authenticode: X509ContentType = ...
    """"""

class X509EnhancedKeyUsageExtension(X509Extension):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, enhancedKeyUsages: OidCollection, critical: bool) -> None:
        """"""
    @overload
    def __init__(self, encodedEnhancedKeyUsages: AsnEncodedData, critical: bool) -> None:
        """"""
    @property
    def Critical(self) -> bool:
        """"""
    @Critical.setter
    def Critical(self, value: bool) -> None: ...
    @property
    def EnhancedKeyUsages(self) -> OidCollection:
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

class X509Extension(AsnEncodedData):
    """"""
    @overload
    def __init__(self, oid: str, rawData: Array[int], critical: bool) -> None:
        """"""
    @overload
    def __init__(self, encodedExtension: AsnEncodedData, critical: bool) -> None:
        """"""
    @overload
    def __init__(self, oid: Oid, rawData: Array[int], critical: bool) -> None:
        """"""
    @property
    def Critical(self) -> bool:
        """"""
    @Critical.setter
    def Critical(self, value: bool) -> None: ...
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

class X509ExtensionCollection(Object, ICollection, IEnumerable):
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
    def Item(self) -> X509Extension:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    def Add(self, extension: X509Extension) -> int:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[X509Extension], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> X509ExtensionEnumerator:
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
    def __getitem__(self, index: int) -> X509Extension:
        """"""
    @overload
    def __getitem__(self, oid: str) -> X509Extension:
        """"""

class X509ExtensionEnumerator(Object, IEnumerator):
    """"""
    @property
    def Current(self) -> X509Extension:
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

class X509FindType(Enum):
    """"""

    FindByThumbprint: X509FindType = ...
    """"""
    FindBySubjectName: X509FindType = ...
    """"""
    FindBySubjectDistinguishedName: X509FindType = ...
    """"""
    FindByIssuerName: X509FindType = ...
    """"""
    FindByIssuerDistinguishedName: X509FindType = ...
    """"""
    FindBySerialNumber: X509FindType = ...
    """"""
    FindByTimeValid: X509FindType = ...
    """"""
    FindByTimeNotYetValid: X509FindType = ...
    """"""
    FindByTimeExpired: X509FindType = ...
    """"""
    FindByTemplateName: X509FindType = ...
    """"""
    FindByApplicationPolicy: X509FindType = ...
    """"""
    FindByCertificatePolicy: X509FindType = ...
    """"""
    FindByExtension: X509FindType = ...
    """"""
    FindByKeyUsage: X509FindType = ...
    """"""
    FindBySubjectKeyIdentifier: X509FindType = ...
    """"""

class X509IncludeOption(Enum):
    """"""

    _None: X509IncludeOption = ...
    """"""
    ExcludeRoot: X509IncludeOption = ...
    """"""
    EndCertOnly: X509IncludeOption = ...
    """"""
    WholeChain: X509IncludeOption = ...
    """"""

class X509KeyStorageFlags(Enum):
    """"""

    DefaultKeySet: X509KeyStorageFlags = ...
    """"""
    UserKeySet: X509KeyStorageFlags = ...
    """"""
    MachineKeySet: X509KeyStorageFlags = ...
    """"""
    Exportable: X509KeyStorageFlags = ...
    """"""
    UserProtected: X509KeyStorageFlags = ...
    """"""
    PersistKeySet: X509KeyStorageFlags = ...
    """"""
    EphemeralKeySet: X509KeyStorageFlags = ...
    """"""

class X509KeyUsageExtension(X509Extension):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, keyUsages: X509KeyUsageFlags, critical: bool) -> None:
        """"""
    @overload
    def __init__(self, encodedKeyUsage: AsnEncodedData, critical: bool) -> None:
        """"""
    @property
    def Critical(self) -> bool:
        """"""
    @Critical.setter
    def Critical(self, value: bool) -> None: ...
    @property
    def KeyUsages(self) -> X509KeyUsageFlags:
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

class X509KeyUsageFlags(Enum):
    """"""

    _None: X509KeyUsageFlags = ...
    """"""
    EncipherOnly: X509KeyUsageFlags = ...
    """"""
    CrlSign: X509KeyUsageFlags = ...
    """"""
    KeyCertSign: X509KeyUsageFlags = ...
    """"""
    KeyAgreement: X509KeyUsageFlags = ...
    """"""
    DataEncipherment: X509KeyUsageFlags = ...
    """"""
    KeyEncipherment: X509KeyUsageFlags = ...
    """"""
    NonRepudiation: X509KeyUsageFlags = ...
    """"""
    DigitalSignature: X509KeyUsageFlags = ...
    """"""
    DecipherOnly: X509KeyUsageFlags = ...
    """"""

class X509NameType(Enum):
    """"""

    SimpleName: X509NameType = ...
    """"""
    EmailName: X509NameType = ...
    """"""
    UpnName: X509NameType = ...
    """"""
    DnsName: X509NameType = ...
    """"""
    DnsFromAlternativeName: X509NameType = ...
    """"""
    UrlName: X509NameType = ...
    """"""

class X509Native(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    class AXL_AUTHENTICODE_SIGNER_INFO(ValueType):
        """"""

        algHash: Final[CapiNative.AlgorithmId]
        """"""
        cbSize: Final[int]
        """"""
        dwError: Final[int]
        """"""
        pChainContext: Final[IntPtr]
        """"""
        pwszDescription: Final[IntPtr]
        """"""
        pwszDescriptionUrl: Final[IntPtr]
        """"""
        pwszHash: Final[IntPtr]
        """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""

    class AXL_AUTHENTICODE_TIMESTAMPER_INFO(ValueType):
        """"""

        algHash: Final[CapiNative.AlgorithmId]
        """"""
        cbsize: Final[int]
        """"""
        dwError: Final[int]
        """"""
        ftTimestamp: Final[FILETIME]
        """"""
        pChainContext: Final[IntPtr]
        """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""

    class AxlVerificationFlags(Enum):
        """"""

        _None: X509Native.AxlVerificationFlags = ...
        """"""
        NoRevocationCheck: X509Native.AxlVerificationFlags = ...
        """"""
        RevocationCheckEndCertOnly: X509Native.AxlVerificationFlags = ...
        """"""
        RevocationCheckEntireChain: X509Native.AxlVerificationFlags = ...
        """"""
        UrlOnlyCacheRetrieval: X509Native.AxlVerificationFlags = ...
        """"""
        LifetimeSigning: X509Native.AxlVerificationFlags = ...
        """"""
        TrustMicrosoftRootOnly: X509Native.AxlVerificationFlags = ...
        """"""

    class UnsafeNativeMethods(ABC, Object):
        """"""
        @classmethod
        def CertFreeAuthenticodeSignerInfo(cls, pSignerInfo: AXL_AUTHENTICODE_SIGNER_INFO) -> int:
            """"""
        @classmethod
        def CertFreeAuthenticodeTimestamperInfo(
            cls, pTimestamperInfo: AXL_AUTHENTICODE_TIMESTAMPER_INFO
        ) -> int:
            """"""
        @classmethod
        def CertVerifyAuthenticodeLicense(
            cls,
            pLicenseBlob: CRYPTOAPI_BLOB,
            dwFlags: X509Native.AxlVerificationFlags,
            pSignerInfo: AXL_AUTHENTICODE_SIGNER_INFO,
            pTimestamperInfo: AXL_AUTHENTICODE_TIMESTAMPER_INFO,
        ) -> tuple[int, AXL_AUTHENTICODE_SIGNER_INFO, AXL_AUTHENTICODE_TIMESTAMPER_INFO]:
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
        def _AxlGetIssuerPublicKeyHash(
            cls, pCertContext: IntPtr, ppwszPublicKeyHash: SafeAxlBufferHandle
        ) -> tuple[int, SafeAxlBufferHandle]:
            """"""

class X509RevocationFlag(Enum):
    """"""

    EndCertificateOnly: X509RevocationFlag = ...
    """"""
    EntireChain: X509RevocationFlag = ...
    """"""
    ExcludeRoot: X509RevocationFlag = ...
    """"""

class X509RevocationMode(Enum):
    """"""

    NoCheck: X509RevocationMode = ...
    """"""
    Online: X509RevocationMode = ...
    """"""
    Offline: X509RevocationMode = ...
    """"""

class X509SignatureGenerator(ABC, Object):
    """"""
    @property
    def PublicKey(self) -> PublicKey:
        """"""
    @classmethod
    def CreateForECDsa(cls, key: ECDsa) -> X509SignatureGenerator:
        """"""
    @classmethod
    def CreateForRSA(
        cls, key: RSA, signaturePadding: RSASignaturePadding
    ) -> X509SignatureGenerator:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetSignatureAlgorithmIdentifier(self, hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """"""
    def GetType(self) -> Type:
        """"""
    def SignData(self, data: Array[int], hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """"""
    def ToString(self) -> str:
        """"""

class X509Store(Object, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, storeName: str) -> None:
        """"""
    @overload
    def __init__(self, storeName: StoreName) -> None:
        """"""
    @overload
    def __init__(self, storeLocation: StoreLocation) -> None:
        """"""
    @overload
    def __init__(self, storeName: StoreName, storeLocation: StoreLocation) -> None:
        """"""
    @overload
    def __init__(self, storeName: str, storeLocation: StoreLocation) -> None:
        """"""
    @overload
    def __init__(self, storeHandle: IntPtr) -> None:
        """"""
    @property
    def Certificates(self) -> X509Certificate2Collection:
        """"""
    @property
    def Location(self) -> StoreLocation:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def StoreHandle(self) -> IntPtr:
        """"""
    def Add(self, certificate: X509Certificate2) -> None:
        """"""
    def AddRange(self, certificates: X509Certificate2Collection) -> None:
        """"""
    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Open(self, flags: OpenFlags) -> None:
        """"""
    def Remove(self, certificate: X509Certificate2) -> None:
        """"""
    def RemoveRange(self, certificates: X509Certificate2Collection) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def __delitem__(self, certificate: X509Certificate2) -> None:
        """"""

class X509SubjectKeyIdentifierExtension(X509Extension):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, subjectKeyIdentifier: str, critical: bool) -> None:
        """"""
    @overload
    def __init__(self, subjectKeyIdentifier: Array[int], critical: bool) -> None:
        """"""
    @overload
    def __init__(self, encodedSubjectKeyIdentifier: AsnEncodedData, critical: bool) -> None:
        """"""
    @overload
    def __init__(self, key: PublicKey, critical: bool) -> None:
        """"""
    @overload
    def __init__(
        self, key: PublicKey, algorithm: X509SubjectKeyIdentifierHashAlgorithm, critical: bool
    ) -> None:
        """"""
    @property
    def Critical(self) -> bool:
        """"""
    @Critical.setter
    def Critical(self, value: bool) -> None: ...
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
    @property
    def SubjectKeyIdentifier(self) -> str:
        """"""
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

class X509SubjectKeyIdentifierHashAlgorithm(Enum):
    """"""

    Sha1: X509SubjectKeyIdentifierHashAlgorithm = ...
    """"""
    ShortSha1: X509SubjectKeyIdentifierHashAlgorithm = ...
    """"""
    CapiSha1: X509SubjectKeyIdentifierHashAlgorithm = ...
    """"""

class X509Utils(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class X509VerificationFlags(Enum):
    """"""

    NoFlag: X509VerificationFlags = ...
    """"""
    IgnoreNotTimeValid: X509VerificationFlags = ...
    """"""
    IgnoreCtlNotTimeValid: X509VerificationFlags = ...
    """"""
    IgnoreNotTimeNested: X509VerificationFlags = ...
    """"""
    IgnoreInvalidBasicConstraints: X509VerificationFlags = ...
    """"""
    AllowUnknownCertificateAuthority: X509VerificationFlags = ...
    """"""
    IgnoreWrongUsage: X509VerificationFlags = ...
    """"""
    IgnoreInvalidName: X509VerificationFlags = ...
    """"""
    IgnoreInvalidPolicy: X509VerificationFlags = ...
    """"""
    IgnoreEndRevocationUnknown: X509VerificationFlags = ...
    """"""
    IgnoreCtlSignerRevocationUnknown: X509VerificationFlags = ...
    """"""
    IgnoreCertificateAuthorityRevocationUnknown: X509VerificationFlags = ...
    """"""
    IgnoreRootRevocationUnknown: X509VerificationFlags = ...
    """"""
    AllFlags: X509VerificationFlags = ...
    """"""
