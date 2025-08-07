"""Automatically generated stubs for C# namespace: System."""

from abc import ABC
from collections.abc import Callable
from collections.abc import Iterator
from typing import ClassVar
from typing import Final
from typing import Self
from typing import overload

from Microsoft.Win32.SafeHandles import SafeHandleZeroOrMinusOneIsInvalid
from System.Collections import ICollection
from System.Collections import IComparer
from System.Collections import IDictionary
from System.Collections import IEnumerable
from System.Collections import IEnumerator
from System.Collections import IEqualityComparer
from System.Collections import IList
from System.Collections import IStructuralComparable
from System.Collections import IStructuralEquatable
from System.Collections.Generic import ICollection
from System.Collections.Generic import IComparer
from System.Collections.Generic import IEnumerable
from System.Collections.Generic import IEnumerator
from System.Collections.Generic import IEqualityComparer
from System.Collections.Generic import IList
from System.Collections.Generic import IReadOnlyCollection
from System.Collections.Generic import IReadOnlyList
from System.Collections.ObjectModel import ReadOnlyCollection
from System.ComponentModel import CategoryAttribute
from System.ComponentModel import DescriptionAttribute
from System.ComponentModel import ITypeDescriptorContext
from System.ComponentModel import PropertyDescriptorCollection
from System.ComponentModel import TypeConverter
from System.Configuration.Assemblies import AssemblyHashAlgorithm
from System.Diagnostics.Tracing import EventChannel
from System.Diagnostics.Tracing import EventCommandEventArgs
from System.Diagnostics.Tracing import EventKeywords
from System.Diagnostics.Tracing import EventLevel
from System.Diagnostics.Tracing import EventSource
from System.Diagnostics.Tracing import EventSourceOptions
from System.Diagnostics.Tracing import EventSourceSettings
from System.Diagnostics.Tracing import T
from System.Globalization import Calendar
from System.Globalization import CompareOptions
from System.Globalization import CultureInfo
from System.Globalization import DateTimeStyles
from System.Globalization import DaylightTime
from System.Globalization import NumberFormatInfo
from System.Globalization import NumberStyles
from System.Globalization import TimeSpanStyles
from System.Globalization import UnicodeCategory
from System.IO import Stream
from System.IO import TextReader
from System.IO import TextWriter
from System.Reflection import Assembly
from System.Reflection import AssemblyName
from System.Reflection import Binder
from System.Reflection import BindingFlags
from System.Reflection import CallingConventions
from System.Reflection import ConstructorInfo
from System.Reflection import CustomAttributeData
from System.Reflection import EventInfo
from System.Reflection import FieldInfo
from System.Reflection import GenericParameterAttributes
from System.Reflection import ICustomAttributeProvider
from System.Reflection import InterfaceMapping
from System.Reflection import IReflect
from System.Reflection import IReflectableType
from System.Reflection import MemberFilter
from System.Reflection import MemberInfo
from System.Reflection import MemberTypes
from System.Reflection import MethodBase
from System.Reflection import MethodInfo
from System.Reflection import Module
from System.Reflection import ParameterInfo
from System.Reflection import ParameterModifier
from System.Reflection import PropertyInfo
from System.Reflection import TypeAttributes
from System.Reflection import TypeFilter
from System.Reflection import TypeInfo
from System.Reflection.Emit import AssemblyBuilder
from System.Reflection.Emit import AssemblyBuilderAccess
from System.Reflection.Emit import CustomAttributeBuilder
from System.Resources import ResourceManager
from System.Runtime.CompilerServices import ITuple
from System.Runtime.ConstrainedExecution import CriticalFinalizerObject
from System.Runtime.ExceptionServices import FirstChanceExceptionEventArgs
from System.Runtime.Hosting import ActivationArguments
from System.Runtime.Hosting import ApplicationActivator
from System.Runtime.InteropServices import StructLayoutAttribute
from System.Runtime.InteropServices import _Activator
from System.Runtime.InteropServices import _Attribute
from System.Runtime.InteropServices import _Exception
from System.Runtime.InteropServices import _MemberInfo
from System.Runtime.InteropServices import _Type
from System.Runtime.Remoting import ObjectHandle
from System.Runtime.Remoting import ObjRef
from System.Runtime.Serialization import IDeserializationCallback
from System.Runtime.Serialization import IObjectReference
from System.Runtime.Serialization import ISerializable
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext
from System.Security import HostSecurityManager
from System.Security import IEvidenceFactory
from System.Security import IPermission
from System.Security import PermissionSet
from System.Security import SecurityContextSource
from System.Security import SecurityState
from System.Security.Policy import ApplicationTrust
from System.Security.Policy import Evidence
from System.Security.Policy import PolicyLevel
from System.Security.Policy import StrongName
from System.Security.Principal import IPrincipal
from System.Security.Principal import PrincipalPolicy
from System.Security.Util import StringMaker
from System.Text import Encoding
from System.Text import NormalizationForm
from System.Text import StringBuilder
from System.Threading import CancellationToken
from System.Threading import HostExecutionContextManager
from System.Threading import LazyThreadSafetyMode
from System.Threading import WaitHandle

class EventType[T]:
    def __iadd__(self, other: T) -> Self: ...
    def __isub__(self, other: T) -> Self: ...

class AccessViolationException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
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

Action: Callable[[T], None] = ...
""""""
Action: Callable[[T1, T2], None] = ...
""""""
Action: Callable[[T1, T2, T3], None] = ...
""""""
Action: Callable[[T1, T2, T3, T4], None] = ...
""""""
Action: Callable[[T1, T2, T3, T4, T5], None] = ...
""""""
Action: Callable[[T1, T2, T3, T4, T5, T6], None] = ...
""""""
Action: Callable[[T1, T2, T3, T4, T5, T6, T7], None] = ...
""""""
Action: Callable[[T1, T2, T3, T4, T5, T6, T7, T8], None] = ...
""""""
Action: Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9], None] = ...
""""""
Action: Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10], None] = ...
""""""
Action: Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11], None] = ...
""""""
Action: Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12], None] = ...
""""""
Action: Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13], None] = ...
""""""
Action: Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14], None] = ...
""""""
Action: Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15], None] = ...
""""""
Action: Callable[
    [T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16], None
] = ...
""""""
Action: Callable[[], None] = ...
""""""

class ActivationContext(Object, ISerializable, IDisposable):
    """"""
    @property
    def ApplicationManifestBytes(self) -> Array[int]:
        """"""
    @property
    def DeploymentManifestBytes(self) -> Array[int]:
        """"""
    @property
    def Form(self) -> ActivationContext.ContextForm:
        """"""
    @property
    def Identity(self) -> ApplicationIdentity:
        """"""
    @classmethod
    @overload
    def CreatePartialActivationContext(cls, identity: ApplicationIdentity) -> ActivationContext:
        """"""
    @classmethod
    @overload
    def CreatePartialActivationContext(
        cls, identity: ApplicationIdentity, manifestPaths: Array[str]
    ) -> ActivationContext:
        """"""
    def Dispose(self) -> None:
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
    class ContextForm(Enum):
        """"""

        Loose: ContextForm = ...
        """"""
        StoreBounded: ContextForm = ...
        """"""

class Activator(Object, _Activator):
    """"""
    @classmethod
    @overload
    def CreateComInstanceFrom(cls, assemblyName: str, typeName: str) -> ObjectHandle:
        """"""
    @classmethod
    @overload
    def CreateComInstanceFrom(
        cls,
        assemblyName: str,
        typeName: str,
        hashValue: Array[int],
        hashAlgorithm: AssemblyHashAlgorithm,
    ) -> ObjectHandle:
        """"""
    @classmethod
    @overload
    def CreateInstance[T](cls) -> T:
        """"""
    @classmethod
    @overload
    def CreateInstance(cls, activationContext: ActivationContext) -> ObjectHandle:
        """"""
    @classmethod
    @overload
    def CreateInstance(
        cls, activationContext: ActivationContext, activationCustomData: Array[str]
    ) -> ObjectHandle:
        """"""
    @classmethod
    @overload
    def CreateInstance(cls, domain: AppDomain, assemblyName: str, typeName: str) -> ObjectHandle:
        """"""
    @classmethod
    @overload
    def CreateInstance(
        cls,
        domain: AppDomain,
        assemblyName: str,
        typeName: str,
        ignoreCase: bool,
        bindingAttr: BindingFlags,
        binder: Binder,
        args: Array[object],
        culture: CultureInfo,
        activationAttributes: Array[object],
    ) -> ObjectHandle:
        """"""
    @classmethod
    @overload
    def CreateInstance(
        cls,
        domain: AppDomain,
        assemblyName: str,
        typeName: str,
        ignoreCase: bool,
        bindingAttr: BindingFlags,
        binder: Binder,
        args: Array[object],
        culture: CultureInfo,
        activationAttributes: Array[object],
        securityAttributes: Evidence,
    ) -> ObjectHandle:
        """"""
    @classmethod
    @overload
    def CreateInstance(cls, assemblyName: str, typeName: str) -> ObjectHandle:
        """"""
    @classmethod
    @overload
    def CreateInstance(
        cls, assemblyName: str, typeName: str, activationAttributes: Array[object]
    ) -> ObjectHandle:
        """"""
    @classmethod
    @overload
    def CreateInstance(
        cls,
        assemblyName: str,
        typeName: str,
        ignoreCase: bool,
        bindingAttr: BindingFlags,
        binder: Binder,
        args: Array[object],
        culture: CultureInfo,
        activationAttributes: Array[object],
    ) -> ObjectHandle:
        """"""
    @classmethod
    @overload
    def CreateInstance(
        cls,
        assemblyName: str,
        typeName: str,
        ignoreCase: bool,
        bindingAttr: BindingFlags,
        binder: Binder,
        args: Array[object],
        culture: CultureInfo,
        activationAttributes: Array[object],
        securityInfo: Evidence,
    ) -> ObjectHandle:
        """"""
    @classmethod
    @overload
    def CreateInstance(cls, type: Type) -> object:
        """"""
    @classmethod
    @overload
    def CreateInstance(
        cls,
        type: Type,
        bindingAttr: BindingFlags,
        binder: Binder,
        args: Array[object],
        culture: CultureInfo,
    ) -> object:
        """"""
    @classmethod
    @overload
    def CreateInstance(
        cls,
        type: Type,
        bindingAttr: BindingFlags,
        binder: Binder,
        args: Array[object],
        culture: CultureInfo,
        activationAttributes: Array[object],
    ) -> object:
        """"""
    @classmethod
    @overload
    def CreateInstance(cls, type: Type, args: Array[object]) -> object:
        """"""
    @classmethod
    @overload
    def CreateInstance(
        cls, type: Type, args: Array[object], activationAttributes: Array[object]
    ) -> object:
        """"""
    @classmethod
    @overload
    def CreateInstance(cls, type: Type, nonPublic: bool) -> object:
        """"""
    @classmethod
    @overload
    def CreateInstanceFrom(
        cls, domain: AppDomain, assemblyFile: str, typeName: str
    ) -> ObjectHandle:
        """"""
    @classmethod
    @overload
    def CreateInstanceFrom(
        cls,
        domain: AppDomain,
        assemblyFile: str,
        typeName: str,
        ignoreCase: bool,
        bindingAttr: BindingFlags,
        binder: Binder,
        args: Array[object],
        culture: CultureInfo,
        activationAttributes: Array[object],
    ) -> ObjectHandle:
        """"""
    @classmethod
    @overload
    def CreateInstanceFrom(
        cls,
        domain: AppDomain,
        assemblyFile: str,
        typeName: str,
        ignoreCase: bool,
        bindingAttr: BindingFlags,
        binder: Binder,
        args: Array[object],
        culture: CultureInfo,
        activationAttributes: Array[object],
        securityAttributes: Evidence,
    ) -> ObjectHandle:
        """"""
    @classmethod
    @overload
    def CreateInstanceFrom(cls, assemblyFile: str, typeName: str) -> ObjectHandle:
        """"""
    @classmethod
    @overload
    def CreateInstanceFrom(
        cls, assemblyFile: str, typeName: str, activationAttributes: Array[object]
    ) -> ObjectHandle:
        """"""
    @classmethod
    @overload
    def CreateInstanceFrom(
        cls,
        assemblyFile: str,
        typeName: str,
        ignoreCase: bool,
        bindingAttr: BindingFlags,
        binder: Binder,
        args: Array[object],
        culture: CultureInfo,
        activationAttributes: Array[object],
    ) -> ObjectHandle:
        """"""
    @classmethod
    @overload
    def CreateInstanceFrom(
        cls,
        assemblyFile: str,
        typeName: str,
        ignoreCase: bool,
        bindingAttr: BindingFlags,
        binder: Binder,
        args: Array[object],
        culture: CultureInfo,
        activationAttributes: Array[object],
        securityInfo: Evidence,
    ) -> ObjectHandle:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    @classmethod
    @overload
    def GetObject(cls, type: Type, url: str) -> object:
        """"""
    @classmethod
    @overload
    def GetObject(cls, type: Type, url: str, state: object) -> object:
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
    def ToString(self) -> str:
        """"""

class AggregateException(Exception, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
        """"""
    @overload
    def __init__(self, innerExceptions: IEnumerable[Exception]) -> None:
        """"""
    @overload
    def __init__(self, innerExceptions: Array[Exception]) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerExceptions: IEnumerable[Exception]) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerExceptions: Array[Exception]) -> None:
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
    def InnerExceptions(self) -> ReadOnlyCollection[Exception]:
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
    def Flatten(self) -> AggregateException:
        """"""
    def GetBaseException(self) -> Exception:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def Handle(self, predicate: Func[Exception, bool]) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class AppContext(ABC, Object):
    """"""
    @classmethod
    @property
    def BaseDirectory(cls) -> str:
        """"""
    @classmethod
    @property
    def TargetFrameworkName(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetData(cls, name: str) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def SetSwitch(cls, switchName: str, isEnabled: bool) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def TryGetSwitch(cls, switchName: str, isEnabled: Boolean) -> tuple[bool, Boolean]:
        """"""

class AppContextDefaultValues(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def PopulateDefaultValues(cls) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def TryGetSwitchOverride(cls, switchName: str, overrideValue: Boolean) -> tuple[bool, Boolean]:
        """"""

class AppContextSwitches(ABC, Object):
    """"""
    @classmethod
    @property
    def BlockLongPaths(cls) -> bool:
        """"""
    @classmethod
    @property
    def DoNotAddrOfCspParentWindowHandle(cls) -> bool:
        """"""
    @classmethod
    @property
    def DoNotMarshalOutByrefSafeArrayOnInvoke(cls) -> bool:
        """"""
    @classmethod
    @property
    def EnforceJapaneseEraYearRanges(cls) -> bool:
        """"""
    @classmethod
    @property
    def EnforceLegacyJapaneseDateParsing(cls) -> bool:
        """"""
    @classmethod
    @property
    def FormatJapaneseFirstYearAsANumber(cls) -> bool:
        """"""
    @classmethod
    @property
    def IgnorePortablePDBsInStackTraces(cls) -> bool:
        """"""
    @classmethod
    @property
    def NoAsyncCurrentCulture(cls) -> bool:
        """"""
    @classmethod
    @property
    def PreserveEventListnerObjectIdentity(cls) -> bool:
        """"""
    @classmethod
    @property
    def SetActorAsReferenceWhenCopyingClaimsIdentity(cls) -> bool:
        """"""
    @classmethod
    @property
    def ThrowExceptionIfDisposedCancellationTokenSource(cls) -> bool:
        """"""
    @classmethod
    @property
    def UseConcurrentFormatterTypeCache(cls) -> bool:
        """"""
    @classmethod
    @property
    def UseLegacyExecutionContextBehaviorUponUndoFailure(cls) -> bool:
        """"""
    @classmethod
    @property
    def UseLegacyFipsThrow(cls) -> bool:
        """"""
    @classmethod
    @property
    def UseLegacyPathHandling(cls) -> bool:
        """"""
    @classmethod
    @property
    def UseNetCoreTimer(cls) -> bool:
        """"""
    @classmethod
    @property
    def UseNewMaxArraySize(cls) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class AppDomain(MarshalByRefObject, IEvidenceFactory, _AppDomain):
    """"""
    @property
    def ActivationContext(self) -> ActivationContext:
        """"""
    @property
    def ApplicationIdentity(self) -> ApplicationIdentity:
        """"""
    @property
    def ApplicationTrust(self) -> ApplicationTrust:
        """"""
    @property
    def BaseDirectory(self) -> str:
        """"""
    @classmethod
    @property
    def CurrentDomain(cls) -> AppDomain:
        """"""
    @property
    def DomainManager(self) -> AppDomainManager:
        """"""
    @property
    def DynamicDirectory(self) -> str:
        """"""
    @property
    def Evidence(self) -> Evidence:
        """"""
    @property
    def FriendlyName(self) -> str:
        """"""
    @property
    def Id(self) -> int:
        """"""
    @property
    def IsFullyTrusted(self) -> bool:
        """"""
    @property
    def IsHomogenous(self) -> bool:
        """"""
    @classmethod
    @property
    def MonitoringIsEnabled(cls) -> bool:
        """"""
    @classmethod
    @MonitoringIsEnabled.setter
    def MonitoringIsEnabled(cls, value: bool) -> None: ...
    @property
    def MonitoringSurvivedMemorySize(self) -> int:
        """"""
    @classmethod
    @property
    def MonitoringSurvivedProcessMemorySize(cls) -> int:
        """"""
    @property
    def MonitoringTotalAllocatedMemorySize(self) -> int:
        """"""
    @property
    def MonitoringTotalProcessorTime(self) -> TimeSpan:
        """"""
    @property
    def PermissionSet(self) -> PermissionSet:
        """"""
    @property
    def RelativeSearchPath(self) -> str:
        """"""
    @property
    def SetupInformation(self) -> AppDomainSetup:
        """"""
    @property
    def ShadowCopyFiles(self) -> bool:
        """"""
    def AppendPrivatePath(self, path: str) -> None:
        """"""
    def ApplyPolicy(self, assemblyName: str) -> str:
        """"""
    def ClearPrivatePath(self) -> None:
        """"""
    def ClearShadowCopyPath(self) -> None:
        """"""
    @overload
    def CreateComInstanceFrom(self, assemblyName: str, typeName: str) -> ObjectHandle:
        """"""
    @overload
    def CreateComInstanceFrom(
        self,
        assemblyFile: str,
        typeName: str,
        hashValue: Array[int],
        hashAlgorithm: AssemblyHashAlgorithm,
    ) -> ObjectHandle:
        """"""
    @classmethod
    @overload
    def CreateDomain(cls, friendlyName: str) -> AppDomain:
        """"""
    @classmethod
    @overload
    def CreateDomain(cls, friendlyName: str, securityInfo: Evidence) -> AppDomain:
        """"""
    @classmethod
    @overload
    def CreateDomain(
        cls, friendlyName: str, securityInfo: Evidence, info: AppDomainSetup
    ) -> AppDomain:
        """"""
    @classmethod
    @overload
    def CreateDomain(
        cls,
        friendlyName: str,
        securityInfo: Evidence,
        info: AppDomainSetup,
        grantSet: PermissionSet,
        fullTrustAssemblies: Array[StrongName],
    ) -> AppDomain:
        """"""
    @classmethod
    @overload
    def CreateDomain(
        cls,
        friendlyName: str,
        securityInfo: Evidence,
        appBasePath: str,
        appRelativeSearchPath: str,
        shadowCopyFiles: bool,
    ) -> AppDomain:
        """"""
    @classmethod
    @overload
    def CreateDomain(
        cls,
        friendlyName: str,
        securityInfo: Evidence,
        appBasePath: str,
        appRelativeSearchPath: str,
        shadowCopyFiles: bool,
        adInit: AppDomainInitializer,
        adInitArgs: Array[str],
    ) -> AppDomain:
        """"""
    @overload
    def CreateInstance(self, assemblyName: str, typeName: str) -> ObjectHandle:
        """"""
    @overload
    def CreateInstance(
        self, assemblyName: str, typeName: str, activationAttributes: Array[object]
    ) -> ObjectHandle:
        """"""
    @overload
    def CreateInstance(
        self,
        assemblyName: str,
        typeName: str,
        ignoreCase: bool,
        bindingAttr: BindingFlags,
        binder: Binder,
        args: Array[object],
        culture: CultureInfo,
        activationAttributes: Array[object],
    ) -> ObjectHandle:
        """"""
    @overload
    def CreateInstance(
        self,
        assemblyName: str,
        typeName: str,
        ignoreCase: bool,
        bindingAttr: BindingFlags,
        binder: Binder,
        args: Array[object],
        culture: CultureInfo,
        activationAttributes: Array[object],
        securityAttributes: Evidence,
    ) -> ObjectHandle:
        """"""
    @overload
    def CreateInstanceAndUnwrap(self, assemblyName: str, typeName: str) -> object:
        """"""
    @overload
    def CreateInstanceAndUnwrap(
        self, assemblyName: str, typeName: str, activationAttributes: Array[object]
    ) -> object:
        """"""
    @overload
    def CreateInstanceAndUnwrap(
        self,
        assemblyName: str,
        typeName: str,
        ignoreCase: bool,
        bindingAttr: BindingFlags,
        binder: Binder,
        args: Array[object],
        culture: CultureInfo,
        activationAttributes: Array[object],
    ) -> object:
        """"""
    @overload
    def CreateInstanceAndUnwrap(
        self,
        assemblyName: str,
        typeName: str,
        ignoreCase: bool,
        bindingAttr: BindingFlags,
        binder: Binder,
        args: Array[object],
        culture: CultureInfo,
        activationAttributes: Array[object],
        securityAttributes: Evidence,
    ) -> object:
        """"""
    @overload
    def CreateInstanceFrom(self, assemblyFile: str, typeName: str) -> ObjectHandle:
        """"""
    @overload
    def CreateInstanceFrom(
        self, assemblyFile: str, typeName: str, activationAttributes: Array[object]
    ) -> ObjectHandle:
        """"""
    @overload
    def CreateInstanceFrom(
        self,
        assemblyFile: str,
        typeName: str,
        ignoreCase: bool,
        bindingAttr: BindingFlags,
        binder: Binder,
        args: Array[object],
        culture: CultureInfo,
        activationAttributes: Array[object],
    ) -> ObjectHandle:
        """"""
    @overload
    def CreateInstanceFrom(
        self,
        assemblyFile: str,
        typeName: str,
        ignoreCase: bool,
        bindingAttr: BindingFlags,
        binder: Binder,
        args: Array[object],
        culture: CultureInfo,
        activationAttributes: Array[object],
        securityAttributes: Evidence,
    ) -> ObjectHandle:
        """"""
    @overload
    def CreateInstanceFromAndUnwrap(self, assemblyName: str, typeName: str) -> object:
        """"""
    @overload
    def CreateInstanceFromAndUnwrap(
        self, assemblyName: str, typeName: str, activationAttributes: Array[object]
    ) -> object:
        """"""
    @overload
    def CreateInstanceFromAndUnwrap(
        self,
        assemblyFile: str,
        typeName: str,
        ignoreCase: bool,
        bindingAttr: BindingFlags,
        binder: Binder,
        args: Array[object],
        culture: CultureInfo,
        activationAttributes: Array[object],
    ) -> object:
        """"""
    @overload
    def CreateInstanceFromAndUnwrap(
        self,
        assemblyName: str,
        typeName: str,
        ignoreCase: bool,
        bindingAttr: BindingFlags,
        binder: Binder,
        args: Array[object],
        culture: CultureInfo,
        activationAttributes: Array[object],
        securityAttributes: Evidence,
    ) -> object:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    @overload
    def DefineDynamicAssembly(
        self, name: AssemblyName, access: AssemblyBuilderAccess
    ) -> AssemblyBuilder:
        """"""
    @overload
    def DefineDynamicAssembly(
        self,
        name: AssemblyName,
        access: AssemblyBuilderAccess,
        assemblyAttributes: IEnumerable[CustomAttributeBuilder],
    ) -> AssemblyBuilder:
        """"""
    @overload
    def DefineDynamicAssembly(
        self,
        name: AssemblyName,
        access: AssemblyBuilderAccess,
        assemblyAttributes: IEnumerable[CustomAttributeBuilder],
        securityContextSource: SecurityContextSource,
    ) -> AssemblyBuilder:
        """"""
    @overload
    def DefineDynamicAssembly(
        self, name: AssemblyName, access: AssemblyBuilderAccess, evidence: Evidence
    ) -> AssemblyBuilder:
        """"""
    @overload
    def DefineDynamicAssembly(
        self,
        name: AssemblyName,
        access: AssemblyBuilderAccess,
        evidence: Evidence,
        requiredPermissions: PermissionSet,
        optionalPermissions: PermissionSet,
        refusedPermissions: PermissionSet,
    ) -> AssemblyBuilder:
        """"""
    @overload
    def DefineDynamicAssembly(
        self,
        name: AssemblyName,
        access: AssemblyBuilderAccess,
        requiredPermissions: PermissionSet,
        optionalPermissions: PermissionSet,
        refusedPermissions: PermissionSet,
    ) -> AssemblyBuilder:
        """"""
    @overload
    def DefineDynamicAssembly(
        self, name: AssemblyName, access: AssemblyBuilderAccess, dir: str
    ) -> AssemblyBuilder:
        """"""
    @overload
    def DefineDynamicAssembly(
        self, name: AssemblyName, access: AssemblyBuilderAccess, dir: str, evidence: Evidence
    ) -> AssemblyBuilder:
        """"""
    @overload
    def DefineDynamicAssembly(
        self,
        name: AssemblyName,
        access: AssemblyBuilderAccess,
        dir: str,
        evidence: Evidence,
        requiredPermissions: PermissionSet,
        optionalPermissions: PermissionSet,
        refusedPermissions: PermissionSet,
    ) -> AssemblyBuilder:
        """"""
    @overload
    def DefineDynamicAssembly(
        self,
        name: AssemblyName,
        access: AssemblyBuilderAccess,
        dir: str,
        evidence: Evidence,
        requiredPermissions: PermissionSet,
        optionalPermissions: PermissionSet,
        refusedPermissions: PermissionSet,
        isSynchronized: bool,
    ) -> AssemblyBuilder:
        """"""
    @overload
    def DefineDynamicAssembly(
        self,
        name: AssemblyName,
        access: AssemblyBuilderAccess,
        dir: str,
        evidence: Evidence,
        requiredPermissions: PermissionSet,
        optionalPermissions: PermissionSet,
        refusedPermissions: PermissionSet,
        isSynchronized: bool,
        assemblyAttributes: IEnumerable[CustomAttributeBuilder],
    ) -> AssemblyBuilder:
        """"""
    @overload
    def DefineDynamicAssembly(
        self,
        name: AssemblyName,
        access: AssemblyBuilderAccess,
        dir: str,
        requiredPermissions: PermissionSet,
        optionalPermissions: PermissionSet,
        refusedPermissions: PermissionSet,
    ) -> AssemblyBuilder:
        """"""
    @overload
    def DefineDynamicAssembly(
        self,
        name: AssemblyName,
        access: AssemblyBuilderAccess,
        dir: str,
        isSynchronized: bool,
        assemblyAttributes: IEnumerable[CustomAttributeBuilder],
    ) -> AssemblyBuilder:
        """"""
    def DoCallBack(self, callBackDelegate: CrossAppDomainDelegate) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def ExecuteAssembly(self, assemblyFile: str) -> int:
        """"""
    @overload
    def ExecuteAssembly(self, assemblyFile: str, assemblySecurity: Evidence) -> int:
        """"""
    @overload
    def ExecuteAssembly(
        self, assemblyFile: str, assemblySecurity: Evidence, args: Array[str]
    ) -> int:
        """"""
    @overload
    def ExecuteAssembly(
        self,
        assemblyFile: str,
        assemblySecurity: Evidence,
        args: Array[str],
        hashValue: Array[int],
        hashAlgorithm: AssemblyHashAlgorithm,
    ) -> int:
        """"""
    @overload
    def ExecuteAssembly(self, assemblyFile: str, args: Array[str]) -> int:
        """"""
    @overload
    def ExecuteAssembly(
        self,
        assemblyFile: str,
        args: Array[str],
        hashValue: Array[int],
        hashAlgorithm: AssemblyHashAlgorithm,
    ) -> int:
        """"""
    @overload
    def ExecuteAssemblyByName(
        self, assemblyName: AssemblyName, assemblySecurity: Evidence, args: Array[str]
    ) -> int:
        """"""
    @overload
    def ExecuteAssemblyByName(self, assemblyName: AssemblyName, args: Array[str]) -> int:
        """"""
    @overload
    def ExecuteAssemblyByName(self, assemblyName: str) -> int:
        """"""
    @overload
    def ExecuteAssemblyByName(self, assemblyName: str, assemblySecurity: Evidence) -> int:
        """"""
    @overload
    def ExecuteAssemblyByName(
        self, assemblyName: str, assemblySecurity: Evidence, args: Array[str]
    ) -> int:
        """"""
    @overload
    def ExecuteAssemblyByName(self, assemblyName: str, args: Array[str]) -> int:
        """"""
    def GetAssemblies(self) -> Array[Assembly]:
        """"""
    @classmethod
    def GetCurrentThreadId(cls) -> int:
        """"""
    def GetData(self, name: str) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def InitializeLifetimeService(self) -> object:
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
    def IsCompatibilitySwitchSet(self, value: str) -> bool | None:
        """"""
    def IsDefaultAppDomain(self) -> bool:
        """"""
    def IsFinalizingForUnload(self) -> bool:
        """"""
    @overload
    def Load(self, assemblyRef: AssemblyName) -> Assembly:
        """"""
    @overload
    def Load(self, assemblyRef: AssemblyName, assemblySecurity: Evidence) -> Assembly:
        """"""
    @overload
    def Load(self, rawAssembly: Array[int]) -> Assembly:
        """"""
    @overload
    def Load(self, rawAssembly: Array[int], rawSymbolStore: Array[int]) -> Assembly:
        """"""
    @overload
    def Load(
        self, rawAssembly: Array[int], rawSymbolStore: Array[int], securityEvidence: Evidence
    ) -> Assembly:
        """"""
    @overload
    def Load(self, assemblyString: str) -> Assembly:
        """"""
    @overload
    def Load(self, assemblyString: str, assemblySecurity: Evidence) -> Assembly:
        """"""
    def ReflectionOnlyGetAssemblies(self) -> Array[Assembly]:
        """"""
    def SetAppDomainPolicy(self, domainPolicy: PolicyLevel) -> None:
        """"""
    def SetCachePath(self, path: str) -> None:
        """"""
    @overload
    def SetData(self, name: str, data: object) -> None:
        """"""
    @overload
    def SetData(self, name: str, data: object, permission: IPermission) -> None:
        """"""
    def SetDynamicBase(self, path: str) -> None:
        """"""
    def SetPrincipalPolicy(self, policy: PrincipalPolicy) -> None:
        """"""
    def SetShadowCopyFiles(self) -> None:
        """"""
    def SetShadowCopyPath(self, path: str) -> None:
        """"""
    def SetThreadPrincipal(self, principal: IPrincipal) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def Unload(cls, domain: AppDomain) -> None:
        """"""
    AssemblyLoad: EventType[AssemblyLoadEventHandler] = ...
    """"""
    AssemblyResolve: EventType[ResolveEventHandler] = ...
    """"""
    DomainUnload: EventType[EventHandler] = ...
    """"""
    FirstChanceException: EventType[EventHandler[FirstChanceExceptionEventArgs]] = ...
    """"""
    ProcessExit: EventType[EventHandler] = ...
    """"""
    ReflectionOnlyAssemblyResolve: EventType[ResolveEventHandler] = ...
    """"""
    ResourceResolve: EventType[ResolveEventHandler] = ...
    """"""
    TypeResolve: EventType[ResolveEventHandler] = ...
    """"""
    UnhandledException: EventType[UnhandledExceptionEventHandler] = ...
    """"""

class AppDomainHandle(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

AppDomainInitializer: Callable[[Array[str]], None] = ...
""""""

class AppDomainInitializerInfo(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class AppDomainManager(MarshalByRefObject):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def ApplicationActivator(self) -> ApplicationActivator:
        """"""
    @property
    def EntryAssembly(self) -> Assembly:
        """"""
    @property
    def HostExecutionContextManager(self) -> HostExecutionContextManager:
        """"""
    @property
    def HostSecurityManager(self) -> HostSecurityManager:
        """"""
    @property
    def InitializationFlags(self) -> AppDomainManagerInitializationOptions:
        """"""
    @InitializationFlags.setter
    def InitializationFlags(self, value: AppDomainManagerInitializationOptions) -> None: ...
    def CheckSecuritySettings(self, state: SecurityState) -> bool:
        """"""
    def CreateDomain(
        self, friendlyName: str, securityInfo: Evidence, appDomainInfo: AppDomainSetup
    ) -> AppDomain:
        """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def InitializeLifetimeService(self) -> object:
        """"""
    def InitializeNewDomain(self, appDomainInfo: AppDomainSetup) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class AppDomainManagerInitializationOptions(Enum):
    """"""

    _None: AppDomainManagerInitializationOptions = ...
    """"""
    RegisterWithHost: AppDomainManagerInitializationOptions = ...
    """"""

class AppDomainPauseManager(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Paused(self) -> None:
        """"""
    def Pausing(self) -> None:
        """"""
    def Resumed(self) -> None:
        """"""
    def Resuming(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class AppDomainSetup(Object, IAppDomainSetup):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, activationContext: ActivationContext) -> None:
        """"""
    @overload
    def __init__(self, activationArguments: ActivationArguments) -> None:
        """"""
    @property
    def ActivationArguments(self) -> ActivationArguments:
        """"""
    @ActivationArguments.setter
    def ActivationArguments(self, value: ActivationArguments) -> None: ...
    @property
    def AppDomainInitializer(self) -> AppDomainInitializer:
        """"""
    @AppDomainInitializer.setter
    def AppDomainInitializer(self, value: AppDomainInitializer) -> None: ...
    @property
    def AppDomainInitializerArguments(self) -> Array[str]:
        """"""
    @AppDomainInitializerArguments.setter
    def AppDomainInitializerArguments(self, value: Array[str]) -> None: ...
    @property
    def AppDomainManagerAssembly(self) -> str:
        """"""
    @AppDomainManagerAssembly.setter
    def AppDomainManagerAssembly(self, value: str) -> None: ...
    @property
    def AppDomainManagerType(self) -> str:
        """"""
    @AppDomainManagerType.setter
    def AppDomainManagerType(self, value: str) -> None: ...
    @property
    def ApplicationBase(self) -> str:
        """"""
    @ApplicationBase.setter
    def ApplicationBase(self, value: str) -> None: ...
    @property
    def ApplicationName(self) -> str:
        """"""
    @ApplicationName.setter
    def ApplicationName(self, value: str) -> None: ...
    @property
    def ApplicationTrust(self) -> ApplicationTrust:
        """"""
    @ApplicationTrust.setter
    def ApplicationTrust(self, value: ApplicationTrust) -> None: ...
    @property
    def CachePath(self) -> str:
        """"""
    @CachePath.setter
    def CachePath(self, value: str) -> None: ...
    @property
    def ConfigurationFile(self) -> str:
        """"""
    @ConfigurationFile.setter
    def ConfigurationFile(self, value: str) -> None: ...
    @property
    def DisallowApplicationBaseProbing(self) -> bool:
        """"""
    @DisallowApplicationBaseProbing.setter
    def DisallowApplicationBaseProbing(self, value: bool) -> None: ...
    @property
    def DisallowBindingRedirects(self) -> bool:
        """"""
    @DisallowBindingRedirects.setter
    def DisallowBindingRedirects(self, value: bool) -> None: ...
    @property
    def DisallowCodeDownload(self) -> bool:
        """"""
    @DisallowCodeDownload.setter
    def DisallowCodeDownload(self, value: bool) -> None: ...
    @property
    def DisallowPublisherPolicy(self) -> bool:
        """"""
    @DisallowPublisherPolicy.setter
    def DisallowPublisherPolicy(self, value: bool) -> None: ...
    @property
    def DynamicBase(self) -> str:
        """"""
    @DynamicBase.setter
    def DynamicBase(self, value: str) -> None: ...
    @property
    def LicenseFile(self) -> str:
        """"""
    @LicenseFile.setter
    def LicenseFile(self, value: str) -> None: ...
    @property
    def LoaderOptimization(self) -> LoaderOptimization:
        """"""
    @LoaderOptimization.setter
    def LoaderOptimization(self, value: LoaderOptimization) -> None: ...
    @property
    def PartialTrustVisibleAssemblies(self) -> Array[str]:
        """"""
    @PartialTrustVisibleAssemblies.setter
    def PartialTrustVisibleAssemblies(self, value: Array[str]) -> None: ...
    @property
    def PrivateBinPath(self) -> str:
        """"""
    @PrivateBinPath.setter
    def PrivateBinPath(self, value: str) -> None: ...
    @property
    def PrivateBinPathProbe(self) -> str:
        """"""
    @PrivateBinPathProbe.setter
    def PrivateBinPathProbe(self, value: str) -> None: ...
    @property
    def SandboxInterop(self) -> bool:
        """"""
    @SandboxInterop.setter
    def SandboxInterop(self, value: bool) -> None: ...
    @property
    def ShadowCopyDirectories(self) -> str:
        """"""
    @ShadowCopyDirectories.setter
    def ShadowCopyDirectories(self, value: str) -> None: ...
    @property
    def ShadowCopyFiles(self) -> str:
        """"""
    @ShadowCopyFiles.setter
    def ShadowCopyFiles(self, value: str) -> None: ...
    @property
    def TargetFrameworkName(self) -> str:
        """"""
    @TargetFrameworkName.setter
    def TargetFrameworkName(self, value: str) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetConfigurationBytes(self) -> Array[int]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetCompatibilitySwitches(self, switches: IEnumerable[str]) -> None:
        """"""
    def SetConfigurationBytes(self, value: Array[int]) -> None:
        """"""
    def SetNativeFunction(
        self, functionName: str, functionVersion: int, functionPointer: IntPtr
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class AppDomainUnloadedException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
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

class ApplicationException(Exception, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
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

class ApplicationId(Object):
    """"""
    def __init__(
        self,
        publicKeyToken: Array[int],
        name: str,
        version: Version,
        processorArchitecture: str,
        culture: str,
    ) -> None:
        """"""
    @property
    def Culture(self) -> str:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def ProcessorArchitecture(self) -> str:
        """"""
    @property
    def PublicKeyToken(self) -> Array[int]:
        """"""
    @property
    def Version(self) -> Version:
        """"""
    def Copy(self) -> ApplicationId:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ApplicationIdentity(Object, ISerializable):
    """"""
    def __init__(self, applicationIdentityFullName: str) -> None:
        """"""
    @property
    def CodeBase(self) -> str:
        """"""
    @property
    def FullName(self) -> str:
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

class ArgIterator(ValueType):
    """"""
    @overload
    def __init__(self, arglist: RuntimeArgumentHandle) -> None:
        """"""
    @overload
    def __init__(self, arglist: RuntimeArgumentHandle, ptr: None) -> None:
        """"""
    def End(self) -> None:
        """"""
    def Equals(self, o: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetNextArg(self) -> TypedReference:
        """"""
    @overload
    def GetNextArg(self, rth: RuntimeTypeHandle) -> TypedReference:
        """"""
    def GetNextArgType(self) -> RuntimeTypeHandle:
        """"""
    def GetRemainingCount(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ArgumentException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
        """"""
    @overload
    def __init__(self, message: str, paramName: str, innerException: Exception) -> None:
        """"""
    @overload
    def __init__(self, message: str, paramName: str) -> None:
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
    def ParamName(self) -> str:
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

class ArgumentNullException(ArgumentException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, paramName: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
        """"""
    @overload
    def __init__(self, paramName: str, message: str) -> None:
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
    def ParamName(self) -> str:
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

class ArgumentOutOfRangeException(ArgumentException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, paramName: str) -> None:
        """"""
    @overload
    def __init__(self, paramName: str, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
        """"""
    @overload
    def __init__(self, paramName: str, actualValue: object, message: str) -> None:
        """"""
    @property
    def ActualValue(self) -> object:
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
    def ParamName(self) -> str:
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

class ArithmeticException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
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

class Array(
    ABC,
    Object,
    ICollection,
    IEnumerable,
    IList,
    IStructuralComparable,
    IStructuralEquatable,
    ICloneable,
):
    """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsFixedSize(self) -> bool:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def IsSynchronized(self) -> bool:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @Item.setter
    def Item(self, value: object) -> None: ...
    @property
    def Length(self) -> int:
        """"""
    @property
    def LongLength(self) -> int:
        """"""
    @property
    def Rank(self) -> int:
        """"""
    @property
    def SyncRoot(self) -> object:
        """"""
    def Add(self, value: object) -> int:
        """"""
    @classmethod
    def AsReadOnly(cls, array: Array[T]) -> ReadOnlyCollection[T]:
        """"""
    @classmethod
    @overload
    def BinarySearch(cls, array: Array, index: int, length: int, value: object) -> int:
        """"""
    @classmethod
    @overload
    def BinarySearch(
        cls, array: Array, index: int, length: int, value: object, comparer: IComparer
    ) -> int:
        """"""
    @classmethod
    @overload
    def BinarySearch(cls, array: Array, value: object) -> int:
        """"""
    @classmethod
    @overload
    def BinarySearch(cls, array: Array, value: object, comparer: IComparer) -> int:
        """"""
    @classmethod
    @overload
    def BinarySearch[T](cls, array: Array[T], value: T) -> int:
        """"""
    @classmethod
    @overload
    def BinarySearch[T](cls, array: Array[T], value: T, comparer: IComparer[T]) -> int:
        """"""
    @classmethod
    @overload
    def BinarySearch[T](cls, array: Array[T], index: int, length: int, value: T) -> int:
        """"""
    @classmethod
    @overload
    def BinarySearch[T](
        cls, array: Array[T], index: int, length: int, value: T, comparer: IComparer[T]
    ) -> int:
        """"""
    @overload
    def Clear(self) -> None:
        """"""
    @classmethod
    @overload
    def Clear(cls, array: Array, index: int, length: int) -> None:
        """"""
    def Clone(self) -> object:
        """"""
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """"""
    @classmethod
    def ConstrainedCopy(
        cls,
        sourceArray: Array,
        sourceIndex: int,
        destinationArray: Array,
        destinationIndex: int,
        length: int,
    ) -> None:
        """"""
    def Contains(self, value: object) -> bool:
        """"""
    @classmethod
    def ConvertAll[TInput, TOutput](
        cls, array: Array[TInput], converter: Converter[TInput, TOutput]
    ) -> Array[TOutput]:
        """"""
    @classmethod
    @overload
    def Copy(cls, sourceArray: Array, destinationArray: Array, length: int) -> None:
        """"""
    @classmethod
    @overload
    def Copy(cls, sourceArray: Array, destinationArray: Array, length: int) -> None:
        """"""
    @classmethod
    @overload
    def Copy(
        cls,
        sourceArray: Array,
        sourceIndex: int,
        destinationArray: Array,
        destinationIndex: int,
        length: int,
    ) -> None:
        """"""
    @classmethod
    @overload
    def Copy(
        cls,
        sourceArray: Array,
        sourceIndex: int,
        destinationArray: Array,
        destinationIndex: int,
        length: int,
    ) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @overload
    def CopyTo(self, array: Array, index: int) -> None:
        """"""
    @classmethod
    @overload
    def CreateInstance(cls, elementType: Type, lengths: Array[int]) -> Array:
        """"""
    @classmethod
    @overload
    def CreateInstance(
        cls, elementType: Type, lengths: Array[int], lowerBounds: Array[int]
    ) -> Array:
        """"""
    @classmethod
    @overload
    def CreateInstance(cls, elementType: Type, lengths: Array[int]) -> Array:
        """"""
    @classmethod
    @overload
    def CreateInstance(cls, elementType: Type, length: int) -> Array:
        """"""
    @classmethod
    @overload
    def CreateInstance(cls, elementType: Type, length1: int, length2: int) -> Array:
        """"""
    @classmethod
    @overload
    def CreateInstance(cls, elementType: Type, length1: int, length2: int, length3: int) -> Array:
        """"""
    @classmethod
    def Empty(cls) -> Array[T]:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """"""
    @classmethod
    def Exists(cls, array: Array[T], match: Predicate[T]) -> bool:
        """"""
    @classmethod
    def Find[T](cls, array: Array[T], match: Predicate[T]) -> T:
        """"""
    @classmethod
    def FindAll(cls, array: Array[T], match: Predicate[T]) -> Array[T]:
        """"""
    @classmethod
    @overload
    def FindIndex(cls, array: Array[T], startIndex: int, count: int, match: Predicate[T]) -> int:
        """"""
    @classmethod
    @overload
    def FindIndex(cls, array: Array[T], startIndex: int, match: Predicate[T]) -> int:
        """"""
    @classmethod
    @overload
    def FindIndex(cls, array: Array[T], match: Predicate[T]) -> int:
        """"""
    @classmethod
    def FindLast[T](cls, array: Array[T], match: Predicate[T]) -> T:
        """"""
    @classmethod
    @overload
    def FindLastIndex(
        cls, array: Array[T], startIndex: int, count: int, match: Predicate[T]
    ) -> int:
        """"""
    @classmethod
    @overload
    def FindLastIndex(cls, array: Array[T], startIndex: int, match: Predicate[T]) -> int:
        """"""
    @classmethod
    @overload
    def FindLastIndex(cls, array: Array[T], match: Predicate[T]) -> int:
        """"""
    @classmethod
    def ForEach(cls, array: Array[T], action: Action[T]) -> None:
        """"""
    def GetEnumerator(self) -> IEnumerator:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """"""
    def GetLength(self, dimension: int) -> int:
        """"""
    def GetLongLength(self, dimension: int) -> int:
        """"""
    def GetLowerBound(self, dimension: int) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetUpperBound(self, dimension: int) -> int:
        """"""
    @overload
    def GetValue(self, indices: Array[int]) -> object:
        """"""
    @overload
    def GetValue(self, indices: Array[int]) -> object:
        """"""
    @overload
    def GetValue(self, index: int) -> object:
        """"""
    @overload
    def GetValue(self, index1: int, index2: int) -> object:
        """"""
    @overload
    def GetValue(self, index1: int, index2: int, index3: int) -> object:
        """"""
    @overload
    def GetValue(self, index: int) -> object:
        """"""
    @overload
    def GetValue(self, index1: int, index2: int) -> object:
        """"""
    @overload
    def GetValue(self, index1: int, index2: int, index3: int) -> object:
        """"""
    @classmethod
    @overload
    def IndexOf(cls, array: Array, value: object) -> int:
        """"""
    @classmethod
    @overload
    def IndexOf(cls, array: Array, value: object, startIndex: int) -> int:
        """"""
    @classmethod
    @overload
    def IndexOf(cls, array: Array, value: object, startIndex: int, count: int) -> int:
        """"""
    @classmethod
    @overload
    def IndexOf[T](cls, array: Array[T], value: T) -> int:
        """"""
    @classmethod
    @overload
    def IndexOf[T](cls, array: Array[T], value: T, startIndex: int) -> int:
        """"""
    @classmethod
    @overload
    def IndexOf[T](cls, array: Array[T], value: T, startIndex: int, count: int) -> int:
        """"""
    @overload
    def IndexOf(self, value: object) -> int:
        """"""
    def Initialize(self) -> None:
        """"""
    def Insert(self, index: int, value: object) -> None:
        """"""
    @classmethod
    @overload
    def LastIndexOf(cls, array: Array, value: object) -> int:
        """"""
    @classmethod
    @overload
    def LastIndexOf(cls, array: Array, value: object, startIndex: int) -> int:
        """"""
    @classmethod
    @overload
    def LastIndexOf(cls, array: Array, value: object, startIndex: int, count: int) -> int:
        """"""
    @classmethod
    @overload
    def LastIndexOf[T](cls, array: Array[T], value: T) -> int:
        """"""
    @classmethod
    @overload
    def LastIndexOf[T](cls, array: Array[T], value: T, startIndex: int) -> int:
        """"""
    @classmethod
    @overload
    def LastIndexOf[T](cls, array: Array[T], value: T, startIndex: int, count: int) -> int:
        """"""
    def Remove(self, value: object) -> None:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    @classmethod
    def Resize(cls, array: T, newSize: int) -> None:
        """"""
    @classmethod
    @overload
    def Reverse(cls, array: Array) -> None:
        """"""
    @classmethod
    @overload
    def Reverse(cls, array: Array, index: int, length: int) -> None:
        """"""
    @overload
    def SetValue(self, value: object, indices: Array[int]) -> None:
        """"""
    @overload
    def SetValue(self, value: object, indices: Array[int]) -> None:
        """"""
    @overload
    def SetValue(self, value: object, index: int) -> None:
        """"""
    @overload
    def SetValue(self, value: object, index1: int, index2: int) -> None:
        """"""
    @overload
    def SetValue(self, value: object, index1: int, index2: int, index3: int) -> None:
        """"""
    @overload
    def SetValue(self, value: object, index: int) -> None:
        """"""
    @overload
    def SetValue(self, value: object, index1: int, index2: int) -> None:
        """"""
    @overload
    def SetValue(self, value: object, index1: int, index2: int, index3: int) -> None:
        """"""
    @classmethod
    @overload
    def Sort(cls, array: Array) -> None:
        """"""
    @classmethod
    @overload
    def Sort(cls, array: Array, comparer: IComparer) -> None:
        """"""
    @classmethod
    @overload
    def Sort(cls, keys: Array, items: Array) -> None:
        """"""
    @classmethod
    @overload
    def Sort(cls, keys: Array, items: Array, comparer: IComparer) -> None:
        """"""
    @classmethod
    @overload
    def Sort(cls, keys: Array, items: Array, index: int, length: int) -> None:
        """"""
    @classmethod
    @overload
    def Sort(cls, keys: Array, items: Array, index: int, length: int, comparer: IComparer) -> None:
        """"""
    @classmethod
    @overload
    def Sort(cls, array: Array, index: int, length: int) -> None:
        """"""
    @classmethod
    @overload
    def Sort(cls, array: Array, index: int, length: int, comparer: IComparer) -> None:
        """"""
    @classmethod
    @overload
    def Sort[TKey, TValue](cls, keys: Array[TKey], items: Array[TValue]) -> None:
        """"""
    @classmethod
    @overload
    def Sort(cls, keys: Array[TKey], items: Array[TValue], comparer: IComparer[TKey]) -> None:
        """"""
    @classmethod
    @overload
    def Sort(cls, keys: Array[TKey], items: Array[TValue], index: int, length: int) -> None:
        """"""
    @classmethod
    @overload
    def Sort(
        cls,
        keys: Array[TKey],
        items: Array[TValue],
        index: int,
        length: int,
        comparer: IComparer[TKey],
    ) -> None:
        """"""
    @classmethod
    @overload
    def Sort(cls, array: Array[T]) -> None:
        """"""
    @classmethod
    @overload
    def Sort(cls, array: Array[T], comparer: IComparer[T]) -> None:
        """"""
    @classmethod
    @overload
    def Sort(cls, array: Array[T], comparison: Comparison[T]) -> None:
        """"""
    @classmethod
    @overload
    def Sort(cls, array: Array[T], index: int, length: int) -> None:
        """"""
    @classmethod
    @overload
    def Sort(cls, array: Array[T], index: int, length: int, comparer: IComparer[T]) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def TrueForAll(cls, array: Array[T], match: Predicate[T]) -> bool:
        """"""
    def __contains__(self, value: object) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    def __delitem__(self, value: object) -> None:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__(self, index: int) -> object:
        """"""
    def __setitem__(self, index: int, value: object) -> None:
        """"""

class ArraySegment[T](
    ValueType,
    ICollection[T],
    IEnumerable[T],
    IList[T],
    IReadOnlyCollection[T],
    IReadOnlyList[T],
    IEnumerable,
):
    """"""
    @overload
    def __init__(self, array: Array[T]) -> None:
        """"""
    @overload
    def __init__(self, array: Array[T], offset: int, count: int) -> None:
        """"""
    @property
    def Array(self) -> Array[T]:
        """"""
    @property
    def Count(self) -> int:
        """"""
    @property
    def IsReadOnly(self) -> bool:
        """"""
    @property
    def Item(self) -> T:
        """"""
    @Item.setter
    def Item(self, value: T) -> None: ...
    @property
    def Offset(self) -> int:
        """"""
    def Add[T](self, item: T) -> None:
        """"""
    def Clear(self) -> None:
        """"""
    def Contains[T](self, item: T) -> bool:
        """"""
    def CopyTo(self, array: Array[T], arrayIndex: int) -> None:
        """"""
    @overload
    def Equals(self, obj: ArraySegment[T]) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetEnumerator(self) -> IEnumerator[T]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def IndexOf[T](self, item: T) -> int:
        """"""
    def Insert[T](self, index: int, item: T) -> None:
        """"""
    def Remove[T](self, item: T) -> bool:
        """"""
    def RemoveAt(self, index: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, a: ArraySegment[T], b: ArraySegment[T]) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, a: ArraySegment[T], b: ArraySegment[T]) -> bool:
        """"""
    def __contains__[T](self, item: T) -> bool:
        """"""
    def __iter__(self) -> Iterator[T]:
        """"""
    def __delitem__[T](self, item: T) -> bool:
        """"""
    def __len__(self) -> int:
        """"""
    def __getitem__[T](self, index: int) -> T:
        """"""
    def __eq__(self, other: ArraySegment[T]) -> bool:
        """"""
    def __ne__(self, other: ArraySegment[T]) -> bool:
        """"""
    def __setitem__[T](self, index: int, value: T) -> None:
        """"""

class ArrayTypeMismatchException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
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

class AssemblyLoadEventArgs(EventArgs):
    """"""
    def __init__(self, loadedAssembly: Assembly) -> None:
        """"""
    @property
    def LoadedAssembly(self) -> Assembly:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

AssemblyLoadEventHandler: Callable[[object, AssemblyLoadEventArgs], None] = ...
""""""
AsyncCallback: Callable[[IAsyncResult], None] = ...
""""""

class Attribute(ABC, Object, _Attribute):
    """"""
    @property
    def TypeId(self) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    @overload
    def GetCustomAttribute(cls, element: Assembly, attributeType: Type) -> Attribute:
        """"""
    @classmethod
    @overload
    def GetCustomAttribute(cls, element: Assembly, attributeType: Type, inherit: bool) -> Attribute:
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
    def GetCustomAttribute(cls, element: Module, attributeType: Type) -> Attribute:
        """"""
    @classmethod
    @overload
    def GetCustomAttribute(cls, element: Module, attributeType: Type, inherit: bool) -> Attribute:
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
    def GetCustomAttributes(cls, element: Assembly) -> Array[Attribute]:
        """"""
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: Assembly, inherit: bool) -> Array[Attribute]:
        """"""
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: Assembly, attributeType: Type) -> Array[Attribute]:
        """"""
    @classmethod
    @overload
    def GetCustomAttributes(
        cls, element: Assembly, attributeType: Type, inherit: bool
    ) -> Array[Attribute]:
        """"""
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: MemberInfo) -> Array[Attribute]:
        """"""
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: MemberInfo, inherit: bool) -> Array[Attribute]:
        """"""
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: MemberInfo, type: Type) -> Array[Attribute]:
        """"""
    @classmethod
    @overload
    def GetCustomAttributes(
        cls, element: MemberInfo, type: Type, inherit: bool
    ) -> Array[Attribute]:
        """"""
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: Module) -> Array[Attribute]:
        """"""
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: Module, inherit: bool) -> Array[Attribute]:
        """"""
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: Module, attributeType: Type) -> Array[Attribute]:
        """"""
    @classmethod
    @overload
    def GetCustomAttributes(
        cls, element: Module, attributeType: Type, inherit: bool
    ) -> Array[Attribute]:
        """"""
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: ParameterInfo) -> Array[Attribute]:
        """"""
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: ParameterInfo, inherit: bool) -> Array[Attribute]:
        """"""
    @classmethod
    @overload
    def GetCustomAttributes(cls, element: ParameterInfo, attributeType: Type) -> Array[Attribute]:
        """"""
    @classmethod
    @overload
    def GetCustomAttributes(
        cls, element: ParameterInfo, attributeType: Type, inherit: bool
    ) -> Array[Attribute]:
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
    @classmethod
    @overload
    def IsDefined(cls, element: Assembly, attributeType: Type) -> bool:
        """"""
    @classmethod
    @overload
    def IsDefined(cls, element: Assembly, attributeType: Type, inherit: bool) -> bool:
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
    def IsDefined(cls, element: Module, attributeType: Type, inherit: bool) -> bool:
        """"""
    @classmethod
    @overload
    def IsDefined(cls, element: ParameterInfo, attributeType: Type) -> bool:
        """"""
    @classmethod
    @overload
    def IsDefined(cls, element: ParameterInfo, attributeType: Type, inherit: bool) -> bool:
        """"""
    def Match(self, obj: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class AttributeTargets(Enum):
    """"""

    Assembly: AttributeTargets = ...
    """"""
    Module: AttributeTargets = ...
    """"""
    Class: AttributeTargets = ...
    """"""
    Struct: AttributeTargets = ...
    """"""
    Enum: AttributeTargets = ...
    """"""
    Constructor: AttributeTargets = ...
    """"""
    Method: AttributeTargets = ...
    """"""
    Property: AttributeTargets = ...
    """"""
    Field: AttributeTargets = ...
    """"""
    Event: AttributeTargets = ...
    """"""
    Interface: AttributeTargets = ...
    """"""
    Parameter: AttributeTargets = ...
    """"""
    Delegate: AttributeTargets = ...
    """"""
    ReturnValue: AttributeTargets = ...
    """"""
    GenericParameter: AttributeTargets = ...
    """"""
    All: AttributeTargets = ...
    """"""

class AttributeUsageAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, validOn: AttributeTargets) -> None:
        """"""
    @property
    def AllowMultiple(self) -> bool:
        """"""
    @AllowMultiple.setter
    def AllowMultiple(self, value: bool) -> None: ...
    @property
    def Inherited(self) -> bool:
        """"""
    @Inherited.setter
    def Inherited(self, value: bool) -> None: ...
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def ValidOn(self) -> AttributeTargets:
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

class BCLDebug(ABC, Object):
    """"""
    @classmethod
    def Assert(cls, condition: bool, message: str) -> None:
        """"""
    @classmethod
    def DumpStack(cls, switchName: str) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def Log(cls, message: str) -> None:
        """"""
    @classmethod
    @overload
    def Log(cls, switchName: str, level: LogLevel, messages: Array[object]) -> None:
        """"""
    @classmethod
    @overload
    def Log(cls, switchName: str, message: str) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    @overload
    def Trace(cls, switchName: str, messages: Array[object]) -> None:
        """"""
    @classmethod
    @overload
    def Trace(cls, switchName: str, format: str, messages: Array[object]) -> None:
        """"""

class BadImageFormatException(SystemException, _Exception, ISerializable):
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
    @overload
    def __init__(self, message: str, fileName: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, fileName: str, inner: Exception) -> None:
        """"""
    @property
    def Data(self) -> IDictionary:
        """"""
    @property
    def FileName(self) -> str:
        """"""
    @property
    def FusionLog(self) -> str:
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

class Base64FormattingOptions(Enum):
    """"""

    _None: Base64FormattingOptions = ...
    """"""
    InsertLineBreaks: Base64FormattingOptions = ...
    """"""

class BaseConfigHandler(ABC, Object):
    """"""
    def __init__(self) -> None:
        """"""
    def BeginChildren(
        self,
        size: int,
        subType: ConfigNodeSubType,
        nType: ConfigNodeType,
        terminal: int,
        text: str,
        textLength: int,
        prefixLength: int,
    ) -> None:
        """"""
    def CreateAttribute(
        self,
        size: int,
        subType: ConfigNodeSubType,
        nType: ConfigNodeType,
        terminal: int,
        text: str,
        textLength: int,
        prefixLength: int,
    ) -> None:
        """"""
    def CreateNode(
        self,
        size: int,
        subType: ConfigNodeSubType,
        nType: ConfigNodeType,
        terminal: int,
        text: str,
        textLength: int,
        prefixLength: int,
    ) -> None:
        """"""
    def EndChildren(
        self,
        fEmpty: int,
        size: int,
        subType: ConfigNodeSubType,
        nType: ConfigNodeType,
        terminal: int,
        text: str,
        textLength: int,
        prefixLength: int,
    ) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Error(
        self,
        size: int,
        subType: ConfigNodeSubType,
        nType: ConfigNodeType,
        terminal: int,
        text: str,
        textLength: int,
        prefixLength: int,
    ) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def NotifyEvent(self, nEvent: ConfigEvents) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class BitConverter(ABC, Object):
    """"""

    IsLittleEndian: ClassVar[bool]
    """"""
    @classmethod
    def DoubleToInt64Bits(cls, value: float) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    @overload
    def GetBytes(cls, value: bool) -> Array[int]:
        """"""
    @classmethod
    @overload
    def GetBytes(cls, value: Char) -> Array[int]:
        """"""
    @classmethod
    @overload
    def GetBytes(cls, value: float) -> Array[int]:
        """"""
    @classmethod
    @overload
    def GetBytes(cls, value: int) -> Array[int]:
        """"""
    @classmethod
    @overload
    def GetBytes(cls, value: int) -> Array[int]:
        """"""
    @classmethod
    @overload
    def GetBytes(cls, value: int) -> Array[int]:
        """"""
    @classmethod
    @overload
    def GetBytes(cls, value: float) -> Array[int]:
        """"""
    @classmethod
    @overload
    def GetBytes(cls, value: int) -> Array[int]:
        """"""
    @classmethod
    @overload
    def GetBytes(cls, value: int) -> Array[int]:
        """"""
    @classmethod
    @overload
    def GetBytes(cls, value: int) -> Array[int]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Int64BitsToDouble(cls, value: int) -> float:
        """"""
    @classmethod
    def ToBoolean(cls, value: Array[int], startIndex: int) -> bool:
        """"""
    @classmethod
    def ToChar(cls, value: Array[int], startIndex: int) -> Char:
        """"""
    @classmethod
    def ToDouble(cls, value: Array[int], startIndex: int) -> float:
        """"""
    @classmethod
    def ToInt16(cls, value: Array[int], startIndex: int) -> int:
        """"""
    @classmethod
    def ToInt32(cls, value: Array[int], startIndex: int) -> int:
        """"""
    @classmethod
    def ToInt64(cls, value: Array[int], startIndex: int) -> int:
        """"""
    @classmethod
    def ToSingle(cls, value: Array[int], startIndex: int) -> float:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: Array[int]) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: Array[int], startIndex: int) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: Array[int], startIndex: int, length: int) -> str:
        """"""
    @classmethod
    def ToUInt16(cls, value: Array[int], startIndex: int) -> int:
        """"""
    @classmethod
    def ToUInt32(cls, value: Array[int], startIndex: int) -> int:
        """"""
    @classmethod
    def ToUInt64(cls, value: Array[int], startIndex: int) -> int:
        """"""

class Boolean(ValueType, IComparable, IComparable[Boolean], IConvertible, IEquatable[Boolean]):
    """"""

    FalseString: ClassVar[str]
    """"""
    TrueString: ClassVar[str]
    """"""
    @overload
    def CompareTo(self, value: bool) -> int:
        """"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """"""
    @overload
    def Equals(self, obj: bool) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeCode(self) -> TypeCode:
        """"""
    @classmethod
    def Parse(cls, value: str) -> bool:
        """"""
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """"""
    def ToByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToChar(self, provider: IFormatProvider) -> Char:
        """"""
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """"""
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """"""
    def ToDouble(self, provider: IFormatProvider) -> float:
        """"""
    def ToInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt64(self, provider: IFormatProvider) -> int:
        """"""
    def ToSByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToSingle(self, provider: IFormatProvider) -> float:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """"""
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """"""
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    def TryParse(cls, value: str, result: Boolean) -> tuple[bool, Boolean]:
        """"""

class Buffer(ABC, Object):
    """"""
    @classmethod
    def BlockCopy(cls, src: Array, srcOffset: int, dst: Array, dstOffset: int, count: int) -> None:
        """"""
    @classmethod
    def ByteLength(cls, array: Array) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetByte(cls, array: Array, index: int) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def MemoryCopy(
        cls, source: None, destination: None, destinationSizeInBytes: int, sourceBytesToCopy: int
    ) -> None:
        """"""
    @classmethod
    @overload
    def MemoryCopy(
        cls, source: None, destination: None, destinationSizeInBytes: int, sourceBytesToCopy: int
    ) -> None:
        """"""
    @classmethod
    def SetByte(cls, array: Array, index: int, value: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class Byte(ValueType, IComparable, IComparable[Byte], IConvertible, IEquatable[Byte], IFormattable):
    """"""

    MaxValue: ClassVar[int]
    """"""
    MinValue: ClassVar[int]
    """"""
    @overload
    def CompareTo(self, value: int) -> int:
        """"""
    @overload
    def CompareTo(self, value: object) -> int:
        """"""
    @overload
    def Equals(self, obj: int) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeCode(self) -> TypeCode:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str) -> int:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles) -> int:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, provider: IFormatProvider) -> int:
        """"""
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """"""
    def ToByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToChar(self, provider: IFormatProvider) -> Char:
        """"""
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """"""
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """"""
    def ToDouble(self, provider: IFormatProvider) -> float:
        """"""
    def ToInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt64(self, provider: IFormatProvider) -> int:
        """"""
    def ToSByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToSingle(self, provider: IFormatProvider) -> float:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """"""
    @overload
    def ToString(self, format: str) -> str:
        """"""
    @overload
    def ToString(self, format: str, provider: IFormatProvider) -> str:
        """"""
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """"""
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def TryParse(
        cls, s: str, style: NumberStyles, provider: IFormatProvider, result: Byte
    ) -> tuple[bool, Byte]:
        """"""
    @classmethod
    @overload
    def TryParse(cls, s: str, result: Byte) -> tuple[bool, Byte]:
        """"""

class CLRConfig(Object):
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

class CLSCompliantAttribute(Attribute, _Attribute):
    """"""
    def __init__(self, isCompliant: bool) -> None:
        """"""
    @property
    def IsCompliant(self) -> bool:
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

class CannotUnloadAppDomainException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
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

class Char(ValueType, IComparable, IComparable[Char], IConvertible, IEquatable[Char]):
    """"""

    MaxValue: ClassVar[Char]
    """"""
    MinValue: ClassVar[Char]
    """"""
    @overload
    def CompareTo(self, value: Char) -> int:
        """"""
    @overload
    def CompareTo(self, value: object) -> int:
        """"""
    @classmethod
    def ConvertFromUtf32(cls, utf32: int) -> str:
        """"""
    @classmethod
    @overload
    def ConvertToUtf32(cls, highSurrogate: Char, lowSurrogate: Char) -> int:
        """"""
    @classmethod
    @overload
    def ConvertToUtf32(cls, s: str, index: int) -> int:
        """"""
    @overload
    def Equals(self, obj: Char) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    @overload
    def GetNumericValue(cls, c: Char) -> float:
        """"""
    @classmethod
    @overload
    def GetNumericValue(cls, s: str, index: int) -> float:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeCode(self) -> TypeCode:
        """"""
    @classmethod
    @overload
    def GetUnicodeCategory(cls, c: Char) -> UnicodeCategory:
        """"""
    @classmethod
    @overload
    def GetUnicodeCategory(cls, s: str, index: int) -> UnicodeCategory:
        """"""
    @classmethod
    @overload
    def IsControl(cls, c: Char) -> bool:
        """"""
    @classmethod
    @overload
    def IsControl(cls, s: str, index: int) -> bool:
        """"""
    @classmethod
    @overload
    def IsDigit(cls, c: Char) -> bool:
        """"""
    @classmethod
    @overload
    def IsDigit(cls, s: str, index: int) -> bool:
        """"""
    @classmethod
    @overload
    def IsHighSurrogate(cls, c: Char) -> bool:
        """"""
    @classmethod
    @overload
    def IsHighSurrogate(cls, s: str, index: int) -> bool:
        """"""
    @classmethod
    @overload
    def IsLetter(cls, c: Char) -> bool:
        """"""
    @classmethod
    @overload
    def IsLetter(cls, s: str, index: int) -> bool:
        """"""
    @classmethod
    @overload
    def IsLetterOrDigit(cls, c: Char) -> bool:
        """"""
    @classmethod
    @overload
    def IsLetterOrDigit(cls, s: str, index: int) -> bool:
        """"""
    @classmethod
    @overload
    def IsLowSurrogate(cls, c: Char) -> bool:
        """"""
    @classmethod
    @overload
    def IsLowSurrogate(cls, s: str, index: int) -> bool:
        """"""
    @classmethod
    @overload
    def IsLower(cls, c: Char) -> bool:
        """"""
    @classmethod
    @overload
    def IsLower(cls, s: str, index: int) -> bool:
        """"""
    @classmethod
    @overload
    def IsNumber(cls, c: Char) -> bool:
        """"""
    @classmethod
    @overload
    def IsNumber(cls, s: str, index: int) -> bool:
        """"""
    @classmethod
    @overload
    def IsPunctuation(cls, c: Char) -> bool:
        """"""
    @classmethod
    @overload
    def IsPunctuation(cls, s: str, index: int) -> bool:
        """"""
    @classmethod
    @overload
    def IsSeparator(cls, c: Char) -> bool:
        """"""
    @classmethod
    @overload
    def IsSeparator(cls, s: str, index: int) -> bool:
        """"""
    @classmethod
    @overload
    def IsSurrogate(cls, c: Char) -> bool:
        """"""
    @classmethod
    @overload
    def IsSurrogate(cls, s: str, index: int) -> bool:
        """"""
    @classmethod
    @overload
    def IsSurrogatePair(cls, highSurrogate: Char, lowSurrogate: Char) -> bool:
        """"""
    @classmethod
    @overload
    def IsSurrogatePair(cls, s: str, index: int) -> bool:
        """"""
    @classmethod
    @overload
    def IsSymbol(cls, c: Char) -> bool:
        """"""
    @classmethod
    @overload
    def IsSymbol(cls, s: str, index: int) -> bool:
        """"""
    @classmethod
    @overload
    def IsUpper(cls, c: Char) -> bool:
        """"""
    @classmethod
    @overload
    def IsUpper(cls, s: str, index: int) -> bool:
        """"""
    @classmethod
    @overload
    def IsWhiteSpace(cls, c: Char) -> bool:
        """"""
    @classmethod
    @overload
    def IsWhiteSpace(cls, s: str, index: int) -> bool:
        """"""
    @classmethod
    def Parse(cls, s: str) -> Char:
        """"""
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """"""
    def ToByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToChar(self, provider: IFormatProvider) -> Char:
        """"""
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """"""
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """"""
    def ToDouble(self, provider: IFormatProvider) -> float:
        """"""
    def ToInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt64(self, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def ToLower(cls, c: Char) -> Char:
        """"""
    @classmethod
    @overload
    def ToLower(cls, c: Char, culture: CultureInfo) -> Char:
        """"""
    @classmethod
    def ToLowerInvariant(cls, c: Char) -> Char:
        """"""
    def ToSByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToSingle(self, provider: IFormatProvider) -> float:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, c: Char) -> str:
        """"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """"""
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """"""
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def ToUpper(cls, c: Char) -> Char:
        """"""
    @classmethod
    @overload
    def ToUpper(cls, c: Char, culture: CultureInfo) -> Char:
        """"""
    @classmethod
    def ToUpperInvariant(cls, c: Char) -> Char:
        """"""
    @classmethod
    def TryParse(cls, s: str, result: Char) -> tuple[bool, Char]:
        """"""

class CharEnumerator(Object, IEnumerator[Char], IEnumerator, ICloneable, IDisposable):
    """"""
    @property
    def Current(self) -> Char:
        """"""
    def Clone(self) -> object:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def MoveNext(self) -> bool:
        """"""
    def Reset(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class ClientUtils(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetBitCount(cls, x: int) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsCriticalException(cls, ex: Exception) -> bool:
        """"""
    @classmethod
    @overload
    def IsEnumValid(cls, enumValue: Enum, value: int, minValue: int, maxValue: int) -> bool:
        """"""
    @classmethod
    @overload
    def IsEnumValid(
        cls, enumValue: Enum, value: int, minValue: int, maxValue: int, maxNumberOfBitsOn: int
    ) -> bool:
        """"""
    @classmethod
    def IsEnumValid_Masked(cls, enumValue: Enum, value: int, mask: int) -> bool:
        """"""
    @classmethod
    def IsEnumValid_NotSequential(cls, enumValue: Enum, value: int, enumValues: Array[int]) -> bool:
        """"""
    @classmethod
    def IsSecurityOrCriticalException(cls, ex: Exception) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

Comparison: Callable[[T, T], int] = ...
""""""

class CompatibilityFlag(Enum):
    """"""

    SwallowUnhandledExceptions: CompatibilityFlag = ...
    """"""
    NullReferenceExceptionOnAV: CompatibilityFlag = ...
    """"""
    EagerlyGenerateRandomAsymmKeys: CompatibilityFlag = ...
    """"""
    FullTrustListAssembliesInGac: CompatibilityFlag = ...
    """"""
    DateTimeParseIgnorePunctuation: CompatibilityFlag = ...
    """"""
    OnlyGACDomainNeutral: CompatibilityFlag = ...
    """"""
    DisableReplacementCustomCulture: CompatibilityFlag = ...
    """"""

class CompatibilitySwitches(ABC, Object):
    """"""
    @classmethod
    @property
    def IsAppEarlierThanSilverlight4(cls) -> bool:
        """"""
    @classmethod
    @property
    def IsAppEarlierThanWindowsPhone8(cls) -> bool:
        """"""
    @classmethod
    @property
    def IsAppEarlierThanWindowsPhoneMango(cls) -> bool:
        """"""
    @classmethod
    @property
    def IsCompatibilityBehaviorDefined(cls) -> bool:
        """"""
    @classmethod
    @property
    def IsNetFx40LegacySecurityPolicy(cls) -> bool:
        """"""
    @classmethod
    @property
    def IsNetFx40TimeSpanLegacyFormatMode(cls) -> bool:
        """"""
    @classmethod
    @property
    def IsNetFx45LegacyManagedDeflateStream(cls) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ConfigEvents(Enum):
    """"""

    StartDocument: ConfigEvents = ...
    """"""
    StartDTD: ConfigEvents = ...
    """"""
    EndDTD: ConfigEvents = ...
    """"""
    StartDTDSubset: ConfigEvents = ...
    """"""
    EndDTDSubset: ConfigEvents = ...
    """"""
    EndProlog: ConfigEvents = ...
    """"""
    StartEntity: ConfigEvents = ...
    """"""
    EndEntity: ConfigEvents = ...
    """"""
    EndDocument: ConfigEvents = ...
    """"""
    DataAvailable: ConfigEvents = ...
    """"""
    LastEvent: ConfigEvents = ...
    """"""

class ConfigNode(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ConfigNodeSubType(Enum):
    """"""

    Version: ConfigNodeSubType = ...
    """"""
    Encoding: ConfigNodeSubType = ...
    """"""
    Standalone: ConfigNodeSubType = ...
    """"""
    NS: ConfigNodeSubType = ...
    """"""
    XMLSpace: ConfigNodeSubType = ...
    """"""
    XMLLang: ConfigNodeSubType = ...
    """"""
    System: ConfigNodeSubType = ...
    """"""
    Public: ConfigNodeSubType = ...
    """"""
    NData: ConfigNodeSubType = ...
    """"""
    AtCData: ConfigNodeSubType = ...
    """"""
    AtId: ConfigNodeSubType = ...
    """"""
    AtIdref: ConfigNodeSubType = ...
    """"""
    AtIdrefs: ConfigNodeSubType = ...
    """"""
    AtEntity: ConfigNodeSubType = ...
    """"""
    AtEntities: ConfigNodeSubType = ...
    """"""
    AtNmToken: ConfigNodeSubType = ...
    """"""
    AtNmTokens: ConfigNodeSubType = ...
    """"""
    AtNotation: ConfigNodeSubType = ...
    """"""
    AtRequired: ConfigNodeSubType = ...
    """"""
    AtImplied: ConfigNodeSubType = ...
    """"""
    AtFixed: ConfigNodeSubType = ...
    """"""
    PentityDecl: ConfigNodeSubType = ...
    """"""
    Empty: ConfigNodeSubType = ...
    """"""
    Any: ConfigNodeSubType = ...
    """"""
    Mixed: ConfigNodeSubType = ...
    """"""
    Sequence: ConfigNodeSubType = ...
    """"""
    Choice: ConfigNodeSubType = ...
    """"""
    Star: ConfigNodeSubType = ...
    """"""
    Plus: ConfigNodeSubType = ...
    """"""
    Questionmark: ConfigNodeSubType = ...
    """"""
    LastSubNodeType: ConfigNodeSubType = ...
    """"""

class ConfigNodeType(Enum):
    """"""

    Element: ConfigNodeType = ...
    """"""
    Attribute: ConfigNodeType = ...
    """"""
    Pi: ConfigNodeType = ...
    """"""
    XmlDecl: ConfigNodeType = ...
    """"""
    DocType: ConfigNodeType = ...
    """"""
    DTDAttribute: ConfigNodeType = ...
    """"""
    EntityDecl: ConfigNodeType = ...
    """"""
    ElementDecl: ConfigNodeType = ...
    """"""
    AttlistDecl: ConfigNodeType = ...
    """"""
    Notation: ConfigNodeType = ...
    """"""
    Group: ConfigNodeType = ...
    """"""
    IncludeSect: ConfigNodeType = ...
    """"""
    PCData: ConfigNodeType = ...
    """"""
    CData: ConfigNodeType = ...
    """"""
    IgnoreSect: ConfigNodeType = ...
    """"""
    Comment: ConfigNodeType = ...
    """"""
    EntityRef: ConfigNodeType = ...
    """"""
    Whitespace: ConfigNodeType = ...
    """"""
    Name: ConfigNodeType = ...
    """"""
    NMToken: ConfigNodeType = ...
    """"""
    String: ConfigNodeType = ...
    """"""
    Peref: ConfigNodeType = ...
    """"""
    Model: ConfigNodeType = ...
    """"""
    ATTDef: ConfigNodeType = ...
    """"""
    ATTType: ConfigNodeType = ...
    """"""
    ATTPresence: ConfigNodeType = ...
    """"""
    DTDSubset: ConfigNodeType = ...
    """"""
    LastNodeType: ConfigNodeType = ...
    """"""

class ConfigTreeParser(BaseConfigHandler):
    """"""
    def __init__(self) -> None:
        """"""
    def BeginChildren(
        self,
        size: int,
        subType: ConfigNodeSubType,
        nType: ConfigNodeType,
        terminal: int,
        text: str,
        textLength: int,
        prefixLength: int,
    ) -> None:
        """"""
    def CreateAttribute(
        self,
        size: int,
        subType: ConfigNodeSubType,
        nType: ConfigNodeType,
        terminal: int,
        text: str,
        textLength: int,
        prefixLength: int,
    ) -> None:
        """"""
    def CreateNode(
        self,
        size: int,
        subType: ConfigNodeSubType,
        nType: ConfigNodeType,
        terminal: int,
        text: str,
        textLength: int,
        prefixLength: int,
    ) -> None:
        """"""
    def EndChildren(
        self,
        fEmpty: int,
        size: int,
        subType: ConfigNodeSubType,
        nType: ConfigNodeType,
        terminal: int,
        text: str,
        textLength: int,
        prefixLength: int,
    ) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def Error(
        self,
        size: int,
        subType: ConfigNodeSubType,
        nType: ConfigNodeType,
        terminal: int,
        text: str,
        textLength: int,
        prefixLength: int,
    ) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def NotifyEvent(self, nEvent: ConfigEvents) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class Console(ABC, Object):
    """"""
    @classmethod
    @property
    def BackgroundColor(cls) -> ConsoleColor:
        """"""
    @classmethod
    @BackgroundColor.setter
    def BackgroundColor(cls, value: ConsoleColor) -> None: ...
    @classmethod
    @property
    def BufferHeight(cls) -> int:
        """"""
    @classmethod
    @BufferHeight.setter
    def BufferHeight(cls, value: int) -> None: ...
    @classmethod
    @property
    def BufferWidth(cls) -> int:
        """"""
    @classmethod
    @BufferWidth.setter
    def BufferWidth(cls, value: int) -> None: ...
    @classmethod
    @property
    def CapsLock(cls) -> bool:
        """"""
    @classmethod
    @property
    def CursorLeft(cls) -> int:
        """"""
    @classmethod
    @CursorLeft.setter
    def CursorLeft(cls, value: int) -> None: ...
    @classmethod
    @property
    def CursorSize(cls) -> int:
        """"""
    @classmethod
    @CursorSize.setter
    def CursorSize(cls, value: int) -> None: ...
    @classmethod
    @property
    def CursorTop(cls) -> int:
        """"""
    @classmethod
    @CursorTop.setter
    def CursorTop(cls, value: int) -> None: ...
    @classmethod
    @property
    def CursorVisible(cls) -> bool:
        """"""
    @classmethod
    @CursorVisible.setter
    def CursorVisible(cls, value: bool) -> None: ...
    @classmethod
    @property
    def Error(cls) -> TextWriter:
        """"""
    @classmethod
    @property
    def ForegroundColor(cls) -> ConsoleColor:
        """"""
    @classmethod
    @ForegroundColor.setter
    def ForegroundColor(cls, value: ConsoleColor) -> None: ...
    @classmethod
    @property
    def In(cls) -> TextReader:
        """"""
    @classmethod
    @property
    def InputEncoding(cls) -> Encoding:
        """"""
    @classmethod
    @InputEncoding.setter
    def InputEncoding(cls, value: Encoding) -> None: ...
    @classmethod
    @property
    def IsErrorRedirected(cls) -> bool:
        """"""
    @classmethod
    @property
    def IsInputRedirected(cls) -> bool:
        """"""
    @classmethod
    @property
    def IsOutputRedirected(cls) -> bool:
        """"""
    @classmethod
    @property
    def KeyAvailable(cls) -> bool:
        """"""
    @classmethod
    @property
    def LargestWindowHeight(cls) -> int:
        """"""
    @classmethod
    @property
    def LargestWindowWidth(cls) -> int:
        """"""
    @classmethod
    @property
    def NumberLock(cls) -> bool:
        """"""
    @classmethod
    @property
    def Out(cls) -> TextWriter:
        """"""
    @classmethod
    @property
    def OutputEncoding(cls) -> Encoding:
        """"""
    @classmethod
    @OutputEncoding.setter
    def OutputEncoding(cls, value: Encoding) -> None: ...
    @classmethod
    @property
    def Title(cls) -> str:
        """"""
    @classmethod
    @Title.setter
    def Title(cls, value: str) -> None: ...
    @classmethod
    @property
    def TreatControlCAsInput(cls) -> bool:
        """"""
    @classmethod
    @TreatControlCAsInput.setter
    def TreatControlCAsInput(cls, value: bool) -> None: ...
    @classmethod
    @property
    def WindowHeight(cls) -> int:
        """"""
    @classmethod
    @WindowHeight.setter
    def WindowHeight(cls, value: int) -> None: ...
    @classmethod
    @property
    def WindowLeft(cls) -> int:
        """"""
    @classmethod
    @WindowLeft.setter
    def WindowLeft(cls, value: int) -> None: ...
    @classmethod
    @property
    def WindowTop(cls) -> int:
        """"""
    @classmethod
    @WindowTop.setter
    def WindowTop(cls, value: int) -> None: ...
    @classmethod
    @property
    def WindowWidth(cls) -> int:
        """"""
    @classmethod
    @WindowWidth.setter
    def WindowWidth(cls, value: int) -> None: ...
    @classmethod
    @overload
    def Beep(cls) -> None:
        """"""
    @classmethod
    @overload
    def Beep(cls, frequency: int, duration: int) -> None:
        """"""
    @classmethod
    def Clear(cls) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def MoveBufferArea(
        cls,
        sourceLeft: int,
        sourceTop: int,
        sourceWidth: int,
        sourceHeight: int,
        targetLeft: int,
        targetTop: int,
    ) -> None:
        """"""
    @classmethod
    @overload
    def MoveBufferArea(
        cls,
        sourceLeft: int,
        sourceTop: int,
        sourceWidth: int,
        sourceHeight: int,
        targetLeft: int,
        targetTop: int,
        sourceChar: Char,
        sourceForeColor: ConsoleColor,
        sourceBackColor: ConsoleColor,
    ) -> None:
        """"""
    @classmethod
    @overload
    def OpenStandardError(cls) -> Stream:
        """"""
    @classmethod
    @overload
    def OpenStandardError(cls, bufferSize: int) -> Stream:
        """"""
    @classmethod
    @overload
    def OpenStandardInput(cls) -> Stream:
        """"""
    @classmethod
    @overload
    def OpenStandardInput(cls, bufferSize: int) -> Stream:
        """"""
    @classmethod
    @overload
    def OpenStandardOutput(cls) -> Stream:
        """"""
    @classmethod
    @overload
    def OpenStandardOutput(cls, bufferSize: int) -> Stream:
        """"""
    @classmethod
    def Read(cls) -> int:
        """"""
    @classmethod
    @overload
    def ReadKey(cls) -> ConsoleKeyInfo:
        """"""
    @classmethod
    @overload
    def ReadKey(cls, intercept: bool) -> ConsoleKeyInfo:
        """"""
    @classmethod
    def ReadLine(cls) -> str:
        """"""
    @classmethod
    def ResetColor(cls) -> None:
        """"""
    @classmethod
    def SetBufferSize(cls, width: int, height: int) -> None:
        """"""
    @classmethod
    def SetCursorPosition(cls, left: int, top: int) -> None:
        """"""
    @classmethod
    def SetError(cls, newError: TextWriter) -> None:
        """"""
    @classmethod
    def SetIn(cls, newIn: TextReader) -> None:
        """"""
    @classmethod
    def SetOut(cls, newOut: TextWriter) -> None:
        """"""
    @classmethod
    def SetWindowPosition(cls, left: int, top: int) -> None:
        """"""
    @classmethod
    def SetWindowSize(cls, width: int, height: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    @overload
    def Write(cls, buffer: Array[Char]) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, buffer: Array[Char], index: int, count: int) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, value: bool) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, value: Char) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, value: Decimal) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, value: float) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, value: int) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, value: int) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, value: object) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, value: float) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, value: str) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, format: str, arg: Array[object]) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, format: str, arg0: object) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, format: str, arg0: object, arg1: object) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, format: str, arg0: object, arg1: object, arg2: object) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, format: str, arg0: object, arg1: object, arg2: object, arg3: object) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, value: int) -> None:
        """"""
    @classmethod
    @overload
    def Write(cls, value: int) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, buffer: Array[Char]) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, buffer: Array[Char], index: int, count: int) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, value: bool) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, value: Char) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, value: Decimal) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, value: float) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, value: int) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, value: int) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, value: object) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, value: float) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, value: str) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, format: str, arg: Array[object]) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, format: str, arg0: object) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, format: str, arg0: object, arg1: object) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, format: str, arg0: object, arg1: object, arg2: object) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, format: str, arg0: object, arg1: object, arg2: object, arg3: object) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, value: int) -> None:
        """"""
    @classmethod
    @overload
    def WriteLine(cls, value: int) -> None:
        """"""
    CancelKeyPress: EventType[ConsoleCancelEventHandler] = ...
    """"""

class ConsoleCancelEventArgs(EventArgs):
    """"""
    @property
    def Cancel(self) -> bool:
        """"""
    @Cancel.setter
    def Cancel(self, value: bool) -> None: ...
    @property
    def SpecialKey(self) -> ConsoleSpecialKey:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

ConsoleCancelEventHandler: Callable[[object, ConsoleCancelEventArgs], None] = ...
""""""

class ConsoleColor(Enum):
    """"""

    Black: ConsoleColor = ...
    """"""
    DarkBlue: ConsoleColor = ...
    """"""
    DarkGreen: ConsoleColor = ...
    """"""
    DarkCyan: ConsoleColor = ...
    """"""
    DarkRed: ConsoleColor = ...
    """"""
    DarkMagenta: ConsoleColor = ...
    """"""
    DarkYellow: ConsoleColor = ...
    """"""
    Gray: ConsoleColor = ...
    """"""
    DarkGray: ConsoleColor = ...
    """"""
    Blue: ConsoleColor = ...
    """"""
    Green: ConsoleColor = ...
    """"""
    Cyan: ConsoleColor = ...
    """"""
    Red: ConsoleColor = ...
    """"""
    Magenta: ConsoleColor = ...
    """"""
    Yellow: ConsoleColor = ...
    """"""
    White: ConsoleColor = ...
    """"""

class ConsoleKey(Enum):
    """"""

    Backspace: ConsoleKey = ...
    """"""
    Tab: ConsoleKey = ...
    """"""
    Clear: ConsoleKey = ...
    """"""
    Enter: ConsoleKey = ...
    """"""
    Pause: ConsoleKey = ...
    """"""
    Escape: ConsoleKey = ...
    """"""
    Spacebar: ConsoleKey = ...
    """"""
    PageUp: ConsoleKey = ...
    """"""
    PageDown: ConsoleKey = ...
    """"""
    End: ConsoleKey = ...
    """"""
    Home: ConsoleKey = ...
    """"""
    LeftArrow: ConsoleKey = ...
    """"""
    UpArrow: ConsoleKey = ...
    """"""
    RightArrow: ConsoleKey = ...
    """"""
    DownArrow: ConsoleKey = ...
    """"""
    Select: ConsoleKey = ...
    """"""
    Print: ConsoleKey = ...
    """"""
    Execute: ConsoleKey = ...
    """"""
    PrintScreen: ConsoleKey = ...
    """"""
    Insert: ConsoleKey = ...
    """"""
    Delete: ConsoleKey = ...
    """"""
    Help: ConsoleKey = ...
    """"""
    D0: ConsoleKey = ...
    """"""
    D1: ConsoleKey = ...
    """"""
    D2: ConsoleKey = ...
    """"""
    D3: ConsoleKey = ...
    """"""
    D4: ConsoleKey = ...
    """"""
    D5: ConsoleKey = ...
    """"""
    D6: ConsoleKey = ...
    """"""
    D7: ConsoleKey = ...
    """"""
    D8: ConsoleKey = ...
    """"""
    D9: ConsoleKey = ...
    """"""
    A: ConsoleKey = ...
    """"""
    B: ConsoleKey = ...
    """"""
    C: ConsoleKey = ...
    """"""
    D: ConsoleKey = ...
    """"""
    E: ConsoleKey = ...
    """"""
    F: ConsoleKey = ...
    """"""
    G: ConsoleKey = ...
    """"""
    H: ConsoleKey = ...
    """"""
    I: ConsoleKey = ...
    """"""
    J: ConsoleKey = ...
    """"""
    K: ConsoleKey = ...
    """"""
    L: ConsoleKey = ...
    """"""
    M: ConsoleKey = ...
    """"""
    N: ConsoleKey = ...
    """"""
    O: ConsoleKey = ...
    """"""
    P: ConsoleKey = ...
    """"""
    Q: ConsoleKey = ...
    """"""
    R: ConsoleKey = ...
    """"""
    S: ConsoleKey = ...
    """"""
    T: ConsoleKey = ...
    """"""
    U: ConsoleKey = ...
    """"""
    V: ConsoleKey = ...
    """"""
    W: ConsoleKey = ...
    """"""
    X: ConsoleKey = ...
    """"""
    Y: ConsoleKey = ...
    """"""
    Z: ConsoleKey = ...
    """"""
    LeftWindows: ConsoleKey = ...
    """"""
    RightWindows: ConsoleKey = ...
    """"""
    Applications: ConsoleKey = ...
    """"""
    Sleep: ConsoleKey = ...
    """"""
    NumPad0: ConsoleKey = ...
    """"""
    NumPad1: ConsoleKey = ...
    """"""
    NumPad2: ConsoleKey = ...
    """"""
    NumPad3: ConsoleKey = ...
    """"""
    NumPad4: ConsoleKey = ...
    """"""
    NumPad5: ConsoleKey = ...
    """"""
    NumPad6: ConsoleKey = ...
    """"""
    NumPad7: ConsoleKey = ...
    """"""
    NumPad8: ConsoleKey = ...
    """"""
    NumPad9: ConsoleKey = ...
    """"""
    Multiply: ConsoleKey = ...
    """"""
    Add: ConsoleKey = ...
    """"""
    Separator: ConsoleKey = ...
    """"""
    Subtract: ConsoleKey = ...
    """"""
    Decimal: ConsoleKey = ...
    """"""
    Divide: ConsoleKey = ...
    """"""
    F1: ConsoleKey = ...
    """"""
    F2: ConsoleKey = ...
    """"""
    F3: ConsoleKey = ...
    """"""
    F4: ConsoleKey = ...
    """"""
    F5: ConsoleKey = ...
    """"""
    F6: ConsoleKey = ...
    """"""
    F7: ConsoleKey = ...
    """"""
    F8: ConsoleKey = ...
    """"""
    F9: ConsoleKey = ...
    """"""
    F10: ConsoleKey = ...
    """"""
    F11: ConsoleKey = ...
    """"""
    F12: ConsoleKey = ...
    """"""
    F13: ConsoleKey = ...
    """"""
    F14: ConsoleKey = ...
    """"""
    F15: ConsoleKey = ...
    """"""
    F16: ConsoleKey = ...
    """"""
    F17: ConsoleKey = ...
    """"""
    F18: ConsoleKey = ...
    """"""
    F19: ConsoleKey = ...
    """"""
    F20: ConsoleKey = ...
    """"""
    F21: ConsoleKey = ...
    """"""
    F22: ConsoleKey = ...
    """"""
    F23: ConsoleKey = ...
    """"""
    F24: ConsoleKey = ...
    """"""
    BrowserBack: ConsoleKey = ...
    """"""
    BrowserForward: ConsoleKey = ...
    """"""
    BrowserRefresh: ConsoleKey = ...
    """"""
    BrowserStop: ConsoleKey = ...
    """"""
    BrowserSearch: ConsoleKey = ...
    """"""
    BrowserFavorites: ConsoleKey = ...
    """"""
    BrowserHome: ConsoleKey = ...
    """"""
    VolumeMute: ConsoleKey = ...
    """"""
    VolumeDown: ConsoleKey = ...
    """"""
    VolumeUp: ConsoleKey = ...
    """"""
    MediaNext: ConsoleKey = ...
    """"""
    MediaPrevious: ConsoleKey = ...
    """"""
    MediaStop: ConsoleKey = ...
    """"""
    MediaPlay: ConsoleKey = ...
    """"""
    LaunchMail: ConsoleKey = ...
    """"""
    LaunchMediaSelect: ConsoleKey = ...
    """"""
    LaunchApp1: ConsoleKey = ...
    """"""
    LaunchApp2: ConsoleKey = ...
    """"""
    Oem1: ConsoleKey = ...
    """"""
    OemPlus: ConsoleKey = ...
    """"""
    OemComma: ConsoleKey = ...
    """"""
    OemMinus: ConsoleKey = ...
    """"""
    OemPeriod: ConsoleKey = ...
    """"""
    Oem2: ConsoleKey = ...
    """"""
    Oem3: ConsoleKey = ...
    """"""
    Oem4: ConsoleKey = ...
    """"""
    Oem5: ConsoleKey = ...
    """"""
    Oem6: ConsoleKey = ...
    """"""
    Oem7: ConsoleKey = ...
    """"""
    Oem8: ConsoleKey = ...
    """"""
    Oem102: ConsoleKey = ...
    """"""
    Process: ConsoleKey = ...
    """"""
    Packet: ConsoleKey = ...
    """"""
    Attention: ConsoleKey = ...
    """"""
    CrSel: ConsoleKey = ...
    """"""
    ExSel: ConsoleKey = ...
    """"""
    EraseEndOfFile: ConsoleKey = ...
    """"""
    Play: ConsoleKey = ...
    """"""
    Zoom: ConsoleKey = ...
    """"""
    NoName: ConsoleKey = ...
    """"""
    Pa1: ConsoleKey = ...
    """"""
    OemClear: ConsoleKey = ...
    """"""

class ConsoleKeyInfo(ValueType):
    """"""
    def __init__(
        self, keyChar: Char, key: ConsoleKey, shift: bool, alt: bool, control: bool
    ) -> None:
        """"""
    @property
    def Key(self) -> ConsoleKey:
        """"""
    @property
    def KeyChar(self) -> Char:
        """"""
    @property
    def Modifiers(self) -> ConsoleModifiers:
        """"""
    @overload
    def Equals(self, obj: ConsoleKeyInfo) -> bool:
        """"""
    @overload
    def Equals(self, value: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, a: ConsoleKeyInfo, b: ConsoleKeyInfo) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, a: ConsoleKeyInfo, b: ConsoleKeyInfo) -> bool:
        """"""
    def __eq__(self, other: ConsoleKeyInfo) -> bool:
        """"""
    def __ne__(self, other: ConsoleKeyInfo) -> bool:
        """"""

class ConsoleModifiers(Enum):
    """"""

    Alt: ConsoleModifiers = ...
    """"""
    Shift: ConsoleModifiers = ...
    """"""
    Control: ConsoleModifiers = ...
    """"""

class ConsoleSpecialKey(Enum):
    """"""

    ControlC: ConsoleSpecialKey = ...
    """"""
    ControlBreak: ConsoleSpecialKey = ...
    """"""

class ContextBoundObject(ABC, MarshalByRefObject):
    """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Equals(self, obj: object) -> bool:
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

class ContextMarshalException(SystemException, _Exception, ISerializable):
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

class ContextStaticAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
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

class Convert(ABC, Object):
    """"""

    DBNull: ClassVar[object]
    """"""
    @classmethod
    @overload
    def ChangeType(cls, value: object, conversionType: Type) -> object:
        """"""
    @classmethod
    @overload
    def ChangeType(cls, value: object, conversionType: Type, provider: IFormatProvider) -> object:
        """"""
    @classmethod
    @overload
    def ChangeType(cls, value: object, typeCode: TypeCode) -> object:
        """"""
    @classmethod
    @overload
    def ChangeType(cls, value: object, typeCode: TypeCode, provider: IFormatProvider) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def FromBase64CharArray(cls, inArray: Array[Char], offset: int, length: int) -> Array[int]:
        """"""
    @classmethod
    def FromBase64String(cls, s: str) -> Array[int]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def GetTypeCode(cls, value: object) -> TypeCode:
        """"""
    @classmethod
    def IsDBNull(cls, value: object) -> bool:
        """"""
    @classmethod
    @overload
    def ToBase64CharArray(
        cls, inArray: Array[int], offsetIn: int, length: int, outArray: Array[Char], offsetOut: int
    ) -> int:
        """"""
    @classmethod
    @overload
    def ToBase64CharArray(
        cls,
        inArray: Array[int],
        offsetIn: int,
        length: int,
        outArray: Array[Char],
        offsetOut: int,
        options: Base64FormattingOptions,
    ) -> int:
        """"""
    @classmethod
    @overload
    def ToBase64String(cls, inArray: Array[int]) -> str:
        """"""
    @classmethod
    @overload
    def ToBase64String(cls, inArray: Array[int], options: Base64FormattingOptions) -> str:
        """"""
    @classmethod
    @overload
    def ToBase64String(cls, inArray: Array[int], offset: int, length: int) -> str:
        """"""
    @classmethod
    @overload
    def ToBase64String(
        cls, inArray: Array[int], offset: int, length: int, options: Base64FormattingOptions
    ) -> str:
        """"""
    @classmethod
    @overload
    def ToBoolean(cls, value: bool) -> bool:
        """"""
    @classmethod
    @overload
    def ToBoolean(cls, value: int) -> bool:
        """"""
    @classmethod
    @overload
    def ToBoolean(cls, value: Char) -> bool:
        """"""
    @classmethod
    @overload
    def ToBoolean(cls, value: DateTime) -> bool:
        """"""
    @classmethod
    @overload
    def ToBoolean(cls, value: Decimal) -> bool:
        """"""
    @classmethod
    @overload
    def ToBoolean(cls, value: float) -> bool:
        """"""
    @classmethod
    @overload
    def ToBoolean(cls, value: int) -> bool:
        """"""
    @classmethod
    @overload
    def ToBoolean(cls, value: int) -> bool:
        """"""
    @classmethod
    @overload
    def ToBoolean(cls, value: int) -> bool:
        """"""
    @classmethod
    @overload
    def ToBoolean(cls, value: object) -> bool:
        """"""
    @classmethod
    @overload
    def ToBoolean(cls, value: object, provider: IFormatProvider) -> bool:
        """"""
    @classmethod
    @overload
    def ToBoolean(cls, value: int) -> bool:
        """"""
    @classmethod
    @overload
    def ToBoolean(cls, value: float) -> bool:
        """"""
    @classmethod
    @overload
    def ToBoolean(cls, value: str) -> bool:
        """"""
    @classmethod
    @overload
    def ToBoolean(cls, value: str, provider: IFormatProvider) -> bool:
        """"""
    @classmethod
    @overload
    def ToBoolean(cls, value: int) -> bool:
        """"""
    @classmethod
    @overload
    def ToBoolean(cls, value: int) -> bool:
        """"""
    @classmethod
    @overload
    def ToBoolean(cls, value: int) -> bool:
        """"""
    @classmethod
    @overload
    def ToByte(cls, value: bool) -> int:
        """"""
    @classmethod
    @overload
    def ToByte(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToByte(cls, value: Char) -> int:
        """"""
    @classmethod
    @overload
    def ToByte(cls, value: DateTime) -> int:
        """"""
    @classmethod
    @overload
    def ToByte(cls, value: Decimal) -> int:
        """"""
    @classmethod
    @overload
    def ToByte(cls, value: float) -> int:
        """"""
    @classmethod
    @overload
    def ToByte(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToByte(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToByte(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToByte(cls, value: object) -> int:
        """"""
    @classmethod
    @overload
    def ToByte(cls, value: object, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def ToByte(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToByte(cls, value: float) -> int:
        """"""
    @classmethod
    @overload
    def ToByte(cls, value: str) -> int:
        """"""
    @classmethod
    @overload
    def ToByte(cls, value: str, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def ToByte(cls, value: str, fromBase: int) -> int:
        """"""
    @classmethod
    @overload
    def ToByte(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToByte(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToByte(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToChar(cls, value: bool) -> Char:
        """"""
    @classmethod
    @overload
    def ToChar(cls, value: int) -> Char:
        """"""
    @classmethod
    @overload
    def ToChar(cls, value: Char) -> Char:
        """"""
    @classmethod
    @overload
    def ToChar(cls, value: DateTime) -> Char:
        """"""
    @classmethod
    @overload
    def ToChar(cls, value: Decimal) -> Char:
        """"""
    @classmethod
    @overload
    def ToChar(cls, value: float) -> Char:
        """"""
    @classmethod
    @overload
    def ToChar(cls, value: int) -> Char:
        """"""
    @classmethod
    @overload
    def ToChar(cls, value: int) -> Char:
        """"""
    @classmethod
    @overload
    def ToChar(cls, value: int) -> Char:
        """"""
    @classmethod
    @overload
    def ToChar(cls, value: object) -> Char:
        """"""
    @classmethod
    @overload
    def ToChar(cls, value: object, provider: IFormatProvider) -> Char:
        """"""
    @classmethod
    @overload
    def ToChar(cls, value: int) -> Char:
        """"""
    @classmethod
    @overload
    def ToChar(cls, value: float) -> Char:
        """"""
    @classmethod
    @overload
    def ToChar(cls, value: str) -> Char:
        """"""
    @classmethod
    @overload
    def ToChar(cls, value: str, provider: IFormatProvider) -> Char:
        """"""
    @classmethod
    @overload
    def ToChar(cls, value: int) -> Char:
        """"""
    @classmethod
    @overload
    def ToChar(cls, value: int) -> Char:
        """"""
    @classmethod
    @overload
    def ToChar(cls, value: int) -> Char:
        """"""
    @classmethod
    @overload
    def ToDateTime(cls, value: bool) -> DateTime:
        """"""
    @classmethod
    @overload
    def ToDateTime(cls, value: int) -> DateTime:
        """"""
    @classmethod
    @overload
    def ToDateTime(cls, value: Char) -> DateTime:
        """"""
    @classmethod
    @overload
    def ToDateTime(cls, value: DateTime) -> DateTime:
        """"""
    @classmethod
    @overload
    def ToDateTime(cls, value: Decimal) -> DateTime:
        """"""
    @classmethod
    @overload
    def ToDateTime(cls, value: float) -> DateTime:
        """"""
    @classmethod
    @overload
    def ToDateTime(cls, value: int) -> DateTime:
        """"""
    @classmethod
    @overload
    def ToDateTime(cls, value: int) -> DateTime:
        """"""
    @classmethod
    @overload
    def ToDateTime(cls, value: int) -> DateTime:
        """"""
    @classmethod
    @overload
    def ToDateTime(cls, value: object) -> DateTime:
        """"""
    @classmethod
    @overload
    def ToDateTime(cls, value: object, provider: IFormatProvider) -> DateTime:
        """"""
    @classmethod
    @overload
    def ToDateTime(cls, value: int) -> DateTime:
        """"""
    @classmethod
    @overload
    def ToDateTime(cls, value: float) -> DateTime:
        """"""
    @classmethod
    @overload
    def ToDateTime(cls, value: str) -> DateTime:
        """"""
    @classmethod
    @overload
    def ToDateTime(cls, value: str, provider: IFormatProvider) -> DateTime:
        """"""
    @classmethod
    @overload
    def ToDateTime(cls, value: int) -> DateTime:
        """"""
    @classmethod
    @overload
    def ToDateTime(cls, value: int) -> DateTime:
        """"""
    @classmethod
    @overload
    def ToDateTime(cls, value: int) -> DateTime:
        """"""
    @classmethod
    @overload
    def ToDecimal(cls, value: bool) -> Decimal:
        """"""
    @classmethod
    @overload
    def ToDecimal(cls, value: int) -> Decimal:
        """"""
    @classmethod
    @overload
    def ToDecimal(cls, value: Char) -> Decimal:
        """"""
    @classmethod
    @overload
    def ToDecimal(cls, value: DateTime) -> Decimal:
        """"""
    @classmethod
    @overload
    def ToDecimal(cls, value: Decimal) -> Decimal:
        """"""
    @classmethod
    @overload
    def ToDecimal(cls, value: float) -> Decimal:
        """"""
    @classmethod
    @overload
    def ToDecimal(cls, value: int) -> Decimal:
        """"""
    @classmethod
    @overload
    def ToDecimal(cls, value: int) -> Decimal:
        """"""
    @classmethod
    @overload
    def ToDecimal(cls, value: int) -> Decimal:
        """"""
    @classmethod
    @overload
    def ToDecimal(cls, value: object) -> Decimal:
        """"""
    @classmethod
    @overload
    def ToDecimal(cls, value: object, provider: IFormatProvider) -> Decimal:
        """"""
    @classmethod
    @overload
    def ToDecimal(cls, value: int) -> Decimal:
        """"""
    @classmethod
    @overload
    def ToDecimal(cls, value: float) -> Decimal:
        """"""
    @classmethod
    @overload
    def ToDecimal(cls, value: str) -> Decimal:
        """"""
    @classmethod
    @overload
    def ToDecimal(cls, value: str, provider: IFormatProvider) -> Decimal:
        """"""
    @classmethod
    @overload
    def ToDecimal(cls, value: int) -> Decimal:
        """"""
    @classmethod
    @overload
    def ToDecimal(cls, value: int) -> Decimal:
        """"""
    @classmethod
    @overload
    def ToDecimal(cls, value: int) -> Decimal:
        """"""
    @classmethod
    @overload
    def ToDouble(cls, value: bool) -> float:
        """"""
    @classmethod
    @overload
    def ToDouble(cls, value: int) -> float:
        """"""
    @classmethod
    @overload
    def ToDouble(cls, value: Char) -> float:
        """"""
    @classmethod
    @overload
    def ToDouble(cls, value: DateTime) -> float:
        """"""
    @classmethod
    @overload
    def ToDouble(cls, value: Decimal) -> float:
        """"""
    @classmethod
    @overload
    def ToDouble(cls, value: float) -> float:
        """"""
    @classmethod
    @overload
    def ToDouble(cls, value: int) -> float:
        """"""
    @classmethod
    @overload
    def ToDouble(cls, value: int) -> float:
        """"""
    @classmethod
    @overload
    def ToDouble(cls, value: int) -> float:
        """"""
    @classmethod
    @overload
    def ToDouble(cls, value: object) -> float:
        """"""
    @classmethod
    @overload
    def ToDouble(cls, value: object, provider: IFormatProvider) -> float:
        """"""
    @classmethod
    @overload
    def ToDouble(cls, value: int) -> float:
        """"""
    @classmethod
    @overload
    def ToDouble(cls, value: float) -> float:
        """"""
    @classmethod
    @overload
    def ToDouble(cls, value: str) -> float:
        """"""
    @classmethod
    @overload
    def ToDouble(cls, value: str, provider: IFormatProvider) -> float:
        """"""
    @classmethod
    @overload
    def ToDouble(cls, value: int) -> float:
        """"""
    @classmethod
    @overload
    def ToDouble(cls, value: int) -> float:
        """"""
    @classmethod
    @overload
    def ToDouble(cls, value: int) -> float:
        """"""
    @classmethod
    @overload
    def ToInt16(cls, value: bool) -> int:
        """"""
    @classmethod
    @overload
    def ToInt16(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToInt16(cls, value: Char) -> int:
        """"""
    @classmethod
    @overload
    def ToInt16(cls, value: DateTime) -> int:
        """"""
    @classmethod
    @overload
    def ToInt16(cls, value: Decimal) -> int:
        """"""
    @classmethod
    @overload
    def ToInt16(cls, value: float) -> int:
        """"""
    @classmethod
    @overload
    def ToInt16(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToInt16(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToInt16(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToInt16(cls, value: object) -> int:
        """"""
    @classmethod
    @overload
    def ToInt16(cls, value: object, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def ToInt16(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToInt16(cls, value: float) -> int:
        """"""
    @classmethod
    @overload
    def ToInt16(cls, value: str) -> int:
        """"""
    @classmethod
    @overload
    def ToInt16(cls, value: str, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def ToInt16(cls, value: str, fromBase: int) -> int:
        """"""
    @classmethod
    @overload
    def ToInt16(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToInt16(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToInt16(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToInt32(cls, value: bool) -> int:
        """"""
    @classmethod
    @overload
    def ToInt32(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToInt32(cls, value: Char) -> int:
        """"""
    @classmethod
    @overload
    def ToInt32(cls, value: DateTime) -> int:
        """"""
    @classmethod
    @overload
    def ToInt32(cls, value: Decimal) -> int:
        """"""
    @classmethod
    @overload
    def ToInt32(cls, value: float) -> int:
        """"""
    @classmethod
    @overload
    def ToInt32(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToInt32(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToInt32(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToInt32(cls, value: object) -> int:
        """"""
    @classmethod
    @overload
    def ToInt32(cls, value: object, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def ToInt32(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToInt32(cls, value: float) -> int:
        """"""
    @classmethod
    @overload
    def ToInt32(cls, value: str) -> int:
        """"""
    @classmethod
    @overload
    def ToInt32(cls, value: str, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def ToInt32(cls, value: str, fromBase: int) -> int:
        """"""
    @classmethod
    @overload
    def ToInt32(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToInt32(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToInt32(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToInt64(cls, value: bool) -> int:
        """"""
    @classmethod
    @overload
    def ToInt64(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToInt64(cls, value: Char) -> int:
        """"""
    @classmethod
    @overload
    def ToInt64(cls, value: DateTime) -> int:
        """"""
    @classmethod
    @overload
    def ToInt64(cls, value: Decimal) -> int:
        """"""
    @classmethod
    @overload
    def ToInt64(cls, value: float) -> int:
        """"""
    @classmethod
    @overload
    def ToInt64(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToInt64(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToInt64(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToInt64(cls, value: object) -> int:
        """"""
    @classmethod
    @overload
    def ToInt64(cls, value: object, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def ToInt64(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToInt64(cls, value: float) -> int:
        """"""
    @classmethod
    @overload
    def ToInt64(cls, value: str) -> int:
        """"""
    @classmethod
    @overload
    def ToInt64(cls, value: str, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def ToInt64(cls, value: str, fromBase: int) -> int:
        """"""
    @classmethod
    @overload
    def ToInt64(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToInt64(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToInt64(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToSByte(cls, value: bool) -> int:
        """"""
    @classmethod
    @overload
    def ToSByte(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToSByte(cls, value: Char) -> int:
        """"""
    @classmethod
    @overload
    def ToSByte(cls, value: DateTime) -> int:
        """"""
    @classmethod
    @overload
    def ToSByte(cls, value: Decimal) -> int:
        """"""
    @classmethod
    @overload
    def ToSByte(cls, value: float) -> int:
        """"""
    @classmethod
    @overload
    def ToSByte(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToSByte(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToSByte(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToSByte(cls, value: object) -> int:
        """"""
    @classmethod
    @overload
    def ToSByte(cls, value: object, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def ToSByte(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToSByte(cls, value: float) -> int:
        """"""
    @classmethod
    @overload
    def ToSByte(cls, value: str) -> int:
        """"""
    @classmethod
    @overload
    def ToSByte(cls, value: str, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def ToSByte(cls, value: str, fromBase: int) -> int:
        """"""
    @classmethod
    @overload
    def ToSByte(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToSByte(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToSByte(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToSingle(cls, value: bool) -> float:
        """"""
    @classmethod
    @overload
    def ToSingle(cls, value: int) -> float:
        """"""
    @classmethod
    @overload
    def ToSingle(cls, value: Char) -> float:
        """"""
    @classmethod
    @overload
    def ToSingle(cls, value: DateTime) -> float:
        """"""
    @classmethod
    @overload
    def ToSingle(cls, value: Decimal) -> float:
        """"""
    @classmethod
    @overload
    def ToSingle(cls, value: float) -> float:
        """"""
    @classmethod
    @overload
    def ToSingle(cls, value: int) -> float:
        """"""
    @classmethod
    @overload
    def ToSingle(cls, value: int) -> float:
        """"""
    @classmethod
    @overload
    def ToSingle(cls, value: int) -> float:
        """"""
    @classmethod
    @overload
    def ToSingle(cls, value: object) -> float:
        """"""
    @classmethod
    @overload
    def ToSingle(cls, value: object, provider: IFormatProvider) -> float:
        """"""
    @classmethod
    @overload
    def ToSingle(cls, value: int) -> float:
        """"""
    @classmethod
    @overload
    def ToSingle(cls, value: float) -> float:
        """"""
    @classmethod
    @overload
    def ToSingle(cls, value: str) -> float:
        """"""
    @classmethod
    @overload
    def ToSingle(cls, value: str, provider: IFormatProvider) -> float:
        """"""
    @classmethod
    @overload
    def ToSingle(cls, value: int) -> float:
        """"""
    @classmethod
    @overload
    def ToSingle(cls, value: int) -> float:
        """"""
    @classmethod
    @overload
    def ToSingle(cls, value: int) -> float:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: bool) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: bool, provider: IFormatProvider) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: int) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: int, provider: IFormatProvider) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: int, toBase: int) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: Char) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: Char, provider: IFormatProvider) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: DateTime) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: DateTime, provider: IFormatProvider) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: Decimal) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: Decimal, provider: IFormatProvider) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: float) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: float, provider: IFormatProvider) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: int) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: int, provider: IFormatProvider) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: int, toBase: int) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: int) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: int, provider: IFormatProvider) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: int, toBase: int) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: int) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: int, provider: IFormatProvider) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: int, toBase: int) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: object) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: object, provider: IFormatProvider) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: int) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: int, provider: IFormatProvider) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: float) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: float, provider: IFormatProvider) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: str) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: str, provider: IFormatProvider) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: int) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: int, provider: IFormatProvider) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: int) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: int, provider: IFormatProvider) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: int) -> str:
        """"""
    @classmethod
    @overload
    def ToString(cls, value: int, provider: IFormatProvider) -> str:
        """"""
    @classmethod
    @overload
    def ToUInt16(cls, value: bool) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt16(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt16(cls, value: Char) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt16(cls, value: DateTime) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt16(cls, value: Decimal) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt16(cls, value: float) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt16(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt16(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt16(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt16(cls, value: object) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt16(cls, value: object, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt16(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt16(cls, value: float) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt16(cls, value: str) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt16(cls, value: str, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt16(cls, value: str, fromBase: int) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt16(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt16(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt16(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt32(cls, value: bool) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt32(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt32(cls, value: Char) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt32(cls, value: DateTime) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt32(cls, value: Decimal) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt32(cls, value: float) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt32(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt32(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt32(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt32(cls, value: object) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt32(cls, value: object, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt32(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt32(cls, value: float) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt32(cls, value: str) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt32(cls, value: str, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt32(cls, value: str, fromBase: int) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt32(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt32(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt32(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt64(cls, value: bool) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt64(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt64(cls, value: Char) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt64(cls, value: DateTime) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt64(cls, value: Decimal) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt64(cls, value: float) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt64(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt64(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt64(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt64(cls, value: object) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt64(cls, value: object, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt64(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt64(cls, value: float) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt64(cls, value: str) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt64(cls, value: str, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt64(cls, value: str, fromBase: int) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt64(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt64(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt64(cls, value: int) -> int:
        """"""

Converter: Callable[[TInput], TOutput] = ...
""""""
CrossAppDomainDelegate: Callable[[], None] = ...
""""""
CtorDelegate: Callable[[object], None] = ...
""""""

class CultureAwareComparer(
    StringComparer,
    IComparer[String],
    IEqualityComparer[String],
    IComparer,
    IEqualityComparer,
    IWellKnownStringEqualityComparer,
):
    """"""
    @overload
    def Compare(self, x: object, y: object) -> int:
        """"""
    @overload
    def Compare(self, x: str, y: str) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, x: object, y: object) -> bool:
        """"""
    @overload
    def Equals(self, x: str, y: str) -> bool:
        """"""
    def GetEqualityComparerForSerialization(self) -> IEqualityComparer:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, obj: object) -> int:
        """"""
    @overload
    def GetHashCode(self, obj: str) -> int:
        """"""
    def GetRandomizedEqualityComparer(self) -> IEqualityComparer:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class CultureAwareRandomizedComparer(
    StringComparer,
    IComparer[String],
    IEqualityComparer[String],
    IComparer,
    IEqualityComparer,
    IWellKnownStringEqualityComparer,
):
    """"""
    @overload
    def Compare(self, x: object, y: object) -> int:
        """"""
    @overload
    def Compare(self, x: str, y: str) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, x: object, y: object) -> bool:
        """"""
    @overload
    def Equals(self, x: str, y: str) -> bool:
        """"""
    def GetEqualityComparerForSerialization(self) -> IEqualityComparer:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, obj: object) -> int:
        """"""
    @overload
    def GetHashCode(self, obj: str) -> int:
        """"""
    def GetRandomizedEqualityComparer(self) -> IEqualityComparer:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Currency(ValueType):
    """"""
    def __init__(self, value: Decimal) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def FromOACurrency(cls, cy: int) -> Currency:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def ToDecimal(cls, c: Currency) -> Decimal:
        """"""
    def ToOACurrency(self) -> int:
        """"""
    def ToString(self) -> str:
        """"""

class CurrentSystemTimeZone(TimeZone):
    """"""
    @property
    def DaylightName(self) -> str:
        """"""
    @property
    def StandardName(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetDaylightChanges(self, year: int) -> DaylightTime:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetUtcOffset(self, time: DateTime) -> TimeSpan:
        """"""
    def IsDaylightSavingTime(self, time: DateTime) -> bool:
        """"""
    def ToLocalTime(self, time: DateTime) -> DateTime:
        """"""
    def ToString(self) -> str:
        """"""
    def ToUniversalTime(self, time: DateTime) -> DateTime:
        """"""

class DBNull(Object, ISerializable, IConvertible):
    """"""

    Value: ClassVar[DBNull]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeCode(self) -> TypeCode:
        """"""
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """"""
    def ToByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToChar(self, provider: IFormatProvider) -> Char:
        """"""
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """"""
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """"""
    def ToDouble(self, provider: IFormatProvider) -> float:
        """"""
    def ToInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt64(self, provider: IFormatProvider) -> int:
        """"""
    def ToSByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToSingle(self, provider: IFormatProvider) -> float:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """"""
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """"""
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """"""

class DTSubString(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DTSubStringType(Enum):
    """"""

    Unknown: DTSubStringType = ...
    """"""
    Invalid: DTSubStringType = ...
    """"""
    Number: DTSubStringType = ...
    """"""
    End: DTSubStringType = ...
    """"""
    Other: DTSubStringType = ...
    """"""

class DataMisalignedException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
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

class DateTime(
    ValueType,
    ISerializable,
    IComparable,
    IComparable[DateTime],
    IConvertible,
    IEquatable[DateTime],
    IFormattable,
):
    """"""

    MaxValue: ClassVar[DateTime]
    """"""
    MinValue: ClassVar[DateTime]
    """"""
    @overload
    def __init__(self, ticks: int) -> None:
        """"""
    @overload
    def __init__(self, ticks: int, kind: DateTimeKind) -> None:
        """"""
    @overload
    def __init__(self, year: int, month: int, day: int) -> None:
        """"""
    @overload
    def __init__(self, year: int, month: int, day: int, calendar: Calendar) -> None:
        """"""
    @overload
    def __init__(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int,
        kind: DateTimeKind,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int,
        calendar: Calendar,
    ) -> None:
        """"""
    @overload
    def __init__(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int,
        millisecond: int,
        kind: DateTimeKind,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int,
        millisecond: int,
        calendar: Calendar,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int,
        millisecond: int,
        calendar: Calendar,
        kind: DateTimeKind,
    ) -> None:
        """"""
    @property
    def Date(self) -> DateTime:
        """"""
    @property
    def Day(self) -> int:
        """"""
    @property
    def DayOfWeek(self) -> DayOfWeek:
        """"""
    @property
    def DayOfYear(self) -> int:
        """"""
    @property
    def Hour(self) -> int:
        """"""
    @property
    def Kind(self) -> DateTimeKind:
        """"""
    @property
    def Millisecond(self) -> int:
        """"""
    @property
    def Minute(self) -> int:
        """"""
    @property
    def Month(self) -> int:
        """"""
    @classmethod
    @property
    def Now(cls) -> DateTime:
        """"""
    @property
    def Second(self) -> int:
        """"""
    @property
    def Ticks(self) -> int:
        """"""
    @property
    def TimeOfDay(self) -> TimeSpan:
        """"""
    @classmethod
    @property
    def Today(cls) -> DateTime:
        """"""
    @classmethod
    @property
    def UtcNow(cls) -> DateTime:
        """"""
    @property
    def Year(self) -> int:
        """"""
    def Add(self, value: TimeSpan) -> DateTime:
        """"""
    def AddDays(self, value: float) -> DateTime:
        """"""
    def AddHours(self, value: float) -> DateTime:
        """"""
    def AddMilliseconds(self, value: float) -> DateTime:
        """"""
    def AddMinutes(self, value: float) -> DateTime:
        """"""
    def AddMonths(self, months: int) -> DateTime:
        """"""
    def AddSeconds(self, value: float) -> DateTime:
        """"""
    def AddTicks(self, value: int) -> DateTime:
        """"""
    def AddYears(self, value: int) -> DateTime:
        """"""
    @classmethod
    def Compare(cls, t1: DateTime, t2: DateTime) -> int:
        """"""
    @overload
    def CompareTo(self, value: DateTime) -> int:
        """"""
    @overload
    def CompareTo(self, value: object) -> int:
        """"""
    @classmethod
    def DaysInMonth(cls, year: int, month: int) -> int:
        """"""
    @overload
    def Equals(self, value: DateTime) -> bool:
        """"""
    @classmethod
    @overload
    def Equals(cls, t1: DateTime, t2: DateTime) -> bool:
        """"""
    @overload
    def Equals(self, value: object) -> bool:
        """"""
    @classmethod
    def FromBinary(cls, dateData: int) -> DateTime:
        """"""
    @classmethod
    def FromFileTime(cls, fileTime: int) -> DateTime:
        """"""
    @classmethod
    def FromFileTimeUtc(cls, fileTime: int) -> DateTime:
        """"""
    @classmethod
    def FromOADate(cls, d: float) -> DateTime:
        """"""
    @overload
    def GetDateTimeFormats(self) -> Array[str]:
        """"""
    @overload
    def GetDateTimeFormats(self, format: Char) -> Array[str]:
        """"""
    @overload
    def GetDateTimeFormats(self, format: Char, provider: IFormatProvider) -> Array[str]:
        """"""
    @overload
    def GetDateTimeFormats(self, provider: IFormatProvider) -> Array[str]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeCode(self) -> TypeCode:
        """"""
    def IsDaylightSavingTime(self) -> bool:
        """"""
    @classmethod
    def IsLeapYear(cls, year: int) -> bool:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str) -> DateTime:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, provider: IFormatProvider) -> DateTime:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, provider: IFormatProvider, styles: DateTimeStyles) -> DateTime:
        """"""
    @classmethod
    @overload
    def ParseExact(
        cls, s: str, formats: Array[str], provider: IFormatProvider, style: DateTimeStyles
    ) -> DateTime:
        """"""
    @classmethod
    @overload
    def ParseExact(cls, s: str, format: str, provider: IFormatProvider) -> DateTime:
        """"""
    @classmethod
    @overload
    def ParseExact(
        cls, s: str, format: str, provider: IFormatProvider, style: DateTimeStyles
    ) -> DateTime:
        """"""
    @classmethod
    def SpecifyKind(cls, value: DateTime, kind: DateTimeKind) -> DateTime:
        """"""
    @overload
    def Subtract(self, value: DateTime) -> TimeSpan:
        """"""
    @overload
    def Subtract(self, value: TimeSpan) -> DateTime:
        """"""
    def ToBinary(self) -> int:
        """"""
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """"""
    def ToByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToChar(self, provider: IFormatProvider) -> Char:
        """"""
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """"""
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """"""
    def ToDouble(self, provider: IFormatProvider) -> float:
        """"""
    def ToFileTime(self) -> int:
        """"""
    def ToFileTimeUtc(self) -> int:
        """"""
    def ToInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt64(self, provider: IFormatProvider) -> int:
        """"""
    def ToLocalTime(self) -> DateTime:
        """"""
    def ToLongDateString(self) -> str:
        """"""
    def ToLongTimeString(self) -> str:
        """"""
    def ToOADate(self) -> float:
        """"""
    def ToSByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToShortDateString(self) -> str:
        """"""
    def ToShortTimeString(self) -> str:
        """"""
    def ToSingle(self, provider: IFormatProvider) -> float:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """"""
    @overload
    def ToString(self, format: str) -> str:
        """"""
    @overload
    def ToString(self, format: str, provider: IFormatProvider) -> str:
        """"""
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """"""
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """"""
    def ToUniversalTime(self) -> DateTime:
        """"""
    @classmethod
    @overload
    def TryParse(cls, s: str, result: DateTime) -> tuple[bool, DateTime]:
        """"""
    @classmethod
    @overload
    def TryParse(
        cls, s: str, provider: IFormatProvider, styles: DateTimeStyles, result: DateTime
    ) -> tuple[bool, DateTime]:
        """"""
    @classmethod
    @overload
    def TryParseExact(
        cls,
        s: str,
        formats: Array[str],
        provider: IFormatProvider,
        style: DateTimeStyles,
        result: DateTime,
    ) -> tuple[bool, DateTime]:
        """"""
    @classmethod
    @overload
    def TryParseExact(
        cls, s: str, format: str, provider: IFormatProvider, style: DateTimeStyles, result: DateTime
    ) -> tuple[bool, DateTime]:
        """"""
    @classmethod
    def op_Addition(cls, d: DateTime, t: TimeSpan) -> DateTime:
        """"""
    @classmethod
    def op_Equality(cls, d1: DateTime, d2: DateTime) -> bool:
        """"""
    @classmethod
    def op_GreaterThan(cls, t1: DateTime, t2: DateTime) -> bool:
        """"""
    @classmethod
    def op_GreaterThanOrEqual(cls, t1: DateTime, t2: DateTime) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, d1: DateTime, d2: DateTime) -> bool:
        """"""
    @classmethod
    def op_LessThan(cls, t1: DateTime, t2: DateTime) -> bool:
        """"""
    @classmethod
    def op_LessThanOrEqual(cls, t1: DateTime, t2: DateTime) -> bool:
        """"""
    @classmethod
    @overload
    def op_Subtraction(cls, d1: DateTime, d2: DateTime) -> TimeSpan:
        """"""
    @classmethod
    @overload
    def op_Subtraction(cls, d: DateTime, t: TimeSpan) -> DateTime:
        """"""
    def __add__(self, other: TimeSpan) -> DateTime:
        """"""
    def __eq__(self, other: DateTime) -> bool:
        """"""
    def __gt__(self, other: DateTime) -> bool:
        """"""
    def __ge__(self, other: DateTime) -> bool:
        """"""
    def __ne__(self, other: DateTime) -> bool:
        """"""
    def __lt__(self, other: DateTime) -> bool:
        """"""
    def __le__(self, other: DateTime) -> bool:
        """"""
    @overload
    def __sub__(self, other: DateTime) -> TimeSpan:
        """"""
    @overload
    def __sub__(self, other: TimeSpan) -> DateTime:
        """"""

class DateTimeFormat(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DateTimeKind(Enum):
    """"""

    Unspecified: DateTimeKind = ...
    """"""
    Utc: DateTimeKind = ...
    """"""
    Local: DateTimeKind = ...
    """"""

class DateTimeOffset(
    ValueType,
    IDeserializationCallback,
    ISerializable,
    IComparable,
    IComparable[DateTimeOffset],
    IEquatable[DateTimeOffset],
    IFormattable,
):
    """"""

    MaxValue: ClassVar[DateTimeOffset]
    """"""
    MinValue: ClassVar[DateTimeOffset]
    """"""
    @overload
    def __init__(self, ticks: int, offset: TimeSpan) -> None:
        """"""
    @overload
    def __init__(self, dateTime: DateTime) -> None:
        """"""
    @overload
    def __init__(self, dateTime: DateTime, offset: TimeSpan) -> None:
        """"""
    @overload
    def __init__(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int, offset: TimeSpan
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int,
        millisecond: int,
        offset: TimeSpan,
    ) -> None:
        """"""
    @overload
    def __init__(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int,
        millisecond: int,
        calendar: Calendar,
        offset: TimeSpan,
    ) -> None:
        """"""
    @property
    def Date(self) -> DateTime:
        """"""
    @property
    def DateTime(self) -> DateTime:
        """"""
    @property
    def Day(self) -> int:
        """"""
    @property
    def DayOfWeek(self) -> DayOfWeek:
        """"""
    @property
    def DayOfYear(self) -> int:
        """"""
    @property
    def Hour(self) -> int:
        """"""
    @property
    def LocalDateTime(self) -> DateTime:
        """"""
    @property
    def Millisecond(self) -> int:
        """"""
    @property
    def Minute(self) -> int:
        """"""
    @property
    def Month(self) -> int:
        """"""
    @classmethod
    @property
    def Now(cls) -> DateTimeOffset:
        """"""
    @property
    def Offset(self) -> TimeSpan:
        """"""
    @property
    def Second(self) -> int:
        """"""
    @property
    def Ticks(self) -> int:
        """"""
    @property
    def TimeOfDay(self) -> TimeSpan:
        """"""
    @property
    def UtcDateTime(self) -> DateTime:
        """"""
    @classmethod
    @property
    def UtcNow(cls) -> DateTimeOffset:
        """"""
    @property
    def UtcTicks(self) -> int:
        """"""
    @property
    def Year(self) -> int:
        """"""
    def Add(self, timeSpan: TimeSpan) -> DateTimeOffset:
        """"""
    def AddDays(self, days: float) -> DateTimeOffset:
        """"""
    def AddHours(self, hours: float) -> DateTimeOffset:
        """"""
    def AddMilliseconds(self, milliseconds: float) -> DateTimeOffset:
        """"""
    def AddMinutes(self, minutes: float) -> DateTimeOffset:
        """"""
    def AddMonths(self, months: int) -> DateTimeOffset:
        """"""
    def AddSeconds(self, seconds: float) -> DateTimeOffset:
        """"""
    def AddTicks(self, ticks: int) -> DateTimeOffset:
        """"""
    def AddYears(self, years: int) -> DateTimeOffset:
        """"""
    @classmethod
    def Compare(cls, first: DateTimeOffset, second: DateTimeOffset) -> int:
        """"""
    @overload
    def CompareTo(self, other: DateTimeOffset) -> int:
        """"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """"""
    @overload
    def Equals(self, other: DateTimeOffset) -> bool:
        """"""
    @classmethod
    @overload
    def Equals(cls, first: DateTimeOffset, second: DateTimeOffset) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def EqualsExact(self, other: DateTimeOffset) -> bool:
        """"""
    @classmethod
    def FromFileTime(cls, fileTime: int) -> DateTimeOffset:
        """"""
    @classmethod
    def FromUnixTimeMilliseconds(cls, milliseconds: int) -> DateTimeOffset:
        """"""
    @classmethod
    def FromUnixTimeSeconds(cls, seconds: int) -> DateTimeOffset:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def OnDeserialization(self, sender: object) -> None:
        """"""
    @classmethod
    @overload
    def Parse(cls, input: str) -> DateTimeOffset:
        """"""
    @classmethod
    @overload
    def Parse(cls, input: str, formatProvider: IFormatProvider) -> DateTimeOffset:
        """"""
    @classmethod
    @overload
    def Parse(
        cls, input: str, formatProvider: IFormatProvider, styles: DateTimeStyles
    ) -> DateTimeOffset:
        """"""
    @classmethod
    @overload
    def ParseExact(
        cls,
        input: str,
        formats: Array[str],
        formatProvider: IFormatProvider,
        styles: DateTimeStyles,
    ) -> DateTimeOffset:
        """"""
    @classmethod
    @overload
    def ParseExact(cls, input: str, format: str, formatProvider: IFormatProvider) -> DateTimeOffset:
        """"""
    @classmethod
    @overload
    def ParseExact(
        cls, input: str, format: str, formatProvider: IFormatProvider, styles: DateTimeStyles
    ) -> DateTimeOffset:
        """"""
    @overload
    def Subtract(self, value: DateTimeOffset) -> TimeSpan:
        """"""
    @overload
    def Subtract(self, value: TimeSpan) -> DateTimeOffset:
        """"""
    def ToFileTime(self) -> int:
        """"""
    def ToLocalTime(self) -> DateTimeOffset:
        """"""
    def ToOffset(self, offset: TimeSpan) -> DateTimeOffset:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, formatProvider: IFormatProvider) -> str:
        """"""
    @overload
    def ToString(self, format: str) -> str:
        """"""
    @overload
    def ToString(self, format: str, formatProvider: IFormatProvider) -> str:
        """"""
    def ToUniversalTime(self) -> DateTimeOffset:
        """"""
    def ToUnixTimeMilliseconds(self) -> int:
        """"""
    def ToUnixTimeSeconds(self) -> int:
        """"""
    @classmethod
    @overload
    def TryParse(cls, input: str, result: DateTimeOffset) -> tuple[bool, DateTimeOffset]:
        """"""
    @classmethod
    @overload
    def TryParse(
        cls,
        input: str,
        formatProvider: IFormatProvider,
        styles: DateTimeStyles,
        result: DateTimeOffset,
    ) -> tuple[bool, DateTimeOffset]:
        """"""
    @classmethod
    @overload
    def TryParseExact(
        cls,
        input: str,
        formats: Array[str],
        formatProvider: IFormatProvider,
        styles: DateTimeStyles,
        result: DateTimeOffset,
    ) -> tuple[bool, DateTimeOffset]:
        """"""
    @classmethod
    @overload
    def TryParseExact(
        cls,
        input: str,
        format: str,
        formatProvider: IFormatProvider,
        styles: DateTimeStyles,
        result: DateTimeOffset,
    ) -> tuple[bool, DateTimeOffset]:
        """"""
    @classmethod
    def op_Addition(cls, dateTimeOffset: DateTimeOffset, timeSpan: TimeSpan) -> DateTimeOffset:
        """"""
    @classmethod
    def op_Equality(cls, left: DateTimeOffset, right: DateTimeOffset) -> bool:
        """"""
    @classmethod
    def op_GreaterThan(cls, left: DateTimeOffset, right: DateTimeOffset) -> bool:
        """"""
    @classmethod
    def op_GreaterThanOrEqual(cls, left: DateTimeOffset, right: DateTimeOffset) -> bool:
        """"""
    @classmethod
    def op_Implicit(cls, dateTime: DateTime) -> DateTimeOffset:
        """"""
    @classmethod
    def op_Inequality(cls, left: DateTimeOffset, right: DateTimeOffset) -> bool:
        """"""
    @classmethod
    def op_LessThan(cls, left: DateTimeOffset, right: DateTimeOffset) -> bool:
        """"""
    @classmethod
    def op_LessThanOrEqual(cls, left: DateTimeOffset, right: DateTimeOffset) -> bool:
        """"""
    @classmethod
    @overload
    def op_Subtraction(cls, left: DateTimeOffset, right: DateTimeOffset) -> TimeSpan:
        """"""
    @classmethod
    @overload
    def op_Subtraction(cls, dateTimeOffset: DateTimeOffset, timeSpan: TimeSpan) -> DateTimeOffset:
        """"""
    def __add__(self, other: TimeSpan) -> DateTimeOffset:
        """"""
    def __eq__(self, other: DateTimeOffset) -> bool:
        """"""
    def __gt__(self, other: DateTimeOffset) -> bool:
        """"""
    def __ge__(self, other: DateTimeOffset) -> bool:
        """"""
    def __ne__(self, other: DateTimeOffset) -> bool:
        """"""
    def __lt__(self, other: DateTimeOffset) -> bool:
        """"""
    def __le__(self, other: DateTimeOffset) -> bool:
        """"""
    @overload
    def __sub__(self, other: DateTimeOffset) -> TimeSpan:
        """"""
    @overload
    def __sub__(self, other: TimeSpan) -> DateTimeOffset:
        """"""

class DateTimeParse(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DateTimeRawInfo(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DateTimeResult(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DateTimeToken(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DayOfWeek(Enum):
    """"""

    Sunday: DayOfWeek = ...
    """"""
    Monday: DayOfWeek = ...
    """"""
    Tuesday: DayOfWeek = ...
    """"""
    Wednesday: DayOfWeek = ...
    """"""
    Thursday: DayOfWeek = ...
    """"""
    Friday: DayOfWeek = ...
    """"""
    Saturday: DayOfWeek = ...
    """"""

class Decimal(
    ValueType,
    IDeserializationCallback,
    IComparable,
    IComparable[Decimal],
    IConvertible,
    IEquatable[Decimal],
    IFormattable,
):
    """"""

    MaxValue: ClassVar[Decimal]
    """"""
    MinValue: ClassVar[Decimal]
    """"""
    MinusOne: ClassVar[Decimal]
    """"""
    One: ClassVar[Decimal]
    """"""
    Zero: ClassVar[Decimal]
    """"""
    @overload
    def __init__(self, value: int) -> None:
        """"""
    @overload
    def __init__(self, value: int) -> None:
        """"""
    @overload
    def __init__(self, value: int) -> None:
        """"""
    @overload
    def __init__(self, value: int) -> None:
        """"""
    @overload
    def __init__(self, value: float) -> None:
        """"""
    @overload
    def __init__(self, value: float) -> None:
        """"""
    @overload
    def __init__(self, bits: Array[int]) -> None:
        """"""
    @overload
    def __init__(self, lo: int, mid: int, hi: int, isNegative: bool, scale: int) -> None:
        """"""
    @classmethod
    def Add(cls, d1: Decimal, d2: Decimal) -> Decimal:
        """"""
    @classmethod
    def Ceiling(cls, d: Decimal) -> Decimal:
        """"""
    @classmethod
    def Compare(cls, d1: Decimal, d2: Decimal) -> int:
        """"""
    @overload
    def CompareTo(self, value: Decimal) -> int:
        """"""
    @overload
    def CompareTo(self, value: object) -> int:
        """"""
    @classmethod
    def Divide(cls, d1: Decimal, d2: Decimal) -> Decimal:
        """"""
    @overload
    def Equals(self, value: Decimal) -> bool:
        """"""
    @classmethod
    @overload
    def Equals(cls, d1: Decimal, d2: Decimal) -> bool:
        """"""
    @overload
    def Equals(self, value: object) -> bool:
        """"""
    @classmethod
    def Floor(cls, d: Decimal) -> Decimal:
        """"""
    @classmethod
    def FromOACurrency(cls, cy: int) -> Decimal:
        """"""
    @classmethod
    def GetBits(cls, d: Decimal) -> Array[int]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeCode(self) -> TypeCode:
        """"""
    @classmethod
    def Multiply(cls, d1: Decimal, d2: Decimal) -> Decimal:
        """"""
    @classmethod
    def Negate(cls, d: Decimal) -> Decimal:
        """"""
    def OnDeserialization(self, sender: object) -> None:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str) -> Decimal:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles) -> Decimal:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles, provider: IFormatProvider) -> Decimal:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, provider: IFormatProvider) -> Decimal:
        """"""
    @classmethod
    def Remainder(cls, d1: Decimal, d2: Decimal) -> Decimal:
        """"""
    @classmethod
    @overload
    def Round(cls, d: Decimal) -> Decimal:
        """"""
    @classmethod
    @overload
    def Round(cls, d: Decimal, decimals: int) -> Decimal:
        """"""
    @classmethod
    @overload
    def Round(cls, d: Decimal, decimals: int, mode: MidpointRounding) -> Decimal:
        """"""
    @classmethod
    @overload
    def Round(cls, d: Decimal, mode: MidpointRounding) -> Decimal:
        """"""
    @classmethod
    def Subtract(cls, d1: Decimal, d2: Decimal) -> Decimal:
        """"""
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """"""
    @classmethod
    @overload
    def ToByte(cls, value: Decimal) -> int:
        """"""
    @overload
    def ToByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToChar(self, provider: IFormatProvider) -> Char:
        """"""
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """"""
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """"""
    @classmethod
    @overload
    def ToDouble(cls, d: Decimal) -> float:
        """"""
    @overload
    def ToDouble(self, provider: IFormatProvider) -> float:
        """"""
    @classmethod
    @overload
    def ToInt16(cls, value: Decimal) -> int:
        """"""
    @overload
    def ToInt16(self, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def ToInt32(cls, d: Decimal) -> int:
        """"""
    @overload
    def ToInt32(self, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def ToInt64(cls, d: Decimal) -> int:
        """"""
    @overload
    def ToInt64(self, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    def ToOACurrency(cls, value: Decimal) -> int:
        """"""
    @classmethod
    @overload
    def ToSByte(cls, value: Decimal) -> int:
        """"""
    @overload
    def ToSByte(self, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def ToSingle(cls, d: Decimal) -> float:
        """"""
    @overload
    def ToSingle(self, provider: IFormatProvider) -> float:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """"""
    @overload
    def ToString(self, format: str) -> str:
        """"""
    @overload
    def ToString(self, format: str, provider: IFormatProvider) -> str:
        """"""
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """"""
    @classmethod
    @overload
    def ToUInt16(cls, value: Decimal) -> int:
        """"""
    @overload
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt32(cls, d: Decimal) -> int:
        """"""
    @overload
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def ToUInt64(cls, d: Decimal) -> int:
        """"""
    @overload
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    def Truncate(cls, d: Decimal) -> Decimal:
        """"""
    @classmethod
    @overload
    def TryParse(
        cls, s: str, style: NumberStyles, provider: IFormatProvider, result: Decimal
    ) -> tuple[bool, Decimal]:
        """"""
    @classmethod
    @overload
    def TryParse(cls, s: str, result: Decimal) -> tuple[bool, Decimal]:
        """"""
    @classmethod
    def op_Addition(cls, d1: Decimal, d2: Decimal) -> Decimal:
        """"""
    @classmethod
    def op_Decrement(cls, d: Decimal) -> Decimal:
        """"""
    @classmethod
    def op_Division(cls, d1: Decimal, d2: Decimal) -> Decimal:
        """"""
    @classmethod
    def op_Equality(cls, d1: Decimal, d2: Decimal) -> bool:
        """"""
    @classmethod
    @overload
    def op_Explicit(cls, value: Decimal) -> float:
        """"""
    @classmethod
    @overload
    def op_Explicit(cls, value: float) -> Decimal:
        """"""
    @classmethod
    @overload
    def op_Explicit(cls, value: float) -> Decimal:
        """"""
    @classmethod
    def op_GreaterThan(cls, d1: Decimal, d2: Decimal) -> bool:
        """"""
    @classmethod
    def op_GreaterThanOrEqual(cls, d1: Decimal, d2: Decimal) -> bool:
        """"""
    @classmethod
    @overload
    def op_Implicit(cls, value: int) -> Decimal:
        """"""
    @classmethod
    @overload
    def op_Implicit(cls, value: Char) -> Decimal:
        """"""
    @classmethod
    @overload
    def op_Implicit(cls, value: int) -> Decimal:
        """"""
    @classmethod
    @overload
    def op_Implicit(cls, value: int) -> Decimal:
        """"""
    @classmethod
    @overload
    def op_Implicit(cls, value: int) -> Decimal:
        """"""
    @classmethod
    @overload
    def op_Implicit(cls, value: int) -> Decimal:
        """"""
    @classmethod
    @overload
    def op_Implicit(cls, value: int) -> Decimal:
        """"""
    @classmethod
    @overload
    def op_Implicit(cls, value: int) -> Decimal:
        """"""
    @classmethod
    @overload
    def op_Implicit(cls, value: int) -> Decimal:
        """"""
    @classmethod
    def op_Increment(cls, d: Decimal) -> Decimal:
        """"""
    @classmethod
    def op_Inequality(cls, d1: Decimal, d2: Decimal) -> bool:
        """"""
    @classmethod
    def op_LessThan(cls, d1: Decimal, d2: Decimal) -> bool:
        """"""
    @classmethod
    def op_LessThanOrEqual(cls, d1: Decimal, d2: Decimal) -> bool:
        """"""
    @classmethod
    def op_Modulus(cls, d1: Decimal, d2: Decimal) -> Decimal:
        """"""
    @classmethod
    def op_Multiply(cls, d1: Decimal, d2: Decimal) -> Decimal:
        """"""
    @classmethod
    def op_Subtraction(cls, d1: Decimal, d2: Decimal) -> Decimal:
        """"""
    @classmethod
    def op_UnaryNegation(cls, d: Decimal) -> Decimal:
        """"""
    @classmethod
    def op_UnaryPlus(cls, d: Decimal) -> Decimal:
        """"""
    def __add__(self, other: Decimal) -> Decimal:
        """"""
    def __truediv__(self, other: Decimal) -> Decimal:
        """"""
    def __eq__(self, other: Decimal) -> bool:
        """"""
    def __gt__(self, other: Decimal) -> bool:
        """"""
    def __ge__(self, other: Decimal) -> bool:
        """"""
    def __ne__(self, other: Decimal) -> bool:
        """"""
    def __lt__(self, other: Decimal) -> bool:
        """"""
    def __le__(self, other: Decimal) -> bool:
        """"""
    def __mod__(self, other: Decimal) -> Decimal:
        """"""
    def __mul__(self, other: Decimal) -> Decimal:
        """"""
    def __sub__(self, other: Decimal) -> Decimal:
        """"""
    def __neg__(self) -> Decimal:
        """"""
    def __pos__(self) -> Decimal:
        """"""

class DefaultBinder(Binder):
    """"""
    def __init__(self) -> None:
        """"""
    def BindToField(
        self,
        bindingAttr: BindingFlags,
        match: Array[FieldInfo],
        value: object,
        cultureInfo: CultureInfo,
    ) -> FieldInfo:
        """"""
    def BindToMethod(
        self,
        bindingAttr: BindingFlags,
        match: Array[MethodBase],
        args: Object,
        modifiers: Array[ParameterModifier],
        cultureInfo: CultureInfo,
        names: Array[str],
        state: Object,
    ) -> tuple[MethodBase, Object]:
        """"""
    def ChangeType(self, value: object, type: Type, cultureInfo: CultureInfo) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def ExactBinding(
        cls, match: Array[MethodBase], types: Array[Type], modifiers: Array[ParameterModifier]
    ) -> MethodBase:
        """"""
    @classmethod
    def ExactPropertyBinding(
        cls,
        match: Array[PropertyInfo],
        returnType: Type,
        types: Array[Type],
        modifiers: Array[ParameterModifier],
    ) -> PropertyInfo:
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

class Delegate(ABC, Object, ISerializable, ICloneable):
    """"""
    @property
    def Method(self) -> MethodInfo:
        """"""
    @property
    def Target(self) -> object:
        """"""
    def Clone(self) -> object:
        """"""
    @classmethod
    @overload
    def Combine(cls, delegates: Array[Delegate]) -> Delegate:
        """"""
    @classmethod
    @overload
    def Combine(cls, a: Delegate, b: Delegate) -> Delegate:
        """"""
    @classmethod
    @overload
    def CreateDelegate(cls, type: Type, method: MethodInfo) -> Delegate:
        """"""
    @classmethod
    @overload
    def CreateDelegate(cls, type: Type, method: MethodInfo, throwOnBindFailure: bool) -> Delegate:
        """"""
    @classmethod
    @overload
    def CreateDelegate(cls, type: Type, firstArgument: object, method: MethodInfo) -> Delegate:
        """"""
    @classmethod
    @overload
    def CreateDelegate(
        cls, type: Type, firstArgument: object, method: MethodInfo, throwOnBindFailure: bool
    ) -> Delegate:
        """"""
    @classmethod
    @overload
    def CreateDelegate(cls, type: Type, target: object, method: str) -> Delegate:
        """"""
    @classmethod
    @overload
    def CreateDelegate(cls, type: Type, target: object, method: str, ignoreCase: bool) -> Delegate:
        """"""
    @classmethod
    @overload
    def CreateDelegate(
        cls, type: Type, target: object, method: str, ignoreCase: bool, throwOnBindFailure: bool
    ) -> Delegate:
        """"""
    @classmethod
    @overload
    def CreateDelegate(cls, type: Type, target: Type, method: str) -> Delegate:
        """"""
    @classmethod
    @overload
    def CreateDelegate(cls, type: Type, target: Type, method: str, ignoreCase: bool) -> Delegate:
        """"""
    @classmethod
    @overload
    def CreateDelegate(
        cls, type: Type, target: Type, method: str, ignoreCase: bool, throwOnBindFailure: bool
    ) -> Delegate:
        """"""
    def DynamicInvoke(self, args: Array[object]) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetInvocationList(self) -> Array[Delegate]:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Remove(cls, source: Delegate, value: Delegate) -> Delegate:
        """"""
    @classmethod
    def RemoveAll(cls, source: Delegate, value: Delegate) -> Delegate:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, d1: Delegate, d2: Delegate) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, d1: Delegate, d2: Delegate) -> bool:
        """"""
    def __delitem__(self, source: Delegate, value: Delegate) -> Delegate:
        """"""
    def __eq__(self, other: Delegate) -> bool:
        """"""
    def __ne__(self, other: Delegate) -> bool:
        """"""

class DelegateBindingFlags(Enum):
    """"""

    StaticMethodOnly: DelegateBindingFlags = ...
    """"""
    InstanceMethodOnly: DelegateBindingFlags = ...
    """"""
    OpenDelegateOnly: DelegateBindingFlags = ...
    """"""
    ClosedDelegateOnly: DelegateBindingFlags = ...
    """"""
    NeverCloseOverNull: DelegateBindingFlags = ...
    """"""
    CaselessMatching: DelegateBindingFlags = ...
    """"""
    SkipSecurityChecks: DelegateBindingFlags = ...
    """"""
    RelaxedSignature: DelegateBindingFlags = ...
    """"""

class DelegateSerializationHolder(Object, IObjectReference, ISerializable):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetRealObject(self, context: StreamingContext) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class DivideByZeroException(ArithmeticException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
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

class DllNotFoundException(TypeLoadException, _Exception, ISerializable):
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
    @property
    def TypeName(self) -> str:
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

class DomainNameHelper(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Double(
    ValueType, IComparable, IComparable[Double], IConvertible, IEquatable[Double], IFormattable
):
    """"""

    Epsilon: ClassVar[float]
    """"""
    MaxValue: ClassVar[float]
    """"""
    MinValue: ClassVar[float]
    """"""
    NaN: ClassVar[float]
    """"""
    NegativeInfinity: ClassVar[float]
    """"""
    PositiveInfinity: ClassVar[float]
    """"""
    @overload
    def CompareTo(self, value: float) -> int:
        """"""
    @overload
    def CompareTo(self, value: object) -> int:
        """"""
    @overload
    def Equals(self, obj: float) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeCode(self) -> TypeCode:
        """"""
    @classmethod
    def IsInfinity(cls, d: float) -> bool:
        """"""
    @classmethod
    def IsNaN(cls, d: float) -> bool:
        """"""
    @classmethod
    def IsNegativeInfinity(cls, d: float) -> bool:
        """"""
    @classmethod
    def IsPositiveInfinity(cls, d: float) -> bool:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str) -> float:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles) -> float:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles, provider: IFormatProvider) -> float:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, provider: IFormatProvider) -> float:
        """"""
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """"""
    def ToByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToChar(self, provider: IFormatProvider) -> Char:
        """"""
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """"""
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """"""
    def ToDouble(self, provider: IFormatProvider) -> float:
        """"""
    def ToInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt64(self, provider: IFormatProvider) -> int:
        """"""
    def ToSByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToSingle(self, provider: IFormatProvider) -> float:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """"""
    @overload
    def ToString(self, format: str) -> str:
        """"""
    @overload
    def ToString(self, format: str, provider: IFormatProvider) -> str:
        """"""
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """"""
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def TryParse(
        cls, s: str, style: NumberStyles, provider: IFormatProvider, result: Double
    ) -> tuple[bool, Double]:
        """"""
    @classmethod
    @overload
    def TryParse(cls, s: str, result: Double) -> tuple[bool, Double]:
        """"""
    @classmethod
    def op_Equality(cls, left: float, right: float) -> bool:
        """"""
    @classmethod
    def op_GreaterThan(cls, left: float, right: float) -> bool:
        """"""
    @classmethod
    def op_GreaterThanOrEqual(cls, left: float, right: float) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: float, right: float) -> bool:
        """"""
    @classmethod
    def op_LessThan(cls, left: float, right: float) -> bool:
        """"""
    @classmethod
    def op_LessThanOrEqual(cls, left: float, right: float) -> bool:
        """"""
    def __eq__(self, other: float) -> bool:
        """"""
    def __gt__(self, other: float) -> bool:
        """"""
    def __ge__(self, other: float) -> bool:
        """"""
    def __ne__(self, other: float) -> bool:
        """"""
    def __lt__(self, other: float) -> bool:
        """"""
    def __le__(self, other: float) -> bool:
        """"""

class DuplicateWaitObjectException(ArgumentException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, parameterName: str) -> None:
        """"""
    @overload
    def __init__(self, parameterName: str, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
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
    def ParamName(self) -> str:
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

class Empty(Object, ISerializable):
    """"""

    Value: ClassVar[Empty]
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

class EntryPointNotFoundException(TypeLoadException, _Exception, ISerializable):
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
    @property
    def TypeName(self) -> str:
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

class Enum(ABC, ValueType, IComparable, IConvertible, IFormattable):
    """"""
    def CompareTo(self, target: object) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def Format(cls, enumType: Type, value: object, format: str) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetName(cls, enumType: Type, value: object) -> str:
        """"""
    @classmethod
    def GetNames(cls, enumType: Type) -> Array[str]:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeCode(self) -> TypeCode:
        """"""
    @classmethod
    def GetUnderlyingType(cls, enumType: Type) -> Type:
        """"""
    @classmethod
    def GetValues(cls, enumType: Type) -> Array:
        """"""
    def HasFlag(self, flag: Enum) -> bool:
        """"""
    @classmethod
    def IsDefined(cls, enumType: Type, value: object) -> bool:
        """"""
    @classmethod
    @overload
    def Parse(cls, enumType: Type, value: str) -> object:
        """"""
    @classmethod
    @overload
    def Parse(cls, enumType: Type, value: str, ignoreCase: bool) -> object:
        """"""
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """"""
    def ToByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToChar(self, provider: IFormatProvider) -> Char:
        """"""
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """"""
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """"""
    def ToDouble(self, provider: IFormatProvider) -> float:
        """"""
    def ToInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt64(self, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def ToObject(cls, enumType: Type, value: int) -> object:
        """"""
    @classmethod
    @overload
    def ToObject(cls, enumType: Type, value: int) -> object:
        """"""
    @classmethod
    @overload
    def ToObject(cls, enumType: Type, value: int) -> object:
        """"""
    @classmethod
    @overload
    def ToObject(cls, enumType: Type, value: int) -> object:
        """"""
    @classmethod
    @overload
    def ToObject(cls, enumType: Type, value: object) -> object:
        """"""
    @classmethod
    @overload
    def ToObject(cls, enumType: Type, value: int) -> object:
        """"""
    @classmethod
    @overload
    def ToObject(cls, enumType: Type, value: int) -> object:
        """"""
    @classmethod
    @overload
    def ToObject(cls, enumType: Type, value: int) -> object:
        """"""
    @classmethod
    @overload
    def ToObject(cls, enumType: Type, value: int) -> object:
        """"""
    def ToSByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToSingle(self, provider: IFormatProvider) -> float:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """"""
    @overload
    def ToString(self, format: str) -> str:
        """"""
    @overload
    def ToString(self, format: str, provider: IFormatProvider) -> str:
        """"""
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """"""
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def TryParse(cls, value: str, result: TEnum) -> tuple[bool, TEnum]:
        """"""
    @classmethod
    @overload
    def TryParse(cls, value: str, ignoreCase: bool, result: TEnum) -> tuple[bool, TEnum]:
        """"""

class Environment(ABC, Object):
    """"""
    @classmethod
    @property
    def CommandLine(cls) -> str:
        """"""
    @classmethod
    @property
    def CurrentDirectory(cls) -> str:
        """"""
    @classmethod
    @CurrentDirectory.setter
    def CurrentDirectory(cls, value: str) -> None: ...
    @classmethod
    @property
    def CurrentManagedThreadId(cls) -> int:
        """"""
    @classmethod
    @property
    def ExitCode(cls) -> int:
        """"""
    @classmethod
    @ExitCode.setter
    def ExitCode(cls, value: int) -> None: ...
    @classmethod
    @property
    def HasShutdownStarted(cls) -> bool:
        """"""
    @classmethod
    @property
    def Is64BitOperatingSystem(cls) -> bool:
        """"""
    @classmethod
    @property
    def Is64BitProcess(cls) -> bool:
        """"""
    @classmethod
    @property
    def MachineName(cls) -> str:
        """"""
    @classmethod
    @property
    def NewLine(cls) -> str:
        """"""
    @classmethod
    @property
    def OSVersion(cls) -> OperatingSystem:
        """"""
    @classmethod
    @property
    def ProcessorCount(cls) -> int:
        """"""
    @classmethod
    @property
    def StackTrace(cls) -> str:
        """"""
    @classmethod
    @property
    def SystemDirectory(cls) -> str:
        """"""
    @classmethod
    @property
    def SystemPageSize(cls) -> int:
        """"""
    @classmethod
    @property
    def TickCount(cls) -> int:
        """"""
    @classmethod
    @property
    def UserDomainName(cls) -> str:
        """"""
    @classmethod
    @property
    def UserInteractive(cls) -> bool:
        """"""
    @classmethod
    @property
    def UserName(cls) -> str:
        """"""
    @classmethod
    @property
    def Version(cls) -> Version:
        """"""
    @classmethod
    @property
    def WorkingSet(cls) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def Exit(cls, exitCode: int) -> None:
        """"""
    @classmethod
    def ExpandEnvironmentVariables(cls, name: str) -> str:
        """"""
    @classmethod
    @overload
    def FailFast(cls, message: str) -> None:
        """"""
    @classmethod
    @overload
    def FailFast(cls, message: str, exception: Exception) -> None:
        """"""
    @classmethod
    def GetCommandLineArgs(cls) -> Array[str]:
        """"""
    @classmethod
    @overload
    def GetEnvironmentVariable(cls, variable: str) -> str:
        """"""
    @classmethod
    @overload
    def GetEnvironmentVariable(cls, variable: str, target: EnvironmentVariableTarget) -> str:
        """"""
    @classmethod
    @overload
    def GetEnvironmentVariables(cls) -> IDictionary:
        """"""
    @classmethod
    @overload
    def GetEnvironmentVariables(cls, target: EnvironmentVariableTarget) -> IDictionary:
        """"""
    @classmethod
    @overload
    def GetFolderPath(cls, folder: Environment.SpecialFolder) -> str:
        """"""
    @classmethod
    @overload
    def GetFolderPath(
        cls, folder: Environment.SpecialFolder, option: Environment.SpecialFolderOption
    ) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetLogicalDrives(cls) -> Array[str]:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def SetEnvironmentVariable(cls, variable: str, value: str) -> None:
        """"""
    @classmethod
    @overload
    def SetEnvironmentVariable(
        cls, variable: str, value: str, target: EnvironmentVariableTarget
    ) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    class SpecialFolder(Enum):
        """"""

        Desktop: SpecialFolder = ...
        """"""
        Programs: SpecialFolder = ...
        """"""
        MyDocuments: SpecialFolder = ...
        """"""
        Personal: SpecialFolder = ...
        """"""
        Favorites: SpecialFolder = ...
        """"""
        Startup: SpecialFolder = ...
        """"""
        Recent: SpecialFolder = ...
        """"""
        SendTo: SpecialFolder = ...
        """"""
        StartMenu: SpecialFolder = ...
        """"""
        MyMusic: SpecialFolder = ...
        """"""
        MyVideos: SpecialFolder = ...
        """"""
        DesktopDirectory: SpecialFolder = ...
        """"""
        MyComputer: SpecialFolder = ...
        """"""
        NetworkShortcuts: SpecialFolder = ...
        """"""
        Fonts: SpecialFolder = ...
        """"""
        Templates: SpecialFolder = ...
        """"""
        CommonStartMenu: SpecialFolder = ...
        """"""
        CommonPrograms: SpecialFolder = ...
        """"""
        CommonStartup: SpecialFolder = ...
        """"""
        CommonDesktopDirectory: SpecialFolder = ...
        """"""
        ApplicationData: SpecialFolder = ...
        """"""
        PrinterShortcuts: SpecialFolder = ...
        """"""
        LocalApplicationData: SpecialFolder = ...
        """"""
        InternetCache: SpecialFolder = ...
        """"""
        Cookies: SpecialFolder = ...
        """"""
        History: SpecialFolder = ...
        """"""
        CommonApplicationData: SpecialFolder = ...
        """"""
        Windows: SpecialFolder = ...
        """"""
        System: SpecialFolder = ...
        """"""
        ProgramFiles: SpecialFolder = ...
        """"""
        MyPictures: SpecialFolder = ...
        """"""
        UserProfile: SpecialFolder = ...
        """"""
        SystemX86: SpecialFolder = ...
        """"""
        ProgramFilesX86: SpecialFolder = ...
        """"""
        CommonProgramFiles: SpecialFolder = ...
        """"""
        CommonProgramFilesX86: SpecialFolder = ...
        """"""
        CommonTemplates: SpecialFolder = ...
        """"""
        CommonDocuments: SpecialFolder = ...
        """"""
        CommonAdminTools: SpecialFolder = ...
        """"""
        AdminTools: SpecialFolder = ...
        """"""
        CommonMusic: SpecialFolder = ...
        """"""
        CommonPictures: SpecialFolder = ...
        """"""
        CommonVideos: SpecialFolder = ...
        """"""
        Resources: SpecialFolder = ...
        """"""
        LocalizedResources: SpecialFolder = ...
        """"""
        CommonOemLinks: SpecialFolder = ...
        """"""
        CDBurning: SpecialFolder = ...
        """"""

    class SpecialFolderOption(Enum):
        """"""

        _None: SpecialFolderOption = ...
        """"""
        DoNotVerify: SpecialFolderOption = ...
        """"""
        Create: SpecialFolderOption = ...
        """"""

class EnvironmentHelpers(ABC, Object):
    """"""
    @classmethod
    @property
    def IsAppContainerProcess(cls) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class EnvironmentVariableTarget(Enum):
    """"""

    Process: EnvironmentVariableTarget = ...
    """"""
    User: EnvironmentVariableTarget = ...
    """"""
    Machine: EnvironmentVariableTarget = ...
    """"""

class EventArgs(Object):
    """"""

    Empty: ClassVar[EventArgs]
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

EventHandler: Callable[[object, TEventArgs], None] = ...
""""""
EventHandler: Callable[[object, EventArgs], None] = ...
""""""

class Exception(Object, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
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

class ExceptionArgument(Enum):
    """"""

    obj: ExceptionArgument = ...
    """"""
    dictionary: ExceptionArgument = ...
    """"""
    dictionaryCreationThreshold: ExceptionArgument = ...
    """"""
    array: ExceptionArgument = ...
    """"""
    info: ExceptionArgument = ...
    """"""
    key: ExceptionArgument = ...
    """"""
    collection: ExceptionArgument = ...
    """"""
    list: ExceptionArgument = ...
    """"""
    match: ExceptionArgument = ...
    """"""
    converter: ExceptionArgument = ...
    """"""
    queue: ExceptionArgument = ...
    """"""
    stack: ExceptionArgument = ...
    """"""
    capacity: ExceptionArgument = ...
    """"""
    index: ExceptionArgument = ...
    """"""
    startIndex: ExceptionArgument = ...
    """"""
    value: ExceptionArgument = ...
    """"""
    count: ExceptionArgument = ...
    """"""
    arrayIndex: ExceptionArgument = ...
    """"""
    name: ExceptionArgument = ...
    """"""
    mode: ExceptionArgument = ...
    """"""
    item: ExceptionArgument = ...
    """"""
    options: ExceptionArgument = ...
    """"""
    view: ExceptionArgument = ...
    """"""
    sourceBytesToCopy: ExceptionArgument = ...
    """"""

class ExceptionResource(Enum):
    """"""

    Argument_ImplementIComparable: ExceptionResource = ...
    """"""
    Argument_InvalidType: ExceptionResource = ...
    """"""
    Argument_InvalidArgumentForComparison: ExceptionResource = ...
    """"""
    Argument_InvalidRegistryKeyPermissionCheck: ExceptionResource = ...
    """"""
    ArgumentOutOfRange_NeedNonNegNum: ExceptionResource = ...
    """"""
    Arg_ArrayPlusOffTooSmall: ExceptionResource = ...
    """"""
    Arg_NonZeroLowerBound: ExceptionResource = ...
    """"""
    Arg_RankMultiDimNotSupported: ExceptionResource = ...
    """"""
    Arg_RegKeyDelHive: ExceptionResource = ...
    """"""
    Arg_RegKeyStrLenBug: ExceptionResource = ...
    """"""
    Arg_RegSetStrArrNull: ExceptionResource = ...
    """"""
    Arg_RegSetMismatchedKind: ExceptionResource = ...
    """"""
    Arg_RegSubKeyAbsent: ExceptionResource = ...
    """"""
    Arg_RegSubKeyValueAbsent: ExceptionResource = ...
    """"""
    Argument_AddingDuplicate: ExceptionResource = ...
    """"""
    Serialization_InvalidOnDeser: ExceptionResource = ...
    """"""
    Serialization_MissingKeys: ExceptionResource = ...
    """"""
    Serialization_NullKey: ExceptionResource = ...
    """"""
    Argument_InvalidArrayType: ExceptionResource = ...
    """"""
    NotSupported_KeyCollectionSet: ExceptionResource = ...
    """"""
    NotSupported_ValueCollectionSet: ExceptionResource = ...
    """"""
    ArgumentOutOfRange_SmallCapacity: ExceptionResource = ...
    """"""
    ArgumentOutOfRange_Index: ExceptionResource = ...
    """"""
    Argument_InvalidOffLen: ExceptionResource = ...
    """"""
    Argument_ItemNotExist: ExceptionResource = ...
    """"""
    ArgumentOutOfRange_Count: ExceptionResource = ...
    """"""
    ArgumentOutOfRange_InvalidThreshold: ExceptionResource = ...
    """"""
    ArgumentOutOfRange_ListInsert: ExceptionResource = ...
    """"""
    NotSupported_ReadOnlyCollection: ExceptionResource = ...
    """"""
    InvalidOperation_CannotRemoveFromStackOrQueue: ExceptionResource = ...
    """"""
    InvalidOperation_EmptyQueue: ExceptionResource = ...
    """"""
    InvalidOperation_EnumOpCantHappen: ExceptionResource = ...
    """"""
    InvalidOperation_EnumFailedVersion: ExceptionResource = ...
    """"""
    InvalidOperation_EmptyStack: ExceptionResource = ...
    """"""
    ArgumentOutOfRange_BiggerThanCollection: ExceptionResource = ...
    """"""
    InvalidOperation_EnumNotStarted: ExceptionResource = ...
    """"""
    InvalidOperation_EnumEnded: ExceptionResource = ...
    """"""
    NotSupported_SortedListNestedWrite: ExceptionResource = ...
    """"""
    InvalidOperation_NoValue: ExceptionResource = ...
    """"""
    InvalidOperation_RegRemoveSubKey: ExceptionResource = ...
    """"""
    Security_RegistryPermission: ExceptionResource = ...
    """"""
    UnauthorizedAccess_RegistryNoWrite: ExceptionResource = ...
    """"""
    ObjectDisposed_RegKeyClosed: ExceptionResource = ...
    """"""
    NotSupported_InComparableType: ExceptionResource = ...
    """"""
    Argument_InvalidRegistryOptionsCheck: ExceptionResource = ...
    """"""
    Argument_InvalidRegistryViewCheck: ExceptionResource = ...
    """"""

class ExecutionEngineException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
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

class ExternDll(ABC, Object):
    """"""

    Activeds: ClassVar[str]
    """"""
    Advapi32: ClassVar[str]
    """"""
    Clr: ClassVar[str]
    """"""
    Comctl32: ClassVar[str]
    """"""
    Comdlg32: ClassVar[str]
    """"""
    Crypt32: ClassVar[str]
    """"""
    Fxassert: ClassVar[str]
    """"""
    Gdi32: ClassVar[str]
    """"""
    Gdiplus: ClassVar[str]
    """"""
    Hhctrl: ClassVar[str]
    """"""
    Imm32: ClassVar[str]
    """"""
    Kernel32: ClassVar[str]
    """"""
    Loadperf: ClassVar[str]
    """"""
    Mqrt: ClassVar[str]
    """"""
    Mscoree: ClassVar[str]
    """"""
    Msi: ClassVar[str]
    """"""
    Ntdll: ClassVar[str]
    """"""
    Ole32: ClassVar[str]
    """"""
    Oleacc: ClassVar[str]
    """"""
    Oleaut32: ClassVar[str]
    """"""
    Olepro32: ClassVar[str]
    """"""
    PerfCounter: ClassVar[str]
    """"""
    Powrprof: ClassVar[str]
    """"""
    Psapi: ClassVar[str]
    """"""
    ShCore: ClassVar[str]
    """"""
    Shell32: ClassVar[str]
    """"""
    Shlwapi: ClassVar[str]
    """"""
    User32: ClassVar[str]
    """"""
    Uxtheme: ClassVar[str]
    """"""
    Version: ClassVar[str]
    """"""
    Vsassert: ClassVar[str]
    """"""
    WinMM: ClassVar[str]
    """"""
    Winspool: ClassVar[str]
    """"""
    Wldp: ClassVar[str]
    """"""
    Wtsapi32: ClassVar[str]
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class FieldAccessException(MemberAccessException, _Exception, ISerializable):
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

class FileStyleUriParser(UriParser):
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

class FlagsAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
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

class FormatException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
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

class FormattableString(ABC, Object, IFormattable):
    """"""
    @property
    def ArgumentCount(self) -> int:
        """"""
    @property
    def Format(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetArgument(self, index: int) -> object:
        """"""
    def GetArguments(self) -> Array[object]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Invariant(cls, formattable: FormattableString) -> str:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, formatProvider: IFormatProvider) -> str:
        """"""
    @overload
    def ToString(self, format: str, formatProvider: IFormatProvider) -> str:
        """"""

class FtpStyleUriParser(UriParser):
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

Func: Callable[[T], TResult] = ...
""""""
Func: Callable[[T1, T2], TResult] = ...
""""""
Func: Callable[[T1, T2, T3], TResult] = ...
""""""
Func: Callable[[T1, T2, T3, T4], TResult] = ...
""""""
Func: Callable[[T1, T2, T3, T4, T5], TResult] = ...
""""""
Func: Callable[[T1, T2, T3, T4, T5, T6], TResult] = ...
""""""
Func: Callable[[T1, T2, T3, T4, T5, T6, T7], TResult] = ...
""""""
Func: Callable[[T1, T2, T3, T4, T5, T6, T7, T8], TResult] = ...
""""""
Func: Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9], TResult] = ...
""""""
Func: Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10], TResult] = ...
""""""
Func: Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11], TResult] = ...
""""""
Func: Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12], TResult] = ...
""""""
Func: Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13], TResult] = ...
""""""
Func: Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14], TResult] = ...
""""""
Func: Callable[[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15], TResult] = ...
""""""
Func: Callable[
    [T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16], TResult
] = ...
""""""
Func: Callable[[], TResult] = ...
""""""

class GC(ABC, Object):
    """"""
    @classmethod
    @property
    def MaxGeneration(cls) -> int:
        """"""
    @classmethod
    def AddMemoryPressure(cls, bytesAllocated: int) -> None:
        """"""
    @classmethod
    def CancelFullGCNotification(cls) -> None:
        """"""
    @classmethod
    @overload
    def Collect(cls) -> None:
        """"""
    @classmethod
    @overload
    def Collect(cls, generation: int) -> None:
        """"""
    @classmethod
    @overload
    def Collect(cls, generation: int, mode: GCCollectionMode) -> None:
        """"""
    @classmethod
    @overload
    def Collect(cls, generation: int, mode: GCCollectionMode, blocking: bool) -> None:
        """"""
    @classmethod
    @overload
    def Collect(
        cls, generation: int, mode: GCCollectionMode, blocking: bool, compacting: bool
    ) -> None:
        """"""
    @classmethod
    def CollectionCount(cls, generation: int) -> int:
        """"""
    @classmethod
    def EndNoGCRegion(cls) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def GetAllocatedBytesForCurrentThread(cls) -> int:
        """"""
    @classmethod
    @overload
    def GetGeneration(cls, obj: object) -> int:
        """"""
    @classmethod
    @overload
    def GetGeneration(cls, wo: WeakReference) -> int:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetTotalMemory(cls, forceFullCollection: bool) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def KeepAlive(cls, obj: object) -> None:
        """"""
    @classmethod
    def ReRegisterForFinalize(cls, obj: object) -> None:
        """"""
    @classmethod
    def RegisterForFullGCNotification(
        cls, maxGenerationThreshold: int, largeObjectHeapThreshold: int
    ) -> None:
        """"""
    @classmethod
    def RemoveMemoryPressure(cls, bytesAllocated: int) -> None:
        """"""
    @classmethod
    def SuppressFinalize(cls, obj: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    @overload
    def TryStartNoGCRegion(cls, totalSize: int) -> bool:
        """"""
    @classmethod
    @overload
    def TryStartNoGCRegion(cls, totalSize: int, disallowFullBlockingGC: bool) -> bool:
        """"""
    @classmethod
    @overload
    def TryStartNoGCRegion(cls, totalSize: int, lohSize: int) -> bool:
        """"""
    @classmethod
    @overload
    def TryStartNoGCRegion(cls, totalSize: int, lohSize: int, disallowFullBlockingGC: bool) -> bool:
        """"""
    @classmethod
    @overload
    def WaitForFullGCApproach(cls) -> GCNotificationStatus:
        """"""
    @classmethod
    @overload
    def WaitForFullGCApproach(cls, millisecondsTimeout: int) -> GCNotificationStatus:
        """"""
    @classmethod
    @overload
    def WaitForFullGCComplete(cls) -> GCNotificationStatus:
        """"""
    @classmethod
    @overload
    def WaitForFullGCComplete(cls, millisecondsTimeout: int) -> GCNotificationStatus:
        """"""
    @classmethod
    def WaitForPendingFinalizers(cls) -> None:
        """"""

class GCCollectionMode(Enum):
    """"""

    Default: GCCollectionMode = ...
    """"""
    Forced: GCCollectionMode = ...
    """"""
    Optimized: GCCollectionMode = ...
    """"""

class GCNotificationStatus(Enum):
    """"""

    Succeeded: GCNotificationStatus = ...
    """"""
    Failed: GCNotificationStatus = ...
    """"""
    Canceled: GCNotificationStatus = ...
    """"""
    Timeout: GCNotificationStatus = ...
    """"""
    NotApplicable: GCNotificationStatus = ...
    """"""

class Gen2GcCallback(CriticalFinalizerObject):
    """"""
    def __init__(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Register(cls, callback: Func[object, bool], targetObj: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class GenericUriParser(UriParser):
    """"""
    def __init__(self, options: GenericUriParserOptions) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class GenericUriParserOptions(Enum):
    """"""

    Default: GenericUriParserOptions = ...
    """"""
    GenericAuthority: GenericUriParserOptions = ...
    """"""
    AllowEmptyAuthority: GenericUriParserOptions = ...
    """"""
    NoUserInfo: GenericUriParserOptions = ...
    """"""
    NoPort: GenericUriParserOptions = ...
    """"""
    NoQuery: GenericUriParserOptions = ...
    """"""
    NoFragment: GenericUriParserOptions = ...
    """"""
    DontConvertPathBackslashes: GenericUriParserOptions = ...
    """"""
    DontCompressPath: GenericUriParserOptions = ...
    """"""
    DontUnescapePathDotsAndSlashes: GenericUriParserOptions = ...
    """"""
    Idn: GenericUriParserOptions = ...
    """"""
    IriParsing: GenericUriParserOptions = ...
    """"""

class GopherStyleUriParser(UriParser):
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

class Guid(ValueType, IComparable, IComparable[Guid], IEquatable[Guid], IFormattable):
    """"""

    Empty: ClassVar[Guid]
    """"""
    @overload
    def __init__(self, b: Array[int]) -> None:
        """"""
    @overload
    def __init__(
        self, a: int, b: int, c: int, d: int, e: int, f: int, g: int, h: int, i: int, j: int, k: int
    ) -> None:
        """"""
    @overload
    def __init__(self, a: int, b: int, c: int, d: Array[int]) -> None:
        """"""
    @overload
    def __init__(
        self, a: int, b: int, c: int, d: int, e: int, f: int, g: int, h: int, i: int, j: int, k: int
    ) -> None:
        """"""
    @overload
    def __init__(self, g: str) -> None:
        """"""
    @overload
    def CompareTo(self, value: Guid) -> int:
        """"""
    @overload
    def CompareTo(self, value: object) -> int:
        """"""
    @overload
    def Equals(self, g: Guid) -> bool:
        """"""
    @overload
    def Equals(self, o: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def NewGuid(cls) -> Guid:
        """"""
    @classmethod
    def Parse(cls, input: str) -> Guid:
        """"""
    @classmethod
    def ParseExact(cls, input: str, format: str) -> Guid:
        """"""
    def ToByteArray(self) -> Array[int]:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, format: str) -> str:
        """"""
    @overload
    def ToString(self, format: str, provider: IFormatProvider) -> str:
        """"""
    @classmethod
    def TryParse(cls, input: str, result: Guid) -> tuple[bool, Guid]:
        """"""
    @classmethod
    def TryParseExact(cls, input: str, format: str, result: Guid) -> tuple[bool, Guid]:
        """"""
    @classmethod
    def op_Equality(cls, a: Guid, b: Guid) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, a: Guid, b: Guid) -> bool:
        """"""
    def __eq__(self, other: Guid) -> bool:
        """"""
    def __ne__(self, other: Guid) -> bool:
        """"""

class HResults(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class HttpStyleUriParser(UriParser):
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

class IAppDomainSetup:
    """"""
    @property
    def ApplicationBase(self) -> str:
        """"""
    @ApplicationBase.setter
    def ApplicationBase(self, value: str) -> None: ...
    @property
    def ApplicationName(self) -> str:
        """"""
    @ApplicationName.setter
    def ApplicationName(self, value: str) -> None: ...
    @property
    def CachePath(self) -> str:
        """"""
    @CachePath.setter
    def CachePath(self, value: str) -> None: ...
    @property
    def ConfigurationFile(self) -> str:
        """"""
    @ConfigurationFile.setter
    def ConfigurationFile(self, value: str) -> None: ...
    @property
    def DynamicBase(self) -> str:
        """"""
    @DynamicBase.setter
    def DynamicBase(self, value: str) -> None: ...
    @property
    def LicenseFile(self) -> str:
        """"""
    @LicenseFile.setter
    def LicenseFile(self, value: str) -> None: ...
    @property
    def PrivateBinPath(self) -> str:
        """"""
    @PrivateBinPath.setter
    def PrivateBinPath(self, value: str) -> None: ...
    @property
    def PrivateBinPathProbe(self) -> str:
        """"""
    @PrivateBinPathProbe.setter
    def PrivateBinPathProbe(self, value: str) -> None: ...
    @property
    def ShadowCopyDirectories(self) -> str:
        """"""
    @ShadowCopyDirectories.setter
    def ShadowCopyDirectories(self, value: str) -> None: ...
    @property
    def ShadowCopyFiles(self) -> str:
        """"""
    @ShadowCopyFiles.setter
    def ShadowCopyFiles(self, value: str) -> None: ...

class IAsyncResult:
    """"""
    @property
    def AsyncState(self) -> object:
        """"""
    @property
    def AsyncWaitHandle(self) -> WaitHandle:
        """"""
    @property
    def CompletedSynchronously(self) -> bool:
        """"""
    @property
    def IsCompleted(self) -> bool:
        """"""

class ICloneable:
    """"""
    def Clone(self) -> object:
        """"""

class IComparable:
    """"""
    def CompareTo(self, obj: object) -> int:
        """"""

class IComparable[T]:
    """"""
    def CompareTo[T](self, other: T) -> int:
        """"""

class IConvertible:
    """"""
    def GetTypeCode(self) -> TypeCode:
        """"""
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """"""
    def ToByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToChar(self, provider: IFormatProvider) -> Char:
        """"""
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """"""
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """"""
    def ToDouble(self, provider: IFormatProvider) -> float:
        """"""
    def ToInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt64(self, provider: IFormatProvider) -> int:
        """"""
    def ToSByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToSingle(self, provider: IFormatProvider) -> float:
        """"""
    def ToString(self, provider: IFormatProvider) -> str:
        """"""
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """"""
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """"""

class ICustomFormatter:
    """"""
    def Format(self, format: str, arg: object, formatProvider: IFormatProvider) -> str:
        """"""

class IDisposable:
    """"""
    def Dispose(self) -> None:
        """"""

class IEquatable[T]:
    """"""
    def Equals[T](self, other: T) -> bool:
        """"""

class IFormatProvider:
    """"""
    def GetFormat(self, formatType: Type) -> object:
        """"""

class IFormattable:
    """"""
    def ToString(self, format: str, formatProvider: IFormatProvider) -> str:
        """"""

class IObservable[T]:
    """"""
    def Subscribe(self, observer: IObserver[T]) -> IDisposable:
        """"""

class IObserver[T]:
    """"""
    def OnCompleted(self) -> None:
        """"""
    def OnError(self, error: Exception) -> None:
        """"""
    def OnNext[T](self, value: T) -> None:
        """"""

class IProgress[T]:
    """"""
    def Report[T](self, value: T) -> None:
        """"""

class IPv4AddressHelper(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IPv6AddressHelper(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IRuntimeFieldInfo:
    """"""
    @property
    def Value(self) -> RuntimeFieldHandleInternal:
        """"""

class IRuntimeMethodInfo:
    """"""
    @property
    def Value(self) -> RuntimeMethodHandleInternal:
        """"""

class IServiceProvider:
    """"""
    def GetService(self, serviceType: Type) -> object:
        """"""

class ITupleInternal(ITuple):
    """"""
    @property
    def Item(self) -> object:
        """"""
    @property
    def Length(self) -> int:
        """"""
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """"""
    def ToString(self, sb: StringBuilder) -> str:
        """"""
    def __getitem__(self, index: int) -> object:
        """"""

class IValueTupleInternal(ITuple):
    """"""
    @property
    def Item(self) -> object:
        """"""
    @property
    def Length(self) -> int:
        """"""
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """"""
    def ToStringEnd(self) -> str:
        """"""
    def __getitem__(self, index: int) -> object:
        """"""

class IWellKnownStringEqualityComparer:
    """"""
    def GetEqualityComparerForSerialization(self) -> IEqualityComparer:
        """"""
    def GetRandomizedEqualityComparer(self) -> IEqualityComparer:
        """"""

class IndexOutOfRangeException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
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

class InsufficientExecutionStackException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
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

class InsufficientMemoryException(OutOfMemoryException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
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

class Int16(
    ValueType, IComparable, IComparable[Int16], IConvertible, IEquatable[Int16], IFormattable
):
    """"""

    MaxValue: ClassVar[int]
    """"""
    MinValue: ClassVar[int]
    """"""
    @overload
    def CompareTo(self, value: int) -> int:
        """"""
    @overload
    def CompareTo(self, value: object) -> int:
        """"""
    @overload
    def Equals(self, obj: int) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeCode(self) -> TypeCode:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str) -> int:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles) -> int:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, provider: IFormatProvider) -> int:
        """"""
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """"""
    def ToByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToChar(self, provider: IFormatProvider) -> Char:
        """"""
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """"""
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """"""
    def ToDouble(self, provider: IFormatProvider) -> float:
        """"""
    def ToInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt64(self, provider: IFormatProvider) -> int:
        """"""
    def ToSByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToSingle(self, provider: IFormatProvider) -> float:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """"""
    @overload
    def ToString(self, format: str) -> str:
        """"""
    @overload
    def ToString(self, format: str, provider: IFormatProvider) -> str:
        """"""
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """"""
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def TryParse(
        cls, s: str, style: NumberStyles, provider: IFormatProvider, result: Int16
    ) -> tuple[bool, Int16]:
        """"""
    @classmethod
    @overload
    def TryParse(cls, s: str, result: Int16) -> tuple[bool, Int16]:
        """"""

class Int32(
    ValueType, IComparable, IComparable[Int32], IConvertible, IEquatable[Int32], IFormattable
):
    """"""

    MaxValue: ClassVar[int]
    """"""
    MinValue: ClassVar[int]
    """"""
    @overload
    def CompareTo(self, value: int) -> int:
        """"""
    @overload
    def CompareTo(self, value: object) -> int:
        """"""
    @overload
    def Equals(self, obj: int) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeCode(self) -> TypeCode:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str) -> int:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles) -> int:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, provider: IFormatProvider) -> int:
        """"""
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """"""
    def ToByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToChar(self, provider: IFormatProvider) -> Char:
        """"""
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """"""
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """"""
    def ToDouble(self, provider: IFormatProvider) -> float:
        """"""
    def ToInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt64(self, provider: IFormatProvider) -> int:
        """"""
    def ToSByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToSingle(self, provider: IFormatProvider) -> float:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """"""
    @overload
    def ToString(self, format: str) -> str:
        """"""
    @overload
    def ToString(self, format: str, provider: IFormatProvider) -> str:
        """"""
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """"""
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def TryParse(
        cls, s: str, style: NumberStyles, provider: IFormatProvider, result: Int32
    ) -> tuple[bool, Int32]:
        """"""
    @classmethod
    @overload
    def TryParse(cls, s: str, result: Int32) -> tuple[bool, Int32]:
        """"""

class Int64(
    ValueType, IComparable, IComparable[Int64], IConvertible, IEquatable[Int64], IFormattable
):
    """"""

    MaxValue: ClassVar[int]
    """"""
    MinValue: ClassVar[int]
    """"""
    @overload
    def CompareTo(self, value: int) -> int:
        """"""
    @overload
    def CompareTo(self, value: object) -> int:
        """"""
    @overload
    def Equals(self, obj: int) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeCode(self) -> TypeCode:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str) -> int:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles) -> int:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, provider: IFormatProvider) -> int:
        """"""
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """"""
    def ToByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToChar(self, provider: IFormatProvider) -> Char:
        """"""
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """"""
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """"""
    def ToDouble(self, provider: IFormatProvider) -> float:
        """"""
    def ToInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt64(self, provider: IFormatProvider) -> int:
        """"""
    def ToSByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToSingle(self, provider: IFormatProvider) -> float:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """"""
    @overload
    def ToString(self, format: str) -> str:
        """"""
    @overload
    def ToString(self, format: str, provider: IFormatProvider) -> str:
        """"""
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """"""
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def TryParse(
        cls, s: str, style: NumberStyles, provider: IFormatProvider, result: Int64
    ) -> tuple[bool, Int64]:
        """"""
    @classmethod
    @overload
    def TryParse(cls, s: str, result: Int64) -> tuple[bool, Int64]:
        """"""

class IntPtr(ValueType, ISerializable):
    """"""

    Zero: ClassVar[IntPtr]
    """"""
    @overload
    def __init__(self, value: int) -> None:
        """"""
    @overload
    def __init__(self, value: int) -> None:
        """"""
    @overload
    def __init__(self, value: None) -> None:
        """"""
    @classmethod
    @property
    def Size(cls) -> int:
        """"""
    @classmethod
    def Add(cls, pointer: IntPtr, offset: int) -> IntPtr:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Subtract(cls, pointer: IntPtr, offset: int) -> IntPtr:
        """"""
    def ToInt32(self) -> int:
        """"""
    def ToInt64(self) -> int:
        """"""
    def ToPointer(self) -> None:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, format: str) -> str:
        """"""
    @classmethod
    def op_Addition(cls, pointer: IntPtr, offset: int) -> IntPtr:
        """"""
    @classmethod
    def op_Equality(cls, value1: IntPtr, value2: IntPtr) -> bool:
        """"""
    @classmethod
    @overload
    def op_Explicit(cls, value: int) -> IntPtr:
        """"""
    @classmethod
    @overload
    def op_Explicit(cls, value: int) -> IntPtr:
        """"""
    @classmethod
    @overload
    def op_Explicit(cls, value: IntPtr) -> int:
        """"""
    @classmethod
    @overload
    def op_Explicit(cls, value: None) -> IntPtr:
        """"""
    @classmethod
    def op_Inequality(cls, value1: IntPtr, value2: IntPtr) -> bool:
        """"""
    @classmethod
    def op_Subtraction(cls, pointer: IntPtr, offset: int) -> IntPtr:
        """"""
    def __add__(self, other: int) -> IntPtr:
        """"""
    def __eq__(self, other: IntPtr) -> bool:
        """"""
    def __ne__(self, other: IntPtr) -> bool:
        """"""
    def __sub__(self, other: int) -> IntPtr:
        """"""

class Internal(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class InternalGCCollectionMode(Enum):
    """"""

    NonBlocking: InternalGCCollectionMode = ...
    """"""
    Blocking: InternalGCCollectionMode = ...
    """"""
    Optimized: InternalGCCollectionMode = ...
    """"""
    Compacting: InternalGCCollectionMode = ...
    """"""

class InvalidCastException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
        """"""
    @overload
    def __init__(self, message: str, errorCode: int) -> None:
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

class InvalidOperationException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
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

class InvalidProgramException(SystemException, _Exception, ISerializable):
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

class InvalidTimeZoneException(Exception, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
        """"""
    @overload
    def __init__(self) -> None:
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

class InvariantComparer(Object, IComparer):
    """"""
    def Compare(self, a: object, b: object) -> int:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class IriHelper(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class LazyHelpers(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Lazy[T](Object):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, valueFactory: Func[T]) -> None:
        """"""
    @overload
    def __init__(self, isThreadSafe: bool) -> None:
        """"""
    @overload
    def __init__(self, mode: LazyThreadSafetyMode) -> None:
        """"""
    @overload
    def __init__(self, valueFactory: Func[T], isThreadSafe: bool) -> None:
        """"""
    @overload
    def __init__(self, valueFactory: Func[T], mode: LazyThreadSafetyMode) -> None:
        """"""
    @property
    def IsValueCreated(self) -> bool:
        """"""
    @property
    def Value(self) -> T:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class LdapStyleUriParser(UriParser):
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

class LoaderOptimization(Enum):
    """"""

    NotSpecified: LoaderOptimization = ...
    """"""
    SingleDomain: LoaderOptimization = ...
    """"""
    MultiDomain: LoaderOptimization = ...
    """"""
    MultiDomainHost: LoaderOptimization = ...
    """"""
    DomainMask: LoaderOptimization = ...
    """"""
    DisallowBindings: LoaderOptimization = ...
    """"""

class LoaderOptimizationAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self, value: int) -> None:
        """"""
    @overload
    def __init__(self, value: LoaderOptimization) -> None:
        """"""
    @property
    def TypeId(self) -> object:
        """"""
    @property
    def Value(self) -> LoaderOptimization:
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

class LocalAppContext(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsSwitchEnabled(cls, switchName: str) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class LocalAppContextSwitches(ABC, Object):
    """"""
    @classmethod
    @property
    def AesCryptoServiceProviderDontCorrectlyResetDecryptor(cls) -> bool:
        """"""
    @classmethod
    @property
    def AllocateOverlappedOnDemand(cls) -> bool:
        """"""
    @classmethod
    @property
    def DisableEventLogRegistryKeysFiltering(cls) -> bool:
        """"""
    @classmethod
    @property
    def DisableTempFileCollectionDirectoryFeature(cls) -> bool:
        """"""
    @classmethod
    @property
    def DoNotCatchSerialStreamThreadExceptions(cls) -> bool:
        """"""
    @classmethod
    @property
    def DoNotUseNativeZipLibraryForDecompression(cls) -> bool:
        """"""
    @classmethod
    @property
    def DoNotUseTypeDescriptorThreadingFix(cls) -> bool:
        """"""
    @classmethod
    @property
    def DoNotValidatePerformanceCounterData(cls) -> bool:
        """"""
    @classmethod
    @property
    def DoNotValidateX509KeyStorageFlags(cls) -> bool:
        """"""
    @classmethod
    @property
    def DontCheckCertificateEKUs(cls) -> bool:
        """"""
    @classmethod
    @property
    def DontCheckCertificateRevocation(cls) -> bool:
        """"""
    @classmethod
    @property
    def DontEnableSchSendAuxRecord(cls) -> bool:
        """"""
    @classmethod
    @property
    def DontEnableSchUseStrongCrypto(cls) -> bool:
        """"""
    @classmethod
    @property
    def DontEnableStrictRFC3986ReservedCharacterSets(cls) -> bool:
        """"""
    @classmethod
    @property
    def DontEnableSystemDefaultTlsVersions(cls) -> bool:
        """"""
    @classmethod
    @property
    def DontEnableTls13(cls) -> bool:
        """"""
    @classmethod
    @property
    def DontEnableTlsAlerts(cls) -> bool:
        """"""
    @classmethod
    @property
    def DontKeepUnicodeBidiFormattingCharacters(cls) -> bool:
        """"""
    @classmethod
    @property
    def DontReliablyClonePrivateKey(cls) -> bool:
        """"""
    @classmethod
    @property
    def MemberDescriptorEqualsReturnsFalseIfEquivalent(cls) -> bool:
        """"""
    @classmethod
    @property
    def SymmetricCngAlwaysUseNCrypt(cls) -> bool:
        """"""
    @classmethod
    @property
    def UseLegacyFipsThrow(cls) -> bool:
        """"""
    @classmethod
    @property
    def UseLegacyPublicKeyBehavior(cls) -> bool:
        """"""
    @classmethod
    @property
    def UseLegacyTimeoutCheck(cls) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class LocalDataStore(Object):
    """"""
    def __init__(self, mgr: LocalDataStoreMgr, InitialCapacity: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetData(self, slot: LocalDataStoreSlot) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetData(self, slot: LocalDataStoreSlot, data: object) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class LocalDataStoreElement(Object):
    """"""
    def __init__(self, cookie: int) -> None:
        """"""
    @property
    def Cookie(self) -> int:
        """"""
    @property
    def Value(self) -> object:
        """"""
    @Value.setter
    def Value(self, value: object) -> None: ...
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class LocalDataStoreHolder(Object):
    """"""
    def __init__(self, store: LocalDataStore) -> None:
        """"""
    @property
    def Store(self) -> LocalDataStore:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class LocalDataStoreMgr(Object):
    """"""
    def __init__(self) -> None:
        """"""
    def AllocateDataSlot(self) -> LocalDataStoreSlot:
        """"""
    def AllocateNamedDataSlot(self, name: str) -> LocalDataStoreSlot:
        """"""
    def CreateLocalDataStore(self) -> LocalDataStoreHolder:
        """"""
    def DeleteLocalDataStore(self, store: LocalDataStore) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FreeNamedDataSlot(self, name: str) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetNamedDataSlot(self, name: str) -> LocalDataStoreSlot:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def ValidateSlot(self, slot: LocalDataStoreSlot) -> None:
        """"""

class LocalDataStoreSlot(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class LogLevel(Enum):
    """"""

    Trace: LogLevel = ...
    """"""
    Status: LogLevel = ...
    """"""
    Warning: LogLevel = ...
    """"""
    Error: LogLevel = ...
    """"""
    Panic: LogLevel = ...
    """"""

class MTAThreadAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
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

class MarshalByRefObject(ABC, Object):
    """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Equals(self, obj: object) -> bool:
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

class Math(ABC, Object):
    """"""

    E: ClassVar[float]
    """"""
    PI: ClassVar[float]
    """"""
    @classmethod
    @overload
    def Abs(cls, value: Decimal) -> Decimal:
        """"""
    @classmethod
    @overload
    def Abs(cls, value: float) -> float:
        """"""
    @classmethod
    @overload
    def Abs(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def Abs(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def Abs(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def Abs(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def Abs(cls, value: float) -> float:
        """"""
    @classmethod
    def Acos(cls, d: float) -> float:
        """"""
    @classmethod
    def Asin(cls, d: float) -> float:
        """"""
    @classmethod
    def Atan(cls, d: float) -> float:
        """"""
    @classmethod
    def Atan2(cls, y: float, x: float) -> float:
        """"""
    @classmethod
    def BigMul(cls, a: int, b: int) -> int:
        """"""
    @classmethod
    @overload
    def Ceiling(cls, d: Decimal) -> Decimal:
        """"""
    @classmethod
    @overload
    def Ceiling(cls, a: float) -> float:
        """"""
    @classmethod
    def Cos(cls, d: float) -> float:
        """"""
    @classmethod
    def Cosh(cls, value: float) -> float:
        """"""
    @classmethod
    @overload
    def DivRem(cls, a: int, b: int, result: Int32) -> tuple[int, Int32]:
        """"""
    @classmethod
    @overload
    def DivRem(cls, a: int, b: int, result: Int64) -> tuple[int, Int64]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def Exp(cls, d: float) -> float:
        """"""
    @classmethod
    @overload
    def Floor(cls, d: Decimal) -> Decimal:
        """"""
    @classmethod
    @overload
    def Floor(cls, d: float) -> float:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IEEERemainder(cls, x: float, y: float) -> float:
        """"""
    @classmethod
    @overload
    def Log(cls, d: float) -> float:
        """"""
    @classmethod
    @overload
    def Log(cls, a: float, newBase: float) -> float:
        """"""
    @classmethod
    def Log10(cls, d: float) -> float:
        """"""
    @classmethod
    @overload
    def Max(cls, val1: int, val2: int) -> int:
        """"""
    @classmethod
    @overload
    def Max(cls, val1: Decimal, val2: Decimal) -> Decimal:
        """"""
    @classmethod
    @overload
    def Max(cls, val1: float, val2: float) -> float:
        """"""
    @classmethod
    @overload
    def Max(cls, val1: int, val2: int) -> int:
        """"""
    @classmethod
    @overload
    def Max(cls, val1: int, val2: int) -> int:
        """"""
    @classmethod
    @overload
    def Max(cls, val1: int, val2: int) -> int:
        """"""
    @classmethod
    @overload
    def Max(cls, val1: int, val2: int) -> int:
        """"""
    @classmethod
    @overload
    def Max(cls, val1: float, val2: float) -> float:
        """"""
    @classmethod
    @overload
    def Max(cls, val1: int, val2: int) -> int:
        """"""
    @classmethod
    @overload
    def Max(cls, val1: int, val2: int) -> int:
        """"""
    @classmethod
    @overload
    def Max(cls, val1: int, val2: int) -> int:
        """"""
    @classmethod
    @overload
    def Min(cls, val1: int, val2: int) -> int:
        """"""
    @classmethod
    @overload
    def Min(cls, val1: Decimal, val2: Decimal) -> Decimal:
        """"""
    @classmethod
    @overload
    def Min(cls, val1: float, val2: float) -> float:
        """"""
    @classmethod
    @overload
    def Min(cls, val1: int, val2: int) -> int:
        """"""
    @classmethod
    @overload
    def Min(cls, val1: int, val2: int) -> int:
        """"""
    @classmethod
    @overload
    def Min(cls, val1: int, val2: int) -> int:
        """"""
    @classmethod
    @overload
    def Min(cls, val1: int, val2: int) -> int:
        """"""
    @classmethod
    @overload
    def Min(cls, val1: float, val2: float) -> float:
        """"""
    @classmethod
    @overload
    def Min(cls, val1: int, val2: int) -> int:
        """"""
    @classmethod
    @overload
    def Min(cls, val1: int, val2: int) -> int:
        """"""
    @classmethod
    @overload
    def Min(cls, val1: int, val2: int) -> int:
        """"""
    @classmethod
    def Pow(cls, x: float, y: float) -> float:
        """"""
    @classmethod
    @overload
    def Round(cls, d: Decimal) -> Decimal:
        """"""
    @classmethod
    @overload
    def Round(cls, d: Decimal, decimals: int) -> Decimal:
        """"""
    @classmethod
    @overload
    def Round(cls, d: Decimal, decimals: int, mode: MidpointRounding) -> Decimal:
        """"""
    @classmethod
    @overload
    def Round(cls, d: Decimal, mode: MidpointRounding) -> Decimal:
        """"""
    @classmethod
    @overload
    def Round(cls, a: float) -> float:
        """"""
    @classmethod
    @overload
    def Round(cls, value: float, digits: int) -> float:
        """"""
    @classmethod
    @overload
    def Round(cls, value: float, digits: int, mode: MidpointRounding) -> float:
        """"""
    @classmethod
    @overload
    def Round(cls, value: float, mode: MidpointRounding) -> float:
        """"""
    @classmethod
    @overload
    def Sign(cls, value: Decimal) -> int:
        """"""
    @classmethod
    @overload
    def Sign(cls, value: float) -> int:
        """"""
    @classmethod
    @overload
    def Sign(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def Sign(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def Sign(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def Sign(cls, value: int) -> int:
        """"""
    @classmethod
    @overload
    def Sign(cls, value: float) -> int:
        """"""
    @classmethod
    def Sin(cls, a: float) -> float:
        """"""
    @classmethod
    def Sinh(cls, value: float) -> float:
        """"""
    @classmethod
    def Sqrt(cls, d: float) -> float:
        """"""
    @classmethod
    def Tan(cls, a: float) -> float:
        """"""
    @classmethod
    def Tanh(cls, value: float) -> float:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    @overload
    def Truncate(cls, d: Decimal) -> Decimal:
        """"""
    @classmethod
    @overload
    def Truncate(cls, d: float) -> float:
        """"""

class Mda(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class MemberAccessException(SystemException, _Exception, ISerializable):
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

class MethodAccessException(MemberAccessException, _Exception, ISerializable):
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

class MidpointRounding(Enum):
    """"""

    ToEven: MidpointRounding = ...
    """"""
    AwayFromZero: MidpointRounding = ...
    """"""

class MissingFieldException(MissingMemberException, _Exception, ISerializable):
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
    @overload
    def __init__(self, className: str, fieldName: str) -> None:
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

class MissingMemberException(MemberAccessException, _Exception, ISerializable):
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
    @overload
    def __init__(self, className: str, memberName: str) -> None:
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

class MissingMethodException(MissingMemberException, _Exception, ISerializable):
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
    @overload
    def __init__(self, className: str, methodName: str) -> None:
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

class ModuleHandle(ValueType):
    """"""

    EmptyHandle: ClassVar[ModuleHandle]
    """"""
    @property
    def MDStreamVersion(self) -> int:
        """"""
    @overload
    def Equals(self, handle: ModuleHandle) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetRuntimeFieldHandleFromMetadataToken(self, fieldToken: int) -> RuntimeFieldHandle:
        """"""
    def GetRuntimeMethodHandleFromMetadataToken(self, methodToken: int) -> RuntimeMethodHandle:
        """"""
    def GetRuntimeTypeHandleFromMetadataToken(self, typeToken: int) -> RuntimeTypeHandle:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def ResolveFieldHandle(self, fieldToken: int) -> RuntimeFieldHandle:
        """"""
    @overload
    def ResolveFieldHandle(
        self,
        fieldToken: int,
        typeInstantiationContext: Array[RuntimeTypeHandle],
        methodInstantiationContext: Array[RuntimeTypeHandle],
    ) -> RuntimeFieldHandle:
        """"""
    @overload
    def ResolveMethodHandle(self, methodToken: int) -> RuntimeMethodHandle:
        """"""
    @overload
    def ResolveMethodHandle(
        self,
        methodToken: int,
        typeInstantiationContext: Array[RuntimeTypeHandle],
        methodInstantiationContext: Array[RuntimeTypeHandle],
    ) -> RuntimeMethodHandle:
        """"""
    @overload
    def ResolveTypeHandle(self, typeToken: int) -> RuntimeTypeHandle:
        """"""
    @overload
    def ResolveTypeHandle(
        self,
        typeToken: int,
        typeInstantiationContext: Array[RuntimeTypeHandle],
        methodInstantiationContext: Array[RuntimeTypeHandle],
    ) -> RuntimeTypeHandle:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, left: ModuleHandle, right: ModuleHandle) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: ModuleHandle, right: ModuleHandle) -> bool:
        """"""
    def __eq__(self, other: ModuleHandle) -> bool:
        """"""
    def __ne__(self, other: ModuleHandle) -> bool:
        """"""

class MulticastDelegate(ABC, Delegate, ISerializable, ICloneable):
    """"""
    @property
    def Method(self) -> MethodInfo:
        """"""
    @property
    def Target(self) -> object:
        """"""
    def Clone(self) -> object:
        """"""
    def DynamicInvoke(self, args: Array[object]) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetInvocationList(self) -> Array[Delegate]:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, d1: MulticastDelegate, d2: MulticastDelegate) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, d1: MulticastDelegate, d2: MulticastDelegate) -> bool:
        """"""
    def __eq__(self, other: MulticastDelegate) -> bool:
        """"""
    def __ne__(self, other: MulticastDelegate) -> bool:
        """"""

class MulticastNotSupportedException(SystemException, _Exception, ISerializable):
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

class NetPipeStyleUriParser(UriParser):
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

class NetTcpStyleUriParser(UriParser):
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

class NewsStyleUriParser(UriParser):
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

class NonSerializedAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
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

class NotFiniteNumberException(ArithmeticException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, offendingNumber: float) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, offendingNumber: float) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
        """"""
    @overload
    def __init__(self, message: str, offendingNumber: float, innerException: Exception) -> None:
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
    def OffendingNumber(self) -> float:
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

class NotImplementedException(SystemException, _Exception, ISerializable):
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

class NotSupportedException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
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

class NullReferenceException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
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

class Nullable(ABC, Object):
    """"""
    @classmethod
    def Compare[T, T](cls, n1: T | None, n2: T | None) -> int:
        """"""
    @classmethod
    @overload
    def Equals[T, T](cls, n1: T | None, n2: T | None) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def GetUnderlyingType(cls, nullableType: Type) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Nullable[T](ValueType):
    """"""
    def __init__(self, value: T) -> None:
        """"""
    @property
    def HasValue(self) -> bool:
        """"""
    @property
    def Value(self) -> T:
        """"""
    def Equals(self, other: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def GetValueOrDefault[T, T](self, defaultValue: T) -> T:
        """"""
    @overload
    def GetValueOrDefault[T](self) -> T:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Explicit[T](cls, value: Nullable[T]) -> T:
        """"""
    @classmethod
    def op_Implicit[T](cls, value: T) -> Nullable[T]:
        """"""

class Number(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    def FormatDecimal(cls, value: Decimal, format: str, info: NumberFormatInfo) -> str:
        """"""
    @classmethod
    def FormatDouble(cls, value: float, format: str, info: NumberFormatInfo) -> str:
        """"""
    @classmethod
    def FormatInt32(cls, value: int, format: str, info: NumberFormatInfo) -> str:
        """"""
    @classmethod
    def FormatInt64(cls, value: int, format: str, info: NumberFormatInfo) -> str:
        """"""
    @classmethod
    def FormatSingle(cls, value: float, format: str, info: NumberFormatInfo) -> str:
        """"""
    @classmethod
    def FormatUInt32(cls, value: int, format: str, info: NumberFormatInfo) -> str:
        """"""
    @classmethod
    def FormatUInt64(cls, value: int, format: str, info: NumberFormatInfo) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def NumberBufferToDecimal(cls, number: int, value: Decimal) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class Object:
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @classmethod
    @overload
    def Equals(cls, objA: object, objB: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def ReferenceEquals(cls, objA: object, objB: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""

class ObjectDisposedException(InvalidOperationException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self, objectName: str) -> None:
        """"""
    @overload
    def __init__(self, objectName: str, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
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
    def ObjectName(self) -> str:
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

class ObsoleteAttribute(Attribute, _Attribute):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, error: bool) -> None:
        """"""
    @property
    def IsError(self) -> bool:
        """"""
    @property
    def Message(self) -> str:
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

class OleAutBinder(DefaultBinder):
    """"""
    def __init__(self) -> None:
        """"""
    def BindToField(
        self,
        bindingAttr: BindingFlags,
        match: Array[FieldInfo],
        value: object,
        cultureInfo: CultureInfo,
    ) -> FieldInfo:
        """"""
    def BindToMethod(
        self,
        bindingAttr: BindingFlags,
        match: Array[MethodBase],
        args: Object,
        modifiers: Array[ParameterModifier],
        cultureInfo: CultureInfo,
        names: Array[str],
        state: Object,
    ) -> tuple[MethodBase, Object]:
        """"""
    def ChangeType(self, value: object, type: Type, cultureInfo: CultureInfo) -> object:
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

class OperatingSystem(Object, ISerializable, ICloneable):
    """"""
    def __init__(self, platform: PlatformID, version: Version) -> None:
        """"""
    @property
    def Platform(self) -> PlatformID:
        """"""
    @property
    def ServicePack(self) -> str:
        """"""
    @property
    def Version(self) -> Version:
        """"""
    @property
    def VersionString(self) -> str:
        """"""
    def Clone(self) -> object:
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

class OperationCanceledException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
        """"""
    @overload
    def __init__(self, token: CancellationToken) -> None:
        """"""
    @overload
    def __init__(self, message: str, token: CancellationToken) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception, token: CancellationToken) -> None:
        """"""
    @property
    def CancellationToken(self) -> CancellationToken:
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

class OrdinalComparer(
    StringComparer,
    IComparer[String],
    IEqualityComparer[String],
    IComparer,
    IEqualityComparer,
    IWellKnownStringEqualityComparer,
):
    """"""
    @overload
    def Compare(self, x: object, y: object) -> int:
        """"""
    @overload
    def Compare(self, x: str, y: str) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, x: object, y: object) -> bool:
        """"""
    @overload
    def Equals(self, x: str, y: str) -> bool:
        """"""
    def GetEqualityComparerForSerialization(self) -> IEqualityComparer:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, obj: object) -> int:
        """"""
    @overload
    def GetHashCode(self, obj: str) -> int:
        """"""
    def GetRandomizedEqualityComparer(self) -> IEqualityComparer:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class OrdinalRandomizedComparer(
    StringComparer,
    IComparer[String],
    IEqualityComparer[String],
    IComparer,
    IEqualityComparer,
    IWellKnownStringEqualityComparer,
):
    """"""
    @overload
    def Compare(self, x: object, y: object) -> int:
        """"""
    @overload
    def Compare(self, x: str, y: str) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, x: object, y: object) -> bool:
        """"""
    @overload
    def Equals(self, x: str, y: str) -> bool:
        """"""
    def GetEqualityComparerForSerialization(self) -> IEqualityComparer:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, obj: object) -> int:
        """"""
    @overload
    def GetHashCode(self, obj: str) -> int:
        """"""
    def GetRandomizedEqualityComparer(self) -> IEqualityComparer:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class OutOfMemoryException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
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

class OverflowException(ArithmeticException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
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

class ParamArrayAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
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

class ParamsArray(ValueType):
    """"""
    @overload
    def __init__(self, arg0: object) -> None:
        """"""
    @overload
    def __init__(self, arg0: object, arg1: object) -> None:
        """"""
    @overload
    def __init__(self, arg0: object, arg1: object, arg2: object) -> None:
        """"""
    @overload
    def __init__(self, args: Array[object]) -> None:
        """"""
    @property
    def Item(self) -> object:
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
    def __getitem__(self, index: int) -> object:
        """"""

class ParseFailureKind(Enum):
    """"""

    _None: ParseFailureKind = ...
    """"""
    ArgumentNull: ParseFailureKind = ...
    """"""
    Format: ParseFailureKind = ...
    """"""
    FormatWithParameter: ParseFailureKind = ...
    """"""
    FormatBadDateTimeCalendar: ParseFailureKind = ...
    """"""

class ParseFlags(Enum):
    """"""

    HaveYear: ParseFlags = ...
    """"""
    HaveMonth: ParseFlags = ...
    """"""
    HaveDay: ParseFlags = ...
    """"""
    HaveHour: ParseFlags = ...
    """"""
    HaveMinute: ParseFlags = ...
    """"""
    HaveSecond: ParseFlags = ...
    """"""
    HaveTime: ParseFlags = ...
    """"""
    HaveDate: ParseFlags = ...
    """"""
    TimeZoneUsed: ParseFlags = ...
    """"""
    TimeZoneUtc: ParseFlags = ...
    """"""
    ParsedMonthName: ParseFlags = ...
    """"""
    CaptureOffset: ParseFlags = ...
    """"""
    YearDefault: ParseFlags = ...
    """"""
    Rfc1123Pattern: ParseFlags = ...
    """"""
    UtcSortPattern: ParseFlags = ...
    """"""

class ParseNumbers(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IntToString(cls, l: int, radix: int, width: int, paddingChar: Char, flags: int) -> str:
        """"""
    @classmethod
    def LongToString(cls, l: int, radix: int, width: int, paddingChar: Char, flags: int) -> str:
        """"""
    @classmethod
    @overload
    def StringToInt(cls, s: str, radix: int, flags: int) -> int:
        """"""
    @classmethod
    @overload
    def StringToInt(cls, s: str, radix: int, flags: int, currPos: Int32) -> int:
        """"""
    @classmethod
    @overload
    def StringToInt(cls, s: str, radix: int, flags: int, currPos: int) -> int:
        """"""
    @classmethod
    @overload
    def StringToLong(cls, s: str, radix: int, flags: int) -> int:
        """"""
    @classmethod
    @overload
    def StringToLong(cls, s: str, radix: int, flags: int, currPos: Int32) -> int:
        """"""
    @classmethod
    @overload
    def StringToLong(cls, s: str, radix: int, flags: int, currPos: int) -> int:
        """"""
    def ToString(self) -> str:
        """"""

class ParsingError(Enum):
    """"""

    _None: ParsingError = ...
    """"""
    BadFormat: ParsingError = ...
    """"""
    BadScheme: ParsingError = ...
    """"""
    BadAuthority: ParsingError = ...
    """"""
    EmptyUriString: ParsingError = ...
    """"""
    LastRelativeUriOkErrIndex: ParsingError = ...
    """"""
    SchemeLimit: ParsingError = ...
    """"""
    SizeLimit: ParsingError = ...
    """"""
    MustRootedPath: ParsingError = ...
    """"""
    BadHostName: ParsingError = ...
    """"""
    NonEmptyHost: ParsingError = ...
    """"""
    BadPort: ParsingError = ...
    """"""
    BadAuthorityTerminator: ParsingError = ...
    """"""
    CannotCreateRelative: ParsingError = ...
    """"""

class ParsingInfo(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class PinnableBufferCache(Object):
    """"""
    def __init__(self, cacheName: str, numberOfElements: int) -> None:
        """"""
    def AllocateBuffer(self) -> Array[int]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FreeBuffer(self, buffer: Array[int]) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class PinnableBufferCacheEventSource(EventSource, IDisposable):
    """"""

    Log: ClassVar[PinnableBufferCacheEventSource]
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def ConstructionException(self) -> Exception:
        """"""
    @property
    def Guid(self) -> Guid:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def Settings(self) -> EventSourceSettings:
        """"""
    def AgePendingBuffersResults(
        self, cacheName: str, promotedToFreeListCount: int, heldBackCount: int
    ) -> None:
        """"""
    def AllocateBuffer(
        self, cacheName: str, objectId: int, objectHash: int, objectGen: int, freeCountAfter: int
    ) -> None:
        """"""
    def AllocateBufferAged(self, cacheName: str, agedCount: int) -> None:
        """"""
    def AllocateBufferCreatingNewBuffers(
        self, cacheName: str, totalBuffsBefore: int, objectCount: int
    ) -> None:
        """"""
    def AllocateBufferFreeListEmpty(self, cacheName: str, notGen2CountBefore: int) -> None:
        """"""
    def AllocateBufferFromNotGen2(self, cacheName: str, notGen2CountAfter: int) -> None:
        """"""
    def Create(self, cacheName: str) -> None:
        """"""
    def DebugMessage(self, message: str) -> None:
        """"""
    def DebugMessage1(self, message: str, value: int) -> None:
        """"""
    def DebugMessage2(self, message: str, value1: int, value2: int) -> None:
        """"""
    def DebugMessage3(self, message: str, value1: int, value2: int, value3: int) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def FreeBuffer(
        self, cacheName: str, objectId: int, objectHash: int, freeCountBefore: int
    ) -> None:
        """"""
    def FreeBufferNull(self, cacheName: str, freeCountBefore: int) -> None:
        """"""
    def FreeBufferStillTooYoung(self, cacheName: str, notGen2CountBefore: int) -> None:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetTrait(self, key: str) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsEnabled(self) -> bool:
        """"""
    @overload
    def IsEnabled(self, level: EventLevel, keywords: EventKeywords) -> bool:
        """"""
    @overload
    def IsEnabled(self, level: EventLevel, keywords: EventKeywords, channel: EventChannel) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    def TrimCheck(
        self, cacheName: str, totalBuffs: int, neededMoreThanFreeList: bool, deltaMSec: int
    ) -> None:
        """"""
    def TrimExperiment(
        self, cacheName: str, totalBuffs: int, freeListCount: int, numTrimTrial: int
    ) -> None:
        """"""
    def TrimFlush(
        self, cacheName: str, totalBuffs: int, freeListCount: int, notGen2CountBefore: int
    ) -> None:
        """"""
    def TrimFree(self, cacheName: str, totalBuffs: int, freeListCount: int, toBeFreed: int) -> None:
        """"""
    def TrimFreeSizeOK(self, cacheName: str, totalBuffs: int, freeListCount: int) -> None:
        """"""
    def WalkFreeListResult(
        self, cacheName: str, freeListCount: int, gen0BuffersInFreeList: int
    ) -> None:
        """"""
    @overload
    def Write(self, eventName: str) -> None:
        """"""
    @overload
    def Write[T](self, eventName: str, data: T) -> None:
        """"""
    @overload
    def Write(self, eventName: str, options: EventSourceOptions, data: T) -> None:
        """"""
    @overload
    def Write(
        self,
        eventName: str,
        options: EventSourceOptions,
        activityId: Guid,
        relatedActivityId: Guid,
        data: T,
    ) -> None:
        """"""
    @overload
    def Write(self, eventName: str, options: EventSourceOptions) -> None:
        """"""
    @overload
    def Write[T](self, eventName: str, options: EventSourceOptions, data: T) -> None:
        """"""
    EventCommandExecuted: EventType[EventHandler[EventCommandEventArgs]] = ...
    """"""

class PlatformID(Enum):
    """"""

    Win32S: PlatformID = ...
    """"""
    Win32Windows: PlatformID = ...
    """"""
    Win32NT: PlatformID = ...
    """"""
    WinCE: PlatformID = ...
    """"""
    Unix: PlatformID = ...
    """"""
    Xbox: PlatformID = ...
    """"""
    MacOSX: PlatformID = ...
    """"""

class PlatformNotSupportedException(NotSupportedException, _Exception, ISerializable):
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

Predicate: Callable[[T], bool] = ...
""""""

class ProgressStatics(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Progress[T](Object, IProgress[T]):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, handler: Action[T]) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Report[T](self, value: T) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    ProgressChanged: EventType[EventHandler[T]] = ...
    """"""

class Random(Object):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, Seed: int) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def Next(self) -> int:
        """"""
    @overload
    def Next(self, maxValue: int) -> int:
        """"""
    @overload
    def Next(self, minValue: int, maxValue: int) -> int:
        """"""
    def NextBytes(self, buffer: Array[int]) -> None:
        """"""
    def NextDouble(self) -> float:
        """"""
    def ToString(self) -> str:
        """"""

class RankException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
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

class ReflectionOnlyType(
    RuntimeType,
    ICustomAttributeProvider,
    IReflect,
    IReflectableType,
    _MemberInfo,
    _Type,
    ISerializable,
    ICloneable,
):
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
    def Clone(self) -> object:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
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
    def GetInterface(self, fullname: str, ignoreCase: bool) -> Type:
        """"""
    def GetInterfaceMap(self, ifaceType: Type) -> InterfaceMapping:
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
    def GetNestedType(self, fullname: str, bindingAttr: BindingFlags) -> Type:
        """"""
    @overload
    def GetNestedTypes(self) -> Array[Type]:
        """"""
    @overload
    def GetNestedTypes(self, bindingAttr: BindingFlags) -> Array[Type]:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
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
        bindingFlags: BindingFlags,
        binder: Binder,
        target: object,
        providedArgs: Array[object],
        modifiers: Array[ParameterModifier],
        culture: CultureInfo,
        namedParams: Array[str],
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
    def IsSubclassOf(self, type: Type) -> bool:
        """"""
    @overload
    def MakeArrayType(self) -> Type:
        """"""
    @overload
    def MakeArrayType(self, rank: int) -> Type:
        """"""
    def MakeByRefType(self) -> Type:
        """"""
    def MakeGenericType(self, instantiation: Array[Type]) -> Type:
        """"""
    def MakePointerType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ResId(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ResolveEventArgs(EventArgs):
    """"""
    @overload
    def __init__(self, name: str) -> None:
        """"""
    @overload
    def __init__(self, name: str, requestingAssembly: Assembly) -> None:
        """"""
    @property
    def Name(self) -> str:
        """"""
    @property
    def RequestingAssembly(self) -> Assembly:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

ResolveEventHandler: Callable[[object, ResolveEventArgs], Assembly] = ...
""""""

class Resolver(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RuntimeArgumentHandle(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RuntimeFieldHandle(ValueType, ISerializable):
    """"""
    @property
    def Value(self) -> IntPtr:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, handle: RuntimeFieldHandle) -> bool:
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
    def op_Equality(cls, left: RuntimeFieldHandle, right: RuntimeFieldHandle) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: RuntimeFieldHandle, right: RuntimeFieldHandle) -> bool:
        """"""
    def __eq__(self, other: RuntimeFieldHandle) -> bool:
        """"""
    def __ne__(self, other: RuntimeFieldHandle) -> bool:
        """"""

class RuntimeFieldHandleInternal(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RuntimeFieldInfoStub(Object, IRuntimeFieldInfo):
    """"""
    def __init__(self, methodHandleValue: IntPtr, keepalive: object) -> None:
        """"""
    @property
    def Value(self) -> RuntimeFieldHandleInternal:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RuntimeMethodHandle(ValueType, ISerializable):
    """"""
    @property
    def Value(self) -> IntPtr:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, handle: RuntimeMethodHandle) -> bool:
        """"""
    def GetFunctionPointer(self) -> IntPtr:
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
    def op_Equality(cls, left: RuntimeMethodHandle, right: RuntimeMethodHandle) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: RuntimeMethodHandle, right: RuntimeMethodHandle) -> bool:
        """"""
    def __eq__(self, other: RuntimeMethodHandle) -> bool:
        """"""
    def __ne__(self, other: RuntimeMethodHandle) -> bool:
        """"""

class RuntimeMethodHandleInternal(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RuntimeMethodInfoStub(Object, IRuntimeMethodInfo):
    """"""

    m_value: Final[RuntimeMethodHandleInternal]
    """"""
    @overload
    def __init__(self, methodHandleValue: RuntimeMethodHandleInternal, keepalive: object) -> None:
        """"""
    @overload
    def __init__(self, methodHandleValue: IntPtr, keepalive: object) -> None:
        """"""
    @property
    def Value(self) -> RuntimeMethodHandleInternal:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class RuntimeType(
    TypeInfo,
    ICustomAttributeProvider,
    IReflect,
    IReflectableType,
    _MemberInfo,
    _Type,
    ISerializable,
    ICloneable,
):
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
    def Clone(self) -> object:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
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
    def GetInterface(self, fullname: str, ignoreCase: bool) -> Type:
        """"""
    def GetInterfaceMap(self, ifaceType: Type) -> InterfaceMapping:
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
    def GetNestedType(self, fullname: str, bindingAttr: BindingFlags) -> Type:
        """"""
    @overload
    def GetNestedTypes(self) -> Array[Type]:
        """"""
    @overload
    def GetNestedTypes(self, bindingAttr: BindingFlags) -> Array[Type]:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
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
        bindingFlags: BindingFlags,
        binder: Binder,
        target: object,
        providedArgs: Array[object],
        modifiers: Array[ParameterModifier],
        culture: CultureInfo,
        namedParams: Array[str],
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
    def IsSubclassOf(self, type: Type) -> bool:
        """"""
    @overload
    def MakeArrayType(self) -> Type:
        """"""
    @overload
    def MakeArrayType(self, rank: int) -> Type:
        """"""
    def MakeByRefType(self) -> Type:
        """"""
    def MakeGenericType(self, instantiation: Array[Type]) -> Type:
        """"""
    def MakePointerType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, left: RuntimeType, right: RuntimeType) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: RuntimeType, right: RuntimeType) -> bool:
        """"""
    def __eq__(self, other: RuntimeType) -> bool:
        """"""
    def __ne__(self, other: RuntimeType) -> bool:
        """"""

class RuntimeTypeHandle(ValueType, ISerializable):
    """"""
    @property
    def Value(self) -> IntPtr:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, handle: RuntimeTypeHandle) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetModuleHandle(self) -> ModuleHandle:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    @overload
    def op_Equality(cls, left: object, right: RuntimeTypeHandle) -> bool:
        """"""
    @classmethod
    @overload
    def op_Equality(cls, left: RuntimeTypeHandle, right: object) -> bool:
        """"""
    @classmethod
    @overload
    def op_Inequality(cls, left: object, right: RuntimeTypeHandle) -> bool:
        """"""
    @classmethod
    @overload
    def op_Inequality(cls, left: RuntimeTypeHandle, right: object) -> bool:
        """"""
    @overload
    def __eq__(self, other: RuntimeTypeHandle) -> bool:
        """"""
    @overload
    def __eq__(self, other: object) -> bool:
        """"""
    @overload
    def __ne__(self, other: RuntimeTypeHandle) -> bool:
        """"""
    @overload
    def __ne__(self, other: object) -> bool:
        """"""

class SByte(
    ValueType, IComparable, IComparable[SByte], IConvertible, IEquatable[SByte], IFormattable
):
    """"""

    MaxValue: ClassVar[int]
    """"""
    MinValue: ClassVar[int]
    """"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """"""
    @overload
    def CompareTo(self, value: int) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, obj: int) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeCode(self) -> TypeCode:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str) -> int:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles) -> int:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, provider: IFormatProvider) -> int:
        """"""
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """"""
    def ToByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToChar(self, provider: IFormatProvider) -> Char:
        """"""
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """"""
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """"""
    def ToDouble(self, provider: IFormatProvider) -> float:
        """"""
    def ToInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt64(self, provider: IFormatProvider) -> int:
        """"""
    def ToSByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToSingle(self, provider: IFormatProvider) -> float:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """"""
    @overload
    def ToString(self, format: str) -> str:
        """"""
    @overload
    def ToString(self, format: str, provider: IFormatProvider) -> str:
        """"""
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """"""
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def TryParse(
        cls, s: str, style: NumberStyles, provider: IFormatProvider, result: SByte
    ) -> tuple[bool, SByte]:
        """"""
    @classmethod
    @overload
    def TryParse(cls, s: str, result: SByte) -> tuple[bool, SByte]:
        """"""

class SR(Object):
    """"""
    @classmethod
    @property
    def Resources(cls) -> ResourceManager:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetObject(cls, name: str) -> object:
        """"""
    @classmethod
    @overload
    def GetString(cls, name: str) -> str:
        """"""
    @classmethod
    @overload
    def GetString(cls, name: str, usedFallback: Boolean) -> tuple[str, Boolean]:
        """"""
    @classmethod
    @overload
    def GetString(cls, name: str, args: Array[object]) -> str:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SRCategoryAttribute(CategoryAttribute, _Attribute):
    """"""
    def __init__(self, category: str) -> None:
        """"""
    @property
    def Category(self) -> str:
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

class SRDescriptionAttribute(DescriptionAttribute, _Attribute):
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

class STAThreadAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
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

class SZArrayHelper(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SafeTypeNameParserHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """"""
    def __init__(self) -> None:
        """"""
    @property
    def IsClosed(self) -> bool:
        """"""
    @property
    def IsInvalid(self) -> bool:
        """"""
    def Close(self) -> None:
        """"""
    def DangerousAddRef(self, success: Boolean) -> None:
        """"""
    def DangerousGetHandle(self) -> IntPtr:
        """"""
    def DangerousRelease(self) -> None:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetHandleAsInvalid(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class SecurityUtils(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SerializableAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
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

class SharedStatics(Object):
    """"""
    @classmethod
    @property
    def Remoting_Identity_IDGuid(cls) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetSharedStringMaker(cls) -> Tokenizer.StringMaker:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def ReleaseSharedStringMaker(cls, maker: StringMaker) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class Signature(Object):
    """"""
    @overload
    def __init__(
        self,
        method: IRuntimeMethodInfo,
        arguments: Array[RuntimeType],
        returnType: RuntimeType,
        callingConvention: CallingConventions,
    ) -> None:
        """"""
    @overload
    def __init__(self, methodHandle: IRuntimeMethodInfo, declaringType: RuntimeType) -> None:
        """"""
    @overload
    def __init__(self, fieldHandle: IRuntimeFieldInfo, declaringType: RuntimeType) -> None:
        """"""
    @overload
    def __init__(self, pCorSig: None, cCorSig: int, declaringType: RuntimeType) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Single(
    ValueType, IComparable, IComparable[Single], IConvertible, IEquatable[Single], IFormattable
):
    """"""

    Epsilon: ClassVar[float]
    """"""
    MaxValue: ClassVar[float]
    """"""
    MinValue: ClassVar[float]
    """"""
    NaN: ClassVar[float]
    """"""
    NegativeInfinity: ClassVar[float]
    """"""
    PositiveInfinity: ClassVar[float]
    """"""
    @overload
    def CompareTo(self, value: object) -> int:
        """"""
    @overload
    def CompareTo(self, value: float) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, obj: float) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeCode(self) -> TypeCode:
        """"""
    @classmethod
    def IsInfinity(cls, f: float) -> bool:
        """"""
    @classmethod
    def IsNaN(cls, f: float) -> bool:
        """"""
    @classmethod
    def IsNegativeInfinity(cls, f: float) -> bool:
        """"""
    @classmethod
    def IsPositiveInfinity(cls, f: float) -> bool:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str) -> float:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles) -> float:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles, provider: IFormatProvider) -> float:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, provider: IFormatProvider) -> float:
        """"""
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """"""
    def ToByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToChar(self, provider: IFormatProvider) -> Char:
        """"""
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """"""
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """"""
    def ToDouble(self, provider: IFormatProvider) -> float:
        """"""
    def ToInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt64(self, provider: IFormatProvider) -> int:
        """"""
    def ToSByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToSingle(self, provider: IFormatProvider) -> float:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """"""
    @overload
    def ToString(self, format: str) -> str:
        """"""
    @overload
    def ToString(self, format: str, provider: IFormatProvider) -> str:
        """"""
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """"""
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def TryParse(
        cls, s: str, style: NumberStyles, provider: IFormatProvider, result: Single
    ) -> tuple[bool, Single]:
        """"""
    @classmethod
    @overload
    def TryParse(cls, s: str, result: Single) -> tuple[bool, Single]:
        """"""
    @classmethod
    def op_Equality(cls, left: float, right: float) -> bool:
        """"""
    @classmethod
    def op_GreaterThan(cls, left: float, right: float) -> bool:
        """"""
    @classmethod
    def op_GreaterThanOrEqual(cls, left: float, right: float) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: float, right: float) -> bool:
        """"""
    @classmethod
    def op_LessThan(cls, left: float, right: float) -> bool:
        """"""
    @classmethod
    def op_LessThanOrEqual(cls, left: float, right: float) -> bool:
        """"""
    def __eq__(self, other: float) -> bool:
        """"""
    def __gt__(self, other: float) -> bool:
        """"""
    def __ge__(self, other: float) -> bool:
        """"""
    def __ne__(self, other: float) -> bool:
        """"""
    def __lt__(self, other: float) -> bool:
        """"""
    def __le__(self, other: float) -> bool:
        """"""

class SizedReference(Object, IDisposable):
    """"""
    def __init__(self, target: object) -> None:
        """"""
    @property
    def ApproximateSize(self) -> int:
        """"""
    @property
    def Target(self) -> object:
        """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class StackOverflowException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
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

class String(
    Object,
    IEnumerable[Char],
    IEnumerable,
    ICloneable,
    IComparable,
    IComparable[String],
    IConvertible,
    IEquatable[String],
):
    """"""

    Empty: ClassVar[str]
    """"""
    @overload
    def __init__(self, value: Char) -> None:
        """"""
    @overload
    def __init__(self, value: Char, startIndex: int, length: int) -> None:
        """"""
    @overload
    def __init__(self, value: int) -> None:
        """"""
    @overload
    def __init__(self, value: int, startIndex: int, length: int) -> None:
        """"""
    @overload
    def __init__(self, value: int, startIndex: int, length: int, enc: Encoding) -> None:
        """"""
    @overload
    def __init__(self, value: Array[Char], startIndex: int, length: int) -> None:
        """"""
    @overload
    def __init__(self, value: Array[Char]) -> None:
        """"""
    @overload
    def __init__(self, c: Char, count: int) -> None:
        """"""
    @property
    def Chars(self) -> Char:
        """"""
    @property
    def Length(self) -> int:
        """"""
    def Clone(self) -> object:
        """"""
    @classmethod
    @overload
    def Compare(cls, strA: str, indexA: int, strB: str, indexB: int, length: int) -> int:
        """"""
    @classmethod
    @overload
    def Compare(
        cls,
        strA: str,
        indexA: int,
        strB: str,
        indexB: int,
        length: int,
        culture: CultureInfo,
        options: CompareOptions,
    ) -> int:
        """"""
    @classmethod
    @overload
    def Compare(
        cls, strA: str, indexA: int, strB: str, indexB: int, length: int, ignoreCase: bool
    ) -> int:
        """"""
    @classmethod
    @overload
    def Compare(
        cls,
        strA: str,
        indexA: int,
        strB: str,
        indexB: int,
        length: int,
        ignoreCase: bool,
        culture: CultureInfo,
    ) -> int:
        """"""
    @classmethod
    @overload
    def Compare(
        cls,
        strA: str,
        indexA: int,
        strB: str,
        indexB: int,
        length: int,
        comparisonType: StringComparison,
    ) -> int:
        """"""
    @classmethod
    @overload
    def Compare(cls, strA: str, strB: str) -> int:
        """"""
    @classmethod
    @overload
    def Compare(cls, strA: str, strB: str, culture: CultureInfo, options: CompareOptions) -> int:
        """"""
    @classmethod
    @overload
    def Compare(cls, strA: str, strB: str, ignoreCase: bool) -> int:
        """"""
    @classmethod
    @overload
    def Compare(cls, strA: str, strB: str, ignoreCase: bool, culture: CultureInfo) -> int:
        """"""
    @classmethod
    @overload
    def Compare(cls, strA: str, strB: str, comparisonType: StringComparison) -> int:
        """"""
    @classmethod
    @overload
    def CompareOrdinal(cls, strA: str, indexA: int, strB: str, indexB: int, length: int) -> int:
        """"""
    @classmethod
    @overload
    def CompareOrdinal(cls, strA: str, strB: str) -> int:
        """"""
    @overload
    def CompareTo(self, value: object) -> int:
        """"""
    @overload
    def CompareTo(self, strB: str) -> int:
        """"""
    @classmethod
    @overload
    def Concat(cls, values: IEnumerable[T]) -> str:
        """"""
    @classmethod
    @overload
    def Concat(cls, values: IEnumerable[str]) -> str:
        """"""
    @classmethod
    @overload
    def Concat(cls, args: Array[object]) -> str:
        """"""
    @classmethod
    @overload
    def Concat(cls, values: Array[str]) -> str:
        """"""
    @classmethod
    @overload
    def Concat(cls, arg0: object) -> str:
        """"""
    @classmethod
    @overload
    def Concat(cls, arg0: object, arg1: object) -> str:
        """"""
    @classmethod
    @overload
    def Concat(cls, arg0: object, arg1: object, arg2: object) -> str:
        """"""
    @classmethod
    @overload
    def Concat(cls, arg0: object, arg1: object, arg2: object, arg3: object) -> str:
        """"""
    @classmethod
    @overload
    def Concat(cls, str0: str, str1: str) -> str:
        """"""
    @classmethod
    @overload
    def Concat(cls, str0: str, str1: str, str2: str) -> str:
        """"""
    @classmethod
    @overload
    def Concat(cls, str0: str, str1: str, str2: str, str3: str) -> str:
        """"""
    def Contains(self, value: str) -> bool:
        """"""
    @classmethod
    def Copy(cls, str: str) -> str:
        """"""
    def CopyTo(
        self, sourceIndex: int, destination: Array[Char], destinationIndex: int, count: int
    ) -> None:
        """"""
    @overload
    def EndsWith(self, value: str) -> bool:
        """"""
    @overload
    def EndsWith(self, value: str, ignoreCase: bool, culture: CultureInfo) -> bool:
        """"""
    @overload
    def EndsWith(self, value: str, comparisonType: StringComparison) -> bool:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, value: str) -> bool:
        """"""
    @classmethod
    @overload
    def Equals(cls, a: str, b: str) -> bool:
        """"""
    @classmethod
    @overload
    def Equals(cls, a: str, b: str, comparisonType: StringComparison) -> bool:
        """"""
    @overload
    def Equals(self, value: str, comparisonType: StringComparison) -> bool:
        """"""
    @classmethod
    @overload
    def Format(cls, provider: IFormatProvider, format: str, args: Array[object]) -> str:
        """"""
    @classmethod
    @overload
    def Format(cls, provider: IFormatProvider, format: str, arg0: object) -> str:
        """"""
    @classmethod
    @overload
    def Format(cls, provider: IFormatProvider, format: str, arg0: object, arg1: object) -> str:
        """"""
    @classmethod
    @overload
    def Format(
        cls, provider: IFormatProvider, format: str, arg0: object, arg1: object, arg2: object
    ) -> str:
        """"""
    @classmethod
    @overload
    def Format(cls, format: str, args: Array[object]) -> str:
        """"""
    @classmethod
    @overload
    def Format(cls, format: str, arg0: object) -> str:
        """"""
    @classmethod
    @overload
    def Format(cls, format: str, arg0: object, arg1: object) -> str:
        """"""
    @classmethod
    @overload
    def Format(cls, format: str, arg0: object, arg1: object, arg2: object) -> str:
        """"""
    def GetEnumerator(self) -> CharEnumerator:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeCode(self) -> TypeCode:
        """"""
    @overload
    def IndexOf(self, value: Char) -> int:
        """"""
    @overload
    def IndexOf(self, value: Char, startIndex: int) -> int:
        """"""
    @overload
    def IndexOf(self, value: Char, startIndex: int, count: int) -> int:
        """"""
    @overload
    def IndexOf(self, value: str) -> int:
        """"""
    @overload
    def IndexOf(self, value: str, startIndex: int) -> int:
        """"""
    @overload
    def IndexOf(self, value: str, startIndex: int, count: int) -> int:
        """"""
    @overload
    def IndexOf(
        self, value: str, startIndex: int, count: int, comparisonType: StringComparison
    ) -> int:
        """"""
    @overload
    def IndexOf(self, value: str, startIndex: int, comparisonType: StringComparison) -> int:
        """"""
    @overload
    def IndexOf(self, value: str, comparisonType: StringComparison) -> int:
        """"""
    @overload
    def IndexOfAny(self, anyOf: Array[Char]) -> int:
        """"""
    @overload
    def IndexOfAny(self, anyOf: Array[Char], startIndex: int) -> int:
        """"""
    @overload
    def IndexOfAny(self, anyOf: Array[Char], startIndex: int, count: int) -> int:
        """"""
    def Insert(self, startIndex: int, value: str) -> str:
        """"""
    @classmethod
    def Intern(cls, str: str) -> str:
        """"""
    @classmethod
    def IsInterned(cls, str: str) -> str:
        """"""
    @overload
    def IsNormalized(self) -> bool:
        """"""
    @overload
    def IsNormalized(self, normalizationForm: NormalizationForm) -> bool:
        """"""
    @classmethod
    def IsNullOrEmpty(cls, value: str) -> bool:
        """"""
    @classmethod
    def IsNullOrWhiteSpace(cls, value: str) -> bool:
        """"""
    @classmethod
    @overload
    def Join(cls, separator: str, values: IEnumerable[T]) -> str:
        """"""
    @classmethod
    @overload
    def Join(cls, separator: str, values: IEnumerable[str]) -> str:
        """"""
    @classmethod
    @overload
    def Join(cls, separator: str, values: Array[object]) -> str:
        """"""
    @classmethod
    @overload
    def Join(cls, separator: str, value: Array[str]) -> str:
        """"""
    @classmethod
    @overload
    def Join(cls, separator: str, value: Array[str], startIndex: int, count: int) -> str:
        """"""
    @overload
    def LastIndexOf(self, value: Char) -> int:
        """"""
    @overload
    def LastIndexOf(self, value: Char, startIndex: int) -> int:
        """"""
    @overload
    def LastIndexOf(self, value: Char, startIndex: int, count: int) -> int:
        """"""
    @overload
    def LastIndexOf(self, value: str) -> int:
        """"""
    @overload
    def LastIndexOf(self, value: str, startIndex: int) -> int:
        """"""
    @overload
    def LastIndexOf(self, value: str, startIndex: int, count: int) -> int:
        """"""
    @overload
    def LastIndexOf(
        self, value: str, startIndex: int, count: int, comparisonType: StringComparison
    ) -> int:
        """"""
    @overload
    def LastIndexOf(self, value: str, startIndex: int, comparisonType: StringComparison) -> int:
        """"""
    @overload
    def LastIndexOf(self, value: str, comparisonType: StringComparison) -> int:
        """"""
    @overload
    def LastIndexOfAny(self, anyOf: Array[Char]) -> int:
        """"""
    @overload
    def LastIndexOfAny(self, anyOf: Array[Char], startIndex: int) -> int:
        """"""
    @overload
    def LastIndexOfAny(self, anyOf: Array[Char], startIndex: int, count: int) -> int:
        """"""
    @overload
    def Normalize(self) -> str:
        """"""
    @overload
    def Normalize(self, normalizationForm: NormalizationForm) -> str:
        """"""
    @overload
    def PadLeft(self, totalWidth: int) -> str:
        """"""
    @overload
    def PadLeft(self, totalWidth: int, paddingChar: Char) -> str:
        """"""
    @overload
    def PadRight(self, totalWidth: int) -> str:
        """"""
    @overload
    def PadRight(self, totalWidth: int, paddingChar: Char) -> str:
        """"""
    @overload
    def Remove(self, startIndex: int) -> str:
        """"""
    @overload
    def Remove(self, startIndex: int, count: int) -> str:
        """"""
    @overload
    def Replace(self, oldChar: Char, newChar: Char) -> str:
        """"""
    @overload
    def Replace(self, oldValue: str, newValue: str) -> str:
        """"""
    @overload
    def Split(self, separator: Array[Char]) -> Array[str]:
        """"""
    @overload
    def Split(self, separator: Array[Char], count: int) -> Array[str]:
        """"""
    @overload
    def Split(self, separator: Array[Char], count: int, options: StringSplitOptions) -> Array[str]:
        """"""
    @overload
    def Split(self, separator: Array[Char], options: StringSplitOptions) -> Array[str]:
        """"""
    @overload
    def Split(self, separator: Array[str], count: int, options: StringSplitOptions) -> Array[str]:
        """"""
    @overload
    def Split(self, separator: Array[str], options: StringSplitOptions) -> Array[str]:
        """"""
    @overload
    def StartsWith(self, value: str) -> bool:
        """"""
    @overload
    def StartsWith(self, value: str, ignoreCase: bool, culture: CultureInfo) -> bool:
        """"""
    @overload
    def StartsWith(self, value: str, comparisonType: StringComparison) -> bool:
        """"""
    @overload
    def Substring(self, startIndex: int) -> str:
        """"""
    @overload
    def Substring(self, startIndex: int, length: int) -> str:
        """"""
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """"""
    def ToByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToChar(self, provider: IFormatProvider) -> Char:
        """"""
    @overload
    def ToCharArray(self) -> Array[Char]:
        """"""
    @overload
    def ToCharArray(self, startIndex: int, length: int) -> Array[Char]:
        """"""
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """"""
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """"""
    def ToDouble(self, provider: IFormatProvider) -> float:
        """"""
    def ToInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt64(self, provider: IFormatProvider) -> int:
        """"""
    @overload
    def ToLower(self) -> str:
        """"""
    @overload
    def ToLower(self, culture: CultureInfo) -> str:
        """"""
    def ToLowerInvariant(self) -> str:
        """"""
    def ToSByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToSingle(self, provider: IFormatProvider) -> float:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """"""
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """"""
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """"""
    @overload
    def ToUpper(self) -> str:
        """"""
    @overload
    def ToUpper(self, culture: CultureInfo) -> str:
        """"""
    def ToUpperInvariant(self) -> str:
        """"""
    @overload
    def Trim(self) -> str:
        """"""
    @overload
    def Trim(self, trimChars: Array[Char]) -> str:
        """"""
    def TrimEnd(self, trimChars: Array[Char]) -> str:
        """"""
    def TrimStart(self, trimChars: Array[Char]) -> str:
        """"""
    @classmethod
    def op_Equality(cls, a: str, b: str) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, a: str, b: str) -> bool:
        """"""
    def __contains__(self, value: str) -> bool:
        """"""
    def __iter__(self) -> Iterator:
        """"""
    @overload
    def __delitem__(self, startIndex: int) -> str:
        """"""
    @overload
    def __delitem__(self, startIndex: int, count: int) -> str:
        """"""
    def __eq__(self, other: str) -> bool:
        """"""
    def __ne__(self, other: str) -> bool:
        """"""

class StringComparer(
    ABC, Object, IComparer[String], IEqualityComparer[String], IComparer, IEqualityComparer
):
    """"""
    @classmethod
    @property
    def CurrentCulture(cls) -> StringComparer:
        """"""
    @classmethod
    @property
    def CurrentCultureIgnoreCase(cls) -> StringComparer:
        """"""
    @classmethod
    @property
    def InvariantCulture(cls) -> StringComparer:
        """"""
    @classmethod
    @property
    def InvariantCultureIgnoreCase(cls) -> StringComparer:
        """"""
    @classmethod
    @property
    def Ordinal(cls) -> StringComparer:
        """"""
    @classmethod
    @property
    def OrdinalIgnoreCase(cls) -> StringComparer:
        """"""
    @overload
    def Compare(self, x: object, y: object) -> int:
        """"""
    @overload
    def Compare(self, x: str, y: str) -> int:
        """"""
    @classmethod
    def Create(cls, culture: CultureInfo, ignoreCase: bool) -> StringComparer:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, x: object, y: object) -> bool:
        """"""
    @overload
    def Equals(self, x: str, y: str) -> bool:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, obj: object) -> int:
        """"""
    @overload
    def GetHashCode(self, obj: str) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class StringComparison(Enum):
    """"""

    CurrentCulture: StringComparison = ...
    """"""
    CurrentCultureIgnoreCase: StringComparison = ...
    """"""
    InvariantCulture: StringComparison = ...
    """"""
    InvariantCultureIgnoreCase: StringComparison = ...
    """"""
    Ordinal: StringComparison = ...
    """"""
    OrdinalIgnoreCase: StringComparison = ...
    """"""

class StringNormalizationExtensions(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def IsNormalized(cls, value: str) -> bool:
        """"""
    @classmethod
    @overload
    def IsNormalized(cls, value: str, normalizationForm: NormalizationForm) -> bool:
        """"""
    @classmethod
    @overload
    def Normalize(cls, value: str) -> str:
        """"""
    @classmethod
    @overload
    def Normalize(cls, value: str, normalizationForm: NormalizationForm) -> str:
        """"""
    def ToString(self) -> str:
        """"""

class StringSplitOptions(Enum):
    """"""

    _None: StringSplitOptions = ...
    """"""
    RemoveEmptyEntries: StringSplitOptions = ...
    """"""

class SwitchStructure(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class SystemException(Exception, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
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

class System_LazyDebugView[T](Object):
    """"""
    def __init__(self, lazy: Lazy[T]) -> None:
        """"""
    @property
    def IsValueCreated(self) -> bool:
        """"""
    @property
    def IsValueFaulted(self) -> bool:
        """"""
    @property
    def Mode(self) -> LazyThreadSafetyMode:
        """"""
    @property
    def Value(self) -> T:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ThreadStaticAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
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

class ThrowHelper(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TimeSpan(ValueType, IComparable, IComparable[TimeSpan], IEquatable[TimeSpan], IFormattable):
    """"""

    MaxValue: ClassVar[TimeSpan]
    """"""
    MinValue: ClassVar[TimeSpan]
    """"""
    TicksPerDay: ClassVar[int]
    """"""
    TicksPerHour: ClassVar[int]
    """"""
    TicksPerMillisecond: ClassVar[int]
    """"""
    TicksPerMinute: ClassVar[int]
    """"""
    TicksPerSecond: ClassVar[int]
    """"""
    Zero: ClassVar[TimeSpan]
    """"""
    @overload
    def __init__(self, ticks: int) -> None:
        """"""
    @overload
    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        """"""
    @overload
    def __init__(self, days: int, hours: int, minutes: int, seconds: int) -> None:
        """"""
    @overload
    def __init__(
        self, days: int, hours: int, minutes: int, seconds: int, milliseconds: int
    ) -> None:
        """"""
    @property
    def Days(self) -> int:
        """"""
    @property
    def Hours(self) -> int:
        """"""
    @property
    def Milliseconds(self) -> int:
        """"""
    @property
    def Minutes(self) -> int:
        """"""
    @property
    def Seconds(self) -> int:
        """"""
    @property
    def Ticks(self) -> int:
        """"""
    @property
    def TotalDays(self) -> float:
        """"""
    @property
    def TotalHours(self) -> float:
        """"""
    @property
    def TotalMilliseconds(self) -> float:
        """"""
    @property
    def TotalMinutes(self) -> float:
        """"""
    @property
    def TotalSeconds(self) -> float:
        """"""
    def Add(self, ts: TimeSpan) -> TimeSpan:
        """"""
    @classmethod
    def Compare(cls, t1: TimeSpan, t2: TimeSpan) -> int:
        """"""
    @overload
    def CompareTo(self, value: object) -> int:
        """"""
    @overload
    def CompareTo(self, value: TimeSpan) -> int:
        """"""
    def Duration(self) -> TimeSpan:
        """"""
    @overload
    def Equals(self, value: object) -> bool:
        """"""
    @overload
    def Equals(self, obj: TimeSpan) -> bool:
        """"""
    @classmethod
    @overload
    def Equals(cls, t1: TimeSpan, t2: TimeSpan) -> bool:
        """"""
    @classmethod
    def FromDays(cls, value: float) -> TimeSpan:
        """"""
    @classmethod
    def FromHours(cls, value: float) -> TimeSpan:
        """"""
    @classmethod
    def FromMilliseconds(cls, value: float) -> TimeSpan:
        """"""
    @classmethod
    def FromMinutes(cls, value: float) -> TimeSpan:
        """"""
    @classmethod
    def FromSeconds(cls, value: float) -> TimeSpan:
        """"""
    @classmethod
    def FromTicks(cls, value: int) -> TimeSpan:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def Negate(self) -> TimeSpan:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str) -> TimeSpan:
        """"""
    @classmethod
    @overload
    def Parse(cls, input: str, formatProvider: IFormatProvider) -> TimeSpan:
        """"""
    @classmethod
    @overload
    def ParseExact(
        cls, input: str, formats: Array[str], formatProvider: IFormatProvider
    ) -> TimeSpan:
        """"""
    @classmethod
    @overload
    def ParseExact(
        cls,
        input: str,
        formats: Array[str],
        formatProvider: IFormatProvider,
        styles: TimeSpanStyles,
    ) -> TimeSpan:
        """"""
    @classmethod
    @overload
    def ParseExact(cls, input: str, format: str, formatProvider: IFormatProvider) -> TimeSpan:
        """"""
    @classmethod
    @overload
    def ParseExact(
        cls, input: str, format: str, formatProvider: IFormatProvider, styles: TimeSpanStyles
    ) -> TimeSpan:
        """"""
    def Subtract(self, ts: TimeSpan) -> TimeSpan:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, format: str) -> str:
        """"""
    @overload
    def ToString(self, format: str, formatProvider: IFormatProvider) -> str:
        """"""
    @classmethod
    @overload
    def TryParse(cls, s: str, result: TimeSpan) -> tuple[bool, TimeSpan]:
        """"""
    @classmethod
    @overload
    def TryParse(
        cls, input: str, formatProvider: IFormatProvider, result: TimeSpan
    ) -> tuple[bool, TimeSpan]:
        """"""
    @classmethod
    @overload
    def TryParseExact(
        cls,
        input: str,
        formats: Array[str],
        formatProvider: IFormatProvider,
        styles: TimeSpanStyles,
        result: TimeSpan,
    ) -> tuple[bool, TimeSpan]:
        """"""
    @classmethod
    @overload
    def TryParseExact(
        cls, input: str, formats: Array[str], formatProvider: IFormatProvider, result: TimeSpan
    ) -> tuple[bool, TimeSpan]:
        """"""
    @classmethod
    @overload
    def TryParseExact(
        cls,
        input: str,
        format: str,
        formatProvider: IFormatProvider,
        styles: TimeSpanStyles,
        result: TimeSpan,
    ) -> tuple[bool, TimeSpan]:
        """"""
    @classmethod
    @overload
    def TryParseExact(
        cls, input: str, format: str, formatProvider: IFormatProvider, result: TimeSpan
    ) -> tuple[bool, TimeSpan]:
        """"""
    @classmethod
    def op_Addition(cls, t1: TimeSpan, t2: TimeSpan) -> TimeSpan:
        """"""
    @classmethod
    def op_Equality(cls, t1: TimeSpan, t2: TimeSpan) -> bool:
        """"""
    @classmethod
    def op_GreaterThan(cls, t1: TimeSpan, t2: TimeSpan) -> bool:
        """"""
    @classmethod
    def op_GreaterThanOrEqual(cls, t1: TimeSpan, t2: TimeSpan) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, t1: TimeSpan, t2: TimeSpan) -> bool:
        """"""
    @classmethod
    def op_LessThan(cls, t1: TimeSpan, t2: TimeSpan) -> bool:
        """"""
    @classmethod
    def op_LessThanOrEqual(cls, t1: TimeSpan, t2: TimeSpan) -> bool:
        """"""
    @classmethod
    def op_Subtraction(cls, t1: TimeSpan, t2: TimeSpan) -> TimeSpan:
        """"""
    @classmethod
    def op_UnaryNegation(cls, t: TimeSpan) -> TimeSpan:
        """"""
    @classmethod
    def op_UnaryPlus(cls, t: TimeSpan) -> TimeSpan:
        """"""
    def __add__(self, other: TimeSpan) -> TimeSpan:
        """"""
    def __eq__(self, other: TimeSpan) -> bool:
        """"""
    def __gt__(self, other: TimeSpan) -> bool:
        """"""
    def __ge__(self, other: TimeSpan) -> bool:
        """"""
    def __ne__(self, other: TimeSpan) -> bool:
        """"""
    def __lt__(self, other: TimeSpan) -> bool:
        """"""
    def __le__(self, other: TimeSpan) -> bool:
        """"""
    def __sub__(self, other: TimeSpan) -> TimeSpan:
        """"""
    def __neg__(self) -> TimeSpan:
        """"""
    def __pos__(self) -> TimeSpan:
        """"""

class TimeZone(ABC, Object):
    """"""
    @classmethod
    @property
    def CurrentTimeZone(cls) -> TimeZone:
        """"""
    @property
    def DaylightName(self) -> str:
        """"""
    @property
    def StandardName(self) -> str:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetDaylightChanges(self, year: int) -> DaylightTime:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetUtcOffset(self, time: DateTime) -> TimeSpan:
        """"""
    @overload
    def IsDaylightSavingTime(self, time: DateTime) -> bool:
        """"""
    @classmethod
    @overload
    def IsDaylightSavingTime(cls, time: DateTime, daylightTimes: DaylightTime) -> bool:
        """"""
    def ToLocalTime(self, time: DateTime) -> DateTime:
        """"""
    def ToString(self) -> str:
        """"""
    def ToUniversalTime(self, time: DateTime) -> DateTime:
        """"""

class TimeZoneInfo(Object, IDeserializationCallback, ISerializable, IEquatable[TimeZoneInfo]):
    """"""
    @property
    def BaseUtcOffset(self) -> TimeSpan:
        """"""
    @property
    def DaylightName(self) -> str:
        """"""
    @property
    def DisplayName(self) -> str:
        """"""
    @property
    def Id(self) -> str:
        """"""
    @classmethod
    @property
    def Local(cls) -> TimeZoneInfo:
        """"""
    @property
    def StandardName(self) -> str:
        """"""
    @property
    def SupportsDaylightSavingTime(self) -> bool:
        """"""
    @classmethod
    @property
    def Utc(cls) -> TimeZoneInfo:
        """"""
    @classmethod
    def ClearCachedData(cls) -> None:
        """"""
    @classmethod
    @overload
    def ConvertTime(cls, dateTime: DateTime, destinationTimeZone: TimeZoneInfo) -> DateTime:
        """"""
    @classmethod
    @overload
    def ConvertTime(
        cls, dateTime: DateTime, sourceTimeZone: TimeZoneInfo, destinationTimeZone: TimeZoneInfo
    ) -> DateTime:
        """"""
    @classmethod
    @overload
    def ConvertTime(
        cls, dateTimeOffset: DateTimeOffset, destinationTimeZone: TimeZoneInfo
    ) -> DateTimeOffset:
        """"""
    @classmethod
    @overload
    def ConvertTimeBySystemTimeZoneId(
        cls, dateTime: DateTime, destinationTimeZoneId: str
    ) -> DateTime:
        """"""
    @classmethod
    @overload
    def ConvertTimeBySystemTimeZoneId(
        cls, dateTime: DateTime, sourceTimeZoneId: str, destinationTimeZoneId: str
    ) -> DateTime:
        """"""
    @classmethod
    @overload
    def ConvertTimeBySystemTimeZoneId(
        cls, dateTimeOffset: DateTimeOffset, destinationTimeZoneId: str
    ) -> DateTimeOffset:
        """"""
    @classmethod
    def ConvertTimeFromUtc(cls, dateTime: DateTime, destinationTimeZone: TimeZoneInfo) -> DateTime:
        """"""
    @classmethod
    @overload
    def ConvertTimeToUtc(cls, dateTime: DateTime) -> DateTime:
        """"""
    @classmethod
    @overload
    def ConvertTimeToUtc(cls, dateTime: DateTime, sourceTimeZone: TimeZoneInfo) -> DateTime:
        """"""
    @classmethod
    @overload
    def CreateCustomTimeZone(
        cls, id: str, baseUtcOffset: TimeSpan, displayName: str, standardDisplayName: str
    ) -> TimeZoneInfo:
        """"""
    @classmethod
    @overload
    def CreateCustomTimeZone(
        cls,
        id: str,
        baseUtcOffset: TimeSpan,
        displayName: str,
        standardDisplayName: str,
        daylightDisplayName: str,
        adjustmentRules: Array[AdjustmentRule],
    ) -> TimeZoneInfo:
        """"""
    @classmethod
    @overload
    def CreateCustomTimeZone(
        cls,
        id: str,
        baseUtcOffset: TimeSpan,
        displayName: str,
        standardDisplayName: str,
        daylightDisplayName: str,
        adjustmentRules: Array[AdjustmentRule],
        disableDaylightSavingTime: bool,
    ) -> TimeZoneInfo:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: TimeZoneInfo) -> bool:
        """"""
    @classmethod
    def FindSystemTimeZoneById(cls, id: str) -> TimeZoneInfo:
        """"""
    @classmethod
    def FromSerializedString(cls, source: str) -> TimeZoneInfo:
        """"""
    def GetAdjustmentRules(self) -> Array[AdjustmentRule]:
        """"""
    @overload
    def GetAmbiguousTimeOffsets(self, dateTime: DateTime) -> Array[TimeSpan]:
        """"""
    @overload
    def GetAmbiguousTimeOffsets(self, dateTimeOffset: DateTimeOffset) -> Array[TimeSpan]:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    @classmethod
    def GetSystemTimeZones(cls) -> ReadOnlyCollection[TimeZoneInfo]:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def GetUtcOffset(self, dateTime: DateTime) -> TimeSpan:
        """"""
    @overload
    def GetUtcOffset(self, dateTimeOffset: DateTimeOffset) -> TimeSpan:
        """"""
    def HasSameRules(self, other: TimeZoneInfo) -> bool:
        """"""
    @overload
    def IsAmbiguousTime(self, dateTime: DateTime) -> bool:
        """"""
    @overload
    def IsAmbiguousTime(self, dateTimeOffset: DateTimeOffset) -> bool:
        """"""
    @overload
    def IsDaylightSavingTime(self, dateTime: DateTime) -> bool:
        """"""
    @overload
    def IsDaylightSavingTime(self, dateTimeOffset: DateTimeOffset) -> bool:
        """"""
    def IsInvalidTime(self, dateTime: DateTime) -> bool:
        """"""
    def OnDeserialization(self, sender: object) -> None:
        """"""
    def ToSerializedString(self) -> str:
        """"""
    def ToString(self) -> str:
        """"""
    class AdjustmentRule(
        Object, IDeserializationCallback, ISerializable, IEquatable[TimeZoneInfo.AdjustmentRule]
    ):
        """"""
        @property
        def DateEnd(self) -> DateTime:
            """"""
        @property
        def DateStart(self) -> DateTime:
            """"""
        @property
        def DaylightDelta(self) -> TimeSpan:
            """"""
        @property
        def DaylightTransitionEnd(self) -> TimeZoneInfo.TransitionTime:
            """"""
        @property
        def DaylightTransitionStart(self) -> TimeZoneInfo.TransitionTime:
            """"""
        @classmethod
        def CreateAdjustmentRule(
            cls,
            dateStart: DateTime,
            dateEnd: DateTime,
            daylightDelta: TimeSpan,
            daylightTransitionStart: TimeZoneInfo.TransitionTime,
            daylightTransitionEnd: TimeZoneInfo.TransitionTime,
        ) -> TimeZoneInfo.AdjustmentRule:
            """"""
        @overload
        def Equals(self, obj: object) -> bool:
            """"""
        @overload
        def Equals(self, other: TimeZoneInfo.AdjustmentRule) -> bool:
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

    class TransitionTime(
        ValueType, IDeserializationCallback, ISerializable, IEquatable[TimeZoneInfo.TransitionTime]
    ):
        """"""
        @property
        def Day(self) -> int:
            """"""
        @property
        def DayOfWeek(self) -> DayOfWeek:
            """"""
        @property
        def IsFixedDateRule(self) -> bool:
            """"""
        @property
        def Month(self) -> int:
            """"""
        @property
        def TimeOfDay(self) -> DateTime:
            """"""
        @property
        def Week(self) -> int:
            """"""
        @classmethod
        def CreateFixedDateRule(
            cls, timeOfDay: DateTime, month: int, day: int
        ) -> TimeZoneInfo.TransitionTime:
            """"""
        @classmethod
        def CreateFloatingDateRule(
            cls, timeOfDay: DateTime, month: int, week: int, dayOfWeek: DayOfWeek
        ) -> TimeZoneInfo.TransitionTime:
            """"""
        @overload
        def Equals(self, obj: object) -> bool:
            """"""
        @overload
        def Equals(self, other: TimeZoneInfo.TransitionTime) -> bool:
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
        @classmethod
        def op_Equality(
            cls, t1: TimeZoneInfo.TransitionTime, t2: TimeZoneInfo.TransitionTime
        ) -> bool:
            """"""
        @classmethod
        def op_Inequality(
            cls, t1: TimeZoneInfo.TransitionTime, t2: TimeZoneInfo.TransitionTime
        ) -> bool:
            """"""
        def __eq__(self, other: TimeZoneInfo.TransitionTime) -> bool:
            """"""
        def __ne__(self, other: TimeZoneInfo.TransitionTime) -> bool:
            """"""

class TimeZoneInfoOptions(Enum):
    """"""

    _None: TimeZoneInfoOptions = ...
    """"""
    NoThrowOnInvalidTime: TimeZoneInfoOptions = ...
    """"""

class TimeZoneNotFoundException(Exception, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
        """"""
    @overload
    def __init__(self) -> None:
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

class TimeoutException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
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

class TokenType(Enum):
    """"""

    NumberToken: TokenType = ...
    """"""
    YearNumberToken: TokenType = ...
    """"""
    Am: TokenType = ...
    """"""
    Pm: TokenType = ...
    """"""
    MonthToken: TokenType = ...
    """"""
    EndOfString: TokenType = ...
    """"""
    DayOfWeekToken: TokenType = ...
    """"""
    TimeZoneToken: TokenType = ...
    """"""
    EraToken: TokenType = ...
    """"""
    DateWordToken: TokenType = ...
    """"""
    UnknownToken: TokenType = ...
    """"""
    HebrewNumber: TokenType = ...
    """"""
    JapaneseEraToken: TokenType = ...
    """"""
    TEraToken: TokenType = ...
    """"""
    IgnorableSymbol: TokenType = ...
    """"""
    RegularTokenMask: TokenType = ...
    """"""
    SEP_Unk: TokenType = ...
    """"""
    SEP_End: TokenType = ...
    """"""
    SEP_Space: TokenType = ...
    """"""
    SEP_Am: TokenType = ...
    """"""
    SEP_Pm: TokenType = ...
    """"""
    SEP_Date: TokenType = ...
    """"""
    SEP_Time: TokenType = ...
    """"""
    SEP_YearSuff: TokenType = ...
    """"""
    SEP_MonthSuff: TokenType = ...
    """"""
    SEP_DaySuff: TokenType = ...
    """"""
    SEP_HourSuff: TokenType = ...
    """"""
    SEP_MinuteSuff: TokenType = ...
    """"""
    SEP_SecondSuff: TokenType = ...
    """"""
    SEP_LocalTimeMark: TokenType = ...
    """"""
    SEP_DateOrOffset: TokenType = ...
    """"""
    SeparatorTokenMask: TokenType = ...
    """"""

class Tuple(ABC, Object):
    """"""
    @classmethod
    @overload
    def Create[T1](cls, item1: T1) -> Tuple[T1]:
        """"""
    @classmethod
    @overload
    def Create[T1, T2](cls, item1: T1, item2: T2) -> Tuple[T1, T2]:
        """"""
    @classmethod
    @overload
    def Create[T1, T2, T3](cls, item1: T1, item2: T2, item3: T3) -> Tuple[T1, T2, T3]:
        """"""
    @classmethod
    @overload
    def Create[T1, T2, T3, T4](
        cls, item1: T1, item2: T2, item3: T3, item4: T4
    ) -> Tuple[T1, T2, T3, T4]:
        """"""
    @classmethod
    @overload
    def Create[T1, T2, T3, T4, T5](
        cls, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5
    ) -> Tuple[T1, T2, T3, T4, T5]:
        """"""
    @classmethod
    @overload
    def Create[T1, T2, T3, T4, T5, T6](
        cls, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6
    ) -> Tuple[T1, T2, T3, T4, T5, T6]:
        """"""
    @classmethod
    @overload
    def Create[T1, T2, T3, T4, T5, T6, T7](
        cls, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7
    ) -> Tuple[T1, T2, T3, T4, T5, T6, T7]:
        """"""
    @classmethod
    @overload
    def Create[T1, T2, T3, T4, T5, T6, T7, T8](
        cls, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7, item8: T8
    ) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8]]:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TupleExtensions(ABC, Object):
    """"""
    @classmethod
    @overload
    def Deconstruct(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13, T14, Tuple[T15]],
        item1: T1,
        item2: T2,
        item3: T3,
        item4: T4,
        item5: T5,
        item6: T6,
        item7: T7,
        item8: T8,
        item9: T9,
        item10: T10,
        item11: T11,
        item12: T12,
        item13: T13,
        item14: T14,
        item15: T15,
        item16: T16,
        item17: T17,
        item18: T18,
        item19: T19,
        item20: T20,
        item21: T21,
    ) -> tuple[
        None,
        T1,
        T2,
        T3,
        T4,
        T5,
        T6,
        T7,
        T8,
        T9,
        T10,
        T11,
        T12,
        T13,
        T14,
        T15,
        T16,
        T17,
        T18,
        T19,
        T20,
        T21,
    ]:
        """"""
    @classmethod
    @overload
    def Deconstruct(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13, T14, Tuple[T15]],
        item1: T1,
        item2: T2,
        item3: T3,
        item4: T4,
        item5: T5,
        item6: T6,
        item7: T7,
        item8: T8,
        item9: T9,
        item10: T10,
        item11: T11,
        item12: T12,
        item13: T13,
        item14: T14,
        item15: T15,
        item16: T16,
        item17: T17,
        item18: T18,
        item19: T19,
        item20: T20,
    ) -> tuple[
        None,
        T1,
        T2,
        T3,
        T4,
        T5,
        T6,
        T7,
        T8,
        T9,
        T10,
        T11,
        T12,
        T13,
        T14,
        T15,
        T16,
        T17,
        T18,
        T19,
        T20,
    ]:
        """"""
    @classmethod
    @overload
    def Deconstruct(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13, T14, Tuple[T15]],
        item1: T1,
        item2: T2,
        item3: T3,
        item4: T4,
        item5: T5,
        item6: T6,
        item7: T7,
        item8: T8,
        item9: T9,
        item10: T10,
        item11: T11,
        item12: T12,
        item13: T13,
        item14: T14,
        item15: T15,
        item16: T16,
        item17: T17,
        item18: T18,
        item19: T19,
    ) -> tuple[
        None, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19
    ]:
        """"""
    @classmethod
    @overload
    def Deconstruct(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13, T14, Tuple[T15]],
        item1: T1,
        item2: T2,
        item3: T3,
        item4: T4,
        item5: T5,
        item6: T6,
        item7: T7,
        item8: T8,
        item9: T9,
        item10: T10,
        item11: T11,
        item12: T12,
        item13: T13,
        item14: T14,
        item15: T15,
        item16: T16,
        item17: T17,
        item18: T18,
    ) -> tuple[
        None, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18
    ]:
        """"""
    @classmethod
    @overload
    def Deconstruct(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13, T14, Tuple[T15]],
        item1: T1,
        item2: T2,
        item3: T3,
        item4: T4,
        item5: T5,
        item6: T6,
        item7: T7,
        item8: T8,
        item9: T9,
        item10: T10,
        item11: T11,
        item12: T12,
        item13: T13,
        item14: T14,
        item15: T15,
        item16: T16,
        item17: T17,
    ) -> tuple[None, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17]:
        """"""
    @classmethod
    @overload
    def Deconstruct(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13, T14, Tuple[T15]],
        item1: T1,
        item2: T2,
        item3: T3,
        item4: T4,
        item5: T5,
        item6: T6,
        item7: T7,
        item8: T8,
        item9: T9,
        item10: T10,
        item11: T11,
        item12: T12,
        item13: T13,
        item14: T14,
        item15: T15,
        item16: T16,
    ) -> tuple[None, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16]:
        """"""
    @classmethod
    @overload
    def Deconstruct(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13, T14, Tuple[T15]],
        item1: T1,
        item2: T2,
        item3: T3,
        item4: T4,
        item5: T5,
        item6: T6,
        item7: T7,
        item8: T8,
        item9: T9,
        item10: T10,
        item11: T11,
        item12: T12,
        item13: T13,
        item14: T14,
        item15: T15,
    ) -> tuple[None, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15]:
        """"""
    @classmethod
    @overload
    def Deconstruct(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14]],
        item1: T1,
        item2: T2,
        item3: T3,
        item4: T4,
        item5: T5,
        item6: T6,
        item7: T7,
        item8: T8,
        item9: T9,
        item10: T10,
        item11: T11,
        item12: T12,
        item13: T13,
        item14: T14,
    ) -> tuple[None, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14]:
        """"""
    @classmethod
    @overload
    def Deconstruct(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13]],
        item1: T1,
        item2: T2,
        item3: T3,
        item4: T4,
        item5: T5,
        item6: T6,
        item7: T7,
        item8: T8,
        item9: T9,
        item10: T10,
        item11: T11,
        item12: T12,
        item13: T13,
    ) -> tuple[None, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13]:
        """"""
    @classmethod
    @overload
    def Deconstruct(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12]],
        item1: T1,
        item2: T2,
        item3: T3,
        item4: T4,
        item5: T5,
        item6: T6,
        item7: T7,
        item8: T8,
        item9: T9,
        item10: T10,
        item11: T11,
        item12: T12,
    ) -> tuple[None, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12]:
        """"""
    @classmethod
    @overload
    def Deconstruct(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11]],
        item1: T1,
        item2: T2,
        item3: T3,
        item4: T4,
        item5: T5,
        item6: T6,
        item7: T7,
        item8: T8,
        item9: T9,
        item10: T10,
        item11: T11,
    ) -> tuple[None, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11]:
        """"""
    @classmethod
    @overload
    def Deconstruct(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10]],
        item1: T1,
        item2: T2,
        item3: T3,
        item4: T4,
        item5: T5,
        item6: T6,
        item7: T7,
        item8: T8,
        item9: T9,
        item10: T10,
    ) -> tuple[None, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10]:
        """"""
    @classmethod
    @overload
    def Deconstruct(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9]],
        item1: T1,
        item2: T2,
        item3: T3,
        item4: T4,
        item5: T5,
        item6: T6,
        item7: T7,
        item8: T8,
        item9: T9,
    ) -> tuple[None, T1, T2, T3, T4, T5, T6, T7, T8, T9]:
        """"""
    @classmethod
    @overload
    def Deconstruct(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8]],
        item1: T1,
        item2: T2,
        item3: T3,
        item4: T4,
        item5: T5,
        item6: T6,
        item7: T7,
        item8: T8,
    ) -> tuple[None, T1, T2, T3, T4, T5, T6, T7, T8]:
        """"""
    @classmethod
    @overload
    def Deconstruct(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7],
        item1: T1,
        item2: T2,
        item3: T3,
        item4: T4,
        item5: T5,
        item6: T6,
        item7: T7,
    ) -> tuple[None, T1, T2, T3, T4, T5, T6, T7]:
        """"""
    @classmethod
    @overload
    def Deconstruct(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6],
        item1: T1,
        item2: T2,
        item3: T3,
        item4: T4,
        item5: T5,
        item6: T6,
    ) -> tuple[None, T1, T2, T3, T4, T5, T6]:
        """"""
    @classmethod
    @overload
    def Deconstruct(
        cls, value: Tuple[T1, T2, T3, T4, T5], item1: T1, item2: T2, item3: T3, item4: T4, item5: T5
    ) -> tuple[None, T1, T2, T3, T4, T5]:
        """"""
    @classmethod
    @overload
    def Deconstruct(
        cls, value: Tuple[T1, T2, T3, T4], item1: T1, item2: T2, item3: T3, item4: T4
    ) -> tuple[None, T1, T2, T3, T4]:
        """"""
    @classmethod
    @overload
    def Deconstruct(
        cls, value: Tuple[T1, T2, T3], item1: T1, item2: T2, item3: T3
    ) -> tuple[None, T1, T2, T3]:
        """"""
    @classmethod
    @overload
    def Deconstruct(cls, value: Tuple[T1, T2], item1: T1, item2: T2) -> tuple[None, T1, T2]:
        """"""
    @classmethod
    @overload
    def Deconstruct(cls, value: Tuple[T1], item1: T1) -> tuple[None, T1]:
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
    @overload
    def ToTuple(
        cls,
        value: ValueTuple[
            T1, T2, T3, T4, T5, T6, T7, ValueTuple, T9, T10, T11, T12, T13, T14, ValueTuple[T15]
        ],
    ) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13, T14, Tuple[T15]]:
        """"""
    @classmethod
    @overload
    def ToTuple(
        cls,
        value: ValueTuple[
            T1, T2, T3, T4, T5, T6, T7, ValueTuple, T9, T10, T11, T12, T13, T14, ValueTuple[T15]
        ],
    ) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13, T14, Tuple[T15]]:
        """"""
    @classmethod
    @overload
    def ToTuple(
        cls,
        value: ValueTuple[
            T1, T2, T3, T4, T5, T6, T7, ValueTuple, T9, T10, T11, T12, T13, T14, ValueTuple[T15]
        ],
    ) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13, T14, Tuple[T15]]:
        """"""
    @classmethod
    @overload
    def ToTuple(
        cls,
        value: ValueTuple[
            T1, T2, T3, T4, T5, T6, T7, ValueTuple, T9, T10, T11, T12, T13, T14, ValueTuple[T15]
        ],
    ) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13, T14, Tuple[T15]]:
        """"""
    @classmethod
    @overload
    def ToTuple(
        cls,
        value: ValueTuple[
            T1, T2, T3, T4, T5, T6, T7, ValueTuple, T9, T10, T11, T12, T13, T14, ValueTuple[T15]
        ],
    ) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13, T14, Tuple[T15]]:
        """"""
    @classmethod
    @overload
    def ToTuple(
        cls,
        value: ValueTuple[
            T1, T2, T3, T4, T5, T6, T7, ValueTuple, T9, T10, T11, T12, T13, T14, ValueTuple[T15]
        ],
    ) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13, T14, Tuple[T15]]:
        """"""
    @classmethod
    @overload
    def ToTuple(
        cls,
        value: ValueTuple[
            T1, T2, T3, T4, T5, T6, T7, ValueTuple, T9, T10, T11, T12, T13, T14, ValueTuple[T15]
        ],
    ) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13, T14, Tuple[T15]]:
        """"""
    @classmethod
    @overload
    def ToTuple(
        cls,
        value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14]],
    ) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14]]:
        """"""
    @classmethod
    @overload
    def ToTuple(
        cls, value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13]]
    ) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13]]:
        """"""
    @classmethod
    @overload
    def ToTuple(
        cls, value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12]]
    ) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12]]:
        """"""
    @classmethod
    @overload
    def ToTuple(
        cls, value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11]]
    ) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11]]:
        """"""
    @classmethod
    @overload
    def ToTuple(
        cls, value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10]]
    ) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10]]:
        """"""
    @classmethod
    @overload
    def ToTuple(
        cls, value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9]]
    ) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9]]:
        """"""
    @classmethod
    @overload
    def ToTuple(
        cls, value: ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8]]
    ) -> Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8]]:
        """"""
    @classmethod
    @overload
    def ToTuple(
        cls, value: ValueTuple[T1, T2, T3, T4, T5, T6, T7]
    ) -> Tuple[T1, T2, T3, T4, T5, T6, T7]:
        """"""
    @classmethod
    @overload
    def ToTuple(cls, value: ValueTuple[T1, T2, T3, T4, T5, T6]) -> Tuple[T1, T2, T3, T4, T5, T6]:
        """"""
    @classmethod
    @overload
    def ToTuple(cls, value: ValueTuple[T1, T2, T3, T4, T5]) -> Tuple[T1, T2, T3, T4, T5]:
        """"""
    @classmethod
    @overload
    def ToTuple(cls, value: ValueTuple[T1, T2, T3, T4]) -> Tuple[T1, T2, T3, T4]:
        """"""
    @classmethod
    @overload
    def ToTuple(cls, value: ValueTuple[T1, T2, T3]) -> Tuple[T1, T2, T3]:
        """"""
    @classmethod
    @overload
    def ToTuple(cls, value: ValueTuple[T1, T2]) -> Tuple[T1, T2]:
        """"""
    @classmethod
    @overload
    def ToTuple(cls, value: ValueTuple[T1]) -> Tuple[T1]:
        """"""
    @classmethod
    @overload
    def ToValueTuple(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13, T14, Tuple[T15]],
    ) -> ValueTuple[
        T1, T2, T3, T4, T5, T6, T7, ValueTuple, T9, T10, T11, T12, T13, T14, ValueTuple[T15]
    ]:
        """"""
    @classmethod
    @overload
    def ToValueTuple(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13, T14, Tuple[T15]],
    ) -> ValueTuple[
        T1, T2, T3, T4, T5, T6, T7, ValueTuple, T9, T10, T11, T12, T13, T14, ValueTuple[T15]
    ]:
        """"""
    @classmethod
    @overload
    def ToValueTuple(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13, T14, Tuple[T15]],
    ) -> ValueTuple[
        T1, T2, T3, T4, T5, T6, T7, ValueTuple, T9, T10, T11, T12, T13, T14, ValueTuple[T15]
    ]:
        """"""
    @classmethod
    @overload
    def ToValueTuple(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13, T14, Tuple[T15]],
    ) -> ValueTuple[
        T1, T2, T3, T4, T5, T6, T7, ValueTuple, T9, T10, T11, T12, T13, T14, ValueTuple[T15]
    ]:
        """"""
    @classmethod
    @overload
    def ToValueTuple(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13, T14, Tuple[T15]],
    ) -> ValueTuple[
        T1, T2, T3, T4, T5, T6, T7, ValueTuple, T9, T10, T11, T12, T13, T14, ValueTuple[T15]
    ]:
        """"""
    @classmethod
    @overload
    def ToValueTuple(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13, T14, Tuple[T15]],
    ) -> ValueTuple[
        T1, T2, T3, T4, T5, T6, T7, ValueTuple, T9, T10, T11, T12, T13, T14, ValueTuple[T15]
    ]:
        """"""
    @classmethod
    @overload
    def ToValueTuple(
        cls,
        value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple, T9, T10, T11, T12, T13, T14, Tuple[T15]],
    ) -> ValueTuple[
        T1, T2, T3, T4, T5, T6, T7, ValueTuple, T9, T10, T11, T12, T13, T14, ValueTuple[T15]
    ]:
        """"""
    @classmethod
    @overload
    def ToValueTuple(
        cls, value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13, T14]]
    ) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13, T14]]:
        """"""
    @classmethod
    @overload
    def ToValueTuple(
        cls, value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12, T13]]
    ) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12, T13]]:
        """"""
    @classmethod
    @overload
    def ToValueTuple(
        cls, value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11, T12]]
    ) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11, T12]]:
        """"""
    @classmethod
    @overload
    def ToValueTuple(
        cls, value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10, T11]]
    ) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10, T11]]:
        """"""
    @classmethod
    @overload
    def ToValueTuple(
        cls, value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9, T10]]
    ) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9, T10]]:
        """"""
    @classmethod
    @overload
    def ToValueTuple(
        cls, value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8, T9]]
    ) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8, T9]]:
        """"""
    @classmethod
    @overload
    def ToValueTuple(
        cls, value: Tuple[T1, T2, T3, T4, T5, T6, T7, Tuple[T8]]
    ) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8]]:
        """"""
    @classmethod
    @overload
    def ToValueTuple(
        cls, value: Tuple[T1, T2, T3, T4, T5, T6, T7]
    ) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7]:
        """"""
    @classmethod
    @overload
    def ToValueTuple(
        cls, value: Tuple[T1, T2, T3, T4, T5, T6]
    ) -> ValueTuple[T1, T2, T3, T4, T5, T6]:
        """"""
    @classmethod
    @overload
    def ToValueTuple(cls, value: Tuple[T1, T2, T3, T4, T5]) -> ValueTuple[T1, T2, T3, T4, T5]:
        """"""
    @classmethod
    @overload
    def ToValueTuple(cls, value: Tuple[T1, T2, T3, T4]) -> ValueTuple[T1, T2, T3, T4]:
        """"""
    @classmethod
    @overload
    def ToValueTuple(cls, value: Tuple[T1, T2, T3]) -> ValueTuple[T1, T2, T3]:
        """"""
    @classmethod
    @overload
    def ToValueTuple(cls, value: Tuple[T1, T2]) -> ValueTuple[T1, T2]:
        """"""
    @classmethod
    @overload
    def ToValueTuple(cls, value: Tuple[T1]) -> ValueTuple[T1]:
        """"""

class Tuple[T1, T2, T3, T4, T5, T6, T7, TRest](
    Object, IStructuralComparable, IStructuralEquatable, ITuple, IComparable, ITupleInternal
):
    """"""
    def __init__(
        self,
        item1: T1,
        item2: T2,
        item3: T3,
        item4: T4,
        item5: T5,
        item6: T6,
        item7: T7,
        rest: TRest,
    ) -> None:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @property
    def Item1(self) -> T1:
        """"""
    @property
    def Item2(self) -> T2:
        """"""
    @property
    def Item3(self) -> T3:
        """"""
    @property
    def Item4(self) -> T4:
        """"""
    @property
    def Item5(self) -> T5:
        """"""
    @property
    def Item6(self) -> T6:
        """"""
    @property
    def Item7(self) -> T7:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @property
    def Rest(self) -> TRest:
        """"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """"""
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, sb: StringBuilder) -> str:
        """"""
    def __getitem__(self, index: int) -> object:
        """"""

class Tuple[T1, T2, T3, T4, T5, T6, T7](
    Object, IStructuralComparable, IStructuralEquatable, ITuple, IComparable, ITupleInternal
):
    """"""
    def __init__(
        self, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7
    ) -> None:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @property
    def Item1(self) -> T1:
        """"""
    @property
    def Item2(self) -> T2:
        """"""
    @property
    def Item3(self) -> T3:
        """"""
    @property
    def Item4(self) -> T4:
        """"""
    @property
    def Item5(self) -> T5:
        """"""
    @property
    def Item6(self) -> T6:
        """"""
    @property
    def Item7(self) -> T7:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """"""
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, sb: StringBuilder) -> str:
        """"""
    def __getitem__(self, index: int) -> object:
        """"""

class Tuple[T1, T2, T3, T4, T5, T6](
    Object, IStructuralComparable, IStructuralEquatable, ITuple, IComparable, ITupleInternal
):
    """"""
    def __init__(self, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6) -> None:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @property
    def Item1(self) -> T1:
        """"""
    @property
    def Item2(self) -> T2:
        """"""
    @property
    def Item3(self) -> T3:
        """"""
    @property
    def Item4(self) -> T4:
        """"""
    @property
    def Item5(self) -> T5:
        """"""
    @property
    def Item6(self) -> T6:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """"""
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, sb: StringBuilder) -> str:
        """"""
    def __getitem__(self, index: int) -> object:
        """"""

class Tuple[T1, T2, T3, T4, T5](
    Object, IStructuralComparable, IStructuralEquatable, ITuple, IComparable, ITupleInternal
):
    """"""
    def __init__(self, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5) -> None:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @property
    def Item1(self) -> T1:
        """"""
    @property
    def Item2(self) -> T2:
        """"""
    @property
    def Item3(self) -> T3:
        """"""
    @property
    def Item4(self) -> T4:
        """"""
    @property
    def Item5(self) -> T5:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """"""
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, sb: StringBuilder) -> str:
        """"""
    def __getitem__(self, index: int) -> object:
        """"""

class Tuple[T1, T2, T3, T4](
    Object, IStructuralComparable, IStructuralEquatable, ITuple, IComparable, ITupleInternal
):
    """"""
    def __init__(self, item1: T1, item2: T2, item3: T3, item4: T4) -> None:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @property
    def Item1(self) -> T1:
        """"""
    @property
    def Item2(self) -> T2:
        """"""
    @property
    def Item3(self) -> T3:
        """"""
    @property
    def Item4(self) -> T4:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """"""
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, sb: StringBuilder) -> str:
        """"""
    def __getitem__(self, index: int) -> object:
        """"""

class Tuple[T1, T2, T3](
    Object, IStructuralComparable, IStructuralEquatable, ITuple, IComparable, ITupleInternal
):
    """"""
    def __init__(self, item1: T1, item2: T2, item3: T3) -> None:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @property
    def Item1(self) -> T1:
        """"""
    @property
    def Item2(self) -> T2:
        """"""
    @property
    def Item3(self) -> T3:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """"""
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, sb: StringBuilder) -> str:
        """"""
    def __getitem__(self, index: int) -> object:
        """"""

class Tuple[T1, T2](
    Object, IStructuralComparable, IStructuralEquatable, ITuple, IComparable, ITupleInternal
):
    """"""
    def __init__(self, item1: T1, item2: T2) -> None:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @property
    def Item1(self) -> T1:
        """"""
    @property
    def Item2(self) -> T2:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """"""
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, sb: StringBuilder) -> str:
        """"""
    def __getitem__(self, index: int) -> object:
        """"""

class Tuple[T1](
    Object, IStructuralComparable, IStructuralEquatable, ITuple, IComparable, ITupleInternal
):
    """"""
    def __init__(self, item1: T1) -> None:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @property
    def Item1(self) -> T1:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """"""
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, sb: StringBuilder) -> str:
        """"""
    def __getitem__(self, index: int) -> object:
        """"""

class Type(ABC, MemberInfo, ICustomAttributeProvider, IReflect, _MemberInfo, _Type):
    """"""

    Delimiter: ClassVar[Char]
    """"""
    EmptyTypes: ClassVar[Array[Type]]
    """"""
    FilterAttribute: ClassVar[MemberFilter]
    """"""
    FilterName: ClassVar[MemberFilter]
    """"""
    FilterNameIgnoreCase: ClassVar[MemberFilter]
    """"""
    Missing: ClassVar[object]
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
    def DeclaringMethod(self) -> MethodBase:
        """"""
    @property
    def DeclaringType(self) -> Type:
        """"""
    @classmethod
    @property
    def DefaultBinder(cls) -> Binder:
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
    def HasElementType(self) -> bool:
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
    @overload
    def GetType(self) -> Type:
        """"""
    @classmethod
    @overload
    def GetType(cls, typeName: str) -> Type:
        """"""
    @classmethod
    @overload
    def GetType(cls, typeName: str, throwOnError: bool) -> Type:
        """"""
    @classmethod
    @overload
    def GetType(cls, typeName: str, throwOnError: bool, ignoreCase: bool) -> Type:
        """"""
    @classmethod
    @overload
    def GetType(
        cls,
        typeName: str,
        assemblyResolver: Func[AssemblyName, Assembly],
        typeResolver: Func[Assembly, str, bool, Type],
    ) -> Type:
        """"""
    @classmethod
    @overload
    def GetType(
        cls,
        typeName: str,
        assemblyResolver: Func[AssemblyName, Assembly],
        typeResolver: Func[Assembly, str, bool, Type],
        throwOnError: bool,
    ) -> Type:
        """"""
    @classmethod
    @overload
    def GetType(
        cls,
        typeName: str,
        assemblyResolver: Func[AssemblyName, Assembly],
        typeResolver: Func[Assembly, str, bool, Type],
        throwOnError: bool,
        ignoreCase: bool,
    ) -> Type:
        """"""
    @classmethod
    def GetTypeArray(cls, args: Array[object]) -> Array[Type]:
        """"""
    @classmethod
    def GetTypeCode(cls, type: Type) -> TypeCode:
        """"""
    @classmethod
    @overload
    def GetTypeFromCLSID(cls, clsid: Guid) -> Type:
        """"""
    @classmethod
    @overload
    def GetTypeFromCLSID(cls, clsid: Guid, throwOnError: bool) -> Type:
        """"""
    @classmethod
    @overload
    def GetTypeFromCLSID(cls, clsid: Guid, server: str) -> Type:
        """"""
    @classmethod
    @overload
    def GetTypeFromCLSID(cls, clsid: Guid, server: str, throwOnError: bool) -> Type:
        """"""
    @classmethod
    def GetTypeFromHandle(cls, handle: RuntimeTypeHandle) -> Type:
        """"""
    @classmethod
    @overload
    def GetTypeFromProgID(cls, progID: str) -> Type:
        """"""
    @classmethod
    @overload
    def GetTypeFromProgID(cls, progID: str, throwOnError: bool) -> Type:
        """"""
    @classmethod
    @overload
    def GetTypeFromProgID(cls, progID: str, server: str) -> Type:
        """"""
    @classmethod
    @overload
    def GetTypeFromProgID(cls, progID: str, server: str, throwOnError: bool) -> Type:
        """"""
    @classmethod
    def GetTypeHandle(cls, o: object) -> RuntimeTypeHandle:
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
    @classmethod
    def ReflectionOnlyGetType(cls, typeName: str, throwIfNotFound: bool, ignoreCase: bool) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    def op_Equality(cls, left: Type, right: Type) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, left: Type, right: Type) -> bool:
        """"""
    def __eq__(self, other: Type) -> bool:
        """"""
    def __ne__(self, other: Type) -> bool:
        """"""

class TypeAccessException(TypeLoadException, _Exception, ISerializable):
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
    @property
    def TypeName(self) -> str:
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

class TypeCode(Enum):
    """"""

    Empty: TypeCode = ...
    """"""
    Object: TypeCode = ...
    """"""
    DBNull: TypeCode = ...
    """"""
    Boolean: TypeCode = ...
    """"""
    Char: TypeCode = ...
    """"""
    SByte: TypeCode = ...
    """"""
    Byte: TypeCode = ...
    """"""
    Int16: TypeCode = ...
    """"""
    UInt16: TypeCode = ...
    """"""
    Int32: TypeCode = ...
    """"""
    UInt32: TypeCode = ...
    """"""
    Int64: TypeCode = ...
    """"""
    UInt64: TypeCode = ...
    """"""
    Single: TypeCode = ...
    """"""
    Double: TypeCode = ...
    """"""
    Decimal: TypeCode = ...
    """"""
    DateTime: TypeCode = ...
    """"""
    String: TypeCode = ...
    """"""

class TypeInitializationException(SystemException, _Exception, ISerializable):
    """"""
    def __init__(self, fullTypeName: str, innerException: Exception) -> None:
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
    @property
    def TypeName(self) -> str:
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

class TypeLoadException(SystemException, _Exception, ISerializable):
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
    @property
    def TypeName(self) -> str:
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

class TypeNameFormatFlags(Enum):
    """"""

    FormatBasic: TypeNameFormatFlags = ...
    """"""
    FormatNamespace: TypeNameFormatFlags = ...
    """"""
    FormatFullInst: TypeNameFormatFlags = ...
    """"""
    FormatAssembly: TypeNameFormatFlags = ...
    """"""
    FormatSignature: TypeNameFormatFlags = ...
    """"""
    FormatNoVersion: TypeNameFormatFlags = ...
    """"""
    FormatAngleBrackets: TypeNameFormatFlags = ...
    """"""
    FormatStubInfo: TypeNameFormatFlags = ...
    """"""
    FormatGenericParam: TypeNameFormatFlags = ...
    """"""
    FormatSerialization: TypeNameFormatFlags = ...
    """"""

class TypeNameKind(Enum):
    """"""

    Name: TypeNameKind = ...
    """"""
    ToString: TypeNameKind = ...
    """"""
    SerializationName: TypeNameKind = ...
    """"""
    FullName: TypeNameKind = ...
    """"""

class TypeNameParser(Object, IDisposable):
    """"""
    def Dispose(self) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class TypeUnloadedException(SystemException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, message: str) -> None:
        """"""
    @overload
    def __init__(self, message: str, innerException: Exception) -> None:
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

class TypedReference(ValueType):
    """"""
    def Equals(self, o: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @classmethod
    def GetTargetType(cls, value: TypedReference) -> Type:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def MakeTypedReference(cls, target: object, flds: Array[FieldInfo]) -> TypedReference:
        """"""
    @classmethod
    def SetTypedReference(cls, target: TypedReference, value: object) -> None:
        """"""
    @classmethod
    def TargetTypeToken(cls, value: TypedReference) -> RuntimeTypeHandle:
        """"""
    @classmethod
    def ToObject(cls, value: TypedReference) -> object:
        """"""
    def ToString(self) -> str:
        """"""

class UInt16(
    ValueType, IComparable, IComparable[UInt16], IConvertible, IEquatable[UInt16], IFormattable
):
    """"""

    MaxValue: ClassVar[int]
    """"""
    MinValue: ClassVar[int]
    """"""
    @overload
    def CompareTo(self, value: object) -> int:
        """"""
    @overload
    def CompareTo(self, value: int) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, obj: int) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeCode(self) -> TypeCode:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str) -> int:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles) -> int:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, provider: IFormatProvider) -> int:
        """"""
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """"""
    def ToByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToChar(self, provider: IFormatProvider) -> Char:
        """"""
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """"""
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """"""
    def ToDouble(self, provider: IFormatProvider) -> float:
        """"""
    def ToInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt64(self, provider: IFormatProvider) -> int:
        """"""
    def ToSByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToSingle(self, provider: IFormatProvider) -> float:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """"""
    @overload
    def ToString(self, format: str) -> str:
        """"""
    @overload
    def ToString(self, format: str, provider: IFormatProvider) -> str:
        """"""
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """"""
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def TryParse(
        cls, s: str, style: NumberStyles, provider: IFormatProvider, result: UInt16
    ) -> tuple[bool, UInt16]:
        """"""
    @classmethod
    @overload
    def TryParse(cls, s: str, result: UInt16) -> tuple[bool, UInt16]:
        """"""

class UInt32(
    ValueType, IComparable, IComparable[UInt32], IConvertible, IEquatable[UInt32], IFormattable
):
    """"""

    MaxValue: ClassVar[int]
    """"""
    MinValue: ClassVar[int]
    """"""
    @overload
    def CompareTo(self, value: object) -> int:
        """"""
    @overload
    def CompareTo(self, value: int) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, obj: int) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeCode(self) -> TypeCode:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str) -> int:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles) -> int:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, provider: IFormatProvider) -> int:
        """"""
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """"""
    def ToByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToChar(self, provider: IFormatProvider) -> Char:
        """"""
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """"""
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """"""
    def ToDouble(self, provider: IFormatProvider) -> float:
        """"""
    def ToInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt64(self, provider: IFormatProvider) -> int:
        """"""
    def ToSByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToSingle(self, provider: IFormatProvider) -> float:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """"""
    @overload
    def ToString(self, format: str) -> str:
        """"""
    @overload
    def ToString(self, format: str, provider: IFormatProvider) -> str:
        """"""
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """"""
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def TryParse(
        cls, s: str, style: NumberStyles, provider: IFormatProvider, result: UInt32
    ) -> tuple[bool, UInt32]:
        """"""
    @classmethod
    @overload
    def TryParse(cls, s: str, result: UInt32) -> tuple[bool, UInt32]:
        """"""

class UInt64(
    ValueType, IComparable, IComparable[UInt64], IConvertible, IEquatable[UInt64], IFormattable
):
    """"""

    MaxValue: ClassVar[int]
    """"""
    MinValue: ClassVar[int]
    """"""
    @overload
    def CompareTo(self, value: object) -> int:
        """"""
    @overload
    def CompareTo(self, value: int) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, obj: int) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeCode(self) -> TypeCode:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str) -> int:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles) -> int:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, style: NumberStyles, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def Parse(cls, s: str, provider: IFormatProvider) -> int:
        """"""
    def ToBoolean(self, provider: IFormatProvider) -> bool:
        """"""
    def ToByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToChar(self, provider: IFormatProvider) -> Char:
        """"""
    def ToDateTime(self, provider: IFormatProvider) -> DateTime:
        """"""
    def ToDecimal(self, provider: IFormatProvider) -> Decimal:
        """"""
    def ToDouble(self, provider: IFormatProvider) -> float:
        """"""
    def ToInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToInt64(self, provider: IFormatProvider) -> int:
        """"""
    def ToSByte(self, provider: IFormatProvider) -> int:
        """"""
    def ToSingle(self, provider: IFormatProvider) -> float:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, provider: IFormatProvider) -> str:
        """"""
    @overload
    def ToString(self, format: str) -> str:
        """"""
    @overload
    def ToString(self, format: str, provider: IFormatProvider) -> str:
        """"""
    def ToType(self, conversionType: Type, provider: IFormatProvider) -> object:
        """"""
    def ToUInt16(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt32(self, provider: IFormatProvider) -> int:
        """"""
    def ToUInt64(self, provider: IFormatProvider) -> int:
        """"""
    @classmethod
    @overload
    def TryParse(
        cls, s: str, style: NumberStyles, provider: IFormatProvider, result: UInt64
    ) -> tuple[bool, UInt64]:
        """"""
    @classmethod
    @overload
    def TryParse(cls, s: str, result: UInt64) -> tuple[bool, UInt64]:
        """"""

class UIntPtr(ValueType, ISerializable):
    """"""

    Zero: ClassVar[UIntPtr]
    """"""
    @overload
    def __init__(self, value: int) -> None:
        """"""
    @overload
    def __init__(self, value: int) -> None:
        """"""
    @overload
    def __init__(self, value: None) -> None:
        """"""
    @classmethod
    @property
    def Size(cls) -> int:
        """"""
    @classmethod
    def Add(cls, pointer: UIntPtr, offset: int) -> UIntPtr:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Subtract(cls, pointer: UIntPtr, offset: int) -> UIntPtr:
        """"""
    def ToPointer(self) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def ToUInt32(self) -> int:
        """"""
    def ToUInt64(self) -> int:
        """"""
    @classmethod
    def op_Addition(cls, pointer: UIntPtr, offset: int) -> UIntPtr:
        """"""
    @classmethod
    def op_Equality(cls, value1: UIntPtr, value2: UIntPtr) -> bool:
        """"""
    @classmethod
    @overload
    def op_Explicit(cls, value: int) -> UIntPtr:
        """"""
    @classmethod
    @overload
    def op_Explicit(cls, value: int) -> UIntPtr:
        """"""
    @classmethod
    @overload
    def op_Explicit(cls, value: UIntPtr) -> None:
        """"""
    @classmethod
    @overload
    def op_Explicit(cls, value: None) -> UIntPtr:
        """"""
    @classmethod
    def op_Inequality(cls, value1: UIntPtr, value2: UIntPtr) -> bool:
        """"""
    @classmethod
    def op_Subtraction(cls, pointer: UIntPtr, offset: int) -> UIntPtr:
        """"""
    def __add__(self, other: int) -> UIntPtr:
        """"""
    def __eq__(self, other: UIntPtr) -> bool:
        """"""
    def __ne__(self, other: UIntPtr) -> bool:
        """"""
    def __sub__(self, other: int) -> UIntPtr:
        """"""

class UnSafeCharBuffer(ValueType):
    """"""
    def __init__(self, buffer: Char, bufferSize: int) -> None:
        """"""
    @property
    def Length(self) -> int:
        """"""
    def AppendString(self, stringToAppend: str) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class UnauthorizedAccessException(SystemException, _Exception, ISerializable):
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

class UncNameHelper(Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class UnescapeMode(Enum):
    """"""

    CopyOnly: UnescapeMode = ...
    """"""
    Escape: UnescapeMode = ...
    """"""
    Unescape: UnescapeMode = ...
    """"""
    EscapeUnescape: UnescapeMode = ...
    """"""
    V1ToStringFlag: UnescapeMode = ...
    """"""
    UnescapeAll: UnescapeMode = ...
    """"""
    UnescapeAllOrThrow: UnescapeMode = ...
    """"""

class UnhandledExceptionEventArgs(EventArgs):
    """"""
    def __init__(self, exception: object, isTerminating: bool) -> None:
        """"""
    @property
    def ExceptionObject(self) -> object:
        """"""
    @property
    def IsTerminating(self) -> bool:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

UnhandledExceptionEventHandler: Callable[[object, UnhandledExceptionEventArgs], None] = ...
""""""

class UnitySerializationHolder(Object, IObjectReference, ISerializable):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetRealObject(self, context: StreamingContext) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Uri(Object, ISerializable):
    """"""

    SchemeDelimiter: ClassVar[str]
    """"""
    UriSchemeFile: ClassVar[str]
    """"""
    UriSchemeFtp: ClassVar[str]
    """"""
    UriSchemeGopher: ClassVar[str]
    """"""
    UriSchemeHttp: ClassVar[str]
    """"""
    UriSchemeHttps: ClassVar[str]
    """"""
    UriSchemeMailto: ClassVar[str]
    """"""
    UriSchemeNetPipe: ClassVar[str]
    """"""
    UriSchemeNetTcp: ClassVar[str]
    """"""
    UriSchemeNews: ClassVar[str]
    """"""
    UriSchemeNntp: ClassVar[str]
    """"""
    @overload
    def __init__(self, uriString: str) -> None:
        """"""
    @overload
    def __init__(self, uriString: str, dontEscape: bool) -> None:
        """"""
    @overload
    def __init__(self, baseUri: Uri, relativeUri: str, dontEscape: bool) -> None:
        """"""
    @overload
    def __init__(self, uriString: str, uriKind: UriKind) -> None:
        """"""
    @overload
    def __init__(self, baseUri: Uri, relativeUri: str) -> None:
        """"""
    @overload
    def __init__(self, baseUri: Uri, relativeUri: Uri) -> None:
        """"""
    @property
    def AbsolutePath(self) -> str:
        """"""
    @property
    def AbsoluteUri(self) -> str:
        """"""
    @property
    def Authority(self) -> str:
        """"""
    @property
    def DnsSafeHost(self) -> str:
        """"""
    @property
    def Fragment(self) -> str:
        """"""
    @property
    def Host(self) -> str:
        """"""
    @property
    def HostNameType(self) -> UriHostNameType:
        """"""
    @property
    def IdnHost(self) -> str:
        """"""
    @property
    def IsAbsoluteUri(self) -> bool:
        """"""
    @property
    def IsDefaultPort(self) -> bool:
        """"""
    @property
    def IsFile(self) -> bool:
        """"""
    @property
    def IsLoopback(self) -> bool:
        """"""
    @property
    def IsUnc(self) -> bool:
        """"""
    @property
    def LocalPath(self) -> str:
        """"""
    @property
    def OriginalString(self) -> str:
        """"""
    @property
    def PathAndQuery(self) -> str:
        """"""
    @property
    def Port(self) -> int:
        """"""
    @property
    def Query(self) -> str:
        """"""
    @property
    def Scheme(self) -> str:
        """"""
    @property
    def Segments(self) -> Array[str]:
        """"""
    @property
    def UserEscaped(self) -> bool:
        """"""
    @property
    def UserInfo(self) -> str:
        """"""
    @classmethod
    def CheckHostName(cls, name: str) -> UriHostNameType:
        """"""
    @classmethod
    def CheckSchemeName(cls, schemeName: str) -> bool:
        """"""
    @classmethod
    def Compare(
        cls,
        uri1: Uri,
        uri2: Uri,
        partsToCompare: UriComponents,
        compareFormat: UriFormat,
        comparisonType: StringComparison,
    ) -> int:
        """"""
    def Equals(self, comparand: object) -> bool:
        """"""
    @classmethod
    def EscapeDataString(cls, stringToEscape: str) -> str:
        """"""
    @classmethod
    def EscapeUriString(cls, stringToEscape: str) -> str:
        """"""
    @classmethod
    def FromHex(cls, digit: Char) -> int:
        """"""
    def GetComponents(self, components: UriComponents, format: UriFormat) -> str:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetLeftPart(self, part: UriPartial) -> str:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def HexEscape(cls, character: Char) -> str:
        """"""
    @classmethod
    def HexUnescape(cls, pattern: str, index: Int32) -> Char:
        """"""
    def IsBaseOf(self, uri: Uri) -> bool:
        """"""
    @classmethod
    def IsHexDigit(cls, character: Char) -> bool:
        """"""
    @classmethod
    def IsHexEncoding(cls, pattern: str, index: int) -> bool:
        """"""
    def IsWellFormedOriginalString(self) -> bool:
        """"""
    @classmethod
    def IsWellFormedUriString(cls, uriString: str, uriKind: UriKind) -> bool:
        """"""
    def MakeRelative(self, toUri: Uri) -> str:
        """"""
    def MakeRelativeUri(self, uri: Uri) -> Uri:
        """"""
    def ToString(self) -> str:
        """"""
    @classmethod
    @overload
    def TryCreate(cls, uriString: str, uriKind: UriKind, result: Uri) -> tuple[bool, Uri]:
        """"""
    @classmethod
    @overload
    def TryCreate(cls, baseUri: Uri, relativeUri: str, result: Uri) -> tuple[bool, Uri]:
        """"""
    @classmethod
    @overload
    def TryCreate(cls, baseUri: Uri, relativeUri: Uri, result: Uri) -> tuple[bool, Uri]:
        """"""
    @classmethod
    def UnescapeDataString(cls, stringToUnescape: str) -> str:
        """"""
    @classmethod
    def op_Equality(cls, uri1: Uri, uri2: Uri) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, uri1: Uri, uri2: Uri) -> bool:
        """"""
    def __eq__(self, other: Uri) -> bool:
        """"""
    def __ne__(self, other: Uri) -> bool:
        """"""

class UriBuilder(Object):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, uri: str) -> None:
        """"""
    @overload
    def __init__(self, uri: Uri) -> None:
        """"""
    @overload
    def __init__(self, schemeName: str, hostName: str) -> None:
        """"""
    @overload
    def __init__(self, scheme: str, host: str, portNumber: int) -> None:
        """"""
    @overload
    def __init__(self, scheme: str, host: str, port: int, pathValue: str) -> None:
        """"""
    @overload
    def __init__(self, scheme: str, host: str, port: int, path: str, extraValue: str) -> None:
        """"""
    @property
    def Fragment(self) -> str:
        """"""
    @Fragment.setter
    def Fragment(self, value: str) -> None: ...
    @property
    def Host(self) -> str:
        """"""
    @Host.setter
    def Host(self, value: str) -> None: ...
    @property
    def Password(self) -> str:
        """"""
    @Password.setter
    def Password(self, value: str) -> None: ...
    @property
    def Path(self) -> str:
        """"""
    @Path.setter
    def Path(self, value: str) -> None: ...
    @property
    def Port(self) -> int:
        """"""
    @Port.setter
    def Port(self, value: int) -> None: ...
    @property
    def Query(self) -> str:
        """"""
    @Query.setter
    def Query(self, value: str) -> None: ...
    @property
    def Scheme(self) -> str:
        """"""
    @Scheme.setter
    def Scheme(self, value: str) -> None: ...
    @property
    def Uri(self) -> Uri:
        """"""
    @property
    def UserName(self) -> str:
        """"""
    @UserName.setter
    def UserName(self, value: str) -> None: ...
    def Equals(self, rparam: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class UriComponents(Enum):
    """"""

    Scheme: UriComponents = ...
    """"""
    UserInfo: UriComponents = ...
    """"""
    Host: UriComponents = ...
    """"""
    Port: UriComponents = ...
    """"""
    SchemeAndServer: UriComponents = ...
    """"""
    Path: UriComponents = ...
    """"""
    Query: UriComponents = ...
    """"""
    PathAndQuery: UriComponents = ...
    """"""
    HttpRequestUrl: UriComponents = ...
    """"""
    Fragment: UriComponents = ...
    """"""
    AbsoluteUri: UriComponents = ...
    """"""
    StrongPort: UriComponents = ...
    """"""
    HostAndPort: UriComponents = ...
    """"""
    StrongAuthority: UriComponents = ...
    """"""
    NormalizedHost: UriComponents = ...
    """"""
    KeepDelimiter: UriComponents = ...
    """"""
    SerializationInfoString: UriComponents = ...
    """"""

class UriFormat(Enum):
    """"""

    UriEscaped: UriFormat = ...
    """"""
    Unescaped: UriFormat = ...
    """"""
    SafeUnescaped: UriFormat = ...
    """"""

class UriFormatException(FormatException, _Exception, ISerializable):
    """"""
    @overload
    def __init__(self) -> None:
        """"""
    @overload
    def __init__(self, textString: str) -> None:
        """"""
    @overload
    def __init__(self, textString: str, e: Exception) -> None:
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

class UriHelper(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class UriHostNameType(Enum):
    """"""

    Unknown: UriHostNameType = ...
    """"""
    Basic: UriHostNameType = ...
    """"""
    Dns: UriHostNameType = ...
    """"""
    IPv4: UriHostNameType = ...
    """"""
    IPv6: UriHostNameType = ...
    """"""

class UriIdnScope(Enum):
    """"""

    _None: UriIdnScope = ...
    """"""
    AllExceptIntranet: UriIdnScope = ...
    """"""
    All: UriIdnScope = ...
    """"""

class UriKind(Enum):
    """"""

    RelativeOrAbsolute: UriKind = ...
    """"""
    Absolute: UriKind = ...
    """"""
    Relative: UriKind = ...
    """"""

class UriParser(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def IsKnownScheme(cls, schemeName: str) -> bool:
        """"""
    @classmethod
    def Register(cls, uriParser: UriParser, schemeName: str, defaultPort: int) -> None:
        """"""
    def ToString(self) -> str:
        """"""

class UriPartial(Enum):
    """"""

    Scheme: UriPartial = ...
    """"""
    Authority: UriPartial = ...
    """"""
    Path: UriPartial = ...
    """"""
    Query: UriPartial = ...
    """"""

class UriSyntaxFlags(Enum):
    """"""

    _None: UriSyntaxFlags = ...
    """"""
    MustHaveAuthority: UriSyntaxFlags = ...
    """"""
    OptionalAuthority: UriSyntaxFlags = ...
    """"""
    MayHaveUserInfo: UriSyntaxFlags = ...
    """"""
    MayHavePort: UriSyntaxFlags = ...
    """"""
    MayHavePath: UriSyntaxFlags = ...
    """"""
    MayHaveQuery: UriSyntaxFlags = ...
    """"""
    MayHaveFragment: UriSyntaxFlags = ...
    """"""
    AllowEmptyHost: UriSyntaxFlags = ...
    """"""
    AllowUncHost: UriSyntaxFlags = ...
    """"""
    AllowDnsHost: UriSyntaxFlags = ...
    """"""
    AllowIPv4Host: UriSyntaxFlags = ...
    """"""
    AllowIPv6Host: UriSyntaxFlags = ...
    """"""
    AllowAnInternetHost: UriSyntaxFlags = ...
    """"""
    AllowAnyOtherHost: UriSyntaxFlags = ...
    """"""
    FileLikeUri: UriSyntaxFlags = ...
    """"""
    MailToLikeUri: UriSyntaxFlags = ...
    """"""
    V1_UnknownUri: UriSyntaxFlags = ...
    """"""
    SimpleUserSyntax: UriSyntaxFlags = ...
    """"""
    BuiltInSyntax: UriSyntaxFlags = ...
    """"""
    ParserSchemeOnly: UriSyntaxFlags = ...
    """"""
    AllowDOSPath: UriSyntaxFlags = ...
    """"""
    PathIsRooted: UriSyntaxFlags = ...
    """"""
    ConvertPathSlashes: UriSyntaxFlags = ...
    """"""
    CompressPath: UriSyntaxFlags = ...
    """"""
    CanonicalizeAsFilePath: UriSyntaxFlags = ...
    """"""
    UnEscapeDotsAndSlashes: UriSyntaxFlags = ...
    """"""
    AllowIdn: UriSyntaxFlags = ...
    """"""
    AllowIriParsing: UriSyntaxFlags = ...
    """"""

class UriTypeConverter(TypeConverter):
    """"""
    def __init__(self) -> None:
        """"""
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertFrom(self, sourceType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool:
        """"""
    @overload
    def CanConvertTo(self, destinationType: Type) -> bool:
        """"""
    @overload
    def ConvertFrom(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> object:
        """"""
    @overload
    def ConvertFrom(self, value: object) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromInvariantString(self, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, text: str
    ) -> object:
        """"""
    @overload
    def ConvertFromString(self, context: ITypeDescriptorContext, text: str) -> object:
        """"""
    @overload
    def ConvertFromString(self, text: str) -> object:
        """"""
    @overload
    def ConvertTo(
        self,
        context: ITypeDescriptorContext,
        culture: CultureInfo,
        value: object,
        destinationType: Type,
    ) -> object:
        """"""
    @overload
    def ConvertTo(self, value: object, destinationType: Type) -> object:
        """"""
    @overload
    def ConvertToInvariantString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToInvariantString(self, value: object) -> str:
        """"""
    @overload
    def ConvertToString(
        self, context: ITypeDescriptorContext, culture: CultureInfo, value: object
    ) -> str:
        """"""
    @overload
    def ConvertToString(self, context: ITypeDescriptorContext, value: object) -> str:
        """"""
    @overload
    def ConvertToString(self, value: object) -> str:
        """"""
    @overload
    def CreateInstance(self, propertyValues: IDictionary) -> object:
        """"""
    @overload
    def CreateInstance(
        self, context: ITypeDescriptorContext, propertyValues: IDictionary
    ) -> object:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self) -> bool:
        """"""
    @overload
    def GetCreateInstanceSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(
        self, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]
    ) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetProperties(self, value: object) -> PropertyDescriptorCollection:
        """"""
    @overload
    def GetPropertiesSupported(self) -> bool:
        """"""
    @overload
    def GetPropertiesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValues(self) -> ICollection:
        """"""
    @overload
    def GetStandardValues(
        self, context: ITypeDescriptorContext
    ) -> TypeConverter.StandardValuesCollection:
        """"""
    @overload
    def GetStandardValuesExclusive(self) -> bool:
        """"""
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self) -> bool:
        """"""
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool:
        """"""
    def GetType(self) -> Type:
        """"""
    @overload
    def IsValid(self, context: ITypeDescriptorContext, value: object) -> bool:
        """"""
    @overload
    def IsValid(self, value: object) -> bool:
        """"""
    def ToString(self) -> str:
        """"""
    class StandardValuesCollection(Object, ICollection, IEnumerable):
        """"""
        def __init__(self, values: ICollection) -> None:
            """"""
        @property
        def Count(self) -> int:
            """"""
        @property
        def IsSynchronized(self) -> bool:
            """"""
        @property
        def Item(self) -> object:
            """"""
        @property
        def SyncRoot(self) -> object:
            """"""
        def CopyTo(self, array: Array, index: int) -> None:
            """"""
        def Equals(self, obj: object) -> bool:
            """"""
        def GetEnumerator(self) -> IEnumerator:
            """"""
        def GetHashCode(self) -> int:
            """"""
        def GetType(self) -> Type:
            """"""
        def ToString(self) -> str:
            """"""
        def __iter__(self) -> Iterator:
            """"""
        def __len__(self) -> int:
            """"""
        def __getitem__(self, index: int) -> object:
            """"""

class Utf8String(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class ValueTuple(
    ValueType,
    IStructuralComparable,
    IStructuralEquatable,
    ITuple,
    IComparable,
    IComparable[ValueTuple],
    IEquatable[ValueTuple],
    IValueTupleInternal,
):
    """"""
    @property
    def Item(self) -> object:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """"""
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """"""
    @overload
    def CompareTo(self, other: ValueTuple) -> int:
        """"""
    @classmethod
    @overload
    def Create[T1](cls, item1: T1) -> ValueTuple[T1]:
        """"""
    @classmethod
    @overload
    def Create[T1, T2](cls, item1: T1, item2: T2) -> ValueTuple[T1, T2]:
        """"""
    @classmethod
    @overload
    def Create[T1, T2, T3](cls, item1: T1, item2: T2, item3: T3) -> ValueTuple[T1, T2, T3]:
        """"""
    @classmethod
    @overload
    def Create[T1, T2, T3, T4](
        cls, item1: T1, item2: T2, item3: T3, item4: T4
    ) -> ValueTuple[T1, T2, T3, T4]:
        """"""
    @classmethod
    @overload
    def Create[T1, T2, T3, T4, T5](
        cls, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5
    ) -> ValueTuple[T1, T2, T3, T4, T5]:
        """"""
    @classmethod
    @overload
    def Create[T1, T2, T3, T4, T5, T6](
        cls, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6
    ) -> ValueTuple[T1, T2, T3, T4, T5, T6]:
        """"""
    @classmethod
    @overload
    def Create[T1, T2, T3, T4, T5, T6, T7](
        cls, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7
    ) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7]:
        """"""
    @classmethod
    @overload
    def Create[T1, T2, T3, T4, T5, T6, T7, T8](
        cls, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7, item8: T8
    ) -> ValueTuple[T1, T2, T3, T4, T5, T6, T7, ValueTuple[T8]]:
        """"""
    @classmethod
    @overload
    def Create(cls) -> ValueTuple:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """"""
    @overload
    def Equals(self, other: ValueTuple) -> bool:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def ToStringEnd(self) -> str:
        """"""
    def __getitem__(self, index: int) -> object:
        """"""

class ValueTuple[T1, T2, T3, T4, T5, T6, T7, TRest](
    ValueType,
    IStructuralComparable,
    IStructuralEquatable,
    ITuple,
    IComparable,
    IComparable[ValueTuple[T1, T2, T3, T4, T5, T6, T7, TRest]],
    IEquatable[ValueTuple[T1, T2, T3, T4, T5, T6, T7, TRest]],
    IValueTupleInternal,
):
    """"""

    Item1: Final[T1]
    """"""
    Item2: Final[T2]
    """"""
    Item3: Final[T3]
    """"""
    Item4: Final[T4]
    """"""
    Item5: Final[T5]
    """"""
    Item6: Final[T6]
    """"""
    Item7: Final[T7]
    """"""
    Rest: Final[TRest]
    """"""
    def __init__(
        self,
        item1: T1,
        item2: T2,
        item3: T3,
        item4: T4,
        item5: T5,
        item6: T6,
        item7: T7,
        rest: TRest,
    ) -> None:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """"""
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """"""
    @overload
    def CompareTo(self, other: ValueTuple[T1, T2, T3, T4, T5, T6, T7, TRest]) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """"""
    @overload
    def Equals(self, other: ValueTuple[T1, T2, T3, T4, T5, T6, T7, TRest]) -> bool:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def ToStringEnd(self) -> str:
        """"""
    def __getitem__(self, index: int) -> object:
        """"""

class ValueTuple[T1, T2, T3, T4, T5, T6, T7](
    ValueType,
    IStructuralComparable,
    IStructuralEquatable,
    ITuple,
    IComparable,
    IComparable[ValueTuple[T1, T2, T3, T4, T5, T6, T7]],
    IEquatable[ValueTuple[T1, T2, T3, T4, T5, T6, T7]],
    IValueTupleInternal,
):
    """"""

    Item1: Final[T1]
    """"""
    Item2: Final[T2]
    """"""
    Item3: Final[T3]
    """"""
    Item4: Final[T4]
    """"""
    Item5: Final[T5]
    """"""
    Item6: Final[T6]
    """"""
    Item7: Final[T7]
    """"""
    def __init__(
        self, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6, item7: T7
    ) -> None:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """"""
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """"""
    @overload
    def CompareTo(self, other: ValueTuple[T1, T2, T3, T4, T5, T6, T7]) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """"""
    @overload
    def Equals(self, other: ValueTuple[T1, T2, T3, T4, T5, T6, T7]) -> bool:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def ToStringEnd(self) -> str:
        """"""
    def __getitem__(self, index: int) -> object:
        """"""

class ValueTuple[T1, T2, T3, T4, T5, T6](
    ValueType,
    IStructuralComparable,
    IStructuralEquatable,
    ITuple,
    IComparable,
    IComparable[ValueTuple[T1, T2, T3, T4, T5, T6]],
    IEquatable[ValueTuple[T1, T2, T3, T4, T5, T6]],
    IValueTupleInternal,
):
    """"""

    Item1: Final[T1]
    """"""
    Item2: Final[T2]
    """"""
    Item3: Final[T3]
    """"""
    Item4: Final[T4]
    """"""
    Item5: Final[T5]
    """"""
    Item6: Final[T6]
    """"""
    def __init__(self, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5, item6: T6) -> None:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """"""
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """"""
    @overload
    def CompareTo(self, other: ValueTuple[T1, T2, T3, T4, T5, T6]) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """"""
    @overload
    def Equals(self, other: ValueTuple[T1, T2, T3, T4, T5, T6]) -> bool:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def ToStringEnd(self) -> str:
        """"""
    def __getitem__(self, index: int) -> object:
        """"""

class ValueTuple[T1, T2, T3, T4, T5](
    ValueType,
    IStructuralComparable,
    IStructuralEquatable,
    ITuple,
    IComparable,
    IComparable[ValueTuple[T1, T2, T3, T4, T5]],
    IEquatable[ValueTuple[T1, T2, T3, T4, T5]],
    IValueTupleInternal,
):
    """"""

    Item1: Final[T1]
    """"""
    Item2: Final[T2]
    """"""
    Item3: Final[T3]
    """"""
    Item4: Final[T4]
    """"""
    Item5: Final[T5]
    """"""
    def __init__(self, item1: T1, item2: T2, item3: T3, item4: T4, item5: T5) -> None:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """"""
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """"""
    @overload
    def CompareTo(self, other: ValueTuple[T1, T2, T3, T4, T5]) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """"""
    @overload
    def Equals(self, other: ValueTuple[T1, T2, T3, T4, T5]) -> bool:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def ToStringEnd(self) -> str:
        """"""
    def __getitem__(self, index: int) -> object:
        """"""

class ValueTuple[T1, T2, T3, T4](
    ValueType,
    IStructuralComparable,
    IStructuralEquatable,
    ITuple,
    IComparable,
    IComparable[ValueTuple[T1, T2, T3, T4]],
    IEquatable[ValueTuple[T1, T2, T3, T4]],
    IValueTupleInternal,
):
    """"""

    Item1: Final[T1]
    """"""
    Item2: Final[T2]
    """"""
    Item3: Final[T3]
    """"""
    Item4: Final[T4]
    """"""
    def __init__(self, item1: T1, item2: T2, item3: T3, item4: T4) -> None:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """"""
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """"""
    @overload
    def CompareTo(self, other: ValueTuple[T1, T2, T3, T4]) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """"""
    @overload
    def Equals(self, other: ValueTuple[T1, T2, T3, T4]) -> bool:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def ToStringEnd(self) -> str:
        """"""
    def __getitem__(self, index: int) -> object:
        """"""

class ValueTuple[T1, T2, T3](
    ValueType,
    IStructuralComparable,
    IStructuralEquatable,
    ITuple,
    IComparable,
    IComparable[ValueTuple[T1, T2, T3]],
    IEquatable[ValueTuple[T1, T2, T3]],
    IValueTupleInternal,
):
    """"""

    Item1: Final[T1]
    """"""
    Item2: Final[T2]
    """"""
    Item3: Final[T3]
    """"""
    def __init__(self, item1: T1, item2: T2, item3: T3) -> None:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """"""
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """"""
    @overload
    def CompareTo(self, other: ValueTuple[T1, T2, T3]) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """"""
    @overload
    def Equals(self, other: ValueTuple[T1, T2, T3]) -> bool:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def ToStringEnd(self) -> str:
        """"""
    def __getitem__(self, index: int) -> object:
        """"""

class ValueTuple[T1, T2](
    ValueType,
    IStructuralComparable,
    IStructuralEquatable,
    ITuple,
    IComparable,
    IComparable[ValueTuple[T1, T2]],
    IEquatable[ValueTuple[T1, T2]],
    IValueTupleInternal,
):
    """"""

    Item1: Final[T1]
    """"""
    Item2: Final[T2]
    """"""
    def __init__(self, item1: T1, item2: T2) -> None:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """"""
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """"""
    @overload
    def CompareTo(self, other: ValueTuple[T1, T2]) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """"""
    @overload
    def Equals(self, other: ValueTuple[T1, T2]) -> bool:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def ToStringEnd(self) -> str:
        """"""
    def __getitem__(self, index: int) -> object:
        """"""

class ValueTuple[T1](
    ValueType,
    IStructuralComparable,
    IStructuralEquatable,
    ITuple,
    IComparable,
    IComparable[ValueTuple[T1]],
    IEquatable[ValueTuple[T1]],
    IValueTupleInternal,
):
    """"""

    Item1: Final[T1]
    """"""
    def __init__(self, item1: T1) -> None:
        """"""
    @property
    def Item(self) -> object:
        """"""
    @property
    def Length(self) -> int:
        """"""
    @overload
    def CompareTo(self, obj: object) -> int:
        """"""
    @overload
    def CompareTo(self, other: object, comparer: IComparer) -> int:
        """"""
    @overload
    def CompareTo(self, other: ValueTuple[T1]) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, other: object, comparer: IEqualityComparer) -> bool:
        """"""
    @overload
    def Equals(self, other: ValueTuple[T1]) -> bool:
        """"""
    @overload
    def GetHashCode(self) -> int:
        """"""
    @overload
    def GetHashCode(self, comparer: IEqualityComparer) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
    def ToStringEnd(self) -> str:
        """"""
    def __getitem__(self, index: int) -> object:
        """"""

class ValueType(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class Variant(ValueType):
    """"""
    @overload
    def __init__(self, val: bool) -> None:
        """"""
    @overload
    def __init__(self, val: int) -> None:
        """"""
    @overload
    def __init__(self, val: int) -> None:
        """"""
    @overload
    def __init__(self, val: int) -> None:
        """"""
    @overload
    def __init__(self, val: int) -> None:
        """"""
    @overload
    def __init__(self, val: Char) -> None:
        """"""
    @overload
    def __init__(self, val: int) -> None:
        """"""
    @overload
    def __init__(self, val: int) -> None:
        """"""
    @overload
    def __init__(self, val: int) -> None:
        """"""
    @overload
    def __init__(self, val: int) -> None:
        """"""
    @overload
    def __init__(self, val: float) -> None:
        """"""
    @overload
    def __init__(self, val: float) -> None:
        """"""
    @overload
    def __init__(self, val: DateTime) -> None:
        """"""
    @overload
    def __init__(self, val: Decimal) -> None:
        """"""
    @overload
    def __init__(self, obj: object) -> None:
        """"""
    @overload
    def __init__(self, voidPointer: None, pointerType: Type) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToObject(self) -> object:
        """"""
    def ToString(self) -> str:
        """"""

class Version(Object, ICloneable, IComparable, IComparable[Version], IEquatable[Version]):
    """"""
    @overload
    def __init__(self, major: int, minor: int, build: int, revision: int) -> None:
        """"""
    @overload
    def __init__(self, major: int, minor: int, build: int) -> None:
        """"""
    @overload
    def __init__(self, major: int, minor: int) -> None:
        """"""
    @overload
    def __init__(self, version: str) -> None:
        """"""
    @overload
    def __init__(self) -> None:
        """"""
    @property
    def Build(self) -> int:
        """"""
    @property
    def Major(self) -> int:
        """"""
    @property
    def MajorRevision(self) -> int:
        """"""
    @property
    def Minor(self) -> int:
        """"""
    @property
    def MinorRevision(self) -> int:
        """"""
    @property
    def Revision(self) -> int:
        """"""
    def Clone(self) -> object:
        """"""
    @overload
    def CompareTo(self, version: object) -> int:
        """"""
    @overload
    def CompareTo(self, value: Version) -> int:
        """"""
    @overload
    def Equals(self, obj: object) -> bool:
        """"""
    @overload
    def Equals(self, obj: Version) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    @classmethod
    def Parse(cls, input: str) -> Version:
        """"""
    @overload
    def ToString(self) -> str:
        """"""
    @overload
    def ToString(self, fieldCount: int) -> str:
        """"""
    @classmethod
    def TryParse(cls, input: str, result: Version) -> tuple[bool, Version]:
        """"""
    @classmethod
    def op_Equality(cls, v1: Version, v2: Version) -> bool:
        """"""
    @classmethod
    def op_GreaterThan(cls, v1: Version, v2: Version) -> bool:
        """"""
    @classmethod
    def op_GreaterThanOrEqual(cls, v1: Version, v2: Version) -> bool:
        """"""
    @classmethod
    def op_Inequality(cls, v1: Version, v2: Version) -> bool:
        """"""
    @classmethod
    def op_LessThan(cls, v1: Version, v2: Version) -> bool:
        """"""
    @classmethod
    def op_LessThanOrEqual(cls, v1: Version, v2: Version) -> bool:
        """"""
    def __eq__(self, other: Version) -> bool:
        """"""
    def __gt__(self, other: Version) -> bool:
        """"""
    def __ge__(self, other: Version) -> bool:
        """"""
    def __ne__(self, other: Version) -> bool:
        """"""
    def __lt__(self, other: Version) -> bool:
        """"""
    def __le__(self, other: Version) -> bool:
        """"""

class Void(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class WeakReference(Object, ISerializable):
    """"""
    @overload
    def __init__(self, target: object) -> None:
        """"""
    @overload
    def __init__(self, target: object, trackResurrection: bool) -> None:
        """"""
    @property
    def IsAlive(self) -> bool:
        """"""
    @property
    def Target(self) -> object:
        """"""
    @Target.setter
    def Target(self, value: object) -> None: ...
    @property
    def TrackResurrection(self) -> bool:
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

class WeakReference[T](Object, ISerializable):
    """"""
    @overload
    def __init__(self, target: T) -> None:
        """"""
    @overload
    def __init__(self, target: T, trackResurrection: bool) -> None:
        """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None:
        """"""
    def GetType(self) -> Type:
        """"""
    def SetTarget[T](self, target: T) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    def TryGetTarget(self, target: T) -> tuple[bool, T]:
        """"""

class XmlIgnoreMemberAttribute(Attribute, _Attribute):
    """"""
    def __init__(self) -> None:
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

class _AppDomain:
    """"""
    @property
    def BaseDirectory(self) -> str:
        """"""
    @property
    def DynamicDirectory(self) -> str:
        """"""
    @property
    def Evidence(self) -> Evidence:
        """"""
    @property
    def FriendlyName(self) -> str:
        """"""
    @property
    def RelativeSearchPath(self) -> str:
        """"""
    @property
    def ShadowCopyFiles(self) -> bool:
        """"""
    def AppendPrivatePath(self, path: str) -> None:
        """"""
    def ClearPrivatePath(self) -> None:
        """"""
    def ClearShadowCopyPath(self) -> None:
        """"""
    @overload
    def CreateInstance(self, assemblyName: str, typeName: str) -> ObjectHandle:
        """"""
    @overload
    def CreateInstance(
        self, assemblyName: str, typeName: str, activationAttributes: Array[object]
    ) -> ObjectHandle:
        """"""
    @overload
    def CreateInstance(
        self,
        assemblyName: str,
        typeName: str,
        ignoreCase: bool,
        bindingAttr: BindingFlags,
        binder: Binder,
        args: Array[object],
        culture: CultureInfo,
        activationAttributes: Array[object],
        securityAttributes: Evidence,
    ) -> ObjectHandle:
        """"""
    @overload
    def CreateInstanceFrom(self, assemblyFile: str, typeName: str) -> ObjectHandle:
        """"""
    @overload
    def CreateInstanceFrom(
        self, assemblyFile: str, typeName: str, activationAttributes: Array[object]
    ) -> ObjectHandle:
        """"""
    @overload
    def CreateInstanceFrom(
        self,
        assemblyFile: str,
        typeName: str,
        ignoreCase: bool,
        bindingAttr: BindingFlags,
        binder: Binder,
        args: Array[object],
        culture: CultureInfo,
        activationAttributes: Array[object],
        securityAttributes: Evidence,
    ) -> ObjectHandle:
        """"""
    @overload
    def DefineDynamicAssembly(
        self, name: AssemblyName, access: AssemblyBuilderAccess
    ) -> AssemblyBuilder:
        """"""
    @overload
    def DefineDynamicAssembly(
        self, name: AssemblyName, access: AssemblyBuilderAccess, evidence: Evidence
    ) -> AssemblyBuilder:
        """"""
    @overload
    def DefineDynamicAssembly(
        self,
        name: AssemblyName,
        access: AssemblyBuilderAccess,
        evidence: Evidence,
        requiredPermissions: PermissionSet,
        optionalPermissions: PermissionSet,
        refusedPermissions: PermissionSet,
    ) -> AssemblyBuilder:
        """"""
    @overload
    def DefineDynamicAssembly(
        self,
        name: AssemblyName,
        access: AssemblyBuilderAccess,
        requiredPermissions: PermissionSet,
        optionalPermissions: PermissionSet,
        refusedPermissions: PermissionSet,
    ) -> AssemblyBuilder:
        """"""
    @overload
    def DefineDynamicAssembly(
        self, name: AssemblyName, access: AssemblyBuilderAccess, dir: str
    ) -> AssemblyBuilder:
        """"""
    @overload
    def DefineDynamicAssembly(
        self, name: AssemblyName, access: AssemblyBuilderAccess, dir: str, evidence: Evidence
    ) -> AssemblyBuilder:
        """"""
    @overload
    def DefineDynamicAssembly(
        self,
        name: AssemblyName,
        access: AssemblyBuilderAccess,
        dir: str,
        evidence: Evidence,
        requiredPermissions: PermissionSet,
        optionalPermissions: PermissionSet,
        refusedPermissions: PermissionSet,
    ) -> AssemblyBuilder:
        """"""
    @overload
    def DefineDynamicAssembly(
        self,
        name: AssemblyName,
        access: AssemblyBuilderAccess,
        dir: str,
        evidence: Evidence,
        requiredPermissions: PermissionSet,
        optionalPermissions: PermissionSet,
        refusedPermissions: PermissionSet,
        isSynchronized: bool,
    ) -> AssemblyBuilder:
        """"""
    @overload
    def DefineDynamicAssembly(
        self,
        name: AssemblyName,
        access: AssemblyBuilderAccess,
        dir: str,
        requiredPermissions: PermissionSet,
        optionalPermissions: PermissionSet,
        refusedPermissions: PermissionSet,
    ) -> AssemblyBuilder:
        """"""
    def DoCallBack(self, theDelegate: CrossAppDomainDelegate) -> None:
        """"""
    def Equals(self, other: object) -> bool:
        """"""
    @overload
    def ExecuteAssembly(self, assemblyFile: str) -> int:
        """"""
    @overload
    def ExecuteAssembly(self, assemblyFile: str, assemblySecurity: Evidence) -> int:
        """"""
    @overload
    def ExecuteAssembly(
        self, assemblyFile: str, assemblySecurity: Evidence, args: Array[str]
    ) -> int:
        """"""
    def GetAssemblies(self) -> Array[Assembly]:
        """"""
    def GetData(self, name: str) -> object:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetIDsOfNames(
        self, riid: Guid, rgszNames: IntPtr, cNames: int, lcid: int, rgDispId: IntPtr
    ) -> None:
        """"""
    def GetLifetimeService(self) -> object:
        """"""
    def GetType(self) -> Type:
        """"""
    def GetTypeInfo(self, iTInfo: int, lcid: int, ppTInfo: IntPtr) -> None:
        """"""
    def GetTypeInfoCount(self, pcTInfo: UInt32) -> tuple[None, UInt32]:
        """"""
    def InitializeLifetimeService(self) -> object:
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
    def Load(self, assemblyRef: AssemblyName) -> Assembly:
        """"""
    @overload
    def Load(self, assemblyRef: AssemblyName, assemblySecurity: Evidence) -> Assembly:
        """"""
    @overload
    def Load(self, rawAssembly: Array[int]) -> Assembly:
        """"""
    @overload
    def Load(self, rawAssembly: Array[int], rawSymbolStore: Array[int]) -> Assembly:
        """"""
    @overload
    def Load(
        self, rawAssembly: Array[int], rawSymbolStore: Array[int], securityEvidence: Evidence
    ) -> Assembly:
        """"""
    @overload
    def Load(self, assemblyString: str) -> Assembly:
        """"""
    @overload
    def Load(self, assemblyString: str, assemblySecurity: Evidence) -> Assembly:
        """"""
    def SetAppDomainPolicy(self, domainPolicy: PolicyLevel) -> None:
        """"""
    def SetCachePath(self, s: str) -> None:
        """"""
    def SetData(self, name: str, data: object) -> None:
        """"""
    def SetPrincipalPolicy(self, policy: PrincipalPolicy) -> None:
        """"""
    def SetShadowCopyPath(self, s: str) -> None:
        """"""
    def SetThreadPrincipal(self, principal: IPrincipal) -> None:
        """"""
    def ToString(self) -> str:
        """"""
    AssemblyLoad: EventType[AssemblyLoadEventHandler] = ...
    """"""
    AssemblyResolve: EventType[ResolveEventHandler] = ...
    """"""
    DomainUnload: EventType[EventHandler] = ...
    """"""
    ProcessExit: EventType[EventHandler] = ...
    """"""
    ResourceResolve: EventType[ResolveEventHandler] = ...
    """"""
    TypeResolve: EventType[ResolveEventHandler] = ...
    """"""
    UnhandledException: EventType[UnhandledExceptionEventHandler] = ...
    """"""

class __Canon(Object):
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

class __ComObject(MarshalByRefObject):
    """"""
    def CreateObjRef(self, requestedType: Type) -> ObjRef:
        """"""
    def Equals(self, obj: object) -> bool:
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

class __DTString(ValueType):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""

class __Filters(Object):
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

class __HResults(ABC, Object):
    """"""
    def Equals(self, obj: object) -> bool:
        """"""
    def GetHashCode(self) -> int:
        """"""
    def GetType(self) -> Type:
        """"""
    def ToString(self) -> str:
        """"""
