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
    StringHeapLarge: ByteType = 1
    GuidHeapLarge: ByteType = 2
    BlobHeapLarge: ByteType = 4
    EncDeltas: ByteType = 32
    DeletedMarks: ByteType = 128


class HeapSizeFlag(Enum):
    StringHeapLarge: ByteType = 1
    GuidHeapLarge: ByteType = 2
    BlobHeapLarge: ByteType = 4
    EncDeltas: ByteType = 32
    DeletedMarks: ByteType = 128


class HeapSizes(Enum):
    StringHeapLarge: ByteType = 1
    GuidHeapLarge: ByteType = 2
    BlobHeapLarge: ByteType = 4
    ExtraData: ByteType = 64


class HeapSizes(Enum):
    StringHeapLarge: ByteType = 1
    GuidHeapLarge: ByteType = 2
    BlobHeapLarge: ByteType = 4
    ExtraData: ByteType = 64


class MetadataStreamKind(Enum):
    Illegal: IntType = 0
    Compressed: IntType = 1
    Uncompressed: IntType = 2


class MetadataStreamKind(Enum):
    Illegal: IntType = 0
    Compressed: IntType = 1
    Uncompressed: IntType = 2


class StringKind(Enum):
    Plain: ByteType = 0
    DotTerminated: ByteType = 1
    Virtual: ByteType = 4
    WinRTPrefixed: ByteType = 5


class StringKind(Enum):
    Plain: ByteType = 0
    DotTerminated: ByteType = 1
    Virtual: ByteType = 4
    WinRTPrefixed: ByteType = 5


class TableIndex(Enum):
    Module: ByteType = 0
    TypeRef: ByteType = 1
    TypeDef: ByteType = 2
    FieldPtr: ByteType = 3
    Field: ByteType = 4
    MethodPtr: ByteType = 5
    MethodDef: ByteType = 6
    ParamPtr: ByteType = 7
    Param: ByteType = 8
    InterfaceImpl: ByteType = 9
    MemberRef: ByteType = 10
    Constant: ByteType = 11
    CustomAttribute: ByteType = 12
    FieldMarshal: ByteType = 13
    DeclSecurity: ByteType = 14
    ClassLayout: ByteType = 15
    FieldLayout: ByteType = 16
    StandAloneSig: ByteType = 17
    EventMap: ByteType = 18
    EventPtr: ByteType = 19
    Event: ByteType = 20
    PropertyMap: ByteType = 21
    PropertyPtr: ByteType = 22
    Property: ByteType = 23
    MethodSemantics: ByteType = 24
    MethodImpl: ByteType = 25
    ModuleRef: ByteType = 26
    TypeSpec: ByteType = 27
    ImplMap: ByteType = 28
    FieldRva: ByteType = 29
    EncLog: ByteType = 30
    EncMap: ByteType = 31
    Assembly: ByteType = 32
    AssemblyProcessor: ByteType = 33
    AssemblyOS: ByteType = 34
    AssemblyRef: ByteType = 35
    AssemblyRefProcessor: ByteType = 36
    AssemblyRefOS: ByteType = 37
    File: ByteType = 38
    ExportedType: ByteType = 39
    ManifestResource: ByteType = 40
    NestedClass: ByteType = 41
    GenericParam: ByteType = 42
    MethodSpec: ByteType = 43
    GenericParamConstraint: ByteType = 44
    Document: ByteType = 48
    MethodDebugInformation: ByteType = 49
    LocalScope: ByteType = 50
    LocalVariable: ByteType = 51
    LocalConstant: ByteType = 52
    ImportScope: ByteType = 53
    StateMachineMethod: ByteType = 54
    CustomDebugInformation: ByteType = 55


class TableIndex(Enum):
    Module: ByteType = 0
    TypeRef: ByteType = 1
    TypeDef: ByteType = 2
    FieldPtr: ByteType = 3
    Field: ByteType = 4
    MethodPtr: ByteType = 5
    MethodDef: ByteType = 6
    ParamPtr: ByteType = 7
    Param: ByteType = 8
    InterfaceImpl: ByteType = 9
    MemberRef: ByteType = 10
    Constant: ByteType = 11
    CustomAttribute: ByteType = 12
    FieldMarshal: ByteType = 13
    DeclSecurity: ByteType = 14
    ClassLayout: ByteType = 15
    FieldLayout: ByteType = 16
    StandAloneSig: ByteType = 17
    EventMap: ByteType = 18
    EventPtr: ByteType = 19
    Event: ByteType = 20
    PropertyMap: ByteType = 21
    PropertyPtr: ByteType = 22
    Property: ByteType = 23
    MethodSemantics: ByteType = 24
    MethodImpl: ByteType = 25
    ModuleRef: ByteType = 26
    TypeSpec: ByteType = 27
    ImplMap: ByteType = 28
    FieldRva: ByteType = 29
    EncLog: ByteType = 30
    EncMap: ByteType = 31
    Assembly: ByteType = 32
    AssemblyProcessor: ByteType = 33
    AssemblyOS: ByteType = 34
    AssemblyRef: ByteType = 35
    AssemblyRefProcessor: ByteType = 36
    AssemblyRefOS: ByteType = 37
    File: ByteType = 38
    ExportedType: ByteType = 39
    ManifestResource: ByteType = 40
    NestedClass: ByteType = 41
    GenericParam: ByteType = 42
    MethodSpec: ByteType = 43
    GenericParamConstraint: ByteType = 44
    Document: ByteType = 48
    MethodDebugInformation: ByteType = 49
    LocalScope: ByteType = 50
    LocalVariable: ByteType = 51
    LocalConstant: ByteType = 52
    ImportScope: ByteType = 53
    StateMachineMethod: ByteType = 54
    CustomDebugInformation: ByteType = 55


class TableMask(Enum):
    Module: ULongType = 1
    TypeRef: ULongType = 2
    TypeDef: ULongType = 4
    FieldPtr: ULongType = 8
    Field: ULongType = 16
    MethodPtr: ULongType = 32
    MethodDef: ULongType = 64
    ParamPtr: ULongType = 128
    Param: ULongType = 256
    InterfaceImpl: ULongType = 512
    MemberRef: ULongType = 1024
    Constant: ULongType = 2048
    CustomAttribute: ULongType = 4096
    FieldMarshal: ULongType = 8192
    DeclSecurity: ULongType = 16384
    ClassLayout: ULongType = 32768
    FieldLayout: ULongType = 65536
    StandAloneSig: ULongType = 131072
    EventMap: ULongType = 262144
    EventPtr: ULongType = 524288
    Event: ULongType = 1048576
    PropertyMap: ULongType = 2097152
    PropertyPtr: ULongType = 4194304
    PtrTables: ULongType = 4718760
    Property: ULongType = 8388608
    MethodSemantics: ULongType = 16777216
    MethodImpl: ULongType = 33554432
    ModuleRef: ULongType = 67108864
    TypeSpec: ULongType = 134217728
    ImplMap: ULongType = 268435456
    FieldRva: ULongType = 536870912
    EnCLog: ULongType = 1073741824
    EnCMap: ULongType = 2147483648
    EncTables: ULongType = 3221225472
    Assembly: ULongType = 4294967296
    AssemblyRef: ULongType = 34359738368
    File: ULongType = 274877906944
    ExportedType: ULongType = 549755813888
    ManifestResource: ULongType = 1099511627776
    NestedClass: ULongType = 2199023255552
    GenericParam: ULongType = 4398046511104
    MethodSpec: ULongType = 8796093022208
    GenericParamConstraint: ULongType = 17592186044416
    ValidPortablePdbExternalTables: ULongType = 34949217910615
    TypeSystemTables: ULongType = 34952443854847
    Document: ULongType = 281474976710656
    MethodDebugInformation: ULongType = 562949953421312
    LocalScope: ULongType = 1125899906842624
    LocalVariable: ULongType = 2251799813685248
    LocalConstant: ULongType = 4503599627370496
    ImportScope: ULongType = 9007199254740992
    StateMachineMethod: ULongType = 18014398509481984
    CustomDebugInformation: ULongType = 36028797018963968
    DebugTables: ULongType = 71776119061217280
    AllTables: ULongType = 71811071505072127


class TableMask(Enum):
    Module: ULongType = 1
    TypeRef: ULongType = 2
    TypeDef: ULongType = 4
    FieldPtr: ULongType = 8
    Field: ULongType = 16
    MethodPtr: ULongType = 32
    MethodDef: ULongType = 64
    ParamPtr: ULongType = 128
    Param: ULongType = 256
    InterfaceImpl: ULongType = 512
    MemberRef: ULongType = 1024
    Constant: ULongType = 2048
    CustomAttribute: ULongType = 4096
    FieldMarshal: ULongType = 8192
    DeclSecurity: ULongType = 16384
    ClassLayout: ULongType = 32768
    FieldLayout: ULongType = 65536
    StandAloneSig: ULongType = 131072
    EventMap: ULongType = 262144
    EventPtr: ULongType = 524288
    Event: ULongType = 1048576
    PropertyMap: ULongType = 2097152
    PropertyPtr: ULongType = 4194304
    PtrTables: ULongType = 4718760
    Property: ULongType = 8388608
    MethodSemantics: ULongType = 16777216
    MethodImpl: ULongType = 33554432
    ModuleRef: ULongType = 67108864
    TypeSpec: ULongType = 134217728
    ImplMap: ULongType = 268435456
    FieldRva: ULongType = 536870912
    EnCLog: ULongType = 1073741824
    EnCMap: ULongType = 2147483648
    EncTables: ULongType = 3221225472
    Assembly: ULongType = 4294967296
    AssemblyRef: ULongType = 34359738368
    File: ULongType = 274877906944
    ExportedType: ULongType = 549755813888
    ManifestResource: ULongType = 1099511627776
    NestedClass: ULongType = 2199023255552
    GenericParam: ULongType = 4398046511104
    MethodSpec: ULongType = 8796093022208
    GenericParamConstraint: ULongType = 17592186044416
    ValidPortablePdbExternalTables: ULongType = 34949217910615
    TypeSystemTables: ULongType = 34952443854847
    Document: ULongType = 281474976710656
    MethodDebugInformation: ULongType = 562949953421312
    LocalScope: ULongType = 1125899906842624
    LocalVariable: ULongType = 2251799813685248
    LocalConstant: ULongType = 4503599627370496
    ImportScope: ULongType = 9007199254740992
    StateMachineMethod: ULongType = 18014398509481984
    CustomDebugInformation: ULongType = 36028797018963968
    DebugTables: ULongType = 71776119061217280
    AllTables: ULongType = 71811071505072127


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
