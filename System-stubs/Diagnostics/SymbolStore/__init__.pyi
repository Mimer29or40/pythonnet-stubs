from __future__ import annotations

from typing import List, Protocol, Union, overload

from System import Array, Boolean, Byte, Enum, Guid, Int32, IntPtr, Object, String, ValueType, Void
from System.Reflection import FieldAttributes, ParameterAttributes

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class SymDocumentType(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Text() -> Guid: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SymLanguageType(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Basic() -> Guid: ...
    
    @staticmethod
    @property
    def C() -> Guid: ...
    
    @staticmethod
    @property
    def CPlusPlus() -> Guid: ...
    
    @staticmethod
    @property
    def CSharp() -> Guid: ...
    
    @staticmethod
    @property
    def Cobol() -> Guid: ...
    
    @staticmethod
    @property
    def ILAssembly() -> Guid: ...
    
    @staticmethod
    @property
    def JScript() -> Guid: ...
    
    @staticmethod
    @property
    def Java() -> Guid: ...
    
    @staticmethod
    @property
    def MCPlusPlus() -> Guid: ...
    
    @staticmethod
    @property
    def Pascal() -> Guid: ...
    
    @staticmethod
    @property
    def SMC() -> Guid: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SymLanguageVendor(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def Microsoft() -> Guid: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Structs ---------- #

class SymbolToken(ValueType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, val: IntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    @overload
    def Equals(self, obj: SymbolToken) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetToken(self) -> IntType: ...
    
    @staticmethod
    def op_Equality(a: SymbolToken, b: SymbolToken) -> BooleanType: ...
    
    @staticmethod
    def op_Inequality(a: SymbolToken, b: SymbolToken) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Interfaces ---------- #

class ISymbolBinder(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetReader(self, importer: IntType, filename: StringType, searchPath: StringType) -> ISymbolReader: ...
    
    # No Events


class ISymbolBinder1(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetReader(self, importer: NIntType, filename: StringType, searchPath: StringType) -> ISymbolReader: ...
    
    # No Events


class ISymbolDocument(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def CheckSumAlgorithmId(self) -> Guid: ...
    
    @property
    def DocumentType(self) -> Guid: ...
    
    @property
    def HasEmbeddedSource(self) -> BooleanType: ...
    
    @property
    def Language(self) -> Guid: ...
    
    @property
    def LanguageVendor(self) -> Guid: ...
    
    @property
    def SourceLength(self) -> IntType: ...
    
    @property
    def URL(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def FindClosestLine(self, line: IntType) -> IntType: ...
    
    def GetCheckSum(self) -> ArrayType[ByteType]: ...
    
    def GetSourceRange(self, startLine: IntType, startColumn: IntType, endLine: IntType, endColumn: IntType) -> ArrayType[ByteType]: ...
    
    def get_CheckSumAlgorithmId(self) -> Guid: ...
    
    def get_DocumentType(self) -> Guid: ...
    
    def get_HasEmbeddedSource(self) -> BooleanType: ...
    
    def get_Language(self) -> Guid: ...
    
    def get_LanguageVendor(self) -> Guid: ...
    
    def get_SourceLength(self) -> IntType: ...
    
    def get_URL(self) -> StringType: ...
    
    # No Events


class ISymbolDocumentWriter(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def SetCheckSum(self, algorithmId: Guid, checkSum: ArrayType[ByteType]) -> VoidType: ...
    
    def SetSource(self, source: ArrayType[ByteType]) -> VoidType: ...
    
    # No Events


class ISymbolMethod(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def RootScope(self) -> ISymbolScope: ...
    
    @property
    def SequencePointCount(self) -> IntType: ...
    
    @property
    def Token(self) -> SymbolToken: ...
    
    # ---------- Methods ---------- #
    
    def GetNamespace(self) -> ISymbolNamespace: ...
    
    def GetOffset(self, document: ISymbolDocument, line: IntType, column: IntType) -> IntType: ...
    
    def GetParameters(self) -> ArrayType[ISymbolVariable]: ...
    
    def GetRanges(self, document: ISymbolDocument, line: IntType, column: IntType) -> ArrayType[IntType]: ...
    
    def GetScope(self, offset: IntType) -> ISymbolScope: ...
    
    def GetSequencePoints(self, offsets: ArrayType[IntType], documents: ArrayType[ISymbolDocument], lines: ArrayType[IntType], columns: ArrayType[IntType], endLines: ArrayType[IntType], endColumns: ArrayType[IntType]) -> VoidType: ...
    
    def GetSourceStartEnd(self, docs: ArrayType[ISymbolDocument], lines: ArrayType[IntType], columns: ArrayType[IntType]) -> BooleanType: ...
    
    def get_RootScope(self) -> ISymbolScope: ...
    
    def get_SequencePointCount(self) -> IntType: ...
    
    def get_Token(self) -> SymbolToken: ...
    
    # No Events


class ISymbolNamespace(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GetNamespaces(self) -> ArrayType[ISymbolNamespace]: ...
    
    def GetVariables(self) -> ArrayType[ISymbolVariable]: ...
    
    def get_Name(self) -> StringType: ...
    
    # No Events


class ISymbolReader(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def UserEntryPoint(self) -> SymbolToken: ...
    
    # ---------- Methods ---------- #
    
    def GetDocument(self, url: StringType, language: Guid, languageVendor: Guid, documentType: Guid) -> ISymbolDocument: ...
    
    def GetDocuments(self) -> ArrayType[ISymbolDocument]: ...
    
    def GetGlobalVariables(self) -> ArrayType[ISymbolVariable]: ...
    
    @overload
    def GetMethod(self, method: SymbolToken) -> ISymbolMethod: ...
    
    @overload
    def GetMethod(self, method: SymbolToken, version: IntType) -> ISymbolMethod: ...
    
    def GetMethodFromDocumentPosition(self, document: ISymbolDocument, line: IntType, column: IntType) -> ISymbolMethod: ...
    
    def GetNamespaces(self) -> ArrayType[ISymbolNamespace]: ...
    
    def GetSymAttribute(self, parent: SymbolToken, name: StringType) -> ArrayType[ByteType]: ...
    
    def GetVariables(self, parent: SymbolToken) -> ArrayType[ISymbolVariable]: ...
    
    def get_UserEntryPoint(self) -> SymbolToken: ...
    
    # No Events


class ISymbolScope(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def EndOffset(self) -> IntType: ...
    
    @property
    def Method(self) -> ISymbolMethod: ...
    
    @property
    def Parent(self) -> ISymbolScope: ...
    
    @property
    def StartOffset(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def GetChildren(self) -> ArrayType[ISymbolScope]: ...
    
    def GetLocals(self) -> ArrayType[ISymbolVariable]: ...
    
    def GetNamespaces(self) -> ArrayType[ISymbolNamespace]: ...
    
    def get_EndOffset(self) -> IntType: ...
    
    def get_Method(self) -> ISymbolMethod: ...
    
    def get_Parent(self) -> ISymbolScope: ...
    
    def get_StartOffset(self) -> IntType: ...
    
    # No Events


class ISymbolVariable(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def AddressField1(self) -> IntType: ...
    
    @property
    def AddressField2(self) -> IntType: ...
    
    @property
    def AddressField3(self) -> IntType: ...
    
    @property
    def AddressKind(self) -> SymAddressKind: ...
    
    @property
    def Attributes(self) -> ObjectType: ...
    
    @property
    def EndOffset(self) -> IntType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def StartOffset(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def GetSignature(self) -> ArrayType[ByteType]: ...
    
    def get_AddressField1(self) -> IntType: ...
    
    def get_AddressField2(self) -> IntType: ...
    
    def get_AddressField3(self) -> IntType: ...
    
    def get_AddressKind(self) -> SymAddressKind: ...
    
    def get_Attributes(self) -> ObjectType: ...
    
    def get_EndOffset(self) -> IntType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_StartOffset(self) -> IntType: ...
    
    # No Events


class ISymbolWriter(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def CloseMethod(self) -> VoidType: ...
    
    def CloseNamespace(self) -> VoidType: ...
    
    def CloseScope(self, endOffset: IntType) -> VoidType: ...
    
    def DefineDocument(self, url: StringType, language: Guid, languageVendor: Guid, documentType: Guid) -> ISymbolDocumentWriter: ...
    
    def DefineField(self, parent: SymbolToken, name: StringType, attributes: FieldAttributes, signature: ArrayType[ByteType], addrKind: SymAddressKind, addr1: IntType, addr2: IntType, addr3: IntType) -> VoidType: ...
    
    def DefineGlobalVariable(self, name: StringType, attributes: FieldAttributes, signature: ArrayType[ByteType], addrKind: SymAddressKind, addr1: IntType, addr2: IntType, addr3: IntType) -> VoidType: ...
    
    def DefineLocalVariable(self, name: StringType, attributes: FieldAttributes, signature: ArrayType[ByteType], addrKind: SymAddressKind, addr1: IntType, addr2: IntType, addr3: IntType, startOffset: IntType, endOffset: IntType) -> VoidType: ...
    
    def DefineParameter(self, name: StringType, attributes: ParameterAttributes, sequence: IntType, addrKind: SymAddressKind, addr1: IntType, addr2: IntType, addr3: IntType) -> VoidType: ...
    
    def DefineSequencePoints(self, document: ISymbolDocumentWriter, offsets: ArrayType[IntType], lines: ArrayType[IntType], columns: ArrayType[IntType], endLines: ArrayType[IntType], endColumns: ArrayType[IntType]) -> VoidType: ...
    
    def Initialize(self, emitter: NIntType, filename: StringType, fFullBuild: BooleanType) -> VoidType: ...
    
    def OpenMethod(self, method: SymbolToken) -> VoidType: ...
    
    def OpenNamespace(self, name: StringType) -> VoidType: ...
    
    def OpenScope(self, startOffset: IntType) -> IntType: ...
    
    def SetMethodSourceRange(self, startDoc: ISymbolDocumentWriter, startLine: IntType, startColumn: IntType, endDoc: ISymbolDocumentWriter, endLine: IntType, endColumn: IntType) -> VoidType: ...
    
    def SetScopeRange(self, scopeID: IntType, startOffset: IntType, endOffset: IntType) -> VoidType: ...
    
    def SetSymAttribute(self, parent: SymbolToken, name: StringType, data: ArrayType[ByteType]) -> VoidType: ...
    
    def SetUnderlyingWriter(self, underlyingWriter: NIntType) -> VoidType: ...
    
    def SetUserEntryPoint(self, entryMethod: SymbolToken) -> VoidType: ...
    
    def UsingNamespace(self, fullName: StringType) -> VoidType: ...
    
    # No Events


# ---------- Enums ---------- #

class SymAddressKind(Enum):
    ILOffset = 1
    NativeRVA = 2
    NativeRegister = 3
    NativeRegisterRelative = 4
    NativeOffset = 5
    NativeRegisterRegister = 6
    NativeRegisterStack = 7
    NativeStackRegister = 8
    BitField = 9
    NativeSectionOffset = 10


# No Delegates

__all__ = [
    SymDocumentType,
    SymLanguageType,
    SymLanguageVendor,
    SymbolToken,
    ISymbolBinder,
    ISymbolBinder1,
    ISymbolDocument,
    ISymbolDocumentWriter,
    ISymbolMethod,
    ISymbolNamespace,
    ISymbolReader,
    ISymbolScope,
    ISymbolVariable,
    ISymbolWriter,
    SymAddressKind,
]
