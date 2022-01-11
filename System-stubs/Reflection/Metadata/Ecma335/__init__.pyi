from __future__ import annotations

from abc import ABC
from typing import Tuple, Union

from System import Boolean, Byte, Enum, Int32, Object, String, UInt64, ValueType
from System.Reflection.Metadata import DocumentNameBlobHandle, Handle, HandleKind, MethodDebugInformationHandle, MethodDefinitionHandle

# ---------- Types ---------- #

BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
ULongType = Union[int, UInt64]


# ---------- Classes ---------- #

class COR20Constants(ABC, ObjectType):
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


class HandleType(ABC, ObjectType):
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


class HeapHandleType(ABC, ObjectType):
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


class MetadataStreamConstants(ABC, ObjectType):
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


class MetadataTokens(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def TableCount() -> IntType: ...
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetHeapOffset(handle: Handle) -> IntType: ...
    
    @staticmethod
    def GetToken(handle: Handle) -> IntType: ...
    
    @staticmethod
    def Handle(token: IntType) -> Handle: ...
    
    @staticmethod
    def MethodDebugInformationHandle(rowNumber: IntType) -> MethodDebugInformationHandle: ...
    
    @staticmethod
    def MethodDefinitionHandle(rowNumber: IntType) -> MethodDefinitionHandle: ...
    
    @staticmethod
    def TryGetTableIndex(type: HandleKind, index: TableIndex) -> Tuple[BooleanType, TableIndex]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class StringHandleType(ABC, ObjectType):
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


class TokenTypeIds(ABC, ObjectType):
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

class BlobHeap(ValueType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetDocumentName(self, handle: DocumentNameBlobHandle) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class DocumentTableReader(ValueType):
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


class MethodDebugInformationTableReader(ValueType):
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


class StreamHeader(ValueType):
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


# No Interfaces

# ---------- Enums ---------- #

class HeapSizeFlag(Enum):
    StringHeapLarge = 1
    GuidHeapLarge = 2
    BlobHeapLarge = 4
    EncDeltas = 32
    DeletedMarks = 128


class HeapSizes(Enum):
    StringHeapLarge = 1
    GuidHeapLarge = 2
    BlobHeapLarge = 4
    ExtraData = 64


class MetadataStreamKind(Enum):
    Illegal = 0
    Compressed = 1
    Uncompressed = 2


class StringKind(Enum):
    Plain = 0
    DotTerminated = 1
    Virtual = 4
    WinRTPrefixed = 5


class TableIndex(Enum):
    Module = 0
    TypeRef = 1
    TypeDef = 2
    FieldPtr = 3
    Field = 4
    MethodPtr = 5
    MethodDef = 6
    ParamPtr = 7
    Param = 8
    InterfaceImpl = 9
    MemberRef = 10
    Constant = 11
    CustomAttribute = 12
    FieldMarshal = 13
    DeclSecurity = 14
    ClassLayout = 15
    FieldLayout = 16
    StandAloneSig = 17
    EventMap = 18
    EventPtr = 19
    Event = 20
    PropertyMap = 21
    PropertyPtr = 22
    Property = 23
    MethodSemantics = 24
    MethodImpl = 25
    ModuleRef = 26
    TypeSpec = 27
    ImplMap = 28
    FieldRva = 29
    EncLog = 30
    EncMap = 31
    Assembly = 32
    AssemblyProcessor = 33
    AssemblyOS = 34
    AssemblyRef = 35
    AssemblyRefProcessor = 36
    AssemblyRefOS = 37
    File = 38
    ExportedType = 39
    ManifestResource = 40
    NestedClass = 41
    GenericParam = 42
    MethodSpec = 43
    GenericParamConstraint = 44
    Document = 48
    MethodDebugInformation = 49
    LocalScope = 50
    LocalVariable = 51
    LocalConstant = 52
    ImportScope = 53
    StateMachineMethod = 54
    CustomDebugInformation = 55


class TableMask(Enum):
    Module = 1
    TypeRef = 2
    TypeDef = 4
    FieldPtr = 8
    Field = 16
    MethodPtr = 32
    MethodDef = 64
    ParamPtr = 128
    Param = 256
    InterfaceImpl = 512
    MemberRef = 1024
    Constant = 2048
    CustomAttribute = 4096
    FieldMarshal = 8192
    DeclSecurity = 16384
    ClassLayout = 32768
    FieldLayout = 65536
    StandAloneSig = 131072
    EventMap = 262144
    EventPtr = 524288
    Event = 1048576
    PropertyMap = 2097152
    PropertyPtr = 4194304
    PtrTables = 4718760
    Property = 8388608
    MethodSemantics = 16777216
    MethodImpl = 33554432
    ModuleRef = 67108864
    TypeSpec = 134217728
    ImplMap = 268435456
    FieldRva = 536870912
    EnCLog = 1073741824
    EnCMap = 2147483648
    EncTables = 3221225472
    Assembly = 4294967296
    AssemblyRef = 34359738368
    File = 274877906944
    ExportedType = 549755813888
    ManifestResource = 1099511627776
    NestedClass = 2199023255552
    GenericParam = 4398046511104
    MethodSpec = 8796093022208
    GenericParamConstraint = 17592186044416
    ValidPortablePdbExternalTables = 34949217910615
    TypeSystemTables = 34952443854847
    Document = 281474976710656
    MethodDebugInformation = 562949953421312
    LocalScope = 1125899906842624
    LocalVariable = 2251799813685248
    LocalConstant = 4503599627370496
    ImportScope = 9007199254740992
    StateMachineMethod = 18014398509481984
    CustomDebugInformation = 36028797018963968
    DebugTables = 71776119061217280
    AllTables = 71811071505072127


# No Delegates

__all__ = [
    COR20Constants,
    HandleType,
    HeapHandleType,
    MetadataStreamConstants,
    MetadataTokens,
    StringHandleType,
    TokenTypeIds,
    BlobHeap,
    DocumentTableReader,
    MethodDebugInformationTableReader,
    StreamHeader,
    HeapSizeFlag,
    HeapSizes,
    MetadataStreamKind,
    StringKind,
    TableIndex,
    TableMask,
]
