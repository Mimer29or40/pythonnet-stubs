from __future__ import annotations

from abc import ABC
from typing import Callable
from typing import ClassVar
from typing import Final
from typing import Generic
from typing import Tuple
from typing import TypeVar
from typing import overload

from System import ApplicationException
from System import Array
from System import Attribute
from System import Delegate
from System import Enum
from System import Exception
from System import FormatException
from System import Guid
from System import ICloneable
from System import IntPtr
from System import IRuntimeFieldInfo
from System import IRuntimeMethodInfo
from System import MarshalByRefObject
from System import ModuleHandle
from System import Object
from System import ResolveEventArgs
from System import RuntimeFieldHandle
from System import RuntimeFieldHandleInternal
from System import RuntimeMethodHandle
from System import RuntimeMethodHandleInternal
from System import RuntimeType
from System import RuntimeTypeHandle
from System import SystemException
from System import Type
from System import TypedReference
from System import Utf8String
from System import ValueType
from System import Version
from System.Collections import IDictionary
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IList
from System.Collections.Immutable import ImmutableArray
from System.Configuration.Assemblies import AssemblyHashAlgorithm
from System.Configuration.Assemblies import AssemblyVersionCompatibility
from System.Globalization import CultureInfo
from System.IO import FileStream
from System.IO import Stream
from System.Runtime.InteropServices import CustomQueryInterfaceResult
from System.Runtime.InteropServices import ICustomQueryInterface
from System.Runtime.InteropServices import StructLayoutAttribute
from System.Runtime.InteropServices import _Assembly
from System.Runtime.InteropServices import _AssemblyName
from System.Runtime.InteropServices import _Attribute
from System.Runtime.InteropServices import _ConstructorInfo
from System.Runtime.InteropServices import _EventInfo
from System.Runtime.InteropServices import _Exception
from System.Runtime.InteropServices import _FieldInfo
from System.Runtime.InteropServices import _MemberInfo
from System.Runtime.InteropServices import _MethodBase
from System.Runtime.InteropServices import _MethodInfo
from System.Runtime.InteropServices import _Module
from System.Runtime.InteropServices import _ParameterInfo
from System.Runtime.InteropServices import _PropertyInfo
from System.Runtime.InteropServices import _Type
from System.Runtime.Remoting import ObjRef
from System.Runtime.Serialization import IDeserializationCallback
from System.Runtime.Serialization import IObjectReference
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Security import IEvidenceFactory
from System.Security import PermissionSet
from System.Security import SecurityContextSource
from System.Security import SecurityRuleSet
from System.Security.Cryptography.X509Certificates import X509Certificate
from System.Security.Policy import Evidence

K = TypeVar("K")
T = TypeVar("T")
V = TypeVar("V")

class EventType(Generic[T]):
    def __iadd__(self, other: T): ...
    def __isub__(self, other: T): ...

class AmbiguousMatchException(SystemException, _Exception, ISerializable):
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

class Assembly(ABC, Object, ICustomAttributeProvider, _Assembly, ISerializable, IEvidenceFactory):
    """"""

    @property
    def CodeBase(self) -> str:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DefinedTypes(self) -> IEnumerable[TypeInfo]:
        """

        :return:
        """
    @property
    def EntryPoint(self) -> MethodInfo:
        """

        :return:
        """
    @property
    def EscapedCodeBase(self) -> str:
        """

        :return:
        """
    @property
    def Evidence(self) -> Evidence:
        """

        :return:
        """
    @property
    def Evidence(self) -> Evidence:
        """

        :return:
        """
    @property
    def ExportedTypes(self) -> IEnumerable[Type]:
        """

        :return:
        """
    @property
    def FullName(self) -> str:
        """

        :return:
        """
    @property
    def GlobalAssemblyCache(self) -> bool:
        """

        :return:
        """
    @property
    def HostContext(self) -> int:
        """

        :return:
        """
    @property
    def ImageRuntimeVersion(self) -> str:
        """

        :return:
        """
    @property
    def IsDynamic(self) -> bool:
        """

        :return:
        """
    @property
    def IsFullyTrusted(self) -> bool:
        """

        :return:
        """
    @property
    def Location(self) -> str:
        """

        :return:
        """
    @property
    def ManifestModule(self) -> Module:
        """

        :return:
        """
    @property
    def Modules(self) -> IEnumerable[Module]:
        """

        :return:
        """
    @property
    def PermissionSet(self) -> PermissionSet:
        """

        :return:
        """
    @property
    def ReflectionOnly(self) -> bool:
        """

        :return:
        """
    @property
    def SecurityRuleSet(self) -> SecurityRuleSet:
        """

        :return:
        """
    @overload
    def CreateInstance(self, typeName: str) -> object:
        """

        :param typeName:
        :return:
        """
    @overload
    def CreateInstance(self, typeName: str, ignoreCase: bool) -> object:
        """

        :param typeName:
        :param ignoreCase:
        :return:
        """
    @overload
    def CreateInstance(
        self,
        typeName: str,
        ignoreCase: bool,
        bindingAttr: BindingFlags,
        binder: Binder,
        args: Array[object],
        culture: CultureInfo,
        activationAttributes: Array[object],
    ) -> object:
        """

        :param typeName:
        :param ignoreCase:
        :param bindingAttr:
        :param binder:
        :param args:
        :param culture:
        :param activationAttributes:
        :return:
        """
    @classmethod
    def CreateQualifiedName(cls, assemblyName: str, typeName: str) -> str:
        """

        :param assemblyName:
        :param typeName:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def GetAssembly(cls, type: Type) -> Assembly:
        """

        :param type:
        :return:
        """
    @classmethod
    def GetCallingAssembly(cls) -> Assembly:
        """

        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    @classmethod
    def GetEntryAssembly(cls) -> Assembly:
        """

        :return:
        """
    @classmethod
    def GetExecutingAssembly(cls) -> Assembly:
        """

        :return:
        """
    def GetExportedTypes(self) -> Array[Type]:
        """

        :return:
        """
    def GetFile(self, name: str) -> FileStream:
        """

        :param name:
        :return:
        """
    @overload
    def GetFiles(self) -> Array[FileStream]:
        """

        :return:
        """
    @overload
    def GetFiles(self, getResourceModules: bool) -> Array[FileStream]:
        """

        :param getResourceModules:
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
    def GetLoadedModules(self) -> Array[Module]:
        """

        :return:
        """
    @overload
    def GetLoadedModules(self, getResourceModules: bool) -> Array[Module]:
        """

        :param getResourceModules:
        :return:
        """
    def GetManifestResourceInfo(self, resourceName: str) -> ManifestResourceInfo:
        """

        :param resourceName:
        :return:
        """
    def GetManifestResourceNames(self) -> Array[str]:
        """

        :return:
        """
    @overload
    def GetManifestResourceStream(self, name: str) -> Stream:
        """

        :param name:
        :return:
        """
    @overload
    def GetManifestResourceStream(self, type: Type, name: str) -> Stream:
        """

        :param type:
        :param name:
        :return:
        """
    def GetModule(self, name: str) -> Module:
        """

        :param name:
        :return:
        """
    @overload
    def GetModules(self) -> Array[Module]:
        """

        :return:
        """
    @overload
    def GetModules(self, getResourceModules: bool) -> Array[Module]:
        """

        :param getResourceModules:
        :return:
        """
    @overload
    def GetName(self) -> AssemblyName:
        """

        :return:
        """
    @overload
    def GetName(self, copiedName: bool) -> AssemblyName:
        """

        :param copiedName:
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
    def GetReferencedAssemblies(self) -> Array[AssemblyName]:
        """

        :return:
        """
    @overload
    def GetSatelliteAssembly(self, culture: CultureInfo) -> Assembly:
        """

        :param culture:
        :return:
        """
    @overload
    def GetSatelliteAssembly(self, culture: CultureInfo, version: Version) -> Assembly:
        """

        :param culture:
        :param version:
        :return:
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
    def GetType(self, name: str) -> Type:
        """

        :param name:
        :return:
        """
    @overload
    def GetType(self, name: str, throwOnError: bool) -> Type:
        """

        :param name:
        :param throwOnError:
        :return:
        """
    @overload
    def GetType(self, name: str, throwOnError: bool, ignoreCase: bool) -> Type:
        """

        :param name:
        :param throwOnError:
        :param ignoreCase:
        :return:
        """
    def GetTypes(self) -> Array[Type]:
        """

        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @classmethod
    @overload
    def Load(cls, assemblyRef: AssemblyName) -> Assembly:
        """

        :param assemblyRef:
        :return:
        """
    @classmethod
    @overload
    def Load(cls, rawAssembly: Array[int]) -> Assembly:
        """

        :param rawAssembly:
        :return:
        """
    @classmethod
    @overload
    def Load(cls, assemblyString: str) -> Assembly:
        """

        :param assemblyString:
        :return:
        """
    @classmethod
    @overload
    def Load(cls, assemblyRef: AssemblyName, assemblySecurity: Evidence) -> Assembly:
        """

        :param assemblyRef:
        :param assemblySecurity:
        :return:
        """
    @classmethod
    @overload
    def Load(cls, rawAssembly: Array[int], rawSymbolStore: Array[int]) -> Assembly:
        """

        :param rawAssembly:
        :param rawSymbolStore:
        :return:
        """
    @classmethod
    @overload
    def Load(cls, assemblyString: str, assemblySecurity: Evidence) -> Assembly:
        """

        :param assemblyString:
        :param assemblySecurity:
        :return:
        """
    @classmethod
    @overload
    def Load(
        cls, rawAssembly: Array[int], rawSymbolStore: Array[int], securityEvidence: Evidence
    ) -> Assembly:
        """

        :param rawAssembly:
        :param rawSymbolStore:
        :param securityEvidence:
        :return:
        """
    @classmethod
    @overload
    def Load(
        cls,
        rawAssembly: Array[int],
        rawSymbolStore: Array[int],
        securityContextSource: SecurityContextSource,
    ) -> Assembly:
        """

        :param rawAssembly:
        :param rawSymbolStore:
        :param securityContextSource:
        :return:
        """
    @classmethod
    @overload
    def LoadFile(cls, path: str) -> Assembly:
        """

        :param path:
        :return:
        """
    @classmethod
    @overload
    def LoadFile(cls, path: str, securityEvidence: Evidence) -> Assembly:
        """

        :param path:
        :param securityEvidence:
        :return:
        """
    @classmethod
    @overload
    def LoadFrom(cls, assemblyFile: str) -> Assembly:
        """

        :param assemblyFile:
        :return:
        """
    @classmethod
    @overload
    def LoadFrom(cls, assemblyFile: str, securityEvidence: Evidence) -> Assembly:
        """

        :param assemblyFile:
        :param securityEvidence:
        :return:
        """
    @classmethod
    @overload
    def LoadFrom(
        cls, assemblyFile: str, hashValue: Array[int], hashAlgorithm: AssemblyHashAlgorithm
    ) -> Assembly:
        """

        :param assemblyFile:
        :param hashValue:
        :param hashAlgorithm:
        :return:
        """
    @classmethod
    @overload
    def LoadFrom(
        cls,
        assemblyFile: str,
        securityEvidence: Evidence,
        hashValue: Array[int],
        hashAlgorithm: AssemblyHashAlgorithm,
    ) -> Assembly:
        """

        :param assemblyFile:
        :param securityEvidence:
        :param hashValue:
        :param hashAlgorithm:
        :return:
        """
    @overload
    def LoadModule(self, moduleName: str, rawModule: Array[int]) -> Module:
        """

        :param moduleName:
        :param rawModule:
        :return:
        """
    @overload
    def LoadModule(
        self, moduleName: str, rawModule: Array[int], rawSymbolStore: Array[int]
    ) -> Module:
        """

        :param moduleName:
        :param rawModule:
        :param rawSymbolStore:
        :return:
        """
    @classmethod
    @overload
    def LoadWithPartialName(cls, partialName: str) -> Assembly:
        """

        :param partialName:
        :return:
        """
    @classmethod
    @overload
    def LoadWithPartialName(cls, partialName: str, securityEvidence: Evidence) -> Assembly:
        """

        :param partialName:
        :param securityEvidence:
        :return:
        """
    @classmethod
    @overload
    def ReflectionOnlyLoad(cls, rawAssembly: Array[int]) -> Assembly:
        """

        :param rawAssembly:
        :return:
        """
    @classmethod
    @overload
    def ReflectionOnlyLoad(cls, assemblyString: str) -> Assembly:
        """

        :param assemblyString:
        :return:
        """
    @classmethod
    def ReflectionOnlyLoadFrom(cls, assemblyFile: str) -> Assembly:
        """

        :param assemblyFile:
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
    @classmethod
    def UnsafeLoadFrom(cls, assemblyFile: str) -> Assembly:
        """

        :param assemblyFile:
        :return:
        """
    def __eq__(self, other: Assembly) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: Assembly) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: Assembly, right: Assembly) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: Assembly, right: Assembly) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    ModuleResolve: EventType[ModuleResolveEventHandler] = ...
    """"""

class AssemblyAlgorithmIdAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self, algorithmId: AssemblyHashAlgorithm):
        """

        :param algorithmId:
        """
    @overload
    def __init__(self, algorithmId: int):
        """

        :param algorithmId:
        """
    @property
    def AlgorithmId(self) -> int:
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

class AssemblyCompanyAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, company: str):
        """

        :param company:
        """
    @property
    def Company(self) -> str:
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

class AssemblyConfigurationAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, configuration: str):
        """

        :param configuration:
        """
    @property
    def Configuration(self) -> str:
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

class AssemblyContentType(Enum):
    """"""

    Default: AssemblyContentType = ...
    """"""
    WindowsRuntime: AssemblyContentType = ...
    """"""

class AssemblyCopyrightAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, copyright: str):
        """

        :param copyright:
        """
    @property
    def Copyright(self) -> str:
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

class AssemblyCultureAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, culture: str):
        """

        :param culture:
        """
    @property
    def Culture(self) -> str:
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

class AssemblyDefaultAliasAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, defaultAlias: str):
        """

        :param defaultAlias:
        """
    @property
    def DefaultAlias(self) -> str:
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

class AssemblyDelaySignAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, delaySign: bool):
        """

        :param delaySign:
        """
    @property
    def DelaySign(self) -> bool:
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

class AssemblyDescriptionAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, description: str):
        """

        :param description:
        """
    @property
    def Description(self) -> str:
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

class AssemblyFileVersionAttribute(Attribute, _Attribute):
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

class AssemblyFlagsAttribute(Attribute, _Attribute):
    """"""

    @overload
    def __init__(self, assemblyFlags: AssemblyNameFlags):
        """

        :param assemblyFlags:
        """
    @overload
    def __init__(self, assemblyFlags: int):
        """

        :param assemblyFlags:
        """
    @overload
    def __init__(self, flags: int):
        """

        :param flags:
        """
    @property
    def AssemblyFlags(self) -> int:
        """

        :return:
        """
    @property
    def Flags(self) -> int:
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

class AssemblyInformationalVersionAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, informationalVersion: str):
        """

        :param informationalVersion:
        """
    @property
    def InformationalVersion(self) -> str:
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

class AssemblyKeyFileAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, keyFile: str):
        """

        :param keyFile:
        """
    @property
    def KeyFile(self) -> str:
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

class AssemblyKeyNameAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, keyName: str):
        """

        :param keyName:
        """
    @property
    def KeyName(self) -> str:
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

class AssemblyMetadataAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, key: str, value: str):
        """

        :param key:
        :param value:
        """
    @property
    def Key(self) -> str:
        """

        :return:
        """
    @property
    def TypeId(self) -> object:
        """

        :return:
        """
    @property
    def Value(self) -> str:
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

class AssemblyName(Object, _AssemblyName, IDeserializationCallback, ISerializable, ICloneable):
    """"""

    @overload
    def __init__(self):
        """"""
    @overload
    def __init__(self, assemblyName: str):
        """

        :param assemblyName:
        """
    @property
    def CodeBase(self) -> str:
        """

        :return:
        """
    @CodeBase.setter
    def CodeBase(self, value: str) -> None: ...
    @property
    def ContentType(self) -> AssemblyContentType:
        """

        :return:
        """
    @ContentType.setter
    def ContentType(self, value: AssemblyContentType) -> None: ...
    @property
    def CultureInfo(self) -> CultureInfo:
        """

        :return:
        """
    @CultureInfo.setter
    def CultureInfo(self, value: CultureInfo) -> None: ...
    @property
    def CultureName(self) -> str:
        """

        :return:
        """
    @CultureName.setter
    def CultureName(self, value: str) -> None: ...
    @property
    def EscapedCodeBase(self) -> str:
        """

        :return:
        """
    @property
    def Flags(self) -> AssemblyNameFlags:
        """

        :return:
        """
    @Flags.setter
    def Flags(self, value: AssemblyNameFlags) -> None: ...
    @property
    def FullName(self) -> str:
        """

        :return:
        """
    @property
    def HashAlgorithm(self) -> AssemblyHashAlgorithm:
        """

        :return:
        """
    @HashAlgorithm.setter
    def HashAlgorithm(self, value: AssemblyHashAlgorithm) -> None: ...
    @property
    def KeyPair(self) -> StrongNameKeyPair:
        """

        :return:
        """
    @KeyPair.setter
    def KeyPair(self, value: StrongNameKeyPair) -> None: ...
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def ProcessorArchitecture(self) -> ProcessorArchitecture:
        """

        :return:
        """
    @ProcessorArchitecture.setter
    def ProcessorArchitecture(self, value: ProcessorArchitecture) -> None: ...
    @property
    def Version(self) -> Version:
        """

        :return:
        """
    @Version.setter
    def Version(self, value: Version) -> None: ...
    @property
    def VersionCompatibility(self) -> AssemblyVersionCompatibility:
        """

        :return:
        """
    @VersionCompatibility.setter
    def VersionCompatibility(self, value: AssemblyVersionCompatibility) -> None: ...
    def Clone(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    def GetAssemblyName(cls, assemblyFile: str) -> AssemblyName:
        """

        :param assemblyFile:
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
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetPublicKey(self) -> Array[int]:
        """

        :return:
        """
    def GetPublicKeyToken(self) -> Array[int]:
        """

        :return:
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
    def OnDeserialization(self, sender: object) -> None:
        """

        :param sender:
        """
    @classmethod
    def ReferenceMatchesDefinition(cls, reference: AssemblyName, definition: AssemblyName) -> bool:
        """

        :param reference:
        :param definition:
        :return:
        """
    def SetPublicKey(self, publicKey: Array[int]) -> None:
        """

        :param publicKey:
        """
    def SetPublicKeyToken(self, publicKeyToken: Array[int]) -> None:
        """

        :param publicKeyToken:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class AssemblyNameFlags(Enum):
    """"""

    _None: AssemblyNameFlags = ...
    """"""
    PublicKey: AssemblyNameFlags = ...
    """"""
    Retargetable: AssemblyNameFlags = ...
    """"""
    EnableJITcompileOptimizer: AssemblyNameFlags = ...
    """"""
    EnableJITcompileTracking: AssemblyNameFlags = ...
    """"""

class AssemblyNameProxy(MarshalByRefObject):
    """"""

    def __init__(self):
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """

        :param requestedType:
        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetAssemblyName(self, assemblyFile: str) -> AssemblyName:
        """

        :param assemblyFile:
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
    def InitializeLifetimeService(self) -> object:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class AssemblyProductAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, product: str):
        """

        :param product:
        """
    @property
    def Product(self) -> str:
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

class AssemblySignatureKeyAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, publicKey: str, countersignature: str):
        """

        :param publicKey:
        :param countersignature:
        """
    @property
    def Countersignature(self) -> str:
        """

        :return:
        """
    @property
    def PublicKey(self) -> str:
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

class AssemblyTitleAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, title: str):
        """

        :param title:
        """
    @property
    def Title(self) -> str:
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

class AssemblyTrademarkAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, trademark: str):
        """

        :param trademark:
        """
    @property
    def Trademark(self) -> str:
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

class AssemblyVersionAttribute(Attribute, _Attribute):
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

class Associates(ABC, Object):
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

class Binder(ABC, Object):
    """"""

    def BindToField(
        self,
        bindingAttr: BindingFlags,
        match: Array[FieldInfo],
        value: object,
        culture: CultureInfo,
    ) -> FieldInfo:
        """

        :param bindingAttr:
        :param match:
        :param value:
        :param culture:
        :return:
        """
    def BindToMethod(
        self,
        bindingAttr: BindingFlags,
        match: Array[MethodBase],
        args: object,
        modifiers: Array[ParameterModifier],
        culture: CultureInfo,
        names: Array[str],
        state: object,
    ) -> Tuple[MethodBase, object]:
        """

        :param bindingAttr:
        :param match:
        :param args:
        :param modifiers:
        :param culture:
        :param names:
        :param state:
        :return:
        """
    def ChangeType(self, value: object, type: Type, culture: CultureInfo) -> object:
        """

        :param value:
        :param type:
        :param culture:
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
    def ReorderArgumentArray(self, args: object, state: object) -> None:
        """

        :param args:
        :param state:
        """
    def SelectMethod(
        self,
        bindingAttr: BindingFlags,
        match: Array[MethodBase],
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodBase:
        """

        :param bindingAttr:
        :param match:
        :param types:
        :param modifiers:
        :return:
        """
    def SelectProperty(
        self,
        bindingAttr: BindingFlags,
        match: Array[PropertyInfo],
        returnType: Type,
        indexes: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> PropertyInfo:
        """

        :param bindingAttr:
        :param match:
        :param returnType:
        :param indexes:
        :param modifiers:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class BindingFlags(Enum):
    """"""

    Default: BindingFlags = ...
    """"""
    IgnoreCase: BindingFlags = ...
    """"""
    DeclaredOnly: BindingFlags = ...
    """"""
    Instance: BindingFlags = ...
    """"""
    Static: BindingFlags = ...
    """"""
    Public: BindingFlags = ...
    """"""
    NonPublic: BindingFlags = ...
    """"""
    FlattenHierarchy: BindingFlags = ...
    """"""
    InvokeMethod: BindingFlags = ...
    """"""
    CreateInstance: BindingFlags = ...
    """"""
    GetField: BindingFlags = ...
    """"""
    SetField: BindingFlags = ...
    """"""
    GetProperty: BindingFlags = ...
    """"""
    SetProperty: BindingFlags = ...
    """"""
    PutDispProperty: BindingFlags = ...
    """"""
    PutRefDispProperty: BindingFlags = ...
    """"""
    ExactBinding: BindingFlags = ...
    """"""
    SuppressChangeType: BindingFlags = ...
    """"""
    OptionalParamBinding: BindingFlags = ...
    """"""
    IgnoreReturn: BindingFlags = ...
    """"""

class BlobUtilities(ABC, Object):
    """"""

    SizeOfGuid: Final[ClassVar[int]] = ...
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
    @classmethod
    def ReadBytes(cls, buffer: int, byteCount: int) -> Array[int]:
        """

        :param buffer:
        :param byteCount:
        :return:
        """
    @classmethod
    def ReadImmutableBytes(cls, buffer: int, byteCount: int) -> ImmutableArray[int]:
        """

        :param buffer:
        :param byteCount:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CallingConventions(Enum):
    """"""

    Standard: CallingConventions = ...
    """"""
    VarArgs: CallingConventions = ...
    """"""
    Any: CallingConventions = ...
    """"""
    HasThis: CallingConventions = ...
    """"""
    ExplicitThis: CallingConventions = ...
    """"""

class CerHashtable(Generic[K, V], ValueType):
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

class ConstArray(ValueType):
    """"""

    @property
    def Item(self) -> int:
        """

        :return:
        """
    @property
    def Length(self) -> int:
        """

        :return:
        """
    @property
    def Signature(self) -> IntPtr:
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
    def __getitem__(self, index: int) -> int:
        """

        :param index:
        :return:
        """

class ConstructorInfo(
    ABC, MethodBase, ICustomAttributeProvider, _ConstructorInfo, _MemberInfo, _MethodBase
):
    """"""

    ConstructorName: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    TypeConstructorName: Final[ClassVar[str]] = ...
    """
    
    :return: 
    """
    @property
    def Attributes(self) -> MethodAttributes:
        """

        :return:
        """
    @property
    def Attributes(self) -> MethodAttributes:
        """

        :return:
        """
    @property
    def CallingConvention(self) -> CallingConventions:
        """

        :return:
        """
    @property
    def CallingConvention(self) -> CallingConventions:
        """

        :return:
        """
    @property
    def ContainsGenericParameters(self) -> bool:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def IsAbstract(self) -> bool:
        """

        :return:
        """
    @property
    def IsAbstract(self) -> bool:
        """

        :return:
        """
    @property
    def IsAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsConstructor(self) -> bool:
        """

        :return:
        """
    @property
    def IsConstructor(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFinal(self) -> bool:
        """

        :return:
        """
    @property
    def IsFinal(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericMethod(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericMethodDefinition(self) -> bool:
        """

        :return:
        """
    @property
    def IsHideBySig(self) -> bool:
        """

        :return:
        """
    @property
    def IsHideBySig(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityTransparent(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsStatic(self) -> bool:
        """

        :return:
        """
    @property
    def IsStatic(self) -> bool:
        """

        :return:
        """
    @property
    def IsVirtual(self) -> bool:
        """

        :return:
        """
    @property
    def IsVirtual(self) -> bool:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """

        :return:
        """
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """

        :return:
        """
    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
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
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    def GetGenericArguments(self) -> Array[Type]:
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
    @overload
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
    @overload
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
    def GetMethodBody(self) -> MethodBody:
        """

        :return:
        """
    @overload
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    @overload
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    @overload
    def GetParameters(self) -> Array[ParameterInfo]:
        """

        :return:
        """
    @overload
    def GetParameters(self) -> Array[ParameterInfo]:
        """

        :return:
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
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def Invoke(self, parameters: Array[object]) -> object:
        """

        :param parameters:
        :return:
        """
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """

        :param obj:
        :param parameters:
        :return:
        """
    @overload
    def Invoke(
        self,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
    @overload
    def Invoke(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param obj:
        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
    @overload
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
    @overload
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
    @overload
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
    def Invoke_2(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param obj:
        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
    def Invoke_3(self, obj: object, parameters: Array[object]) -> object:
        """

        :param obj:
        :param parameters:
        :return:
        """
    def Invoke_4(
        self,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
    def Invoke_5(self, parameters: Array[object]) -> object:
        """

        :param parameters:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
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
    def __eq__(self, other: ConstructorInfo) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: ConstructorInfo) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: ConstructorInfo, right: ConstructorInfo) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: ConstructorInfo, right: ConstructorInfo) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

class CorElementType(Enum):
    """"""

    End: CorElementType = ...
    """"""
    Void: CorElementType = ...
    """"""
    Boolean: CorElementType = ...
    """"""
    Char: CorElementType = ...
    """"""
    I1: CorElementType = ...
    """"""
    U1: CorElementType = ...
    """"""
    I2: CorElementType = ...
    """"""
    U2: CorElementType = ...
    """"""
    I4: CorElementType = ...
    """"""
    U4: CorElementType = ...
    """"""
    I8: CorElementType = ...
    """"""
    U8: CorElementType = ...
    """"""
    R4: CorElementType = ...
    """"""
    R8: CorElementType = ...
    """"""
    String: CorElementType = ...
    """"""
    Ptr: CorElementType = ...
    """"""
    ByRef: CorElementType = ...
    """"""
    ValueType: CorElementType = ...
    """"""
    Class: CorElementType = ...
    """"""
    Var: CorElementType = ...
    """"""
    Array: CorElementType = ...
    """"""
    GenericInst: CorElementType = ...
    """"""
    TypedByRef: CorElementType = ...
    """"""
    I: CorElementType = ...
    """"""
    U: CorElementType = ...
    """"""
    FnPtr: CorElementType = ...
    """"""
    Object: CorElementType = ...
    """"""
    SzArray: CorElementType = ...
    """"""
    MVar: CorElementType = ...
    """"""
    CModReqd: CorElementType = ...
    """"""
    CModOpt: CorElementType = ...
    """"""
    Internal: CorElementType = ...
    """"""
    Max: CorElementType = ...
    """"""
    Modifier: CorElementType = ...
    """"""
    Sentinel: CorElementType = ...
    """"""
    Pinned: CorElementType = ...
    """"""

class CustomAttribute(ABC, Object):
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

class CustomAttributeCtorParameter(ValueType):
    """"""

    def __init__(self, type: CustomAttributeType):
        """

        :param type:
        """
    @property
    def CustomAttributeEncodedArgument(self) -> CustomAttributeEncodedArgument:
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

class CustomAttributeData(Object):
    """"""

    @property
    def AttributeType(self) -> Type:
        """

        :return:
        """
    @property
    def Constructor(self) -> ConstructorInfo:
        """

        :return:
        """
    @property
    def ConstructorArguments(self) -> IList[CustomAttributeTypedArgument]:
        """

        :return:
        """
    @property
    def NamedArguments(self) -> IList[CustomAttributeNamedArgument]:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(cls, target: Assembly) -> IList[CustomAttributeData]:
        """

        :param target:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(cls, target: MemberInfo) -> IList[CustomAttributeData]:
        """

        :param target:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(cls, target: Module) -> IList[CustomAttributeData]:
        """

        :param target:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(cls, target: ParameterInfo) -> IList[CustomAttributeData]:
        """

        :param target:
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

class CustomAttributeEncodedArgument(ValueType):
    """"""

    @property
    def ArrayValue(self) -> Array[CustomAttributeEncodedArgument]:
        """

        :return:
        """
    @property
    def CustomAttributeType(self) -> CustomAttributeType:
        """

        :return:
        """
    @property
    def PrimitiveValue(self) -> int:
        """

        :return:
        """
    @property
    def StringValue(self) -> str:
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

class CustomAttributeEncoding(Enum):
    """"""

    Undefined: CustomAttributeEncoding = ...
    """"""
    Boolean: CustomAttributeEncoding = ...
    """"""
    Char: CustomAttributeEncoding = ...
    """"""
    SByte: CustomAttributeEncoding = ...
    """"""
    Byte: CustomAttributeEncoding = ...
    """"""
    Int16: CustomAttributeEncoding = ...
    """"""
    UInt16: CustomAttributeEncoding = ...
    """"""
    Int32: CustomAttributeEncoding = ...
    """"""
    UInt32: CustomAttributeEncoding = ...
    """"""
    Int64: CustomAttributeEncoding = ...
    """"""
    UInt64: CustomAttributeEncoding = ...
    """"""
    Float: CustomAttributeEncoding = ...
    """"""
    Double: CustomAttributeEncoding = ...
    """"""
    String: CustomAttributeEncoding = ...
    """"""
    Array: CustomAttributeEncoding = ...
    """"""
    Type: CustomAttributeEncoding = ...
    """"""
    Object: CustomAttributeEncoding = ...
    """"""
    Field: CustomAttributeEncoding = ...
    """"""
    Property: CustomAttributeEncoding = ...
    """"""
    Enum: CustomAttributeEncoding = ...
    """"""

class CustomAttributeExtensions(ABC, Object):
    """"""

    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttribute(cls, element: Assembly) -> T:
        """

        :param element:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttribute(cls, element: MemberInfo) -> T:
        """

        :param element:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttribute(cls, element: Module) -> T:
        """

        :param element:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttribute(cls, element: ParameterInfo) -> T:
        """

        :param element:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttribute(cls, element: Assembly, attributeType: Type) -> Attribute:
        """

        :param element:
        :param attributeType:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttribute(cls, element: MemberInfo, inherit: bool) -> T:
        """

        :param element:
        :param inherit:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttribute(cls, element: MemberInfo, attributeType: Type) -> Attribute:
        """

        :param element:
        :param attributeType:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttribute(cls, element: Module, attributeType: Type) -> Attribute:
        """

        :param element:
        :param attributeType:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttribute(cls, element: ParameterInfo, inherit: bool) -> T:
        """

        :param element:
        :param inherit:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttribute(cls, element: ParameterInfo, attributeType: Type) -> Attribute:
        """

        :param element:
        :param attributeType:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttribute(
        cls, element: MemberInfo, attributeType: Type, inherit: bool
    ) -> Attribute:
        """

        :param element:
        :param attributeType:
        :param inherit:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttribute(
        cls, element: ParameterInfo, attributeType: Type, inherit: bool
    ) -> Attribute:
        """

        :param element:
        :param attributeType:
        :param inherit:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: Assembly) -> IEnumerable[T]:
        """

        :param element:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: MemberInfo) -> IEnumerable[T]:
        """

        :param element:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: Module) -> IEnumerable[T]:
        """

        :param element:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: ParameterInfo) -> IEnumerable[T]:
        """

        :param element:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: Assembly, attributeType: Type) -> IEnumerable[Attribute]:
        """

        :param element:
        :param attributeType:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: MemberInfo, inherit: bool) -> IEnumerable[T]:
        """

        :param element:
        :param inherit:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(
        cls, element: MemberInfo, attributeType: Type
    ) -> IEnumerable[Attribute]:
        """

        :param element:
        :param attributeType:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: Module, attributeType: Type) -> IEnumerable[Attribute]:
        """

        :param element:
        :param attributeType:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: ParameterInfo, inherit: bool) -> IEnumerable[T]:
        """

        :param element:
        :param inherit:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(
        cls, element: ParameterInfo, attributeType: Type
    ) -> IEnumerable[Attribute]:
        """

        :param element:
        :param attributeType:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(
        cls, element: MemberInfo, attributeType: Type, inherit: bool
    ) -> IEnumerable[Attribute]:
        """

        :param element:
        :param attributeType:
        :param inherit:
        :return:
        """
    @classmethod
    @overload
    def GetCustomAttributes(
        cls, element: ParameterInfo, attributeType: Type, inherit: bool
    ) -> IEnumerable[Attribute]:
        """

        :param element:
        :param attributeType:
        :param inherit:
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
    @classmethod
    @overload
    def IsDefined(cls, element: Assembly, attributeType: Type) -> bool:
        """

        :param element:
        :param attributeType:
        :return:
        """
    @classmethod
    @overload
    def IsDefined(cls, element: MemberInfo, attributeType: Type) -> bool:
        """

        :param element:
        :param attributeType:
        :return:
        """
    @classmethod
    @overload
    def IsDefined(cls, element: Module, attributeType: Type) -> bool:
        """

        :param element:
        :param attributeType:
        :return:
        """
    @classmethod
    @overload
    def IsDefined(cls, element: ParameterInfo, attributeType: Type) -> bool:
        """

        :param element:
        :param attributeType:
        :return:
        """
    @classmethod
    @overload
    def IsDefined(cls, element: MemberInfo, attributeType: Type, inherit: bool) -> bool:
        """

        :param element:
        :param attributeType:
        :param inherit:
        :return:
        """
    @classmethod
    @overload
    def IsDefined(cls, element: ParameterInfo, attributeType: Type, inherit: bool) -> bool:
        """

        :param element:
        :param attributeType:
        :param inherit:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class CustomAttributeFormatException(FormatException, _Exception, ISerializable):
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

class CustomAttributeNamedArgument(ValueType):
    """"""

    @overload
    def __init__(self, memberInfo: MemberInfo, typedArgument: CustomAttributeTypedArgument):
        """

        :param memberInfo:
        :param typedArgument:
        """
    @overload
    def __init__(self, memberInfo: MemberInfo, value: object):
        """

        :param memberInfo:
        :param value:
        """
    @property
    def IsField(self) -> bool:
        """

        :return:
        """
    @property
    def MemberInfo(self) -> MemberInfo:
        """

        :return:
        """
    @property
    def MemberName(self) -> str:
        """

        :return:
        """
    @property
    def TypedValue(self) -> CustomAttributeTypedArgument:
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
    def __eq__(self, other: CustomAttributeNamedArgument) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: CustomAttributeNamedArgument) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(
        cls, left: CustomAttributeNamedArgument, right: CustomAttributeNamedArgument
    ) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(
        cls, left: CustomAttributeNamedArgument, right: CustomAttributeNamedArgument
    ) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

class CustomAttributeNamedParameter(ValueType):
    """"""

    def __init__(
        self, argumentName: str, fieldOrProperty: CustomAttributeEncoding, type: CustomAttributeType
    ):
        """

        :param argumentName:
        :param fieldOrProperty:
        :param type:
        """
    @property
    def EncodedArgument(self) -> CustomAttributeEncodedArgument:
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

class CustomAttributeRecord(ValueType):
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

class CustomAttributeType(ValueType):
    """"""

    def __init__(
        self,
        encodedType: CustomAttributeEncoding,
        encodedArrayType: CustomAttributeEncoding,
        encodedEnumType: CustomAttributeEncoding,
        enumName: str,
    ):
        """

        :param encodedType:
        :param encodedArrayType:
        :param encodedEnumType:
        :param enumName:
        """
    @property
    def EncodedArrayType(self) -> CustomAttributeEncoding:
        """

        :return:
        """
    @property
    def EncodedEnumType(self) -> CustomAttributeEncoding:
        """

        :return:
        """
    @property
    def EncodedType(self) -> CustomAttributeEncoding:
        """

        :return:
        """
    @property
    def EnumName(self) -> str:
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

class CustomAttributeTypedArgument(ValueType):
    """"""

    @overload
    def __init__(self, value: object):
        """

        :param value:
        """
    @overload
    def __init__(self, argumentType: Type, value: object):
        """

        :param argumentType:
        :param value:
        """
    @property
    def ArgumentType(self) -> Type:
        """

        :return:
        """
    @property
    def Value(self) -> object:
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
    def __eq__(self, other: CustomAttributeTypedArgument) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: CustomAttributeTypedArgument) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(
        cls, left: CustomAttributeTypedArgument, right: CustomAttributeTypedArgument
    ) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(
        cls, left: CustomAttributeTypedArgument, right: CustomAttributeTypedArgument
    ) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

class DefaultMemberAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, memberName: str):
        """

        :param memberName:
        """
    @property
    def MemberName(self) -> str:
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

class EventAttributes(Enum):
    """"""

    _None: EventAttributes = ...
    """"""
    SpecialName: EventAttributes = ...
    """"""
    ReservedMask: EventAttributes = ...
    """"""
    RTSpecialName: EventAttributes = ...
    """"""

class EventInfo(ABC, MemberInfo, ICustomAttributeProvider, _EventInfo, _MemberInfo):
    """"""

    @property
    def AddMethod(self) -> MethodInfo:
        """

        :return:
        """
    @property
    def Attributes(self) -> EventAttributes:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def EventHandlerType(self) -> Type:
        """

        :return:
        """
    @property
    def IsMulticast(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def RaiseMethod(self) -> MethodInfo:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def RemoveMethod(self) -> MethodInfo:
        """

        :return:
        """
    def AddEventHandler(self, target: object, handler: Delegate) -> None:
        """

        :param target:
        :param handler:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def GetAddMethod(self) -> MethodInfo:
        """

        :return:
        """
    @overload
    def GetAddMethod(self, nonPublic: bool) -> MethodInfo:
        """

        :param nonPublic:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
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
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
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
    @overload
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
    @overload
    def GetOtherMethods(self) -> Array[MethodInfo]:
        """

        :return:
        """
    @overload
    def GetOtherMethods(self, nonPublic: bool) -> Array[MethodInfo]:
        """

        :param nonPublic:
        :return:
        """
    @overload
    def GetRaiseMethod(self) -> MethodInfo:
        """

        :return:
        """
    @overload
    def GetRaiseMethod(self, nonPublic: bool) -> MethodInfo:
        """

        :param nonPublic:
        :return:
        """
    @overload
    def GetRemoveMethod(self) -> MethodInfo:
        """

        :return:
        """
    @overload
    def GetRemoveMethod(self, nonPublic: bool) -> MethodInfo:
        """

        :param nonPublic:
        :return:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
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
    @overload
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
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def RemoveEventHandler(self, target: object, handler: Delegate) -> None:
        """

        :param target:
        :param handler:
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
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    def __eq__(self, other: EventInfo) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: EventInfo) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: EventInfo, right: EventInfo) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: EventInfo, right: EventInfo) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

class ExceptionHandlingClause(Object):
    """"""

    @property
    def CatchType(self) -> Type:
        """

        :return:
        """
    @property
    def FilterOffset(self) -> int:
        """

        :return:
        """
    @property
    def Flags(self) -> ExceptionHandlingClauseOptions:
        """

        :return:
        """
    @property
    def HandlerLength(self) -> int:
        """

        :return:
        """
    @property
    def HandlerOffset(self) -> int:
        """

        :return:
        """
    @property
    def TryLength(self) -> int:
        """

        :return:
        """
    @property
    def TryOffset(self) -> int:
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

class ExceptionHandlingClauseOptions(Enum):
    """"""

    Clause: ExceptionHandlingClauseOptions = ...
    """"""
    Filter: ExceptionHandlingClauseOptions = ...
    """"""
    Finally: ExceptionHandlingClauseOptions = ...
    """"""
    Fault: ExceptionHandlingClauseOptions = ...
    """"""

class FieldAttributes(Enum):
    """"""

    PrivateScope: FieldAttributes = ...
    """"""
    Private: FieldAttributes = ...
    """"""
    FamANDAssem: FieldAttributes = ...
    """"""
    Assembly: FieldAttributes = ...
    """"""
    Family: FieldAttributes = ...
    """"""
    FamORAssem: FieldAttributes = ...
    """"""
    Public: FieldAttributes = ...
    """"""
    FieldAccessMask: FieldAttributes = ...
    """"""
    Static: FieldAttributes = ...
    """"""
    InitOnly: FieldAttributes = ...
    """"""
    Literal: FieldAttributes = ...
    """"""
    NotSerialized: FieldAttributes = ...
    """"""
    HasFieldRVA: FieldAttributes = ...
    """"""
    SpecialName: FieldAttributes = ...
    """"""
    RTSpecialName: FieldAttributes = ...
    """"""
    HasFieldMarshal: FieldAttributes = ...
    """"""
    PinvokeImpl: FieldAttributes = ...
    """"""
    HasDefault: FieldAttributes = ...
    """"""
    ReservedMask: FieldAttributes = ...
    """"""

class FieldInfo(ABC, MemberInfo, ICustomAttributeProvider, _FieldInfo, _MemberInfo):
    """"""

    @property
    def Attributes(self) -> FieldAttributes:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def FieldHandle(self) -> RuntimeFieldHandle:
        """

        :return:
        """
    @property
    def FieldType(self) -> Type:
        """

        :return:
        """
    @property
    def IsAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsInitOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsLiteral(self) -> bool:
        """

        :return:
        """
    @property
    def IsNotSerialized(self) -> bool:
        """

        :return:
        """
    @property
    def IsPinvokeImpl(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityTransparent(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsStatic(self) -> bool:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
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
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    @classmethod
    @overload
    def GetFieldFromHandle(cls, handle: RuntimeFieldHandle) -> FieldInfo:
        """

        :param handle:
        :return:
        """
    @classmethod
    @overload
    def GetFieldFromHandle(
        cls, handle: RuntimeFieldHandle, declaringType: RuntimeTypeHandle
    ) -> FieldInfo:
        """

        :param handle:
        :param declaringType:
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
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
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
    @overload
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
    def GetOptionalCustomModifiers(self) -> Array[Type]:
        """

        :return:
        """
    def GetRawConstantValue(self) -> object:
        """

        :return:
        """
    def GetRequiredCustomModifiers(self) -> Array[Type]:
        """

        :return:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    def GetValue(self, obj: object) -> object:
        """

        :param obj:
        :return:
        """
    def GetValueDirect(self, obj: TypedReference) -> object:
        """

        :param obj:
        :return:
        """
    @overload
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
    @overload
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
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def SetValue(self, obj: object, value: object) -> None:
        """

        :param obj:
        :param value:
        """
    @overload
    def SetValue(
        self,
        obj: object,
        value: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        culture: CultureInfo,
    ) -> None:
        """

        :param obj:
        :param value:
        :param invokeAttr:
        :param binder:
        :param culture:
        """
    def SetValueDirect(self, obj: TypedReference, value: object) -> None:
        """

        :param obj:
        :param value:
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
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    def __eq__(self, other: FieldInfo) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: FieldInfo) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: FieldInfo, right: FieldInfo) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: FieldInfo, right: FieldInfo) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

class GenericParameterAttributes(Enum):
    """"""

    _None: GenericParameterAttributes = ...
    """"""
    Covariant: GenericParameterAttributes = ...
    """"""
    Contravariant: GenericParameterAttributes = ...
    """"""
    VarianceMask: GenericParameterAttributes = ...
    """"""
    ReferenceTypeConstraint: GenericParameterAttributes = ...
    """"""
    NotNullableValueTypeConstraint: GenericParameterAttributes = ...
    """"""
    DefaultConstructorConstraint: GenericParameterAttributes = ...
    """"""
    SpecialConstraintMask: GenericParameterAttributes = ...
    """"""

class ICustomAttributeProvider:
    """"""

    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """

class ICustomTypeProvider:
    """"""

    def GetCustomType(self) -> Type:
        """

        :return:
        """

class INVOCATION_FLAGS(Enum):
    """"""

    INVOCATION_FLAGS_UNKNOWN: INVOCATION_FLAGS = ...
    """"""
    INVOCATION_FLAGS_INITIALIZED: INVOCATION_FLAGS = ...
    """"""
    INVOCATION_FLAGS_NO_INVOKE: INVOCATION_FLAGS = ...
    """"""
    INVOCATION_FLAGS_NEED_SECURITY: INVOCATION_FLAGS = ...
    """"""
    INVOCATION_FLAGS_NO_CTOR_INVOKE: INVOCATION_FLAGS = ...
    """"""
    INVOCATION_FLAGS_IS_CTOR: INVOCATION_FLAGS = ...
    """"""
    INVOCATION_FLAGS_SPECIAL_FIELD: INVOCATION_FLAGS = ...
    """"""
    INVOCATION_FLAGS_RISKY_METHOD: INVOCATION_FLAGS = ...
    """"""
    INVOCATION_FLAGS_FIELD_SPECIAL_CAST: INVOCATION_FLAGS = ...
    """"""
    INVOCATION_FLAGS_NON_W8P_FX_API: INVOCATION_FLAGS = ...
    """"""
    INVOCATION_FLAGS_IS_DELEGATE_CTOR: INVOCATION_FLAGS = ...
    """"""
    INVOCATION_FLAGS_CONTAINS_STACK_POINTERS: INVOCATION_FLAGS = ...
    """"""
    INVOCATION_FLAGS_CONSTRUCTOR_INVOKE: INVOCATION_FLAGS = ...
    """"""

class IReflect:
    """"""

    @property
    def UnderlyingSystemType(self) -> Type:
        """

        :return:
        """
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """

        :param bindingAttr:
        :return:
        """
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param types:
        :param modifiers:
        :return:
        """
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """

        :param bindingAttr:
        :return:
        """
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        returnType: Type,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> PropertyInfo:
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param returnType:
        :param types:
        :param modifiers:
        :return:
        """
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
        modifiers: Array[ParameterModifier],
        culture: CultureInfo,
        namedParameters: Array[str],
    ) -> object:
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :param modifiers:
        :param culture:
        :param namedParameters:
        :return:
        """

class IReflectableType:
    """"""

    def GetTypeInfo(self) -> TypeInfo:
        """

        :return:
        """

class ImageFileMachine(Enum):
    """"""

    I386: ImageFileMachine = ...
    """"""
    ARM: ImageFileMachine = ...
    """"""
    IA64: ImageFileMachine = ...
    """"""
    AMD64: ImageFileMachine = ...
    """"""

class InterfaceMapping(ValueType):
    """"""

    InterfaceMethods: Final[Array[MethodInfo]] = ...
    """
    
    :return: 
    """
    InterfaceType: Final[Type] = ...
    """
    
    :return: 
    """
    TargetMethods: Final[Array[MethodInfo]] = ...
    """
    
    :return: 
    """
    TargetType: Final[Type] = ...
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

class IntrospectionExtensions(ABC, Object):
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
    @classmethod
    def GetTypeInfo(cls, type: Type) -> TypeInfo:
        """

        :param type:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class InvalidFilterCriteriaException(ApplicationException, _Exception, ISerializable):
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

class LoadContext(Enum):
    """"""

    DEFAULT: LoadContext = ...
    """"""
    LOADFROM: LoadContext = ...
    """"""
    UNKNOWN: LoadContext = ...
    """"""
    HOSTED: LoadContext = ...
    """"""

class LoaderAllocator(Object):
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

class LoaderAllocatorScout(Object):
    """"""

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

class LocalVariableInfo(Object):
    """"""

    @property
    def IsPinned(self) -> bool:
        """

        :return:
        """
    @property
    def LocalIndex(self) -> int:
        """

        :return:
        """
    @property
    def LocalType(self) -> Type:
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

class ManifestResourceInfo(Object):
    """"""

    def __init__(
        self,
        containingAssembly: Assembly,
        containingFileName: str,
        resourceLocation: ResourceLocation,
    ):
        """

        :param containingAssembly:
        :param containingFileName:
        :param resourceLocation:
        """
    @property
    def FileName(self) -> str:
        """

        :return:
        """
    @property
    def ReferencedAssembly(self) -> Assembly:
        """

        :return:
        """
    @property
    def ResourceLocation(self) -> ResourceLocation:
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

class MdConstant(ABC, Object):
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
    @classmethod
    def GetValue(
        cls, scope: MetadataImport, token: int, fieldTypeHandle: RuntimeTypeHandle, raw: bool
    ) -> object:
        """

        :param scope:
        :param token:
        :param fieldTypeHandle:
        :param raw:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class MdFieldInfo(
    RuntimeFieldInfo, ICustomAttributeProvider, _FieldInfo, _MemberInfo, ISerializable
):
    """"""

    @property
    def Attributes(self) -> FieldAttributes:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def FieldHandle(self) -> RuntimeFieldHandle:
        """

        :return:
        """
    @property
    def FieldType(self) -> Type:
        """

        :return:
        """
    @property
    def IsAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsInitOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsLiteral(self) -> bool:
        """

        :return:
        """
    @property
    def IsNotSerialized(self) -> bool:
        """

        :return:
        """
    @property
    def IsPinvokeImpl(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityTransparent(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsStatic(self) -> bool:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
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
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
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
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
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
    @overload
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
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetOptionalCustomModifiers(self) -> Array[Type]:
        """

        :return:
        """
    def GetRawConstantValue(self) -> object:
        """

        :return:
        """
    def GetRequiredCustomModifiers(self) -> Array[Type]:
        """

        :return:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    def GetValue(self, obj: object) -> object:
        """

        :param obj:
        :return:
        """
    def GetValueDirect(self, obj: TypedReference) -> object:
        """

        :param obj:
        :return:
        """
    @overload
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
    @overload
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
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def SetValue(self, obj: object, value: object) -> None:
        """

        :param obj:
        :param value:
        """
    @overload
    def SetValue(
        self,
        obj: object,
        value: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        culture: CultureInfo,
    ) -> None:
        """

        :param obj:
        :param value:
        :param invokeAttr:
        :param binder:
        :param culture:
        """
    def SetValueDirect(self, obj: TypedReference, value: object) -> None:
        """

        :param obj:
        :param value:
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
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class MdSigCallingConvention(Enum):
    """"""

    Default: MdSigCallingConvention = ...
    """"""
    C: MdSigCallingConvention = ...
    """"""
    StdCall: MdSigCallingConvention = ...
    """"""
    ThisCall: MdSigCallingConvention = ...
    """"""
    FastCall: MdSigCallingConvention = ...
    """"""
    Vararg: MdSigCallingConvention = ...
    """"""
    Field: MdSigCallingConvention = ...
    """"""
    LocalSig: MdSigCallingConvention = ...
    """"""
    Property: MdSigCallingConvention = ...
    """"""
    Unmgd: MdSigCallingConvention = ...
    """"""
    GenericInst: MdSigCallingConvention = ...
    """"""
    CallConvMask: MdSigCallingConvention = ...
    """"""
    Generic: MdSigCallingConvention = ...
    """"""
    HasThis: MdSigCallingConvention = ...
    """"""
    ExplicitThis: MdSigCallingConvention = ...
    """"""

MemberFilter: Callable[[MemberInfo, object], bool] = ...
"""

:param m: 
:param filterCriteria: 
:return: 
"""

class MemberInfo(ABC, Object, ICustomAttributeProvider, _MemberInfo):
    """"""

    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
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
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
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
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
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
    def __eq__(self, other: MemberInfo) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: MemberInfo) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: MemberInfo, right: MemberInfo) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: MemberInfo, right: MemberInfo) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

class MemberInfoSerializationHolder(Object, IObjectReference, ISerializable):
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
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetRealObject(self, context: StreamingContext) -> object:
        """

        :param context:
        :return:
        """
    @classmethod
    @overload
    def GetSerializationInfo(
        cls,
        info: SerializationInfo,
        name: str,
        reflectedClass: RuntimeType,
        signature: str,
        type: MemberTypes,
    ) -> None:
        """

        :param info:
        :param name:
        :param reflectedClass:
        :param signature:
        :param type:
        """
    @classmethod
    @overload
    def GetSerializationInfo(
        cls,
        info: SerializationInfo,
        name: str,
        reflectedClass: RuntimeType,
        signature: str,
        signature2: str,
        type: MemberTypes,
        genericArguments: Array[Type],
    ) -> None:
        """

        :param info:
        :param name:
        :param reflectedClass:
        :param signature:
        :param signature2:
        :param type:
        :param genericArguments:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class MemberTypes(Enum):
    """"""

    Constructor: MemberTypes = ...
    """"""
    Event: MemberTypes = ...
    """"""
    Field: MemberTypes = ...
    """"""
    Method: MemberTypes = ...
    """"""
    Property: MemberTypes = ...
    """"""
    TypeInfo: MemberTypes = ...
    """"""
    Custom: MemberTypes = ...
    """"""
    NestedType: MemberTypes = ...
    """"""
    All: MemberTypes = ...
    """"""

class MetadataEnumResult(ValueType):
    """"""

    @property
    def Item(self) -> int:
        """

        :return:
        """
    @property
    def Length(self) -> int:
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
    def __getitem__(self, index: int) -> int:
        """

        :param index:
        :return:
        """

    class smallResulte__FixedBuffer(ValueType):
        """"""

        FixedElementField: Final[int] = ...
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

class MetadataException(Exception, _Exception, ISerializable):
    """"""

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

class MetadataImport(ValueType):
    """"""

    def Enum(
        self, type: MetadataTokenType, parent: int, result: MetadataEnumResult
    ) -> Tuple[None, MetadataEnumResult]:
        """

        :param type:
        :param parent:
        :param result:
        """
    def EnumCustomAttributes(
        self, mdToken: int, result: MetadataEnumResult
    ) -> Tuple[None, MetadataEnumResult]:
        """

        :param mdToken:
        :param result:
        """
    def EnumEvents(
        self, mdTypeDef: int, result: MetadataEnumResult
    ) -> Tuple[None, MetadataEnumResult]:
        """

        :param mdTypeDef:
        :param result:
        """
    def EnumFields(
        self, mdTypeDef: int, result: MetadataEnumResult
    ) -> Tuple[None, MetadataEnumResult]:
        """

        :param mdTypeDef:
        :param result:
        """
    def EnumNestedTypes(
        self, mdTypeDef: int, result: MetadataEnumResult
    ) -> Tuple[None, MetadataEnumResult]:
        """

        :param mdTypeDef:
        :param result:
        """
    def EnumParams(
        self, mdMethodDef: int, result: MetadataEnumResult
    ) -> Tuple[None, MetadataEnumResult]:
        """

        :param mdMethodDef:
        :param result:
        """
    def EnumProperties(
        self, mdTypeDef: int, result: MetadataEnumResult
    ) -> Tuple[None, MetadataEnumResult]:
        """

        :param mdTypeDef:
        :param result:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def GetClassLayout(
        self, typeTokenDef: int, packSize: int, classSize: int
    ) -> Tuple[None, int, int]:
        """

        :param typeTokenDef:
        :param packSize:
        :param classSize:
        """
    def GetCustomAttributeProps(
        self, customAttributeToken: int, constructorToken: int, signature: ConstArray
    ) -> Tuple[None, int, ConstArray]:
        """

        :param customAttributeToken:
        :param constructorToken:
        :param signature:
        """
    def GetDefaultValue(
        self, mdToken: int, value: int, length: int, corElementType: CorElementType
    ) -> Tuple[str, int, int, CorElementType]:
        """

        :param mdToken:
        :param value:
        :param length:
        :param corElementType:
        :return:
        """
    def GetEventProps(
        self, mdToken: int, name: None, eventAttributes: EventAttributes
    ) -> Tuple[None, None, EventAttributes]:
        """

        :param mdToken:
        :param name:
        :param eventAttributes:
        """
    def GetFieldDefProps(
        self, mdToken: int, fieldAttributes: FieldAttributes
    ) -> Tuple[None, FieldAttributes]:
        """

        :param mdToken:
        :param fieldAttributes:
        """
    def GetFieldMarshal(self, fieldToken: int) -> ConstArray:
        """

        :param fieldToken:
        :return:
        """
    def GetFieldOffset(
        self, typeTokenDef: int, fieldTokenDef: int, offset: int
    ) -> Tuple[bool, int]:
        """

        :param typeTokenDef:
        :param fieldTokenDef:
        :param offset:
        :return:
        """
    def GetGenericParamProps(
        self, genericParameter: int, attributes: GenericParameterAttributes
    ) -> Tuple[None, GenericParameterAttributes]:
        """

        :param genericParameter:
        :param attributes:
        """
    def GetHashCode(self) -> int:
        """

        :return:
        """
    def GetMemberRefProps(self, memberTokenRef: int) -> ConstArray:
        """

        :param memberTokenRef:
        :return:
        """
    def GetMethodSignature(self, token: MetadataToken) -> ConstArray:
        """

        :param token:
        :return:
        """
    def GetName(self, mdToken: int) -> Utf8String:
        """

        :param mdToken:
        :return:
        """
    def GetNamespace(self, mdToken: int) -> Utf8String:
        """

        :param mdToken:
        :return:
        """
    def GetPInvokeMap(
        self, token: int, attributes: PInvokeAttributes, importName: str, importDll: str
    ) -> Tuple[None, PInvokeAttributes, str, str]:
        """

        :param token:
        :param attributes:
        :param importName:
        :param importDll:
        """
    def GetParamDefProps(
        self, parameterToken: int, sequence: int, attributes: ParameterAttributes
    ) -> Tuple[None, int, ParameterAttributes]:
        """

        :param parameterToken:
        :param sequence:
        :param attributes:
        """
    def GetParentToken(self, tkToken: int) -> int:
        """

        :param tkToken:
        :return:
        """
    def GetPropertyProps(
        self,
        mdToken: int,
        name: None,
        propertyAttributes: PropertyAttributes,
        signature: ConstArray,
    ) -> Tuple[None, None, PropertyAttributes, ConstArray]:
        """

        :param mdToken:
        :param name:
        :param propertyAttributes:
        :param signature:
        """
    def GetScopeProps(self, mvid: Guid) -> Tuple[None, Guid]:
        """

        :param mvid:
        """
    def GetSigOfFieldDef(self, fieldToken: int) -> ConstArray:
        """

        :param fieldToken:
        :return:
        """
    def GetSigOfMethodDef(self, methodToken: int) -> ConstArray:
        """

        :param methodToken:
        :return:
        """
    def GetSignatureFromToken(self, token: int) -> ConstArray:
        """

        :param token:
        :return:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def GetUserString(self, mdToken: int) -> str:
        """

        :param mdToken:
        :return:
        """
    def IsValidToken(self, token: int) -> bool:
        """

        :param token:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class MetadataToken(ValueType):
    """"""

    Value: Final[int] = ...
    """
    
    :return: 
    """
    def __init__(self, token: int):
        """

        :param token:
        """
    @property
    def IsAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsEvent(self) -> bool:
        """

        :return:
        """
    @property
    def IsFieldDef(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericPar(self) -> bool:
        """

        :return:
        """
    @property
    def IsGlobalTypeDefToken(self) -> bool:
        """

        :return:
        """
    @property
    def IsMemberRef(self) -> bool:
        """

        :return:
        """
    @property
    def IsMethodDef(self) -> bool:
        """

        :return:
        """
    @property
    def IsMethodSpec(self) -> bool:
        """

        :return:
        """
    @property
    def IsModule(self) -> bool:
        """

        :return:
        """
    @property
    def IsParamDef(self) -> bool:
        """

        :return:
        """
    @property
    def IsProperty(self) -> bool:
        """

        :return:
        """
    @property
    def IsSignature(self) -> bool:
        """

        :return:
        """
    @property
    def IsString(self) -> bool:
        """

        :return:
        """
    @property
    def IsTypeDef(self) -> bool:
        """

        :return:
        """
    @property
    def IsTypeRef(self) -> bool:
        """

        :return:
        """
    @property
    def IsTypeSpec(self) -> bool:
        """

        :return:
        """
    @property
    def TokenType(self) -> MetadataTokenType:
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
    @classmethod
    def IsNullToken(cls, token: int) -> bool:
        """

        :param token:
        :return:
        """
    @classmethod
    def IsTokenOfType(cls, token: int, types: Array[MetadataTokenType]) -> bool:
        """

        :param token:
        :param types:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    @overload
    def op_Implicit(cls, token: MetadataToken) -> int:
        """

        :param token:
        :return:
        """
    @classmethod
    @overload
    def op_Implicit(cls, token: int) -> MetadataToken:
        """

        :param token:
        :return:
        """

class MetadataTokenType(Enum):
    """"""

    Module: MetadataTokenType = ...
    """"""
    TypeRef: MetadataTokenType = ...
    """"""
    TypeDef: MetadataTokenType = ...
    """"""
    FieldDef: MetadataTokenType = ...
    """"""
    MethodDef: MetadataTokenType = ...
    """"""
    ParamDef: MetadataTokenType = ...
    """"""
    InterfaceImpl: MetadataTokenType = ...
    """"""
    MemberRef: MetadataTokenType = ...
    """"""
    CustomAttribute: MetadataTokenType = ...
    """"""
    Permission: MetadataTokenType = ...
    """"""
    Signature: MetadataTokenType = ...
    """"""
    Event: MetadataTokenType = ...
    """"""
    Property: MetadataTokenType = ...
    """"""
    ModuleRef: MetadataTokenType = ...
    """"""
    TypeSpec: MetadataTokenType = ...
    """"""
    Assembly: MetadataTokenType = ...
    """"""
    AssemblyRef: MetadataTokenType = ...
    """"""
    File: MetadataTokenType = ...
    """"""
    ExportedType: MetadataTokenType = ...
    """"""
    ManifestResource: MetadataTokenType = ...
    """"""
    GenericPar: MetadataTokenType = ...
    """"""
    MethodSpec: MetadataTokenType = ...
    """"""
    String: MetadataTokenType = ...
    """"""
    Name: MetadataTokenType = ...
    """"""
    BaseType: MetadataTokenType = ...
    """"""
    Invalid: MetadataTokenType = ...
    """"""

class MethodAttributes(Enum):
    """"""

    ReuseSlot: MethodAttributes = ...
    """"""
    PrivateScope: MethodAttributes = ...
    """"""
    Private: MethodAttributes = ...
    """"""
    FamANDAssem: MethodAttributes = ...
    """"""
    Assembly: MethodAttributes = ...
    """"""
    Family: MethodAttributes = ...
    """"""
    FamORAssem: MethodAttributes = ...
    """"""
    Public: MethodAttributes = ...
    """"""
    MemberAccessMask: MethodAttributes = ...
    """"""
    UnmanagedExport: MethodAttributes = ...
    """"""
    Static: MethodAttributes = ...
    """"""
    Final: MethodAttributes = ...
    """"""
    Virtual: MethodAttributes = ...
    """"""
    HideBySig: MethodAttributes = ...
    """"""
    NewSlot: MethodAttributes = ...
    """"""
    VtableLayoutMask: MethodAttributes = ...
    """"""
    CheckAccessOnOverride: MethodAttributes = ...
    """"""
    Abstract: MethodAttributes = ...
    """"""
    SpecialName: MethodAttributes = ...
    """"""
    RTSpecialName: MethodAttributes = ...
    """"""
    PinvokeImpl: MethodAttributes = ...
    """"""
    HasSecurity: MethodAttributes = ...
    """"""
    RequireSecObject: MethodAttributes = ...
    """"""
    ReservedMask: MethodAttributes = ...
    """"""

class MethodBase(ABC, MemberInfo, ICustomAttributeProvider, _MemberInfo, _MethodBase):
    """"""

    @property
    def Attributes(self) -> MethodAttributes:
        """

        :return:
        """
    @property
    def CallingConvention(self) -> CallingConventions:
        """

        :return:
        """
    @property
    def ContainsGenericParameters(self) -> bool:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def IsAbstract(self) -> bool:
        """

        :return:
        """
    @property
    def IsAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsConstructor(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFinal(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericMethod(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericMethodDefinition(self) -> bool:
        """

        :return:
        """
    @property
    def IsHideBySig(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityTransparent(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsStatic(self) -> bool:
        """

        :return:
        """
    @property
    def IsVirtual(self) -> bool:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """

        :return:
        """
    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
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
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def GetCurrentMethod(cls) -> MethodBase:
        """

        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    def GetGenericArguments(self) -> Array[Type]:
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
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
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
    @overload
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
    def GetMethodBody(self) -> MethodBody:
        """

        :return:
        """
    @classmethod
    @overload
    def GetMethodFromHandle(cls, handle: RuntimeMethodHandle) -> MethodBase:
        """

        :param handle:
        :return:
        """
    @classmethod
    @overload
    def GetMethodFromHandle(
        cls, handle: RuntimeMethodHandle, declaringType: RuntimeTypeHandle
    ) -> MethodBase:
        """

        :param handle:
        :param declaringType:
        :return:
        """
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    def GetParameters(self) -> Array[ParameterInfo]:
        """

        :return:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """

        :param obj:
        :param parameters:
        :return:
        """
    @overload
    def Invoke(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param obj:
        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
    @overload
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
    @overload
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
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
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
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    def __eq__(self, other: MethodBase) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: MethodBase) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: MethodBase, right: MethodBase) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: MethodBase, right: MethodBase) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

class MethodBody(Object):
    """"""

    @property
    def ExceptionHandlingClauses(self) -> IList[ExceptionHandlingClause]:
        """

        :return:
        """
    @property
    def InitLocals(self) -> bool:
        """

        :return:
        """
    @property
    def LocalSignatureMetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def LocalVariables(self) -> IList[LocalVariableInfo]:
        """

        :return:
        """
    @property
    def MaxStackSize(self) -> int:
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
    def GetILAsByteArray(self) -> Array[int]:
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

class MethodImplAttributes(Enum):
    """"""

    IL: MethodImplAttributes = ...
    """"""
    Managed: MethodImplAttributes = ...
    """"""
    Native: MethodImplAttributes = ...
    """"""
    OPTIL: MethodImplAttributes = ...
    """"""
    Runtime: MethodImplAttributes = ...
    """"""
    CodeTypeMask: MethodImplAttributes = ...
    """"""
    Unmanaged: MethodImplAttributes = ...
    """"""
    ManagedMask: MethodImplAttributes = ...
    """"""
    NoInlining: MethodImplAttributes = ...
    """"""
    ForwardRef: MethodImplAttributes = ...
    """"""
    Synchronized: MethodImplAttributes = ...
    """"""
    NoOptimization: MethodImplAttributes = ...
    """"""
    PreserveSig: MethodImplAttributes = ...
    """"""
    AggressiveInlining: MethodImplAttributes = ...
    """"""
    SecurityMitigations: MethodImplAttributes = ...
    """"""
    InternalCall: MethodImplAttributes = ...
    """"""
    MaxMethodImplVal: MethodImplAttributes = ...
    """"""

class MethodInfo(ABC, MethodBase, ICustomAttributeProvider, _MemberInfo, _MethodBase, _MethodInfo):
    """"""

    @property
    def Attributes(self) -> MethodAttributes:
        """

        :return:
        """
    @property
    def Attributes(self) -> MethodAttributes:
        """

        :return:
        """
    @property
    def CallingConvention(self) -> CallingConventions:
        """

        :return:
        """
    @property
    def CallingConvention(self) -> CallingConventions:
        """

        :return:
        """
    @property
    def ContainsGenericParameters(self) -> bool:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def IsAbstract(self) -> bool:
        """

        :return:
        """
    @property
    def IsAbstract(self) -> bool:
        """

        :return:
        """
    @property
    def IsAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsConstructor(self) -> bool:
        """

        :return:
        """
    @property
    def IsConstructor(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFinal(self) -> bool:
        """

        :return:
        """
    @property
    def IsFinal(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericMethod(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericMethodDefinition(self) -> bool:
        """

        :return:
        """
    @property
    def IsHideBySig(self) -> bool:
        """

        :return:
        """
    @property
    def IsHideBySig(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityTransparent(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsStatic(self) -> bool:
        """

        :return:
        """
    @property
    def IsStatic(self) -> bool:
        """

        :return:
        """
    @property
    def IsVirtual(self) -> bool:
        """

        :return:
        """
    @property
    def IsVirtual(self) -> bool:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """

        :return:
        """
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """

        :return:
        """
    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReturnParameter(self) -> ParameterInfo:
        """

        :return:
        """
    @property
    def ReturnType(self) -> Type:
        """

        :return:
        """
    @property
    def ReturnTypeCustomAttributes(self) -> ICustomAttributeProvider:
        """

        :return:
        """
    @overload
    def CreateDelegate(self, delegateType: Type) -> Delegate:
        """

        :param delegateType:
        :return:
        """
    @overload
    def CreateDelegate(self, delegateType: Type, target: object) -> Delegate:
        """

        :param delegateType:
        :param target:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    def GetBaseDefinition(self) -> MethodInfo:
        """

        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    def GetGenericArguments(self) -> Array[Type]:
        """

        :return:
        """
    def GetGenericMethodDefinition(self) -> MethodInfo:
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
    @overload
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
    @overload
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
    def GetMethodBody(self) -> MethodBody:
        """

        :return:
        """
    @overload
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    @overload
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    @overload
    def GetParameters(self) -> Array[ParameterInfo]:
        """

        :return:
        """
    @overload
    def GetParameters(self) -> Array[ParameterInfo]:
        """

        :return:
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
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """

        :param obj:
        :param parameters:
        :return:
        """
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """

        :param obj:
        :param parameters:
        :return:
        """
    @overload
    def Invoke(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param obj:
        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
    @overload
    def Invoke(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param obj:
        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
    @overload
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
    @overload
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
    @overload
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
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def MakeGenericMethod(self, typeArguments: Array[Type]) -> MethodInfo:
        """

        :param typeArguments:
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
    def __eq__(self, other: MethodInfo) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: MethodInfo) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: MethodInfo, right: MethodInfo) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: MethodInfo, right: MethodInfo) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

class MethodSemanticsAttributes(Enum):
    """"""

    Setter: MethodSemanticsAttributes = ...
    """"""
    Getter: MethodSemanticsAttributes = ...
    """"""
    Other: MethodSemanticsAttributes = ...
    """"""
    AddOn: MethodSemanticsAttributes = ...
    """"""
    RemoveOn: MethodSemanticsAttributes = ...
    """"""
    Fire: MethodSemanticsAttributes = ...
    """"""

class Missing(Object, ISerializable):
    """"""

    Value: Final[ClassVar[Missing]] = ...
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
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class Module(ABC, Object, ICustomAttributeProvider, _Module, ISerializable):
    """"""

    FilterTypeName: Final[ClassVar[TypeFilter]] = ...
    """
    
    :return: 
    """
    FilterTypeNameIgnoreCase: Final[ClassVar[TypeFilter]] = ...
    """
    
    :return: 
    """
    @property
    def Assembly(self) -> Assembly:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def FullyQualifiedName(self) -> str:
        """

        :return:
        """
    @property
    def MDStreamVersion(self) -> int:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def ModuleHandle(self) -> ModuleHandle:
        """

        :return:
        """
    @property
    def ModuleVersionId(self) -> Guid:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ScopeName(self) -> str:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FindTypes(self, filter: TypeFilter, filterCriteria: object) -> Array[Type]:
        """

        :param filter:
        :param filterCriteria:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    @overload
    def GetField(self, name: str) -> FieldInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetFields(self) -> Array[FieldInfo]:
        """

        :return:
        """
    @overload
    def GetFields(self, bindingFlags: BindingFlags) -> Array[FieldInfo]:
        """

        :param bindingFlags:
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
    @overload
    def GetMethod(self, name: str) -> MethodInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetMethod(self, name: str, types: Array[Type]) -> MethodInfo:
        """

        :param name:
        :param types:
        :return:
        """
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        callConvention: CallingConventions,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param callConvention:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetMethods(self) -> Array[MethodInfo]:
        """

        :return:
        """
    @overload
    def GetMethods(self, bindingFlags: BindingFlags) -> Array[MethodInfo]:
        """

        :param bindingFlags:
        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetPEKind(
        self, peKind: PortableExecutableKinds, machine: ImageFileMachine
    ) -> Tuple[None, PortableExecutableKinds, ImageFileMachine]:
        """

        :param peKind:
        :param machine:
        """
    def GetSignerCertificate(self) -> X509Certificate:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self, className: str) -> Type:
        """

        :param className:
        :return:
        """
    @overload
    def GetType(self, className: str, ignoreCase: bool) -> Type:
        """

        :param className:
        :param ignoreCase:
        :return:
        """
    @overload
    def GetType(self, className: str, throwOnError: bool, ignoreCase: bool) -> Type:
        """

        :param className:
        :param throwOnError:
        :param ignoreCase:
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
    def GetTypes(self) -> Array[Type]:
        """

        :return:
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
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def IsResource(self) -> bool:
        """

        :return:
        """
    @overload
    def ResolveField(self, metadataToken: int) -> FieldInfo:
        """

        :param metadataToken:
        :return:
        """
    @overload
    def ResolveField(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> FieldInfo:
        """

        :param metadataToken:
        :param genericTypeArguments:
        :param genericMethodArguments:
        :return:
        """
    @overload
    def ResolveMember(self, metadataToken: int) -> MemberInfo:
        """

        :param metadataToken:
        :return:
        """
    @overload
    def ResolveMember(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> MemberInfo:
        """

        :param metadataToken:
        :param genericTypeArguments:
        :param genericMethodArguments:
        :return:
        """
    @overload
    def ResolveMethod(self, metadataToken: int) -> MethodBase:
        """

        :param metadataToken:
        :return:
        """
    @overload
    def ResolveMethod(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> MethodBase:
        """

        :param metadataToken:
        :param genericTypeArguments:
        :param genericMethodArguments:
        :return:
        """
    def ResolveSignature(self, metadataToken: int) -> Array[int]:
        """

        :param metadataToken:
        :return:
        """
    def ResolveString(self, metadataToken: int) -> str:
        """

        :param metadataToken:
        :return:
        """
    @overload
    def ResolveType(self, metadataToken: int) -> Type:
        """

        :param metadataToken:
        :return:
        """
    @overload
    def ResolveType(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> Type:
        """

        :param metadataToken:
        :param genericTypeArguments:
        :param genericMethodArguments:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    def __eq__(self, other: Module) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: Module) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: Module, right: Module) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: Module, right: Module) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

ModuleResolveEventHandler: Callable[[object, ResolveEventArgs], Module] = ...
"""

:param sender: 
:param e: 
:return: 
"""

class ObfuscateAssemblyAttribute(Attribute, _Attribute):
    """"""

    def __init__(self, assemblyIsPrivate: bool):
        """

        :param assemblyIsPrivate:
        """
    @property
    def AssemblyIsPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def StripAfterObfuscation(self) -> bool:
        """

        :return:
        """
    @StripAfterObfuscation.setter
    def StripAfterObfuscation(self, value: bool) -> None: ...
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

class ObfuscationAttribute(Attribute, _Attribute):
    """"""

    def __init__(self):
        """"""
    @property
    def ApplyToMembers(self) -> bool:
        """

        :return:
        """
    @ApplyToMembers.setter
    def ApplyToMembers(self, value: bool) -> None: ...
    @property
    def Exclude(self) -> bool:
        """

        :return:
        """
    @Exclude.setter
    def Exclude(self, value: bool) -> None: ...
    @property
    def Feature(self) -> str:
        """

        :return:
        """
    @Feature.setter
    def Feature(self, value: str) -> None: ...
    @property
    def StripAfterObfuscation(self) -> bool:
        """

        :return:
        """
    @StripAfterObfuscation.setter
    def StripAfterObfuscation(self, value: bool) -> None: ...
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

class PInvokeAttributes(Enum):
    """"""

    ThrowOnUnmappableCharUseAssem: PInvokeAttributes = ...
    """"""
    CharSetNotSpec: PInvokeAttributes = ...
    """"""
    BestFitUseAssem: PInvokeAttributes = ...
    """"""
    NoMangle: PInvokeAttributes = ...
    """"""
    CharSetAnsi: PInvokeAttributes = ...
    """"""
    CharSetUnicode: PInvokeAttributes = ...
    """"""
    CharSetAuto: PInvokeAttributes = ...
    """"""
    CharSetMask: PInvokeAttributes = ...
    """"""
    BestFitEnabled: PInvokeAttributes = ...
    """"""
    BestFitDisabled: PInvokeAttributes = ...
    """"""
    BestFitMask: PInvokeAttributes = ...
    """"""
    SupportsLastError: PInvokeAttributes = ...
    """"""
    CallConvWinapi: PInvokeAttributes = ...
    """"""
    CallConvCdecl: PInvokeAttributes = ...
    """"""
    CallConvStdcall: PInvokeAttributes = ...
    """"""
    CallConvThiscall: PInvokeAttributes = ...
    """"""
    CallConvFastcall: PInvokeAttributes = ...
    """"""
    CallConvMask: PInvokeAttributes = ...
    """"""
    ThrowOnUnmappableCharEnabled: PInvokeAttributes = ...
    """"""
    ThrowOnUnmappableCharDisabled: PInvokeAttributes = ...
    """"""
    ThrowOnUnmappableCharMask: PInvokeAttributes = ...
    """"""
    MaxValue: PInvokeAttributes = ...
    """"""

class ParameterAttributes(Enum):
    """"""

    _None: ParameterAttributes = ...
    """"""
    In: ParameterAttributes = ...
    """"""
    Out: ParameterAttributes = ...
    """"""
    Lcid: ParameterAttributes = ...
    """"""
    Retval: ParameterAttributes = ...
    """"""
    Optional: ParameterAttributes = ...
    """"""
    HasDefault: ParameterAttributes = ...
    """"""
    HasFieldMarshal: ParameterAttributes = ...
    """"""
    Reserved3: ParameterAttributes = ...
    """"""
    Reserved4: ParameterAttributes = ...
    """"""
    ReservedMask: ParameterAttributes = ...
    """"""

class ParameterInfo(Object, ICustomAttributeProvider, _ParameterInfo, IObjectReference):
    """"""

    @property
    def Attributes(self) -> ParameterAttributes:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DefaultValue(self) -> object:
        """

        :return:
        """
    @property
    def HasDefaultValue(self) -> bool:
        """

        :return:
        """
    @property
    def IsIn(self) -> bool:
        """

        :return:
        """
    @property
    def IsLcid(self) -> bool:
        """

        :return:
        """
    @property
    def IsOptional(self) -> bool:
        """

        :return:
        """
    @property
    def IsOut(self) -> bool:
        """

        :return:
        """
    @property
    def IsRetval(self) -> bool:
        """

        :return:
        """
    @property
    def Member(self) -> MemberInfo:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ParameterType(self) -> Type:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @property
    def RawDefaultValue(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

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
    def GetOptionalCustomModifiers(self) -> Array[Type]:
        """

        :return:
        """
    def GetRealObject(self, context: StreamingContext) -> object:
        """

        :param context:
        :return:
        """
    def GetRequiredCustomModifiers(self) -> Array[Type]:
        """

        :return:
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
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ParameterModifier(ValueType):
    """"""

    def __init__(self, parameterCount: int):
        """

        :param parameterCount:
        """
    @property
    def Item(self) -> bool:
        """

        :return:
        """
    @Item.setter
    def Item(self, value: bool) -> None: ...
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
    def __getitem__(self, index: int) -> bool:
        """

        :param index:
        :return:
        """
    def __setitem__(self, index: int, value: bool) -> None:
        """

        :param index:
        :param value:
        """

class Pointer(Object, ISerializable):
    """"""

    @classmethod
    def Box(cls, ptr: None, type: Type) -> object:
        """

        :param ptr:
        :param type:
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
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """
    @classmethod
    def Unbox(cls, ptr: object) -> None:
        """

        :param ptr:
        """

class PortableExecutableKinds(Enum):
    """"""

    NotAPortableExecutableImage: PortableExecutableKinds = ...
    """"""
    ILOnly: PortableExecutableKinds = ...
    """"""
    Required32Bit: PortableExecutableKinds = ...
    """"""
    PE32Plus: PortableExecutableKinds = ...
    """"""
    Unmanaged32Bit: PortableExecutableKinds = ...
    """"""
    Preferred32Bit: PortableExecutableKinds = ...
    """"""

class ProcessorArchitecture(Enum):
    """"""

    _None: ProcessorArchitecture = ...
    """"""
    MSIL: ProcessorArchitecture = ...
    """"""
    X86: ProcessorArchitecture = ...
    """"""
    IA64: ProcessorArchitecture = ...
    """"""
    Amd64: ProcessorArchitecture = ...
    """"""
    Arm: ProcessorArchitecture = ...
    """"""

class PropertyAttributes(Enum):
    """"""

    _None: PropertyAttributes = ...
    """"""
    SpecialName: PropertyAttributes = ...
    """"""
    RTSpecialName: PropertyAttributes = ...
    """"""
    HasDefault: PropertyAttributes = ...
    """"""
    Reserved2: PropertyAttributes = ...
    """"""
    Reserved3: PropertyAttributes = ...
    """"""
    Reserved4: PropertyAttributes = ...
    """"""
    ReservedMask: PropertyAttributes = ...
    """"""

class PropertyInfo(ABC, MemberInfo, ICustomAttributeProvider, _MemberInfo, _PropertyInfo):
    """"""

    @property
    def Attributes(self) -> PropertyAttributes:
        """

        :return:
        """
    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def GetMethod(self) -> MethodInfo:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def PropertyType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def SetMethod(self) -> MethodInfo:
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
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def GetAccessors(self) -> Array[MethodInfo]:
        """

        :return:
        """
    @overload
    def GetAccessors(self, nonPublic: bool) -> Array[MethodInfo]:
        """

        :param nonPublic:
        :return:
        """
    def GetConstantValue(self) -> object:
        """

        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    @overload
    def GetGetMethod(self) -> MethodInfo:
        """

        :return:
        """
    @overload
    def GetGetMethod(self, nonPublic: bool) -> MethodInfo:
        """

        :param nonPublic:
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
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
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
    @overload
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
    def GetIndexParameters(self) -> Array[ParameterInfo]:
        """

        :return:
        """
    def GetOptionalCustomModifiers(self) -> Array[Type]:
        """

        :return:
        """
    def GetRawConstantValue(self) -> object:
        """

        :return:
        """
    def GetRequiredCustomModifiers(self) -> Array[Type]:
        """

        :return:
        """
    @overload
    def GetSetMethod(self) -> MethodInfo:
        """

        :return:
        """
    @overload
    def GetSetMethod(self, nonPublic: bool) -> MethodInfo:
        """

        :param nonPublic:
        :return:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetValue(self, obj: object) -> object:
        """

        :param obj:
        :return:
        """
    @overload
    def GetValue(self, obj: object, index: Array[object]) -> object:
        """

        :param obj:
        :param index:
        :return:
        """
    @overload
    def GetValue(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        index: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param obj:
        :param invokeAttr:
        :param binder:
        :param index:
        :param culture:
        :return:
        """
    @overload
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
    @overload
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
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def SetValue(self, obj: object, value: object) -> None:
        """

        :param obj:
        :param value:
        """
    @overload
    def SetValue(self, obj: object, value: object, index: Array[object]) -> None:
        """

        :param obj:
        :param value:
        :param index:
        """
    @overload
    def SetValue(
        self,
        obj: object,
        value: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        index: Array[object],
        culture: CultureInfo,
    ) -> None:
        """

        :param obj:
        :param value:
        :param invokeAttr:
        :param binder:
        :param index:
        :param culture:
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
    @overload
    def ToString(self) -> str:
        """

        :return:
        """
    def __eq__(self, other: PropertyInfo) -> bool:
        """

        :param other:
        :return:
        """
    def __ne__(self, other: PropertyInfo) -> bool:
        """

        :param other:
        :return:
        """
    @classmethod
    def op_Equality(cls, left: PropertyInfo, right: PropertyInfo) -> bool:
        """

        :param left:
        :param right:
        :return:
        """
    @classmethod
    def op_Inequality(cls, left: PropertyInfo, right: PropertyInfo) -> bool:
        """

        :param left:
        :param right:
        :return:
        """

class PseudoCustomAttribute(ABC, Object):
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

class ReflectionContext(ABC, Object):
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
    def GetTypeForObject(self, value: object) -> TypeInfo:
        """

        :param value:
        :return:
        """
    def MapAssembly(self, assembly: Assembly) -> Assembly:
        """

        :param assembly:
        :return:
        """
    def MapType(self, type: TypeInfo) -> TypeInfo:
        """

        :param type:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class ReflectionTypeLoadException(SystemException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self, classes: Array[Type], exceptions: Array[Exception]):
        """

        :param classes:
        :param exceptions:
        """
    @overload
    def __init__(self, classes: Array[Type], exceptions: Array[Exception], message: str):
        """

        :param classes:
        :param exceptions:
        :param message:
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
    def LoaderExceptions(self) -> Array[Exception]:
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
    @property
    def Types(self) -> Array[Type]:
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

class ResourceAttributes(Enum):
    """"""

    Public: ResourceAttributes = ...
    """"""
    Private: ResourceAttributes = ...
    """"""

class ResourceLocation(Enum):
    """"""

    Embedded: ResourceLocation = ...
    """"""
    ContainedInAnotherAssembly: ResourceLocation = ...
    """"""
    ContainedInManifestFile: ResourceLocation = ...
    """"""

class RtFieldInfo(
    RuntimeFieldInfo,
    ICustomAttributeProvider,
    _FieldInfo,
    _MemberInfo,
    ISerializable,
    IRuntimeFieldInfo,
):
    """"""

    @property
    def Attributes(self) -> FieldAttributes:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def FieldHandle(self) -> RuntimeFieldHandle:
        """

        :return:
        """
    @property
    def FieldType(self) -> Type:
        """

        :return:
        """
    @property
    def IsAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsInitOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsLiteral(self) -> bool:
        """

        :return:
        """
    @property
    def IsNotSerialized(self) -> bool:
        """

        :return:
        """
    @property
    def IsPinvokeImpl(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityTransparent(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsStatic(self) -> bool:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def Value(self) -> RuntimeFieldHandleInternal:
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
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
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
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
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
    @overload
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
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetOptionalCustomModifiers(self) -> Array[Type]:
        """

        :return:
        """
    def GetRawConstantValue(self) -> object:
        """

        :return:
        """
    def GetRequiredCustomModifiers(self) -> Array[Type]:
        """

        :return:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    def GetValue(self, obj: object) -> object:
        """

        :param obj:
        :return:
        """
    def GetValueDirect(self, obj: TypedReference) -> object:
        """

        :param obj:
        :return:
        """
    @overload
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
    @overload
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
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def SetValue(self, obj: object, value: object) -> None:
        """

        :param obj:
        :param value:
        """
    @overload
    def SetValue(
        self,
        obj: object,
        value: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        culture: CultureInfo,
    ) -> None:
        """

        :param obj:
        :param value:
        :param invokeAttr:
        :param binder:
        :param culture:
        """
    def SetValueDirect(self, obj: TypedReference, value: object) -> None:
        """

        :param obj:
        :param value:
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
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class RuntimeAssembly(
    Assembly,
    ICustomAttributeProvider,
    ICustomQueryInterface,
    _Assembly,
    ISerializable,
    IEvidenceFactory,
):
    """"""

    @property
    def CodeBase(self) -> str:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DefinedTypes(self) -> IEnumerable[TypeInfo]:
        """

        :return:
        """
    @property
    def EntryPoint(self) -> MethodInfo:
        """

        :return:
        """
    @property
    def EscapedCodeBase(self) -> str:
        """

        :return:
        """
    @property
    def Evidence(self) -> Evidence:
        """

        :return:
        """
    @property
    def Evidence(self) -> Evidence:
        """

        :return:
        """
    @property
    def ExportedTypes(self) -> IEnumerable[Type]:
        """

        :return:
        """
    @property
    def FullName(self) -> str:
        """

        :return:
        """
    @property
    def GlobalAssemblyCache(self) -> bool:
        """

        :return:
        """
    @property
    def HostContext(self) -> int:
        """

        :return:
        """
    @property
    def ImageRuntimeVersion(self) -> str:
        """

        :return:
        """
    @property
    def IsDynamic(self) -> bool:
        """

        :return:
        """
    @property
    def IsFullyTrusted(self) -> bool:
        """

        :return:
        """
    @property
    def Location(self) -> str:
        """

        :return:
        """
    @property
    def ManifestModule(self) -> Module:
        """

        :return:
        """
    @property
    def Modules(self) -> IEnumerable[Module]:
        """

        :return:
        """
    @property
    def PermissionSet(self) -> PermissionSet:
        """

        :return:
        """
    @property
    def ReflectionOnly(self) -> bool:
        """

        :return:
        """
    @property
    def SecurityRuleSet(self) -> SecurityRuleSet:
        """

        :return:
        """
    @overload
    def CreateInstance(self, typeName: str) -> object:
        """

        :param typeName:
        :return:
        """
    @overload
    def CreateInstance(self, typeName: str, ignoreCase: bool) -> object:
        """

        :param typeName:
        :param ignoreCase:
        :return:
        """
    @overload
    def CreateInstance(
        self,
        typeName: str,
        ignoreCase: bool,
        bindingAttr: BindingFlags,
        binder: Binder,
        args: Array[object],
        culture: CultureInfo,
        activationAttributes: Array[object],
    ) -> object:
        """

        :param typeName:
        :param ignoreCase:
        :param bindingAttr:
        :param binder:
        :param args:
        :param culture:
        :param activationAttributes:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    def GetExportedTypes(self) -> Array[Type]:
        """

        :return:
        """
    def GetFile(self, name: str) -> FileStream:
        """

        :param name:
        :return:
        """
    @overload
    def GetFiles(self) -> Array[FileStream]:
        """

        :return:
        """
    @overload
    def GetFiles(self, getResourceModules: bool) -> Array[FileStream]:
        """

        :param getResourceModules:
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
    def GetInterface(self, iid: Guid, ppv: IntPtr) -> Tuple[CustomQueryInterfaceResult, IntPtr]:
        """

        :param iid:
        :param ppv:
        :return:
        """
    @overload
    def GetLoadedModules(self) -> Array[Module]:
        """

        :return:
        """
    @overload
    def GetLoadedModules(self, getResourceModules: bool) -> Array[Module]:
        """

        :param getResourceModules:
        :return:
        """
    def GetManifestResourceInfo(self, resourceName: str) -> ManifestResourceInfo:
        """

        :param resourceName:
        :return:
        """
    def GetManifestResourceNames(self) -> Array[str]:
        """

        :return:
        """
    @overload
    def GetManifestResourceStream(self, name: str) -> Stream:
        """

        :param name:
        :return:
        """
    @overload
    def GetManifestResourceStream(self, type: Type, name: str) -> Stream:
        """

        :param type:
        :param name:
        :return:
        """
    def GetModule(self, name: str) -> Module:
        """

        :param name:
        :return:
        """
    @overload
    def GetModules(self) -> Array[Module]:
        """

        :return:
        """
    @overload
    def GetModules(self, getResourceModules: bool) -> Array[Module]:
        """

        :param getResourceModules:
        :return:
        """
    @overload
    def GetName(self) -> AssemblyName:
        """

        :return:
        """
    @overload
    def GetName(self, copiedName: bool) -> AssemblyName:
        """

        :param copiedName:
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
    def GetReferencedAssemblies(self) -> Array[AssemblyName]:
        """

        :return:
        """
    @overload
    def GetSatelliteAssembly(self, culture: CultureInfo) -> Assembly:
        """

        :param culture:
        :return:
        """
    @overload
    def GetSatelliteAssembly(self, culture: CultureInfo, version: Version) -> Assembly:
        """

        :param culture:
        :param version:
        :return:
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
    def GetType(self, name: str) -> Type:
        """

        :param name:
        :return:
        """
    @overload
    def GetType(self, name: str, throwOnError: bool) -> Type:
        """

        :param name:
        :param throwOnError:
        :return:
        """
    @overload
    def GetType(self, name: str, throwOnError: bool, ignoreCase: bool) -> Type:
        """

        :param name:
        :param throwOnError:
        :param ignoreCase:
        :return:
        """
    def GetTypes(self) -> Array[Type]:
        """

        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def LoadModule(self, moduleName: str, rawModule: Array[int]) -> Module:
        """

        :param moduleName:
        :param rawModule:
        :return:
        """
    @overload
    def LoadModule(
        self, moduleName: str, rawModule: Array[int], rawSymbolStore: Array[int]
    ) -> Module:
        """

        :param moduleName:
        :param rawModule:
        :param rawSymbolStore:
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
    ModuleResolve: EventType[ModuleResolveEventHandler] = ...
    """"""

class RuntimeConstructorInfo(
    ConstructorInfo,
    ICustomAttributeProvider,
    _ConstructorInfo,
    _MemberInfo,
    _MethodBase,
    ISerializable,
    IRuntimeMethodInfo,
):
    """"""

    @property
    def Attributes(self) -> MethodAttributes:
        """

        :return:
        """
    @property
    def Attributes(self) -> MethodAttributes:
        """

        :return:
        """
    @property
    def CallingConvention(self) -> CallingConventions:
        """

        :return:
        """
    @property
    def CallingConvention(self) -> CallingConventions:
        """

        :return:
        """
    @property
    def ContainsGenericParameters(self) -> bool:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def IsAbstract(self) -> bool:
        """

        :return:
        """
    @property
    def IsAbstract(self) -> bool:
        """

        :return:
        """
    @property
    def IsAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsConstructor(self) -> bool:
        """

        :return:
        """
    @property
    def IsConstructor(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFinal(self) -> bool:
        """

        :return:
        """
    @property
    def IsFinal(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericMethod(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericMethodDefinition(self) -> bool:
        """

        :return:
        """
    @property
    def IsHideBySig(self) -> bool:
        """

        :return:
        """
    @property
    def IsHideBySig(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityTransparent(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsStatic(self) -> bool:
        """

        :return:
        """
    @property
    def IsStatic(self) -> bool:
        """

        :return:
        """
    @property
    def IsVirtual(self) -> bool:
        """

        :return:
        """
    @property
    def IsVirtual(self) -> bool:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """

        :return:
        """
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """

        :return:
        """
    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def Value(self) -> RuntimeMethodHandleInternal:
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
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    def GetGenericArguments(self) -> Array[Type]:
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
    @overload
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
    @overload
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
    def GetMethodBody(self) -> MethodBody:
        """

        :return:
        """
    @overload
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    @overload
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetParameters(self) -> Array[ParameterInfo]:
        """

        :return:
        """
    @overload
    def GetParameters(self) -> Array[ParameterInfo]:
        """

        :return:
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
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def Invoke(self, parameters: Array[object]) -> object:
        """

        :param parameters:
        :return:
        """
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """

        :param obj:
        :param parameters:
        :return:
        """
    @overload
    def Invoke(
        self,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
    @overload
    def Invoke(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param obj:
        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
    @overload
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
    @overload
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
    @overload
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
    def Invoke_2(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param obj:
        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
    def Invoke_3(self, obj: object, parameters: Array[object]) -> object:
        """

        :param obj:
        :param parameters:
        :return:
        """
    def Invoke_4(
        self,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
    def Invoke_5(self, parameters: Array[object]) -> object:
        """

        :param parameters:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
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

class RuntimeEventInfo(EventInfo, ICustomAttributeProvider, _EventInfo, _MemberInfo, ISerializable):
    """"""

    @property
    def AddMethod(self) -> MethodInfo:
        """

        :return:
        """
    @property
    def Attributes(self) -> EventAttributes:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def EventHandlerType(self) -> Type:
        """

        :return:
        """
    @property
    def IsMulticast(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def RaiseMethod(self) -> MethodInfo:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def RemoveMethod(self) -> MethodInfo:
        """

        :return:
        """
    def AddEventHandler(self, target: object, handler: Delegate) -> None:
        """

        :param target:
        :param handler:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def GetAddMethod(self) -> MethodInfo:
        """

        :return:
        """
    @overload
    def GetAddMethod(self, nonPublic: bool) -> MethodInfo:
        """

        :param nonPublic:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
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
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
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
    @overload
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
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetOtherMethods(self) -> Array[MethodInfo]:
        """

        :return:
        """
    @overload
    def GetOtherMethods(self, nonPublic: bool) -> Array[MethodInfo]:
        """

        :param nonPublic:
        :return:
        """
    @overload
    def GetRaiseMethod(self) -> MethodInfo:
        """

        :return:
        """
    @overload
    def GetRaiseMethod(self, nonPublic: bool) -> MethodInfo:
        """

        :param nonPublic:
        :return:
        """
    @overload
    def GetRemoveMethod(self) -> MethodInfo:
        """

        :return:
        """
    @overload
    def GetRemoveMethod(self, nonPublic: bool) -> MethodInfo:
        """

        :param nonPublic:
        :return:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
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
    @overload
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
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def RemoveEventHandler(self, target: object, handler: Delegate) -> None:
        """

        :param target:
        :param handler:
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
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class RuntimeFieldInfo(
    ABC, FieldInfo, ICustomAttributeProvider, _FieldInfo, _MemberInfo, ISerializable
):
    """"""

    @property
    def Attributes(self) -> FieldAttributes:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def FieldHandle(self) -> RuntimeFieldHandle:
        """

        :return:
        """
    @property
    def FieldType(self) -> Type:
        """

        :return:
        """
    @property
    def IsAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsInitOnly(self) -> bool:
        """

        :return:
        """
    @property
    def IsLiteral(self) -> bool:
        """

        :return:
        """
    @property
    def IsNotSerialized(self) -> bool:
        """

        :return:
        """
    @property
    def IsPinvokeImpl(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityTransparent(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsStatic(self) -> bool:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
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
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
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
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
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
    @overload
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
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetOptionalCustomModifiers(self) -> Array[Type]:
        """

        :return:
        """
    def GetRawConstantValue(self) -> object:
        """

        :return:
        """
    def GetRequiredCustomModifiers(self) -> Array[Type]:
        """

        :return:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    def GetValue(self, obj: object) -> object:
        """

        :param obj:
        :return:
        """
    def GetValueDirect(self, obj: TypedReference) -> object:
        """

        :param obj:
        :return:
        """
    @overload
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
    @overload
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
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def SetValue(self, obj: object, value: object) -> None:
        """

        :param obj:
        :param value:
        """
    @overload
    def SetValue(
        self,
        obj: object,
        value: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        culture: CultureInfo,
    ) -> None:
        """

        :param obj:
        :param value:
        :param invokeAttr:
        :param binder:
        :param culture:
        """
    def SetValueDirect(self, obj: TypedReference, value: object) -> None:
        """

        :param obj:
        :param value:
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
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class RuntimeMethodInfo(
    MethodInfo,
    ICustomAttributeProvider,
    _MemberInfo,
    _MethodBase,
    _MethodInfo,
    ISerializable,
    IRuntimeMethodInfo,
):
    """"""

    @property
    def Attributes(self) -> MethodAttributes:
        """

        :return:
        """
    @property
    def Attributes(self) -> MethodAttributes:
        """

        :return:
        """
    @property
    def CallingConvention(self) -> CallingConventions:
        """

        :return:
        """
    @property
    def CallingConvention(self) -> CallingConventions:
        """

        :return:
        """
    @property
    def ContainsGenericParameters(self) -> bool:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def IsAbstract(self) -> bool:
        """

        :return:
        """
    @property
    def IsAbstract(self) -> bool:
        """

        :return:
        """
    @property
    def IsAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsConstructor(self) -> bool:
        """

        :return:
        """
    @property
    def IsConstructor(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsFinal(self) -> bool:
        """

        :return:
        """
    @property
    def IsFinal(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericMethod(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericMethodDefinition(self) -> bool:
        """

        :return:
        """
    @property
    def IsHideBySig(self) -> bool:
        """

        :return:
        """
    @property
    def IsHideBySig(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityTransparent(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsStatic(self) -> bool:
        """

        :return:
        """
    @property
    def IsStatic(self) -> bool:
        """

        :return:
        """
    @property
    def IsVirtual(self) -> bool:
        """

        :return:
        """
    @property
    def IsVirtual(self) -> bool:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """

        :return:
        """
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """

        :return:
        """
    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReturnParameter(self) -> ParameterInfo:
        """

        :return:
        """
    @property
    def ReturnType(self) -> Type:
        """

        :return:
        """
    @property
    def ReturnTypeCustomAttributes(self) -> ICustomAttributeProvider:
        """

        :return:
        """
    @property
    def Value(self) -> RuntimeMethodHandleInternal:
        """

        :return:
        """
    @overload
    def CreateDelegate(self, delegateType: Type) -> Delegate:
        """

        :param delegateType:
        :return:
        """
    @overload
    def CreateDelegate(self, delegateType: Type, target: object) -> Delegate:
        """

        :param delegateType:
        :param target:
        :return:
        """
    @overload
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    def GetBaseDefinition(self) -> MethodInfo:
        """

        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    def GetGenericArguments(self) -> Array[Type]:
        """

        :return:
        """
    def GetGenericMethodDefinition(self) -> MethodInfo:
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
    @overload
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
    @overload
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
    def GetMethodBody(self) -> MethodBody:
        """

        :return:
        """
    @overload
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    @overload
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """

        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    @overload
    def GetParameters(self) -> Array[ParameterInfo]:
        """

        :return:
        """
    @overload
    def GetParameters(self) -> Array[ParameterInfo]:
        """

        :return:
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
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """

        :param obj:
        :param parameters:
        :return:
        """
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """

        :param obj:
        :param parameters:
        :return:
        """
    @overload
    def Invoke(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param obj:
        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
    @overload
    def Invoke(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param obj:
        :param invokeAttr:
        :param binder:
        :param parameters:
        :param culture:
        :return:
        """
    @overload
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
    @overload
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
    @overload
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
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def MakeGenericMethod(self, typeArguments: Array[Type]) -> MethodInfo:
        """

        :param typeArguments:
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

class RuntimeModule(Module, ICustomAttributeProvider, _Module, ISerializable):
    """"""

    @property
    def Assembly(self) -> Assembly:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def FullyQualifiedName(self) -> str:
        """

        :return:
        """
    @property
    def MDStreamVersion(self) -> int:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def ModuleHandle(self) -> ModuleHandle:
        """

        :return:
        """
    @property
    def ModuleVersionId(self) -> Guid:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ScopeName(self) -> str:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FindTypes(self, filter: TypeFilter, filterCriteria: object) -> Array[Type]:
        """

        :param filter:
        :param filterCriteria:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    @overload
    def GetField(self, name: str) -> FieldInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetFields(self) -> Array[FieldInfo]:
        """

        :return:
        """
    @overload
    def GetFields(self, bindingFlags: BindingFlags) -> Array[FieldInfo]:
        """

        :param bindingFlags:
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
    @overload
    def GetMethod(self, name: str) -> MethodInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetMethod(self, name: str, types: Array[Type]) -> MethodInfo:
        """

        :param name:
        :param types:
        :return:
        """
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        callConvention: CallingConventions,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param callConvention:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetMethods(self) -> Array[MethodInfo]:
        """

        :return:
        """
    @overload
    def GetMethods(self, bindingFlags: BindingFlags) -> Array[MethodInfo]:
        """

        :param bindingFlags:
        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetPEKind(
        self, peKind: PortableExecutableKinds, machine: ImageFileMachine
    ) -> Tuple[None, PortableExecutableKinds, ImageFileMachine]:
        """

        :param peKind:
        :param machine:
        """
    def GetSignerCertificate(self) -> X509Certificate:
        """

        :return:
        """
    @overload
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetType(self, className: str) -> Type:
        """

        :param className:
        :return:
        """
    @overload
    def GetType(self, className: str, ignoreCase: bool) -> Type:
        """

        :param className:
        :param ignoreCase:
        :return:
        """
    @overload
    def GetType(self, className: str, throwOnError: bool, ignoreCase: bool) -> Type:
        """

        :param className:
        :param throwOnError:
        :param ignoreCase:
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
    def GetTypes(self) -> Array[Type]:
        """

        :return:
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
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def IsResource(self) -> bool:
        """

        :return:
        """
    @overload
    def ResolveField(self, metadataToken: int) -> FieldInfo:
        """

        :param metadataToken:
        :return:
        """
    @overload
    def ResolveField(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> FieldInfo:
        """

        :param metadataToken:
        :param genericTypeArguments:
        :param genericMethodArguments:
        :return:
        """
    @overload
    def ResolveMember(self, metadataToken: int) -> MemberInfo:
        """

        :param metadataToken:
        :return:
        """
    @overload
    def ResolveMember(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> MemberInfo:
        """

        :param metadataToken:
        :param genericTypeArguments:
        :param genericMethodArguments:
        :return:
        """
    @overload
    def ResolveMethod(self, metadataToken: int) -> MethodBase:
        """

        :param metadataToken:
        :return:
        """
    @overload
    def ResolveMethod(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> MethodBase:
        """

        :param metadataToken:
        :param genericTypeArguments:
        :param genericMethodArguments:
        :return:
        """
    def ResolveSignature(self, metadataToken: int) -> Array[int]:
        """

        :param metadataToken:
        :return:
        """
    def ResolveString(self, metadataToken: int) -> str:
        """

        :param metadataToken:
        :return:
        """
    @overload
    def ResolveType(self, metadataToken: int) -> Type:
        """

        :param metadataToken:
        :return:
        """
    @overload
    def ResolveType(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> Type:
        """

        :param metadataToken:
        :param genericTypeArguments:
        :param genericMethodArguments:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class RuntimeParameterInfo(
    ParameterInfo, ICustomAttributeProvider, _ParameterInfo, IObjectReference, ISerializable
):
    """"""

    @property
    def Attributes(self) -> ParameterAttributes:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DefaultValue(self) -> object:
        """

        :return:
        """
    @property
    def HasDefaultValue(self) -> bool:
        """

        :return:
        """
    @property
    def IsIn(self) -> bool:
        """

        :return:
        """
    @property
    def IsLcid(self) -> bool:
        """

        :return:
        """
    @property
    def IsOptional(self) -> bool:
        """

        :return:
        """
    @property
    def IsOut(self) -> bool:
        """

        :return:
        """
    @property
    def IsRetval(self) -> bool:
        """

        :return:
        """
    @property
    def Member(self) -> MemberInfo:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def ParameterType(self) -> Type:
        """

        :return:
        """
    @property
    def Position(self) -> int:
        """

        :return:
        """
    @property
    def RawDefaultValue(self) -> object:
        """

        :return:
        """
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

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
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetOptionalCustomModifiers(self) -> Array[Type]:
        """

        :return:
        """
    def GetRealObject(self, context: StreamingContext) -> object:
        """

        :param context:
        :return:
        """
    def GetRequiredCustomModifiers(self) -> Array[Type]:
        """

        :return:
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
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class RuntimePropertyInfo(
    PropertyInfo, ICustomAttributeProvider, _MemberInfo, _PropertyInfo, ISerializable
):
    """"""

    @property
    def Attributes(self) -> PropertyAttributes:
        """

        :return:
        """
    @property
    def CanRead(self) -> bool:
        """

        :return:
        """
    @property
    def CanWrite(self) -> bool:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def GetMethod(self) -> MethodInfo:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def PropertyType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def SetMethod(self) -> MethodInfo:
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
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def GetAccessors(self) -> Array[MethodInfo]:
        """

        :return:
        """
    @overload
    def GetAccessors(self, nonPublic: bool) -> Array[MethodInfo]:
        """

        :param nonPublic:
        :return:
        """
    def GetConstantValue(self) -> object:
        """

        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    @overload
    def GetGetMethod(self) -> MethodInfo:
        """

        :return:
        """
    @overload
    def GetGetMethod(self, nonPublic: bool) -> MethodInfo:
        """

        :param nonPublic:
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
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
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
    @overload
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
    def GetIndexParameters(self) -> Array[ParameterInfo]:
        """

        :return:
        """
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetOptionalCustomModifiers(self) -> Array[Type]:
        """

        :return:
        """
    def GetRawConstantValue(self) -> object:
        """

        :return:
        """
    def GetRequiredCustomModifiers(self) -> Array[Type]:
        """

        :return:
        """
    @overload
    def GetSetMethod(self) -> MethodInfo:
        """

        :return:
        """
    @overload
    def GetSetMethod(self, nonPublic: bool) -> MethodInfo:
        """

        :param nonPublic:
        :return:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetValue(self, obj: object) -> object:
        """

        :param obj:
        :return:
        """
    @overload
    def GetValue(self, obj: object, index: Array[object]) -> object:
        """

        :param obj:
        :param index:
        :return:
        """
    @overload
    def GetValue(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        index: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param obj:
        :param invokeAttr:
        :param binder:
        :param index:
        :param culture:
        :return:
        """
    @overload
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
    @overload
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
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def SetValue(self, obj: object, value: object) -> None:
        """

        :param obj:
        :param value:
        """
    @overload
    def SetValue(self, obj: object, value: object, index: Array[object]) -> None:
        """

        :param obj:
        :param value:
        :param index:
        """
    @overload
    def SetValue(
        self,
        obj: object,
        value: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        index: Array[object],
        culture: CultureInfo,
    ) -> None:
        """

        :param obj:
        :param value:
        :param invokeAttr:
        :param binder:
        :param index:
        :param culture:
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
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class RuntimeReflectionExtensions(ABC, Object):
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
    @classmethod
    def GetMethodInfo(cls, _del: Delegate) -> MethodInfo:
        """

        :param _del:
        :return:
        """
    @classmethod
    def GetRuntimeBaseDefinition(cls, method: MethodInfo) -> MethodInfo:
        """

        :param method:
        :return:
        """
    @classmethod
    def GetRuntimeEvent(cls, type: Type, name: str) -> EventInfo:
        """

        :param type:
        :param name:
        :return:
        """
    @classmethod
    def GetRuntimeEvents(cls, type: Type) -> IEnumerable[EventInfo]:
        """

        :param type:
        :return:
        """
    @classmethod
    def GetRuntimeField(cls, type: Type, name: str) -> FieldInfo:
        """

        :param type:
        :param name:
        :return:
        """
    @classmethod
    def GetRuntimeFields(cls, type: Type) -> IEnumerable[FieldInfo]:
        """

        :param type:
        :return:
        """
    @classmethod
    def GetRuntimeInterfaceMap(cls, typeInfo: TypeInfo, interfaceType: Type) -> InterfaceMapping:
        """

        :param typeInfo:
        :param interfaceType:
        :return:
        """
    @classmethod
    def GetRuntimeMethod(cls, type: Type, name: str, parameters: Array[Type]) -> MethodInfo:
        """

        :param type:
        :param name:
        :param parameters:
        :return:
        """
    @classmethod
    def GetRuntimeMethods(cls, type: Type) -> IEnumerable[MethodInfo]:
        """

        :param type:
        :return:
        """
    @classmethod
    def GetRuntimeProperties(cls, type: Type) -> IEnumerable[PropertyInfo]:
        """

        :param type:
        :return:
        """
    @classmethod
    def GetRuntimeProperty(cls, type: Type, name: str) -> PropertyInfo:
        """

        :param type:
        :param name:
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

class SecurityContextFrame(ValueType):
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
    def Pop(self) -> None:
        """"""
    def Push(self, assembly: RuntimeAssembly) -> None:
        """

        :param assembly:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class StrongNameKeyPair(Object, IDeserializationCallback, ISerializable):
    """"""

    @overload
    def __init__(self, keyPairFile: FileStream):
        """

        :param keyPairFile:
        """
    @overload
    def __init__(self, keyPairArray: Array[int]):
        """

        :param keyPairArray:
        """
    @overload
    def __init__(self, keyPairContainer: str):
        """

        :param keyPairContainer:
        """
    @property
    def PublicKey(self) -> Array[int]:
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
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """

        :param info:
        :param context:
        """
    def GetType(self) -> Type:
        """

        :return:
        """
    def OnDeserialization(self, sender: object) -> None:
        """

        :param sender:
        """
    def ToString(self) -> str:
        """

        :return:
        """

class TargetException(ApplicationException, _Exception, ISerializable):
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

class TargetInvocationException(ApplicationException, _Exception, ISerializable):
    """"""

    @overload
    def __init__(self, inner: Exception):
        """

        :param inner:
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

class TargetParameterCountException(ApplicationException, _Exception, ISerializable):
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

class Throw(ABC, Object):
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

class TypeAttributes(Enum):
    """"""

    NotPublic: TypeAttributes = ...
    """"""
    AutoLayout: TypeAttributes = ...
    """"""
    AnsiClass: TypeAttributes = ...
    """"""
    Class: TypeAttributes = ...
    """"""
    Public: TypeAttributes = ...
    """"""
    NestedPublic: TypeAttributes = ...
    """"""
    NestedPrivate: TypeAttributes = ...
    """"""
    NestedFamily: TypeAttributes = ...
    """"""
    NestedAssembly: TypeAttributes = ...
    """"""
    NestedFamANDAssem: TypeAttributes = ...
    """"""
    NestedFamORAssem: TypeAttributes = ...
    """"""
    VisibilityMask: TypeAttributes = ...
    """"""
    SequentialLayout: TypeAttributes = ...
    """"""
    ExplicitLayout: TypeAttributes = ...
    """"""
    LayoutMask: TypeAttributes = ...
    """"""
    Interface: TypeAttributes = ...
    """"""
    ClassSemanticsMask: TypeAttributes = ...
    """"""
    Abstract: TypeAttributes = ...
    """"""
    Sealed: TypeAttributes = ...
    """"""
    SpecialName: TypeAttributes = ...
    """"""
    RTSpecialName: TypeAttributes = ...
    """"""
    Import: TypeAttributes = ...
    """"""
    Serializable: TypeAttributes = ...
    """"""
    WindowsRuntime: TypeAttributes = ...
    """"""
    UnicodeClass: TypeAttributes = ...
    """"""
    AutoClass: TypeAttributes = ...
    """"""
    StringFormatMask: TypeAttributes = ...
    """"""
    CustomFormatClass: TypeAttributes = ...
    """"""
    HasSecurity: TypeAttributes = ...
    """"""
    ReservedMask: TypeAttributes = ...
    """"""
    BeforeFieldInit: TypeAttributes = ...
    """"""
    CustomFormatMask: TypeAttributes = ...
    """"""

class TypeDelegator(
    TypeInfo, ICustomAttributeProvider, IReflect, IReflectableType, _MemberInfo, _Type
):
    """"""

    def __init__(self, delegatingType: Type):
        """

        :param delegatingType:
        """
    @property
    def Assembly(self) -> Assembly:
        """

        :return:
        """
    @property
    def AssemblyQualifiedName(self) -> str:
        """

        :return:
        """
    @property
    def Attributes(self) -> TypeAttributes:
        """

        :return:
        """
    @property
    def BaseType(self) -> Type:
        """

        :return:
        """
    @property
    def ContainsGenericParameters(self) -> bool:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaredConstructors(self) -> IEnumerable[ConstructorInfo]:
        """

        :return:
        """
    @property
    def DeclaredEvents(self) -> IEnumerable[EventInfo]:
        """

        :return:
        """
    @property
    def DeclaredFields(self) -> IEnumerable[FieldInfo]:
        """

        :return:
        """
    @property
    def DeclaredMembers(self) -> IEnumerable[MemberInfo]:
        """

        :return:
        """
    @property
    def DeclaredMethods(self) -> IEnumerable[MethodInfo]:
        """

        :return:
        """
    @property
    def DeclaredNestedTypes(self) -> IEnumerable[TypeInfo]:
        """

        :return:
        """
    @property
    def DeclaredProperties(self) -> IEnumerable[PropertyInfo]:
        """

        :return:
        """
    @property
    def DeclaringMethod(self) -> MethodBase:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @classmethod
    @property
    def DefaultBinder(cls) -> Binder:
        """

        :return:
        """
    @property
    def FullName(self) -> str:
        """

        :return:
        """
    @property
    def GUID(self) -> Guid:
        """

        :return:
        """
    @property
    def GenericParameterAttributes(self) -> GenericParameterAttributes:
        """

        :return:
        """
    @property
    def GenericParameterPosition(self) -> int:
        """

        :return:
        """
    @property
    def GenericTypeArguments(self) -> Array[Type]:
        """

        :return:
        """
    @property
    def GenericTypeParameters(self) -> Array[Type]:
        """

        :return:
        """
    @property
    def HasElementType(self) -> bool:
        """

        :return:
        """
    @property
    def ImplementedInterfaces(self) -> IEnumerable[Type]:
        """

        :return:
        """
    @property
    def IsAbstract(self) -> bool:
        """

        :return:
        """
    @property
    def IsAnsiClass(self) -> bool:
        """

        :return:
        """
    @property
    def IsArray(self) -> bool:
        """

        :return:
        """
    @property
    def IsAutoClass(self) -> bool:
        """

        :return:
        """
    @property
    def IsAutoLayout(self) -> bool:
        """

        :return:
        """
    @property
    def IsByRef(self) -> bool:
        """

        :return:
        """
    @property
    def IsCOMObject(self) -> bool:
        """

        :return:
        """
    @property
    def IsClass(self) -> bool:
        """

        :return:
        """
    @property
    def IsConstructedGenericType(self) -> bool:
        """

        :return:
        """
    @property
    def IsContextful(self) -> bool:
        """

        :return:
        """
    @property
    def IsEnum(self) -> bool:
        """

        :return:
        """
    @property
    def IsExplicitLayout(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericParameter(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericType(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericTypeDefinition(self) -> bool:
        """

        :return:
        """
    @property
    def IsImport(self) -> bool:
        """

        :return:
        """
    @property
    def IsInterface(self) -> bool:
        """

        :return:
        """
    @property
    def IsLayoutSequential(self) -> bool:
        """

        :return:
        """
    @property
    def IsMarshalByRef(self) -> bool:
        """

        :return:
        """
    @property
    def IsNested(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedFamANDAssem(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedFamORAssem(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsNotPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsPointer(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrimitive(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsSealed(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityTransparent(self) -> bool:
        """

        :return:
        """
    @property
    def IsSerializable(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsUnicodeClass(self) -> bool:
        """

        :return:
        """
    @property
    def IsValueType(self) -> bool:
        """

        :return:
        """
    @property
    def IsVisible(self) -> bool:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Namespace(self) -> str:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def StructLayoutAttribute(self) -> StructLayoutAttribute:
        """

        :return:
        """
    @property
    def TypeHandle(self) -> RuntimeTypeHandle:
        """

        :return:
        """
    @property
    def TypeInitializer(self) -> ConstructorInfo:
        """

        :return:
        """
    @property
    def UnderlyingSystemType(self) -> Type:
        """

        :return:
        """
    @property
    def UnderlyingSystemType(self) -> Type:
        """

        :return:
        """
    def AsType(self) -> Type:
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
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, o: Type) -> bool:
        """

        :param o:
        :return:
        """
    def FindInterfaces(self, filter: TypeFilter, filterCriteria: object) -> Array[Type]:
        """

        :param filter:
        :param filterCriteria:
        :return:
        """
    def FindMembers(
        self,
        memberType: MemberTypes,
        bindingAttr: BindingFlags,
        filter: MemberFilter,
        filterCriteria: object,
    ) -> Array[MemberInfo]:
        """

        :param memberType:
        :param bindingAttr:
        :param filter:
        :param filterCriteria:
        :return:
        """
    def GetArrayRank(self) -> int:
        """

        :return:
        """
    @overload
    def GetConstructor(self, types: Array[Type]) -> ConstructorInfo:
        """

        :param types:
        :return:
        """
    @overload
    def GetConstructor(
        self,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> ConstructorInfo:
        """

        :param bindingAttr:
        :param binder:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetConstructor(
        self,
        bindingAttr: BindingFlags,
        binder: Binder,
        callConvention: CallingConventions,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> ConstructorInfo:
        """

        :param bindingAttr:
        :param binder:
        :param callConvention:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetConstructors(self) -> Array[ConstructorInfo]:
        """

        :return:
        """
    @overload
    def GetConstructors(self, bindingAttr: BindingFlags) -> Array[ConstructorInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    def GetDeclaredEvent(self, name: str) -> EventInfo:
        """

        :param name:
        :return:
        """
    def GetDeclaredField(self, name: str) -> FieldInfo:
        """

        :param name:
        :return:
        """
    def GetDeclaredMethod(self, name: str) -> MethodInfo:
        """

        :param name:
        :return:
        """
    def GetDeclaredMethods(self, name: str) -> IEnumerable[MethodInfo]:
        """

        :param name:
        :return:
        """
    def GetDeclaredNestedType(self, name: str) -> TypeInfo:
        """

        :param name:
        :return:
        """
    def GetDeclaredProperty(self, name: str) -> PropertyInfo:
        """

        :param name:
        :return:
        """
    def GetDefaultMembers(self) -> Array[MemberInfo]:
        """

        :return:
        """
    def GetElementType(self) -> Type:
        """

        :return:
        """
    def GetEnumName(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    def GetEnumNames(self) -> Array[str]:
        """

        :return:
        """
    def GetEnumUnderlyingType(self) -> Type:
        """

        :return:
        """
    def GetEnumValues(self) -> Array:
        """

        :return:
        """
    @overload
    def GetEvent(self, name: str) -> EventInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetEvent(self, name: str, bindingAttr: BindingFlags) -> EventInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetEvents(self) -> Array[EventInfo]:
        """

        :return:
        """
    @overload
    def GetEvents(self, bindingAttr: BindingFlags) -> Array[EventInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetField(self, name: str) -> FieldInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetFields(self) -> Array[FieldInfo]:
        """

        :return:
        """
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """

        :param bindingAttr:
        :return:
        """
    def GetGenericArguments(self) -> Array[Type]:
        """

        :return:
        """
    def GetGenericParameterConstraints(self) -> Array[Type]:
        """

        :return:
        """
    def GetGenericTypeDefinition(self) -> Type:
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
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
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
    @overload
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
    @overload
    def GetInterface(self, name: str) -> Type:
        """

        :param name:
        :return:
        """
    @overload
    def GetInterface(self, name: str, ignoreCase: bool) -> Type:
        """

        :param name:
        :param ignoreCase:
        :return:
        """
    def GetInterfaceMap(self, interfaceType: Type) -> InterfaceMapping:
        """

        :param interfaceType:
        :return:
        """
    def GetInterfaces(self) -> Array[Type]:
        """

        :return:
        """
    @overload
    def GetMember(self, name: str) -> Array[MemberInfo]:
        """

        :param name:
        :return:
        """
    @overload
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMember(
        self, name: str, type: MemberTypes, bindingAttr: BindingFlags
    ) -> Array[MemberInfo]:
        """

        :param name:
        :param type:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMembers(self) -> Array[MemberInfo]:
        """

        :return:
        """
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str) -> MethodInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str, types: Array[Type]) -> MethodInfo:
        """

        :param name:
        :param types:
        :return:
        """
    @overload
    def GetMethod(
        self, name: str, types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> MethodInfo:
        """

        :param name:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        callConvention: CallingConventions,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param callConvention:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetMethods(self) -> Array[MethodInfo]:
        """

        :return:
        """
    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetNestedType(self, name: str) -> Type:
        """

        :param name:
        :return:
        """
    @overload
    def GetNestedType(self, name: str, bindingAttr: BindingFlags) -> Type:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetNestedTypes(self) -> Array[Type]:
        """

        :return:
        """
    @overload
    def GetNestedTypes(self, bindingAttr: BindingFlags) -> Array[Type]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperties(self) -> Array[PropertyInfo]:
        """

        :return:
        """
    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str) -> PropertyInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str, types: Array[Type]) -> PropertyInfo:
        """

        :param name:
        :param types:
        :return:
        """
    @overload
    def GetProperty(self, name: str, returnType: Type) -> PropertyInfo:
        """

        :param name:
        :param returnType:
        :return:
        """
    @overload
    def GetProperty(self, name: str, returnType: Type, types: Array[Type]) -> PropertyInfo:
        """

        :param name:
        :param returnType:
        :param types:
        :return:
        """
    @overload
    def GetProperty(
        self, name: str, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> PropertyInfo:
        """

        :param name:
        :param returnType:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetProperty(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        returnType: Type,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> PropertyInfo:
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param returnType:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetProperty(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        returnType: Type,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> PropertyInfo:
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param returnType:
        :param types:
        :param modifiers:
        :return:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self) -> TypeInfo:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
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
    @overload
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
    @overload
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
    ) -> object:
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :return:
        """
    @overload
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :param culture:
        :return:
        """
    @overload
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
        modifiers: Array[ParameterModifier],
        culture: CultureInfo,
        namedParameters: Array[str],
    ) -> object:
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :param modifiers:
        :param culture:
        :param namedParameters:
        :return:
        """
    @overload
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
        modifiers: Array[ParameterModifier],
        culture: CultureInfo,
        namedParameters: Array[str],
    ) -> object:
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :param modifiers:
        :param culture:
        :param namedParameters:
        :return:
        """
    @overload
    def IsAssignableFrom(self, typeInfo: TypeInfo) -> bool:
        """

        :param typeInfo:
        :return:
        """
    @overload
    def IsAssignableFrom(self, c: Type) -> bool:
        """

        :param c:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def IsEnumDefined(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def IsEquivalentTo(self, other: Type) -> bool:
        """

        :param other:
        :return:
        """
    def IsInstanceOfType(self, o: object) -> bool:
        """

        :param o:
        :return:
        """
    def IsSubclassOf(self, c: Type) -> bool:
        """

        :param c:
        :return:
        """
    @overload
    def MakeArrayType(self) -> Type:
        """

        :return:
        """
    @overload
    def MakeArrayType(self, rank: int) -> Type:
        """

        :param rank:
        :return:
        """
    def MakeByRefType(self) -> Type:
        """

        :return:
        """
    def MakeGenericType(self, typeArguments: Array[Type]) -> Type:
        """

        :param typeArguments:
        :return:
        """
    def MakePointerType(self) -> Type:
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
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

TypeFilter: Callable[[Type, object], bool] = ...
"""

:param m: 
:param filterCriteria: 
:return: 
"""

class TypeInfo(ABC, Type, ICustomAttributeProvider, IReflect, IReflectableType, _MemberInfo, _Type):
    """"""

    @property
    def Assembly(self) -> Assembly:
        """

        :return:
        """
    @property
    def AssemblyQualifiedName(self) -> str:
        """

        :return:
        """
    @property
    def Attributes(self) -> TypeAttributes:
        """

        :return:
        """
    @property
    def BaseType(self) -> Type:
        """

        :return:
        """
    @property
    def ContainsGenericParameters(self) -> bool:
        """

        :return:
        """
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """

        :return:
        """
    @property
    def DeclaredConstructors(self) -> IEnumerable[ConstructorInfo]:
        """

        :return:
        """
    @property
    def DeclaredEvents(self) -> IEnumerable[EventInfo]:
        """

        :return:
        """
    @property
    def DeclaredFields(self) -> IEnumerable[FieldInfo]:
        """

        :return:
        """
    @property
    def DeclaredMembers(self) -> IEnumerable[MemberInfo]:
        """

        :return:
        """
    @property
    def DeclaredMethods(self) -> IEnumerable[MethodInfo]:
        """

        :return:
        """
    @property
    def DeclaredNestedTypes(self) -> IEnumerable[TypeInfo]:
        """

        :return:
        """
    @property
    def DeclaredProperties(self) -> IEnumerable[PropertyInfo]:
        """

        :return:
        """
    @property
    def DeclaringMethod(self) -> MethodBase:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @property
    def DeclaringType(self) -> Type:
        """

        :return:
        """
    @classmethod
    @property
    def DefaultBinder(cls) -> Binder:
        """

        :return:
        """
    @property
    def FullName(self) -> str:
        """

        :return:
        """
    @property
    def GUID(self) -> Guid:
        """

        :return:
        """
    @property
    def GenericParameterAttributes(self) -> GenericParameterAttributes:
        """

        :return:
        """
    @property
    def GenericParameterPosition(self) -> int:
        """

        :return:
        """
    @property
    def GenericTypeArguments(self) -> Array[Type]:
        """

        :return:
        """
    @property
    def GenericTypeParameters(self) -> Array[Type]:
        """

        :return:
        """
    @property
    def HasElementType(self) -> bool:
        """

        :return:
        """
    @property
    def ImplementedInterfaces(self) -> IEnumerable[Type]:
        """

        :return:
        """
    @property
    def IsAbstract(self) -> bool:
        """

        :return:
        """
    @property
    def IsAnsiClass(self) -> bool:
        """

        :return:
        """
    @property
    def IsArray(self) -> bool:
        """

        :return:
        """
    @property
    def IsAutoClass(self) -> bool:
        """

        :return:
        """
    @property
    def IsAutoLayout(self) -> bool:
        """

        :return:
        """
    @property
    def IsByRef(self) -> bool:
        """

        :return:
        """
    @property
    def IsCOMObject(self) -> bool:
        """

        :return:
        """
    @property
    def IsClass(self) -> bool:
        """

        :return:
        """
    @property
    def IsConstructedGenericType(self) -> bool:
        """

        :return:
        """
    @property
    def IsContextful(self) -> bool:
        """

        :return:
        """
    @property
    def IsEnum(self) -> bool:
        """

        :return:
        """
    @property
    def IsExplicitLayout(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericParameter(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericType(self) -> bool:
        """

        :return:
        """
    @property
    def IsGenericTypeDefinition(self) -> bool:
        """

        :return:
        """
    @property
    def IsImport(self) -> bool:
        """

        :return:
        """
    @property
    def IsInterface(self) -> bool:
        """

        :return:
        """
    @property
    def IsLayoutSequential(self) -> bool:
        """

        :return:
        """
    @property
    def IsMarshalByRef(self) -> bool:
        """

        :return:
        """
    @property
    def IsNested(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedAssembly(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedFamANDAssem(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedFamORAssem(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedFamily(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedPrivate(self) -> bool:
        """

        :return:
        """
    @property
    def IsNestedPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsNotPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsPointer(self) -> bool:
        """

        :return:
        """
    @property
    def IsPrimitive(self) -> bool:
        """

        :return:
        """
    @property
    def IsPublic(self) -> bool:
        """

        :return:
        """
    @property
    def IsSealed(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """

        :return:
        """
    @property
    def IsSecurityTransparent(self) -> bool:
        """

        :return:
        """
    @property
    def IsSerializable(self) -> bool:
        """

        :return:
        """
    @property
    def IsSpecialName(self) -> bool:
        """

        :return:
        """
    @property
    def IsUnicodeClass(self) -> bool:
        """

        :return:
        """
    @property
    def IsValueType(self) -> bool:
        """

        :return:
        """
    @property
    def IsVisible(self) -> bool:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MemberType(self) -> MemberTypes:
        """

        :return:
        """
    @property
    def MetadataToken(self) -> int:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Module(self) -> Module:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Name(self) -> str:
        """

        :return:
        """
    @property
    def Namespace(self) -> str:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def ReflectedType(self) -> Type:
        """

        :return:
        """
    @property
    def StructLayoutAttribute(self) -> StructLayoutAttribute:
        """

        :return:
        """
    @property
    def TypeHandle(self) -> RuntimeTypeHandle:
        """

        :return:
        """
    @property
    def TypeInitializer(self) -> ConstructorInfo:
        """

        :return:
        """
    @property
    def UnderlyingSystemType(self) -> Type:
        """

        :return:
        """
    @property
    def UnderlyingSystemType(self) -> Type:
        """

        :return:
        """
    def AsType(self) -> Type:
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
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, other: object) -> bool:
        """

        :param other:
        :return:
        """
    @overload
    def Equals(self, o: Type) -> bool:
        """

        :param o:
        :return:
        """
    def FindInterfaces(self, filter: TypeFilter, filterCriteria: object) -> Array[Type]:
        """

        :param filter:
        :param filterCriteria:
        :return:
        """
    def FindMembers(
        self,
        memberType: MemberTypes,
        bindingAttr: BindingFlags,
        filter: MemberFilter,
        filterCriteria: object,
    ) -> Array[MemberInfo]:
        """

        :param memberType:
        :param bindingAttr:
        :param filter:
        :param filterCriteria:
        :return:
        """
    def GetArrayRank(self) -> int:
        """

        :return:
        """
    @overload
    def GetConstructor(self, types: Array[Type]) -> ConstructorInfo:
        """

        :param types:
        :return:
        """
    @overload
    def GetConstructor(
        self,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> ConstructorInfo:
        """

        :param bindingAttr:
        :param binder:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetConstructor(
        self,
        bindingAttr: BindingFlags,
        binder: Binder,
        callConvention: CallingConventions,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> ConstructorInfo:
        """

        :param bindingAttr:
        :param binder:
        :param callConvention:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetConstructors(self) -> Array[ConstructorInfo]:
        """

        :return:
        """
    @overload
    def GetConstructors(self, bindingAttr: BindingFlags) -> Array[ConstructorInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """

        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """

        :return:
        """
    def GetDeclaredEvent(self, name: str) -> EventInfo:
        """

        :param name:
        :return:
        """
    def GetDeclaredField(self, name: str) -> FieldInfo:
        """

        :param name:
        :return:
        """
    def GetDeclaredMethod(self, name: str) -> MethodInfo:
        """

        :param name:
        :return:
        """
    def GetDeclaredMethods(self, name: str) -> IEnumerable[MethodInfo]:
        """

        :param name:
        :return:
        """
    def GetDeclaredNestedType(self, name: str) -> TypeInfo:
        """

        :param name:
        :return:
        """
    def GetDeclaredProperty(self, name: str) -> PropertyInfo:
        """

        :param name:
        :return:
        """
    def GetDefaultMembers(self) -> Array[MemberInfo]:
        """

        :return:
        """
    def GetElementType(self) -> Type:
        """

        :return:
        """
    def GetEnumName(self, value: object) -> str:
        """

        :param value:
        :return:
        """
    def GetEnumNames(self) -> Array[str]:
        """

        :return:
        """
    def GetEnumUnderlyingType(self) -> Type:
        """

        :return:
        """
    def GetEnumValues(self) -> Array:
        """

        :return:
        """
    @overload
    def GetEvent(self, name: str) -> EventInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetEvent(self, name: str, bindingAttr: BindingFlags) -> EventInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetEvents(self) -> Array[EventInfo]:
        """

        :return:
        """
    @overload
    def GetEvents(self, bindingAttr: BindingFlags) -> Array[EventInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetField(self, name: str) -> FieldInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetFields(self) -> Array[FieldInfo]:
        """

        :return:
        """
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """

        :param bindingAttr:
        :return:
        """
    def GetGenericArguments(self) -> Array[Type]:
        """

        :return:
        """
    def GetGenericParameterConstraints(self) -> Array[Type]:
        """

        :return:
        """
    def GetGenericTypeDefinition(self) -> Type:
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
    def GetHashCode(self) -> int:
        """

        :return:
        """
    @overload
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
    @overload
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
    @overload
    def GetInterface(self, name: str) -> Type:
        """

        :param name:
        :return:
        """
    @overload
    def GetInterface(self, name: str, ignoreCase: bool) -> Type:
        """

        :param name:
        :param ignoreCase:
        :return:
        """
    def GetInterfaceMap(self, interfaceType: Type) -> InterfaceMapping:
        """

        :param interfaceType:
        :return:
        """
    def GetInterfaces(self) -> Array[Type]:
        """

        :return:
        """
    @overload
    def GetMember(self, name: str) -> Array[MemberInfo]:
        """

        :param name:
        :return:
        """
    @overload
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMember(
        self, name: str, type: MemberTypes, bindingAttr: BindingFlags
    ) -> Array[MemberInfo]:
        """

        :param name:
        :param type:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMembers(self) -> Array[MemberInfo]:
        """

        :return:
        """
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str) -> MethodInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethod(self, name: str, types: Array[Type]) -> MethodInfo:
        """

        :param name:
        :param types:
        :return:
        """
    @overload
    def GetMethod(
        self, name: str, types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> MethodInfo:
        """

        :param name:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        callConvention: CallingConventions,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param callConvention:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetMethods(self) -> Array[MethodInfo]:
        """

        :return:
        """
    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetNestedType(self, name: str) -> Type:
        """

        :param name:
        :return:
        """
    @overload
    def GetNestedType(self, name: str, bindingAttr: BindingFlags) -> Type:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetNestedTypes(self) -> Array[Type]:
        """

        :return:
        """
    @overload
    def GetNestedTypes(self, bindingAttr: BindingFlags) -> Array[Type]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperties(self) -> Array[PropertyInfo]:
        """

        :return:
        """
    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """

        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str) -> PropertyInfo:
        """

        :param name:
        :return:
        """
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """

        :param name:
        :param bindingAttr:
        :return:
        """
    @overload
    def GetProperty(self, name: str, types: Array[Type]) -> PropertyInfo:
        """

        :param name:
        :param types:
        :return:
        """
    @overload
    def GetProperty(self, name: str, returnType: Type) -> PropertyInfo:
        """

        :param name:
        :param returnType:
        :return:
        """
    @overload
    def GetProperty(self, name: str, returnType: Type, types: Array[Type]) -> PropertyInfo:
        """

        :param name:
        :param returnType:
        :param types:
        :return:
        """
    @overload
    def GetProperty(
        self, name: str, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> PropertyInfo:
        """

        :param name:
        :param returnType:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetProperty(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        returnType: Type,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> PropertyInfo:
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param returnType:
        :param types:
        :param modifiers:
        :return:
        """
    @overload
    def GetProperty(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        returnType: Type,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> PropertyInfo:
        """

        :param name:
        :param bindingAttr:
        :param binder:
        :param returnType:
        :param types:
        :param modifiers:
        :return:
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
    def GetType(self) -> Type:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self) -> TypeInfo:
        """

        :return:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """

        :param iTInfo:
        :param lcid:
        :param ppTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
    def GetTypeInfoCount(self, pcTInfo: int) -> Tuple[None, int]:
        """

        :param pcTInfo:
        """
    @overload
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
    @overload
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
    @overload
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
    ) -> object:
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :return:
        """
    @overload
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
        culture: CultureInfo,
    ) -> object:
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :param culture:
        :return:
        """
    @overload
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
        modifiers: Array[ParameterModifier],
        culture: CultureInfo,
        namedParameters: Array[str],
    ) -> object:
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :param modifiers:
        :param culture:
        :param namedParameters:
        :return:
        """
    @overload
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
        modifiers: Array[ParameterModifier],
        culture: CultureInfo,
        namedParameters: Array[str],
    ) -> object:
        """

        :param name:
        :param invokeAttr:
        :param binder:
        :param target:
        :param args:
        :param modifiers:
        :param culture:
        :param namedParameters:
        :return:
        """
    @overload
    def IsAssignableFrom(self, typeInfo: TypeInfo) -> bool:
        """

        :param typeInfo:
        :return:
        """
    @overload
    def IsAssignableFrom(self, c: Type) -> bool:
        """

        :param c:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    @overload
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """

        :param attributeType:
        :param inherit:
        :return:
        """
    def IsEnumDefined(self, value: object) -> bool:
        """

        :param value:
        :return:
        """
    def IsEquivalentTo(self, other: Type) -> bool:
        """

        :param other:
        :return:
        """
    def IsInstanceOfType(self, o: object) -> bool:
        """

        :param o:
        :return:
        """
    def IsSubclassOf(self, c: Type) -> bool:
        """

        :param c:
        :return:
        """
    @overload
    def MakeArrayType(self) -> Type:
        """

        :return:
        """
    @overload
    def MakeArrayType(self, rank: int) -> Type:
        """

        :param rank:
        :return:
        """
    def MakeByRefType(self) -> Type:
        """

        :return:
        """
    def MakeGenericType(self, typeArguments: Array[Type]) -> Type:
        """

        :param typeArguments:
        :return:
        """
    def MakePointerType(self) -> Type:
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
    @overload
    def ToString(self) -> str:
        """

        :return:
        """

class __Filters(Object):
    """"""

    def __init__(self):
        """"""
    def Equals(self, obj: object) -> bool:
        """

        :param obj:
        :return:
        """
    def FilterTypeName(self, cls: Type, filterCriteria: object) -> bool:
        """

        :param cls:
        :param filterCriteria:
        :return:
        """
    def FilterTypeNameIgnoreCase(self, cls: Type, filterCriteria: object) -> bool:
        """

        :param cls:
        :param filterCriteria:
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
