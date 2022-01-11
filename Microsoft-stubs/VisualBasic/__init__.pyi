from __future__ import annotations

from abc import ABC
from typing import Union, overload

from System import Boolean, IDisposable, Object, String, Type, Void
from System.CodeDom import CodeTypeMember
from System.CodeDom.Compiler import CodeCompiler, CodeDomProvider, CodeGeneratorOptions, ICodeCompiler, ICodeGenerator, LanguageOptions
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

class VBCodeGenerator(CodeCompiler, ICodeGenerator, ICodeCompiler):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def IsKeyword(value: StringType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class VBCodeGenerator(CodeCompiler, ICodeGenerator, ICodeCompiler):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def IsKeyword(value: StringType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class VBCodeProvider(CodeDomProvider, IComponent, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, providerOptions: IDictionary[StringType, StringType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def FileExtension(self) -> StringType: ...
    
    @property
    def LanguageOptions(self) -> LanguageOptions: ...
    
    # ---------- Methods ---------- #
    
    def CreateCompiler(self) -> ICodeCompiler: ...
    
    @overload
    def CreateGenerator(self) -> ICodeGenerator: ...
    
    def GenerateCodeFromMember(self, member: CodeTypeMember, writer: TextWriter, options: CodeGeneratorOptions) -> VoidType: ...
    
    def GetConverter(self, type: TypeType) -> TypeConverter: ...
    
    def get_FileExtension(self) -> StringType: ...
    
    def get_LanguageOptions(self) -> LanguageOptions: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class VBCodeProvider(CodeDomProvider, IComponent, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, providerOptions: IDictionary[StringType, StringType]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def FileExtension(self) -> StringType: ...
    
    @property
    def LanguageOptions(self) -> LanguageOptions: ...
    
    # ---------- Methods ---------- #
    
    def CreateCompiler(self) -> ICodeCompiler: ...
    
    @overload
    def CreateGenerator(self) -> ICodeGenerator: ...
    
    def GenerateCodeFromMember(self, member: CodeTypeMember, writer: TextWriter, options: CodeGeneratorOptions) -> VoidType: ...
    
    def GetConverter(self, type: TypeType) -> TypeConverter: ...
    
    def get_FileExtension(self) -> StringType: ...
    
    def get_LanguageOptions(self) -> LanguageOptions: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class VBMemberAttributeConverter(VBModifierAttributeConverter):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Default() -> VBMemberAttributeConverter: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def get_Default() -> VBMemberAttributeConverter: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class VBMemberAttributeConverter(VBModifierAttributeConverter):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Default() -> VBMemberAttributeConverter: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def get_Default() -> VBMemberAttributeConverter: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class VBModifierAttributeConverter(ABC, TypeConverter):
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


class VBModifierAttributeConverter(ABC, TypeConverter):
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


class VBTypeAttributeConverter(VBModifierAttributeConverter):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Default() -> VBTypeAttributeConverter: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def get_Default() -> VBTypeAttributeConverter: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class VBTypeAttributeConverter(VBModifierAttributeConverter):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @staticmethod
    @property
    def Default() -> VBTypeAttributeConverter: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def get_Default() -> VBTypeAttributeConverter: ...
    
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
    VBCodeGenerator,
    VBCodeProvider,
    VBMemberAttributeConverter,
    VBModifierAttributeConverter,
    VBTypeAttributeConverter,
]
