from __future__ import annotations

from abc import ABC
from typing import List, Protocol, Tuple, Union, overload

from System import Array, Attribute, Boolean, Byte, Enum, Exception, Func, IDisposable, Int32, Object, String, SystemException, Type, ValueType, Void
from System.Collections import IComparer, IDictionaryEnumerator, IEnumerable, IEqualityComparer
from System.Collections.Generic import Dictionary, IComparer, IEnumerable, IEnumerator, IEqualityComparer
from System.Globalization import CultureInfo
from System.IO import Stream, UnmanagedMemoryStream
from System.Reflection import Assembly
from System.Runtime.InteropServices import _Attribute, _Exception
from System.Runtime.Serialization import ISerializable
from System.Threading import StackCrawlMark

# ---------- Types ---------- #

ArrayType = Union[List, Array]
BooleanType = Union[bool, Boolean]
ByteType = Union[int, Byte]
IntType = Union[int, Int32]
ObjectType = Object
StringType = Union[str, String]
TypeType = Union[type, Type]
VoidType = Union[None, Void]

# ---------- Classes ---------- #

class FastResourceComparer(ObjectType, IComparer, IEqualityComparer, IComparer[StringType], IEqualityComparer[StringType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Compare(self, a: ObjectType, b: ObjectType) -> IntType: ...
    
    @overload
    def Compare(self, a: StringType, b: StringType) -> IntType: ...
    
    @staticmethod
    @overload
    def CompareOrdinal(a: StringType, bytes: ArrayType[ByteType], bCharLength: IntType) -> IntType: ...
    
    @staticmethod
    @overload
    def CompareOrdinal(bytes: ArrayType[ByteType], aCharLength: IntType, b: StringType) -> IntType: ...
    
    @overload
    def Equals(self, a: StringType, b: StringType) -> BooleanType: ...
    
    @overload
    def Equals(self, a: ObjectType, b: ObjectType) -> BooleanType: ...
    
    @overload
    def GetHashCode(self, key: ObjectType) -> IntType: ...
    
    @overload
    def GetHashCode(self, key: StringType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FastResourceComparer(ObjectType, IComparer, IEqualityComparer, IComparer[StringType], IEqualityComparer[StringType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Compare(self, a: ObjectType, b: ObjectType) -> IntType: ...
    
    @overload
    def Compare(self, a: StringType, b: StringType) -> IntType: ...
    
    @staticmethod
    @overload
    def CompareOrdinal(a: StringType, bytes: ArrayType[ByteType], bCharLength: IntType) -> IntType: ...
    
    @staticmethod
    @overload
    def CompareOrdinal(bytes: ArrayType[ByteType], aCharLength: IntType, b: StringType) -> IntType: ...
    
    @overload
    def Equals(self, a: StringType, b: StringType) -> BooleanType: ...
    
    @overload
    def Equals(self, a: ObjectType, b: ObjectType) -> BooleanType: ...
    
    @overload
    def GetHashCode(self, key: ObjectType) -> IntType: ...
    
    @overload
    def GetHashCode(self, key: StringType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FastResourceComparer(ObjectType, IComparer, IEqualityComparer, IComparer[StringType], IEqualityComparer[StringType]):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def Compare(self, a: ObjectType, b: ObjectType) -> IntType: ...
    
    @overload
    def Compare(self, a: StringType, b: StringType) -> IntType: ...
    
    @staticmethod
    @overload
    def CompareOrdinal(a: StringType, bytes: ArrayType[ByteType], bCharLength: IntType) -> IntType: ...
    
    @staticmethod
    @overload
    def CompareOrdinal(bytes: ArrayType[ByteType], aCharLength: IntType, b: StringType) -> IntType: ...
    
    @overload
    def Equals(self, a: StringType, b: StringType) -> BooleanType: ...
    
    @overload
    def Equals(self, a: ObjectType, b: ObjectType) -> BooleanType: ...
    
    @overload
    def GetHashCode(self, key: ObjectType) -> IntType: ...
    
    @overload
    def GetHashCode(self, key: StringType) -> IntType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileBasedResourceGroveler(ObjectType, IResourceGroveler):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, mediator: ResourceManagerMediator): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GrovelForResourceSet(self, culture: CultureInfo, localResourceSets: Dictionary[StringType, ResourceSet], tryParents: BooleanType, createIfNotExists: BooleanType, stackMark: StackCrawlMark) -> Tuple[ResourceSet, StackCrawlMark]: ...
    
    def HasNeutralResources(self, culture: CultureInfo, defaultResName: StringType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileBasedResourceGroveler(ObjectType, IResourceGroveler):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, mediator: ResourceManagerMediator): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GrovelForResourceSet(self, culture: CultureInfo, localResourceSets: Dictionary[StringType, ResourceSet], tryParents: BooleanType, createIfNotExists: BooleanType, stackMark: StackCrawlMark) -> Tuple[ResourceSet, StackCrawlMark]: ...
    
    def HasNeutralResources(self, culture: CultureInfo, defaultResName: StringType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class FileBasedResourceGroveler(ObjectType, IResourceGroveler):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, mediator: ResourceManagerMediator): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GrovelForResourceSet(self, culture: CultureInfo, localResourceSets: Dictionary[StringType, ResourceSet], tryParents: BooleanType, createIfNotExists: BooleanType, stackMark: StackCrawlMark) -> Tuple[ResourceSet, StackCrawlMark]: ...
    
    def HasNeutralResources(self, culture: CultureInfo, defaultResName: StringType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManifestBasedResourceGroveler(ObjectType, IResourceGroveler):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, mediator: ResourceManagerMediator): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GrovelForResourceSet(self, culture: CultureInfo, localResourceSets: Dictionary[StringType, ResourceSet], tryParents: BooleanType, createIfNotExists: BooleanType, stackMark: StackCrawlMark) -> Tuple[ResourceSet, StackCrawlMark]: ...
    
    def HasNeutralResources(self, culture: CultureInfo, defaultResName: StringType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManifestBasedResourceGroveler(ObjectType, IResourceGroveler):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, mediator: ResourceManagerMediator): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GrovelForResourceSet(self, culture: CultureInfo, localResourceSets: Dictionary[StringType, ResourceSet], tryParents: BooleanType, createIfNotExists: BooleanType, stackMark: StackCrawlMark) -> Tuple[ResourceSet, StackCrawlMark]: ...
    
    def HasNeutralResources(self, culture: CultureInfo, defaultResName: StringType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ManifestBasedResourceGroveler(ObjectType, IResourceGroveler):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, mediator: ResourceManagerMediator): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GrovelForResourceSet(self, culture: CultureInfo, localResourceSets: Dictionary[StringType, ResourceSet], tryParents: BooleanType, createIfNotExists: BooleanType, stackMark: StackCrawlMark) -> Tuple[ResourceSet, StackCrawlMark]: ...
    
    def HasNeutralResources(self, culture: CultureInfo, defaultResName: StringType) -> BooleanType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MissingManifestResourceException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MissingManifestResourceException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MissingManifestResourceException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MissingSatelliteAssemblyException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, cultureName: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CultureName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_CultureName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MissingSatelliteAssemblyException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, cultureName: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CultureName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_CultureName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class MissingSatelliteAssemblyException(SystemException, ISerializable, _Exception):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, message: StringType): ...
    
    @overload
    def __init__(self, message: StringType, cultureName: StringType): ...
    
    @overload
    def __init__(self, message: StringType, inner: Exception): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CultureName(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_CultureName(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NeutralResourcesLanguageAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, cultureName: StringType): ...
    
    @overload
    def __init__(self, cultureName: StringType, location: UltimateResourceFallbackLocation): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CultureName(self) -> StringType: ...
    
    @property
    def Location(self) -> UltimateResourceFallbackLocation: ...
    
    # ---------- Methods ---------- #
    
    def get_CultureName(self) -> StringType: ...
    
    def get_Location(self) -> UltimateResourceFallbackLocation: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NeutralResourcesLanguageAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, cultureName: StringType): ...
    
    @overload
    def __init__(self, cultureName: StringType, location: UltimateResourceFallbackLocation): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CultureName(self) -> StringType: ...
    
    @property
    def Location(self) -> UltimateResourceFallbackLocation: ...
    
    # ---------- Methods ---------- #
    
    def get_CultureName(self) -> StringType: ...
    
    def get_Location(self) -> UltimateResourceFallbackLocation: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class NeutralResourcesLanguageAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, cultureName: StringType): ...
    
    @overload
    def __init__(self, cultureName: StringType, location: UltimateResourceFallbackLocation): ...
    
    # ---------- Properties ---------- #
    
    @property
    def CultureName(self) -> StringType: ...
    
    @property
    def Location(self) -> UltimateResourceFallbackLocation: ...
    
    # ---------- Methods ---------- #
    
    def get_CultureName(self) -> StringType: ...
    
    def get_Location(self) -> UltimateResourceFallbackLocation: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PRIExceptionInfo(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def _PackageSimpleName(self) -> StringType: ...
    
    @_PackageSimpleName.setter
    def _PackageSimpleName(self, value: StringType) -> None: ...
    
    @property
    def _ResWFile(self) -> StringType: ...
    
    @_ResWFile.setter
    def _ResWFile(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PRIExceptionInfo(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def _PackageSimpleName(self) -> StringType: ...
    
    @_PackageSimpleName.setter
    def _PackageSimpleName(self, value: StringType) -> None: ...
    
    @property
    def _ResWFile(self) -> StringType: ...
    
    @_ResWFile.setter
    def _ResWFile(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class PRIExceptionInfo(ObjectType):
    # ---------- Fields ---------- #
    
    @property
    def _PackageSimpleName(self) -> StringType: ...
    
    @_PackageSimpleName.setter
    def _PackageSimpleName(self, value: StringType) -> None: ...
    
    @property
    def _ResWFile(self) -> StringType: ...
    
    @_ResWFile.setter
    def _ResWFile(self, value: StringType) -> None: ...
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ResourceFallbackManager(ObjectType, IEnumerable[CultureInfo], IEnumerable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetEnumerator(self) -> IEnumerator[CultureInfo]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ResourceFallbackManager(ObjectType, IEnumerable[CultureInfo], IEnumerable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetEnumerator(self) -> IEnumerator[CultureInfo]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ResourceFallbackManager(ObjectType, IEnumerable[CultureInfo], IEnumerable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetEnumerator(self) -> IEnumerator[CultureInfo]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ResourceManager(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def HeaderVersionNumber() -> IntType: ...
    
    @staticmethod
    @property
    def MagicNumber() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, baseName: StringType, assembly: Assembly): ...
    
    @overload
    def __init__(self, baseName: StringType, assembly: Assembly, usingResourceSet: TypeType): ...
    
    @overload
    def __init__(self, resourceSource: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BaseName(self) -> StringType: ...
    
    @property
    def IgnoreCase(self) -> BooleanType: ...
    
    @IgnoreCase.setter
    def IgnoreCase(self, value: BooleanType) -> None: ...
    
    @property
    def ResourceSetType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CreateFileBasedResourceManager(baseName: StringType, resourceDir: StringType, usingResourceSet: TypeType) -> ResourceManager: ...
    
    @overload
    def GetObject(self, name: StringType) -> ObjectType: ...
    
    @overload
    def GetObject(self, name: StringType, culture: CultureInfo) -> ObjectType: ...
    
    def GetResourceSet(self, culture: CultureInfo, createIfNotExists: BooleanType, tryParents: BooleanType) -> ResourceSet: ...
    
    @overload
    def GetStream(self, name: StringType) -> UnmanagedMemoryStream: ...
    
    @overload
    def GetStream(self, name: StringType, culture: CultureInfo) -> UnmanagedMemoryStream: ...
    
    @overload
    def GetString(self, name: StringType) -> StringType: ...
    
    @overload
    def GetString(self, name: StringType, culture: CultureInfo) -> StringType: ...
    
    def ReleaseAllResources(self) -> VoidType: ...
    
    def get_BaseName(self) -> StringType: ...
    
    def get_IgnoreCase(self) -> BooleanType: ...
    
    def get_ResourceSetType(self) -> TypeType: ...
    
    def set_IgnoreCase(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ResourceManager(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def HeaderVersionNumber() -> IntType: ...
    
    @staticmethod
    @property
    def MagicNumber() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, baseName: StringType, assembly: Assembly): ...
    
    @overload
    def __init__(self, baseName: StringType, assembly: Assembly, usingResourceSet: TypeType): ...
    
    @overload
    def __init__(self, resourceSource: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BaseName(self) -> StringType: ...
    
    @property
    def IgnoreCase(self) -> BooleanType: ...
    
    @IgnoreCase.setter
    def IgnoreCase(self, value: BooleanType) -> None: ...
    
    @property
    def ResourceSetType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CreateFileBasedResourceManager(baseName: StringType, resourceDir: StringType, usingResourceSet: TypeType) -> ResourceManager: ...
    
    @overload
    def GetObject(self, name: StringType) -> ObjectType: ...
    
    @overload
    def GetObject(self, name: StringType, culture: CultureInfo) -> ObjectType: ...
    
    def GetResourceSet(self, culture: CultureInfo, createIfNotExists: BooleanType, tryParents: BooleanType) -> ResourceSet: ...
    
    @overload
    def GetStream(self, name: StringType) -> UnmanagedMemoryStream: ...
    
    @overload
    def GetStream(self, name: StringType, culture: CultureInfo) -> UnmanagedMemoryStream: ...
    
    @overload
    def GetString(self, name: StringType) -> StringType: ...
    
    @overload
    def GetString(self, name: StringType, culture: CultureInfo) -> StringType: ...
    
    def ReleaseAllResources(self) -> VoidType: ...
    
    def get_BaseName(self) -> StringType: ...
    
    def get_IgnoreCase(self) -> BooleanType: ...
    
    def get_ResourceSetType(self) -> TypeType: ...
    
    def set_IgnoreCase(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ResourceManager(ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def HeaderVersionNumber() -> IntType: ...
    
    @staticmethod
    @property
    def MagicNumber() -> IntType: ...
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, baseName: StringType, assembly: Assembly): ...
    
    @overload
    def __init__(self, baseName: StringType, assembly: Assembly, usingResourceSet: TypeType): ...
    
    @overload
    def __init__(self, resourceSource: TypeType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def BaseName(self) -> StringType: ...
    
    @property
    def IgnoreCase(self) -> BooleanType: ...
    
    @IgnoreCase.setter
    def IgnoreCase(self, value: BooleanType) -> None: ...
    
    @property
    def ResourceSetType(self) -> TypeType: ...
    
    # ---------- Methods ---------- #
    
    @staticmethod
    def CreateFileBasedResourceManager(baseName: StringType, resourceDir: StringType, usingResourceSet: TypeType) -> ResourceManager: ...
    
    @overload
    def GetObject(self, name: StringType) -> ObjectType: ...
    
    @overload
    def GetObject(self, name: StringType, culture: CultureInfo) -> ObjectType: ...
    
    def GetResourceSet(self, culture: CultureInfo, createIfNotExists: BooleanType, tryParents: BooleanType) -> ResourceSet: ...
    
    @overload
    def GetStream(self, name: StringType) -> UnmanagedMemoryStream: ...
    
    @overload
    def GetStream(self, name: StringType, culture: CultureInfo) -> UnmanagedMemoryStream: ...
    
    @overload
    def GetString(self, name: StringType) -> StringType: ...
    
    @overload
    def GetString(self, name: StringType, culture: CultureInfo) -> StringType: ...
    
    def ReleaseAllResources(self) -> VoidType: ...
    
    def get_BaseName(self) -> StringType: ...
    
    def get_IgnoreCase(self) -> BooleanType: ...
    
    def get_ResourceSetType(self) -> TypeType: ...
    
    def set_IgnoreCase(self, value: BooleanType) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ResourceReader(ObjectType, IResourceReader, IEnumerable, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, fileName: StringType): ...
    
    @overload
    def __init__(self, stream: Stream): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    def GetEnumerator(self) -> IDictionaryEnumerator: ...
    
    def GetResourceData(self, resourceName: StringType, resourceType: StringType, resourceData: ByteType) -> Tuple[VoidType, StringType, ByteType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ResourceReader(ObjectType, IResourceReader, IEnumerable, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, fileName: StringType): ...
    
    @overload
    def __init__(self, stream: Stream): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    def GetEnumerator(self) -> IDictionaryEnumerator: ...
    
    def GetResourceData(self, resourceName: StringType, resourceType: StringType, resourceData: ByteType) -> Tuple[VoidType, StringType, ByteType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ResourceReader(ObjectType, IResourceReader, IEnumerable, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, fileName: StringType): ...
    
    @overload
    def __init__(self, stream: Stream): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    def GetEnumerator(self) -> IDictionaryEnumerator: ...
    
    def GetResourceData(self, resourceName: StringType, resourceType: StringType, resourceData: ByteType) -> Tuple[VoidType, StringType, ByteType]: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ResourceSet(ObjectType, IDisposable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, fileName: StringType): ...
    
    @overload
    def __init__(self, stream: Stream): ...
    
    @overload
    def __init__(self, reader: IResourceReader): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    def GetDefaultReader(self) -> TypeType: ...
    
    def GetDefaultWriter(self) -> TypeType: ...
    
    def GetEnumerator(self) -> IDictionaryEnumerator: ...
    
    @overload
    def GetObject(self, name: StringType) -> ObjectType: ...
    
    @overload
    def GetObject(self, name: StringType, ignoreCase: BooleanType) -> ObjectType: ...
    
    @overload
    def GetString(self, name: StringType) -> StringType: ...
    
    @overload
    def GetString(self, name: StringType, ignoreCase: BooleanType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ResourceSet(ObjectType, IDisposable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, fileName: StringType): ...
    
    @overload
    def __init__(self, stream: Stream): ...
    
    @overload
    def __init__(self, reader: IResourceReader): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    def GetDefaultReader(self) -> TypeType: ...
    
    def GetDefaultWriter(self) -> TypeType: ...
    
    def GetEnumerator(self) -> IDictionaryEnumerator: ...
    
    @overload
    def GetObject(self, name: StringType) -> ObjectType: ...
    
    @overload
    def GetObject(self, name: StringType, ignoreCase: BooleanType) -> ObjectType: ...
    
    @overload
    def GetString(self, name: StringType) -> StringType: ...
    
    @overload
    def GetString(self, name: StringType, ignoreCase: BooleanType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ResourceSet(ObjectType, IDisposable, IEnumerable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, fileName: StringType): ...
    
    @overload
    def __init__(self, stream: Stream): ...
    
    @overload
    def __init__(self, reader: IResourceReader): ...
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    def GetDefaultReader(self) -> TypeType: ...
    
    def GetDefaultWriter(self) -> TypeType: ...
    
    def GetEnumerator(self) -> IDictionaryEnumerator: ...
    
    @overload
    def GetObject(self, name: StringType) -> ObjectType: ...
    
    @overload
    def GetObject(self, name: StringType, ignoreCase: BooleanType) -> ObjectType: ...
    
    @overload
    def GetString(self, name: StringType) -> StringType: ...
    
    @overload
    def GetString(self, name: StringType, ignoreCase: BooleanType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ResourceWriter(ObjectType, IResourceWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, fileName: StringType): ...
    
    @overload
    def __init__(self, stream: Stream): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeNameConverter(self) -> Func[TypeType, StringType]: ...
    
    @TypeNameConverter.setter
    def TypeNameConverter(self, value: Func[TypeType, StringType]) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def AddResource(self, name: StringType, value: StringType) -> VoidType: ...
    
    @overload
    def AddResource(self, name: StringType, value: ObjectType) -> VoidType: ...
    
    @overload
    def AddResource(self, name: StringType, value: Stream) -> VoidType: ...
    
    @overload
    def AddResource(self, name: StringType, value: Stream, closeAfterWrite: BooleanType) -> VoidType: ...
    
    @overload
    def AddResource(self, name: StringType, value: ArrayType[ByteType]) -> VoidType: ...
    
    def AddResourceData(self, name: StringType, typeName: StringType, serializedData: ArrayType[ByteType]) -> VoidType: ...
    
    def Close(self) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    def Generate(self) -> VoidType: ...
    
    def get_TypeNameConverter(self) -> Func[TypeType, StringType]: ...
    
    def set_TypeNameConverter(self, value: Func[TypeType, StringType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ResourceWriter(ObjectType, IResourceWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, fileName: StringType): ...
    
    @overload
    def __init__(self, stream: Stream): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeNameConverter(self) -> Func[TypeType, StringType]: ...
    
    @TypeNameConverter.setter
    def TypeNameConverter(self, value: Func[TypeType, StringType]) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def AddResource(self, name: StringType, value: StringType) -> VoidType: ...
    
    @overload
    def AddResource(self, name: StringType, value: ObjectType) -> VoidType: ...
    
    @overload
    def AddResource(self, name: StringType, value: Stream) -> VoidType: ...
    
    @overload
    def AddResource(self, name: StringType, value: Stream, closeAfterWrite: BooleanType) -> VoidType: ...
    
    @overload
    def AddResource(self, name: StringType, value: ArrayType[ByteType]) -> VoidType: ...
    
    def AddResourceData(self, name: StringType, typeName: StringType, serializedData: ArrayType[ByteType]) -> VoidType: ...
    
    def Close(self) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    def Generate(self) -> VoidType: ...
    
    def get_TypeNameConverter(self) -> Func[TypeType, StringType]: ...
    
    def set_TypeNameConverter(self, value: Func[TypeType, StringType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class ResourceWriter(ObjectType, IResourceWriter, IDisposable):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    @overload
    def __init__(self, fileName: StringType): ...
    
    @overload
    def __init__(self, stream: Stream): ...
    
    # ---------- Properties ---------- #
    
    @property
    def TypeNameConverter(self) -> Func[TypeType, StringType]: ...
    
    @TypeNameConverter.setter
    def TypeNameConverter(self, value: Func[TypeType, StringType]) -> None: ...
    
    # ---------- Methods ---------- #
    
    @overload
    def AddResource(self, name: StringType, value: StringType) -> VoidType: ...
    
    @overload
    def AddResource(self, name: StringType, value: ObjectType) -> VoidType: ...
    
    @overload
    def AddResource(self, name: StringType, value: Stream) -> VoidType: ...
    
    @overload
    def AddResource(self, name: StringType, value: Stream, closeAfterWrite: BooleanType) -> VoidType: ...
    
    @overload
    def AddResource(self, name: StringType, value: ArrayType[ByteType]) -> VoidType: ...
    
    def AddResourceData(self, name: StringType, typeName: StringType, serializedData: ArrayType[ByteType]) -> VoidType: ...
    
    def Close(self) -> VoidType: ...
    
    def Dispose(self) -> VoidType: ...
    
    def Generate(self) -> VoidType: ...
    
    def get_TypeNameConverter(self) -> Func[TypeType, StringType]: ...
    
    def set_TypeNameConverter(self, value: Func[TypeType, StringType]) -> VoidType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RuntimeResourceSet(ResourceSet, IDisposable, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetEnumerator(self) -> IDictionaryEnumerator: ...
    
    @overload
    def GetObject(self, key: StringType) -> ObjectType: ...
    
    @overload
    def GetObject(self, key: StringType, ignoreCase: BooleanType) -> ObjectType: ...
    
    @overload
    def GetString(self, key: StringType) -> StringType: ...
    
    @overload
    def GetString(self, key: StringType, ignoreCase: BooleanType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RuntimeResourceSet(ResourceSet, IDisposable, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetEnumerator(self) -> IDictionaryEnumerator: ...
    
    @overload
    def GetObject(self, key: StringType) -> ObjectType: ...
    
    @overload
    def GetObject(self, key: StringType, ignoreCase: BooleanType) -> ObjectType: ...
    
    @overload
    def GetString(self, key: StringType) -> StringType: ...
    
    @overload
    def GetString(self, key: StringType, ignoreCase: BooleanType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class RuntimeResourceSet(ResourceSet, IDisposable, IEnumerable):
    # No Fields
    
    # No Constructors
    
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GetEnumerator(self) -> IDictionaryEnumerator: ...
    
    @overload
    def GetObject(self, key: StringType) -> ObjectType: ...
    
    @overload
    def GetObject(self, key: StringType, ignoreCase: BooleanType) -> ObjectType: ...
    
    @overload
    def GetString(self, key: StringType) -> StringType: ...
    
    @overload
    def GetString(self, key: StringType, ignoreCase: BooleanType) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SatelliteContractVersionAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, version: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Version(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Version(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SatelliteContractVersionAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, version: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Version(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Version(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class SatelliteContractVersionAttribute(Attribute, _Attribute):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self, version: StringType): ...
    
    # ---------- Properties ---------- #
    
    @property
    def Version(self) -> StringType: ...
    
    # ---------- Methods ---------- #
    
    def get_Version(self) -> StringType: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WindowsRuntimeResourceManagerBase(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def GlobalResourceContextBestFitCultureInfo(self) -> CultureInfo: ...
    
    # ---------- Methods ---------- #
    
    def GetString(self, stringName: StringType, startingCulture: StringType, neutralResourcesCulture: StringType) -> StringType: ...
    
    def Initialize(self, libpath: StringType, reswFilename: StringType, exceptionInfo: PRIExceptionInfo) -> Tuple[BooleanType, PRIExceptionInfo]: ...
    
    def SetGlobalResourceContextDefaultCulture(self, ci: CultureInfo) -> BooleanType: ...
    
    def get_GlobalResourceContextBestFitCultureInfo(self) -> CultureInfo: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WindowsRuntimeResourceManagerBase(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def GlobalResourceContextBestFitCultureInfo(self) -> CultureInfo: ...
    
    # ---------- Methods ---------- #
    
    def GetString(self, stringName: StringType, startingCulture: StringType, neutralResourcesCulture: StringType) -> StringType: ...
    
    def Initialize(self, libpath: StringType, reswFilename: StringType, exceptionInfo: PRIExceptionInfo) -> Tuple[BooleanType, PRIExceptionInfo]: ...
    
    def SetGlobalResourceContextDefaultCulture(self, ci: CultureInfo) -> BooleanType: ...
    
    def get_GlobalResourceContextBestFitCultureInfo(self) -> CultureInfo: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class WindowsRuntimeResourceManagerBase(ObjectType):
    # No Fields
    
    # ---------- Constructors ---------- #
    
    def __init__(self): ...
    
    # ---------- Properties ---------- #
    
    @property
    def GlobalResourceContextBestFitCultureInfo(self) -> CultureInfo: ...
    
    # ---------- Methods ---------- #
    
    def GetString(self, stringName: StringType, startingCulture: StringType, neutralResourcesCulture: StringType) -> StringType: ...
    
    def Initialize(self, libpath: StringType, reswFilename: StringType, exceptionInfo: PRIExceptionInfo) -> Tuple[BooleanType, PRIExceptionInfo]: ...
    
    def SetGlobalResourceContextDefaultCulture(self, ci: CultureInfo) -> BooleanType: ...
    
    def get_GlobalResourceContextBestFitCultureInfo(self) -> CultureInfo: ...
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class __HResults(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def ERROR_MRM_MAP_NOT_FOUND() -> IntType: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class __HResults(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def ERROR_MRM_MAP_NOT_FOUND() -> IntType: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


class __HResults(ABC, ObjectType):
    # ---------- Fields ---------- #
    
    @staticmethod
    @property
    def ERROR_MRM_MAP_NOT_FOUND() -> IntType: ...
    
    # No Constructors
    
    # No Properties
    
    # No Methods
    
    # No Events
    
    # No Sub Classes
    
    # No Sub Structs
    
    # No Sub Interfaces
    
    # No Sub Enums


# ---------- Structs ---------- #

class ResourceLocator(ValueType):
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


class ResourceLocator(ValueType):
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


class ResourceLocator(ValueType):
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


# ---------- Interfaces ---------- #

class IResourceGroveler(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GrovelForResourceSet(self, culture: CultureInfo, localResourceSets: Dictionary[StringType, ResourceSet], tryParents: BooleanType, createIfNotExists: BooleanType, stackMark: StackCrawlMark) -> Tuple[ResourceSet, StackCrawlMark]: ...
    
    def HasNeutralResources(self, culture: CultureInfo, defaultResName: StringType) -> BooleanType: ...
    
    # No Events


class IResourceGroveler(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GrovelForResourceSet(self, culture: CultureInfo, localResourceSets: Dictionary[StringType, ResourceSet], tryParents: BooleanType, createIfNotExists: BooleanType, stackMark: StackCrawlMark) -> Tuple[ResourceSet, StackCrawlMark]: ...
    
    def HasNeutralResources(self, culture: CultureInfo, defaultResName: StringType) -> BooleanType: ...
    
    # No Events


class IResourceGroveler(Protocol):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def GrovelForResourceSet(self, culture: CultureInfo, localResourceSets: Dictionary[StringType, ResourceSet], tryParents: BooleanType, createIfNotExists: BooleanType, stackMark: StackCrawlMark) -> Tuple[ResourceSet, StackCrawlMark]: ...
    
    def HasNeutralResources(self, culture: CultureInfo, defaultResName: StringType) -> BooleanType: ...
    
    # No Events


class IResourceReader(Protocol, IEnumerable, IDisposable):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def GetEnumerator(self) -> IDictionaryEnumerator: ...
    
    # No Events


class IResourceReader(Protocol, IEnumerable, IDisposable):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def GetEnumerator(self) -> IDictionaryEnumerator: ...
    
    # No Events


class IResourceReader(Protocol, IEnumerable, IDisposable):
    # No Properties
    
    # ---------- Methods ---------- #
    
    def Close(self) -> VoidType: ...
    
    def GetEnumerator(self) -> IDictionaryEnumerator: ...
    
    # No Events


class IResourceWriter(Protocol, IDisposable):
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def AddResource(self, name: StringType, value: StringType) -> VoidType: ...
    
    @overload
    def AddResource(self, name: StringType, value: ObjectType) -> VoidType: ...
    
    @overload
    def AddResource(self, name: StringType, value: ArrayType[ByteType]) -> VoidType: ...
    
    def Close(self) -> VoidType: ...
    
    def Generate(self) -> VoidType: ...
    
    # No Events


class IResourceWriter(Protocol, IDisposable):
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def AddResource(self, name: StringType, value: StringType) -> VoidType: ...
    
    @overload
    def AddResource(self, name: StringType, value: ObjectType) -> VoidType: ...
    
    @overload
    def AddResource(self, name: StringType, value: ArrayType[ByteType]) -> VoidType: ...
    
    def Close(self) -> VoidType: ...
    
    def Generate(self) -> VoidType: ...
    
    # No Events


class IResourceWriter(Protocol, IDisposable):
    # No Properties
    
    # ---------- Methods ---------- #
    
    @overload
    def AddResource(self, name: StringType, value: StringType) -> VoidType: ...
    
    @overload
    def AddResource(self, name: StringType, value: ObjectType) -> VoidType: ...
    
    @overload
    def AddResource(self, name: StringType, value: ArrayType[ByteType]) -> VoidType: ...
    
    def Close(self) -> VoidType: ...
    
    def Generate(self) -> VoidType: ...
    
    # No Events


# ---------- Enums ---------- #

class ResourceTypeCode(Enum):
    Null: IntType = 0
    String: IntType = 1
    Boolean: IntType = 2
    Char: IntType = 3
    Byte: IntType = 4
    SByte: IntType = 5
    Int16: IntType = 6
    UInt16: IntType = 7
    Int32: IntType = 8
    UInt32: IntType = 9
    Int64: IntType = 10
    UInt64: IntType = 11
    Single: IntType = 12
    Double: IntType = 13
    Decimal: IntType = 14
    DateTime: IntType = 15
    TimeSpan: IntType = 16
    LastPrimitive: IntType = 16
    ByteArray: IntType = 32
    Stream: IntType = 33
    StartOfUserTypes: IntType = 64


class ResourceTypeCode(Enum):
    Null: IntType = 0
    String: IntType = 1
    Boolean: IntType = 2
    Char: IntType = 3
    Byte: IntType = 4
    SByte: IntType = 5
    Int16: IntType = 6
    UInt16: IntType = 7
    Int32: IntType = 8
    UInt32: IntType = 9
    Int64: IntType = 10
    UInt64: IntType = 11
    Single: IntType = 12
    Double: IntType = 13
    Decimal: IntType = 14
    DateTime: IntType = 15
    TimeSpan: IntType = 16
    LastPrimitive: IntType = 16
    ByteArray: IntType = 32
    Stream: IntType = 33
    StartOfUserTypes: IntType = 64


class ResourceTypeCode(Enum):
    Null: IntType = 0
    String: IntType = 1
    Boolean: IntType = 2
    Char: IntType = 3
    Byte: IntType = 4
    SByte: IntType = 5
    Int16: IntType = 6
    UInt16: IntType = 7
    Int32: IntType = 8
    UInt32: IntType = 9
    Int64: IntType = 10
    UInt64: IntType = 11
    Single: IntType = 12
    Double: IntType = 13
    Decimal: IntType = 14
    DateTime: IntType = 15
    TimeSpan: IntType = 16
    LastPrimitive: IntType = 16
    ByteArray: IntType = 32
    Stream: IntType = 33
    StartOfUserTypes: IntType = 64


class UltimateResourceFallbackLocation(Enum):
    MainAssembly: IntType = 0
    Satellite: IntType = 1


class UltimateResourceFallbackLocation(Enum):
    MainAssembly: IntType = 0
    Satellite: IntType = 1


class UltimateResourceFallbackLocation(Enum):
    MainAssembly: IntType = 0
    Satellite: IntType = 1


# No Delegates

__all__ = [
    FastResourceComparer,
    FileBasedResourceGroveler,
    ManifestBasedResourceGroveler,
    MissingManifestResourceException,
    MissingSatelliteAssemblyException,
    NeutralResourcesLanguageAttribute,
    PRIExceptionInfo,
    ResourceFallbackManager,
    ResourceManager,
    ResourceReader,
    ResourceSet,
    ResourceWriter,
    RuntimeResourceSet,
    SatelliteContractVersionAttribute,
    WindowsRuntimeResourceManagerBase,
    __HResults,
    ResourceLocator,
    IResourceGroveler,
    IResourceReader,
    IResourceWriter,
    ResourceTypeCode,
    UltimateResourceFallbackLocation,
]
