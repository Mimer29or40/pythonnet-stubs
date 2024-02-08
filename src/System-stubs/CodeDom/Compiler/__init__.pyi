from __future__ import annotations

from abc import ABC
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import Iterator
from typing import Tuple
from typing import TypeVar
from typing import overload

from Microsoft.Win32.SafeHandles import SafeFileHandle
from System import Array
from System import Attribute
from System import Char
from System import Decimal
from System import Enum
from System import EventHandler
from System import Guid
from System import IDisposable
from System import IFormatProvider
from System import IntPtr
from System import Object
from System import Type
from System.CodeDom import CodeCompileUnit
from System.CodeDom import CodeExpression
from System.CodeDom import CodeNamespace
from System.CodeDom import CodeObject
from System.CodeDom import CodeStatement
from System.CodeDom import CodeTypeDeclaration
from System.CodeDom import CodeTypeMember
from System.CodeDom import CodeTypeReference
from System.Collections import CollectionBase
from System.Collections import ICollection
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections import IList
from System.Collections.Generic import IDictionary
from System.Collections.Specialized import StringCollection
from System.ComponentModel import Component
from System.ComponentModel import IComponent
from System.ComponentModel import IContainer
from System.ComponentModel import ISite
from System.ComponentModel import TypeConverter
from System.Configuration import IConfigurationSectionHandler
from System.IO import TextReader
from System.IO import TextWriter
from System.Reflection import Assembly
from System.Runtime.InteropServices import _Attribute
from System.Runtime.Remoting import ObjRef
from System.Security.Policy import Evidence
from System.Text import Encoding
from System.Threading.Tasks import Task
from System.Xml import XmlNode

T = TypeVar("T")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

class CodeCompiler(ABC, CodeGenerator, ICodeCompiler, ICodeGenerator):
    """"""

    def CompileAssemblyFromDom(
        self, options: CompilerParameters, compilationUnit: CodeCompileUnit
    ) -> CompilerResults:
        """

        :param options:
        :param compilationUnit:
        :return:
        """
    def CompileAssemblyFromDomBatch(
        self, options: CompilerParameters, compilationUnits: Array[CodeCompileUnit]
    ) -> CompilerResults:
        """

        :param options:
        :param compilationUnits:
        :return:
        """
    def CompileAssemblyFromFile(
        self, options: CompilerParameters, fileName: str
    ) -> CompilerResults:
        """

        :param options:
        :param fileName:
        :return:
        """
    def CompileAssemblyFromFileBatch(
        self, options: CompilerParameters, fileNames: Array[str]
    ) -> CompilerResults:
        """

        :param options:
        :param fileNames:
        :return:
        """
    def CompileAssemblyFromSource(
        self, options: CompilerParameters, source: str
    ) -> CompilerResults:
        """

        :param options:
        :param source:
        :return:
        """
    def CompileAssemblyFromSourceBatch(
        self, options: CompilerParameters, sources: Array[str]
    ) -> CompilerResults:
        """

        :param options:
        :param sources:
        :return:
        """
    def CreateEscapedIdentifier(self, value: str) -> str:
        """

        :param value:
        :return:
        """
    def CreateValidIdentifier(self, value: str) -> str:
        """

        :param value:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GenerateCodeFromCompileUnit(
        self, e: CodeCompileUnit, w: TextWriter, o: CodeGeneratorOptions
    ) -> None:
        """

        :param e:
        :param w:
        :param o:
        """
    def GenerateCodeFromExpression(
        self, e: CodeExpression, w: TextWriter, o: CodeGeneratorOptions
    ) -> None:
        """

        :param e:
        :param w:
        :param o:
        """
    def GenerateCodeFromMember(
        self, member: CodeTypeMember, writer: TextWriter, options: CodeGeneratorOptions
    ) -> None:
        """

        :param member:
        :param writer:
        :param options:
        """
    def GenerateCodeFromNamespace(
        self, e: CodeNamespace, w: TextWriter, o: CodeGeneratorOptions
    ) -> None:
        """

        :param e:
        :param w:
        :param o:
        """
    def GenerateCodeFromStatement(
        self, e: CodeStatement, w: TextWriter, o: CodeGeneratorOptions
    ) -> None:
        """

        :param e:
        :param w:
        :param o:
        """
    def GenerateCodeFromType(
        self, e: CodeTypeDeclaration, w: TextWriter, o: CodeGeneratorOptions
    ) -> None:
        """

        :param e:
        :param w:
        :param o:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeOutput(self, type: CodeTypeReference) -> str:
        """

        :param type:
        :return:
        """
    def IsValidIdentifier(self, value: str) -> bool:
        """

        :param value:
        :return:
        """
    def Supports(self, supports: GeneratorSupport) -> bool:
        """

        :param supports:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def ValidateIdentifier(self, value: str) -> None:
        """

        :param value:
        """

class CodeDomCompilationConfiguration(Object):
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

class CodeDomConfigurationHandler(Object, IConfigurationSectionHandler):
    """"""

    def Create(self, parent: object, configContext: object, section: XmlNode) -> object:
        """

        :param parent:
        :param configContext:
        :param section:
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

class CodeDomProvider(ABC, Component, IComponent, IDisposable):
    """"""

    @property
    def Container(self) -> IContainer:
        """

        :return:
        """
    @property
    def FileExtension(self) -> str:
        """

        :return:
        """
    @property
    def LanguageOptions(self) -> LanguageOptions:
        """

        :return:
        """
    @property
    def Site(self) -> ISite:
        """

        :return:
        """
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    def CompileAssemblyFromDom(
        self, options: CompilerParameters, compilationUnits: Array[CodeCompileUnit]
    ) -> CompilerResults:
        """

        :param options:
        :param compilationUnits:
        :return:
        """
    def CompileAssemblyFromFile(
        self, options: CompilerParameters, fileNames: Array[str]
    ) -> CompilerResults:
        """

        :param options:
        :param fileNames:
        :return:
        """
    def CompileAssemblyFromSource(
        self, options: CompilerParameters, sources: Array[str]
    ) -> CompilerResults:
        """

        :param options:
        :param sources:
        :return:
        """
    def CreateCompiler(self) -> ICodeCompiler:
        """

        :return:
        """
    def CreateEscapedIdentifier(self, value: str) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def CreateGenerator(self) -> ICodeGenerator:
        """

        :return:
        """
    @overload
    def CreateGenerator(self, output: TextWriter) -> ICodeGenerator:
        """

        :param output:
        :return:
        """
    @overload
    def CreateGenerator(self, fileName: str) -> ICodeGenerator:
        """

        :param fileName:
        :return:
        """
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def CreateParser(self) -> ICodeParser:
        """

        :return:
        """
    @classmethod
    @overload
    def CreateProvider(cls, language: str) -> CodeDomProvider:
        """

        :param language:
        :return:
        """
    @classmethod
    @overload
    def CreateProvider(
        cls, language: str, providerOptions: IDictionary[str, str]
    ) -> CodeDomProvider:
        """

        :param language:
        :param providerOptions:
        :return:
        """
    def CreateValidIdentifier(self, value: str) -> str:
        """

        :param value:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GenerateCodeFromCompileUnit(
        self, compileUnit: CodeCompileUnit, writer: TextWriter, options: CodeGeneratorOptions
    ) -> None:
        """

        :param compileUnit:
        :param writer:
        :param options:
        """
    def GenerateCodeFromExpression(
        self, expression: CodeExpression, writer: TextWriter, options: CodeGeneratorOptions
    ) -> None:
        """

        :param expression:
        :param writer:
        :param options:
        """
    def GenerateCodeFromMember(
        self, member: CodeTypeMember, writer: TextWriter, options: CodeGeneratorOptions
    ) -> None:
        """

        :param member:
        :param writer:
        :param options:
        """
    def GenerateCodeFromNamespace(
        self, codeNamespace: CodeNamespace, writer: TextWriter, options: CodeGeneratorOptions
    ) -> None:
        """

        :param codeNamespace:
        :param writer:
        :param options:
        """
    def GenerateCodeFromStatement(
        self, statement: CodeStatement, writer: TextWriter, options: CodeGeneratorOptions
    ) -> None:
        """

        :param statement:
        :param writer:
        :param options:
        """
    def GenerateCodeFromType(
        self, codeType: CodeTypeDeclaration, writer: TextWriter, options: CodeGeneratorOptions
    ) -> None:
        """

        :param codeType:
        :param writer:
        :param options:
        """
    @classmethod
    def GetAllCompilerInfo(cls) -> Array[CompilerInfo]:
        """

        :return:
        """
    @classmethod
    def GetCompilerInfo(cls, language: str) -> CompilerInfo:
        """

        :param language:
        :return:
        """
    def GetConverter(self, type: Type) -> TypeConverter:
        """

        :param type:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @classmethod
    def GetLanguageFromExtension(cls, extension: str) -> str:
        """

        :param extension:
        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeOutput(self, type: CodeTypeReference) -> str:
        """

        :param type:
        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    @classmethod
    def IsDefinedExtension(cls, extension: str) -> bool:
        """

        :param extension:
        :return:
        """
    @classmethod
    def IsDefinedLanguage(cls, language: str) -> bool:
        """

        :param language:
        :return:
        """
    def IsValidIdentifier(self, value: str) -> bool:
        """

        :param value:
        :return:
        """
    def Parse(self, codeStream: TextReader) -> CodeCompileUnit:
        """

        :param codeStream:
        :return:
        """
    def Supports(self, generatorSupport: GeneratorSupport) -> bool:
        """

        :param generatorSupport:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    Disposed: EventType[EventHandler] = ...
    """"""

class CodeGenerator(ABC, Object, ICodeGenerator):
    """"""

    def CreateEscapedIdentifier(self, value: str) -> str:
        """

        :param value:
        :return:
        """
    def CreateValidIdentifier(self, value: str) -> str:
        """

        :param value:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GenerateCodeFromCompileUnit(
        self, e: CodeCompileUnit, w: TextWriter, o: CodeGeneratorOptions
    ) -> None:
        """

        :param e:
        :param w:
        :param o:
        """
    def GenerateCodeFromExpression(
        self, e: CodeExpression, w: TextWriter, o: CodeGeneratorOptions
    ) -> None:
        """

        :param e:
        :param w:
        :param o:
        """
    def GenerateCodeFromMember(
        self, member: CodeTypeMember, writer: TextWriter, options: CodeGeneratorOptions
    ) -> None:
        """

        :param member:
        :param writer:
        :param options:
        """
    def GenerateCodeFromNamespace(
        self, e: CodeNamespace, w: TextWriter, o: CodeGeneratorOptions
    ) -> None:
        """

        :param e:
        :param w:
        :param o:
        """
    def GenerateCodeFromStatement(
        self, e: CodeStatement, w: TextWriter, o: CodeGeneratorOptions
    ) -> None:
        """

        :param e:
        :param w:
        :param o:
        """
    def GenerateCodeFromType(
        self, e: CodeTypeDeclaration, w: TextWriter, o: CodeGeneratorOptions
    ) -> None:
        """

        :param e:
        :param w:
        :param o:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeOutput(self, type: CodeTypeReference) -> str:
        """

        :param type:
        :return:
        """
    def IsValidIdentifier(self, value: str) -> bool:
        """

        :param value:
        :return:
        """
    @classmethod
    def IsValidLanguageIndependentIdentifier(cls, value: str) -> bool:
        """

        :param value:
        :return:
        """
    def Supports(self, supports: GeneratorSupport) -> bool:
        """

        :param supports:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def ValidateIdentifier(self, value: str) -> None:
        """

        :param value:
        """
    @classmethod
    def ValidateIdentifiers(cls, e: CodeObject) -> None:
        """

        :param e:
        """

class CodeGeneratorOptions(Object):
    """"""

    def __init__(self):
        """"""
    @property
    def BlankLinesBetweenMembers(self) -> bool:
        """

        :return:
        """
    @BlankLinesBetweenMembers.setter
    def BlankLinesBetweenMembers(self, value: bool) -> None: ...
    @property
    def BracingStyle(self) -> str:
        """

        :return:
        """
    @BracingStyle.setter
    def BracingStyle(self, value: str) -> None: ...
    @property
    def ElseOnClosing(self) -> bool:
        """

        :return:
        """
    @ElseOnClosing.setter
    def ElseOnClosing(self, value: bool) -> None: ...
    @property
    def IndentString(self) -> str:
        """

        :return:
        """
    @IndentString.setter
    def IndentString(self, value: str) -> None: ...
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def VerbatimOrder(self) -> bool:
        """

        :return:
        """
    @VerbatimOrder.setter
    def VerbatimOrder(self, value: bool) -> None: ...
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
    def __getitem__(self, index: str) -> object:
        """

        :param index:
        :return:
        """
    def __setitem__(self, index: str, value: object) -> None:
        """

        :param index:
        :param value:
        """

class CodeParser(ABC, Object, ICodeParser):
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
    def Parse(self, codeStream: TextReader) -> CodeCompileUnit:
        """

        :param codeStream:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CodeValidator(Object):
    """"""

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

class CompilerError(Object):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, fileName: str, line: int, column: int, errorNumber: str, errorText: str):
        """

        :param fileName:
        :param line:
        :param column:
        :param errorNumber:
        :param errorText:
        """
    @property
    def Column(self) -> int:
        """

        :return:
        """
    @Column.setter
    def Column(self, value: int) -> None: ...
    @property
    def ErrorNumber(self) -> str:
        """

        :return:
        """
    @ErrorNumber.setter
    def ErrorNumber(self, value: str) -> None: ...
    @property
    def ErrorText(self) -> str:
        """

        :return:
        """
    @ErrorText.setter
    def ErrorText(self, value: str) -> None: ...
    @property
    def FileName(self) -> str:
        """

        :return:
        """
    @FileName.setter
    def FileName(self, value: str) -> None: ...
    @property
    def IsWarning(self) -> bool:
        """

        :return:
        """
    @IsWarning.setter
    def IsWarning(self, value: bool) -> None: ...
    @property
    def Line(self) -> int:
        """

        :return:
        """
    @Line.setter
    def Line(self, value: int) -> None: ...
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

class CompilerErrorCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, value: CompilerErrorCollection):
        """

        :param value:
        """
    @overload
    def __init__(self, value: Array[CompilerError]):
        """

        :param value:
        """
    @property
    def Capacity(self) -> int:
        """

        :return:
        """
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def HasErrors(self) -> bool:
        """

        :return:
        """
    @property
    def HasWarnings(self) -> bool:
        """

        :return:
        """
    @property
    def IsFixedSize(self) -> bool:
        """

        :return:
        """
    @property
    def IsReadOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def Item(self) -> object:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @overload
    def Add(self, value: CompilerError) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Add(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def AddRange(self, value: CompilerErrorCollection) -> None:
        """

        :param value:
        """
    @overload
    def AddRange(self, value: Array[CompilerError]) -> None:
        """

        :param value:
        """
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: CompilerError) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def Contains(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, array: Array[CompilerError], index: int) -> None:
        """

        :param array:
        :param index:
        """
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
    @overload
    def IndexOf(self, value: CompilerError) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def IndexOf(self, value: object) -> int:
        """

        :param value:
        :return:
        """
    @overload
    def Insert(self, index: int, value: CompilerError) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Insert(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def Remove(self, value: CompilerError) -> None:
        """

        :param value:
        """
    @overload
    def Remove(self, value: object) -> None:
        """

        :param value:
        """
    def RemoveAt(self, index: int) -> None:
        """

        :param index:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __getitem__(self, index: int) -> object:
        """

        :param index:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
    @overload
    def __setitem__(self, index: int, value: CompilerError) -> None:
        """

        :param index:
        :param value:
        """
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """

        :param index:
        :param value:
        """

class CompilerInfo(Object):
    """"""

    @property
    def CodeDomProviderType(self) -> Type:
        """

        :return:
        """
    @property
    def IsCodeDomProviderTypeValid(self) -> bool:
        """

        :return:
        """
    def CreateDefaultCompilerParameters(self) -> CompilerParameters:
        """

        :return:
        """
    @overload
    def CreateProvider(self) -> CodeDomProvider:
        """

        :return:
        """
    @overload
    def CreateProvider(self, providerOptions: IDictionary[str, str]) -> CodeDomProvider:
        """

        :param providerOptions:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetExtensions(self) -> Array[str]:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLanguages(self) -> Array[str]:
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

class CompilerParameters(Object):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, assemblyNames: Array[str]):
        """

        :param assemblyNames:
        """
    @overload
    def __init__(self, assemblyNames: Array[str], outputName: str):
        """

        :param assemblyNames:
        :param outputName:
        """
    @overload
    def __init__(self, assemblyNames: Array[str], outputName: str, includeDebugInformation: bool):
        """

        :param assemblyNames:
        :param outputName:
        :param includeDebugInformation:
        """
    @property
    def CompilerOptions(self) -> str:
        """

        :return:
        """
    @CompilerOptions.setter
    def CompilerOptions(self, value: str) -> None: ...
    @property
    def CoreAssemblyFileName(self) -> str:
        """

        :return:
        """
    @CoreAssemblyFileName.setter
    def CoreAssemblyFileName(self, value: str) -> None: ...
    @property
    def EmbeddedResources(self) -> StringCollection:
        """

        :return:
        """
    @property
    def Evidence(self) -> Evidence:
        """

        :return:
        """
    @Evidence.setter
    def Evidence(self, value: Evidence) -> None: ...
    @property
    def GenerateExecutable(self) -> bool:
        """

        :return:
        """
    @GenerateExecutable.setter
    def GenerateExecutable(self, value: bool) -> None: ...
    @property
    def GenerateInMemory(self) -> bool:
        """

        :return:
        """
    @GenerateInMemory.setter
    def GenerateInMemory(self, value: bool) -> None: ...
    @property
    def IncludeDebugInformation(self) -> bool:
        """

        :return:
        """
    @IncludeDebugInformation.setter
    def IncludeDebugInformation(self, value: bool) -> None: ...
    @property
    def LinkedResources(self) -> StringCollection:
        """

        :return:
        """
    @property
    def MainClass(self) -> str:
        """

        :return:
        """
    @MainClass.setter
    def MainClass(self, value: str) -> None: ...
    @property
    def OutputAssembly(self) -> str:
        """

        :return:
        """
    @OutputAssembly.setter
    def OutputAssembly(self, value: str) -> None: ...
    @property
    def ReferencedAssemblies(self) -> StringCollection:
        """

        :return:
        """
    @property
    def TempFiles(self) -> TempFileCollection:
        """

        :return:
        """
    @TempFiles.setter
    def TempFiles(self, value: TempFileCollection) -> None: ...
    @property
    def TreatWarningsAsErrors(self) -> bool:
        """

        :return:
        """
    @TreatWarningsAsErrors.setter
    def TreatWarningsAsErrors(self, value: bool) -> None: ...
    @property
    def UserToken(self) -> IntPtr:
        """

        :return:
        """
    @UserToken.setter
    def UserToken(self, value: IntPtr) -> None: ...
    @property
    def WarningLevel(self) -> int:
        """

        :return:
        """
    @WarningLevel.setter
    def WarningLevel(self, value: int) -> None: ...
    @property
    def Win32Resource(self) -> str:
        """

        :return:
        """
    @Win32Resource.setter
    def Win32Resource(self, value: str) -> None: ...
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

class CompilerResults(Object):
    """"""

    def __init__(self, tempFiles: TempFileCollection):
        """

        :param tempFiles:
        """
    @property
    def CompiledAssembly(self) -> Assembly:
        """

        :return:
        """
    @CompiledAssembly.setter
    def CompiledAssembly(self, value: Assembly) -> None: ...
    @property
    def Errors(self) -> CompilerErrorCollection:
        """

        :return:
        """
    @property
    def Evidence(self) -> Evidence:
        """

        :return:
        """
    @Evidence.setter
    def Evidence(self, value: Evidence) -> None: ...
    @property
    def NativeCompilerReturnValue(self) -> int:
        """

        :return:
        """
    @NativeCompilerReturnValue.setter
    def NativeCompilerReturnValue(self, value: int) -> None: ...
    @property
    def Output(self) -> StringCollection:
        """

        :return:
        """
    @property
    def PathToAssembly(self) -> str:
        """

        :return:
        """
    @PathToAssembly.setter
    def PathToAssembly(self, value: str) -> None: ...
    @property
    def TempFiles(self) -> TempFileCollection:
        """

        :return:
        """
    @TempFiles.setter
    def TempFiles(self, value: TempFileCollection) -> None: ...
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

class Executor(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def ExecWait(cls, cmd: str, tempFiles: TempFileCollection) -> None:
        """

        :param cmd:
        :param tempFiles:
        """
    @classmethod
    @overload
    def ExecWaitWithCapture(
        cls, cmd: str, tempFiles: TempFileCollection, outputName: str, errorName: str
    ) -> int:
        """

        :param cmd:
        :param tempFiles:
        :param outputName:
        :param errorName:
        :return:
        """
    @classmethod
    @overload
    def ExecWaitWithCapture(
        cls,
        userToken: IntPtr,
        cmd: str,
        tempFiles: TempFileCollection,
        outputName: str,
        errorName: str,
    ) -> int:
        """

        :param userToken:
        :param cmd:
        :param tempFiles:
        :param outputName:
        :param errorName:
        :return:
        """
    @classmethod
    @overload
    def ExecWaitWithCapture(
        cls,
        cmd: str,
        currentDir: str,
        tempFiles: TempFileCollection,
        outputName: str,
        errorName: str,
    ) -> int:
        """

        :param cmd:
        :param currentDir:
        :param tempFiles:
        :param outputName:
        :param errorName:
        :return:
        """
    @classmethod
    @overload
    def ExecWaitWithCapture(
        cls,
        userToken: IntPtr,
        cmd: str,
        currentDir: str,
        tempFiles: TempFileCollection,
        outputName: str,
        errorName: str,
    ) -> int:
        """

        :param userToken:
        :param cmd:
        :param currentDir:
        :param tempFiles:
        :param outputName:
        :param errorName:
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

class FileIntegrity(ABC, Object):
    """"""

    @classmethod
    @property
    def IsEnabled(cls) -> bool:
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
    @classmethod
    def IsTrusted(cls, safeFileHandle: SafeFileHandle) -> bool:
        """

        :param safeFileHandle:
        :return:
        """
    @classmethod
    def MarkAsTrusted(cls, safeFileHandle: SafeFileHandle) -> None:
        """

        :param safeFileHandle:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class GeneratedCodeAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, tool: str, version: str):
        """

        :param tool:
        :param version:
        """
    @property
    def Tool(self) -> str:
        """

        :return:
        """
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Version(self) -> str:
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
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    def Invoke(
        self,
        dispIdMember: int,
        riid: Guid,
        lcid: int,
        wFlags: int,
        pDispParams: IntPtr,
        pVarResult: IntPtr,
        pExcepInfo: IntPtr,
        puArgErr: IntPtr,
    ) -> None:
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class GeneratorSupport(Enum):
    """"""

    ArraysOfArrays: GeneratorSupport = ...
    """"""
    EntryPointMethod: GeneratorSupport = ...
    """"""
    GotoStatements: GeneratorSupport = ...
    """"""
    MultidimensionalArrays: GeneratorSupport = ...
    """"""
    StaticConstructors: GeneratorSupport = ...
    """"""
    TryCatchStatements: GeneratorSupport = ...
    """"""
    ReturnTypeAttributes: GeneratorSupport = ...
    """"""
    DeclareValueTypes: GeneratorSupport = ...
    """"""
    DeclareEnums: GeneratorSupport = ...
    """"""
    DeclareDelegates: GeneratorSupport = ...
    """"""
    DeclareInterfaces: GeneratorSupport = ...
    """"""
    DeclareEvents: GeneratorSupport = ...
    """"""
    AssemblyAttributes: GeneratorSupport = ...
    """"""
    ParameterAttributes: GeneratorSupport = ...
    """"""
    ReferenceParameters: GeneratorSupport = ...
    """"""
    ChainedConstructorArguments: GeneratorSupport = ...
    """"""
    NestedTypes: GeneratorSupport = ...
    """"""
    MultipleInterfaceMembers: GeneratorSupport = ...
    """"""
    PublicStaticMembers: GeneratorSupport = ...
    """"""
    ComplexExpressions: GeneratorSupport = ...
    """"""
    Win32Resources: GeneratorSupport = ...
    """"""
    Resources: GeneratorSupport = ...
    """"""
    PartialTypes: GeneratorSupport = ...
    """"""
    GenericTypeReference: GeneratorSupport = ...
    """"""
    GenericTypeDeclaration: GeneratorSupport = ...
    """"""
    DeclareIndexerProperties: GeneratorSupport = ...
    """"""

class HandlerBase(ABC, Object):
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

class ICodeCompiler:
    """"""

    def CompileAssemblyFromDom(
        self, options: CompilerParameters, compilationUnit: CodeCompileUnit
    ) -> CompilerResults:
        """

        :param options:
        :param compilationUnit:
        :return:
        """
    def CompileAssemblyFromDomBatch(
        self, options: CompilerParameters, compilationUnits: Array[CodeCompileUnit]
    ) -> CompilerResults:
        """

        :param options:
        :param compilationUnits:
        :return:
        """
    def CompileAssemblyFromFile(
        self, options: CompilerParameters, fileName: str
    ) -> CompilerResults:
        """

        :param options:
        :param fileName:
        :return:
        """
    def CompileAssemblyFromFileBatch(
        self, options: CompilerParameters, fileNames: Array[str]
    ) -> CompilerResults:
        """

        :param options:
        :param fileNames:
        :return:
        """
    def CompileAssemblyFromSource(
        self, options: CompilerParameters, source: str
    ) -> CompilerResults:
        """

        :param options:
        :param source:
        :return:
        """
    def CompileAssemblyFromSourceBatch(
        self, options: CompilerParameters, sources: Array[str]
    ) -> CompilerResults:
        """

        :param options:
        :param sources:
        :return:
        """

class ICodeGenerator:
    """"""

    def CreateEscapedIdentifier(self, value: str) -> str:
        """

        :param value:
        :return:
        """
    def CreateValidIdentifier(self, value: str) -> str:
        """

        :param value:
        :return:
        """
    def GenerateCodeFromCompileUnit(
        self, e: CodeCompileUnit, w: TextWriter, o: CodeGeneratorOptions
    ) -> None:
        """

        :param e:
        :param w:
        :param o:
        """
    def GenerateCodeFromExpression(
        self, e: CodeExpression, w: TextWriter, o: CodeGeneratorOptions
    ) -> None:
        """

        :param e:
        :param w:
        :param o:
        """
    def GenerateCodeFromNamespace(
        self, e: CodeNamespace, w: TextWriter, o: CodeGeneratorOptions
    ) -> None:
        """

        :param e:
        :param w:
        :param o:
        """
    def GenerateCodeFromStatement(
        self, e: CodeStatement, w: TextWriter, o: CodeGeneratorOptions
    ) -> None:
        """

        :param e:
        :param w:
        :param o:
        """
    def GenerateCodeFromType(
        self, e: CodeTypeDeclaration, w: TextWriter, o: CodeGeneratorOptions
    ) -> None:
        """

        :param e:
        :param w:
        :param o:
        """
    def GetTypeOutput(self, type: CodeTypeReference) -> str:
        """

        :param type:
        :return:
        """
    def IsValidIdentifier(self, value: str) -> bool:
        """

        :param value:
        :return:
        """
    def Supports(self, supports: GeneratorSupport) -> bool:
        """

        :param supports:
        :return:
        """
    def ValidateIdentifier(self, value: str) -> None:
        """

        :param value:
        """

class ICodeParser:
    """"""

    def Parse(self, codeStream: TextReader) -> CodeCompileUnit:
        """

        :param codeStream:
        :return:
        """

class Indentation(Object):
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

class IndentedTextWriter(TextWriter, IDisposable):
    """"""

    DefaultTabString: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, writer: TextWriter):
        """

        :param writer:
        """
    @overload
    def __init__(self, writer: TextWriter, tabString: str):
        """

        :param writer:
        :param tabString:
        """
    @property
    def Encoding(self) -> Encoding:
        """

        :return:
        """
    @property
    def FormatProvider(self) -> IFormatProvider:
        """

        :return:
        """
    @property
    def Indent(self) -> int:
        """

        :return:
        """
    @Indent.setter
    def Indent(self, value: int) -> None: ...
    @property
    def InnerWriter(self) -> TextWriter:
        """

        :return:
        """
    @property
    def NewLine(self) -> str:
        """

        :return:
        """
    @NewLine.setter
    def NewLine(self, value: str) -> None: ...
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Flush(self) -> None:
        """"""
    def FlushAsync(self) -> Task:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetLifetimeService(self) -> object:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def Write(self, buffer: Array[Char]) -> None:
        """

        :param buffer:
        """
    @overload
    def Write(self, value: bool) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: Char) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: Decimal) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: float) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: object) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: float) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: str) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def Write(self, format: str, arg: Array[object]) -> None:
        """

        :param format:
        :param arg:
        """
    @overload
    def Write(self, format: str, arg0: object) -> None:
        """

        :param format:
        :param arg0:
        """
    @overload
    def Write(self, buffer: Array[Char], index: int, count: int) -> None:
        """

        :param buffer:
        :param index:
        :param count:
        """
    @overload
    def Write(self, format: str, arg0: object, arg1: object) -> None:
        """

        :param format:
        :param arg0:
        :param arg1:
        """
    @overload
    def Write(self, format: str, arg0: object, arg1: object, arg2: object) -> None:
        """

        :param format:
        :param arg0:
        :param arg1:
        :param arg2:
        """
    @overload
    def WriteAsync(self, buffer: Array[Char]) -> Task:
        """

        :param buffer:
        :return:
        """
    @overload
    def WriteAsync(self, value: Char) -> Task:
        """

        :param value:
        :return:
        """
    @overload
    def WriteAsync(self, value: str) -> Task:
        """

        :param value:
        :return:
        """
    @overload
    def WriteAsync(self, buffer: Array[Char], index: int, count: int) -> Task:
        """

        :param buffer:
        :param index:
        :param count:
        :return:
        """
    @overload
    def WriteLine(self) -> None:
        """"""
    @overload
    def WriteLine(self, buffer: Array[Char]) -> None:
        """

        :param buffer:
        """
    @overload
    def WriteLine(self, value: bool) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: Char) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: Decimal) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: float) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: object) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: float) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: str) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, value: int) -> None:
        """

        :param value:
        """
    @overload
    def WriteLine(self, format: str, arg: Array[object]) -> None:
        """

        :param format:
        :param arg:
        """
    @overload
    def WriteLine(self, format: str, arg0: object) -> None:
        """

        :param format:
        :param arg0:
        """
    @overload
    def WriteLine(self, buffer: Array[Char], index: int, count: int) -> None:
        """

        :param buffer:
        :param index:
        :param count:
        """
    @overload
    def WriteLine(self, format: str, arg0: object, arg1: object) -> None:
        """

        :param format:
        :param arg0:
        :param arg1:
        """
    @overload
    def WriteLine(self, format: str, arg0: object, arg1: object, arg2: object) -> None:
        """

        :param format:
        :param arg0:
        :param arg1:
        :param arg2:
        """
    @overload
    def WriteLineAsync(self) -> Task:
        """

        :return:
        """
    @overload
    def WriteLineAsync(self, buffer: Array[Char]) -> Task:
        """

        :param buffer:
        :return:
        """
    @overload
    def WriteLineAsync(self, value: Char) -> Task:
        """

        :param value:
        :return:
        """
    @overload
    def WriteLineAsync(self, value: str) -> Task:
        """

        :param value:
        :return:
        """
    @overload
    def WriteLineAsync(self, buffer: Array[Char], index: int, count: int) -> Task:
        """

        :param buffer:
        :param index:
        :param count:
        :return:
        """
    def WriteLineNoTabs(self, s: str) -> None:
        """

        :param s:
        """

class LanguageOptions(Enum):
    """"""

    _None: LanguageOptions = ...
    """"""
    CaseInsensitive: LanguageOptions = ...
    """"""

class RedistVersionInfo(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def GetCompilerPath(cls, provOptions: IDictionary[str, str], compilerExecutable: str) -> str:
        """

        :param provOptions:
        :param compilerExecutable:
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

class TempFileCollection(Object, ICollection, IEnumerable, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, tempDir: str):
        """

        :param tempDir:
        """
    @overload
    def __init__(self, tempDir: str, keepFiles: bool):
        """

        :param tempDir:
        :param keepFiles:
        """
    @property
    def BasePath(self) -> str:
        """

        :return:
        """
    @property
    def Count(self) -> int:
        """

        :return:
        """
    @property
    def IsSynchronized(self) -> bool:
        """

        :return:
        """
    @property
    def KeepFiles(self) -> bool:
        """

        :return:
        """
    @KeepFiles.setter
    def KeepFiles(self, value: bool) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """

        :return:
        """
    @property
    def TempDir(self) -> str:
        """

        :return:
        """
    @overload
    def AddExtension(self, fileExtension: str) -> str:
        """

        :param fileExtension:
        :return:
        """
    @overload
    def AddExtension(self, fileExtension: str, keepFile: bool) -> str:
        """

        :param fileExtension:
        :param keepFile:
        :return:
        """
    def AddFile(self, fileName: str, keepFile: bool) -> None:
        """

        :param fileName:
        :param keepFile:
        """
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """

        :param array:
        :param index:
        """
    @overload
    def CopyTo(self, fileNames: Array[str], start: int) -> None:
        """

        :param fileNames:
        :param start:
        """
    def Delete(self) -> None:
        """"""
    def Dispose(self) -> None:
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
    def __contains__(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    def __len__(self) -> int:
        """

        :return:
        """
