from __future__ import annotations

from abc import ABC
from typing import Generic
from typing import TypeVar
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
from System.Collections.Generic import IDictionary
from System.ComponentModel import IComponent
from System.ComponentModel import IContainer
from System.ComponentModel import ISite
from System.ComponentModel import ITypeDescriptorContext
from System.ComponentModel import PropertyDescriptorCollection
from System.ComponentModel import TypeConverter
from System.ComponentModel.TypeConverter import StandardValuesCollection
from System.Globalization import CultureInfo
from System.IO import TextReader
from System.IO import TextWriter
from System.Runtime.Remoting import ObjRef

T = TypeVar("T")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

class CSharpCodeGenerator(Object, ICodeCompiler, ICodeGenerator):
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

class CSharpCodeProvider(CodeDomProvider, IComponent, IDisposable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, providerOptions: IDictionary[str, str]):
        """

        :param providerOptions:
        """
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
    def GetConverter(self, type: Type) -> TypeConverter:
        """

        :param type:
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
    def GetTypeOutput(self, type: CodeTypeReference) -> str:
        """

        :param type:
        :return:
        """
    def InitializeLifetimeService(self) -> object:
        """

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

class CSharpMemberAttributeConverter(CSharpModifierAttributeConverter):
    """"""

    @classmethod
    @property
    def Default(cls) -> CSharpMemberAttributeConverter:
        """

        :return:
        """
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CSharpModifierAttributeConverter(ABC, TypeConverter):
    """"""

    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CSharpTypeAttributeConverter(CSharpModifierAttributeConverter):
    """"""

    @classmethod
    @property
    def Default(cls) -> CSharpTypeAttributeConverter:
        """

        :return:
        """
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """

        :param sourceType:
        :return:
        """
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """

        :param context:
        :param sourceType:
        :return:
        """
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """

        :param destinationType:
        :return:
        """
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """

        :param context:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertFrom(self, value: object) -> object:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, text: str) -> object:
        """

        :param text:
        :return:
        """
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """

        :param context:
        :param text:
        :return:
        """
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """

        :param context:
        :param culture:
        :param text:
        :return:
        """
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """

        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """

        :param context:
        :param culture:
        :param value:
        :param destinationType:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """

        :param context:
        :param culture:
        :param value:
        :return:
        """
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """

        :param propertyValues:
        :return:
        """
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """

        :param context:
        :param propertyValues:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """

        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :return:
        """
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """

        :param context:
        :param value:
        :param attributes:
        :return:
        """
    @overload
    def GetPropertiesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValues(self) -> ICollection:
        """

        :return:
        """
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """

        :return:
        """
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """

        :param context:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def IsValid(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """

        :param context:
        :param value:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
