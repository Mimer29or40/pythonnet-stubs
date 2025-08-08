"""Automatically generated stubs for C# namespace: System.Diagnostics.SymbolStore."""

from abc import ABC
from typing import ClassVar
from typing import overload

from System import Array
from System import Enum
from System import Guid
from System import IntPtr
from System import Object
from System import Type
from System import ValueType
from System.Reflection import FieldAttributes
from System.Reflection import ParameterAttributes

class ISymbolBinder(ABC):
    """"""
    def GetReader(self, importer: int, filename: str, searchPath: str) -> ISymbolReader:
        """"""

class ISymbolBinder1(ABC):
    """"""
    def GetReader(self, importer: IntPtr, filename: str, searchPath: str) -> ISymbolReader:
        """"""

class ISymbolDocument(ABC):
    """"""
    @property
    def CheckSumAlgorithmId(self) -> Guid:
        """"""
    @property
    def DocumentType(self) -> Guid:
        """"""
    @property
    def HasEmbeddedSource(self) -> bool:
        """"""
    @property
    def Language(self) -> Guid:
        """"""
    @property
    def LanguageVendor(self) -> Guid:
        """"""
    @property
    def SourceLength(self) -> int:
        """"""
    @property
    def URL(self) -> str:
        """"""
    def FindClosestLine(self, line: int) -> int:
        """"""
    def GetCheckSum(self) -> Array[int]:
        """"""
    def GetSourceRange(
        self, startLine: int, startColumn: int, endLine: int, endColumn: int
    ) -> Array[int]:
        """"""

class ISymbolDocumentWriter(ABC):
    """"""
    def SetCheckSum(self, algorithmId: Guid, checkSum: Array[int]) -> None:
        """"""
    def SetSource(self, source: Array[int]) -> None:
        """"""

class ISymbolMethod(ABC):
    """"""
    @property
    def RootScope(self) -> ISymbolScope:
        """"""
    @property
    def SequencePointCount(self) -> int:
        """"""
    @property
    def Token(self) -> SymbolToken:
        """"""
    def GetNamespace(self) -> ISymbolNamespace:
        """"""
    def GetOffset(self, document: ISymbolDocument, line: int, column: int) -> int:
        """"""
    def GetParameters(self) -> Array[ISymbolVariable]:
        """"""
    def GetRanges(self, document: ISymbolDocument, line: int, column: int) -> Array[int]:
        """"""
    def GetScope(self, offset: int) -> ISymbolScope:
        """"""
    def GetSequencePoints(
        self,
        offsets: Array[int],
        documents: Array[ISymbolDocument],
        lines: Array[int],
        columns: Array[int],
        endLines: Array[int],
        endColumns: Array[int],
    ) -> None:
        """"""
    def GetSourceStartEnd(
        self, docs: Array[ISymbolDocument], lines: Array[int], columns: Array[int]
    ) -> bool:
        """"""

class ISymbolNamespace(ABC):
    """"""
    @property
    def Name(self) -> str:
        """"""
    def GetNamespaces(self) -> Array[ISymbolNamespace]:
        """"""
    def GetVariables(self) -> Array[ISymbolVariable]:
        """"""

class ISymbolReader(ABC):
    """"""
    @property
    def UserEntryPoint(self) -> SymbolToken:
        """"""
    def GetDocument(
        self, url: str, language: Guid, languageVendor: Guid, documentType: Guid
    ) -> ISymbolDocument:
        """"""
    def GetDocuments(self) -> Array[ISymbolDocument]:
        """"""
    def GetGlobalVariables(self) -> Array[ISymbolVariable]:
        """"""
    @overload
    def GetMethod(self, method: SymbolToken) -> ISymbolMethod:
        """"""
    @overload
    def GetMethod(self, method: SymbolToken, version: int) -> ISymbolMethod:
        """"""
    def GetMethodFromDocumentPosition(
        self, document: ISymbolDocument, line: int, column: int
    ) -> ISymbolMethod:
        """"""
    def GetNamespaces(self) -> Array[ISymbolNamespace]:
        """"""
    def GetSymAttribute(self, parent: SymbolToken, name: str) -> Array[int]:
        """"""
    def GetVariables(self, parent: SymbolToken) -> Array[ISymbolVariable]:
        """"""

class ISymbolScope(ABC):
    """"""
    @property
    def EndOffset(self) -> int:
        """"""
    @property
    def Method(self) -> ISymbolMethod:
        """"""
    @property
    def Parent(self) -> ISymbolScope:
        """"""
    @property
    def StartOffset(self) -> int:
        """"""
    def GetChildren(self) -> Array[ISymbolScope]:
        """"""
    def GetLocals(self) -> Array[ISymbolVariable]:
        """"""
    def GetNamespaces(self) -> Array[ISymbolNamespace]:
        """"""

class ISymbolVariable(ABC):
    """"""
    @property
    def AddressField1(self) -> int:
        """"""
    @property
    def AddressField2(self) -> int:
        """"""
    @property
    def AddressField3(self) -> int:
        """"""
    @property
    def AddressKind(self) -> SymAddressKind:
        """"""
    @property
    def Attributes(self) -> object:
        """"""
    @property
    def EndOffset(self) -> int:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def StartOffset(self) -> int:
        """"""
    def GetSignature(self) -> Array[int]:
        """"""

class ISymbolWriter(ABC):
    """"""
    def Close(self) -> None:
        """"""
    def CloseMethod(self) -> None:
        """"""
    def CloseNamespace(self) -> None:
        """"""
    def CloseScope(self, endOffset: int) -> None:
        """"""
    def DefineDocument(
        self, url: str, language: Guid, languageVendor: Guid, documentType: Guid
    ) -> ISymbolDocumentWriter:
        """"""
    def DefineField(
        self,
        parent: SymbolToken,
        name: str,
        attributes: FieldAttributes,
        signature: Array[int],
        addrKind: SymAddressKind,
        addr1: int,
        addr2: int,
        addr3: int,
    ) -> None:
        """"""
    def DefineGlobalVariable(
        self,
        name: str,
        attributes: FieldAttributes,
        signature: Array[int],
        addrKind: SymAddressKind,
        addr1: int,
        addr2: int,
        addr3: int,
    ) -> None:
        """"""
    def DefineLocalVariable(
        self,
        name: str,
        attributes: FieldAttributes,
        signature: Array[int],
        addrKind: SymAddressKind,
        addr1: int,
        addr2: int,
        addr3: int,
        startOffset: int,
        endOffset: int,
    ) -> None:
        """"""
    def DefineParameter(
        self,
        name: str,
        attributes: ParameterAttributes,
        sequence: int,
        addrKind: SymAddressKind,
        addr1: int,
        addr2: int,
        addr3: int,
    ) -> None:
        """"""
    def DefineSequencePoints(
        self,
        document: ISymbolDocumentWriter,
        offsets: Array[int],
        lines: Array[int],
        columns: Array[int],
        endLines: Array[int],
        endColumns: Array[int],
    ) -> None:
        """"""
    def Initialize(self, emitter: IntPtr, filename: str, fFullBuild: bool) -> None:
        """"""
    def OpenMethod(self, method: SymbolToken) -> None:
        """"""
    def OpenNamespace(self, name: str) -> None:
        """"""
    def OpenScope(self, startOffset: int) -> int:
        """"""
    def SetMethodSourceRange(
        self,
        startDoc: ISymbolDocumentWriter,
        startLine: int,
        startColumn: int,
        endDoc: ISymbolDocumentWriter,
        endLine: int,
        endColumn: int,
    ) -> None:
        """"""
    def SetScopeRange(self, scopeID: int, startOffset: int, endOffset: int) -> None:
        """"""
    def SetSymAttribute(self, parent: SymbolToken, name: str, data: Array[int]) -> None:
        """"""
    def SetUnderlyingWriter(self, underlyingWriter: IntPtr) -> None:
        """"""
    def SetUserEntryPoint(self, entryMethod: SymbolToken) -> None:
        """"""
    def UsingNamespace(self, fullName: str) -> None:
        """"""

class SymAddressKind(Enum):
    """"""

    ILOffset: SymAddressKind = ...
    """"""
    NativeRVA: SymAddressKind = ...
    """"""
    NativeRegister: SymAddressKind = ...
    """"""
    NativeRegisterRelative: SymAddressKind = ...
    """"""
    NativeOffset: SymAddressKind = ...
    """"""
    NativeRegisterRegister: SymAddressKind = ...
    """"""
    NativeRegisterStack: SymAddressKind = ...
    """"""
    NativeStackRegister: SymAddressKind = ...
    """"""
    BitField: SymAddressKind = ...
    """"""
    NativeSectionOffset: SymAddressKind = ...
    """"""

class SymDocumentType(Object):
    """"""

    Text: ClassVar[Guid]
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SymLanguageType(Object):
    """"""

    Basic: ClassVar[Guid]
    """"""
    C: ClassVar[Guid]
    """"""
    CPlusPlus: ClassVar[Guid]
    """"""
    CSharp: ClassVar[Guid]
    """"""
    Cobol: ClassVar[Guid]
    """"""
    ILAssembly: ClassVar[Guid]
    """"""
    JScript: ClassVar[Guid]
    """"""
    Java: ClassVar[Guid]
    """"""
    MCPlusPlus: ClassVar[Guid]
    """"""
    Pascal: ClassVar[Guid]
    """"""
    SMC: ClassVar[Guid]
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SymLanguageVendor(Object):
    """"""

    Microsoft: ClassVar[Guid]
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SymbolToken(ValueType):
    """"""
    def __init__(self, val: int) -> None:
        """"""
    @overload
    def Equals(self, obj: SymbolToken) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetToken(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, a: SymbolToken, b: SymbolToken) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, a: SymbolToken, b: SymbolToken) -> bool:
        """"""
    def __eq__(self, other: SymbolToken) -> bool:
        """"""
    def __ne__(self, other: SymbolToken) -> bool:
        """"""
