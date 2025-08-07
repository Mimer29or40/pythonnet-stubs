"""Automatically generated stubs for C# namespace: System.Reflection.Metadata."""

from abc import ABC
from collections.abc import Iterator
from typing import ClassVar
from typing import overload

from System import Array
from System import Char
from System import DateTime
from System import Decimal
from System import Enum
from System import Guid
from System import IDisposable
from System import IEquatable
from System import Int32
from System import Object
from System import Type
from System import ValueType
from System.Collections import IEnumerable
from System.Collections.Generic import IEnumerable
from System.Collections.Immutable import ImmutableArray
from System.IO import Stream

class BlobContentId(ValueType, IEquatable[BlobContentId]):
    """"""
    @overload
    def __init__(self, guid: Guid, stamp: int) -> None:
        """"""
    @overload
    def __init__(self, id: ImmutableArray[int]) -> None:
        """"""
    @overload
    def __init__(self, id: Array[int]) -> None:
        """"""
    @property
    def Guid(self) -> Guid:
        """"""
    @property
    def IsDefault(self) -> bool:
        """"""
    @property
    def Stamp(self) -> int:
        """"""
    @overload
    def Equals(self, other: BlobContentId) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, left: BlobContentId, right: BlobContentId) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: BlobContentId, right: BlobContentId) -> bool:
        """"""
    def __eq__(self, other: BlobContentId) -> bool:
        """"""
    def __ne__(self, other: BlobContentId) -> bool:
        """"""

class BlobHandle(ValueType, IEquatable[BlobHandle]):
    """"""
    @property
    def IsNil(self) -> bool:
        """"""
    @overload
    def Equals(self, other: BlobHandle) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class BlobReader(ValueType):
    """"""
    def __init__(self, buffer: int, length: int) -> None:
        """"""
    @property
    def CurrentPointer(self) -> int:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Offset(self) -> int:
        """"""
    @Offset.setter
    def Offset(self, value: int) -> None: ...
    @property
    def RemainingBytes(self) -> int:
        """"""
    @property
    def StartPointer(self) -> int:
        """"""
    def Align(self, alignment: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IndexOf(self, value: int) -> int:
        """"""
    def ReadBlobHandle(self) -> BlobHandle:
        """"""
    def ReadBoolean(self) -> bool:
        """"""
    def ReadByte(self) -> int:
        """"""
    @overload
    def ReadBytes(self, byteCount: int) -> Array[int]:
        """"""
    @overload
    def ReadBytes(self, byteCount: int, buffer: Array[int], bufferOffset: int) -> None:
        """"""
    def ReadChar(self) -> Char:
        """"""
    def ReadCompressedInteger(self) -> int:
        """"""
    def ReadCompressedSignedInteger(self) -> int:
        """"""
    def ReadDateTime(self) -> DateTime:
        """"""
    def ReadDecimal(self) -> Decimal:
        """"""
    def ReadDouble(self) -> float:
        """"""
    def ReadGuid(self) -> Guid:
        """"""
    def ReadInt16(self) -> int:
        """"""
    def ReadInt32(self) -> int:
        """"""
    def ReadInt64(self) -> int:
        """"""
    def ReadSByte(self) -> int:
        """"""
    def ReadSingle(self) -> float:
        """"""
    def ReadUInt16(self) -> int:
        """"""
    def ReadUInt32(self) -> int:
        """"""
    def ReadUInt64(self) -> int:
        """"""
    def ReadUTF16(self, byteCount: int) -> str:
        """"""
    def ReadUTF8(self, byteCount: int) -> str:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TryReadCompressedInteger(self, value: Int32) -> tuple[bool, Int32]:
        """"""
    def TryReadCompressedSignedInteger(self, value: Int32) -> tuple[bool, Int32]:
        """"""

class DebugMetadataHeader(Object):
    """"""
    @property
    def EntryPoint(self) -> MethodDefinitionHandle:
        """"""
    @property
    def Id(self) -> ImmutableArray[int]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Document(ValueType):
    """"""
    @property
    def Name(self) -> DocumentNameBlobHandle:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DocumentHandle(ValueType, IEquatable[DocumentHandle]):
    """"""
    @property
    def IsNil(self) -> bool:
        """"""
    @overload
    def Equals(self, other: DocumentHandle) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, left: DocumentHandle, right: DocumentHandle) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: DocumentHandle, right: DocumentHandle) -> bool:
        """"""
    def __eq__(self, other: DocumentHandle) -> bool:
        """"""
    def __ne__(self, other: DocumentHandle) -> bool:
        """"""

class DocumentNameBlobHandle(ValueType, IEquatable[DocumentNameBlobHandle]):
    """"""
    @property
    def IsNil(self) -> bool:
        """"""
    @overload
    def Equals(self, other: DocumentNameBlobHandle) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, left: DocumentNameBlobHandle, right: DocumentNameBlobHandle) -> bool:
        """"""
    @classmethod
    def op_Explicit(cls, handle: BlobHandle) -> DocumentNameBlobHandle:
        """"""
    @classmethod
    def op_Implicit(cls, handle: DocumentNameBlobHandle) -> BlobHandle:
        """"""
    @classmethod
    def op_Inequality(cls, left: DocumentNameBlobHandle, right: DocumentNameBlobHandle) -> bool:
        """"""
    def __eq__(self, other: DocumentNameBlobHandle) -> bool:
        """"""
    def __ne__(self, other: DocumentNameBlobHandle) -> bool:
        """"""

class Handle(ValueType, IEquatable[Handle]):
    """"""
    @property
    def IsNil(self) -> bool:
        """"""
    @property
    def Kind(self) -> HandleKind:
        """"""
    @overload
    def Equals(self, other: Handle) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, left: Handle, right: Handle) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: Handle, right: Handle) -> bool:
        """"""
    def __eq__(self, other: Handle) -> bool:
        """"""
    def __ne__(self, other: Handle) -> bool:
        """"""

class HandleKind(Enum):
    """"""

    ModuleDefinition: HandleKind = ...
    """"""
    TypeReference: HandleKind = ...
    """"""
    TypeDefinition: HandleKind = ...
    """"""
    FieldDefinition: HandleKind = ...
    """"""
    MethodDefinition: HandleKind = ...
    """"""
    Parameter: HandleKind = ...
    """"""
    InterfaceImplementation: HandleKind = ...
    """"""
    MemberReference: HandleKind = ...
    """"""
    Constant: HandleKind = ...
    """"""
    CustomAttribute: HandleKind = ...
    """"""
    DeclarativeSecurityAttribute: HandleKind = ...
    """"""
    StandaloneSignature: HandleKind = ...
    """"""
    EventDefinition: HandleKind = ...
    """"""
    PropertyDefinition: HandleKind = ...
    """"""
    MethodImplementation: HandleKind = ...
    """"""
    ModuleReference: HandleKind = ...
    """"""
    TypeSpecification: HandleKind = ...
    """"""
    AssemblyDefinition: HandleKind = ...
    """"""
    AssemblyReference: HandleKind = ...
    """"""
    AssemblyFile: HandleKind = ...
    """"""
    ExportedType: HandleKind = ...
    """"""
    ManifestResource: HandleKind = ...
    """"""
    GenericParameter: HandleKind = ...
    """"""
    MethodSpecification: HandleKind = ...
    """"""
    GenericParameterConstraint: HandleKind = ...
    """"""
    Document: HandleKind = ...
    """"""
    MethodDebugInformation: HandleKind = ...
    """"""
    LocalScope: HandleKind = ...
    """"""
    LocalVariable: HandleKind = ...
    """"""
    LocalConstant: HandleKind = ...
    """"""
    ImportScope: HandleKind = ...
    """"""
    CustomDebugInformation: HandleKind = ...
    """"""
    UserString: HandleKind = ...
    """"""
    Blob: HandleKind = ...
    """"""
    Guid: HandleKind = ...
    """"""
    String: HandleKind = ...
    """"""
    NamespaceDefinition: HandleKind = ...
    """"""

class HandleKindExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MetadataKind(Enum):
    """"""

    Ecma335: MetadataKind = ...
    """"""
    WindowsMetadata: MetadataKind = ...
    """"""
    ManagedWindowsMetadata: MetadataKind = ...
    """"""

class MetadataReader(Object):
    """"""
    def __init__(self, metadata: int, length: int, options: MetadataReaderOptions) -> None:
        """"""
    @property
    def DebugMetadataHeader(self) -> DebugMetadataHeader:
        """"""
    @property
    def MetadataVersion(self) -> str:
        """"""
    @property
    def Options(self) -> MetadataReaderOptions:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetDocument(self, handle: DocumentHandle) -> Document:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetMethodDebugInformation(
        self, handle: MethodDebugInformationHandle
    ) -> MethodDebugInformation:
        """"""
    def GetString(self, handle: DocumentNameBlobHandle) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MetadataReaderOptions(Enum):
    """"""

    _None: MetadataReaderOptions = ...
    """"""
    Default: MetadataReaderOptions = ...
    """"""
    ApplyWindowsRuntimeProjections: MetadataReaderOptions = ...
    """"""

class MetadataReaderProvider(Object, IDisposable):
    """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    @overload
    def FromMetadataImage(cls, image: ImmutableArray[int]) -> MetadataReaderProvider:
        """"""
    @classmethod
    @overload
    def FromMetadataImage(cls, start: int, size: int) -> MetadataReaderProvider:
        """"""
    @classmethod
    def FromMetadataStream(
        cls, stream: Stream, options: MetadataStreamOptions = ..., size: int = ...
    ) -> MetadataReaderProvider:
        """"""
    @classmethod
    @overload
    def FromPortablePdbImage(cls, image: ImmutableArray[int]) -> MetadataReaderProvider:
        """"""
    @classmethod
    @overload
    def FromPortablePdbImage(cls, start: int, size: int) -> MetadataReaderProvider:
        """"""
    @classmethod
    def FromPortablePdbStream(
        cls, stream: Stream, options: MetadataStreamOptions = ..., size: int = ...
    ) -> MetadataReaderProvider:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetMetadataReader(self, options: MetadataReaderOptions = ...) -> MetadataReader:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MetadataStreamOptions(Enum):
    """"""

    Default: MetadataStreamOptions = ...
    """"""
    LeaveOpen: MetadataStreamOptions = ...
    """"""
    PrefetchMetadata: MetadataStreamOptions = ...
    """"""

class MetadataStreamOptionsExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsValid(cls, options: MetadataStreamOptions) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class MethodDebugInformation(ValueType):
    """"""
    @property
    def Document(self) -> DocumentHandle:
        """"""
    @property
    def SequencePointsBlob(self) -> BlobHandle:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetSequencePoints(self) -> SequencePointCollection:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MethodDebugInformationHandle(ValueType, IEquatable[MethodDebugInformationHandle]):
    """"""
    @property
    def IsNil(self) -> bool:
        """"""
    @overload
    def Equals(self, other: MethodDebugInformationHandle) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(
        cls, left: MethodDebugInformationHandle, right: MethodDebugInformationHandle
    ) -> bool:
        """"""
    @classmethod
    def op_Explicit(cls, handle: Handle) -> MethodDebugInformationHandle:
        """"""
    @classmethod
    def op_Implicit(cls, handle: MethodDebugInformationHandle) -> Handle:
        """"""
    @classmethod
    def op_Inequality(
        cls, left: MethodDebugInformationHandle, right: MethodDebugInformationHandle
    ) -> bool:
        """"""
    def __eq__(self, other: MethodDebugInformationHandle) -> bool:
        """"""
    def __ne__(self, other: MethodDebugInformationHandle) -> bool:
        """"""

class MethodDefinitionHandle(ValueType, IEquatable[MethodDefinitionHandle]):
    """"""
    @property
    def IsNil(self) -> bool:
        """"""
    @overload
    def Equals(self, other: MethodDefinitionHandle) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToDebugInformationHandle(self) -> MethodDebugInformationHandle:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, left: MethodDefinitionHandle, right: MethodDefinitionHandle) -> bool:
        """"""
    @classmethod
    def op_Explicit(cls, handle: Handle) -> MethodDefinitionHandle:
        """"""
    @classmethod
    def op_Implicit(cls, handle: MethodDefinitionHandle) -> Handle:
        """"""
    @classmethod
    def op_Inequality(cls, left: MethodDefinitionHandle, right: MethodDefinitionHandle) -> bool:
        """"""
    def __eq__(self, other: MethodDefinitionHandle) -> bool:
        """"""
    def __ne__(self, other: MethodDefinitionHandle) -> bool:
        """"""

class PathUtilities(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class PortablePdbVersions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SequencePoint(ValueType, IEquatable[SequencePoint]):
    """"""

    HiddenLine: ClassVar[int]
    """"""
    @property
    def Document(self) -> DocumentHandle:
        """"""
    @property
    def EndColumn(self) -> int:
        """"""
    @property
    def EndLine(self) -> int:
        """"""
    @property
    def IsHidden(self) -> bool:
        """"""
    @property
    def Offset(self) -> int:
        """"""
    @property
    def StartColumn(self) -> int:
        """"""
    @property
    def StartLine(self) -> int:
        """"""
    @overload
    def Equals(self, other: SequencePoint) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SequencePointCollection(ValueType, IEnumerable[SequencePoint], IEnumerable):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> SequencePointCollection.Enumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
