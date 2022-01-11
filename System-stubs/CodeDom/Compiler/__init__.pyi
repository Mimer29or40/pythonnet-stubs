from __future__ import annotations

from abc import ABC
from typing import List, Protocol, Tuple, Union, overload

from Microsoft.Win32.SafeHandles import SafeFileHandle
from System import Array, Attribute, Boolean, Char, Double, Enum, IDisposable, Int32, Int64, IntPtr, Object, Single, String, Type, UInt32, Void
from System.CodeDom import CodeCompileUnit, CodeExpression, CodeNamespace, CodeObject, CodeStatement, CodeTypeDeclaration, CodeTypeMember, CodeTypeReference
from System.Collections import CollectionBase, ICollection, IEnumerable, IEnumerator, IList
from System.Collections.Generic import IDictionary
from System.Collections.Specialized import StringCollection
from System.ComponentModel import Component, IComponent, TypeConverter
from System.Configuration import IConfigurationSectionHandler
from System.IO import TextReader, TextWriter
from System.Reflection import Assembly
from System.Runtime.InteropServices import _Attribute
from System.Security.Policy import Evidence
from System.Text import Encoding
from System.Xml import XmlNode

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
CharType = Union[str, Char]
DoubleType = Union[float, Double]
FloatType = Union[float, Single]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
UIntType = Union[int, UInt32]
VoidType = Union[None, Void]


# ---------- Classes ---------- #

class CodeCompiler(ABC, CodeGenerator, ICodeGenerator, ICodeCompiler):
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


class CodeDomCompilationConfiguration(ObjectType):
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


class CodeDomConfigurationHandler(ObjectType, IConfigurationSectionHandler):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Create(self, inheritedObject: ObjectType, configContextObj: ObjectType, node: XmlNode) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeDomProvider(ABC, Component, IComponent, IDisposable):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def FileExtension(self) -> StringType: ...
    
    @property
    def LanguageOptions(self) -> LanguageOptions: ...
    
    # ---------- Methods ---------- #
    
    def CompileAssemblyFromDom(self, options: CompilerParameters, compilationUnits: ArrayType[CodeCompileUnit]) -> CompilerResults: ...
    
    def CompileAssemblyFromFile(self, options: CompilerParameters, fileNames: ArrayType[StringType]) -> CompilerResults: ...
    
    def CompileAssemblyFromSource(self, options: CompilerParameters, sources: ArrayType[StringType]) -> CompilerResults: ...
    
    def CreateCompiler(self) -> ICodeCompiler: ...
    
    def CreateEscapedIdentifier(self, value: StringType) -> StringType: ...
    
    @overload
    def CreateGenerator(self, output: TextWriter) -> ICodeGenerator: ...
    
    @overload
    def CreateGenerator(self, fileName: StringType) -> ICodeGenerator: ...
    
    @overload
    def CreateGenerator(self) -> ICodeGenerator: ...
    
    def CreateParser(self) -> ICodeParser: ...
    
    @staticmethod
    @overload
    def CreateProvider(language: StringType, providerOptions: IDictionary[StringType, StringType]) -> CodeDomProvider: ...
    
    @staticmethod
    @overload
    def CreateProvider(language: StringType) -> CodeDomProvider: ...
    
    def CreateValidIdentifier(self, value: StringType) -> StringType: ...
    
    def GenerateCodeFromCompileUnit(self, compileUnit: CodeCompileUnit, writer: TextWriter, options: CodeGeneratorOptions) -> VoidType: ...
    
    def GenerateCodeFromExpression(self, expression: CodeExpression, writer: TextWriter, options: CodeGeneratorOptions) -> VoidType: ...
    
    def GenerateCodeFromMember(self, member: CodeTypeMember, writer: TextWriter, options: CodeGeneratorOptions) -> VoidType: ...
    
    def GenerateCodeFromNamespace(self, codeNamespace: CodeNamespace, writer: TextWriter, options: CodeGeneratorOptions) -> VoidType: ...
    
    def GenerateCodeFromStatement(self, statement: CodeStatement, writer: TextWriter, options: CodeGeneratorOptions) -> VoidType: ...
    
    def GenerateCodeFromType(self, codeType: CodeTypeDeclaration, writer: TextWriter, options: CodeGeneratorOptions) -> VoidType: ...
    
    @staticmethod
    def GetAllCompilerInfo() -> ArrayType[CompilerInfo]: ...
    
    @staticmethod
    def GetCompilerInfo(language: StringType) -> CompilerInfo: ...
    
    def GetConverter(self, type: TypeType) -> TypeConverter: ...
    
    @staticmethod
    def GetLanguageFromExtension(extension: StringType) -> StringType: ...
    
    def GetTypeOutput(self, type: CodeTypeReference) -> StringType: ...
    
    @staticmethod
    def IsDefinedExtension(extension: StringType) -> BooleanType: ...
    
    @staticmethod
    def IsDefinedLanguage(language: StringType) -> BooleanType: ...
    
    def IsValidIdentifier(self, value: StringType) -> BooleanType: ...
    
    def Parse(self, codeStream: TextReader) -> CodeCompileUnit: ...
    
    def Supports(self, generatorSupport: GeneratorSupport) -> BooleanType: ...
    
    def get_FileExtension(self) -> StringType: ...
    
    def get_LanguageOptions(self) -> LanguageOptions: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeGenerator(ABC, ObjectType, ICodeGenerator):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GenerateCodeFromMember(self, member: CodeTypeMember, writer: TextWriter, options: CodeGeneratorOptions) -> VoidType: ...
    
    @staticmethod
    def IsValidLanguageIndependentIdentifier(value: StringType) -> BooleanType: ...
    
    @staticmethod
    def ValidateIdentifiers(e: CodeObject) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeGeneratorOptions(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BlankLinesBetweenMembers(self) -> BooleanType: ...
    
    @BlankLinesBetweenMembers.setter
    def BlankLinesBetweenMembers(self, value: BooleanType) -> None: ...
    
    @property
    def BracingStyle(self) -> StringType: ...
    
    @BracingStyle.setter
    def BracingStyle(self, value: StringType) -> None: ...
    
    @property
    def ElseOnClosing(self) -> BooleanType: ...
    
    @ElseOnClosing.setter
    def ElseOnClosing(self, value: BooleanType) -> None: ...
    
    @property
    def IndentString(self) -> StringType: ...
    
    @IndentString.setter
    def IndentString(self, value: StringType) -> None: ...
    
    def __getitem__(self, key: StringType) -> ObjectType: ...
    
    def __setitem__(self, key: StringType, value: ObjectType) -> None: ...
    
    @property
    def VerbatimOrder(self) -> BooleanType: ...
    
    @VerbatimOrder.setter
    def VerbatimOrder(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_BlankLinesBetweenMembers(self) -> BooleanType: ...
    
    def get_BracingStyle(self) -> StringType: ...
    
    def get_ElseOnClosing(self) -> BooleanType: ...
    
    def get_IndentString(self) -> StringType: ...
    
    def get_Item(self, index: StringType) -> ObjectType: ...
    
    def get_VerbatimOrder(self) -> BooleanType: ...
    
    def set_BlankLinesBetweenMembers(self, value: BooleanType) -> VoidType: ...
    
    def set_BracingStyle(self, value: StringType) -> VoidType: ...
    
    def set_ElseOnClosing(self, value: BooleanType) -> VoidType: ...
    
    def set_IndentString(self, value: StringType) -> VoidType: ...
    
    def set_Item(self, index: StringType, value: ObjectType) -> VoidType: ...
    
    def set_VerbatimOrder(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeParser(ABC, ObjectType, ICodeParser):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Parse(self, codeStream: TextReader) -> CodeCompileUnit: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeValidator(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CompilerError(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, fileName: StringType, line: IntType, column: IntType, errorNumber: StringType, errorText: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Column(self) -> IntType: ...
    
    @Column.setter
    def Column(self, value: IntType) -> None: ...
    
    @property
    def ErrorNumber(self) -> StringType: ...
    
    @ErrorNumber.setter
    def ErrorNumber(self, value: StringType) -> None: ...
    
    @property
    def ErrorText(self) -> StringType: ...
    
    @ErrorText.setter
    def ErrorText(self, value: StringType) -> None: ...
    
    @property
    def FileName(self) -> StringType: ...
    
    @FileName.setter
    def FileName(self, value: StringType) -> None: ...
    
    @property
    def IsWarning(self) -> BooleanType: ...
    
    @IsWarning.setter
    def IsWarning(self, value: BooleanType) -> None: ...
    
    @property
    def Line(self) -> IntType: ...
    
    @Line.setter
    def Line(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    def get_Column(self) -> IntType: ...
    
    def get_ErrorNumber(self) -> StringType: ...
    
    def get_ErrorText(self) -> StringType: ...
    
    def get_FileName(self) -> StringType: ...
    
    def get_IsWarning(self) -> BooleanType: ...
    
    def get_Line(self) -> IntType: ...
    
    def set_Column(self, value: IntType) -> VoidType: ...
    
    def set_ErrorNumber(self, value: StringType) -> VoidType: ...
    
    def set_ErrorText(self, value: StringType) -> VoidType: ...
    
    def set_FileName(self, value: StringType) -> VoidType: ...
    
    def set_IsWarning(self, value: BooleanType) -> VoidType: ...
    
    def set_Line(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CompilerErrorCollection(CollectionBase, IList, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, value: CompilerErrorCollection): ...
    
    @overload
    def __init__(self, value: ArrayType[CompilerError]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def HasErrors(self) -> BooleanType: ...
    
    @property
    def HasWarnings(self) -> BooleanType: ...
    
    def __getitem__(self, key: IntType) -> CompilerError: ...
    
    def __setitem__(self, key: IntType, value: CompilerError) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, value: CompilerError) -> IntType: ...
    
    @overload
    def AddRange(self, value: ArrayType[CompilerError]) -> VoidType: ...
    
    @overload
    def AddRange(self, value: CompilerErrorCollection) -> VoidType: ...
    
    def Contains(self, value: CompilerError) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[CompilerError], index: IntType) -> VoidType: ...
    
    def IndexOf(self, value: CompilerError) -> IntType: ...
    
    def Insert(self, index: IntType, value: CompilerError) -> VoidType: ...
    
    def Remove(self, value: CompilerError) -> VoidType: ...
    
    def get_HasErrors(self) -> BooleanType: ...
    
    def get_HasWarnings(self) -> BooleanType: ...
    
    def get_Item(self, index: IntType) -> CompilerError: ...
    
    def set_Item(self, index: IntType, value: CompilerError) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CompilerInfo(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def CodeDomProviderType(self) -> TypeType: ...
    
    @property
    def IsCodeDomProviderTypeValid(self) -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    def CreateDefaultCompilerParameters(self) -> CompilerParameters: ...
    
    @overload
    def CreateProvider(self, providerOptions: IDictionary[StringType, StringType]) -> CodeDomProvider: ...
    
    @overload
    def CreateProvider(self) -> CodeDomProvider: ...
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetExtensions(self) -> ArrayType[StringType]: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def GetLanguages(self) -> ArrayType[StringType]: ...
    
    def get_CodeDomProviderType(self) -> TypeType: ...
    
    def get_IsCodeDomProviderTypeValid(self) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CompilerParameters(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, assemblyNames: ArrayType[StringType]): ...
    
    @overload
    def __init__(self, assemblyNames: ArrayType[StringType], outputName: StringType): ...
    
    @overload
    def __init__(self, assemblyNames: ArrayType[StringType], outputName: StringType, includeDebugInformation: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CompilerOptions(self) -> StringType: ...
    
    @CompilerOptions.setter
    def CompilerOptions(self, value: StringType) -> None: ...
    
    @property
    def CoreAssemblyFileName(self) -> StringType: ...
    
    @CoreAssemblyFileName.setter
    def CoreAssemblyFileName(self, value: StringType) -> None: ...
    
    @property
    def EmbeddedResources(self) -> StringCollection: ...
    
    @property
    def Evidence(self) -> Evidence: ...
    
    @Evidence.setter
    def Evidence(self, value: Evidence) -> None: ...
    
    @property
    def GenerateExecutable(self) -> BooleanType: ...
    
    @GenerateExecutable.setter
    def GenerateExecutable(self, value: BooleanType) -> None: ...
    
    @property
    def GenerateInMemory(self) -> BooleanType: ...
    
    @GenerateInMemory.setter
    def GenerateInMemory(self, value: BooleanType) -> None: ...
    
    @property
    def IncludeDebugInformation(self) -> BooleanType: ...
    
    @IncludeDebugInformation.setter
    def IncludeDebugInformation(self, value: BooleanType) -> None: ...
    
    @property
    def LinkedResources(self) -> StringCollection: ...
    
    @property
    def MainClass(self) -> StringType: ...
    
    @MainClass.setter
    def MainClass(self, value: StringType) -> None: ...
    
    @property
    def OutputAssembly(self) -> StringType: ...
    
    @OutputAssembly.setter
    def OutputAssembly(self, value: StringType) -> None: ...
    
    @property
    def ReferencedAssemblies(self) -> StringCollection: ...
    
    @property
    def TempFiles(self) -> TempFileCollection: ...
    
    @TempFiles.setter
    def TempFiles(self, value: TempFileCollection) -> None: ...
    
    @property
    def TreatWarningsAsErrors(self) -> BooleanType: ...
    
    @TreatWarningsAsErrors.setter
    def TreatWarningsAsErrors(self, value: BooleanType) -> None: ...
    
    @property
    def UserToken(self) -> NIntType: ...
    
    @UserToken.setter
    def UserToken(self, value: NIntType) -> None: ...
    
    @property
    def WarningLevel(self) -> IntType: ...
    
    @WarningLevel.setter
    def WarningLevel(self, value: IntType) -> None: ...
    
    @property
    def Win32Resource(self) -> StringType: ...
    
    @Win32Resource.setter
    def Win32Resource(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_CompilerOptions(self) -> StringType: ...
    
    def get_CoreAssemblyFileName(self) -> StringType: ...
    
    def get_EmbeddedResources(self) -> StringCollection: ...
    
    def get_Evidence(self) -> Evidence: ...
    
    def get_GenerateExecutable(self) -> BooleanType: ...
    
    def get_GenerateInMemory(self) -> BooleanType: ...
    
    def get_IncludeDebugInformation(self) -> BooleanType: ...
    
    def get_LinkedResources(self) -> StringCollection: ...
    
    def get_MainClass(self) -> StringType: ...
    
    def get_OutputAssembly(self) -> StringType: ...
    
    def get_ReferencedAssemblies(self) -> StringCollection: ...
    
    def get_TempFiles(self) -> TempFileCollection: ...
    
    def get_TreatWarningsAsErrors(self) -> BooleanType: ...
    
    def get_UserToken(self) -> NIntType: ...
    
    def get_WarningLevel(self) -> IntType: ...
    
    def get_Win32Resource(self) -> StringType: ...
    
    def set_CompilerOptions(self, value: StringType) -> VoidType: ...
    
    def set_CoreAssemblyFileName(self, value: StringType) -> VoidType: ...
    
    def set_Evidence(self, value: Evidence) -> VoidType: ...
    
    def set_GenerateExecutable(self, value: BooleanType) -> VoidType: ...
    
    def set_GenerateInMemory(self, value: BooleanType) -> VoidType: ...
    
    def set_IncludeDebugInformation(self, value: BooleanType) -> VoidType: ...
    
    def set_MainClass(self, value: StringType) -> VoidType: ...
    
    def set_OutputAssembly(self, value: StringType) -> VoidType: ...
    
    def set_TempFiles(self, value: TempFileCollection) -> VoidType: ...
    
    def set_TreatWarningsAsErrors(self, value: BooleanType) -> VoidType: ...
    
    def set_UserToken(self, value: NIntType) -> VoidType: ...
    
    def set_WarningLevel(self, value: IntType) -> VoidType: ...
    
    def set_Win32Resource(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CompilerResults(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, tempFiles: TempFileCollection): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CompiledAssembly(self) -> Assembly: ...
    
    @CompiledAssembly.setter
    def CompiledAssembly(self, value: Assembly) -> None: ...
    
    @property
    def Errors(self) -> CompilerErrorCollection: ...
    
    @property
    def Evidence(self) -> Evidence: ...
    
    @Evidence.setter
    def Evidence(self, value: Evidence) -> None: ...
    
    @property
    def NativeCompilerReturnValue(self) -> IntType: ...
    
    @NativeCompilerReturnValue.setter
    def NativeCompilerReturnValue(self, value: IntType) -> None: ...
    
    @property
    def Output(self) -> StringCollection: ...
    
    @property
    def PathToAssembly(self) -> StringType: ...
    
    @PathToAssembly.setter
    def PathToAssembly(self, value: StringType) -> None: ...
    
    @property
    def TempFiles(self) -> TempFileCollection: ...
    
    @TempFiles.setter
    def TempFiles(self, value: TempFileCollection) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_CompiledAssembly(self) -> Assembly: ...
    
    def get_Errors(self) -> CompilerErrorCollection: ...
    
    def get_Evidence(self) -> Evidence: ...
    
    def get_NativeCompilerReturnValue(self) -> IntType: ...
    
    def get_Output(self) -> StringCollection: ...
    
    def get_PathToAssembly(self) -> StringType: ...
    
    def get_TempFiles(self) -> TempFileCollection: ...
    
    def set_CompiledAssembly(self, value: Assembly) -> VoidType: ...
    
    def set_Evidence(self, value: Evidence) -> VoidType: ...
    
    def set_NativeCompilerReturnValue(self, value: IntType) -> VoidType: ...
    
    def set_PathToAssembly(self, value: StringType) -> VoidType: ...
    
    def set_TempFiles(self, value: TempFileCollection) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Executor(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def ExecWait(cmd: StringType, tempFiles: TempFileCollection) -> VoidType: ...
    
    @staticmethod
    @overload
    def ExecWaitWithCapture(cmd: StringType, tempFiles: TempFileCollection, outputName: StringType, errorName: StringType) -> Tuple[IntType, StringType, StringType]: ...
    
    @staticmethod
    @overload
    def ExecWaitWithCapture(cmd: StringType, currentDir: StringType, tempFiles: TempFileCollection, outputName: StringType, errorName: StringType) -> Tuple[IntType, StringType, StringType]: ...
    
    @staticmethod
    @overload
    def ExecWaitWithCapture(userToken: NIntType, cmd: StringType, tempFiles: TempFileCollection, outputName: StringType, errorName: StringType) -> Tuple[IntType, StringType, StringType]: ...
    
    @staticmethod
    @overload
    def ExecWaitWithCapture(userToken: NIntType, cmd: StringType, currentDir: StringType, tempFiles: TempFileCollection, outputName: StringType, errorName: StringType) -> Tuple[IntType, StringType, StringType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileIntegrity(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def IsEnabled() -> BooleanType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def IsTrusted(safeFileHandle: SafeFileHandle) -> BooleanType: ...
    
    @staticmethod
    def MarkAsTrusted(safeFileHandle: SafeFileHandle) -> VoidType: ...
    
    @staticmethod
    def get_IsEnabled() -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class GeneratedCodeAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, tool: StringType, version: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Tool(self) -> StringType: ...
    
    @property
    def Version(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Tool(self) -> StringType: ...
    
    def get_Version(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class HandlerBase(ABC, ObjectType):
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


class Indentation(ObjectType):
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


class IndentedTextWriter(TextWriter, IDisposable):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def DefaultTabString() -> StringType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, writer: TextWriter): ...
    
    @overload
    def __init__(self, writer: TextWriter, tabString: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Encoding(self) -> Encoding: ...
    
    @property
    def Indent(self) -> IntType: ...
    
    @Indent.setter
    def Indent(self, value: IntType) -> None: ...
    
    @property
    def InnerWriter(self) -> TextWriter: ...
    
    @property
    def NewLine(self) -> StringType: ...
    
    @NewLine.setter
    def NewLine(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Flush(self) -> VoidType: ...
    
    @overload
    def Write(self, s: StringType) -> VoidType: ...
    
    @overload
    def Write(self, value: BooleanType) -> VoidType: ...
    
    @overload
    def Write(self, value: CharType) -> VoidType: ...
    
    @overload
    def Write(self, buffer: ArrayType[CharType]) -> VoidType: ...
    
    @overload
    def Write(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def Write(self, value: DoubleType) -> VoidType: ...
    
    @overload
    def Write(self, value: FloatType) -> VoidType: ...
    
    @overload
    def Write(self, value: IntType) -> VoidType: ...
    
    @overload
    def Write(self, value: LongType) -> VoidType: ...
    
    @overload
    def Write(self, value: ObjectType) -> VoidType: ...
    
    @overload
    def Write(self, format: StringType, arg0: ObjectType) -> VoidType: ...
    
    @overload
    def Write(self, format: StringType, arg0: ObjectType, arg1: ObjectType) -> VoidType: ...
    
    @overload
    def Write(self, format: StringType, arg: ArrayType[ObjectType]) -> VoidType: ...
    
    @overload
    def WriteLine(self, s: StringType) -> VoidType: ...
    
    @overload
    def WriteLine(self) -> VoidType: ...
    
    @overload
    def WriteLine(self, value: BooleanType) -> VoidType: ...
    
    @overload
    def WriteLine(self, value: CharType) -> VoidType: ...
    
    @overload
    def WriteLine(self, buffer: ArrayType[CharType]) -> VoidType: ...
    
    @overload
    def WriteLine(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> VoidType: ...
    
    @overload
    def WriteLine(self, value: DoubleType) -> VoidType: ...
    
    @overload
    def WriteLine(self, value: FloatType) -> VoidType: ...
    
    @overload
    def WriteLine(self, value: IntType) -> VoidType: ...
    
    @overload
    def WriteLine(self, value: LongType) -> VoidType: ...
    
    @overload
    def WriteLine(self, value: ObjectType) -> VoidType: ...
    
    @overload
    def WriteLine(self, format: StringType, arg0: ObjectType) -> VoidType: ...
    
    @overload
    def WriteLine(self, format: StringType, arg0: ObjectType, arg1: ObjectType) -> VoidType: ...
    
    @overload
    def WriteLine(self, format: StringType, arg: ArrayType[ObjectType]) -> VoidType: ...
    
    @overload
    def WriteLine(self, value: UIntType) -> VoidType: ...
    
    def WriteLineNoTabs(self, s: StringType) -> VoidType: ...
    
    def get_Encoding(self) -> Encoding: ...
    
    def get_Indent(self) -> IntType: ...
    
    def get_InnerWriter(self) -> TextWriter: ...
    
    def get_NewLine(self) -> StringType: ...
    
    def set_Indent(self, value: IntType) -> VoidType: ...
    
    def set_NewLine(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RedistVersionInfo(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def GetCompilerPath(provOptions: IDictionary[StringType, StringType], compilerExecutable: StringType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TempFileCollection(ObjectType, ICollection, IEnumerable, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, tempDir: StringType): ...
    
    @overload
    def __init__(self, tempDir: StringType, keepFiles: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BasePath(self) -> StringType: ...
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def KeepFiles(self) -> BooleanType: ...
    
    @KeepFiles.setter
    def KeepFiles(self, value: BooleanType) -> None: ...
    
    @property
    def TempDir(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def AddExtension(self, fileExtension: StringType, keepFile: BooleanType) -> StringType: ...
    
    @overload
    def AddExtension(self, fileExtension: StringType) -> StringType: ...
    
    def AddFile(self, fileName: StringType, keepFile: BooleanType) -> VoidType: ...
    
    def CopyTo(self, fileNames: ArrayType[StringType], start: IntType) -> VoidType: ...
    
    def Delete(self) -> VoidType: ...
    
    def GetEnumerator(self) -> IEnumerator: ...
    
    def get_BasePath(self) -> StringType: ...
    
    def get_Count(self) -> IntType: ...
    
    def get_KeepFiles(self) -> BooleanType: ...
    
    def get_TempDir(self) -> StringType: ...
    
    def set_KeepFiles(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# ---------- Interfaces ---------- #

class ICodeCompiler(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CompileAssemblyFromDom(self, options: CompilerParameters, compilationUnit: CodeCompileUnit) -> CompilerResults: ...
    
    def CompileAssemblyFromDomBatch(self, options: CompilerParameters, compilationUnits: ArrayType[CodeCompileUnit]) -> CompilerResults: ...
    
    def CompileAssemblyFromFile(self, options: CompilerParameters, fileName: StringType) -> CompilerResults: ...
    
    def CompileAssemblyFromFileBatch(self, options: CompilerParameters, fileNames: ArrayType[StringType]) -> CompilerResults: ...
    
    def CompileAssemblyFromSource(self, options: CompilerParameters, source: StringType) -> CompilerResults: ...
    
    def CompileAssemblyFromSourceBatch(self, options: CompilerParameters, sources: ArrayType[StringType]) -> CompilerResults: ...
    
    # No Events


class ICodeGenerator(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CreateEscapedIdentifier(self, value: StringType) -> StringType: ...
    
    def CreateValidIdentifier(self, value: StringType) -> StringType: ...
    
    def GenerateCodeFromCompileUnit(self, e: CodeCompileUnit, w: TextWriter, o: CodeGeneratorOptions) -> VoidType: ...
    
    def GenerateCodeFromExpression(self, e: CodeExpression, w: TextWriter, o: CodeGeneratorOptions) -> VoidType: ...
    
    def GenerateCodeFromNamespace(self, e: CodeNamespace, w: TextWriter, o: CodeGeneratorOptions) -> VoidType: ...
    
    def GenerateCodeFromStatement(self, e: CodeStatement, w: TextWriter, o: CodeGeneratorOptions) -> VoidType: ...
    
    def GenerateCodeFromType(self, e: CodeTypeDeclaration, w: TextWriter, o: CodeGeneratorOptions) -> VoidType: ...
    
    def GetTypeOutput(self, type: CodeTypeReference) -> StringType: ...
    
    def IsValidIdentifier(self, value: StringType) -> BooleanType: ...
    
    def Supports(self, supports: GeneratorSupport) -> BooleanType: ...
    
    def ValidateIdentifier(self, value: StringType) -> VoidType: ...
    
    # No Events


class ICodeParser(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Parse(self, codeStream: TextReader) -> CodeCompileUnit: ...
    
    # No Events


# ---------- Enums ---------- #

class GeneratorSupport(Enum):
    ArraysOfArrays = 1
    EntryPointMethod = 2
    GotoStatements = 4
    MultidimensionalArrays = 8
    StaticConstructors = 16
    TryCatchStatements = 32
    ReturnTypeAttributes = 64
    DeclareValueTypes = 128
    DeclareEnums = 256
    DeclareDelegates = 512
    DeclareInterfaces = 1024
    DeclareEvents = 2048
    AssemblyAttributes = 4096
    ParameterAttributes = 8192
    ReferenceParameters = 16384
    ChainedConstructorArguments = 32768
    NestedTypes = 65536
    MultipleInterfaceMembers = 131072
    PublicStaticMembers = 262144
    ComplexExpressions = 524288
    Win32Resources = 1048576
    Resources = 2097152
    PartialTypes = 4194304
    GenericTypeReference = 8388608
    GenericTypeDeclaration = 16777216
    DeclareIndexerProperties = 33554432


class LanguageOptions(Enum):
    #None = 0
    CaseInsensitive = 1


# No Delegates

__all__ = [
    CodeCompiler,
    CodeDomCompilationConfiguration,
    CodeDomConfigurationHandler,
    CodeDomProvider,
    CodeGenerator,
    CodeGeneratorOptions,
    CodeParser,
    CodeValidator,
    CompilerError,
    CompilerErrorCollection,
    CompilerInfo,
    CompilerParameters,
    CompilerResults,
    Executor,
    FileIntegrity,
    GeneratedCodeAttribute,
    HandlerBase,
    Indentation,
    IndentedTextWriter,
    RedistVersionInfo,
    TempFileCollection,
    ICodeCompiler,
    ICodeGenerator,
    ICodeParser,
    GeneratorSupport,
    LanguageOptions,
]
