from __future__ import annotations

from abc import ABC
from typing import Union, overload

from System import Boolean, Enum, Int32, Object, String, Type, Void
from System.Collections import ICollection, IEnumerable
from System.Configuration import ConfigurationElement, ConfigurationElementCollection, ConfigurationSection, ConfigurationSectionGroup, ConfigurationValidatorBase

# ---------- Types ---------- #

BooleanType = Union[bool, Boolean]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class ConfigurationStrings(ABC, ObjectType):
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


class ConfigurationStrings(ABC, ObjectType):
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


class DateTimeSerializationSection(ConfigurationSection):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Mode(self) -> DateTimeSerializationMode: ...
    
    @Mode.setter
    def Mode(self, value: DateTimeSerializationMode) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Mode(self) -> DateTimeSerializationMode: ...
    
    def set_Mode(self, value: DateTimeSerializationMode) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class DateTimeSerializationMode(Enum):
        Default: IntType = 0
        Roundtrip: IntType = 1
        Local: IntType = 2
    


class DateTimeSerializationSection(ConfigurationSection):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Mode(self) -> DateTimeSerializationMode: ...
    
    @Mode.setter
    def Mode(self, value: DateTimeSerializationMode) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Mode(self) -> DateTimeSerializationMode: ...
    
    def set_Mode(self, value: DateTimeSerializationMode) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # ---------- Sub Enums ---------- #
    
    class DateTimeSerializationMode(Enum):
        Default: IntType = 0
        Roundtrip: IntType = 1
        Local: IntType = 2
    


class RootedPathValidator(ConfigurationValidatorBase):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CanValidate(self, type: TypeType) -> BooleanType: ...
    
    def Validate(self, value: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RootedPathValidator(ConfigurationValidatorBase):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def CanValidate(self, type: TypeType) -> BooleanType: ...
    
    def Validate(self, value: ObjectType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SchemaImporterExtensionElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, name: StringType, type: StringType): ...
    
    @overload
    def __init__(self, name: StringType, type: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    @Type.setter
    def Type(self, value: TypeType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> StringType: ...
    
    def get_Type(self) -> TypeType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_Type(self, value: TypeType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SchemaImporterExtensionElement(ConfigurationElement):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, name: StringType, type: StringType): ...
    
    @overload
    def __init__(self, name: StringType, type: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Name(self) -> StringType: ...
    
    @Name.setter
    def Name(self, value: StringType) -> None: ...
    
    @property
    def Type(self) -> TypeType: ...
    
    @Type.setter
    def Type(self, value: TypeType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_Name(self) -> StringType: ...
    
    def get_Type(self) -> TypeType: ...
    
    def set_Name(self, value: StringType) -> VoidType: ...
    
    def set_Type(self, value: TypeType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SchemaImporterExtensionElementCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> SchemaImporterExtensionElement: ...
    
    @Item.setter
    def Item(self, value: SchemaImporterExtensionElement) -> None: ...
    
    @property
    def Item(self) -> SchemaImporterExtensionElement: ...
    
    @Item.setter
    def Item(self, value: SchemaImporterExtensionElement) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, element: SchemaImporterExtensionElement) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def IndexOf(self, element: SchemaImporterExtensionElement) -> IntType: ...
    
    @overload
    def Remove(self, element: SchemaImporterExtensionElement) -> VoidType: ...
    
    @overload
    def Remove(self, name: StringType) -> VoidType: ...
    
    def RemoveAt(self, index: IntType) -> VoidType: ...
    
    @overload
    def get_Item(self, index: IntType) -> SchemaImporterExtensionElement: ...
    
    @overload
    def get_Item(self, name: StringType) -> SchemaImporterExtensionElement: ...
    
    @overload
    def set_Item(self, index: IntType, value: SchemaImporterExtensionElement) -> VoidType: ...
    
    @overload
    def set_Item(self, name: StringType, value: SchemaImporterExtensionElement) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SchemaImporterExtensionElementCollection(ConfigurationElementCollection, ICollection, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Item(self) -> SchemaImporterExtensionElement: ...
    
    @Item.setter
    def Item(self, value: SchemaImporterExtensionElement) -> None: ...
    
    @property
    def Item(self) -> SchemaImporterExtensionElement: ...
    
    @Item.setter
    def Item(self, value: SchemaImporterExtensionElement) -> None: ...
    
    # ---------- Methods ---------- #
    
    def Add(self, element: SchemaImporterExtensionElement) -> VoidType: ...
    
    def Clear(self) -> VoidType: ...
    
    def IndexOf(self, element: SchemaImporterExtensionElement) -> IntType: ...
    
    @overload
    def Remove(self, element: SchemaImporterExtensionElement) -> VoidType: ...
    
    @overload
    def Remove(self, name: StringType) -> VoidType: ...
    
    def RemoveAt(self, index: IntType) -> VoidType: ...
    
    @overload
    def get_Item(self, index: IntType) -> SchemaImporterExtensionElement: ...
    
    @overload
    def get_Item(self, name: StringType) -> SchemaImporterExtensionElement: ...
    
    @overload
    def set_Item(self, index: IntType, value: SchemaImporterExtensionElement) -> VoidType: ...
    
    @overload
    def set_Item(self, name: StringType, value: SchemaImporterExtensionElement) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SchemaImporterExtensionsSection(ConfigurationSection):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def SchemaImporterExtensions(self) -> SchemaImporterExtensionElementCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_SchemaImporterExtensions(self) -> SchemaImporterExtensionElementCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SchemaImporterExtensionsSection(ConfigurationSection):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def SchemaImporterExtensions(self) -> SchemaImporterExtensionElementCollection: ...
    
    # ---------- Methods ---------- #
    
    def get_SchemaImporterExtensions(self) -> SchemaImporterExtensionElementCollection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerializationSectionGroup(ConfigurationSectionGroup):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DateTimeSerialization(self) -> DateTimeSerializationSection: ...
    
    @property
    def SchemaImporterExtensions(self) -> SchemaImporterExtensionsSection: ...
    
    @property
    def XmlSerializer(self) -> XmlSerializerSection: ...
    
    # ---------- Methods ---------- #
    
    def get_DateTimeSerialization(self) -> DateTimeSerializationSection: ...
    
    def get_SchemaImporterExtensions(self) -> SchemaImporterExtensionsSection: ...
    
    def get_XmlSerializer(self) -> XmlSerializerSection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SerializationSectionGroup(ConfigurationSectionGroup):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def DateTimeSerialization(self) -> DateTimeSerializationSection: ...
    
    @property
    def SchemaImporterExtensions(self) -> SchemaImporterExtensionsSection: ...
    
    @property
    def XmlSerializer(self) -> XmlSerializerSection: ...
    
    # ---------- Methods ---------- #
    
    def get_DateTimeSerialization(self) -> DateTimeSerializationSection: ...
    
    def get_SchemaImporterExtensions(self) -> SchemaImporterExtensionsSection: ...
    
    def get_XmlSerializer(self) -> XmlSerializerSection: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSerializerSection(ConfigurationSection):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CheckDeserializeAdvances(self) -> BooleanType: ...
    
    @CheckDeserializeAdvances.setter
    def CheckDeserializeAdvances(self, value: BooleanType) -> None: ...
    
    @property
    def TempFilesLocation(self) -> StringType: ...
    
    @TempFilesLocation.setter
    def TempFilesLocation(self, value: StringType) -> None: ...
    
    @property
    def UseLegacySerializerGeneration(self) -> BooleanType: ...
    
    @UseLegacySerializerGeneration.setter
    def UseLegacySerializerGeneration(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_CheckDeserializeAdvances(self) -> BooleanType: ...
    
    def get_TempFilesLocation(self) -> StringType: ...
    
    def get_UseLegacySerializerGeneration(self) -> BooleanType: ...
    
    def set_CheckDeserializeAdvances(self, value: BooleanType) -> VoidType: ...
    
    def set_TempFilesLocation(self, value: StringType) -> VoidType: ...
    
    def set_UseLegacySerializerGeneration(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class XmlSerializerSection(ConfigurationSection):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CheckDeserializeAdvances(self) -> BooleanType: ...
    
    @CheckDeserializeAdvances.setter
    def CheckDeserializeAdvances(self, value: BooleanType) -> None: ...
    
    @property
    def TempFilesLocation(self) -> StringType: ...
    
    @TempFilesLocation.setter
    def TempFilesLocation(self, value: StringType) -> None: ...
    
    @property
    def UseLegacySerializerGeneration(self) -> BooleanType: ...
    
    @UseLegacySerializerGeneration.setter
    def UseLegacySerializerGeneration(self, value: BooleanType) -> None: ...
    
    # ---------- Methods ---------- #
    
    def get_CheckDeserializeAdvances(self) -> BooleanType: ...
    
    def get_TempFilesLocation(self) -> StringType: ...
    
    def get_UseLegacySerializerGeneration(self) -> BooleanType: ...
    
    def set_CheckDeserializeAdvances(self, value: BooleanType) -> VoidType: ...
    
    def set_TempFilesLocation(self, value: StringType) -> VoidType: ...
    
    def set_UseLegacySerializerGeneration(self, value: BooleanType) -> VoidType: ...
    
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
    ConfigurationStrings,
    DateTimeSerializationSection,
    RootedPathValidator,
    SchemaImporterExtensionElement,
    SchemaImporterExtensionElementCollection,
    SchemaImporterExtensionsSection,
    SerializationSectionGroup,
    XmlSerializerSection,
]
