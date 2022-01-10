from __future__ import annotations

from abc import ABC
from typing import Union, overload

from System import Boolean, IDisposable, Object, String, Type, Void
from System.CodeDom import CodeTypeMember, CodeTypeReference
from System.CodeDom.Compiler import CodeDomProvider, CodeGeneratorOptions, GeneratorSupport, ICodeCompiler, ICodeGenerator
from System.Collections.Generic import IDictionary
from System.ComponentModel import IComponent, ITypeDescriptorContext, TypeConverter
from System.Globalization import CultureInfo
from System.IO import TextWriter

# ---------- Types ---------- #

BooleanType = Union[bool, Boolean]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class CSharpCodeGenerator(ObjectType, ICodeCompiler, ICodeGenerator):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CreateEscapedIdentifier(self, name: StringType) -> StringType: ...
    
    def CreateValidIdentifier(self, name: StringType) -> StringType: ...
    
    def GenerateCodeFromMember(self, member: CodeTypeMember, writer: TextWriter, options: CodeGeneratorOptions) -> VoidType: ...
    
    def GetTypeOutput(self, typeRef: CodeTypeReference) -> StringType: ...
    
    def IsValidIdentifier(self, value: StringType) -> BooleanType: ...
    
    def Supports(self, support: GeneratorSupport) -> BooleanType: ...
    
    def ValidateIdentifier(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CSharpCodeProvider(CodeDomProvider, IComponent, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, providerOptions: IDictionary[StringType, StringType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def FileExtension(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def CreateCompiler(self) -> ICodeCompiler: ...
    
    @overload
    def CreateGenerator(self) -> ICodeGenerator: ...
    
    def GenerateCodeFromMember(self, member: CodeTypeMember, writer: TextWriter, options: CodeGeneratorOptions) -> VoidType: ...
    
    def GetConverter(self, type: TypeType) -> TypeConverter: ...
    
    def get_FileExtension(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CSharpMemberAttributeConverter(CSharpModifierAttributeConverter):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Default() -> CSharpMemberAttributeConverter: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def get_Default() -> CSharpMemberAttributeConverter: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CSharpModifierAttributeConverter(ABC, TypeConverter):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: TypeType) -> BooleanType: ...
    
    @overload
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType) -> ObjectType: ...
    
    @overload
    def ConvertTo(self, context: ITypeDescriptorContext, culture: CultureInfo, value: ObjectType, destinationType: TypeType) -> ObjectType: ...
    
    @overload
    def GetStandardValues(self, context: ITypeDescriptorContext) -> StandardValuesCollection: ...
    
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> BooleanType: ...
    
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CSharpTypeAttributeConverter(CSharpModifierAttributeConverter):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Default() -> CSharpTypeAttributeConverter: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def get_Default() -> CSharpTypeAttributeConverter: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# No Structs

# No Interfaces

# No Enums

# No Delegates

__all__ = [
    CSharpCodeGenerator,
    CSharpCodeProvider,
    CSharpMemberAttributeConverter,
    CSharpModifierAttributeConverter,
    CSharpTypeAttributeConverter,
]
