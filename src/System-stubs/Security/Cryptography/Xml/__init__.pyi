from __future__ import annotations

from abc import ABC
from typing import List
from typing import Protocol
from typing import Tuple
from typing import Union
from typing import overload

from System import Array
from System import Boolean
from System import Byte
from System import Enum
from System import Exception
from System import Func
from System import ICloneable
from System import IDisposable
from System import Int32
from System import Object
from System import String
from System import Type
from System import ValueType
from System import Void
from System.Collections import ArrayList
from System.Collections import Hashtable
from System.Collections import ICollection
from System.Collections import IComparer
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections import IList
from System.Collections.ObjectModel import Collection
from System.IO import Stream
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import ISerializable
from System.Security import ManifestKinds
from System.Security.Cryptography import DSA
from System.Security.Cryptography import RSA
from System.Security.Cryptography import AsymmetricAlgorithm
from System.Security.Cryptography import CipherMode
from System.Security.Cryptography import HashAlgorithm
from System.Security.Cryptography import KeyedHashAlgorithm
from System.Security.Cryptography import ManifestSignatureInformation
from System.Security.Cryptography import PaddingMode
from System.Security.Cryptography import SymmetricAlgorithm
from System.Security.Cryptography.X509Certificates import X509Certificate
from System.Security.Cryptography.X509Certificates import X509Certificate2
from System.Security.Cryptography.X509Certificates import X509IncludeOption
from System.Security.Cryptography.X509Certificates import X509RevocationFlag
from System.Security.Cryptography.X509Certificates import X509RevocationMode
from System.Security.Policy import Evidence
from System.Text import Encoding
from System.Text import StringBuilder
from System.Xml import XmlAttribute
from System.Xml import XmlCDataSection
from System.Xml import XmlComment
from System.Xml import XmlDocument
from System.Xml import XmlElement
from System.Xml import XmlEntityReference
from System.Xml import XmlException
from System.Xml import XmlNode
from System.Xml import XmlNodeList
from System.Xml import XmlProcessingInstruction
from System.Xml import XmlResolver
from System.Xml import XmlSignificantWhitespace
from System.Xml import XmlText
from System.Xml import XmlWhitespace
from System.Xml.XPath import IXPathNavigable

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class AncestralNamespaceContextManager(ABC, ObjectType):
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

class AttributeSortOrder(ObjectType, IComparer):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def Compare(self, a: ObjectType, b: ObjectType) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class C14NAncestralNamespaceContextManager(AncestralNamespaceContextManager):
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

class CanonicalXml(ObjectType):
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

class CanonicalXmlAttribute(
    XmlAttribute, ICloneable, IEnumerable, IXPathNavigable, ICanonicalizableNode
):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(
        self,
        prefix: StringType,
        localName: StringType,
        namespaceURI: StringType,
        doc: XmlDocument,
        defaultNodeSetInclusionState: BooleanType,
    ): ...

    # ---------- Properties ---------- #

    @property
    def IsInNodeSet(self) -> BooleanType: ...
    @IsInNodeSet.setter
    def IsInNodeSet(self, value: BooleanType) -> None: ...

    # ---------- Methods ---------- #

    def Write(
        self, strBuilder: StringBuilder, docPos: DocPosition, anc: AncestralNamespaceContextManager
    ) -> VoidType: ...
    def WriteHash(
        self, hash: HashAlgorithm, docPos: DocPosition, anc: AncestralNamespaceContextManager
    ) -> VoidType: ...
    def get_IsInNodeSet(self) -> BooleanType: ...
    def set_IsInNodeSet(self, value: BooleanType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CanonicalXmlCDataSection(
    XmlCDataSection, ICloneable, IEnumerable, IXPathNavigable, ICanonicalizableNode
):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(
        self, data: StringType, doc: XmlDocument, defaultNodeSetInclusionState: BooleanType
    ): ...

    # ---------- Properties ---------- #

    @property
    def IsInNodeSet(self) -> BooleanType: ...
    @IsInNodeSet.setter
    def IsInNodeSet(self, value: BooleanType) -> None: ...

    # ---------- Methods ---------- #

    def Write(
        self, strBuilder: StringBuilder, docPos: DocPosition, anc: AncestralNamespaceContextManager
    ) -> VoidType: ...
    def WriteHash(
        self, hash: HashAlgorithm, docPos: DocPosition, anc: AncestralNamespaceContextManager
    ) -> VoidType: ...
    def get_IsInNodeSet(self) -> BooleanType: ...
    def set_IsInNodeSet(self, value: BooleanType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CanonicalXmlComment(
    XmlComment, ICloneable, IEnumerable, IXPathNavigable, ICanonicalizableNode
):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(
        self,
        comment: StringType,
        doc: XmlDocument,
        defaultNodeSetInclusionState: BooleanType,
        includeComments: BooleanType,
    ): ...

    # ---------- Properties ---------- #

    @property
    def IncludeComments(self) -> BooleanType: ...
    @property
    def IsInNodeSet(self) -> BooleanType: ...
    @IsInNodeSet.setter
    def IsInNodeSet(self, value: BooleanType) -> None: ...

    # ---------- Methods ---------- #

    def Write(
        self, strBuilder: StringBuilder, docPos: DocPosition, anc: AncestralNamespaceContextManager
    ) -> VoidType: ...
    def WriteHash(
        self, hash: HashAlgorithm, docPos: DocPosition, anc: AncestralNamespaceContextManager
    ) -> VoidType: ...
    def get_IncludeComments(self) -> BooleanType: ...
    def get_IsInNodeSet(self) -> BooleanType: ...
    def set_IsInNodeSet(self, value: BooleanType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CanonicalXmlDocument(
    XmlDocument, ICloneable, IEnumerable, IXPathNavigable, ICanonicalizableNode
):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, defaultNodeSetInclusionState: BooleanType, includeComments: BooleanType): ...

    # ---------- Properties ---------- #

    @property
    def IsInNodeSet(self) -> BooleanType: ...
    @IsInNodeSet.setter
    def IsInNodeSet(self, value: BooleanType) -> None: ...

    # ---------- Methods ---------- #

    @overload
    def CreateAttribute(
        self, prefix: StringType, localName: StringType, namespaceURI: StringType
    ) -> XmlAttribute: ...
    def CreateCDataSection(self, data: StringType) -> XmlCDataSection: ...
    def CreateComment(self, data: StringType) -> XmlComment: ...
    @overload
    def CreateElement(
        self, prefix: StringType, localName: StringType, namespaceURI: StringType
    ) -> XmlElement: ...
    def CreateEntityReference(self, name: StringType) -> XmlEntityReference: ...
    def CreateProcessingInstruction(
        self, target: StringType, data: StringType
    ) -> XmlProcessingInstruction: ...
    def CreateSignificantWhitespace(self, text: StringType) -> XmlSignificantWhitespace: ...
    def CreateTextNode(self, text: StringType) -> XmlText: ...
    def CreateWhitespace(self, prefix: StringType) -> XmlWhitespace: ...
    def Write(
        self, strBuilder: StringBuilder, docPos: DocPosition, anc: AncestralNamespaceContextManager
    ) -> VoidType: ...
    def WriteHash(
        self, hash: HashAlgorithm, docPos: DocPosition, anc: AncestralNamespaceContextManager
    ) -> VoidType: ...
    def get_IsInNodeSet(self) -> BooleanType: ...
    def set_IsInNodeSet(self, value: BooleanType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CanonicalXmlElement(
    XmlElement, ICloneable, IEnumerable, IXPathNavigable, ICanonicalizableNode
):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(
        self,
        prefix: StringType,
        localName: StringType,
        namespaceURI: StringType,
        doc: XmlDocument,
        defaultNodeSetInclusionState: BooleanType,
    ): ...

    # ---------- Properties ---------- #

    @property
    def IsInNodeSet(self) -> BooleanType: ...
    @IsInNodeSet.setter
    def IsInNodeSet(self, value: BooleanType) -> None: ...

    # ---------- Methods ---------- #

    def Write(
        self, strBuilder: StringBuilder, docPos: DocPosition, anc: AncestralNamespaceContextManager
    ) -> VoidType: ...
    def WriteHash(
        self, hash: HashAlgorithm, docPos: DocPosition, anc: AncestralNamespaceContextManager
    ) -> VoidType: ...
    def get_IsInNodeSet(self) -> BooleanType: ...
    def set_IsInNodeSet(self, value: BooleanType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CanonicalXmlEntityReference(
    XmlEntityReference, ICloneable, IEnumerable, IXPathNavigable, ICanonicalizableNode
):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(
        self, name: StringType, doc: XmlDocument, defaultNodeSetInclusionState: BooleanType
    ): ...

    # ---------- Properties ---------- #

    @property
    def IsInNodeSet(self) -> BooleanType: ...
    @IsInNodeSet.setter
    def IsInNodeSet(self, value: BooleanType) -> None: ...

    # ---------- Methods ---------- #

    def Write(
        self, strBuilder: StringBuilder, docPos: DocPosition, anc: AncestralNamespaceContextManager
    ) -> VoidType: ...
    def WriteHash(
        self, hash: HashAlgorithm, docPos: DocPosition, anc: AncestralNamespaceContextManager
    ) -> VoidType: ...
    def get_IsInNodeSet(self) -> BooleanType: ...
    def set_IsInNodeSet(self, value: BooleanType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CanonicalXmlNodeList(XmlNodeList, IEnumerable, IDisposable, IList, ICollection):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Count(self) -> IntType: ...
    @property
    def IsFixedSize(self) -> BooleanType: ...
    @property
    def IsReadOnly(self) -> BooleanType: ...
    @property
    def IsSynchronized(self) -> BooleanType: ...
    @property
    def SyncRoot(self) -> ObjectType: ...

    # ---------- Methods ---------- #

    def Add(self, value: ObjectType) -> IntType: ...
    def Clear(self) -> VoidType: ...
    def Contains(self, value: ObjectType) -> BooleanType: ...
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def IndexOf(self, value: ObjectType) -> IntType: ...
    def Insert(self, index: IntType, value: ObjectType) -> VoidType: ...
    def Item(self, index: IntType) -> XmlNode: ...
    def Remove(self, value: ObjectType) -> VoidType: ...
    def RemoveAt(self, index: IntType) -> VoidType: ...
    def get_Count(self) -> IntType: ...
    def get_IsFixedSize(self) -> BooleanType: ...
    def get_IsReadOnly(self) -> BooleanType: ...
    def get_IsSynchronized(self) -> BooleanType: ...
    def get_SyncRoot(self) -> ObjectType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CanonicalXmlProcessingInstruction(
    XmlProcessingInstruction, ICloneable, IEnumerable, IXPathNavigable, ICanonicalizableNode
):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(
        self,
        target: StringType,
        data: StringType,
        doc: XmlDocument,
        defaultNodeSetInclusionState: BooleanType,
    ): ...

    # ---------- Properties ---------- #

    @property
    def IsInNodeSet(self) -> BooleanType: ...
    @IsInNodeSet.setter
    def IsInNodeSet(self, value: BooleanType) -> None: ...

    # ---------- Methods ---------- #

    def Write(
        self, strBuilder: StringBuilder, docPos: DocPosition, anc: AncestralNamespaceContextManager
    ) -> VoidType: ...
    def WriteHash(
        self, hash: HashAlgorithm, docPos: DocPosition, anc: AncestralNamespaceContextManager
    ) -> VoidType: ...
    def get_IsInNodeSet(self) -> BooleanType: ...
    def set_IsInNodeSet(self, value: BooleanType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CanonicalXmlSignificantWhitespace(
    XmlSignificantWhitespace, ICloneable, IEnumerable, IXPathNavigable, ICanonicalizableNode
):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(
        self, strData: StringType, doc: XmlDocument, defaultNodeSetInclusionState: BooleanType
    ): ...

    # ---------- Properties ---------- #

    @property
    def IsInNodeSet(self) -> BooleanType: ...
    @IsInNodeSet.setter
    def IsInNodeSet(self, value: BooleanType) -> None: ...

    # ---------- Methods ---------- #

    def Write(
        self, strBuilder: StringBuilder, docPos: DocPosition, anc: AncestralNamespaceContextManager
    ) -> VoidType: ...
    def WriteHash(
        self, hash: HashAlgorithm, docPos: DocPosition, anc: AncestralNamespaceContextManager
    ) -> VoidType: ...
    def get_IsInNodeSet(self) -> BooleanType: ...
    def set_IsInNodeSet(self, value: BooleanType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CanonicalXmlText(XmlText, ICloneable, IEnumerable, IXPathNavigable, ICanonicalizableNode):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(
        self, strData: StringType, doc: XmlDocument, defaultNodeSetInclusionState: BooleanType
    ): ...

    # ---------- Properties ---------- #

    @property
    def IsInNodeSet(self) -> BooleanType: ...
    @IsInNodeSet.setter
    def IsInNodeSet(self, value: BooleanType) -> None: ...

    # ---------- Methods ---------- #

    def Write(
        self, strBuilder: StringBuilder, docPos: DocPosition, anc: AncestralNamespaceContextManager
    ) -> VoidType: ...
    def WriteHash(
        self, hash: HashAlgorithm, docPos: DocPosition, anc: AncestralNamespaceContextManager
    ) -> VoidType: ...
    def get_IsInNodeSet(self) -> BooleanType: ...
    def set_IsInNodeSet(self, value: BooleanType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CanonicalXmlWhitespace(
    XmlWhitespace, ICloneable, IEnumerable, IXPathNavigable, ICanonicalizableNode
):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(
        self, strData: StringType, doc: XmlDocument, defaultNodeSetInclusionState: BooleanType
    ): ...

    # ---------- Properties ---------- #

    @property
    def IsInNodeSet(self) -> BooleanType: ...
    @IsInNodeSet.setter
    def IsInNodeSet(self, value: BooleanType) -> None: ...

    # ---------- Methods ---------- #

    def Write(
        self, strBuilder: StringBuilder, docPos: DocPosition, anc: AncestralNamespaceContextManager
    ) -> VoidType: ...
    def WriteHash(
        self, hash: HashAlgorithm, docPos: DocPosition, anc: AncestralNamespaceContextManager
    ) -> VoidType: ...
    def get_IsInNodeSet(self) -> BooleanType: ...
    def set_IsInNodeSet(self, value: BooleanType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CanonicalizationDispatcher(ObjectType):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    @staticmethod
    def Write(
        node: XmlNode,
        strBuilder: StringBuilder,
        docPos: DocPosition,
        anc: AncestralNamespaceContextManager,
    ) -> VoidType: ...
    @staticmethod
    def WriteGenericNode(
        node: XmlNode,
        strBuilder: StringBuilder,
        docPos: DocPosition,
        anc: AncestralNamespaceContextManager,
    ) -> VoidType: ...
    @staticmethod
    def WriteHash(
        node: XmlNode,
        hash: HashAlgorithm,
        docPos: DocPosition,
        anc: AncestralNamespaceContextManager,
    ) -> VoidType: ...
    @staticmethod
    def WriteHashGenericNode(
        node: XmlNode,
        hash: HashAlgorithm,
        docPos: DocPosition,
        anc: AncestralNamespaceContextManager,
    ) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CipherData(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, cipherValue: ArrayType[ByteType]): ...
    @overload
    def __init__(self, cipherReference: CipherReference): ...

    # ---------- Properties ---------- #

    @property
    def CipherReference(self) -> CipherReference: ...
    @CipherReference.setter
    def CipherReference(self, value: CipherReference) -> None: ...
    @property
    def CipherValue(self) -> ArrayType[ByteType]: ...
    @CipherValue.setter
    def CipherValue(self, value: ArrayType[ByteType]) -> None: ...

    # ---------- Methods ---------- #

    def GetXml(self) -> XmlElement: ...
    def LoadXml(self, value: XmlElement) -> VoidType: ...
    def get_CipherReference(self) -> CipherReference: ...
    def get_CipherValue(self) -> ArrayType[ByteType]: ...
    def set_CipherReference(self, value: CipherReference) -> VoidType: ...
    def set_CipherValue(self, value: ArrayType[ByteType]) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CipherReference(EncryptedReference):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, uri: StringType): ...
    @overload
    def __init__(self, uri: StringType, transformChain: TransformChain): ...

    # No Properties

    # ---------- Methods ---------- #

    def GetXml(self) -> XmlElement: ...
    def LoadXml(self, value: XmlElement) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class CryptoSignedXmlRecursionException(XmlException, ISerializable, _Exception):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: StringType): ...
    @overload
    def __init__(self, message: StringType, inner: Exception): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class DSAKeyValue(KeyInfoClause):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, key: DSA): ...

    # ---------- Properties ---------- #

    @property
    def Key(self) -> DSA: ...
    @Key.setter
    def Key(self, value: DSA) -> None: ...

    # ---------- Methods ---------- #

    def GetXml(self) -> XmlElement: ...
    def LoadXml(self, value: XmlElement) -> VoidType: ...
    def get_Key(self) -> DSA: ...
    def set_Key(self, value: DSA) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class DataObject(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(
        self, id: StringType, mimeType: StringType, encoding: StringType, data: XmlElement
    ): ...

    # ---------- Properties ---------- #

    @property
    def Data(self) -> XmlNodeList: ...
    @Data.setter
    def Data(self, value: XmlNodeList) -> None: ...
    @property
    def Encoding(self) -> StringType: ...
    @Encoding.setter
    def Encoding(self, value: StringType) -> None: ...
    @property
    def Id(self) -> StringType: ...
    @Id.setter
    def Id(self, value: StringType) -> None: ...
    @property
    def MimeType(self) -> StringType: ...
    @MimeType.setter
    def MimeType(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    def GetXml(self) -> XmlElement: ...
    def LoadXml(self, value: XmlElement) -> VoidType: ...
    def get_Data(self) -> XmlNodeList: ...
    def get_Encoding(self) -> StringType: ...
    def get_Id(self) -> StringType: ...
    def get_MimeType(self) -> StringType: ...
    def set_Data(self, value: XmlNodeList) -> VoidType: ...
    def set_Encoding(self, value: StringType) -> VoidType: ...
    def set_Id(self, value: StringType) -> VoidType: ...
    def set_MimeType(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class DataReference(EncryptedReference):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, uri: StringType): ...
    @overload
    def __init__(self, uri: StringType, transformChain: TransformChain): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EncryptedData(EncryptedType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # No Properties

    # ---------- Methods ---------- #

    def GetXml(self) -> XmlElement: ...
    def LoadXml(self, value: XmlElement) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EncryptedKey(EncryptedType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def CarriedKeyName(self) -> StringType: ...
    @CarriedKeyName.setter
    def CarriedKeyName(self, value: StringType) -> None: ...
    @property
    def Recipient(self) -> StringType: ...
    @Recipient.setter
    def Recipient(self, value: StringType) -> None: ...
    @property
    def ReferenceList(self) -> ReferenceList: ...

    # ---------- Methods ---------- #

    @overload
    def AddReference(self, dataReference: DataReference) -> VoidType: ...
    @overload
    def AddReference(self, keyReference: KeyReference) -> VoidType: ...
    def GetXml(self) -> XmlElement: ...
    def LoadXml(self, value: XmlElement) -> VoidType: ...
    def get_CarriedKeyName(self) -> StringType: ...
    def get_Recipient(self) -> StringType: ...
    def get_ReferenceList(self) -> ReferenceList: ...
    def set_CarriedKeyName(self, value: StringType) -> VoidType: ...
    def set_Recipient(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EncryptedReference(ABC, ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def TransformChain(self) -> TransformChain: ...
    @TransformChain.setter
    def TransformChain(self, value: TransformChain) -> None: ...
    @property
    def Uri(self) -> StringType: ...
    @Uri.setter
    def Uri(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    def AddTransform(self, transform: Transform) -> VoidType: ...
    def GetXml(self) -> XmlElement: ...
    def LoadXml(self, value: XmlElement) -> VoidType: ...
    def get_TransformChain(self) -> TransformChain: ...
    def get_Uri(self) -> StringType: ...
    def set_TransformChain(self, value: TransformChain) -> VoidType: ...
    def set_Uri(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EncryptedType(ABC, ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def CipherData(self) -> CipherData: ...
    @CipherData.setter
    def CipherData(self, value: CipherData) -> None: ...
    @property
    def Encoding(self) -> StringType: ...
    @Encoding.setter
    def Encoding(self, value: StringType) -> None: ...
    @property
    def EncryptionMethod(self) -> EncryptionMethod: ...
    @EncryptionMethod.setter
    def EncryptionMethod(self, value: EncryptionMethod) -> None: ...
    @property
    def EncryptionProperties(self) -> EncryptionPropertyCollection: ...
    @property
    def Id(self) -> StringType: ...
    @Id.setter
    def Id(self, value: StringType) -> None: ...
    @property
    def KeyInfo(self) -> KeyInfo: ...
    @KeyInfo.setter
    def KeyInfo(self, value: KeyInfo) -> None: ...
    @property
    def MimeType(self) -> StringType: ...
    @MimeType.setter
    def MimeType(self, value: StringType) -> None: ...
    @property
    def Type(self) -> StringType: ...
    @Type.setter
    def Type(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    def AddProperty(self, ep: EncryptionProperty) -> VoidType: ...
    def GetXml(self) -> XmlElement: ...
    def LoadXml(self, value: XmlElement) -> VoidType: ...
    def get_CipherData(self) -> CipherData: ...
    def get_Encoding(self) -> StringType: ...
    def get_EncryptionMethod(self) -> EncryptionMethod: ...
    def get_EncryptionProperties(self) -> EncryptionPropertyCollection: ...
    def get_Id(self) -> StringType: ...
    def get_KeyInfo(self) -> KeyInfo: ...
    def get_MimeType(self) -> StringType: ...
    def get_Type(self) -> StringType: ...
    def set_CipherData(self, value: CipherData) -> VoidType: ...
    def set_Encoding(self, value: StringType) -> VoidType: ...
    def set_EncryptionMethod(self, value: EncryptionMethod) -> VoidType: ...
    def set_Id(self, value: StringType) -> VoidType: ...
    def set_KeyInfo(self, value: KeyInfo) -> VoidType: ...
    def set_MimeType(self, value: StringType) -> VoidType: ...
    def set_Type(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EncryptedXml(ObjectType):
    # ---------- Fields ---------- #

    @staticmethod
    @property
    def XmlEncAES128KeyWrapUrl() -> StringType: ...
    @staticmethod
    @property
    def XmlEncAES128Url() -> StringType: ...
    @staticmethod
    @property
    def XmlEncAES192KeyWrapUrl() -> StringType: ...
    @staticmethod
    @property
    def XmlEncAES192Url() -> StringType: ...
    @staticmethod
    @property
    def XmlEncAES256KeyWrapUrl() -> StringType: ...
    @staticmethod
    @property
    def XmlEncAES256Url() -> StringType: ...
    @staticmethod
    @property
    def XmlEncDESUrl() -> StringType: ...
    @staticmethod
    @property
    def XmlEncElementContentUrl() -> StringType: ...
    @staticmethod
    @property
    def XmlEncElementUrl() -> StringType: ...
    @staticmethod
    @property
    def XmlEncEncryptedKeyUrl() -> StringType: ...
    @staticmethod
    @property
    def XmlEncNamespaceUrl() -> StringType: ...
    @staticmethod
    @property
    def XmlEncRSA15Url() -> StringType: ...
    @staticmethod
    @property
    def XmlEncRSAOAEPUrl() -> StringType: ...
    @staticmethod
    @property
    def XmlEncSHA256Url() -> StringType: ...
    @staticmethod
    @property
    def XmlEncSHA512Url() -> StringType: ...
    @staticmethod
    @property
    def XmlEncTripleDESKeyWrapUrl() -> StringType: ...
    @staticmethod
    @property
    def XmlEncTripleDESUrl() -> StringType: ...

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, document: XmlDocument): ...
    @overload
    def __init__(self, document: XmlDocument, evidence: Evidence): ...

    # ---------- Properties ---------- #

    @property
    def DocumentEvidence(self) -> Evidence: ...
    @DocumentEvidence.setter
    def DocumentEvidence(self, value: Evidence) -> None: ...
    @property
    def Encoding(self) -> Encoding: ...
    @Encoding.setter
    def Encoding(self, value: Encoding) -> None: ...
    @property
    def Mode(self) -> CipherMode: ...
    @Mode.setter
    def Mode(self, value: CipherMode) -> None: ...
    @property
    def Padding(self) -> PaddingMode: ...
    @Padding.setter
    def Padding(self, value: PaddingMode) -> None: ...
    @property
    def Recipient(self) -> StringType: ...
    @Recipient.setter
    def Recipient(self, value: StringType) -> None: ...
    @property
    def Resolver(self) -> XmlResolver: ...
    @Resolver.setter
    def Resolver(self, value: XmlResolver) -> None: ...
    @property
    def XmlDSigSearchDepth(self) -> IntType: ...
    @XmlDSigSearchDepth.setter
    def XmlDSigSearchDepth(self, value: IntType) -> None: ...

    # ---------- Methods ---------- #

    def AddKeyNameMapping(self, keyName: StringType, keyObject: ObjectType) -> VoidType: ...
    def ClearKeyNameMappings(self) -> VoidType: ...
    def DecryptData(
        self, encryptedData: EncryptedData, symmetricAlgorithm: SymmetricAlgorithm
    ) -> ArrayType[ByteType]: ...
    def DecryptDocument(self) -> VoidType: ...
    def DecryptEncryptedKey(self, encryptedKey: EncryptedKey) -> ArrayType[ByteType]: ...
    @staticmethod
    @overload
    def DecryptKey(
        keyData: ArrayType[ByteType], symmetricAlgorithm: SymmetricAlgorithm
    ) -> ArrayType[ByteType]: ...
    @staticmethod
    @overload
    def DecryptKey(
        keyData: ArrayType[ByteType], rsa: RSA, useOAEP: BooleanType
    ) -> ArrayType[ByteType]: ...
    @overload
    def Encrypt(self, inputElement: XmlElement, certificate: X509Certificate2) -> EncryptedData: ...
    @overload
    def Encrypt(self, inputElement: XmlElement, keyName: StringType) -> EncryptedData: ...
    @overload
    def EncryptData(
        self, plaintext: ArrayType[ByteType], symmetricAlgorithm: SymmetricAlgorithm
    ) -> ArrayType[ByteType]: ...
    @overload
    def EncryptData(
        self, inputElement: XmlElement, symmetricAlgorithm: SymmetricAlgorithm, content: BooleanType
    ) -> ArrayType[ByteType]: ...
    @staticmethod
    @overload
    def EncryptKey(
        keyData: ArrayType[ByteType], symmetricAlgorithm: SymmetricAlgorithm
    ) -> ArrayType[ByteType]: ...
    @staticmethod
    @overload
    def EncryptKey(
        keyData: ArrayType[ByteType], rsa: RSA, useOAEP: BooleanType
    ) -> ArrayType[ByteType]: ...
    def GetDecryptionIV(
        self, encryptedData: EncryptedData, symmetricAlgorithmUri: StringType
    ) -> ArrayType[ByteType]: ...
    def GetDecryptionKey(
        self, encryptedData: EncryptedData, symmetricAlgorithmUri: StringType
    ) -> SymmetricAlgorithm: ...
    def GetIdElement(self, document: XmlDocument, idValue: StringType) -> XmlElement: ...
    def ReplaceData(
        self, inputElement: XmlElement, decryptedData: ArrayType[ByteType]
    ) -> VoidType: ...
    @staticmethod
    def ReplaceElement(
        inputElement: XmlElement, encryptedData: EncryptedData, content: BooleanType
    ) -> VoidType: ...
    def get_DocumentEvidence(self) -> Evidence: ...
    def get_Encoding(self) -> Encoding: ...
    def get_Mode(self) -> CipherMode: ...
    def get_Padding(self) -> PaddingMode: ...
    def get_Recipient(self) -> StringType: ...
    def get_Resolver(self) -> XmlResolver: ...
    def get_XmlDSigSearchDepth(self) -> IntType: ...
    def set_DocumentEvidence(self, value: Evidence) -> VoidType: ...
    def set_Encoding(self, value: Encoding) -> VoidType: ...
    def set_Mode(self, value: CipherMode) -> VoidType: ...
    def set_Padding(self, value: PaddingMode) -> VoidType: ...
    def set_Recipient(self, value: StringType) -> VoidType: ...
    def set_Resolver(self, value: XmlResolver) -> VoidType: ...
    def set_XmlDSigSearchDepth(self, value: IntType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EncryptionMethod(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, algorithm: StringType): ...

    # ---------- Properties ---------- #

    @property
    def KeyAlgorithm(self) -> StringType: ...
    @KeyAlgorithm.setter
    def KeyAlgorithm(self, value: StringType) -> None: ...
    @property
    def KeySize(self) -> IntType: ...
    @KeySize.setter
    def KeySize(self, value: IntType) -> None: ...

    # ---------- Methods ---------- #

    def GetXml(self) -> XmlElement: ...
    def LoadXml(self, value: XmlElement) -> VoidType: ...
    def get_KeyAlgorithm(self) -> StringType: ...
    def get_KeySize(self) -> IntType: ...
    def set_KeyAlgorithm(self, value: StringType) -> VoidType: ...
    def set_KeySize(self, value: IntType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EncryptionProperty(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, elementProperty: XmlElement): ...

    # ---------- Properties ---------- #

    @property
    def Id(self) -> StringType: ...
    @property
    def PropertyElement(self) -> XmlElement: ...
    @PropertyElement.setter
    def PropertyElement(self, value: XmlElement) -> None: ...
    @property
    def Target(self) -> StringType: ...

    # ---------- Methods ---------- #

    def GetXml(self) -> XmlElement: ...
    def LoadXml(self, value: XmlElement) -> VoidType: ...
    def get_Id(self) -> StringType: ...
    def get_PropertyElement(self) -> XmlElement: ...
    def get_Target(self) -> StringType: ...
    def set_PropertyElement(self, value: XmlElement) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class EncryptionPropertyCollection(ObjectType, IList, ICollection, IEnumerable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def Count(self) -> IntType: ...
    @property
    def IsFixedSize(self) -> BooleanType: ...
    @property
    def IsReadOnly(self) -> BooleanType: ...
    @property
    def IsSynchronized(self) -> BooleanType: ...
    @property
    def ItemOf(self) -> EncryptionProperty: ...
    @ItemOf.setter
    def ItemOf(self, value: EncryptionProperty) -> None: ...
    @property
    def SyncRoot(self) -> ObjectType: ...

    # ---------- Methods ---------- #

    def Add(self, value: EncryptionProperty) -> IntType: ...
    def Clear(self) -> VoidType: ...
    def Contains(self, value: EncryptionProperty) -> BooleanType: ...
    @overload
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    @overload
    def CopyTo(self, array: ArrayType[EncryptionProperty], index: IntType) -> VoidType: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def IndexOf(self, value: EncryptionProperty) -> IntType: ...
    def Insert(self, index: IntType, value: EncryptionProperty) -> VoidType: ...
    def Item(self, index: IntType) -> EncryptionProperty: ...
    def Remove(self, value: EncryptionProperty) -> VoidType: ...
    def RemoveAt(self, index: IntType) -> VoidType: ...
    def get_Count(self) -> IntType: ...
    def get_IsFixedSize(self) -> BooleanType: ...
    def get_IsReadOnly(self) -> BooleanType: ...
    def get_IsSynchronized(self) -> BooleanType: ...
    def get_ItemOf(self, index: IntType) -> EncryptionProperty: ...
    def get_SyncRoot(self) -> ObjectType: ...
    def set_ItemOf(self, index: IntType, value: EncryptionProperty) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ExcAncestralNamespaceContextManager(AncestralNamespaceContextManager):
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

class ExcCanonicalXml(ObjectType):
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

class KeyInfo(ObjectType, IEnumerable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def Count(self) -> IntType: ...
    @property
    def Id(self) -> StringType: ...
    @Id.setter
    def Id(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    def AddClause(self, clause: KeyInfoClause) -> VoidType: ...
    @overload
    def GetEnumerator(self) -> IEnumerator: ...
    @overload
    def GetEnumerator(self, requestedObjectType: TypeType) -> IEnumerator: ...
    def GetXml(self) -> XmlElement: ...
    def LoadXml(self, value: XmlElement) -> VoidType: ...
    def get_Count(self) -> IntType: ...
    def get_Id(self) -> StringType: ...
    def set_Id(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class KeyInfoClause(ABC, ObjectType):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def GetXml(self) -> XmlElement: ...
    def LoadXml(self, element: XmlElement) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class KeyInfoEncryptedKey(KeyInfoClause):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, encryptedKey: EncryptedKey): ...

    # ---------- Properties ---------- #

    @property
    def EncryptedKey(self) -> EncryptedKey: ...
    @EncryptedKey.setter
    def EncryptedKey(self, value: EncryptedKey) -> None: ...

    # ---------- Methods ---------- #

    def GetXml(self) -> XmlElement: ...
    def LoadXml(self, value: XmlElement) -> VoidType: ...
    def get_EncryptedKey(self) -> EncryptedKey: ...
    def set_EncryptedKey(self, value: EncryptedKey) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class KeyInfoName(KeyInfoClause):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, keyName: StringType): ...

    # ---------- Properties ---------- #

    @property
    def Value(self) -> StringType: ...
    @Value.setter
    def Value(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    def GetXml(self) -> XmlElement: ...
    def LoadXml(self, value: XmlElement) -> VoidType: ...
    def get_Value(self) -> StringType: ...
    def set_Value(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class KeyInfoNode(KeyInfoClause):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, node: XmlElement): ...

    # ---------- Properties ---------- #

    @property
    def Value(self) -> XmlElement: ...
    @Value.setter
    def Value(self, value: XmlElement) -> None: ...

    # ---------- Methods ---------- #

    def GetXml(self) -> XmlElement: ...
    def LoadXml(self, value: XmlElement) -> VoidType: ...
    def get_Value(self) -> XmlElement: ...
    def set_Value(self, value: XmlElement) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class KeyInfoRetrievalMethod(KeyInfoClause):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, strUri: StringType): ...
    @overload
    def __init__(self, strUri: StringType, typeName: StringType): ...

    # ---------- Properties ---------- #

    @property
    def Type(self) -> StringType: ...
    @Type.setter
    def Type(self, value: StringType) -> None: ...
    @property
    def Uri(self) -> StringType: ...
    @Uri.setter
    def Uri(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    def GetXml(self) -> XmlElement: ...
    def LoadXml(self, value: XmlElement) -> VoidType: ...
    def get_Type(self) -> StringType: ...
    def get_Uri(self) -> StringType: ...
    def set_Type(self, value: StringType) -> VoidType: ...
    def set_Uri(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class KeyInfoX509Data(KeyInfoClause):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, rgbCert: ArrayType[ByteType]): ...
    @overload
    def __init__(self, cert: X509Certificate): ...
    @overload
    def __init__(self, cert: X509Certificate, includeOption: X509IncludeOption): ...

    # ---------- Properties ---------- #

    @property
    def CRL(self) -> ArrayType[ByteType]: ...
    @CRL.setter
    def CRL(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def Certificates(self) -> ArrayList: ...
    @property
    def IssuerSerials(self) -> ArrayList: ...
    @property
    def SubjectKeyIds(self) -> ArrayList: ...
    @property
    def SubjectNames(self) -> ArrayList: ...

    # ---------- Methods ---------- #

    def AddCertificate(self, certificate: X509Certificate) -> VoidType: ...
    def AddIssuerSerial(self, issuerName: StringType, serialNumber: StringType) -> VoidType: ...
    @overload
    def AddSubjectKeyId(self, subjectKeyId: ArrayType[ByteType]) -> VoidType: ...
    @overload
    def AddSubjectKeyId(self, subjectKeyId: StringType) -> VoidType: ...
    def AddSubjectName(self, subjectName: StringType) -> VoidType: ...
    def GetXml(self) -> XmlElement: ...
    def LoadXml(self, element: XmlElement) -> VoidType: ...
    def get_CRL(self) -> ArrayType[ByteType]: ...
    def get_Certificates(self) -> ArrayList: ...
    def get_IssuerSerials(self) -> ArrayList: ...
    def get_SubjectKeyIds(self) -> ArrayList: ...
    def get_SubjectNames(self) -> ArrayList: ...
    def set_CRL(self, value: ArrayType[ByteType]) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class KeyReference(EncryptedReference):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, uri: StringType): ...
    @overload
    def __init__(self, uri: StringType, transformChain: TransformChain): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ManifestSignedXml(SignedXml):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self, manifestXml: XmlDocument, manifest: ManifestKinds): ...

    # No Properties

    # ---------- Methods ---------- #

    def GetIdElement(self, document: XmlDocument, idValue: StringType) -> XmlElement: ...
    def VerifySignature(
        self, revocationFlag: X509RevocationFlag, revocationMode: X509RevocationMode
    ) -> ManifestSignatureInformation: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class MyXmlDocument(XmlDocument, ICloneable, IEnumerable, IXPathNavigable):
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

class NamespaceFrame(ObjectType):
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

class NamespaceSortOrder(ObjectType, IComparer):
    # No Fields

    # No Constructors

    # No Properties

    # ---------- Methods ---------- #

    def Compare(self, a: ObjectType, b: ObjectType) -> IntType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class RSAKeyValue(KeyInfoClause):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, key: RSA): ...

    # ---------- Properties ---------- #

    @property
    def Key(self) -> RSA: ...
    @Key.setter
    def Key(self, value: RSA) -> None: ...

    # ---------- Methods ---------- #

    def GetXml(self) -> XmlElement: ...
    def LoadXml(self, value: XmlElement) -> VoidType: ...
    def get_Key(self) -> RSA: ...
    def set_Key(self, value: RSA) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Reference(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, stream: Stream): ...
    @overload
    def __init__(self, uri: StringType): ...

    # ---------- Properties ---------- #

    @property
    def DigestMethod(self) -> StringType: ...
    @DigestMethod.setter
    def DigestMethod(self, value: StringType) -> None: ...
    @property
    def DigestValue(self) -> ArrayType[ByteType]: ...
    @DigestValue.setter
    def DigestValue(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def Id(self) -> StringType: ...
    @Id.setter
    def Id(self, value: StringType) -> None: ...
    @property
    def TransformChain(self) -> TransformChain: ...
    @TransformChain.setter
    def TransformChain(self, value: TransformChain) -> None: ...
    @property
    def Type(self) -> StringType: ...
    @Type.setter
    def Type(self, value: StringType) -> None: ...
    @property
    def Uri(self) -> StringType: ...
    @Uri.setter
    def Uri(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    def AddTransform(self, transform: Transform) -> VoidType: ...
    def GetXml(self) -> XmlElement: ...
    def LoadXml(self, value: XmlElement) -> VoidType: ...
    def get_DigestMethod(self) -> StringType: ...
    def get_DigestValue(self) -> ArrayType[ByteType]: ...
    def get_Id(self) -> StringType: ...
    def get_TransformChain(self) -> TransformChain: ...
    def get_Type(self) -> StringType: ...
    def get_Uri(self) -> StringType: ...
    def set_DigestMethod(self, value: StringType) -> VoidType: ...
    def set_DigestValue(self, value: ArrayType[ByteType]) -> VoidType: ...
    def set_Id(self, value: StringType) -> VoidType: ...
    def set_TransformChain(self, value: TransformChain) -> VoidType: ...
    def set_Type(self, value: StringType) -> VoidType: ...
    def set_Uri(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class ReferenceList(ObjectType, IList, ICollection, IEnumerable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def Count(self) -> IntType: ...
    @property
    def IsSynchronized(self) -> BooleanType: ...
    @property
    def ItemOf(self) -> EncryptedReference: ...
    @ItemOf.setter
    def ItemOf(self, value: EncryptedReference) -> None: ...
    @property
    def SyncRoot(self) -> ObjectType: ...

    # ---------- Methods ---------- #

    def Add(self, value: ObjectType) -> IntType: ...
    def Clear(self) -> VoidType: ...
    def Contains(self, value: ObjectType) -> BooleanType: ...
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def IndexOf(self, value: ObjectType) -> IntType: ...
    def Insert(self, index: IntType, value: ObjectType) -> VoidType: ...
    def Item(self, index: IntType) -> EncryptedReference: ...
    def Remove(self, value: ObjectType) -> VoidType: ...
    def RemoveAt(self, index: IntType) -> VoidType: ...
    def get_Count(self) -> IntType: ...
    def get_IsSynchronized(self) -> BooleanType: ...
    def get_ItemOf(self, index: IntType) -> EncryptedReference: ...
    def get_SyncRoot(self) -> ObjectType: ...
    def set_ItemOf(self, index: IntType, value: EncryptedReference) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Signature(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def Id(self) -> StringType: ...
    @Id.setter
    def Id(self, value: StringType) -> None: ...
    @property
    def KeyInfo(self) -> KeyInfo: ...
    @KeyInfo.setter
    def KeyInfo(self, value: KeyInfo) -> None: ...
    @property
    def ObjectList(self) -> IList: ...
    @ObjectList.setter
    def ObjectList(self, value: IList) -> None: ...
    @property
    def SignatureValue(self) -> ArrayType[ByteType]: ...
    @SignatureValue.setter
    def SignatureValue(self, value: ArrayType[ByteType]) -> None: ...
    @property
    def SignedInfo(self) -> SignedInfo: ...
    @SignedInfo.setter
    def SignedInfo(self, value: SignedInfo) -> None: ...

    # ---------- Methods ---------- #

    def AddObject(self, dataObject: DataObject) -> VoidType: ...
    def GetXml(self) -> XmlElement: ...
    def LoadXml(self, value: XmlElement) -> VoidType: ...
    def get_Id(self) -> StringType: ...
    def get_KeyInfo(self) -> KeyInfo: ...
    def get_ObjectList(self) -> IList: ...
    def get_SignatureValue(self) -> ArrayType[ByteType]: ...
    def get_SignedInfo(self) -> SignedInfo: ...
    def set_Id(self, value: StringType) -> VoidType: ...
    def set_KeyInfo(self, value: KeyInfo) -> VoidType: ...
    def set_ObjectList(self, value: IList) -> VoidType: ...
    def set_SignatureValue(self, value: ArrayType[ByteType]) -> VoidType: ...
    def set_SignedInfo(self, value: SignedInfo) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SignedInfo(ObjectType, ICollection, IEnumerable):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def CanonicalizationMethod(self) -> StringType: ...
    @CanonicalizationMethod.setter
    def CanonicalizationMethod(self, value: StringType) -> None: ...
    @property
    def CanonicalizationMethodObject(self) -> Transform: ...
    @property
    def Count(self) -> IntType: ...
    @property
    def Id(self) -> StringType: ...
    @Id.setter
    def Id(self, value: StringType) -> None: ...
    @property
    def IsReadOnly(self) -> BooleanType: ...
    @property
    def IsSynchronized(self) -> BooleanType: ...
    @property
    def References(self) -> ArrayList: ...
    @property
    def SignatureLength(self) -> StringType: ...
    @SignatureLength.setter
    def SignatureLength(self, value: StringType) -> None: ...
    @property
    def SignatureMethod(self) -> StringType: ...
    @SignatureMethod.setter
    def SignatureMethod(self, value: StringType) -> None: ...
    @property
    def SyncRoot(self) -> ObjectType: ...

    # ---------- Methods ---------- #

    def AddReference(self, reference: Reference) -> VoidType: ...
    def CopyTo(self, array: Array, index: IntType) -> VoidType: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def GetXml(self) -> XmlElement: ...
    def LoadXml(self, value: XmlElement) -> VoidType: ...
    def get_CanonicalizationMethod(self) -> StringType: ...
    def get_CanonicalizationMethodObject(self) -> Transform: ...
    def get_Count(self) -> IntType: ...
    def get_Id(self) -> StringType: ...
    def get_IsReadOnly(self) -> BooleanType: ...
    def get_IsSynchronized(self) -> BooleanType: ...
    def get_References(self) -> ArrayList: ...
    def get_SignatureLength(self) -> StringType: ...
    def get_SignatureMethod(self) -> StringType: ...
    def get_SyncRoot(self) -> ObjectType: ...
    def set_CanonicalizationMethod(self, value: StringType) -> VoidType: ...
    def set_Id(self, value: StringType) -> VoidType: ...
    def set_SignatureLength(self, value: StringType) -> VoidType: ...
    def set_SignatureMethod(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SignedXml(ObjectType):
    # ---------- Fields ---------- #

    @staticmethod
    @property
    def XmlDecryptionTransformUrl() -> StringType: ...
    @staticmethod
    @property
    def XmlDsigBase64TransformUrl() -> StringType: ...
    @staticmethod
    @property
    def XmlDsigC14NTransformUrl() -> StringType: ...
    @staticmethod
    @property
    def XmlDsigC14NWithCommentsTransformUrl() -> StringType: ...
    @staticmethod
    @property
    def XmlDsigCanonicalizationUrl() -> StringType: ...
    @staticmethod
    @property
    def XmlDsigCanonicalizationWithCommentsUrl() -> StringType: ...
    @staticmethod
    @property
    def XmlDsigDSAUrl() -> StringType: ...
    @staticmethod
    @property
    def XmlDsigEnvelopedSignatureTransformUrl() -> StringType: ...
    @staticmethod
    @property
    def XmlDsigExcC14NTransformUrl() -> StringType: ...
    @staticmethod
    @property
    def XmlDsigExcC14NWithCommentsTransformUrl() -> StringType: ...
    @staticmethod
    @property
    def XmlDsigHMACSHA1Url() -> StringType: ...
    @staticmethod
    @property
    def XmlDsigMinimalCanonicalizationUrl() -> StringType: ...
    @staticmethod
    @property
    def XmlDsigNamespaceUrl() -> StringType: ...
    @staticmethod
    @property
    def XmlDsigRSASHA1Url() -> StringType: ...
    @staticmethod
    @property
    def XmlDsigRSASHA256Url() -> StringType: ...
    @staticmethod
    @property
    def XmlDsigRSASHA384Url() -> StringType: ...
    @staticmethod
    @property
    def XmlDsigRSASHA512Url() -> StringType: ...
    @staticmethod
    @property
    def XmlDsigSHA1Url() -> StringType: ...
    @staticmethod
    @property
    def XmlDsigSHA256Url() -> StringType: ...
    @staticmethod
    @property
    def XmlDsigSHA384Url() -> StringType: ...
    @staticmethod
    @property
    def XmlDsigSHA512Url() -> StringType: ...
    @staticmethod
    @property
    def XmlDsigXPathTransformUrl() -> StringType: ...
    @staticmethod
    @property
    def XmlDsigXsltTransformUrl() -> StringType: ...
    @staticmethod
    @property
    def XmlLicenseTransformUrl() -> StringType: ...

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, document: XmlDocument): ...
    @overload
    def __init__(self, elem: XmlElement): ...

    # ---------- Properties ---------- #

    @property
    def EncryptedXml(self) -> EncryptedXml: ...
    @EncryptedXml.setter
    def EncryptedXml(self, value: EncryptedXml) -> None: ...
    @property
    def KeyInfo(self) -> KeyInfo: ...
    @KeyInfo.setter
    def KeyInfo(self, value: KeyInfo) -> None: ...
    @Resolver.setter
    def Resolver(self, value: XmlResolver) -> None: ...
    @property
    def SafeCanonicalizationMethods(self) -> Collection[StringType]: ...
    @property
    def Signature(self) -> Signature: ...
    @property
    def SignatureFormatValidator(self) -> Func[SignedXml, BooleanType]: ...
    @SignatureFormatValidator.setter
    def SignatureFormatValidator(self, value: Func[SignedXml, BooleanType]) -> None: ...
    @property
    def SignatureLength(self) -> StringType: ...
    @property
    def SignatureMethod(self) -> StringType: ...
    @property
    def SignatureValue(self) -> ArrayType[ByteType]: ...
    @property
    def SignedInfo(self) -> SignedInfo: ...
    @property
    def SigningKey(self) -> AsymmetricAlgorithm: ...
    @SigningKey.setter
    def SigningKey(self, value: AsymmetricAlgorithm) -> None: ...
    @property
    def SigningKeyName(self) -> StringType: ...
    @SigningKeyName.setter
    def SigningKeyName(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    def AddObject(self, dataObject: DataObject) -> VoidType: ...
    def AddReference(self, reference: Reference) -> VoidType: ...
    @overload
    def CheckSignature(self) -> BooleanType: ...
    @overload
    def CheckSignature(self, key: AsymmetricAlgorithm) -> BooleanType: ...
    @overload
    def CheckSignature(self, macAlg: KeyedHashAlgorithm) -> BooleanType: ...
    @overload
    def CheckSignature(
        self, certificate: X509Certificate2, verifySignatureOnly: BooleanType
    ) -> BooleanType: ...
    def CheckSignatureReturningKey(
        self, signingKey: AsymmetricAlgorithm
    ) -> Tuple[BooleanType, AsymmetricAlgorithm]: ...
    @overload
    def ComputeSignature(self) -> VoidType: ...
    @overload
    def ComputeSignature(self, macAlg: KeyedHashAlgorithm) -> VoidType: ...
    def GetIdElement(self, document: XmlDocument, idValue: StringType) -> XmlElement: ...
    def GetXml(self) -> XmlElement: ...
    def LoadXml(self, value: XmlElement) -> VoidType: ...
    def get_EncryptedXml(self) -> EncryptedXml: ...
    def get_KeyInfo(self) -> KeyInfo: ...
    def get_SafeCanonicalizationMethods(self) -> Collection[StringType]: ...
    def get_Signature(self) -> Signature: ...
    def get_SignatureFormatValidator(self) -> Func[SignedXml, BooleanType]: ...
    def get_SignatureLength(self) -> StringType: ...
    def get_SignatureMethod(self) -> StringType: ...
    def get_SignatureValue(self) -> ArrayType[ByteType]: ...
    def get_SignedInfo(self) -> SignedInfo: ...
    def get_SigningKey(self) -> AsymmetricAlgorithm: ...
    def get_SigningKeyName(self) -> StringType: ...
    def set_EncryptedXml(self, value: EncryptedXml) -> VoidType: ...
    def set_KeyInfo(self, value: KeyInfo) -> VoidType: ...
    def set_Resolver(self, value: XmlResolver) -> VoidType: ...
    def set_SignatureFormatValidator(self, value: Func[SignedXml, BooleanType]) -> VoidType: ...
    def set_SigningKey(self, value: AsymmetricAlgorithm) -> VoidType: ...
    def set_SigningKeyName(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class SignedXmlDebugLog(ABC, ObjectType):
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

class SymmetricKeyWrap(ABC, ObjectType):
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

class Transform(ABC, ObjectType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def Algorithm(self) -> StringType: ...
    @Algorithm.setter
    def Algorithm(self, value: StringType) -> None: ...
    @property
    def Context(self) -> XmlElement: ...
    @Context.setter
    def Context(self, value: XmlElement) -> None: ...
    @property
    def InputTypes(self) -> ArrayType[TypeType]: ...
    @property
    def OutputTypes(self) -> ArrayType[TypeType]: ...
    @property
    def PropagatedNamespaces(self) -> Hashtable: ...
    @Resolver.setter
    def Resolver(self, value: XmlResolver) -> None: ...

    # ---------- Methods ---------- #

    def GetDigestedOutput(self, hash: HashAlgorithm) -> ArrayType[ByteType]: ...
    @overload
    def GetOutput(self) -> ObjectType: ...
    @overload
    def GetOutput(self, type: TypeType) -> ObjectType: ...
    def GetXml(self) -> XmlElement: ...
    def LoadInnerXml(self, nodeList: XmlNodeList) -> VoidType: ...
    def LoadInput(self, obj: ObjectType) -> VoidType: ...
    def get_Algorithm(self) -> StringType: ...
    def get_Context(self) -> XmlElement: ...
    def get_InputTypes(self) -> ArrayType[TypeType]: ...
    def get_OutputTypes(self) -> ArrayType[TypeType]: ...
    def get_PropagatedNamespaces(self) -> Hashtable: ...
    def set_Algorithm(self, value: StringType) -> VoidType: ...
    def set_Context(self, value: XmlElement) -> VoidType: ...
    def set_Resolver(self, value: XmlResolver) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class TransformChain(ObjectType):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def Count(self) -> IntType: ...
    def __getitem__(self, key: IntType) -> Transform: ...

    # ---------- Methods ---------- #

    def Add(self, transform: Transform) -> VoidType: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def get_Count(self) -> IntType: ...
    def get_Item(self, index: IntType) -> Transform: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class Utils(ObjectType):
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

class XmlDecryptionTransform(Transform):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def EncryptedXml(self) -> EncryptedXml: ...
    @EncryptedXml.setter
    def EncryptedXml(self, value: EncryptedXml) -> None: ...
    @property
    def InputTypes(self) -> ArrayType[TypeType]: ...
    @property
    def OutputTypes(self) -> ArrayType[TypeType]: ...

    # ---------- Methods ---------- #

    def AddExceptUri(self, uri: StringType) -> VoidType: ...
    @overload
    def GetOutput(self) -> ObjectType: ...
    @overload
    def GetOutput(self, type: TypeType) -> ObjectType: ...
    def LoadInnerXml(self, nodeList: XmlNodeList) -> VoidType: ...
    def LoadInput(self, obj: ObjectType) -> VoidType: ...
    def get_EncryptedXml(self) -> EncryptedXml: ...
    def get_InputTypes(self) -> ArrayType[TypeType]: ...
    def get_OutputTypes(self) -> ArrayType[TypeType]: ...
    def set_EncryptedXml(self, value: EncryptedXml) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class XmlDsigBase64Transform(Transform):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def InputTypes(self) -> ArrayType[TypeType]: ...
    @property
    def OutputTypes(self) -> ArrayType[TypeType]: ...

    # ---------- Methods ---------- #

    @overload
    def GetOutput(self) -> ObjectType: ...
    @overload
    def GetOutput(self, type: TypeType) -> ObjectType: ...
    def LoadInnerXml(self, nodeList: XmlNodeList) -> VoidType: ...
    def LoadInput(self, obj: ObjectType) -> VoidType: ...
    def get_InputTypes(self) -> ArrayType[TypeType]: ...
    def get_OutputTypes(self) -> ArrayType[TypeType]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class XmlDsigC14NTransform(Transform):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, includeComments: BooleanType): ...

    # ---------- Properties ---------- #

    @property
    def InputTypes(self) -> ArrayType[TypeType]: ...
    @property
    def OutputTypes(self) -> ArrayType[TypeType]: ...

    # ---------- Methods ---------- #

    def GetDigestedOutput(self, hash: HashAlgorithm) -> ArrayType[ByteType]: ...
    @overload
    def GetOutput(self) -> ObjectType: ...
    @overload
    def GetOutput(self, type: TypeType) -> ObjectType: ...
    def LoadInnerXml(self, nodeList: XmlNodeList) -> VoidType: ...
    def LoadInput(self, obj: ObjectType) -> VoidType: ...
    def get_InputTypes(self) -> ArrayType[TypeType]: ...
    def get_OutputTypes(self) -> ArrayType[TypeType]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class XmlDsigC14NWithCommentsTransform(XmlDsigC14NTransform):
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

class XmlDsigEnvelopedSignatureTransform(Transform):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, includeComments: BooleanType): ...

    # ---------- Properties ---------- #

    @property
    def InputTypes(self) -> ArrayType[TypeType]: ...
    @property
    def OutputTypes(self) -> ArrayType[TypeType]: ...

    # ---------- Methods ---------- #

    @overload
    def GetOutput(self) -> ObjectType: ...
    @overload
    def GetOutput(self, type: TypeType) -> ObjectType: ...
    def LoadInnerXml(self, nodeList: XmlNodeList) -> VoidType: ...
    def LoadInput(self, obj: ObjectType) -> VoidType: ...
    def get_InputTypes(self) -> ArrayType[TypeType]: ...
    def get_OutputTypes(self) -> ArrayType[TypeType]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class XmlDsigExcC14NTransform(Transform):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, includeComments: BooleanType): ...
    @overload
    def __init__(self, inclusiveNamespacesPrefixList: StringType): ...
    @overload
    def __init__(self, includeComments: BooleanType, inclusiveNamespacesPrefixList: StringType): ...

    # ---------- Properties ---------- #

    @property
    def InclusiveNamespacesPrefixList(self) -> StringType: ...
    @InclusiveNamespacesPrefixList.setter
    def InclusiveNamespacesPrefixList(self, value: StringType) -> None: ...
    @property
    def InputTypes(self) -> ArrayType[TypeType]: ...
    @property
    def OutputTypes(self) -> ArrayType[TypeType]: ...

    # ---------- Methods ---------- #

    def GetDigestedOutput(self, hash: HashAlgorithm) -> ArrayType[ByteType]: ...
    @overload
    def GetOutput(self) -> ObjectType: ...
    @overload
    def GetOutput(self, type: TypeType) -> ObjectType: ...
    def LoadInnerXml(self, nodeList: XmlNodeList) -> VoidType: ...
    def LoadInput(self, obj: ObjectType) -> VoidType: ...
    def get_InclusiveNamespacesPrefixList(self) -> StringType: ...
    def get_InputTypes(self) -> ArrayType[TypeType]: ...
    def get_OutputTypes(self) -> ArrayType[TypeType]: ...
    def set_InclusiveNamespacesPrefixList(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class XmlDsigExcC14NWithCommentsTransform(XmlDsigExcC14NTransform):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, inclusiveNamespacesPrefixList: StringType): ...

    # No Properties

    # No Methods

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class XmlDsigXPathTransform(Transform):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def InputTypes(self) -> ArrayType[TypeType]: ...
    @property
    def OutputTypes(self) -> ArrayType[TypeType]: ...

    # ---------- Methods ---------- #

    @overload
    def GetOutput(self) -> ObjectType: ...
    @overload
    def GetOutput(self, type: TypeType) -> ObjectType: ...
    def LoadInnerXml(self, nodeList: XmlNodeList) -> VoidType: ...
    def LoadInput(self, obj: ObjectType) -> VoidType: ...
    def get_InputTypes(self) -> ArrayType[TypeType]: ...
    def get_OutputTypes(self) -> ArrayType[TypeType]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class XmlDsigXsltTransform(Transform):
    # No Fields

    # ---------- Constructors ---------- #

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, includeComments: BooleanType): ...

    # ---------- Properties ---------- #

    @property
    def InputTypes(self) -> ArrayType[TypeType]: ...
    @property
    def OutputTypes(self) -> ArrayType[TypeType]: ...

    # ---------- Methods ---------- #

    @overload
    def GetOutput(self) -> ObjectType: ...
    @overload
    def GetOutput(self, type: TypeType) -> ObjectType: ...
    def LoadInnerXml(self, nodeList: XmlNodeList) -> VoidType: ...
    def LoadInput(self, obj: ObjectType) -> VoidType: ...
    def get_InputTypes(self) -> ArrayType[TypeType]: ...
    def get_OutputTypes(self) -> ArrayType[TypeType]: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

class XmlLicenseTransform(Transform):
    # No Fields

    # ---------- Constructors ---------- #

    def __init__(self): ...

    # ---------- Properties ---------- #

    @property
    def Decryptor(self) -> IRelDecryptor: ...
    @Decryptor.setter
    def Decryptor(self, value: IRelDecryptor) -> None: ...
    @property
    def InputTypes(self) -> ArrayType[TypeType]: ...
    @property
    def OutputTypes(self) -> ArrayType[TypeType]: ...

    # ---------- Methods ---------- #

    @overload
    def GetOutput(self) -> ObjectType: ...
    @overload
    def GetOutput(self, type: TypeType) -> ObjectType: ...
    def LoadInnerXml(self, nodeList: XmlNodeList) -> VoidType: ...
    def LoadInput(self, obj: ObjectType) -> VoidType: ...
    def get_Decryptor(self) -> IRelDecryptor: ...
    def get_InputTypes(self) -> ArrayType[TypeType]: ...
    def get_OutputTypes(self) -> ArrayType[TypeType]: ...
    def set_Decryptor(self, value: IRelDecryptor) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

# ---------- Structs ---------- #

class X509IssuerSerial(ValueType):
    # No Fields

    # No Constructors

    # ---------- Properties ---------- #

    @property
    def IssuerName(self) -> StringType: ...
    @IssuerName.setter
    def IssuerName(self, value: StringType) -> None: ...
    @property
    def SerialNumber(self) -> StringType: ...
    @SerialNumber.setter
    def SerialNumber(self, value: StringType) -> None: ...

    # ---------- Methods ---------- #

    def get_IssuerName(self) -> StringType: ...
    def get_SerialNumber(self) -> StringType: ...
    def set_IssuerName(self, value: StringType) -> VoidType: ...
    def set_SerialNumber(self, value: StringType) -> VoidType: ...

    # No Events

    # No Sub Classes

    # No Sub Structs

    # No Sub Interfaces

    # No Sub Enums

# ---------- Interfaces ---------- #

class ICanonicalizableNode(Protocol):
    # ---------- Properties ---------- #

    @property
    def IsInNodeSet(self) -> BooleanType: ...
    @IsInNodeSet.setter
    def IsInNodeSet(self, value: BooleanType) -> None: ...

    # ---------- Methods ---------- #

    def Write(
        self, strBuilder: StringBuilder, docPos: DocPosition, anc: AncestralNamespaceContextManager
    ) -> VoidType: ...
    def WriteHash(
        self, hash: HashAlgorithm, docPos: DocPosition, anc: AncestralNamespaceContextManager
    ) -> VoidType: ...
    def get_IsInNodeSet(self) -> BooleanType: ...
    def set_IsInNodeSet(self, value: BooleanType) -> VoidType: ...

    # No Events

class IRelDecryptor(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def Decrypt(
        self, encryptionMethod: EncryptionMethod, keyInfo: KeyInfo, toDecrypt: Stream
    ) -> Stream: ...

    # No Events

# ---------- Enums ---------- #

class CertUsageType(Enum):
    Verification = 0
    Decryption = 1

class DocPosition(Enum):
    BeforeRootElement = 0
    InRootElement = 1
    AfterRootElement = 2

class ReferenceTargetType(Enum):
    Stream = 0
    XmlElement = 1
    UriReference = 2

class TransformInputType(Enum):
    XmlDocument = 1
    XmlStream = 2
    XmlNodeSet = 3

# No Delegates

__all__ = [
    AncestralNamespaceContextManager,
    AttributeSortOrder,
    C14NAncestralNamespaceContextManager,
    CanonicalXml,
    CanonicalXmlAttribute,
    CanonicalXmlCDataSection,
    CanonicalXmlComment,
    CanonicalXmlDocument,
    CanonicalXmlElement,
    CanonicalXmlEntityReference,
    CanonicalXmlNodeList,
    CanonicalXmlProcessingInstruction,
    CanonicalXmlSignificantWhitespace,
    CanonicalXmlText,
    CanonicalXmlWhitespace,
    CanonicalizationDispatcher,
    CipherData,
    CipherReference,
    CryptoSignedXmlRecursionException,
    DSAKeyValue,
    DataObject,
    DataReference,
    EncryptedData,
    EncryptedKey,
    EncryptedReference,
    EncryptedType,
    EncryptedXml,
    EncryptionMethod,
    EncryptionProperty,
    EncryptionPropertyCollection,
    ExcAncestralNamespaceContextManager,
    ExcCanonicalXml,
    KeyInfo,
    KeyInfoClause,
    KeyInfoEncryptedKey,
    KeyInfoName,
    KeyInfoNode,
    KeyInfoRetrievalMethod,
    KeyInfoX509Data,
    KeyReference,
    ManifestSignedXml,
    MyXmlDocument,
    NamespaceFrame,
    NamespaceSortOrder,
    RSAKeyValue,
    Reference,
    ReferenceList,
    Signature,
    SignedInfo,
    SignedXml,
    SignedXmlDebugLog,
    SymmetricKeyWrap,
    Transform,
    TransformChain,
    Utils,
    XmlDecryptionTransform,
    XmlDsigBase64Transform,
    XmlDsigC14NTransform,
    XmlDsigC14NWithCommentsTransform,
    XmlDsigEnvelopedSignatureTransform,
    XmlDsigExcC14NTransform,
    XmlDsigExcC14NWithCommentsTransform,
    XmlDsigXPathTransform,
    XmlDsigXsltTransform,
    XmlLicenseTransform,
    X509IssuerSerial,
    ICanonicalizableNode,
    IRelDecryptor,
    CertUsageType,
    DocPosition,
    ReferenceTargetType,
    TransformInputType,
]
