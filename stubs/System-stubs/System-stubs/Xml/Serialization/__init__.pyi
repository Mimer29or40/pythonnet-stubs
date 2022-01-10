from __future__ import annotations

from abc import ABC
from typing import Callable, Generic, List, Protocol, Tuple, TypeVar, Union, overload

from System import Array, AsyncCallback, Attribute, Boolean, Byte, Char, DateTime, Double, Enum, EventArgs, Exception, IAsyncResult, ICloneable, IDisposable, Int32, Int64, IntPtr, MulticastDelegate, Object, String, Tuple, Type, Uri, ValueType, Void
from System.CodeDom import CodeAttributeDeclarationCollection, CodeCompileUnit, CodeNamespace
from System.CodeDom.Compiler import CodeDomProvider, CompilerParameters
from System.Collections import CaseInsensitiveComparer, CollectionBase, Hashtable, ICollection, IComparer, IEnumerable, IEnumerator, IEqualityComparer, IList
from System.Collections.Generic import Dictionary, IEnumerable, IEnumerator, Queue
from System.Collections.Specialized import StringCollection
from System.IO import Stream, TextReader, TextWriter
from System.Reflection import Assembly, ICustomAttributeProvider, MemberInfo, MethodAttributes
from System.Reflection.Emit import LocalBuilder, MethodBuilder
from System.Runtime.InteropServices import _Attribute, _Exception
from System.Runtime.Serialization import ISerializable
from System.Security.Policy import Evidence
from System.Xml import IXmlLineInfo, IXmlNamespaceResolver, ReadState, WhitespaceHandling, XmlAttribute, XmlElement, XmlNameTable, XmlNodeType, XmlQualifiedName, XmlReader, XmlReaderSettings, XmlSpace, XmlWriter
from System.Xml.Schema import IXmlSchemaInfo, ValidationEventHandler, XmlSchema, XmlSchemaForm
from System.Xml.Serialization.Advanced import SchemaImporterExtensionCollection

# ---------- Types ---------- #

T = TypeVar('T')

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
CharType = Union[str, Char]
DoubleType = Union[float, Double]
IntType = Union[int, Int32]
LongType = Union[int, Int64]
NIntType = Union[int, IntPtr]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]


class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    
    def __isub__(self, other: T): ...


# ---------- Classes ---------- #

class Accessor(ABC, ObjectType):
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


class AccessorMapping(ABC, Mapping):
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


class AppSettings(ABC, ObjectType):
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


class ArgBuilder(ObjectType):
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


class ArrayMapping(TypeMapping):
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


class ArrayModel(TypeModel):
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


class AttributeAccessor(Accessor):
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


class CaseInsensitiveKeyComparer(CaseInsensitiveComparer, IComparer, IEqualityComparer):
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


class ChoiceIdentifierAccessor(Accessor):
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


class CodeExporter(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def IncludeMetadata(self) -> CodeAttributeDeclarationCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_IncludeMetadata(self) -> CodeAttributeDeclarationCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeGenerator(ObjectType):
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


class CodeGeneratorConversionException(Exception, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, sourceType: TypeType, targetType: TypeType, isAddress: BooleanType, reason: StringType): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeIdentifier(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def MakeCamel(identifier: StringType) -> StringType: ...
    
    @staticmethod
    def MakePascal(identifier: StringType) -> StringType: ...
    
    @staticmethod
    def MakeValid(identifier: StringType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class CodeIdentifiers(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, caseSensitive: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def UseCamelCasing(self) -> BooleanType: ...
    
    @UseCamelCasing.setter
    def UseCamelCasing(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, identifier: StringType, value: ObjectType) -> VoidType: ...
    
    def AddReserved(self, identifier: StringType) -> VoidType: ...
    
    def AddUnique(self, identifier: StringType, value: ObjectType) -> StringType: ...
    
    def Clear(self) -> VoidType: ...
    
    def IsInUse(self, identifier: StringType) -> BooleanType: ...
    
    def MakeRightCase(self, identifier: StringType) -> StringType: ...
    
    def MakeUnique(self, identifier: StringType) -> StringType: ...
    
    def Remove(self, identifier: StringType) -> VoidType: ...
    
    def RemoveReserved(self, identifier: StringType) -> VoidType: ...
    
    def ToArray(self, type: TypeType) -> ObjectType: ...
    
    def get_UseCamelCasing(self) -> BooleanType: ...
    
    def set_UseCamelCasing(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Compiler(ObjectType):
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


class ConstantMapping(Mapping):
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


class ConstantModel(ObjectType):
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


class DynamicAssemblies(ABC, ObjectType):
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


class ElementAccessor(Accessor):
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


class EnumMapping(PrimitiveMapping):
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


class EnumModel(TypeModel):
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


class FieldModel(ObjectType):
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


class ForState(ObjectType):
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


class IfState(ObjectType):
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


class ImportContext(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, identifiers: CodeIdentifiers, shareTypes: BooleanType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ShareTypes(self) -> BooleanType: ...
    
    @property
    def TypeIdentifiers(self) -> CodeIdentifiers: ...
    
    @property
    def Warnings(self) -> StringCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_ShareTypes(self) -> BooleanType: ...
    
    def get_TypeIdentifiers(self) -> CodeIdentifiers: ...
    
    def get_Warnings(self) -> StringCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ImportStructWorkItem(ObjectType):
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


class IndentedWriter(ObjectType):
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


class LocalScope(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def parent(self) -> LocalScope: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, parent: LocalScope): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> LocalBuilder: ...
    
    @Item.setter
    def Item(self, value: LocalBuilder) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, key: StringType, value: LocalBuilder) -> VoidType: ...
    
    def AddToFreeLocals(self, freeLocals: Dictionary[Tuple[TypeType, StringType], Queue[LocalBuilder]]) -> VoidType: ...
    
    def ContainsKey(self, key: StringType) -> BooleanType: ...
    
    def TryGetValue(self, key: StringType, value: LocalBuilder) -> Tuple[BooleanType, LocalBuilder]: ...
    
    def get_Item(self, key: StringType) -> LocalBuilder: ...
    
    def set_Item(self, key: StringType, value: LocalBuilder) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class Mapping(ABC, ObjectType):
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


class MemberMapping(AccessorMapping):
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


class MemberMappingComparer(ObjectType, IComparer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Compare(self, o1: ObjectType, o2: ObjectType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MembersMapping(TypeMapping):
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


class MethodBuilderInfo(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def MethodBuilder(self) -> MethodBuilder: ...
    
    @property
    def ParameterTypes(self) -> ArrayType[TypeType]: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, methodBuilder: MethodBuilder, parameterTypes: ArrayType[TypeType]): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Validate(self, returnType: TypeType, parameterTypes: ArrayType[TypeType], attributes: MethodAttributes) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ModelScope(ObjectType):
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


class NameKey(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, other: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NameTable(ObjectType, INameScope):
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


class NullableMapping(TypeMapping):
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


class PrimitiveMapping(TypeMapping):
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


class PrimitiveModel(TypeModel):
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


class QNameComparer(ObjectType, IComparer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Compare(self, o1: ObjectType, o2: ObjectType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RecursionLimiter(ObjectType):
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


class ReflectionAwareCodeGen(ObjectType):
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


class ReflectionAwareILGen(ObjectType):
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


class SchemaGraph(ObjectType):
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


class SchemaImporter(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Extensions(self) -> SchemaImporterExtensionCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_Extensions(self) -> SchemaImporterExtensionCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SchemaObjectCache(ObjectType):
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


class SchemaObjectWriter(ObjectType):
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


class SerializableMapping(SpecialMapping):
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


class Soap(ObjectType):
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


class Soap12(ObjectType):
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


class SoapAttributeAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, attributeName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeName(self) -> StringType: ...
    
    @AttributeName.setter
    def AttributeName(self, value: StringType) -> None: ...
    
    @property
    def DataType(self) -> StringType: ...
    
    @DataType.setter
    def DataType(self, value: StringType) -> None: ...
    
    @property
    def Namespace(self) -> StringType: ...
    
    @Namespace.setter
    def Namespace(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_AttributeName(self) -> StringType: ...
    
    def get_DataType(self) -> StringType: ...
    
    def get_Namespace(self) -> StringType: ...
    
    def set_AttributeName(self, value: StringType) -> VoidType: ...
    
    def set_DataType(self, value: StringType) -> VoidType: ...
    
    def set_Namespace(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapAttributeOverrides(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> SoapAttributes: ...
    
    @property
    def Item(self) -> SoapAttributes: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Add(self, type: TypeType, attributes: SoapAttributes) -> VoidType: ...
    
    @overload
    def Add(self, type: TypeType, member: StringType, attributes: SoapAttributes) -> VoidType: ...
    
    @overload
    def get_Item(self, type: TypeType) -> SoapAttributes: ...
    
    @overload
    def get_Item(self, type: TypeType, member: StringType) -> SoapAttributes: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapAttributes(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, provider: ICustomAttributeProvider): ...
    
    # ---------- Properties ---------- #
    
    @property
    def SoapAttribute(self) -> SoapAttributeAttribute: ...
    
    @SoapAttribute.setter
    def SoapAttribute(self, value: SoapAttributeAttribute) -> None: ...
    
    @property
    def SoapDefaultValue(self) -> ObjectType: ...
    
    @SoapDefaultValue.setter
    def SoapDefaultValue(self, value: ObjectType) -> None: ...
    
    @property
    def SoapElement(self) -> SoapElementAttribute: ...
    
    @SoapElement.setter
    def SoapElement(self, value: SoapElementAttribute) -> None: ...
    
    @property
    def SoapEnum(self) -> SoapEnumAttribute: ...
    
    @SoapEnum.setter
    def SoapEnum(self, value: SoapEnumAttribute) -> None: ...
    
    @property
    def SoapIgnore(self) -> BooleanType: ...
    
    @SoapIgnore.setter
    def SoapIgnore(self, value: BooleanType) -> None: ...
    
    @property
    def SoapType(self) -> SoapTypeAttribute: ...
    
    @SoapType.setter
    def SoapType(self, value: SoapTypeAttribute) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_SoapAttribute(self) -> SoapAttributeAttribute: ...
    
    def get_SoapDefaultValue(self) -> ObjectType: ...
    
    def get_SoapElement(self) -> SoapElementAttribute: ...
    
    def get_SoapEnum(self) -> SoapEnumAttribute: ...
    
    def get_SoapIgnore(self) -> BooleanType: ...
    
    def get_SoapType(self) -> SoapTypeAttribute: ...
    
    def set_SoapAttribute(self, value: SoapAttributeAttribute) -> VoidType: ...
    
    def set_SoapDefaultValue(self, value: ObjectType) -> VoidType: ...
    
    def set_SoapElement(self, value: SoapElementAttribute) -> VoidType: ...
    
    def set_SoapEnum(self, value: SoapEnumAttribute) -> VoidType: ...
    
    def set_SoapIgnore(self, value: BooleanType) -> VoidType: ...
    
    def set_SoapType(self, value: SoapTypeAttribute) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapCodeExporter(CodeExporter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, codeNamespace: CodeNamespace): ...
    
    @overload
    def __init__(self, codeNamespace: CodeNamespace, codeCompileUnit: CodeCompileUnit): ...
    
    @overload
    def __init__(self, codeNamespace: CodeNamespace, codeCompileUnit: CodeCompileUnit, options: CodeGenerationOptions): ...
    
    @overload
    def __init__(self, codeNamespace: CodeNamespace, codeCompileUnit: CodeCompileUnit, options: CodeGenerationOptions, mappings: Hashtable): ...
    
    @overload
    def __init__(self, codeNamespace: CodeNamespace, codeCompileUnit: CodeCompileUnit, codeProvider: CodeDomProvider, options: CodeGenerationOptions, mappings: Hashtable): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def AddMappingMetadata(self, metadata: CodeAttributeDeclarationCollection, member: XmlMemberMapping, forceUseMemberName: BooleanType) -> VoidType: ...
    
    @overload
    def AddMappingMetadata(self, metadata: CodeAttributeDeclarationCollection, member: XmlMemberMapping) -> VoidType: ...
    
    def ExportMembersMapping(self, xmlMembersMapping: XmlMembersMapping) -> VoidType: ...
    
    def ExportTypeMapping(self, xmlTypeMapping: XmlTypeMapping) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapElementAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, elementName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DataType(self) -> StringType: ...
    
    @DataType.setter
    def DataType(self, value: StringType) -> None: ...
    
    @property
    def ElementName(self) -> StringType: ...
    
    @ElementName.setter
    def ElementName(self, value: StringType) -> None: ...
    
    @property
    def IsNullable(self) -> BooleanType: ...
    
    @IsNullable.setter
    def IsNullable(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_DataType(self) -> StringType: ...
    
    def get_ElementName(self) -> StringType: ...
    
    def get_IsNullable(self) -> BooleanType: ...
    
    def set_DataType(self, value: StringType) -> VoidType: ...
    
    def set_ElementName(self, value: StringType) -> VoidType: ...
    
    def set_IsNullable(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapEnumAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> StringType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapIgnoreAttribute(Attribute, _Attribute):
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


class SoapIncludeAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, type: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Type(self) -> TypeType: ...
    
    @Type.setter
    def Type(self, value: TypeType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Type(self) -> TypeType: ...
    
    def set_Type(self, value: TypeType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapReflectionImporter(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, defaultNamespace: StringType): ...
    
    @overload
    def __init__(self, attributeOverrides: SoapAttributeOverrides): ...
    
    @overload
    def __init__(self, attributeOverrides: SoapAttributeOverrides, defaultNamespace: StringType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def ImportMembersMapping(self, elementName: StringType, ns: StringType, members: ArrayType[XmlReflectionMember]) -> XmlMembersMapping: ...
    
    @overload
    def ImportMembersMapping(self, elementName: StringType, ns: StringType, members: ArrayType[XmlReflectionMember], hasWrapperElement: BooleanType, writeAccessors: BooleanType) -> XmlMembersMapping: ...
    
    @overload
    def ImportMembersMapping(self, elementName: StringType, ns: StringType, members: ArrayType[XmlReflectionMember], hasWrapperElement: BooleanType, writeAccessors: BooleanType, validate: BooleanType) -> XmlMembersMapping: ...
    
    @overload
    def ImportMembersMapping(self, elementName: StringType, ns: StringType, members: ArrayType[XmlReflectionMember], hasWrapperElement: BooleanType, writeAccessors: BooleanType, validate: BooleanType, access: XmlMappingAccess) -> XmlMembersMapping: ...
    
    @overload
    def ImportTypeMapping(self, type: TypeType) -> XmlTypeMapping: ...
    
    @overload
    def ImportTypeMapping(self, type: TypeType, defaultNamespace: StringType) -> XmlTypeMapping: ...
    
    def IncludeType(self, type: TypeType) -> VoidType: ...
    
    def IncludeTypes(self, provider: ICustomAttributeProvider) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapSchemaExporter(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, schemas: XmlSchemas): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def ExportMembersMapping(self, xmlMembersMapping: XmlMembersMapping) -> VoidType: ...
    
    @overload
    def ExportMembersMapping(self, xmlMembersMapping: XmlMembersMapping, exportEnclosingType: BooleanType) -> VoidType: ...
    
    def ExportTypeMapping(self, xmlTypeMapping: XmlTypeMapping) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapSchemaImporter(SchemaImporter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, schemas: XmlSchemas): ...
    
    @overload
    def __init__(self, schemas: XmlSchemas, typeIdentifiers: CodeIdentifiers): ...
    
    @overload
    def __init__(self, schemas: XmlSchemas, typeIdentifiers: CodeIdentifiers, options: CodeGenerationOptions): ...
    
    @overload
    def __init__(self, schemas: XmlSchemas, options: CodeGenerationOptions, context: ImportContext): ...
    
    @overload
    def __init__(self, schemas: XmlSchemas, options: CodeGenerationOptions, codeProvider: CodeDomProvider, context: ImportContext): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ImportDerivedTypeMapping(self, name: XmlQualifiedName, baseType: TypeType, baseTypeCanBeIndirect: BooleanType) -> XmlTypeMapping: ...
    
    @overload
    def ImportMembersMapping(self, name: StringType, ns: StringType, members: ArrayType[SoapSchemaMember]) -> XmlMembersMapping: ...
    
    @overload
    def ImportMembersMapping(self, name: StringType, ns: StringType, members: ArrayType[SoapSchemaMember], hasWrapperElement: BooleanType) -> XmlMembersMapping: ...
    
    @overload
    def ImportMembersMapping(self, name: StringType, ns: StringType, member: SoapSchemaMember) -> XmlMembersMapping: ...
    
    @overload
    def ImportMembersMapping(self, name: StringType, ns: StringType, members: ArrayType[SoapSchemaMember], hasWrapperElement: BooleanType, baseType: TypeType, baseTypeCanBeIndirect: BooleanType) -> XmlMembersMapping: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapSchemaMember(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def MemberName(self) -> StringType: ...
    
    @MemberName.setter
    def MemberName(self, value: StringType) -> None: ...
    
    @property
    def MemberType(self) -> XmlQualifiedName: ...
    
    @MemberType.setter
    def MemberType(self, value: XmlQualifiedName) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_MemberName(self) -> StringType: ...
    
    def get_MemberType(self) -> XmlQualifiedName: ...
    
    def set_MemberName(self, value: StringType) -> VoidType: ...
    
    def set_MemberType(self, value: XmlQualifiedName) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SoapTypeAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, typeName: StringType): ...
    
    @overload
    def __init__(self, typeName: StringType, ns: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IncludeInSchema(self) -> BooleanType: ...
    
    @IncludeInSchema.setter
    def IncludeInSchema(self, value: BooleanType) -> None: ...
    
    @property
    def Namespace(self) -> StringType: ...
    
    @Namespace.setter
    def Namespace(self, value: StringType) -> None: ...
    
    @property
    def TypeName(self) -> StringType: ...
    
    @TypeName.setter
    def TypeName(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_IncludeInSchema(self) -> BooleanType: ...
    
    def get_Namespace(self) -> StringType: ...
    
    def get_TypeName(self) -> StringType: ...
    
    def set_IncludeInSchema(self, value: BooleanType) -> VoidType: ...
    
    def set_Namespace(self, value: StringType) -> VoidType: ...
    
    def set_TypeName(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SourceInfo(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def Arg(self) -> StringType: ...
    
    @property
    def ILG(self) -> CodeGenerator: ...
    
    @property
    def MemberInfo(self) -> MemberInfo: ...
    
    @property
    def Source(self) -> StringType: ...
    
    @Source.setter
    def Source(self, value: StringType) -> None: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self, source: StringType, arg: StringType, memberInfo: MemberInfo, type: TypeType, ilg: CodeGenerator): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CastTo(self, td: TypeDesc) -> SourceInfo: ...
    
    def Equals(self, obj: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    def Load(self, elementType: TypeType) -> VoidType: ...
    
    def LoadAddress(self, elementType: TypeType) -> VoidType: ...
    
    @staticmethod
    def op_Equality(a: SourceInfo, b: SourceInfo) -> BooleanType: ...
    
    @staticmethod
    def op_Implicit(source: SourceInfo) -> StringType: ...
    
    @staticmethod
    def op_Inequality(a: SourceInfo, b: SourceInfo) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SpecialMapping(TypeMapping):
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


class SpecialModel(TypeModel):
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


class StructMapping(TypeMapping, INameScope):
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


class StructModel(TypeModel):
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


class TempAssembly(ObjectType):
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


class TempAssemblyCache(ObjectType):
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


class TempAssemblyCacheKey(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Equals(self, o: ObjectType) -> BooleanType: ...
    
    def GetHashCode(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TextAccessor(Accessor):
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


class TypeDesc(ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ToString(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypeExtensions(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def TryConvertTo(targetType: TypeType, data: ObjectType, returnValue: ObjectType) -> Tuple[BooleanType, ObjectType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class TypeMapping(ABC, Mapping):
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


class TypeModel(ABC, ObjectType):
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


class TypeScope(ObjectType):
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


class UnreferencedObjectEventArgs(EventArgs):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, o: ObjectType, id: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def UnreferencedId(self) -> StringType: ...
    
    @property
    def UnreferencedObject(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_UnreferencedId(self) -> StringType: ...
    
    def get_UnreferencedObject(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UnreferencedObjectEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: UnreferencedObjectEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: UnreferencedObjectEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class UrtTypes(ObjectType):
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


class WorkItems(ObjectType):
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


class Wsdl(ObjectType):
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


class XmlAnyAttributeAttribute(Attribute, _Attribute):
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


class XmlAnyElementAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, name: StringType): ...
    
    @overload
    def __init__(self, name: StringType, ns: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def Namespace(self) -> StringType: ...
    
    @Namespace.setter
    def Namespace(self, value: StringType) -> None: ...
    
    @property
    def Order(self) -> IntType: ...
    
    @Order.setter
    def Order(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> StringType: ...
    
    def get_Namespace(self) -> StringType: ...
    
    def get_Order(self) -> IntType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_Namespace(self, value: StringType) -> VoidType: ...
    
    def set_Order(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlAnyElementAttributes(CollectionBase, IList, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> XmlAnyElementAttribute: ...
    
    @Item.setter
    def Item(self, value: XmlAnyElementAttribute) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, attribute: XmlAnyElementAttribute) -> IntType: ...
    
    def Contains(self, attribute: XmlAnyElementAttribute) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[XmlAnyElementAttribute], index: IntType) -> VoidType: ...
    
    def IndexOf(self, attribute: XmlAnyElementAttribute) -> IntType: ...
    
    def Insert(self, index: IntType, attribute: XmlAnyElementAttribute) -> VoidType: ...
    
    def Remove(self, attribute: XmlAnyElementAttribute) -> VoidType: ...
    
    def get_Item(self, index: IntType) -> XmlAnyElementAttribute: ...
    
    def set_Item(self, index: IntType, value: XmlAnyElementAttribute) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlArrayAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, elementName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def ElementName(self) -> StringType: ...
    
    @ElementName.setter
    def ElementName(self, value: StringType) -> None: ...
    
    @property
    def Form(self) -> XmlSchemaForm: ...
    
    @Form.setter
    def Form(self, value: XmlSchemaForm) -> None: ...
    
    @property
    def IsNullable(self) -> BooleanType: ...
    
    @IsNullable.setter
    def IsNullable(self, value: BooleanType) -> None: ...
    
    @property
    def Namespace(self) -> StringType: ...
    
    @Namespace.setter
    def Namespace(self, value: StringType) -> None: ...
    
    @property
    def Order(self) -> IntType: ...
    
    @Order.setter
    def Order(self, value: IntType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_ElementName(self) -> StringType: ...
    
    def get_Form(self) -> XmlSchemaForm: ...
    
    def get_IsNullable(self) -> BooleanType: ...
    
    def get_Namespace(self) -> StringType: ...
    
    def get_Order(self) -> IntType: ...
    
    def set_ElementName(self, value: StringType) -> VoidType: ...
    
    def set_Form(self, value: XmlSchemaForm) -> VoidType: ...
    
    def set_IsNullable(self, value: BooleanType) -> VoidType: ...
    
    def set_Namespace(self, value: StringType) -> VoidType: ...
    
    def set_Order(self, value: IntType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlArrayItemAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, elementName: StringType): ...
    
    @overload
    def __init__(self, type: TypeType): ...
    
    @overload
    def __init__(self, elementName: StringType, type: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DataType(self) -> StringType: ...
    
    @DataType.setter
    def DataType(self, value: StringType) -> None: ...
    
    @property
    def ElementName(self) -> StringType: ...
    
    @ElementName.setter
    def ElementName(self, value: StringType) -> None: ...
    
    @property
    def Form(self) -> XmlSchemaForm: ...
    
    @Form.setter
    def Form(self, value: XmlSchemaForm) -> None: ...
    
    @property
    def IsNullable(self) -> BooleanType: ...
    
    @IsNullable.setter
    def IsNullable(self, value: BooleanType) -> None: ...
    
    @property
    def Namespace(self) -> StringType: ...
    
    @Namespace.setter
    def Namespace(self, value: StringType) -> None: ...
    
    @property
    def NestingLevel(self) -> IntType: ...
    
    @NestingLevel.setter
    def NestingLevel(self, value: IntType) -> None: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    @Type.setter
    def Type(self, value: TypeType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_DataType(self) -> StringType: ...
    
    def get_ElementName(self) -> StringType: ...
    
    def get_Form(self) -> XmlSchemaForm: ...
    
    def get_IsNullable(self) -> BooleanType: ...
    
    def get_Namespace(self) -> StringType: ...
    
    def get_NestingLevel(self) -> IntType: ...
    
    def get_Type(self) -> TypeType: ...
    
    def set_DataType(self, value: StringType) -> VoidType: ...
    
    def set_ElementName(self, value: StringType) -> VoidType: ...
    
    def set_Form(self, value: XmlSchemaForm) -> VoidType: ...
    
    def set_IsNullable(self, value: BooleanType) -> VoidType: ...
    
    def set_Namespace(self, value: StringType) -> VoidType: ...
    
    def set_NestingLevel(self, value: IntType) -> VoidType: ...
    
    def set_Type(self, value: TypeType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlArrayItemAttributes(CollectionBase, IList, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> XmlArrayItemAttribute: ...
    
    @Item.setter
    def Item(self, value: XmlArrayItemAttribute) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, attribute: XmlArrayItemAttribute) -> IntType: ...
    
    def Contains(self, attribute: XmlArrayItemAttribute) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[XmlArrayItemAttribute], index: IntType) -> VoidType: ...
    
    def IndexOf(self, attribute: XmlArrayItemAttribute) -> IntType: ...
    
    def Insert(self, index: IntType, attribute: XmlArrayItemAttribute) -> VoidType: ...
    
    def Remove(self, attribute: XmlArrayItemAttribute) -> VoidType: ...
    
    def get_Item(self, index: IntType) -> XmlArrayItemAttribute: ...
    
    def set_Item(self, index: IntType, value: XmlArrayItemAttribute) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlAttributeAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, attributeName: StringType): ...
    
    @overload
    def __init__(self, type: TypeType): ...
    
    @overload
    def __init__(self, attributeName: StringType, type: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeName(self) -> StringType: ...
    
    @AttributeName.setter
    def AttributeName(self, value: StringType) -> None: ...
    
    @property
    def DataType(self) -> StringType: ...
    
    @DataType.setter
    def DataType(self, value: StringType) -> None: ...
    
    @property
    def Form(self) -> XmlSchemaForm: ...
    
    @Form.setter
    def Form(self, value: XmlSchemaForm) -> None: ...
    
    @property
    def Namespace(self) -> StringType: ...
    
    @Namespace.setter
    def Namespace(self, value: StringType) -> None: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    @Type.setter
    def Type(self, value: TypeType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_AttributeName(self) -> StringType: ...
    
    def get_DataType(self) -> StringType: ...
    
    def get_Form(self) -> XmlSchemaForm: ...
    
    def get_Namespace(self) -> StringType: ...
    
    def get_Type(self) -> TypeType: ...
    
    def set_AttributeName(self, value: StringType) -> VoidType: ...
    
    def set_DataType(self, value: StringType) -> VoidType: ...
    
    def set_Form(self, value: XmlSchemaForm) -> VoidType: ...
    
    def set_Namespace(self, value: StringType) -> VoidType: ...
    
    def set_Type(self, value: TypeType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlAttributeComparer(ObjectType, IComparer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Compare(self, o1: ObjectType, o2: ObjectType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlAttributeEventArgs(EventArgs):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Attr(self) -> XmlAttribute: ...
    
    @property
    def ExpectedAttributes(self) -> StringType: ...
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    @property
    def ObjectBeingDeserialized(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_Attr(self) -> XmlAttribute: ...
    
    def get_ExpectedAttributes(self) -> StringType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    def get_ObjectBeingDeserialized(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlAttributeEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: XmlAttributeEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: XmlAttributeEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlAttributeOverrides(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> XmlAttributes: ...
    
    @property
    def Item(self) -> XmlAttributes: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Add(self, type: TypeType, attributes: XmlAttributes) -> VoidType: ...
    
    @overload
    def Add(self, type: TypeType, member: StringType, attributes: XmlAttributes) -> VoidType: ...
    
    @overload
    def get_Item(self, type: TypeType) -> XmlAttributes: ...
    
    @overload
    def get_Item(self, type: TypeType, member: StringType) -> XmlAttributes: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlAttributes(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, provider: ICustomAttributeProvider): ...
    
    # ---------- Properties ---------- #
    
    @property
    def XmlAnyAttribute(self) -> XmlAnyAttributeAttribute: ...
    
    @XmlAnyAttribute.setter
    def XmlAnyAttribute(self, value: XmlAnyAttributeAttribute) -> None: ...
    
    @property
    def XmlAnyElements(self) -> XmlAnyElementAttributes: ...
    
    @property
    def XmlArray(self) -> XmlArrayAttribute: ...
    
    @XmlArray.setter
    def XmlArray(self, value: XmlArrayAttribute) -> None: ...
    
    @property
    def XmlArrayItems(self) -> XmlArrayItemAttributes: ...
    
    @property
    def XmlAttribute(self) -> XmlAttributeAttribute: ...
    
    @XmlAttribute.setter
    def XmlAttribute(self, value: XmlAttributeAttribute) -> None: ...
    
    @property
    def XmlChoiceIdentifier(self) -> XmlChoiceIdentifierAttribute: ...
    
    @property
    def XmlDefaultValue(self) -> ObjectType: ...
    
    @XmlDefaultValue.setter
    def XmlDefaultValue(self, value: ObjectType) -> None: ...
    
    @property
    def XmlElements(self) -> XmlElementAttributes: ...
    
    @property
    def XmlEnum(self) -> XmlEnumAttribute: ...
    
    @XmlEnum.setter
    def XmlEnum(self, value: XmlEnumAttribute) -> None: ...
    
    @property
    def XmlIgnore(self) -> BooleanType: ...
    
    @XmlIgnore.setter
    def XmlIgnore(self, value: BooleanType) -> None: ...
    
    @property
    def XmlRoot(self) -> XmlRootAttribute: ...
    
    @XmlRoot.setter
    def XmlRoot(self, value: XmlRootAttribute) -> None: ...
    
    @property
    def XmlText(self) -> XmlTextAttribute: ...
    
    @XmlText.setter
    def XmlText(self, value: XmlTextAttribute) -> None: ...
    
    @property
    def XmlType(self) -> XmlTypeAttribute: ...
    
    @XmlType.setter
    def XmlType(self, value: XmlTypeAttribute) -> None: ...
    
    @property
    def Xmlns(self) -> BooleanType: ...
    
    @Xmlns.setter
    def Xmlns(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_XmlAnyAttribute(self) -> XmlAnyAttributeAttribute: ...
    
    def get_XmlAnyElements(self) -> XmlAnyElementAttributes: ...
    
    def get_XmlArray(self) -> XmlArrayAttribute: ...
    
    def get_XmlArrayItems(self) -> XmlArrayItemAttributes: ...
    
    def get_XmlAttribute(self) -> XmlAttributeAttribute: ...
    
    def get_XmlChoiceIdentifier(self) -> XmlChoiceIdentifierAttribute: ...
    
    def get_XmlDefaultValue(self) -> ObjectType: ...
    
    def get_XmlElements(self) -> XmlElementAttributes: ...
    
    def get_XmlEnum(self) -> XmlEnumAttribute: ...
    
    def get_XmlIgnore(self) -> BooleanType: ...
    
    def get_XmlRoot(self) -> XmlRootAttribute: ...
    
    def get_XmlText(self) -> XmlTextAttribute: ...
    
    def get_XmlType(self) -> XmlTypeAttribute: ...
    
    def get_Xmlns(self) -> BooleanType: ...
    
    def set_XmlAnyAttribute(self, value: XmlAnyAttributeAttribute) -> VoidType: ...
    
    def set_XmlArray(self, value: XmlArrayAttribute) -> VoidType: ...
    
    def set_XmlAttribute(self, value: XmlAttributeAttribute) -> VoidType: ...
    
    def set_XmlDefaultValue(self, value: ObjectType) -> VoidType: ...
    
    def set_XmlEnum(self, value: XmlEnumAttribute) -> VoidType: ...
    
    def set_XmlIgnore(self, value: BooleanType) -> VoidType: ...
    
    def set_XmlRoot(self, value: XmlRootAttribute) -> VoidType: ...
    
    def set_XmlText(self, value: XmlTextAttribute) -> VoidType: ...
    
    def set_XmlType(self, value: XmlTypeAttribute) -> VoidType: ...
    
    def set_Xmlns(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlChoiceIdentifierAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def MemberName(self) -> StringType: ...
    
    @MemberName.setter
    def MemberName(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_MemberName(self) -> StringType: ...
    
    def set_MemberName(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlCodeExporter(CodeExporter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, codeNamespace: CodeNamespace): ...
    
    @overload
    def __init__(self, codeNamespace: CodeNamespace, codeCompileUnit: CodeCompileUnit): ...
    
    @overload
    def __init__(self, codeNamespace: CodeNamespace, codeCompileUnit: CodeCompileUnit, options: CodeGenerationOptions): ...
    
    @overload
    def __init__(self, codeNamespace: CodeNamespace, codeCompileUnit: CodeCompileUnit, options: CodeGenerationOptions, mappings: Hashtable): ...
    
    @overload
    def __init__(self, codeNamespace: CodeNamespace, codeCompileUnit: CodeCompileUnit, codeProvider: CodeDomProvider, options: CodeGenerationOptions, mappings: Hashtable): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def AddMappingMetadata(self, metadata: CodeAttributeDeclarationCollection, mapping: XmlTypeMapping, ns: StringType) -> VoidType: ...
    
    @overload
    def AddMappingMetadata(self, metadata: CodeAttributeDeclarationCollection, member: XmlMemberMapping, ns: StringType, forceUseMemberName: BooleanType) -> VoidType: ...
    
    @overload
    def AddMappingMetadata(self, metadata: CodeAttributeDeclarationCollection, member: XmlMemberMapping, ns: StringType) -> VoidType: ...
    
    def ExportMembersMapping(self, xmlMembersMapping: XmlMembersMapping) -> VoidType: ...
    
    def ExportTypeMapping(self, xmlTypeMapping: XmlTypeMapping) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlCountingReader(XmlReader, IDisposable, IXmlTextParser, IXmlLineInfo):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def AttributeCount(self) -> IntType: ...
    
    @property
    def BaseURI(self) -> StringType: ...
    
    @property
    def CanReadBinaryContent(self) -> BooleanType: ...
    
    @property
    def CanReadValueChunk(self) -> BooleanType: ...
    
    @property
    def CanResolveEntity(self) -> BooleanType: ...
    
    @property
    def Depth(self) -> IntType: ...
    
    @property
    def EOF(self) -> BooleanType: ...
    
    @property
    def HasAttributes(self) -> BooleanType: ...
    
    @property
    def HasValue(self) -> BooleanType: ...
    
    @property
    def IsDefault(self) -> BooleanType: ...
    
    @property
    def IsEmptyElement(self) -> BooleanType: ...
    
    @property
    def Item(self) -> StringType: ...
    
    @property
    def Item(self) -> StringType: ...
    
    @property
    def Item(self) -> StringType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NameTable(self) -> XmlNameTable: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def Prefix(self) -> StringType: ...
    
    @property
    def QuoteChar(self) -> CharType: ...
    
    @property
    def ReadState(self) -> ReadState: ...
    
    @property
    def SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    @property
    def Settings(self) -> XmlReaderSettings: ...
    
    @property
    def Value(self) -> StringType: ...
    
    @property
    def ValueType(self) -> TypeType: ...
    
    @property
    def XmlLang(self) -> StringType: ...
    
    @property
    def XmlSpace(self) -> XmlSpace: ...
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    @overload
    def GetAttribute(self, name: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, name: StringType, namespaceURI: StringType) -> StringType: ...
    
    @overload
    def GetAttribute(self, i: IntType) -> StringType: ...
    
    @overload
    def IsStartElement(self) -> BooleanType: ...
    
    @overload
    def IsStartElement(self, name: StringType) -> BooleanType: ...
    
    @overload
    def IsStartElement(self, localname: StringType, ns: StringType) -> BooleanType: ...
    
    def LookupNamespace(self, prefix: StringType) -> StringType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, name: StringType, ns: StringType) -> BooleanType: ...
    
    @overload
    def MoveToAttribute(self, i: IntType) -> VoidType: ...
    
    def MoveToContent(self) -> XmlNodeType: ...
    
    def MoveToElement(self) -> BooleanType: ...
    
    def MoveToFirstAttribute(self) -> BooleanType: ...
    
    def MoveToNextAttribute(self) -> BooleanType: ...
    
    def Read(self) -> BooleanType: ...
    
    def ReadAttributeValue(self) -> BooleanType: ...
    
    def ReadContentAs(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    def ReadContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadContentAsBoolean(self) -> BooleanType: ...
    
    def ReadContentAsDateTime(self) -> DateTime: ...
    
    def ReadContentAsDouble(self) -> DoubleType: ...
    
    def ReadContentAsInt(self) -> IntType: ...
    
    def ReadContentAsLong(self) -> LongType: ...
    
    def ReadContentAsObject(self) -> ObjectType: ...
    
    def ReadContentAsString(self) -> StringType: ...
    
    @overload
    def ReadElementContentAs(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver) -> ObjectType: ...
    
    @overload
    def ReadElementContentAs(self, returnType: TypeType, namespaceResolver: IXmlNamespaceResolver, localName: StringType, namespaceURI: StringType) -> ObjectType: ...
    
    def ReadElementContentAsBase64(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    def ReadElementContentAsBinHex(self, buffer: ArrayType[ByteType], index: IntType, count: IntType) -> IntType: ...
    
    @overload
    def ReadElementContentAsBoolean(self) -> BooleanType: ...
    
    @overload
    def ReadElementContentAsBoolean(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def ReadElementContentAsDateTime(self) -> DateTime: ...
    
    @overload
    def ReadElementContentAsDateTime(self, localName: StringType, namespaceURI: StringType) -> DateTime: ...
    
    @overload
    def ReadElementContentAsDouble(self) -> DoubleType: ...
    
    @overload
    def ReadElementContentAsDouble(self, localName: StringType, namespaceURI: StringType) -> DoubleType: ...
    
    @overload
    def ReadElementContentAsInt(self) -> IntType: ...
    
    @overload
    def ReadElementContentAsInt(self, localName: StringType, namespaceURI: StringType) -> IntType: ...
    
    @overload
    def ReadElementContentAsLong(self) -> LongType: ...
    
    @overload
    def ReadElementContentAsLong(self, localName: StringType, namespaceURI: StringType) -> LongType: ...
    
    @overload
    def ReadElementContentAsObject(self) -> ObjectType: ...
    
    @overload
    def ReadElementContentAsObject(self, localName: StringType, namespaceURI: StringType) -> ObjectType: ...
    
    @overload
    def ReadElementContentAsString(self) -> StringType: ...
    
    @overload
    def ReadElementContentAsString(self, localName: StringType, namespaceURI: StringType) -> StringType: ...
    
    @overload
    def ReadElementString(self) -> StringType: ...
    
    @overload
    def ReadElementString(self, name: StringType) -> StringType: ...
    
    @overload
    def ReadElementString(self, localname: StringType, ns: StringType) -> StringType: ...
    
    def ReadEndElement(self) -> VoidType: ...
    
    def ReadInnerXml(self) -> StringType: ...
    
    def ReadOuterXml(self) -> StringType: ...
    
    @overload
    def ReadStartElement(self) -> VoidType: ...
    
    @overload
    def ReadStartElement(self, name: StringType) -> VoidType: ...
    
    @overload
    def ReadStartElement(self, localname: StringType, ns: StringType) -> VoidType: ...
    
    def ReadString(self) -> StringType: ...
    
    def ReadSubtree(self) -> XmlReader: ...
    
    @overload
    def ReadToDescendant(self, name: StringType) -> BooleanType: ...
    
    @overload
    def ReadToDescendant(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def ReadToFollowing(self, name: StringType) -> BooleanType: ...
    
    @overload
    def ReadToFollowing(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    @overload
    def ReadToNextSibling(self, name: StringType) -> BooleanType: ...
    
    @overload
    def ReadToNextSibling(self, localName: StringType, namespaceURI: StringType) -> BooleanType: ...
    
    def ReadValueChunk(self, buffer: ArrayType[CharType], index: IntType, count: IntType) -> IntType: ...
    
    def ResolveEntity(self) -> VoidType: ...
    
    def Skip(self) -> VoidType: ...
    
    def get_AttributeCount(self) -> IntType: ...
    
    def get_BaseURI(self) -> StringType: ...
    
    def get_CanReadBinaryContent(self) -> BooleanType: ...
    
    def get_CanReadValueChunk(self) -> BooleanType: ...
    
    def get_CanResolveEntity(self) -> BooleanType: ...
    
    def get_Depth(self) -> IntType: ...
    
    def get_EOF(self) -> BooleanType: ...
    
    def get_HasAttributes(self) -> BooleanType: ...
    
    def get_HasValue(self) -> BooleanType: ...
    
    def get_IsDefault(self) -> BooleanType: ...
    
    def get_IsEmptyElement(self) -> BooleanType: ...
    
    @overload
    def get_Item(self, i: IntType) -> StringType: ...
    
    @overload
    def get_Item(self, name: StringType) -> StringType: ...
    
    @overload
    def get_Item(self, name: StringType, namespaceURI: StringType) -> StringType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NameTable(self) -> XmlNameTable: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_Prefix(self) -> StringType: ...
    
    def get_QuoteChar(self) -> CharType: ...
    
    def get_ReadState(self) -> ReadState: ...
    
    def get_SchemaInfo(self) -> IXmlSchemaInfo: ...
    
    def get_Settings(self) -> XmlReaderSettings: ...
    
    def get_Value(self) -> StringType: ...
    
    def get_ValueType(self) -> TypeType: ...
    
    def get_XmlLang(self) -> StringType: ...
    
    def get_XmlSpace(self) -> XmlSpace: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlCustomFormatter(ObjectType):
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


class XmlElementAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, elementName: StringType): ...
    
    @overload
    def __init__(self, type: TypeType): ...
    
    @overload
    def __init__(self, elementName: StringType, type: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DataType(self) -> StringType: ...
    
    @DataType.setter
    def DataType(self, value: StringType) -> None: ...
    
    @property
    def ElementName(self) -> StringType: ...
    
    @ElementName.setter
    def ElementName(self, value: StringType) -> None: ...
    
    @property
    def Form(self) -> XmlSchemaForm: ...
    
    @Form.setter
    def Form(self, value: XmlSchemaForm) -> None: ...
    
    @property
    def IsNullable(self) -> BooleanType: ...
    
    @IsNullable.setter
    def IsNullable(self, value: BooleanType) -> None: ...
    
    @property
    def Namespace(self) -> StringType: ...
    
    @Namespace.setter
    def Namespace(self, value: StringType) -> None: ...
    
    @property
    def Order(self) -> IntType: ...
    
    @Order.setter
    def Order(self, value: IntType) -> None: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    @Type.setter
    def Type(self, value: TypeType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_DataType(self) -> StringType: ...
    
    def get_ElementName(self) -> StringType: ...
    
    def get_Form(self) -> XmlSchemaForm: ...
    
    def get_IsNullable(self) -> BooleanType: ...
    
    def get_Namespace(self) -> StringType: ...
    
    def get_Order(self) -> IntType: ...
    
    def get_Type(self) -> TypeType: ...
    
    def set_DataType(self, value: StringType) -> VoidType: ...
    
    def set_ElementName(self, value: StringType) -> VoidType: ...
    
    def set_Form(self, value: XmlSchemaForm) -> VoidType: ...
    
    def set_IsNullable(self, value: BooleanType) -> VoidType: ...
    
    def set_Namespace(self, value: StringType) -> VoidType: ...
    
    def set_Order(self, value: IntType) -> VoidType: ...
    
    def set_Type(self, value: TypeType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlElementAttributes(CollectionBase, IList, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> XmlElementAttribute: ...
    
    @Item.setter
    def Item(self, value: XmlElementAttribute) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, attribute: XmlElementAttribute) -> IntType: ...
    
    def Contains(self, attribute: XmlElementAttribute) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[XmlElementAttribute], index: IntType) -> VoidType: ...
    
    def IndexOf(self, attribute: XmlElementAttribute) -> IntType: ...
    
    def Insert(self, index: IntType, attribute: XmlElementAttribute) -> VoidType: ...
    
    def Remove(self, attribute: XmlElementAttribute) -> VoidType: ...
    
    def get_Item(self, index: IntType) -> XmlElementAttribute: ...
    
    def set_Item(self, index: IntType, value: XmlElementAttribute) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlElementEventArgs(EventArgs):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Element(self) -> XmlElement: ...
    
    @property
    def ExpectedElements(self) -> StringType: ...
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    @property
    def ObjectBeingDeserialized(self) -> ObjectType: ...
    
    # ---------- Methods ---------- #
    
    def get_Element(self) -> XmlElement: ...
    
    def get_ExpectedElements(self) -> StringType: ...
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    def get_ObjectBeingDeserialized(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlElementEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: XmlElementEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: XmlElementEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlEnumAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, name: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> StringType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlFacetComparer(ObjectType, IComparer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Compare(self, o1: ObjectType, o2: ObjectType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlIgnoreAttribute(Attribute, _Attribute):
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


class XmlIncludeAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, type: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Type(self) -> TypeType: ...
    
    @Type.setter
    def Type(self, value: TypeType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Type(self) -> TypeType: ...
    
    def set_Type(self, value: TypeType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlMapping(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ElementName(self) -> StringType: ...
    
    @property
    def Namespace(self) -> StringType: ...
    
    @property
    def XsdElementName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def SetKey(self, key: StringType) -> VoidType: ...
    
    def get_ElementName(self) -> StringType: ...
    
    def get_Namespace(self) -> StringType: ...
    
    def get_XsdElementName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlMemberMapping(ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Any(self) -> BooleanType: ...
    
    @property
    def CheckSpecified(self) -> BooleanType: ...
    
    @property
    def ElementName(self) -> StringType: ...
    
    @property
    def MemberName(self) -> StringType: ...
    
    @property
    def Namespace(self) -> StringType: ...
    
    @property
    def TypeFullName(self) -> StringType: ...
    
    @property
    def TypeName(self) -> StringType: ...
    
    @property
    def TypeNamespace(self) -> StringType: ...
    
    @property
    def XsdElementName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def GenerateTypeName(self, codeProvider: CodeDomProvider) -> StringType: ...
    
    def get_Any(self) -> BooleanType: ...
    
    def get_CheckSpecified(self) -> BooleanType: ...
    
    def get_ElementName(self) -> StringType: ...
    
    def get_MemberName(self) -> StringType: ...
    
    def get_Namespace(self) -> StringType: ...
    
    def get_TypeFullName(self) -> StringType: ...
    
    def get_TypeName(self) -> StringType: ...
    
    def get_TypeNamespace(self) -> StringType: ...
    
    def get_XsdElementName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlMembersMapping(XmlMapping):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    @property
    def Item(self) -> XmlMemberMapping: ...
    
    @property
    def TypeName(self) -> StringType: ...
    
    @property
    def TypeNamespace(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Count(self) -> IntType: ...
    
    def get_Item(self, index: IntType) -> XmlMemberMapping: ...
    
    def get_TypeName(self) -> StringType: ...
    
    def get_TypeNamespace(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNamespaceDeclarationsAttribute(Attribute, _Attribute):
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


class XmlNodeEventArgs(EventArgs):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def LineNumber(self) -> IntType: ...
    
    @property
    def LinePosition(self) -> IntType: ...
    
    @property
    def LocalName(self) -> StringType: ...
    
    @property
    def Name(self) -> StringType: ...
    
    @property
    def NamespaceURI(self) -> StringType: ...
    
    @property
    def NodeType(self) -> XmlNodeType: ...
    
    @property
    def ObjectBeingDeserialized(self) -> ObjectType: ...
    
    @property
    def Text(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_LineNumber(self) -> IntType: ...
    
    def get_LinePosition(self) -> IntType: ...
    
    def get_LocalName(self) -> StringType: ...
    
    def get_Name(self) -> StringType: ...
    
    def get_NamespaceURI(self) -> StringType: ...
    
    def get_NodeType(self) -> XmlNodeType: ...
    
    def get_ObjectBeingDeserialized(self) -> ObjectType: ...
    
    def get_Text(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlNodeEventHandler(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, sender: ObjectType, e: XmlNodeEventArgs, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, sender: ObjectType, e: XmlNodeEventArgs) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlReflectionImporter(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, defaultNamespace: StringType): ...
    
    @overload
    def __init__(self, attributeOverrides: XmlAttributeOverrides): ...
    
    @overload
    def __init__(self, attributeOverrides: XmlAttributeOverrides, defaultNamespace: StringType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def ImportMembersMapping(self, elementName: StringType, ns: StringType, members: ArrayType[XmlReflectionMember], hasWrapperElement: BooleanType) -> XmlMembersMapping: ...
    
    @overload
    def ImportMembersMapping(self, elementName: StringType, ns: StringType, members: ArrayType[XmlReflectionMember], hasWrapperElement: BooleanType, rpc: BooleanType) -> XmlMembersMapping: ...
    
    @overload
    def ImportMembersMapping(self, elementName: StringType, ns: StringType, members: ArrayType[XmlReflectionMember], hasWrapperElement: BooleanType, rpc: BooleanType, openModel: BooleanType) -> XmlMembersMapping: ...
    
    @overload
    def ImportMembersMapping(self, elementName: StringType, ns: StringType, members: ArrayType[XmlReflectionMember], hasWrapperElement: BooleanType, rpc: BooleanType, openModel: BooleanType, access: XmlMappingAccess) -> XmlMembersMapping: ...
    
    @overload
    def ImportTypeMapping(self, type: TypeType) -> XmlTypeMapping: ...
    
    @overload
    def ImportTypeMapping(self, type: TypeType, defaultNamespace: StringType) -> XmlTypeMapping: ...
    
    @overload
    def ImportTypeMapping(self, type: TypeType, root: XmlRootAttribute) -> XmlTypeMapping: ...
    
    @overload
    def ImportTypeMapping(self, type: TypeType, root: XmlRootAttribute, defaultNamespace: StringType) -> XmlTypeMapping: ...
    
    def IncludeType(self, type: TypeType) -> VoidType: ...
    
    def IncludeTypes(self, provider: ICustomAttributeProvider) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlReflectionMember(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsReturnValue(self) -> BooleanType: ...
    
    @IsReturnValue.setter
    def IsReturnValue(self, value: BooleanType) -> None: ...
    
    @property
    def MemberName(self) -> StringType: ...
    
    @MemberName.setter
    def MemberName(self, value: StringType) -> None: ...
    
    @property
    def MemberType(self) -> TypeType: ...
    
    @MemberType.setter
    def MemberType(self, value: TypeType) -> None: ...
    
    @property
    def OverrideIsNullable(self) -> BooleanType: ...
    
    @OverrideIsNullable.setter
    def OverrideIsNullable(self, value: BooleanType) -> None: ...
    
    @property
    def SoapAttributes(self) -> SoapAttributes: ...
    
    @SoapAttributes.setter
    def SoapAttributes(self, value: SoapAttributes) -> None: ...
    
    @property
    def XmlAttributes(self) -> XmlAttributes: ...
    
    @XmlAttributes.setter
    def XmlAttributes(self, value: XmlAttributes) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_IsReturnValue(self) -> BooleanType: ...
    
    def get_MemberName(self) -> StringType: ...
    
    def get_MemberType(self) -> TypeType: ...
    
    def get_OverrideIsNullable(self) -> BooleanType: ...
    
    def get_SoapAttributes(self) -> SoapAttributes: ...
    
    def get_XmlAttributes(self) -> XmlAttributes: ...
    
    def set_IsReturnValue(self, value: BooleanType) -> VoidType: ...
    
    def set_MemberName(self, value: StringType) -> VoidType: ...
    
    def set_MemberType(self, value: TypeType) -> VoidType: ...
    
    def set_OverrideIsNullable(self, value: BooleanType) -> VoidType: ...
    
    def set_SoapAttributes(self, value: SoapAttributes) -> VoidType: ...
    
    def set_XmlAttributes(self, value: XmlAttributes) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlRootAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, elementName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DataType(self) -> StringType: ...
    
    @DataType.setter
    def DataType(self, value: StringType) -> None: ...
    
    @property
    def ElementName(self) -> StringType: ...
    
    @ElementName.setter
    def ElementName(self, value: StringType) -> None: ...
    
    @property
    def IsNullable(self) -> BooleanType: ...
    
    @IsNullable.setter
    def IsNullable(self, value: BooleanType) -> None: ...
    
    @property
    def Namespace(self) -> StringType: ...
    
    @Namespace.setter
    def Namespace(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_DataType(self) -> StringType: ...
    
    def get_ElementName(self) -> StringType: ...
    
    def get_IsNullable(self) -> BooleanType: ...
    
    def get_Namespace(self) -> StringType: ...
    
    def set_DataType(self, value: StringType) -> VoidType: ...
    
    def set_ElementName(self, value: StringType) -> VoidType: ...
    
    def set_IsNullable(self, value: BooleanType) -> VoidType: ...
    
    def set_Namespace(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaEnumerator(ObjectType, IEnumerator[XmlSchema], IDisposable, IEnumerator):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, list: XmlSchemas): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Current(self) -> XmlSchema: ...
    
    # ---------- Methods ---------- #
    
    def Dispose(self) -> VoidType: ...
    
    def MoveNext(self) -> BooleanType: ...
    
    def get_Current(self) -> XmlSchema: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaExporter(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, schemas: XmlSchemas): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def ExportAnyType(self, ns: StringType) -> StringType: ...
    
    @overload
    def ExportAnyType(self, members: XmlMembersMapping) -> StringType: ...
    
    @overload
    def ExportMembersMapping(self, xmlMembersMapping: XmlMembersMapping) -> VoidType: ...
    
    @overload
    def ExportMembersMapping(self, xmlMembersMapping: XmlMembersMapping, exportEnclosingType: BooleanType) -> VoidType: ...
    
    @overload
    def ExportTypeMapping(self, xmlTypeMapping: XmlTypeMapping) -> VoidType: ...
    
    @overload
    def ExportTypeMapping(self, xmlMembersMapping: XmlMembersMapping) -> XmlQualifiedName: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaImporter(SchemaImporter):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, schemas: XmlSchemas): ...
    
    @overload
    def __init__(self, schemas: XmlSchemas, typeIdentifiers: CodeIdentifiers): ...
    
    @overload
    def __init__(self, schemas: XmlSchemas, typeIdentifiers: CodeIdentifiers, options: CodeGenerationOptions): ...
    
    @overload
    def __init__(self, schemas: XmlSchemas, options: CodeGenerationOptions, context: ImportContext): ...
    
    @overload
    def __init__(self, schemas: XmlSchemas, options: CodeGenerationOptions, codeProvider: CodeDomProvider, context: ImportContext): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def ImportAnyType(self, typeName: XmlQualifiedName, elementName: StringType) -> XmlMembersMapping: ...
    
    @overload
    def ImportDerivedTypeMapping(self, name: XmlQualifiedName, baseType: TypeType) -> XmlTypeMapping: ...
    
    @overload
    def ImportDerivedTypeMapping(self, name: XmlQualifiedName, baseType: TypeType, baseTypeCanBeIndirect: BooleanType) -> XmlTypeMapping: ...
    
    @overload
    def ImportMembersMapping(self, name: XmlQualifiedName) -> XmlMembersMapping: ...
    
    @overload
    def ImportMembersMapping(self, names: ArrayType[XmlQualifiedName]) -> XmlMembersMapping: ...
    
    @overload
    def ImportMembersMapping(self, name: StringType, ns: StringType, members: ArrayType[SoapSchemaMember]) -> XmlMembersMapping: ...
    
    @overload
    def ImportMembersMapping(self, names: ArrayType[XmlQualifiedName], baseType: TypeType, baseTypeCanBeIndirect: BooleanType) -> XmlMembersMapping: ...
    
    @overload
    def ImportSchemaType(self, typeName: XmlQualifiedName) -> XmlTypeMapping: ...
    
    @overload
    def ImportSchemaType(self, typeName: XmlQualifiedName, baseType: TypeType) -> XmlTypeMapping: ...
    
    @overload
    def ImportSchemaType(self, typeName: XmlQualifiedName, baseType: TypeType, baseTypeCanBeIndirect: BooleanType) -> XmlTypeMapping: ...
    
    def ImportTypeMapping(self, name: XmlQualifiedName) -> XmlTypeMapping: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaObjectComparer(ObjectType, IComparer):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Compare(self, o1: ObjectType, o2: ObjectType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemaProviderAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, methodName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsAny(self) -> BooleanType: ...
    
    @IsAny.setter
    def IsAny(self, value: BooleanType) -> None: ...
    
    @property
    def MethodName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_IsAny(self) -> BooleanType: ...
    
    def get_MethodName(self) -> StringType: ...
    
    def set_IsAny(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSchemas(CollectionBase, IList, ICollection, IEnumerable, IEnumerable[XmlSchema]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def IsCompiled(self) -> BooleanType: ...
    
    @property
    def Item(self) -> XmlSchema: ...
    
    @Item.setter
    def Item(self, value: XmlSchema) -> None: ...
    
    @property
    def Item(self) -> XmlSchema: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def Add(self, schema: XmlSchema) -> IntType: ...
    
    @overload
    def Add(self, schema: XmlSchema, baseUri: Uri) -> IntType: ...
    
    @overload
    def Add(self, schemas: XmlSchemas) -> VoidType: ...
    
    def AddReference(self, schema: XmlSchema) -> VoidType: ...
    
    def Compile(self, handler: ValidationEventHandler, fullCompile: BooleanType) -> VoidType: ...
    
    @overload
    def Contains(self, schema: XmlSchema) -> BooleanType: ...
    
    @overload
    def Contains(self, targetNamespace: StringType) -> BooleanType: ...
    
    def CopyTo(self, array: ArrayType[XmlSchema], index: IntType) -> VoidType: ...
    
    def Find(self, name: XmlQualifiedName, type: TypeType) -> ObjectType: ...
    
    def GetSchemas(self, ns: StringType) -> IList: ...
    
    def IndexOf(self, schema: XmlSchema) -> IntType: ...
    
    def Insert(self, index: IntType, schema: XmlSchema) -> VoidType: ...
    
    @staticmethod
    def IsDataSet(schema: XmlSchema) -> BooleanType: ...
    
    def Remove(self, schema: XmlSchema) -> VoidType: ...
    
    def get_IsCompiled(self) -> BooleanType: ...
    
    @overload
    def get_Item(self, index: IntType) -> XmlSchema: ...
    
    @overload
    def get_Item(self, ns: StringType) -> XmlSchema: ...
    
    def set_Item(self, index: IntType, value: XmlSchema) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSerializationCodeGen(ObjectType):
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


class XmlSerializationCollectionFixupCallback(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, collection: ObjectType, collectionItems: ObjectType, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, collection: ObjectType, collectionItems: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSerializationFixupCallback(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, fixup: ObjectType, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, fixup: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSerializationGeneratedCode(ABC, ObjectType):
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


class XmlSerializationILGen(ObjectType):
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


class XmlSerializationPrimitiveReader(XmlSerializationReader):
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


class XmlSerializationPrimitiveWriter(XmlSerializationWriter):
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


class XmlSerializationReadCallback(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> ObjectType: ...
    
    def Invoke(self) -> ObjectType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSerializationReader(ABC, XmlSerializationGeneratedCode):
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


class XmlSerializationReaderCodeGen(XmlSerializationCodeGen):
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


class XmlSerializationReaderILGen(XmlSerializationILGen):
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


class XmlSerializationWriteCallback(MulticastDelegate, ICloneable, ISerializable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, object: ObjectType, method: NIntType): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def BeginInvoke(self, o: ObjectType, callback: AsyncCallback, object: ObjectType) -> IAsyncResult: ...
    
    def EndInvoke(self, result: IAsyncResult) -> VoidType: ...
    
    def Invoke(self, o: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSerializationWriter(ABC, XmlSerializationGeneratedCode):
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


class XmlSerializationWriterCodeGen(XmlSerializationCodeGen):
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


class XmlSerializationWriterILGen(XmlSerializationILGen):
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


class XmlSerializer(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, type: TypeType, overrides: XmlAttributeOverrides, extraTypes: ArrayType[TypeType], root: XmlRootAttribute, defaultNamespace: StringType): ...
    
    @overload
    def __init__(self, type: TypeType, root: XmlRootAttribute): ...
    
    @overload
    def __init__(self, type: TypeType, extraTypes: ArrayType[TypeType]): ...
    
    @overload
    def __init__(self, type: TypeType, overrides: XmlAttributeOverrides): ...
    
    @overload
    def __init__(self, xmlTypeMapping: XmlTypeMapping): ...
    
    @overload
    def __init__(self, type: TypeType): ...
    
    @overload
    def __init__(self, type: TypeType, defaultNamespace: StringType): ...
    
    @overload
    def __init__(self, type: TypeType, overrides: XmlAttributeOverrides, extraTypes: ArrayType[TypeType], root: XmlRootAttribute, defaultNamespace: StringType, location: StringType): ...
    
    @overload
    def __init__(self, type: TypeType, overrides: XmlAttributeOverrides, extraTypes: ArrayType[TypeType], root: XmlRootAttribute, defaultNamespace: StringType, location: StringType, evidence: Evidence): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CanDeserialize(self, xmlReader: XmlReader) -> BooleanType: ...
    
    @overload
    def Deserialize(self, stream: Stream) -> ObjectType: ...
    
    @overload
    def Deserialize(self, textReader: TextReader) -> ObjectType: ...
    
    @overload
    def Deserialize(self, xmlReader: XmlReader) -> ObjectType: ...
    
    @overload
    def Deserialize(self, xmlReader: XmlReader, events: XmlDeserializationEvents) -> ObjectType: ...
    
    @overload
    def Deserialize(self, xmlReader: XmlReader, encodingStyle: StringType) -> ObjectType: ...
    
    @overload
    def Deserialize(self, xmlReader: XmlReader, encodingStyle: StringType, events: XmlDeserializationEvents) -> ObjectType: ...
    
    @staticmethod
    @overload
    def FromMappings(mappings: ArrayType[XmlMapping]) -> ArrayType[XmlSerializer]: ...
    
    @staticmethod
    @overload
    def FromMappings(mappings: ArrayType[XmlMapping], type: TypeType) -> ArrayType[XmlSerializer]: ...
    
    @staticmethod
    @overload
    def FromMappings(mappings: ArrayType[XmlMapping], evidence: Evidence) -> ArrayType[XmlSerializer]: ...
    
    @staticmethod
    def FromTypes(types: ArrayType[TypeType]) -> ArrayType[XmlSerializer]: ...
    
    @staticmethod
    @overload
    def GenerateSerializer(types: ArrayType[TypeType], mappings: ArrayType[XmlMapping]) -> Assembly: ...
    
    @staticmethod
    @overload
    def GenerateSerializer(types: ArrayType[TypeType], mappings: ArrayType[XmlMapping], parameters: CompilerParameters) -> Assembly: ...
    
    @staticmethod
    @overload
    def GetXmlSerializerAssemblyName(type: TypeType) -> StringType: ...
    
    @staticmethod
    @overload
    def GetXmlSerializerAssemblyName(type: TypeType, defaultNamespace: StringType) -> StringType: ...
    
    @overload
    def Serialize(self, textWriter: TextWriter, o: ObjectType) -> VoidType: ...
    
    @overload
    def Serialize(self, textWriter: TextWriter, o: ObjectType, namespaces: XmlSerializerNamespaces) -> VoidType: ...
    
    @overload
    def Serialize(self, stream: Stream, o: ObjectType) -> VoidType: ...
    
    @overload
    def Serialize(self, stream: Stream, o: ObjectType, namespaces: XmlSerializerNamespaces) -> VoidType: ...
    
    @overload
    def Serialize(self, xmlWriter: XmlWriter, o: ObjectType) -> VoidType: ...
    
    @overload
    def Serialize(self, xmlWriter: XmlWriter, o: ObjectType, namespaces: XmlSerializerNamespaces) -> VoidType: ...
    
    @overload
    def Serialize(self, xmlWriter: XmlWriter, o: ObjectType, namespaces: XmlSerializerNamespaces, encodingStyle: StringType) -> VoidType: ...
    
    @overload
    def Serialize(self, xmlWriter: XmlWriter, o: ObjectType, namespaces: XmlSerializerNamespaces, encodingStyle: StringType, id: StringType) -> VoidType: ...
    
    def add_UnknownAttribute(self, value: XmlAttributeEventHandler) -> VoidType: ...
    
    def add_UnknownElement(self, value: XmlElementEventHandler) -> VoidType: ...
    
    def add_UnknownNode(self, value: XmlNodeEventHandler) -> VoidType: ...
    
    def add_UnreferencedObject(self, value: UnreferencedObjectEventHandler) -> VoidType: ...
    
    def remove_UnknownAttribute(self, value: XmlAttributeEventHandler) -> VoidType: ...
    
    def remove_UnknownElement(self, value: XmlElementEventHandler) -> VoidType: ...
    
    def remove_UnknownNode(self, value: XmlNodeEventHandler) -> VoidType: ...
    
    def remove_UnreferencedObject(self, value: UnreferencedObjectEventHandler) -> VoidType: ...
    
    # ---------- Events ---------- #
    
    UnknownAttribute: EventType[XmlAttributeEventHandler] = ...
    
    UnknownElement: EventType[XmlElementEventHandler] = ...
    
    UnknownNode: EventType[XmlNodeEventHandler] = ...
    
    UnreferencedObject: EventType[UnreferencedObjectEventHandler] = ...
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSerializerAssemblyAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, assemblyName: StringType): ...
    
    @overload
    def __init__(self, assemblyName: StringType, codeBase: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AssemblyName(self) -> StringType: ...
    
    @AssemblyName.setter
    def AssemblyName(self, value: StringType) -> None: ...
    
    @property
    def CodeBase(self) -> StringType: ...
    
    @CodeBase.setter
    def CodeBase(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_AssemblyName(self) -> StringType: ...
    
    def get_CodeBase(self) -> StringType: ...
    
    def set_AssemblyName(self, value: StringType) -> VoidType: ...
    
    def set_CodeBase(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSerializerCompilerParameters(ObjectType):
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


class XmlSerializerFactory(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def CreateSerializer(self, type: TypeType, overrides: XmlAttributeOverrides, extraTypes: ArrayType[TypeType], root: XmlRootAttribute, defaultNamespace: StringType) -> XmlSerializer: ...
    
    @overload
    def CreateSerializer(self, type: TypeType, extraTypes: ArrayType[TypeType]) -> XmlSerializer: ...
    
    @overload
    def CreateSerializer(self, xmlTypeMapping: XmlTypeMapping) -> XmlSerializer: ...
    
    @overload
    def CreateSerializer(self, type: TypeType) -> XmlSerializer: ...
    
    @overload
    def CreateSerializer(self, type: TypeType, defaultNamespace: StringType) -> XmlSerializer: ...
    
    @overload
    def CreateSerializer(self, type: TypeType, overrides: XmlAttributeOverrides, extraTypes: ArrayType[TypeType], root: XmlRootAttribute, defaultNamespace: StringType, location: StringType) -> XmlSerializer: ...
    
    @overload
    def CreateSerializer(self, type: TypeType, overrides: XmlAttributeOverrides, extraTypes: ArrayType[TypeType], root: XmlRootAttribute, defaultNamespace: StringType, location: StringType, evidence: Evidence) -> XmlSerializer: ...
    
    @overload
    def CreateSerializer(self, type: TypeType, root: XmlRootAttribute) -> XmlSerializer: ...
    
    @overload
    def CreateSerializer(self, type: TypeType, overrides: XmlAttributeOverrides) -> XmlSerializer: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSerializerImplementation(ABC, ObjectType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def ReadMethods(self) -> Hashtable: ...
    
    @property
    def Reader(self) -> XmlSerializationReader: ...
    
    @property
    def TypedSerializers(self) -> Hashtable: ...
    
    @property
    def WriteMethods(self) -> Hashtable: ...
    
    @property
    def Writer(self) -> XmlSerializationWriter: ...
    
    # ---------- Methods ---------- #
    
    def CanSerialize(self, type: TypeType) -> BooleanType: ...
    
    def GetSerializer(self, type: TypeType) -> XmlSerializer: ...
    
    def get_ReadMethods(self) -> Hashtable: ...
    
    def get_Reader(self) -> XmlSerializationReader: ...
    
    def get_TypedSerializers(self) -> Hashtable: ...
    
    def get_WriteMethods(self) -> Hashtable: ...
    
    def get_Writer(self) -> XmlSerializationWriter: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSerializerNamespaces(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, namespaces: XmlSerializerNamespaces): ...
    
    @overload
    def __init__(self, namespaces: ArrayType[XmlQualifiedName]): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Count(self) -> IntType: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, prefix: StringType, ns: StringType) -> VoidType: ...
    
    def ToArray(self) -> ArrayType[XmlQualifiedName]: ...
    
    def get_Count(self) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSerializerVersionAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, type: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Namespace(self) -> StringType: ...
    
    @Namespace.setter
    def Namespace(self, value: StringType) -> None: ...
    
    @property
    def ParentAssemblyId(self) -> StringType: ...
    
    @ParentAssemblyId.setter
    def ParentAssemblyId(self, value: StringType) -> None: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    @Type.setter
    def Type(self, value: TypeType) -> None: ...
    
    @property
    def Version(self) -> StringType: ...
    
    @Version.setter
    def Version(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Namespace(self) -> StringType: ...
    
    def get_ParentAssemblyId(self) -> StringType: ...
    
    def get_Type(self) -> TypeType: ...
    
    def get_Version(self) -> StringType: ...
    
    def set_Namespace(self, value: StringType) -> VoidType: ...
    
    def set_ParentAssemblyId(self, value: StringType) -> VoidType: ...
    
    def set_Type(self, value: TypeType) -> VoidType: ...
    
    def set_Version(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlTextAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, type: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DataType(self) -> StringType: ...
    
    @DataType.setter
    def DataType(self, value: StringType) -> None: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    @Type.setter
    def Type(self, value: TypeType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_DataType(self) -> StringType: ...
    
    def get_Type(self) -> TypeType: ...
    
    def set_DataType(self, value: StringType) -> VoidType: ...
    
    def set_Type(self, value: TypeType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlTypeAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, typeName: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def AnonymousType(self) -> BooleanType: ...
    
    @AnonymousType.setter
    def AnonymousType(self, value: BooleanType) -> None: ...
    
    @property
    def IncludeInSchema(self) -> BooleanType: ...
    
    @IncludeInSchema.setter
    def IncludeInSchema(self, value: BooleanType) -> None: ...
    
    @property
    def Namespace(self) -> StringType: ...
    
    @Namespace.setter
    def Namespace(self, value: StringType) -> None: ...
    
    @property
    def TypeName(self) -> StringType: ...
    
    @TypeName.setter
    def TypeName(self, value: StringType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_AnonymousType(self) -> BooleanType: ...
    
    def get_IncludeInSchema(self) -> BooleanType: ...
    
    def get_Namespace(self) -> StringType: ...
    
    def get_TypeName(self) -> StringType: ...
    
    def set_AnonymousType(self, value: BooleanType) -> VoidType: ...
    
    def set_IncludeInSchema(self, value: BooleanType) -> VoidType: ...
    
    def set_Namespace(self, value: StringType) -> VoidType: ...
    
    def set_TypeName(self, value: StringType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlTypeMapping(XmlMapping):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def TypeFullName(self) -> StringType: ...
    
    @property
    def TypeName(self) -> StringType: ...
    
    @property
    def XsdTypeName(self) -> StringType: ...
    
    @property
    def XsdTypeNamespace(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_TypeFullName(self) -> StringType: ...
    
    def get_TypeName(self) -> StringType: ...
    
    def get_XsdTypeName(self) -> StringType: ...
    
    def get_XsdTypeNamespace(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlnsAccessor(Accessor):
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


# ---------- Structs ---------- #

class XmlDeserializationEvents(ValueType):
    # No Fields
    
    # No Constructors
    
    # ---------- Properties ---------- #
    
    @property
    def OnUnknownAttribute(self) -> XmlAttributeEventHandler: ...
    
    @OnUnknownAttribute.setter
    def OnUnknownAttribute(self, value: XmlAttributeEventHandler) -> None: ...
    
    @property
    def OnUnknownElement(self) -> XmlElementEventHandler: ...
    
    @OnUnknownElement.setter
    def OnUnknownElement(self, value: XmlElementEventHandler) -> None: ...
    
    @property
    def OnUnknownNode(self) -> XmlNodeEventHandler: ...
    
    @OnUnknownNode.setter
    def OnUnknownNode(self, value: XmlNodeEventHandler) -> None: ...
    
    @property
    def OnUnreferencedObject(self) -> UnreferencedObjectEventHandler: ...
    
    @OnUnreferencedObject.setter
    def OnUnreferencedObject(self, value: UnreferencedObjectEventHandler) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_OnUnknownAttribute(self) -> XmlAttributeEventHandler: ...
    
    def get_OnUnknownElement(self) -> XmlElementEventHandler: ...
    
    def get_OnUnknownNode(self) -> XmlNodeEventHandler: ...
    
    def get_OnUnreferencedObject(self) -> UnreferencedObjectEventHandler: ...
    
    def set_OnUnknownAttribute(self, value: XmlAttributeEventHandler) -> VoidType: ...
    
    def set_OnUnknownElement(self, value: XmlElementEventHandler) -> VoidType: ...
    
    def set_OnUnknownNode(self, value: XmlNodeEventHandler) -> VoidType: ...
    
    def set_OnUnreferencedObject(self, value: UnreferencedObjectEventHandler) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Interfaces ---------- #

class INameScope(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> ObjectType: ...
    
    @Item.setter
    def Item(self, value: ObjectType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Item(self, name: StringType, ns: StringType) -> ObjectType: ...
    
    def set_Item(self, name: StringType, ns: StringType, value: ObjectType) -> VoidType: ...
    
    # No Events


class IXmlSerializable(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetSchema(self) -> XmlSchema: ...
    
    def ReadXml(self, reader: XmlReader) -> VoidType: ...
    
    def WriteXml(self, writer: XmlWriter) -> VoidType: ...
    
    # No Events


class IXmlTextParser(Protocol):
    # ---------- Properties ---------- #
    
    @property
    def Normalized(self) -> BooleanType: ...
    
    @Normalized.setter
    def Normalized(self, value: BooleanType) -> None: ...
    
    @property
    def WhitespaceHandling(self) -> WhitespaceHandling: ...
    
    @WhitespaceHandling.setter
    def WhitespaceHandling(self, value: WhitespaceHandling) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Normalized(self) -> BooleanType: ...
    
    def get_WhitespaceHandling(self) -> WhitespaceHandling: ...
    
    def set_Normalized(self, value: BooleanType) -> VoidType: ...
    
    def set_WhitespaceHandling(self, value: WhitespaceHandling) -> VoidType: ...
    
    # No Events


# ---------- Enums ---------- #

class Cmp(Enum):
    LessThan: IntType = 0
    EqualTo: IntType = 1
    LessThanOrEqualTo: IntType = 2
    GreaterThan: IntType = 3
    NotEqualTo: IntType = 4
    GreaterThanOrEqualTo: IntType = 5


class CodeGenerationOptions(Enum):
    #None: IntType = 0
    GenerateProperties: IntType = 1
    GenerateNewAsync: IntType = 2
    GenerateOldAsync: IntType = 4
    GenerateOrder: IntType = 8
    EnableDataBinding: IntType = 16


class SoapAttributeFlags(Enum):
    Enum: IntType = 1
    Type: IntType = 2
    Element: IntType = 4
    Attribute: IntType = 8


class SpecifiedAccessor(Enum):
    #None: IntType = 0
    ReadOnly: IntType = 1
    ReadWrite: IntType = 2


class TypeFlags(Enum):
    #None: IntType = 0
    Abstract: IntType = 1
    Reference: IntType = 2
    Special: IntType = 4
    CanBeAttributeValue: IntType = 8
    CanBeTextValue: IntType = 16
    CanBeElementValue: IntType = 32
    HasCustomFormatter: IntType = 64
    AmbiguousDataType: IntType = 128
    IgnoreDefault: IntType = 512
    HasIsEmpty: IntType = 1024
    HasDefaultConstructor: IntType = 2048
    XmlEncodingNotRequired: IntType = 4096
    UseReflection: IntType = 16384
    CollapseWhitespace: IntType = 32768
    OptionalValue: IntType = 65536
    CtorInaccessible: IntType = 131072
    UsePrivateImplementation: IntType = 262144
    GenericInterface: IntType = 524288
    Unsupported: IntType = 1048576


class TypeKind(Enum):
    Root: IntType = 0
    Primitive: IntType = 1
    Enum: IntType = 2
    Struct: IntType = 3
    Class: IntType = 4
    Array: IntType = 5
    Collection: IntType = 6
    Enumerable: IntType = 7
    Void: IntType = 8
    Node: IntType = 9
    Attribute: IntType = 10
    Serializable: IntType = 11


class XmlAttributeFlags(Enum):
    Enum: IntType = 1
    Array: IntType = 2
    Text: IntType = 4
    ArrayItems: IntType = 8
    Elements: IntType = 16
    Attribute: IntType = 32
    Root: IntType = 64
    Type: IntType = 128
    AnyElements: IntType = 256
    AnyAttribute: IntType = 512
    ChoiceIdentifier: IntType = 1024
    XmlnsDeclarations: IntType = 2048


class XmlMappingAccess(Enum):
    #None: IntType = 0
    Read: IntType = 1
    Write: IntType = 2


# ---------- Delegates ---------- #

UnreferencedObjectEventHandler = Callable[[ObjectType, UnreferencedObjectEventArgs], VoidType]

XmlAttributeEventHandler = Callable[[ObjectType, XmlAttributeEventArgs], VoidType]

XmlElementEventHandler = Callable[[ObjectType, XmlElementEventArgs], VoidType]

XmlNodeEventHandler = Callable[[ObjectType, XmlNodeEventArgs], VoidType]

XmlSerializationCollectionFixupCallback = Callable[[ObjectType, ObjectType], VoidType]

XmlSerializationFixupCallback = Callable[[ObjectType], VoidType]

XmlSerializationReadCallback = Callable[[], ObjectType]

XmlSerializationWriteCallback = Callable[[ObjectType], VoidType]

__all__ = [
    Accessor,
    AccessorMapping,
    AppSettings,
    ArgBuilder,
    ArrayMapping,
    ArrayModel,
    AttributeAccessor,
    CaseInsensitiveKeyComparer,
    ChoiceIdentifierAccessor,
    CodeExporter,
    CodeGenerator,
    CodeGeneratorConversionException,
    CodeIdentifier,
    CodeIdentifiers,
    Compiler,
    ConstantMapping,
    ConstantModel,
    DynamicAssemblies,
    ElementAccessor,
    EnumMapping,
    EnumModel,
    FieldModel,
    ForState,
    IfState,
    ImportContext,
    ImportStructWorkItem,
    IndentedWriter,
    LocalScope,
    Mapping,
    MemberMapping,
    MemberMappingComparer,
    MembersMapping,
    MethodBuilderInfo,
    ModelScope,
    NameKey,
    NameTable,
    NullableMapping,
    PrimitiveMapping,
    PrimitiveModel,
    QNameComparer,
    RecursionLimiter,
    ReflectionAwareCodeGen,
    ReflectionAwareILGen,
    SchemaGraph,
    SchemaImporter,
    SchemaObjectCache,
    SchemaObjectWriter,
    SerializableMapping,
    Soap,
    Soap12,
    SoapAttributeAttribute,
    SoapAttributeOverrides,
    SoapAttributes,
    SoapCodeExporter,
    SoapElementAttribute,
    SoapEnumAttribute,
    SoapIgnoreAttribute,
    SoapIncludeAttribute,
    SoapReflectionImporter,
    SoapSchemaExporter,
    SoapSchemaImporter,
    SoapSchemaMember,
    SoapTypeAttribute,
    SourceInfo,
    SpecialMapping,
    SpecialModel,
    StructMapping,
    StructModel,
    TempAssembly,
    TempAssemblyCache,
    TempAssemblyCacheKey,
    TextAccessor,
    TypeDesc,
    TypeExtensions,
    TypeMapping,
    TypeModel,
    TypeScope,
    UnreferencedObjectEventArgs,
    UnreferencedObjectEventHandler,
    UrtTypes,
    WorkItems,
    Wsdl,
    XmlAnyAttributeAttribute,
    XmlAnyElementAttribute,
    XmlAnyElementAttributes,
    XmlArrayAttribute,
    XmlArrayItemAttribute,
    XmlArrayItemAttributes,
    XmlAttributeAttribute,
    XmlAttributeComparer,
    XmlAttributeEventArgs,
    XmlAttributeEventHandler,
    XmlAttributeOverrides,
    XmlAttributes,
    XmlChoiceIdentifierAttribute,
    XmlCodeExporter,
    XmlCountingReader,
    XmlCustomFormatter,
    XmlElementAttribute,
    XmlElementAttributes,
    XmlElementEventArgs,
    XmlElementEventHandler,
    XmlEnumAttribute,
    XmlFacetComparer,
    XmlIgnoreAttribute,
    XmlIncludeAttribute,
    XmlMapping,
    XmlMemberMapping,
    XmlMembersMapping,
    XmlNamespaceDeclarationsAttribute,
    XmlNodeEventArgs,
    XmlNodeEventHandler,
    XmlReflectionImporter,
    XmlReflectionMember,
    XmlRootAttribute,
    XmlSchemaEnumerator,
    XmlSchemaExporter,
    XmlSchemaImporter,
    XmlSchemaObjectComparer,
    XmlSchemaProviderAttribute,
    XmlSchemas,
    XmlSerializationCodeGen,
    XmlSerializationCollectionFixupCallback,
    XmlSerializationFixupCallback,
    XmlSerializationGeneratedCode,
    XmlSerializationILGen,
    XmlSerializationPrimitiveReader,
    XmlSerializationPrimitiveWriter,
    XmlSerializationReadCallback,
    XmlSerializationReader,
    XmlSerializationReaderCodeGen,
    XmlSerializationReaderILGen,
    XmlSerializationWriteCallback,
    XmlSerializationWriter,
    XmlSerializationWriterCodeGen,
    XmlSerializationWriterILGen,
    XmlSerializer,
    XmlSerializerAssemblyAttribute,
    XmlSerializerCompilerParameters,
    XmlSerializerFactory,
    XmlSerializerImplementation,
    XmlSerializerNamespaces,
    XmlSerializerVersionAttribute,
    XmlTextAttribute,
    XmlTypeAttribute,
    XmlTypeMapping,
    XmlnsAccessor,
    XmlDeserializationEvents,
    INameScope,
    IXmlSerializable,
    IXmlTextParser,
    Cmp,
    CodeGenerationOptions,
    SoapAttributeFlags,
    SpecifiedAccessor,
    TypeFlags,
    TypeKind,
    XmlAttributeFlags,
    XmlMappingAccess,
    UnreferencedObjectEventHandler,
    XmlAttributeEventHandler,
    XmlElementEventHandler,
    XmlNodeEventHandler,
    XmlSerializationCollectionFixupCallback,
    XmlSerializationFixupCallback,
    XmlSerializationReadCallback,
    XmlSerializationWriteCallback,
]
