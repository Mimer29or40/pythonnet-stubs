from __future__ import annotations

from abc import ABC
from typing import List, Union, overload

from System import Array, Boolean, Byte, DateTime, Enum, Int32, Object, String, Void
from System.Collections import ICollection, IEnumerable, IEnumerator
from System.Security.Cryptography import AsnEncodedData, CryptographicAttributeObject, CryptographicAttributeObjectCollection, CspParameters, Oid
from System.Security.Cryptography.X509Certificates import X509Certificate2, X509Certificate2Collection, X509IncludeOption

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class AlgorithmIdentifier(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, oid: Oid): ...
    
    @overload
    def __init__(self, oid: Oid, keyLength: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def KeyLength(self) -> IntType: ...
    
    @KeyLength.setter
    def KeyLength(self, value: IntType) -> None: ...
    
    @property
    def Oid(self) -> Oid: ...
    
    @Oid.setter
    def Oid(self, value: Oid) -> None: ...
    
    @property
    def Parameters(self) -> ArrayType[ByteType]: ...
    
    @Parameters.setter
    def Parameters(self, value: ArrayType[ByteType]) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_KeyLength(self) -> IntType: ...
    
    def get_Oid(self) -> Oid: ...
    
    def get_Parameters(self) -> ArrayType[ByteType]: ...
    
    def set_KeyLength(self, value: IntType) -> VoidType: ...
    
    def set_Oid(self, value: Oid) -> VoidType: ...
    
    def set_Parameters(self, value: ArrayType[ByteType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CmsRecipient(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, certificate: X509Certificate2): ...
    
    @overload
    def __init__(self, recipientIdentifierType: SubjectIdentifierType, certificate: X509Certificate2): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Certificate(self) -> X509Certificate2: ...
    
    @property
    def RecipientIdentifierType(self) -> SubjectIdentifierType: ...
    
    # ---------- Methods ---------- #
    
    def get_Certificate(self) -> X509Certificate2: ...
    
    def get_RecipientIdentifierType(self) -> SubjectIdentifierType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CmsRecipientCollection(ObjectType, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, recipient: CmsRecipient): ...
    
    @overload
    def __init__(self, recipientIdentifierType: SubjectIdentifierType, certificates: X509Certificate2Collection): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    @property
    def Item(self) -> CmsRecipient: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, recipient: CmsRecipient) -> IntType: ...
    
    @overload
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    
    @overload
    def CopyTo(self, array: ArrayType[CmsRecipient], index: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> CmsRecipientEnumerator: ...
    
    def Remove(self, recipient: CmsRecipient) -> VoidType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_Item(self, index: IntType) -> CmsRecipient: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CmsRecipientEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> CmsRecipient: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> CmsRecipient: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CmsSigner(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, signerIdentifierType: SubjectIdentifierType): ...
    
    @overload
    def __init__(self, certificate: X509Certificate2): ...
    
    @overload
    def __init__(self, parameters: CspParameters): ...
    
    @overload
    def __init__(self, signerIdentifierType: SubjectIdentifierType, certificate: X509Certificate2): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Certificate(self) -> X509Certificate2: ...
    
    @Certificate.setter
    def Certificate(self, value: X509Certificate2) -> None: ...
    
    @property
    def Certificates(self) -> X509Certificate2Collection: ...
    
    @property
    def DigestAlgorithm(self) -> Oid: ...
    
    @DigestAlgorithm.setter
    def DigestAlgorithm(self, value: Oid) -> None: ...
    
    @property
    def IncludeOption(self) -> X509IncludeOption: ...
    
    @IncludeOption.setter
    def IncludeOption(self, value: X509IncludeOption) -> None: ...
    
    @property
    def SignedAttributes(self) -> CryptographicAttributeObjectCollection: ...
    
    @property
    def SignerIdentifierType(self) -> SubjectIdentifierType: ...
    
    @SignerIdentifierType.setter
    def SignerIdentifierType(self, value: SubjectIdentifierType) -> None: ...
    
    @property
    def UnsignedAttributes(self) -> CryptographicAttributeObjectCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_Certificate(self) -> X509Certificate2: ...
    
    def get_Certificates(self) -> X509Certificate2Collection: ...
    
    def get_DigestAlgorithm(self) -> Oid: ...
    
    def get_IncludeOption(self) -> X509IncludeOption: ...
    
    def get_SignedAttributes(self) -> CryptographicAttributeObjectCollection: ...
    
    def get_SignerIdentifierType(self) -> SubjectIdentifierType: ...
    
    def get_UnsignedAttributes(self) -> CryptographicAttributeObjectCollection: ...
    
    def set_Certificate(self, value: X509Certificate2) -> VoidType: ...
    
    def set_DigestAlgorithm(self, value: Oid) -> VoidType: ...
    
    def set_IncludeOption(self, value: X509IncludeOption) -> VoidType: ...
    
    def set_SignerIdentifierType(self, value: SubjectIdentifierType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ContentInfo(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, content: ArrayType[ByteType]): ...
    
    @overload
    def __init__(self, contentType: Oid, content: ArrayType[ByteType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Content(self) -> ArrayType[ByteType]: ...
    
    @property
    def ContentType(self) -> Oid: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetContentType(encodedMessage: ArrayType[ByteType]) -> Oid: ...
    
    def get_Content(self) -> ArrayType[ByteType]: ...
    
    def get_ContentType(self) -> Oid: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EnvelopedCms(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, contentInfo: ContentInfo): ...
    
    @overload
    def __init__(self, recipientIdentifierType: SubjectIdentifierType, contentInfo: ContentInfo): ...
    
    @overload
    def __init__(self, contentInfo: ContentInfo, encryptionAlgorithm: AlgorithmIdentifier): ...
    
    @overload
    def __init__(self, recipientIdentifierType: SubjectIdentifierType, contentInfo: ContentInfo, encryptionAlgorithm: AlgorithmIdentifier): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Certificates(self) -> X509Certificate2Collection: ...
    
    @property
    def ContentEncryptionAlgorithm(self) -> AlgorithmIdentifier: ...
    
    @property
    def ContentInfo(self) -> ContentInfo: ...
    
    @property
    def RecipientInfos(self) -> RecipientInfoCollection: ...
    
    @property
    def UnprotectedAttributes(self) -> CryptographicAttributeObjectCollection: ...
    
    @property
    def Version(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Decode(self, encodedMessage: ArrayType[ByteType]) -> VoidType: ...
    
    @overload
    def Decrypt(self) -> VoidType: ...
    
    @overload
    def Decrypt(self, recipientInfo: RecipientInfo) -> VoidType: ...
    
    @overload
    def Decrypt(self, extraStore: X509Certificate2Collection) -> VoidType: ...
    
    @overload
    def Decrypt(self, recipientInfo: RecipientInfo, extraStore: X509Certificate2Collection) -> VoidType: ...
    
    def Encode(self) -> ArrayType[ByteType]: ...
    
    @overload
    def Encrypt(self) -> VoidType: ...
    
    @overload
    def Encrypt(self, recipient: CmsRecipient) -> VoidType: ...
    
    @overload
    def Encrypt(self, recipients: CmsRecipientCollection) -> VoidType: ...
    
    def get_Certificates(self) -> X509Certificate2Collection: ...
    
    def get_ContentEncryptionAlgorithm(self) -> AlgorithmIdentifier: ...
    
    def get_ContentInfo(self) -> ContentInfo: ...
    
    def get_RecipientInfos(self) -> RecipientInfoCollection: ...
    
    def get_UnprotectedAttributes(self) -> CryptographicAttributeObjectCollection: ...
    
    def get_Version(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class KeyAgreeRecipientInfo(RecipientInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Date(self) -> DateTime: ...
    
    @property
    def EncryptedKey(self) -> ArrayType[ByteType]: ...
    
    @property
    def KeyEncryptionAlgorithm(self) -> AlgorithmIdentifier: ...
    
    @property
    def OriginatorIdentifierOrKey(self) -> SubjectIdentifierOrKey: ...
    
    @property
    def OtherKeyAttribute(self) -> CryptographicAttributeObject: ...
    
    @property
    def RecipientIdentifier(self) -> SubjectIdentifier: ...
    
    @property
    def Version(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_Date(self) -> DateTime: ...
    
    def get_EncryptedKey(self) -> ArrayType[ByteType]: ...
    
    def get_KeyEncryptionAlgorithm(self) -> AlgorithmIdentifier: ...
    
    def get_OriginatorIdentifierOrKey(self) -> SubjectIdentifierOrKey: ...
    
    def get_OtherKeyAttribute(self) -> CryptographicAttributeObject: ...
    
    def get_RecipientIdentifier(self) -> SubjectIdentifier: ...
    
    def get_Version(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class KeyTransRecipientInfo(RecipientInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def EncryptedKey(self) -> ArrayType[ByteType]: ...
    
    @property
    def KeyEncryptionAlgorithm(self) -> AlgorithmIdentifier: ...
    
    @property
    def RecipientIdentifier(self) -> SubjectIdentifier: ...
    
    @property
    def Version(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_EncryptedKey(self) -> ArrayType[ByteType]: ...
    
    def get_KeyEncryptionAlgorithm(self) -> AlgorithmIdentifier: ...
    
    def get_RecipientIdentifier(self) -> SubjectIdentifier: ...
    
    def get_Version(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Pkcs9AttributeObject(AsnEncodedData):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, oid: StringType, encodedData: ArrayType[ByteType]): ...
    
    @overload
    def __init__(self, oid: Oid, encodedData: ArrayType[ByteType]): ...
    
    @overload
    def __init__(self, asnEncodedData: AsnEncodedData): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Oid(self) -> Oid: ...
    
    # ---------- Methods ---------- #
    
    def CopyFrom(self, asnEncodedData: AsnEncodedData) -> VoidType: ...
    
    @overload
    def get_Oid(self) -> Oid: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Pkcs9ContentType(Pkcs9AttributeObject):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ContentType(self) -> Oid: ...
    
    # ---------- Methods ---------- #
    
    def CopyFrom(self, asnEncodedData: AsnEncodedData) -> VoidType: ...
    
    def get_ContentType(self) -> Oid: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Pkcs9DocumentDescription(Pkcs9AttributeObject):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, documentDescription: StringType): ...
    
    @overload
    def __init__(self, encodedDocumentDescription: ArrayType[ByteType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DocumentDescription(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def CopyFrom(self, asnEncodedData: AsnEncodedData) -> VoidType: ...
    
    def get_DocumentDescription(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Pkcs9DocumentName(Pkcs9AttributeObject):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, documentName: StringType): ...
    
    @overload
    def __init__(self, encodedDocumentName: ArrayType[ByteType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DocumentName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def CopyFrom(self, asnEncodedData: AsnEncodedData) -> VoidType: ...
    
    def get_DocumentName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Pkcs9MessageDigest(Pkcs9AttributeObject):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def MessageDigest(self) -> ArrayType[ByteType]: ...
    
    # ---------- Methods ---------- #
    
    def CopyFrom(self, asnEncodedData: AsnEncodedData) -> VoidType: ...
    
    def get_MessageDigest(self) -> ArrayType[ByteType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Pkcs9SigningTime(Pkcs9AttributeObject):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, signingTime: DateTime): ...
    
    @overload
    def __init__(self, encodedSigningTime: ArrayType[ByteType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def SigningTime(self) -> DateTime: ...
    
    # ---------- Methods ---------- #
    
    def CopyFrom(self, asnEncodedData: AsnEncodedData) -> VoidType: ...
    
    def get_SigningTime(self) -> DateTime: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PkcsUtils(ABC, ObjectType):
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


class PublicKeyInfo(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Algorithm(self) -> AlgorithmIdentifier: ...
    
    @property
    def KeyValue(self) -> ArrayType[ByteType]: ...
    
    # ---------- Methods ---------- #
    
    def get_Algorithm(self) -> AlgorithmIdentifier: ...
    
    def get_KeyValue(self) -> ArrayType[ByteType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RecipientInfo(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def EncryptedKey(self) -> ArrayType[ByteType]: ...
    
    @property
    def KeyEncryptionAlgorithm(self) -> AlgorithmIdentifier: ...
    
    @property
    def RecipientIdentifier(self) -> SubjectIdentifier: ...
    
    @property
    def Type(self) -> RecipientInfoType: ...
    
    @property
    def Version(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def get_EncryptedKey(self) -> ArrayType[ByteType]: ...
    
    def get_KeyEncryptionAlgorithm(self) -> AlgorithmIdentifier: ...
    
    def get_RecipientIdentifier(self) -> SubjectIdentifier: ...
    
    def get_Type(self) -> RecipientInfoType: ...
    
    def get_Version(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RecipientInfoCollection(ObjectType, ICollection, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    @property
    def Item(self) -> RecipientInfo: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    
    @overload
    def CopyTo(self, array: ArrayType[RecipientInfo], index: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> RecipientInfoEnumerator: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_Item(self, index: IntType) -> RecipientInfo: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RecipientInfoEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> RecipientInfo: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> RecipientInfo: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SignedCms(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, signerIdentifierType: SubjectIdentifierType): ...
    
    @overload
    def __init__(self, contentInfo: ContentInfo): ...
    
    @overload
    def __init__(self, signerIdentifierType: SubjectIdentifierType, contentInfo: ContentInfo): ...
    
    @overload
    def __init__(self, contentInfo: ContentInfo, detached: BooleanType): ...
    
    @overload
    def __init__(self, signerIdentifierType: SubjectIdentifierType, contentInfo: ContentInfo, detached: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Certificates(self) -> X509Certificate2Collection: ...
    
    @property
    def ContentInfo(self) -> ContentInfo: ...
    
    @property
    def Detached(self) -> BooleanType: ...
    
    @property
    def SignerInfos(self) -> SignerInfoCollection: ...
    
    @property
    def Version(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def CheckHash(self) -> VoidType: ...
    
    @overload
    def CheckSignature(self, verifySignatureOnly: BooleanType) -> VoidType: ...
    
    @overload
    def CheckSignature(self, extraStore: X509Certificate2Collection, verifySignatureOnly: BooleanType) -> VoidType: ...
    
    @overload
    def ComputeSignature(self) -> VoidType: ...
    
    @overload
    def ComputeSignature(self, signer: CmsSigner) -> VoidType: ...
    
    @overload
    def ComputeSignature(self, signer: CmsSigner, silent: BooleanType) -> VoidType: ...
    
    def Decode(self, encodedMessage: ArrayType[ByteType]) -> VoidType: ...
    
    def Encode(self) -> ArrayType[ByteType]: ...
    
    @overload
    def RemoveSignature(self, index: IntType) -> VoidType: ...
    
    @overload
    def RemoveSignature(self, signerInfo: SignerInfo) -> VoidType: ...
    
    def get_Certificates(self) -> X509Certificate2Collection: ...
    
    def get_ContentInfo(self) -> ContentInfo: ...
    
    def get_Detached(self) -> BooleanType: ...
    
    def get_SignerInfos(self) -> SignerInfoCollection: ...
    
    def get_Version(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SignerInfo(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Certificate(self) -> X509Certificate2: ...
    
    @property
    def CounterSignerInfos(self) -> SignerInfoCollection: ...
    
    @property
    def DigestAlgorithm(self) -> Oid: ...
    
    @property
    def SignatureAlgorithm(self) -> Oid: ...
    
    @property
    def SignedAttributes(self) -> CryptographicAttributeObjectCollection: ...
    
    @property
    def SignerIdentifier(self) -> SubjectIdentifier: ...
    
    @property
    def UnsignedAttributes(self) -> CryptographicAttributeObjectCollection: ...
    
    @property
    def Version(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def CheckHash(self) -> VoidType: ...
    
    @overload
    def CheckSignature(self, verifySignatureOnly: BooleanType) -> VoidType: ...
    
    @overload
    def CheckSignature(self, extraStore: X509Certificate2Collection, verifySignatureOnly: BooleanType) -> VoidType: ...
    
    @overload
    def ComputeCounterSignature(self) -> VoidType: ...
    
    @overload
    def ComputeCounterSignature(self, signer: CmsSigner) -> VoidType: ...
    
    def GetSignature(self) -> ArrayType[ByteType]: ...
    
    @overload
    def RemoveCounterSignature(self, index: IntType) -> VoidType: ...
    
    @overload
    def RemoveCounterSignature(self, counterSignerInfo: SignerInfo) -> VoidType: ...
    
    def get_Certificate(self) -> X509Certificate2: ...
    
    def get_CounterSignerInfos(self) -> SignerInfoCollection: ...
    
    def get_DigestAlgorithm(self) -> Oid: ...
    
    def get_SignatureAlgorithm(self) -> Oid: ...
    
    def get_SignedAttributes(self) -> CryptographicAttributeObjectCollection: ...
    
    def get_SignerIdentifier(self) -> SubjectIdentifier: ...
    
    def get_UnsignedAttributes(self) -> CryptographicAttributeObjectCollection: ...
    
    def get_Version(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SignerInfoCollection(ObjectType, ICollection, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def IsSynchronized(self) -> BooleanType: ...
    
    @property
    def Item(self) -> SignerInfo: ...
    
    @property
    def SyncRoot(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    
    @overload
    def CopyTo(self, array: ArrayType[SignerInfo], index: IntType) -> VoidType: ...
    
    def GetEnumerator(self) -> SignerInfoEnumerator: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_IsSynchronized(self) -> BooleanType: ...
    
    def get_Item(self, index: IntType) -> SignerInfo: ...
    
    def get_SyncRoot(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SignerInfoEnumerator(ObjectType, IEnumerator):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> SignerInfo: ...
    
    # ---------- Methods ---------- #
    
    def MoveNext(self) -> BooleanType: ...
    
    def Reset(self) -> VoidType: ...
    
    def get_Current(self) -> SignerInfo: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SubjectIdentifier(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Type(self) -> SubjectIdentifierType: ...
    
    @property
    def Value(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_Type(self) -> SubjectIdentifierType: ...
    
    def get_Value(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SubjectIdentifierOrKey(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Type(self) -> SubjectIdentifierOrKeyType: ...
    
    @property
    def Value(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_Type(self) -> SubjectIdentifierOrKeyType: ...
    
    def get_Value(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# No Interfaces

# ---------- Enums ---------- #

class KeyAgreeKeyChoice(Enum):
    Unknown: IntType = 0
    EphemeralKey: IntType = 1
    StaticKey: IntType = 2


class RecipientInfoType(Enum):
    Unknown: IntType = 0
    KeyTransport: IntType = 1
    KeyAgreement: IntType = 2


class RecipientSubType(Enum):
    Unknown: IntType = 0
    Pkcs7KeyTransport: IntType = 1
    CmsKeyTransport: IntType = 2
    CertIdKeyAgreement: IntType = 3
    PublicKeyAgreement: IntType = 4


class SubjectIdentifierOrKeyType(Enum):
    Unknown: IntType = 0
    IssuerAndSerialNumber: IntType = 1
    SubjectKeyIdentifier: IntType = 2
    PublicKeyInfo: IntType = 3


class SubjectIdentifierType(Enum):
    Unknown: IntType = 0
    IssuerAndSerialNumber: IntType = 1
    SubjectKeyIdentifier: IntType = 2
    NoSignature: IntType = 3


# No Delegates

__all__ = [
    AlgorithmIdentifier,
    CmsRecipient,
    CmsRecipientCollection,
    CmsRecipientEnumerator,
    CmsSigner,
    ContentInfo,
    EnvelopedCms,
    KeyAgreeRecipientInfo,
    KeyTransRecipientInfo,
    Pkcs9AttributeObject,
    Pkcs9ContentType,
    Pkcs9DocumentDescription,
    Pkcs9DocumentName,
    Pkcs9MessageDigest,
    Pkcs9SigningTime,
    PkcsUtils,
    PublicKeyInfo,
    RecipientInfo,
    RecipientInfoCollection,
    RecipientInfoEnumerator,
    SignedCms,
    SignerInfo,
    SignerInfoCollection,
    SignerInfoEnumerator,
    SubjectIdentifier,
    SubjectIdentifierOrKey,
    KeyAgreeKeyChoice,
    RecipientInfoType,
    RecipientSubType,
    SubjectIdentifierOrKeyType,
    SubjectIdentifierType,
]
