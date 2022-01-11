from __future__ import annotations

from abc import ABC
from typing import List, Protocol, Union, overload

from System import Array, AsyncCallback, Boolean, Byte, DateTime, Enum, IAsyncResult, IDisposable, Int32, Int64, Object, String, Void
from System.Collections import ICollection, IEnumerable
from System.Collections.Specialized import NameValueCollection, StringDictionary
from System.IO import Stream
from System.Net import DelegatedStream, LazyAsyncResult
from System.Runtime.Serialization import IDeserializationCallback, ISerializable

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class Base64WriteStateInfo(WriteStateInfoBase):
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


class BaseWriter(ABC, ObjectType):
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


class ContentDisposition(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, disposition: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CreationDate(self) -> DateTime: ...
    
    @CreationDate.setter
    def CreationDate(self, value: DateTime) -> None: ...
    
    @property
    def DispositionType(self) -> StringType: ...
    
    @DispositionType.setter
    def DispositionType(self, value: StringType) -> None: ...
    
    @property
    def FileName(self) -> StringType: ...
    
    @FileName.setter
    def FileName(self, value: StringType) -> None: ...
    
    @property
    def Inline(self) -> BooleanType: ...
    
    @Inline.setter
    def Inline(self, value: BooleanType) -> None: ...
    
    @property
    def ModificationDate(self) -> DateTime: ...
    
    @ModificationDate.setter
    def ModificationDate(self, value: DateTime) -> None: ...
    
    @property
    def Parameters(self) -> StringDictionary: ...
    
    @property
    def ReadDate(self) -> DateTime: ...
    
    @ReadDate.setter
    def ReadDate(self, value: DateTime) -> None: ...
    
    @property
    def Size(self) -> LongType: ...
    
    @Size.setter
    def Size(self, value: LongType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, rparam: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_CreationDate(self) -> DateTime: ...
    
    def get_DispositionType(self) -> StringType: ...
    
    def get_FileName(self) -> StringType: ...
    
    def get_Inline(self) -> BooleanType: ...
    
    def get_ModificationDate(self) -> DateTime: ...
    
    def get_Parameters(self) -> StringDictionary: ...
    
    def get_ReadDate(self) -> DateTime: ...
    
    def get_Size(self) -> LongType: ...
    
    def set_CreationDate(self, value: DateTime) -> VoidType: ...
    
    def set_DispositionType(self, value: StringType) -> VoidType: ...
    
    def set_FileName(self, value: StringType) -> VoidType: ...
    
    def set_Inline(self, value: BooleanType) -> VoidType: ...
    
    def set_ModificationDate(self, value: DateTime) -> VoidType: ...
    
    def set_ReadDate(self, value: DateTime) -> VoidType: ...
    
    def set_Size(self, value: LongType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ContentType(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, contentType: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Boundary(self) -> StringType: ...
    
    @Boundary.setter
    def Boundary(self, value: StringType) -> None: ...
    
    @property
    def CharSet(self) -> StringType: ...
    
    @CharSet.setter
    def CharSet(self, value: StringType) -> None: ...
    
    @property
    def MediaType(self) -> StringType: ...
    
    @MediaType.setter
    def MediaType(self, value: StringType) -> None: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def Parameters(self) -> StringDictionary: ...
    
    # ---------- Methods ---------- #
    
    def Equals(self, rparam: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToString(self) -> StringType: ...
    
    def get_Boundary(self) -> StringType: ...
    
    def get_CharSet(self) -> StringType: ...
    
    def get_MediaType(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_Parameters(self) -> StringDictionary: ...
    
    def set_Boundary(self, value: StringType) -> VoidType: ...
    
    def set_CharSet(self, value: StringType) -> VoidType: ...
    
    def set_MediaType(self, value: StringType) -> VoidType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DispositionTypeNames(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Attachment() -> StringType: ...
    
    @staticmethod
    @property
    def Inline() -> StringType: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EightBitStream(DelegatedStream, IDisposable, IEncodableStream):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginWrite(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def DecodeBytes(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    
    def EncodeBytes(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    def GetEncodedString(self) -> StringType: ...
    
    def GetStream(self) -> Stream: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class EncodedStreamFactory(ObjectType):
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


class HeaderCollection(NameValueCollection, ICollection, IEnumerable, ISerializable, IDeserializationCallback):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Add(self, name: StringType, value: StringType) -> VoidType: ...
    
    @overload
    def Get(self, name: StringType) -> StringType: ...
    
    @overload
    def GetValues(self, name: StringType) -> ArrayType[StringType]: ...
    
    def Remove(self, name: StringType) -> VoidType: ...
    
    def Set(self, name: StringType, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MailBnfHelper(ABC, ObjectType):
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


class MediaTypeNames(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    
    # ---------- Sub Classes ---------- #
    
    class Text(ABC, ObjectType):
        # ---------- Fields ---------- #
        
        @staticmethod
        @property
        def Html() -> StringType: ...
        
        @staticmethod
        @property
        def Plain() -> StringType: ...
        
        @staticmethod
        @property
        def RichText() -> StringType: ...
        
        @staticmethod
        @property
        def Xml() -> StringType: ...
        
        # No Constructors
        
        # No Properties
        
        # No Methods
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    class Application(ABC, ObjectType):
        # ---------- Fields ---------- #
        
        @staticmethod
        @property
        def Octet() -> StringType: ...
        
        @staticmethod
        @property
        def Pdf() -> StringType: ...
        
        @staticmethod
        @property
        def Rtf() -> StringType: ...
        
        @staticmethod
        @property
        def Soap() -> StringType: ...
        
        @staticmethod
        @property
        def Zip() -> StringType: ...
        
        # No Constructors
        
        # No Properties
        
        # No Methods
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    class Image(ABC, ObjectType):
        # ---------- Fields ---------- #
        
        @staticmethod
        @property
        def Gif() -> StringType: ...
        
        @staticmethod
        @property
        def Jpeg() -> StringType: ...
        
        @staticmethod
        @property
        def Tiff() -> StringType: ...
        
        # No Constructors
        
        # No Properties
        
        # No Methods
        
        # No Events
        
        # No Sub Classes
        
        # No Sub Structs
        
        # No Sub Interfaces
        
        # No Sub Enums
    
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MimeBasePart(ObjectType):
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


class MimeMultiPart(MimeBasePart):
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


class MimePart(MimeBasePart, IDisposable):
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


class MimeWriter(BaseWriter):
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


class MultiAsyncResult(LazyAsyncResult, IAsyncResult):
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


class QEncodedStream(DelegatedStream, IDisposable, IEncodableStream):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginWrite(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def Close(self) -> VoidType: ...
    
    def DecodeBytes(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    
    def EncodeBytes(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def GetEncodedString(self) -> StringType: ...
    
    def GetStream(self) -> Stream: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class QuotedPrintableStream(DelegatedStream, IDisposable, IEncodableStream):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginWrite(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType, callback: AsyncCallback, state: ObjectType) -> IAsyncResult: ...
    
    def Close(self) -> VoidType: ...
    
    def DecodeBytes(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    
    def EncodeBytes(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    
    def EndWrite(self, asyncResult: IAsyncResult) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    def GetEncodedString(self) -> StringType: ...
    
    def GetStream(self) -> Stream: ...
    
    def Write(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SmtpDateTime(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WriteStateInfoBase(ObjectType):
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


# No Structs

# ---------- Interfaces ---------- #

class IEncodableStream(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def DecodeBytes(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    
    def EncodeBytes(self, buffer: ArrayType[ByteType], offset: IntType, count: IntType) -> IntType: ...
    
    def GetEncodedString(self) -> StringType: ...
    
    def GetStream(self) -> Stream: ...
    
    # No Events


# ---------- Enums ---------- #

class ContentTransferEncoding(Enum):
    SevenBit: IntType = 0
    EightBit: IntType = 1
    Binary: IntType = 2
    Base64: IntType = 3
    QuotedPrintable: IntType = 4
    QEncoded: IntType = 5
    Other: IntType = 6
    Unspecified: IntType = 7


class MimeMultiPartType(Enum):
    Unknown: IntType = -1
    Mixed: IntType = 0
    Alternative: IntType = 1
    Parallel: IntType = 2
    Related: IntType = 3


class TransferEncoding(Enum):
    Unknown: IntType = -1
    QuotedPrintable: IntType = 0
    Base64: IntType = 1
    SevenBit: IntType = 2
    EightBit: IntType = 3


# No Delegates

__all__ = [
    Base64WriteStateInfo,
    BaseWriter,
    ContentDisposition,
    ContentType,
    DispositionTypeNames,
    EightBitStream,
    EncodedStreamFactory,
    HeaderCollection,
    MailBnfHelper,
    MediaTypeNames,
    MimeBasePart,
    MimeMultiPart,
    MimePart,
    MimeWriter,
    MultiAsyncResult,
    QEncodedStream,
    QuotedPrintableStream,
    SmtpDateTime,
    WriteStateInfoBase,
    IEncodableStream,
    ContentTransferEncoding,
    MimeMultiPartType,
    TransferEncoding,
]
