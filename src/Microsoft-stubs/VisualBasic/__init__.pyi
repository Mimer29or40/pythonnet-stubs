"""Automatically generated stubs for C# namespace: Microsoft.VisualBasic."""

from abc import ABC
from collections.abc import Iterator
from typing import Self
from typing import overload

from System import Array
from System import Attribute
from System import EventHandler
from System import IDisposable
from System import Object
from System import Type
from System.CodeDom import CodeCompileUnit
from System.CodeDom import CodeExpression
from System.CodeDom import CodeNamespace
from System.CodeDom import CodeStatement
from System.CodeDom import CodeTypeDeclaration
from System.CodeDom import CodeTypeMember
from System.CodeDom import CodeTypeReference
from System.CodeDom.Compiler import CodeCompiler
from System.CodeDom.Compiler import CodeDomProvider
from System.CodeDom.Compiler import CodeGeneratorOptions
from System.CodeDom.Compiler import CompilerParameters
from System.CodeDom.Compiler import CompilerResults
from System.CodeDom.Compiler import GeneratorSupport
from System.CodeDom.Compiler import ICodeCompiler
from System.CodeDom.Compiler import ICodeGenerator
from System.CodeDom.Compiler import ICodeParser
from System.CodeDom.Compiler import LanguageOptions
from System.Collections import ICollection
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections.Generic import IDictionary
from System.ComponentModel import IComponent
from System.ComponentModel import IContainer
from System.ComponentModel import ISite
from System.ComponentModel import ITypeDescriptorContext
from System.ComponentModel import PropertyDescriptorCollection
from System.ComponentModel import TypeConverter
from System.Globalization import CultureInfo
from System.IO import TextReader
from System.IO import TextWriter
from System.Runtime.Remoting import ObjRef

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

class VBCodeGenerator(CodeCompiler, ICodeCompiler, ICodeGenerator):
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
    @classmethod
    def IsKeyword(cls, value: str) -> bool:
        """"""
    def IsValidIdentifier(self, value: str) -> bool:
        """"""
    def Supports(self, supports: GeneratorSupport) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def ValidateIdentifier(self, value: str) -> None:
        """"""

class VBCodeProvider(CodeDomProvider, IComponent, IDisposable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, providerOptions: IDictionary[str, str]) -> None:
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
    def GetConverter(self, type: Type) -> TypeConverter:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeOutput(self, type: CodeTypeReference) -> str:
        """"""
    def InitializeLifetimeService(self) -> object:
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

class VBMemberAttributeConverter(VBModifierAttributeConverter):
    """"""
    @classmethod
    @property
    def Default(cls) -> VBMemberAttributeConverter:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
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
        def __getitem__(self, index: int) -> object:
            """"""

class VBModifierAttributeConverter(ABC, TypeConverter):
    """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
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
        def __getitem__(self, index: int) -> object:
            """"""

class VBTypeAttributeConverter(VBModifierAttributeConverter):
    """"""
    @classmethod
    @property
    def Default(cls) -> VBTypeAttributeConverter:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
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
        def __getitem__(self, index: int) -> object:
            """"""
