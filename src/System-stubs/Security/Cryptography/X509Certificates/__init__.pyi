from __future__ import annotations

from abc import ABC
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import Iterator
from typing import Optional
from typing import Tuple
from typing import TypeVar
from typing import overload

from Microsoft.Win32.SafeHandles import SafeAxlBufferHandle
from Microsoft.Win32.SafeHandles import SafeHandleZeroOrMinusOneIsInvalid
from Microsoft.Win32.SafeHandles import SafeX509ChainHandle
from System import Array
from System import ArraySegment
from System import Byte
from System import Char
from System import DateTime
from System import DateTimeOffset
from System import Enum
from System import IDisposable
from System import IEquatable
from System import IntPtr
from System import Object
from System import TimeSpan
from System import Type
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
from System.Security.Cryptography.CapiNative import AlgorithmId
from System.Security.Cryptography.X509Certificates.X509Native import AxlVerificationFlags
from System.Text import Encoding

T = TypeVar("T")
T1 = TypeVar("T1")
T2 = TypeVar("T2")
T3 = TypeVar("T3")

class AlgorithmIdentifierAsn(ValueType):
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

class Asn1Tag(ValueType, IEquatable[Asn1Tag]):
    """"""

    ConstructedBitString: Final[ClassVar[Asn1Tag]] = ...
    """
    
    :return: 
    """
    ConstructedOctetString: Final[ClassVar[Asn1Tag]] = ...
    """
    
    :return: 
    """
    Integer: Final[ClassVar[Asn1Tag]] = ...
    """
    
    :return: 
    """
    Null: Final[ClassVar[Asn1Tag]] = ...
    """
    
    :return: 
    """
    ObjectIdentifier: Final[ClassVar[Asn1Tag]] = ...
    """
    
    :return: 
    """
    PrimitiveBitString: Final[ClassVar[Asn1Tag]] = ...
    """
    
    :return: 
    """
    PrimitiveOctetString: Final[ClassVar[Asn1Tag]] = ...
    """
    
    :return: 
    """
    Sequence: Final[ClassVar[Asn1Tag]] = ...
    """
    
    :return: 
    """
    SetOf: Final[ClassVar[Asn1Tag]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, tagClass: TagClass, tagValue: int):
        """

        :param tagClass:
        :param tagValue:
        """
    @overload
    def __init__(self, universalTagNumber: UniversalTagNumber, isConstructed: bool):
        """

        :param universalTagNumber:
        :param isConstructed:
        """
    @overload
    def __init__(self, tagClass: TagClass, tagValue: int, isConstructed: bool):
        """

        :param tagClass:
        :param tagValue:
        :param isConstructed:
        """
    @property
    def IsConstructed(self) -> bool:
        """

        :return:
        """
    @property
    def TagClass(self) -> TagClass:
        """

        :return:
        """
    @property
    def TagValue(self) -> int:
        """

        :return:
        """
    def AsConstructed(self) -> Asn1Tag:
        """

        :return:
        """
    @classmethod
    def Decode(cls, source: ReadOnlySpan[int], bytesConsumed: int) -> Tuple[Asn1Tag, int]:
        """

        :param source:
        :param bytesConsumed:
        :return:
        """
    @overload
    def Equals(self, other: Asn1Tag) -> bool:
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
    def HasSameClassAndValue(self, other: Asn1Tag) -> bool:
        """

        :param other:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    def TryDecode(
        cls, source: ReadOnlySpan[int], tag: Asn1Tag, bytesConsumed: int
    ) -> Tuple[bool, Asn1Tag, int]:
        """

        :param source:
        :param tag:
        :param bytesConsumed:
        :return:
        """
    def __eq__(self, other: Asn1Tag) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: Asn1Tag) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: Asn1Tag, right: Asn1Tag) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: Asn1Tag, right: Asn1Tag) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

class AsnDecoder(ABC, Object):
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
    @classmethod
    def ReadBitString(
        cls,
        source: ReadOnlySpan[int],
        ruleSet: AsnEncodingRules,
        unusedBitCount: int,
        bytesConsumed: int,
        expectedTag: Optional[Asn1Tag],
    ) -> Tuple[Array[int], int, int]:
        """

        :param source:
        :param ruleSet:
        :param unusedBitCount:
        :param bytesConsumed:
        :param expectedTag:
        :return:
        """
    @classmethod
    def ReadEncodedValue(
        cls,
        source: ReadOnlySpan[int],
        ruleSet: AsnEncodingRules,
        contentOffset: int,
        contentLength: int,
        bytesConsumed: int,
    ) -> Tuple[Asn1Tag, int, int, int]:
        """

        :param source:
        :param ruleSet:
        :param contentOffset:
        :param contentLength:
        :param bytesConsumed:
        :return:
        """
    @classmethod
    def ReadIntegerBytes(
        cls,
        source: ReadOnlySpan[int],
        ruleSet: AsnEncodingRules,
        bytesConsumed: int,
        expectedTag: Optional[Asn1Tag],
    ) -> Tuple[ReadOnlySpan[int], int]:
        """

        :param source:
        :param ruleSet:
        :param bytesConsumed:
        :param expectedTag:
        :return:
        """
    @classmethod
    def ReadNull(
        cls,
        source: ReadOnlySpan[int],
        ruleSet: AsnEncodingRules,
        bytesConsumed: int,
        expectedTag: Optional[Asn1Tag],
    ) -> Tuple[None, int]:
        """

        :param source:
        :param ruleSet:
        :param bytesConsumed:
        :param expectedTag:
        """
    @classmethod
    def ReadObjectIdentifier(
        cls,
        source: ReadOnlySpan[int],
        ruleSet: AsnEncodingRules,
        bytesConsumed: int,
        expectedTag: Optional[Asn1Tag],
    ) -> Tuple[Array[int], int]:
        """

        :param source:
        :param ruleSet:
        :param bytesConsumed:
        :param expectedTag:
        :return:
        """
    @classmethod
    def ReadOctetString(
        cls,
        source: ReadOnlySpan[int],
        ruleSet: AsnEncodingRules,
        bytesConsumed: int,
        expectedTag: Optional[Asn1Tag],
    ) -> Tuple[Array[int], int]:
        """

        :param source:
        :param ruleSet:
        :param bytesConsumed:
        :param expectedTag:
        :return:
        """
    @classmethod
    def ReadSequence(
        cls,
        source: ReadOnlySpan[int],
        ruleSet: AsnEncodingRules,
        contentOffset: int,
        contentLength: int,
        bytesConsumed: int,
        expectedTag: Optional[Asn1Tag],
    ) -> Tuple[None, int, int, int]:
        """

        :param source:
        :param ruleSet:
        :param contentOffset:
        :param contentLength:
        :param bytesConsumed:
        :param expectedTag:
        """
    @classmethod
    def ReadSetOf(
        cls,
        source: ReadOnlySpan[int],
        ruleSet: AsnEncodingRules,
        contentOffset: int,
        contentLength: int,
        bytesConsumed: int,
        skipSortOrderValidation: bool,
        expectedTag: Optional[Asn1Tag],
    ) -> Tuple[None, int, int, int]:
        """

        :param source:
        :param ruleSet:
        :param contentOffset:
        :param contentLength:
        :param bytesConsumed:
        :param skipSortOrderValidation:
        :param expectedTag:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    def TryReadBitString(
        cls,
        source: ReadOnlySpan[int],
        destination: Span[int],
        ruleSet: AsnEncodingRules,
        unusedBitCount: int,
        bytesConsumed: int,
        bytesWritten: int,
        expectedTag: Optional[Asn1Tag],
    ) -> Tuple[bool, int, int, int]:
        """

        :param source:
        :param destination:
        :param ruleSet:
        :param unusedBitCount:
        :param bytesConsumed:
        :param bytesWritten:
        :param expectedTag:
        :return:
        """
    @classmethod
    def TryReadEncodedValue(
        cls,
        source: ReadOnlySpan[int],
        ruleSet: AsnEncodingRules,
        tag: Asn1Tag,
        contentOffset: int,
        contentLength: int,
        bytesConsumed: int,
    ) -> Tuple[bool, Asn1Tag, int, int, int]:
        """

        :param source:
        :param ruleSet:
        :param tag:
        :param contentOffset:
        :param contentLength:
        :param bytesConsumed:
        :return:
        """
    @classmethod
    def TryReadInt32(
        cls,
        source: ReadOnlySpan[int],
        ruleSet: AsnEncodingRules,
        value: int,
        bytesConsumed: int,
        expectedTag: Optional[Asn1Tag],
    ) -> Tuple[bool, int, int]:
        """

        :param source:
        :param ruleSet:
        :param value:
        :param bytesConsumed:
        :param expectedTag:
        :return:
        """
    @classmethod
    def TryReadInt64(
        cls,
        source: ReadOnlySpan[int],
        ruleSet: AsnEncodingRules,
        value: int,
        bytesConsumed: int,
        expectedTag: Optional[Asn1Tag],
    ) -> Tuple[bool, int, int]:
        """

        :param source:
        :param ruleSet:
        :param value:
        :param bytesConsumed:
        :param expectedTag:
        :return:
        """
    @classmethod
    def TryReadOctetString(
        cls,
        source: ReadOnlySpan[int],
        destination: Span[int],
        ruleSet: AsnEncodingRules,
        bytesConsumed: int,
        bytesWritten: int,
        expectedTag: Optional[Asn1Tag],
    ) -> Tuple[bool, int, int]:
        """

        :param source:
        :param destination:
        :param ruleSet:
        :param bytesConsumed:
        :param bytesWritten:
        :param expectedTag:
        :return:
        """
    @classmethod
    def TryReadPrimitiveBitString(
        cls,
        source: ReadOnlySpan[int],
        ruleSet: AsnEncodingRules,
        unusedBitCount: int,
        value: ReadOnlySpan[int],
        bytesConsumed: int,
        expectedTag: Optional[Asn1Tag],
    ) -> Tuple[bool, int, ReadOnlySpan[int], int]:
        """

        :param source:
        :param ruleSet:
        :param unusedBitCount:
        :param value:
        :param bytesConsumed:
        :param expectedTag:
        :return:
        """
    @classmethod
    def TryReadPrimitiveOctetString(
        cls,
        source: ReadOnlySpan[int],
        ruleSet: AsnEncodingRules,
        value: ReadOnlySpan[int],
        bytesConsumed: int,
        expectedTag: Optional[Asn1Tag],
    ) -> Tuple[bool, ReadOnlySpan[int], int]:
        """

        :param source:
        :param ruleSet:
        :param value:
        :param bytesConsumed:
        :param expectedTag:
        :return:
        """
    @classmethod
    def TryReadUInt32(
        cls,
        source: ReadOnlySpan[int],
        ruleSet: AsnEncodingRules,
        value: int,
        bytesConsumed: int,
        expectedTag: Optional[Asn1Tag],
    ) -> Tuple[bool, int, int]:
        """

        :param source:
        :param ruleSet:
        :param value:
        :param bytesConsumed:
        :param expectedTag:
        :return:
        """
    @classmethod
    def TryReadUInt64(
        cls,
        source: ReadOnlySpan[int],
        ruleSet: AsnEncodingRules,
        value: int,
        bytesConsumed: int,
        expectedTag: Optional[Asn1Tag],
    ) -> Tuple[bool, int, int]:
        """

        :param source:
        :param ruleSet:
        :param value:
        :param bytesConsumed:
        :param expectedTag:
        :return:
        """

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
    def __init__(self, data: ReadOnlyMemory[int], ruleSet: AsnEncodingRules):
        """

        :param data:
        :param ruleSet:
        """
    @overload
    def __init__(
        self, data: ReadOnlyMemory[int], ruleSet: AsnEncodingRules, options: AsnReaderOptions
    ):
        """

        :param data:
        :param ruleSet:
        :param options:
        """
    @property
    def HasData(self) -> bool:
        """

        :return:
        """
    @property
    def RuleSet(self) -> AsnEncodingRules:
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
    def PeekContentBytes(self) -> ReadOnlyMemory[int]:
        """

        :return:
        """
    def PeekEncodedValue(self) -> ReadOnlyMemory[int]:
        """

        :return:
        """
    def PeekTag(self) -> Asn1Tag:
        """

        :return:
        """
    def ReadBitString(
        self, unusedBitCount: int, expectedTag: Optional[Asn1Tag]
    ) -> Tuple[Array[int], int]:
        """

        :param unusedBitCount:
        :param expectedTag:
        :return:
        """
    def ReadEncodedValue(self) -> ReadOnlyMemory[int]:
        """

        :return:
        """
    def ReadIntegerBytes(self, expectedTag: Optional[Asn1Tag]) -> ReadOnlyMemory[int]:
        """

        :param expectedTag:
        :return:
        """
    def ReadNull(self, expectedTag: Optional[Asn1Tag]) -> None:
        """

        :param expectedTag:
        """
    def ReadObjectIdentifier(self, expectedTag: Optional[Asn1Tag]) -> Array[int]:
        """

        :param expectedTag:
        :return:
        """
    def ReadOctetString(self, expectedTag: Optional[Asn1Tag]) -> Array[int]:
        """

        :param expectedTag:
        :return:
        """
    def ReadSequence(self, expectedTag: Optional[Asn1Tag]) -> AsnReader:
        """

        :param expectedTag:
        :return:
        """
    @overload
    def ReadSetOf(self, expectedTag: Optional[Asn1Tag]) -> AsnReader:
        """

        :param expectedTag:
        :return:
        """
    @overload
    def ReadSetOf(self, skipSortOrderValidation: bool, expectedTag: Optional[Asn1Tag]) -> AsnReader:
        """

        :param skipSortOrderValidation:
        :param expectedTag:
        :return:
        """
    def ThrowIfNotEmpty(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TryReadBitString(
        self,
        destination: Span[int],
        unusedBitCount: int,
        bytesWritten: int,
        expectedTag: Optional[Asn1Tag],
    ) -> Tuple[bool, int, int]:
        """

        :param destination:
        :param unusedBitCount:
        :param bytesWritten:
        :param expectedTag:
        :return:
        """
    def TryReadInt32(self, value: int, expectedTag: Optional[Asn1Tag]) -> Tuple[bool, int]:
        """

        :param value:
        :param expectedTag:
        :return:
        """
    def TryReadInt64(self, value: int, expectedTag: Optional[Asn1Tag]) -> Tuple[bool, int]:
        """

        :param value:
        :param expectedTag:
        :return:
        """
    def TryReadOctetString(
        self, destination: Span[int], bytesWritten: int, expectedTag: Optional[Asn1Tag]
    ) -> Tuple[bool, int]:
        """

        :param destination:
        :param bytesWritten:
        :param expectedTag:
        :return:
        """
    def TryReadPrimitiveBitString(
        self, unusedBitCount: int, value: ReadOnlyMemory[int], expectedTag: Optional[Asn1Tag]
    ) -> Tuple[bool, int, ReadOnlyMemory[int]]:
        """

        :param unusedBitCount:
        :param value:
        :param expectedTag:
        :return:
        """
    def TryReadPrimitiveOctetString(
        self, contents: ReadOnlyMemory[int], expectedTag: Optional[Asn1Tag]
    ) -> Tuple[bool, ReadOnlyMemory[int]]:
        """

        :param contents:
        :param expectedTag:
        :return:
        """
    def TryReadUInt32(self, value: int, expectedTag: Optional[Asn1Tag]) -> Tuple[bool, int]:
        """

        :param value:
        :param expectedTag:
        :return:
        """
    def TryReadUInt64(self, value: int, expectedTag: Optional[Asn1Tag]) -> Tuple[bool, int]:
        """

        :param value:
        :param expectedTag:
        :return:
        """

class AsnReaderOptions(ValueType):
    """"""

    @property
    def SkipSetSortOrderVerification(self) -> bool:
        """

        :return:
        """
    @SkipSetSortOrderVerification.setter
    def SkipSetSortOrderVerification(self, value: bool) -> None: ...
    @property
    def UtcTimeTwoDigitYearMax(self) -> int:
        """

        :return:
        """
    @UtcTimeTwoDigitYearMax.setter
    def UtcTimeTwoDigitYearMax(self, value: int) -> None: ...
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

class AsnValueReader(ValueType):
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

class AttributeAsn(ValueType):
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

class AuthenticodeSignatureInformation(Object):
    """"""

    @property
    def Description(self) -> str:
        """

        :return:
        """
    @property
    def DescriptionUrl(self) -> Uri:
        """

        :return:
        """
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
    def SignatureChain(self) -> X509Chain:
        """

        :return:
        """
    @property
    def SigningCertificate(self) -> X509Certificate2:
        """

        :return:
        """
    @property
    def Timestamp(self) -> TimestampInformation:
        """

        :return:
        """
    @property
    def TrustStatus(self) -> TrustStatus:
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

class BinaryPrimitives(ABC, Object):
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
    @classmethod
    def ReadInt16BigEndian(cls, bytes: ReadOnlySpan[int]) -> int:
        """

        :param bytes:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    def TryReadUInt16BigEndian(cls, bytes: ReadOnlySpan[int], value: int) -> Tuple[bool, int]:
        """

        :param bytes:
        :param value:
        :return:
        """

class CRYPT_OID_INFO(ValueType):
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

class CertificateExtensionsCommon(ABC, Object):
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

class CertificateRequest(Object):
    """"""

    @overload
    def __init__(
        self,
        subjectName: X500DistinguishedName,
        publicKey: PublicKey,
        hashAlgorithm: HashAlgorithmName,
    ):
        """

        :param subjectName:
        :param publicKey:
        :param hashAlgorithm:
        """
    @overload
    def __init__(
        self, subjectName: X500DistinguishedName, key: ECDsa, hashAlgorithm: HashAlgorithmName
    ):
        """

        :param subjectName:
        :param key:
        :param hashAlgorithm:
        """
    @overload
    def __init__(self, subjectName: str, key: ECDsa, hashAlgorithm: HashAlgorithmName):
        """

        :param subjectName:
        :param key:
        :param hashAlgorithm:
        """
    @overload
    def __init__(
        self,
        subjectName: X500DistinguishedName,
        key: RSA,
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ):
        """

        :param subjectName:
        :param key:
        :param hashAlgorithm:
        :param padding:
        """
    @overload
    def __init__(
        self,
        subjectName: str,
        key: RSA,
        hashAlgorithm: HashAlgorithmName,
        padding: RSASignaturePadding,
    ):
        """

        :param subjectName:
        :param key:
        :param hashAlgorithm:
        :param padding:
        """
    @property
    def CertificateExtensions(self) -> Collection[X509Extension]:
        """

        :return:
        """
    @property
    def HashAlgorithm(self) -> HashAlgorithmName:
        """

        :return:
        """
    @property
    def PublicKey(self) -> PublicKey:
        """

        :return:
        """
    @property
    def SubjectName(self) -> X500DistinguishedName:
        """

        :return:
        """
    @overload
    def Create(
        self,
        issuerCertificate: X509Certificate2,
        notBefore: DateTimeOffset,
        notAfter: DateTimeOffset,
        serialNumber: Array[int],
    ) -> X509Certificate2:
        """

        :param issuerCertificate:
        :param notBefore:
        :param notAfter:
        :param serialNumber:
        :return:
        """
    @overload
    def Create(
        self,
        issuerName: X500DistinguishedName,
        generator: X509SignatureGenerator,
        notBefore: DateTimeOffset,
        notAfter: DateTimeOffset,
        serialNumber: Array[int],
    ) -> X509Certificate2:
        """

        :param issuerName:
        :param generator:
        :param notBefore:
        :param notAfter:
        :param serialNumber:
        :return:
        """
    def CreateSelfSigned(
        self, notBefore: DateTimeOffset, notAfter: DateTimeOffset
    ) -> X509Certificate2:
        """

        :param notBefore:
        :param notAfter:
        :return:
        """
    @overload
    def CreateSigningRequest(self) -> Array[int]:
        """

        :return:
        """
    @overload
    def CreateSigningRequest(self, signatureGenerator: X509SignatureGenerator) -> Array[int]:
        """

        :param signatureGenerator:
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

class ContentInfoAsn(ValueType):
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

class CryptoPool(ABC, Object):
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
    @classmethod
    def Rent(cls, size: int) -> Array[int]:
        """

        :param size:
        :return:
        """
    @classmethod
    @overload
    def Return(cls, segment: ArraySegment[int]) -> None:
        """

        :param segment:
        """
    @classmethod
    @overload
    def Return(cls, array: Array[int]) -> None:
        """

        :param array:
        """
    @classmethod
    @overload
    def Return(cls, segment: ArraySegment[int], clearSize: int) -> None:
        """

        :param segment:
        :param clearSize:
        """
    @classmethod
    @overload
    def Return(cls, array: Array[int], clearSize: int) -> None:
        """

        :param array:
        :param clearSize:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CryptographicOperations(ABC, Object):
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
    @classmethod
    def ZeroMemory(cls, buffer: Span[int]) -> None:
        """

        :param buffer:
        """

class DSACertificateExtensions(ABC, Object):
    """"""

    @classmethod
    def CopyWithPrivateKey(cls, certificate: X509Certificate2, privateKey: DSA) -> X509Certificate2:
        """

        :param certificate:
        :param privateKey:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def GetDSAPrivateKey(cls, certificate: X509Certificate2) -> DSA:
        """

        :param certificate:
        :return:
        """
    @classmethod
    def GetDSAPublicKey(cls, certificate: X509Certificate2) -> DSA:
        """

        :param certificate:
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

class DerEncoder(ABC, Object):
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

class DerSequenceReader(Object):
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

class DigestInfoAsn(ValueType):
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

class ECDsaCertificateExtensions(ABC, Object):
    """"""

    @classmethod
    def CopyWithPrivateKey(
        cls, certificate: X509Certificate2, privateKey: ECDsa
    ) -> X509Certificate2:
        """

        :param certificate:
        :param privateKey:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def GetECDsaPrivateKey(cls, certificate: X509Certificate2) -> ECDsa:
        """

        :param certificate:
        :return:
        """
    @classmethod
    def GetECDsaPublicKey(cls, certificate: X509Certificate2) -> ECDsa:
        """

        :param certificate:
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

class ECDsaX509SignatureGenerator(X509SignatureGenerator):
    """"""

    @property
    def PublicKey(self) -> PublicKey:
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
    def GetSignatureAlgorithmIdentifier(self, hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """

        :param hashAlgorithm:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def SignData(self, data: Array[int], hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """

        :param data:
        :param hashAlgorithm:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class EncodingHelpers(ABC, Object):
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

class EncryptedContentInfoAsn(ValueType):
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

class EncryptedDataAsn(ValueType):
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

class EncryptedPrivateKeyInfoAsn(ValueType):
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

class GeneralNameEncoder(Object):
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

class Helpers(ABC, Object):
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

class IncrementalHash(Object, IDisposable):
    """"""

    def AppendData(self, data: ReadOnlySpan[int]) -> None:
        """

        :param data:
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
    def TryGetHashAndReset(self, destination: Span[int], bytesWritten: int) -> Tuple[bool, int]:
        """

        :param destination:
        :param bytesWritten:
        :return:
        """

class IterationCountLimitEnforcer(ABC, Object):
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

class KdfWorkLimiter(ABC, Object):
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

class MacData(ValueType):
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

    AnyCertPolicy: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    ApplicationCertPolicies: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    AuthorityInformationAccess: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    BasicConstraints: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    BasicConstraints2: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    CertPolicies: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    CertPolicyConstraints: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    CertPolicyMappings: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    CertificateAuthorityIssuers: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    CertificateTemplate: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    CommonName: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    CrlDistributionPoints: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    DsaDsa: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    ECDsaSha256: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    ECDsaSha384: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    ECDsaSha512: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Ecc: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    EccCurveSecp256r1: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    EccCurveSecp384r1: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    EccCurveSecp521r1: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    EmailAddress: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    EnhancedKeyUsage: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    EnrollCertTypeExtension: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    InhibitAnyPolicyExtension: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    IssuerAltName: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    KeyUsage: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Mgf1: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Organization: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    OrganizationalUnit: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Pkcs9ExtensionRequest: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    RsaPkcs1Sha256: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    RsaPkcs1Sha384: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    RsaPkcs1Sha512: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    RsaRsa: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    RsaSsaPss: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Sha256: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Sha384: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    Sha512: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    SubjectAltName: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    SubjectKeyIdentifier: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    UserPrincipalName: Final[ClassVar[str]] = ...
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

class PBES2Params(ValueType):
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

class PasswordBasedEncryption(ABC, Object):
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

class Pbkdf2(ABC, Object):
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

class Pbkdf2Params(ValueType):
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

class Pbkdf2SaltChoice(ValueType):
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

class PfxAsn(ValueType):
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

class PinAndClear(ValueType, IDisposable):
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

class Pkcs10CertificationRequestInfo(Object):
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

class Pkcs12Kdf(ABC, Object):
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

class Pkcs9ExtensionRequest(X501Attribute):
    """"""

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

class PublicKey(Object):
    """"""

    def __init__(self, oid: Oid, parameters: AsnEncodedData, keyValue: AsnEncodedData):
        """

        :param oid:
        :param parameters:
        :param keyValue:
        """
    @property
    def EncodedKeyValue(self) -> AsnEncodedData:
        """

        :return:
        """
    @property
    def EncodedParameters(self) -> AsnEncodedData:
        """

        :return:
        """
    @property
    def Key(self) -> AsymmetricAlgorithm:
        """

        :return:
        """
    @property
    def Oid(self) -> Oid:
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

class RSACertificateExtensions(ABC, Object):
    """"""

    @classmethod
    def CopyWithPrivateKey(cls, certificate: X509Certificate2, privateKey: RSA) -> X509Certificate2:
        """

        :param certificate:
        :param privateKey:
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
    @classmethod
    def GetRSAPrivateKey(cls, certificate: X509Certificate2) -> RSA:
        """

        :param certificate:
        :return:
        """
    @classmethod
    def GetRSAPublicKey(cls, certificate: X509Certificate2) -> RSA:
        """

        :param certificate:
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

class RSAPkcs1X509SignatureGenerator(X509SignatureGenerator):
    """"""

    @property
    def PublicKey(self) -> PublicKey:
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
    def GetSignatureAlgorithmIdentifier(self, hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """

        :param hashAlgorithm:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def SignData(self, data: Array[int], hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """

        :param data:
        :param hashAlgorithm:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class RSAPssX509SignatureGenerator(X509SignatureGenerator):
    """"""

    @property
    def PublicKey(self) -> PublicKey:
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
    def GetSignatureAlgorithmIdentifier(self, hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """

        :param hashAlgorithm:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def SignData(self, data: Array[int], hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """

        :param data:
        :param hashAlgorithm:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class Rc2CbcParameters(ValueType):
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

class ReadOnlyMemory(Generic[T], ValueType):
    """"""

    @overload
    def __init__(self, segment: ArraySegment[T]):
        """

        :param segment:
        """
    @overload
    def __init__(self, array: Array[T]):
        """

        :param array:
        """
    @overload
    def __init__(self, array: Array[T], offset: int, count: int):
        """

        :param array:
        :param offset:
        :param count:
        """
    @property
    def IsEmpty(self) -> bool:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Span(self) -> ReadOnlySpan[T]:
        """

        :return:
        """
    def CopyTo(self, destination: Span[T]) -> None:
        """

        :param destination:
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
    @overload
    def Slice(self, start: int) -> ReadOnlyMemory[T]:
        """

        :param start:
        :return:
        """
    @overload
    def Slice(self, start: int, length: int) -> ReadOnlyMemory[T]:
        """

        :param start:
        :param length:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    @overload
    def op_Implicit(cls, memory: ReadOnlyMemory[T]) -> ArraySegment[T]:
        """

        :param memory:
        :return:
        """
    @classmethod
    @overload
    def op_Implicit(cls, segment: ArraySegment[T]) -> ReadOnlyMemory[T]:
        """

        :param segment:
        :return:
        """
    @classmethod
    @overload
    def op_Implicit(cls, array: Array[T]) -> ReadOnlyMemory[T]:
        """

        :param array:
        :return:
        """

class ReadOnlySpan(Generic[T], ValueType):
    """"""

    Empty: Final[ClassVar[Span[T]]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, segment: ArraySegment[T]):
        """

        :param segment:
        """
    @overload
    def __init__(self, array: Array[T]):
        """

        :param array:
        """
    @overload
    def __init__(self, array: Array[T], offset: int, count: int):
        """

        :param array:
        :param offset:
        :param count:
        """
    @property
    def IsEmpty(self) -> bool:
        """

        :return:
        """
    @property
    def IsNull(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> T:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    def CopyTo(self, destination: Span[T]) -> None:
        """

        :param destination:
        """
    def DangerousGetArraySegment(self) -> ArraySegment[T]:
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
    @overload
    def Overlaps(self, destination: ReadOnlySpan[T]) -> bool:
        """

        :param destination:
        :return:
        """
    @overload
    def Overlaps(self, destination: ReadOnlySpan[T], elementOffset: int) -> Tuple[bool, int]:
        """

        :param destination:
        :param elementOffset:
        :return:
        """
    @overload
    def Slice(self, start: int) -> ReadOnlySpan[T]:
        """

        :param start:
        :return:
        """
    @overload
    def Slice(self, start: int, length: int) -> ReadOnlySpan[T]:
        """

        :param start:
        :param length:
        :return:
        """
    def ToArray(self) -> Array[T]:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __getitem__(self, index: int) -> T:
        """

        :param index:
        :return:
        """
    @classmethod
    def op_Implicit(cls, array: Array[T]) -> ReadOnlySpan[T]:
        """

        :param array:
        :return:
        """

class SR(ABC, Object):
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

class SafeBCryptAlgorithmHandle(SafeHandle, IDisposable):
    """"""

    def __init__(self):
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

class SafeBagAsn(ValueType):
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

class SetOfValueComparer(Object, IComparer[ReadOnlyMemory[Byte]]):
    """"""

    def __init__(self):
        """"""
    def Compare(self, x: ReadOnlyMemory[int], y: ReadOnlyMemory[int]) -> int:
        """

        :param x:
        :param y:
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

class Span(Generic[T], ValueType):
    """"""

    Empty: Final[ClassVar[Span[T]]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, segment: ArraySegment[T]):
        """

        :param segment:
        """
    @overload
    def __init__(self, array: Array[T]):
        """

        :param array:
        """
    @overload
    def __init__(self, array: Array[T], offset: int, count: int):
        """

        :param array:
        :param offset:
        :param count:
        """
    @property
    def IsEmpty(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> T:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: T) -> None: ...
    @property
    def Length(self) -> int:
        """

        :return:
        """
    def Clear(self) -> None:
        """"""
    def CopyTo(self, destination: Span[T]) -> None:
        """

        :param destination:
        """
    def DangerousGetArrayForPinning(self) -> Array[T]:
        """

        :return:
        """
    def DangerousGetArraySegment(self) -> ArraySegment[T]:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Fill(self, value: T) -> None:
        """

        :param value:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Overlaps(self, destination: ReadOnlySpan[T], elementOffset: int) -> Tuple[bool, int]:
        """

        :param destination:
        :param elementOffset:
        :return:
        """
    @overload
    def Slice(self, start: int) -> Span[T]:
        """

        :param start:
        :return:
        """
    @overload
    def Slice(self, start: int, length: int) -> Span[T]:
        """

        :param start:
        :param length:
        :return:
        """
    def ToArray(self) -> Array[T]:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __getitem__(self, index: int) -> T:
        """

        :param index:
        :return:
        """
    def __setitem__(self, index: int, value: T) -> None:
        """

        :param index:
        :param value:
        """
    @classmethod
    @overload
    def op_Implicit(cls, span: Span[T]) -> ReadOnlySpan[T]:
        """

        :param span:
        :return:
        """
    @classmethod
    @overload
    def op_Implicit(cls, array: Array[T]) -> Span[T]:
        """

        :param array:
        :return:
        """

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

    def __init__(self):
        """"""
    def AddDnsName(self, dnsName: str) -> None:
        """

        :param dnsName:
        """
    def AddEmailAddress(self, emailAddress: str) -> None:
        """

        :param emailAddress:
        """
    def AddIpAddress(self, ipAddress: IPAddress) -> None:
        """

        :param ipAddress:
        """
    def AddUri(self, uri: Uri) -> None:
        """

        :param uri:
        """
    def AddUserPrincipalName(self, upn: str) -> None:
        """

        :param upn:
        """
    def Build(self, critical: bool = ...) -> X509Extension:
        """

        :param critical:
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

    def __init__(self):
        """"""
    @property
    def Extensions(self) -> Collection[X509Extension]:
        """

        :return:
        """
    @property
    def Issuer(self) -> X500DistinguishedName:
        """

        :return:
        """
    @Issuer.setter
    def Issuer(self, value: X500DistinguishedName) -> None: ...
    @property
    def NotAfter(self) -> DateTimeOffset:
        """

        :return:
        """
    @NotAfter.setter
    def NotAfter(self, value: DateTimeOffset) -> None: ...
    @property
    def NotBefore(self) -> DateTimeOffset:
        """

        :return:
        """
    @NotBefore.setter
    def NotBefore(self, value: DateTimeOffset) -> None: ...
    @property
    def PublicKey(self) -> PublicKey:
        """

        :return:
        """
    @PublicKey.setter
    def PublicKey(self, value: PublicKey) -> None: ...
    @property
    def SerialNumber(self) -> Array[int]:
        """

        :return:
        """
    @SerialNumber.setter
    def SerialNumber(self, value: Array[int]) -> None: ...
    @property
    def SignatureAlgorithm(self) -> Array[int]:
        """

        :return:
        """
    @SignatureAlgorithm.setter
    def SignatureAlgorithm(self, value: Array[int]) -> None: ...
    @property
    def Subject(self) -> X500DistinguishedName:
        """

        :return:
        """
    @Subject.setter
    def Subject(self, value: X500DistinguishedName) -> None: ...
    @property
    def Version(self) -> int:
        """

        :return:
        """
    @Version.setter
    def Version(self, value: int) -> None: ...
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

class TimestampInformation(Object):
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
    def SignatureChain(self) -> X509Chain:
        """

        :return:
        """
    @property
    def SigningCertificate(self) -> X509Certificate2:
        """

        :return:
        """
    @property
    def Timestamp(self) -> DateTime:
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

class Triple(Generic[T1, T2, T3], ValueType):
    """"""

    @property
    def Item1(self) -> T1:
        """

        :return:
        """
    @property
    def Item2(self) -> T2:
        """

        :return:
        """
    @property
    def Item3(self) -> T3:
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
        """

        :param encoding:
        :param input:
        :return:
        """
    @classmethod
    @overload
    def EncodingGetBytes(
        cls, encoding: Encoding, input: ReadOnlySpan[Char], destination: Span[int]
    ) -> int:
        """

        :param encoding:
        :param input:
        :param destination:
        :return:
        """
    @classmethod
    @overload
    def EncodingGetBytes(
        cls, encoding: Encoding, input: Array[Char], destination: Span[int]
    ) -> int:
        """

        :param encoding:
        :param input:
        :param destination:
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
    @classmethod
    @overload
    def GetSpanForArray(cls, array: Array[T], offset: int) -> Span[T]:
        """

        :param array:
        :param offset:
        :return:
        """
    @classmethod
    @overload
    def GetSpanForArray(cls, array: Array[T], offset: int, count: int) -> Span[T]:
        """

        :param array:
        :param offset:
        :param count:
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

class X500DistinguishedName(AsnEncodedData):
    """"""

    @overload
    def __init__(self, distinguishedName: X500DistinguishedName):
        """

        :param distinguishedName:
        """
    @overload
    def __init__(self, encodedDistinguishedName: AsnEncodedData):
        """

        :param encodedDistinguishedName:
        """
    @overload
    def __init__(self, encodedDistinguishedName: Array[int]):
        """

        :param encodedDistinguishedName:
        """
    @overload
    def __init__(self, distinguishedName: str):
        """

        :param distinguishedName:
        """
    @overload
    def __init__(self, distinguishedName: str, flag: X500DistinguishedNameFlags):
        """

        :param distinguishedName:
        :param flag:
        """
    @property
    def Name(self) -> str:
        """

        :return:
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
    def Decode(self, flag: X500DistinguishedNameFlags) -> str:
        """

        :param flag:
        :return:
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

class X509BasicConstraintsExtension(X509Extension):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, encodedBasicConstraints: AsnEncodedData, critical: bool):
        """

        :param encodedBasicConstraints:
        :param critical:
        """
    @overload
    def __init__(
        self,
        certificateAuthority: bool,
        hasPathLengthConstraint: bool,
        pathLengthConstraint: int,
        critical: bool,
    ):
        """

        :param certificateAuthority:
        :param hasPathLengthConstraint:
        :param pathLengthConstraint:
        :param critical:
        """
    @property
    def CertificateAuthority(self) -> bool:
        """

        :return:
        """
    @property
    def Critical(self) -> bool:
        """

        :return:
        """
    @Critical.setter
    def Critical(self, value: bool) -> None: ...
    @property
    def HasPathLengthConstraint(self) -> bool:
        """

        :return:
        """
    @property
    def Oid(self) -> Oid:
        """

        :return:
        """
    @Oid.setter
    def Oid(self, value: Oid) -> None: ...
    @property
    def PathLengthConstraint(self) -> int:
        """

        :return:
        """
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

class X509Certificate(Object, IDeserializationCallback, ISerializable, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, cert: X509Certificate):
        """

        :param cert:
        """
    @overload
    def __init__(self, data: Array[int]):
        """

        :param data:
        """
    @overload
    def __init__(self, handle: IntPtr):
        """

        :param handle:
        """
    @overload
    def __init__(self, fileName: str):
        """

        :param fileName:
        """
    @overload
    def __init__(self, info: SerializationInfo, context: StreamingContext):
        """

        :param info:
        :param context:
        """
    @overload
    def __init__(self, rawData: Array[int], password: SecureString):
        """

        :param rawData:
        :param password:
        """
    @overload
    def __init__(self, rawData: Array[int], password: str):
        """

        :param rawData:
        :param password:
        """
    @overload
    def __init__(self, fileName: str, password: SecureString):
        """

        :param fileName:
        :param password:
        """
    @overload
    def __init__(self, fileName: str, password: str):
        """

        :param fileName:
        :param password:
        """
    @overload
    def __init__(
        self, rawData: Array[int], password: SecureString, keyStorageFlags: X509KeyStorageFlags
    ):
        """

        :param rawData:
        :param password:
        :param keyStorageFlags:
        """
    @overload
    def __init__(self, rawData: Array[int], password: str, keyStorageFlags: X509KeyStorageFlags):
        """

        :param rawData:
        :param password:
        :param keyStorageFlags:
        """
    @overload
    def __init__(self, fileName: str, password: SecureString, keyStorageFlags: X509KeyStorageFlags):
        """

        :param fileName:
        :param password:
        :param keyStorageFlags:
        """
    @overload
    def __init__(self, fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags):
        """

        :param fileName:
        :param password:
        :param keyStorageFlags:
        """
    @property
    def Handle(self) -> IntPtr:
        """

        :return:
        """
    @property
    def Issuer(self) -> str:
        """

        :return:
        """
    @property
    def Subject(self) -> str:
        """

        :return:
        """
    @classmethod
    def CreateFromCertFile(cls, filename: str) -> X509Certificate:
        """

        :param filename:
        :return:
        """
    @classmethod
    def CreateFromSignedFile(cls, filename: str) -> X509Certificate:
        """

        :param filename:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    @overload
    def Equals(self, other: X509Certificate) -> bool:
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
    @overload
    def Export(self, contentType: X509ContentType) -> Array[int]:
        """

        :param contentType:
        :return:
        """
    @overload
    def Export(self, contentType: X509ContentType, password: SecureString) -> Array[int]:
        """

        :param contentType:
        :param password:
        :return:
        """
    @overload
    def Export(self, contentType: X509ContentType, password: str) -> Array[int]:
        """

        :param contentType:
        :param password:
        :return:
        """
    @overload
    def GetCertHash(self) -> Array[int]:
        """

        :return:
        """
    @overload
    def GetCertHash(self, hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """

        :param hashAlgorithm:
        :return:
        """
    @overload
    def GetCertHashString(self) -> str:
        """

        :return:
        """
    @overload
    def GetCertHashString(self, hashAlgorithm: HashAlgorithmName) -> str:
        """

        :param hashAlgorithm:
        :return:
        """
    def GetEffectiveDateString(self) -> str:
        """

        :return:
        """
    def GetExpirationDateString(self) -> str:
        """

        :return:
        """
    def GetFormat(self) -> str:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIssuerName(self) -> str:
        """

        :return:
        """
    def GetKeyAlgorithm(self) -> str:
        """

        :return:
        """
    def GetKeyAlgorithmParameters(self) -> Array[int]:
        """

        :return:
        """
    def GetKeyAlgorithmParametersString(self) -> str:
        """

        :return:
        """
    def GetName(self) -> str:
        """

        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetPublicKey(self) -> Array[int]:
        """

        :return:
        """
    def GetPublicKeyString(self) -> str:
        """

        :return:
        """
    def GetRawCertData(self) -> Array[int]:
        """

        :return:
        """
    def GetRawCertDataString(self) -> str:
        """

        :return:
        """
    def GetSerialNumber(self) -> Array[int]:
        """

        :return:
        """
    def GetSerialNumberString(self) -> str:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def Import(self, rawData: Array[int]) -> None:
        """

        :param rawData:
        """
    @overload
    def Import(self, fileName: str) -> None:
        """

        :param fileName:
        """
    @overload
    def Import(
        self, rawData: Array[int], password: SecureString, keyStorageFlags: X509KeyStorageFlags
    ) -> None:
        """

        :param rawData:
        :param password:
        :param keyStorageFlags:
        """
    @overload
    def Import(
        self, rawData: Array[int], password: str, keyStorageFlags: X509KeyStorageFlags
    ) -> None:
        """

        :param rawData:
        :param password:
        :param keyStorageFlags:
        """
    @overload
    def Import(
        self, fileName: str, password: SecureString, keyStorageFlags: X509KeyStorageFlags
    ) -> None:
        """

        :param fileName:
        :param password:
        :param keyStorageFlags:
        """
    @overload
    def Import(self, fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags) -> None:
        """

        :param fileName:
        :param password:
        :param keyStorageFlags:
        """
    def OnDeserialization(self, sender: object) -> None:
        """

        :param sender:
        """
    def Reset(self) -> None:
        """"""
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self, fVerbose: bool) -> str:
        """

        :param fVerbose:
        :return:
        """

class X509Certificate2(X509Certificate, IDeserializationCallback, ISerializable, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, certificate: X509Certificate):
        """

        :param certificate:
        """
    @overload
    def __init__(self, rawData: Array[int]):
        """

        :param rawData:
        """
    @overload
    def __init__(self, handle: IntPtr):
        """

        :param handle:
        """
    @overload
    def __init__(self, fileName: str):
        """

        :param fileName:
        """
    @overload
    def __init__(self, rawData: Array[int], password: SecureString):
        """

        :param rawData:
        :param password:
        """
    @overload
    def __init__(self, rawData: Array[int], password: str):
        """

        :param rawData:
        :param password:
        """
    @overload
    def __init__(self, fileName: str, password: SecureString):
        """

        :param fileName:
        :param password:
        """
    @overload
    def __init__(self, fileName: str, password: str):
        """

        :param fileName:
        :param password:
        """
    @overload
    def __init__(
        self, rawData: Array[int], password: SecureString, keyStorageFlags: X509KeyStorageFlags
    ):
        """

        :param rawData:
        :param password:
        :param keyStorageFlags:
        """
    @overload
    def __init__(self, rawData: Array[int], password: str, keyStorageFlags: X509KeyStorageFlags):
        """

        :param rawData:
        :param password:
        :param keyStorageFlags:
        """
    @overload
    def __init__(self, fileName: str, password: SecureString, keyStorageFlags: X509KeyStorageFlags):
        """

        :param fileName:
        :param password:
        :param keyStorageFlags:
        """
    @overload
    def __init__(self, fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags):
        """

        :param fileName:
        :param password:
        :param keyStorageFlags:
        """
    @property
    def Archived(self) -> bool:
        """

        :return:
        """
    @Archived.setter
    def Archived(self, value: bool) -> None: ...
    @property
    def Extensions(self) -> X509ExtensionCollection:
        """

        :return:
        """
    @property
    def FriendlyName(self) -> str:
        """

        :return:
        """
    @FriendlyName.setter
    def FriendlyName(self, value: str) -> None: ...
    @property
    def Handle(self) -> IntPtr:
        """

        :return:
        """
    @property
    def HasPrivateKey(self) -> bool:
        """

        :return:
        """
    @property
    def Issuer(self) -> str:
        """

        :return:
        """
    @property
    def IssuerName(self) -> X500DistinguishedName:
        """

        :return:
        """
    @property
    def NotAfter(self) -> DateTime:
        """

        :return:
        """
    @property
    def NotBefore(self) -> DateTime:
        """

        :return:
        """
    @property
    def PrivateKey(self) -> AsymmetricAlgorithm:
        """

        :return:
        """
    @PrivateKey.setter
    def PrivateKey(self, value: AsymmetricAlgorithm) -> None: ...
    @property
    def PublicKey(self) -> PublicKey:
        """

        :return:
        """
    @property
    def RawData(self) -> Array[int]:
        """

        :return:
        """
    @property
    def SerialNumber(self) -> str:
        """

        :return:
        """
    @property
    def SignatureAlgorithm(self) -> Oid:
        """

        :return:
        """
    @property
    def Subject(self) -> str:
        """

        :return:
        """
    @property
    def SubjectName(self) -> X500DistinguishedName:
        """

        :return:
        """
    @property
    def Thumbprint(self) -> str:
        """

        :return:
        """
    @property
    def Version(self) -> int:
        """

        :return:
        """
    def Dispose(self) -> None:
        """"""
    @overload
    def Equals(self, other: X509Certificate) -> bool:
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
    @overload
    def Export(self, contentType: X509ContentType) -> Array[int]:
        """

        :param contentType:
        :return:
        """
    @overload
    def Export(self, contentType: X509ContentType, password: SecureString) -> Array[int]:
        """

        :param contentType:
        :param password:
        :return:
        """
    @overload
    def Export(self, contentType: X509ContentType, password: str) -> Array[int]:
        """

        :param contentType:
        :param password:
        :return:
        """
    @classmethod
    @overload
    def GetCertContentType(cls, rawData: Array[int]) -> X509ContentType:
        """

        :param rawData:
        :return:
        """
    @classmethod
    @overload
    def GetCertContentType(cls, fileName: str) -> X509ContentType:
        """

        :param fileName:
        :return:
        """
    @overload
    def GetCertHash(self) -> Array[int]:
        """

        :return:
        """
    @overload
    def GetCertHash(self, hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """

        :param hashAlgorithm:
        :return:
        """
    @overload
    def GetCertHashString(self) -> str:
        """

        :return:
        """
    @overload
    def GetCertHashString(self, hashAlgorithm: HashAlgorithmName) -> str:
        """

        :param hashAlgorithm:
        :return:
        """
    def GetEffectiveDateString(self) -> str:
        """

        :return:
        """
    def GetExpirationDateString(self) -> str:
        """

        :return:
        """
    def GetFormat(self) -> str:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIssuerName(self) -> str:
        """

        :return:
        """
    def GetKeyAlgorithm(self) -> str:
        """

        :return:
        """
    def GetKeyAlgorithmParameters(self) -> Array[int]:
        """

        :return:
        """
    def GetKeyAlgorithmParametersString(self) -> str:
        """

        :return:
        """
    def GetName(self) -> str:
        """

        :return:
        """
    def GetNameInfo(self, nameType: X509NameType, forIssuer: bool) -> str:
        """

        :param nameType:
        :param forIssuer:
        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetPublicKey(self) -> Array[int]:
        """

        :return:
        """
    def GetPublicKeyString(self) -> str:
        """

        :return:
        """
    def GetRawCertData(self) -> Array[int]:
        """

        :return:
        """
    def GetRawCertDataString(self) -> str:
        """

        :return:
        """
    def GetSerialNumber(self) -> Array[int]:
        """

        :return:
        """
    def GetSerialNumberString(self) -> str:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def Import(self, rawData: Array[int]) -> None:
        """

        :param rawData:
        """
    @overload
    def Import(self, fileName: str) -> None:
        """

        :param fileName:
        """
    @overload
    def Import(
        self, rawData: Array[int], password: SecureString, keyStorageFlags: X509KeyStorageFlags
    ) -> None:
        """

        :param rawData:
        :param password:
        :param keyStorageFlags:
        """
    @overload
    def Import(
        self, rawData: Array[int], password: str, keyStorageFlags: X509KeyStorageFlags
    ) -> None:
        """

        :param rawData:
        :param password:
        :param keyStorageFlags:
        """
    @overload
    def Import(
        self, fileName: str, password: SecureString, keyStorageFlags: X509KeyStorageFlags
    ) -> None:
        """

        :param fileName:
        :param password:
        :param keyStorageFlags:
        """
    @overload
    def Import(self, fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags) -> None:
        """

        :param fileName:
        :param password:
        :param keyStorageFlags:
        """
    def OnDeserialization(self, sender: object) -> None:
        """

        :param sender:
        """
    def Reset(self) -> None:
        """"""
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self, fVerbose: bool) -> str:
        """

        :param fVerbose:
        :return:
        """
    def Verify(self) -> bool:
        """

        :return:
        """

class X509Certificate2Collection(X509CertificateCollection, ICollection, IEnumerable, IList):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, certificate: X509Certificate2):
        """

        :param certificate:
        """
    @overload
    def __init__(self, certificates: X509Certificate2Collection):
        """

        :param certificates:
        """
    @overload
    def __init__(self, certificates: Array[X509Certificate2]):
        """

        :param certificates:
        """
    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
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
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, value: X509Certificate) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Add(self, certificate: X509Certificate2) -> int:
        """

        :param certificate:
        :return:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def AddRange(self, certificates: X509Certificate2Collection) -> None:
        """

        :param certificates:
        """
    @overload
    def AddRange(self, value: X509CertificateCollection) -> None:
        """

        :param value:
        """
    @overload
    def AddRange(self, certificates: Array[X509Certificate2]) -> None:
        """

        :param certificates:
        """
    @overload
    def AddRange(self, value: Array[X509Certificate]) -> None:
        """

        :param value:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: X509Certificate) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def Contains(self, certificate: X509Certificate2) -> bool:
        """

        :param certificate:
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
    def CopyTo(self, array: Array[X509Certificate], index: int) -> None:
        """

        :param array:
        :param index:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Export(self, contentType: X509ContentType) -> Array[int]:
        """

        :param contentType:
        :return:
        """
    @overload
    def Export(self, contentType: X509ContentType, password: str) -> Array[int]:
        """

        :param contentType:
        :param password:
        :return:
        """
    def Find(
        self, findType: X509FindType, findValue: object, validOnly: bool
    ) -> X509Certificate2Collection:
        """

        :param findType:
        :param findValue:
        :param validOnly:
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
    def Import(self, rawData: Array[int]) -> None:
        """

        :param rawData:
        """
    @overload
    def Import(self, fileName: str) -> None:
        """

        :param fileName:
        """
    @overload
    def Import(
        self, rawData: Array[int], password: str, keyStorageFlags: X509KeyStorageFlags
    ) -> None:
        """

        :param rawData:
        :param password:
        :param keyStorageFlags:
        """
    @overload
    def Import(self, fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags) -> None:
        """

        :param fileName:
        :param password:
        :param keyStorageFlags:
        """
    @overload
    def IndexOf(self, value: X509Certificate) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: X509Certificate) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Insert(self, index: int, certificate: X509Certificate2) -> None:
        """

        :param index:
        :param certificate:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, value: X509Certificate) -> None:
        """

        :param value:
        """
    @overload
    def Remove(self, certificate: X509Certificate2) -> None:
        """

        :param certificate:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    @overload
    def RemoveRange(self, certificates: X509Certificate2Collection) -> None:
        """

        :param certificates:
        """
    @overload
    def RemoveRange(self, certificates: Array[X509Certificate2]) -> None:
        """

        :param certificates:
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
    def __getitem__(self, index: int) -> object:
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
    @overload
    def __setitem__(self, index: int, value: X509Certificate) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: X509Certificate2) -> None:
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

class X509Certificate2Enumerator(Object, IEnumerator):
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

class X509CertificateCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: X509CertificateCollection):
        """

        :param value:
        """
    @overload
    def __init__(self, value: Array[X509Certificate]):
        """

        :param value:
        """
    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
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
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, value: X509Certificate) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def AddRange(self, value: X509CertificateCollection) -> None:
        """

        :param value:
        """
    @overload
    def AddRange(self, value: Array[X509Certificate]) -> None:
        """

        :param value:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: X509Certificate) -> bool:
        """

        :param value:
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
    def CopyTo(self, array: Array[X509Certificate], index: int) -> None:
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
    @overload
    def IndexOf(self, value: X509Certificate) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: X509Certificate) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, value: X509Certificate) -> None:
        """

        :param value:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
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
    def __getitem__(self, index: int) -> object:
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
    @overload
    def __setitem__(self, index: int, value: X509Certificate) -> None:
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

    class X509CertificateEnumerator(Object, IEnumerator):
        """"""

        def __init__(self, mappings: X509CertificateCollection):
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

class X509Chain(Object, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, useMachineContext: bool):
        """

        :param useMachineContext:
        """
    @overload
    def __init__(self, chainContext: IntPtr):
        """

        :param chainContext:
        """
    @property
    def ChainContext(self) -> IntPtr:
        """

        :return:
        """
    @property
    def ChainElements(self) -> X509ChainElementCollection:
        """

        :return:
        """
    @property
    def ChainPolicy(self) -> X509ChainPolicy:
        """

        :return:
        """
    @ChainPolicy.setter
    def ChainPolicy(self, value: X509ChainPolicy) -> None: ...
    @property
    def ChainStatus(self) -> Array[X509ChainStatus]:
        """

        :return:
        """
    @property
    def SafeHandle(self) -> SafeX509ChainHandle:
        """

        :return:
        """
    def Build(self, certificate: X509Certificate2) -> bool:
        """

        :param certificate:
        :return:
        """
    @classmethod
    def Create(cls) -> X509Chain:
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
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class X509ChainElement(Object):
    """"""

    @property
    def Certificate(self) -> X509Certificate2:
        """

        :return:
        """
    @property
    def ChainElementStatus(self) -> Array[X509ChainStatus]:
        """

        :return:
        """
    @property
    def Information(self) -> str:
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

class X509ChainElementCollection(Object, ICollection, IEnumerable):
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
    def Item(self) -> X509ChainElement:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[X509ChainElement], index: int) -> None:
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
    def __getitem__(self, index: int) -> X509ChainElement:
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

class X509ChainElementEnumerator(Object, IEnumerator):
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

class X509ChainPolicy(Object):
    """"""

    def __init__(self):
        """"""
    @property
    def ApplicationPolicy(self) -> OidCollection:
        """

        :return:
        """
    @property
    def CertificatePolicy(self) -> OidCollection:
        """

        :return:
        """
    @property
    def ExtraStore(self) -> X509Certificate2Collection:
        """

        :return:
        """
    @property
    def RevocationFlag(self) -> X509RevocationFlag:
        """

        :return:
        """
    @RevocationFlag.setter
    def RevocationFlag(self, value: X509RevocationFlag) -> None: ...
    @property
    def RevocationMode(self) -> X509RevocationMode:
        """

        :return:
        """
    @RevocationMode.setter
    def RevocationMode(self, value: X509RevocationMode) -> None: ...
    @property
    def UrlRetrievalTimeout(self) -> TimeSpan:
        """

        :return:
        """
    @UrlRetrievalTimeout.setter
    def UrlRetrievalTimeout(self, value: TimeSpan) -> None: ...
    @property
    def VerificationFlags(self) -> X509VerificationFlags:
        """

        :return:
        """
    @VerificationFlags.setter
    def VerificationFlags(self, value: X509VerificationFlags) -> None: ...
    @property
    def VerificationTime(self) -> DateTime:
        """

        :return:
        """
    @VerificationTime.setter
    def VerificationTime(self, value: DateTime) -> None: ...
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

class X509ChainStatus(ValueType):
    """"""

    @property
    def Status(self) -> X509ChainStatusFlags:
        """

        :return:
        """
    @Status.setter
    def Status(self, value: X509ChainStatusFlags) -> None: ...
    @property
    def StatusInformation(self) -> str:
        """

        :return:
        """
    @StatusInformation.setter
    def StatusInformation(self, value: str) -> None: ...
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
    def __init__(self):
        """"""
    @overload
    def __init__(self, encodedEnhancedKeyUsages: AsnEncodedData, critical: bool):
        """

        :param encodedEnhancedKeyUsages:
        :param critical:
        """
    @overload
    def __init__(self, enhancedKeyUsages: OidCollection, critical: bool):
        """

        :param enhancedKeyUsages:
        :param critical:
        """
    @property
    def Critical(self) -> bool:
        """

        :return:
        """
    @Critical.setter
    def Critical(self, value: bool) -> None: ...
    @property
    def EnhancedKeyUsages(self) -> OidCollection:
        """

        :return:
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

class X509Extension(AsnEncodedData):
    """"""

    @overload
    def __init__(self, encodedExtension: AsnEncodedData, critical: bool):
        """

        :param encodedExtension:
        :param critical:
        """
    @overload
    def __init__(self, oid: Oid, rawData: Array[int], critical: bool):
        """

        :param oid:
        :param rawData:
        :param critical:
        """
    @overload
    def __init__(self, oid: str, rawData: Array[int], critical: bool):
        """

        :param oid:
        :param rawData:
        :param critical:
        """
    @property
    def Critical(self) -> bool:
        """

        :return:
        """
    @Critical.setter
    def Critical(self, value: bool) -> None: ...
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

class X509ExtensionCollection(Object, ICollection, IEnumerable):
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
    def Item(self) -> X509Extension:
        """

        :return:
        """
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    def Add(self, extension: X509Extension) -> int:
        """

        :param extension:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[X509Extension], index: int) -> None:
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
    def __getitem__(self, index: int) -> X509Extension:
        """

        :param index:
        :return:
        """
    @overload
    def __getitem__(self, oid: str) -> X509Extension:
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

class X509ExtensionEnumerator(Object, IEnumerator):
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
    def __init__(self):
        """"""
    @overload
    def __init__(self, keyUsages: X509KeyUsageFlags, critical: bool):
        """

        :param keyUsages:
        :param critical:
        """
    @overload
    def __init__(self, encodedKeyUsage: AsnEncodedData, critical: bool):
        """

        :param encodedKeyUsage:
        :param critical:
        """
    @property
    def Critical(self) -> bool:
        """

        :return:
        """
    @Critical.setter
    def Critical(self, value: bool) -> None: ...
    @property
    def KeyUsages(self) -> X509KeyUsageFlags:
        """

        :return:
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

    class AXL_AUTHENTICODE_SIGNER_INFO(ValueType):
        """"""

        algHash: Final[CapiNative.AlgorithmId] = ...
        """"""
        cbSize: Final[int] = ...
        """"""
        dwError: Final[int] = ...
        """"""
        pChainContext: Final[IntPtr] = ...
        """"""
        pwszDescription: Final[IntPtr] = ...
        """"""
        pwszDescriptionUrl: Final[IntPtr] = ...
        """"""
        pwszHash: Final[IntPtr] = ...
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

    class AXL_AUTHENTICODE_TIMESTAMPER_INFO(ValueType):
        """"""

        algHash: Final[CapiNative.AlgorithmId] = ...
        """"""
        cbsize: Final[int] = ...
        """"""
        dwError: Final[int] = ...
        """"""
        ftTimestamp: Final[FILETIME] = ...
        """"""
        pChainContext: Final[IntPtr] = ...
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

    class AxlVerificationFlags(Enum):
        """"""

        _None: AxlVerificationFlags = ...
        """"""
        NoRevocationCheck: AxlVerificationFlags = ...
        """"""
        RevocationCheckEndCertOnly: AxlVerificationFlags = ...
        """"""
        RevocationCheckEntireChain: AxlVerificationFlags = ...
        """"""
        UrlOnlyCacheRetrieval: AxlVerificationFlags = ...
        """"""
        LifetimeSigning: AxlVerificationFlags = ...
        """"""
        TrustMicrosoftRootOnly: AxlVerificationFlags = ...
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
        ) -> Tuple[int, AXL_AUTHENTICODE_SIGNER_INFO, AXL_AUTHENTICODE_TIMESTAMPER_INFO]:
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
        @classmethod
        def _AxlGetIssuerPublicKeyHash(
            cls, pCertContext: IntPtr, ppwszPublicKeyHash: SafeAxlBufferHandle
        ) -> Tuple[int, SafeAxlBufferHandle]:
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
        """

        :return:
        """
    @classmethod
    def CreateForECDsa(cls, key: ECDsa) -> X509SignatureGenerator:
        """

        :param key:
        :return:
        """
    @classmethod
    def CreateForRSA(
        cls, key: RSA, signaturePadding: RSASignaturePadding
    ) -> X509SignatureGenerator:
        """

        :param key:
        :param signaturePadding:
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
    def GetSignatureAlgorithmIdentifier(self, hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """

        :param hashAlgorithm:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def SignData(self, data: Array[int], hashAlgorithm: HashAlgorithmName) -> Array[int]:
        """

        :param data:
        :param hashAlgorithm:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class X509Store(Object, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, storeLocation: StoreLocation):
        """

        :param storeLocation:
        """
    @overload
    def __init__(self, storeName: StoreName):
        """

        :param storeName:
        """
    @overload
    def __init__(self, storeHandle: IntPtr):
        """

        :param storeHandle:
        """
    @overload
    def __init__(self, storeName: str):
        """

        :param storeName:
        """
    @overload
    def __init__(self, storeName: StoreName, storeLocation: StoreLocation):
        """

        :param storeName:
        :param storeLocation:
        """
    @overload
    def __init__(self, storeName: str, storeLocation: StoreLocation):
        """

        :param storeName:
        :param storeLocation:
        """
    @property
    def Certificates(self) -> X509Certificate2Collection:
        """

        :return:
        """
    @property
    def Location(self) -> StoreLocation:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def StoreHandle(self) -> IntPtr:
        """

        :return:
        """
    def Add(self, certificate: X509Certificate2) -> None:
        """

        :param certificate:
        """
    def AddRange(self, certificates: X509Certificate2Collection) -> None:
        """

        :param certificates:
        """
    def Close(self) -> None:
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
    def Open(self, flags: OpenFlags) -> None:
        """

        :param flags:
        """
    def Remove(self, certificate: X509Certificate2) -> None:
        """

        :param certificate:
        """
    def RemoveRange(self, certificates: X509Certificate2Collection) -> None:
        """

        :param certificates:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class X509SubjectKeyIdentifierExtension(X509Extension):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, key: PublicKey, critical: bool):
        """

        :param key:
        :param critical:
        """
    @overload
    def __init__(self, encodedSubjectKeyIdentifier: AsnEncodedData, critical: bool):
        """

        :param encodedSubjectKeyIdentifier:
        :param critical:
        """
    @overload
    def __init__(self, subjectKeyIdentifier: Array[int], critical: bool):
        """

        :param subjectKeyIdentifier:
        :param critical:
        """
    @overload
    def __init__(self, subjectKeyIdentifier: str, critical: bool):
        """

        :param subjectKeyIdentifier:
        :param critical:
        """
    @overload
    def __init__(
        self, key: PublicKey, algorithm: X509SubjectKeyIdentifierHashAlgorithm, critical: bool
    ):
        """

        :param key:
        :param algorithm:
        :param critical:
        """
    @property
    def Critical(self) -> bool:
        """

        :return:
        """
    @Critical.setter
    def Critical(self, value: bool) -> None: ...
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
    @property
    def SubjectKeyIdentifier(self) -> str:
        """

        :return:
        """
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
