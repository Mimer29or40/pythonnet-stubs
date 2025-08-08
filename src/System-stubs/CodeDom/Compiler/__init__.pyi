"""Automatically generated stubs for C# namespace: System.CodeDom.Compiler."""

from abc import ABC
from collections.abc import Iterator
from typing import ClassVar
from typing import Self
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
from System import String
from System import Type
from System import UInt32
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

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

class CodeCompiler(ABC, CodeGenerator, ICodeCompiler, ICodeGenerator):
    """"""
    def CompileAssemblyFromDom(
        self, options: CompilerParameters, compilationUnit: CodeCompileUnit
    ) -> CompilerResults:
        """"""
    def CompileAssemblyFromDomBatch(
        self, options: CompilerParameters, compilationUnits: Array[CodeCompileUnit]
    ) -> CompilerResults:
        """"""
    def CompileAssemblyFromFile(
        self, options: CompilerParameters, fileName: str
    ) -> CompilerResults:
        """"""
    def CompileAssemblyFromFileBatch(
        self, options: CompilerParameters, fileNames: Array[str]
    ) -> CompilerResults:
        """"""
    def CompileAssemblyFromSource(
        self, options: CompilerParameters, source: str
    ) -> CompilerResults:
        """"""
    def CompileAssemblyFromSourceBatch(
        self, options: CompilerParameters, sources: Array[str]
    ) -> CompilerResults:
        """"""
    def CreateEscapedIdentifier(self, value: str) -> str:
        """"""
    def CreateValidIdentifier(self, value: str) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GenerateCodeFromCompileUnit(
        self, e: CodeCompileUnit, w: TextWriter, o: CodeGeneratorOptions
    ) -> None:
        """"""
    def GenerateCodeFromExpression(
        self, e: CodeExpression, w: TextWriter, o: CodeGeneratorOptions
    ) -> None:
        """"""
    def GenerateCodeFromMember(
        self, member: CodeTypeMember, writer: TextWriter, options: CodeGeneratorOptions
    ) -> None:
        """"""
    def GenerateCodeFromNamespace(
        self, e: CodeNamespace, w: TextWriter, o: CodeGeneratorOptions
    ) -> None:
        """"""
    def GenerateCodeFromStatement(
        self, e: CodeStatement, w: TextWriter, o: CodeGeneratorOptions
    ) -> None:
        """"""
    def GenerateCodeFromType(
        self, e: CodeTypeDeclaration, w: TextWriter, o: CodeGeneratorOptions
    ) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeOutput(self, type: CodeTypeReference) -> str:
        """"""
    def IsValidIdentifier(self, value: str) -> bool:
        """"""
    def Supports(self, supports: GeneratorSupport) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def ValidateIdentifier(self, value: str) -> None:
        """"""

class CodeDomCompilationConfiguration(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CodeDomConfigurationHandler(Object, IConfigurationSectionHandler):
    """"""
    def Create(self, inheritedObject: object, configContextObj: object, node: XmlNode) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CodeDomProvider(ABC, Component, IComponent, IDisposable):
    """"""
    @property
    def Container(self) -> IContainer:
        """"""
    @property
    def FileExtension(self) -> str:
        """"""
    @property
    def LanguageOptions(self) -> LanguageOptions:
        """"""
    @property
    def Site(self) -> ISite:
        """"""
    @Site.setter
    def Site(self, value: ISite) -> None: ...
    def CompileAssemblyFromDom(
        self, options: CompilerParameters, compilationUnits: Array[CodeCompileUnit]
    ) -> CompilerResults:
        """"""
    def CompileAssemblyFromFile(
        self, options: CompilerParameters, fileNames: Array[str]
    ) -> CompilerResults:
        """"""
    def CompileAssemblyFromSource(
        self, options: CompilerParameters, sources: Array[str]
    ) -> CompilerResults:
        """"""
    def CreateCompiler(self) -> ICodeCompiler:
        """"""
    def CreateEscapedIdentifier(self, value: str) -> str:
        """"""
    @overload
    def CreateGenerator(self) -> ICodeGenerator:
        """"""
    @overload
    def CreateGenerator(self, output: TextWriter) -> ICodeGenerator:
        """"""
    @overload
    def CreateGenerator(self, fileName: str) -> ICodeGenerator:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def CreateParser(self) -> ICodeParser:
        """"""
    @classmethod
    @overload
    def CreateProvider(cls, language: str) -> CodeDomProvider:
        """"""
    @classmethod
    @overload
    def CreateProvider(
        cls, language: str, providerOptions: IDictionary[str, str]
    ) -> CodeDomProvider:
        """"""
    def CreateValidIdentifier(self, value: str) -> str:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GenerateCodeFromCompileUnit(
        self, compileUnit: CodeCompileUnit, writer: TextWriter, options: CodeGeneratorOptions
    ) -> None:
        """"""
    def GenerateCodeFromExpression(
        self, expression: CodeExpression, writer: TextWriter, options: CodeGeneratorOptions
    ) -> None:
        """"""
    def GenerateCodeFromMember(
        self, member: CodeTypeMember, writer: TextWriter, options: CodeGeneratorOptions
    ) -> None:
        """"""
    def GenerateCodeFromNamespace(
        self, codeNamespace: CodeNamespace, writer: TextWriter, options: CodeGeneratorOptions
    ) -> None:
        """"""
    def GenerateCodeFromStatement(
        self, statement: CodeStatement, writer: TextWriter, options: CodeGeneratorOptions
    ) -> None:
        """"""
    def GenerateCodeFromType(
        self, codeType: CodeTypeDeclaration, writer: TextWriter, options: CodeGeneratorOptions
    ) -> None:
        """"""
    @classmethod
    def GetAllCompilerInfo(cls) -> Array[CompilerInfo]:
        """"""
    @classmethod
    def GetCompilerInfo(cls, language: str) -> CompilerInfo:
        """"""
    def GetConverter(self, type: Type) -> TypeConverter:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetLanguageFromExtension(cls, extension: str) -> str:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeOutput(self, type: CodeTypeReference) -> str:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    @classmethod
    def IsDefinedExtension(cls, extension: str) -> bool:
        """"""
    @classmethod
    def IsDefinedLanguage(cls, language: str) -> bool:
        """"""
    def IsValidIdentifier(self, value: str) -> bool:
        """"""
    def Parse(self, codeStream: TextReader) -> CodeCompileUnit:
        """"""
    def Supports(self, generatorSupport: GeneratorSupport) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    Disposed: EventType[EventHandler] = ...
    """"""

class CodeGenerator(ABC, Object, ICodeGenerator):
    """"""
    def CreateEscapedIdentifier(self, value: str) -> str:
        """"""
    def CreateValidIdentifier(self, value: str) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GenerateCodeFromCompileUnit(
        self, e: CodeCompileUnit, w: TextWriter, o: CodeGeneratorOptions
    ) -> None:
        """"""
    def GenerateCodeFromExpression(
        self, e: CodeExpression, w: TextWriter, o: CodeGeneratorOptions
    ) -> None:
        """"""
    def GenerateCodeFromMember(
        self, member: CodeTypeMember, writer: TextWriter, options: CodeGeneratorOptions
    ) -> None:
        """"""
    def GenerateCodeFromNamespace(
        self, e: CodeNamespace, w: TextWriter, o: CodeGeneratorOptions
    ) -> None:
        """"""
    def GenerateCodeFromStatement(
        self, e: CodeStatement, w: TextWriter, o: CodeGeneratorOptions
    ) -> None:
        """"""
    def GenerateCodeFromType(
        self, e: CodeTypeDeclaration, w: TextWriter, o: CodeGeneratorOptions
    ) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeOutput(self, type: CodeTypeReference) -> str:
        """"""
    def IsValidIdentifier(self, value: str) -> bool:
        """"""
    @classmethod
    def IsValidLanguageIndependentIdentifier(cls, value: str) -> bool:
        """"""
    def Supports(self, supports: GeneratorSupport) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def ValidateIdentifier(self, value: str) -> None:
        """"""
    @classmethod
    def ValidateIdentifiers(cls, e: CodeObject) -> None:
        """"""

class CodeGeneratorOptions(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def BlankLinesBetweenMembers(self) -> bool:
        """"""
    @BlankLinesBetweenMembers.setter
    def BlankLinesBetweenMembers(self, value: bool) -> None: ...
    @property
    def BracingStyle(self) -> str:
        """"""
    @BracingStyle.setter
    def BracingStyle(self, value: str) -> None: ...
    @property
    def ElseOnClosing(self) -> bool:
        """"""
    @ElseOnClosing.setter
    def ElseOnClosing(self, value: bool) -> None: ...
    @property
    def IndentString(self) -> str:
        """"""
    @IndentString.setter
    def IndentString(self, value: str) -> None: ...
    @property
    def Item(self) -> object:
        """"""
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def VerbatimOrder(self) -> bool:
        """"""
    @VerbatimOrder.setter
    def VerbatimOrder(self, value: bool) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __getitem__(self, index: str) -> object:
        """"""
    def __setitem__(self, index: str, value: object) -> None:
        """"""

class CodeParser(ABC, Object, ICodeParser):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Parse(self, codeStream: TextReader) -> CodeCompileUnit:
        """"""
    def ToString(self) -> str:
        """"""

class CodeValidator(Object):
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

class CompilerError(Object):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(
        self, fileName: str, line: int, column: int, errorNumber: str, errorText: str
    ) -> None:
        """"""
    @property
    def Column(self) -> int:
        """"""
    @Column.setter
    def Column(self, value: int) -> None: ...
    @property
    def ErrorNumber(self) -> str:
        """"""
    @ErrorNumber.setter
    def ErrorNumber(self, value: str) -> None: ...
    @property
    def ErrorText(self) -> str:
        """"""
    @ErrorText.setter
    def ErrorText(self, value: str) -> None: ...
    @property
    def FileName(self) -> str:
        """"""
    @FileName.setter
    def FileName(self, value: str) -> None: ...
    @property
    def IsWarning(self) -> bool:
        """"""
    @IsWarning.setter
    def IsWarning(self, value: bool) -> None: ...
    @property
    def Line(self) -> int:
        """"""
    @Line.setter
    def Line(self, value: int) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CompilerErrorCollection(CollectionBase, ICollection, IEnumerable, IList):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, value: CompilerErrorCollection) -> None:
        """"""
    @overload
    def __init__(self, value: Array[CompilerError]) -> None:
        """"""
    @property
    def Capacity(self) -> int:
        """"""
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @property
    def Count(self) -> int:
        """"""
    @property
    def HasErrors(self) -> bool:
        """"""
    @property
    def HasWarnings(self) -> bool:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> CompilerError:
        """"""
    @Item.setter
    def Item(self, value: CompilerError) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @overload
    def Add(self, value: CompilerError) -> int:
        """"""
    @overload
    def Add(self, value: object) -> int:
        """"""
    @overload
    def AddRange(self, value: CompilerErrorCollection) -> None:
        """"""
    @overload
    def AddRange(self, value: Array[CompilerError]) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    @overload
    def Contains(self, value: CompilerError) -> bool:
        """"""
    @overload
    def Contains(self, value: object) -> bool:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array[CompilerError], index: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IndexOf(self, value: CompilerError) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    @overload
    def Insert(self, index: int, value: CompilerError) -> None:
        """"""
    @overload
    def Insert(self, index: int, value: object) -> None:
        """"""
    @overload
    def Remove(self, value: CompilerError) -> None:
        """"""
    @overload
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def __contains__(self, value: CompilerError) -> bool:
        """"""
    @overload
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, value: CompilerError) -> None:
        """"""
    @overload
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> CompilerError:
        """"""
    @overload
    def __setitem__(self, index: int, value: CompilerError) -> None:
        """"""
    @overload
    def __setitem__(self, index: int, value: object) -> None:
        """"""

class CompilerInfo(Object):
    """"""
    @property
    def CodeDomProviderType(self) -> Type:
        """"""
    @property
    def IsCodeDomProviderTypeValid(self) -> bool:
        """"""
    def CreateDefaultCompilerParameters(self) -> CompilerParameters:
        """"""
    @overload
    def CreateProvider(self) -> CodeDomProvider:
        """"""
    @overload
    def CreateProvider(self, providerOptions: IDictionary[str, str]) -> CodeDomProvider:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    def GetExtensions(self) -> Array[str]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLanguages(self) -> Array[str]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CompilerParameters(Object):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, assemblyNames: Array[str]) -> None:
        """"""
    @overload
    def __init__(self, assemblyNames: Array[str], outputName: str) -> None:
        """"""
    @overload
    def __init__(
        self, assemblyNames: Array[str], outputName: str, includeDebugInformation: bool
    ) -> None:
        """"""
    @property
    def CompilerOptions(self) -> str:
        """"""
    @CompilerOptions.setter
    def CompilerOptions(self, value: str) -> None: ...
    @property
    def CoreAssemblyFileName(self) -> str:
        """"""
    @CoreAssemblyFileName.setter
    def CoreAssemblyFileName(self, value: str) -> None: ...
    @property
    def EmbeddedResources(self) -> StringCollection:
        """"""
    @property
    def Evidence(self) -> Evidence:
        """"""
    @Evidence.setter
    def Evidence(self, value: Evidence) -> None: ...
    @property
    def GenerateExecutable(self) -> bool:
        """"""
    @GenerateExecutable.setter
    def GenerateExecutable(self, value: bool) -> None: ...
    @property
    def GenerateInMemory(self) -> bool:
        """"""
    @GenerateInMemory.setter
    def GenerateInMemory(self, value: bool) -> None: ...
    @property
    def IncludeDebugInformation(self) -> bool:
        """"""
    @IncludeDebugInformation.setter
    def IncludeDebugInformation(self, value: bool) -> None: ...
    @property
    def LinkedResources(self) -> StringCollection:
        """"""
    @property
    def MainClass(self) -> str:
        """"""
    @MainClass.setter
    def MainClass(self, value: str) -> None: ...
    @property
    def OutputAssembly(self) -> str:
        """"""
    @OutputAssembly.setter
    def OutputAssembly(self, value: str) -> None: ...
    @property
    def ReferencedAssemblies(self) -> StringCollection:
        """"""
    @property
    def TempFiles(self) -> TempFileCollection:
        """"""
    @TempFiles.setter
    def TempFiles(self, value: TempFileCollection) -> None: ...
    @property
    def TreatWarningsAsErrors(self) -> bool:
        """"""
    @TreatWarningsAsErrors.setter
    def TreatWarningsAsErrors(self, value: bool) -> None: ...
    @property
    def UserToken(self) -> IntPtr:
        """"""
    @UserToken.setter
    def UserToken(self, value: IntPtr) -> None: ...
    @property
    def WarningLevel(self) -> int:
        """"""
    @WarningLevel.setter
    def WarningLevel(self, value: int) -> None: ...
    @property
    def Win32Resource(self) -> str:
        """"""
    @Win32Resource.setter
    def Win32Resource(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CompilerResults(Object):
    """"""
    def __init__(self, tempFiles: TempFileCollection) -> None:
        """"""
    @property
    def CompiledAssembly(self) -> Assembly:
        """"""
    @CompiledAssembly.setter
    def CompiledAssembly(self, value: Assembly) -> None: ...
    @property
    def Errors(self) -> CompilerErrorCollection:
        """"""
    @property
    def Evidence(self) -> Evidence:
        """"""
    @Evidence.setter
    def Evidence(self, value: Evidence) -> None: ...
    @property
    def NativeCompilerReturnValue(self) -> int:
        """"""
    @NativeCompilerReturnValue.setter
    def NativeCompilerReturnValue(self, value: int) -> None: ...
    @property
    def Output(self) -> StringCollection:
        """"""
    @property
    def PathToAssembly(self) -> str:
        """"""
    @PathToAssembly.setter
    def PathToAssembly(self, value: str) -> None: ...
    @property
    def TempFiles(self) -> TempFileCollection:
        """"""
    @TempFiles.setter
    def TempFiles(self, value: TempFileCollection) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Executor(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def ExecWait(cls, cmd: str, tempFiles: TempFileCollection) -> None:
        """"""
    @classmethod
    @overload
    def ExecWaitWithCapture(
        cls,
        userToken: IntPtr,
        cmd: str,
        tempFiles: TempFileCollection,
        outputName: String,
        errorName: String,
    ) -> int:
        """"""
    @classmethod
    @overload
    def ExecWaitWithCapture(
        cls,
        userToken: IntPtr,
        cmd: str,
        currentDir: str,
        tempFiles: TempFileCollection,
        outputName: String,
        errorName: String,
    ) -> int:
        """"""
    @classmethod
    @overload
    def ExecWaitWithCapture(
        cls, cmd: str, tempFiles: TempFileCollection, outputName: String, errorName: String
    ) -> int:
        """"""
    @classmethod
    @overload
    def ExecWaitWithCapture(
        cls,
        cmd: str,
        currentDir: str,
        tempFiles: TempFileCollection,
        outputName: String,
        errorName: String,
    ) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class FileIntegrity(ABC, Object):
    """"""
    @classmethod
    @property
    def IsEnabled(cls) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsTrusted(cls, safeFileHandle: SafeFileHandle) -> bool:
        """"""
    @classmethod
    def MarkAsTrusted(cls, safeFileHandle: SafeFileHandle) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class GeneratedCodeAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, tool: str, version: str) -> None:
        """"""
    @property
    def Tool(self) -> str:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Version(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
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
        """"""
    def IsDefaultAttribute(self) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

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
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ICodeCompiler(ABC):
    """"""
    def CompileAssemblyFromDom(
        self, options: CompilerParameters, compilationUnit: CodeCompileUnit
    ) -> CompilerResults:
        """"""
    def CompileAssemblyFromDomBatch(
        self, options: CompilerParameters, compilationUnits: Array[CodeCompileUnit]
    ) -> CompilerResults:
        """"""
    def CompileAssemblyFromFile(
        self, options: CompilerParameters, fileName: str
    ) -> CompilerResults:
        """"""
    def CompileAssemblyFromFileBatch(
        self, options: CompilerParameters, fileNames: Array[str]
    ) -> CompilerResults:
        """"""
    def CompileAssemblyFromSource(
        self, options: CompilerParameters, source: str
    ) -> CompilerResults:
        """"""
    def CompileAssemblyFromSourceBatch(
        self, options: CompilerParameters, sources: Array[str]
    ) -> CompilerResults:
        """"""

class ICodeGenerator(ABC):
    """"""
    def CreateEscapedIdentifier(self, value: str) -> str:
        """"""
    def CreateValidIdentifier(self, value: str) -> str:
        """"""
    def GenerateCodeFromCompileUnit(
        self, e: CodeCompileUnit, w: TextWriter, o: CodeGeneratorOptions
    ) -> None:
        """"""
    def GenerateCodeFromExpression(
        self, e: CodeExpression, w: TextWriter, o: CodeGeneratorOptions
    ) -> None:
        """"""
    def GenerateCodeFromNamespace(
        self, e: CodeNamespace, w: TextWriter, o: CodeGeneratorOptions
    ) -> None:
        """"""
    def GenerateCodeFromStatement(
        self, e: CodeStatement, w: TextWriter, o: CodeGeneratorOptions
    ) -> None:
        """"""
    def GenerateCodeFromType(
        self, e: CodeTypeDeclaration, w: TextWriter, o: CodeGeneratorOptions
    ) -> None:
        """"""
    def GetTypeOutput(self, type: CodeTypeReference) -> str:
        """"""
    def IsValidIdentifier(self, value: str) -> bool:
        """"""
    def Supports(self, supports: GeneratorSupport) -> bool:
        """"""
    def ValidateIdentifier(self, value: str) -> None:
        """"""

class ICodeParser(ABC):
    """"""
    def Parse(self, codeStream: TextReader) -> CodeCompileUnit:
        """"""

class Indentation(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IndentedTextWriter(TextWriter, IDisposable):
    """"""

    DefaultTabString: ClassVar[str]
    """"""
    @overload
    def __init__(self, writer: TextWriter) -> None:
        """"""
    @overload
    def __init__(self, writer: TextWriter, tabString: str) -> None:
        """"""
    @property
    def Encoding(self) -> Encoding:
        """"""
    @property
    def FormatProvider(self) -> IFormatProvider:
        """"""
    @property
    def Indent(self) -> int:
        """"""
    @Indent.setter
    def Indent(self, value: int) -> None: ...
    @property
    def InnerWriter(self) -> TextWriter:
        """"""
    @property
    def NewLine(self) -> str:
        """"""
    @NewLine.setter
    def NewLine(self, value: str) -> None: ...
    def Close(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Flush(self) -> None:
        """"""
    def FlushAsync(self) -> Task:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def ToString(self) -> str:
        """"""
    @overload
    def Write(self, buffer: Array[Char]) -> None:
        """"""
    @overload
    def Write(self, buffer: Array[Char], index: int, count: int) -> None:
        """"""
    @overload
    def Write(self, value: bool) -> None:
        """"""
    @overload
    def Write(self, value: Char) -> None:
        """"""
    @overload
    def Write(self, value: Decimal) -> None:
        """"""
    @overload
    def Write(self, value: float) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""
    @overload
    def Write(self, value: object) -> None:
        """"""
    @overload
    def Write(self, value: float) -> None:
        """"""
    @overload
    def Write(self, s: str) -> None:
        """"""
    @overload
    def Write(self, format: str, arg: Array[object]) -> None:
        """"""
    @overload
    def Write(self, format: str, arg0: object) -> None:
        """"""
    @overload
    def Write(self, format: str, arg0: object, arg1: object) -> None:
        """"""
    @overload
    def Write(self, format: str, arg0: object, arg1: object, arg2: object) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""
    @overload
    def Write(self, value: int) -> None:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[Char]) -> Task:
        """"""
    @overload
    def WriteAsync(self, buffer: Array[Char], index: int, count: int) -> Task:
        """"""
    @overload
    def WriteAsync(self, value: Char) -> Task:
        """"""
    @overload
    def WriteAsync(self, value: str) -> Task:
        """"""
    @overload
    def WriteLine(self) -> None:
        """"""
    @overload
    def WriteLine(self, buffer: Array[Char]) -> None:
        """"""
    @overload
    def WriteLine(self, buffer: Array[Char], index: int, count: int) -> None:
        """"""
    @overload
    def WriteLine(self, value: bool) -> None:
        """"""
    @overload
    def WriteLine(self, value: Char) -> None:
        """"""
    @overload
    def WriteLine(self, value: Decimal) -> None:
        """"""
    @overload
    def WriteLine(self, value: float) -> None:
        """"""
    @overload
    def WriteLine(self, value: int) -> None:
        """"""
    @overload
    def WriteLine(self, value: int) -> None:
        """"""
    @overload
    def WriteLine(self, value: object) -> None:
        """"""
    @overload
    def WriteLine(self, value: float) -> None:
        """"""
    @overload
    def WriteLine(self, s: str) -> None:
        """"""
    @overload
    def WriteLine(self, format: str, arg: Array[object]) -> None:
        """"""
    @overload
    def WriteLine(self, format: str, arg0: object) -> None:
        """"""
    @overload
    def WriteLine(self, format: str, arg0: object, arg1: object) -> None:
        """"""
    @overload
    def WriteLine(self, format: str, arg0: object, arg1: object, arg2: object) -> None:
        """"""
    @overload
    def WriteLine(self, value: int) -> None:
        """"""
    @overload
    def WriteLine(self, value: int) -> None:
        """"""
    @overload
    def WriteLineAsync(self) -> Task:
        """"""
    @overload
    def WriteLineAsync(self, buffer: Array[Char]) -> Task:
        """"""
    @overload
    def WriteLineAsync(self, buffer: Array[Char], index: int, count: int) -> Task:
        """"""
    @overload
    def WriteLineAsync(self, value: Char) -> Task:
        """"""
    @overload
    def WriteLineAsync(self, value: str) -> Task:
        """"""
    def WriteLineNoTabs(self, s: str) -> None:
        """"""

class LanguageOptions(Enum):
    """"""

    _None: LanguageOptions = ...
    """"""
    CaseInsensitive: LanguageOptions = ...
    """"""

class RedistVersionInfo(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetCompilerPath(cls, provOptions: IDictionary[str, str], compilerExecutable: str) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TempFileCollection(Object, ICollection, IEnumerable, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, tempDir: str) -> None:
        """"""
    @overload
    def __init__(self, tempDir: str, keepFiles: bool) -> None:
        """"""
    @property
    def BasePath(self) -> str:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def KeepFiles(self) -> bool:
        """"""
    @KeepFiles.setter
    def KeepFiles(self, value: bool) -> None: ...
    @property
    def SyncRoot(self) -> object:
        """"""
    @property
    def TempDir(self) -> str:
        """"""
    @overload
    def AddExtension(self, fileExtension: str) -> str:
        """"""
    @overload
    def AddExtension(self, fileExtension: str, keepFile: bool) -> str:
        """"""
    def AddFile(self, fileName: str, keepFile: bool) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, fileNames: Array[str], start: int) -> None:
        """"""
    def Delete(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __len__(self) -> int:
        """"""
