"""Automatically generated stubs for C# namespace: System.Reflection."""

from abc import ABC
from collections.abc import Callable
from typing import ClassVar
from typing import Final
from typing import Self
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
from System import Int32
from System import Int64
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
from System import String
from System import SystemException
from System import Type
from System import TypedReference
from System import UInt32
from System import Utf8String
from System import ValueType
from System import Version
from System import Void
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

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AmbiguousMatchException(SystemException, _Exception, ISerializable):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Assembly(ABC, Object, ICustomAttributeProvider, _Assembly, ISerializable, IEvidenceFactory):
    """"""
    @property
    def CodeBase(self) -> str:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DefinedTypes(self) -> IEnumerable[TypeInfo]:
        """"""
    @property
    def EntryPoint(self) -> MethodInfo:
        """"""
    @property
    def EscapedCodeBase(self) -> str:
        """"""
    @property
    def Evidence(self) -> Evidence:
        """"""
    @property
    def ExportedTypes(self) -> IEnumerable[Type]:
        """"""
    @property
    def FullName(self) -> str:
        """"""
    @property
    def GlobalAssemblyCache(self) -> bool:
        """"""
    @property
    def HostContext(self) -> int:
        """"""
    @property
    def ImageRuntimeVersion(self) -> str:
        """"""
    @property
    def IsDynamic(self) -> bool:
        """"""
    @property
    def IsFullyTrusted(self) -> bool:
        """"""
    @property
    def Location(self) -> str:
        """"""
    @property
    def ManifestModule(self) -> Module:
        """"""
    @property
    def Modules(self) -> IEnumerable[Module]:
        """"""
    @property
    def PermissionSet(self) -> PermissionSet:
        """"""
    @property
    def ReflectionOnly(self) -> bool:
        """"""
    @property
    def SecurityRuleSet(self) -> SecurityRuleSet:
        """"""
    @overload
    def CreateInstance(self, typeName: str) -> object:
        """"""
    @overload
    def CreateInstance(self, typeName: str, ignoreCase: bool) -> object:
        """"""
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
        """"""
    @classmethod
    def CreateQualifiedName(cls, assemblyName: str, typeName: str) -> str:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    @classmethod
    def GetAssembly(cls, type: Type) -> Assembly:
        """"""
    @classmethod
    def GetCallingAssembly(cls) -> Assembly:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    @classmethod
    def GetEntryAssembly(cls) -> Assembly:
        """"""
    @classmethod
    def GetExecutingAssembly(cls) -> Assembly:
        """"""
    def GetExportedTypes(self) -> Array[Type]:
        """"""
    def GetFile(self, name: str) -> FileStream:
        """"""
    @overload
    def GetFiles(self) -> Array[FileStream]:
        """"""
    @overload
    def GetFiles(self, getResourceModules: bool) -> Array[FileStream]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetLoadedModules(self) -> Array[Module]:
        """"""
    @overload
    def GetLoadedModules(self, getResourceModules: bool) -> Array[Module]:
        """"""
    def GetManifestResourceInfo(self, resourceName: str) -> ManifestResourceInfo:
        """"""
    def GetManifestResourceNames(self) -> Array[str]:
        """"""
    @overload
    def GetManifestResourceStream(self, name: str) -> Stream:
        """"""
    @overload
    def GetManifestResourceStream(self, type: Type, name: str) -> Stream:
        """"""
    def GetModule(self, name: str) -> Module:
        """"""
    @overload
    def GetModules(self) -> Array[Module]:
        """"""
    @overload
    def GetModules(self, getResourceModules: bool) -> Array[Module]:
        """"""
    @overload
    def GetName(self) -> AssemblyName:
        """"""
    @overload
    def GetName(self, copiedName: bool) -> AssemblyName:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetReferencedAssemblies(self) -> Array[AssemblyName]:
        """"""
    @overload
    def GetSatelliteAssembly(self, culture: CultureInfo) -> Assembly:
        """"""
    @overload
    def GetSatelliteAssembly(self, culture: CultureInfo, version: Version) -> Assembly:
        """"""
    @overload
    def GetType(self) -> Type:
        """"""
    @overload
    def GetType(self, name: str) -> Type:
        """"""
    @overload
    def GetType(self, name: str, throwOnError: bool) -> Type:
        """"""
    @overload
    def GetType(self, name: str, throwOnError: bool, ignoreCase: bool) -> Type:
        """"""
    def GetTypes(self) -> Array[Type]:
        """"""
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    @classmethod
    @overload
    def Load(cls, assemblyRef: AssemblyName) -> Assembly:
        """"""
    @classmethod
    @overload
    def Load(cls, assemblyRef: AssemblyName, assemblySecurity: Evidence) -> Assembly:
        """"""
    @classmethod
    @overload
    def Load(cls, rawAssembly: Array[int]) -> Assembly:
        """"""
    @classmethod
    @overload
    def Load(cls, rawAssembly: Array[int], rawSymbolStore: Array[int]) -> Assembly:
        """"""
    @classmethod
    @overload
    def Load(
        cls, rawAssembly: Array[int], rawSymbolStore: Array[int], securityEvidence: Evidence
    ) -> Assembly:
        """"""
    @classmethod
    @overload
    def Load(
        cls,
        rawAssembly: Array[int],
        rawSymbolStore: Array[int],
        securityContextSource: SecurityContextSource,
    ) -> Assembly:
        """"""
    @classmethod
    @overload
    def Load(cls, assemblyString: str) -> Assembly:
        """"""
    @classmethod
    @overload
    def Load(cls, assemblyString: str, assemblySecurity: Evidence) -> Assembly:
        """"""
    @classmethod
    @overload
    def LoadFile(cls, path: str) -> Assembly:
        """"""
    @classmethod
    @overload
    def LoadFile(cls, path: str, securityEvidence: Evidence) -> Assembly:
        """"""
    @classmethod
    @overload
    def LoadFrom(cls, assemblyFile: str) -> Assembly:
        """"""
    @classmethod
    @overload
    def LoadFrom(cls, assemblyFile: str, securityEvidence: Evidence) -> Assembly:
        """"""
    @classmethod
    @overload
    def LoadFrom(
        cls,
        assemblyFile: str,
        securityEvidence: Evidence,
        hashValue: Array[int],
        hashAlgorithm: AssemblyHashAlgorithm,
    ) -> Assembly:
        """"""
    @classmethod
    @overload
    def LoadFrom(
        cls, assemblyFile: str, hashValue: Array[int], hashAlgorithm: AssemblyHashAlgorithm
    ) -> Assembly:
        """"""
    @overload
    def LoadModule(self, moduleName: str, rawModule: Array[int]) -> Module:
        """"""
    @overload
    def LoadModule(
        self, moduleName: str, rawModule: Array[int], rawSymbolStore: Array[int]
    ) -> Module:
        """"""
    @classmethod
    @overload
    def LoadWithPartialName(cls, partialName: str) -> Assembly:
        """"""
    @classmethod
    @overload
    def LoadWithPartialName(cls, partialName: str, securityEvidence: Evidence) -> Assembly:
        """"""
    @classmethod
    @overload
    def ReflectionOnlyLoad(cls, rawAssembly: Array[int]) -> Assembly:
        """"""
    @classmethod
    @overload
    def ReflectionOnlyLoad(cls, assemblyString: str) -> Assembly:
        """"""
    @classmethod
    def ReflectionOnlyLoadFrom(cls, assemblyFile: str) -> Assembly:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def UnsafeLoadFrom(cls, assemblyFile: str) -> Assembly:
        """"""
    @classmethod
    def op_Equality(cls, left: Assembly, right: Assembly) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: Assembly, right: Assembly) -> bool:
        """"""
    def __eq__(self, other: Assembly) -> bool:
        """"""
    def __ne__(self, other: Assembly) -> bool:
        """"""
    ModuleResolve: EventType[ModuleResolveEventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AssemblyAlgorithmIdAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, algorithmId: AssemblyHashAlgorithm) -> None:
        """"""
    @overload
    def __init__(self, algorithmId: int) -> None:
        """"""
    @property
    def AlgorithmId(self) -> int:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AssemblyCompanyAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, company: str) -> None:
        """"""
    @property
    def Company(self) -> str:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AssemblyConfigurationAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, configuration: str) -> None:
        """"""
    @property
    def Configuration(self) -> str:
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class AssemblyContentType(Enum):
    """"""

    Default: AssemblyContentType = ...
    """"""
    WindowsRuntime: AssemblyContentType = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AssemblyCopyrightAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, copyright: str) -> None:
        """"""
    @property
    def Copyright(self) -> str:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AssemblyCultureAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, culture: str) -> None:
        """"""
    @property
    def Culture(self) -> str:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AssemblyDefaultAliasAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, defaultAlias: str) -> None:
        """"""
    @property
    def DefaultAlias(self) -> str:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AssemblyDelaySignAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, delaySign: bool) -> None:
        """"""
    @property
    def DelaySign(self) -> bool:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AssemblyDescriptionAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, description: str) -> None:
        """"""
    @property
    def Description(self) -> str:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AssemblyFileVersionAttribute(Attribute, _Attribute):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AssemblyFlagsAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, flags: int) -> None:
        """"""
    @overload
    def __init__(self, assemblyFlags: int) -> None:
        """"""
    @overload
    def __init__(self, assemblyFlags: AssemblyNameFlags) -> None:
        """"""
    @property
    def AssemblyFlags(self) -> int:
        """"""
    @property
    def Flags(self) -> int:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AssemblyInformationalVersionAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, informationalVersion: str) -> None:
        """"""
    @property
    def InformationalVersion(self) -> str:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AssemblyKeyFileAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, keyFile: str) -> None:
        """"""
    @property
    def KeyFile(self) -> str:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AssemblyKeyNameAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, keyName: str) -> None:
        """"""
    @property
    def KeyName(self) -> str:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AssemblyMetadataAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, key: str, value: str) -> None:
        """"""
    @property
    def Key(self) -> str:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Value(self) -> str:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AssemblyName(Object, _AssemblyName, IDeserializationCallback, ISerializable, ICloneable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, assemblyName: str) -> None:
        """"""
    @property
    def CodeBase(self) -> str:
        """"""
    @CodeBase.setter
    def CodeBase(self, value: str) -> None: ...
    @property
    def ContentType(self) -> AssemblyContentType:
        """"""
    @ContentType.setter
    def ContentType(self, value: AssemblyContentType) -> None: ...
    @property
    def CultureInfo(self) -> CultureInfo:
        """"""
    @CultureInfo.setter
    def CultureInfo(self, value: CultureInfo) -> None: ...
    @property
    def CultureName(self) -> str:
        """"""
    @CultureName.setter
    def CultureName(self, value: str) -> None: ...
    @property
    def EscapedCodeBase(self) -> str:
        """"""
    @property
    def Flags(self) -> AssemblyNameFlags:
        """"""
    @Flags.setter
    def Flags(self, value: AssemblyNameFlags) -> None: ...
    @property
    def FullName(self) -> str:
        """"""
    @property
    def HashAlgorithm(self) -> AssemblyHashAlgorithm:
        """"""
    @HashAlgorithm.setter
    def HashAlgorithm(self, value: AssemblyHashAlgorithm) -> None: ...
    @property
    def KeyPair(self) -> StrongNameKeyPair:
        """"""
    @KeyPair.setter
    def KeyPair(self, value: StrongNameKeyPair) -> None: ...
    @property
    def Name(self) -> str:
        """"""
    @Name.setter
    def Name(self, value: str) -> None: ...
    @property
    def ProcessorArchitecture(self) -> ProcessorArchitecture:
        """"""
    @ProcessorArchitecture.setter
    def ProcessorArchitecture(self, value: ProcessorArchitecture) -> None: ...
    @property
    def Version(self) -> Version:
        """"""
    @Version.setter
    def Version(self, value: Version) -> None: ...
    @property
    def VersionCompatibility(self) -> AssemblyVersionCompatibility:
        """"""
    @VersionCompatibility.setter
    def VersionCompatibility(self, value: AssemblyVersionCompatibility) -> None: ...
    def Clone(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetAssemblyName(cls, assemblyFile: str) -> AssemblyName:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetPublicKey(self) -> Array[int]:
        """"""
    def GetPublicKeyToken(self) -> Array[int]:
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
    def OnDeserialization(self, sender: object) -> None:
        """"""
    @classmethod
    def ReferenceMatchesDefinition(cls, reference: AssemblyName, definition: AssemblyName) -> bool:
        """"""
    def SetPublicKey(self, publicKey: Array[int]) -> None:
        """"""
    def SetPublicKeyToken(self, publicKeyToken: Array[int]) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AssemblyNameProxy(MarshalByRefObject):
    """"""
    def __init__(self) -> None:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetAssemblyName(self, assemblyFile: str) -> AssemblyName:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AssemblyProductAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, product: str) -> None:
        """"""
    @property
    def Product(self) -> str:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AssemblySignatureKeyAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, publicKey: str, countersignature: str) -> None:
        """"""
    @property
    def Countersignature(self) -> str:
        """"""
    @property
    def PublicKey(self) -> str:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AssemblyTitleAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, title: str) -> None:
        """"""
    @property
    def Title(self) -> str:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AssemblyTrademarkAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, trademark: str) -> None:
        """"""
    @property
    def Trademark(self) -> str:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class AssemblyVersionAttribute(Attribute, _Attribute):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Associates(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Binder(ABC, Object):
    """"""
    def BindToField(
        self,
        bindingAttr: BindingFlags,
        match: Array[FieldInfo],
        value: object,
        culture: CultureInfo,
    ) -> FieldInfo:
        """"""
    def BindToMethod(
        self,
        bindingAttr: BindingFlags,
        match: Array[MethodBase],
        args: Object,
        modifiers: Array[ParameterModifier],
        culture: CultureInfo,
        names: Array[str],
        state: Object,
    ) -> tuple[MethodBase, Object]:
        """"""
    def ChangeType(self, value: object, type: Type, culture: CultureInfo) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ReorderArgumentArray(self, args: Object, state: object) -> None:
        """"""
    def SelectMethod(
        self,
        bindingAttr: BindingFlags,
        match: Array[MethodBase],
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodBase:
        """"""
    def SelectProperty(
        self,
        bindingAttr: BindingFlags,
        match: Array[PropertyInfo],
        returnType: Type,
        indexes: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> PropertyInfo:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class BlobUtilities(ABC, Object):
    """"""

    SizeOfGuid: ClassVar[int]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def ReadBytes(cls, buffer: int, byteCount: int) -> Array[int]:
        """"""
    @classmethod
    def ReadImmutableBytes(cls, buffer: int, byteCount: int) -> ImmutableArray[int]:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CerHashtable[K, V](ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ConstArray(ValueType):
    """"""
    @property
    def Item(self) -> int:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Signature(self) -> IntPtr:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __getitem__(self, index: int) -> int:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ConstructorInfo(
    ABC, MethodBase, ICustomAttributeProvider, _ConstructorInfo, _MemberInfo, _MethodBase
):
    """"""

    ConstructorName: ClassVar[str]
    """"""
    TypeConstructorName: ClassVar[str]
    """"""
    @property
    def Attributes(self) -> MethodAttributes:
        """"""
    @property
    def CallingConvention(self) -> CallingConventions:
        """"""
    @property
    def ContainsGenericParameters(self) -> bool:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def IsAbstract(self) -> bool:
        """"""
    @property
    def IsAssembly(self) -> bool:
        """"""
    @property
    def IsConstructor(self) -> bool:
        """"""
    @property
    def IsFamily(self) -> bool:
        """"""
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """"""
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """"""
    @property
    def IsFinal(self) -> bool:
        """"""
    @property
    def IsGenericMethod(self) -> bool:
        """"""
    @property
    def IsGenericMethodDefinition(self) -> bool:
        """"""
    @property
    def IsHideBySig(self) -> bool:
        """"""
    @property
    def IsPrivate(self) -> bool:
        """"""
    @property
    def IsPublic(self) -> bool:
        """"""
    @property
    def IsSecurityCritical(self) -> bool:
        """"""
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """"""
    @property
    def IsSecurityTransparent(self) -> bool:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def IsStatic(self) -> bool:
        """"""
    @property
    def IsVirtual(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """"""
    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetGenericArguments(self) -> Array[Type]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetMethodBody(self) -> MethodBody:
        """"""
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """"""
    def GetParameters(self) -> Array[ParameterInfo]:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    @overload
    def Invoke(
        self,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    @overload
    def Invoke(self, parameters: Array[object]) -> object:
        """"""
    @overload
    def Invoke(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """"""
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
        """"""
    def Invoke_2(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    def Invoke_3(self, obj: object, parameters: Array[object]) -> object:
        """"""
    def Invoke_4(
        self,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    def Invoke_5(self, parameters: Array[object]) -> object:
        """"""
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, left: ConstructorInfo, right: ConstructorInfo) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: ConstructorInfo, right: ConstructorInfo) -> bool:
        """"""
    def __eq__(self, other: ConstructorInfo) -> bool:
        """"""
    def __ne__(self, other: ConstructorInfo) -> bool:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CustomAttribute(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CustomAttributeCtorParameter(ValueType):
    """"""
    def __init__(self, type: CustomAttributeType) -> None:
        """"""
    @property
    def CustomAttributeEncodedArgument(self) -> CustomAttributeEncodedArgument:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CustomAttributeData(Object):
    """"""
    @property
    def AttributeType(self) -> Type:
        """"""
    @property
    def Constructor(self) -> ConstructorInfo:
        """"""
    @property
    def ConstructorArguments(self) -> IList[CustomAttributeTypedArgument]:
        """"""
    @property
    def NamedArguments(self) -> IList[CustomAttributeNamedArgument]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    @overload
    def GetCustomAttributes(cls, target: Assembly) -> IList[CustomAttributeData]:
        """"""
    @classmethod
    @overload
    def GetCustomAttributes(cls, target: MemberInfo) -> IList[CustomAttributeData]:
        """"""
    @classmethod
    @overload
    def GetCustomAttributes(cls, target: Module) -> IList[CustomAttributeData]:
        """"""
    @classmethod
    @overload
    def GetCustomAttributes(cls, target: ParameterInfo) -> IList[CustomAttributeData]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CustomAttributeEncodedArgument(ValueType):
    """"""
    @property
    def ArrayValue(self) -> Array[CustomAttributeEncodedArgument]:
        """"""
    @property
    def CustomAttributeType(self) -> CustomAttributeType:
        """"""
    @property
    def PrimitiveValue(self) -> int:
        """"""
    @property
    def StringValue(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CustomAttributeExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    @overload
    def GetCustomAttribute[T](cls, element: Assembly) -> T:
        """"""
    @classmethod
    @overload
    def GetCustomAttribute(cls, element: Assembly, attributeType: Type) -> Attribute:
        """"""
    @classmethod
    @overload
    def GetCustomAttribute[T](cls, element: MemberInfo) -> T:
        """"""
    @classmethod
    @overload
    def GetCustomAttribute[T](cls, element: MemberInfo, inherit: bool) -> T:
        """"""
    @classmethod
    @overload
    def GetCustomAttribute(cls, element: MemberInfo, attributeType: Type) -> Attribute:
        """"""
    @classmethod
    @overload
    def GetCustomAttribute(
        cls, element: MemberInfo, attributeType: Type, inherit: bool
    ) -> Attribute:
        """"""
    @classmethod
    @overload
    def GetCustomAttribute[T](cls, element: Module) -> T:
        """"""
    @classmethod
    @overload
    def GetCustomAttribute(cls, element: Module, attributeType: Type) -> Attribute:
        """"""
    @classmethod
    @overload
    def GetCustomAttribute[T](cls, element: ParameterInfo) -> T:
        """"""
    @classmethod
    @overload
    def GetCustomAttribute[T](cls, element: ParameterInfo, inherit: bool) -> T:
        """"""
    @classmethod
    @overload
    def GetCustomAttribute(cls, element: ParameterInfo, attributeType: Type) -> Attribute:
        """"""
    @classmethod
    @overload
    def GetCustomAttribute(
        cls, element: ParameterInfo, attributeType: Type, inherit: bool
    ) -> Attribute:
        """"""
    @classmethod
    @overload
    def GetCustomAttributes[T](cls, element: Assembly) -> IEnumerable[T]:
        """"""
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: Assembly, attributeType: Type) -> IEnumerable[Attribute]:
        """"""
    @classmethod
    @overload
    def GetCustomAttributes[T](cls, element: MemberInfo) -> IEnumerable[T]:
        """"""
    @classmethod
    @overload
    def GetCustomAttributes[T](cls, element: MemberInfo, inherit: bool) -> IEnumerable[T]:
        """"""
    @classmethod
    @overload
    def GetCustomAttributes(
        cls, element: MemberInfo, attributeType: Type
    ) -> IEnumerable[Attribute]:
        """"""
    @classmethod
    @overload
    def GetCustomAttributes(
        cls, element: MemberInfo, attributeType: Type, inherit: bool
    ) -> IEnumerable[Attribute]:
        """"""
    @classmethod
    @overload
    def GetCustomAttributes[T](cls, element: Module) -> IEnumerable[T]:
        """"""
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: Module, attributeType: Type) -> IEnumerable[Attribute]:
        """"""
    @classmethod
    @overload
    def GetCustomAttributes[T](cls, element: ParameterInfo) -> IEnumerable[T]:
        """"""
    @classmethod
    @overload
    def GetCustomAttributes[T](cls, element: ParameterInfo, inherit: bool) -> IEnumerable[T]:
        """"""
    @classmethod
    @overload
    def GetCustomAttributes(
        cls, element: ParameterInfo, attributeType: Type
    ) -> IEnumerable[Attribute]:
        """"""
    @classmethod
    @overload
    def GetCustomAttributes(
        cls, element: ParameterInfo, attributeType: Type, inherit: bool
    ) -> IEnumerable[Attribute]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def IsDefined(cls, element: Assembly, attributeType: Type) -> bool:
        """"""
    @classmethod
    @overload
    def IsDefined(cls, element: MemberInfo, attributeType: Type) -> bool:
        """"""
    @classmethod
    @overload
    def IsDefined(cls, element: MemberInfo, attributeType: Type, inherit: bool) -> bool:
        """"""
    @classmethod
    @overload
    def IsDefined(cls, element: Module, attributeType: Type) -> bool:
        """"""
    @classmethod
    @overload
    def IsDefined(cls, element: ParameterInfo, attributeType: Type) -> bool:
        """"""
    @classmethod
    @overload
    def IsDefined(cls, element: ParameterInfo, attributeType: Type, inherit: bool) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CustomAttributeFormatException(FormatException, _Exception, ISerializable):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CustomAttributeNamedArgument(ValueType):
    """"""
    @overload
    def __init__(self, memberInfo: MemberInfo, value: object) -> None:
        """"""
    @overload
    def __init__(self, memberInfo: MemberInfo, typedArgument: CustomAttributeTypedArgument) -> None:
        """"""
    @property
    def IsField(self) -> bool:
        """"""
    @property
    def MemberInfo(self) -> MemberInfo:
        """"""
    @property
    def MemberName(self) -> str:
        """"""
    @property
    def TypedValue(self) -> CustomAttributeTypedArgument:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(
        cls, left: CustomAttributeNamedArgument, right: CustomAttributeNamedArgument
    ) -> bool:
        """"""
    @classmethod
    def op_Inequality(
        cls, left: CustomAttributeNamedArgument, right: CustomAttributeNamedArgument
    ) -> bool:
        """"""
    def __eq__(self, other: CustomAttributeNamedArgument) -> bool:
        """"""
    def __ne__(self, other: CustomAttributeNamedArgument) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CustomAttributeNamedParameter(ValueType):
    """"""
    def __init__(
        self, argumentName: str, fieldOrProperty: CustomAttributeEncoding, type: CustomAttributeType
    ) -> None:
        """"""
    @property
    def EncodedArgument(self) -> CustomAttributeEncodedArgument:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CustomAttributeRecord(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CustomAttributeType(ValueType):
    """"""
    def __init__(
        self,
        encodedType: CustomAttributeEncoding,
        encodedArrayType: CustomAttributeEncoding,
        encodedEnumType: CustomAttributeEncoding,
        enumName: str,
    ) -> None:
        """"""
    @property
    def EncodedArrayType(self) -> CustomAttributeEncoding:
        """"""
    @property
    def EncodedEnumType(self) -> CustomAttributeEncoding:
        """"""
    @property
    def EncodedType(self) -> CustomAttributeEncoding:
        """"""
    @property
    def EnumName(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class CustomAttributeTypedArgument(ValueType):
    """"""
    @overload
    def __init__(self, argumentType: Type, value: object) -> None:
        """"""
    @overload
    def __init__(self, value: object) -> None:
        """"""
    @property
    def ArgumentType(self) -> Type:
        """"""
    @property
    def Value(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(
        cls, left: CustomAttributeTypedArgument, right: CustomAttributeTypedArgument
    ) -> bool:
        """"""
    @classmethod
    def op_Inequality(
        cls, left: CustomAttributeTypedArgument, right: CustomAttributeTypedArgument
    ) -> bool:
        """"""
    def __eq__(self, other: CustomAttributeTypedArgument) -> bool:
        """"""
    def __ne__(self, other: CustomAttributeTypedArgument) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class DefaultMemberAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, memberName: str) -> None:
        """"""
    @property
    def MemberName(self) -> str:
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class EventInfo(ABC, MemberInfo, ICustomAttributeProvider, _EventInfo, _MemberInfo):
    """"""
    @property
    def AddMethod(self) -> MethodInfo:
        """"""
    @property
    def Attributes(self) -> EventAttributes:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def EventHandlerType(self) -> Type:
        """"""
    @property
    def IsMulticast(self) -> bool:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def RaiseMethod(self) -> MethodInfo:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    @property
    def RemoveMethod(self) -> MethodInfo:
        """"""
    def AddEventHandler(self, target: object, handler: Delegate) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetAddMethod(self) -> MethodInfo:
        """"""
    @overload
    def GetAddMethod(self, nonPublic: bool) -> MethodInfo:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    @overload
    def GetOtherMethods(self) -> Array[MethodInfo]:
        """"""
    @overload
    def GetOtherMethods(self, nonPublic: bool) -> Array[MethodInfo]:
        """"""
    @overload
    def GetRaiseMethod(self) -> MethodInfo:
        """"""
    @overload
    def GetRaiseMethod(self, nonPublic: bool) -> MethodInfo:
        """"""
    @overload
    def GetRemoveMethod(self) -> MethodInfo:
        """"""
    @overload
    def GetRemoveMethod(self, nonPublic: bool) -> MethodInfo:
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
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    def RemoveEventHandler(self, target: object, handler: Delegate) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, left: EventInfo, right: EventInfo) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: EventInfo, right: EventInfo) -> bool:
        """"""
    def __eq__(self, other: EventInfo) -> bool:
        """"""
    def __ne__(self, other: EventInfo) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ExceptionHandlingClause(Object):
    """"""
    @property
    def CatchType(self) -> Type:
        """"""
    @property
    def FilterOffset(self) -> int:
        """"""
    @property
    def Flags(self) -> ExceptionHandlingClauseOptions:
        """"""
    @property
    def HandlerLength(self) -> int:
        """"""
    @property
    def HandlerOffset(self) -> int:
        """"""
    @property
    def TryLength(self) -> int:
        """"""
    @property
    def TryOffset(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class FieldInfo(ABC, MemberInfo, ICustomAttributeProvider, _FieldInfo, _MemberInfo):
    """"""
    @property
    def Attributes(self) -> FieldAttributes:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def FieldHandle(self) -> RuntimeFieldHandle:
        """"""
    @property
    def FieldType(self) -> Type:
        """"""
    @property
    def IsAssembly(self) -> bool:
        """"""
    @property
    def IsFamily(self) -> bool:
        """"""
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """"""
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """"""
    @property
    def IsInitOnly(self) -> bool:
        """"""
    @property
    def IsLiteral(self) -> bool:
        """"""
    @property
    def IsNotSerialized(self) -> bool:
        """"""
    @property
    def IsPinvokeImpl(self) -> bool:
        """"""
    @property
    def IsPrivate(self) -> bool:
        """"""
    @property
    def IsPublic(self) -> bool:
        """"""
    @property
    def IsSecurityCritical(self) -> bool:
        """"""
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """"""
    @property
    def IsSecurityTransparent(self) -> bool:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def IsStatic(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    @classmethod
    @overload
    def GetFieldFromHandle(cls, handle: RuntimeFieldHandle) -> FieldInfo:
        """"""
    @classmethod
    @overload
    def GetFieldFromHandle(
        cls, handle: RuntimeFieldHandle, declaringType: RuntimeTypeHandle
    ) -> FieldInfo:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetOptionalCustomModifiers(self) -> Array[Type]:
        """"""
    def GetRawConstantValue(self) -> object:
        """"""
    def GetRequiredCustomModifiers(self) -> Array[Type]:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def GetValue(self, obj: object) -> object:
        """"""
    def GetValueDirect(self, obj: TypedReference) -> object:
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
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    @overload
    def SetValue(self, obj: object, value: object) -> None:
        """"""
    @overload
    def SetValue(
        self,
        obj: object,
        value: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        culture: CultureInfo,
    ) -> None:
        """"""
    def SetValueDirect(self, obj: TypedReference, value: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, left: FieldInfo, right: FieldInfo) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: FieldInfo, right: FieldInfo) -> bool:
        """"""
    def __eq__(self, other: FieldInfo) -> bool:
        """"""
    def __ne__(self, other: FieldInfo) -> bool:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ICustomAttributeProvider(ABC):
    """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ICustomTypeProvider(ABC):
    """"""
    def GetCustomType(self) -> Type:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IReflect(ABC):
    """"""
    @property
    def UnderlyingSystemType(self) -> Type:
        """"""
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """"""
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """"""
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """"""
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """"""
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """"""
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """"""
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """"""
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """"""
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
        """"""
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
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IReflectableType(ABC):
    """"""
    def GetTypeInfo(self) -> TypeInfo:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class InterfaceMapping(ValueType):
    """"""

    InterfaceMethods: Final[Array[MethodInfo]]
    """"""
    InterfaceType: Final[Type]
    """"""
    TargetMethods: Final[Array[MethodInfo]]
    """"""
    TargetType: Final[Type]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class IntrospectionExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def GetTypeInfo(cls, type: Type) -> TypeInfo:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class InvalidFilterCriteriaException(ApplicationException, _Exception, ISerializable):
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class LoaderAllocator(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class LoaderAllocatorScout(Object):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class LocalVariableInfo(Object):
    """"""
    @property
    def IsPinned(self) -> bool:
        """"""
    @property
    def LocalIndex(self) -> int:
        """"""
    @property
    def LocalType(self) -> Type:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ManifestResourceInfo(Object):
    """"""
    def __init__(
        self,
        containingAssembly: Assembly,
        containingFileName: str,
        resourceLocation: ResourceLocation,
    ) -> None:
        """"""
    @property
    def FileName(self) -> str:
        """"""
    @property
    def ReferencedAssembly(self) -> Assembly:
        """"""
    @property
    def ResourceLocation(self) -> ResourceLocation:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MdConstant(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def GetValue(
        cls, scope: MetadataImport, token: int, fieldTypeHandle: RuntimeTypeHandle, raw: bool
    ) -> object:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MdFieldInfo(
    RuntimeFieldInfo, ICustomAttributeProvider, _FieldInfo, _MemberInfo, ISerializable
):
    """"""
    @property
    def Attributes(self) -> FieldAttributes:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def FieldHandle(self) -> RuntimeFieldHandle:
        """"""
    @property
    def FieldType(self) -> Type:
        """"""
    @property
    def IsAssembly(self) -> bool:
        """"""
    @property
    def IsFamily(self) -> bool:
        """"""
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """"""
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """"""
    @property
    def IsInitOnly(self) -> bool:
        """"""
    @property
    def IsLiteral(self) -> bool:
        """"""
    @property
    def IsNotSerialized(self) -> bool:
        """"""
    @property
    def IsPinvokeImpl(self) -> bool:
        """"""
    @property
    def IsPrivate(self) -> bool:
        """"""
    @property
    def IsPublic(self) -> bool:
        """"""
    @property
    def IsSecurityCritical(self) -> bool:
        """"""
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """"""
    @property
    def IsSecurityTransparent(self) -> bool:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def IsStatic(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetOptionalCustomModifiers(self) -> Array[Type]:
        """"""
    def GetRawConstantValue(self) -> object:
        """"""
    def GetRequiredCustomModifiers(self) -> Array[Type]:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def GetValue(self, obj: object) -> object:
        """"""
    def GetValueDirect(self, obj: TypedReference) -> object:
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
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    @overload
    def SetValue(self, obj: object, value: object) -> None:
        """"""
    @overload
    def SetValue(
        self,
        obj: object,
        value: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        culture: CultureInfo,
    ) -> None:
        """"""
    def SetValueDirect(self, obj: TypedReference, value: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

type MemberFilter = Callable[[MemberInfo, object], bool]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MemberInfo(ABC, Object, ICustomAttributeProvider, _MemberInfo):
    """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
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
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, left: MemberInfo, right: MemberInfo) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: MemberInfo, right: MemberInfo) -> bool:
        """"""
    def __eq__(self, other: MemberInfo) -> bool:
        """"""
    def __ne__(self, other: MemberInfo) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MemberInfoSerializationHolder(Object, IObjectReference, ISerializable):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetRealObject(self, context: StreamingContext) -> object:
        """"""
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
        """"""
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
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MetadataEnumResult(ValueType):
    """"""
    @property
    def Item(self) -> int:
        """"""
    @property
    def Length(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __getitem__(self, index: int) -> int:
        """"""
    # noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
    class smallResulte__FixedBuffer(ValueType):
        """"""

        FixedElementField: Final[int]
        """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MetadataException(Exception, _Exception, ISerializable):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MetadataImport(ValueType):
    """"""
    def Enum(
        self, type: MetadataTokenType, parent: int, result: MetadataEnumResult
    ) -> tuple[None, MetadataEnumResult]:
        """"""
    def EnumCustomAttributes(
        self, mdToken: int, result: MetadataEnumResult
    ) -> tuple[None, MetadataEnumResult]:
        """"""
    def EnumEvents(
        self, mdTypeDef: int, result: MetadataEnumResult
    ) -> tuple[None, MetadataEnumResult]:
        """"""
    def EnumFields(
        self, mdTypeDef: int, result: MetadataEnumResult
    ) -> tuple[None, MetadataEnumResult]:
        """"""
    def EnumNestedTypes(
        self, mdTypeDef: int, result: MetadataEnumResult
    ) -> tuple[None, MetadataEnumResult]:
        """"""
    def EnumParams(
        self, mdMethodDef: int, result: MetadataEnumResult
    ) -> tuple[None, MetadataEnumResult]:
        """"""
    def EnumProperties(
        self, mdTypeDef: int, result: MetadataEnumResult
    ) -> tuple[None, MetadataEnumResult]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetClassLayout(
        self, typeTokenDef: int, packSize: Int32, classSize: Int32
    ) -> tuple[None, Int32, Int32]:
        """"""
    def GetCustomAttributeProps(
        self, customAttributeToken: int, constructorToken: Int32, signature: ConstArray
    ) -> tuple[None, Int32, ConstArray]:
        """"""
    def GetDefaultValue(
        self, mdToken: int, value: Int64, length: Int32, corElementType: CorElementType
    ) -> tuple[str, Int64, Int32, CorElementType]:
        """"""
    def GetEventProps(
        self, mdToken: int, name: Void, eventAttributes: EventAttributes
    ) -> tuple[None, Void, EventAttributes]:
        """"""
    def GetFieldDefProps(
        self, mdToken: int, fieldAttributes: FieldAttributes
    ) -> tuple[None, FieldAttributes]:
        """"""
    def GetFieldMarshal(self, fieldToken: int) -> ConstArray:
        """"""
    def GetFieldOffset(
        self, typeTokenDef: int, fieldTokenDef: int, offset: Int32
    ) -> tuple[bool, Int32]:
        """"""
    def GetGenericParamProps(
        self, genericParameter: int, attributes: GenericParameterAttributes
    ) -> tuple[None, GenericParameterAttributes]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetMemberRefProps(self, memberTokenRef: int) -> ConstArray:
        """"""
    def GetMethodSignature(self, token: MetadataToken) -> ConstArray:
        """"""
    def GetName(self, mdToken: int) -> Utf8String:
        """"""
    def GetNamespace(self, mdToken: int) -> Utf8String:
        """"""
    def GetPInvokeMap(
        self, token: int, attributes: PInvokeAttributes, importName: String, importDll: String
    ) -> tuple[None, PInvokeAttributes, String, String]:
        """"""
    def GetParamDefProps(
        self, parameterToken: int, sequence: Int32, attributes: ParameterAttributes
    ) -> tuple[None, Int32, ParameterAttributes]:
        """"""
    def GetParentToken(self, tkToken: int) -> int:
        """"""
    def GetPropertyProps(
        self,
        mdToken: int,
        name: Void,
        propertyAttributes: PropertyAttributes,
        signature: ConstArray,
    ) -> tuple[None, Void, PropertyAttributes, ConstArray]:
        """"""
    def GetScopeProps(self, mvid: Guid) -> tuple[None, Guid]:
        """"""
    def GetSigOfFieldDef(self, fieldToken: int) -> ConstArray:
        """"""
    def GetSigOfMethodDef(self, methodToken: int) -> ConstArray:
        """"""
    def GetSignatureFromToken(self, token: int) -> ConstArray:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetUserString(self, mdToken: int) -> str:
        """"""
    def IsValidToken(self, token: int) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MetadataToken(ValueType):
    """"""

    Value: Final[int]
    """"""
    def __init__(self, token: int) -> None:
        """"""
    @property
    def IsAssembly(self) -> bool:
        """"""
    @property
    def IsEvent(self) -> bool:
        """"""
    @property
    def IsFieldDef(self) -> bool:
        """"""
    @property
    def IsGenericPar(self) -> bool:
        """"""
    @property
    def IsGlobalTypeDefToken(self) -> bool:
        """"""
    @property
    def IsMemberRef(self) -> bool:
        """"""
    @property
    def IsMethodDef(self) -> bool:
        """"""
    @property
    def IsMethodSpec(self) -> bool:
        """"""
    @property
    def IsModule(self) -> bool:
        """"""
    @property
    def IsParamDef(self) -> bool:
        """"""
    @property
    def IsProperty(self) -> bool:
        """"""
    @property
    def IsSignature(self) -> bool:
        """"""
    @property
    def IsString(self) -> bool:
        """"""
    @property
    def IsTypeDef(self) -> bool:
        """"""
    @property
    def IsTypeRef(self) -> bool:
        """"""
    @property
    def IsTypeSpec(self) -> bool:
        """"""
    @property
    def TokenType(self) -> MetadataTokenType:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsNullToken(cls, token: int) -> bool:
        """"""
    @classmethod
    def IsTokenOfType(cls, token: int, types: Array[MetadataTokenType]) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    @overload
    def op_Implicit(cls, token: MetadataToken) -> int:
        """"""
    @classmethod
    @overload
    def op_Implicit(cls, token: int) -> MetadataToken:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MethodBase(ABC, MemberInfo, ICustomAttributeProvider, _MemberInfo, _MethodBase):
    """"""
    @property
    def Attributes(self) -> MethodAttributes:
        """"""
    @property
    def CallingConvention(self) -> CallingConventions:
        """"""
    @property
    def ContainsGenericParameters(self) -> bool:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def IsAbstract(self) -> bool:
        """"""
    @property
    def IsAssembly(self) -> bool:
        """"""
    @property
    def IsConstructor(self) -> bool:
        """"""
    @property
    def IsFamily(self) -> bool:
        """"""
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """"""
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """"""
    @property
    def IsFinal(self) -> bool:
        """"""
    @property
    def IsGenericMethod(self) -> bool:
        """"""
    @property
    def IsGenericMethodDefinition(self) -> bool:
        """"""
    @property
    def IsHideBySig(self) -> bool:
        """"""
    @property
    def IsPrivate(self) -> bool:
        """"""
    @property
    def IsPublic(self) -> bool:
        """"""
    @property
    def IsSecurityCritical(self) -> bool:
        """"""
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """"""
    @property
    def IsSecurityTransparent(self) -> bool:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def IsStatic(self) -> bool:
        """"""
    @property
    def IsVirtual(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """"""
    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetCurrentMethod(cls) -> MethodBase:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetGenericArguments(self) -> Array[Type]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetMethodBody(self) -> MethodBody:
        """"""
    @classmethod
    @overload
    def GetMethodFromHandle(cls, handle: RuntimeMethodHandle) -> MethodBase:
        """"""
    @classmethod
    @overload
    def GetMethodFromHandle(
        cls, handle: RuntimeMethodHandle, declaringType: RuntimeTypeHandle
    ) -> MethodBase:
        """"""
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """"""
    def GetParameters(self) -> Array[ParameterInfo]:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    @overload
    def Invoke(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """"""
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
        """"""
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, left: MethodBase, right: MethodBase) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: MethodBase, right: MethodBase) -> bool:
        """"""
    def __eq__(self, other: MethodBase) -> bool:
        """"""
    def __ne__(self, other: MethodBase) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MethodBody(Object):
    """"""
    @property
    def ExceptionHandlingClauses(self) -> IList[ExceptionHandlingClause]:
        """"""
    @property
    def InitLocals(self) -> bool:
        """"""
    @property
    def LocalSignatureMetadataToken(self) -> int:
        """"""
    @property
    def LocalVariables(self) -> IList[LocalVariableInfo]:
        """"""
    @property
    def MaxStackSize(self) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetILAsByteArray(self) -> Array[int]:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class MethodInfo(ABC, MethodBase, ICustomAttributeProvider, _MemberInfo, _MethodBase, _MethodInfo):
    """"""
    @property
    def Attributes(self) -> MethodAttributes:
        """"""
    @property
    def CallingConvention(self) -> CallingConventions:
        """"""
    @property
    def ContainsGenericParameters(self) -> bool:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def IsAbstract(self) -> bool:
        """"""
    @property
    def IsAssembly(self) -> bool:
        """"""
    @property
    def IsConstructor(self) -> bool:
        """"""
    @property
    def IsFamily(self) -> bool:
        """"""
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """"""
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """"""
    @property
    def IsFinal(self) -> bool:
        """"""
    @property
    def IsGenericMethod(self) -> bool:
        """"""
    @property
    def IsGenericMethodDefinition(self) -> bool:
        """"""
    @property
    def IsHideBySig(self) -> bool:
        """"""
    @property
    def IsPrivate(self) -> bool:
        """"""
    @property
    def IsPublic(self) -> bool:
        """"""
    @property
    def IsSecurityCritical(self) -> bool:
        """"""
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """"""
    @property
    def IsSecurityTransparent(self) -> bool:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def IsStatic(self) -> bool:
        """"""
    @property
    def IsVirtual(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """"""
    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    @property
    def ReturnParameter(self) -> ParameterInfo:
        """"""
    @property
    def ReturnType(self) -> Type:
        """"""
    @property
    def ReturnTypeCustomAttributes(self) -> ICustomAttributeProvider:
        """"""
    @overload
    def CreateDelegate(self, delegateType: Type) -> Delegate:
        """"""
    @overload
    def CreateDelegate(self, delegateType: Type, target: object) -> Delegate:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseDefinition(self) -> MethodInfo:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetGenericArguments(self) -> Array[Type]:
        """"""
    def GetGenericMethodDefinition(self) -> MethodInfo:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetMethodBody(self) -> MethodBody:
        """"""
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """"""
    def GetParameters(self) -> Array[ParameterInfo]:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    @overload
    def Invoke(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """"""
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
        """"""
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    def MakeGenericMethod(self, typeArguments: Array[Type]) -> MethodInfo:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, left: MethodInfo, right: MethodInfo) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: MethodInfo, right: MethodInfo) -> bool:
        """"""
    def __eq__(self, other: MethodInfo) -> bool:
        """"""
    def __ne__(self, other: MethodInfo) -> bool:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Missing(Object, ISerializable):
    """"""

    Value: ClassVar[Missing]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Module(ABC, Object, ICustomAttributeProvider, _Module, ISerializable):
    """"""

    FilterTypeName: ClassVar[TypeFilter]
    """"""
    FilterTypeNameIgnoreCase: ClassVar[TypeFilter]
    """"""
    @property
    def Assembly(self) -> Assembly:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def FullyQualifiedName(self) -> str:
        """"""
    @property
    def MDStreamVersion(self) -> int:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def ModuleHandle(self) -> ModuleHandle:
        """"""
    @property
    def ModuleVersionId(self) -> Guid:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ScopeName(self) -> str:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    def FindTypes(self, filter: TypeFilter, filterCriteria: object) -> Array[Type]:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    @overload
    def GetField(self, name: str) -> FieldInfo:
        """"""
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """"""
    @overload
    def GetFields(self) -> Array[FieldInfo]:
        """"""
    @overload
    def GetFields(self, bindingFlags: BindingFlags) -> Array[FieldInfo]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    @overload
    def GetMethod(self, name: str) -> MethodInfo:
        """"""
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
        """"""
    @overload
    def GetMethod(self, name: str, types: Array[Type]) -> MethodInfo:
        """"""
    @overload
    def GetMethods(self) -> Array[MethodInfo]:
        """"""
    @overload
    def GetMethods(self, bindingFlags: BindingFlags) -> Array[MethodInfo]:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetPEKind(
        self, peKind: PortableExecutableKinds, machine: ImageFileMachine
    ) -> tuple[None, PortableExecutableKinds, ImageFileMachine]:
        """"""
    def GetSignerCertificate(self) -> X509Certificate:
        """"""
    @overload
    def GetType(self) -> Type:
        """"""
    @overload
    def GetType(self, className: str) -> Type:
        """"""
    @overload
    def GetType(self, className: str, ignoreCase: bool) -> Type:
        """"""
    @overload
    def GetType(self, className: str, throwOnError: bool, ignoreCase: bool) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def GetTypes(self) -> Array[Type]:
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
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    def IsResource(self) -> bool:
        """"""
    @overload
    def ResolveField(self, metadataToken: int) -> FieldInfo:
        """"""
    @overload
    def ResolveField(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> FieldInfo:
        """"""
    @overload
    def ResolveMember(self, metadataToken: int) -> MemberInfo:
        """"""
    @overload
    def ResolveMember(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> MemberInfo:
        """"""
    @overload
    def ResolveMethod(self, metadataToken: int) -> MethodBase:
        """"""
    @overload
    def ResolveMethod(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> MethodBase:
        """"""
    def ResolveSignature(self, metadataToken: int) -> Array[int]:
        """"""
    def ResolveString(self, metadataToken: int) -> str:
        """"""
    @overload
    def ResolveType(self, metadataToken: int) -> Type:
        """"""
    @overload
    def ResolveType(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, left: Module, right: Module) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: Module, right: Module) -> bool:
        """"""
    def __eq__(self, other: Module) -> bool:
        """"""
    def __ne__(self, other: Module) -> bool:
        """"""

type ModuleResolveEventHandler = Callable[[object, ResolveEventArgs], Module]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ObfuscateAssemblyAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, assemblyIsPrivate: bool) -> None:
        """"""
    @property
    def AssemblyIsPrivate(self) -> bool:
        """"""
    @property
    def StripAfterObfuscation(self) -> bool:
        """"""
    @StripAfterObfuscation.setter
    def StripAfterObfuscation(self, value: bool) -> None: ...
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ObfuscationAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def ApplyToMembers(self) -> bool:
        """"""
    @ApplyToMembers.setter
    def ApplyToMembers(self, value: bool) -> None: ...
    @property
    def Exclude(self) -> bool:
        """"""
    @Exclude.setter
    def Exclude(self, value: bool) -> None: ...
    @property
    def Feature(self) -> str:
        """"""
    @Feature.setter
    def Feature(self, value: str) -> None: ...
    @property
    def StripAfterObfuscation(self) -> bool:
        """"""
    @StripAfterObfuscation.setter
    def StripAfterObfuscation(self, value: bool) -> None: ...
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ParameterInfo(Object, ICustomAttributeProvider, _ParameterInfo, IObjectReference):
    """"""
    @property
    def Attributes(self) -> ParameterAttributes:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DefaultValue(self) -> object:
        """"""
    @property
    def HasDefaultValue(self) -> bool:
        """"""
    @property
    def IsIn(self) -> bool:
        """"""
    @property
    def IsLcid(self) -> bool:
        """"""
    @property
    def IsOptional(self) -> bool:
        """"""
    @property
    def IsOut(self) -> bool:
        """"""
    @property
    def IsRetval(self) -> bool:
        """"""
    @property
    def Member(self) -> MemberInfo:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ParameterType(self) -> Type:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @property
    def RawDefaultValue(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetOptionalCustomModifiers(self) -> Array[Type]:
        """"""
    def GetRealObject(self, context: StreamingContext) -> object:
        """"""
    def GetRequiredCustomModifiers(self) -> Array[Type]:
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
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ParameterModifier(ValueType):
    """"""
    def __init__(self, parameterCount: int) -> None:
        """"""
    @property
    def Item(self) -> bool:
        """"""
    @Item.setter
    def Item(self, value: bool) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def __getitem__(self, index: int) -> bool:
        """"""
    def __setitem__(self, index: int, value: bool) -> None:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Pointer(Object, ISerializable):
    """"""
    @classmethod
    def Box(cls, ptr: None, type: Type) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def Unbox(cls, ptr: object) -> None:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PropertyInfo(ABC, MemberInfo, ICustomAttributeProvider, _MemberInfo, _PropertyInfo):
    """"""
    @property
    def Attributes(self) -> PropertyAttributes:
        """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def GetMethod(self) -> MethodInfo:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def PropertyType(self) -> Type:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    @property
    def SetMethod(self) -> MethodInfo:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetAccessors(self) -> Array[MethodInfo]:
        """"""
    @overload
    def GetAccessors(self, nonPublic: bool) -> Array[MethodInfo]:
        """"""
    def GetConstantValue(self) -> object:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    @overload
    def GetGetMethod(self) -> MethodInfo:
        """"""
    @overload
    def GetGetMethod(self, nonPublic: bool) -> MethodInfo:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetIndexParameters(self) -> Array[ParameterInfo]:
        """"""
    def GetOptionalCustomModifiers(self) -> Array[Type]:
        """"""
    def GetRawConstantValue(self) -> object:
        """"""
    def GetRequiredCustomModifiers(self) -> Array[Type]:
        """"""
    @overload
    def GetSetMethod(self) -> MethodInfo:
        """"""
    @overload
    def GetSetMethod(self, nonPublic: bool) -> MethodInfo:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    @overload
    def GetValue(self, obj: object) -> object:
        """"""
    @overload
    def GetValue(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        index: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    @overload
    def GetValue(self, obj: object, index: Array[object]) -> object:
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
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    @overload
    def SetValue(self, obj: object, value: object) -> None:
        """"""
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
        """"""
    @overload
    def SetValue(self, obj: object, value: object, index: Array[object]) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, left: PropertyInfo, right: PropertyInfo) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: PropertyInfo, right: PropertyInfo) -> bool:
        """"""
    def __eq__(self, other: PropertyInfo) -> bool:
        """"""
    def __ne__(self, other: PropertyInfo) -> bool:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class PseudoCustomAttribute(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ReflectionContext(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeForObject(self, value: object) -> TypeInfo:
        """"""
    def MapAssembly(self, assembly: Assembly) -> Assembly:
        """"""
    def MapType(self, type: TypeInfo) -> TypeInfo:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class ReflectionTypeLoadException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self, classes: Array[Type], exceptions: Array[Exception]) -> None:
        """"""
    @overload
    def __init__(self, classes: Array[Type], exceptions: Array[Exception], message: str) -> None:
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
    def LoaderExceptions(self) -> Array[Exception]:
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
    @property
    def Types(self) -> Array[Type]:
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

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class ResourceAttributes(Enum):
    """"""

    Public: ResourceAttributes = ...
    """"""
    Private: ResourceAttributes = ...
    """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
class ResourceLocation(Enum):
    """"""

    Embedded: ResourceLocation = ...
    """"""
    ContainedInAnotherAssembly: ResourceLocation = ...
    """"""
    ContainedInManifestFile: ResourceLocation = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def FieldHandle(self) -> RuntimeFieldHandle:
        """"""
    @property
    def FieldType(self) -> Type:
        """"""
    @property
    def IsAssembly(self) -> bool:
        """"""
    @property
    def IsFamily(self) -> bool:
        """"""
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """"""
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """"""
    @property
    def IsInitOnly(self) -> bool:
        """"""
    @property
    def IsLiteral(self) -> bool:
        """"""
    @property
    def IsNotSerialized(self) -> bool:
        """"""
    @property
    def IsPinvokeImpl(self) -> bool:
        """"""
    @property
    def IsPrivate(self) -> bool:
        """"""
    @property
    def IsPublic(self) -> bool:
        """"""
    @property
    def IsSecurityCritical(self) -> bool:
        """"""
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """"""
    @property
    def IsSecurityTransparent(self) -> bool:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def IsStatic(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    @property
    def Value(self) -> RuntimeFieldHandleInternal:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetOptionalCustomModifiers(self) -> Array[Type]:
        """"""
    def GetRawConstantValue(self) -> object:
        """"""
    def GetRequiredCustomModifiers(self) -> Array[Type]:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def GetValue(self, obj: object) -> object:
        """"""
    def GetValueDirect(self, obj: TypedReference) -> object:
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
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    @overload
    def SetValue(self, obj: object, value: object) -> None:
        """"""
    @overload
    def SetValue(
        self,
        obj: object,
        value: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        culture: CultureInfo,
    ) -> None:
        """"""
    def SetValueDirect(self, obj: TypedReference, value: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DefinedTypes(self) -> IEnumerable[TypeInfo]:
        """"""
    @property
    def EntryPoint(self) -> MethodInfo:
        """"""
    @property
    def EscapedCodeBase(self) -> str:
        """"""
    @property
    def Evidence(self) -> Evidence:
        """"""
    @property
    def ExportedTypes(self) -> IEnumerable[Type]:
        """"""
    @property
    def FullName(self) -> str:
        """"""
    @property
    def GlobalAssemblyCache(self) -> bool:
        """"""
    @property
    def HostContext(self) -> int:
        """"""
    @property
    def ImageRuntimeVersion(self) -> str:
        """"""
    @property
    def IsDynamic(self) -> bool:
        """"""
    @property
    def IsFullyTrusted(self) -> bool:
        """"""
    @property
    def Location(self) -> str:
        """"""
    @property
    def ManifestModule(self) -> Module:
        """"""
    @property
    def Modules(self) -> IEnumerable[Module]:
        """"""
    @property
    def PermissionSet(self) -> PermissionSet:
        """"""
    @property
    def ReflectionOnly(self) -> bool:
        """"""
    @property
    def SecurityRuleSet(self) -> SecurityRuleSet:
        """"""
    @overload
    def CreateInstance(self, typeName: str) -> object:
        """"""
    @overload
    def CreateInstance(self, typeName: str, ignoreCase: bool) -> object:
        """"""
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
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetExportedTypes(self) -> Array[Type]:
        """"""
    def GetFile(self, name: str) -> FileStream:
        """"""
    @overload
    def GetFiles(self) -> Array[FileStream]:
        """"""
    @overload
    def GetFiles(self, getResourceModules: bool) -> Array[FileStream]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetInterface(self, iid: Guid, ppv: IntPtr) -> tuple[CustomQueryInterfaceResult, IntPtr]:
        """"""
    @overload
    def GetLoadedModules(self) -> Array[Module]:
        """"""
    @overload
    def GetLoadedModules(self, getResourceModules: bool) -> Array[Module]:
        """"""
    def GetManifestResourceInfo(self, resourceName: str) -> ManifestResourceInfo:
        """"""
    def GetManifestResourceNames(self) -> Array[str]:
        """"""
    @overload
    def GetManifestResourceStream(self, name: str) -> Stream:
        """"""
    @overload
    def GetManifestResourceStream(self, type: Type, name: str) -> Stream:
        """"""
    def GetModule(self, name: str) -> Module:
        """"""
    @overload
    def GetModules(self) -> Array[Module]:
        """"""
    @overload
    def GetModules(self, getResourceModules: bool) -> Array[Module]:
        """"""
    @overload
    def GetName(self) -> AssemblyName:
        """"""
    @overload
    def GetName(self, copiedName: bool) -> AssemblyName:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetReferencedAssemblies(self) -> Array[AssemblyName]:
        """"""
    @overload
    def GetSatelliteAssembly(self, culture: CultureInfo) -> Assembly:
        """"""
    @overload
    def GetSatelliteAssembly(self, culture: CultureInfo, version: Version) -> Assembly:
        """"""
    @overload
    def GetType(self) -> Type:
        """"""
    @overload
    def GetType(self, name: str) -> Type:
        """"""
    @overload
    def GetType(self, name: str, throwOnError: bool) -> Type:
        """"""
    @overload
    def GetType(self, name: str, throwOnError: bool, ignoreCase: bool) -> Type:
        """"""
    def GetTypes(self) -> Array[Type]:
        """"""
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    @overload
    def LoadModule(self, moduleName: str, rawModule: Array[int]) -> Module:
        """"""
    @overload
    def LoadModule(
        self, moduleName: str, rawModule: Array[int], rawSymbolStore: Array[int]
    ) -> Module:
        """"""
    def ToString(self) -> str:
        """"""
    ModuleResolve: EventType[ModuleResolveEventHandler] = ...
    """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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
        """"""
    @property
    def CallingConvention(self) -> CallingConventions:
        """"""
    @property
    def ContainsGenericParameters(self) -> bool:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def IsAbstract(self) -> bool:
        """"""
    @property
    def IsAssembly(self) -> bool:
        """"""
    @property
    def IsConstructor(self) -> bool:
        """"""
    @property
    def IsFamily(self) -> bool:
        """"""
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """"""
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """"""
    @property
    def IsFinal(self) -> bool:
        """"""
    @property
    def IsGenericMethod(self) -> bool:
        """"""
    @property
    def IsGenericMethodDefinition(self) -> bool:
        """"""
    @property
    def IsHideBySig(self) -> bool:
        """"""
    @property
    def IsPrivate(self) -> bool:
        """"""
    @property
    def IsPublic(self) -> bool:
        """"""
    @property
    def IsSecurityCritical(self) -> bool:
        """"""
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """"""
    @property
    def IsSecurityTransparent(self) -> bool:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def IsStatic(self) -> bool:
        """"""
    @property
    def IsVirtual(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """"""
    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    @property
    def Value(self) -> RuntimeMethodHandleInternal:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetGenericArguments(self) -> Array[Type]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetMethodBody(self) -> MethodBody:
        """"""
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetParameters(self) -> Array[ParameterInfo]:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    @overload
    def Invoke(
        self,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    @overload
    def Invoke(self, parameters: Array[object]) -> object:
        """"""
    @overload
    def Invoke(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """"""
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
        """"""
    def Invoke_2(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    def Invoke_3(self, obj: object, parameters: Array[object]) -> object:
        """"""
    def Invoke_4(
        self,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    def Invoke_5(self, parameters: Array[object]) -> object:
        """"""
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RuntimeEventInfo(EventInfo, ICustomAttributeProvider, _EventInfo, _MemberInfo, ISerializable):
    """"""
    @property
    def AddMethod(self) -> MethodInfo:
        """"""
    @property
    def Attributes(self) -> EventAttributes:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def EventHandlerType(self) -> Type:
        """"""
    @property
    def IsMulticast(self) -> bool:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def RaiseMethod(self) -> MethodInfo:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    @property
    def RemoveMethod(self) -> MethodInfo:
        """"""
    def AddEventHandler(self, target: object, handler: Delegate) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetAddMethod(self) -> MethodInfo:
        """"""
    @overload
    def GetAddMethod(self, nonPublic: bool) -> MethodInfo:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    @overload
    def GetOtherMethods(self) -> Array[MethodInfo]:
        """"""
    @overload
    def GetOtherMethods(self, nonPublic: bool) -> Array[MethodInfo]:
        """"""
    @overload
    def GetRaiseMethod(self) -> MethodInfo:
        """"""
    @overload
    def GetRaiseMethod(self, nonPublic: bool) -> MethodInfo:
        """"""
    @overload
    def GetRemoveMethod(self) -> MethodInfo:
        """"""
    @overload
    def GetRemoveMethod(self, nonPublic: bool) -> MethodInfo:
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
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    def RemoveEventHandler(self, target: object, handler: Delegate) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RuntimeFieldInfo(
    ABC, FieldInfo, ICustomAttributeProvider, _FieldInfo, _MemberInfo, ISerializable
):
    """"""
    @property
    def Attributes(self) -> FieldAttributes:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def FieldHandle(self) -> RuntimeFieldHandle:
        """"""
    @property
    def FieldType(self) -> Type:
        """"""
    @property
    def IsAssembly(self) -> bool:
        """"""
    @property
    def IsFamily(self) -> bool:
        """"""
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """"""
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """"""
    @property
    def IsInitOnly(self) -> bool:
        """"""
    @property
    def IsLiteral(self) -> bool:
        """"""
    @property
    def IsNotSerialized(self) -> bool:
        """"""
    @property
    def IsPinvokeImpl(self) -> bool:
        """"""
    @property
    def IsPrivate(self) -> bool:
        """"""
    @property
    def IsPublic(self) -> bool:
        """"""
    @property
    def IsSecurityCritical(self) -> bool:
        """"""
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """"""
    @property
    def IsSecurityTransparent(self) -> bool:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def IsStatic(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetOptionalCustomModifiers(self) -> Array[Type]:
        """"""
    def GetRawConstantValue(self) -> object:
        """"""
    def GetRequiredCustomModifiers(self) -> Array[Type]:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def GetValue(self, obj: object) -> object:
        """"""
    def GetValueDirect(self, obj: TypedReference) -> object:
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
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    @overload
    def SetValue(self, obj: object, value: object) -> None:
        """"""
    @overload
    def SetValue(
        self,
        obj: object,
        value: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        culture: CultureInfo,
    ) -> None:
        """"""
    def SetValueDirect(self, obj: TypedReference, value: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
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
        """"""
    @property
    def CallingConvention(self) -> CallingConventions:
        """"""
    @property
    def ContainsGenericParameters(self) -> bool:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def IsAbstract(self) -> bool:
        """"""
    @property
    def IsAssembly(self) -> bool:
        """"""
    @property
    def IsConstructor(self) -> bool:
        """"""
    @property
    def IsFamily(self) -> bool:
        """"""
    @property
    def IsFamilyAndAssembly(self) -> bool:
        """"""
    @property
    def IsFamilyOrAssembly(self) -> bool:
        """"""
    @property
    def IsFinal(self) -> bool:
        """"""
    @property
    def IsGenericMethod(self) -> bool:
        """"""
    @property
    def IsGenericMethodDefinition(self) -> bool:
        """"""
    @property
    def IsHideBySig(self) -> bool:
        """"""
    @property
    def IsPrivate(self) -> bool:
        """"""
    @property
    def IsPublic(self) -> bool:
        """"""
    @property
    def IsSecurityCritical(self) -> bool:
        """"""
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """"""
    @property
    def IsSecurityTransparent(self) -> bool:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def IsStatic(self) -> bool:
        """"""
    @property
    def IsVirtual(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """"""
    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    @property
    def ReturnParameter(self) -> ParameterInfo:
        """"""
    @property
    def ReturnType(self) -> Type:
        """"""
    @property
    def ReturnTypeCustomAttributes(self) -> ICustomAttributeProvider:
        """"""
    @property
    def Value(self) -> RuntimeMethodHandleInternal:
        """"""
    @overload
    def CreateDelegate(self, delegateType: Type) -> Delegate:
        """"""
    @overload
    def CreateDelegate(self, delegateType: Type, target: object) -> Delegate:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetBaseDefinition(self) -> MethodInfo:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetGenericArguments(self) -> Array[Type]:
        """"""
    def GetGenericMethodDefinition(self) -> MethodInfo:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetMethodBody(self) -> MethodBody:
        """"""
    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetParameters(self) -> Array[ParameterInfo]:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    @overload
    def Invoke(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        parameters: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    @overload
    def Invoke(self, obj: object, parameters: Array[object]) -> object:
        """"""
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
        """"""
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    def MakeGenericMethod(self, methodInstantiation: Array[Type]) -> MethodInfo:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RuntimeModule(Module, ICustomAttributeProvider, _Module, ISerializable):
    """"""
    @property
    def Assembly(self) -> Assembly:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def FullyQualifiedName(self) -> str:
        """"""
    @property
    def MDStreamVersion(self) -> int:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def ModuleHandle(self) -> ModuleHandle:
        """"""
    @property
    def ModuleVersionId(self) -> Guid:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ScopeName(self) -> str:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    def FindTypes(self, filter: TypeFilter, filterCriteria: object) -> Array[Type]:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    @overload
    def GetField(self, name: str) -> FieldInfo:
        """"""
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """"""
    @overload
    def GetFields(self) -> Array[FieldInfo]:
        """"""
    @overload
    def GetFields(self, bindingFlags: BindingFlags) -> Array[FieldInfo]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    @overload
    def GetMethod(self, name: str) -> MethodInfo:
        """"""
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
        """"""
    @overload
    def GetMethod(self, name: str, types: Array[Type]) -> MethodInfo:
        """"""
    @overload
    def GetMethods(self) -> Array[MethodInfo]:
        """"""
    @overload
    def GetMethods(self, bindingFlags: BindingFlags) -> Array[MethodInfo]:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetPEKind(
        self, peKind: PortableExecutableKinds, machine: ImageFileMachine
    ) -> tuple[None, PortableExecutableKinds, ImageFileMachine]:
        """"""
    def GetSignerCertificate(self) -> X509Certificate:
        """"""
    @overload
    def GetType(self) -> Type:
        """"""
    @overload
    def GetType(self, className: str) -> Type:
        """"""
    @overload
    def GetType(self, className: str, ignoreCase: bool) -> Type:
        """"""
    @overload
    def GetType(self, className: str, throwOnError: bool, ignoreCase: bool) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def GetTypes(self) -> Array[Type]:
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
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    def IsResource(self) -> bool:
        """"""
    @overload
    def ResolveField(self, metadataToken: int) -> FieldInfo:
        """"""
    @overload
    def ResolveField(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> FieldInfo:
        """"""
    @overload
    def ResolveMember(self, metadataToken: int) -> MemberInfo:
        """"""
    @overload
    def ResolveMember(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> MemberInfo:
        """"""
    @overload
    def ResolveMethod(self, metadataToken: int) -> MethodBase:
        """"""
    @overload
    def ResolveMethod(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> MethodBase:
        """"""
    def ResolveSignature(self, metadataToken: int) -> Array[int]:
        """"""
    def ResolveString(self, metadataToken: int) -> str:
        """"""
    @overload
    def ResolveType(self, metadataToken: int) -> Type:
        """"""
    @overload
    def ResolveType(
        self,
        metadataToken: int,
        genericTypeArguments: Array[Type],
        genericMethodArguments: Array[Type],
    ) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RuntimeParameterInfo(
    ParameterInfo, ICustomAttributeProvider, _ParameterInfo, IObjectReference, ISerializable
):
    """"""
    @property
    def Attributes(self) -> ParameterAttributes:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DefaultValue(self) -> object:
        """"""
    @property
    def HasDefaultValue(self) -> bool:
        """"""
    @property
    def IsIn(self) -> bool:
        """"""
    @property
    def IsLcid(self) -> bool:
        """"""
    @property
    def IsOptional(self) -> bool:
        """"""
    @property
    def IsOut(self) -> bool:
        """"""
    @property
    def IsRetval(self) -> bool:
        """"""
    @property
    def Member(self) -> MemberInfo:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ParameterType(self) -> Type:
        """"""
    @property
    def Position(self) -> int:
        """"""
    @property
    def RawDefaultValue(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetOptionalCustomModifiers(self) -> Array[Type]:
        """"""
    def GetRealObject(self, context: StreamingContext) -> object:
        """"""
    def GetRequiredCustomModifiers(self) -> Array[Type]:
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
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RuntimePropertyInfo(
    PropertyInfo, ICustomAttributeProvider, _MemberInfo, _PropertyInfo, ISerializable
):
    """"""
    @property
    def Attributes(self) -> PropertyAttributes:
        """"""
    @property
    def CanRead(self) -> bool:
        """"""
    @property
    def CanWrite(self) -> bool:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def GetMethod(self) -> MethodInfo:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def PropertyType(self) -> Type:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    @property
    def SetMethod(self) -> MethodInfo:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetAccessors(self) -> Array[MethodInfo]:
        """"""
    @overload
    def GetAccessors(self, nonPublic: bool) -> Array[MethodInfo]:
        """"""
    def GetConstantValue(self) -> object:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    @overload
    def GetGetMethod(self) -> MethodInfo:
        """"""
    @overload
    def GetGetMethod(self, nonPublic: bool) -> MethodInfo:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetIndexParameters(self) -> Array[ParameterInfo]:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetOptionalCustomModifiers(self) -> Array[Type]:
        """"""
    def GetRawConstantValue(self) -> object:
        """"""
    def GetRequiredCustomModifiers(self) -> Array[Type]:
        """"""
    @overload
    def GetSetMethod(self) -> MethodInfo:
        """"""
    @overload
    def GetSetMethod(self, nonPublic: bool) -> MethodInfo:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    @overload
    def GetValue(self, obj: object) -> object:
        """"""
    @overload
    def GetValue(
        self,
        obj: object,
        invokeAttr: BindingFlags,
        binder: Binder,
        index: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    @overload
    def GetValue(self, obj: object, index: Array[object]) -> object:
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
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    @overload
    def SetValue(self, obj: object, value: object) -> None:
        """"""
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
        """"""
    @overload
    def SetValue(self, obj: object, value: object, index: Array[object]) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class RuntimeReflectionExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetMethodInfo(cls, _del: Delegate) -> MethodInfo:
        """"""
    @classmethod
    def GetRuntimeBaseDefinition(cls, method: MethodInfo) -> MethodInfo:
        """"""
    @classmethod
    def GetRuntimeEvent(cls, type: Type, name: str) -> EventInfo:
        """"""
    @classmethod
    def GetRuntimeEvents(cls, type: Type) -> IEnumerable[EventInfo]:
        """"""
    @classmethod
    def GetRuntimeField(cls, type: Type, name: str) -> FieldInfo:
        """"""
    @classmethod
    def GetRuntimeFields(cls, type: Type) -> IEnumerable[FieldInfo]:
        """"""
    @classmethod
    def GetRuntimeInterfaceMap(cls, typeInfo: TypeInfo, interfaceType: Type) -> InterfaceMapping:
        """"""
    @classmethod
    def GetRuntimeMethod(cls, type: Type, name: str, parameters: Array[Type]) -> MethodInfo:
        """"""
    @classmethod
    def GetRuntimeMethods(cls, type: Type) -> IEnumerable[MethodInfo]:
        """"""
    @classmethod
    def GetRuntimeProperties(cls, type: Type) -> IEnumerable[PropertyInfo]:
        """"""
    @classmethod
    def GetRuntimeProperty(cls, type: Type, name: str) -> PropertyInfo:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class SecurityContextFrame(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Pop(self) -> None:
        """"""
    def Push(self, assembly: RuntimeAssembly) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class StrongNameKeyPair(Object, IDeserializationCallback, ISerializable):
    """"""
    @overload
    def __init__(self, keyPairFile: FileStream) -> None:
        """"""
    @overload
    def __init__(self, keyPairArray: Array[int]) -> None:
        """"""
    @overload
    def __init__(self, keyPairContainer: str) -> None:
        """"""
    @property
    def PublicKey(self) -> Array[int]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def OnDeserialization(self, sender: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TargetException(ApplicationException, _Exception, ISerializable):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TargetInvocationException(ApplicationException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self, inner: Exception) -> None:
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TargetParameterCountException(ApplicationException, _Exception, ISerializable):
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class Throw(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyPep8Naming,PyRedeclaration,DuplicatedCode,SpellCheckingInspection
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

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TypeDelegator(
    TypeInfo, ICustomAttributeProvider, IReflect, IReflectableType, _MemberInfo, _Type
):
    """"""
    def __init__(self, delegatingType: Type) -> None:
        """"""
    @property
    def Assembly(self) -> Assembly:
        """"""
    @property
    def AssemblyQualifiedName(self) -> str:
        """"""
    @property
    def Attributes(self) -> TypeAttributes:
        """"""
    @property
    def BaseType(self) -> Type:
        """"""
    @property
    def ContainsGenericParameters(self) -> bool:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaredConstructors(self) -> IEnumerable[ConstructorInfo]:
        """"""
    @property
    def DeclaredEvents(self) -> IEnumerable[EventInfo]:
        """"""
    @property
    def DeclaredFields(self) -> IEnumerable[FieldInfo]:
        """"""
    @property
    def DeclaredMembers(self) -> IEnumerable[MemberInfo]:
        """"""
    @property
    def DeclaredMethods(self) -> IEnumerable[MethodInfo]:
        """"""
    @property
    def DeclaredNestedTypes(self) -> IEnumerable[TypeInfo]:
        """"""
    @property
    def DeclaredProperties(self) -> IEnumerable[PropertyInfo]:
        """"""
    @property
    def DeclaringMethod(self) -> MethodBase:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def FullName(self) -> str:
        """"""
    @property
    def GUID(self) -> Guid:
        """"""
    @property
    def GenericParameterAttributes(self) -> GenericParameterAttributes:
        """"""
    @property
    def GenericParameterPosition(self) -> int:
        """"""
    @property
    def GenericTypeArguments(self) -> Array[Type]:
        """"""
    @property
    def GenericTypeParameters(self) -> Array[Type]:
        """"""
    @property
    def HasElementType(self) -> bool:
        """"""
    @property
    def ImplementedInterfaces(self) -> IEnumerable[Type]:
        """"""
    @property
    def IsAbstract(self) -> bool:
        """"""
    @property
    def IsAnsiClass(self) -> bool:
        """"""
    @property
    def IsArray(self) -> bool:
        """"""
    @property
    def IsAutoClass(self) -> bool:
        """"""
    @property
    def IsAutoLayout(self) -> bool:
        """"""
    @property
    def IsByRef(self) -> bool:
        """"""
    @property
    def IsCOMObject(self) -> bool:
        """"""
    @property
    def IsClass(self) -> bool:
        """"""
    @property
    def IsConstructedGenericType(self) -> bool:
        """"""
    @property
    def IsContextful(self) -> bool:
        """"""
    @property
    def IsEnum(self) -> bool:
        """"""
    @property
    def IsExplicitLayout(self) -> bool:
        """"""
    @property
    def IsGenericParameter(self) -> bool:
        """"""
    @property
    def IsGenericType(self) -> bool:
        """"""
    @property
    def IsGenericTypeDefinition(self) -> bool:
        """"""
    @property
    def IsImport(self) -> bool:
        """"""
    @property
    def IsInterface(self) -> bool:
        """"""
    @property
    def IsLayoutSequential(self) -> bool:
        """"""
    @property
    def IsMarshalByRef(self) -> bool:
        """"""
    @property
    def IsNested(self) -> bool:
        """"""
    @property
    def IsNestedAssembly(self) -> bool:
        """"""
    @property
    def IsNestedFamANDAssem(self) -> bool:
        """"""
    @property
    def IsNestedFamORAssem(self) -> bool:
        """"""
    @property
    def IsNestedFamily(self) -> bool:
        """"""
    @property
    def IsNestedPrivate(self) -> bool:
        """"""
    @property
    def IsNestedPublic(self) -> bool:
        """"""
    @property
    def IsNotPublic(self) -> bool:
        """"""
    @property
    def IsPointer(self) -> bool:
        """"""
    @property
    def IsPrimitive(self) -> bool:
        """"""
    @property
    def IsPublic(self) -> bool:
        """"""
    @property
    def IsSealed(self) -> bool:
        """"""
    @property
    def IsSecurityCritical(self) -> bool:
        """"""
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """"""
    @property
    def IsSecurityTransparent(self) -> bool:
        """"""
    @property
    def IsSerializable(self) -> bool:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def IsUnicodeClass(self) -> bool:
        """"""
    @property
    def IsValueType(self) -> bool:
        """"""
    @property
    def IsVisible(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Namespace(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    @property
    def StructLayoutAttribute(self) -> StructLayoutAttribute:
        """"""
    @property
    def TypeHandle(self) -> RuntimeTypeHandle:
        """"""
    @property
    def TypeInitializer(self) -> ConstructorInfo:
        """"""
    @property
    def UnderlyingSystemType(self) -> Type:
        """"""
    def AsType(self) -> Type:
        """"""
    @overload
    def Equals(self, o: object) -> bool:
        """"""
    @overload
    def Equals(self, o: Type) -> bool:
        """"""
    def FindInterfaces(self, filter: TypeFilter, filterCriteria: object) -> Array[Type]:
        """"""
    def FindMembers(
        self,
        memberType: MemberTypes,
        bindingAttr: BindingFlags,
        filter: MemberFilter,
        filterCriteria: object,
    ) -> Array[MemberInfo]:
        """"""
    def GetArrayRank(self) -> int:
        """"""
    @overload
    def GetConstructor(
        self,
        bindingAttr: BindingFlags,
        binder: Binder,
        callConvention: CallingConventions,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> ConstructorInfo:
        """"""
    @overload
    def GetConstructor(
        self,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> ConstructorInfo:
        """"""
    @overload
    def GetConstructor(self, types: Array[Type]) -> ConstructorInfo:
        """"""
    @overload
    def GetConstructors(self) -> Array[ConstructorInfo]:
        """"""
    @overload
    def GetConstructors(self, bindingAttr: BindingFlags) -> Array[ConstructorInfo]:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetDeclaredEvent(self, name: str) -> EventInfo:
        """"""
    def GetDeclaredField(self, name: str) -> FieldInfo:
        """"""
    def GetDeclaredMethod(self, name: str) -> MethodInfo:
        """"""
    def GetDeclaredMethods(self, name: str) -> IEnumerable[MethodInfo]:
        """"""
    def GetDeclaredNestedType(self, name: str) -> TypeInfo:
        """"""
    def GetDeclaredProperty(self, name: str) -> PropertyInfo:
        """"""
    def GetDefaultMembers(self) -> Array[MemberInfo]:
        """"""
    def GetElementType(self) -> Type:
        """"""
    def GetEnumName(self, value: object) -> str:
        """"""
    def GetEnumNames(self) -> Array[str]:
        """"""
    def GetEnumUnderlyingType(self) -> Type:
        """"""
    def GetEnumValues(self) -> Array:
        """"""
    @overload
    def GetEvent(self, name: str) -> EventInfo:
        """"""
    @overload
    def GetEvent(self, name: str, bindingAttr: BindingFlags) -> EventInfo:
        """"""
    @overload
    def GetEvents(self) -> Array[EventInfo]:
        """"""
    @overload
    def GetEvents(self, bindingAttr: BindingFlags) -> Array[EventInfo]:
        """"""
    @overload
    def GetField(self, name: str) -> FieldInfo:
        """"""
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """"""
    @overload
    def GetFields(self) -> Array[FieldInfo]:
        """"""
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """"""
    def GetGenericArguments(self) -> Array[Type]:
        """"""
    def GetGenericParameterConstraints(self) -> Array[Type]:
        """"""
    def GetGenericTypeDefinition(self) -> Type:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    @overload
    def GetInterface(self, name: str) -> Type:
        """"""
    @overload
    def GetInterface(self, name: str, ignoreCase: bool) -> Type:
        """"""
    def GetInterfaceMap(self, interfaceType: Type) -> InterfaceMapping:
        """"""
    def GetInterfaces(self) -> Array[Type]:
        """"""
    @overload
    def GetMember(self, name: str) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMember(
        self, name: str, type: MemberTypes, bindingAttr: BindingFlags
    ) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMembers(self) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMethod(self, name: str) -> MethodInfo:
        """"""
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """"""
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
        """"""
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """"""
    @overload
    def GetMethod(self, name: str, types: Array[Type]) -> MethodInfo:
        """"""
    @overload
    def GetMethod(
        self, name: str, types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> MethodInfo:
        """"""
    @overload
    def GetMethods(self) -> Array[MethodInfo]:
        """"""
    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """"""
    @overload
    def GetNestedType(self, name: str) -> Type:
        """"""
    @overload
    def GetNestedType(self, name: str, bindingAttr: BindingFlags) -> Type:
        """"""
    @overload
    def GetNestedTypes(self) -> Array[Type]:
        """"""
    @overload
    def GetNestedTypes(self, bindingAttr: BindingFlags) -> Array[Type]:
        """"""
    @overload
    def GetProperties(self) -> Array[PropertyInfo]:
        """"""
    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """"""
    @overload
    def GetProperty(self, name: str) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """"""
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
        """"""
    @overload
    def GetProperty(self, name: str, types: Array[Type]) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(self, name: str, returnType: Type) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(self, name: str, returnType: Type, types: Array[Type]) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(
        self, name: str, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> PropertyInfo:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def GetTypeInfo(self) -> TypeInfo:
        """"""
    @overload
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
    @overload
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
    ) -> object:
        """"""
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
        """"""
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
        """"""
    @overload
    def IsAssignableFrom(self, typeInfo: TypeInfo) -> bool:
        """"""
    @overload
    def IsAssignableFrom(self, c: Type) -> bool:
        """"""
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    def IsEnumDefined(self, value: object) -> bool:
        """"""
    def IsEquivalentTo(self, other: Type) -> bool:
        """"""
    def IsInstanceOfType(self, o: object) -> bool:
        """"""
    def IsSubclassOf(self, c: Type) -> bool:
        """"""
    @overload
    def MakeArrayType(self) -> Type:
        """"""
    @overload
    def MakeArrayType(self, rank: int) -> Type:
        """"""
    def MakeByRefType(self) -> Type:
        """"""
    def MakeGenericType(self, typeArguments: Array[Type]) -> Type:
        """"""
    def MakePointerType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

type TypeFilter = Callable[[Type, object], bool]
""""""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class TypeInfo(ABC, Type, ICustomAttributeProvider, IReflect, IReflectableType, _MemberInfo, _Type):
    """"""
    @property
    def Assembly(self) -> Assembly:
        """"""
    @property
    def AssemblyQualifiedName(self) -> str:
        """"""
    @property
    def Attributes(self) -> TypeAttributes:
        """"""
    @property
    def BaseType(self) -> Type:
        """"""
    @property
    def ContainsGenericParameters(self) -> bool:
        """"""
    @property
    def CustomAttributes(self) -> IEnumerable[CustomAttributeData]:
        """"""
    @property
    def DeclaredConstructors(self) -> IEnumerable[ConstructorInfo]:
        """"""
    @property
    def DeclaredEvents(self) -> IEnumerable[EventInfo]:
        """"""
    @property
    def DeclaredFields(self) -> IEnumerable[FieldInfo]:
        """"""
    @property
    def DeclaredMembers(self) -> IEnumerable[MemberInfo]:
        """"""
    @property
    def DeclaredMethods(self) -> IEnumerable[MethodInfo]:
        """"""
    @property
    def DeclaredNestedTypes(self) -> IEnumerable[TypeInfo]:
        """"""
    @property
    def DeclaredProperties(self) -> IEnumerable[PropertyInfo]:
        """"""
    @property
    def DeclaringMethod(self) -> MethodBase:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @property
    def FullName(self) -> str:
        """"""
    @property
    def GUID(self) -> Guid:
        """"""
    @property
    def GenericParameterAttributes(self) -> GenericParameterAttributes:
        """"""
    @property
    def GenericParameterPosition(self) -> int:
        """"""
    @property
    def GenericTypeArguments(self) -> Array[Type]:
        """"""
    @property
    def GenericTypeParameters(self) -> Array[Type]:
        """"""
    @property
    def HasElementType(self) -> bool:
        """"""
    @property
    def ImplementedInterfaces(self) -> IEnumerable[Type]:
        """"""
    @property
    def IsAbstract(self) -> bool:
        """"""
    @property
    def IsAnsiClass(self) -> bool:
        """"""
    @property
    def IsArray(self) -> bool:
        """"""
    @property
    def IsAutoClass(self) -> bool:
        """"""
    @property
    def IsAutoLayout(self) -> bool:
        """"""
    @property
    def IsByRef(self) -> bool:
        """"""
    @property
    def IsCOMObject(self) -> bool:
        """"""
    @property
    def IsClass(self) -> bool:
        """"""
    @property
    def IsConstructedGenericType(self) -> bool:
        """"""
    @property
    def IsContextful(self) -> bool:
        """"""
    @property
    def IsEnum(self) -> bool:
        """"""
    @property
    def IsExplicitLayout(self) -> bool:
        """"""
    @property
    def IsGenericParameter(self) -> bool:
        """"""
    @property
    def IsGenericType(self) -> bool:
        """"""
    @property
    def IsGenericTypeDefinition(self) -> bool:
        """"""
    @property
    def IsImport(self) -> bool:
        """"""
    @property
    def IsInterface(self) -> bool:
        """"""
    @property
    def IsLayoutSequential(self) -> bool:
        """"""
    @property
    def IsMarshalByRef(self) -> bool:
        """"""
    @property
    def IsNested(self) -> bool:
        """"""
    @property
    def IsNestedAssembly(self) -> bool:
        """"""
    @property
    def IsNestedFamANDAssem(self) -> bool:
        """"""
    @property
    def IsNestedFamORAssem(self) -> bool:
        """"""
    @property
    def IsNestedFamily(self) -> bool:
        """"""
    @property
    def IsNestedPrivate(self) -> bool:
        """"""
    @property
    def IsNestedPublic(self) -> bool:
        """"""
    @property
    def IsNotPublic(self) -> bool:
        """"""
    @property
    def IsPointer(self) -> bool:
        """"""
    @property
    def IsPrimitive(self) -> bool:
        """"""
    @property
    def IsPublic(self) -> bool:
        """"""
    @property
    def IsSealed(self) -> bool:
        """"""
    @property
    def IsSecurityCritical(self) -> bool:
        """"""
    @property
    def IsSecuritySafeCritical(self) -> bool:
        """"""
    @property
    def IsSecurityTransparent(self) -> bool:
        """"""
    @property
    def IsSerializable(self) -> bool:
        """"""
    @property
    def IsSpecialName(self) -> bool:
        """"""
    @property
    def IsUnicodeClass(self) -> bool:
        """"""
    @property
    def IsValueType(self) -> bool:
        """"""
    @property
    def IsVisible(self) -> bool:
        """"""
    @property
    def MemberType(self) -> MemberTypes:
        """"""
    @property
    def MetadataToken(self) -> int:
        """"""
    @property
    def Module(self) -> Module:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Namespace(self) -> str:
        """"""
    @property
    def ReflectedType(self) -> Type:
        """"""
    @property
    def StructLayoutAttribute(self) -> StructLayoutAttribute:
        """"""
    @property
    def TypeHandle(self) -> RuntimeTypeHandle:
        """"""
    @property
    def TypeInitializer(self) -> ConstructorInfo:
        """"""
    @property
    def UnderlyingSystemType(self) -> Type:
        """"""
    def AsType(self) -> Type:
        """"""
    @overload
    def Equals(self, o: object) -> bool:
        """"""
    @overload
    def Equals(self, o: Type) -> bool:
        """"""
    def FindInterfaces(self, filter: TypeFilter, filterCriteria: object) -> Array[Type]:
        """"""
    def FindMembers(
        self,
        memberType: MemberTypes,
        bindingAttr: BindingFlags,
        filter: MemberFilter,
        filterCriteria: object,
    ) -> Array[MemberInfo]:
        """"""
    def GetArrayRank(self) -> int:
        """"""
    @overload
    def GetConstructor(
        self,
        bindingAttr: BindingFlags,
        binder: Binder,
        callConvention: CallingConventions,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> ConstructorInfo:
        """"""
    @overload
    def GetConstructor(
        self,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> ConstructorInfo:
        """"""
    @overload
    def GetConstructor(self, types: Array[Type]) -> ConstructorInfo:
        """"""
    @overload
    def GetConstructors(self) -> Array[ConstructorInfo]:
        """"""
    @overload
    def GetConstructors(self, bindingAttr: BindingFlags) -> Array[ConstructorInfo]:
        """"""
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Array[object]:
        """"""
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Array[object]:
        """"""
    def GetCustomAttributesData(self) -> IList[CustomAttributeData]:
        """"""
    def GetDeclaredEvent(self, name: str) -> EventInfo:
        """"""
    def GetDeclaredField(self, name: str) -> FieldInfo:
        """"""
    def GetDeclaredMethod(self, name: str) -> MethodInfo:
        """"""
    def GetDeclaredMethods(self, name: str) -> IEnumerable[MethodInfo]:
        """"""
    def GetDeclaredNestedType(self, name: str) -> TypeInfo:
        """"""
    def GetDeclaredProperty(self, name: str) -> PropertyInfo:
        """"""
    def GetDefaultMembers(self) -> Array[MemberInfo]:
        """"""
    def GetElementType(self) -> Type:
        """"""
    def GetEnumName(self, value: object) -> str:
        """"""
    def GetEnumNames(self) -> Array[str]:
        """"""
    def GetEnumUnderlyingType(self) -> Type:
        """"""
    def GetEnumValues(self) -> Array:
        """"""
    @overload
    def GetEvent(self, name: str) -> EventInfo:
        """"""
    @overload
    def GetEvent(self, name: str, bindingAttr: BindingFlags) -> EventInfo:
        """"""
    @overload
    def GetEvents(self) -> Array[EventInfo]:
        """"""
    @overload
    def GetEvents(self, bindingAttr: BindingFlags) -> Array[EventInfo]:
        """"""
    @overload
    def GetField(self, name: str) -> FieldInfo:
        """"""
    @overload
    def GetField(self, name: str, bindingAttr: BindingFlags) -> FieldInfo:
        """"""
    @overload
    def GetFields(self) -> Array[FieldInfo]:
        """"""
    @overload
    def GetFields(self, bindingAttr: BindingFlags) -> Array[FieldInfo]:
        """"""
    def GetGenericArguments(self) -> Array[Type]:
        """"""
    def GetGenericParameterConstraints(self) -> Array[Type]:
        """"""
    def GetGenericTypeDefinition(self) -> Type:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    @overload
    def GetInterface(self, name: str) -> Type:
        """"""
    @overload
    def GetInterface(self, name: str, ignoreCase: bool) -> Type:
        """"""
    def GetInterfaceMap(self, interfaceType: Type) -> InterfaceMapping:
        """"""
    def GetInterfaces(self) -> Array[Type]:
        """"""
    @overload
    def GetMember(self, name: str) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMember(self, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMember(
        self, name: str, type: MemberTypes, bindingAttr: BindingFlags
    ) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMembers(self) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMembers(self, bindingAttr: BindingFlags) -> Array[MemberInfo]:
        """"""
    @overload
    def GetMethod(self, name: str) -> MethodInfo:
        """"""
    @overload
    def GetMethod(self, name: str, bindingAttr: BindingFlags) -> MethodInfo:
        """"""
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
        """"""
    @overload
    def GetMethod(
        self,
        name: str,
        bindingAttr: BindingFlags,
        binder: Binder,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> MethodInfo:
        """"""
    @overload
    def GetMethod(self, name: str, types: Array[Type]) -> MethodInfo:
        """"""
    @overload
    def GetMethod(
        self, name: str, types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> MethodInfo:
        """"""
    @overload
    def GetMethods(self) -> Array[MethodInfo]:
        """"""
    @overload
    def GetMethods(self, bindingAttr: BindingFlags) -> Array[MethodInfo]:
        """"""
    @overload
    def GetNestedType(self, name: str) -> Type:
        """"""
    @overload
    def GetNestedType(self, name: str, bindingAttr: BindingFlags) -> Type:
        """"""
    @overload
    def GetNestedTypes(self) -> Array[Type]:
        """"""
    @overload
    def GetNestedTypes(self, bindingAttr: BindingFlags) -> Array[Type]:
        """"""
    @overload
    def GetProperties(self) -> Array[PropertyInfo]:
        """"""
    @overload
    def GetProperties(self, bindingAttr: BindingFlags) -> Array[PropertyInfo]:
        """"""
    @overload
    def GetProperty(self, name: str) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(self, name: str, bindingAttr: BindingFlags) -> PropertyInfo:
        """"""
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
        """"""
    @overload
    def GetProperty(self, name: str, types: Array[Type]) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(self, name: str, returnType: Type) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(self, name: str, returnType: Type, types: Array[Type]) -> PropertyInfo:
        """"""
    @overload
    def GetProperty(
        self, name: str, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> PropertyInfo:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def GetTypeInfo(self) -> TypeInfo:
        """"""
    @overload
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
    @overload
    def InvokeMember(
        self,
        name: str,
        invokeAttr: BindingFlags,
        binder: Binder,
        target: object,
        args: Array[object],
    ) -> object:
        """"""
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
        """"""
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
        """"""
    @overload
    def IsAssignableFrom(self, typeInfo: TypeInfo) -> bool:
        """"""
    @overload
    def IsAssignableFrom(self, c: Type) -> bool:
        """"""
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool:
        """"""
    def IsEnumDefined(self, value: object) -> bool:
        """"""
    def IsEquivalentTo(self, other: Type) -> bool:
        """"""
    def IsInstanceOfType(self, o: object) -> bool:
        """"""
    def IsSubclassOf(self, c: Type) -> bool:
        """"""
    @overload
    def MakeArrayType(self) -> Type:
        """"""
    @overload
    def MakeArrayType(self, rank: int) -> Type:
        """"""
    def MakeByRefType(self) -> Type:
        """"""
    def MakeGenericType(self, typeArguments: Array[Type]) -> Type:
        """"""
    def MakePointerType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

# noinspection PyMethodOverriding,PyPep8Naming,PyRedeclaration,PyTypeHints,PyUnresolvedReferences,PyOverloads,PyClassVar,DuplicatedCode,SpellCheckingInspection
class __Filters(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FilterTypeName(self, _cls: Type, filterCriteria: object) -> bool:
        """"""
    def FilterTypeNameIgnoreCase(self, _cls: Type, filterCriteria: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
