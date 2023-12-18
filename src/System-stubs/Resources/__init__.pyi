from __future__ import annotations

from abc import ABC
from typing import List
from typing import Protocol
from typing import Tuple
from typing import Union
from typing import overload

from System import Array
from System import Attribute
from System import Boolean
from System import Byte
from System import Enum
from System import Exception
from System import Func
from System import IDisposable
from System import Int32
from System import Object
from System import String
from System import SystemException
from System import Type
from System import ValueType
from System import Void
from System.Collections import IComparer
from System.Collections import IDictionaryEnumerator
from System.Collections import IEnumerable
from System.Collections import IEqualityComparer
from System.Collections.Generic import Dictionary
from System.Collections.Generic import IComparer
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IEnumerator
from System.Collections.Generic import IEqualityComparer
from System.Globalization import CultureInfo
from System.IO import Stream
from System.IO import UnmanagedMemoryStream
from System.Reflection import Assembly
from System.Runtime.InteropServices import _Attribute
from System.Runtime.InteropServices import _Exception
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

class FastResourceComparer(
    ObjectType, IComparer, IEqualityComparer, IComparer[StringType], IEqualityComparer[StringType]
):
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
    def CompareOrdinal(
        a: StringType, bytes: ArrayType[ByteType], bCharLength: IntType
    ) -> IntType: ...
    @staticmethod
    @overload
    def CompareOrdinal(
        bytes: ArrayType[ByteType], aCharLength: IntType, b: StringType
    ) -> IntType: ...
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

    def GrovelForResourceSet(
        self,
        culture: CultureInfo,
        localResourceSets: Dictionary[StringType, ResourceSet],
        tryParents: BooleanType,
        createIfNotExists: BooleanType,
        stackMark: StackCrawlMark,
    ) -> Tuple[ResourceSet, StackCrawlMark]: ...
    def HasNeutralResources(
        self, culture: CultureInfo, defaultResName: StringType
    ) -> BooleanType: ...

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

    def GrovelForResourceSet(
        self,
        culture: CultureInfo,
        localResourceSets: Dictionary[StringType, ResourceSet],
        tryParents: BooleanType,
        createIfNotExists: BooleanType,
        stackMark: StackCrawlMark,
    ) -> Tuple[ResourceSet, StackCrawlMark]: ...
    def HasNeutralResources(
        self, culture: CultureInfo, defaultResName: StringType
    ) -> BooleanType: ...

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
    def CreateFileBasedResourceManager(
        baseName: StringType, resourceDir: StringType, usingResourceSet: TypeType
    ) -> ResourceManager: ...
    @overload
    def GetObject(self, name: StringType) -> ObjectType: ...
    @overload
    def GetObject(self, name: StringType, culture: CultureInfo) -> ObjectType: ...
    def GetResourceSet(
        self, culture: CultureInfo, createIfNotExists: BooleanType, tryParents: BooleanType
    ) -> ResourceSet: ...
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
    def GetResourceData(
        self, resourceName: StringType, resourceType: StringType, resourceData: ByteType
    ) -> Tuple[VoidType, StringType, ByteType]: ...

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
    def AddResource(
        self, name: StringType, value: Stream, closeAfterWrite: BooleanType
    ) -> VoidType: ...
    @overload
    def AddResource(self, name: StringType, value: ArrayType[ByteType]) -> VoidType: ...
    def AddResourceData(
        self, name: StringType, typeName: StringType, serializedData: ArrayType[ByteType]
    ) -> VoidType: ...
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

    def GetString(
        self,
        stringName: StringType,
        startingCulture: StringType,
        neutralResourcesCulture: StringType,
    ) -> StringType: ...
    def Initialize(
        self, libpath: StringType, reswFilename: StringType, exceptionInfo: PRIExceptionInfo
    ) -> Tuple[BooleanType, PRIExceptionInfo]: ...
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

# ---------- Interfaces ---------- #

class IResourceGroveler(Protocol):
    # No Properties

    # ---------- Methods ---------- #

    def GrovelForResourceSet(
        self,
        culture: CultureInfo,
        localResourceSets: Dictionary[StringType, ResourceSet],
        tryParents: BooleanType,
        createIfNotExists: BooleanType,
        stackMark: StackCrawlMark,
    ) -> Tuple[ResourceSet, StackCrawlMark]: ...
    def HasNeutralResources(
        self, culture: CultureInfo, defaultResName: StringType
    ) -> BooleanType: ...

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

# ---------- Enums ---------- #

class ResourceTypeCode(Enum):
    Null = 0
    String = 1
    Boolean = 2
    Char = 3
    Byte = 4
    SByte = 5
    Int16 = 6
    UInt16 = 7
    Int32 = 8
    UInt32 = 9
    Int64 = 10
    UInt64 = 11
    Single = 12
    Double = 13
    Decimal = 14
    DateTime = 15
    TimeSpan = 16
    LastPrimitive = 16
    ByteArray = 32
    Stream = 33
    StartOfUserTypes = 64

class UltimateResourceFallbackLocation(Enum):
    MainAssembly = 0
    Satellite = 1

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
