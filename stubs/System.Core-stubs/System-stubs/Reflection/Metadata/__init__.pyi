from __future__ import annotations

from abc import ABC
from typing import List, Tuple, Union, overload

from System import Array, Boolean, Byte, Char, DateTime, Decimal, Double, Enum, Guid, IDisposable, IEquatable, Int16, Int32, Int64, Object, SByte, Single, String, UInt16, UInt32, UInt64, ValueType, Void
from System.Collections import IEnumerable
from System.Collections.Generic import IEnumerable
from System.Collections.Immutable import ImmutableArray
from System.IO import Stream

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
CharType = Union[str, Char]
DecimalType = Union[float, Decimal]
DoubleType = Union[float, Double]
FloatType = Union[float, Single]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
ObjectType = Object
SByteType = Union[int, SByte]
ShortType = Union[int, Int16]
StringType = Union[str, String]
UIntType = Union[int, UInt32]
ULongType = Union[int, UInt64]
UShortType = Union[int, UInt16]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class DebugMetadataHeader(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def EntryPoint(self) -> MethodDefinitionHandle: ...
    
    @property
    def Id(self) -> ImmutableArray[ByteType]: ...
    
    # ---------- Methods ---------- #
    
    def get_EntryPoint(self) -> MethodDefinitionHandle: ...
    
    def get_Id(self) -> ImmutableArray[ByteType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DebugMetadataHeader(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def EntryPoint(self) -> MethodDefinitionHandle: ...
    
    @property
    def Id(self) -> ImmutableArray[ByteType]: ...
    
    # ---------- Methods ---------- #
    
    def get_EntryPoint(self) -> MethodDefinitionHandle: ...
    
    def get_Id(self) -> ImmutableArray[ByteType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HandleKindExtensions(ABC, ObjectType):
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


class HandleKindExtensions(ABC, ObjectType):
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


class MetadataReader(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, metadata: ByteType, length: IntType, options: MetadataReaderOptions): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DebugMetadataHeader(self) -> DebugMetadataHeader: ...
    
    @property
    def MetadataVersion(self) -> StringType: ...
    
    @property
    def Options(self) -> MetadataReaderOptions: ...
    
    # ---------- Methods ---------- #
    
    def GetDocument(self, handle: DocumentHandle) -> Document: ...
    
    def GetMethodDebugInformation(self, handle: MethodDebugInformationHandle) -> MethodDebugInformation: ...
    
    def GetString(self, handle: DocumentNameBlobHandle) -> StringType: ...
    
    def get_DebugMetadataHeader(self) -> DebugMetadataHeader: ...
    
    def get_MetadataVersion(self) -> StringType: ...
    
    def get_Options(self) -> MetadataReaderOptions: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MetadataReader(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, metadata: ByteType, length: IntType, options: MetadataReaderOptions): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DebugMetadataHeader(self) -> DebugMetadataHeader: ...
    
    @property
    def MetadataVersion(self) -> StringType: ...
    
    @property
    def Options(self) -> MetadataReaderOptions: ...
    
    # ---------- Methods ---------- #
    
    def GetDocument(self, handle: DocumentHandle) -> Document: ...
    
    def GetMethodDebugInformation(self, handle: MethodDebugInformationHandle) -> MethodDebugInformation: ...
    
    def GetString(self, handle: DocumentNameBlobHandle) -> StringType: ...
    
    def get_DebugMetadataHeader(self) -> DebugMetadataHeader: ...
    
    def get_MetadataVersion(self) -> StringType: ...
    
    def get_Options(self) -> MetadataReaderOptions: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MetadataReaderProvider(ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    @staticmethod
    @overload
    def FromMetadataImage(start: ByteType, size: IntType) -> MetadataReaderProvider: ...
    
    @staticmethod
    @overload
    def FromMetadataImage(image: ImmutableArray[ByteType]) -> MetadataReaderProvider: ...
    
    @staticmethod
    def FromMetadataStream(stream: Stream, options: MetadataStreamOptions, size: IntType) -> MetadataReaderProvider: ...
    
    @staticmethod
    @overload
    def FromPortablePdbImage(start: ByteType, size: IntType) -> MetadataReaderProvider: ...
    
    @staticmethod
    @overload
    def FromPortablePdbImage(image: ImmutableArray[ByteType]) -> MetadataReaderProvider: ...
    
    @staticmethod
    def FromPortablePdbStream(stream: Stream, options: MetadataStreamOptions, size: IntType) -> MetadataReaderProvider: ...
    
    def GetMetadataReader(self, options: MetadataReaderOptions = 1) -> MetadataReader: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MetadataReaderProvider(ObjectType, IDisposable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    @staticmethod
    @overload
    def FromMetadataImage(start: ByteType, size: IntType) -> MetadataReaderProvider: ...
    
    @staticmethod
    @overload
    def FromMetadataImage(image: ImmutableArray[ByteType]) -> MetadataReaderProvider: ...
    
    @staticmethod
    def FromMetadataStream(stream: Stream, options: MetadataStreamOptions, size: IntType) -> MetadataReaderProvider: ...
    
    @staticmethod
    @overload
    def FromPortablePdbImage(start: ByteType, size: IntType) -> MetadataReaderProvider: ...
    
    @staticmethod
    @overload
    def FromPortablePdbImage(image: ImmutableArray[ByteType]) -> MetadataReaderProvider: ...
    
    @staticmethod
    def FromPortablePdbStream(stream: Stream, options: MetadataStreamOptions, size: IntType) -> MetadataReaderProvider: ...
    
    def GetMetadataReader(self, options: MetadataReaderOptions = 1) -> MetadataReader: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MetadataStreamOptionsExtensions(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def IsValid(options: MetadataStreamOptions) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MetadataStreamOptionsExtensions(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def IsValid(options: MetadataStreamOptions) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PathUtilities(ABC, ObjectType):
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


class PathUtilities(ABC, ObjectType):
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


class PortablePdbVersions(ABC, ObjectType):
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


class PortablePdbVersions(ABC, ObjectType):
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

class BlobContentId(ValueType, IEquatable[BlobContentId]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, guid: Guid, stamp: UIntType): ...
    
    @overload
    def __init__(self, id: ImmutableArray[ByteType]): ...
    
    @overload
    def __init__(self, id: ArrayType[ByteType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Guid(self) -> Guid: ...
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def Stamp(self) -> UIntType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, other: BlobContentId) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Guid(self) -> Guid: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_Stamp(self) -> UIntType: ...
    
    @staticmethod
    def op_Equality(left: BlobContentId, right: BlobContentId) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: BlobContentId, right: BlobContentId) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BlobContentId(ValueType, IEquatable[BlobContentId]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, guid: Guid, stamp: UIntType): ...
    
    @overload
    def __init__(self, id: ImmutableArray[ByteType]): ...
    
    @overload
    def __init__(self, id: ArrayType[ByteType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Guid(self) -> Guid: ...
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def Stamp(self) -> UIntType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, other: BlobContentId) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Guid(self) -> Guid: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_Stamp(self) -> UIntType: ...
    
    @staticmethod
    def op_Equality(left: BlobContentId, right: BlobContentId) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: BlobContentId, right: BlobContentId) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BlobHandle(ValueType, IEquatable[BlobHandle]):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsNil(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: BlobHandle) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_IsNil(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BlobHandle(ValueType, IEquatable[BlobHandle]):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsNil(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: BlobHandle) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_IsNil(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BlobReader(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, buffer: ByteType, length: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CurrentPointer(self) -> ByteType: ...
    
    @property
    def Length(self) -> IntType: ...
    
    @property
    def Offset(self) -> IntType: ...
    
    @Offset.setter
    def Offset(self, value: IntType) -> None: ...
    
    @property
    def RemainingBytes(self) -> IntType: ...
    
    @property
    def StartPointer(self) -> ByteType: ...
    
    # ---------- Methods ---------- #
    
    def Align(self, alignment: ByteType) -> VoidType: ...
    
    def IndexOf(self, value: ByteType) -> IntType: ...
    
    def ReadBlobHandle(self) -> BlobHandle: ...
    
    def ReadBoolean(self) -> BooleanType: ...
    
    def ReadByte(self) -> ByteType: ...
    
    @overload
    def ReadBytes(self, byteCount: IntType) -> ArrayType[ByteType]: ...
    
    @overload
    def ReadBytes(self, byteCount: IntType, buffer: ArrayType[ByteType], bufferOffset: IntType) -> VoidType: ...
    
    def ReadChar(self) -> CharType: ...
    
    def ReadCompressedInteger(self) -> IntType: ...
    
    def ReadCompressedSignedInteger(self) -> IntType: ...
    
    def ReadDateTime(self) -> DateTime: ...
    
    def ReadDecimal(self) -> DecimalType: ...
    
    def ReadDouble(self) -> DoubleType: ...
    
    def ReadGuid(self) -> Guid: ...
    
    def ReadInt16(self) -> ShortType: ...
    
    def ReadInt32(self) -> IntType: ...
    
    def ReadInt64(self) -> LongType: ...
    
    def ReadSByte(self) -> SByteType: ...
    
    def ReadSingle(self) -> FloatType: ...
    
    def ReadUInt16(self) -> UShortType: ...
    
    def ReadUInt32(self) -> UIntType: ...
    
    def ReadUInt64(self) -> ULongType: ...
    
    def ReadUTF16(self, byteCount: IntType) -> StringType: ...
    
    def ReadUTF8(self, byteCount: IntType) -> StringType: ...
    
    def Reset(self) -> VoidType: ...
    
    def TryReadCompressedInteger(self, value: IntType) -> Tuple[BooleanType, IntType]: ...
    
    def TryReadCompressedSignedInteger(self, value: IntType) -> Tuple[BooleanType, IntType]: ...
    
    def get_CurrentPointer(self) -> ByteType: ...
    
    def get_Length(self) -> IntType: ...
    
    def get_Offset(self) -> IntType: ...
    
    def get_RemainingBytes(self) -> IntType: ...
    
    def get_StartPointer(self) -> ByteType: ...
    
    def set_Offset(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class BlobReader(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, buffer: ByteType, length: IntType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CurrentPointer(self) -> ByteType: ...
    
    @property
    def Length(self) -> IntType: ...
    
    @property
    def Offset(self) -> IntType: ...
    
    @Offset.setter
    def Offset(self, value: IntType) -> None: ...
    
    @property
    def RemainingBytes(self) -> IntType: ...
    
    @property
    def StartPointer(self) -> ByteType: ...
    
    # ---------- Methods ---------- #
    
    def Align(self, alignment: ByteType) -> VoidType: ...
    
    def IndexOf(self, value: ByteType) -> IntType: ...
    
    def ReadBlobHandle(self) -> BlobHandle: ...
    
    def ReadBoolean(self) -> BooleanType: ...
    
    def ReadByte(self) -> ByteType: ...
    
    @overload
    def ReadBytes(self, byteCount: IntType) -> ArrayType[ByteType]: ...
    
    @overload
    def ReadBytes(self, byteCount: IntType, buffer: ArrayType[ByteType], bufferOffset: IntType) -> VoidType: ...
    
    def ReadChar(self) -> CharType: ...
    
    def ReadCompressedInteger(self) -> IntType: ...
    
    def ReadCompressedSignedInteger(self) -> IntType: ...
    
    def ReadDateTime(self) -> DateTime: ...
    
    def ReadDecimal(self) -> DecimalType: ...
    
    def ReadDouble(self) -> DoubleType: ...
    
    def ReadGuid(self) -> Guid: ...
    
    def ReadInt16(self) -> ShortType: ...
    
    def ReadInt32(self) -> IntType: ...
    
    def ReadInt64(self) -> LongType: ...
    
    def ReadSByte(self) -> SByteType: ...
    
    def ReadSingle(self) -> FloatType: ...
    
    def ReadUInt16(self) -> UShortType: ...
    
    def ReadUInt32(self) -> UIntType: ...
    
    def ReadUInt64(self) -> ULongType: ...
    
    def ReadUTF16(self, byteCount: IntType) -> StringType: ...
    
    def ReadUTF8(self, byteCount: IntType) -> StringType: ...
    
    def Reset(self) -> VoidType: ...
    
    def TryReadCompressedInteger(self, value: IntType) -> Tuple[BooleanType, IntType]: ...
    
    def TryReadCompressedSignedInteger(self, value: IntType) -> Tuple[BooleanType, IntType]: ...
    
    def get_CurrentPointer(self) -> ByteType: ...
    
    def get_Length(self) -> IntType: ...
    
    def get_Offset(self) -> IntType: ...
    
    def get_RemainingBytes(self) -> IntType: ...
    
    def get_StartPointer(self) -> ByteType: ...
    
    def set_Offset(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Document(ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> DocumentNameBlobHandle: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> DocumentNameBlobHandle: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Document(ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> DocumentNameBlobHandle: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> DocumentNameBlobHandle: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DocumentHandle(ValueType, IEquatable[DocumentHandle]):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsNil(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: DocumentHandle) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_IsNil(self) -> BooleanType: ...
    
    @staticmethod
    def op_Equality(left: DocumentHandle, right: DocumentHandle) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: DocumentHandle, right: DocumentHandle) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DocumentHandle(ValueType, IEquatable[DocumentHandle]):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsNil(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: DocumentHandle) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_IsNil(self) -> BooleanType: ...
    
    @staticmethod
    def op_Equality(left: DocumentHandle, right: DocumentHandle) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: DocumentHandle, right: DocumentHandle) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DocumentNameBlobHandle(ValueType, IEquatable[DocumentNameBlobHandle]):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsNil(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: DocumentNameBlobHandle) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_IsNil(self) -> BooleanType: ...
    
    @staticmethod
    def op_Equality(left: DocumentNameBlobHandle, right: DocumentNameBlobHandle) -> BooleanType: ...
    
    @staticmethod
    def op_Explicit(handle: BlobHandle) -> DocumentNameBlobHandle: ...
    
    @staticmethod
    def op_Implicit(handle: DocumentNameBlobHandle) -> BlobHandle: ...
    
    @staticmethod
    def op_Inequality(left: DocumentNameBlobHandle, right: DocumentNameBlobHandle) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DocumentNameBlobHandle(ValueType, IEquatable[DocumentNameBlobHandle]):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsNil(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: DocumentNameBlobHandle) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_IsNil(self) -> BooleanType: ...
    
    @staticmethod
    def op_Equality(left: DocumentNameBlobHandle, right: DocumentNameBlobHandle) -> BooleanType: ...
    
    @staticmethod
    def op_Explicit(handle: BlobHandle) -> DocumentNameBlobHandle: ...
    
    @staticmethod
    def op_Implicit(handle: DocumentNameBlobHandle) -> BlobHandle: ...
    
    @staticmethod
    def op_Inequality(left: DocumentNameBlobHandle, right: DocumentNameBlobHandle) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Handle(ValueType, IEquatable[Handle]):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsNil(self) -> BooleanType: ...
    
    @property
    def Kind(self) -> HandleKind: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: Handle) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_IsNil(self) -> BooleanType: ...
    
    def get_Kind(self) -> HandleKind: ...
    
    @staticmethod
    def op_Equality(left: Handle, right: Handle) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: Handle, right: Handle) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Handle(ValueType, IEquatable[Handle]):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsNil(self) -> BooleanType: ...
    
    @property
    def Kind(self) -> HandleKind: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: Handle) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_IsNil(self) -> BooleanType: ...
    
    def get_Kind(self) -> HandleKind: ...
    
    @staticmethod
    def op_Equality(left: Handle, right: Handle) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(left: Handle, right: Handle) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MethodDebugInformation(ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Document(self) -> DocumentHandle: ...
    
    @property
    def SequencePointsBlob(self) -> BlobHandle: ...
    
    # ---------- Methods ---------- #
    
    def GetSequencePoints(self) -> SequencePointCollection: ...
    
    def get_Document(self) -> DocumentHandle: ...
    
    def get_SequencePointsBlob(self) -> BlobHandle: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MethodDebugInformation(ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Document(self) -> DocumentHandle: ...
    
    @property
    def SequencePointsBlob(self) -> BlobHandle: ...
    
    # ---------- Methods ---------- #
    
    def GetSequencePoints(self) -> SequencePointCollection: ...
    
    def get_Document(self) -> DocumentHandle: ...
    
    def get_SequencePointsBlob(self) -> BlobHandle: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MethodDebugInformationHandle(ValueType, IEquatable[MethodDebugInformationHandle]):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsNil(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: MethodDebugInformationHandle) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_IsNil(self) -> BooleanType: ...
    
    @staticmethod
    def op_Equality(left: MethodDebugInformationHandle, right: MethodDebugInformationHandle) -> BooleanType: ...
    
    @staticmethod
    def op_Explicit(handle: Handle) -> MethodDebugInformationHandle: ...
    
    @staticmethod
    def op_Implicit(handle: MethodDebugInformationHandle) -> Handle: ...
    
    @staticmethod
    def op_Inequality(left: MethodDebugInformationHandle, right: MethodDebugInformationHandle) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MethodDebugInformationHandle(ValueType, IEquatable[MethodDebugInformationHandle]):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsNil(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: MethodDebugInformationHandle) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_IsNil(self) -> BooleanType: ...
    
    @staticmethod
    def op_Equality(left: MethodDebugInformationHandle, right: MethodDebugInformationHandle) -> BooleanType: ...
    
    @staticmethod
    def op_Explicit(handle: Handle) -> MethodDebugInformationHandle: ...
    
    @staticmethod
    def op_Implicit(handle: MethodDebugInformationHandle) -> Handle: ...
    
    @staticmethod
    def op_Inequality(left: MethodDebugInformationHandle, right: MethodDebugInformationHandle) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MethodDefinitionHandle(ValueType, IEquatable[MethodDefinitionHandle]):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsNil(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: MethodDefinitionHandle) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToDebugInformationHandle(self) -> MethodDebugInformationHandle: ...
    
    def get_IsNil(self) -> BooleanType: ...
    
    @staticmethod
    def op_Equality(left: MethodDefinitionHandle, right: MethodDefinitionHandle) -> BooleanType: ...
    
    @staticmethod
    def op_Explicit(handle: Handle) -> MethodDefinitionHandle: ...
    
    @staticmethod
    def op_Implicit(handle: MethodDefinitionHandle) -> Handle: ...
    
    @staticmethod
    def op_Inequality(left: MethodDefinitionHandle, right: MethodDefinitionHandle) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MethodDefinitionHandle(ValueType, IEquatable[MethodDefinitionHandle]):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IsNil(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: MethodDefinitionHandle) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def ToDebugInformationHandle(self) -> MethodDebugInformationHandle: ...
    
    def get_IsNil(self) -> BooleanType: ...
    
    @staticmethod
    def op_Equality(left: MethodDefinitionHandle, right: MethodDefinitionHandle) -> BooleanType: ...
    
    @staticmethod
    def op_Explicit(handle: Handle) -> MethodDefinitionHandle: ...
    
    @staticmethod
    def op_Implicit(handle: MethodDefinitionHandle) -> Handle: ...
    
    @staticmethod
    def op_Inequality(left: MethodDefinitionHandle, right: MethodDefinitionHandle) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SequencePoint(ValueType, IEquatable[SequencePoint]):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def HiddenLine() -> IntType: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Document(self) -> DocumentHandle: ...
    
    @property
    def EndColumn(self) -> IntType: ...
    
    @property
    def EndLine(self) -> IntType: ...
    
    @property
    def IsHidden(self) -> BooleanType: ...
    
    @property
    def Offset(self) -> IntType: ...
    
    @property
    def StartColumn(self) -> IntType: ...
    
    @property
    def StartLine(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: SequencePoint) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Document(self) -> DocumentHandle: ...
    
    def get_EndColumn(self) -> IntType: ...
    
    def get_EndLine(self) -> IntType: ...
    
    def get_IsHidden(self) -> BooleanType: ...
    
    def get_Offset(self) -> IntType: ...
    
    def get_StartColumn(self) -> IntType: ...
    
    def get_StartLine(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SequencePoint(ValueType, IEquatable[SequencePoint]):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def HiddenLine() -> IntType: ...
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Document(self) -> DocumentHandle: ...
    
    @property
    def EndColumn(self) -> IntType: ...
    
    @property
    def EndLine(self) -> IntType: ...
    
    @property
    def IsHidden(self) -> BooleanType: ...
    
    @property
    def Offset(self) -> IntType: ...
    
    @property
    def StartColumn(self) -> IntType: ...
    
    @property
    def StartLine(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, other: SequencePoint) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def get_Document(self) -> DocumentHandle: ...
    
    def get_EndColumn(self) -> IntType: ...
    
    def get_EndLine(self) -> IntType: ...
    
    def get_IsHidden(self) -> BooleanType: ...
    
    def get_Offset(self) -> IntType: ...
    
    def get_StartColumn(self) -> IntType: ...
    
    def get_StartLine(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SequencePointCollection(ValueType, IEnumerable[SequencePoint], IEnumerable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetEnumerator(self) -> Enumerator: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SequencePointCollection(ValueType, IEnumerable[SequencePoint], IEnumerable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetEnumerator(self) -> Enumerator: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Interfaces

# ---------- Enums ---------- #

class HandleKind(Enum):
    ModuleDefinition: ByteType = 0
    TypeReference: ByteType = 1
    TypeDefinition: ByteType = 2
    FieldDefinition: ByteType = 4
    MethodDefinition: ByteType = 6
    Parameter: ByteType = 8
    InterfaceImplementation: ByteType = 9
    MemberReference: ByteType = 10
    Constant: ByteType = 11
    CustomAttribute: ByteType = 12
    DeclarativeSecurityAttribute: ByteType = 14
    StandaloneSignature: ByteType = 17
    EventDefinition: ByteType = 20
    PropertyDefinition: ByteType = 23
    MethodImplementation: ByteType = 25
    ModuleReference: ByteType = 26
    TypeSpecification: ByteType = 27
    AssemblyDefinition: ByteType = 32
    AssemblyReference: ByteType = 35
    AssemblyFile: ByteType = 38
    ExportedType: ByteType = 39
    ManifestResource: ByteType = 40
    GenericParameter: ByteType = 42
    MethodSpecification: ByteType = 43
    GenericParameterConstraint: ByteType = 44
    Document: ByteType = 48
    MethodDebugInformation: ByteType = 49
    LocalScope: ByteType = 50
    LocalVariable: ByteType = 51
    LocalConstant: ByteType = 52
    ImportScope: ByteType = 53
    CustomDebugInformation: ByteType = 55
    UserString: ByteType = 112
    Blob: ByteType = 113
    Guid: ByteType = 114
    String: ByteType = 120
    NamespaceDefinition: ByteType = 124


class HandleKind(Enum):
    ModuleDefinition: ByteType = 0
    TypeReference: ByteType = 1
    TypeDefinition: ByteType = 2
    FieldDefinition: ByteType = 4
    MethodDefinition: ByteType = 6
    Parameter: ByteType = 8
    InterfaceImplementation: ByteType = 9
    MemberReference: ByteType = 10
    Constant: ByteType = 11
    CustomAttribute: ByteType = 12
    DeclarativeSecurityAttribute: ByteType = 14
    StandaloneSignature: ByteType = 17
    EventDefinition: ByteType = 20
    PropertyDefinition: ByteType = 23
    MethodImplementation: ByteType = 25
    ModuleReference: ByteType = 26
    TypeSpecification: ByteType = 27
    AssemblyDefinition: ByteType = 32
    AssemblyReference: ByteType = 35
    AssemblyFile: ByteType = 38
    ExportedType: ByteType = 39
    ManifestResource: ByteType = 40
    GenericParameter: ByteType = 42
    MethodSpecification: ByteType = 43
    GenericParameterConstraint: ByteType = 44
    Document: ByteType = 48
    MethodDebugInformation: ByteType = 49
    LocalScope: ByteType = 50
    LocalVariable: ByteType = 51
    LocalConstant: ByteType = 52
    ImportScope: ByteType = 53
    CustomDebugInformation: ByteType = 55
    UserString: ByteType = 112
    Blob: ByteType = 113
    Guid: ByteType = 114
    String: ByteType = 120
    NamespaceDefinition: ByteType = 124


class MetadataKind(Enum):
    Ecma335: IntType = 0
    WindowsMetadata: IntType = 1
    ManagedWindowsMetadata: IntType = 2


class MetadataKind(Enum):
    Ecma335: IntType = 0
    WindowsMetadata: IntType = 1
    ManagedWindowsMetadata: IntType = 2


class MetadataReaderOptions(Enum):
    #None: IntType = 0
    Default: IntType = 1
    ApplyWindowsRuntimeProjections: IntType = 1


class MetadataReaderOptions(Enum):
    #None: IntType = 0
    Default: IntType = 1
    ApplyWindowsRuntimeProjections: IntType = 1


class MetadataStreamOptions(Enum):
    Default: IntType = 0
    LeaveOpen: IntType = 1
    PrefetchMetadata: IntType = 2


class MetadataStreamOptions(Enum):
    Default: IntType = 0
    LeaveOpen: IntType = 1
    PrefetchMetadata: IntType = 2


# No Delegates

__all__ = [
    DebugMetadataHeader,
    HandleKindExtensions,
    MetadataReader,
    MetadataReaderProvider,
    MetadataStreamOptionsExtensions,
    PathUtilities,
    PortablePdbVersions,
    BlobContentId,
    BlobHandle,
    BlobReader,
    Document,
    DocumentHandle,
    DocumentNameBlobHandle,
    Handle,
    MethodDebugInformation,
    MethodDebugInformationHandle,
    MethodDefinitionHandle,
    SequencePoint,
    SequencePointCollection,
    HandleKind,
    MetadataKind,
    MetadataReaderOptions,
    MetadataStreamOptions,
]
