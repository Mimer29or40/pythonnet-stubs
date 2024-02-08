from __future__ import annotations

from abc import ABC
from typing import ClassVar
from typing import Final
from typing import Iterator
from typing import Tuple
from typing import overload

from System import Array
from System import Attribute
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
from System import ValueType
from System.Collections import IComparer
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections import IEqualityComparer
from System.Collections.Generic import Dictionary
from System.Collections.Generic import IComparer
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IEqualityComparer
from System.Globalization import CultureInfo
from System.IO import Stream
from System.IO import UnmanagedMemoryStream
from System.Reflection import Assembly
from System.Reflection import MethodBase
from System.Resources.ResourceManager import ResourceManagerMediator
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

    def __init__(self):
        """"""
    @overload
    def Compare(self, x: object, y: object) -> int:
        """

        :param x:
        :param y:
        :return:
        """
    @overload
    def Compare(self, x: str, y: str) -> int:
        """

        :param x:
        :param y:
        :return:
        """
    @classmethod
    @overload
    def CompareOrdinal(cls, bytes: Array[int], aCharLength: int, b: str) -> int:
        """

        :param bytes:
        :param aCharLength:
        :param b:
        :return:
        """
    @classmethod
    @overload
    def CompareOrdinal(cls, a: str, bytes: Array[int], bCharLength: int) -> int:
        """

        :param a:
        :param bytes:
        :param bCharLength:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, x: object, y: object) -> bool:
        """

        :param x:
        :param y:
        :return:
        """
    @overload
    def Equals(self, x: str, y: str) -> bool:
        """

        :param x:
        :param y:
        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self, obj: object) -> int:
        """

        :param obj:
        :return:
        """
    @overload
    def GetHashCode(self, obj: str) -> int:
        """

        :param obj:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class FileBasedResourceGroveler(Object, IResourceGroveler):
    """"""

    def __init__(self, mediator: ResourceManager.ResourceManagerMediator):
        """

        :param mediator:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GrovelForResourceSet(
        self,
        culture: CultureInfo,
        localResourceSets: Dictionary[str, ResourceSet],
        tryParents: bool,
        createIfNotExists: bool,
        stackMark: StackCrawlMark,
    ) -> ResourceSet:
        """

        :param culture:
        :param localResourceSets:
        :param tryParents:
        :param createIfNotExists:
        :param stackMark:
        :return:
        """
    def HasNeutralResources(self, culture: CultureInfo, defaultResName: str) -> bool:
        """

        :param culture:
        :param defaultResName:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class IResourceGroveler:
    """"""

    def GrovelForResourceSet(
        self,
        culture: CultureInfo,
        localResourceSets: Dictionary[str, ResourceSet],
        tryParents: bool,
        createIfNotExists: bool,
        stackMark: StackCrawlMark,
    ) -> ResourceSet:
        """

        :param culture:
        :param localResourceSets:
        :param tryParents:
        :param createIfNotExists:
        :param stackMark:
        :return:
        """
    def HasNeutralResources(self, culture: CultureInfo, defaultResName: str) -> bool:
        """

        :param culture:
        :param defaultResName:
        :return:
        """

class IResourceReader(IEnumerable, IDisposable):
    """"""

    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """

class IResourceWriter(IDisposable):
    """"""

    @overload
    def AddResource(self, name: str, value: Array[int]) -> None:
        """

        :param name:
        :param value:
        """
    @overload
    def AddResource(self, name: str, value: object) -> None:
        """

        :param name:
        :param value:
        """
    @overload
    def AddResource(self, name: str, value: str) -> None:
        """

        :param name:
        :param value:
        """
    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Generate(self) -> None:
        """"""

class ManifestBasedResourceGroveler(Object, IResourceGroveler):
    """"""

    def __init__(self, mediator: ResourceManager.ResourceManagerMediator):
        """

        :param mediator:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GrovelForResourceSet(
        self,
        culture: CultureInfo,
        localResourceSets: Dictionary[str, ResourceSet],
        tryParents: bool,
        createIfNotExists: bool,
        stackMark: StackCrawlMark,
    ) -> ResourceSet:
        """

        :param culture:
        :param localResourceSets:
        :param tryParents:
        :param createIfNotExists:
        :param stackMark:
        :return:
        """
    def HasNeutralResources(self, culture: CultureInfo, defaultResName: str) -> bool:
        """

        :param culture:
        :param defaultResName:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class MissingManifestResourceException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """

        :param message:
        """
    @overload
    def __init__(self, message: str, inner: Exception):
        """

        :param message:
        :param inner:
        """
    @property
    def Data(self) -> IDictionary:
        """

        :return:
        """
    @property
    def HResult(self) -> int:
        """

        :return:
        """
    @property
    def HelpLink(self) -> str:
        """

        :return:
        """
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """

        :return:
        """
    @property
    def Message(self) -> str:
        """

        :return:
        """
    @property
    def Source(self) -> str:
        """

        :return:
        """
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """

        :return:
        """
    @property
    def TargetSite(self) -> MethodBase:
        """

        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class MissingSatelliteAssemblyException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, message: str):
        """

        :param message:
        """
    @overload
    def __init__(self, message: str, inner: Exception):
        """

        :param message:
        :param inner:
        """
    @overload
    def __init__(self, message: str, cultureName: str):
        """

        :param message:
        :param cultureName:
        """
    @property
    def CultureName(self) -> str:
        """

        :return:
        """
    @property
    def Data(self) -> IDictionary:
        """

        :return:
        """
    @property
    def HResult(self) -> int:
        """

        :return:
        """
    @property
    def HelpLink(self) -> str:
        """

        :return:
        """
    @HelpLink.setter
    def HelpLink(self, value: str) -> None: ...
    @property
    def InnerException(self) -> Exception:
        """

        :return:
        """
    @property
    def Message(self) -> str:
        """

        :return:
        """
    @property
    def Source(self) -> str:
        """

        :return:
        """
    @Source.setter
    def Source(self, value: str) -> None: ...
    @property
    def StackTrace(self) -> str:
        """

        :return:
        """
    @property
    def TargetSite(self) -> MethodBase:
        """

        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetBaseException(self) -> Exception:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class NeutralResourcesLanguageAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self, cultureName: str):
        """

        :param cultureName:
        """
    @overload
    def __init__(self, cultureName: str, location: UltimateResourceFallbackLocation):
        """

        :param cultureName:
        :param location:
        """
    @property
    def CultureName(self) -> str:
        """

        :return:
        """
    @property
    def Location(self) -> UltimateResourceFallbackLocation:
        """

        :return:
        """
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class PRIExceptionInfo(Object):
    """"""

    _PackageSimpleName: Final[str] = ...
    """
    
    :return: 
    """
    _ResWFile: Final[str] = ...
    """
    
    :return: 
    """
    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ResourceFallbackManager(Object, IEnumerable[CultureInfo], IEnumerable):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """
    @overload
    def __iter__(self) -> Iterator[CultureInfo]:
        """

        :return:
        """

class ResourceLocator(ValueType):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ResourceManager(Object):
    """"""

    HeaderVersionNumber: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    MagicNumber: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    @overload
    def __init__(self, resourceSource: Type):
        """

        :param resourceSource:
        """
    @overload
    def __init__(self, baseName: str, assembly: Assembly):
        """

        :param baseName:
        :param assembly:
        """
    @overload
    def __init__(self, baseName: str, assembly: Assembly, usingResourceSet: Type):
        """

        :param baseName:
        :param assembly:
        :param usingResourceSet:
        """
    @property
    def BaseName(self) -> str:
        """

        :return:
        """
    @property
    def IgnoreCase(self) -> bool:
        """

        :return:
        """
    @IgnoreCase.setter
    def IgnoreCase(self, value: bool) -> None: ...
    @property
    def ResourceSetType(self) -> Type:
        """

        :return:
        """
    @classmethod
    def CreateFileBasedResourceManager(
        cls, baseName: str, resourceDir: str, usingResourceSet: Type
    ) -> ResourceManager:
        """

        :param baseName:
        :param resourceDir:
        :param usingResourceSet:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetObject(self, name: str) -> object:
        """

        :param name:
        :return:
        """
    @overload
    def GetObject(self, name: str, culture: CultureInfo) -> object:
        """

        :param name:
        :param culture:
        :return:
        """
    def GetResourceSet(
        self, culture: CultureInfo, createIfNotExists: bool, tryParents: bool
    ) -> ResourceSet:
        """

        :param culture:
        :param createIfNotExists:
        :param tryParents:
        :return:
        """
    @overload
    def GetStream(self, name: str) -> UnmanagedMemoryStream:
        """

        :param name:
        :return:
        """
    @overload
    def GetStream(self, name: str, culture: CultureInfo) -> UnmanagedMemoryStream:
        """

        :param name:
        :param culture:
        :return:
        """
    @overload
    def GetString(self, name: str) -> str:
        """

        :param name:
        :return:
        """
    @overload
    def GetString(self, name: str, culture: CultureInfo) -> str:
        """

        :param name:
        :param culture:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ReleaseAllResources(self) -> None:
        """"""
    def ToString(self) -> str:
        """

        :return:
        """

class ResourceReader(Object, IEnumerable, IResourceReader, IDisposable):
    """"""

    @overload
    def __init__(self, stream: Stream):
        """

        :param stream:
        """
    @overload
    def __init__(self, fileName: str):
        """

        :param fileName:
        """
    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetResourceData(
        self, resourceName: str, resourceType: str, resourceData: int
    ) -> Tuple[None, str, int]:
        """

        :param resourceName:
        :param resourceType:
        :param resourceData:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """

class ResourceSet(Object, IEnumerable, IDisposable):
    """"""

    @overload
    def __init__(self, stream: Stream):
        """

        :param stream:
        """
    @overload
    def __init__(self, reader: IResourceReader):
        """

        :param reader:
        """
    @overload
    def __init__(self, fileName: str):
        """

        :param fileName:
        """
    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetDefaultReader(self) -> Type:
        """

        :return:
        """
    def GetDefaultWriter(self) -> Type:
        """

        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetObject(self, name: str) -> object:
        """

        :param name:
        :return:
        """
    @overload
    def GetObject(self, name: str, ignoreCase: bool) -> object:
        """

        :param name:
        :param ignoreCase:
        :return:
        """
    @overload
    def GetString(self, name: str) -> str:
        """

        :param name:
        :return:
        """
    @overload
    def GetString(self, name: str, ignoreCase: bool) -> str:
        """

        :param name:
        :param ignoreCase:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """

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
    def __init__(self, stream: Stream):
        """

        :param stream:
        """
    @overload
    def __init__(self, fileName: str):
        """

        :param fileName:
        """
    @property
    def TypeNameConverter(self) -> Func[Type, str]:
        """

        :return:
        """
    @TypeNameConverter.setter
    def TypeNameConverter(self, value: Func[Type, str]) -> None: ...
    @overload
    def AddResource(self, name: str, value: Stream) -> None:
        """

        :param name:
        :param value:
        """
    @overload
    def AddResource(self, name: str, value: Array[int]) -> None:
        """

        :param name:
        :param value:
        """
    @overload
    def AddResource(self, name: str, value: object) -> None:
        """

        :param name:
        :param value:
        """
    @overload
    def AddResource(self, name: str, value: str) -> None:
        """

        :param name:
        :param value:
        """
    @overload
    def AddResource(self, name: str, value: Stream, closeAfterWrite: bool) -> None:
        """

        :param name:
        :param value:
        :param closeAfterWrite:
        """
    def AddResourceData(self, name: str, typeName: str, serializedData: Array[int]) -> None:
        """

        :param name:
        :param typeName:
        :param serializedData:
        """
    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def Generate(self) -> None:
        """"""
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class RuntimeResourceSet(ResourceSet, IEnumerable, IDisposable):
    """"""

    def Close(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetDefaultReader(self) -> Type:
        """

        :return:
        """
    def GetDefaultWriter(self) -> Type:
        """

        :return:
        """
    def GetEnumerator(self) -> IEnumerator:
        """

        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
    def GetObject(self, name: str) -> object:
        """

        :param name:
        :return:
        """
    @overload
    def GetObject(self, name: str, ignoreCase: bool) -> object:
        """

        :param name:
        :param ignoreCase:
        :return:
        """
    @overload
    def GetString(self, name: str) -> str:
        """

        :param name:
        :return:
        """
    @overload
    def GetString(self, name: str, ignoreCase: bool) -> str:
        """

        :param name:
        :param ignoreCase:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __iter__(self) -> Iterator[object]:
        """

        :return:
        """

class SatelliteContractVersionAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, version: str):
        """

        :param version:
        """
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Version(self) -> str:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """

        :param riid:
        :param rgszNames:
        :param cNames:
        :param lcid:
        :param rgDispId:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
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
        """

        :param dispIdMember:
        :param riid:
        :param lcid:
        :param wFlags:
        :param pDispParams:
        :param pVarResult:
        :param pExcepInfo:
        :param puArgErr:
        """
    def IsDefaultAttribute(self) -> bool:
        """

        :return:
        """
    def Match(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class UltimateResourceFallbackLocation(Enum):
    """"""

    MainAssembly: UltimateResourceFallbackLocation = ...
    """"""
    Satellite: UltimateResourceFallbackLocation = ...
    """"""

class WindowsRuntimeResourceManagerBase(Object):
    """"""

    def __init__(self):
        """"""
    @property
    def GlobalResourceContextBestFitCultureInfo(self) -> CultureInfo:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetString(self, stringName: str, startingCulture: str, neutralResourcesCulture: str) -> str:
        """

        :param stringName:
        :param startingCulture:
        :param neutralResourcesCulture:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def Initialize(
        self, libpath: str, reswFilename: str, exceptionInfo: PRIExceptionInfo
    ) -> Tuple[bool, PRIExceptionInfo]:
        """

        :param libpath:
        :param reswFilename:
        :param exceptionInfo:
        :return:
        """
    def SetGlobalResourceContextDefaultCulture(self, ci: CultureInfo) -> bool:
        """

        :param ci:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class __HResults(ABC, Object):
    """"""

    ERROR_MRM_MAP_NOT_FOUND: Final[ClassVar[int]] = ...
    """
    
    :return: 
    """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
