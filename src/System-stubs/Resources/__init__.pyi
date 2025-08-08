"""Automatically generated stubs for C# namespace: System.Resources."""

from abc import ABC
from collections.abc import Iterator
from typing import ClassVar
from typing import Final
from typing import overload

from System import Array
from System import Attribute
from System import Byte
from System import Enum
from System import Exception
from System import Func
from System import Guid
from System import IDisposable
from System import IntPtr
from System import Object
from System import String
from System import SystemException
from System import Type
from System import UInt32
from System import ValueType
from System.Collections import IComparer
from System.Collections import IDictionary
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
from System.Reflection import MethodBase
from System.Runtime.InteropServices import _Attribute
from System.Runtime.InteropServices import _Exception
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Threading import StackCrawlMark

class FastResourceComparer(
    Object, IComparer[String], IEqualityComparer[String], IComparer, IEqualityComparer
):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def Compare(self, a: object, b: object) -> int:
        """"""
    @overload
    def Compare(self, a: str, b: str) -> int:
        """"""
    @classmethod
    @overload
    def CompareOrdinal(cls, bytes: Array[int], aCharLength: int, b: str) -> int:
        """"""
    @classmethod
    @overload
    def CompareOrdinal(cls, a: str, bytes: Array[int], bCharLength: int) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, a: object, b: object) -> bool:
        """"""
    @overload
    def Equals(self, a: str, b: str) -> bool:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, key: object) -> int:
        """"""
    @overload
    def GetHashCode(self, key: str) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class FileBasedResourceGroveler(Object, IResourceGroveler):
    """"""
    def __init__(self, mediator: ResourceManager.ResourceManagerMediator) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GrovelForResourceSet(
        self,
        culture: CultureInfo,
        localResourceSets: Dictionary[str, ResourceSet],
        tryParents: bool,
        createIfNotExists: bool,
        stackMark: StackCrawlMark,
    ) -> ResourceSet:
        """"""
    def HasNeutralResources(self, culture: CultureInfo, defaultResName: str) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class IResourceGroveler(ABC):
    """"""
    def GrovelForResourceSet(
        self,
        culture: CultureInfo,
        localResourceSets: Dictionary[str, ResourceSet],
        tryParents: bool,
        createIfNotExists: bool,
        stackMark: StackCrawlMark,
    ) -> ResourceSet:
        """"""
    def HasNeutralResources(self, culture: CultureInfo, defaultResName: str) -> bool:
        """"""

class IResourceReader(ABC, IEnumerable, IDisposable):
    """"""
    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def GetEnumerator(self) -> IDictionaryEnumerator:
        """"""
    def __iter__(self) -> Iterator:
        """"""

class IResourceWriter(ABC, IDisposable):
    """"""
    @overload
    def AddResource(self, name: str, value: Array[int]) -> None:
        """"""
    @overload
    def AddResource(self, name: str, value: object) -> None:
        """"""
    @overload
    def AddResource(self, name: str, value: str) -> None:
        """"""
    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Generate(self) -> None:
        """"""

class ManifestBasedResourceGroveler(Object, IResourceGroveler):
    """"""
    def __init__(self, mediator: ResourceManager.ResourceManagerMediator) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GrovelForResourceSet(
        self,
        culture: CultureInfo,
        localResourceSets: Dictionary[str, ResourceSet],
        tryParents: bool,
        createIfNotExists: bool,
        stackMark: StackCrawlMark,
    ) -> ResourceSet:
        """"""
    def HasNeutralResources(self, culture: CultureInfo, defaultResName: str) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class MissingManifestResourceException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, inner: Exception) -> None:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def HResult(self) -> int:
        """"""
    @property
    def HelpLink(self) -> str:
        """"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """"""
    @property
    def Message(self) -> str:
        """"""
    @property
    def Source(self) -> str:
        """"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """"""
    @property
    def TargetSite(self) -> MethodBase:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseException(self) -> Exception:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MissingSatelliteAssemblyException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, cultureName: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, inner: Exception) -> None:
        """"""
    @property
    def CultureName(self) -> str:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def HResult(self) -> int:
        """"""
    @property
    def HelpLink(self) -> str:
        """"""
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """"""
    @property
    def Message(self) -> str:
        """"""
    @property
    def Source(self) -> str:
        """"""
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """"""
    @property
    def TargetSite(self) -> MethodBase:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseException(self) -> Exception:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class NeutralResourcesLanguageAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, cultureName: str) -> None:
        """"""
    @overload
    def __init__(self, cultureName: str, location: UltimateResourceFallbackLocation) -> None:
        """"""
    @property
    def CultureName(self) -> str:
        """"""
    @property
    def Location(self) -> UltimateResourceFallbackLocation:
        """"""
    @property
    def TypeId(self) -> object:
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

class PRIExceptionInfo(Object):
    """"""

    _PackageSimpleName: Final[str]
    """"""
    _ResWFile: Final[str]
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

class ResourceFallbackManager(Object, IEnumerable[CultureInfo], IEnumerable):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[CultureInfo]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator[CultureInfo]:
        """"""

class ResourceLocator(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ResourceManager(Object):
    """"""

    HeaderVersionNumber: ClassVar[int]
    """"""
    MagicNumber: ClassVar[int]
    """"""
    @overload
    def __init__(self, baseName: str, assembly: Assembly) -> None:
        """"""
    @overload
    def __init__(self, baseName: str, assembly: Assembly, usingResourceSet: Type) -> None:
        """"""
    @overload
    def __init__(self, resourceSource: Type) -> None:
        """"""
    @property
    def BaseName(self) -> str:
        """"""
    @property
    def IgnoreCase(self) -> bool:
        """"""
    @IgnoreCase.setter
    def IgnoreCase(self, value: bool) -> None: ...
    @property
    def ResourceSetType(self) -> Type:
        """"""
    @classmethod
    def CreateFileBasedResourceManager(
        cls, baseName: str, resourceDir: str, usingResourceSet: Type
    ) -> ResourceManager:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetObject(self, name: str) -> object:
        """"""
    @overload
    def GetObject(self, name: str, culture: CultureInfo) -> object:
        """"""
    def GetResourceSet(
        self, culture: CultureInfo, createIfNotExists: bool, tryParents: bool
    ) -> ResourceSet:
        """"""
    @overload
    def GetStream(self, name: str) -> UnmanagedMemoryStream:
        """"""
    @overload
    def GetStream(self, name: str, culture: CultureInfo) -> UnmanagedMemoryStream:
        """"""
    @overload
    def GetString(self, name: str) -> str:
        """"""
    @overload
    def GetString(self, name: str, culture: CultureInfo) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def ReleaseAllResources(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class ResourceReader(Object, IEnumerable, IResourceReader, IDisposable):
    """"""
    @overload
    def __init__(self, fileName: str) -> None:
        """"""
    @overload
    def __init__(self, stream: Stream) -> None:
        """"""
    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IDictionaryEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetResourceData(
        self, resourceName: str, resourceType: String, resourceData: Byte
    ) -> tuple[None, String, Byte]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""

class ResourceSet(Object, IEnumerable, IDisposable):
    """"""
    @overload
    def __init__(self, fileName: str) -> None:
        """"""
    @overload
    def __init__(self, stream: Stream) -> None:
        """"""
    @overload
    def __init__(self, reader: IResourceReader) -> None:
        """"""
    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetDefaultReader(self) -> Type:
        """"""
    def GetDefaultWriter(self) -> Type:
        """"""
    def GetEnumerator(self) -> IDictionaryEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetObject(self, name: str) -> object:
        """"""
    @overload
    def GetObject(self, name: str, ignoreCase: bool) -> object:
        """"""
    @overload
    def GetString(self, name: str) -> str:
        """"""
    @overload
    def GetString(self, name: str, ignoreCase: bool) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""

class ResourceTypeCode(Enum):
    """"""

    Null: ResourceTypeCode = ...
    """"""
    String: ResourceTypeCode = ...
    """"""
    Boolean: ResourceTypeCode = ...
    """"""
    Char: ResourceTypeCode = ...
    """"""
    Byte: ResourceTypeCode = ...
    """"""
    SByte: ResourceTypeCode = ...
    """"""
    Int16: ResourceTypeCode = ...
    """"""
    UInt16: ResourceTypeCode = ...
    """"""
    Int32: ResourceTypeCode = ...
    """"""
    UInt32: ResourceTypeCode = ...
    """"""
    Int64: ResourceTypeCode = ...
    """"""
    UInt64: ResourceTypeCode = ...
    """"""
    Single: ResourceTypeCode = ...
    """"""
    Double: ResourceTypeCode = ...
    """"""
    Decimal: ResourceTypeCode = ...
    """"""
    DateTime: ResourceTypeCode = ...
    """"""
    TimeSpan: ResourceTypeCode = ...
    """"""
    LastPrimitive: ResourceTypeCode = ...
    """"""
    ByteArray: ResourceTypeCode = ...
    """"""
    Stream: ResourceTypeCode = ...
    """"""
    StartOfUserTypes: ResourceTypeCode = ...
    """"""

class ResourceWriter(Object, IResourceWriter, IDisposable):
    """"""
    @overload
    def __init__(self, fileName: str) -> None:
        """"""
    @overload
    def __init__(self, stream: Stream) -> None:
        """"""
    @property
    def TypeNameConverter(self) -> Func[Type, str]:
        """"""
    @TypeNameConverter.setter
    def TypeNameConverter(self, value: Func[Type, str]) -> None: ...
    @overload
    def AddResource(self, name: str, value: Stream) -> None:
        """"""
    @overload
    def AddResource(self, name: str, value: Stream, closeAfterWrite: bool) -> None:
        """"""
    @overload
    def AddResource(self, name: str, value: Array[int]) -> None:
        """"""
    @overload
    def AddResource(self, name: str, value: object) -> None:
        """"""
    @overload
    def AddResource(self, name: str, value: str) -> None:
        """"""
    def AddResourceData(self, name: str, typeName: str, serializedData: Array[int]) -> None:
        """"""
    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Generate(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RuntimeResourceSet(ResourceSet, IEnumerable, IDisposable):
    """"""
    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetDefaultReader(self) -> Type:
        """"""
    def GetDefaultWriter(self) -> Type:
        """"""
    def GetEnumerator(self) -> IDictionaryEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetObject(self, key: str) -> object:
        """"""
    @overload
    def GetObject(self, key: str, ignoreCase: bool) -> object:
        """"""
    @overload
    def GetString(self, key: str) -> str:
        """"""
    @overload
    def GetString(self, key: str, ignoreCase: bool) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __iter__(self) -> Iterator:
        """"""

class SatelliteContractVersionAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, version: str) -> None:
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

class UltimateResourceFallbackLocation(Enum):
    """"""

    MainAssembly: UltimateResourceFallbackLocation = ...
    """"""
    Satellite: UltimateResourceFallbackLocation = ...
    """"""

class WindowsRuntimeResourceManagerBase(Object):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def GlobalResourceContextBestFitCultureInfo(self) -> CultureInfo:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetString(self, stringName: str, startingCulture: str, neutralResourcesCulture: str) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def Initialize(
        self, libpath: str, reswFilename: str, exceptionInfo: PRIExceptionInfo
    ) -> tuple[bool, PRIExceptionInfo]:
        """"""
    def SetGlobalResourceContextDefaultCulture(self, ci: CultureInfo) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class __HResults(ABC, Object):
    """"""

    ERROR_MRM_MAP_NOT_FOUND: ClassVar[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
