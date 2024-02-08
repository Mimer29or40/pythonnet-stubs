from __future__ import annotations

from abc import ABC
from typing import ClassVar
from typing import Final
from typing import Tuple

from System import Enum
from System import Object
from System import Type
from System import ValueType
from System.Reflection.Metadata import DocumentNameBlobHandle
from System.Reflection.Metadata import Handle
from System.Reflection.Metadata import HandleKind
from System.Reflection.Metadata import MethodDebugInformationHandle
from System.Reflection.Metadata import MethodDefinitionHandle

class BlobHeap(ValueType):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetDocumentName(self, handle: DocumentNameBlobHandle) -> str:
        """

        :param handle:
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

class COR20Constants(ABC, Object):
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

class DocumentTableReader(ValueType):
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

class HandleType(ABC, Object):
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

class HeapHandleType(ABC, Object):
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

class HeapSizeFlag(Enum):
    """"""

    StringHeapLarge: HeapSizeFlag = ...
    """"""
    GuidHeapLarge: HeapSizeFlag = ...
    """"""
    BlobHeapLarge: HeapSizeFlag = ...
    """"""
    EncDeltas: HeapSizeFlag = ...
    """"""
    DeletedMarks: HeapSizeFlag = ...
    """"""

class HeapSizes(Enum):
    """"""

    StringHeapLarge: HeapSizes = ...
    """"""
    GuidHeapLarge: HeapSizes = ...
    """"""
    BlobHeapLarge: HeapSizes = ...
    """"""
    ExtraData: HeapSizes = ...
    """"""

class MetadataStreamConstants(ABC, Object):
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

class MetadataStreamKind(Enum):
    """"""

    Illegal: MetadataStreamKind = ...
    """"""
    Compressed: MetadataStreamKind = ...
    """"""
    Uncompressed: MetadataStreamKind = ...
    """"""

class MetadataTokens(ABC, Object):
    """"""

    TableCount: Final[ClassVar[int]] = ...
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
    @classmethod
    def GetHeapOffset(cls, handle: Handle) -> int:
        """

        :param handle:
        :return:
        """
    @classmethod
    def GetToken(cls, handle: Handle) -> int:
        """

        :param handle:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def Handle(cls, token: int) -> Handle:
        """

        :param token:
        :return:
        """
    @classmethod
    def MethodDebugInformationHandle(cls, rowNumber: int) -> MethodDebugInformationHandle:
        """

        :param rowNumber:
        :return:
        """
    @classmethod
    def MethodDefinitionHandle(cls, rowNumber: int) -> MethodDefinitionHandle:
        """

        :param rowNumber:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    def TryGetTableIndex(cls, type: HandleKind, index: TableIndex) -> Tuple[bool, TableIndex]:
        """

        :param type:
        :param index:
        :return:
        """

class MethodDebugInformationTableReader(ValueType):
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

class StreamHeader(ValueType):
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

class StringHandleType(ABC, Object):
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

class StringKind(Enum):
    """"""

    Plain: StringKind = ...
    """"""
    DotTerminated: StringKind = ...
    """"""
    Virtual: StringKind = ...
    """"""
    WinRTPrefixed: StringKind = ...
    """"""

class TableIndex(Enum):
    """"""

    Module: TableIndex = ...
    """"""
    TypeRef: TableIndex = ...
    """"""
    TypeDef: TableIndex = ...
    """"""
    FieldPtr: TableIndex = ...
    """"""
    Field: TableIndex = ...
    """"""
    MethodPtr: TableIndex = ...
    """"""
    MethodDef: TableIndex = ...
    """"""
    ParamPtr: TableIndex = ...
    """"""
    Param: TableIndex = ...
    """"""
    InterfaceImpl: TableIndex = ...
    """"""
    MemberRef: TableIndex = ...
    """"""
    Constant: TableIndex = ...
    """"""
    CustomAttribute: TableIndex = ...
    """"""
    FieldMarshal: TableIndex = ...
    """"""
    DeclSecurity: TableIndex = ...
    """"""
    ClassLayout: TableIndex = ...
    """"""
    FieldLayout: TableIndex = ...
    """"""
    StandAloneSig: TableIndex = ...
    """"""
    EventMap: TableIndex = ...
    """"""
    EventPtr: TableIndex = ...
    """"""
    Event: TableIndex = ...
    """"""
    PropertyMap: TableIndex = ...
    """"""
    PropertyPtr: TableIndex = ...
    """"""
    Property: TableIndex = ...
    """"""
    MethodSemantics: TableIndex = ...
    """"""
    MethodImpl: TableIndex = ...
    """"""
    ModuleRef: TableIndex = ...
    """"""
    TypeSpec: TableIndex = ...
    """"""
    ImplMap: TableIndex = ...
    """"""
    FieldRva: TableIndex = ...
    """"""
    EncLog: TableIndex = ...
    """"""
    EncMap: TableIndex = ...
    """"""
    Assembly: TableIndex = ...
    """"""
    AssemblyProcessor: TableIndex = ...
    """"""
    AssemblyOS: TableIndex = ...
    """"""
    AssemblyRef: TableIndex = ...
    """"""
    AssemblyRefProcessor: TableIndex = ...
    """"""
    AssemblyRefOS: TableIndex = ...
    """"""
    File: TableIndex = ...
    """"""
    ExportedType: TableIndex = ...
    """"""
    ManifestResource: TableIndex = ...
    """"""
    NestedClass: TableIndex = ...
    """"""
    GenericParam: TableIndex = ...
    """"""
    MethodSpec: TableIndex = ...
    """"""
    GenericParamConstraint: TableIndex = ...
    """"""
    Document: TableIndex = ...
    """"""
    MethodDebugInformation: TableIndex = ...
    """"""
    LocalScope: TableIndex = ...
    """"""
    LocalVariable: TableIndex = ...
    """"""
    LocalConstant: TableIndex = ...
    """"""
    ImportScope: TableIndex = ...
    """"""
    StateMachineMethod: TableIndex = ...
    """"""
    CustomDebugInformation: TableIndex = ...
    """"""

class TableMask(Enum):
    """"""

    Module: TableMask = ...
    """"""
    TypeRef: TableMask = ...
    """"""
    TypeDef: TableMask = ...
    """"""
    FieldPtr: TableMask = ...
    """"""
    Field: TableMask = ...
    """"""
    MethodPtr: TableMask = ...
    """"""
    MethodDef: TableMask = ...
    """"""
    ParamPtr: TableMask = ...
    """"""
    Param: TableMask = ...
    """"""
    InterfaceImpl: TableMask = ...
    """"""
    MemberRef: TableMask = ...
    """"""
    Constant: TableMask = ...
    """"""
    CustomAttribute: TableMask = ...
    """"""
    FieldMarshal: TableMask = ...
    """"""
    DeclSecurity: TableMask = ...
    """"""
    ClassLayout: TableMask = ...
    """"""
    FieldLayout: TableMask = ...
    """"""
    StandAloneSig: TableMask = ...
    """"""
    EventMap: TableMask = ...
    """"""
    EventPtr: TableMask = ...
    """"""
    Event: TableMask = ...
    """"""
    PropertyMap: TableMask = ...
    """"""
    PropertyPtr: TableMask = ...
    """"""
    PtrTables: TableMask = ...
    """"""
    Property: TableMask = ...
    """"""
    MethodSemantics: TableMask = ...
    """"""
    MethodImpl: TableMask = ...
    """"""
    ModuleRef: TableMask = ...
    """"""
    TypeSpec: TableMask = ...
    """"""
    ImplMap: TableMask = ...
    """"""
    FieldRva: TableMask = ...
    """"""
    EnCLog: TableMask = ...
    """"""
    EnCMap: TableMask = ...
    """"""
    EncTables: TableMask = ...
    """"""
    Assembly: TableMask = ...
    """"""
    AssemblyRef: TableMask = ...
    """"""
    File: TableMask = ...
    """"""
    ExportedType: TableMask = ...
    """"""
    ManifestResource: TableMask = ...
    """"""
    NestedClass: TableMask = ...
    """"""
    GenericParam: TableMask = ...
    """"""
    MethodSpec: TableMask = ...
    """"""
    GenericParamConstraint: TableMask = ...
    """"""
    ValidPortablePdbExternalTables: TableMask = ...
    """"""
    TypeSystemTables: TableMask = ...
    """"""
    Document: TableMask = ...
    """"""
    MethodDebugInformation: TableMask = ...
    """"""
    LocalScope: TableMask = ...
    """"""
    LocalVariable: TableMask = ...
    """"""
    LocalConstant: TableMask = ...
    """"""
    ImportScope: TableMask = ...
    """"""
    StateMachineMethod: TableMask = ...
    """"""
    CustomDebugInformation: TableMask = ...
    """"""
    DebugTables: TableMask = ...
    """"""
    AllTables: TableMask = ...
    """"""

class TokenTypeIds(ABC, Object):
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
