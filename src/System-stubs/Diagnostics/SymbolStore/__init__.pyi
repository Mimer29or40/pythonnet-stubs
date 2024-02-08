from __future__ import annotations

from typing import ClassVar
from typing import Final
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

class ISymbolBinder:
    """"""

    def GetReader(self, importer: int, filename: str, searchPath: str) -> ISymbolReader:
        """

        :param importer:
        :param filename:
        :param searchPath:
        :return:
        """

class ISymbolBinder1:
    """"""

    def GetReader(self, importer: IntPtr, filename: str, searchPath: str) -> ISymbolReader:
        """

        :param importer:
        :param filename:
        :param searchPath:
        :return:
        """

class ISymbolDocument:
    """"""

    @property
    def CheckSumAlgorithmId(self) -> Guid:
        """

        :return:
        """
    @property
    def DocumentType(self) -> Guid:
        """

        :return:
        """
    @property
    def HasEmbeddedSource(self) -> bool:
        """

        :return:
        """
    @property
    def Language(self) -> Guid:
        """

        :return:
        """
    @property
    def LanguageVendor(self) -> Guid:
        """

        :return:
        """
    @property
    def SourceLength(self) -> int:
        """

        :return:
        """
    @property
    def URL(self) -> str:
        """

        :return:
        """
    def FindClosestLine(self, line: int) -> int:
        """

        :param line:
        :return:
        """
    def GetCheckSum(self) -> Array[int]:
        """

        :return:
        """
    def GetSourceRange(
        self, startLine: int, startColumn: int, endLine: int, endColumn: int
    ) -> Array[int]:
        """

        :param startLine:
        :param startColumn:
        :param endLine:
        :param endColumn:
        :return:
        """

class ISymbolDocumentWriter:
    """"""

    def SetCheckSum(self, algorithmId: Guid, checkSum: Array[int]) -> None:
        """

        :param algorithmId:
        :param checkSum:
        """
    def SetSource(self, source: Array[int]) -> None:
        """

        :param source:
        """

class ISymbolMethod:
    """"""

    @property
    def RootScope(self) -> ISymbolScope:
        """

        :return:
        """
    @property
    def SequencePointCount(self) -> int:
        """

        :return:
        """
    @property
    def Token(self) -> SymbolToken:
        """

        :return:
        """
    def GetNamespace(self) -> ISymbolNamespace:
        """

        :return:
        """
    def GetOffset(self, document: ISymbolDocument, line: int, column: int) -> int:
        """

        :param document:
        :param line:
        :param column:
        :return:
        """
    def GetParameters(self) -> Array[ISymbolVariable]:
        """

        :return:
        """
    def GetRanges(self, document: ISymbolDocument, line: int, column: int) -> Array[int]:
        """

        :param document:
        :param line:
        :param column:
        :return:
        """
    def GetScope(self, offset: int) -> ISymbolScope:
        """

        :param offset:
        :return:
        """
    def GetSequencePoints(
        self,
        offsets: Array[int],
        documents: Array[ISymbolDocument],
        lines: Array[int],
        columns: Array[int],
        endLines: Array[int],
        endColumns: Array[int],
    ) -> None:
        """

        :param offsets:
        :param documents:
        :param lines:
        :param columns:
        :param endLines:
        :param endColumns:
        """
    def GetSourceStartEnd(
        self, docs: Array[ISymbolDocument], lines: Array[int], columns: Array[int]
    ) -> bool:
        """

        :param docs:
        :param lines:
        :param columns:
        :return:
        """

class ISymbolNamespace:
    """"""

    @property
    def Name(self) -> str:
        """

        :return:
        """
    def GetNamespaces(self) -> Array[ISymbolNamespace]:
        """

        :return:
        """
    def GetVariables(self) -> Array[ISymbolVariable]:
        """

        :return:
        """

class ISymbolReader:
    """"""

    @property
    def UserEntryPoint(self) -> SymbolToken:
        """

        :return:
        """
    def GetDocument(
        self, url: str, language: Guid, languageVendor: Guid, documentType: Guid
    ) -> ISymbolDocument:
        """

        :param url:
        :param language:
        :param languageVendor:
        :param documentType:
        :return:
        """
    def GetDocuments(self) -> Array[ISymbolDocument]:
        """

        :return:
        """
    def GetGlobalVariables(self) -> Array[ISymbolVariable]:
        """

        :return:
        """
    @overload
    def GetMethod(self, method: SymbolToken) -> ISymbolMethod:
        """

        :param method:
        :return:
        """
    @overload
    def GetMethod(self, method: SymbolToken, version: int) -> ISymbolMethod:
        """

        :param method:
        :param version:
        :return:
        """
    def GetMethodFromDocumentPosition(
        self, document: ISymbolDocument, line: int, column: int
    ) -> ISymbolMethod:
        """

        :param document:
        :param line:
        :param column:
        :return:
        """
    def GetNamespaces(self) -> Array[ISymbolNamespace]:
        """

        :return:
        """
    def GetSymAttribute(self, parent: SymbolToken, name: str) -> Array[int]:
        """

        :param parent:
        :param name:
        :return:
        """
    def GetVariables(self, parent: SymbolToken) -> Array[ISymbolVariable]:
        """

        :param parent:
        :return:
        """

class ISymbolScope:
    """"""

    @property
    def EndOffset(self) -> int:
        """

        :return:
        """
    @property
    def Method(self) -> ISymbolMethod:
        """

        :return:
        """
    @property
    def Parent(self) -> ISymbolScope:
        """

        :return:
        """
    @property
    def StartOffset(self) -> int:
        """

        :return:
        """
    def GetChildren(self) -> Array[ISymbolScope]:
        """

        :return:
        """
    def GetLocals(self) -> Array[ISymbolVariable]:
        """

        :return:
        """
    def GetNamespaces(self) -> Array[ISymbolNamespace]:
        """

        :return:
        """

class ISymbolVariable:
    """"""

    @property
    def AddressField1(self) -> int:
        """

        :return:
        """
    @property
    def AddressField2(self) -> int:
        """

        :return:
        """
    @property
    def AddressField3(self) -> int:
        """

        :return:
        """
    @property
    def AddressKind(self) -> SymAddressKind:
        """

        :return:
        """
    @property
    def Attributes(self) -> object:
        """

        :return:
        """
    @property
    def EndOffset(self) -> int:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def StartOffset(self) -> int:
        """

        :return:
        """
    def GetSignature(self) -> Array[int]:
        """

        :return:
        """

class ISymbolWriter:
    """"""

    def Close(self) -> None:
        """"""
    def CloseMethod(self) -> None:
        """"""
    def CloseNamespace(self) -> None:
        """"""
    def CloseScope(self, endOffset: int) -> None:
        """

        :param endOffset:
        """
    def DefineDocument(
        self, url: str, language: Guid, languageVendor: Guid, documentType: Guid
    ) -> ISymbolDocumentWriter:
        """

        :param url:
        :param language:
        :param languageVendor:
        :param documentType:
        :return:
        """
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
        """

        :param parent:
        :param name:
        :param attributes:
        :param signature:
        :param addrKind:
        :param addr1:
        :param addr2:
        :param addr3:
        """
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
        """

        :param name:
        :param attributes:
        :param signature:
        :param addrKind:
        :param addr1:
        :param addr2:
        :param addr3:
        """
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
        """

        :param name:
        :param attributes:
        :param signature:
        :param addrKind:
        :param addr1:
        :param addr2:
        :param addr3:
        :param startOffset:
        :param endOffset:
        """
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
        """

        :param name:
        :param attributes:
        :param sequence:
        :param addrKind:
        :param addr1:
        :param addr2:
        :param addr3:
        """
    def DefineSequencePoints(
        self,
        document: ISymbolDocumentWriter,
        offsets: Array[int],
        lines: Array[int],
        columns: Array[int],
        endLines: Array[int],
        endColumns: Array[int],
    ) -> None:
        """

        :param document:
        :param offsets:
        :param lines:
        :param columns:
        :param endLines:
        :param endColumns:
        """
    def Initialize(self, emitter: IntPtr, filename: str, fFullBuild: bool) -> None:
        """

        :param emitter:
        :param filename:
        :param fFullBuild:
        """
    def OpenMethod(self, method: SymbolToken) -> None:
        """

        :param method:
        """
    def OpenNamespace(self, name: str) -> None:
        """

        :param name:
        """
    def OpenScope(self, startOffset: int) -> int:
        """

        :param startOffset:
        :return:
        """
    def SetMethodSourceRange(
        self,
        startDoc: ISymbolDocumentWriter,
        startLine: int,
        startColumn: int,
        endDoc: ISymbolDocumentWriter,
        endLine: int,
        endColumn: int,
    ) -> None:
        """

        :param startDoc:
        :param startLine:
        :param startColumn:
        :param endDoc:
        :param endLine:
        :param endColumn:
        """
    def SetScopeRange(self, scopeID: int, startOffset: int, endOffset: int) -> None:
        """

        :param scopeID:
        :param startOffset:
        :param endOffset:
        """
    def SetSymAttribute(self, parent: SymbolToken, name: str, data: Array[int]) -> None:
        """

        :param parent:
        :param name:
        :param data:
        """
    def SetUnderlyingWriter(self, underlyingWriter: IntPtr) -> None:
        """

        :param underlyingWriter:
        """
    def SetUserEntryPoint(self, entryMethod: SymbolToken) -> None:
        """

        :param entryMethod:
        """
    def UsingNamespace(self, fullName: str) -> None:
        """

        :param fullName:
        """

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

    Text: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    def __init__(self):
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

class SymLanguageType(Object):
    """"""

    Basic: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    C: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    CPlusPlus: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    CSharp: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    Cobol: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    ILAssembly: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    JScript: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    Java: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    MCPlusPlus: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    Pascal: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    SMC: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    def __init__(self):
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

class SymLanguageVendor(Object):
    """"""

    Microsoft: Final[ClassVar[Guid]] = ...
    """
    
    :return: 
    """
    def __init__(self):
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

class SymbolToken(ValueType):
    """"""

    def __init__(self, val: int):
        """

        :param val:
        """
    @overload
    def Equals(self, obj: SymbolToken) -> bool:
        """

        :param obj:
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
    def GetToken(self) -> int:
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
    def __eq__(self, other: SymbolToken) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: SymbolToken) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, a: SymbolToken, b: SymbolToken) -> bool:
        """

        :param a:
        :param b:
        :return:
        """
    @classmethod
    def op_Inequality(cls, a: SymbolToken, b: SymbolToken) -> bool:
        """

        :param a:
        :param b:
        :return:
        """
