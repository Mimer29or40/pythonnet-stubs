from __future__ import annotations

from abc import ABC
from typing import ClassVar
from typing import Final
from typing import Iterator
from typing import Tuple
from typing import overload

from System import Array
from System import Char
from System import DateTime
from System import Decimal
from System import Enum
from System import Guid
from System import IDisposable
from System import IEquatable
from System import Object
from System import Type
from System import ValueType
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections.Generic import IEnumerable
from System.Collections.Immutable import ImmutableArray
from System.IO import Stream

class BlobContentId(ValueType, IEquatable[BlobContentId]):
    """"""

    @overload
    def __init__(self, id: ImmutableArray[int]):
        """

        :param id:
        """
    @overload
    def __init__(self, id: Array[int]):
        """

        :param id:
        """
    @overload
    def __init__(self, guid: Guid, stamp: int):
        """

        :param guid:
        :param stamp:
        """
    @property
    def Guid(self) -> Guid:
        """

        :return:
        """
    @property
    def IsDefault(self) -> bool:
        """

        :return:
        """
    @property
    def Stamp(self) -> int:
        """

        :return:
        """
    @overload
    def Equals(self, other: BlobContentId) -> bool:
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
    def ToString(self) -> str:
        """

        :return:
        """
    def __eq__(self, other: BlobContentId) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: BlobContentId) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: BlobContentId, right: BlobContentId) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: BlobContentId, right: BlobContentId) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

class BlobHandle(ValueType, IEquatable[BlobHandle]):
    """"""

    @property
    def IsNil(self) -> bool:
        """

        :return:
        """
    @overload
    def Equals(self, other: BlobHandle) -> bool:
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
    def ToString(self) -> str:
        """

        :return:
        """

class BlobReader(ValueType):
    """"""

    def __init__(self, buffer: int, length: int):
        """

        :param buffer:
        :param length:
        """
    @property
    def CurrentPointer(self) -> int:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Offset(self) -> int:
        """

        :return:
        """
    @Offset.setter
    def Offset(self, value: int) -> None: ...
    @property
    def RemainingBytes(self) -> int:
        """

        :return:
        """
    @property
    def StartPointer(self) -> int:
        """

        :return:
        """
    def Align(self, alignment: int) -> None:
        """

        :param alignment:
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
    def IndexOf(self, value: int) -> int:
        """

        :param value:
        :return:
        """
    def ReadBlobHandle(self) -> BlobHandle:
        """

        :return:
        """
    def ReadBoolean(self) -> bool:
        """

        :return:
        """
    def ReadByte(self) -> int:
        """

        :return:
        """
    @overload
    def ReadBytes(self, byteCount: int) -> Array[int]:
        """

        :param byteCount:
        :return:
        """
    @overload
    def ReadBytes(self, byteCount: int, buffer: Array[int], bufferOffset: int) -> None:
        """

        :param byteCount:
        :param buffer:
        :param bufferOffset:
        """
    def ReadChar(self) -> Char:
        """

        :return:
        """
    def ReadCompressedInteger(self) -> int:
        """

        :return:
        """
    def ReadCompressedSignedInteger(self) -> int:
        """

        :return:
        """
    def ReadDateTime(self) -> DateTime:
        """

        :return:
        """
    def ReadDecimal(self) -> Decimal:
        """

        :return:
        """
    def ReadDouble(self) -> float:
        """

        :return:
        """
    def ReadGuid(self) -> Guid:
        """

        :return:
        """
    def ReadInt16(self) -> int:
        """

        :return:
        """
    def ReadInt32(self) -> int:
        """

        :return:
        """
    def ReadInt64(self) -> int:
        """

        :return:
        """
    def ReadSByte(self) -> int:
        """

        :return:
        """
    def ReadSingle(self) -> float:
        """

        :return:
        """
    def ReadUInt16(self) -> int:
        """

        :return:
        """
    def ReadUInt32(self) -> int:
        """

        :return:
        """
    def ReadUInt64(self) -> int:
        """

        :return:
        """
    def ReadUTF16(self, byteCount: int) -> str:
        """

        :param byteCount:
        :return:
        """
    def ReadUTF8(self, byteCount: int) -> str:
        """

        :param byteCount:
        :return:
        """
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """
    def TryReadCompressedInteger(self, value: int) -> Tuple[bool, int]:
        """

        :param value:
        :return:
        """
    def TryReadCompressedSignedInteger(self, value: int) -> Tuple[bool, int]:
        """

        :param value:
        :return:
        """

class DebugMetadataHeader(Object):
    """"""

    @property
    def EntryPoint(self) -> MethodDefinitionHandle:
        """

        :return:
        """
    @property
    def Id(self) -> ImmutableArray[int]:
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

class Document(ValueType):
    """"""

    @property
    def Name(self) -> DocumentNameBlobHandle:
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

class DocumentHandle(ValueType, IEquatable[DocumentHandle]):
    """"""

    @property
    def IsNil(self) -> bool:
        """

        :return:
        """
    @overload
    def Equals(self, other: DocumentHandle) -> bool:
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
    def ToString(self) -> str:
        """

        :return:
        """
    def __eq__(self, other: DocumentHandle) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: DocumentHandle) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: DocumentHandle, right: DocumentHandle) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: DocumentHandle, right: DocumentHandle) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

class DocumentNameBlobHandle(ValueType, IEquatable[DocumentNameBlobHandle]):
    """"""

    @property
    def IsNil(self) -> bool:
        """

        :return:
        """
    @overload
    def Equals(self, other: DocumentNameBlobHandle) -> bool:
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
    def ToString(self) -> str:
        """

        :return:
        """
    def __eq__(self, other: DocumentNameBlobHandle) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: DocumentNameBlobHandle) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: DocumentNameBlobHandle, right: DocumentNameBlobHandle) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Explicit(cls, handle: BlobHandle) -> DocumentNameBlobHandle:
        """

        :param handle:
        :return:
        """
    @classmethod
    def op_Implicit(cls, handle: DocumentNameBlobHandle) -> BlobHandle:
        """

        :param handle:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: DocumentNameBlobHandle, right: DocumentNameBlobHandle) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

class Handle(ValueType, IEquatable[Handle]):
    """"""

    @property
    def IsNil(self) -> bool:
        """

        :return:
        """
    @property
    def Kind(self) -> HandleKind:
        """

        :return:
        """
    @overload
    def Equals(self, other: Handle) -> bool:
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
    def ToString(self) -> str:
        """

        :return:
        """
    def __eq__(self, other: Handle) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: Handle) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: Handle, right: Handle) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: Handle, right: Handle) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

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

    def __init__(self, metadata: int, length: int, options: MetadataReaderOptions):
        """

        :param metadata:
        :param length:
        :param options:
        """
    @property
    def DebugMetadataHeader(self) -> DebugMetadataHeader:
        """

        :return:
        """
    @property
    def MetadataVersion(self) -> str:
        """

        :return:
        """
    @property
    def Options(self) -> MetadataReaderOptions:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetDocument(self, handle: DocumentHandle) -> Document:
        """

        :param handle:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetMethodDebugInformation(
        self, handle: MethodDebugInformationHandle
    ) -> MethodDebugInformation:
        """

        :param handle:
        :return:
        """
    def GetString(self, handle: DocumentNameBlobHandle) -> str:
        """

        :param handle:
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
        """

        :param obj:
        :return:
        """
    @classmethod
    @overload
    def FromMetadataImage(cls, image: ImmutableArray[int]) -> MetadataReaderProvider:
        """

        :param image:
        :return:
        """
    @classmethod
    @overload
    def FromMetadataImage(cls, start: int, size: int) -> MetadataReaderProvider:
        """

        :param start:
        :param size:
        :return:
        """
    @classmethod
    def FromMetadataStream(
        cls, stream: Stream, options: MetadataStreamOptions = ..., size: int = ...
    ) -> MetadataReaderProvider:
        """

        :param stream:
        :param options:
        :param size:
        :return:
        """
    @classmethod
    @overload
    def FromPortablePdbImage(cls, image: ImmutableArray[int]) -> MetadataReaderProvider:
        """

        :param image:
        :return:
        """
    @classmethod
    @overload
    def FromPortablePdbImage(cls, start: int, size: int) -> MetadataReaderProvider:
        """

        :param start:
        :param size:
        :return:
        """
    @classmethod
    def FromPortablePdbStream(
        cls, stream: Stream, options: MetadataStreamOptions = ..., size: int = ...
    ) -> MetadataReaderProvider:
        """

        :param stream:
        :param options:
        :param size:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetMetadataReader(self, options: MetadataReaderOptions = ...) -> MetadataReader:
        """

        :param options:
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
    def IsValid(cls, options: MetadataStreamOptions) -> bool:
        """

        :param options:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class MethodDebugInformation(ValueType):
    """"""

    @property
    def Document(self) -> DocumentHandle:
        """

        :return:
        """
    @property
    def SequencePointsBlob(self) -> BlobHandle:
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
    def GetSequencePoints(self) -> SequencePointCollection:
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

class MethodDebugInformationHandle(ValueType, IEquatable[MethodDebugInformationHandle]):
    """"""

    @property
    def IsNil(self) -> bool:
        """

        :return:
        """
    @overload
    def Equals(self, other: MethodDebugInformationHandle) -> bool:
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
    def ToString(self) -> str:
        """

        :return:
        """
    def __eq__(self, other: MethodDebugInformationHandle) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: MethodDebugInformationHandle) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(
        cls, left: MethodDebugInformationHandle, right: MethodDebugInformationHandle
    ) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Explicit(cls, handle: Handle) -> MethodDebugInformationHandle:
        """

        :param handle:
        :return:
        """
    @classmethod
    def op_Implicit(cls, handle: MethodDebugInformationHandle) -> Handle:
        """

        :param handle:
        :return:
        """
    @classmethod
    def op_Inequality(
        cls, left: MethodDebugInformationHandle, right: MethodDebugInformationHandle
    ) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

class MethodDefinitionHandle(ValueType, IEquatable[MethodDefinitionHandle]):
    """"""

    @property
    def IsNil(self) -> bool:
        """

        :return:
        """
    @overload
    def Equals(self, other: MethodDefinitionHandle) -> bool:
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
    def ToDebugInformationHandle(self) -> MethodDebugInformationHandle:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __eq__(self, other: MethodDefinitionHandle) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: MethodDefinitionHandle) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: MethodDefinitionHandle, right: MethodDefinitionHandle) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Explicit(cls, handle: Handle) -> MethodDefinitionHandle:
        """

        :param handle:
        :return:
        """
    @classmethod
    def op_Implicit(cls, handle: MethodDefinitionHandle) -> Handle:
        """

        :param handle:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: MethodDefinitionHandle, right: MethodDefinitionHandle) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

class PathUtilities(ABC, Object):
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

class PortablePdbVersions(ABC, Object):
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

class SequencePoint(ValueType, IEquatable[SequencePoint]):
    """"""

    HiddenLine: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @property
    def Document(self) -> DocumentHandle:
        """

        :return:
        """
    @property
    def EndColumn(self) -> int:
        """

        :return:
        """
    @property
    def EndLine(self) -> int:
        """

        :return:
        """
    @property
    def IsHidden(self) -> bool:
        """

        :return:
        """
    @property
    def Offset(self) -> int:
        """

        :return:
        """
    @property
    def StartColumn(self) -> int:
        """

        :return:
        """
    @property
    def StartLine(self) -> int:
        """

        :return:
        """
    @overload
    def Equals(self, other: SequencePoint) -> bool:
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
    def ToString(self) -> str:
        """

        :return:
        """

class SequencePointCollection(ValueType, IEnumerable[SequencePoint], IEnumerable):
    """"""

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
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[SequencePoint]:
        """

        :return:
        """
